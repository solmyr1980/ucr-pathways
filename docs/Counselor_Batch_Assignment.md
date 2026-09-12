# Counselor Batch Assignment

**Reference name:** Counselor Batch Assignment  
**Purpose:** Reusable production assignment for batches of deterministic counselor comparisons  
**Default batch size:** 20 programme-provider records  
**Fixed UCR starting cohort:** Fall 2026  
**Repository:** `solmyr1980/ucr-pathways`

Use this assignment when producing counselor-comparison batches. For later batches, select the next 20 unprocessed programme-provider records in registry worksheet order unless the user explicitly specifies a different batch.

---

# UCR Pathways — Counselor Corpus Production

## Objective

Produce the next batch of deterministic counselor comparisons for the UCR counselor comparison library.

This is production work, not another methodology pilot.

Each selected Dutch bachelor programme-provider record must produce one fixed four-programme comparison:

1. the exact external Dutch bachelor programme-provider record;
2. `ucr-depth` — the closest feasible UCR match;
3. `ucr-balanced` — the field plus substantively related subjects;
4. `ucr-thematic` — a broader coherent UCR programme built around relevant questions, applications and academic directions connected to the field.

The comparison belongs to the programme-provider record. It is not personalized to an individual student.

## 1. Retrieve the authoritative project instructions first

Before analysing or producing anything, retrieve the current versions directly from GitHub of:

- `docs/UCR_Pathways_Master_Specification.md`
- `docs/UCR_Pathways_Production_Instructions.md`
- `docs/UCR_Pathways_Web_LinkedIn_Workflow.md`

Also inspect the current repository implementation relevant to counselor records, including:

- `data/counselor/README.md`
- `data/schema/example.schema.json`
- existing comparison examples where useful;
- the counselor Shiny implementation where necessary to confirm the current data contract.

Use the GitHub versions as authoritative. Do not substitute remembered instructions, earlier chats or superseded Project Source copies.

## 2. Required source data

Use:

- the current `UCR_Pathways_Programme_Registry.xlsx`;
- `Pathways_programmes` as the authoritative programme-provider registry;
- `programme_interests` as the existing programme-interest evidence/discovery table;
- the current `ucr_courses_enriched.xlsx` as the authoritative UCR course database;
- current official university sources for external programme structure.

Do not modify either source workbook during this assignment.

## 3. Select the batch

For the first production run, process exactly **worksheet rows 2–21 inclusive** of `Pathways_programmes`.

For subsequent runs, process the next 20 programme-provider records in ascending worksheet-row order that do not already have a completed current production counselor comparison, unless the user explicitly specifies another batch.

Use the exact programme-provider record on each selected row. Do not substitute:

- another provider;
- the parent programme for a variant;
- another language version;
- a similarly named programme;
- a programme that appears easier to compare with UCR.

The stable programme-provider identifier is the row's `AANGEBODEN_OPLEIDINGCODE`.

Pilot search fixtures and public examples do **not** automatically count as completed production counselor records. If an existing validated example corresponds to a selected record, use it as useful prior work, verify it against the current sources and course database, and convert it into a production counselor record rather than unnecessarily starting from zero.

Do not replace a blocked record with the next registry row merely to keep the number of completed records at 20. Complete the remainder of the selected batch and report the blocked case.

## 4. Research each external programme independently

For every selected programme-provider record, establish the exact current programme and reconstruct it from current official sources.

Use this source hierarchy where available:

1. formal curriculum or graduation requirements;
2. official curriculum/study-programme pages;
3. official tracks, routes or specialisations;
4. official course-catalogue information;
5. general official prospective-student pages.

The registry `WEBSITE` field is a starting point, not automatically the definitive curriculum source.

Verify the exact provider and programme variant.

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
- silently force official curriculum information to agree with registry metadata when they conflict.

If registry information and current official programme information materially disagree, preserve the official programme structure and report the discrepancy.

Research quality must not decline for programmes appearing later in the batch.

## 5. Use programme-interest evidence correctly

Retrieve the `programme_interests` rows belonging to the exact programme-provider record.

These records are supporting evidence about academically relevant interests and directions associated with the programme. They are **not** a student's submitted interests.

Use them as follows:

- `Direct programme interest` and `Stable study direction` provide the strongest evidence for related directions;
- `Curricular topic` may broaden the substantive picture;
- `Illustrative or temporary topic` and `Outcome or individual trajectory` may inform applications or themes cautiously but should not define the programme's core.

Do not generate a different comparison depending on a search term. Every search route must ultimately lead to the same fixed comparison.

## 6. Construct `ucr-depth`

Construct the feasible UCR programme that comes closest to the substantive core, progression and methods of the external programme.

Consider disciplinary content, methods, mathematics/statistics, research training and advanced work—not merely similarities in course titles.

Where UCR genuinely lacks important specialist areas, preserve that limitation. Do not compensate with weakly related courses merely to create apparent equivalence.

## 7. Construct `ucr-balanced`

Retain a substantial core of the external field while deliberately adding closely related subjects available at UCR.

Choose those related subjects from:

- the academic structure of the external programme;
- strong associated programme-interest evidence;
- neighbouring academic questions that are substantively defensible.

The result should be meaningfully broader than `ucr-depth`, not simply the same programme with a few arbitrary substitutions.

## 8. Construct `ucr-thematic`

Construct the broadest coherent UCR programme that remains recognisably connected to the external field.

Organise it around relevant questions, phenomena, applications or combinations of perspectives rather than attempting to reproduce the external disciplinary structure.

Use associated programme-interest evidence where helpful, but do not imply that every theme included in the UCR version is itself a structural part of the external bachelor.

Use a case-specific visible label. Avoid wording that falsely implies an individual counselor user has supplied personal interests.

## 9. Build and mechanically validate every UCR programme

Use the enriched UCR course database, especially:

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

## 10. Build the comparison only after all four curricula are complete

Do not design comparison blocks while the programmes are still being assembled.

After reconstructing the external programme and validating all three UCR programmes:

- derive substantive comparison blocks;
- align genuinely comparable components horizontally;
- preserve meaningful blank cells;
- preserve actual EC weights;
- show credits consistently for external and UCR components;
- treat methods/research training as substantive disciplinary content where appropriate.

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

Create one structured counselor comparison record per successfully completed programme-provider.

Use the current repository comparison structure and schema conventions rather than inventing a parallel format.

Each record must at minimum contain:

- current schema version;
- `origin: "counselor"`;
- a stable record ID;
- `programmeProvider.sourceExcelRow`;
- `programmeProvider.programmeProviderId`;
- the recognized-programme identifier where actually available;
- exact programme/provider metadata needed for traceability;
- comparator programme name and institution;
- approved primary official source URL;
- relevant additional official sources/provenance;
- academic year/currentness information;
- selected route/track where applicable;
- all four programme roles;
- the complete UCR six-semester schedules;
- external curriculum/component information and EC;
- comparison blocks and alignments;
- deliberate gaps;
- explanatory note where warranted;
- internal validation/source metadata.

For this production corpus, use the exact `AANGEBODEN_OPLEIDINGCODE` as the stable `programmeProviderId`.

Unless the current repository already establishes a different production convention, also use this value as the comparison record ID and filename:

`data/counselor/comparisons/<AANGEBODEN_OPLEIDINGCODE>.json`

Do not infer an `ERKENDEOPLEIDINGSCODE` where the registry field is blank. Preserve variant information separately where relevant.

## 13. Incremental-production rule

Create the individual comparison files under `data/counselor/comparisons/`, but **do not create the production `programmes.json` or `interests.json` discovery indexes while the corpus is incomplete**.

Leave the existing pilot indexes unchanged during incremental production.

Generate the full production discovery indexes in one later finalisation step after the deterministic comparison corpus is complete and quality-controlled. This prevents the deployed counselor app from switching prematurely to a partial production database.

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

- correct source registry row;
- correct programme-provider ID;
- exact programme and provider identity;
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

For each batch, also inspect the records as a set for systematic failure modes—for example repetitive UCR programmes, overuse of the same courses without substantive justification, generic thematic programmes, or a tendency to weaken external programmes.

Do not change a sound record merely to create artificial variety across the batch.

## 15. Exceptions

If a selected programme cannot be reconstructed confidently from current official evidence:

- do not guess;
- do not substitute another programme;
- do not manufacture curriculum structure;
- leave that production comparison uncreated;
- document the exact unresolved problem and the official sources checked;
- continue processing the other selected records.

Likewise, if no academically defensible UCR alternative can satisfy the feasibility rules, report the genuine limitation rather than manufacturing a match.

## 16. GitHub working rules

Work only on the existing `main` branch.

Do not create:

- another branch;
- a pull request;
- a duplicate repository structure.

Do not restructure the repository.

Do not change the authoritative project documentation, application code or schemas merely to make a batch easier. If a genuine contract problem is discovered, report it rather than silently redesigning the project during production.

Commit the completed production records and any strictly necessary batch-validation changes to `main`.

## 17. Final deliverable

At the end, report concisely:

1. the exact source worksheet rows selected;
2. the programme names and programme-provider IDs;
3. the number of completed comparison records;
4. any unresolved/exception records;
5. confirmation that all completed UCR programmes passed mechanical feasibility validation;
6. any material source discrepancies;
7. the GitHub commit containing the batch;
8. any issue that should be resolved before starting the next batch.

Do not stop for routine intermediate approval during the batch.
