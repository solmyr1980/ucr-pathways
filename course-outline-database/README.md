# UCR Course-Outline Database

The database records UCR courses as described in their course outlines, semester by semester. It is a standalone longitudinal source-data resource that can support curriculum research, institutional analysis, and UCR Pathways.

## Permanent files and locations

| Location | Purpose |
| --- | --- |
| [UCR_Course_Outline_Database.xlsx](UCR_Course_Outline_Database.xlsx) | The single cumulative database, updated in place as batches are added. |
| [COURSE_OUTLINE_EXTRACTION_ASSIGNMENT.md](COURSE_OUTLINE_EXTRACTION_ASSIGNMENT.md) | Governing extraction instructions, seven-sheet schema, and validation requirements. |
| [reports/](reports/) | Dated processing reports for individual input batches. |

The workbook filename has no semester suffix. Earlier workbook versions remain available through Git history; do not create a separate database workbook for each semester.

## Current coverage

| Semester | Course–semester–group offerings | Course codes | Processing report |
| --- | ---: | ---: | --- |
| 2026h2 | 63 | 62 | [27 October 2026](reports/2026h2_2026-10-27.txt) |

The initial batch contains 699 PDF pages. ACCPPDE101 groups 1 and 2 are distinct offerings. Material source inconsistencies are preserved in the workbook and documented in the processing report.

## Adding a batch

1. Retrieve the current workbook and extraction assignment from `main`.
2. Extract the new batch using only its course-outline PDFs as substantive evidence. The container determines the semester; each PDF filename determines the course code and group.
3. Append new records to the same seven sheets. Preserve every previously accepted cell. A matching key and source checksum is an already-processed duplicate; a changed checksum is a source revision conflict requiring an explicit decision before replacement.
4. Run the assignment's quality checks, including historical-cell preservation, unique composite keys, child-table references, and catch-up-week quotations.
5. Add a report named `reports/YYYYhN_YYYY-MM-DD.txt`, using `_02`, `_03`, etc. if necessary. Update the coverage table above.
6. Refresh `main` before publication and preserve any intervening workbook updates. Commit the cumulative workbook, new report, and coverage update together directly on `main`, following the repository's `AGENTS.md`.

Keep report filenames specific to their batches while retaining the workbook's permanent filename. Source PDFs and ZIP archives remain outside the repository unless separately authorized.
