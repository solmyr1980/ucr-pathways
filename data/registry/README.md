# Counselor registry normalization

This directory is the authoritative plain-text normalization layer between the original UCR Pathways programme registry and deterministic counselor comparison production.

**DUO/RIO source snapshot:** 2026-08-21  
**Step 2 official-source check date:** 2026-09-12  
**Step 3 normalized-registry build date:** 2026-09-12

The original programme workbook and DUO/RIO CSV remain unchanged.

## Status

**Step 1 — complete.** 478 source registry rows were unpacked into 569 atomic offered-programme identifiers and an 83-case ambiguity queue.

**Step 2 — complete.** All 83 ambiguity cases were researched and resolved using 90 current official source records.

**Step 3 — complete.** The source rows, atomic offerings and overlapping resolution decisions have been applied jointly to create the normalized counselor programme registry and complete provenance crosswalks.

## Final normalized scope

- Normalized programme targets: **460** (`478 - 1 excluded - 18 net merge consolidation + 1 genuine one-to-many split`)
- Production-eligible counselor targets: **457**
- Retained non-production targets (teach-out/inactive): **3**
- Explicitly excluded source identities with no current target: **1** (`Academische Pabo`, source row 2)
- Normalized institutions: **20**
- Original programme-interest records preserved: **22227**
- Normalized programme-interest rows after target mapping: **22259**

The production corpus must now use `counselor_programme_id`, not source worksheet row, `AANGEBODEN_OPLEIDINGCODE`, programme-unit code or CROHO/recognized-programme code, as the stable comparison identity.

## Files

- `source_rows.csv` — immutable Step 1 source-row baseline (478 rows).
- `offerings.csv` — immutable Step 1 atomic offered-programme baseline (569 rows).
- `resolution_cases.csv` — immutable Step 1 ambiguity queue (83 cases).
- `resolution_decisions.csv` — Step 2 researched decision for every ambiguity case.
- `resolution_sources.csv` — Step 2 official evidence (90 source records).
- `programmes.csv` — final normalized programme targets with permanent counselor IDs and production order.
- `programme_offerings.csv` — every atomic `AANGEBODEN_OPLEIDINGCODE` mapped to its normalized target or explicit exclusion.
- `programme_source_rows.csv` — every original `Pathways_programmes` worksheet row mapped to its normalized target(s) or explicit exclusion.
- `institutions.csv` — normalized institution identities used by programme targets, with original provider IDs/names retained as aliases/provenance.
- `programme_interests.csv` — all original programme-interest evidence, preserved in plain text and linked to normalized counselor target IDs.
- `build_report.json` — Step 1 reconciliation and validation.
- `step2_report.json` — Step 2 research-resolution summary and validation.
- `step3_report.json` — Step 3 normalized-registry reconciliation and validation.

## Permanent target identity

`counselor_programme_id` values use `cp-000001` style IDs. They are assigned in normalized registry order for this initial build. **After this build is committed, these IDs are permanent.** A future registry refresh must reconcile new source data against the existing target table and preserve established IDs rather than regenerate all IDs from worksheet order.

A counselor target may therefore have:

- several source worksheet rows;
- several offered-programme UUIDs;
- several delivery modes or languages;
- several participating institutions; or
- one source row that was split into multiple academically distinct targets.

None of the source identifiers above is, by itself, the counselor comparison identity.

## Production order

Counselor comparison production follows `production_order` in `programmes.csv`. It is derived from the original registry ordering while applying the approved normalization decisions:

- merged targets occupy the earliest contributing source-row position;
- genuine splits create adjacent targets where required;
- `production_eligible=false` targets remain auditable but have no production order.

## Interest mapping

`programme_interests.csv` preserves the original high-recall evidence rather than rewriting it. Each record is linked through its original `source_excel_row` to the normalized target.

Where one source row now represents multiple academic targets and the historical interest evidence cannot distinguish them, the evidence is inherited by each split target and marked `inherited-across-split-targets`. This currently applies to the Leiden Political Science split. It is provenance-preserving, not a claim that every historical signal is equally strong for both routes.

Records linked to the excluded Academische Pabo source row remain in the file with no counselor target so that no original evidence disappears silently.

## Production boundary

This registry layer defines **what the counselor production targets are**. It does not reconstruct their curricula, create UCR alternatives, or publish any comparison. Full external-programme research and UCR programme construction remain governed by the Production Instructions and Counselor Batch Assignment.
