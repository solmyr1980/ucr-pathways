# UCR course reference files

This directory contains the repository copies of the UCR course datasets used by UCR Pathways.

## Files

### `ucr_courses.xlsx`

Base UCR course dataset. It contains the shared course fields used for course identity, descriptions, prerequisites, labels/classification and planned semester availability.

Use it when a task requires only the base course data. Do **not** substitute it for the enriched dataset when academic course selection, interpretation or counselor-production feasibility requires the enriched evidence.

### `ucr_courses_enriched.xlsx`

Enriched UCR course dataset. It contains the same base course fields plus the enrichment fields `outline_source`, `outline_semester`, `enrichment_basis`, `profile`, `discipline`, `topics` and `methods`.

For counselor production, this is the authoritative UCR course-evidence dataset for course selection, academic interpretation, scheduling and feasibility assessment.

## AI access rule

The files in this directory are the authoritative repository copies.

For counselor production, the AI must retrieve `data/reference/ucr_courses_enriched.xlsx` directly from the current GitHub `main` branch and verify that it is readable before academic production begins. Do not require a separate upload, Project Source copy or other human-provided duplicate.

Use the retrieved GitHub copy throughout the production workstream. Retrieve it again only when repository changes may have altered it. If the file is unavailable or unreadable, stop and report the missing dependency rather than reconstructing UCR course evidence from memory, public web sources or incomplete substitutes.
