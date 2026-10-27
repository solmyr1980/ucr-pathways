# UCR Course-Outline Database

This folder maintains a **standalone, outline-only academic-content database**. It supports UCR Pathways but is not the centrally maintained course dataset or the enriched dataset used by Pathways. Extraction and downstream enrichment are separate operations.

## Files

- [COURSE_OUTLINE_EXTRACTION_ASSIGNMENT.md](COURSE_OUTLINE_EXTRACTION_ASSIGNMENT.md) — current targeted extraction specification and validation rules.
- [UCR_Course_Outline_Database.xlsx](UCR_Course_Outline_Database.xlsx) — the **one-sheet, flat, cumulative extraction workbook**.

**Current coverage:** `2026h2` — 63 course–semester–group records covering 62 distinct course codes, extracted from all 63 PDFs in `outlines_2026h2(2).zip` on 27 October 2026 under assignment version 2.0. No PDFs were skipped and no incoming records were already present. Source conflicts and content limitations are recorded in the relevant workbook rows. This fresh extraction replaces the rejected seven-sheet output; no data from that output was reused.

The workbook contains one row per course–semester–group and focus on `profile`, `discipline`, `topics` and `methods`, alongside minimal source/identity fields. The source PDFs and ZIPs are not stored here.

## Two separate stages

**Stage 1 — extract from outlines:** use the supplied PDF outlines and their file/container names only. Never consult the central course database or the existing Pathways-enriched file as evidence for missing content. Maintain the standalone flat workbook here.

**Stage 2 — enrich for Pathways:** separately combine the accepted outline-derived content with centrally managed course attributes such as official course identity, classification, formal prerequisites and planned semester availability. The current Pathways-enriched database remains unaffected until that merge is deliberately carried out.

For each new semester, append to the same extraction workbook rather than making another file. The assignment defines source revision checks and quality control; the run response supplies a short processing summary rather than generating a separate report file.
