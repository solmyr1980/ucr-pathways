# Counselor registry normalization baseline

This directory is the plain-text normalization layer between the original UCR Pathways programme registry and later counselor comparison production.

**Source snapshot:** DUO/RIO extract dated 2026-08-21.

The source-file SHA-256 hashes and validation results are stored in `build_report.json`. The original workbook and DUO/RIO CSV remain unchanged; this directory contains only derived plain-text data needed for normalization work.

## Step 1 status

Step 1 is deliberately mechanical. It does **not** decide which delivery offerings should merge into one counselor comparison target, which language/campus variants should split, or which anomalous records are in/out of scope. No current-programme web research was performed.

## Files

- `source_rows.csv` — one row per original `Pathways_programmes` worksheet row (478 rows), retaining the source identity fields needed for joins plus mechanical flags and resolution-case links.
- `offerings.csv` — one row per referenced `AANGEBODEN_OPLEIDINGCODE` (569 rows). Pipe-delimited source aggregation has been unpacked into atomic offerings. The most useful DUO/RIO identity, provider, language, mode, lifecycle, URL, cooperation and location fields are retained. Where an offering ID occurs in multiple raw DUO rows, row references and conflicting values are preserved explicitly.
- `resolution_cases.csv` — the ambiguity/research queue. Delivery-mode differences alone are not treated as ambiguity. Identity-sensitive language, programme-unit, location, cross-row reuse, special-structure, lifecycle and missing-core-metadata cases are queued.
- `build_report.json` — reconciliation totals, input hashes, case-type counts and validation results.

## Key reconciliation

- Source registry rows: **478**
- Distinct referenced offering IDs: **569**
- Raw DUO/RIO source records behind those IDs: **577**
- Offering IDs with more than one DUO/RIO row: **8**
- Source rows containing multiple offering IDs: **87**
- Of those multi-offering rows, identity-sensitive on language/programme-unit/location: **30**
- Of those multi-offering rows, administrative-only on those identity dimensions: **57**
- Resolution cases: **83**, affecting **96** source rows
- Source rows with no explicit resolution case at this stage: **382**

The 57/30 multi-offering split is intentionally separate from other review dimensions: an administratively mergeable delivery pair can still require review for lifecycle status, special-degree structure, missing metadata, or another independent issue.

## Data rules

1. `source_excel_row` remains the join back to the existing `programme_interests` evidence.
2. `AANGEBODEN_OPLEIDINGCODE` is source provenance, not the final counselor comparison ID.
3. One referenced offering ID maps to exactly one original source row in this snapshot.
4. Multiple modes such as full-time/part-time do not automatically imply separate counselor comparison targets.
5. No current-programme web research or merge/split decision was performed in Step 1.
6. The final counselor target count must emerge from resolving `resolution_cases.csv`; it must not be forced to remain 478.

## Next stage

Resolve the ambiguity queue, then create the normalized counselor-programme target table plus offering/source-row crosswalks. Only after that should counselor comparison production resume.
