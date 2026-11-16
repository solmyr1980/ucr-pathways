# UCR Pathways — Stage 2: review the remaining 61 deferred counselor comparisons

**Status:** User-authorized Stage 2 production assignment for ChatGPT Work, 15 November 2026.  
**Repository and branch:** `solmyr1980/ucr-pathways`, `main`.  
**Boundary:** Review **exactly the 61 cases** remaining outside Stage 1. Proceed in small manual batches with a first-batch quality checkpoint. **Do not deploy, publish final discovery data, revive automations or release the corpus.**  
**Handoff:** This document is self-contained and authoritative for the *scope of this authorized Stage 2 work*. It does not replace the governing academic Production Instructions or implemented materiality policy.

## Execution amendment: 16 November 2026

The user has now authorized two hourly small-batch scheduled tasks, staggered at :00 and :30 Europe/Amsterdam. The [scheduled execution instructions](deferred-case-qualified-comparison-stage2-scheduling-2026-11-16.md) and `postAuditReviews[0].scheduling` in the active register supersede this assignment's manual-only, sequential next-case selection and no-new-automation restrictions for these two tasks only. Each task owns a disjoint 24-case queue and processes up to two cases per run, preserving the 13 reviews already complete. Existing ten-case QA groups remain. All academic, preservation, verification and release boundaries below remain binding. Old exhausted Restart Corpus A/B tasks remain paused.

## 1. Background and approval

The completed 438-case full-restart audit initially left 71 unresolved cases. The ten-case analytical pilot and subsequently authorized Stage 1 implementation established an explicit **bounded materiality standard**: a carefully limited qualified comparison, a qualified academic-core comparison, or a robust academic no-match may be approved when the evidence supports the precise academic claim, even if some external administrative/curriculum detail is unresolved. **Academic comparability and full UCR feasibility are not relaxed.** Missing information that could change the material academic judgment still requires a deferral.

**Actual Stage 1 outcome:** Six qualified comparisons, two robust no-matches and two still unresolved. The corpus then contained **375 verified dispositions** (311 approved comparisons, 63 approved no-matches, one registry exception) and **63 unresolved** of 438. Two Stage 1 cases, `cp-000099` and `cp-000072`, remain deferred and **are excluded from Stage 2**. The other **61** are the exact authorized scope. The Stage 1 report documents successful full-438 checks, 50 live counselor desktop/mobile browser checks, byte-preservation of preexisting cases, and existing working support in the compiler, schema, validators and UI.

On 15 November 2026 the user reviewed Stage 1 and **authorized Stage 2**, with an initial batch of approximately ten, a quality assessment after that first batch, and continuation in manageable manual batches **without routine additional approvals if quality remains consistent**. This does not authorize publishing or deploying the counselor application. It also does not authorize a higher approval rate, changed policy, new automations, a fresh full re-audit or indefinite source searching.

If Work cannot complete all 61 in one interactive session, it must leave a **GitHub-published, exact, verifiable resume checkpoint**. Do not claim work continues in the background; the next Work session resumes from that checkpoint.

## 2. Read the current authoritative GitHub evidence before beginning

Read current versions in this repository; do not rely on chat history or superseded handoffs:

1. `AGENTS.md` — mandatory `main` policy, authenticated GitHub connector writes, fresh-parent/fast-forward safety, publication script and validation.
2. `docs/UCR_Pathways_Production_Instructions.md` — especially **§2.1A (approved bounded materiality), §§2.1–2.3, 4.3–4.4, 5, 7 and 9**. This owns academic production and acceptance.
3. `docs/UCR_Pathways_Master_Specification.md` — especially counselor product meaning, academic integrity and explanation boundaries (§§4–6). The Web/LinkedIn publishing workflow is **not** part of this assignment.
4. `docs/qc/counselor-comprehensive-reaudit-protocol.md` — six review stages, evidence reuse, history, approvals, final source-first challenge and post-audit work.
5. `docs/qc/deferred-case-qualified-comparison-stage1-implementation-report-2026-11-15.md` and `docs/qc/evidence/qualified-comparison-stage1-2026-11-15/integration-results.json` — tested implementation, 375-approval baseline, verification gates, compatible representations, known caveats.
6. `docs/qc/deferred-case-qualified-comparison-pilot-results-2026-11-15.md` — detailed materiality reasoning and *How to handle the remaining 61*, including shared-source groups. Use it to challenge judgments, **not** to predetermine outcomes.
7. `data/counselor/qc/comprehensive-reaudit.json`, its `activeAudit` pointer to `data/counselor/qc/full-restart-2026-10-27.json`, and `docs/qc/evidence/counselor-full-restart-2026-10-27/cp-000458/overall-assessment-37.json`. For every case, inspect its **current** `data/counselor/qc/full-restart-2026-10-27/cp-XXXXXX.json`, its relevant `docs/qc/evidence/counselor-full-restart-2026-10-27/cp-XXXXXX/` sources and the current decision/canonical files. Reuse reviewed information only where the actual source/version and claim remain valid.
8. `docs/qc/evidence/qualified-comparison-stage1-2026-11-15/baseline.json` — **authoritative frozen list of the 61 out-of-Stage-1 deferred IDs** under the keys of `otherDeferred`. Confirm exactly 61, and verify each is still within the active 438-case scope and not newly approved by another authorized workstream. If there has been a material concurrent change, reconcile to current main rather than overwrite it.
9. Current enriched UCR course evidence: `data/reference/ucr_courses_enriched.xlsx` and `data/reference/README.md`; retain actual available description/outline distinctions and course availability. Do not change the workbook.

The exact **61-case scope** is also enumerated in the appendix. The two excluded Stage 1 deferrals must never be inadvertently selected.

## 3. Review standard and decision branches

For **each** assigned case, independently decide whether the existing and selectively refreshed official evidence supports:

- **Ordinary verified comparison** only if all established complete-external-pathway and current UCR academic/feasibility gates pass.
- **Qualified comparison** if the correct target, cohort and neutral route, defining subjects/methods, strongest meaningful current UCR response, precise documented external boundary and credible adverse resolutions support a robust **limited** academic claim.
- **Qualified academic-core comparison** if a stable, substantial confirmed core is enough for the explicitly restricted claim; label excluded required study and culmination prominently (as implemented for CP317). This is not a full-degree comparison and cannot be used when the unknown later academic weighting would change even the limited conclusion.
- **Robust no-defensible-UCR-match** if the strongest actual feasible UCR response lacks the defining external academic substance regardless of the bounded uncertainty. The absence of a professional title, particular language, license, travel or institution-specific format alone is not proof.
- **Remain external-programme-unresolved** where material unknowns could change the external programme's defining weight, selected neutral route, the strongest UCR option or the scope's meaning; when credible adverse resolutions cannot be bounded; or where source evidence is materially missing.

No percentage-of-EC rule, automatic approval, quota or presumption of no-match. For every unknown distinguish (a) formal access/credit/progression and (b) defining academic inquiry, methods, practical training, route and curricular weight. **Run the adverse-resolution test on the precise proposed claim**. If one credible resolution would overturn that claim, narrow it honestly only if a substantial academic core independently supports a meaningful bachelor-level comparison; otherwise defer. Preserve the distinction between genuine open elective credits, restricted choices and unknown required credits. Never fabricate missing courses, credits, regulations, waivers, thesis requirements, independent-research permission or UCR specialist teaching.

A 24-course feasible UCR schedule is necessary but never sufficient for a positive academic comparison. Apply actual course descriptions and available outlines, coherent concept-to-target assessment, traceability, course-to-concept content, sequential alternatives and stopping logic, pairwise 30-EC distinctness and all prerequisite/semester constraints. Keep optional independent research outside the 180 EC unless a scheduled UCR research course is legitimately selected. No-match requires actual strongest-response attempts and course evidence, even when no UCR schedule is published.

Preserve all approved Stage 1 contract semantics: internal `acceptance` evidence, academic-core scope, positive/no-match validation, partial curriculum and prominently bounded reader-facing view; do not make an `external-programme-unresolved` record render as an approved comparison through prose or a caution flag.

## 4. Initial batch: ten exact cases

Start **only** with these ten. They were chosen to test source reuse and different materiality boundaries, not to maximize approval. Process each whole case independently, even if official documents are shared.

| Case | Institution / programme family | Shared question and risk |
|---|---|---|
| `cp-000041` | Radboud Economics and Business Economics | Renewed cohort thesis-entry rules refer to old methods courses. |
| `cp-000042` | Radboud Economics and Business Economics (separate target) | Same apparent thesis-rule problem as CP041; verify distinct exact registry/cohort identity and evidence before reuse. |
| `cp-000053` | Radboud International Business Administration | Related but different old/new methods and thesis-entry reconciliation. |
| `cp-000040` | Radboud German Language and Culture | Three repeated 5-EC modules (15 EC); replacement/rotation could affect real academic content. |
| `cp-000046` | Radboud French Language and Culture | Separate repeated 15 EC and route/transition conditions; do not import CP040 corrections. |
| `cp-000100` | VU Health Sciences | Verified 150 EC; unknown third-year methods, placement and thesis. Test whether a core claim would be substantive and robust. |
| `cp-000112` | VU Global Politics | Unverified final 30 EC; thesis/mentorship conditions. |
| `cp-000113` | VU National Politics and Governance | Related to CP112 but different formal degree target and emphasis. |
| `cp-000397` | UvA Fiscal Economics | Shares 3313GEBRVY enrolment restriction with CP396 Tax Law, but **CP396's academic no-match must not be carried over** to Fiscal Economics. |
| `cp-000263` | TU/e Architecture, Urbanism and Building Sciences | 5/10-EC project and elective allocation conflict; compare own evidence, not CP266 Industrial Design's resolution. |

For the first batch: confirm the precise current evidence, use current UCR data, complete all academic and technical gates for each genuinely approvable disposition, and preserve genuine deferrals. Publish each approved/changed case with its decision, canonical, detailed case history and actual verification. An unresolved outcome is acceptable; do not repeatedly revisit it within this batch without genuinely new material evidence.

**After completing the ten**, publish a specific **first-batch QA assessment**: dispositions and remaining deferrals, whether academic materiality was applied consistently, adverse-resolution challenges, shared evidence reuse, source limitations, UCR feasibility and concept integrity, renderer/technical checks, errors fixed and any new policy question. If quality and safety pass, **continue automatically to the next manual batch** without asking for routine approval. If there is a material systemic integrity, correctness, publication or policy issue, stop safely, checkpoint and report it; do not silently change the standard.

## 5. Remaining 51 cases and batch selection

After first-batch QA, process the remaining authorized 51 in batches of **up to ten full cases**, with the last batch containing the remainder. Select them from the frozen `baseline.json.otherDeferred` keys **minus cases already fully reviewed in Stage 2**, not from an old case-number queue or the original worker assignments. Never take CP072, CP099 or any earlier verified disposition. Recheck the actual register and GitHub input versions immediately before selecting and publishing.

Prioritize related evidence families to reduce duplicate research, but do not let source sharing erase cohort, exact provider, route or substantive differences. Useful clusters from the pilot: the Radboud repeated humanities modules; Leiden biennial or duplicated language requirements; revised final-year cohorts across VU and Leiden; WUR chair-specific thesis preparation; UvA tax course and enrolment issues; TU/e framework inconsistencies. A difficult or still-unpublished source is **not** a reason to stop independent later cases; record a precise persistent deferral and continue.

For **each subsequent batch**: process whole cases through verified disposition or documented ongoing deferral, save durable evidence and commits, run batch quality checks, report actual count changes, and select the next cases by the frozen scope minus completed Stage 2 reviews. Continue while no substantive boundary is exceeded and the execution environment permits. Do not impose a separate intermediate approval gate after each routine batch. If a Work session ends, the next one must be able to resume exactly from GitHub, without redoing completed cases.

## 6. Required full case workflow and recorded outcome

For every case, in the existing production and review structure:

1. **Source-first external determination:** exact registry/provider identity, academic year/cohort and neutral applicable route; latest controlling official curriculum/course/formal evidence; preserve verified source versions. Inspect a source when a material claim depends on it; do not treat dynamic page shells or URLs as verified content. Prefer narrow fresh research only where it can answer a claim-critical question; do not re-run exhausted broad searches.
2. **Interests and academic substance:** assess every relevant target interest and current substantive external core; distinguish outcome/career mentions from programme substance. Retain checked previous work, document material changes and dependencies.
3. **UCR academic comparison:** examine real current taught UCR course content; strongest feasible closest programme, substantive concept-to-target match and missing specialist depth. Test genuinely distinct additional alternatives sequentially and stop when the next is unsupported. For negative proof, record strongest challenges and why they fail or remain plausible.
4. **Course and comparison implementation:** all 24-course/180-EC six-term UCR feasibility, PPD, six advanced, prerequisites, offerings, traceability, legitimate EC/category representation, correct alignment and explanatory notes; encode only supported external components and relationships.
5. **Reader-facing content:** make verification scope, exclusions, unknown required study, external nominal versus documented EC, open electives and UCR limitations accurate and prominent. Validate current course descriptions and links through the renderer mapping; no raw audit logs in public prose.
6. **Final verification and disposition:** separately identified source-first challenge against underlying official/UCR evidence, truthful same-AI independence disclosure, actual reviewed input versions, academic/mechanical/content checks, compiler/decision-canonical byte-exact replay, schema/operational/feasibility validation and applicable CI. Approve only after all case dependencies close. Document an unresolved case as **reviewed under Stage 2 but still incomplete**, not as an approved no-match or falsely completed audit case.

Keep original worker stages, retry/deferral history, claims and 2026-10-27 exhaustion evidence intact. Retain still-valid prior evidence and transparent case history/snapshots. Avoid copying a prior approval by assertion; the Stage 2 production review owns its new case conclusion.

## 7. Publication, progress and regression discipline

**Stage 1 implementation is already in place.** Do not redesign its acceptance data contract, schemas, renderer or governing policy without a concrete discovered defect. Changes necessary to represent this new **Stage 2 authorized case scope and progress** in the existing review register/validator are permitted, but must be minimal, tested and backward-compatible. In particular:

- The current `scripts/validate-comprehensive-reaudit.py` validates a `postAuditReview` entry scoped to the exact ten Stage 1 cases and excludes them from exhausted-worker completion mirrors. It cannot simply be reused unchanged for a second independent scope. Support Stage 2 **without overwriting Stage 1 metadata, rewriting worker histories or weakening counts and state checks**. Use one compatible auditable extension in the existing active register and its validator, not a second competing 438-case registry. Add negative tests for unauthorized IDs, overlap and stale/missing evidence.
- At the beginning, freeze the **375 current approved** case IDs and decision/canonical/case hashes. Create/check a Stage 2 preservation baseline (do not overwrite the Stage 1 baseline). Unprocessed cases, CP099/CP072, original approved records, course database, registry and student sources must stay unchanged unless independently evidenced and separately authorized.
- **Stage 1's existing preservation checker asserts that all 61 remaining cases are byte-identical; it must not be used unmodified as the Stage 2 preservation gate.** Use a Stage 2 checker that explicitly permits only reviewed/authorized scope changes, proves preservation of the 375 previous approvals and the cases not yet processed, and catches unauthorized input changes.
- Derived progress counts must come from active case states/actual approvals, not manual increments. A case reviewed but left unresolved must remain academically incomplete while being distinguishable from a case not yet examined under Stage 2. Avoid parallel redundant totals.
- Publish only completed **case-specific bounded deltas**, with no more than **one active decision/canonical repair pair per commit** under the repository guard. Serialize GitHub writes and use the authenticated connector, complete byte transfers, fresh parent, Git blob SHA verification, fast-forward `main`, read-back and applicable CI. Confirm prior publication before retrying any timeout; never overwrite another writer.
- When an unresolved case receives new evidence/notes, preserve its previous partial work and history. Source/integration checkpoints must make subsequent resume safe. No invented approved case, review check, evidence reference or CI success.
- For each batch, run affected-case schema/operational/feasibility and compiler/replay checks, derived audit validation, targeted acceptance tests and required CI. At the beginning and end of a batch, check preservation and fixed 438-case scope. Re-run relevant actual desktop/mobile app tests for newly exposed **types of qualified or partial-core displays**, renderer changes, or regressions; the first batch should include at least one representative browser-level check of each new disposition/presentation mode actually created and unchanged ordinary/unresolved controls. If no application implementation changes, reuse unchanged validated renderer logic but still confirm representative real case output and document the exact tested commit. Do not claim screenshots/browser checks not performed.

Batch checkpoint locations (create as needed; no giant duplicate corpus):
- `docs/qc/evidence/qualified-comparison-stage2-2026-11-15/batches/batch-01.md`, `batch-02.md`, etc. Each records its exact ten-or-fewer case IDs, completed reviews and states, commits, QA/CI evidence and the next selected batch.
- A concise **resume/current-status document** `docs/qc/deferred-case-qualified-comparison-stage2-progress-2026-11-15.md`, updated after every finished batch. It references individual case evidence and published batches, identifies the last verified HEAD, completed Stage 2 reviews **including those still unresolved**, source/policy blockers and the exact next action. Derive totals from the register, not parallel counts.
- At final completion, publish `docs/qc/deferred-case-qualified-comparison-stage2-final-report-2026-11-15.md` with all 61 case outcomes, approved/qualified/no-match/still-unresolved breakdown, academic and UI limitations, and reproducible validation/preservation/CI references.

If a session is interrupted mid-batch, persist **per-case** durable evidence and a precise restart action on GitHub, not just a temporary local file. Subsequent Work mode sessions must be able to determine exactly what was successfully published and what still needs doing.

## 8. Stop conditions, completion criteria and retained authority

Do not turn conditional or historical source evidence into a current fact. A new major academic uncertainty is a reason to **defer that case**, not to stop the entire remaining scope. Stop the **overall work** only for a real integrity/safety issue, a reproducible validation failure that makes further publication unsafe, irreconcilable concurrent repository changes, or a **new substantive policy decision** beyond the approved standard. Report exact root cause, preserved progress and what requires user decision. Technical failures should be recovered conservatively using the existing publication/replay workflow, with durable scope and next action rather than disabling anything.

After the first batch, review the results against the standard. If sound, continue other batches without seeking routine user approvals. Do not demand all 61 be approved: a genuinely unresolved final disposition is an acceptable completed **review** but does not count as an approved academic case. Do not treat 375/438 as an approval target; it is the Stage 2 starting baseline. Preserve separate counts of cases academically approved and Stage 2 cases that have received complete review.

**Never** create/restart scheduled automations, alter worker/model schedules, create branches/PRs, change the enriched UCR course database, student app/private records, production discovery/publishing indexes or externally deploy the counselor app. No public counselor release, website/LinkedIn rollout or university outreach. Do not begin a new full academic re-audit of the existing approved corpus.

**Final deliverable:** all 61 authorized cases have one documented Stage 2 disposition/review (including justified unresolved outcomes), verified GitHub evidence and preservation/validation results, and the final report. The user's **separate decision** governs any remaining deferred-case follow-up and final corpus release/deployment.

## Appendix: frozen Stage 2 case IDs (61)

Derived from the `otherDeferred` keys of the Stage 1 preservation baseline at the time of this handoff. The current register must confirm them before work starts.

`cp-000013` ·   `cp-000020` ·   `cp-000026` ·   `cp-000040` ·   `cp-000041` ·   `cp-000042` ·   `cp-000046` · 
`cp-000051` ·   `cp-000052` ·   `cp-000053` ·   `cp-000055` ·   `cp-000056` ·   `cp-000069` ·   `cp-000087` · 
`cp-000100` ·   `cp-000112` ·   `cp-000113` ·   `cp-000122` ·   `cp-000124` ·   `cp-000135` ·   `cp-000149` · 
`cp-000178` ·   `cp-000211` ·   `cp-000218` ·   `cp-000245` ·   `cp-000255` ·   `cp-000258` ·   `cp-000263` · 
`cp-000275` ·   `cp-000278` ·   `cp-000282` ·   `cp-000283` ·   `cp-000284` ·   `cp-000286` ·   `cp-000288` · 
`cp-000289` ·   `cp-000290` ·   `cp-000291` ·   `cp-000293` ·   `cp-000295` ·   `cp-000296` ·   `cp-000300` · 
`cp-000304` ·   `cp-000305` ·   `cp-000306` ·   `cp-000309` ·   `cp-000311` ·   `cp-000312` ·   `cp-000314` · 
`cp-000318` ·   `cp-000322` ·   `cp-000324` ·   `cp-000364` ·   `cp-000384` ·   `cp-000397` ·   `cp-000410` · 
`cp-000431` ·   `cp-000441` ·   `cp-000445` ·   `cp-000446` ·   `cp-000458`

**Excluded from Stage 2:** `cp-000072`, `cp-000099` (Stage 1 reviewed and remain unresolved). **Protected:** the 375 previously approved dispositions, all unrelated case data and the exhausted workers' audit histories.
