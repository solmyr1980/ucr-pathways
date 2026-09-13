# Counselor Batch Assignment

**Reference name:** Counselor Batch Assignment  
**Purpose:** Reusable production assignment for deterministic counselor-comparison batches  
**Default batch size:** 20 normalized counselor programme targets in the current production scope  
**Fixed UCR starting cohort:** Fall 2026  
**Repository:** `solmyr1980/ucr-pathways`

Use this assignment for counselor corpus production. Select targets from the normalized registry, not directly from the original Excel worksheet or DUO/RIO offered-programme rows.

---

# UCR Pathways — Counselor Corpus Production

## Objective

Produce the next batch of deterministic counselor comparisons. Each selected normalized target produces one fixed four-programme comparison:

1. exact external Dutch bachelor/route represented by the normalized target;
2. `ucr-depth` — closest feasible UCR match;
3. `ucr-balanced` — field plus one or two evidence-backed adjacent directions;
4. `ucr-thematic` — coherent UCR programme organised around one explicit evidence-backed question/problem/phenomenon/application.

The comparison belongs to the normalized target and is never personalized to a search term or individual student.

## 1. Retrieve authoritative instructions first

Before analysing or producing anything, retrieve current GitHub versions of:

- `docs/UCR_Pathways_Master_Specification.md`
- `docs/UCR_Pathways_Production_Instructions.md`
- `docs/UCR_Pathways_Web_LinkedIn_Workflow.md`

Also inspect relevant current repository state, including `data/registry/`, `data/counselor/`, existing current production comparisons, schemas and validator code. Use GitHub as authoritative; do not substitute memory, previous chats or superseded Project Source copies.

## 2. Current production scope and identity

Select only normalized targets from `data/registry/programmes.csv` with:

- permanent `counselor_programme_id`;
- `production_eligible=true`;
- nonblank `production_order`;
- `programme_type=standard`.

`joint-degree`, `double-bachelor` and `dual-degree-route` targets remain valid registry targets but are temporarily outside current comparison production. Do not change registry identity or lifecycle fields to implement this exclusion.

`counselor_programme_id` is the production identity. Worksheet rows, offered-programme UUIDs, programme-unit codes, recognized-programme codes, language/mode/campus registrations are provenance and join identifiers.

## 3. Select the batch

Unless the user specifies otherwise, process the next 20 in-scope targets in ascending `production_order` that do not already have a completed **schema-1.3** production record requiring no repair.

Skipped non-standard targets do not consume a batch slot. Do not replace a genuinely blocked selected in-scope target with a later one merely to keep the completed count at 20; complete the rest and report the blocker.

## 4. Preserve normalized registry metadata

For every selected target preserve the current registry values required by the schema, including permanent ID, registry/production orders, canonical name, institution IDs, programme type/status, eligibility, normalized languages/modes, source rows, offered-programme UUIDs, programme-unit/recognized/variant identifiers, aliases and resolution provenance where applicable.

Do not undo normalized merges/splits or collapse language/mode arrays to one scalar.

## 5. Research the external programme independently

Use current official sources for the exact programme/route. Prefer formal curriculum/graduation requirements, official curriculum pages, official routes/tracks/specialisations, official course-catalogue information, then general official prospective-student pages.

Distinguish compulsory components, restricted choices, routes, genuinely open elective/profile space, methods/mathematics/statistics/research training, thesis/capstone and EC weights. Choose one coherent valid pathway where choices must be instantiated.

Do not combine mutually exclusive options, treat optional material as compulsory, invent electives, deliberately weaken the external programme, or silently force official evidence to agree with registry metadata. Flag a registry exception if identity appears materially wrong.

## 6. Use programme-interest evidence correctly

Retrieve rows linked to the exact `counselor_programme_id` from `data/registry/programme_interests.csv`.

- `Direct programme interest` and `Stable study direction`: strongest evidence;
- `Curricular topic`: may broaden the substantive picture;
- `Illustrative or temporary topic` and `Outcome or individual trajectory`: cautious application/theme context only.

`inherited-across-split-targets` rows are not target-specific evidence unless independently corroborated by current official evidence for the exact target.

## 7. Build the academic interest map before UCR course selection

This step is mandatory. Do not browse UCR courses first and work backwards to a rationale.

Create three evidence-backed layers: `coreField`, `adjacentDirections`, and `questionsApplications`. Every map item must trace to current official target-specific evidence or a valid target-specific programme-interest row. UCR course availability is not evidence for the map.

## 8. Freeze the three UCR concepts before selecting courses

### 8.1 `ucr-depth`

Target the `coreField`. Preserve genuine specialist gaps instead of filling them with weakly related material.

### 8.2 `ucr-balanced`

Retain a substantial core and select one or two exact labels from `adjacentDirections`. Store them in `academicRationale.balancedDirections`.

### 8.3 `ucr-thematic`

State one explicit organising question/problem/phenomenon/application and store it in `academicRationale.thematicQuestion` with its evidence and exact `basisLabels` from the map.

The theme is **scope-closed by those basis labels**. It may combine them, but it may not introduce a new substantive domain, population, problem or application absent from them. “Several relevant perspectives” means several perspectives on the same evidenced question, not permission to invent another interest.

If evidence for broad expansion is weak, keep the thematic programme close to the field rather than manufacturing eclecticism.

## 9. Construct UCR programmes and create course-level traceability

Only now use the current enriched UCR course database, especially `osiris`, `name`, `profile`, `discipline`, `topics`, `methods`, `description2`, prerequisites and semester availability.

Use the fixed Fall 2026 sequence: `2026h2`, `2027h1`, `2027h2`, `2028h1`, `2028h2`, `2029h1`.

Each UCR programme must have exactly 24 unique courses, four per semester, at least six 300-level courses, `ACCPPDE101` during Year 1, all prerequisites completed earlier and actual availability in the assigned semester.

### 9.1 Mandatory `academicRationale.courseAlignment`

Before a schedule can be production-complete, store exactly one alignment entry for every scheduled course in each role and no extra entries.

Permitted academic bases:

- `ucr-depth`: only `coreField` labels;
- `ucr-balanced`: `coreField` labels plus selected `balancedDirections`;
- `ucr-thematic`: only labels listed in `thematicQuestion.basisLabels`.

For every course except `ACCPPDE101`, `basisType` must be `academic-map`, `basisLabels` must contain at least one permitted label, and `reason` must explain substantively how the course serves that label.

For `ACCPPDE101` only, `basisType` must be `ucr-required` and `basisLabels` must be empty.

“Adds breadth”, “adds another perspective”, “is interesting” or similar generic reasons are invalid. If a course cannot be justified, remove it or revise the concept/map only if new external evidence genuinely supports the revision.

Validate both course traceability and mechanical feasibility before export.

## 10. Build the comparison only after all curricula are complete

Comparison blocks are **analytical alignments**, not partitions of 180 EC curricula.

There is no required number of blocks, no default three-block structure, no automatic 60-EC blocks, and external curriculum components are not automatically comparison-block titles. There is no automatic one-external-component → fixed UCR course-group mapping. Not all 24 UCR courses need appear. Blocks may aggregate or split external components when analytically justified. Unequal credit totals and meaningful blanks are expected when warranted.

A repeated fixed UCR allocation across every block—for example the same number of courses or same EC total in every block—is presumed to be a template failure. Rebuild it unless independently justified by the underlying curricula.

Align only substantively comparable content, preserve actual EC and genuine gaps, and leave specialist external components unmatched where UCR has no genuine counterpart.

## 11. Explanatory notes

Use only when materially needed: `less-disciplinary-depth`, `related-fields-not-full-discipline`, `missing-specialist-components`, or `different-curricular-structure`. Populate only evidenced claims and omit unnecessary boilerplate.

## 12. Production record

Current counselor production records use `schemaVersion: "1.3"`.

Each record must include stable identity/registry metadata, official sources/currentness, selected external route, `academicRationale` with map + concepts + `courseAlignment`, four programme roles, complete UCR schedules, external curriculum/EC, comparison blocks/gaps, notes where warranted and validation metadata.

Under the current contract:

`id == programmeProvider.counselorProgrammeId == counselor_programme_id`

Store as `data/counselor/comparisons/<counselor_programme_id>.json`.

## 13. Incremental-production rule

During incremental production create only individual comparison records. Do **not** create production `programmes.json` or `interests.json` while the corpus is incomplete. Leave pilot indexes unchanged until finalisation.

Do not modify public examples, catalog, website, LinkedIn records, queues or generated PDFs merely because counselor production advances.

## 14. Batch quality control

Before completing a run verify every record for scope/identity and registry parity; current official source basis and fair external reconstruction; complete evidence-backed academic map; balanced directions from actual adjacent labels; thematic question evidence-backed and scope-closed; exact course-level traceability with no unsupported UCR course; distinct UCR alternatives without manufactured breadth; all mechanical feasibility rules; genuine comparison alignments rather than fixed allocations; no invented equivalence or hidden UCR limitation; and schema validity.

Run automated validation across all completed current production records.

Inspect each batch as a set for systematic failure modes, especially repetitive programme templates, generic thematic palettes, interchangeable thematic questions, unsupported cross-disciplinary jumps, frequent thematic courses without evidence, forced comparison symmetry/fixed credit allocation, and weakening of external programmes.

Do not change a sound record merely to manufacture variety.

## 15. Exceptions

If a selected in-scope target cannot be reconstructed confidently, an academically defensible adjacent direction/theme cannot be established, or no feasible UCR implementation exists, do not guess. Leave the comparison incomplete, document the exact problem and continue the rest of the batch.

## 16. GitHub working rules

Work only on existing `main`. Do not create another branch, pull request or duplicate repository structure. Do not restructure the repository.

A genuine upstream contract/registry problem must be fixed in the appropriate authoritative layer rather than silently worked around in production.

## 17. Exact operating sequence

For every selected target:

1. confirm normalized identity and registry metadata;
2. reconstruct the exact external programme;
3. retrieve target-specific programme-interest evidence;
4. build the academic interest map;
5. freeze depth, balanced directions and thematic question;
6. select UCR courses from the enriched database;
7. create and validate `courseAlignment` for every selected course;
8. schedule and mechanically validate all three UCR programmes;
9. build comparison blocks from completed curricula without forced symmetry;
10. create the schema-1.3 record;
11. run record-level and batch-level QC.

Do not skip or reorder the rationale/traceability steps even when the field appears obvious.

## 18. Final deliverable

Report concisely the selected IDs/orders, programme names/institutions, number completed, exceptions, mechanical-feasibility status, source/registry discrepancies, GitHub commit, and any issue that must be resolved before the next batch.

Do not stop for routine intermediate approval during the batch.
