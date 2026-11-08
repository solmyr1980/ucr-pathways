# Master's admissions database instructions

## Scope and location

Build an admissions database for Dutch research-university master's programmes. Start with programme identity from DUO/RIO and verify the programme, specialisation, applicant category and intake against the university's own admissions information. Record published admissions rules and their sources. Keep admissions research and its outputs in `research/masters-admissions/database/`.

The existing files one directory up are pilot evidence. Use them as a starting point and preserve their history. The production workbook is `master_admission_requirements.xlsx` in this directory. Use one plain worksheet, `admission_requirements`, with one row per admission condition. Repeat programme and route information on each row. Keep the workbook flat, with one header row and no merged cells, formatting, formulas or cross-sheet references.

Linking admissions to UCR courses or curricula, counselor comparisons and student records belongs to a later phase. Changes in this phase belong in this directory. Follow the root repository rules for work on `main` and publication.

## Workbook columns

Use these columns in the order shown.

| Column | What to enter |
| --- | --- |
| `programme_id` | Stable identifier for the programme or separately assessed specialisation. Reuse pilot IDs where the identity matches. |
| `university` | Official university name. |
| `programme_name` | Official master's programme name. |
| `rio_code` | DUO/RIO recognised programme code, or parent code for a variant. Keep it as text. Leave blank if it cannot be verified. |
| `specialisation` | Official name when the row applies to a specific specialisation. |
| `intake` | Entry year and month as text, such as `2027-09`. Use `unstated` when the source does not establish the applicable intake. |
| `route_id` | Stable identifier within the programme for this route. |
| `route_name` | Short name for the published route. |
| `applicant_scope` | Prior qualification or applicant category to which the route applies. |
| `route_outcome` | `direct_eligibility`, `individual_assessment` or `bridge`. Explain any qualification in the relevant condition row. |
| `condition_id` | Stable identifier within the programme, route and intake. |
| `condition_type` | `required`, `selection`, `recommended`, `conditional_outcome` or `information`. |
| `subject` | What the condition concerns, such as academic writing, statistics or English language proficiency. |
| `operator` | `min`, `max`, `equal`, `approx` or `lookup` when applicable. |
| `value` | Numeric threshold when published. Leave blank for rules without a numeric value or for an external lookup. |
| `unit` | Unit of the threshold, such as `EC`, `GPA (1–10)` or `GMAT score`. |
| `condition` | Short paraphrase of the rule, including any trigger, exception or outcome needed to interpret it. |
| `source_rule` | Faithful record of the operative published rule. Keep the exact thresholds, units, qualifications, exceptions, and relationships needed to reconstruct it. A precise paraphrase is sufficient. Include the path relative to the workbook and section when the rule relies on retained evidence. |
| `accepted_evidence` | Evidence the university says it will consider, such as course descriptions, assessed writing or a named test. |
| `choice_group_id` | Identifier for a choice between options within the same route. |
| `option_id` | Identifier for one option within that choice. Give each condition in the same option the same identifier. |
| `credit_pool_id` | Identifier shared by requirements and caps that apply to the same pool of courses. |
| `assessment` | `explicit`, `individual_review`, `not_published` or `unverified`. |
| `source_url` | Official source supporting the condition. |
| `source_section` | Heading, page, article or table that locates the rule. |
| `supporting_source_url` | Second official source when it adds detail, qualifies the rule or conflicts with it. |
| `supporting_source_section` | Location of the relevant material in that second source. |
| `verified_on` | Date the sources for the row were checked, as `YYYY-MM-DD`. |

## Recording rules

- Use separate routes for materially different eligibility paths. For example, a named degree route, assessment of another Dutch WO degree, and a pre-master route can all lead to the same programme. Keep requirements attached to the applicable route and intake. Repeat a common rule in each applicable route.
- Required conditions without a choice group apply together within the route. Within a choice group, one complete option is sufficient. Conditions belonging to the same option apply together. The old GMAT option, for example, has one row for the total score and another for the writing score.
- Use the same credit pool identifier for a minimum and a cap that apply to the same coursework. For example, UvA's 60 EC subject minimum and 12 EC cap on introductory coursework constrain the same pool.
- Keep recommendations, selection factors and conditional outcomes separate from minimum eligibility conditions. Use `approx` only when the university describes a figure as indicative or approximate. Record a published score matrix as a `lookup` and link to the exact table. Record any separate effect of a higher score on a `conditional_outcome` row.
- Use `individual_review` when the university explicitly leaves a decision to its admissions committee. Use `not_published` when the relevant official information was found and gives no rule on the point being recorded. Use `unverified` when evidence is missing, inaccessible or conflicting. Identify the open point in `condition`.
- Use programme-specific official sources and the applicable applicant category. Check formal regulations or linked checklists where they qualify the admissions page. Record the stated intake separately from the date checked. Preserve the applicable cycle and record any unresolved discrepancy. Keep earlier verified intake rows when the rules change for a new intake.
- Capture source evidence at extraction. Preserve a dated factual extract or a checked transcription in `evidence/` when a linked table, named list, checklist, or complex clause cannot be reconstructed from the row. Record the official URL, locator, date checked, and applicable cycle when stated. Save only the relevant material. For a conflict, retain each source's position and its scope. For inaccessible material, identify the missing detail and mark it unresolved if it can affect the outcome. Preserve earlier evidence versions when a source changes.
- For each programme, track and intake, review every route in the declared applicant scope against the official sources before marking collection complete. Check the prior qualification, academic conditions, accepted evidence, language, selection, deadlines, application or enrolment conditions, and any bridge. Capture the trigger and limits of each exception or remedy, including nonacademic restrictions. Keep AND/OR combinations explicit. Record how credit pools relate, including any published rules for overlapping or double-counted credits. Record silence on a consequential point without inferring a policy.
- Reconcile reviewed programmes against the scoped programme list. Keep an explicit record of any route or consequential detail whose source cannot be verified. Use an information row for a gap where the source and the affected route can be identified. A deliberately selected test slice is partial coverage.
- Before marking a production batch complete, have a second reviewer independently compare the workbook with the official admissions sources for the declared scope. Check for missing routes, conditions and exceptions. Correct omissions and record any points the reviewer cannot verify under the rules above.
- Keep UCR course matches and applicant eligibility judgments out of this workbook.

## Pilot reconstruction checks

Use the original four cases and the additional stress tests to validate collection before scaling.

| Pilot case | Rule the flat rows must reproduce |
| --- | --- |
| MA-04, Erasmus Social Inequalities and Change | The 7.5 EC methods minimum applies to the assessed route. The named Sociology degree has a separate route. |
| MA-22, UvA New Media and Digital Culture | The 60 EC subject minimum and 12 EC introductory cap constrain the same credit pool. |
| MA-08, Maastricht Work and Organisational Psychology | The 10 EC academic writing requirement is explicit. The recognised credit amount can remain unresolved when evidence is incomplete. |
| MA-32, Maastricht International Business, Strategy and Innovation | The portfolio and test options are alternatives. The old GMAT option has both a total-score and a writing-score threshold. The GRE option uses an official matrix. |

Reconstruct each rule from the rows and test at least one boundary or unresolved case. Check that identifiers are unique at the stated level, repeated programme and route fields are consistent, choices and credit pools are intact, and each condition has a verifiable source and location.

| Stress test | Rule to reconstruct from the saved record |
| --- | --- |
| MA-07, Radboud Cognitive Neuroscience, Perception, Action and Decision-making | One complete subject combination is required. A pair drawn from different alternatives does not satisfy the track requirement. Competitive selection remains separate. |
| MA-28, Utrecht Social, Health and Organisational Psychology | The named UCR route and general assessment are distinct. The two discretionary remedies address different gaps. Apply the housing and study-residence-permit restrictions to the pre-master route. |
| MA-32, Maastricht International Business, Strategy and Innovation | Reproduce the GRE matrix outcomes and exact named qualifications from retained evidence, including the distinction between board review and conditional automatic admission. |

Have a second reviewer reconstruct the tested rules from the worksheet and retained evidence without opening the live sources. Check an eligible case, a near miss and an unresolved case where applicable. Record the tested scope and any remaining coverage gaps before expanding.
