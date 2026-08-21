# UCR Pathways programme registry

This directory contains the reproducible filtering and aggregation logic for the private UCR Pathways working programme registry. It does **not** contain the programme data itself.

## Source-of-truth boundary

Keep programme data out of the public repository.

- The untouched DUO/RIO source file in private Project Sources is the source of truth.
- The derived working registry also belongs in private Project Sources.
- The public GitHub repository contains only the transformation logic.
- `data/` remains reserved for approved public UCR Pathways publication records.

The current source is DUO's **HO Opleidingsoverzicht**, derived from RIO.

## Current working-registry contract

The working registry is deliberately minimal. It contains only actual DUO data.

- Keep all original DUO columns.
- Select the current student-facing WO bachelor programmes relevant to the pilot.
- Exclude recognition-only rows without an education provider.
- Exclude non-bachelor offerings that sit under bachelor registrations, such as premasters, bridging programmes, educational modules and minors.
- Do not exclude by language or full-time/part-time mode.
- Use one row per distinct student-facing bachelor choice.
- Aggregate multiple DUO rows when they describe the same student-facing programme.
- Keep genuinely distinct student-facing variants separate, even when DUO links them to the same recognised programme; UCR and UCU are examples.
- When source values differ across aggregated rows, preserve the distinct DUO values in the existing source column rather than inventing a new derived field.
- Do not add Pathways enrichment fields, placeholder columns, review fields or a separate Pathways identifier until a later step explicitly requires and defines them.

Because the untouched DUO file remains available, the working registry can always be reconstructed or expanded if additional programmes are needed.

## Build

`build_registry.py` takes the DUO/RIO CSV and writes one derived CSV containing only the original DUO columns after the agreed selection and aggregation.

Example:

```bash
python research/programme_registry/build_registry.py \
  --input DUO_RIO_HO_Opleidingsoverzicht_2026-08-21.csv \
  --output ucr_pathways_programme_registry.csv
```

The Excel workbook used for day-to-day monitoring is the same derived programme table saved as `.xlsx`. The untouched DUO CSV remains the archival source of truth.

## Comparator verification remains separate

The registry is a discovery and indexing layer. A programme's presence in the registry is not evidence that its curriculum has been reconstructed sufficiently for use in a Pathways comparison.

Before a programme is used as the disciplinary reference programme, follow the Master Specification and Production Instructions: inspect current official curriculum sources, reconstruct the programme fairly, record provenance, and obtain the required human approval.
