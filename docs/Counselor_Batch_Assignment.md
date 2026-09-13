# Counselor Batch Assignment

**Reference name:** Counselor Batch Assignment  
**Purpose:** Reusable production assignment for batches of deterministic counselor comparisons  
**Default batch size:** 20 normalized counselor programme targets  
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
3. `ucr-balanced` — the field plus substantively related subjects;
4. `ucr-thematic` — a broader coherent UCR programme built around relevant questions, applications and academic directions connected to the field.

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

## 2. Authoritative registry model

The unit of production is one row of `data/registry/programmes.csv` with:

- a permanent `counselor_programme_id`;
- `production_eligible=true`;
- a nonblank `production_order`.

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
- combine delivery/language/campus registrations that represent one academic programme;
- represent one joint/double/dual-degree route involving several institutions; or
- result from a split where one source representation contained several academically distinct targets.

Do not undo the Step 2/Step 3 normalization during comparison production.

## 3. Select the batch

Unless the user specifies otherwise, process the next **20** rows in ascending `production_order` from `data/registry/programmes.csv` that:

- have `production_eligible=true`; and
- do not already have a completed current production counselor comparison requiring no repair.

Do not select from original worksheet-row order independently of `production_order`.

Do not replace a blocked target with a later target merely to keep the number of completed comparisons at 20. Complete the remainder of the selected batch and report the blocked case.

Pilot search fixtures and public examples do **not** automatically count as completed production counselor records. Existing pre-normalization counselor records may be reused only after confirming that they correspond to the normalized target and satisfy the current production rules.

## 4. Preserve normalized target identity

For each selected target preserve:

- `counselor_programme_id`;
- `registry_order` and `production_order`;
- canonical target name;
- normalized institution identity/identities;
- programme type and current status;
- source worksheet rows;
- offered-programme UUIDs;
- programme-unit/recognized-programme/variant identifiers where present;
- aliases and relevant registry URLs;
- Step 2 resolution/provenance fields where applicable.

When the target is a normalized merge, research the current academic programme represented by the target rather than treating each historical registration as a separate comparator.

When the target is a normalized split, research the exact named route/track represented by that target.

When the target is joint/double/dual, preserve the real multi-institution/special structure rather than forcing it into a standard 180-EC single-provider model.

## 5. Research each external programme independently

For every selected target, establish the exact current programme and reconstruct it from current official sources.

Use this source hierarchy where available:

1. formal curriculum or graduation requirements;
2. official curriculum/study-programme pages;
3. official tracks, routes or specialisations;
4. official course-catalogue information;
5. general official prospective-student pages.

Registry URLs and Step 2 identity-resolution sources are starting evidence, not automatically sufficient curriculum evidence.

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
- deliberately select weak options to make UCR look stronger;
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

Where `target_mapping_status` is `inherited-across-split-targets`, treat the historical interest evidence cautiously: it was inherited from a pre-normalization source row and is not evidence that every signal is equally characteristic of every split target.

Do not generate a different comparison depending on a search term. Every search route must ultimately lead to the same fixed comparison.

## 7. Construct `ucr-depth`

Construct the feasible UCR programme that comes closest to the substantive core, progression and methods of the external programme.

Consider disciplinary content, methods, mathematics/statistics, research training and advanced work—not merely similarities in course titles.

Where UCR genuinely lacks important specialist areas, preserve that limitation. Do not compensate with weakly related courses merely to create apparent equivalence.

## 8. Construct `ucr-balanced`

Retain a substantial core of the external field while deliberately adding closely related subjects available at UCR.

Choose those related subjects from:

- the academic structure of the external programme;
- strong associated programme-interest evidence;
- neighbouring academic questions that are substantively defensible.

The result should be meaningfully broader than `ucr-depth`, not simply the same programme with arbitrary substitutions.

## 9. Construct `ucr-thematic`

Construct the broadest coherent UCR programme that remains recognisably connected to the external field.

Organise it around relevant questions, phenomena, applications or combinations of perspectives rather than attempting to reproduce the external disciplinary structure.

Use associated programme-interest evidence where helpful, but do not imply that every theme included in the UCR version is itself a structural part of the external bachelor.

Use a case-specific visible label. Avoid wording that falsely implies an individual counselor user has supplied personal interests.

## 10. Build and mechanically validate every UCR programme

Use the current enriched UCR course database, especially:

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

For the counselor corpus use the fixed **Fall 2026 UCR start**, with:

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

## 11. Build the comparison only after all four curricula are complete

Do not design comparison blocks while the programmes are still being assembled.

After reconstructing the external programme and validating all three UCR programmes:

- derive substantive comparison blocks from the complete curricula;
- align genuinely comparable components horizontally;
- preserve meaningful blank cells;
- preserve actual EC weights;
- show credits consistently for external and UCR components;
- treat methods/research training as substantive disciplinary content where appropriate.

Do not force one external component to equal one UCR course.

Do not fill gaps for visual symmetry.

Do not use numerical depth or breadth scores.

## 12. Explanatory notes

Use the existing reusable note taxonomy only where a material difference could otherwise be misunderstood:

- `less-disciplinary-depth`
- `related-fields-not-full-discipline`
- `missing-specialist-components`
- `different-curricular-structure`

Do not add a note merely because a template exists.

Populate only claims supported by the researched curricula.

## 13. Production record

Create one structured counselor comparison record per successfully completed normalized target.

Use the current repository comparison structure and schema conventions rather than inventing a parallel format.

Each record must at minimum contain:

- current schema version;
- `origin: "counselor"`;
- stable record/comparison ID equal to `counselor_programme_id` unless the repository contract explicitly separates them;
- `counselorProgrammeId` / normalized target identity;
- normalized target name and institution identity/identities;
- source registry rows and offered-programme UUIDs as provenance;
- programme-unit, recognized-programme and variant identifiers where available;
- approved primary official source URL;
- relevant additional official sources/provenance;
- academic year/currentness information;
- selected route/track where applicable;
- all four programme roles;
- complete UCR six-semester schedules;
- external curriculum/component information and EC;
- comparison blocks and alignments;
- deliberate gaps;
- explanatory note where warranted;
- internal validation/source metadata.

Do **not** use `AANGEBODEN_OPLEIDINGCODE`, source worksheet row, programme-unit code or recognized-programme code as the comparison ID.

Use:

`data/counselor/comparisons/<counselor_programme_id>.json`

unless a later explicit repository schema decision establishes a separate comparison ID.

## 14. Incremental-production rule

Create the individual comparison files under `data/counselor/comparisons/`, but **do not create the production `programmes.json` or `interests.json` discovery indexes while the comparison corpus is incomplete**.

Leave existing pilot indexes unchanged during incremental production.

Generate the full production discovery indexes in one later finalisation step after the deterministic comparison corpus is complete and quality-controlled. Build those indexes from the normalized registry/interest layer rather than directly from the legacy workbook.

Do not modify:

- `data/examples/`;
- `data/catalog.json`;
- the public website;
- LinkedIn records;
- publication queues;
- generated PDFs.

Counselor production does not constitute public approval.

## 15. Batch quality control

Before completing the run, verify for every new record:

- correct `counselor_programme_id` and `production_order`;
- correct normalized target identity and participating institution(s);
- source-row/offering provenance retained;
- current official source basis;
- coherent and valid external pathway;
- fair treatment of optional/open curriculum space;
- three substantively distinct UCR alternatives;
- exact 24-course UCR totals;
- four courses per semester;
- unique UCR courses;
- at least six 300-level courses;
- PPD in Year 1;
- prerequisites satisfied;
- semester availability satisfied;
- comparison credits preserved;
- substantive alignment of comparison blocks;
- no invented equivalence;
- no hidden UCR limitation;
- schema/structural validity.

Run automated validation across all completed records.

For each batch, inspect the records as a set for systematic failure modes—for example repetitive UCR programmes, overuse of the same courses without substantive justification, generic thematic programmes, or a tendency to weaken external programmes.

Do not change a sound record merely to create artificial variety across the batch.

## 16. Exceptions

If a selected target cannot be reconstructed confidently from current official evidence:

- do not guess;
- do not substitute another programme;
- do not manufacture curriculum structure;
- leave that production comparison uncreated;
- document the exact unresolved problem and official sources checked;
- continue processing the other selected targets.

If current official evidence suggests the normalized target identity itself is wrong or has materially changed, flag a **registry exception** rather than silently changing the comparison target during production.

Likewise, if no academically defensible UCR alternative can satisfy the feasibility rules, report the genuine limitation rather than manufacturing a match.

## 17. GitHub working rules

Work only on the existing `main` branch.

Do not create:

- another branch;
- a pull request;
- a duplicate repository structure.

Do not restructure the repository.

Do not change the authoritative project documentation, normalized registry, application code or schemas merely to make a production batch easier. If a genuine contract or registry problem is discovered, report it and fix it in the appropriate upstream layer rather than silently redesigning the project during production.

Commit completed production records and strictly necessary validation changes to `main`.

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
