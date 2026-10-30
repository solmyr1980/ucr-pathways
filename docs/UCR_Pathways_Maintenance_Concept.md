# UCR Pathways — Incremental maintenance

**Status:** Adopted maintenance approach. This document owns change assessment and reuse; Production Instructions own academic production and the review protocol owns case execution. It does not authorise a refresh, resume a paused audit, change scope or publish/deploy anything.

## Preserve durable assets

Retain permanent programme IDs, normalized source provenance, external curriculum research, programme-interest evidence, explicit academic decisions and canonical records. Compare a proposed update with the latest accepted version before deciding what to redo. Current official evidence still controls academic claims; unchanged storage or a prior approval is not proof of continuing validity.

Routine maintenance is incremental. An explicitly authorised fresh audit overrides ordinary approval reuse within its defined scope, while still preserving independently confirmed material and history.

## Assess the actual change

| Change | Required response |
| --- | --- |
| Administrative name or source URL, academic identity unchanged | Verify identity; update affected metadata/copy and dependent references |
| External curriculum changes materially | Repair its reconstruction and reconsider dependent concepts, alignments and claims |
| UCR offering or prerequisite changes | Check affected schedules; replace courses only when necessary and then reassess their academic dependencies |
| UCR content changes | Reassess its role and claims where used; consider newly supported subject areas |
| New UCR course | Targeted subject-area reassessment, including relevant previous no-match cases |
| Comparison policy changes | Reassess affected alignments/explanations; preserve sound complete curricula |
| Interface or search changes | Rebuild/test the relevant presentation/discovery outputs; preserve academic records |
| Starting cohort changes | Verify the complete planning horizon and reschedule; retain selections that remain feasible |

A material change alters a required component/credit/choice/cohort rule, program-level academic interpretation, course feasibility or a substantive claim. A different but defensible choice is not itself a defect. Broader consequences must follow actual dependencies, not the mere fact that a file hash changed.

## Course-reference comparison

Run `python scripts/validate-course-feasibility.py --compare-workbook <previous.xlsx>` after an authorised deliberate reference regeneration. It reports added/removed courses, changed fields and existing counselor records using changed courses. It does not modify either workbook or academic records. Supply explicit private canonical paths when assessing private student records; do not copy private records into GitHub.

Use the output to define review scope, not to declare every listed record invalid. A use-based report cannot identify all opportunities created by new courses or improved content: separately inspect relevant subject areas and documented gaps in previous no-match cases. Do not automatically regenerate the entire corpus.

## Reuse and verification

Preserve independently valid stage results and record which downstream conclusions changed. Refer to the review protocol’s dependency table rather than maintaining another case procedure here. Do not regenerate programme-interest research merely because search ranking or a UCR offering changed. Maintain registry order/source references across a refresh; the compact decision’s interest-row tokens must not silently resolve to different rows. Reconcile any remapping explicitly and replay affected decisions against their recorded source versions.

Reviewed course descriptions retain the historical workbook blob and selected source/description hashes plus the reviewed course name. Validate current source-field text and name; an unrelated workbook edit does not require refreshing every provenance entry. Changes that conflict with historical outline content require a course-specific judgment and proportionate claims, not automatic restoration of old values.

Future alumni/master’s enrichment remains a separate downstream extension. It may use a completed curriculum without becoming a prerequisite for its construction or forcing regeneration of existing comparisons. Its future plan remains inactive until separately authorised.
