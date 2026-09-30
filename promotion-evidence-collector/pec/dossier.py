"""Dossier generator for the UCR Career Progression Procedure (UD1 to UHD2).

The dossier has exactly three sections: Reflective Statement, Career
Framework Overview and Selective Evidence Portfolio. The generator produces an
editable draft (plain JSON) from the evidence database. The candidate edits
the draft in the interface and exports it to DOCX.

Every sentence the generator writes is assembled from stored evidence records
and their sources. It adds no evaluative adjectives and no outcomes.

A separate full evidence report exports every non-rejected record as an audit
trail. It is not part of the dossier.
"""

from __future__ import annotations

import io
import re
from dataclasses import asdict, dataclass, field
from datetime import date
from pathlib import Path

from . import framework as fw
from . import queries
from .db import Store

L3_LEVELS = ("L3A", "L3B")
TITLE_GENRES = {"handbook", "policy", "report", "proposal", "publication", "minutes", "certificate", "course_material"}
PORTFOLIO_MIN, PORTFOLIO_MAX = 8, 15


@dataclass
class DossierOptions:
    include_supported: bool = False
    include_gaps: bool = False
    include_source_list: bool = False
    include_appendix: bool = False
    include_passages: bool = False


@dataclass
class PortfolioEntry:
    fingerprint: str
    title: str
    domain: str
    level: str
    evidence_type: str
    description: str
    why: str
    period: str
    primary_source: str
    supporting_sources: str
    status: str
    passages: list[str] = field(default_factory=list)


@dataclass
class DossierDraft:
    candidate: str
    options: dict
    statement: str
    overview_header: dict
    overview: list[dict]
    portfolio: list[dict]
    gaps: list[str] = field(default_factory=list)
    appendix: list[dict] = field(default_factory=list)
    source_list: list[str] = field(default_factory=list)
    generated: str = ""

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "DossierDraft":
        return cls(**{k: data[k] for k in cls.__dataclass_fields__ if k in data})


# ---------------------------------------------------------------------------
# Short source references


class References:
    """Short, human-readable references such as "CV, p. 1" or
    "Interdisciplinary Education Programme Proposal, 2022"."""

    def __init__(self, store: Store):
        self.store = store
        self._names: dict[int, str] = {}

    def name(self, doc_id: int) -> str:
        if doc_id in self._names:
            return self._names[doc_id]
        doc = self.store.one("SELECT * FROM documents WHERE id = ?", (doc_id,))
        name = ""
        if doc["genre"] == "cv":
            name = "CV"
        elif doc["genre"] in TITLE_GENRES and doc["genre"] != "certificate":
            first = self.store.one("SELECT text FROM pages WHERE document_id = ? ORDER BY page_no LIMIT 1", (doc_id,))
            for line in (first["text"] if first else "").splitlines():
                line = re.sub(r"^(proposal|report|certificate)\s*:\s*", "", line.strip(), flags=re.I).strip(" .:")
                if 10 <= len(line) <= 90 and len(line.split()) >= 2 and sum(ch.isalpha() for ch in line) > 8:
                    name = line
                    break
            if name and doc["genre"] == "proposal" and "proposal" not in name.lower():
                name += " proposal"
        if not name:
            stem = Path(doc["filename"]).stem
            stem = re.sub(r"\((copy|\d+)\)|\b(final|draft|v\d+)\b", "", stem, flags=re.I)
            stem = re.sub(r"[_]+", " ", stem)
            stem = re.sub(r"\s+", " ", stem).strip(" -")
            name = stem or doc["filename"]
            if doc["genre"] == "reflective" and not re.search(r"statement|reflect", name, re.I):
                name += " (reflective statement)"
        self._names[doc_id] = name
        return name

    def ref(self, src: queries.Source) -> str:
        name = self.name(src.document_id)
        if src.paged and src.page_label == "page":
            return f"{name}, p. {src.page_no}"
        if src.paged and src.page_label == "slide":
            return f"{name}, slide {src.page_no}"
        year = src.doc_date[:4] if src.doc_date and src.doc_date_source == "document text" else ""
        return f"{name}, {year}" if year and year not in name else name

    def join(self, sources: list[queries.Source]) -> str:
        return "; ".join(dict.fromkeys(self.ref(s) for s in sources))


# ---------------------------------------------------------------------------
# Selection


def _load(store: Store) -> list[dict]:
    items = queries.evidence(store, "WHERE status != 'REJECT'")
    for item in items:
        srcs = [s for s in queries.sources_for(store, item["id"]) if s.role != "duplicate copy"]
        item["sources"] = srcs
        item["primary"] = next((s for s in srcs if s.role == "primary"), srcs[0] if srcs else None)
        item["supporting"] = [s for s in srcs if s.role != "primary"]
        item["independent_docs"] = len({s.document_id for s in srcs if not s.self_description})
        item["period"] = queries.fmt_dates(item)
    return items


def _years(period: str) -> int:
    nums = re.findall(r"\d{4}", period)
    if not nums:
        return 0
    end = date.today().year if "present" in period else int(nums[-1])
    return max(0, end - int(nums[0]))


def _score(item: dict) -> float:
    score = {"VERIFIED": 100, "SUPPORTED": 45, "POTENTIAL": 20}.get(item["status"], 0)
    score += {"L4": 60, "L3A": 50, "L3B": 50, "L2": 20, "L1": 8}.get(item["level"], 0)
    score += min(item["independent_docs"], 3) * 8
    score += 10 if "U" in item["evidence_types"] else 0
    score += 5 if _years(item["period"]) >= 2 else 0
    score += 5 if "R" in item["evidence_types"] else 0
    return score


def _eligible(item: dict, options: DossierOptions) -> bool:
    if item["status"] == "VERIFIED":
        return item["level"] != "Not assigned" or "R" in item["evidence_types"]
    if item["status"] == "SUPPORTED":
        return options.include_supported and item["level"] != "Not assigned"
    if item["status"] == "POTENTIAL":
        return bool(item["include_in_dossier"])
    return False


def select_portfolio(items: list[dict], options: DossierOptions) -> list[dict]:
    """Greedy selection: strongest first, with limits on repetition so that no
    domain or low level fills the portfolio."""
    pool = sorted((i for i in items if _eligible(i, options)), key=_score, reverse=True)
    chosen: list[dict] = []
    per_domain: dict[int, int] = {}
    low = 0
    for item in pool:
        if len(chosen) >= PORTFOLIO_MAX:
            break
        d = item["domains"][0]
        is_low = item["level"] in ("L1", "Not assigned")
        if per_domain.get(d, 0) >= 4 or (is_low and (low >= 4 or per_domain.get(d, 0) >= 2)):
            continue
        chosen.append(item)
        per_domain[d] = per_domain.get(d, 0) + 1
        low += is_low
    # Selected potential items always appear when the user chose them.
    for item in pool:
        if item["status"] == "POTENTIAL" and item not in chosen:
            chosen.append(item)
    order = {d: i for i, d in enumerate(fw.DOMAINS)}
    return sorted(chosen, key=lambda i: (order[i["domains"][0]], -_score(i)))


# ---------------------------------------------------------------------------
# Text helpers


SENTENCE_END = re.compile(
    r"(?<!\bDr\.)(?<!\bProf\.)(?<!\bMr\.)(?<!\bMs\.)(?<!\bMrs\.)(?<!\be\.g\.)(?<!\bi\.e\.)(?<!\bvs\.)"
    r"(?<!\bno\.)(?<!\bp\.)(?<!\b[A-Z]\.)(?<=[.!?])\s+(?=[A-Z0-9\"'(])"
)
BULLET_START = re.compile(r"^\s*([-*\u2022]|\d+[.)])\s+")


def _units(text: str) -> list[str]:
    """Rejoin lines that a PDF or text file wrapped mid-sentence. Bullet
    items, table rows and short heading lines stay separate."""
    units: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            units.append("")
            continue
        is_row = " | " in stripped
        starts_new = (not units or not units[-1] or BULLET_START.match(line) or is_row
                      or " | " in units[-1] or re.search(r"[.!?:]$", units[-1])
                      or (len(units[-1]) < 60 and not re.search(r"[,;]$|\b(a|an|the|and|of|to|in|for|with)$", units[-1])))
        if starts_new:
            units.append(stripped)
        else:
            units[-1] += " " + stripped
    return [u for u in units if u]


def _split_sentences(text: str) -> list[str]:
    parts = []
    for unit in _units(text):
        unit = BULLET_START.sub("", unit).strip()
        if not unit or re.match(r"^sheet:", unit, re.I) or (" | " in unit and ":" not in unit):
            continue
        parts.extend(s.strip() for s in SENTENCE_END.split(unit) if s and s.strip())
    return parts


def _key_sentences(text: str, limit: int = 240) -> str:
    """The sentences of a source passage that state the activity, in their
    original order. Headers and table header rows are dropped."""
    from . import signals as sg

    sentences = _split_sentences(text)
    if not sentences:
        return ""

    def weight(s: str) -> int:
        sig = sg.compute(s)
        return 3 * sig.action + 2 * sig.scope + 2 * len(sig.inquiry) + (2 if sg.match_entity(s) else 0) + (1 if sg.YEAR_RE.search(s) else 0)

    ranked = sorted(range(len(sentences)), key=lambda i: (-weight(sentences[i]), i))
    keep: list[int] = []
    for i in ranked:
        if weight(sentences[i]) == 0 and keep:
            break
        if sum(len(sentences[j]) for j in keep) + len(sentences[i]) > limit and keep:
            continue
        keep.append(i)
    out = " ".join(sentences[i].rstrip(" .;:") + "." for i in sorted(keep))
    return out if len(out) <= limit + 40 else out[:limit].rsplit(" ", 1)[0] + " [...]"


def _sentence(text: str, limit: int = 240) -> str:
    return _key_sentences(text, limit)


def _phrase(item: dict) -> str:
    title = re.sub(r"[,;]?\s*\(?\b(19|20)\d{2}\s*(-\s*((19|20)\d{2}|present))?\)?\.?$", "", item["title"]).strip(" ,.")
    title = re.sub(r"\s*\[\.\.\.\]$", "", title)
    return f"{title} ({item['period']})" if item["period"] else title


def _lower_first(text: str) -> str:
    """Lowercase the first word unless it begins a proper name."""
    words = text.split()
    if len(words) >= 2 and words[1][:1].isupper():
        return text
    if words and (words[0].isupper() or re.match(r"^[A-Z][a-z]*[A-Z]", words[0])):
        return text
    return text[:1].lower() + text[1:]


def _why(item: dict) -> str:
    d = item["domains"][0]
    parts = [item["level_reason"]]
    if item["level"] == "L3A" and item["status"] != "POTENTIAL":
        parts.append(f"Framework description for L3A in {fw.DOMAINS[d].lower()}: {fw.L3A_DOMAIN_RULES[d]}")
    elif item["level"] == "L3B" and item["status"] != "POTENTIAL":
        parts.append(f"Framework description for L3B in {fw.DOMAINS[d].lower()}: {fw.L3B_DOMAIN_RULES[d]}")
    if item["status"] == "SUPPORTED":
        parts.append("Status: supported. An additional independent source would strengthen this claim.")
    if item["status"] == "POTENTIAL":
        parts.append("Status: potential. Included at the candidate's request. The evidence is incomplete.")
    return " ".join(p.strip() for p in parts if p.strip())


def portfolio_entry(item: dict, refs: References, include_passages: bool) -> PortfolioEntry:
    domains = item["domains"]
    return PortfolioEntry(
        fingerprint=item["fingerprint"],
        title=re.sub(r"\s*\[\.\.\.\]$", "", item["title"]),
        domain=fw.DOMAINS[domains[0]] + (f" (also: {', '.join(fw.SHORT_DOMAINS[d].lower() for d in domains[1:])})" if len(domains) > 1 else ""),
        level=item["level"] if item["status"] != "POTENTIAL" else f"Potential {item['level']}",
        evidence_type=", ".join(item["evidence_types"]) or "None assigned",
        description=_sentence(item["primary"].text if item["primary"] else item["claim"]),
        why=_why(item),
        period=item["period"] or "Not stated in the sources",
        primary_source=refs.ref(item["primary"]) if item["primary"] else "",
        supporting_sources=refs.join([s for s in item["supporting"] if s.document_id != (item["primary"].document_id if item["primary"] else None)]),
        status=item["status"],
        passages=[f"{refs.ref(s)}: \"{re.sub(chr(10), ' ', s.text).strip()}\"" for s in item["sources"]] if include_passages else [],
    )


# ---------------------------------------------------------------------------
# Section 2: overview


def _best(items: list[dict], domain: int) -> dict | None:
    in_domain = [i for i in items if queries.primary_domain(i) == domain and i["level"] != "Not assigned"]
    for statuses in (("VERIFIED",), ("SUPPORTED",)):
        pool = [i for i in in_domain if i["status"] in statuses]
        if pool:
            return max(pool, key=lambda i: (fw.LEVEL_RANK[i["level"]], _score(i)))
    chosen = [i for i in in_domain if i["status"] == "POTENTIAL" and i["include_in_dossier"]]
    return max(chosen, key=_score) if chosen else None


def build_overview(items: list[dict], refs: References) -> tuple[dict, list[dict]]:
    rows = []
    l3_verified = 0
    for d, name in fw.DOMAINS.items():
        best = _best(items, d)
        if best is None:
            rows.append({"Domain": f"{d}. {name}", "Highest supported level": "No evidence uploaded",
                         "Strongest claim": "", "Evidence type": "", "Key evidence": "", "Source": "", "Status": ""})
            continue
        if best["level"] in L3_LEVELS and best["status"] == "VERIFIED":
            l3_verified += 1
        level = best["level"] if best["status"] != "POTENTIAL" else f"Potential {best['level']}"
        also = [i for i in items if queries.primary_domain(i) == d and i["status"] == best["status"] and i["level"] in L3_LEVELS
                and i["level"] != best["level"] and best["level"] in L3_LEVELS]
        if also:
            level = " and ".join(sorted({best["level"], also[0]["level"]}))
        rows.append({
            "Domain": f"{d}. {name}",
            "Highest supported level": level,
            "Strongest claim": re.sub(r"\s*\[\.\.\.\]$", "", best["title"]),
            "Evidence type": ", ".join(best["evidence_types"]),
            "Key evidence": _sentence(best["primary"].text if best["primary"] else best["claim"], 160),
            "Source": refs.join(best["sources"][:3]),
            "Status": best["status"].title(),
        })
    header = {
        "Target": "Level 3",
        "L3 domains supported": str(l3_verified),
        "L3 domains required for UHD2": str(fw.L3_DOMAINS_REQUIRED),
        "Summary": f"Current uploaded evidence supports Level 3 claims in {l3_verified} domain{'s' if l3_verified != 1 else ''}.",
    }
    return header, rows


# ---------------------------------------------------------------------------
# Section 1: reflective statement


def _evidence_sentence(item: dict, refs: References, limit: int) -> str:
    primary = item["primary"]
    others = [s for s in item["sources"] if primary is None or s.document_id != primary.document_id]
    text = f"{_phrase(item)}. "
    if primary is not None:
        text += f"{refs.ref(primary)} records: \"{_sentence(primary.text, limit).rstrip('.')}.\" "
    if others:
        text += f"Corroborating sources: {refs.join(others[:3])}. "
    return text


def build_statement(items: list[dict], refs: References, candidate: str) -> str:
    usable = [i for i in items if i["status"] in ("VERIFIED", "SUPPORTED")]
    dated = sorted((i for i in usable if i["date_start"]), key=lambda i: (i["date_start"], i["date_end"]))
    paras: list[str] = []

    # Development as an educator.
    reflective = [i for i in items if "REFLECTIVE" in i["evidence_types"] and i["primary"] and i["primary"].self_description]
    if dated:
        early = [i for i in dated if i["level"] in ("L1", "L2")][:3]
        later = [i for i in dated if i["level"] in ("L2", "L3A", "L3B") and i not in early][-3:]
        text = f"This statement accompanies my application for promotion from {fw.PROMOTION_ROUTE}. The uploaded sources document my educational work at UCR from {dated[0]['date_start']}"
        last = max((i["date_end"] for i in dated if i["date_end"]), default="present")
        text += " to the present." if last == "present" else f" to {last}."
        if early:
            text += " The earliest documented activities are " + "; ".join(_lower_first(_phrase(i)) for i in early) + "."
        if later:
            text += " Later sources record " + "; ".join(_lower_first(_phrase(i)) for i in later) + "."
        paras.append(text)
    else:
        paras.append(f"This statement accompanies my application for promotion from {fw.PROMOTION_ROUTE}.")
    for item in reflective[:2]:
        source_name = re.sub(r"\s*\(?\b(19|20)\d{2}\b\)?", "", refs.name(item["primary"].document_id)).strip().lower()
        paras.append(f"In my {source_name} I wrote: \"{_sentence(item['primary'].text, 400).rstrip('.')}.\"")
    paras.append("[Describe how your approach to teaching and supporting student learning has developed, and what prompted the changes.]")

    # Principal educational contributions by domain.
    contributions = []
    for d, name in fw.DOMAINS.items():
        best = _best(usable, d)
        if best and best["level"] in ("L2", "L3A", "L3B", "L4"):
            contributions.append(f"In {name.lower()}, the principal documented contribution is {_lower_first(_phrase(best))} ({refs.join(best['sources'][:2])}).")
    if contributions:
        paras.append("My principal educational contributions fall in the following domains. " + " ".join(contributions))

    # Institutional leadership (L3A).
    l3a = sorted((i for i in usable if i["level"] == "L3A"), key=_score, reverse=True)
    verified_a = [i for i in l3a if i["status"] == "VERIFIED"]
    if verified_a:
        text = "Institutional leadership (Level 3A). "
        for item in verified_a[:3]:
            text += _evidence_sentence(item, refs, 220)
        paras.append(text.strip())
        paras.append("[Explain what you changed in these structures or systems, how colleagues were involved, and what the documented use of this work shows.]")
    supported_a = [i for i in l3a if i["status"] == "SUPPORTED"]
    if supported_a:
        paras.append("The following leadership work is described in my own account but is not yet corroborated by an independent uploaded source, so it is presented as supported rather than verified: "
                     + "; ".join(_lower_first(_phrase(i)) for i in supported_a[:3]) + ".")
    if not verified_a and not supported_a:
        paras.append("The uploaded evidence does not currently document institutional leadership at Level 3A.")

    # Scholarly inquiry (L3B).
    l3b = sorted((i for i in items if i["level"] == "L3B" and i["status"] != "REJECT"), key=_score, reverse=True)
    verified_b = [i for i in l3b if i["status"] == "VERIFIED"]
    if verified_b:
        text = "Scholarly teaching and educational inquiry (Level 3B). "
        for item in verified_b[:2]:
            text += _evidence_sentence(item, refs, 300)
        paras.append(text.strip())
        paras.append("[Explain the educational question, how you investigated it, what you found, and how the findings changed practice.]")
    potential_b = [i for i in l3b if i["status"] in ("POTENTIAL", "SUPPORTED")]
    for item in potential_b[:2]:
        missing = "; ".join(_lower_first(m.strip().rstrip(".")) for m in item["missing_evidence"].splitlines() if m.strip()) or "a report of completed inquiry"
        paras.append(f"{_phrase(item)} is presented as potential Level 3B work. The uploaded sources do not yet document: {_lower_first(missing)}.")
    if not verified_b and not potential_b:
        paras.append("The uploaded evidence does not currently document systematic educational inquiry at Level 3B.")
    disciplinary = [i for i in items if i["status"] == "CONTEXT" and re.search(r"disciplinary", i["level_reason"], re.I)]
    if disciplinary:
        paras.append("My disciplinary research is relevant context for my teaching. It is not presented here as educational inquiry.")

    # Development over time and professional development.
    pd = [i for i in items if i["status"] == "CONTEXT" and 4 in i["domains"] and "R" in i["evidence_types"]
          and re.search(r"qualification|professional", i["title"] + i["level_reason"], re.I)]
    if pd:
        paras.append("My professional development as a teacher is recorded in " + "; ".join(
            f"{_lower_first(_phrase(i))} ({refs.join(i['sources'][:2])})" for i in pd[:3])
            + ". These records support my educational expertise. They are not presented as evidence of Level 3.")
    l3_dated = [i for i in dated if i["level"] in L3_LEVELS and i["status"] == "VERIFIED"]
    lower_dated = [i for i in dated if i["level"] in ("L1", "L2")]
    if l3_dated and lower_dated:
        paras.append(f"Over time, the documented work moves from activity within courses and programmes, beginning in {lower_dated[0]['date_start']}, "
                     f"to institutional and inquiry-based work from {min(i['date_start'] for i in l3_dated)}.")

    # Strongest current Level 3 evidence.
    l3_domains = sorted({d for i in usable if i["level"] in L3_LEVELS and i["status"] == "VERIFIED" for d in i["domains"][:1]})
    n = len(l3_domains)
    closing = f"Current uploaded evidence supports Level 3 claims in {n} domain{'s' if n != 1 else ''}"
    closing += (": " + "; ".join(fw.DOMAINS[d].lower() for d in l3_domains) + "." if n else ".")
    closing += f" The procedure requires Level 3 evidence in at least {fw.L3_DOMAINS_REQUIRED} domains for {fw.TARGET_POSITION}."
    strongest = sorted((i for i in usable if i["level"] in L3_LEVELS and i["status"] == "VERIFIED"), key=_score, reverse=True)[:3]
    if strongest:
        closing += " The strongest current items are " + "; ".join(_lower_first(_phrase(i)) for i in strongest) + "."
    paras.append(closing)
    paras.append("[Close with the direction of your educational work in the coming years.]")
    return "\n\n".join(paras)


# ---------------------------------------------------------------------------
# Gaps, appendix and source list


def build_gaps(items: list[dict], portfolio: list[dict]) -> list[str]:
    gaps = []
    for item in sorted(items, key=_score, reverse=True):
        if item["status"] in ("SUPPORTED", "POTENTIAL") and item["missing_evidence"] and item["level"] in ("L2", "L3A", "L3B", "L4"):
            gaps.append(f"{_phrase(item)}: " + " ".join(m.strip().rstrip(".") + "." for m in item["missing_evidence"].splitlines() if m.strip()))
        if "unclear_authorship" in item["review_reasons"]:
            gaps.append(f"{_phrase(item)}: documentation establishing authorship or substantial contribution.")
    covered = {d for i in portfolio for d in i["domains"][:1] if i["level"] in L3_LEVELS and i["status"] == "VERIFIED"}
    if len(covered) < fw.L3_DOMAINS_REQUIRED:
        gaps.append(f"Verified Level 3 evidence in at least {fw.L3_DOMAINS_REQUIRED} domains. Currently verified in {len(covered)}.")
    return list(dict.fromkeys(gaps))[:25]


def build_appendix(items: list[dict], portfolio: list[dict], refs: References) -> list[dict]:
    chosen = {i["fingerprint"] for i in portfolio}
    rows = []
    for item in sorted(items, key=lambda i: (i["domains"][0], -_score(i))):
        if item["fingerprint"] in chosen or item["status"] not in ("VERIFIED", "SUPPORTED", "CONTEXT"):
            continue
        rows.append({"Domain": fw.SHORT_DOMAINS[item["domains"][0]], "Evidence": _phrase(item),
                     "Level": item["level"], "Status": item["status"].title(),
                     "Source": refs.join(item["sources"][:2])})
    return rows


def build_source_list(portfolio_items: list[dict], refs: References) -> list[str]:
    docs = {}
    for item in portfolio_items:
        for s in item["sources"]:
            docs.setdefault(s.document_id, s)
    lines = []
    for doc_id, s in sorted(docs.items(), key=lambda x: refs.name(x[0]).lower()):
        date_note = f", {s.doc_date}" if s.doc_date and s.doc_date_source == "document text" else ""
        lines.append(f"{refs.name(doc_id)} (file: {s.filename}{date_note})")
    return lines


# ---------------------------------------------------------------------------
# Generate and edit


def generate(store: Store, options: DossierOptions | None = None) -> DossierDraft:
    options = options or DossierOptions()
    refs = References(store)
    items = _load(store)
    chosen = select_portfolio(items, options)
    header, overview = build_overview(items, refs)
    return DossierDraft(
        candidate=store.get_setting("candidate_name"),
        options=asdict(options),
        statement=build_statement(items, refs, store.get_setting("candidate_name")),
        overview_header=header,
        overview=overview,
        portfolio=[asdict(portfolio_entry(i, refs, options.include_passages)) for i in chosen],
        gaps=build_gaps(items, chosen) if options.include_gaps else [],
        appendix=build_appendix(items, chosen, refs) if options.include_appendix else [],
        source_list=build_source_list(chosen, refs) if options.include_source_list else [],
        generated=date.today().isoformat(),
    )


def add_to_portfolio(store: Store, draft: DossierDraft, fingerprint: str) -> DossierDraft:
    """Add one database item to an existing draft without regenerating."""
    if any(p["fingerprint"] == fingerprint for p in draft.portfolio):
        return draft
    items = [i for i in _load(store) if i["fingerprint"] == fingerprint]
    if items:
        entry = portfolio_entry(items[0], References(store), draft.options.get("include_passages", False))
        draft.portfolio.append(asdict(entry))
        if draft.options.get("include_source_list"):
            draft.source_list = list(dict.fromkeys(draft.source_list + build_source_list(items, References(store))))
    return draft


def remove_from_portfolio(draft: DossierDraft, fingerprint: str) -> DossierDraft:
    draft.portfolio = [p for p in draft.portfolio if p["fingerprint"] != fingerprint]
    return draft


def word_count(text: str) -> int:
    return len(re.findall(r"\b\w[\w'-]*\b", text))


# ---------------------------------------------------------------------------
# DOCX export


def _page_number_footer(section) -> None:
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.enum.text import WD_ALIGN_PARAGRAPH

    paragraph = section.footer.paragraphs[0]
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = paragraph.add_run()
    for tag, text in (("begin", None), (None, "PAGE"), ("end", None)):
        if tag:
            el = OxmlElement("w:fldChar")
            el.set(qn("w:fldCharType"), tag)
        else:
            el = OxmlElement("w:instrText")
            el.set(qn("xml:space"), "preserve")
            el.text = text
        run._r.append(el)


def _document():
    import docx
    from docx.shared import Pt, Cm

    document = docx.Document()
    normal = document.styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(11)
    for section in document.sections:
        section.left_margin = section.right_margin = Cm(2.3)
        _page_number_footer(section)
    return document


def _table(document, rows: list[list[str]], widths=None, font_size: float = 9, header: bool = True):
    from docx.shared import Pt, Cm

    table = document.add_table(rows=len(rows), cols=len(rows[0]))
    table.style = "Table Grid"
    for r, row in enumerate(rows):
        for c, value in enumerate(row):
            cell = table.cell(r, c)
            cell.text = ""
            run = cell.paragraphs[0].add_run(str(value))
            run.font.size = Pt(font_size)
            if header and r == 0:
                run.bold = True
            if widths:
                cell.width = Cm(widths[c])
    return table


def _paragraphs(document, text: str) -> None:
    for para in re.split(r"\n\s*\n", text.strip()):
        if para.strip():
            document.add_paragraph(re.sub(r"\s*\n\s*", " ", para.strip()))


def dossier_docx(draft: DossierDraft) -> bytes:
    from docx.enum.section import WD_ORIENT

    document = _document()
    document.add_heading("Academic Career Progression Dossier", level=0)
    document.add_paragraph("Level 3 Teaching Career Framework", style="Subtitle")
    document.add_paragraph(draft.candidate or "[Candidate name]")
    document.add_paragraph(f"Target: {fw.PROMOTION_ROUTE}")

    document.add_heading("1. Reflective Statement", level=1)
    _paragraphs(document, draft.statement)

    document.add_heading("2. Career Framework Overview", level=1)
    h = draft.overview_header
    document.add_paragraph(f"Target: {h['Target']}. L3 domains supported: {h['L3 domains supported']}. "
                           f"L3 domains required for UHD2: {h['L3 domains required for UHD2']}.")
    document.add_paragraph(h["Summary"])
    cols = ["Domain", "Highest supported level", "Strongest claim", "Evidence type", "Key evidence", "Source", "Status"]
    _table(document, [cols] + [[row.get(c, "") for c in cols] for row in draft.overview],
           widths=[3.2, 1.8, 2.8, 1.3, 3.6, 2.8, 1.6], font_size=8)

    document.add_heading("3. Selective Evidence Portfolio", level=1)
    fields = [("Domain", "domain"), ("Claimed level", "level"), ("Evidence type", "evidence_type"),
              ("Description", "description"), ("Why it supports the criterion", "why"), ("Date or period", "period"),
              ("Primary source", "primary_source"), ("Supporting sources", "supporting_sources")]
    for n, entry in enumerate(draft.portfolio, start=1):
        document.add_heading(f"E{n}. {entry['title']}", level=2)
        rows = [[label, entry.get(key) or "None"] for label, key in fields]
        if entry.get("passages"):
            rows.append(["Source passages", "\n".join(entry["passages"])])
        _table(document, rows, widths=[4.0, 12.4], font_size=9.5, header=False)
        for row in document.tables[-1].rows:
            row.cells[0].paragraphs[0].runs[0].bold = True

    if draft.appendix:
        document.add_heading("Appendix: Additional Evidence", level=1)
        cols = ["Domain", "Evidence", "Level", "Status", "Source"]
        _table(document, [cols] + [[r[c] for c in cols] for r in draft.appendix], widths=[2.8, 6.0, 1.6, 1.8, 4.2])
    if draft.source_list:
        document.add_heading("Sources", level=1)
        for line in draft.source_list:
            document.add_paragraph(line, style="List Bullet")
    if draft.gaps:
        document.add_heading("Evidence Still to Locate", level=1)
        document.add_paragraph("Working section for the candidate. Remove before submission.")
        for gap in draft.gaps:
            document.add_paragraph(gap, style="List Bullet")

    buffer = io.BytesIO()
    document.save(buffer)
    return buffer.getvalue()


def full_report_docx(store: Store) -> bytes:
    """Every non-rejected record grouped by primary domain, with exact source
    passages. An audit trail and working archive, not the dossier."""
    refs = References(store)
    items = _load(store)
    document = _document()
    document.add_heading("Full Evidence Report", level=0)
    document.add_paragraph(f"{store.get_setting('candidate_name') or '[Candidate name]'}. Generated {date.today().isoformat()}.")
    document.add_paragraph("Working archive of all evidence records that have not been rejected, including lower-level and "
                           "contextual evidence. This report is not the promotion dossier.")
    counts = {s: sum(i["status"] == s for i in items) for s in ("VERIFIED", "SUPPORTED", "POTENTIAL", "CONTEXT")}
    document.add_paragraph("Records: " + ", ".join(f"{k.title()} {v}" for k, v in counts.items()) + ".")
    for d, name in fw.DOMAINS.items():
        group = sorted((i for i in items if i["domains"][0] == d),
                       key=lambda i: (-fw.STATUS_RANK[i["status"]], -fw.LEVEL_RANK.get(i["level"], 0)))
        document.add_heading(f"{d}. {name}", level=1)
        if not group:
            document.add_paragraph("No records.")
            continue
        for item in group:
            document.add_heading(re.sub(r"\s*\[\.\.\.\]$", "", item["title"]), level=2)
            rows = [
                ["Level", item["level"]], ["Status", item["status"].title()], ["Classification confidence", item["confidence"]],
                ["Review", {"none": "No review needed", "pending": "Awaiting review", "accepted": "Accepted",
                            "edited": "Edited by candidate", "rejected": "Rejected"}.get(item["review_state"], item["review_state"])],
                ["Domains", "; ".join(fw.DOMAINS[x] for x in item["domains"])],
                ["Evidence type", ", ".join(item["evidence_types"]) or "None assigned"],
                ["Date or period", item["period"] or "Not stated"],
                ["Claim", item["claim"]], ["Reason", item["level_reason"]],
            ]
            if item["missing_evidence"]:
                rows.append(["Missing evidence", item["missing_evidence"].replace("\n", " ")])
            if item["notes"]:
                rows.append(["Notes", item["notes"].replace("\n", " ")])
            _table(document, rows, widths=[4.0, 12.4], font_size=9, header=False)
            for s in item["sources"]:
                label = "Primary" if s.role == "primary" else "Supporting"
                p = document.add_paragraph(style="List Bullet")
                p.add_run(f"{label}: {refs.ref(s)} (file: {s.filename}). ").bold = True
                p.add_run(re.sub(r"\s+", " ", s.text).strip())
    buffer = io.BytesIO()
    document.save(buffer)
    return buffer.getvalue()


def to_markdown(draft: DossierDraft) -> str:
    """Plain-text rendering used by the command line and the tests."""
    out = ["# Academic Career Progression Dossier", "Level 3 Teaching Career Framework", draft.candidate,
           f"Target: {fw.PROMOTION_ROUTE}", "", "## 1. Reflective Statement", draft.statement, "",
           "## 2. Career Framework Overview", draft.overview_header["Summary"]]
    for row in draft.overview:
        out.append("- " + " | ".join(str(v) for v in row.values()))
    out += ["", "## 3. Selective Evidence Portfolio"]
    for n, e in enumerate(draft.portfolio, start=1):
        out.append(f"### E{n}. {e['title']}")
        out.append(f"{e['domain']} | {e['level']} | {e['evidence_type']} | {e['period']}")
        out.append(e["description"])
        out.append(f"Why: {e['why']}")
        out.append(f"Primary source: {e['primary_source']}. Supporting sources: {e['supporting_sources'] or 'None'}.")
    if draft.gaps:
        out += ["", "## Evidence Still to Locate"] + [f"- {g}" for g in draft.gaps]
    return "\n".join(out)
