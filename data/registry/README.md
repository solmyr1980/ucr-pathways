# Counselor registry normalization baseline

This directory is the plain-text normalization layer between the original UCR Pathways programme registry and later counselor comparison production.

**DUO/RIO source snapshot:** 2026-08-21  
**Step 2 official-source check date:** 2026-09-12

The original programme workbook and DUO/RIO CSV remain unchanged. This directory contains derived, auditable normalization data.

## Status

**Step 1 — complete.** The 478 source registry rows were mechanically unpacked into 569 atomic offered-programme identifiers and an 83-case ambiguity queue.

**Step 2 — complete.** All 83 ambiguity cases have been researched and resolved against current official programme/institution sources. The decisions concern registry identity only: merge/split treatment, current identity, delivery/language/location variants, lifecycle status, joint/special structures and missing core metadata. They do **not** reconstruct full external curricula or generate UCR comparisons.

## Files

- `source_rows.csv` — one row per original `Pathways_programmes` worksheet row (478 rows), retaining source identity fields needed for joins plus Step 1 flags and resolution-case links.
- `offerings.csv` — one row per referenced `AANGEBODEN_OPLEIDINGCODE` (569 rows), preserving atomic DUO/RIO identity, provider, language, mode, lifecycle, URL, cooperation and location evidence.
- `resolution_cases.csv` — immutable Step 1 mechanical ambiguity/research queue (83 cases).
- `resolution_decisions.csv` — one researched decision for each of the 83 cases.
- `resolution_sources.csv` — 90 current official source records supporting the Step 2 decisions.
- `build_report.json` — Step 1 reconciliation totals, input hashes, case-type counts and validation results.
- `step2_report.json` — Step 2 completion summary and global validation results.

## Step 1 reconciliation

- Source registry rows: **478**
- Distinct referenced offering IDs: **569**
- Raw DUO/RIO source records behind those IDs: **577**
- Offering IDs with more than one raw DUO/RIO row: **8**
- Source rows containing multiple offering IDs: **87**
- Multi-offering rows identity-sensitive on language/programme-unit/location: **30**
- Multi-offering rows administrative-only on those identity dimensions: **57**
- Resolution cases: **83**, affecting **96** source rows
- Source rows with no explicit Step 1 resolution case: **382**

The 57/30 split concerns only language/programme-unit/location differences. A row in the 57 can still require resolution for lifecycle status, special-degree structure or another independent issue.

## Step 2 outcome

All **83/83** cases are resolved. The evidence base contains **90 official-source records** across 14 institutions/provider groups.

The research confirms that the source registry mixes several kinds of identity:

- academic programme identity;
- offered-programme/registration identity;
- delivery mode;
- language route;
- campus/location;
- joint/double/dual-degree structure;
- legacy or teach-out registrations.

These dimensions must not be collapsed into one key or treated as automatically equivalent.

Important recurring treatments recorded in `resolution_decisions.csv` include:

- merge full-time/part-time offerings when they are delivery variants of one academic programme;
- merge language offerings when official sources show one programme, but split them when they are genuinely distinct academic tracks;
- merge administrative/free-registration rows with the corresponding public programme when no separate student-facing academic identity exists;
- retain genuine joint/double/dual-degree structures and their participating institutions;
- split one source representation when current official evidence shows multiple distinct student-facing programmes;
- normalize stale names or registrations to a current successor where continuity is clear;
- retain teach-out records for provenance but mark them not production-eligible;
- exclude a source identity from current counselor production when the present route is not an in-scope WO bachelor.

## Data rules

1. `source_excel_row` remains the join back to existing `programme_interests` evidence.
2. `AANGEBODEN_OPLEIDINGCODE` is source provenance, not the future counselor comparison ID.
3. Academic identity is distinct from registration identity, delivery mode, language and campus.
4. Multiple source rows and offerings may map to one counselor target.
5. One source row may map to several counselor targets when official evidence supports genuinely distinct programmes/tracks.
6. Joint programmes should be represented as one academic target with all participating institutions where the current programme is genuinely joint.
7. `resolution_cases.csv` remains immutable; researched outcomes and evidence are stored separately.
8. Do not infer the final target count by summing case-level `target_count`, because cases overlap. Step 3 must apply the full decision set jointly.
9. The original workbook, programme-interest table and Step 1 source tables remain unchanged.

## Next stage

Step 3 will construct the actual normalized counselor programme registry and crosswalks from:

- the 382 source rows with no Step 1 ambiguity case;
- the 83 resolved case decisions;
- the atomic offering table;
- the source-row provenance links.

Step 3 should assign permanent counselor target IDs, normalize institution identity, create source-row/offering crosswalks, reconcile the existing interest links and calculate the final number of counselor production targets. Only after that normalized registry is validated should counselor comparison production resume.
