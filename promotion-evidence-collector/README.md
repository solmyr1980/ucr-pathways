# Promotion Evidence Collector

A local application for preparing a promotion dossier under the University College Roosevelt (UCR) Teaching Career Framework, for the UD1 to UHD2 route with a Level 3 target (L3A Institutional Leader, L3B Scholarly Teacher).

## Workflow

1. Open the app.
2. Enter the candidate name in the sidebar.
3. Drop documents (PDF, DOCX, TXT, PPTX, XLSX) or give a folder path.
4. Click **Analyze**.
5. Work through the **Review inbox**. Each item has Accept, Edit and Reject.
6. Open **Dossier**, click **GENERATE DOSSIER**, edit the preview, and click **EXPORT TO DOCX**.

## Running

```
pip install -r requirements.txt
streamlit run app.py
```

Data is stored locally in `pec_data/` (SQLite database and copies of the original files). Set `PEC_DATA_DIR` to use another folder.

Command line:

```
python -m pec.cli samples ./sample_docs                        # fictional test corpus
python -m pec.cli analyze ./sample_docs --name "Sam Verhoeven"
python -m pec.cli dossier dossier.docx [--supported] [--gaps] [--sources] [--appendix]
python -m pec.cli report full_report.docx
python -m pytest tests
```

## Design

| Module | Role |
|---|---|
| `pec/extract.py` | Text and metadata extraction, SHA-256 hashing, near-duplicate sketches. Files without a usable text layer are marked "Needs visual review". |
| `pec/signals.py` | Deterministic signals: genre, dates, known roles and projects, domain vocabulary, institutional action and reach, inquiry components, disciplinary scholarship. |
| `pec/classifier/` | Extraction engines behind one interface (`base.py`). `rules.py` runs locally. `llm.py` is provider-neutral and ships with an Anthropic provider. `guardrails.py` applies the conservative rules to every engine's output. `registry.py` is the only place to register a new engine. |
| `pec/pipeline.py` | Ingest, analyze, merge candidates across documents, corroboration, contradiction checks, status assignment, review decisions. |
| `pec/queries.py` | Dashboard, requirement check, review inbox, evidence matrix, search. |
| `pec/dossier.py` | Reflective Statement, Career Framework Overview, Selective Evidence Portfolio, DOCX export, and the separate full evidence report. |
| `pec/framework.py` | Domains, levels, evidence types, statuses and the UHD2 requirement rules. |

### Conservative rules

- A title, a committee membership, an award, a course, or a publication never establishes L3A or L3B on its own.
- L3A requires a passage that shows institutional action and institutional reach. A claim that rests only on the candidate's CV or reflective statement is SUPPORTED, not VERIFIED, until an independent uploaded source corroborates it.
- L3B requires an educational question, method, evidence, findings, and use in practice. A proposal alone stays POTENTIAL.
- Disciplinary scholarship is CONTEXT.
- An engine's draft is discarded if its quoted passage cannot be found in the source document.
- A metadata author field does not establish authorship.
- Exact duplicate files are stored once. Near-duplicates go to the review inbox.

### Requirement rules

The UHD2 check in `pec/framework.py` (`REQUIREMENT_RULES`) is the application's working reading of the procedure. Check it against the current UCR procedure text.

### Optional LLM engine

Select "Claude via Anthropic API" in the sidebar after `pip install anthropic` and setting `ANTHROPIC_API_KEY`. This sends the extracted text of new documents to Anthropic. Original files stay local. To add another provider, implement `JSONProvider.complete_json` in `pec/classifier/llm.py` and register it in `pec/classifier/registry.py`.
