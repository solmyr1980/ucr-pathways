# UCR Pathways — Production Instructions

**Status:** Authoritative academic production procedure

## Purpose and boundary

This document is the **single authoritative procedure** for generating, validating and recording UCR Pathways academic comparisons.

It governs:

1. **student workflow** — personalized generation from an actual prospective student's submitted interests;
2. **counselor workflow** — deterministic generation of one comparison per normalized counselor programme target in the current production scope.

Use the Master Specification for durable product meaning, branding and architecture. Use the Web and LinkedIn Workflow only for downstream public curation/publication. Use `UCR_Pathways_Supporting_Research_Workflows.md` only when the task concerns programme-interest enrichment or synthetic interests; it is not part of routine comparison-production context.

Academic production uses:

- current official university sources for the external programme;
- the enriched UCR course database for UCR course evidence and feasibility;
- `data/registry/` for normalized counselor identity, order, provenance and programme-interest evidence;
- repository schemas/validators for executable record contracts.

Do not duplicate this procedure in batch assignments or other workflow documents.

---

# 1. Shared academic principles

Every comparison uses the four stable semantic roles:

1. `comparator`;
2. `ucr-depth`;
3. `ucr-balanced`;
4. `ucr-thematic`.

For both workflows:

- construct the four programmes before designing the comparison;
- use course/component content rather than titles alone;
- represent genuine gaps and limitations honestly;
- do not manufacture weak UCR matches;
- do not weaken the external programme to make UCR look better;
- preserve actual EC weights;
- account for the complete 180 EC of every programme in the comparison exactly once;
- do not force row-by-row, credit-by-credit or aesthetic symmetry;
- use reusable explanatory notes only when they prevent a material misunderstanding.

Visible labels follow the Master Specification rather than exposing internal role names.

---

# 2. Shared evidence and feasibility rules

## 2.1 External programme reconstruction

Use current official university evidence. Prefer, where available:

1. formal curriculum or graduation requirements;
2. official curriculum/study-programme pages;
3. official route, track or specialization pages;
4. official course-catalogue entries;
5. general official prospective-student pages.

For the comparator distinguish:

- compulsory components;
- restricted choices;
- routes/tracks/specializations;
- genuinely free elective/profiling space;
- mathematics, statistics, methods and research training where relevant;
- thesis/capstone requirements;
- EC weights.

Reconstruct one coherent **180-EC pathway**. Where choices must be instantiated, select one coherent valid pathway. Where the programme contains genuine open elective or profiling space, preserve that space explicitly as a curriculum component rather than inventing content for it or dropping it from the comparison.

Never combine mutually exclusive choices, present optional material as compulsory, invent components to fill open space, violate programme rules, deliberately choose weak options, or make the programme artificially narrow.

Preserve relevant source metadata, including primary/additional official URLs, academic/curriculum year, date checked, selected route/track and exception notes.

## 2.2 UCR course evidence and mechanical feasibility

Use the enriched UCR course database as the authoritative source for UCR selection and scheduling. Use actual course content, giving particular weight to outline-derived `profile` information where available, alongside name, discipline, topics, methods, descriptions, prerequisites and planned semester availability.

Each UCR programme must have:

- exactly **24 unique courses**;
- exactly **4 courses in each of six semesters**;
- at least **6 courses at 300 level**;
- **Personal & Professional Development** during Year 1;
- every prerequisite completed in an earlier semester;
- every course available in its assigned semester.

Do not invent additional cluster, unit, concentration, breadth or disciplinary-distribution requirements.

Validate these rules mechanically against the enriched course database. Repository/schema validation does not replace academic feasibility validation.

---

# 3. Student workflow

## 3.1 Input and interpretation

Receive the actual `interest_statement`, a stable internal delivery identifier where needed, and relevant cohort/starting-semester context.

Preserve the student's original wording exactly and store the academic interpretation separately. Do not collect unnecessary personal information in the academic record or assume that the first-mentioned interest is more important.

Interpret the statement in terms of relevant disciplines, questions, phenomena/problems, practical interests/skills and meaningful connections. For one stated interest, broaden through genuine subfields, questions and neighbouring perspectives rather than inventing a second interest.

## 3.2 Comparator and production sequence

Choose the Dutch bachelor that provides the most useful disciplinary/depth endpoint for the student's interests. Do not automatically choose the first-mentioned discipline. Prefer a current Dutch research-university bachelor where suitable.

For manually supervised production, propose the comparator and authoritative source basis for approval before full generation unless an approved automated configuration explicitly removes that checkpoint.

Then work in this order:

1. preserve and interpret the student input;
2. select and reconstruct the external comparator under Section 2.1;
3. construct `ucr-depth` as the closest feasible UCR match responsive to the student's interests;
4. construct `ucr-balanced` with substantially more balanced weight across the student's interests;
5. construct `ucr-thematic` from questions/themes connecting those interests;
6. schedule and mechanically validate all three UCR programmes under Section 2.2;
7. construct the comparison under Section 5;
8. create the canonical student record under Section 7;
9. render the requested private student-app/PDF representations;
10. only after explicit public approval, derive a publication-safe record when requested.

## 3.3 Student output requirements

The student interface must preserve the distinction between:

- **You told us that…** — original wording;
- **For us, this means that…** — academic interpretation.

Use the placeholder disclaimer until approved final wording is supplied:

> **[PLACEHOLDER — insert approved student-program disclaimer from the printed butterfly.]**

Canonical student records remain private.

---

# 4. Counselor workflow

## 4.1 Unit, scope and identity

The production unit is one normalized target from `data/registry/programmes.csv`.

A target is currently in scope only when:

- `production_eligible=true`;
- `production_order` is nonblank; and
- `programme_type=standard`.

`joint-degree`, `double-bachelor` and `dual-degree-route` targets remain valid normalized registry targets but are temporarily outside counselor comparison production. Do not alter registry identity or lifecycle fields merely to implement that presentation-scope exclusion.

The stable production identity is `counselor_programme_id`. Source worksheet rows, offered-programme UUIDs, programme-unit codes, recognized-programme codes, language/mode and campus registrations are provenance/normalization inputs rather than independent comparison identities.

Follow `production_order` among in-scope targets. Production is resumable: skip a target only when a completed current production record already exists and requires no repair.

## 4.2 Programme-interest evidence

Retrieve normalized programme-interest rows linked to the exact `counselor_programme_id`.

Use relationship types as follows:

- **Direct programme interest** and **Stable study direction** — strongest evidence for related directions;
- **Curricular topic** — may broaden the substantive picture;
- **Illustrative or temporary topic** and **Outcome or individual trajectory** — may inform applications/themes cautiously but do not by themselves define the core or a major direction.

Where `target_mapping_status=inherited-across-split-targets`, the row is provenance/general discovery context only and is not target-specific academic evidence unless independently corroborated by current official evidence for that exact target.

A search term never changes or personalizes the fixed comparison.

## 4.3 Canonical counselor production pipeline

Complete the following sequence for **one target end-to-end** before moving to the next target.

### Step 1 — Confirm target and reconstruct the external programme

Confirm normalized identity, institutions and provenance. Research the exact academic programme/route represented by the normalized target and reconstruct one coherent valid 180-EC pathway under Section 2.1.

When the target is a normalized merge, research the current academic programme rather than re-splitting administrative registrations. When it is a normalized split, research the exact named route/track represented by that target.

If current official evidence materially conflicts with normalized identity, treat it as a registry exception rather than silently changing the target.

### Step 2 — Build the evidence-backed academic interest map

Build the map **before selecting any UCR courses**. The UCR course catalogue must not generate the map.

The map has three layers:

**Core field** — defining disciplines/subfields, foundations/progression, methods/mathematics/statistics/research training, advanced/specialist work and thesis/capstone where relevant.

**Adjacent directions** — genuinely related directions supported by formal routes/specializations, stable study directions, strong direct programme interests, recurring curricular connections or programme-supported questions/applications.

**Questions and applications** — evidenced questions, phenomena, problems and applications that the field addresses and that could support a thematic programme.

Every substantive map item must be traceable to at least one current official source for the exact target or one valid target-specific programme-interest row.

### Step 3 — Freeze the three UCR programme concepts

Establish all three concepts before course selection.

**`ucr-depth`** — target the core field. Reproduce as closely as feasible the substantive core, progression, methods and advanced work. Preserve genuine UCR limitations rather than compensating with weakly related material.

**`ucr-balanced`** — retain a substantial core and select **one or two adjacent directions from the map**. Those selected directions are the only intended basis for broadening.

**`ucr-thematic`** — state one explicit organising question, problem, phenomenon or application based on evidenced map items.

The thematic question is **scope-closed by its evidence**: it may synthesize evidenced items but must not introduce a new substantive domain, population, problem or application absent from them. Evidence about economic decision-making, for example, does not by itself justify historical, social, environmental or ethical systems; each such direction needs its own evidence.

“Several relevant perspectives” means perspectives already justified by the evidence-backed map. If the evidence does not support a compelling expansion far beyond the field, keep the thematic concept relatively close to the field rather than manufacturing eclecticism.

### Step 4 — Select UCR courses from the frozen concepts

Only now use the enriched UCR course database.

Select courses because their actual content implements the already frozen concept. Do not pick attractive courses first and then widen the concept, invent a bridge argument or add a new interest to justify them.

If availability makes a course set infeasible, repair course selection while preserving the concept. Revisit a concept only when the concept itself proves genuinely infeasible, and then return first to the external evidence and interest map.

### Step 5 — Run course-to-concept traceability

Except for mandatory `ACCPPDE101` Personal & Professional Development:

- every `ucr-depth` course must map to one or more `coreField` items;
- every `ucr-balanced` course must map to the core field or one selected `balancedDirection`;
- every `ucr-thematic` course must map to the thematic question and at least one evidenced map item that genuinely forms part of that question.

For each course, be able to state one concrete sentence explaining what part of the fixed concept it serves using actual course content. Generic claims such as “adds breadth,” “adds context,” “provides another perspective,” or “helps understand complex systems” do not count unless that perspective/context is itself evidenced and directly relevant.

If a course cannot pass this test, remove it. The checklist is an internal production/QC aid under the current schema and is not a required record field.

### Step 6 — Schedule and mechanically validate

For the current counselor corpus use the fixed **Fall 2026 UCR start**:

- Semester 1: `2026h2`
- Semester 2: `2027h1`
- Semester 3: `2027h2`
- Semester 4: `2028h1`
- Semester 5: `2028h2`
- Semester 6: `2029h1`

Apply all feasibility rules in Section 2.2. Repair and revalidate until they pass; do not export a knowingly invalid programme.

### Step 7 — Build the comparison

Only after the external curriculum and all three UCR curricula are complete and validated, construct comparison blocks under Section 5.

### Step 8 — Create and validate the production record

Create the canonical counselor record under Section 7, run repository/schema validation and apply the completion gates in Section 9.

## 4.4 Counselor exceptions

Do not guess or substitute another target when a selected in-scope programme cannot be reconstructed confidently.

If no defensible adjacent direction or thematic question can be established from evidence, do not invent one. If no academically defensible UCR alternative can satisfy the feasibility rules, report the limitation rather than manufacturing a match.

A non-standard target excluded by the current scope is not a blocked case; it is simply outside production scope.

---

# 5. Comparison construction

Construct comparison blocks only from the **completed and validated 180-EC curricula**. The blocks are a lossless classification and alignment of those curricula, not a selective analytical summary.

Apply all of the following rules:

- there is no required number of blocks and no default three-block or 60/60/60 structure;
- every UCR course must appear in the comparison **exactly once**, including `ACCPPDE101` Personal & Professional Development;
- every external curriculum component in the reconstructed coherent pathway must appear **exactly once**;
- the displayed components for each of the four programme columns must total **180 EC**;
- genuine open-elective, profiling or restricted-choice space in the external programme must appear explicitly as such and retain its actual EC value;
- one comparison cell represents one canonical course/component; do not combine several UCR courses into a prose bundle;
- meaningful blank cells are legitimate when there is no sufficiently comparable component in another programme;
- unequal block sizes, unequal numbers of components within a block and structural gaps are legitimate and often desirable;
- methods, mathematics, statistics, econometrics, laboratory work and research training count as substantive disciplinary content where appropriate.

For current production records, comparison cells must refer back to the canonical programme data using stable identifiers rather than relying on free text alone:

- UCR cells use `courseCode` matching the scheduled UCR course;
- comparator cells use `componentId` matching the reconstructed external curriculum component.

Displayed text and credits must agree with the referenced canonical course/component. These stable references are validation keys; renderers may continue to display ordinary course/component names and EC values.

Start from substantive correspondences and differences and let them determine block number, titles, row alignment and size. Do not force one external component to equal one UCR course, move a component into more than one block, omit inconvenient components, or fill gaps for visual symmetry.

A pattern such as three round 60-EC blocks or identical UCR course allocation across blocks is a review signal when it appears repeatedly or without curricular justification; it is not forbidden when the actual curricula independently justify it.

Show EC credits consistently on both external and UCR components. Do not use numerical depth/breadth scores.

---

# 6. Reusable explanatory-note taxonomy

A note is optional and should appear only when a material difference could otherwise be misunderstood.

## `less-disciplinary-depth`

Use when UCR covers the field but the external programme provides a materially deeper specialist sequence.

> The [external programme] includes a more extensive sequence in [specialist areas]. At UCR, students can study [relevant UCR areas], but UCR does not offer the same depth or sequence in [field].

## `related-fields-not-full-discipline`

Use when UCR approaches the central subject/problem through related disciplines rather than offering the full disciplinary curriculum.

> The [external programme] combines [key components]. At UCR, students can approach [central subject/problem] through fields such as [relevant UCR fields]. These programmes therefore offer related perspectives rather than reproducing a full [discipline] curriculum.

## `missing-specialist-components`

Use when UCR provides a substantial core match but lacks particular specialist components.

> Both programmes include substantial study of [shared field]. The [external programme] additionally includes specialist work in [missing areas]. UCR students can instead combine [UCR strengths], but those specialist components are not offered at the same level of depth.

## `different-curricular-structure`

Use when similar substantive territory is organized differently.

> The [external programme] organizes study around a structured sequence in [discipline/route]. At UCR, comparable subjects are distributed across courses in [fields]. The UCR programme therefore covers related territory through a different curricular structure rather than reproducing the external programme course by course.

Populate only evidenced parameters, do not exaggerate equivalence, and omit the note when the comparison is already self-explanatory.

---

# 7. Canonical records

Create one canonical structured record before rendering any output.

## 7.1 Shared core

Preserve at minimum:

- stable record ID and `origin` (`student` or `counselor`);
- four programme identities and semantic roles;
- comparator name, institution/provider, official source and the complete reconstructed 180-EC component list;
- complete 24-course set and six-semester schedule for each UCR programme;
- comparison blocks that account for every canonical component exactly once while preserving deliberate gaps in horizontal alignment;
- stable comparison references back to UCR course codes and comparator component IDs in current production records;
- explanatory-note type/parameters or rendered note where needed;
- academic validation status and internal source/verification metadata.

## 7.2 Student additions

Preserve original `interest_statement`, separate academic interpretation, internal delivery identifier where required, and relevant cohort/starting-semester context. Student records remain private.

## 7.3 Counselor additions

Current counselor production records use `schemaVersion: "1.3"`.

Preserve the permanent `counselor_programme_id`, normalized target metadata/provenance required by the current schema, and `academicRationale` containing:

- evidence-backed `coreField`;
- evidence-backed `adjacentDirections`;
- evidence-backed `questionsApplications`;
- one or two selected `balancedDirections`;
- explicit `thematicQuestion`, its evidence and the map labels on which it is based.

The canonical comparator object must contain its complete reconstructed `components` list. Each component has a stable `id`, display `name` and `credits`; the list totals 180 EC. Comparison cells then refer to those components by `componentId`.

Every UCR comparison cell must contain the scheduled course's `courseCode`. The cell text and credits must match that canonical course. This prevents a course from being duplicated, omitted or silently renamed in the comparison layer.

For current production records:

`id == programmeProvider.counselorProgrammeId == counselor_programme_id`

Use normalized arrays for languages and modes. Legacy provider/offering identifiers remain provenance only.

The canonical record contains semantic content, not renderer coordinates, CSS or page geometry.

---

# 8. Library and public-export boundaries

The counselor comparison library stores one fixed record per completed in-scope normalized target. Discovery programme metadata and programme-interest indexes remain separate from comparison content. Do not flatten all interests into a comparison record; `academicRationale` stores only evidence actually used for the three UCR concepts.

During incremental counselor production, create individual files under `data/counselor/comparisons/` but do not create the final production `programmes.json` or `interests.json` discovery indexes until the comparison corpus is complete and quality-controlled. Leave pilot indexes unchanged.

Neither workflow publishes automatically. Public export requires substantive human review and explicit public-use approval. Derive publication-safe records from canonical academic records without reselecting courses, rebuilding alignments or inventing renderer-specific academic facts.

---

# 9. Completion gates

The purpose of final QC is to confirm that the procedure above was followed, not to restate it in a second instruction set.

## 9.1 Record-level counselor gates

A counselor record is complete only when all six gates pass:

1. **Evidence gate** — external programme is fairly reconstructed and every substantive interest-map item is evidence-backed for the exact target.
2. **Concept gate** — depth target, one/two balanced directions and thematic question were frozen before UCR course selection; the theme introduces no unevidenced domain, population, problem or application.
3. **Course gate** — every non-PPD course passes course-to-concept traceability; no course relies only on generic breadth/context language.
4. **Feasibility gate** — all mechanical UCR schedule constraints pass against the enriched database.
5. **Comparison gate** — all four columns account for exactly 180 EC; each canonical UCR course/external component appears exactly once; PPD is visible; stable references agree with canonical data; and block alignment preserves genuine gaps rather than imposing a symmetry template.
6. **Record gate** — the current counselor schema/validator passes and normalized identity/provenance matches the registry.

## 9.2 Batch-level counselor QC

After all individually completed records pass the gates, inspect the batch only for **systematic** failure modes:

- unsupported thematic domains or cross-disciplinary jumps;
- generic/interchangeable thematic questions across unrelated targets;
- recurring thematic course palettes or course reuse without independent justification;
- recurring block templates or equal allocations that are not independently justified by the curricula;
- copied logic between variants without target-specific support;
- systematic weakening of external programmes.

Similarity between genuinely related programmes is not itself a defect. Do not change a sound record merely to create artificial variety.

## 9.3 Student completion

Confirm the student input is preserved verbatim, interpretation stored separately, UCR schedules mechanically valid, all four comparison columns account for the complete 180 EC without duplication or omission, comparison alignment is fair, and privacy/publication boundaries are respected.

Only then release the requested artifact or library record.