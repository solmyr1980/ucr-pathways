# Detailed course-outline extraction — Cowork reference

This directory is for a **reference-only** copy of Microsoft Cowork's detailed extraction of the `2026h2` UCR course outlines, produced under the **superseded seven-sheet assignment**.

## Expected reference workbook

`UCR_Course_Outline_Database_Cowork_Detailed_2026h2.xlsx`

- Origin: Microsoft Cowork output supplied by the user on 28 October 2026.
- Scope: `2026h2` only; seven worksheets (`courses`, `instructors`, `assessments`, `course_schedule`, `learning_outcomes`, `course_materials`, `additional_sections`).
- Original binary size: 985,536 bytes.
- SHA-256: `afc30e3475a5fc6b91cba29ef14aee72b766eb75ef0836e6360cb7e65867163f`.
- Status: **reference-only, not an accepted production extraction**.

**Transfer status:** This README does not establish that the binary workbook has been uploaded. The workbook must be checked for actual presence in this directory and its checksum verified before treating it as available on GitHub. The authenticated GitHub connection available for this operation supports repository text and metadata writes, not direct binary transfer from a chat attachment.

## Keep separate from the active course-outline database

The active workbook is [`../UCR_Course_Outline_Database.xlsx`](../UCR_Course_Outline_Database.xlsx). It is a **single-sheet, flat, cumulative dataset**, maintained under the current [targeted extraction assignment](../COURSE_OUTLINE_EXTRACTION_ASSIGNMENT.md).

The Cowork workbook is retained only for historical comparison, extraction-quality checks, or possible future research. It is **not** the active cumulative workbook, is **not** a source for the targeted extraction workflow, and must **not** automatically feed into Pathways course enrichment. The later merge with centrally managed course attributes remains a separate operation.
