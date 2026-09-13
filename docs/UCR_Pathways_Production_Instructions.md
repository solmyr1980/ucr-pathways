# UCR Pathways — Production Instructions

## Purpose and boundary

These instructions govern academic production for the UCR Pathways project.

They implement the **UCR Pathways Master Specification** and should not redefine product-level branding, website behavior or LinkedIn publication mechanics.

They govern two academic production paths:

1. **student workflow** — personalized generation from an actual prospective student's submitted interests;
2. **counselor workflow** — deterministic generation of one comparison per production-eligible normalized counselor programme target in the approved Dutch bachelor scope.

Use:

- the Master Specification for durable product decisions, copy principles and visual identity;
- the enriched UCR course database for UCR course evidence and feasibility;
- the normalized registry layer in `data/registry/` for counselor target identity, production order, provenance and normalized programme-interest discovery metadata;
- current official university sources for external programme reconstruction;
- the current repository schemas only when creating records for implementation or public use.

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

## 3.1 Unit of production

The unit of counselor production is one **production-eligible normalized counselor programme target** from `data/registry/programmes.csv`.

The stable identity is `counselor_programme_id`. Source worksheet rows, offered-programme UUIDs, programme-unit codes, recognized-programme codes, language, delivery mode and campus registrations are provenance/normalization inputs rather than independent production identities.

Follow `production_order` in the normalized registry. Do not prioritize by:

- UCR fit;
- number of blank comparison cells;
- applicant popularity;
- institution;
- discipline;
- expected marketing value.

Production should be resumable. Skip normalized targets for which a completed current comparison already exists unless a specific factual or quality problem requires regeneration. Permanent `counselor_programme_id` values must be preserved across later registry refreshes.

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

The associated interests support **search/discovery**. They are not an individual student's input and must not personalize the fixed comparison. Source identifiers remain traceability fields and must not replace `counselor_programme_id` as the production identity.

## 3.3 Reconstruct the selected external programme

The comparator is predetermined by the normalized counselor target. Do not select a different comparator because another programme would make a stronger UCR contrast.

Use current official sources for the exact academic programme/route represented by the normalized target and its participating institution(s). When the target is a normalized merge, do not re-split administrative registrations. When it is a normalized split, research the exact named track/route represented by that target.

If the programme cannot be reconstructed with reasonable confidence, flag the record for exception review rather than guessing or silently substituting another provider.

Where formal routes/tracks/specializations exist, choose one coherent representative pathway using current official rules. Record the chosen route and source basis internally.

When choices are genuinely open, preserve that openness rather than inventing a fictitious set of electives.

## 3.4 Construct the three deterministic UCR alternatives

### `ucr-depth` — closest match

Construct the feasible UCR programme that most closely reproduces the substantive core, progression and methods of the selected external programme.

Depth includes foundations, methods, research training and advanced specialization where UCR genuinely provides them.

Do not define closeness merely by counting course labels.

### `ucr-balanced` — field plus related subjects

Retain a substantial core of the external field while deliberately adding closely related UCR subjects that broaden the academic perspective.

The related subjects must be substantively defensible from the comparator's field, programme-interest evidence or neighbouring academic questions. Do not invent unrelated breadth merely to create visual difference.

### `ucr-thematic` — broader programme

Construct the broadest coherent UCR programme connected to the external programme's field, questions, applications and evidenced associated interests.

It should demonstrate how UCR can bring relevant perspectives together without implying that the external bachelor itself contains all of those perspectives.

## 3.5 Counselor operating sequence

For each normalized counselor programme target:

1. identify the next unprocessed production-eligible target in `production_order`;
2. confirm normalized target identity, participating institution(s), provenance and current official source basis;
3. reconstruct a coherent valid external curriculum/pathway;
4. construct the three deterministic UCR alternatives;
5. schedule and mechanically validate all three UCR programmes;
6. compare all four completed curricula;
7. assign the approved descriptive labels;
8. select a reusable explanatory-note type only if needed;
9. create the canonical counselor record with `counselor_programme_id` and registry provenance;
10. add/update the deterministic comparison library;
11. run structural and academic quality control;
12. flag exceptions rather than inventing missing facts.

There is no student-specific personalization step in this workflow.

---

# 4. Dutch bachelor programme-interest enrichment

Maintain Dutch bachelor programme enrichment as two linked tables within the same working workbook or data artefact:

- `Pathways_programmes`: one row per programme-provider record;
- `programme_interests`: one row per programme-provider × candidate interest signal.

Use a reliable programme-provider key during the historical enrichment stage. A CROHO/recognized-programme code alone is not sufficient where the same programme is offered by multiple providers.

For counselor production and discovery, use the normalized derivative in `data/registry/programme_interests.csv`, linked by permanent `counselor_programme_id`. The original workbook rows remain provenance. Where historical interest evidence is inherited across a resolved split target, preserve and respect its `target_mapping_status` rather than treating it as target-specific research.

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

`interest query → ranked normalized counselor programme targets → fixed counselor comparison`

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

## 9.1 Comparison blocks

Derive meaningful substantive blocks from the completed curricula, such as:

- major disciplines;
- methods and research;
- important substantive themes;
- advanced specialization;
- other distinct perspectives.

Do not create a broad theme that merely renames an existing disciplinary block.

## 9.2 Alignments and gaps

Within blocks:

- align substantively comparable components horizontally;
- preserve meaningful blank cells;
- do not fill gaps for visual symmetry;
- preserve genuine structural differences;
- label genuinely open space where necessary for fair interpretation;
- show credit weights consistently.

Do not use numerical depth/breadth scores.

---

# 10. Reusable explanatory-note taxonomy

Do **not** write a bespoke prose note for every counselor comparison.

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
- Expand a selected template into final text before exporting an implementation/public record. Retain its type and evidenced parameters as provenance where useful; do not send a parameter-only note to a renderer that expects text.

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

Preserve:

- permanent `counselor_programme_id`;
- normalized target name, programme type/status and participating institution(s);
- source registry rows and offered-programme UUIDs;
- programme-unit, recognized-programme and variant identifiers where present;
- other provenance/join keys required to connect the record to normalized programme metadata and programme-interest search indexes.

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

The counselor comparison library contains the fixed canonical/implementation record for each completed normalized counselor programme target.

Maintain discovery data separately from comparison content:

- programme metadata/index;
- programme-interest index;
- deterministic comparison records.

Do not flatten all interests into the comparison record merely for search convenience.

Search results always resolve to normalized counselor programme targets and then load the pre-produced comparison.

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

## UCR programmes

- all mechanical feasibility checks pass;
- `ucr-depth` is genuinely the closest feasible match;
- `ucr-balanced` broadens through defensible related subjects/interests;
- `ucr-thematic` is genuinely broader while remaining coherent;
- progression arises from course content rather than quotas.

## Comparison

- same substantive classification principles across all four programmes;
- alignments justified;
- genuine gaps preserved;
- EC shown consistently on external and UCR components;
- explanatory note used only when needed and generated from an approved template.

## Student records

- original input preserved verbatim;
- academic interpretation stored separately;
- privacy/delivery data kept out of public records;
- placeholder/final disclaimer handled correctly.

## Counselor records

- correct permanent `counselor_programme_id` and normalized target provenance;
- no accidental personalization from an interest query;
- discovery interests remain linked rather than becoming programme claims;
- record order/resumability preserved.

## Public export, when requested

- explicit public-use approval;
- privacy-safe content;
- current repository schema conformity;
- final explanatory-note text present wherever a semantic template was selected;
- no substantive reinterpretation during export.

Only then release the requested artifact or library record.
