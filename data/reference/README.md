# UCR course reference

`ucr_courses_enriched.xlsx` is the single authoritative course reference for UCR Pathways, used by both student and counselor production. It contains one row per active course, keyed by `osiris`. There is no separate base-course workbook.

## Sources and field ownership

| Source | Authoritative fields |
| --- | --- |
| Central BOS database | Active course identities, `osiris`, official `name` and `description2`, department/track classifications and labels, and formal `preq1` prerequisites. |
| YearPlan | Planned availability in the semester columns named `YYYYh1` or `YYYYh2`. |
| Cumulative [course-outline database](../../course-outline-database/README.md) | Selected `outline_source`, `outline_semester`, `profile`, `discipline`, `topics` and `methods`. |

During a deliberate regeneration, retain the active BOS course set and join sources by `osiris`. For each course, select the most recent available `outline_semester` and, within that semester, the lowest numeric `group_number`. Copy the selected row's evidence and provenance together; do not combine content across groups or semesters. Historical outlines do not override current official attributes or establish future offerings.

Where no outline exists, leave the six outline-derived fields blank. The official `description2` remains available for academic use under Production Instructions Section 2.2; do not generate replacement enrichment from it. `enrichment_basis` has been discontinued and `CRG` is absent from the current reference. Missing official descriptions must remain missing rather than being restored from superseded data or silently filled with outline prose.

For GOSHIST312, use the official `description2` and leave all six outline-derived fields blank by user decision of 30 October 2026. The archived Walcheren outline does not establish the content of the current course, Researching the “American Century”. Preserve that historical outline in the cumulative database, but exclude it from deliberate Pathways regenerations unless a suitable current outline is accepted or the user revises this decision.

The extraction workbook retains all accepted course–semester–group records and their source hashes and limitation notes. Its `outline_semester`, `osiris` and `outline_source` identify the selected source when a material ambiguity needs review. Extraction and Pathways regeneration remain separate: appending new outlines does not update this workbook automatically. Assess the latest-semester/lowest-group selection against the extraction input used for the deliberate merge, rather than treating a later outline append as an invalidation of the existing reference.

Use `python scripts/validate-course-feasibility.py <canonical.json>` to verify explicit schedules against this workbook during academic production. Use its `--compare-workbook <previous.xlsx>` option for a read-only field-change/impact report after deliberate regeneration; new or changed content also needs targeted subject-area judgment beyond records that already use the course. Neither command edits the reference or makes academic selections.

Read planning coverage from the actual semester columns. Within a covered term, `X` means planned availability and a blank cell means no planned offering. A missing term column supplies no planning evidence. Production Instructions Section 2.2 owns the academic evidence and feasibility rules, including treatment of an insufficient horizon; the Master Specification owns the customer-facing content boundary.

## AI access rule

Retrieve `data/reference/ucr_courses_enriched.xlsx` directly from current GitHub `main` and verify that it is readable before course-level academic production begins. Do not require a separate upload, Project Source copy or other human-provided duplicate.

Use the retrieved copy throughout the workstream. Retrieve it again only when repository changes may have altered it. If it is unavailable or unreadable, stop and report the missing dependency rather than reconstructing UCR course evidence from memory, public web sources or incomplete substitutes.
