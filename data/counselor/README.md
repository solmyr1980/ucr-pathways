# Counselor comparison data

This directory is the implementation home for counselor-app discovery data and the deterministic comparison corpus.

It is separate from `data/examples/`, which contains only examples explicitly selected and approved for the public website and/or LinkedIn.

## Authoritative programme identity

The counselor corpus is keyed by the normalized registry in `data/registry/`.

The stable programme identity is `counselor_programme_id` from `data/registry/programmes.csv` (for example `cp-000001`). Source worksheet rows, `AANGEBODEN_OPLEIDINGCODE`, programme-unit codes and recognized-programme codes are retained as provenance/crosswalk identifiers and must not be used as the counselor comparison identity.

The normalized registry may merge several registrations into one academic target or split a legacy source representation into several genuine academic targets.

Registry eligibility and current counselor production scope are deliberately separate concepts. The current corpus includes only normalized targets with `production_eligible=true`, nonblank `production_order` and `programme_type=standard`. Targets classified as `joint-degree`, `double-bachelor` or `dual-degree-route` remain valid normalized targets but are temporarily excluded from counselor comparison production until an approved presentation method exists. Do not change the registry identity or lifecycle fields to implement that exclusion.

## Pilot files

The current pilot files are deliberately small end-to-end test fixtures:

- `pilot-programmes.json` — five discovery records linked to existing comparison examples;
- `pilot-interests.json` — a small set of classified interest signals for those fixtures.

They exist to prove the counselor search/retrieval architecture. They are **not** the production programme registry and must not be interpreted as complete coverage.

## Production shape

Keep three concerns separate:

1. `programmes.json` — deployed programme discovery metadata, one record per normalized target in the current counselor production scope;
2. `interests.json` — deployed programme-interest discovery index linked by `counselor_programme_id`, limited to targets in the current counselor production scope;
3. `comparisons/<counselor_programme_id>.json` — one completed validated deterministic comparison per in-scope normalized target, unless a later explicit schema decision separates comparison ID from target ID.

For current production records, the top-level `id`, `programmeProvider.counselorProgrammeId` and permanent registry `counselor_programme_id` must be identical. Legacy source/provider/offering identifiers remain provenance only.

Validate normalized production records with `npm run validate:counselor`. The validator intentionally ignores UUID-named pre-normalization comparison files; those files do not count as current production records until they are checked and migrated to the normalized target contract.

During incremental corpus production, do **not** create the production `programmes.json` or `interests.json` indexes. Leave pilot indexes unchanged until the comparison corpus is complete and quality-controlled; then build the production indexes in one finalisation step from `data/registry/programmes.csv` and `data/registry/programme_interests.csv`, applying the then-current counselor production-scope rules.

Interest search resolves to normalized counselor targets and then loads the fixed comparison. An interest query never regenerates or personalizes comparison content.

Where `target_mapping_status=inherited-across-split-targets`, the inherited interest row is provenance/general discovery context only. It must not be used as target-specific academic evidence unless independently corroborated by current official evidence for the exact normalized target.

## Registry provenance

Use the crosswalks in `data/registry/` when traceability is needed:

- `programme_source_rows.csv` — legacy workbook row → normalized target;
- `programme_offerings.csv` — offered-programme UUID → normalized target;
- `institutions.csv` — normalized institution identity and source aliases/IDs;
- `resolution_decisions.csv` / `resolution_sources.csv` — identity-resolution evidence for ambiguous cases.

Existing comparison records created before registry normalization must not be treated as evidence that the corresponding normalized target is production-complete until they have been checked/migrated against the current target ID and production rules.

## Runtime and deployment

GitHub remains the version-controlled source of truth. A deployed counselor app should receive the programme index, interest index and comparison records as part of the same deployment release as the application code rather than retrieving them from `raw.githubusercontent.com` during counselor use.

At runtime, discovery indexes should be loaded and prepared once per application process. Individual comparison records should be read locally on demand. This keeps the app independent of GitHub latency or availability and ensures that code and data belong to the same release.

The authoritative academic production rules are in `docs/UCR_Pathways_Production_Instructions.md` and the reusable batch procedure is in `docs/Counselor_Batch_Assignment.md`. Exact renderer/search implementation remains repository implementation detail under the Master Specification's implementation boundary.
