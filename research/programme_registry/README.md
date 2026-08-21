# UCR Pathways programme registry

This directory contains the reproducible machinery for the private UCR Pathways national programme registry. It does **not** contain the programme database itself.

## Source-of-truth boundary

Keep programme data out of the public repository.

- **Raw external source files** belong in private Project Sources and are preserved unchanged.
- **The normalized UCR Pathways programme registry** also belongs in private Project Sources.
- **This public GitHub directory** contains only the schema, transformation/validation logic and refresh workflow.
- **`data/` in this repository remains publication data** for approved public UCR Pathways examples; do not place the national programme registry there.

The current backbone is DUO's public **HO Opleidingsoverzicht**, derived from RIO and licensed CC BY 4.0. It contains funded current and future higher-education offerings. When the Studiekeuzedatabase becomes available, treat it as an enrichment source for the normalized registry rather than assuming that it must replace DUO/RIO wholesale.

## Registry contract

The stable downstream object is `ucr_pathways_programme_registry.csv`, not any upstream source layout.

The row unit is:

> one programme × one education provider

Modes, languages, locations and offered variants are aggregated into delimited source fields unless later evidence shows that they represent materially different curricula requiring separate programme records.

`programme_key` is currently constructed as:

`ONDERWIJSAANBIEDERID::(VARIANT_VAN or ERKENDEOPLEIDINGSCODE or OPLEIDINGSEENHEIDCODE)`

The raw DUO file remains available privately, so this normalization is reversible and can be revised if the source semantics require it.

## Source fields versus Pathways fields

Columns describing the external programme are source-derived. Columns beginning with `pathways_` are owned by UCR Pathways.

The importer never uses Pathways judgments to overwrite source facts. When `--previous-registry` is supplied, every existing `pathways_` column is preserved by `programme_key`, including custom columns added after schema version 1.0.

Current default scope flags encode only decisions already settled:

- WO bachelors are included by default as sources for prospective-student-interest discovery;
- WO bachelors are comparator candidates by default;
- HBO programmes are not comparator candidates;
- language does not affect inclusion;
- full-time versus part-time does not affect inclusion;
- final comparator eligibility and disciplinary character remain separate review fields.

These are flags, not destructive filters. The normalized registry retains programmes outside the default Pathways scope.

## Build and refresh

`build_registry.py` takes the DUO/RIO CSV and creates:

- `ucr_pathways_programme_registry.csv` — normalized working registry;
- `registry_manifest.json` — provenance, source checksum and counts;
- `registry_changes.csv` — new/removed/changed programme keys when a previous registry is supplied.

Example:

```bash
python research/programme_registry/build_registry.py \
  --input raw/ho_opleidingsoverzicht.csv \
  --output processed/ucr_pathways_programme_registry.csv \
  --manifest processed/registry_manifest.json \
  --changes processed/registry_changes.csv \
  --previous-registry previous/ucr_pathways_programme_registry.csv \
  --acquired-date 2026-08-21
```

## GitHub Actions handoff

`.github/workflows/build-programme-registry.yml` is a manual acquisition/build workflow. It downloads the current DUO/RIO source, runs the importer and uploads a temporary Actions artifact containing both the untouched raw CSV and the normalized outputs.

The artifact is a handoff mechanism, not the long-term source of truth. After a successful run, download the artifact and add the raw source plus normalized registry to Project Sources. Do not commit them to this public repository.

The workflow is intentionally **not scheduled**. Refreshes should be deliberate because the working registry contains Pathways-owned enrichment that must be reconciled rather than silently overwritten.

## Comparator verification remains separate

The registry is a discovery and indexing layer. A programme's presence in the registry is not evidence that its curriculum has been reconstructed sufficiently for use in a Pathways comparison.

Before a programme is used as the disciplinary reference programme, follow the Master Specification and Production Instructions: inspect current official curriculum sources, reconstruct the programme fairly, record provenance, and obtain the required human approval.
