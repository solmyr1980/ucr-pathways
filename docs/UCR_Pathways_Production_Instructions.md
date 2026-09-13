# UCR Pathways — Production Instructions

## Purpose and boundary

These instructions govern academic production for UCR Pathways. They implement the **UCR Pathways Master Specification** and govern two academic production paths:

1. **student workflow** — personalized generation from an actual prospective student's submitted interests;
2. **counselor workflow** — deterministic generation of one comparison per normalized counselor programme target in the current counselor production scope.

Use the Master Specification for durable product decisions and branding; the enriched UCR course database for UCR course evidence and feasibility; `data/registry/` for counselor identity, production order, provenance and normalized programme-interest evidence; current official university sources for external programmes; and repository schemas for executable contracts.

These instructions produce and validate academic records. They do not publish directly to the public website or LinkedIn.

---

# 1. Shared academic principles

For both workflows:

- construct and validate programme content before designing the visual comparison;
- use course/component content rather than titles alone;
- represent genuine gaps honestly;
- do not manufacture weak UCR matches or weaken an external programme to make UCR look better;
- preserve actual EC weights and show EC consistently on comparable displayed components;
- do not force row-by-row, course-count or credit symmetry;
- do not fill gaps for visual balance;
- do not introduce research-seminar, exchange or elective-space devices merely to reduce gaps;
- use reusable explanatory-note types only when they prevent a material misunderstanding.

Every comparison uses the four stable semantic roles `comparator`, `ucr-depth`, `ucr-balanced`, `ucr-thematic`. Visible labels follow the Master Specification rather than exposing these internal names.

---

# 2. Student workflow

## 2.1 Inputs and interpretation

Preserve the student's actual `interest_statement` exactly, together with a separate concise academic interpretation. Do not collect unnecessary personal information, assume first-mentioned interests are more important, or require the student to understand UCR curriculum structure.

Interpret, where relevant, disciplines, substantive questions, phenomena/problems, practical interests/skills and meaningful connections. For one stated interest, broaden through genuine subfields, questions and neighbouring perspectives rather than inventing a second interest.

## 2.2 Comparator and operating sequence

Choose the Dutch bachelor that provides the most useful disciplinary/depth endpoint for the student's interests; do not automatically choose the first-mentioned discipline. Prefer a current Dutch research-university bachelor where suitable.

For a manually supervised student run, propose the comparator and authoritative source basis for approval before full generation unless an approved automated configuration removes that checkpoint.

Work in this order:

1. preserve and interpret the student's interests;
2. identify the most defensible external comparator and authoritative source basis;
3. reconstruct one coherent valid pathway through that external programme;
4. construct `ucr-depth` as the closest feasible UCR match while responding to the student's interests;
5. construct `ucr-balanced` with substantially more balanced weight across the student's interests;
6. construct `ucr-thematic` from questions/themes connecting those interests;
7. schedule and mechanically validate all three UCR programmes;
8. compare the four completed curricula;
9. create the canonical student record and requested app/PDF representations;
10. derive a publication-safe record only after explicit public approval.

---

# 3. Counselor workflow

## 3.1 Unit and current scope

The production unit is one normalized target from `data/registry/programmes.csv`. A target is currently in scope only when:

- `production_eligible=true`;
- `production_order` is nonblank; and
- `programme_type=standard`.

Targets classified as `joint-degree`, `double-bachelor` or `dual-degree-route` remain valid normalized targets but are temporarily outside counselor production until an approved presentation method exists. Do not alter their identity, lifecycle fields or normalization merely to implement this exclusion.

The stable identity is `counselor_programme_id`. Source worksheet rows, offered-programme UUIDs, programme-unit codes, recognized-programme codes, language, mode and campus registrations are provenance/normalization inputs rather than independent production identities.

Follow `production_order`. Production is resumable; skip an in-scope target only when a completed current production comparison exists and requires no repair.

## 3.2 Inputs

Preserve, as available, permanent ID; registry and production order; canonical name and programme type/status; participating institution IDs; source worksheet rows and offered-programme UUIDs; programme-unit/recognized/variant codes; aliases, locations, languages and modes; identity-resolution provenance; and associated normalized programme-interest rows.

Programme-interest evidence supports discovery and academic reasoning. It is not an individual student's input and never personalizes the fixed comparison.

## 3.3 Reconstruct the external programme

The comparator is predetermined by the normalized target. Use current official sources for the exact programme/route. When a target is a normalized merge, do not re-split administrative registrations. When it is a normalized split, research the exact named route represented by that target.

Prefer formal curriculum/graduation requirements, official curriculum pages, official track/specialization pages, official course catalogues, then general prospective-student pages. Distinguish compulsory components, restricted choices, tracks/routes, genuinely open space, methods/research training, thesis/capstone and EC weights.

Choose one coherent valid pathway when choices must be instantiated. Preserve genuine openness. If the programme cannot be reconstructed confidently, flag an exception rather than guessing or substituting another provider.

## 3.4 Build the academic interest map before UCR course selection

The counselor workflow begins with a named bachelor rather than a student's personal combination of interests. Therefore `ucr-balanced` and `ucr-thematic` must not be generated by inventing extra interests or by browsing the UCR catalogue for attractive breadth.

Build an evidence-backed map with three layers:

### A. Core field

Defining disciplines/subfields, foundations and progression, mathematics/statistics/methods/research training, advanced specialist work, and thesis/capstone expectations where relevant.

### B. Adjacent directions

Genuinely related directions supported by formal tracks/routes, stable study directions, strong direct programme interests, recurring curricular connections, or neighbouring directions explicitly supported by the programme's own questions/applications.

### C. Questions and applications

Substantive questions, phenomena, problems and applications the field addresses and that may support a thematic programme.

Every substantive map item must trace to a current official source for the exact target or a valid target-specific row in `data/registry/programme_interests.csv`. `Curricular topic` evidence may broaden the picture. `Illustrative or temporary topic` and `Outcome or individual trajectory` may inform applications cautiously but must not by themselves define the core or a major thematic direction. `inherited-across-split-targets` evidence is not target-specific unless independently corroborated.

Do not use the UCR catalogue as evidence for what the external field is interested in.

## 3.5 Freeze the three UCR programme concepts

Before selecting individual UCR courses, establish all three concepts.

### `ucr-depth`

Use the core field as the principal target. Reproduce the substantive core, progression, methods and advanced work as closely as UCR genuinely permits. Preserve important specialist gaps rather than compensating with weakly related courses.

### `ucr-balanced`

Retain a substantial core and deliberately select one or two evidenced adjacent directions. Store those exact labels in `academicRationale.balancedDirections`. Do not introduce a direction absent from the map merely to create variety.

### `ucr-thematic`

State one explicit organising question, problem, phenomenon or application before course selection. Store it in `academicRationale.thematicQuestion` with the exact map labels and evidence on which it rests.

The thematic question is **scope-closed by its evidence**: it must not introduce a substantive domain, population, problem or application that is absent from its cited `basisLabels`. “Several relevant perspectives” means several academic perspectives on that same evidence-backed question; it is not permission to invent an additional interest or domain.

If evidence does not support a compelling expansion far beyond the field, keep the thematic programme relatively close to the field. Do not manufacture eclecticism merely to make option 3 look dramatically different.

## 3.6 Course-level traceability is mandatory

After selecting candidate UCR courses and before treating a schedule as complete, justify every selected course against the fixed programme concept.

Store this in `academicRationale.courseAlignment` for each UCR role. There must be exactly one alignment entry for every scheduled course and no entry for a course that is not scheduled.

Permitted academic bases are deliberately narrow:

- `ucr-depth`: only labels from `coreField`;
- `ucr-balanced`: labels from `coreField` plus the selected `balancedDirections`;
- `ucr-thematic`: only labels listed in `thematicQuestion.basisLabels`.

For every course except `ACCPPDE101`, record `basisType: "academic-map"`, at least one permitted `basisLabel`, and a concise substantive reason explaining how the course serves that label. `ACCPPDE101` is the only `basisType: "ucr-required"` exception and uses no academic basis label.

A post-hoc statement that a course “adds another perspective”, “creates breadth” or is generally interesting is not sufficient. If a course cannot be justified under the permitted labels, remove it or revise the concept/map only when new external evidence genuinely warrants that revision.

## 3.7 Counselor operating sequence

For each target:

1. confirm normalized identity, provenance and official source basis;
2. reconstruct one coherent external curriculum/pathway;
3. retrieve and assess exact target-specific programme-interest evidence;
4. build the academic interest map;
5. freeze depth, balanced directions and thematic question;
6. only then select UCR courses from the enriched database;
7. create and validate course-level traceability for all three UCR programmes;
8. schedule and mechanically validate all three UCR programmes;
9. compare all four completed curricula;
10. create the canonical counselor record;
11. run structural and academic QC;
12. flag exceptions rather than inventing missing facts.

---

# 4. Dutch bachelor programme-interest enrichment

Maintain the programme registry and high-recall interest enrichment as linked data. The historical workbook uses `Pathways_programmes` and `programme_interests`; counselor production uses the normalized derivative in `data/registry/programme_interests.csv` linked by permanent `counselor_programme_id`.

Research current official programme-specific material to substantive saturation. Candidate signals may concern fields, questions, problems, substantive skills, combinations, stable routes/directions, illustrative topics, or later applications/outcomes. Exclude generic teaching/campus/workload preferences.

Classify each signal as exactly one of:

1. **Direct programme interest**;
2. **Stable study direction**;
3. **Curricular topic**;
4. **Illustrative or temporary topic**;
5. **Outcome or individual trajectory**.

Categories 1–2 form the conservative discovery core; category 3 may broaden discovery; categories 4–5 remain lower-confidence context. `interest_relationship`, not `strength`, is the principal downstream distinction.

Interest search is a discovery index only:

`interest query → ranked in-scope normalized targets → fixed counselor comparison`

---

# 5. Synthetic interests

Synthetic interests may be used for testing, demonstrations or curated public-example development. Generate candidates independently of the UCR catalogue, then use the enriched UCR database as a feasibility filter. Synthetic interests are not a substitute for actual student input in the production student app.

---

# 6. External programme evidence and reconstruction

Use current official university sources. Never present optional components as compulsory, combine mutually exclusive choices, violate programme rules, choose weak options to favor UCR, invent courses to fill open space, or make the comparator artificially narrow.

Preserve programme/provider, permanent counselor identity and registry provenance where relevant, source URLs, academic/curriculum year, date checked, selected route/track and validation/exception notes.

---

# 7. UCR course evidence

Use the enriched UCR course database as authoritative for UCR course selection and feasibility. Use course `name`, outline-derived `profile`, `discipline`, `topics`, `methods`, `description2`, prerequisites, planned semester availability and credits as relevant. Use course content rather than administrative cluster labels or title similarity alone.

For counselor production, the UCR database **implements** already established concepts. Convenient availability must not retroactively generate or broaden a concept.

---

# 8. UCR feasibility validation

Each UCR programme must contain exactly 24 unique courses, four in each of six semesters, at least six 300-level courses, and Personal & Professional Development in Year 1. Every prerequisite must be completed earlier, every course must be available in its assigned semester, and no course may be duplicated.

Do not invent cluster/concentration/breadth requirements. Validate course count, uniqueness, semester load, level minimum, PPD, prerequisite order and semester availability mechanically against the enriched database. If validation fails, repair and validate again. Repository/schema validation is not a substitute for academic feasibility validation.

---

# 9. Compare the completed curricula

Construct and validate all four programmes before building comparison blocks. Apply the same substantive classification principles across all four programmes. Treat methods/statistics/mathematics/econometrics/laboratory work/research training as disciplinary depth where they genuinely serve that role.

## 9.1 Blocks are analytical alignments, not curriculum partitions

Derive blocks from genuinely comparable parts of the completed curricula. An external curriculum component is not automatically a comparison-block title, and there is no automatic one-external-component-to-UCR-course-group mapping.

There is no required number of blocks, no default three-block structure, no default 60-EC block, and no requirement that all UCR courses appear. Blocks may aggregate or split external components when that gives a more truthful substantive alignment. Unequal credit totals and blank cells are legitimate.

A repeated fixed UCR allocation across every block—for example the same number of courses or the same EC total in every block—is presumed to be a template failure unless the curriculum itself independently justifies that pattern. Rebuild such a comparison rather than defending the symmetry after the fact.

## 9.2 Alignments and gaps

Align substantively comparable material horizontally; preserve actual EC; preserve blank cells and structural differences; label genuinely open space when needed; leave specialist components unmatched when UCR has no genuine counterpart; and do not insert a UCR course simply because every scheduled course needs somewhere to go. Do not use numerical depth/breadth scores.

---

# 10. Reusable explanatory notes

Use a note only when a material difference could otherwise be misunderstood. Approved types are:

- `less-disciplinary-depth` — UCR covers the field but not the external specialist sequence;
- `related-fields-not-full-discipline` — UCR approaches the subject through related fields rather than the full discipline;
- `missing-specialist-components` — substantial core overlap but specialist external components are absent at UCR;
- `different-curricular-structure` — related territory is organized differently.

Populate only evidenced claims, do not exaggerate equivalence or hide absence, and omit the note when the comparison is self-explanatory.

---

# 11. Canonical records

Create one structured record before rendering any output. Preserve stable ID/origin, four programme identities and roles, comparator metadata and official URL, complete UCR schedules, component credits, comparison alignments/gaps, explanatory notes where needed, validation status and internal source metadata.

Student records additionally preserve original interest wording and separate interpretation and remain private unless explicitly approved for public use.

## 11.1 Counselor-origin additions

Current counselor production records use `schemaVersion: "1.3"`.

Preserve permanent `counselor_programme_id`; normalized target identity and provenance; registry/production order; institutions, languages and modes; source/offering/programme-unit/recognized/variant identifiers; and `academicRationale` containing:

- evidence-backed `coreField`;
- evidence-backed `adjacentDirections`;
- evidence-backed `questionsApplications`;
- selected `balancedDirections`;
- evidence-backed `thematicQuestion` and its `basisLabels`;
- `courseAlignment` covering exactly the 24 scheduled courses in each of `ucr-depth`, `ucr-balanced` and `ucr-thematic` under the role-specific traceability rules above.

Top-level `id` and `programmeProvider.counselorProgrammeId` must both equal the permanent `counselor_programme_id` (`cp-000001` format). Use normalized arrays for languages and modes.

---

# 12. Student app and optional PDF

Render student outputs from the canonical student record. Preserve the distinction between **You told us that…** (original wording) and **For us, this means that…** (academic interpretation). Until approved final wording is supplied, use the explicit disclaimer placeholder:

> **[PLACEHOLDER — insert approved student-program disclaimer from the printed butterfly.]**

Any optional PDF must draw from the same canonical record rather than maintain independent academic content.

---

# 13. Counselor library and discovery indexes

Keep programme discovery metadata, programme-interest discovery index and deterministic comparison records separate. Do not flatten all interests into comparison records. The academic rationale stores only evidence actually used to justify the UCR concepts and courses.

Search always resolves to an in-scope normalized target and then loads the fixed comparison. Targets outside current production scope remain in the registry but not the production discovery indexes while no approved comparison exists.

---

# 14. Public export

Neither workflow publishes automatically. Prepare a publication record only after substantive human review and explicit public approval. Derive public content from the canonical record without reselecting courses, rebuilding alignments, exposing private identity or inventing renderer-specific academic facts.

---

# 15. Final validation

Before marking a counselor record complete, confirm:

## External programme

- correct normalized target and institution(s);
- current official source basis;
- compulsory/restricted/open components and route represented fairly;
- EC and provenance recorded without invented components.

## Academic rationale

- map created before UCR course selection;
- every map item evidence-backed;
- inherited split evidence not misused;
- balanced directions are actual adjacent map directions;
- thematic question is evidence-backed, scope-closed by its basis labels and introduces no unsupported domain;
- broadening is not generated from convenient UCR availability.

## Course-level traceability

- every scheduled UCR course has exactly one `courseAlignment` entry and vice versa;
- every non-PPD depth course traces to `coreField`;
- every non-PPD balanced course traces to `coreField` or the selected balanced directions;
- every non-PPD thematic course traces to a `thematicQuestion.basisLabel`;
- reasons are substantive rather than generic breadth claims;
- `ACCPPDE101` is the only `ucr-required` exception.

## UCR feasibility

- 24 unique courses, four per semester, at least six 300-level, PPD in Year 1;
- prerequisites and semester availability satisfied;
- depth/balanced/thematic programmes actually implement their fixed concepts.

## Comparison

- blocks are genuine analytical alignments rather than curriculum partitions;
- no automatic external-component-to-block mapping;
- no fixed repeated UCR course/credit allocation across blocks;
- genuine gaps and unequal weights remain visible;
- credits are shown consistently;
- notes are used only where needed.

## Record and export controls

- schema/structural validity and registry metadata parity;
- permanent ID consistency;
- no accidental personalization from search;
- production order/resumability preserved;
- public export, if requested, has explicit approval and no substantive reinterpretation.

Only then release the record or requested artifact.
