# Comprehensive counselor re-audit: operational protocol

Date: 17 October 2026. Status: preparation completed; no cases reviewed under this protocol.

This protocol implements the authorised comprehensive re-audit. It does not replace the [Production Instructions](../UCR_Pathways_Production_Instructions.md) or [Master Specification](../UCR_Pathways_Master_Specification.md). The [preparation report](counselor-comprehensive-reaudit-preparation-2026-10-17.md) records the baseline inventory, application diagnosis and six-case selection. The [review register](../../data/counselor/qc/comprehensive-reaudit.json) holds progress.

## Review unit and outcomes

Review one permanent counselor target end to end, including every alternative and its rendered explanations. Preserve sound work after independent verification. Earlier approval, stored `passed` declarations and successful compilation are evidence of past procedure, not proof of academic correctness.

Each stage receives one outcome:

| Outcome | Meaning and required record |
|---|---|
| Retain | Independently confirmed; identify the preserved material and evidence. |
| Correct | A bounded defect can be repaired; identify the affected fields, evidence and dependent claims. |
| Reconstruct | The underlying structure is unreliable; identify what must be rebuilt and which verified material survives. |
| Blocked | Essential evidence is missing or contradictory; identify the exact question and evidence needed to resolve it. Preserve the supported subset. |

An outcome describes the review finding. A separate action state records whether a correction/reconstruction is proposed, implemented or verified. `Retain` must not mean “not examined.” An unstarted stage has no outcome. No scores or automatic quality rankings are used.

## Six stages

### 1. External identity and curriculum

**Inputs:** current registry identity/provenance; decision and canonical comparator; earlier research; official programme, curriculum, course and formal sources applicable to the chosen entrant cohort and route.

**Procedure and acceptance:** confirm institution, exact target, teaching language/mode, cohort and any formal route. Apply the existing neutral route-selection rule. Check every component's EC, compulsory/restricted/open status and relevant progression conditions. Reconcile parent/child units, duplicate names/codes, repeat/resit versions, replacements and mutually exclusive choices. Verify research/thesis, placement and genuine open space. Record non-credit obligations separately. The complete pathway must contain 180 unique EC and be valid for one coherent cohort/route; numerical closure alone is insufficient. A 180-EC list with an unmet prerequisite or unresolved formal rule does not pass. Consult applicable formal regulations when ambiguity or conflict requires them; do not impose an OER requirement where sufficient official evidence already exists.

**Evidence:** concise claim-to-source references with URL, academic/cohort year, check date and section/page/course identifier where needed. Preserve an existing source record if inspection confirms it; do not copy whole research logs. Record the controlling source and resolution of any material conflict. A link without inspection is not verification.

**Outcomes and dependencies:** retain a confirmed pathway; correct isolated errors; reconstruct mixed or unreliable pathways; block essential unresolved requirements without inventing credits. A material identity change affects stages 2–6. A component/route change requires reassessment of affected interests, concepts, alignment, totals and descriptions, not automatic replacement of unaffected work. Do not certify dependent UCR correspondence while the external basis remains unresolved.

### 2. Academic interests and evidence

**Inputs:** every exact-target row in `programme_interests.csv`, current official evidence, stage-1 findings and the stored interest assessment/evidence map.

**Procedure and acceptance:** reconcile the complete target-linked row set, not a convenient selection. Check substance and attribution; distinguish central interests, stable directions, curricular topics, examples and individual outcomes. Apply existing generator-eligible, support-only, search-only and excluded-inherited roles. Corroborate inherited split-target evidence before using it for construction. Every generator-eligible row must be covered substantively by the core or belong to a coherent candidate direction; reject omnibus residual categories. Assess unsupported discovery claims even when they did not generate an alternative.

**Evidence:** row identifiers plus the inspected official material supporting disputed classifications or exact-target corroboration. Reuse verified classifications and sources.

**Outcomes and dependencies:** use the four outcomes above. Changed interests require reassessment only of the concepts, course contributions, stopping decisions, search content and descriptions that depend on them. Independently established interests can still be reviewed while a different stage-1 requirement is blocked; their use in a complete comparison remains provisional.

### 3. UCR comparability and concepts

**Inputs:** verified external academic structure, complete interest assessment, existing concepts/candidate dispositions/no-match evidence and the current enriched UCR workbook.

**Procedure and acceptance:** independently test the strongest feasible closest response. Review both positive decisions and no-match judgments. A coherent concept must precede its course implementation. Test additional concepts sequentially under the existing evidence, coherence, substantive distinctness and feasibility gates. Preserve the existing pairwise 30-EC/four-course floor and stopping rule. Neither three alternatives nor one alternative is a default. A no-match must follow a genuine programme-level attempt against actual UCR content; absence of the degree title, language training or a professional licence alone is insufficient.

**Evidence:** a concise concept/basis assessment, candidate and stopping decisions, and workbook references explaining either viable implementation or the specific academic shortfall. Prior course palettes are leads, not a constraint on judgment.

**Outcomes and dependencies:** retain independently justified concepts/decisions; correct bounded claims or dispositions; reconstruct an unsupported organising concept; block a comparability conclusion that depends on unresolved external evidence. Reassess affected selections, schedules, comparisons and wording at stages 4–6. Do not manufacture a substitute to avoid an exception.

### 4. UCR courses, schedules and comparison

**Inputs:** accepted concepts; current `data/reference/ucr_courses_enriched.xlsx`; complete schedules, traceability, components, blocks and alignments; current validators/compiler.

**Procedure and acceptance:** check every selected course's identity, substantive contribution and direct/complementary role against actual enriched content. Check programme-level weight: an incidental topic cannot justify a defining theme. Recheck 24 unique courses, four per semester over six terms, 180 EC, at least six 300-level courses and Year-1 PPD. Read each formal prerequisite and assigned-term offering directly from the workbook; store the check result and any ambiguous prerequisite interpretation. Consider advisory progression without inventing extra hard constraints. Test qualitative distinctness as well as the numerical floor.

Check complete, nonduplicated external/UCR coverage and stable references. Review all positive and unmatched component placements using Production Instructions §5. Preserve meaningful blanks, choose the strongest adequate content relationship and distinguish partial correspondence from equivalence. Include optional independent research exactly as specified, outside the scheduled 180 EC. Recompute affected comparator placements after a UCR row changes.

**Evidence:** workbook blob/version, exact course codes and relevant content/term/prerequisite facts; component-level alignment reasoning, retained in existing traceability structures where possible; validator and compiler-replay results. Stored feasibility declarations alone do not verify the workbook. Existing validators do not independently read its prerequisite/availability fields.

**Outcomes and dependencies:** use the four outcomes; a failed implementation may reopen stage 3 rather than force unrelated substitutions. An exception has no fabricated UCR schedule to validate: record that limit explicitly and review its supported external structure and stage-3 no-match evidence. Reassess all affected claims and presentation at stages 5–6.

### 5. User-facing explanations

**Inputs:** the verified academic record, actual field-to-renderer map, exception state, notes, labels, concepts, sources and presentation messages.

**Procedure and acceptance:** read every substantive displayed title, concept, summary, limitation, component/cell note and exception explanation in context. The text must be intelligible to prospective students/counselors, accurate, proportionate to curricular weight and useful to their decision. State important gaps and uncertainty plainly. Keep source retrieval, API/cohort investigation logs, validation reasoning and unexplained identifiers in internal evidence. Preserve well-written content. Check English programme names against the current display metadata; do not expose administrative names through fallback rendering.

**Evidence:** exact field paths and short reasons for any finding; corrected copy linked to the verified claims when implementation is authorised. Review source links and the course-description content actually used by the modal, as well as record text. A keyword scan can flag candidates but cannot approve prose.

**Outcomes and dependencies:** use the four outcomes. If accurate wording reveals an unsupported academic claim, reopen its originating stage. Do not hide a material academic limitation by merely suppressing an internal note. Stage 6 must inspect the resulting display, including missing-description and other fallback paths.

### 6. Rendered experience and final validation

**Inputs:** exact code/data/presentation release, stage findings, implementation state and relevant validation results.

**Procedure and acceptance:** inspect the running counselor app at desktop and narrow mobile widths. Exercise search, result opening, back navigation, source links and course modals. Inspect normal, caution and external-only presentations, including genuine exceptions and a comparison withheld only from display. Confirm labels, notes, source information, empty cells, scrolling, long text and partial/unresolved curricula communicate accurately. An unresolved or diagnostic component list must not appear to be a certified degree pathway.

Separate academic, technical and communication findings. Final approval requires all applicable findings resolved, an independent academic/communication review of the finished result, and mechanical checks; identify the reviewer or review pass and its evidence. Independent review must reconsider claims against sources, not simply endorse the producer's report. Screenshots/observations must identify record, viewport, code/data commit and presentation mode. JSON inspection and R startup tests cannot substitute for rendered inspection.

**Evidence and checks:** run `npm run validate:counselor`; replay changed v2 decision/canonical pairs through the existing compiler in temporary output and compare bytes. For compiler/contract changes run the compiler/exception/optional-research regressions; for app/shared-renderer changes run the applicable Shiny tests and bundle check. Validate registry interests if changed and rebuild/check review indexes when their inputs change. Leave the final production discovery indexes absent until authorised finalisation. Do not repeat unrelated tests after unchanged passing results.

**Outcomes and dependencies:** use the four outcomes; a shared rendering defect can block stage 6 across cases without invalidating their verified academic stages. A supported unresolved exception can finish its review as `reviewed-with-blockers`, with an accurate external-only explanation, but is not an approved complete comparison. Do not turn a missing finding into approval because a batch has ended.

## Dependency and evidence discipline

Progress through stages 1–6 for one case before starting the next, pausing dependent conclusions when evidence is blocked. Continue genuinely independent checks and identify their limited scope. After an upstream change, record which later findings need reassessment and why; each is closed by a fresh retain/correct/reconstruct/blocked finding. Never copy an old approval across a changed basis.

Reuse verified components, research, course choices and explanations. Retain the original historical QC reports. Cite them as leads or prior evidence, not as current approvals. When a source remains inaccessible, seek a reasonable official alternative once; document the precise unresolved claim rather than repeatedly retrying an empty catalogue. No monitoring task or correspondence with a university is implied.

## Register and shared defects

`data/counselor/qc/comprehensive-reaudit.json` is the compact progress record. Git history supplies old versions, so the register should link evidence and changed fields rather than duplicate curricula or every course rationale.

For each started case record: permanent ID; reviewed input commit and canonical/decision blobs (or absent decision); lifecycle state; six stage entries; retained material; bounded changes/reconstruction; unresolved questions; source/check references; dependent stages requiring reassessment; implementation commits and final review evidence. A stage contains `outcome`, concise `finding`, `preserved`, `actions`, `evidence`, `blockedBy` and `reassessStages`. Each action has its field/scope and `state` (`proposed`, `implemented`, `verified`) with a commit/check reference when available. These are review metadata, not a second academic record.

Lifecycle values are `not-started`, `in-progress`, `reviewed-with-blockers` and `approved`. Stages not reached remain absent. An `approved` record has six completed stage findings, verified required actions, no unresolved dependent reassessments and final evidence. Where UCR-only checks do not apply to an exception, the stage finding must state exactly what was reviewed and why the absent structures were not required. A blocked stage cannot support `approved`.

Record recurring mechanisms once in `sharedIssues`, with affected field paths, example IDs, remedy, implementation/check references and status. Individual cases link the shared issue and record their own affected text; do not re-diagnose the common renderer six times. Verify the common remedy once across its full presentation/viewport matrix, then check each case's actual copy and data integration. Keyword/content scans and cross-case course/alternative patterns are triage signals, not grounds for automatic rewriting.

## Execution sequence

1. Preserve the preparation baseline and six-case selection. This assignment stops here: no pilot outcomes are assigned.
2. On authorisation to execute, process pilot pairs **CP277 + CP119**, **CP001 + CP019**, then **CP035 + CP330**. Complete the academic stages and communication diagnosis; keep stage 6 open where a shared architecture defect prevents approval. Any record repairs follow the existing material-error rules.
3. Review the proposed audience-content contract before implementing it. Implement the agreed shared remedy once, preserve internal research, and complete rendered checks across normal/caution/external-only, unresolved/no-match and withheld-comparison variants. Revisit only affected pilot stages.
4. Assess whether the procedure exposed missing criteria or disproportionate documentation. Resolve material methodological questions and complete independent final review before starting corpus-wide batches.
5. Process the remaining baseline targets in registry `production_order`, two whole cases per batch, skipping pilot cases only when their full review is complete. Prior approvals from other exercises do not remove targets. With 438 targets and six completed pilot cases, 432 remain: 216 pairs. A blocked case stays visibly unresolved; continue to the next unstarted case without counting the blocker as approved or repeatedly selecting it without new evidence.
6. Reconcile counts after each batch: approved, in progress, reviewed with blockers and unstarted must sum to scope. Track new/withdrawn/changed targets separately against the fixed baseline; never silently change the denominator. Reserve final corpus approval until unresolved blockers are resolved or an explicit, documented release decision addresses them.

Review batches contain two cases; the existing repair Action accepts only one active decision repair per commit. Publish necessary repairs as separate validated decision/canonical commits, then update the batch register. Refresh the remote parent before every write, preserve intervening work and use no force update. The first five canonical records lack root production decisions; handle any necessary repair explicitly under the existing fallback/manual recovery arrangements rather than claiming a v2 replay or treating a new decision as new production.
