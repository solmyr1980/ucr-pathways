# Counselor comparison data

This directory is the implementation home for counselor-app discovery data and the deterministic programme-provider comparison corpus.

It is separate from `data/examples/`, which contains only examples explicitly selected and approved for the public website and/or LinkedIn.

## Pilot files

The current pilot files are deliberately small end-to-end test fixtures:

- `pilot-programmes.json` — five programme-provider records linked to the five existing comparison examples;
- `pilot-interests.json` — a small set of classified interest signals for those five records.

They exist to prove the counselor search/retrieval architecture before the full corpus is produced. They are **not** the production programme registry and must not be interpreted as complete coverage.

## Production shape

Keep three concerns separate:

1. `programmes.json` — programme metadata/index, one record per programme-provider;
2. `interests.json` — programme-interest discovery index, many interest signals linked to programme-provider IDs;
3. `comparisons/<comparison-id>.json` — one completed validated deterministic comparison per programme-provider. The programme index should carry `comparisonId`; the programme-provider ID remains the fallback stable identifier.

Interest search resolves to programme-provider records and then loads the fixed comparison. An interest query never regenerates or personalizes comparison content.

## Runtime and deployment

GitHub remains the version-controlled source of truth for these files. A deployed counselor app should receive the programme index, interest index and comparison records as part of the same deployment release as the application code rather than retrieving them from `raw.githubusercontent.com` during counselor use.

At runtime, the discovery indexes should be loaded and prepared once per application process. Individual comparison records should be read locally on demand. This keeps the running app independent of GitHub latency or availability and ensures that code and data belong to the same release.

The authoritative academic production rules are in `docs/UCR_Pathways_Production_Instructions.md`. Exact storage paths and search implementation remain repository implementation details under the Master Specification's implementation boundary.
