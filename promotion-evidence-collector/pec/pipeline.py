"""Ingest, analyze and rebuild the evidence base.

Flow:
1. ``ingest`` hashes each file. An exact duplicate becomes a named copy of
   the existing document and never produces separate evidence.
2. ``analyze`` extracts text, runs the selected engine once per new document
   and stores candidate drafts against exact source passages.
3. ``rebuild`` merges candidates across all documents into evidence records,
   checks corroboration and contradictions, sets statuses and review flags,
   and reapplies earlier human decisions.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

from . import signals as sg
from .classifier import DocumentContext, Draft, get_engine
from .classifier import guardrails
from .db import Store, now
from .extract import (
    SUPPORTED_EXTENSIONS, containment, extract, jaccard, normalize_text, sha256_bytes, sketch,
    sketch_similarity,
)
from .framework import L3B_COMPONENTS, LEVEL_RANK, STATUS_RANK

NEAR_DUP_JACCARD = 0.8
NEAR_DUP_CONTAINMENT = 0.9
INSTITUTIONAL_GENRES = {"handbook", "policy", "minutes", "report", "letter", "evaluation", "certificate"}
WORK_GENRES = {"handbook", "policy", "report", "proposal", "course_material"}
# First-person passages count as self-description only in these genres.
SELF_FIRST_PERSON_GENRES = {"other", "letter"}
# A candidate's name near the top of these documents links the whole document
# to the candidate. In minutes, handbooks and policies the name must appear in
# the passage itself.
DOC_LINK_GENRES = {"certificate", "evaluation", "letter", "report", "proposal", "publication", "course_material", "application"}
STOPWORDS = set("""about above after again against among because before being below between both could during each
further having other their there these those through under until while which would should within without
students student teaching taught course courses university college roosevelt faculty staff years present
member members since level levels including include various number""".split())


# ---------------------------------------------------------------------------
# Ingest


def ingest(store: Store, filename: str, data: bytes) -> tuple[str, int]:
    """Store one file. Returns (outcome, document_id) where outcome is
    'new', 'duplicate' or 'unsupported'."""
    filename = Path(filename).name
    ext = Path(filename).suffix.lower()
    digest = sha256_bytes(data)
    existing = store.one("SELECT id FROM documents WHERE sha256 = ?", (digest,))
    if existing:
        with store.tx() as c:
            c.execute(
                "INSERT INTO document_copies(document_id, filename, uploaded_at) VALUES (?, ?, ?)",
                (existing["id"], filename, now()),
            )
        return "duplicate", existing["id"]
    stored = store.originals_dir / f"{digest}{ext}"
    stored.write_bytes(data)
    with store.tx() as c:
        cur = c.execute(
            "INSERT INTO documents(sha256, filename, ext, size, stored_path, uploaded_at) VALUES (?, ?, ?, ?, ?, ?)",
            (digest, filename, ext, len(data), str(stored), now()),
        )
        doc_id = cur.lastrowid
        c.execute(
            "INSERT INTO document_copies(document_id, filename, uploaded_at) VALUES (?, ?, ?)",
            (doc_id, filename, now()),
        )
    return ("new" if ext in SUPPORTED_EXTENSIONS else "unsupported"), doc_id


def ingest_folder(store: Store, folder: str | Path) -> Counter:
    outcomes: Counter = Counter()
    for path in sorted(Path(folder).rglob("*")):
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS and not path.name.startswith("~$"):
            outcome, _ = ingest(store, path.name, path.read_bytes())
            outcomes[outcome] += 1
    return outcomes


# ---------------------------------------------------------------------------
# Analyze


def _flat(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _passage_hash(text: str) -> str:
    return hashlib.sha1(normalize_text(text).encode()).hexdigest()[:16]


def _locate(draft: Draft, pages: list[str]) -> tuple[int, str] | None:
    """Find the draft's passage in the source pages. Returns (page_no, exact
    source text) or None when the passage is not in the document."""
    quote = _flat(draft.passage)
    if len(quote) < 8:
        return None
    order = list(range(len(pages)))
    if 1 <= draft.page_no <= len(pages):
        order.remove(draft.page_no - 1)
        order.insert(0, draft.page_no - 1)
    for i in order:
        if quote in _flat(pages[i]) or quote.lower() in _flat(pages[i]).lower():
            return i + 1, draft.passage.strip()
    return None


def _doc_date(text: str, metadata_date: str) -> tuple[str, str]:
    found = sg.first_full_date(text[:4000])
    if found:
        return found, "document text"
    if metadata_date:
        return metadata_date, "file metadata"
    return "", ""


def analyze_document(store: Store, doc_id: int, engine) -> None:
    doc = store.one("SELECT * FROM documents WHERE id = ?", (doc_id,))
    if doc["manual_text"]:
        pages = [r["text"] for r in store.q("SELECT text FROM pages WHERE document_id = ? ORDER BY page_no", (doc_id,))]
        status, detail = "ok", "Text entered manually after visual review."
        meta_author, meta_title, meta_date = doc["metadata_author"], doc["metadata_title"], ""
        page_label, paged = "section", 0
    else:
        data = Path(doc["stored_path"]).read_bytes()
        extracted = extract(doc["filename"], data)
        pages, status, detail = extracted.pages, extracted.status, extracted.status_detail
        meta_author, meta_title, meta_date = extracted.metadata_author, extracted.metadata_title, extracted.metadata_date
        page_label, paged = extracted.page_label, int(extracted.paged)
    full = "\n\n".join(pages)
    genre = sg.detect_genre(doc["filename"], full)
    doc_date, date_source = _doc_date(full, meta_date)

    with store.tx() as c:
        c.execute("DELETE FROM passages WHERE document_id = ?", (doc_id,))
        if not doc["manual_text"]:
            c.execute("DELETE FROM pages WHERE document_id = ?", (doc_id,))
            c.executemany(
                "INSERT INTO pages(document_id, page_no, text) VALUES (?, ?, ?)",
                [(doc_id, i, t) for i, t in enumerate(pages, start=1)],
            )
        c.execute(
            "UPDATE documents SET genre = ?, metadata_author = ?, metadata_title = ?, doc_date = ?, "
            "doc_date_source = ?, page_label = ?, paged = ?, page_count = ?, char_count = ?, text_status = ?, "
            "status_detail = ?, sketch = ?, analyzed = 1, engine = ? WHERE id = ?",
            (genre, meta_author, meta_title, doc_date, date_source, page_label, paged, len(pages), len(full),
             status, detail, json.dumps(sketch(full)), engine.name, doc_id),
        )

    if sum(ch.isalpha() for ch in full) < 20:
        return
    drafts = engine.extract(DocumentContext(doc["filename"], genre, pages, page_label))
    with store.tx() as c:
        seen: dict[tuple[int, str], int] = {}
        for draft in drafts:
            located = _locate(draft, pages)
            if located is None:
                continue  # untraceable: discard
            page_no, text = located
            key = (page_no, _passage_hash(text))
            if key not in seen:
                cur = c.execute(
                    "INSERT INTO passages(document_id, page_no, text, norm_hash) VALUES (?, ?, ?, ?)",
                    (doc_id, page_no, text, key[1]),
                )
                seen[key] = cur.lastrowid
            draft.page_no = page_no
            c.execute(
                "INSERT INTO candidates(passage_id, engine, draft) VALUES (?, ?, ?)",
                (seen[key], engine.name, json.dumps(draft.to_dict())),
            )


def detect_near_duplicates(store: Store, doc_ids: list[int]) -> int:
    docs = store.q("SELECT id, sketch, char_count FROM documents WHERE analyzed = 1 AND char_count > 200")
    sketches = {d["id"]: json.loads(d["sketch"] or "[]") for d in docs}
    found = 0
    targets = set(doc_ids)
    for a in docs:
        if a["id"] not in targets:
            continue
        for b in docs:
            if b["id"] == a["id"] or (b["id"] in targets and b["id"] < a["id"]):
                continue
            estimate = sketch_similarity(sketches[a["id"]], sketches[b["id"]])
            if estimate < 0.3:
                continue
            text_a = "\n".join(r["text"] for r in store.q("SELECT text FROM pages WHERE document_id = ?", (a["id"],)))
            text_b = "\n".join(r["text"] for r in store.q("SELECT text FROM pages WHERE document_id = ?", (b["id"],)))
            sim, cont = jaccard(text_a, text_b), containment(text_a, text_b)
            if sim >= NEAR_DUP_JACCARD or cont >= NEAR_DUP_CONTAINMENT:
                lo, hi = sorted((a["id"], b["id"]))
                with store.tx() as c:
                    c.execute(
                        "INSERT OR IGNORE INTO document_relations(doc_a, doc_b, relation, similarity) VALUES (?, ?, 'near_duplicate', ?)",
                        (lo, hi, round(max(sim, cont), 3)),
                    )
                found += 1
    return found


def analyze(store: Store, engine_name: str = "rules", progress: Callable[[int, int, str], None] | None = None) -> dict:
    engine = get_engine(engine_name)
    pending = store.q("SELECT id, filename FROM documents WHERE analyzed = 0 AND excluded = 0 ORDER BY id")
    errors = []
    for i, doc in enumerate(pending, start=1):
        if progress:
            progress(i, len(pending), doc["filename"])
        try:
            analyze_document(store, doc["id"], engine)
        except Exception as exc:
            errors.append(f"{doc['filename']}: {exc}")
            with store.tx() as c:
                c.execute(
                    "UPDATE documents SET analyzed = 1, text_status = 'needs_visual_review', status_detail = ? WHERE id = ?",
                    (f"Analysis failed: {exc}"[:300], doc["id"]),
                )
    detect_near_duplicates(store, [d["id"] for d in pending])
    stats = rebuild(store)
    stats["documents_analyzed"] = len(pending)
    stats["errors"] = errors
    return stats


# ---------------------------------------------------------------------------
# Rebuild


@dataclass
class Member:
    passage_id: int
    doc: dict
    page_no: int
    text: str
    norm_hash: str
    draft: Draft
    sig: sg.Signals
    self_desc: bool
    linked: bool
    metadata_link_only: bool
    group: int

    @property
    def l3a_ok(self) -> bool:
        return self.draft.level == "L3A" and self.sig.action and self.sig.scope and not self.sig.membership_only


@dataclass
class Item:
    fingerprint: str
    title: str
    claim: str
    domains: list[int]
    level: str
    level_reason: str
    evidence_types: list[str]
    status: str
    confidence: str
    date_start: str = ""
    date_end: str = ""
    missing: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    reasons: list[str] = field(default_factory=list)
    sources: list[tuple[int, str, bool]] = field(default_factory=list)  # (passage_id, role, self)
    suggestions: list[str] = field(default_factory=list)  # fingerprints of possible corroborating items


class _UnionFind:
    def __init__(self):
        self.parent: dict[int, int] = {}

    def find(self, x: int) -> int:
        self.parent.setdefault(x, x)
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        self.parent[self.find(a)] = self.find(b)


def _doc_groups(store: Store) -> dict[int, int]:
    uf = _UnionFind()
    rejected = {k for k, v in store.decisions("relation").items() if v["decision"] == "reject"}
    for rel in store.q("SELECT * FROM document_relations"):
        if str(rel["id"]) not in rejected:
            uf.union(rel["doc_a"], rel["doc_b"])
    return {d["id"]: uf.find(d["id"]) for d in store.q("SELECT id FROM documents")}


def _publication_titles(store: Store) -> dict[str, int]:
    """Map the normalized title line of each uploaded publication to its
    document group, so that a CV entry and the article itself merge."""
    titles = {}
    for d in store.q("SELECT d.id, p.text FROM documents d JOIN pages p ON p.document_id = d.id "
                     "WHERE d.genre = 'publication' AND d.excluded = 0 AND p.page_no = 1"):
        first = next((ln.strip() for ln in d["text"].splitlines() if len(ln.strip()) >= 20), "")
        if first:
            titles[sg.normalize(first)] = d["id"]
    return titles


def _cluster_key(member: Member, pub_titles: dict[str, int] | None = None) -> str:
    if pub_titles:
        flat = sg.normalize(member.text)
        for title, doc_id in pub_titles.items():
            if title in flat or member.doc["id"] == doc_id:
                return f"publication:{doc_id}"
    if member.draft.entity_key:
        return member.draft.entity_key
    entity = sg.match_entity(member.text)
    if entity:
        return entity.key
    generic = sg.generic_entity(member.text)
    if generic:
        return f"generic:{sg.normalize(generic)}"
    if member.draft.level == "L3B" and member.doc["genre"] not in sg.SELF_GENRES:
        return f"inquiry:{member.group}"
    if member.doc["genre"] == "evaluation" and "E" in member.draft.evidence_types:
        return f"evaluation:{member.group}"
    return f"passage:{member.norm_hash}"


def _load_members(store: Store, candidate_name: str) -> list[Member]:
    groups = _doc_groups(store)
    docs = {d["id"]: dict(d) for d in store.q("SELECT * FROM documents WHERE excluded = 0 AND analyzed = 1")}
    last = sg.surname(candidate_name)
    doc_linked: dict[int, bool] = {}
    meta_linked: dict[int, bool] = {}
    for doc_id, doc in docs.items():
        head = "\n".join(r["text"] for r in store.q(
            "SELECT text FROM pages WHERE document_id = ? ORDER BY page_no LIMIT 2", (doc_id,)))
        in_text = doc["genre"] in DOC_LINK_GENRES and (sg.mentions_person(head[:2500], candidate_name) or (
            doc["char_count"] < 5000 and sg.mentions_person(head, candidate_name)))
        doc_linked[doc_id] = in_text
        meta_linked[doc_id] = bool(last) and not in_text and sg.mentions_person(
            doc["metadata_author"] or "", candidate_name)

    rows = store.q(
        "SELECT c.draft, p.id AS pid, p.document_id, p.page_no, p.text, p.norm_hash "
        "FROM candidates c JOIN passages p ON p.id = c.passage_id ORDER BY p.document_id, p.id"
    )
    members = []
    for row in rows:
        doc = docs.get(row["document_id"])
        if doc is None:
            continue
        draft = guardrails.apply(Draft.from_dict(json.loads(row["draft"])))
        sig = sg.compute(row["text"])
        genre = doc["genre"]
        self_desc = genre in sg.SELF_GENRES or (sig.first_person and genre in SELF_FIRST_PERSON_GENRES)
        mentions = sg.mentions_person(row["text"], candidate_name)
        linked = self_desc or mentions or doc_linked[doc["id"]] or meta_linked[doc["id"]]
        members.append(Member(
            passage_id=row["pid"], doc=doc, page_no=row["page_no"], text=row["text"], norm_hash=row["norm_hash"],
            draft=draft, sig=sig, self_desc=self_desc, linked=linked,
            metadata_link_only=linked and not (self_desc or mentions or doc_linked[doc["id"]]),
            group=groups.get(doc["id"], doc["id"]),
        ))
    return members


def _doc_inquiry(store: Store, doc_id: int, cache: dict) -> set[str]:
    if doc_id not in cache:
        text = "\n".join(r["text"] for r in store.q("SELECT text FROM pages WHERE document_id = ?", (doc_id,)))
        s = sg.compute(text)
        cache[doc_id] = s.inquiry if s.edu_object else set()
    return cache[doc_id]


def _ordered_types(types: set[str]) -> list[str]:
    return [t for t in ["REFLECTIVE", "W", "E", "U", "R"] if t in types]


def build_item(key: str, members: list[Member], store: Store, inquiry_cache: dict) -> Item | None:
    linked = [m for m in members if m.linked]
    is_known_entity = not key.startswith(("passage:", "generic:", "inquiry:", "evaluation:"))
    role_desc = [m for m in members if not m.linked and not m.self_desc and is_known_entity]
    if not linked:
        if not is_known_entity:
            return None
        m = max(members, key=lambda x: (LEVEL_RANK.get(x.draft.level, 0), len(x.text)))
        return Item(
            fingerprint=key, title=m.draft.title, claim=m.draft.claim, domains=m.draft.domains,
            level="Not assigned", level_reason="No uploaded source links the candidate to this role or activity.",
            evidence_types=[], status="CONTEXT", confidence="Medium",
            notes=["Institutional description only. Upload a source that names the candidate in this role to use it as evidence."],
            sources=[(x.passage_id, "supporting", False) for x in members],
        )

    independent_groups = {m.group for m in linked if not m.self_desc}
    all_groups = {m.group for m in linked + role_desc}
    reasons: list[str] = []
    missing: list[str] = []
    notes: list[str] = []

    # Candidate primary: the most informative linked passage.
    primary = max(linked, key=lambda m: (
        LEVEL_RANK.get(m.draft.level, 0), STATUS_RANK.get(m.draft.status, 0),
        m.sig.action_count, not m.self_desc, len(m.text)))

    level, status, confidence, level_reason = primary.draft.level, primary.draft.status, primary.draft.confidence, primary.draft.level_reason

    # L3A: institutional action with reach, corroborated by an independent source.
    l3a_self = [m for m in linked if m.self_desc and m.l3a_ok]
    l3a_indep = [m for m in linked + role_desc if not m.self_desc and m.l3a_ok]
    l3a_potential = any(m.draft.level == "L3A" for m in linked)
    decided = False
    if l3a_indep:
        level, status = "L3A", "VERIFIED"
        corroborating = {m.group for m in l3a_indep}
        confidence = "High" if len(corroborating | {m.group for m in l3a_self} | independent_groups) >= 2 or len(l3a_indep) >= 2 else "Medium"
        src = max(l3a_indep, key=lambda m: (m.doc["genre"] in INSTITUTIONAL_GENRES, m.sig.action_count, len(m.text)))
        kind = {"minutes": "meeting minutes", "other": "document", "cv": "CV"}.get(src.doc["genre"], src.doc["genre"].replace("_", " "))
        level_reason = (
            f"An independent source ({kind}) documents institutional action with reach across UCR or a significant unit"
            + (", and a second source links the candidate to it." if len(all_groups) >= 2 else ".")
        )
        primary = l3a_self[0] if l3a_self else primary
        decided = True
    elif l3a_self:
        level, status, confidence = "L3A", "SUPPORTED", "Medium"
        level_reason = "The candidate's own account describes institutional action with reach, but no independent uploaded source corroborates it."
        missing.append("An independent source (handbook, minutes, report, policy, appointment letter, or evaluation) that corroborates the institutional action and reach.")
        reasons.append("uncorroborated_claim")
        primary = l3a_self[0]
        decided = True

    # L3B: all inquiry components across the linked sources.
    inquiry_members = [m for m in linked if m.sig.edu_object and m.draft.level == "L3B"]
    if inquiry_members and not (decided and status == "VERIFIED"):
        comps: set[str] = set()
        for m in linked:
            if m.sig.edu_object:
                comps |= m.sig.inquiry
            if not m.self_desc and m.doc["genre"] not in ("proposal",) and m.draft.level == "L3B":
                comps |= _doc_inquiry(store, m.doc["id"], inquiry_cache)
        only_proposals = all(m.doc["genre"] == "proposal" for m in inquiry_members)
        complete = set(L3B_COMPONENTS) <= comps and not only_proposals
        indep_findings = [m for m in inquiry_members if not m.self_desc and m.doc["genre"] != "proposal"]
        primary = max(inquiry_members, key=lambda m: (len(m.sig.inquiry), len(m.text)))
        if complete and indep_findings:
            level, status = "L3B", "VERIFIED"
            confidence = "High" if len(comps) == len(L3B_COMPONENTS) and not primary.sig.disciplinary else "Medium"
            level_reason = "The uploaded sources report an educational question, systematic method, evidence, findings, and use of the findings in practice."
        elif complete:
            level, status, confidence = "L3B", "SUPPORTED", "Medium"
            level_reason = "The candidate's own account reports all components of educational inquiry, but no independent report or publication is uploaded."
            reasons.append("uncorroborated_claim")
        else:
            level, status, confidence = "L3B", "POTENTIAL", "Medium"
            level_reason = "The sources establish an educational inquiry question or intervention but do not show that systematic inquiry was completed and reported."
            missing.extend(L3B_COMPONENTS[c] for c in L3B_COMPONENTS if c not in comps)
            if only_proposals and "findings" in comps:
                missing.append("A report of completed work: the only inquiry source is a proposal, which describes planned rather than completed inquiry.")
            reasons.append("l3b_incomplete")
        decided = True

    if not decided:
        if level in ("L3A", "L3B"):
            status = "POTENTIAL"
        if level == "L3A" and l3a_potential:
            reasons.append("l3a_reach_unclear")
        if status == "VERIFIED" and not independent_groups:
            status = "SUPPORTED"
            if level in ("L2",) and primary.doc["genre"] == "cv":
                missing.append("An independent source confirming the role or activity (appointment letter, minutes, or programme document).")
        for m in linked:
            missing.extend(m.draft.missing_evidence if m.draft.status != "VERIFIED" or status != "VERIFIED" else [])

    # Evidence types.
    types: set[str] = set()
    for m in linked + role_desc:
        types |= set(m.draft.evidence_types)
        if not m.self_desc:
            if m.doc["genre"] in WORK_GENRES:
                types.add("W")
            if m.doc["genre"] == "evaluation":
                types.add("E")
            if m.l3a_ok and m.doc["genre"] in ("handbook", "policy", "minutes"):
                types.add("U")
        if m.doc["genre"] == "reflective":
            types.add("REFLECTIVE")
    if level == "Not assigned" and status == "CONTEXT":
        types.discard("U")

    # Domains weighted by position.
    weights: Counter = Counter()
    for m in linked + role_desc:
        for i, d in enumerate(m.draft.domains):
            weights[d] += 2 if i == 0 else 1
    for d in primary.draft.domains[:1]:
        weights[d] += 3
    top = weights.most_common(1)[0][1]
    domains = [d for d, w in weights.most_common() if w >= top * 0.4][:3]

    # Dates and contradictions.
    ranges: dict[int, tuple[str, str]] = {}
    starts, ends = [], []
    for m in linked:
        start, end = sg.date_range(m.text)
        if start:
            starts.append(start)
            ends.append(end)
            if start != end and m.doc["id"] not in ranges:
                ranges[m.doc["id"]] = (start, end)
    distinct = set(ranges.values())
    if len(distinct) > 1 and is_known_entity:
        reasons.append("conflicting_dates")
        notes.append("Date ranges differ across sources: " + ", ".join(f"{a}-{b}" for a, b in sorted(distinct)) + ".")
    date_start = min(starts) if starts else ""
    real_ends = [e for e in ends if e != "present"]
    date_end = "present" if "present" in ends else (max(real_ends) if real_ends else "")

    if any(m.metadata_link_only for m in linked):
        reasons.append("unclear_authorship")
        notes.append("The only link to the candidate is the file's metadata author field, which does not establish authorship.")
        if status == "VERIFIED":
            status = "SUPPORTED"

    if confidence == "Low":
        reasons.append("low_confidence")

    # Sources: primary, supporting and exact duplicate copies.
    sources: list[tuple[int, str, bool]] = [(primary.passage_id, "primary", primary.self_desc)]
    seen_hashes = {primary.norm_hash}
    for m in sorted(linked + role_desc, key=lambda x: (x.self_desc, -len(x.text))):
        if m.passage_id == primary.passage_id:
            continue
        role = "duplicate copy" if m.norm_hash in seen_hashes else "supporting"
        seen_hashes.add(m.norm_hash)
        sources.append((m.passage_id, role, m.self_desc))

    entity = next((e for e in sg.ENTITIES if e.key == key), None)
    if entity:
        title = entity.l3a_title if (level == "L3A" and status == "VERIFIED") else entity.title
    elif key.startswith("evaluation:"):
        title = f"Evaluation: {Path(primary.doc['filename']).stem.replace('_', ' ')}"
    else:
        title = primary.draft.title

    if status in ("VERIFIED", "CONTEXT", "REJECT"):
        missing = [] if status == "VERIFIED" else missing
    missing = list(dict.fromkeys(x for x in missing if x))
    notes.extend(n for n in dict.fromkeys(m.draft.notes for m in linked) if n)

    return Item(
        fingerprint=key, title=title, claim=primary.draft.claim or primary.text, domains=domains,
        level=level, level_reason=level_reason.strip(), evidence_types=_ordered_types(types), status=status,
        confidence=confidence, date_start=date_start, date_end=date_end, missing=missing,
        notes=list(dict.fromkeys(notes)), reasons=list(dict.fromkeys(reasons)), sources=sources,
    )


def _terms(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z]{5,}", text.lower()) if w not in STOPWORDS}


def suggest_corroboration(items: list[Item]) -> None:
    """For claims that rest only on the candidate's own account, point to
    independently sourced items that may corroborate them. The user confirms
    a link in the review inbox. Nothing is merged automatically."""
    independent = [i for i in items if i.status == "VERIFIED" and any(not s for _, _, s in i.sources)]
    for item in items:
        if "uncorroborated_claim" not in item.reasons and "l3a_reach_unclear" not in item.reasons:
            continue
        terms = _terms(item.title + " " + item.claim)
        scored = []
        for other in independent:
            if other.fingerprint == item.fingerprint or not set(other.domains) & set(item.domains):
                continue
            shared = terms & _terms(other.title + " " + other.claim)
            if shared:
                scored.append((len(shared), other.fingerprint))
        item.suggestions = [fp for _, fp in sorted(scored, reverse=True)[:3]]


def rebuild(store: Store) -> dict:
    candidate_name = store.get_setting("candidate_name")
    members = _load_members(store, candidate_name)
    pub_titles = _publication_titles(store)
    clusters: dict[str, list[Member]] = defaultdict(list)
    for m in members:
        clusters[_cluster_key(m, pub_titles)].append(m)
    # Links confirmed by the user: merge one item's sources into another.
    for key, row in store.decisions("merge").items():
        into = json.loads(row["payload"] or "{}").get("into", "")
        if row["decision"] == "merge" and key in clusters and into in clusters and key != into:
            clusters[into].extend(clusters.pop(key))
    inquiry_cache: dict = {}
    items = [i for i in (build_item(k, v, store, inquiry_cache) for k, v in clusters.items()) if i]
    suggest_corroboration(items)

    with store.tx() as c:
        c.execute("DELETE FROM evidence")
        for item in items:
            auto = {
                "title": item.title, "claim": item.claim, "domains": item.domains, "level": item.level,
                "level_reason": item.level_reason, "evidence_types": item.evidence_types, "status": item.status,
                "confidence": item.confidence, "missing_evidence": "\n".join(item.missing), "notes": "\n".join(item.notes),
            }
            cur = c.execute(
                "INSERT INTO evidence(fingerprint, title, claim, domains, level, level_reason, evidence_types, status, "
                "confidence, date_start, date_end, needs_more_evidence, missing_evidence, notes, review_reasons, "
                "review_state, auto_classification, suggested_links) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (item.fingerprint, item.title, item.claim, json.dumps(item.domains), item.level, item.level_reason,
                 json.dumps(item.evidence_types), item.status, item.confidence, item.date_start, item.date_end,
                 int(bool(item.missing) and item.status in ("SUPPORTED", "POTENTIAL")), "\n".join(item.missing),
                 "\n".join(item.notes), json.dumps(item.reasons), "pending" if item.reasons else "none",
                 json.dumps(auto), json.dumps(item.suggestions)),
            )
            c.executemany(
                "INSERT OR IGNORE INTO evidence_sources(evidence_id, passage_id, role, self_description) VALUES (?, ?, ?, ?)",
                [(cur.lastrowid, pid, role, int(self_)) for pid, role, self_ in item.sources],
            )
    apply_decisions(store)
    return {"evidence_items": len(items)}


# ---------------------------------------------------------------------------
# Review decisions

EDITABLE = ("title", "claim", "domains", "level", "level_reason", "evidence_types", "status", "confidence",
            "missing_evidence", "notes", "date_start", "date_end")


def apply_decisions(store: Store) -> None:
    with store.tx() as c:
        for key, row in store.decisions("evidence").items():
            payload = json.loads(row["payload"] or "{}")
            if row["decision"] == "accept":
                c.execute("UPDATE evidence SET review_state = 'accepted' WHERE fingerprint = ?", (key,))
            elif row["decision"] == "reject":
                c.execute("UPDATE evidence SET status = 'REJECT', review_state = 'rejected' WHERE fingerprint = ?", (key,))
            elif row["decision"] == "edit":
                fields = {k: v for k, v in payload.items() if k in EDITABLE}
                for k in ("domains", "evidence_types"):
                    if k in fields:
                        fields[k] = json.dumps(fields[k])
                if fields:
                    sets = ", ".join(f"{k} = ?" for k in fields)
                    c.execute(f"UPDATE evidence SET {sets}, review_state = 'edited' WHERE fingerprint = ?",
                              (*fields.values(), key))
        for key, row in store.decisions("dossier").items():
            c.execute("UPDATE evidence SET include_in_dossier = ? WHERE fingerprint = ?",
                      (1 if row["decision"] == "include" else 0, key))


def decide_evidence(store: Store, fingerprint: str, decision: str, payload: dict | None = None) -> None:
    store.record_decision("evidence", fingerprint, decision, payload)
    apply_decisions(store)


def decide_document(store: Store, doc_id: int, decision: str, manual_text: str = "") -> None:
    """Accept: keep the unreadable document on record for visual review.
    Edit: replace its text with a manual transcription and analyze it.
    Reject: exclude it from the evidence base."""
    store.record_decision("document", str(doc_id), decision, {"manual_text": bool(manual_text)})
    with store.tx() as c:
        if decision == "reject":
            c.execute("UPDATE documents SET excluded = 1 WHERE id = ?", (doc_id,))
        elif decision == "edit" and manual_text.strip():
            c.execute("DELETE FROM pages WHERE document_id = ?", (doc_id,))
            c.execute("INSERT INTO pages(document_id, page_no, text) VALUES (?, 1, ?)", (doc_id, manual_text))
            c.execute("UPDATE documents SET manual_text = 1, analyzed = 0 WHERE id = ?", (doc_id,))


def decide_relation(store: Store, relation_id: int, decision: str) -> None:
    """Accept: the documents are duplicates, so the later one is excluded and
    one logical source remains. Reject: they are different documents."""
    store.record_decision("relation", str(relation_id), decision)
    if decision == "accept":
        rel = store.one("SELECT * FROM document_relations WHERE id = ?", (relation_id,))
        if rel:
            with store.tx() as c:
                c.execute("UPDATE documents SET excluded = 1 WHERE id = ?", (rel["doc_b"],))
    rebuild(store)


def link_evidence(store: Store, fingerprint: str, into: str) -> None:
    """Record that the sources of one item corroborate another, then rebuild
    so that status and confidence are recalculated from the combined sources."""
    store.record_decision("merge", fingerprint, "merge", {"into": into})
    store.record_decision("evidence", into, "accept")
    rebuild(store)


def set_dossier_inclusion(store: Store, fingerprint: str, include: bool) -> None:
    store.record_decision("dossier", fingerprint, "include" if include else "exclude")
    apply_decisions(store)
