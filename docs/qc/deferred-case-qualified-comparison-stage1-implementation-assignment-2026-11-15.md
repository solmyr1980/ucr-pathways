# UCR Pathways — Stage 1 implementation of bounded materiality standard

**Status:** User-approved implementation assignment for ChatGPT Work, 15 November 2026. **Implement Stage 1 now; Stage 2 and release are not authorized.**  
**Canonical repository:** `solmyr1980/ucr-pathways`, `main`.  
**Owner of the substantive policy decision:** User, who approved the pilot's modified bounded materiality standard and clearly labeled confirmed-academic-core comparisons (including the narrow Leiden Law CP317 option).  
**Purpose:** Build the smallest safe production support for the approved standard; complete full case reviews of the ten pilot targets; demonstrate that existing verified records are not compromised; return a decision-quality implementation report.  
**Execution mode:** ChatGPT Work using current authenticated GitHub access. This document is a complete handoff and does **not** depend on prior conversation context.

## 1. Governing sources and existing state

**At start, read directly from current GitHub** (not recollections or stale excerpts):

1. `AGENTS.md` for mandatory `main` and authenticated GitHub publication, fresh-parent safety, validation, and no-force-push rules.
2. `docs/qc/deferred-case-qualified-comparison-pilot-results-2026-11-15.md` **in full**, especially *Decision in brief*, *Proposed operational acceptance standard*, ten case findings, *Implementation implications*, *Essential QA*, and *Decisions requested*. The entire report, including appendices and source refs, governs academic meaning and cases. The pilot's six/two/two counts are **analytical hypotheses**, not production dispositions.
3. `docs/qc/deferred-case-qualified-comparison-pilot-assignment-2026-11-15.md` for pilot background and handoff details.
4. `docs/UCR_Pathways_Production_Instructions.md`, especially §§2.1, 2.2, 2.3, 4.3–4.4, 7.3–7.4, 9; `docs/UCR_Pathways_Master_Specification.md`, especially §§4.4, 5, 6 and 12; and `docs/qc/counselor-comprehensive-reaudit-protocol.md`, especially its six stages and *Current full-restart: agreed next action after case processing (2 November 2026)*.
5. `data/counselor/qc/comprehensive-reaudit.json` and its `activeAudit` pointer, leading to `data/counselor/qc/full-restart-2026-10-27.json`; case evidence directory `data/counselor/qc/full-restart-2026-10-27/`; final 71-case assessment at `docs/qc/evidence/counselor-full-restart-2026-10-27/cp-000458/overall-assessment-37.json`.
6. Current record schemas, compiler/validators, counselor renderer, existing samples/fixtures and tests. Inspect relevant implementation files **in their current versions**, not merely these example names:
   - `scripts/build-counselor-comparison-v2.mjs`
   - `scripts/validate-counselor-comparison.mjs`
   - `scripts/counselor-audience.mjs`
   - `scripts/validate-comprehensive-reaudit.py`
   - `data/schema/counselor-comparison.schema.json`
   - `data/schema/counselor-exception.schema.json`
   - `data/schema/counselor-audience.schema.json`
   - `pilot/counselor-shiny/app.R`, relevant shared rendering helpers and tests
   - applicable `data/counselor/decisions/`, `data/counselor/comparisons/`, presentations, index/compiler entrypoints and validation/CI workflows.

**Verified baseline before implementation:** 438 fixed reviewed targets; **367 approved final dispositions** (305 comparisons, 61 no-matches, one registry exception); **71 deferred cases** (A 28, B 43). Both full-restart workers exhausted all assignments/revisits and their automations are disabled. The ten pilot cases are among the 71. Preserve the original review evidence. Do not restart the old workers or treat earlier QC as current academic approval.

Record and check the actual current `main` commit before implementation. The pilot was published at `bbce351a49ee132437c8bbc79f6faa167ff8b989`, but **do not assume it remains HEAD**.

## 2. Authorization and immutable boundaries

The user has **approved**:

- The **bounded materiality acceptance standard**: academic conclusion and completeness of the external pathway are distinct. Uncertainty in administrative or curriculum details may be explicitly qualified only if the comparison remains defensible under credible adverse resolutions. The academic-strength threshold for the UCR response is **not relaxed**.
- A **robust no-match** when already verified defining external academic substance is enough to establish a substantive UCR shortfall, despite immaterial missing external detail.
- A **narrowly labeled academic-core comparison**, including the CP317 boundary where 30 EC of later required external study remain unpublished. Such a view must visibly identify what is and is not compared; it must not be presented as a complete curriculum or hidden behind a generic footnote.
- **Stage 1 implementation**: governing documentation, minimal data contracts, validation, compiler, counselor presentation and necessary tests; full production review of the ten pilot cases; integration and QA report.

**Not authorized**: automatic approval of the pilot's hypothetical conclusions; an approval quota; changes to the fixed 438-case scope; bulk review or implementation of the **other 61 deferrals** (Stage 2 requires a separate decision); reopening the 367 verified cases except when a demonstrable material hard-rule violation requires it (report such an issue rather than expanding silently); changing student production rules; restarting/scheduling automations; publishing final counselor discovery/index products; live deployment; public release; university contact; model/schedule changes; or changing research/course database files.

Preserve sound existing data and schema semantics. Never fabricate missing course names, credit amounts, allocation, permissions, thesis eligibility, project requirements or UCR teaching. Never infer verified formal 180 EC from a nominal degree total.

## 3. Implement the accepted policy precisely

### 3.1 Governing documentation

Update the appropriate **authoritative** sections in the Master Specification (only for durable product meaning, if affected), Production Instructions (acceptance and production rules), and review protocol (review/verification method), according to their existing document ownership. Preserve all unrelated requirements and historical explanations. Document the new principle, applicable routes to verified/qualified/no-match/unresolved, mandatory adverse-resolution tests, reader transparency, audit and final-review gates, and appropriate authority for case approval. Explicitly retain the already verified pathway's ordinary default behaviour. Do not create competing sources of truth or overengineer a parallel corpus.

### 3.2 Minimal explicit acceptance evidence and schema

Inspect current decision, canonical and exception schemas, their consumers and the audit representation. Design the **smallest explicit, validated acceptance record** that distinguishes:

- an ordinary **verified comparison** with a complete external pathway;
- a **qualified comparison** whose limited academic claim is backed by specified verified external substance, bounded unknowns, credible adverse resolutions, fully feasible UCR closest response and readable limitation;
- a **robust no-match based on verified defining substance**, possibly with a partial external pathway;
- an **unresolved exception**, which must **never** display as a qualified comparison.

The pilot report proposes using existing top-level status semantics and a compact internal verification/qualification object rather than introducing a new top-level `recordStatus` or public score. Confirm actual constraints and choose the simplest schema-compatible form; there is no requirement to use a particular new field name. Preserve backward compatibility for the 367 existing verified records and for unaffected student records. Store evidence refs and the acceptance basis in internal fields; keep concise, accurate academic limits in audience fields. Do not use `caution` or mere prose flags as a substitute for verified academic acceptance.

### 3.3 Compiler, validators, audit checks and other consumers

The current v2 compiler and operational validator reject partial external curricula for positive comparisons and for `no-defensible-ucr-match`. The current audit sync/validation also assumes completed, verified external curricula in approved cases. Amend only the necessary branches to enforce the new **explicitly authorized** exceptions without weakening the ordinary complete-180 gate or any UCR 180-EC feasibility and academic gate. Check retained v1/other writer and reader paths for bypasses, and update or fail-closed as appropriate.

Every accepted qualified record must have a defensible claim, verified evidence boundary, limitations, plausible adverse-resolution check, valid current UCR 24-course/180-EC programme and content review. Missing external EC are **unknown requirements**, not free electives, balancing credits, matched cells or a fictitious generic thesis. Robust no-matches also require explicit academic negative proof from current UCR courses. Preserve byte-exact round trips and consistency across decision/canonical, audit and any displayed/exported representations.

### 3.4 Counselor application and truthful rendering

Inspect the actual `render_comparison` and shared rendering logic. Currently partial/unresolved curricula route to an external-only display even when a qualified positive comparison would be academically justified. Implement an explicit, validated qualified-comparison rendering route **without exposing ordinary unresolved records**.

In the reader-facing UI, distinguish:

- nominal external 180-EC degree versus **documented components and credits**;
- genuine open elective space versus **unverified required study**;
- known external component without a close UCR match versus **unknown component not assessed**;
- qualified academic-core relation versus **full-programme comparison**;
- unverified external thesis/progression requirements versus supported requirements;
- substantive disciplinary gaps that persist even if administration is clarified.

CP317 must visibly exclude the unknown final required 30 EC and culminating training from its assessed scope, while comparing only the supported legal core; avoid presenting 150 EC as an entire degree or as a complete third year. Retain already verified standard comparison presentation, explanations, links, course descriptions and optional independent research semantics. Do not present technical audit or internal source labels to prospective students. Implement only necessary interface changes and test them.

## 4. Ten approved pilot targets for full Stage 1 production review

All ten begin as deferred. The pilot's expected analytical conclusions are listed for orientation, **not permission to auto-flip statuses**:

| Case | Comparator | Pilot hypothesis | Special consideration |
|---|---|---|---|
| `cp-000250` | Clinical Technology, TU Delft/Leiden/Erasmus | Qualified | 180/181 EC conflict; pilot's new UCR feasibility demonstration needs actual production review. |
| `cp-000060` | Dutch Language and Culture, Radboud | Qualified | Repeated 5 EC; closest UCR trial needs the pilot's bounded course substitution and full review. |
| `cp-000033` | Business Administration, Radboud | Qualified | Thesis-entry conflict against already evidenced 180 EC; narrower claims only. |
| `cp-000396` | Tax Law, UvA | No defensible UCR match | Challenge the negative conclusion against the strongest plausible fiscal/legal UCR response; don't rely merely on professional title. |
| `cp-000440` | Business and Consumer Studies, Wageningen | Qualified | Missing chair-specific thesis guide; do not assume eligibility. |
| `cp-000317` | Law, Leiden | Qualified **academic core only** | 120 named first/second-year EC + 30 known open EC; unknown required final 30 EC not compared. |
| `cp-000277` | African Studies, Leiden | No defensible UCR match | Borderline heritage/postcolonial UCR content requires independent substantive challenge; unknown required 5 EC cannot be fabricated. |
| `cp-000099` | Health and Life Sciences, VU | Unresolved | Missing later curriculum may determine defining academic weight; retain if still material. |
| `cp-000072` | Spanish Language and Culture, Radboud | Unresolved | Interacting duplicated/rotating courses and mobility/seminar requirements; retain if material. |
| `cp-000266` | Industrial Design, Eindhoven | Qualified | 180/185 EC conflict and missing integrated design-studio spine; test actual limited UCR product/design response. |

For **each** case, inspect current case, official source evidence and source versions; independently reconsider external identity/cohort/route and UCR comparability, meaningfully test its **strongest feasible UCR response** and correct bounded academic/course/schedule issues. Reuse sound verified findings and existing 71-case research; do not bulk rereview irrelevant evidence. Apply the six-stage review protocol insofar as relevant to its changed academic acceptance basis, preserving stage history, dependencies, exact input versions, implementation and verification evidence.

Require a **separately identified source-first challenge** against underlying evidence, not endorsement of the editor's narrative. A same-AI second pass must be labeled accurately, not claimed to be independent human review. Run every relevant course-feasibility, schema, operational, compiler/replay, actual-display/content and applicable CI gate before final approval. Approve **only** if all new acceptance and old UCR academic/feasibility requirements are met; leave a case unresolved if material evidence is still absent. Preserve genuine alternatives while enforcing substantive distinctness and the stopping rule. Candidate counts are not targets.

The first ten cases must be treated as a production proof, not an assumed 6/2/2 conversion. Report actual outcomes and how they differ from the pilot's proposals. If some are unresolved, do not suppress or fill the gap. Document any remaining steps clearly.

## 5. Implementation order and verification

Organize Stage 1 into safe, bounded checkpoints; do not leave `main` broken. Recommended order:

1. **Baseline and dependency mapping.** Record current HEAD, active audit, the 367 previously approved case IDs and their current content hashes or comparable byte-identical basis, current validations and renderer paths. Identify the exact files/tests to change and any migration hazards. Do not modify production records before the new contract works and has representative tests.
2. **Policy and contract implementation.** Amend governing docs and the minimum schema/compiler/validator/audit/renderer paths. Write bounded fixtures covering verified, qualified, partial no-match and unresolved states before changing actual deferred cases. Handle the CP317 academic-core scope explicitly.
3. **Regression testing.** Exercise at least: unchanged ordinary verified comparison; qualified 180-EC substantive content with unresolved access (CP033); disputed credit weight (CP250); unrepresented final-year academic-core (CP317); design-studio gap (CP266); partial negative proof (CP277, CP396); and unresolved fallback (CP099, CP072). Verify complete-versus-unknown credits, open-space distinction, independent research, selected description links, default status semantics, and fail-closed behavior.
4. **Ten case-specific reviews and publication.** Use fresh GitHub parents; implement only academically supported dispositions with their exact UCR course and presentation checks. Preserve accepted existing cases and workers' historical audit findings. Rebuild/register only legitimately affected derived records. Run `scripts/validate-comprehensive-reaudit.py --sync` as applicable, inspect its diff, and do not manually invent progress counts.
5. **Integration and representative actual UI testing.** Run relevant validations and CI plus actual representative counselor desktop/mobile rendering for ordinary verified, qualified complete, qualified partial-core, partial no-match and unresolved. Validate renderer/fallback/clickable details. If runtime facilities are unavailable, report the untested dependency precisely; do not claim display verification or readiness for release.
6. **Final Stage 1 QC and report.** Reconcile successful productions to current HEAD, verify case-level decisions and canonical contents, derived register counts, the untouched 367 verified cases (same status and bytes unless an explicitly justified nonsemantic representation migration was essential), and all applicable validators/CI. Explain any unchanged or deferred cases and report exact links/commits.

**Do not** modify the live student app or private student records, change UCR enriched-course data, introduce a new scoring model, backfill the entire 438-case corpus, create a parallel comparisons library, or create scheduled workers. Do not start Stage 2 (61 cases) as part of this assignment.

## 6. GitHub writes and failure handling

Work **directly on `main`**, no new branches or PRs. Follow `AGENTS.md`: authenticated GitHub connector, confirm fresh remote parent before each write, use `scripts/github-publication.cjs` and complete content bytes, verify Git blob hashes and the new remote HEAD. Serialize commits; do not overwrite concurrent work. Validate proposed changes before committing, and avoid breaking HEAD between checkpoints. If connector, environment or source failures prevent completing a stage, checkpoint usable analysis/proposals with specific blockers and next actions; do not fabricate success, weaken gates or silently skip tests.

A current audit registry may have state/status fields tailored to the original exhausted automations. Preserve their history and never reactivate an old worker. Record any new approved Stage 1 case decisions and evidence under an explicitly scoped, compatible, traceable process; do not masquerade as output from an exhausted scheduled worker. Update the audit protocol and relevant validators to accept the authorized new standard without rewriting old review history.

## 7. Deliverables and decision gate

Publish on GitHub:

- All necessary **implemented** governing policy and minimal code/schema/renderer/test changes, with applicable validation and verified commits.
- Independently reviewed and, where justified, **updated production decision/canonical** and case-evidence records for the ten pilot cases. Preserve existing evidence and accurate audit trail; leave unapproved ones deferred. Explicitly identify any case where a necessary technical or academic gate is not yet met.
- A polished self-contained Stage 1 implementation report at:
  `docs/qc/deferred-case-qualified-comparison-stage1-implementation-report-2026-11-15.md`

The report must give: changed files and rationale; exact accepted materiality contract; **10-case per-case disposition and evidence table**; source-first challenges and UCR feasibility results; final counts and how derived; regression, validator and CI outcomes; actual desktop/mobile test results or explicitly untested paths; proof of preservation of the **367 original approvals**; any necessary additional work; risks, edge cases and relevant commits.

Conclude with a **clear user decision request about Stage 2** (the other 61 unresolved cases), but **do not start Stage 2 or deploy**. No final-corpus release, app deployment, public discovery indexes or new automation is authorized. If all Stage 1 gates do not pass, report the precise incomplete implementation instead of announcing completion.

**Success criterion:** User-approved, bounded qualification and robust no-match production pathways demonstrably work without weakening academic correspondence, UCR programme feasibility, ordinary verified-case semantics or reader transparency; ten pilot cases have defensible, individually checked outcomes; the existing 367 verified dispositions remain preserved; full release remains separately controlled.
