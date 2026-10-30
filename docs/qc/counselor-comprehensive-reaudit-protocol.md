# Comprehensive counselor review protocol

**Purpose:** Reusable review, correction and verification procedure. Production Instructions own academic generation; this protocol owns review execution. Current assignments and status belong in the active register, not in this document.

## Authority and current state

Before work and immediately before publication, read `data/counselor/qc/comprehensive-reaudit.json`. Follow its `activeAudit` pointer when present. The active register owns scope/order, case-evidence directory, assignments, task identities, claims, pauses, source-retry history and reporting intervals. Preserve explicit assignments and scope. A user pause prohibits academic processing until explicitly lifted; maintenance of tooling does not lift it. Do not create tasks or change models or schedules as a side effect of review.

When a fresh audit is explicitly authorised, old approvals and failure counts confer no new progress. Verify the assigned case from underlying current sources; retain sound artifacts only after that verification. Otherwise apply the material-error and hard-rule reopening threshold in Production Instructions Section 9. Neither rule authorises arbitrary rewriting of defensible work.

Earlier pilot instructions, dated queue amendments and dispositions are historical. The [pre-consolidation protocol](https://github.com/solmyr1980/ucr-pathways/blob/b12c0d88bd74f24af6bec29fa763792e104dc58b/docs/qc/counselor-comprehensive-reaudit-protocol.md) and dated completion reports preserve that history; they are not competing active instructions.

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

## Integrated processing of each case

A normal reporting pair contains two whole cases; the current two-task continuation processes one complete assigned case per worker execution. For each case, complete the following workflow before moving to the next case; do not create a diagnosis queue followed by a separate corpus-wide correction exercise:

1. Independently examine the existing academic evidence and decisions through all six stages below, including the actual user-facing output. Treat previous QC and validation as leads, not approvals to inherit.
2. Identify precisely what can be retained, what needs bounded correction and what needs reconstruction. Record the evidence, affected fields and dependencies. Preserve independently verified work.
3. Implement the necessary corrections through the existing decision/canonical repair and validation infrastructure. Preserve sound components and internal research. An unavailable external source does not excuse leaving independently repairable defects unimplemented.
4. Reassess every materially affected downstream decision: interest classifications and discovery, concepts and stopping decisions, course contributions, schedules, distinctness, traceability, comparison alignment and wording, as applicable. If a repair invalidates the concept, reopen that concept rather than force unrelated substitutions. Close each dependency with fresh evidence; leave unaffected verified work intact.
5. Independently verify the corrected academic record, mechanical validity and actual running user experience. The final reviewer or separately identified independent review pass must inspect underlying official/course evidence and the finished record, rather than endorse the correction author's account. Record the reviewed input versions, source checks, reviewer/pass and how independence was maintained. If independence cannot be established, final approval remains blocked.
6. Record final disposition only after implementation and verification. Approve only when all applicable checks pass, required actions are verified and dependent reassessments are closed. A case may finish as `reviewed-with-blockers` when essential evidence is genuinely unavailable: state the precise missing evidence and supported subset, implement all independently possible repairs, and withhold unsupported academic and presentation approval.

`Reviewed-with-blockers` is not a device for deferring repairable work. The initial first-pair review used that status while awaiting shared fixes; its subsequent integrated completion approved CP019 and retained only CP277’s genuine external blocker. Shared application defects are resolved once and then checked with each affected case. Normal corpus batches must not reproduce that preparatory diagnosis-only arrangement.

This final check is part of the same case's normal processing. Recheck changed foundations and all applicable completion gates; do not commission a second general academic audit after the corrections. A distinct reviewer is preferable; where a separately identified review pass is used, it must independently establish claims from the sources and record its method and limitations. Merely renaming a self-check does not establish independence.

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

As an operational challenge under the existing standard, distinguish whether the courses implement the proposed concept from whether that concept materially responds to the target's defining academic substance. General coherence and a transparent limitation do not themselves establish the latter. The [CP119 adjudication](cp119-comparability-adjudication-2026-10-18.md) illustrates this distinction; it introduces no matching-course quota or disciplinary-equivalence requirement.

**Outcomes and dependencies:** retain independently justified concepts/decisions; correct bounded claims or dispositions; reconstruct an unsupported organising concept; block a comparability conclusion that depends on unresolved external evidence. Reassess affected selections, schedules, comparisons and wording at stages 4–6. Do not manufacture a substitute to avoid an exception.

### 4. UCR courses, schedules and comparison

**Inputs:** accepted concepts; current `data/reference/ucr_courses_enriched.xlsx`; complete schedules, traceability, components, blocks and alignments; current validators/compiler.

**Procedure and acceptance:** check every selected course's identity, substantive contribution and direct/complementary role against actual enriched content. Check programme-level weight: an incidental topic cannot justify a defining theme. Recheck 24 unique courses, four per semester over six terms, 180 EC, at least six 300-level courses and Year-1 PPD. Read each formal prerequisite and assigned-term offering directly from the workbook; store the check result and any ambiguous prerequisite interpretation. Consider advisory progression without inventing extra hard constraints. Test qualitative distinctness as well as the numerical floor.

Check complete, nonduplicated external/UCR coverage and stable references. Review all positive and unmatched component placements using Production Instructions §5. Preserve meaningful blanks, choose the strongest adequate content relationship and distinguish partial correspondence from equivalence. Include optional independent research exactly as specified, outside the scheduled 180 EC. Recompute affected comparator placements after a UCR row changes.

**Evidence:** workbook blob/version, exact course codes and relevant content/term/prerequisite facts; component-level alignment reasoning, retained in existing traceability structures where possible; validator and compiler-replay results. Stored feasibility declarations alone do not verify the workbook. Run `python scripts/validate-course-feasibility.py <canonical.json>` against the retrieved workbook; stored feasibility declarations alone do not satisfy this check.

**Outcomes and dependencies:** use the four outcomes; a failed implementation may reopen stage 3 rather than force unrelated substitutions. An exception has no fabricated UCR schedule to validate: record that limit explicitly and review its supported external structure and stage-3 no-match evidence. Reassess all affected claims and presentation at stages 5–6.

### 5. User-facing explanations

**Inputs:** the verified academic record, actual field-to-renderer map, exception state, notes, labels, concepts, sources and presentation messages.

**Procedure and acceptance:** read every substantive displayed title, concept, summary, limitation, component/cell note and exception explanation in context. The text must be intelligible to prospective students/counselors, accurate, proportionate to curricular weight and useful to their decision. State important gaps and uncertainty plainly. Keep source retrieval, API/cohort investigation logs, validation reasoning and unexplained identifiers in internal evidence. Preserve well-written content. Check English programme names against the current display metadata; do not expose administrative names through fallback rendering.

**Evidence:** exact field paths and short reasons for any finding; corrected copy linked to the verified claims when implementation is authorised. Review source links and the course-description content actually used by the modal, as well as record text. A keyword scan can flag candidates but cannot approve prose.

**Outcomes and dependencies:** use the four outcomes. If accurate wording reveals an unsupported academic claim, reopen its originating stage. Do not hide a material academic limitation by merely suppressing an internal note. Stage 6 must inspect the resulting display, including missing-description and other fallback paths.

### 6. Rendered experience and final validation

**Inputs:** exact code/data/presentation release, stage findings, implementation state and relevant validation results.

**Procedure and acceptance:** inspect the actual finished case in the running counselor app at desktop and narrow mobile widths, in its applicable presentation mode. Exercise search, result opening, back navigation, source links and the case’s course-modal integrations. A shared renderer change requires the full normal/caution/external-only matrix, genuine exceptions and a comparison withheld only from display; unchanged shared behavior need not receive a fresh full-matrix review for every case. Confirm labels, notes, source information, empty cells, scrolling, long text and partial/unresolved curricula communicate accurately. An unresolved or diagnostic component list must not appear to be a certified degree pathway.

Separate academic, technical and communication findings. Final approval requires all applicable findings resolved, an independent academic/communication review of the finished result, and mechanical checks; identify the reviewer or review pass and its evidence. Independent review must reconsider claims against sources, not simply endorse the producer's report. Screenshots/observations must identify record, viewport, code/data commit and presentation mode. JSON inspection and R startup tests cannot substitute for rendered inspection.

**Evidence and checks:** run `npm run validate:counselor`, `python scripts/validate-counselor-schema.py <canonical.json>` and the shared course-feasibility check; replay changed v2 decision/canonical pairs through the existing compiler in temporary output and compare bytes. For compiler/contract changes run the compiler/exception/optional-research regressions; for app/shared-renderer changes run the applicable Shiny tests and bundle check. Validate registry interests if changed and rebuild/check review indexes when their inputs change. Leave the final production discovery indexes absent until authorised finalisation. Do not repeat unrelated tests after unchanged passing results.

**Outcomes and dependencies:** use the four outcomes; a shared rendering defect can block stage 6 across cases without invalidating their verified academic stages. A supported unresolved exception can finish its review as `reviewed-with-blockers`, with an accurate external-only explanation, but is not an approved complete comparison. Do not turn a missing finding into approval because a batch has ended.


## Reuse and affected dependencies

Complete one assigned case end to end before starting the next, resuming its exact unfinished action after an interruption. A checkpoint preserves work; it is not completion. Apply source-search limits and deferral authority from the active register. An inaccessible external source does not prevent independently repairable work, and a deferral is not a verified final disposition or an academic no-match.

Record which input changed, which conclusions depend on it, what can be retained and what needs fresh verification. Preserve original findings and source versions. A separately authorised fresh-review scope still requires fresh source verification; evidence reuse cannot carry an old approval into that audit.

| Changed basis | Normally reassess | Normally preserve |
| --- | --- | --- |
| Course offering or prerequisite | Affected schedules; selections if rescheduling fails | External curriculum and interest research |
| Course content | Its program contribution, matches and claims | Unaffected course judgments and external research |
| Comparison rule | Alignments, blocks and explanations | Sound curricula and feasible schedules |
| Renderer or layout | Shared rendering and case integration | Academic judgments |
| Discovery ranking | Discovery indexes and search tests | Fixed comparisons |
| Starting cohort | Scheduling within the actual horizon | Concepts/selections that remain feasible |

These are review boundaries, not automatic exemptions. Course replacement can change a concept; a revised external curriculum can change comparability. Cite the independently confirmed subset and close each affected dependency with a retain/correct/reconstruct/blocked finding. Never copy approval across a changed basis.

Compare deliberately regenerated course references with `python scripts/validate-course-feasibility.py --compare-workbook <previous.xlsx>`. The report identifies changed fields and records using changed courses; it neither repairs records nor judges validity. New or substantially changed content also needs targeted subject-area reassessment, including previous no-match cases that never used the course. Do not infer that a use-based report finds those opportunities.

## Shared content and rendered verification

Review a shared course description once for the same code, selected evidence, course name and displayed text. Record its provenance in the existing cache; cite that verified version in later cases. Reassess each course’s contribution to each program independently. Shared description approval never establishes program relevance.

Run the full shared mode/viewport regression matrix when shared app code, contracts or behavior change. For an ordinary case, inspect its actual complete content, applicable mode, desktop/mobile usability and selected-course modal integrations. Reuse unchanged shared prose and behavior findings rather than recreating their academic reviews or identical screenshots. Capture evidence sufficient to show the actual case and material layout/content findings; record exact code/data/presentation inputs and viewports. Case inspection cannot be replaced by JSON inspection, a generic fixture or a previous case’s screenshot.

Re-run checks when their inputs or relevant dependencies change. Unrelated private-student deployment regressions need not repeat for counselor-only content or bookkeeping changes; shared changes and final release require the applicable broader checks. Keep the separately identified source-first final academic pass. It must establish claims from underlying evidence and record its method and limits; a same-AI pass is not independent human review.

## Case evidence and derived progress

The detailed case file owns stage findings, evidence, actions, dependencies, academic disposition and final review. Preserve complete substantive findings, original diagnoses and superseded evidence in its existing history. Source references, screenshot hashes and implementation commits remain traceable. The active register owns operational scope, assignments, pauses, claims, deferrals, reporting decisions and release authority.

After changing case evidence, run `python scripts/validate-comprehensive-reaudit.py --sync`. This derives central case mirrors, progress counts and worker completion summaries from detailed evidence, then validates; a failed validation restores the prior local register. It never creates academic findings, approves a case, closes a reporting pair, clears a pause or advances a queue. Check the local diff and publish the changed case and derived register together. The same command without `--sync` is read-only validation.

Retain existing stage/action structures: each stage has outcome, finding, preserved material, actions, evidence, blockers and reassessment dependencies. Implemented actions cite a commit; verified actions cite actual verification evidence. `finalReview` identifies reviewer/pass, independence method, date, reviewed inputs and academic/mechanical/rendered checks. Each check must cite actual evidence. Full findings remain in the case file; derived summaries do not replace them.

Record recurring shared defects once, with implementation and verification evidence; cases reference the shared issue and retain their particular findings. Preserve supported blockers precisely. No-match approval and positive-comparison approval remain distinct from unavailable external evidence, operational deferral and presentation visibility.

## Publication and release

Academic work on explicitly disjoint assignments may proceed concurrently in separate checkouts, ports and render paths. Serialize publication only. Immediately before every write fetch current main, active audit, pause state and touched paths. Merge only the current case/worker delta into fresh shared contents. Publish one active decision repair with its regenerated canonical pair; include the corresponding case/register changes when their evidence is ready. Use one atomic authenticated-connector commit on the fresh parent and an expected-parent, non-forced fast-forward update. On conflict refresh, reconcile and revalidate; never overwrite another worker’s state or force-update main.

For a decision repair, replay the compiler into temporary output and compare the canonical bytes. New and repaired canonical records must pass strict full JSON Schema and workbook feasibility checks before publication/approval, in addition to operational validators and source-based academic checks. Rebuild/check indexes only when their inputs change. Verify the published commit and relevant workflows before final disposition. Do not generate final discovery indexes or deploy the counselor app without the separate release authority.

The read-only full-schema inventory may identify unrepaired legacy records while unrelated tooling work proceeds. It is explicitly not a passing academic or release gate. Missing candidate evidence remains required and must be resolved in the relevant case review. Final release requires every canonical record to pass strict schema validation, with operational validation and academic blockers separately resolved. Technical representation fixes must not invent academic evidence.

Progress reports follow the active register’s reporting interval and count only verified final dispositions; a trigger or an in-progress claim is not completion. Ordinary case blockers do not automatically pause independent work. Record an evidenced systemic review/publication failure and stop the affected work under the active register’s authority. One final corpus integration/release check follows completed case reviews; it is not another full academic re-audit.
