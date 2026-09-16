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

The copies in this directory are maintained in GitHub for **human distribution and version control**.

The human operator is responsible for obtaining the required file from the current `main` branch and making it available to the AI system through whatever persistent file-access mechanism that system supports.

For counselor production, the AI must have access to `ucr_courses_enriched.xlsx` before academic production begins. The AI must verify that the file is accessible in its working environment. If it is not accessible, stop and report the missing dependency rather than reconstructing UCR course evidence from memory, public web sources or incomplete substitutes.

Once the human has supplied the file, use that supplied copy throughout the production workstream. Do **not** repeatedly retrieve the workbook from GitHub for individual counselor targets. The human operator is responsible for ensuring that the supplied copy corresponds to the current authoritative GitHub version when the workstream begins.
