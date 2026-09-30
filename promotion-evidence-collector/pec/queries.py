"""Read-side queries for the dashboard, review inbox, matrix and search."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass

from . import framework as fw
from .db import Store


@dataclass
class Source:
    passage_id: int
    role: str
    self_description: bool
    document_id: int
    filename: str
    page_no: int
    page_label: str
    paged: bool
    text: str
    doc_date: str
    doc_date_source: str
    metadata_author: str
    genre: str
    copies: list[str]

    @property
    def location(self) -> str:
        return f"{self.page_label} {self.page_no}"

    @property
    def reference(self) -> str:
        # File metadata dates often reflect a template or a conversion, so
        # references cite only dates found in the document text.
        date = f", {self.doc_date}" if self.doc_date and self.doc_date_source == "document text" else ""
        return f"{self.filename}, {self.location}{date}"


def evidence(store: Store, where: str = "", params=()) -> list[dict]:
    rows = store.q(f"SELECT * FROM evidence {where}", params)
    items = []
    for r in rows:
        item = dict(r)
        item["domains"] = json.loads(item["domains"])
        item["evidence_types"] = json.loads(item["evidence_types"])
        item["review_reasons"] = json.loads(item["review_reasons"])
        item["suggested_links"] = json.loads(item.get("suggested_links") or "[]")
        items.append(item)
    return items


def sources_for(store: Store, evidence_id: int) -> list[Source]:
    rows = store.q(
        "SELECT es.role, es.self_description, p.id AS pid, p.page_no, p.text, d.id AS did, d.filename, d.page_label, "
        "d.paged, d.doc_date, d.doc_date_source, d.metadata_author, d.genre "
        "FROM evidence_sources es JOIN passages p ON p.id = es.passage_id JOIN documents d ON d.id = p.document_id "
        "WHERE es.evidence_id = ? ORDER BY CASE es.role WHEN 'primary' THEN 0 WHEN 'supporting' THEN 1 ELSE 2 END, d.filename",
        (evidence_id,),
    )
    out = []
    for r in rows:
        copies = [c["filename"] for c in store.q(
            "SELECT DISTINCT filename FROM document_copies WHERE document_id = ? AND filename != ?", (r["did"], r["filename"]))]
        out.append(Source(
            passage_id=r["pid"], role=r["role"], self_description=bool(r["self_description"]), document_id=r["did"],
            filename=r["filename"], page_no=r["page_no"], page_label=r["page_label"], paged=bool(r["paged"]),
            text=r["text"], doc_date=r["doc_date"], doc_date_source=r["doc_date_source"],
            metadata_author=r["metadata_author"], genre=r["genre"], copies=copies,
        ))
    return out


def counts(store: Store) -> dict:
    docs = store.one("SELECT COUNT(*) AS n FROM documents WHERE analyzed = 1 AND excluded = 0")["n"]
    pending = store.one("SELECT COUNT(*) AS n FROM documents WHERE analyzed = 0 AND excluded = 0")["n"]
    items = store.one("SELECT COUNT(*) AS n FROM evidence WHERE status != 'REJECT'")["n"]
    copies = store.one("SELECT COUNT(*) - (SELECT COUNT(*) FROM documents) AS n FROM document_copies")["n"]
    return {"documents": docs, "pending": pending, "evidence": items, "review": len(review_inbox(store)),
            "duplicate_copies": copies}


def domain_summary(store: Store) -> list[dict]:
    items = evidence(store, "WHERE status != 'REJECT'")
    summary = []
    for number, name in fw.DOMAINS.items():
        in_domain = [i for i in items if number in i["domains"]]
        supported_levels = [i["level"] for i in in_domain if i["status"] in ("VERIFIED", "SUPPORTED") and i["level"] != "Not assigned"]
        best_rank = max((fw.LEVEL_RANK[lv] for lv in supported_levels), default=0)
        best = sorted({lv for lv in supported_levels if fw.LEVEL_RANK[lv] == best_rank}) if best_rank else []
        verified_levels = [i["level"] for i in in_domain if i["status"] == "VERIFIED" and i["level"] != "Not assigned"]
        v_rank = max((fw.LEVEL_RANK[lv] for lv in verified_levels), default=0)
        summary.append({
            "domain": number, "name": name,
            "highest": " / ".join(best) if best else "None yet",
            "highest_verified": " / ".join(sorted({lv for lv in verified_levels if fw.LEVEL_RANK[lv] == v_rank})) if v_rank else "None yet",
            "verified": sum(i["status"] == "VERIFIED" for i in in_domain),
            "supported": sum(i["status"] == "SUPPORTED" for i in in_domain),
            "potential": sum(i["status"] == "POTENTIAL" for i in in_domain),
            "context": sum(i["status"] == "CONTEXT" for i in in_domain),
        })
    return summary


def requirement_check(store: Store) -> dict:
    items = evidence(store, "WHERE status IN ('VERIFIED', 'SUPPORTED')")
    results = []
    for key, rule in fw.REQUIREMENT_RULES.items():
        verified_domains, supported_domains = set(), set()
        for item in items:
            if not fw.level_at_least(item["level"], rule["min_level"]) or item["level"] == "Not assigned":
                continue
            for d in item["domains"]:
                if d in rule["domains"]:
                    (verified_domains if item["status"] == "VERIFIED" else supported_domains).add(d)
        needed = rule["min_domains"]
        if len(verified_domains) >= needed:
            outcome = "met"
        elif verified_domains or supported_domains:
            outcome = "partial"
        else:
            outcome = "none"
        results.append({
            "key": key, "label": rule["label"], "rule": rule["rule"], "outcome": outcome,
            "outcome_text": fw.REQUIREMENT_OUTCOMES[outcome],
            "verified_domains": sorted(verified_domains),
            "supported_only_domains": sorted(supported_domains - verified_domains),
        })
    l3 = next(r for r in results if r["key"] == "L3")
    n = len(l3["verified_domains"])
    statement = f"Current uploaded evidence supports Level 3 claims in {n} domain{'s' if n != 1 else ''}."
    if l3["supported_only_domains"]:
        m = len(l3["supported_only_domains"])
        statement += f" L3 evidence in {m} further domain{'s' if m != 1 else ''} is supported but not yet verified."
    return {"checks": results, "statement": statement}


def review_inbox(store: Store) -> list[dict]:
    inbox = []
    doc_decisions = store.decisions("document")
    for d in store.q("SELECT * FROM documents WHERE text_status = 'needs_visual_review' AND excluded = 0"):
        if str(d["id"]) not in doc_decisions:
            inbox.append({"kind": "document", "id": d["id"], "title": d["filename"],
                          "reasons": [fw.REVIEW_REASONS["unreadable"]], "detail": d["status_detail"]})
    rel_decisions = store.decisions("relation")
    for r in store.q(
        "SELECT r.*, a.filename AS fa, b.filename AS fb FROM document_relations r "
        "JOIN documents a ON a.id = r.doc_a JOIN documents b ON b.id = r.doc_b WHERE a.excluded = 0 AND b.excluded = 0"
    ):
        if str(r["id"]) not in rel_decisions:
            inbox.append({"kind": "relation", "id": r["id"], "title": f"{r['fa']} and {r['fb']}",
                          "reasons": [fw.REVIEW_REASONS["possible_duplicate"]],
                          "detail": f"Text similarity {r['similarity']:.0%}. Accept keeps {r['fa']} as the single logical source."})
    for item in evidence(store, "WHERE review_state = 'pending' AND status != 'REJECT'"):
        inbox.append({"kind": "evidence", "id": item["id"], "fingerprint": item["fingerprint"], "title": item["title"],
                      "reasons": [fw.REVIEW_REASONS.get(r, r) for r in item["review_reasons"]], "item": item})
    return inbox


def fmt_dates(item: dict) -> str:
    a, b = item.get("date_start") or "", item.get("date_end") or ""
    if a and b and a != b:
        return f"{a}-{b}"
    return a or b


def matrix(store: Store) -> list[dict]:
    rows = []
    for item in evidence(store, "ORDER BY id"):
        srcs = sources_for(store, item["id"])
        primary = next((s for s in srcs if s.role == "primary"), None)
        rows.append({
            "id": item["id"],
            "Domain": "; ".join(fw.domain_label(d, short=True) for d in item["domains"]),
            "Claim": item["title"],
            "Level": item["level"],
            "Evidence type": ", ".join(item["evidence_types"]),
            "Status": item["status"],
            "Confidence": item["confidence"],
            "Date": fmt_dates(item),
            "Primary source": primary.reference if primary else "",
            "Supporting sources": "; ".join(s.reference for s in srcs if s.role == "supporting"),
            "Missing evidence": item["missing_evidence"].replace("\n", " "),
        })
    return rows


def _snippet(text: str, term: str, width: int = 90) -> str:
    match = re.search(re.escape(term), text, re.I)
    if not match:
        return text[: width * 2]
    start = max(0, match.start() - width)
    end = min(len(text), match.end() + width)
    return ("[...] " if start else "") + re.sub(r"\s+", " ", text[start:end]) + (" [...]" if end < len(text) else "")


def search(store: Store, term: str) -> dict:
    term = term.strip()
    if not term:
        return {"evidence": [], "documents": []}
    like = f"%{term}%"
    ev = evidence(store, (
        "WHERE title LIKE ? OR claim LIKE ? OR notes LIKE ? OR missing_evidence LIKE ? OR level_reason LIKE ? "
        "OR id IN (SELECT es.evidence_id FROM evidence_sources es JOIN passages p ON p.id = es.passage_id WHERE p.text LIKE ?)"
    ), (like, like, like, like, like, like))
    docs = []
    for d in store.q(
        "SELECT d.id, d.filename, d.genre, d.doc_date, p.page_no, p.text, d.page_label FROM documents d "
        "JOIN pages p ON p.document_id = d.id WHERE d.excluded = 0 AND (p.text LIKE ? OR d.filename LIKE ?) "
        "ORDER BY d.filename, p.page_no", (like, like)
    ):
        docs.append({"document_id": d["id"], "filename": d["filename"], "genre": d["genre"],
                     "location": f"{d['page_label']} {d['page_no']}", "snippet": _snippet(d["text"], term)})
    return {"evidence": ev, "documents": docs}


def documents(store: Store) -> list[dict]:
    rows = []
    for d in store.q("SELECT * FROM documents ORDER BY filename"):
        copies = [c["filename"] for c in store.q("SELECT filename FROM document_copies WHERE document_id = ?", (d["id"],))]
        n_items = store.one(
            "SELECT COUNT(DISTINCT es.evidence_id) AS n FROM evidence_sources es JOIN passages p ON p.id = es.passage_id "
            "WHERE p.document_id = ?", (d["id"],))["n"]
        status = {"ok": "Text extracted", "needs_visual_review": "Needs visual review", "pending": "Not analyzed"}.get(d["text_status"], d["text_status"])
        if d["excluded"]:
            status = "Excluded"
        rows.append({
            "id": d["id"], "File": d["filename"], "Type": d["genre"], "Status": status,
            "Date": f"{d['doc_date']} ({d['doc_date_source']})" if d["doc_date"] else "",
            "Metadata author": d["metadata_author"], "Pages": d["page_count"], "Evidence items": n_items,
            "Duplicate copies": ", ".join(sorted(set(copies) - {d["filename"]})) or ("" if len(copies) <= 1 else f"{len(copies) - 1} identical upload(s)"),
            "Detail": d["status_detail"],
        })
    return rows
