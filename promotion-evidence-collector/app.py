"""Promotion Evidence Collector: Streamlit interface.

Run with:  streamlit run app.py
"""

from __future__ import annotations

import html
from pathlib import Path

import pandas as pd
import streamlit as st

from pec import framework as fw
from pec import queries
from pec.classifier import ENGINES
from pec.db import Store
import json

from pec.dossier import (
    DossierDraft, DossierOptions, add_to_portfolio, dossier_docx, full_report_docx, generate,
    remove_from_portfolio, word_count,
)
from pec.extract import SUPPORTED_EXTENSIONS
from pec.pipeline import (
    EDITABLE, analyze, decide_document, decide_evidence, decide_relation, ingest, ingest_folder,
    link_evidence, rebuild, set_dossier_inclusion,
)

st.set_page_config(page_title="Promotion Evidence Collector", layout="wide")

st.markdown(
    """
<style>
.pec-card {border: 1px solid rgba(128,128,128,.35); border-radius: 8px; padding: 12px 14px; margin-bottom: 12px; min-height: 150px;}
.pec-card h4 {margin: 0 0 6px 0; font-size: 0.95rem; font-weight: 600;}
.pec-level {font-size: 1.6rem; font-weight: 700; margin: 2px 0 6px 0;}
.pec-counts {font-size: 0.9rem; line-height: 1.5;}
.pec-passage {border-left: 3px solid rgba(128,128,128,.6); padding: 6px 10px; margin: 4px 0 10px 0; white-space: pre-wrap; font-size: 0.9rem;}
.pec-reason {display: inline-block; border: 1px solid rgba(200,120,0,.6); border-radius: 4px; padding: 0 6px; margin: 0 4px 4px 0; font-size: 0.8rem;}
</style>
""",
    unsafe_allow_html=True,
)


@st.cache_resource
def get_store() -> Store:
    return Store()


store = get_store()
ss = st.session_state
ss.setdefault("uploader_key", 0)
ss.setdefault("editing", None)
ss.setdefault("last_run", None)


# ---------------------------------------------------------------------------
# Shared rendering


def render_sources(evidence_id: int, limit: int | None = None) -> None:
    sources = queries.sources_for(store, evidence_id)
    for src in sources[:limit] if limit else sources:
        label = {"primary": "Primary source", "supporting": "Supporting source", "duplicate copy": "Identical passage in another file"}[src.role]
        facts = [f"**{label}:** {src.filename}", src.location]
        if src.doc_date:
            facts.append(f"dated {src.doc_date} ({src.doc_date_source})")
        if src.metadata_author:
            facts.append(f"file metadata author: {src.metadata_author}")
        if src.self_description:
            facts.append("candidate's own account")
        st.markdown(" | ".join(facts))
        st.markdown(f"<div class='pec-passage'>{html.escape(src.text)}</div>", unsafe_allow_html=True)
        if src.copies:
            st.caption("Identical copies uploaded as: " + ", ".join(src.copies))
    if limit and len(sources) > limit:
        st.caption(f"{len(sources) - limit} further source passage(s) in the evidence matrix.")


def render_item(item: dict, show_sources: bool = True) -> None:
    domains = "; ".join(fw.domain_label(d) for d in item["domains"])
    st.markdown(f"**{item['title']}**")
    st.markdown(
        f"{domains}  \nLevel **{item['level']}** | Status **{item['status']}** | Confidence {item['confidence']}"
        + (f" | Evidence type {', '.join(item['evidence_types'])}" if item["evidence_types"] else "")
        + (f" | Date {queries.fmt_dates(item)}" if queries.fmt_dates(item) else "")
    )
    st.markdown(f"_Reason:_ {item['level_reason']}")
    if item["missing_evidence"]:
        st.markdown("_Missing evidence:_ " + item["missing_evidence"].replace("\n", " "))
    if item["notes"]:
        st.markdown("_Notes:_ " + item["notes"].replace("\n", " "))
    if show_sources:
        render_sources(item["id"])


def download_original(document_id: int, key: str) -> None:
    doc = store.one("SELECT filename, stored_path FROM documents WHERE id = ?", (document_id,))
    path = Path(doc["stored_path"])
    if path.exists():
        st.download_button(f"Open original: {doc['filename']}", path.read_bytes(), file_name=doc["filename"], key=key)


# ---------------------------------------------------------------------------
# Sidebar settings

with st.sidebar:
    st.header("Settings")
    name = st.text_input("Candidate name", value=store.get_setting("candidate_name"),
                         help="Used to link institutional documents to you. Documents are never assumed to be yours because you uploaded them.")
    if name != store.get_setting("candidate_name"):
        store.set_setting("candidate_name", name)
        rebuild(store)
        st.rerun()
    engine_keys = list(ENGINES)
    engine = st.selectbox("Analysis engine", engine_keys, format_func=ENGINES.get,
                          index=engine_keys.index(store.get_setting("engine", "rules")))
    store.set_setting("engine", engine)
    if engine != "rules":
        st.warning("This engine sends the extracted text of each new document to an external API. Original files stay on this computer.")
    st.caption(f"Data folder: {Path(store.path).parent}")
    with st.expander("Start over"):
        st.write("Deletes all documents, evidence, and review decisions from the local database.")
        if st.checkbox("I understand") and st.button("Delete everything"):
            store.reset()
            ss.last_run = None
            st.rerun()


# ---------------------------------------------------------------------------
# Header and intake

st.title("PROMOTION EVIDENCE COLLECTOR")
st.markdown(f"Target: **{fw.TARGET_POSITION}** | Career Framework target: **{fw.TARGET_FRAMEWORK_LEVEL}** (L3A Institutional Leader, L3B Scholarly Teacher)")

c = queries.counts(store)
m1, m2, m3 = st.columns(3)
m1.metric("Documents analyzed", c["documents"])
m2.metric("Evidence items found", c["evidence"])
m3.metric("Items needing review", c["review"])

with st.container(border=True):
    files = st.file_uploader(
        "Drop documents here (PDF, DOCX, TXT, PPTX, XLSX). Hundreds of files at once are fine.",
        type=[e.strip(".") for e in SUPPORTED_EXTENSIONS], accept_multiple_files=True, key=f"up{ss.uploader_key}",
    )
    with st.expander("Or import a folder from this computer"):
        folder = st.text_input("Folder path", placeholder="/Users/me/Documents/promotion")
    ready = bool(name.strip())
    if not ready:
        st.info("Enter the candidate name in the sidebar before analysis.")
    pending = c["pending"]
    label = "Analyze" if not pending or files or folder else f"Analyze ({pending} pending)"
    if st.button(label, type="primary", disabled=not ready):
        new = dup = 0
        for f in files or []:
            outcome, _ = ingest(store, f.name, f.getvalue())
            new += outcome != "duplicate"
            dup += outcome == "duplicate"
        if folder.strip():
            if Path(folder).expanduser().is_dir():
                counts = ingest_folder(store, Path(folder).expanduser())
                new += counts["new"] + counts["unsupported"]
                dup += counts["duplicate"]
            else:
                st.error("Folder not found.")
        bar = st.progress(0.0, text="Analyzing")
        try:
            stats = analyze(store, engine, lambda i, n, f: bar.progress(i / n, text=f"Analyzing {i} of {n}: {f}"))
        except Exception as exc:  # e.g. missing API credentials
            st.error(f"Analysis stopped: {exc}")
            stats = None
        bar.empty()
        if stats is not None:
            ss.last_run = {"new": new, "dup": dup, **stats}
        ss.uploader_key += 1
        st.rerun()
    if ss.last_run:
        r = ss.last_run
        msg = f"Last run: {r['new']} new file(s), {r['documents_analyzed']} analyzed."
        if r["dup"]:
            msg += f" {r['dup']} identical cop{'y' if r['dup'] == 1 else 'ies'} of already stored files recorded without creating duplicate evidence."
        st.success(msg)
        for err in r.get("errors", []):
            st.warning(err)

inbox = queries.review_inbox(store)
tabs = st.tabs(["Dashboard", f"Review inbox ({len(inbox)})", "Evidence matrix", "Documents", "Search", "Dossier"])


# ---------------------------------------------------------------------------
# Dashboard

with tabs[0]:
    summary = queries.domain_summary(store)
    cols = st.columns(3)
    for i, s in enumerate(summary):
        with cols[i % 3]:
            st.markdown(
                f"<div class='pec-card'><h4>{html.escape(s['name'])}</h4>"
                f"<div class='pec-level'>{s['highest'] if s['highest'] != 'None yet' else 'No level yet'}</div>"
                f"<div class='pec-counts'>Verified: {s['verified']}<br>Supported: {s['supported']}<br>Potential: {s['potential']}</div></div>",
                unsafe_allow_html=True,
            )
    st.caption("Highest supported level counts VERIFIED and SUPPORTED items. Context items are not counted.")

    st.subheader(f"Promotion requirement check ({fw.TARGET_POSITION})")
    check = queries.requirement_check(store)
    for r in check["checks"]:
        with st.container(border=True):
            st.markdown(f"**{r['label']}**: {r['outcome_text']}")
            detail = f"Rule applied: {r['rule']}"
            if r["verified_domains"]:
                detail += " Verified in domains " + ", ".join(map(str, r["verified_domains"])) + "."
            if r["supported_only_domains"]:
                detail += " Supported only in domains " + ", ".join(map(str, r["supported_only_domains"])) + "."
            st.caption(detail)
    st.markdown(f"**{check['statement']}**")
    st.caption("This check describes the uploaded evidence. The formal promotion decision belongs to UCR. "
               "The requirement rules are set in pec/framework.py and should be checked against the current UCR procedure.")


# ---------------------------------------------------------------------------
# Review inbox


def evidence_edit_form(item: dict) -> None:
    with st.form(f"edit{item['id']}"):
        title = st.text_input("Title", item["title"])
        claim = st.text_area("Claim", item["claim"], height=80)
        domains = st.multiselect("Domains", list(fw.DOMAINS), item["domains"], format_func=fw.domain_label)
        a, b, cc = st.columns(3)
        level = a.selectbox("Level", fw.LEVELS, fw.LEVELS.index(item["level"]))
        status = b.selectbox("Status", fw.STATUSES, fw.STATUSES.index(item["status"]))
        confidence = cc.selectbox("Confidence", fw.CONFIDENCES, fw.CONFIDENCES.index(item["confidence"]))
        types = st.multiselect("Evidence types", list(fw.EVIDENCE_TYPES), item["evidence_types"])
        d1, d2 = st.columns(2)
        date_start = d1.text_input("Start", item["date_start"])
        date_end = d2.text_input("End", item["date_end"])
        missing = st.text_area("Missing evidence", item["missing_evidence"], height=68)
        notes = st.text_area("Notes", item["notes"], height=68)
        others = queries.evidence(store, "WHERE id != ? AND status != 'REJECT' ORDER BY title", (item["id"],))
        suggested = [o for fp in item["suggested_links"] for o in others if o["fingerprint"] == fp]
        options = [None] + suggested + [o for o in others if o not in suggested]
        link = st.selectbox(
            "Corroborated by another evidence item (optional)", options,
            format_func=lambda o: "No link" if o is None else (("Suggested: " if o in suggested else "") + f"{o['title']} [{o['status']}]"),
            help="Merges the sources of both items. Status and confidence are then recalculated from the combined sources.",
        )
        save, cancel = st.columns(2)
        if save.form_submit_button("Save", type="primary"):
            if link is not None:
                link_evidence(store, item["fingerprint"], link["fingerprint"])
            else:
                decide_evidence(store, item["fingerprint"], "edit", {
                    "title": title, "claim": claim, "domains": domains or item["domains"], "level": level,
                    "status": status, "confidence": confidence, "evidence_types": types, "date_start": date_start,
                    "date_end": date_end, "missing_evidence": missing, "notes": notes,
                    "level_reason": item["level_reason"] + ("" if (level, status) == (item["level"], item["status"]) else " Classification edited by the candidate."),
                })
            ss.editing = None
            st.rerun()
        if cancel.form_submit_button("Cancel"):
            ss.editing = None
            st.rerun()


with tabs[1]:
    if not inbox:
        st.info("Nothing needs review.")
    evidence_entries = [e for e in inbox if e["kind"] == "evidence"]
    if evidence_entries:
        b1, b2, _ = st.columns([1, 1, 4])
        if b1.button("Select all"):
            for e in evidence_entries:
                ss[f"sel{e['id']}"] = True
        if b2.button("Accept selected"):
            for e in evidence_entries:
                if ss.get(f"sel{e['id']}"):
                    decide_evidence(store, e["fingerprint"], "accept")
                    ss[f"sel{e['id']}"] = False
            st.rerun()
    for entry in inbox:
        with st.container(border=True):
            reasons = "".join(f"<span class='pec-reason'>{html.escape(r)}</span>" for r in entry["reasons"])
            if entry["kind"] == "evidence":
                item = entry["item"]
                top = st.columns([0.05, 0.95])
                top[0].checkbox("Select", key=f"sel{item['id']}", label_visibility="collapsed")
                with top[1]:
                    st.markdown(reasons, unsafe_allow_html=True)
                    render_item(item, show_sources=False)
                    render_sources(item["id"], limit=2)
                a, e, r, _ = st.columns([1, 1, 1, 5])
                if a.button("Accept", key=f"acc{item['id']}"):
                    decide_evidence(store, item["fingerprint"], "accept")
                    st.rerun()
                if e.button("Edit", key=f"edt{item['id']}"):
                    ss.editing = ("evidence", item["id"])
                if r.button("Reject", key=f"rej{item['id']}"):
                    decide_evidence(store, item["fingerprint"], "reject")
                    st.rerun()
                if ss.editing == ("evidence", item["id"]):
                    evidence_edit_form(item)
            elif entry["kind"] == "document":
                st.markdown(reasons, unsafe_allow_html=True)
                st.markdown(f"**{entry['title']}**: {entry['detail']}")
                download_original(entry["id"], key=f"dl{entry['id']}")
                st.caption("Accept keeps the file on record as needing visual review. Edit lets you type or paste its text for analysis. Reject excludes it.")
                a, e, r, _ = st.columns([1, 1, 1, 5])
                if a.button("Accept", key=f"dacc{entry['id']}"):
                    decide_document(store, entry["id"], "accept")
                    st.rerun()
                if e.button("Edit", key=f"dedt{entry['id']}"):
                    ss.editing = ("document", entry["id"])
                if r.button("Reject", key=f"drej{entry['id']}"):
                    decide_document(store, entry["id"], "reject")
                    rebuild(store)
                    st.rerun()
                if ss.editing == ("document", entry["id"]):
                    with st.form(f"dform{entry['id']}"):
                        text = st.text_area("Text of the document", height=200)
                        if st.form_submit_button("Save and analyze", type="primary") and text.strip():
                            decide_document(store, entry["id"], "edit", text)
                            analyze(store, "rules")
                            ss.editing = None
                            st.rerun()
            else:
                st.markdown(reasons, unsafe_allow_html=True)
                st.markdown(f"**{entry['title']}**: {entry['detail']}")
                st.caption("Accept treats the files as the same document and keeps one logical source. Reject keeps both as separate documents. Edit lets you choose which file to keep.")
                a, e, r, _ = st.columns([1, 1, 1, 5])
                if a.button("Accept", key=f"racc{entry['id']}"):
                    decide_relation(store, entry["id"], "accept")
                    st.rerun()
                if e.button("Edit", key=f"redt{entry['id']}"):
                    ss.editing = ("relation", entry["id"])
                if r.button("Reject", key=f"rrej{entry['id']}"):
                    decide_relation(store, entry["id"], "reject")
                    st.rerun()
                if ss.editing == ("relation", entry["id"]):
                    rel = store.one(
                        "SELECT r.*, a.filename AS fa, b.filename AS fb FROM document_relations r "
                        "JOIN documents a ON a.id = r.doc_a JOIN documents b ON b.id = r.doc_b WHERE r.id = ?", (entry["id"],))
                    keep = st.radio("Keep", [rel["fa"], rel["fb"]], key=f"keep{entry['id']}")
                    if st.button("Save", key=f"rsave{entry['id']}"):
                        if keep == rel["fb"]:
                            with store.tx() as cx:
                                cx.execute("UPDATE document_relations SET doc_a = ?, doc_b = ? WHERE id = ?",
                                           (rel["doc_b"], rel["doc_a"], rel["id"]))
                        decide_relation(store, entry["id"], "accept")
                        ss.editing = None
                        st.rerun()


# ---------------------------------------------------------------------------
# Evidence matrix

with tabs[2]:
    rows = queries.matrix(store)
    if not rows:
        st.info("No evidence yet. Drop documents above and click Analyze.")
    else:
        df = pd.DataFrame(rows)
        f1, f2, f3, f4 = st.columns([2, 2, 2, 3])
        dom = f1.multiselect("Domain", list(fw.DOMAINS), format_func=lambda d: fw.domain_label(d, short=True))
        sts = f2.multiselect("Status", fw.STATUSES, default=[s for s in fw.STATUSES if s != "REJECT"])
        lvl = f3.multiselect("Level", fw.LEVELS)
        txt = f4.text_input("Filter text")
        view = df
        if dom:
            view = view[view["Domain"].apply(lambda v: any(v.startswith(f"{d}.") or f"; {d}." in v for d in dom))]
        if sts:
            view = view[view["Status"].isin(sts)]
        if lvl:
            view = view[view["Level"].isin(lvl)]
        if txt:
            view = view[view.apply(lambda r: txt.lower() in " ".join(map(str, r.values)).lower(), axis=1)]
        st.caption(f"{len(view)} of {len(df)} items. Click a column header to sort. Select a row to see where the evidence came from.")
        event = st.dataframe(view.drop(columns=["id"]), width="stretch", hide_index=True,
                             on_select="rerun", selection_mode="single-row", key="matrix")
        st.download_button("Download matrix (CSV)", view.drop(columns=["id"]).to_csv(index=False).encode(), "evidence_matrix.csv")
        selected = event.selection.rows if event and event.selection else []
        if selected:
            item_id = int(view.iloc[selected[0]]["id"])
            item = queries.evidence(store, "WHERE id = ?", (item_id,))[0]
            with st.container(border=True):
                render_item(item)
                if item["status"] == "POTENTIAL":
                    inc = st.checkbox("Include this potential item in the dossier", value=bool(item["include_in_dossier"]), key=f"inc{item_id}")
                    if inc != bool(item["include_in_dossier"]):
                        set_dossier_inclusion(store, item["fingerprint"], inc)
                        st.rerun()
                a, e, r, _ = st.columns([1, 1, 1, 5])
                if a.button("Accept", key=f"macc{item_id}"):
                    decide_evidence(store, item["fingerprint"], "accept")
                    st.rerun()
                if e.button("Edit", key=f"medt{item_id}"):
                    ss.editing = ("matrix", item_id)
                if r.button("Reject", key=f"mrej{item_id}"):
                    decide_evidence(store, item["fingerprint"], "reject")
                    st.rerun()
                if ss.editing == ("matrix", item_id):
                    evidence_edit_form(item)
                for src_doc in {s.document_id for s in queries.sources_for(store, item_id)}:
                    download_original(src_doc, key=f"mdl{item_id}_{src_doc}")


# ---------------------------------------------------------------------------
# Documents

with tabs[3]:
    docs = queries.documents(store)
    if not docs:
        st.info("No documents yet.")
    else:
        ddf = pd.DataFrame(docs)
        event = st.dataframe(ddf.drop(columns=["id"]), width="stretch", hide_index=True,
                             on_select="rerun", selection_mode="single-row", key="docs")
        selected = event.selection.rows if event and event.selection else []
        if selected:
            doc_id = int(ddf.iloc[selected[0]]["id"])
            download_original(doc_id, key=f"ddl{doc_id}")
            for page in store.q("SELECT page_no, text FROM pages WHERE document_id = ? ORDER BY page_no", (doc_id,)):
                with st.expander(f"{ddf.iloc[selected[0]]['File']}: part {page['page_no']}"):
                    st.text(page["text"] or "(no text)")


# ---------------------------------------------------------------------------
# Search

with tabs[4]:
    term = st.text_input("Search evidence and documents", placeholder="Head Tutor, curriculum, assessment, NVAO, mentoring")
    if term:
        results = queries.search(store, term)
        st.markdown(f"**Evidence records ({len(results['evidence'])})**")
        for item in results["evidence"]:
            with st.expander(f"{item['title']} | {item['level']} | {item['status']}"):
                render_item(item)
        st.markdown(f"**Source documents ({len(results['documents'])})**")
        for d in results["documents"]:
            st.markdown(f"{d['filename']}, {d['location']} ({d['genre']})")
            st.markdown(f"<div class='pec-passage'>{html.escape(d['snippet'])}</div>", unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Dossier


def load_draft() -> DossierDraft | None:
    raw = store.get_setting("dossier_draft")
    return DossierDraft.from_dict(json.loads(raw)) if raw else None


def save_draft(draft: DossierDraft) -> None:
    store.set_setting("dossier_draft", json.dumps(draft.to_dict()))


with tabs[5]:
    st.markdown(f"Route: **{fw.PROMOTION_ROUTE}** | Career Framework target: **Level 3** (L3A and/or L3B)")
    o1, o2, o3, o4 = st.columns(4)
    opt_supported = o1.checkbox("Include supported evidence")
    opt_gaps = o2.checkbox("Include evidence gaps")
    opt_sources = o3.checkbox("Include full source list")
    opt_appendix = o4.checkbox("Include appendix of additional evidence")
    draft = load_draft()
    if st.button("GENERATE DOSSIER", type="primary"):
        draft = generate(store, DossierOptions(include_supported=opt_supported, include_gaps=opt_gaps,
                                               include_source_list=opt_sources, include_appendix=opt_appendix))
        save_draft(draft)
        st.rerun()
    if draft is None:
        st.caption("The concise dossier uses verified evidence only. Generating again replaces earlier edits.")
    else:
        st.caption(f"Draft generated {draft.generated}. Edits are saved automatically. Generating again replaces them.")
        t1, t2, t3 = st.tabs(["Reflective Statement", "Framework Overview", "Evidence Portfolio"])
        with t1:
            text = st.text_area("Reflective Statement", draft.statement, height=520, label_visibility="collapsed")
            st.caption(f"{word_count(text)} words. Target 600 to 900. Replace or delete the bracketed prompts before export.")
            if text != draft.statement:
                draft.statement = text
                save_draft(draft)
        with t2:
            h = draft.overview_header
            st.markdown(f"Target: **{h['Target']}** | L3 domains supported: **{h['L3 domains supported']}** | "
                        f"L3 domains required for UHD2: **{h['L3 domains required for UHD2']}**")
            st.markdown(h["Summary"])
            edited = st.data_editor(pd.DataFrame(draft.overview), hide_index=True, width="stretch",
                                    disabled=["Domain"], key="overview_editor")
            rows = edited.fillna("").to_dict("records")
            if rows != draft.overview:
                draft.overview = rows
                save_draft(draft)
        with t3:
            st.caption(f"{len(draft.portfolio)} items. The portfolio should normally hold about 8 to 15 items.")
            changed = False
            for n, entry in enumerate(draft.portfolio, start=1):
                with st.expander(f"E{n}. {entry['title']} ({entry['level']})"):
                    for field_name, label, tall in (("title", "Title", False), ("description", "Brief description", True),
                                                    ("why", "Why it supports the criterion", True), ("period", "Date or period", False),
                                                    ("primary_source", "Primary source", False), ("supporting_sources", "Supporting sources", False)):
                        widget = st.text_area if tall else st.text_input
                        value = widget(label, entry[field_name], key=f"pf_{entry['fingerprint']}_{field_name}")
                        if value != entry[field_name]:
                            entry[field_name] = value
                            changed = True
                    st.caption(f"Domain: {entry['domain']}. Evidence type: {entry['evidence_type']}.")
                    if st.button("Remove from portfolio", key=f"rm_{entry['fingerprint']}"):
                        save_draft(remove_from_portfolio(draft, entry["fingerprint"]))
                        st.rerun()
            if changed:
                save_draft(draft)
            in_portfolio = {p["fingerprint"] for p in draft.portfolio}
            candidates = [i for i in queries.evidence(store, "WHERE status != 'REJECT' ORDER BY title")
                          if i["fingerprint"] not in in_portfolio]
            if candidates:
                a1, a2 = st.columns([4, 1])
                pick = a1.selectbox("Add an evidence item from the database", candidates,
                                    format_func=lambda i: f"{i['title']} ({i['level']}, {i['status'].title()})")
                if a2.button("Add", width="stretch"):
                    save_draft(add_to_portfolio(store, draft, pick["fingerprint"]))
                    st.rerun()
            if draft.gaps:
                gaps = st.text_area("Evidence Still to Locate (working copy only)", "\n".join(draft.gaps), height=160)
                if gaps.splitlines() != draft.gaps:
                    draft.gaps = [g for g in gaps.splitlines() if g.strip()]
                    save_draft(draft)
        slug = (draft.candidate or "candidate").replace(" ", "_")
        e1, e2 = st.columns(2)
        e1.download_button("EXPORT TO DOCX", dossier_docx(draft), file_name=f"Career_Progression_Dossier_{slug}.docx",
                           mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document", type="primary")
        e2.download_button("EXPORT FULL EVIDENCE REPORT", full_report_docx(store), file_name=f"Full_Evidence_Report_{slug}.docx",
                           mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
