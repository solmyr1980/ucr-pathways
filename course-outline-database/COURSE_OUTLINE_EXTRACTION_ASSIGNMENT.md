# UCR Course-Outline Database — Longitudinal Extraction Assignment

**Status:** Reusable standalone production instruction  
**Version:** 1.0 (27 October 2026)  
**Scope:** Extract all reasonably structured course information from UCR course-outline PDFs, semester by semester.

## 1. Purpose and independence

Build a cumulative, detailed, longitudinal database of courses as they were described and taught in each semester. The database should support curriculum research, course comparisons, teaching and assessment analysis, institutional reporting, and other future uses, including UCR Pathways. It is **not** a UCR Pathways production record or a course-feasibility judgment.

**The uploaded course outlines are the sole substantive evidence.** Do not use a course catalogue, curriculum register, existing enriched course database, prior semester's outlines, institutional website, another Excel file, or general knowledge to complete, verify, correct, or enrich the contents of a new course outline. A previously generated copy of **this database workbook** may be used only to preserve and append historical records, never as evidence to fill gaps in a new outline. If no existing workbook is provided, create one.

Extract extensively. Prefer retaining potentially useful detail to discarding it, but do not invent information and do not transform a weak mention into a strong claim.

## 2. Inputs and authoritative identifiers

Each run receives a folder or ZIP archive of PDF course outlines for one semester. The archive or supplied root-folder name supplies the authoritative semester; each PDF filename supplies the authoritative course code and group number.

- If the input is a ZIP, derive the semester from the **ZIP filename**, not an internal folder or text printed in a PDF. If the input is a folder, derive it from the **supplied folder name**. Retain the original container name in the batch report.
- Accept a name such as **outlines_2026h2.zip** or **2026h2/** when it contains exactly one unambiguous semester token of the form **YYYYh1** or **YYYYh2**. The resulting semester value is **2026h2**. Do not infer a semester from the PDFs when the name is unclear; report a blocker.
- For a PDF named **ACCPPDE1012.pdf**, set **course_code = ACCPPDE101** and **group_number = 2**: the final digit of the filename stem is the group number, and every preceding character is the course code. Retain **ACCPPDE1012.pdf** as **source_filename**.
- Apply the same rule to every PDF. Do not strip other digits from the course code and do not use the code or group stated inside the outline to determine identity.
- Keep the PDF's internally printed code, semester, group, or title as *reported outline content*, if present. They are not authoritative identifiers. Record material discrepancies without correcting either source.
- One PDF represents one **course–semester–group** offering. Its unique key is therefore **(semester, course_code, group_number)**. A course–semester pair alone is not unique when there are several groups. Use all three key fields in every worksheet.
- Two PDFs that resolve to the same key must not be silently combined or overwritten. Flag the collision, identify the files, and retain all other unambiguous records.
- Ignore ZIP housekeeping entries and non-PDF files. Record unreadable, protected, scanned, malformed, or ambiguously named PDFs as exceptions; continue processing the remainder.

For the supplied example, the archive **outlines_2026h2.zip** includes two outlines named **ACCPPDE1011.pdf** and **ACCPPDE1012.pdf**. These are separate records of course **ACCPPDE101**, semester **2026h2**, groups **1** and **2**.

## 3. Extraction principles

1. **Read the whole PDF**, including tables, appendices, schedules, rubrics, policies, and supplementary instructions. Do not stop after the introductory pages. Inspect page layouts where text extraction can misorder columns or table rows.
2. **Extract what is there, not what ought to be there.** Do not repair typographical errors, contradictory dates, implausible policies, or nonstandard statements using outside knowledge.
3. **Verbatim fields** reproduce the relevant original words, order, spelling, punctuation, numbers, qualifications, and substantive paragraph boundaries. Remove only mechanical artifacts of PDF extraction, such as line-wrapping that has split a word. Never silently paraphrase or rewrite a verbatim passage.
4. **Structured factual fields** report explicit outline evidence. Extract a numeric weight, date, duration, title, role, room, or contact detail only where the text supports it; preserve the source wording in its corresponding verbatim field where specified.
5. **Analytical fields** (e.g., topics, disciplines, theories, methods, skills, tools, applications, and content summary) may synthesize explicit evidence from any part of that *same* outline. Use concise, specific English terms; do not overinterpret a passing reference. Coverage should be high-recall, not limited to five keywords. List multiple items using a consistent **semicolon + space** separator.
6. **Distinguish missing from zero or none.** Leave an unsupported field blank. Write zero only when explicitly indicated. Do not infer course characteristics from the course code, title, or disciplinary expectations.
7. **Preserve internal inconsistencies.** The ZIP/folder and filename win only for the authoritative key. The PDF's conflicting claims still belong in outline fields and the discrepancy note.
8. **Do not invent linked relationships.** For example, link a learning outcome to an assessment only if the outline actually makes that connection.
9. **Do not deduplicate away distinct information** within a PDF. Where similar entries differ in wording, deadline, scope, material, session, or assessment requirement, retain the distinction.
10. **Make the output reusable outside UCR Pathways.** Do not add Pathways clusters, suitability judgments, synthetic student interests, comparator matches, or external curricula.

## 4. Workbook contract

Return one **flat, unformatted .xlsx workbook** containing exactly the seven worksheets below, in this order. Each sheet has one header row, ordinary cell values, and no merged cells, decorative formatting, formulas, filters, or hidden data. Use lower-case snake_case column names exactly as listed.

All seven worksheets begin with **semester, course_code, group_number**, in that order. Within each sheet, the remaining columns follow the order shown. The unique main record is keyed by those three fields; subsidiary tables use the key plus their own sequence number.

### 4.1 Worksheet: courses

**One row per authoritative course–semester–group.**

Identification (ordered first):
- semester, course_code, group_number, course_title, course_subtitle

Source and verification:
- source_filename, outline_course_code, outline_semester, outline_version, source_page_count, source_file_hash, source_discrepancy_note

Curriculum:
- cluster_or_track_information, prerequisites_verbatim, recommended_background, special_entry_requirements

Academic content:
- course_description_verbatim, course_objectives, content_summary, disciplinary_fields, substantive_topics, theories_and_concepts, research_methods, other_methods_and_techniques, academic_and_practical_skills, software_and_tools, applications_and_contexts

Teaching arrangements:
- classroom, class_times, teaching_format, course_organization_verbatim, student_preparation_requirements

Study load:
- credits_ec, contact_hours_per_week, preparation_hours_per_week, study_load_verbatim

Course requirements:
- attendance_policy, absence_policy, participation_requirements, late_submission_policy, communication_policy, academic_integrity_policy, ai_use_policy, accommodation_provisions, fieldwork_or_excursion_requirements

Assessment and feedback:
- assessment_overview_verbatim, grading_policy, feedback_policy, resit_or_reassessment_policy

Catch-up week:
- catch_up_week_text_verbatim, catch_up_week_evidence_type, catch_up_week_source_page

Other:
- additional_course_requirements, extraction_notes

**Interpretation notes.** Keep course_title and course_subtitle as stated in the PDF, even if the filename suggests another title. The course objectives are separate from the formal learning outcomes in sheet 5 when the outline makes that distinction. credits_ec, contact_hours_per_week, and preparation_hours_per_week are numeric when explicitly stated; do not calculate an unstated weekly workload from timetables. source_page_count is the actual PDF page count. source_file_hash is the PDF's SHA-256 checksum in hexadecimal. The semester and course code shown inside the PDF belong exclusively in their outline_* fields, never in the authoritative key.

### 4.2 Worksheet: instructors

**One row per identifiable instructor, co-instructor, or teaching contact**, keyed by the three identifiers plus instructor_number.

Columns, in order:
- semester, course_code, group_number, instructor_number, instructor_name, instructor_role, email, telephone, office_location, office_hours

When contact details cover multiple instructors jointly and cannot be attributed confidently, do not assign them to an individual by guesswork; retain the complete contact statement in additional_sections, and explain the unresolved attribution in extraction_notes.

### 4.3 Worksheet: assessments

**One row per distinct formally specified assessment component**, keyed by the three identifiers plus assessment_number.

Columns, in order:
- semester, course_code, group_number, assessment_number, assessment_name, assessment_type, assessment_description_verbatim, assessment_weight_percent, assessment_deadline, assessment_format, individual_or_group, submission_requirements, ai_index_level, assessment_criteria_verbatim, grading_rubric_verbatim

Include exams, papers, quizzes, presentations, group projects, portfolios, participation marks, and other graded components as supported. Retain zero-weight or explicitly ungraded assessment components when the outline presents them as formal assessments, identifying their actual status. Do not create a separate component for every mention of the same assignment in the schedule. Keep relative deadlines verbatim rather than assigning invented calendar dates. assessment_weight_percent is numeric only when explicitly available; do not force components to sum to 100 when the outline does not.

### 4.4 Worksheet: course_schedule

**One row per separately identifiable scheduled session or other defined teaching period**, keyed by the three identifiers plus schedule_row_number.

Columns, in order:
- semester, course_code, group_number, schedule_row_number, week_number, session_number, period_verbatim, session_date, session_time, topic_verbatim, activities_verbatim, course_materials_verbatim, assignments_verbatim, assessments_verbatim, class_status, catch_up_week_indicator, additional_schedule_notes

Preserve the granularity of the schedule: do not split a multiweek period into invented sessions, or merge separately scheduled sessions. If the outline gives weeks rather than exact dates, keep week_number when explicit and leave session_date blank. class_status may retain an explicit status such as cancelled, independent work, no class, or holiday; do not infer that a blank date is a cancellation. catch_up_week_indicator is true only where the schedule explicitly identifies the row as catch-up week (or an unambiguous spelling variant), false where the row explicitly describes a different period, and blank where it cannot be determined.

### 4.5 Worksheet: learning_outcomes

**One row per separately stated student learning outcome**, keyed by the three identifiers plus outcome_number.

Columns, in order:
- semester, course_code, group_number, outcome_number, learning_outcome_verbatim, period_or_week, teaching_and_learning_activities, assessment_methods, additional_outcome_notes

Preserve formal outcome numbering and wording where possible, while outcome_number provides a sequential database key. Where an outline presents an outcome-to-teaching-to-assessment matrix, retain the explicit associations in the same row. Where it provides only outcomes, leave the related columns blank rather than reverse-engineering a mapping.

### 4.6 Worksheet: course_materials

**One row per distinct identifiable learning resource**, keyed by the three identifiers plus material_number.

Columns, in order:
- semester, course_code, group_number, material_number, material_category, required_or_recommended, reference_verbatim, authors, publication_year, title, edition, publisher, url_or_identifier, assigned_chapters_or_sections, material_notes

Include required and recommended textbooks, articles, book chapters, podcasts, films, websites, datasets, software, and other explicitly specified resources. Preserve bibliographic entries exactly in reference_verbatim, including incomplete ones. Parse bibliographic components only when evident; do not complete references by searching externally. Generic instructions such as "additional readings on Moodle" can be one resource-level row with unparsed reference text, not fabricated individual readings. Scheduled readings may be linked through the course_schedule description without inventing a separate citation.

### 4.7 Worksheet: additional_sections

**One row per substantive, identifiable section or appendix that the other tables do not preserve sufficiently**, keyed by the three identifiers plus section_number.

Columns, in order:
- semester, course_code, group_number, section_number, section_heading_verbatim, section_category, section_text_verbatim, source_page_start, source_page_end

Use this sheet to retain significant residual source material: special instructions, policies, detailed assignment briefs, field-trip rules, extended rubric appendices, course-specific forms, unusual matrices, or other sections that exceed or evade the standardized columns. A section may also be retained here when its full wording or layout matters beyond the details extracted into other sheets. Do not duplicate every ordinary section mechanically, but do not discard substantive text simply because it does not fit an anticipated category.

## 5. Mandatory catch-up-week extraction

This is a **priority verbatim extraction**, independent of whether catch-up week is described as prose, a timetable row, or both.

- Search the **entire PDF** for catch-up week and close orthographic variants (e.g., catch up week, catch-up, catchup) and inspect all relevant schedule cells and policy text.
- In **courses.catch_up_week_text_verbatim**, reproduce **every distinct passage explicitly concerning catch-up week**, not a summary. Include the complete relevant paragraph, list item, or schedule-cell statement, preserving its qualifications about activities, make-up work, attendance, or assessment.
- When references are noncontiguous, place the verbatim excerpts in their original document order, separated by a blank line. Do not insert invented wording inside the excerpts.
- In **catch_up_week_evidence_type**, use exactly one value: **dedicated_prose**, **schedule**, **both**, or **not_mentioned**. Use **both** if relevant prose and timetable material occur separately.
- In **catch_up_week_source_page**, list all relevant actual PDF page numbers, separated by semicolons. This is a source-location aid, not part of the quotation.
- In **course_schedule**, also retain the corresponding catch-up rows at their original level of detail and set catch_up_week_indicator accordingly.
- If no explicit catch-up-week reference exists, leave the verbatim text and page fields blank and set the evidence type to **not_mentioned**. Do **not** assume a standard catch-up week, infer one from the semester calendar, or substitute a general absence/reassessment policy.
- Visually recheck the extracted passage against the PDF when text flow, tables, OCR, or page breaks make exact quotation uncertain. Report any part that cannot be recovered reliably.

## 6. Parsing and representation

- Maintain the order in which instructors, assessments, sessions, outcomes, materials, and additional sections first appear in the outline. Number the rows **1, 2, 3, ...** within each course–semester–group key and each child sheet.
- Preserve words and punctuation in *_verbatim fields. Do not quietly translate Dutch or other-language source text; analytical summaries may be in English.
- Use **ISO dates (YYYY-MM-DD)** only when the day, month, and year are explicit and unambiguous. Otherwise use the source wording in the appropriate verbatim or notes field. Do not infer dates from week numbers or the semester label.
- Use numeric Excel cell values for explicitly stated credit, percentage, weekly-hour, row-number, and page-number fields. Do not silently convert ambiguous units; explain them in the related notes or verbatim field.
- For a field containing multiple analytical terms, use **semicolon + space** consistently. Preserve full source prose as paragraphs rather than forcing it into keyword lists.
- For materials, assessments, and schedule information split across several pages, combine all relevant parts before extracting individual records. A page break is not a new assessment or learning resource.
- Treat unreadable figures and tables as a reporting issue. Do not mark a field missing merely because automatic PDF text extraction skipped text that is visibly on the page.
- Excel cells have a maximum of 32,767 characters. Do not silently truncate any text. When a retained passage exceeds that limit, split it into ordered, non-overlapping chunks in **additional_sections**, clearly label the chunks and source-page spans, and leave an extraction_notes explanation rather than inserting an incomplete excerpt into the nominal column.

## 7. Incremental production and protection of history

1. If an existing workbook from earlier runs of **this same assignment** is provided, verify its seven sheet names, columns, and composite keys. It is the cumulative output, **not an additional source**.
2. Preserve every accepted historical row and cell unchanged. Never re-research, normalize, reorder, or replace earlier records merely for consistency.
3. Process all valid PDFs in the supplied new batch, including separate groups of the same course. Append records absent from the cumulative workbook.
4. When an incoming key already exists:
   - If its PDF checksum matches the stored source_file_hash, treat it as a previously processed duplicate; make no change.
   - If the checksum differs, report a **source revision conflict**. Do not overwrite the existing course or subsidiary rows without explicit authorization and a versioning decision.
5. Process independent outlines even when other files are blocked. Track skipped files and reasons; do not invent placeholder course records.
6. Never filter records by programme usefulness, student eligibility, administrative status, level, academic subject, or relevance to UCR Pathways. The archive defines the input population.

## 8. Quality control before returning the workbook

Perform a systematic check of the new batch:

- Count archive PDFs, successfully processed source files, existing duplicates, collisions, and unresolved exceptions.
- Verify every semester, course_code, and group_number **against its authoritative container and filename**; never against headings inside the PDF.
- Confirm one unique **(semester, course_code, group_number)** in courses for each successfully processed distinct PDF.
- Confirm every subsidiary row refers to exactly one courses key; no orphan or duplicate child sequence numbers.
- Check the required sheet and column names and their order; verify all prior rows remain byte-for-byte equivalent in cell values to the input workbook.
- Inspect the first, middle, and final portions of each outline, its schedule, and its appendices. Check extraction completeness across long and short PDFs alike.
- Reconcile every separately stated learning outcome, assessment component, and explicitly named resource with the appropriate child table; check that the original wording has not been fabricated or editorially corrected.
- Check reported assessment weights, credits, dates, and hours against actual document evidence without forcing consistency.
- Recheck **every catch-up-week verbatim text against the PDF**, including table rows and multiple mentions. Verify page numbers and the evidence classification.
- Check that substantive unusual sections are either captured in standard fields or retained in additional_sections.
- Identify issues such as contradictory internal codes, incorrect printed semesters, irregular templates, illegible scans, and incomplete matrices in the discrepancy or extraction notes rather than repairing them.
- Check for Excel cell-length truncation and ensure the workbook opens normally as a plain seven-sheet .xlsx file.

## 9. Deliverables and report

Return **(1)** the updated cumulative Excel workbook and **(2)** a short processing report with:

1. The authoritative semester, input container name, and number of PDF files discovered.
2. The course–semester–group keys processed and counts of new, already-present, and blocked records.
3. New-row counts for **each of the seven worksheets**.
4. Catch-up-week coverage: number classified dedicated_prose, schedule, both, and not_mentioned.
5. Only material anomalies, conflicting revisions, illegible passages, and unresolved blockers, with filenames and affected fields.

Do not demand routine approval during extraction and do not begin another semester until this run is finished. Unless specifically instructed otherwise, **never upload the course-outline PDFs or their extracted workbook to a public GitHub repository**. The repository stores this reusable assignment, not the underlying teaching documents or personnel details.

## 10. Boundaries and future development

This assignment is exclusively for **extraction and structured documentation**. It does not judge pedagogical quality, harmonize curricula, validate prerequisites against external rules, recommend courses, map courses to careers, or construct UCR Pathways programmes. Those are separate downstream uses.

The seven-sheet schema is the baseline for all semesters. When a genuinely recurrent source field cannot be represented adequately, **propose a documented schema revision** rather than inventing columns mid-batch. Apply approved structural changes consistently to the future production contract without silently rewriting historical source values.
