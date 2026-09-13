# UCR Pathways — Production Instructions

## Purpose and boundary

These instructions govern academic production for the UCR Pathways project.

They implement the **UCR Pathways Master Specification** and should not redefine product-level branding, website behavior or LinkedIn publication mechanics.

They govern two academic production paths:

1. **student workflow** — personalized generation from an actual prospective student's submitted interests;
2. **counselor workflow** — deterministic generation of one comparison per normalized counselor programme target in the current counselor production scope.

Use:

- the Master Specification for durable product decisions, copy principles and visual identity;
- the enriched UCR course database for UCR course evidence and feasibility;
- the normalized registry layer in `data/registry/` for counselor target identity, production order, provenance and normalized programme-interest discovery metadata;
- current official university sources for external programme reconstruction;
- the current repository schemas for executable data contracts.

These instructions produce and validate academic records. They do not publish directly to the public website or LinkedIn.

---

# 1. Shared academic principles

For both workflows:

- construct and validate programme content before designing the visual comparison;
- use course/component content rather than titles alone;
- represent genuine gaps honestly;
- do not manufacture weak UCR matches;
- do not weaken an external programme to make UCR look better;
- preserve actual EC weights;
- show EC credits consistently on both external and UCR components in user-facing comparisons;
- do not force exact row-by-row or credit-by-credit symmetry;
- do not fill gaps merely for visual balance;
- do not introduce research-seminar callouts or exchange opportunities merely to reduce gaps;
- do not create a special elective-space symmetry rule;
- use reusable explanatory-note types only when they prevent a material misunderstanding.

Every comparison uses the four stable semantic roles:

1. `comparator`;
2. `ucr-depth`;
3. `ucr-balanced`;
4. `ucr-thematic`.

Visible labels follow the Master Specification rather than exposing these internal role names.

---

# 2. Student workflow

## 2.1 Inputs

Receive:

- a stable internal student/participant identifier where needed for delivery;
- the actual `interest_statement` submitted through the approved intake route;
- batch/cohort or starting-semester context where applicable.

Preserve the student's original wording exactly.

Do not request or collect names or other unnecessary personal information in the academic record.

Do not assume that the first-mentioned interest is more important.

Do not require the student to understand UCR's curriculum structure.

## 2.2 Interpret the student's interests

Produce a concise academic interpretation that identifies, where relevant:

- disciplines;
- substantive questions;
- phenomena or problems;
- practical interests or skills;
- meaningful connections among them.

For one stated interest, broaden through meaningful subfields, questions and neighbouring perspectives rather than inventing a second interest.

Preserve both:

- the original student wording; and
- the academic interpretation.

These are distinct fields. The interpretation must not replace the original statement.

## 2.3 Select the external comparator

Choose the Dutch bachelor that provides the most useful disciplinary/depth endpoint for the student's interests.

Do not automatically choose the discipline mentioned first.

Prefer a current Dutch research-university bachelor where suitable.

For a manually supervised student run, propose the external programme and authoritative source basis for approval before full generation continues, unless an approved automated production configuration explicitly removes that checkpoint.

## 2.4 Student operating sequence

Work in this order:

1. preserve and interpret the student's interests;
2. identify the most defensible external comparator;
3. establish and, where required, approve its authoritative source basis;
4. reconstruct one coherent valid pathway through that external programme;
5. construct `ucr-depth` as the closest feasible UCR match while responding meaningfully to the student's interests;
6. construct `ucr-balanced` with substantially more balanced weight across the student's interests;
7. construct `ucr-thematic` from questions/themes connecting those interests;
8. schedule and mechanically validate all three UCR programmes;
9. compare all four completed curricula;
10. assign student-facing descriptive labels;
11. create the canonical student record;
12. generate the requested student-app/PDF representations from that record;
13. only after explicit public approval, derive a publication-safe record when requested.

---

# 3. Counselor workflow

## 3.1 Unit and current scope of production

The unit of counselor production is one normalized counselor programme target from `data/registry/programmes.csv` that is inside the **current counselor production scope**.

A target is currently in scope only when all three conditions hold:

- `production_eligible=true`;
- `production_order` is nonblank; and
- `programme_type=standard`.

Targets with `programme_type=joint-degree`, `double-bachelor` or `dual-degree-route` are temporarily outside counselor production until an approved comparison/presentation method exists for those structures. They remain in the normalized registry with their permanent identity, provenance, institutions and lifecycle status. Do not change `production_eligible`, current status, `production_order`, normalization decisions or permanent IDs merely to implement this temporary presentation-scope exclusion.

The stable identity is `counselor_programme_id`. Source worksheet rows, offered-programme UUIDs, programme-unit codes, recognized-programme codes, language, delivery mode and campus registrations are provenance/normalization inputs rather than independent production identities.

Follow `production_order` among targets that satisfy the current production-scope filter. Do not prioritize by UCR fit, number of blank comparison cells, applicant popularity, institution, discipline or expected marketing value.

Production is resumable. Skip an in-scope target only when a completed current production comparison already exists and requires no repair. Permanent `counselor_programme_id` values must be preserved across later registry refreshes.

## 3.2 Counselor inputs

For each normalized counselor target receive/preserve, as available:

- permanent `counselor_programme_id`;
- `registry_order` and `production_order`;
- canonical target name and programme type/status;
- normalized participating institution identity/identities;
- source worksheet rows and offered-programme UUIDs;
- programme-unit, recognized-programme and variant identifiers;
- aliases, locations, languages and modes;
- Step 2 identity-resolution provenance where applicable;
- associated normalized programme-interest rows linked by `counselor_programme_id`.

The associated interests support discovery and academic evidence. They are not an individual student's input and must not personalize the fixed comparison. A search term never changes the fixed comparison.

## 3.3 Reconstruct the selected external programme

The comparator is predetermined by the normalized counselor target. Do not select a different comparator because another programme would make a stronger UCR contrast.

Use current official sources for the exact academic programme/route represented by the normalized target and its participating institution(s). When the target is a normalized merge, do not re-split administrative registrations. When it is a normalized split, research the exact named track/route represented by that target.

If the programme cannot be reconstructed with reasonable confidence, flag the record for exception review rather than guessing or silently substituting another provider.

Where formal routes/tracks/specializations exist, choose one coherent representative pathway using current official rules. Record the chosen route and source basis internally.

When choices are genuinely open, preserve that openness rather than inventing a fictitious set of electives.

## 3.4 Build the academic interest map before constructing UCR programmes

The counselor workflow normally starts from a named external bachelor rather than from a student's personal combination of interests. Therefore `ucr-balanced` and `ucr-thematic` must not be generated by inventing extra interests or by browsing the UCR catalogue for attractive breadth.

After reconstructing the external programme and before selecting UCR courses, build an **evidence-backed academic interest map** for the exact normalized target.

The map has three layers.

### A. Core field

Record the academic content that defines the external programme, including as applicable:

- central disciplines and subfields;
- foundations and progression;
- mathematics, statistics, methods and research training;
- advanced/specialist work;
- thesis/capstone expectations.

This layer is based primarily on the reconstructed curriculum and current official programme evidence.

### B. Adjacent directions

Record genuinely related academic directions that can support a broader programme. Suitable evidence includes:

- formal tracks, routes or specialisations;
- stable study directions;
- strong direct programme interests;
- recurring curricular connections to neighbouring disciplines;
- neighbouring academic directions explicitly supported by the programme's own questions or applications.

Do not add a direction merely because UCR happens to offer appealing courses in it.

### C. Questions and applications

Record substantive questions, phenomena, problems and applications that the field addresses and that can support a thematic programme.

Use current official programme evidence and valid target-specific programme-interest evidence. `Curricular topic` signals may broaden this layer. `Illustrative or temporary topic` and `Outcome or individual trajectory` signals may support an application cautiously, but they must not by themselves define the programme's core or a major thematic direction.

Where `target_mapping_status=inherited-across-split-targets`, the inherited interest record is provenance/general discovery context only. It is not target-specific academic evidence unless independently corroborated by current official evidence for the exact target.

### Evidence rule

Every substantive item in the map must be traceable to at least one of:

- a current official source for the exact target; or
- a valid target-specific row in `data/registry/programme_interests.csv`.

Do not use the UCR course catalogue as evidence for what the external field is interested in. The UCR database enters only after the interest map and programme concepts have been established.

## 3.5 Freeze the three UCR programme concepts before course selection

Before selecting individual UCR courses, explicitly establish the logic of all three alternatives.

### `ucr-depth` — closest match

Use the **core field** layer as the principal target. Construct the feasible UCR programme that most closely reproduces the substantive core, progression and methods of the external programme.

Depth includes foundations, methods, research training and advanced specialization where UCR genuinely provides them. Do not define closeness merely by counting similar course titles.

Where UCR lacks important specialist areas, preserve that limitation. Do not compensate with weakly related courses merely to create apparent equivalence.

### `ucr-balanced` — field plus related subjects

Retain a substantial core of the external field and deliberately select **one or two adjacent directions** from the academic interest map.

Those selected directions become the explicit basis for broadening the curriculum. The result must be meaningfully broader than `ucr-depth`, not simply the same programme with arbitrary substitutions.

Do not introduce a direction that is absent from the evidence-backed map merely to make the programme look more interdisciplinary.

### `ucr-thematic` — broader programme around an evidenced question

Before selecting courses, state **one explicit organising question, problem, phenomenon or application**.

The organising theme must be traceable to the academic interest map. It may connect several evidenced directions, but it must not be invented from UCR course availability.

The thematic question is **scope-closed by its evidence**. It may synthesize, combine or rephrase evidenced map items, but it must not introduce a new substantive domain, population, problem or application that is absent from those items. Evidence about economic decision-making, for example, does not by itself justify widening the theme to historical, social, environmental or ethical systems; each such direction needs its own support in the map.

“Address the question from several relevant perspectives” means several perspectives that are substantively justified by the evidence-backed map. It is not permission to import unrelated disciplines merely to create breadth.

Then construct the broadest coherent UCR programme that addresses that organising question from those evidenced perspectives.

A course belongs in the thematic programme because its actual content helps answer the organising question, not simply because it is broad, interesting or available.

Do not choose a course first and then widen the thematic question or invent a bridge argument to justify it. If a candidate course requires a new interest or perspective that was not established before course selection, exclude it unless the concept is formally revisited from the external evidence and academic interest map.

If the evidence does not support a compelling expansion far beyond the field, keep the thematic programme relatively close to the field. Do not manufacture eclecticism merely to make the third option look dramatically different.

## 3.6 Counselor operating sequence

For each counselor programme target:

1. identify the next unprocessed target in `production_order` that satisfies the current production-scope filter;
2. confirm normalized target identity, participating institution(s), provenance and current official source basis;
3. reconstruct a coherent valid external curriculum/pathway;
4. retrieve and assess the exact target's programme-interest evidence;
5. build the evidence-backed academic interest map: core field, adjacent directions, questions/applications;
6. freeze the three programme concepts: depth target, one or two balanced directions, and one thematic organising question;
7. test the thematic question against its cited map basis and remove any domain or perspective not actually supported by that basis;
8. only then use the enriched UCR course database to construct the three UCR programmes;
9. complete the internal course-to-concept traceability check in Section 7.1;
10. schedule and mechanically validate all three UCR programmes;
11. compare all four completed curricula;
12. assign the approved descriptive labels;
13. select a reusable explanatory-note type only if needed;
14. create the canonical counselor record, including the academic rationale;
15. add/update the deterministic comparison library;
16. run structural and academic quality control;
17. flag exceptions rather than inventing missing facts.

If a non-standard target (`joint-degree`, `double-bachelor` or `dual-degree-route`) is encountered as though it were selectable, do not produce it. Treat that as a scope-selection error and correct the selection logic rather than forcing the programme into the standard comparison model.

There is no student-specific personalization step in this workflow.

---

# 4. Dutch bachelor programme-interest enrichment

Maintain Dutch bachelor programme enrichment as two linked tables within the same working workbook or data artefact:

- `Pathways_programmes`: one row per programme-provider record;
- `programme_interests`: one row per programme-provider × candidate interest signal.

Use a reliable programme-provider key during the historical enrichment stage. A CROHO/recognized-programme code alone is not sufficient where the same programme is offered by multiple providers.

For counselor production and discovery, use the normalized derivative in `data/registry/programme_interests.csv`, linked by permanent `counselor_programme_id`. The original workbook rows remain provenance.

Where `target_mapping_status=inherited-across-split-targets`, the historical interest evidence came from a source row that was later split into distinct normalized targets. Such a row may be retained as provenance and general discovery context, but it is not target-specific academic evidence for either split target unless independently corroborated by current official evidence for that exact normalized target.

## 4.1 High-recall research objective

For each programme preserve a high-recall set of distinct, evidence-backed candidate interest signals associated with the programme.

A signal may concern:

- a discipline or field;
- a substantive question;
- a phenomenon or real-world problem;
- a practical, analytical or research skill;
- a meaningful combination of fields;
- a stable route, track, specialization or thematic direction;
- an illustrative/changing curricular topic;
- a career, alumni or further-study direction demonstrating plausible application/outcome.

Prefer current official programme-facing sources.

Do not create signals from isolated course titles when richer programme-facing evidence exists.

Exclude generic preferences about teaching method, group work, campus life, location, class size, workload or similar non-academic features.

## 4.2 Relationship classification

Assign exactly one `interest_relationship` category:

1. **Direct programme interest**;
2. **Stable study direction**;
3. **Curricular topic**;
4. **Illustrative or temporary topic**;
5. **Outcome or individual trajectory**.

Classify the relationship between the signal and the bachelor, not merely the webpage type.

For conservative counselor search ranking, categories 1–2 are the default core. Category 3 may broaden discovery. Categories 4–5 remain searchable but receive lower confidence/priority.

Retain `strength` for compatibility/provenance where present, but use `interest_relationship` as the principal downstream distinction.

## 4.3 Search use

The programme-interest data provides a discovery index:

`interest query → ranked in-scope normalized counselor programme targets → fixed counselor comparison`

Do not use the interest query to regenerate the comparison.

---

# 5. Synthetic interest portfolios

Synthetic interests may still be used for testing, demonstrations or curated public-example development.

Generate candidates independently of the UCR catalogue, then use the enriched UCR course database as a feasibility filter rather than as the generator of the wording.

Prefer realistic prospective-student language and vary statement form and specificity.

Avoid catalogue leakage and repetitive combinations.

Synthetic interests are not a substitute for actual student input in the production student app.

---

# 6. External programme evidence and reconstruction

Use current official university sources.

Prefer:

1. formal curriculum or graduation requirements;
2. official student-facing curriculum pages;
3. official route, track or specialization pages;
4. official course-catalogue entries;
5. general prospective-student programme pages.

For each comparator distinguish:

- compulsory components;
- restricted choices;
- routes/tracks/specializations;
- genuinely free elective/profiling space;
- methods and research training;
- thesis/capstone requirements;
- relevant EC weights.

Never:

- present optional components as compulsory;
- combine mutually exclusive choices;
- violate programme rules;
- choose weak options to make UCR look better;
- invent courses to fill open space;
- make the programme artificially narrow.

Preserve internally, where relevant:

- programme name;
- institution/provider;
- `counselor_programme_id` and source registry/offering provenance identifiers;
- primary official source URL;
- additional official source URLs;
- academic/curriculum year;
- date checked;
- route/track/specialization selected;
- source notes;
- validation/exception notes.

---

# 7. UCR course evidence

Use the enriched UCR course database as the authoritative source for UCR course selection and feasibility.

Use, as relevant:

- `name`;
- `profile`;
- `discipline`;
- `topics`;
- `methods`;
- `description2`;
- prerequisites;
- planned semester availability;
- EC/credit information where present.

Give outline-derived `profile` information particular weight where available.

Use course content rather than administrative cluster or unit labels.

Do not infer fit from a title alone when richer course evidence points elsewhere.

For the counselor workflow, use the UCR database to **implement** the already established depth/balanced/thematic concepts. Do not let convenient course availability retroactively generate or redefine those concepts without evidence.

## 7.1 Internal course-to-concept traceability check for counselor production

Before finalizing a counselor UCR programme, test every selected course against the concept fixed before course selection. Keep an internal traceability checklist or table during production and QC. The current schema does **not** require this checklist to be stored in the production record.

Except for mandatory `ACCPPDE101` Personal & Professional Development:

- every `ucr-depth` course must be justified by one or more `coreField` items;
- every `ucr-balanced` course must be justified by the core field or one of the selected `balancedDirections`;
- every `ucr-thematic` course must be justified by the stated thematic question and at least one evidenced map item that genuinely forms part of that question.

For each course, be able to state in one concrete sentence what part of the programme concept it serves, using the actual course profile/content as evidence. Generic statements such as “this adds breadth,” “this provides another perspective,” “this adds context,” or “this helps understand complex systems” are insufficient unless that perspective or context is itself established in the academic interest map and directly relevant to the fixed question.

If a course cannot pass this test, remove it. Do not repair the problem by retroactively widening the academic interest map or thematic question to fit an attractive UCR course.

Revisit a fixed concept only when it proves genuinely infeasible at UCR, and then return first to the external evidence and academic interest map.

---

# 8. UCR feasibility validation

Each UCR programme must contain:

- exactly **24 unique courses**;
- exactly **4 courses in each of six semesters**;
- at least **6 courses at 300 level**;
- **Personal & Professional Development** during Year 1.

Also require:

- every prerequisite completed in an earlier semester;
- every selected course actually available in its assigned semester;
- no duplicated courses.

Do not invent requirements concerning clusters, units, concentrations, breadth or disciplinary distributions.

Use data-analysis/code against the enriched UCR course database to validate mechanically:

- 24-course total;
- uniqueness;
- six-semester structure;
- four courses per semester;
- 300-level minimum;
- PPD placement;
- prerequisite order;
- actual semester availability.

If validation fails, repair and validate again. Do not export a knowingly invalid UCR programme.

Repository/schema validation is not a substitute for academic feasibility validation.

---

# 9. Compare the completed curricula

Construct and validate all four programmes before building the comparison.

Treat methods, statistics, mathematics, econometrics, laboratory work and research training as part of disciplinary depth where they genuinely serve that role.

Do not assume one comparator component equals one UCR course.

Preserve actual EC weights and show credits consistently on both sides in rendered comparison components.

## 9.1 Comparison blocks are analytical alignments, not curriculum partitions

Derive meaningful substantive blocks from the completed curricula, such as:

- major disciplines;
- methods and research;
- important substantive themes;
- advanced specialization;
- other distinct perspectives.

A comparison block exists to align substantively comparable material. It is **not** a bucket into which all 180 EC of every programme must be allocated.

Therefore:

- there is no required number of comparison blocks;
- there is no default three-block structure;
- blocks are not automatically 60 EC each;
- a UCR programme's 24 courses do not all have to appear in the comparison blocks;
- total credits shown within blocks do not have to sum to 180 EC for each programme;
- unequal credit totals across aligned cells are legitimate when they reflect the actual curricula.

Do not create a broad theme that merely renames an existing disciplinary block.

Do not decide first how many blocks are aesthetically convenient and then aggregate curricula to fit them. Start from substantive correspondences and differences in the completed curricula and let those determine the number and size of blocks.

A pattern in which the comparator has three round 60-EC blocks, or every UCR column contributes the same number of courses or the same credits to every block, is **presumptively a template artefact** rather than evidence of genuine alignment. If such a pattern appears, stop and verify each block independently. Retain it only when the actual external curriculum structure and actual UCR correspondences independently justify those equalities.

Do not aggregate an external 180-EC curriculum into three 60-EC buckets merely because 180 divides evenly by three. Do not use four UCR courses/30 EC per block, or any other fixed allocation, as a default comparison recipe.

## 9.2 Alignments and gaps

Within blocks:

- align substantively comparable components horizontally;
- preserve meaningful blank cells;
- do not fill gaps for visual symmetry;
- preserve genuine structural differences;
- label genuinely open space where necessary for fair interpretation;
- show credit weights consistently;
- leave specialist components unmatched when UCR has no genuine counterpart;
- do not force a UCR course into a block merely because every course exists somewhere in the 24-course programme.

A blank cell or unequal alignment is often the correct representation of a real curricular difference.

Do not use numerical depth/breadth scores.

---

# 10. Reusable explanatory-note taxonomy

Do not write a bespoke prose note for every counselor comparison.

Use a small semantic taxonomy. A note is optional and should appear only when a material difference could otherwise be misunderstood.

Store the note type and parameters where practical; render the final sentence/paragraph from the template.

## 10.1 `less-disciplinary-depth`

Use when UCR covers the field but the external programme provides a materially deeper specialist sequence.

Template:

> The [external programme] includes a more extensive sequence in [specialist areas]. At UCR, students can study [relevant UCR areas], but UCR does not offer the same depth or sequence in [field].

## 10.2 `related-fields-not-full-discipline`

Use when UCR approaches the central subject/problem through related disciplines rather than offering the full disciplinary curriculum.

Template:

> The [external programme] combines [key components]. At UCR, students can approach [central subject/problem] through fields such as [relevant UCR fields]. These programmes therefore offer related perspectives rather than reproducing a full [discipline] curriculum.

## 10.3 `missing-specialist-components`

Use when UCR provides a substantial core match but lacks particular specialist components.

Template:

> Both programmes include substantial study of [shared field]. The [external programme] additionally includes specialist work in [missing areas]. UCR students can instead combine [UCR strengths], but those specialist components are not offered at the same level of depth.

## 10.4 `different-curricular-structure`

Use when similar substantive territory is organized differently.

Template:

> The [external programme] organizes study around a structured sequence in [discipline/route]. At UCR, comparable subjects are distributed across courses in [fields]. The UCR programme therefore covers related territory through a different curricular structure rather than reproducing the external programme course by course.

## 10.5 Note-generation rules

- Populate only evidenced parameters.
- Do not exaggerate equivalence.
- Do not hide genuine absence behind generic wording.
- Do not mention research seminars, exchange opportunities or elective-space symmetry merely because those were once suggested as comparison devices.
- Omit the note entirely when the comparison is already self-explanatory.
- Expand a selected template into final text before exporting an implementation/public record. Retain its type and evidenced parameters as provenance where useful.

---

# 11. Canonical records

Create one canonical structured record before rendering any output.

## 11.1 Shared core

Preserve at minimum:

- stable record ID;
- `origin` (`student` or `counselor`);
- four programme identities and semantic roles;
- comparator name, institution/provider and approved official URL;
- comparator components and relevant EC values;
- complete 24-course set for each UCR programme;
- six-semester schedule for each UCR programme;
- UCR course credits where available/required;
- comparison blocks;
- alignments and deliberate gaps;
- explanatory-note type/parameters or rendered note where needed;
- academic validation status;
- internal source/verification metadata.

## 11.2 Student-origin additions

Preserve:

- original `interest_statement`;
- academic interpretation;
- internal delivery identifier where required;
- relevant cohort/starting-semester context.

Canonical student records remain private.

## 11.3 Counselor-origin additions

Current counselor production records use `schemaVersion: "1.2"`.

Preserve:

- permanent `counselor_programme_id`;
- normalized target name, programme type/status and participating institution(s);
- registry order and production order;
- normalized languages and modes;
- source registry rows and offered-programme UUIDs;
- programme-unit, recognized-programme and variant identifiers where present;
- other provenance/join keys required to connect the record to normalized programme metadata and programme-interest search indexes;
- `academicRationale`, containing:
  - evidence-backed `coreField` items;
  - evidence-backed `adjacentDirections`;
  - evidence-backed `questionsApplications`;
  - the one or two selected `balancedDirections`;
  - the explicit `thematicQuestion`, its evidence and the map items on which it is based.

The internal course-to-concept traceability checklist in Section 7.1 is a production/QC aid under the current contract; it does not add a required schema field.

For current production records, the top-level stable record `id` and `programmeProvider.counselorProgrammeId` must both equal the same permanent `counselor_programme_id` (`cp-000001` format).

Use normalized arrays for languages and modes in new counselor production records. Do not reduce a multilingual or multi-mode normalized target to a single scalar value.

Counselor records are deterministic library content but are not automatically public website/LinkedIn examples.

The canonical record contains semantic content, not renderer coordinates, CSS or page geometry.

---

# 12. Student-app and optional PDF output

Render the student interface from the canonical student record.

The welcome view must preserve the distinction between:

- **You told us that…** — original wording;
- **For us, this means that…** — academic interpretation.

Provide the personalized programme view and comparison view from the same record.

Use the placeholder disclaimer until approved final wording is supplied:

> **[PLACEHOLDER — insert approved student-program disclaimer from the printed butterfly.]**

Existing Open Day/two-page PDF output may continue as an optional renderer where useful. It must draw from the same canonical record rather than maintain independent academic content.

---

# 13. Counselor library and discovery indexes

The counselor comparison library contains the fixed canonical/implementation record for each completed normalized counselor programme target in the current production scope.

Maintain discovery data separately from comparison content:

- programme metadata/index;
- programme-interest index;
- deterministic comparison records.

Do not flatten all interests into the comparison record merely for search convenience. The `academicRationale` stores only the evidence actually used to justify the three UCR programme concepts.

Search results always resolve to in-scope normalized counselor programme targets and then load the pre-produced comparison.

Targets outside the current counselor production scope remain available in the normalized registry for provenance and future reconsideration but are not included in the production counselor discovery indexes while no approved comparison exists for them.

---

# 14. Public export

Neither workflow publishes automatically.

Prepare a public publication record only after substantive human review and explicit approval for public use.

The normal public source is a selected counselor record. A student-origin record may be exported only when privacy-safe and explicitly approved.

Derive the public record from the canonical comparison. Do not:

- reselect courses;
- rebuild alignments independently;
- expose private student/delivery identity;
- invent renderer-specific academic content.

The public website and LinkedIn render downstream from the same approved public record when they present the same case.

---

# 15. Final validation

Before marking a record complete, confirm the relevant checks.

## External programme

- correct normalized counselor target identity and participating institution(s);
- current authoritative official source basis;
- compulsory/restricted/open components distinguished correctly;
- selected route/path valid;
- EC weights represented fairly;
- no invented components;
- provenance/source metadata recorded.

## Counselor academic rationale

- the academic interest map was created before UCR course selection;
- every substantive map item is evidence-backed;
- inherited-across-split interest evidence has not been treated as target-specific without independent official corroboration;
- `balancedDirections` select one or two actual adjacent directions from the map;
- `thematicQuestion` is explicit and traceable to the map and evidence;
- the thematic question introduces no substantive domain, population, problem or application absent from its cited map basis;
- “several relevant perspectives” has not been used as permission to import unevidenced disciplines;
- the thematic concept was not generated from convenient UCR course availability;
- if evidence for broad thematic expansion is weak, the thematic programme remains appropriately close to the field rather than becoming generic.

## UCR programmes

- all mechanical feasibility checks pass;
- `ucr-depth` is genuinely the closest feasible match to the core field;
- `ucr-balanced` retains a substantial core and actually reflects its selected adjacent direction(s);
- `ucr-thematic` coherently addresses its stated organising question;
- except for mandatory PPD, every selected course passes the internal course-to-concept traceability check;
- no course is justified only by a generic claim that it adds breadth, context or another perspective;
- individual courses are justified by programme logic, not by a quota for breadth or difference;
- progression arises from course content rather than arbitrary level placement.

## Comparison

- same substantive classification principles across all four programmes;
- comparison blocks are analytical alignments rather than 180-EC partitions;
- there is no forced three-block/60-EC structure;
- external components have not been aggregated into round credit buckets merely to create a neat block layout;
- UCR courses have not been distributed by a fixed equal-per-block recipe such as four courses/30 EC per block;
- any suspiciously uniform block pattern has been independently justified from the actual curricula rather than accepted because it is visually convenient;
- alignments are justified;
- genuine gaps are preserved;
- courses/components are not inserted merely to fill visual space;
- EC is shown consistently on external and UCR components;
- explanatory note is used only when needed and generated from an approved template.

## Student records

- original input preserved verbatim;
- academic interpretation stored separately;
- privacy/delivery data kept out of public records;
- placeholder/final disclaimer handled correctly.

## Counselor records

- current counselor schema/structural validity;
- target satisfies the current counselor production-scope filter;
- correct permanent `counselor_programme_id` and normalized target provenance;
- production metadata matches `data/registry/programmes.csv`, including canonical name, orders, institution IDs, programme type/status, eligibility, languages, modes and provenance arrays required by the schema;
- top-level `id` equals `programmeProvider.counselorProgrammeId` and both equal the permanent `counselor_programme_id`;
- no accidental personalization from an interest query;
- discovery interests remain linked rather than becoming unsupported programme claims;
- record order/resumability preserved.

## Batch-level counselor QC

For each counselor batch, inspect the records as a set, not only one by one. Check for:

- unsupported domains introduced in thematic questions;
- thematic courses that fail course-to-concept traceability;
- recurring thematic course palettes across unrelated disciplines without independent justification;
- fixed comparison-allocation patterns such as three external 60-EC buckets or equal UCR course/credit totals in every block;
- generic thematic questions that could be swapped between unrelated targets;
- copied logic between Dutch/international variants where the overlap has not been independently justified by the actual programme evidence.

Similarity between genuinely related or language-variant programmes is not itself a defect. The problem is unsupported reuse or template-driven construction.

## Public export, when requested

- explicit public-use approval;
- privacy-safe content;
- current repository schema conformity;
- final explanatory-note text present wherever a semantic template was selected;
- no substantive reinterpretation during export.

Only then release the requested artifact or library record.
