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

Every comparison contains exactly one external `comparator` and between **one and three ordered UCR alternatives**.

The first UCR alternative is always the closest feasible response to the field/interests under consideration. Additional alternatives are optional and are generated sequentially only when they are evidence-backed, coherent, substantively distinct and mechanically feasible.

Concept labels such as `closest-match`, `related-direction` and `question-led` may be stored as internal metadata, but they are not mandatory slots. Do not create an alternative merely to instantiate a category.

For both workflows:

- construct the comparator and all included UCR programmes before designing the comparison;
- use course/component content rather than titles alone;
- represent genuine gaps and limitations honestly;
- do not manufacture weak UCR matches;
- do not weaken the external programme to make UCR look better;
- preserve actual EC weights;
- account for the complete 180 EC of every included programme in the comparison exactly once;
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

Each included UCR programme must have:

- exactly **24 unique courses**;
- exactly **4 courses in each of six semesters**;
- at least **6 courses at 300 level**;
- **Personal & Professional Development** during Year 1;
- every prerequisite completed in an earlier semester;
- every course available in its assigned semester.

Do not invent additional cluster, unit, concentration, breadth or disciplinary-distribution requirements.

Validate these rules mechanically against the enriched course database. Repository/schema validation does not replace academic feasibility validation.

## 2.3 Shared alternative-selection rule

Always attempt the UCR alternatives in order.

### Alternative 1 — closest feasible response

Construct the strongest defensible UCR programme for the evidenced field/interests. If no defensible 24-course UCR programme can be built, treat the case as an exception rather than exporting a weak comparison.

### Alternative 2 — first genuinely different route

Consider one additional coherent programme concept supported by the applicable evidence boundary. Include it only if it passes all four tests:

1. **evidence** — the concept is supported by permitted evidence;
2. **coherence** — it has a clear academic organising logic before course selection;
3. **distinctness** — it represents a substantively different choice from Alternative 1 rather than cosmetic reshuffling;
4. **feasibility** — it can satisfy all UCR mechanical constraints.

If Alternative 2 fails, stop. Do not manufacture Alternative 3.

### Alternative 3 — second genuinely different route

Only after Alternative 2 is included, consider one further concept under the same four tests. Include it if defensible; otherwise stop at two.

### Mechanical distinctness floor

The qualitative distinctness test above is primary, but every additional UCR alternative must also pass a hard mechanical floor.

For **every pair** of included UCR alternatives:

- each programme must contain at least **30 EC** of courses that are not present in the other programme;
- under the current 7.5-EC UCR course structure, this means at least **4 different courses** in each programme;
- equivalently, two 24-course alternatives may share at most **20 courses**.

This is a necessary condition, not a sufficient definition of distinctness. Passing the 30-EC floor does not make an alternative academically distinct by itself. The alternative must first have an evidence-backed organising concept, and the courses that differ must be genuine curricular consequences of that concept rather than arbitrary substitutions made to satisfy the number.

If an otherwise proposed alternative shares 21 or more of its 24 courses with any already included UCR alternative, reject it as `not-substantively-distinct`. Do not repair the failure by swapping unrelated courses merely to cross the threshold.

Three is the maximum, not the target. The stopping decision must be auditable in current production records.

---

# 3. Student workflow

## 3.1 Input and interpretation

Receive the actual `interest_statement`, a stable internal delivery identifier where needed, and relevant cohort/starting-semester context.

Preserve the student's original wording exactly and store the academic interpretation separately. Do not collect unnecessary personal information in the academic record or assume that the first-mentioned interest is more important.

Interpret the statement in terms of relevant disciplines, questions, phenomena/problems, practical interests/skills and meaningful connections. For one stated interest, broaden through genuine subfields, questions and neighbouring perspectives rather than inventing a second interest.

The student's complete submitted statement is valid evidence. If the student supplies several interests, alternatives may legitimately vary their relative emphasis, combine them differently or organise them around an evidenced question. Do not add an interest the student did not supply merely to make alternatives more different.

## 3.2 Comparator and production sequence

Choose the Dutch bachelor that provides the most useful disciplinary/depth endpoint for the student's interests. Do not automatically choose the first-mentioned discipline. Prefer a current Dutch research-university bachelor where suitable.

For manually supervised production, propose the comparator and authoritative source basis for approval before full generation unless an approved automated configuration explicitly removes that checkpoint.

Then work in this order:

1. preserve and interpret the student input;
2. select and reconstruct the external comparator under Section 2.1;
3. construct and validate Alternative 1 under Sections 2.2–2.3;
4. consider Alternative 2 under the same gates, including the pairwise 30-EC distinctness floor, and stop if it cannot be justified;
5. if Alternative 2 is included, consider Alternative 3 and require it to pass the same 30-EC floor against **each** already included UCR alternative;
6. construct the comparison under Section 5 using only the included programmes;
7. create the canonical student record under Section 7;
8. render the requested private student-app/PDF representations;
9. only after explicit public approval, derive a publication-safe record when requested.

## 3.3 Student output requirements

The student interface must preserve the distinction between:

- **You told us that…** — original wording;
- **For us, this means that…** — academic interpretation.

Do not promise a fixed number of programme options. Present the included alternatives as the UCR programmes that best fit what the student told us.

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

Programme-interest data describe interests associated with the target programme. They do **not** establish that an imagined individual student also has unrelated additional interests. Use them to identify defensible academic directions, not to invent a fictional personal profile.

For construction, retrieve **every** `programme_interests` row linked to the exact `counselor_programme_id` and assign it one construction role before defining additional alternatives:

- `Direct programme interest` and `Stable study direction` → **generator-eligible**: may generate a candidate direction;
- `Curricular topic` → **support-only**: may strengthen or enrich a direction but may not generate one by itself;
- `Illustrative or temporary topic` and `Outcome or individual trajectory` → **search-only**: retain for discovery but do not use to generate UCR alternatives;
- `target_mapping_status=inherited-across-split-targets` → **excluded-inherited** for construction unless the same substantive direction is independently corroborated for the exact target by current official evidence.

Do not select a convenient subset of generator-eligible rows. Cluster all generator-eligible interests into coherent substantive directions before choosing an additional alternative. Record all assessed rows and the exact generating/supporting rows for every candidate direction so that inclusion and rejection decisions are auditable.

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

**Questions and applications** — evidenced questions, phenomena, problems and applications that the field addresses and that could support a broader programme.

Every substantive map item must be traceable to at least one current official source for the exact target or one valid target-specific programme-interest row.

Adjacent directions and questions/applications may legitimately be empty. Absence of evidence is a reason to stop generating alternatives, not a reason to fill the map from the UCR catalogue.

When programme-interest rows are available, the evidence map must reflect the complete construction assessment described in Section 4.2. Build candidate directions from substantive clusters of generator-eligible interests, using support-only rows only as supplementary evidence. A single isolated interest row may define a candidate only when it is itself a coherent substantive direction. Search-only and excluded-inherited rows must not enter candidate construction. Preserve the exact interest-row provenance and disposition of each candidate direction in `academicRationale.interestSelection`.

### Step 3 — Freeze Alternative 1

Define the closest feasible UCR concept from the core field. Reproduce as closely as feasible the substantive core, progression, methods and advanced work. Preserve genuine UCR limitations rather than compensating with weakly related material.

Freeze this concept before selecting courses.

### Step 4 — Select, trace and validate Alternative 1

Use the enriched UCR course database only after the concept is frozen. Select courses because their actual content implements that concept.

Except for mandatory `ACCPPDE101` Personal & Professional Development, every course must map concretely to one or more evidenced items used by the concept. Generic claims such as “adds breadth,” “adds context,” “provides another perspective,” or “helps understand complex systems” do not count unless that perspective/context is itself evidenced and directly relevant.

Schedule and mechanically validate under Section 2.2.

### Step 5 — Consider Alternative 2

Return to the evidence map before looking for courses. Identify one coherent alternative concept that differs substantively from Alternative 1 and is supported by map items. It may use an adjacent direction, a question/application, or another defensible reorganisation of the evidenced field.

Freeze the concept first, then select courses, run course-to-concept traceability and validate feasibility. Record a concrete distinctness rationale explaining the educational choice that differs from Alternative 1 and how that choice materially changes course selection.

After the schedule is complete, apply the Section 2.3 mechanical floor. Alternative 2 must differ from Alternative 1 by at least **30 EC / 4 courses** in each programme. If it does not, reject Alternative 2 as `not-substantively-distinct`; do not make arbitrary course substitutions to force it over the threshold.

If no concept passes evidence, coherence, distinctness and feasibility, stop at one and record the stopping reason.

### Step 6 — Consider Alternative 3

Only if Alternative 2 is included, repeat Step 5 for one further defensible concept. It must be substantively distinct from the already included alternatives and remain inside the evidence boundary.

After scheduling, Alternative 3 must pass the **30 EC / 4-course floor separately against Alternative 1 and Alternative 2**. Failing either pairwise comparison means Alternative 3 is `not-substantively-distinct` and must not be included.

If it fails any gate, stop at two and record the stopping reason. If it passes, include three and record `maximum-reached` as the stopping state.

### Step 6A — Finalize visible UCR labels

After every included 24-course UCR curriculum has been selected, scheduled and validated, review its visible label against the completed curriculum. Preserve the generating `concept` separately in the academic rationale. The final `label` must describe what the completed programme actually contains and must not let one motivating strand masquerade as the whole programme. Use a single-field label only when the completed curriculum is genuinely dominated by that field; otherwise use an accurate combination or question/application label. Record a concise `labelRationale` for each UCR alternative.

### Step 7 — Schedule terms

For the current counselor corpus use the fixed **Fall 2026 UCR start**:

- Semester 1: `2026h2`
- Semester 2: `2027h1`
- Semester 3: `2027h2`
- Semester 4: `2028h1`
- Semester 5: `2028h2`
- Semester 6: `2029h1`

### Step 8 — Build the comparison

Only after the external curriculum and all included UCR curricula are complete and validated, construct comparison blocks under Section 5.

### Step 9 — Create and validate the production record

Create the canonical counselor record under Section 7, run repository/schema validation and apply the completion gates in Section 9.

## 4.4 Counselor exceptions

Do not guess or substitute another target when a selected in-scope programme cannot be reconstructed confidently.

If no academically defensible closest UCR alternative can satisfy the feasibility rules, report the limitation rather than manufacturing a match. If Alternative 2 or 3 cannot be established, stop with the number of defensible alternatives already completed.

A non-standard target excluded by the current scope is not a blocked case; it is simply outside production scope.

---

# 5. Comparison construction

Construct comparison blocks only from the **completed and validated 180-EC curricula**. The blocks are a lossless classification and alignment of those curricula, not a selective analytical summary.

Apply all of the following rules:

- there is no required number of blocks and no default three-block or 60/60/60 structure;
- every included UCR course must appear in the comparison **exactly once**, including `ACCPPDE101` Personal & Professional Development;
- every external curriculum component in the reconstructed coherent pathway must appear **exactly once**;
- the displayed components for every included programme column must total **180 EC**;
- genuine open-elective, profiling or restricted-choice space in the external programme must appear explicitly as such and retain its actual EC value;
- one comparison cell represents one canonical course/component; do not combine several UCR courses into a prose bundle;

- for the UCR alternatives, exact `courseCode` identity is the **only** basis for sharing a row: build the UCR side of the comparison from the union of included UCR course codes, create one canonical row and block for each code, populate every UCR alternative that contains that exact code, and leave the other UCR cells blank;
- two different UCR course codes must occupy separate rows even when their content is similar; never create a row-level equivalence merely for visual alignment;
- assign the canonical block once for the course code within that comparison; the same course may not appear under different blocks in different UCR alternatives;
- **only after the UCR rows are fixed**, place every comparator component independently against the strongest defensible UCR counterpart, using actual component/course content rather than previous row position;
- a shared comparator/UCR row asserts **substantial curricular correspondence**, not full course equivalence. Place components on the same row when they address materially the same primary academic subject, method or educational function, even when their disciplinary framing, breadth or emphasis differs;
- prefer the strongest defensible counterpart and use actual component/course content rather than title similarity alone. A direct same-subject match remains preferable to a looser thematic association (for example, Developmental Psychology belongs with Lifespan Developmental Psychology rather than with an unrelated social-science course);
- keep components on separate rows when the overlap is only partial, adjacent, incidental or merely methodological rather than substantively the same area. When no substantial curricular counterpart exists, give the comparator component its own row with blank UCR cells. Never preserve or invent a weak match merely to reduce blank space;
- record the decision for every comparator component in `comparisonAlignment`: either `substantive-match` with the selected `ucrCourseCode`, or `unmatched`, together with a concise rationale. If the UCR row structure changes, comparator placement must be recomputed rather than carried over by row index;
- meaningful blank cells are legitimate when there is no sufficiently comparable component in another programme;
- unequal block sizes, unequal numbers of components within a block and structural gaps are legitimate and often desirable;
- methods, mathematics, statistics, econometrics, laboratory work and research training count as substantive disciplinary content where appropriate.

For current production records, comparison cells must refer back to the canonical programme data using stable identifiers rather than relying on free text alone:

- UCR cells use `courseCode` matching the scheduled UCR course;
- comparator cells use `componentId` matching the reconstructed external curriculum component.

Displayed text and credits must agree with the referenced canonical course/component. These stable references are validation keys; renderers may continue to display ordinary course/component names and EC values.

Start from substantive correspondences and differences and let them determine block number, titles, row alignment and size. Do not force one external component to equal one UCR course, move a component into more than one block, omit inconvenient components, or fill gaps for visual symmetry.

A pattern such as three round 60-EC blocks or identical allocations across several programme columns is a review signal when it appears repeatedly or without curricular justification; it is not forbidden when the actual curricula independently justify it.

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
- exactly one comparator identity and one to three ordered UCR alternative identities;
- comparator name, institution/provider, official source and the complete reconstructed 180-EC component list;
- complete 24-course set and six-semester schedule for each included UCR programme;
- comparison blocks that account for every canonical component exactly once while preserving deliberate gaps in horizontal alignment;
- stable comparison references back to UCR course codes and comparator component IDs in current production records;
- explanatory-note type/parameters or rendered note where needed;
- academic validation status and internal source/verification metadata.

Optional internal `alternativeKind` metadata may describe an alternative as `closest-match`, `related-direction`, `question-led` or another approved type. It does not create a quota.

## 7.2 Student additions

Preserve original `interest_statement`, separate academic interpretation, internal delivery identifier where required, relevant cohort/starting-semester context and the rationale/stopping decision used to determine how many UCR alternatives were included. Student records remain private.

## 7.3 Counselor additions

Current counselor production records use `schemaVersion: "2.0"`.

Preserve the permanent `counselor_programme_id`, normalized target metadata/provenance required by the current schema, and `academicRationale` containing:

- evidence-backed `coreField`;
- evidence-backed `adjacentDirections`, which may be empty;
- evidence-backed `questionsApplications`, which may be empty;
- one rationale object for every included UCR alternative, identifying its `programmeId`, concept, evidence-map basis and evidence;
- a distinctness rationale for every included alternative after the first that explains the evidenced organising difference and the material curricular consequences.

Preserve `alternativeSelection` containing the number of included UCR alternatives, a stopping state and a concise assessment. The included count must equal the number of UCR alternatives in `programmes`. For one or two alternatives, the stopping state explains why another was not defensible; for three, use `maximum-reached`.

The canonical comparator object must contain its complete reconstructed `components` list. Each component has a stable `id`, display `name` and `credits`; the list totals 180 EC. Comparison cells then refer to those components by `componentId`.

Every UCR comparison cell must contain the scheduled course's `courseCode`. The cell text and credits must match that canonical course. This prevents a course from being duplicated, omitted or silently renamed in the comparison layer.

For current production records:

`id == programmeProvider.counselorProgrammeId == counselor_programme_id`

Use normalized arrays for languages and modes. Legacy provider/offering identifiers remain provenance only.

The canonical record contains semantic content, not renderer coordinates, CSS or page geometry.

---

# 8. Library and public-export boundaries

The counselor comparison library stores one fixed record per completed in-scope normalized target. Discovery programme metadata and programme-interest indexes remain separate from comparison content. Do not flatten all interests into a comparison record; `academicRationale` stores only evidence actually used for the included UCR alternatives.

During incremental counselor production, create individual files under `data/counselor/comparisons/` but do not create the final production `programmes.json` or `interests.json` discovery indexes until the comparison corpus is complete and quality-controlled. Leave pilot indexes unchanged.

Neither workflow publishes automatically. Public export requires substantive human review and explicit public-use approval. Derive publication-safe records from canonical academic records without reselecting courses, rebuilding alignments or inventing renderer-specific academic facts.

---

# 9. Completion gates

The purpose of final QC is to confirm that the procedure above was followed, not to restate it in a second instruction set.

## 9.1 Record-level counselor gates

A counselor record is complete only when all six gates pass:

1. **Evidence gate** — external programme is fairly reconstructed and every substantive interest-map item used in an alternative is evidence-backed for the exact target.
2. **Alternative gate** — Alternative 1 is the closest defensible response; each additional alternative passed evidence, coherence, qualitative distinctness, the pairwise **30 EC / 4-course minimum**, and feasibility; the sequential stopping decision is recorded and no skipped slot was manufactured later.
3. **Course gate** — every non-PPD course passes course-to-concept traceability; no course relies only on generic breadth/context language; every included alternative after the first has a concrete distinctness rationale; and courses changed to establish distinctness are genuine consequences of the evidenced concept rather than arbitrary threshold-filling substitutions.
4. **Feasibility gate** — all mechanical UCR schedule constraints pass against the enriched database for every included programme.
5. **Comparison gate** — every included column accounts for exactly 180 EC; each canonical UCR course/external component appears exactly once; PPD is visible; stable references agree with canonical data; and block alignment preserves genuine gaps rather than imposing a symmetry template.
6. **Record gate** — the current counselor schema/validator passes and normalized identity/provenance matches the registry.

## 9.2 Batch-level counselor QC

After all individually completed records pass the gates, inspect the batch only for **systematic** failure modes:

- unsupported domains or cross-disciplinary jumps;
- generic/interchangeable alternative concepts across unrelated targets;
- recurring course palettes or course reuse without independent justification;
- systematic production of three alternatives regardless of evidence;
- systematic production of only one alternative to avoid the work of testing additional possibilities;
- recurring block templates or equal allocations that are not independently justified by the curricula;
- systematic weakening of external programmes.

Similarity between genuinely related programmes is not itself a defect. Do not change a sound record merely to create artificial variety. The 30-EC rule is a minimum safeguard against near-duplicates, not a target for maximizing difference.

## 9.3 Student completion

Confirm the student input is preserved verbatim, interpretation stored separately, the number of alternatives follows the sequential evidence/coherence/distinctness/feasibility rule, every pair of included UCR alternatives passes the **30 EC / 4-course distinctness floor**, every included UCR schedule is mechanically valid, every comparison column accounts for the complete 180 EC without duplication or omission, comparison alignment is fair, and privacy/publication boundaries are respected.

Only then release the requested artifact or library record.
