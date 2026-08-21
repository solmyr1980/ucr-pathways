# Step 1 — Dutch WO bachelor longlist

Generated: 2026-08-21

## Scope

Current recognised Dutch WO bachelor programmes with a full-time route. This is an external candidate universe: **no UCR feasibility filtering has been applied**.

## Counts

- Studiekeuze123 reports **447** WO bachelor offerings, including **438** with a full-time route.
- DUO RIO contributes 529 retained current full-time WO-bachelor rows.
- Those rows contain **522 offered-programme UUIDs**; this is retained as an audit/provenance view because one registered bachelor can have several offered records.
- Collapsing to the registered bachelor + provider identity yields **345 programme/institution candidates**. This is the frozen external longlist for Step 2.
- **9/10** existing pilot seeds were automatically located; this marker is diagnostic only and does not affect the longlist.

## Saved files

- `rio_wo_bachelor_fulltime_offerings.csv` — retained official RIO rows.
- `dutch_wo_bachelor_fulltime_offerings.csv` — RIO offered-programme provenance view.
- `dutch_wo_bachelor_fulltime_longlist.csv` — registered programme/provider candidate universe for Step 2.
- `step1_summary.json` — provenance and reconciliation counts.

## Boundary

No candidate has been removed because it looks difficult for UCR. UCR feasibility belongs to Step 2. Studiekeuze123 and RIO use different public-record units, so their counts are retained side by side rather than artificially forced to match. The candidate view uses the registered bachelor identity so premaster or other alternate offered names attached to that bachelor do not become separate comparator programmes.
