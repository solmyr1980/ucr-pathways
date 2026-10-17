# Counselor shared application foundation — implementation and verification

Date: 17 October 2026. Implementation: [`44c87cd9157ce7c257ce2a990b7f8a91979eaaee`](https://github.com/solmyr1980/ucr-pathways/commit/44c87cd9157ce7c257ce2a990b7f8a91979eaaee), based on `5d71e371eb5a5484c55bb3151756ccfbfd832bca` (including the intervening PDF publication after `860e2bf`).

The three shared remedies passed their relevant checks: audience boundary, course-modal content and counselor mobile table. This verifies the common mechanism; it does not approve the academic or communication content of individual cases. CP277 and CP019 remain `reviewed-with-blockers`. No canonical academic record, root decision, programme-interest row, workbook or presentation setting was changed. No next pilot pair or corpus processing was started, and no Shiny deployment or final production discovery-index release was performed.

## Settled audience contract

An optional `audience` object, version `1.0`, travels unchanged through the existing compact decision → canonical record → counselor renderer pipeline. Active decisions and canonical records remain version `2.0`; the v1 recovery compiler also preserves the optional object. Existing records remain valid inputs without bulk migration. JSON Schema and the manual validator check the new object; cross-record/cell references and completeness are checked mechanically, while prose and curricular judgments still require substantive case review.

The object contains `programmeDescription`, separate `comparisonExplanation`, and `curriculum` with status, permitted component IDs, clean year/route labels and any limitation. `conceptProgrammeIds` selects the existing canonical concepts; `noteTypes` selects unambiguous existing explanatory notes. `componentNotes` and stable-reference `cellNotes` contain reviewed audience notes. There is no second programme-concept field or second academic corpus.

The counselor renderer never falls back to `exception.reason`, `exception.curriculumContext`, `comparator.sourceNotes`, unrestricted `academicYear`/`route`, raw component/cell notes or presentation-override `message`. Those fields and all underlying evidence remain intact. Ordinary programme/course/component names, credits, meaningful blank cells and official-source links remain usable academic facts. Displayed narratives are escaped text, not executable HTML. Presentation mode still controls visibility independently of the academic decision; generic caution text preserves a clear specialist-training warning, with case-specific detail supplied by reviewed audience content.

| Curriculum display state | Behavior |
|---|---|
| Complete, explicitly reviewed | External-only display shows all selected components, totaling 180 EC. An unresolved external exception cannot acquire this state just by reaching a numerical total. |
| Verified partial | Show only explicitly selected, verified component IDs, with an unmistakable incomplete-degree heading and a substantive missing-requirement explanation. |
| Unresolved | Explain the uncertainty and withhold the diagnostic component list. |
| Missing/incomplete audience fields | Use neutral review-status copy and official links; never display internal prose as a fallback. Unreviewed external-only component lists are withheld. Legacy comparisons keep their factual table under a review notice, with mixed narratives awaiting selection. |

A comparison explicitly declared partial/unresolved uses the external-only presentation until its foundations support comparison. Reviewed concepts stay in their established canonical field and appear only after selection. Final case approval now also requires complete reviewed audience explanations, a complete verified 180-EC curriculum declaration and selection of every included canonical UCR concept; generic awaiting-review copy cannot pass that gate.

## Course descriptions and mobile presentation

BENBUSI211 now uses the coherent AI-focused `profile` from the current enriched workbook, rather than its older organisational-design `description2`. MCCHEAM316 now uses the existing `description2` about the history and methods of art history. Both texts were read as course descriptions before selection, copied verbatim and checked against the displayed modal text. No universal profile-over-description rule was introduced.

The existing code-keyed department caches now carry `descriptionSources` for reviewed corrections: selected field, workbook blob, source/description hashes, basis, date, verbatim/edited mode and review note. `validate-course-descriptions.py` detects later changes; an edited description still requires human/academic judgment. Other cached descriptions remain unchanged. The absent-description fallback was tested in the running app as well as in R.

At widths up to 700px, the same table uses readable-width columns and horizontal scrolling. Previous/next, programme selection, current full name/position, sticky block titles and Back to overview provide navigation without changing row relationships, partial correspondences or deliberate gaps. Desktop retains the side-by-side table. At 390px, CP019's columns are 360px wide, rather than compressing four columns into 360px. The verified table height is approximately 4,894px versus the prior recorded 9,179px; the page remains 390px wide. Empty rows remain where the academic alignment requires them.

Screenshot inspection caught a partly scrolled column and disappearing block titles during development; instant column selection and sticky block titles corrected both. Browser assertions were strengthened accordingly. Modal screenshots wait for Bootstrap transitions to settle and close completely.

## Actual rendered verification

The reproducible test starts the actual Shiny app locally with R 4.3.3 and Shiny 1.8.0, using Playwright 1.56 Chromium. A separate verification pass inspected actual DOM text and settled screenshots, compared modal content afresh with workbook evidence and tested internal-field contamination. The same agent performed this pass; no independent human academic review is claimed.

The final run passed **26 case/viewport combinations**, each at desktop **1440 × 1000** or mobile **390 × 844**:

| Inputs | Coverage |
|---|---|
| Unchanged CP003, CP001, CP019 | Normal comparisons with one, two and three UCR alternatives. |
| Unchanged CP330 | Caution comparison. |
| Unchanged CP119 | Genuine stored no-match exception; safe absent-audience state. |
| Unchanged CP277 | Unresolved external curriculum; no diagnostic list or internal research displayed. |
| Runtime-only CP004 fixture | Complete audience contract; existing concepts and meaningful limitation text selected without rewriting them. |
| Runtime-only CP002 fixture | Valid comparison withheld by presentation mode; complete external-only view. |
| Runtime-only CP005 fixture | Description present while other audience fields remain incomplete; safe fallback. |
| Runtime-only CP119/CP277 fixtures | Complete no-match external view; verified 175-EC partial list with the required 5 EC explicitly unidentified. |
| Runtime-only CP019/CP330 fixtures | Internal fields and presentation messages deliberately contaminated with sentinels; no sentinel displayed. |

Every case exercised search/open/back with query retention and inspected the exact official-source href from the record. Mobile comparisons exercised every column, previous/next, current name/position, visible block titles and return to overview. Tests checked page width, cell geometry and actual displayed text; no browser page errors were observed. Both corrected course modals opened and closed on desktop/mobile in actual and contaminated-fixture runs. A missing-code modal showed the readable unavailable-description fallback.

Source-link targets were checked against canonical URLs; this did not re-audit remote university content or certify remote availability. Runtime fixtures never wrote corpus files. Loading CP119/CP001 for renderer regression coverage did not begin their academic review. Current canonical audience content remains unpopulated pending the integrated case-by-case work.

Evidence: [rendered observations, complete displayed text, screenshots and code/data hashes](evidence/counselor-shared-foundation-2026-10-17/rendered-results.json). This identifies every case, viewport, input canonical blob, presentation mode and the exact implementation/runtime version. Representative settled screenshots:

- [CP019 mobile table](evidence/counselor-shared-foundation-2026-10-17/actual-cp-000019-mobile-table.png) and [desktop view](evidence/counselor-shared-foundation-2026-10-17/actual-cp-000019-desktop-top.png).
- [CP277 safe unreviewed view](evidence/counselor-shared-foundation-2026-10-17/actual-cp-000277-mobile-top.png) and [explicit partial-list fixture](evidence/counselor-shared-foundation-2026-10-17/fixtures-cp-000277-mobile-top.png).
- [BENBUSI211 modal](evidence/counselor-shared-foundation-2026-10-17/actual-BENBUSI211-desktop.png) and [MCCHEAM316 modal](evidence/counselor-shared-foundation-2026-10-17/actual-MCCHEAM316-mobile.png).
- [Withheld-comparison fixture](evidence/counselor-shared-foundation-2026-10-17/fixtures-cp-000002-mobile-top.png) and [selected canonical concepts/notes fixture](evidence/counselor-shared-foundation-2026-10-17/fixtures-cp-000004-desktop-top.png).

## Validation and limits

Passed: the complete compiler regression suite (v1/v2, exception and optional research), new audience positive/negative compiler tests, audience JSON Schema/canonical-reference tests, eight existing comparison-integrity tests, operational full-corpus counselor validators, registry-interest validation, six registry-correction tests and correction-ledger check, current 438-programme/21,212-interest review indexes, existing student/counselor Shiny behavior tests, dedicated audience/leakage tests, source-description fidelity checks, the 26 rendered tests, comprehensive-register consistency and diff/YAML checks.

The counselor deployment bundle check passed with exactly the selected 466 runtime files, required Shiny/jsonlite dependencies and a temporary manifest that was removed. A small check-only compatibility wrapper accepts installed rsconnect APIs with or without explicit `dependencyResolution`; deployment selection and the deploy action are unchanged. No deployment was performed.

Two pre-existing limits remain visible:

- A full formal JSON Schema run, beyond the normal operational validators, reports failures in **64 existing records**. The complete before/after error lists were identical: **zero new failures**. They concern component-ID format restrictions, legacy internal-note enums and candidate `evidence` requiredness. Nested `allOf` checks duplicate some messages; 969 validation messages are not 969 independent academic defects. [Affected IDs and categories](evidence/counselor-shared-foundation-2026-10-17/preexisting-schema-discrepancies.json) are recorded without changing identities or academic data. This schema/manual-validator discrepancy requires targeted reconciliation; this assignment does not claim the whole corpus passes every raw schema.
- Public-example validation retains the existing p-003 distinctness warning (three differing courses rather than four). It was not introduced or repaired here and does not concern the unchanged counselor corpus.

Shared-mechanism verification is limited to the tested matrix and source-backed modal corrections. Other course descriptions and every case's audience prose still require their normal substantive reviews. Complete/partial declarations must be supported by evidence; schema acceptance is not academic certification.

## Disposition and next work

Mark `audience-boundary`, `course-modal-content` and `counselor-mobile-table` verified for their shared remedies, with this implementation and evidence. Preserve all original diagnoses, case findings, row/course/alignment reviews and earlier screenshots. Record shared-foundation verification and close only the matching renderer/cache/layout action items in the two case files, preserving their original proposed states in explicit history. Academic and case-specific copy actions remain unimplemented; no approval is granted.

The next Work assignment returns to CP277 and CP019: implement their recorded bounded academic and communication corrections, populate/verify appropriate audience content, reassess affected dependencies and independently verify the finished cases. CP277's missing required 5 EC and exact-target attribution questions remain genuine evidence blockers. CP019's candidate/course rationale and other content corrections remain unimplemented. Only afterwards may the remaining pilot pairs proceed under the agreed integrated workflow.
