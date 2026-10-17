# Comprehensive counselor re-audit: preparation and findings

Date: 17 October 2026. Baseline: `bb2c4b5bd41e060b501448e057757f661ef22d4e` on `main`.

Status: preparatory assignment completed. No counselor comparison, decision, curriculum, programme description, schema, validator, application or presentation setting has been changed. The six-case re-audit has not begun. The earlier alignment pilot is a separate historical exercise.

Deliverables: [operational protocol](counselor-comprehensive-reaudit-protocol.md), this inventory and architecture diagnosis, the pilot below, and an initial [review register](../../data/counselor/qc/comprehensive-reaudit.json). Counts come from the baseline files, not historical report summaries. Inventory inspection is not stage approval.

## Current corpus

| Item | Baseline count/status |
|---|---:|
| Permanent normalized targets | 460 |
| In-scope targets and active canonical records | 438; exact ID sets agree |
| Comparisons | 391 |
| Exceptions | 47 |
| Unresolved external programmes | 32 |
| No-defensible-UCR-match exceptions | 15 |
| Pending UCR assessments / registry exceptions | 0 / 0 |
| UCR alternatives | 967: 39 comparisons with one, 128 with two, 224 with three |
| Root production decision files | 433; all v2 |
| Canonical schema version | All 438 use 2.0 |
| Presentation modes | 302 normal; 89 caution; 47 external-only |
| Registry programme-interest rows | 22,259 |
| Current review indexes | 438 programmes; 21,212 linked interest rows |
| Final production discovery indexes | Absent, as required before finalisation |

The five early canonical records CP001–CP005 have no root decision file. Regression fixtures for CP004/CP005 are not active production inputs. These five records are still in scope; any later repair must acknowledge its actual input path and cannot claim a root v2 replay. There are no orphaned active decisions or missing in-scope canonical records.

Twenty-two targets are excluded by the existing scope rule: 18 joint/double/dual targets and four standard targets without current production eligibility. Archived decision/comparison pairs exist for CP134, CP199 and CP333 under `data/counselor/withdrawn/`; retain them as evidence, not active corpus entries. CP333 also has an unresolved combined-study-load question in historical remediation; it does not add a 33rd unresolved active exception.

The current enriched workbook was retrieved in the checkout, opened successfully and inspected: 151 data rows, 26 columns, including enriched profiles, topics/methods, prerequisites and planned terms. Its blob is `c2bcc3b63ec7831fd0f7b8ddfb32de1260521655`. This preparation does not independently validate any selected course or schedule.

## Existing reviews and what survives

The historical labels “stage 1” and “stage 2” below refer to earlier projects, not the six stages of the new protocol.

| Existing evidence | Recorded extent and result | Reuse and limitation |
|---|---|---|
| `qc/stage1-completeness-exceptions.json`; `docs/qc/counselor-completeness-exceptions-stage1.md` | 159 audited populations: 140 exceptions and 19 scope exclusions; no pending entries | Identity/curriculum findings, source references and initial failure mechanisms. Its 441-record baseline is historical. |
| `qc/stage1-remediation.json`; matching Markdown report | 97 processed cases: 64 resolved, 24 partially resolved, nine corrected with research pending | Preserve implemented factual/registry corrections and specific open questions. Thirty-three historical cases with remaining research comprise 32 active unresolved exceptions plus withdrawn CP333. |
| `qc/stage2-ucr-assessment.json`; matching report | 50 assessments: 35 comparisons and 15 no-match decisions; includes the first ten and subsequent fixed queue of 40 | Reuse research, concepts and explicit choices after verification. Its corpus totals precede later no-match reversals. |
| `qc/stage2-ucr-quality-control.json`; matching report | All ten earlier UCR assessments reviewed; none remain in that queue | Course/interest/feasibility findings are useful evidence, not full audience-quality approval. |
| `qc/stage2-preexisting-no-match-review.json`; matching report | All 55 reviewed: 54 replaced by comparisons, one retained no-match | Preserve candidate/course evidence and reasoned decisions. Do not presume either reversals or the retained judgment correct. Completion metadata records that automation as disabled; no schedule is created or changed here. |
| `docs/qc/counselor-comparison-qc-pilot-2026-10-17.md` | Six comparisons, 12 alternatives; alignment/coherence diagnostic | Keep unchanged. It did not include African Studies or cover the new six-stage scope. |
| `docs/qc/counselor-comparison-qc-follow-up-2026-10-17.md`; `qc/alignment-review-2026-10-17.json` | Five repaired pairs: CP019, CP035, CP330, CP435, CP459. Nine cases/21 programmes/504 placements received recorded independent workbook feasibility checks | Reuse exact corrected alignments/rationales and check evidence. Not fresh certification of every external curriculum or the rendered experience. Four external-content questions remain. |
| `docs/quality-control/2026-09-11-audit.md` | Earlier project audit | Historical context, not approval of the current counselor corpus. |

Four detailed-content follow-ups remain in the alignment register: CP004 `psy-ethics` and `psy-science-practical`, CP009 `b3-ethics`, CP035 `bio2-philosophy`. Their rows were retained because material error had not been established; detailed external-syllabus certification was explicitly withheld. Carry those questions forward without calling them confirmed errors or silently closing them.

The active unresolved IDs are listed below. These figures are stored component totals, not fresh curricular judgments. Five unresolved records already total 180 EC (CP266, CP309, CP322, CP404, CP416); credit closure cannot resolve cohort, prerequisite or authority conflicts.

| ID | Stored external programme | Stored EC |
|---|---|---:|
| cp-000040 | German Language and Culture | 165 |
| cp-000051 | Human Neuroscience | 164 |
| cp-000099 | Health and Life Sciences (Gezondheid en Leven) | 90 |
| cp-000100 | Health Sciences (Gezondheidswetenschappen) | 150 |
| cp-000149 | General Cultural Studies (Algemene Cultuurwetenschappen) | 0 |
| cp-000250 | Bachelor Clinical Technology | 181 |
| cp-000263 | Bachelor Architecture, Urbanism and Building Sciences | 175 |
| cp-000266 | Bachelor Industrial Design | 180 |
| cp-000275 | Bachelor Theology | 60 |
| cp-000277 | African Studies | 175 |
| cp-000278 | Archaeology | 90 |
| cp-000283 | Chinese Studies | 190 |
| cp-000284 | Criminology | 120 |
| cp-000286 | Cybersecurity & Cybercrime | 150 |
| cp-000288 | German Language and Culture | 175 |
| cp-000289 | Economics & Society | 120 |
| cp-000290 | English Language and Culture | 120 |
| cp-000293 | Tax Law | 120 |
| cp-000295 | Medicine | 120 |
| cp-000300 | Italian Language and Culture | 170 |
| cp-000306 | Middle Eastern Studies | 175 |
| cp-000309 | Dutch Studies | 180 |
| cp-000311 | Notarial Law | 120 |
| cp-000312 | Ancient Near Eastern Studies | 155 |
| cp-000314 | Political Science | 60 |
| cp-000317 | Law | 120 |
| cp-000318 | Religious Studies | 60 |
| cp-000322 | South and Southeast Asian Studies | 180 |
| cp-000324 | Linguistics (Taalwetenschap) | 175 |
| cp-000364 | Politiek, cultuur en religie | 172.5 |
| cp-000404 | Hebrew Language and Culture (Hebreeuwse taal en cultuur) | 180 |
| cp-000416 | Musicology (Muziekwetenschap) | 180 |

## Reusable infrastructure and its limits

- `data/registry/` provides stable identities, production order, provenance crosswalks, resolution decisions/sources and complete target-linked interests. The guarded corrections ledger and withdrawn archives preserve earlier identity decisions.
- `data/counselor/decisions/` holds explicit academic inputs. Existing v2 compilation and regression fixtures can reproduce mechanical structure; they do not independently decide course relevance, curriculum validity or communication quality.
- `data/schema/counselor-comparison.schema.json`, `counselor-final-methodology.schema.json`, `counselor-exception.schema.json` and the shared example schema describe current contracts. Runtime checks live in `scripts/validate-counselor-{comparison,structural-rules,final-rules}.mjs`; `npm run validate:counselor` orchestrates them through temporary storage and the optional-research handling.
- The validators check identity, coverage, references, counts, traceability structure and declared methodology. They do not inspect official sources or independently read workbook prerequisites/term availability, nor establish that a rationale or programme description is true.
- `presentation-overrides.json` separates presentation from academic status. Normal/caution are historical provenance categories, not quality judgments; the generic caution message must not stand in for a case-specific verified limitation.
- `review-programmes.json` / `review-interests.json`, their builder/checker, Shiny tests and deployment bundle checker remain reusable. `pilot/shiny/data/courses/*.json` supplies clickable UCR descriptions; its correspondence with workbook evidence also needs review when material.
- The repair Action accepts one active root decision repair with its regenerated canonical file per commit. A two-case review batch therefore need not be one two-decision commit. No new compiler or audit service is needed.

Preparation checks: `npm run validate:counselor` passed across the unchanged corpus; `npm run validate:counselor-review` confirmed the 438-programme/21,212-interest indexes. These are mechanical baseline results, not completed re-audit findings.

## User-facing/internal-content diagnosis

The root failure is that some required evidence fields also serve as display prose. The exception schema/validator requires nonempty `reason`, `curriculumContext`, `academicYear` and `sourceNotes`, but imposes no audience boundary. The compiler preserves research text, and the renderer displays it. Rewriting isolated records would leave the mechanism intact.

| Current field or source | Actual display path | Diagnosis and proposed handling |
|---|---|---|
| Discovery `displayName`, institution, matched interest text | `render_result_cards`; English search indexes | Intended audience content. Review exact target naming and interest claims; preserve provenance separately. |
| `comparator.name`, institution, `primarySourceUrl`; `programmes[].label` | Page headings, comparator table header/link; shared `visible_label` | Intended labels/sources. `visible_label` uses canonical comparator names rather than the registry English display name, and can generate generic labels. Check these paths, not only search names. |
| `comparator.route` | Comparison summary and exception pathway line | Material pathway choice should remain visible in readable form. Keep route-selection reasoning internal. |
| `academicRationale.alternatives[].concept` | `render_comparison_summary` | Existing field already supplies descriptions. Review and retain good text; do not create a competing concept field. |
| Block titles; comparison-cell `text`, EC, emphasis | `render_compare_table` | Intended academic display. Preserve verified course/component names, gaps and credits. |
| `blocks[].rows[].cells.*.note` | Beneath comparison cells | Mixed audience/evidence role. CP019 includes “First-listed Culture and Economics focus-area course.” Review case notes; route-selection bookkeeping is not a curriculum explanation. |
| `notes[].text` where placement is absent or `comparison` | Shared `render_comparison_notes` | Audience-intended explanatory notes. The permissive missing-placement fallback is part of the surface to check. Preserve warranted limitations. |
| `exception.reason` | Paragraph under “About this programme” | Contains academic production reasoning as well as potentially useful reasons; CP119 explains concept testing and assembly. Preserve the decision evidence and supply a concise audience explanation separately. |
| `exception.curriculumContext` | Same exception summary | Often duplicates long reconstruction logs. Retain internally; do not render as a programme description. |
| `comparator.academicYear` | Exception “Curriculum context” line | Currently unrestricted prose; e.g. CP278 combines year, entrant status, known EC and unresolved requirements. Display a clean year/cohort label and a separate material limitation. |
| `comparator.components[].name`, EC and `.note` | Exception/external-only component table | Notes include internal catalogue/cohort evidence. A diagnostic list may total 190 EC (CP283) or only 175 EC (CP277); do not present it as a complete certified pathway. Preserve supported/diagnostic evidence internally. |
| `comparator.sourceNotes` | Exception/external-only transparency panel | Direct research-log exposure. CP277/278/283/306 are concrete examples. Keep URLs accessible with ordinary link labels; preserve full reconciliation internally. |
| Presentation mode/message | Caution banner or withheld-comparison explanation | Separate presentation concern. Do not use it to overwrite an academic decision or house the entire academic description. |
| Course-description JSON, selected by code | `course_description_dialog` | User-facing course evidence; inspect accuracy and fallback message, not just canonical record wording. |

`render_exception(..., presentation_only=TRUE)` suppresses `exception.reason` and `curriculumContext` but still renders academicYear, component notes and sourceNotes. Thus hiding UCR columns does not solve disclosure. Ordinary comparison pages do not currently render comparator sourceNotes/academicYear directly; they expose concepts, cell notes and comparison notes instead. This distinction matters when estimating migration work.

Content counts identify scale, not defect prevalence: 408 records have component notes; 365 have comparison-cell notes; 390 have displayed comparison notes. Each needs audience review where it reaches a surface. The counts do not imply every note is defective.

### Proposed remedy: review before implementation

Keep internal research where it is; define explicit audience fields and an allowlist for rendering. Reuse existing intended display fields (labels, concepts, comparison notes) after review. For mixed exception/metadata/component notes, add the smallest explicit audience contract to the existing decision → canonical pipeline, provisionally a canonical `audience` object with programme description, limitation/explanation, clean curriculum label and component-note mapping by stable ID. The exact field names and requiredness remain a design choice, not an implemented contract. Research detail remains in the existing internal fields and QC evidence.

The renderer should use approved audience fields and ordinary academic facts only. It must never fall back from missing audience copy to `sourceNotes`, `curriculumContext`, mixed `reason` or arbitrary notes. A missing field should yield a neutral status-specific message or omit optional prose, while preserving any material academic limitation in approved copy. An unresolved diagnostic list should be withheld or explicitly marked incomplete/uncertified; do not silently call all its entries verified requirements. No generative rewriting at runtime.

This is a targeted extension of existing records/compiler/renderers, not a second comparison corpus or a description sidecar in presentation overrides. A later contract change must cover decision inputs, compiler, schemas/manual validators, repair workflow, app/shared helpers, fixtures and deployment bundle. Student concepts already have an established canonical display role and should remain intact.

## Six-case pilot

| Pair / case | Current state | Why it is included |
|---|---|---|
| 1 — CP277, Leiden African Studies | External unresolved; 175 EC; external-only | Mandatory case. Tests cohort separation, duplicated Swahili, unresolved required credits, preservation of corrected evidence and severe internal-note exposure. |
| 1 — CP119, VU Theology and Religious Studies | No defensible match; 180 EC; external-only | Tests independent reconsideration of a retained no-match, an exact part-time/route identity and readable explanation of substantive coverage gaps. Earlier ten-case QC is evidence, not approval. |
| 2 — CP001, Erasmus Public Administration | Original comparison; two alternatives; normal | Positive control: prior alignment review found no material error. Tests preservation of sound work and the early-record path without a root decision. |
| 2 — CP019, Erasmus Arts and Culture Studies | Recently repaired comparison; three alternatives; normal | Tests preservation of corrected matches, bounded route choices, internship/thesis distinctions, relative academic emphasis and audience quality beyond mechanical validity. |
| 3 — CP035, Radboud Biology | Recently repaired comparison; three alternatives; normal | Natural-science breadth, ecological versus biomedical purposes, explicitly provisional prospective curriculum and the still-open ethics-content question. Tests source-year handling and downstream restraint. |
| 3 — CP330, Twente Mechanical Engineering | Reassessment comparison; one alternative; caution | Tests separately credited units versus parent modules, specialist engineering gaps, a restrained related-fields concept and whether the caution text accurately explains this case. |

This selection covers all three presentation modes and one/two/three alternatives. It is purposive, not representative: do not estimate corpus error rates from it. CP278, CP283 and CP306 remain documented diagnostic examples for the common renderer, not additional pilot reviews. A temporary in-memory external-only setting for an otherwise normal pilot comparison can exercise the withheld-comparison branch without changing the committed settings.

## Remaining choices and immediate action

The six-stage order, preservation principle, four outcomes and two-case batches are settled by this assignment. The existing academic matching standard, route rule, feasibility constraints and presentation/academic separation remain unchanged.

Three implementation choices remain: the precise audience-field contract and migration of mixed notes; whether to withhold unresolved diagnostic component lists or display them with an explicit incomplete/uncertified label; and how to record independent final-review and rendered evidence consistently. The recommended defaults are an explicit canonical audience extension, withholding uncertified diagnostic lists while showing supported programme information and a clear limitation, and compact source-linked review observations plus identified viewport screenshots. None is implemented here.

Next, execute the first pilot pair, CP277 and CP119, under the new protocol. Record academic and communication findings without granting final approval through the known renderer defect. Use the pilot's actual content needs to settle the audience contract, implement the shared remedy once when authorised, then complete all six cases before beginning the 216 subsequent pairs. No corpus-wide run, recurring task or application deployment is started by this preparation.
