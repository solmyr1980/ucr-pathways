# Counselor Batch Assignment

**Reference name:** Counselor Batch Assignment  
**Purpose:** Reusable production assignment for batches of deterministic counselor comparisons  
**Default batch size:** 20 normalized counselor programme targets in the current production scope  
**Fixed UCR starting cohort:** Fall 2026  
**Repository:** `solmyr1980/ucr-pathways`

Use this assignment when producing counselor-comparison batches. Select targets from the normalized registry, not directly from the original Excel worksheet or DUO/RIO offered-programme rows.

---

# UCR Pathways — Counselor Corpus Production

## Objective

Produce the next batch of deterministic counselor comparisons for the UCR counselor comparison library.

This is production work, not a methodology pilot.

Each selected normalized counselor programme target must produce one fixed four-programme comparison:

1. the exact external Dutch bachelor programme/route represented by the normalized target;
2. `ucr-depth` — the closest feasible UCR match;
3. `ucr-balanced` — the field plus one or two evidence-backed adjacent directions;
4. `ucr-thematic` — a broader coherent UCR programme organised around one explicit evidence-backed question, problem, phenomenon or application.

The comparison belongs to the normalized counselor programme target. It is not personalized to an individual student.

## 1. Retrieve the authoritative project instructions first

Before analysing or producing anything, retrieve the current versions directly from GitHub of:

- `docs/UCR_Pathways_Master_Specification.md`
- `docs/UCR_Pathways_Production_Instructions.md`
- `docs/UCR_Pathways_Web_LinkedIn_Workflow.md`

Also inspect the current repository implementation relevant to counselor records, including:

- `data/registry/README.md`
- `data/registry/programmes.csv`
- `data/registry/programme_interests.csv`
- `data/registry/programme_source_rows.csv`
- `data/registry/programme_offerings.csv`
- `data/registry/institutions.csv`
- `data/counselor/README.md`
- existing counselor comparison records where useful;
- current repository schemas/validator code where relevant.

Use the GitHub versions as authoritative. Do not substitute remembered instructions, earlier chats or superseded Project Source copies.

## 2. Authoritative registry model and current production scope

The normalized registry and the current counselor production scope are related but not identical.

The stable registry identity is one row of `data/registry/programmes.csv` with a permanent `counselor_programme_id`. Registry lifecycle/currentness is represented by `production_eligible` and `production_order`.

For the **current counselor corpus**, select only targets that satisfy all of the following:

- permanent `counselor_programme_id`;
- `production_eligible=true`;
- nonblank `production_order`; and
- `programme_type=standard`.

Targets with `programme_type=joint-degree`, `double-bachelor` or `dual-degree-route` are temporarily excluded from counselor comparison production until an approved way of presenting those structures has been adopted. Keep them in the normalized registry. Do not change their permanent IDs, normalization decisions, current status, institutions, `production_eligible` value or `production_order` merely to implement this temporary presentation-scope decision.

`counselor_programme_id` is the stable counselor comparison identity.

The following are provenance and join identifiers, not the production identity by themselves:

- original `source_excel_row` values;
- `AANGEBODEN_OPLEIDINGCODE` offered-programme UUIDs;
- `OPLEIDINGSEENHEIDCODE` values;
- `ERKENDEOPLEIDINGSCODE`/recognized-programme codes;
- delivery mode, language or campus registrations.

The normalized target may legitimately:

- merge several source worksheet rows;
- merge several offered-programme UUIDs;
- combine delivery/language/campus registrations that represent one academic programme; or
- result from a split where one source representation contained several academically distinct targets.

Joint/double/dual structures remain legitimate normalized targets, but they are not selectable under the current counselor production scope.

Do not undo the normalization during comparison production.

## 3. Select the batch

Unless the user specifies otherwise, process the next **20** rows in ascending `production_order` from `data/registry/programmes.csv` that:

- have `production_eligible=true`;
- have `programme_type=standard`; and
- do not already have a completed current production counselor comparison requiring no repair.

The batch size is 20 **in-scope targets**. A non-standard target skipped by the current production-scope rule does not consume a batch slot and is not a blocked case.

Do not select from original worksheet-row order independently of `production_order`.

Do not replace a genuinely blocked **selected in-scope target** with a later target merely to keep the number of completed comparisons at 20. Complete the remainder of the selected batch and report the blocked case.

Pilot search fixtures and public examples do not automatically count as completed production counselor records. Existing pre-normalization counselor records may be reused only after confirming that they correspond to the normalized target and satisfy the current production rules.

## 4. Preserve normalized target identity and registry metadata

For each selected target preserve the current normalized registry values required by the counselor-production schema, including:

- `counselor_programme_id`;
- `registry_order` and `production_order`;
- canonical target name;
- normalized institution identity/identities;
- programme type and current status;
- production eligibility;
- normalized languages and modes;
- source worksheet rows;
- offered-programme UUIDs;
- programme-unit/recognized-programme/variant identifiers where present;
- aliases and relevant registry URLs;
- Step 2 resolution/provenance fields where applicable.

Do not collapse normalized language or mode arrays to one scalar value.

When the target is a normalized merge, research the current academic programme represented by the target rather than treating each historical registration as a separate comparator.

When the target is a normalized split, research the exact named route/track represented by that target.

If a `joint-degree`, `double-bachelor` or `dual-degree-route` target appears in a selected batch, do not produce it. Treat that as a selection-logic error because these types are currently outside production scope.

## 5. Research each external programme independently

For every selected target, establish the exact current programme and reconstruct it from current official sources.

Use this source hierarchy where available:

1. formal curriculum or graduation requirements;
2. official curriculum/study-programme pages;
3. official tracks, routes or specialisations;
4. official course-catalogue information;
5. general official prospective-student pages.

Registry URLs and identity-resolution sources are starting evidence, not automatically sufficient curriculum evidence.

For the external programme distinguish:

- compulsory components;
- restricted choices;
- tracks/routes/specialisations;
- genuinely open elective or profiling space;
- methods, mathematics, statistics and research training;
- thesis/capstone requirements;
- EC weights.

Choose one coherent valid pathway where genuine choices must be instantiated.

Do not:

- combine mutually exclusive options;
- treat optional courses as compulsory;
- invent courses to fill elective space;
- deliberately select weak options to make UCR stronger;
- artificially narrow the external programme;
- silently force current official information to agree with old registry metadata.

If normalized registry information and current official programme information materially disagree, preserve the current official programme structure and report the discrepancy. Do not silently change target identity; identity changes belong in the registry layer.

Research quality must not decline for targets appearing later in the batch.

## 6. Use programme-interest evidence correctly

Use `data/registry/programme_interests.csv` and retrieve rows linked to the selected `counselor_programme_id`.

These records are supporting evidence about academically relevant interests and directions associated with the target. They are **not** a student's submitted interests.

Use them as follows:

- `Direct programme interest` and `Stable study direction` provide the strongest evidence for related directions;
- `Curricular topic` may broaden the substantive picture;
- `Illustrative or temporary topic` and `Outcome or individual trajectory` may inform applications or themes cautiously but should not define the programme's core.

Where `target_mapping_status=inherited-across-split-targets`, the historical interest record is inherited provenance/general discovery context only. It is not target-specific academic evidence unless the same claim is independently corroborated by current official evidence for that exact normalized target.

Do not generate a different comparison depending on a search term. Every search route must ultimately lead to the same fixed comparison.

## 7. Build an academic interest map before selecting UCR courses

This step is mandatory.

The counselor workflow begins with a named bachelor, not with a student's personal list of interests. Therefore do not invent additional interests to create `ucr-balanced` or `ucr-thematic`, and do not browse the UCR catalogue for attractive breadth and then work backwards to a rationale.

Build an **evidence-backed academic interest map** for the exact target with three layers.

### 7.1 Core field

Identify what defines the external programme academically:

- central disciplines and subfields;
- foundations and progression;
- mathematics/statistics/methods/research training;
- advanced or specialist work;
- thesis/capstone where relevant.

### 7.2 Adjacent directions

Identify genuinely related directions supported by evidence, such as:

- formal tracks/routes/specialisations;
- stable study directions;
- strong direct programme interests;
- recurring curricular connections to neighbouring disciplines;
- neighbouring academic directions clearly supported by programme questions or applications.

Do not add a direction merely because UCR offers a course in it.

### 7.3 Questions and applications

Identify substantive questions, phenomena, problems and applications that the field addresses and that could support a thematic programme.

These may come from current official programme evidence or valid target-specific programme-interest evidence.

### 7.4 Evidence rule

Every substantive map item must be traceable to at least one current official source or valid target-specific programme-interest row.

In the production record, preserve that traceability in `academicRationale` using evidence references.

Do not use the UCR course database to generate the map. Use it only after the map and the three programme concepts have been established.

## 8. Freeze the three programme concepts before course selection

Before selecting individual UCR courses, explicitly establish all three programme concepts.

### 8.1 `ucr-depth`

Use the core-field layer as the principal target.

Construct the feasible UCR programme that comes closest to the substantive core, progression and methods of the external programme.

Consider disciplinary content, methods, mathematics/statistics, research training and advanced work—not merely similarities in course titles.

Where UCR genuinely lacks important specialist areas, preserve that limitation. Do not compensate with weakly related courses merely to create apparent equivalence.

### 8.2 `ucr-balanced`

Retain a substantial core of the external field and select **one or two adjacent directions from the academic interest map**.

Store the selected direction labels in `academicRationale.balancedDirections`.

The result should be meaningfully broader than `ucr-depth`, not the same programme with arbitrary substitutions.

Do not use a direction absent from the map merely to create difference.

### 8.3 `ucr-thematic`

Before selecting courses, state **one explicit organising question, problem, phenomenon or application**.

The theme must be traceable to the academic interest map and supported by evidence. Store it in `academicRationale.thematicQuestion`, including the map labels and evidence on which it is based.

The thematic question is **scope-closed by that evidence**. It may synthesize, combine or rephrase evidenced map items, but it must not introduce a new substantive domain, population, problem or application that is absent from them. Evidence about economic decision-making does not by itself justify widening the theme to historical, social, environmental or ethical systems; each such direction requires its own support in the map.

“Several relevant perspectives” means several perspectives already justified by the evidence-backed map. It is not permission to import unrelated disciplines merely to create breadth.

Then construct the broadest coherent UCR programme that addresses the question from those evidenced perspectives.

A course belongs in this programme because its actual content helps answer the organising question, not simply because it is broad, interesting or available.

Do not choose a course first and then widen the thematic question or invent a bridge argument to justify it. If a candidate course requires a new interest or perspective not established before course selection, exclude it unless the concept is formally revisited from the external evidence and interest map.

If the evidence does not support a compelling expansion far beyond the field, keep the thematic programme relatively close to the field. Do not manufacture eclecticism merely to make option 3 look dramatically different.

## 9. Construct the three UCR programmes from the fixed concepts

Only now use the current enriched UCR course database, especially:

- `osiris`
- `name`
- `profile`
- `discipline`
- `topics`
- `methods`
- `description2`
- `preq1`
- semester-availability columns.

Give outline-derived `profile` information particular weight where available.

For the counselor corpus use the fixed **Fall 2026 UCR start**:

- Semester 1: `2026h2`
- Semester 2: `2027h1`
- Semester 3: `2027h2`
- Semester 4: `2028h1`
- Semester 5: `2028h2`
- Semester 6: `2029h1`

Each of the three UCR programmes must have:

- exactly 24 unique courses;
- exactly four courses in each semester;
- at least six 300-level courses;
- `ACCPPDE101` Personal & Professional Development during Year 1;
- every prerequisite completed in an earlier semester;
- every course actually offered in its assigned semester;
- no duplicated course.

Validate these rules mechanically with code against the course database.

Do not export a programme that fails validation. Repair it and validate again.

Do not invent additional UCR requirements concerning clusters, concentrations, disciplinary distributions or breadth.

If course availability makes the fixed concept infeasible, repair the course selection while preserving the concept. If the concept itself proves academically infeasible at UCR, revisit it using the same evidence-backed map; do not simply switch to an unrelated theme that happens to fit the catalogue.

### 9.1 Internal course-to-concept traceability check

Before finalizing the three UCR programmes, keep an **internal** course-to-concept checklist or table for production/QC. This is not a new required schema field under the current `1.2` contract.

Except for mandatory `ACCPPDE101`:

- each `ucr-depth` course must map to one or more `coreField` items;
- each `ucr-balanced` course must map to the core field or one of the selected `balancedDirections`;
- each `ucr-thematic` course must map to the thematic question and at least one evidenced map item that genuinely forms part of that question.

For each course, be able to state in one concrete sentence what part of the fixed concept it serves, using the actual course profile/content. Generic claims such as “adds breadth,” “adds context,” “provides another perspective,” or “helps understand complex systems” do not count unless that perspective/context is itself evidenced in the academic interest map and directly relevant to the question.

If a course cannot pass this test, remove it. Do not repair the problem by retroactively widening the academic interest map or thematic question to fit the course.

## 10. Build the comparison only after all four curricula are complete

Do not design comparison blocks while the programmes are still being assembled.

After reconstructing the external programme and validating all three UCR programmes, derive substantive comparison blocks from the complete curricula.

Comparison blocks are **analytical alignments**, not partitions of the 180-EC curricula.

Therefore:

- there is no required number of blocks;
- there is no default three-block structure;
- blocks are not automatically 60 EC each;
- do not allocate all 24 UCR courses to blocks merely because they exist in the programme;
- block totals do not have to sum to 180 EC for every programme;
- unequal credit totals across aligned cells are legitimate;
- meaningful blank cells are expected when no genuine counterpart exists.

Start from substantive correspondences and differences in the completed curricula and let those determine the number and size of blocks. Do not first choose an aesthetically convenient number of blocks and then aggregate the curricula to fit it.

A pattern in which the comparator has three round 60-EC blocks, or every UCR column contributes the same number of courses or same credits to every block, is **presumptively a template artefact**. Stop and verify each block independently. Retain such equality only when the actual curricula independently justify it.

Do not aggregate an external 180-EC curriculum into three 60-EC buckets merely because 180 divides evenly by three. Do not use four UCR courses/30 EC per block, or any other fixed allocation, as a default comparison recipe.

Within blocks:

- align genuinely comparable components horizontally;
- preserve actual EC weights;
- show credits consistently for external and UCR components;
- preserve meaningful blank cells;
- preserve genuine structural differences;
- treat methods/research training as substantive disciplinary content where appropriate;
- leave specialist external components unmatched when UCR has no genuine counterpart.

Do not force one external component to equal one UCR course.

Do not fill gaps for visual symmetry.

Do not use numerical depth or breadth scores.

## 11. Explanatory notes

Use the existing reusable note taxonomy only where a material difference could otherwise be misunderstood:

- `less-disciplinary-depth`
- `related-fields-not-full-discipline`
- `missing-specialist-components`
- `different-curricular-structure`

Do not add a note merely because a template exists.

Populate only claims supported by the researched curricula.

## 12. Production record

Create one structured counselor comparison record per successfully completed normalized target.

Use the current repository comparison structure and counselor-production schema. Current production records use:

`schemaVersion: "1.2"`

Each record must at minimum contain:

- `origin: "counselor"`;
- top-level stable record `id` equal to the permanent `counselor_programme_id`;
- `programmeProvider.counselorProgrammeId` equal to the same permanent ID;
- normalized registry metadata required by the schema, including canonical target name, orders, institution IDs, programme type/status, eligibility, normalized languages and modes, and provenance arrays;
- approved primary official source URL;
- relevant additional official sources/provenance;
- academic year/currentness information;
- selected route/track where applicable;
- `academicRationale` containing the evidence-backed map, balanced directions and thematic question;
- all four programme roles;
- complete UCR six-semester schedules;
- external curriculum/component information and EC;
- comparison blocks and alignments;
- deliberate gaps;
- explanatory note where warranted;
- internal validation/source metadata.

The internal course-to-concept checklist in Section 9.1 is a production/QC aid; do not add a new record field merely to store it unless the schema is separately changed by an explicit later decision.

Do not use `AANGEBODEN_OPLEIDINGCODE`, source worksheet row, programme-unit code or recognized-programme code as the comparison ID.

Under the current contract:

`id == programmeProvider.counselorProgrammeId == counselor_programme_id`

Use:

`data/counselor/comparisons/<counselor_programme_id>.json`

Legacy provider/offering identifiers remain provenance fields only.

## 13. Incremental-production rule

Create the individual comparison files under `data/counselor/comparisons/`, but **do not create the production `programmes.json` or `interests.json` discovery indexes while the comparison corpus is incomplete**.

Leave existing pilot indexes unchanged during incremental production.

Generate the full production discovery indexes in one later finalisation step after the deterministic comparison corpus is complete and quality-controlled. Build those indexes from the normalized registry/interest layer and include only targets in the then-current counselor production scope.

Do not modify:

- `data/examples/`;
- `data/catalog.json`;
- the public website;
- LinkedIn records;
- publication queues;
- generated PDFs.

Counselor production does not constitute public approval.

## 14. Batch quality control

Before completing the run, verify for every new record:

- target satisfies the current production-scope filter;
- correct `counselor_programme_id`, `registry_order` and `production_order`;
- production metadata matches `data/registry/programmes.csv`, including canonical name, institutions, programme type/status, eligibility, languages, modes and required provenance arrays;
- top-level `id` and `programmeProvider.counselorProgrammeId` both equal the permanent ID;
- current official source basis;
- coherent and valid external pathway;
- fair treatment of optional/open curriculum space;
- inherited-across-split interest evidence is not used as target-specific evidence without independent official corroboration;
- complete evidence-backed academic interest map;
- one or two `balancedDirections` selected from actual adjacent directions in the map;
- explicit evidence-backed `thematicQuestion` tied to map items;
- the thematic question introduces no new substantive domain, population, problem or application absent from its cited evidence basis;
- “several relevant perspectives” has not been used to import unevidenced disciplines;
- thematic concept was not generated from UCR course availability;
- three substantively distinct UCR alternatives without manufactured breadth;
- every non-PPD UCR course passes the internal course-to-concept traceability check;
- no course is justified only by generic breadth/context/perspective language;
- exact 24-course UCR totals;
- four courses per semester;
- unique UCR courses;
- at least six 300-level courses;
- PPD in Year 1;
- prerequisites satisfied;
- semester availability satisfied;
- comparison blocks are genuine alignments rather than forced 180-EC partitions;
- external curriculum has not been aggregated into round credit buckets merely to create a neat layout;
- UCR courses have not been distributed by a fixed equal-per-block recipe such as four courses/30 EC per block;
- comparison credits preserved;
- substantive alignment of comparison blocks;
- no invented equivalence;
- no hidden UCR limitation;
- counselor-production schema/structural validity.

Run automated validation across all completed current production records.

For each batch, inspect the records as a set for systematic failure modes, including:

- repetitive UCR programmes;
- overuse of the same courses without substantive justification;
- recurring thematic course palettes across unrelated disciplines;
- generic thematic programmes;
- thematic questions that are interchangeable across unrelated targets;
- unsupported domains introduced in thematic questions;
- unsupported cross-disciplinary jumps;
- forced three-block/60-EC comparison structures;
- fixed equal UCR course/credit allocations across comparison blocks;
- copied logic between Dutch/international variants where the overlap has not been independently justified by the actual target evidence;
- a tendency to weaken external programmes.

Similarity between genuinely related or language-variant programmes is not itself a defect. The defect is unsupported reuse or template-driven construction.

Do not change a sound record merely to create artificial variety across the batch.

## 15. Exceptions

If a selected in-scope target cannot be reconstructed confidently from current official evidence:

- do not guess;
- do not substitute another programme;
- do not manufacture curriculum structure;
- leave that production comparison uncreated;
- document the exact unresolved problem and official sources checked;
- continue processing the other selected targets.

If current official evidence suggests the normalized target identity itself is wrong or has materially changed, flag a **registry exception** rather than silently changing the comparison target during production.

If no academically defensible adjacent direction or thematic question can be established from the evidence, do not invent one. Report the limitation and resolve it explicitly before treating that record as complete.

Likewise, if no academically defensible UCR alternative can satisfy the feasibility rules, report the genuine limitation rather than manufacturing a match.

A target excluded solely because its programme type is `joint-degree`, `double-bachelor` or `dual-degree-route` is not an exception or blocked case under the current rules; it is simply outside the current counselor production scope.

## 16. GitHub working rules

Work only on the existing `main` branch.

Do not create:

- another branch;
- a pull request;
- a duplicate repository structure.

Do not restructure the repository.

Do not change the authoritative project documentation, normalized registry, application code or schemas merely to make a production batch easier. If a genuine contract or registry problem is discovered, report it and fix it in the appropriate upstream layer rather than silently redesigning the project during production.

Commit completed production records and strictly necessary validation changes to `main`.

## 17. Operating sequence for each selected target

Use this exact high-level sequence:

1. confirm normalized target and registry metadata;
2. reconstruct the exact external programme from current official sources;
3. retrieve target-specific programme-interest evidence;
4. build the academic interest map;
5. freeze `ucr-depth`, selected balanced direction(s), and the thematic organising question;
6. verify that the thematic question adds no unevidenced domain or perspective;
7. only then select UCR courses;
8. complete the internal course-to-concept traceability check;
9. schedule and mechanically validate all three UCR programmes;
10. build comparison blocks from the completed curricula without forcing symmetry or fixed allocation;
11. create the schema-1.2 production record with `academicRationale`;
12. run record-level and batch-level QC.

Do not skip the academic interest map, theme-definition or traceability step even when the field appears obvious.

## 18. Final deliverable

At the end, report concisely:

1. the exact `counselor_programme_id` values and `production_order` values selected;
2. the normalized programme names and participating institution(s);
3. the number of completed comparison records;
4. any unresolved/exception targets;
5. confirmation that all completed UCR programmes passed mechanical feasibility validation;
6. any material source discrepancies or registry exceptions;
7. the GitHub commit containing the batch;
8. any issue that should be resolved before starting the next batch.

Do not stop for routine intermediate approval during the batch.
