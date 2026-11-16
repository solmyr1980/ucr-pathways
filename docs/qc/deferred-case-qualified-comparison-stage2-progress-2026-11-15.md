# Stage 2 current status

16 November 2026. The browser regression is repaired. Batch 1 passed; batch 2 is in progress under the existing authorization.

- Completed Stage 2 reviews: **13/61**. Remaining to complete: **48**, including CP051 in progress and 47 not started under Stage 2.
- Current academic approvals: **387/438**; academically unresolved: **51**.
- Stage 2 has added **12 approvals**: eleven qualified comparisons and one robust no-match. CP013 has a completed review but remains unresolved.
- Latest verified production-output commit: `3ccb3cb7b8e4552d5ccfecaac18c76d488708f92` (CP026). Its exact compiler replay, record validation and review-index CI passed. CP026's final disposition was recorded at `8a02ed4f3a61fe9e84dfaa31904b6bb803a06bb7`; its validation CI also passed. Individual case evidence owns the exact decision/canonical blobs.

[Batch 1 QA](evidence/qualified-comparison-stage2-2026-11-15/batches/batch-01.md) retains its ten completed reviews. [Batch 2 checkpoint](evidence/qualified-comparison-stage2-2026-11-15/batches/batch-02.md) records the three completed batch-2 reviews and the unfinished CP051 work. [Current checks](evidence/qualified-comparison-stage2-2026-11-15/batch-02-current-checks.json) derive counts from actual case states and record full-438 schema/feasibility, audit, preservation and related checks. Batch 2 has not received a final ten-case QA assessment.

## Browser regression repair

The actual full running-app suite passed **60 desktop/mobile checks**, with zero page errors, on `5df42b776ce49f230b1463a1cacdff53ef5feead` (Actions run `43819609100`; browser step executed). CP113, CP397 and CP263 assertions now accept normal spacing. The downloaded artifact digest, tested text and inspected screenshots are retained in [verification](evidence/qualified-comparison-stage2-2026-11-15/runtime/browser-repair-2026-11-16/verification.json). The later case-only CI skips unchanged browser tests; those skips are not browser-test claims.

## Exact next action

The user authorized two small-batch scheduled workers on 16 November 2026. Follow the [scheduled instructions](deferred-case-qualified-comparison-stage2-scheduling-2026-11-16.md) and the disjoint assignments in `postAuditReviews[0].scheduling` of the active register. Worker A runs at :00 and resumes **CP051**, then CP055. Worker B runs at :30 and starts **CP052**, then CP056. Each execution handles up to two owned unfinished cases; all 13 completed reviews are skipped, including unresolved CP013. Claims and expected-parent publication protect overlapping executions. The old exhausted Restart Corpus A/B tasks remain paused.

CP051's [source and academic checkpoint](evidence/qualified-comparison-stage2-2026-11-15/cp-000051/checkpoint.json) preserves its confirmed first-year core, provisional later teaching and feasible UCR trial. Decide the exact limited-claim materiality question, finish all gates or record a justified unresolved review. Do not repeat exhausted broad searching or infer approval from feasibility.

The existing ten-case batch 2 remains CP013, CP020, CP026, CP051, CP052, CP055, CP056, CP069, CP087 and CP149. Its remaining reviews may be completed by both workers; close its QA only after all ten are reviewed. The overall 61-case scope, case-specific history and evidence remain authoritative.

Use the current assignment, governing Production Instructions, active register and frozen Stage 2 baseline. Preserve all 375 original approvals, CP072/CP099, completed Stage 2 work, unprocessed cases, registry/course/student inputs, Stage 1 metadata and exhausted-worker histories. Use authenticated, fresh-parent, complete-byte, verified fast-forward publication with at most one decision/canonical repair pair per commit. Derive counts from actual cases. Update the checkpoint after progress and publish final batch QA when all ten reviews close.

Only the two new Stage 2 schedules are authorized. No old automation restart, counselor deployment, final discovery product or corpus release is authorized. Publish the final Stage 2 report only after all 61 reviews close.
