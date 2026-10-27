# UCR Course-Outline Database

This folder maintains a **standalone, outline-only academic-content database**. It supports UCR Pathways but is not the centrally maintained course dataset or the enriched dataset used by Pathways. Extraction and downstream enrichment are separate operations.

## Files

- [COURSE_OUTLINE_EXTRACTION_ASSIGNMENT.md](COURSE_OUTLINE_EXTRACTION_ASSIGNMENT.md) — current targeted extraction specification and validation rules.
- `UCR_Course_Outline_Database.xlsx` — permanent filename for the **one-sheet, flat, cumulative extraction workbook**, created when the first batch is re-extracted under the new assignment.

**Current status:** No accepted extraction workbook is currently present. The original seven-sheet workbook and its associated 27 October 2026 processing report were discarded and removed from the current branch. They must not be reused as accepted input. The 2026h2 outlines require re-extraction under the revised specification.

The workbook will contain one row per course–semester–group and focus on `profile`, `discipline`, `topics` and `methods`, alongside minimal source/identity fields. The source PDFs and ZIPs are not stored here.

## Two separate stages

**Stage 1 — extract from outlines:** use the supplied PDF outlines and their file/container names only. Never consult the central course database or the existing Pathways-enriched file as evidence for missing content. Maintain the standalone flat workbook here.

**Stage 2 — enrich for Pathways:** separately combine the accepted outline-derived content with centrally managed course attributes such as official course identity, classification, formal prerequisites and planned semester availability. The current Pathways-enriched database remains unaffected until that merge is deliberately carried out.

For each new semester, append to the same extraction workbook rather than making another file. The assignment defines source revision checks and quality control; the run response supplies a short processing summary rather than generating a separate report file.
