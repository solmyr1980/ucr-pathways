# Counselor comparison data

This directory is the implementation home for counselor-app discovery data and, later, the deterministic programme-provider comparison corpus.

It is separate from `data/examples/`, which contains only examples explicitly selected and approved for the public website and/or LinkedIn.

## Pilot files

The current files are deliberately small end-to-end test fixtures:

- `pilot-programmes.json` — five programme-provider records linked to the five existing comparison examples;
- `pilot-interests.json` — a small set of classified interest signals for those five records.

They exist to prove the counselor search/retrieval architecture before the full corpus is produced. They are **not** the production programme registry and must not be interpreted as complete coverage.

## Intended production shape

The production counselor implementation should keep three concerns separate:

1. programme metadata/index — one row/record per programme-provider;
2. programme-interest discovery index — many interest signals linked to programme-provider IDs;
3. deterministic comparison records — one completed validated comparison per programme-provider.

Interest search resolves to programme-provider records and then loads the fixed comparison. An interest query never regenerates or personalizes comparison content.

The authoritative academic production rules are in `docs/UCR_Pathways_Production_Instructions.md`.
