# UCR Course-Outline Database — Targeted Extraction Assignment

**Status:** Reusable standalone production instruction  
**Version:** 2.1 (29 October 2026)

**Purpose:** Maintain a focused, longitudinal record of the academic substance of UCR courses, extracted from course outlines alone.

## 1. Scope and independence

The course-outline database is a **separate source dataset**, not the central course database and not the enriched UCR Pathways course database. Its main downstream use is to improve the substantive course evidence used for course selection and academic comparisons in UCR Pathways.

**Use only the supplied course-outline PDFs as substantive evidence.** Do not retrieve, consult or use the central course database, a previously enriched course file, prior-semester outlines, course catalogues, university websites or general knowledge to complete the extraction. Existing rows in this *same* accepted extraction database may be used only to maintain historical records and detect duplicates, never to fill gaps in a new outline.

The extraction stage does **not** merge, replace or verify central attributes such as official course title, cluster/track, course requirements, formal prerequisites, active status or planned semester availability. A **separate downstream enrichment stage** joins relevant extracted content with centrally maintained course attributes. This separation is deliberate: preserve what the outline says, then reconcile it only when producing the Pathways-enriched database.

## 2. Inputs and record identity

Receive a folder or ZIP archive of PDF course outlines for one semester.

- Take the authoritative semester from the supplied ZIP filename (or the supplied root-folder name), using exactly one unambiguous token of the form `YYYYh1` or `YYYYh2`.
- Take the authoritative course code and group number from each PDF filename. For `ACCPPDE1012.pdf`, use `osiris = ACCPPDE101` and `group_number = 2`. The last digit is the group number; the preceding characters are the course code.
- Use the composite key `(outline_semester, osiris, group_number)`. Separate groups are separate source records even when most text is identical.
- Retain the course title as printed in the outline for identification and verification, not as an authoritative central-course title.
- Do not repair a conflict between the filename/container and the contents of a PDF. Keep the authoritative key and describe material differences in `source_discrepancy_note`.
- Process all valid PDFs in the supplied collection, including less directly relevant courses. Skip unreadable or ambiguously named files with an explicit exception; continue with the rest.

## 3. Output: one flat file

Maintain **one cumulative, plain, unformatted Excel workbook** at:

`course-outline-database/UCR_Course_Outline_Database.xlsx`

It contains **one worksheet named `courses`, one header row, and one row per course–semester–group offering**. No extra worksheets, nested tables, formulas, merged cells, filters, decorative formatting or hidden content. Preserve the column names and order below.

| Column | Content |
| --- | --- |
| `outline_semester` | Semester from input container |
| `osiris` | Course code from filename |
| `group_number` | Final filename digit, numeric |
| `course_title` | Course title reported in PDF |
| `profile` | Accurate, concise description of what the course substantively studies and does |
| `discipline` | Academic disciplines or substantive disciplinary subfields genuinely represented |
| `topics` | Distinct, meaningful concepts, questions, subject areas and phenomena covered |
| `methods` | Specific research, analytical, technical or practical methods substantively taught or applied |
| `outline_source` | Exact PDF filename |
| `source_file_hash` | SHA-256 of the source PDF |
| `source_discrepancy_note` | Material conflicts within the PDF or between its identity and the authoritative key |
| `extraction_notes` | Only unresolved source ambiguities or limitations materially affecting the four content fields |

Use semicolon + space to separate multiple items in `discipline`, `topics` and `methods`. Keep blank any field the source does not support. Do not populate fields with “none” or invented content to give an impression of completeness.

## 4. Extract academic signal, not document inventory

Read the **whole PDF**, using its description, objectives, learning outcomes, substantive schedule, assessment briefs and readings as evidence where they reveal actual course content. Inspect tables visually when extraction order is uncertain. **Do not transcribe these sections as separate data**: they are evidence for the four content fields.

### `profile`

Write a focused, source-faithful academic account, normally one concise paragraph. Identify the main intellectual subject, important themes, and relevant methodological or applied dimensions. Make the central emphasis visible and describe narrower components in proportion to their actual role.

Do not merely repeat promotional wording, list classes chronologically, or foreground a one-off topic as a defining course theme. Distinguish courses that *introduce*, *examine*, or *teach students to apply* an area or method. Preserve important distinctions in scope and depth.

### `discipline`

List fields substantially represented by the course. Include meaningful interdisciplinary combinations when the outline establishes them. Do not infer a field from the course code or assume that a passing example makes the course part of that discipline.

### `topics`

List **academic content**, not timetable events. Use precise terms grounded in the outline: concepts, substantive questions, fields, phenomena, and applications studied to a meaningful degree. Exclude quizzes, spare sessions, reading weeks, guest lectures as events, excursions as events, assignment deadlines and generic phrases such as “links”, “understanding”, “research” or “critical thinking”.

Do not mechanically turn every session title or cited reading into a topic. A single class, case or illustrative example does not justify disproportionate weight in the profile or topics list. Include narrower topics where their substantive treatment is clear; do not impose an arbitrary count or quota.

### `methods`

List identifiable methods actually taught or used substantively, such as statistical modelling, case-law analysis, ethnography, laboratory techniques, textual analysis or software-based analytical approaches, **only when supported by this outline**. Generic course activities such as group work, presenting or attending lectures are not methods for this purpose.

Distinguish substantive methodological training from an incidental mention or a method that students merely encounter as a case. Leave the field blank when the outline offers no defensible method.

## 5. Quality checks

For **each** course, before acceptance:

1. Check that the key matches the container and PDF filename, the source hash is recorded, and no duplicate composite key is introduced.
2. Compare the `profile`, `discipline`, `topics` and `methods` directly with the actual PDF. Check for missing major content and unsupported additions.
3. Check that the profile reflects the **relative importance** of substantive strands; one mention must not be promoted into a central course characteristic.
4. Remove scheduling artifacts, generic wording and near-duplicates from topic/method lists. Ensure terms are genuinely useful for selecting courses and substantiating Pathways comparisons.
5. Record material conflicts and genuine uncertainties without silently correcting the source. Leave unsupported fields blank.
6. Ensure the workbook has one unformatted sheet, stable columns, no duplicate keys, and all historical accepted rows remain unchanged.

Review the earliest, middle and latest outlines in a batch with the same care. Do not let extraction quality decline over the batch.

## 6. Incremental publication

- When there is no accepted workbook in the repository, create the new one-sheet workbook from the supplied input. For subsequent runs, retrieve the current accepted workbook from `main` and append new distinct keys without rewriting accepted rows.
- If an incoming key already exists with the same `source_file_hash`, leave it unchanged. If its checksum differs, report a source revision conflict and do not replace it without an explicit decision.
- Publish the updated workbook to the **same stable path** on `main`. Do not generate separate workbooks for each semester. Keep the `README.md` coverage note current.
- In the run response, briefly report the processed semester, input container, numbers processed/skipped/already present, and any material unresolved issues. **No separate processing-report file is required.**
- Follow the repository `AGENTS.md` rules: inspect the current remote `main` before writing, preserve concurrent changes and publish one atomic fast-forward commit. Never commit the source PDFs or ZIP unless explicitly asked.

## 7. Separate downstream merge

The extraction workbook remains **outline-only evidence**. The separate Pathways enrichment stage joins accepted content by `osiris` to BOS course attributes and YearPlan planned availability. Its source ownership and deterministic outline-selection rule are defined in [`../data/reference/README.md`](../data/reference/README.md).

The downstream merge selects outline evidence under that rule; extraction preserves every accepted course–semester–group record. Outline evidence must not overwrite central attributes or be treated as a guarantee of future content. This extraction assignment does not modify the Pathways-enriched database or regenerate academic records.

If a future use requires another attribute, add it **only after identifying that concrete need**, rather than resuming comprehensive extraction.
