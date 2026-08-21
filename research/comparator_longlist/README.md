# Step 1 — Dutch WO bachelor longlist

Generated: 2026-08-21

## Scope

Current recognised Dutch WO bachelor programmes with a full-time route. This is an external candidate universe: **no UCR feasibility filtering has been applied**.

## Counts

- Studiekeuze123 reports 447 WO bachelor offerings, including 438 with a full-time route.
- DUO RIO contains 517 current full-time WO-bachelor offering/location rows after restricting to `SOORT = OPLEIDING`.
- Deduplication by recognised programme code + provider yields **341 programme/institution candidates**.
- Existing pilot seeds identified in the official longlist: **9/10**.

## Saved files

- `rio_wo_bachelor_fulltime_offerings.csv` — official RIO rows retained for audit/reconstruction.
- `dutch_wo_bachelor_fulltime_longlist.csv` — deduplicated candidate universe for Step 2.
- `step1_summary.json` — source provenance, counts and pilot-seed matches.

## Boundary

No candidate has been removed because it looks difficult for UCR. UCR feasibility belongs to Step 2. The difference between Studiekeuze123's offering count and the RIO programme/provider count is retained transparently rather than forced away: the two sources use different units (public offerings versus recognised programme/provider records).
