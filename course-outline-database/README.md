# UCR Course-Outline Database

This folder maintains a **standalone, outline-only academic-content database**. It supports UCR Pathways but is not the centrally maintained course dataset or the enriched dataset used by Pathways. Extraction and downstream enrichment are separate operations.

## Files

- [COURSE_OUTLINE_EXTRACTION_ASSIGNMENT.md](COURSE_OUTLINE_EXTRACTION_ASSIGNMENT.md) — current targeted extraction specification and validation rules.
- [UCR_Course_Outline_Database.xlsx](UCR_Course_Outline_Database.xlsx) — the **one-sheet, flat, cumulative extraction workbook**.

**Current coverage:** 196 course–semester–group records covering 142 distinct course codes across `2025h2`, `2026h1` and `2026h2`.

| Semester | Records | Distinct course codes | Input container | Outlines |
| --- | ---: | ---: | --- | --- |
| `2025h2` | 67 | 67 | `outlines_2025h2.zip` | 45 PDFs; 22 DOCX files |
| `2026h1` | 66 | 66 | `outlines_2026h1.zip` plus three supplemental files | 37 PDFs; 29 DOCX files |
| `2026h2` | 63 | 62 | `outlines_2026h2(2).zip` | 63 PDFs |

All three batches were extracted on 27 October 2026 under assignment version 2.0. No input outlines were skipped and no incoming records were already present. All 63 accepted `2026h2` records were preserved unchanged when `2026h1` was appended; all 126 accepted records were preserved unchanged when `2025h2` was appended. The `2025h2` append has no source revision conflicts; 24 incoming outlines have source discrepancies documented in their rows. Source conflicts and content limitations are recorded in the relevant workbook rows.

On 29 October 2026, three supplemental files supplied individually by the user were appended under the user-confirmed `2026h1` classification: `HCBPSYC111.docx`, `ENSENVI212.docx` and `MCCCOMM112.pdf`. All 193 previously accepted records were preserved unchanged; none of the three incoming keys was already present, no file was skipped and no source revision conflict occurred. The two DOCX files describe summer 2026 delivery and contain internal course codes that differ from their filenames; those differences are recorded in their `source_discrepancy_note` fields. The complete filename stems supply `osiris`, and numeric group 1 follows the same archive convention below.

**Input convention for `2026h1` and `2025h2`:** the user explicitly instructed the `2026h1` batch to process both PDF and DOCX outlines; the continuing `2025h2` batch uses the same convention. These filenames contain complete course codes without group suffixes, so retain each complete filename stem as `osiris` and assign numeric `group_number = 1` to every record. This is an archive-specific override of the assignment's PDF-only input and final-digit group convention; group 1 is an assigned convention, not an inferred source value. Preserve the exact original filename and SHA-256 hash. The input container supplies the semester (`2026h1` or `2025h2`), including where an outline contains a conflicting semester or year.

The workbook contains one row per course–semester–group and focuses on `profile`, `discipline`, `topics` and `methods`, alongside minimal source/identity fields. The source outlines and ZIPs are not stored here. The accepted `2026h2` extraction replaced the rejected seven-sheet output; no data from that rejected output was reused.

## Detailed historical reference

The [`detailed-reference/` directory](detailed-reference/README.md) is reserved for the seven-sheet **Microsoft Cowork 2026h2 detailed extraction**, named `UCR_Course_Outline_Database_Cowork_Detailed_2026h2.xlsx`. That material is **reference-only**, not part of the accepted cumulative targeted database. The directory README identifies its provenance and reference-only status.

## Two separate stages

**Stage 1 — extract from outlines:** use the supplied course outlines and their file/container names only, applying the explicitly documented input convention above for `2026h1` and `2025h2`. Never consult the central course database or the existing Pathways-enriched file as evidence for missing content. Maintain the standalone flat workbook here.

**Stage 2 — enrich for Pathways:** separately combine selected outline-derived content with BOS course attributes and YearPlan availability under the [reference-database rules](../data/reference/README.md). The resulting `data/reference/ucr_courses_enriched.xlsx` is the single authoritative Pathways course reference. Appending extraction rows does not automatically regenerate it or any academic records.

For each new semester, append to the same extraction workbook rather than making another file. The assignment defines source revision checks and quality control; the run response supplies a short processing summary rather than generating a separate report file.
