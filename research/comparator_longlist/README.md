# Step 1 — Dutch WO bachelor longlist

Generated: 2026-08-21

## Scope

Current recognised Dutch WO bachelor offerings with a full-time route. This is an external candidate universe: **no UCR feasibility filtering has been applied**.

## Counts

- Studiekeuze123 reports **447** WO bachelor offerings, including **438** with a full-time route.
- DUO RIO contributes 529 retained current full-time WO-bachelor rows.
- Grouping those rows by RIO `AANGEBODEN_OPLEIDINGCODE` yields **522 official offered-programme records**.
- Collapsing further to programme/provider identity yields **345 programme/institution candidates** for later portfolio selection.
- Existing pilot-seed marking is diagnostic only; it is not used to include or exclude candidates.

## Saved files

- `rio_wo_bachelor_fulltime_offerings.csv` — official retained RIO rows, untouched after filtering.
- `dutch_wo_bachelor_fulltime_offerings.csv` — offering-level RIO view keyed by `AANGEBODEN_OPLEIDINGCODE`.
- `dutch_wo_bachelor_fulltime_longlist.csv` — deduplicated programme/provider candidate view for Step 2.
- `step1_summary.json` — provenance and reconciliation counts.

## Boundary

No candidate has been removed because it looks difficult for UCR. UCR feasibility belongs to Step 2. Studiekeuze123 and RIO do not use exactly the same public-record unit, so their counts are retained side by side rather than artificially forced to match.
