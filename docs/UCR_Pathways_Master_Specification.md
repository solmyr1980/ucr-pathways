# UCR Pathways — Master Specification and Decision Record

**Status:** Authoritative product specification

## Purpose and document boundary

This document contains the durable product, academic, content and architectural decisions for the UCR Pathways project.

It does **not** record implementation status, completed work, temporary problems, deployment history, exact build commands or a running backlog.

Use the following sources of truth for those matters:

- the **UCR Pathways Production Instructions** for academic generation, validation and record creation;
- the **UCR Pathways Web and LinkedIn Workflow** for public curation and publication operations;
- the enriched UCR course database for UCR course evidence and availability;
- the Dutch bachelor programme registry and programme-interest enrichment data for the counselor corpus and discovery layer;
- the repository schemas for executable data contracts;
- the GitHub repository, Actions configuration and commit history for implementation state and build mechanics.

A document should change only when a durable decision within its own domain changes.

---

# 1. Project identity and four-surface architecture

## 1.1 UCR Pathways is the internal project name

**UCR Pathways** remains the internal project name and the name of the GitHub repository.

It is **not** a user-facing product or sub-brand. Student-facing, counselor-facing and public interfaces must use UCR branding without displaying `UCR Pathways`, `Pathways` or equivalent project identifiers as a visible product identity.

Technical repository paths and internal identifiers may continue to contain `ucr-pathways` where changing them would add no user value.

## 1.2 Four user/public surfaces

The project supports four distinct surfaces that share academic comparison content but serve different purposes:

1. **Student app** — a personalized experience generated from an actual prospective student's submitted interests.
2. **Counselor app** — a deterministic searchable library of pre-produced comparisons, one per programme-provider record in scope.
3. **Public website** — a curated communication and showcase layer, not an exhaustive comparison database.
4. **LinkedIn** — an editorial distribution channel using selected approved comparisons and stories.

The website and LinkedIn are not additional academic-generation workflows. They reuse approved content from the student or counselor workflow.

## 1.3 UCR Program Builder

The **UCR Program Builder** is a separate downstream experience in which a prospective student can build or modify a programme.

Canonical destination:

`https://program.ucr.nl/`

Do not imply that a displayed programme transfers automatically into the Program Builder unless that functionality has actually been implemented.

---

# 2. Core comparison model

The project should make curriculum choices and trade-offs visible rather than explain Liberal Arts and Sciences primarily in abstract language.

A comparison contains exactly four programme roles in this semantic order:

1. `comparator` — one external Dutch bachelor programme;
2. `ucr-depth` — the closest feasible UCR match;
3. `ucr-balanced` — a UCR programme combining the field with related subjects or the student's additional interests;
4. `ucr-thematic` — a broader UCR programme organised around relevant interests, questions or themes.

The semantic roles are stable internal meanings. Visible labels are case-specific and should use ordinary language rather than internal role names.

Neither the external bachelor nor UCR should be presented as inherently superior. Genuine strengths of the external programme and genuine limitations of UCR must remain visible.

## 2.1 Visible programme labels

Use descriptive labels in the style of:

- comparator: **[Programme] at [Institution]**;
- `ucr-depth`: **Closest match to [programme or field]**;
- `ucr-balanced`: **[programme or field] + related subjects**;
- `ucr-thematic`: **A broader programme around your interests** or the equivalent case-specific wording.

Do not use visible labels such as `Reference programme`, `greatest disciplinary depth`, `balanced interests`, `thematic breadth`, `strong match` or `off the beaten track` as the default interface taxonomy.

The comparator heading itself supplies programme and institution provenance and should link to the approved official programme or curriculum source.

---

# 3. Student app

## 3.1 Input and generation model

The student app is **organic and personalized**. It is generated only from actual prospective-student input received through the designated website form or equivalent approved intake route.

The standard question remains:

**“What are your interests?”**

The answer may contain disciplines, topics, questions, problems, practical interests, skills or phenomena in any combination.

The production process must:

- preserve the student's original wording;
- interpret the response academically;
- not assume that the first-mentioned interest is more important;
- not require the student to understand UCR's curriculum structure;
- not manufacture weak curricular matches where UCR represents an interest poorly.

For a student who supplies one interest, broaden through meaningful subfields, questions and neighbouring perspectives rather than inventing an additional interest.

## 3.2 Student app journey

The student experience should begin with a personalized welcome screen.

Show both:

> **You told us that…**
>
> [student's original wording]

and:

> **For us, this means that…**
>
> [concise academic interpretation]

The welcome screen should provide access to two views of the same approved personalized record:

- **View my personalized programme options** — semester-by-semester views of all three UCR programmes, in the stable order `ucr-depth`, `ucr-balanced`, `ucr-thematic`;
- **See how these options compare** — the four-programme comparison.

All three UCR programmes are personalized options generated from the same student interests. The student app must not present `ucr-depth` as the sole personalized programme while hiding the other two semester schedules. Within the programme-options view, use clear sub-navigation such as tabs or selectors so that the student can inspect each complete six-semester programme without requiring one long stacked page.

The interface may allow movement between these views without regenerating academic content.

## 3.3 Student calls to action

After the substantive programme content, provide two distinct next steps where the interface supports them:

- **Speak to Admissions** — to the approved Admissions contact or booking route;
- **Tweak this programme to your liking** — to the canonical UCR Program Builder destination.

Exact Admissions destination is implementation/configuration data rather than a durable academic rule.

## 3.4 Student disclaimer

Each personalized programme option must carry an approved disclaimer explaining its illustrative status and the relevance of actual curriculum rules and course availability.

Until the approved text from the printed butterfly is supplied, use the explicit placeholder:

> **[PLACEHOLDER — insert approved student-program disclaimer from the printed butterfly.]**

The placeholder must be visibly distinguishable in development and must not be mistaken for approved final copy.

## 3.5 Student privacy and access

Names and unnecessary personal information remain outside academic pathway records.

Student-specific access codes or links must not expose private pathway records through a public code-to-record mapping. Production privacy must use an appropriate private access/storage mechanism.

A student case is not automatically approved for public website or LinkedIn use.

---

# 4. Counselor app

## 4.1 Deterministic corpus

The counselor app is **deterministic**, not a live personalization engine.

Produce one fixed comparison for every programme-provider record in the approved Dutch bachelor registry scope. The programme-provider record is the unit of production: the same recognized programme offered by two providers is treated as two records when the registry distinguishes them.

Production proceeds in existing registry worksheet order. Do not prioritize cases by UCR fit, applicant popularity, blank-cell count or another ranking criterion.

## 4.2 Two discovery routes, one comparison library

The counselor may discover the same fixed comparison through either:

- programme identity; or
- student-facing interests associated with programmes in the programme-interest enrichment data.

These routes are **not competing products**. They are two entry points into one deterministic comparison library.

Use one search experience where practical:

> **Search by programme or interest**

Programme name, institution and relevant metadata may be searched directly. Interest search uses the linked programme-interest table to return ranked programme-provider records.

Interest search is a **discovery mechanism only**. Entering an interest does not regenerate or personalize the selected comparison. The interface must not imply otherwise.

## 4.3 Interest-search ranking

Use `interest_relationship` as the principal evidence distinction for deterministic search ranking:

1. direct programme interest;
2. stable study direction;
3. curricular topic;
4. illustrative or temporary topic;
5. outcome or individual trajectory.

Categories 1–2 form the conservative core. Category 3 may broaden discovery. Categories 4–5 may remain searchable but should not be presented as equally strong evidence that the bachelor structurally targets the interest.

The interface may show matching interests or other concise reasons for a programme appearing in the results.

## 4.4 Counselor filters

The counselor interface may provide filters supported reliably by the programme registry, such as institution, location, degree type or disciplinary grouping.

Filters refine discovery; they do not alter the underlying fixed comparison.

## 4.5 Counselor transparency

The counselor interface must explain that:

- comparisons are pre-produced at programme-provider level;
- interest search helps locate relevant programmes but does not personalize the comparison to an individual student;
- the UCR programmes are illustrative feasible compositions rather than official tracks or guaranteed future schedules.

---

# 5. External programme evidence and fair reconstruction

## 5.1 Source basis

Use current official university sources to reconstruct each comparator.

Prefer, where available:

1. formal curriculum or graduation requirements;
2. official student-facing curriculum pages;
3. official route, track or specialization pages;
4. official course-catalogue entries;
5. general prospective-student programme pages.

Do not use rankings, aggregators or unofficial summaries to establish programme structure.

For public-facing links, prefer one current official page that makes the programme and its structure easy to verify. Preserve additional official sources internally where needed.

## 5.2 Fair reconstruction

Before selecting what to display, distinguish:

- compulsory components;
- restricted choices;
- tracks, routes or specializations;
- genuinely free elective or profiling space;
- methods and research training;
- thesis or capstone requirements;
- relevant EC weights.

Where choices exist, select one coherent valid pathway appropriate to the production context.

Never:

- present optional components as compulsory;
- combine mutually exclusive choices;
- violate programme rules;
- deliberately choose weak options to make UCR look better;
- invent courses to fill genuinely open elective space;
- make the external programme artificially narrow merely to sharpen the contrast with UCR.

Represent genuine gaps honestly.

## 5.3 Comparator presentation

In user-facing digital interfaces, identify the comparator directly as:

> **[Programme] at [Institution]**

Link this heading or an adjacent clear source link to the approved official programme page.

Do not require a separate visible `Reference programme:` line.

Internal records must still preserve the programme name, institution and source metadata explicitly.

---

# 6. UCR course evidence and feasibility

Use the enriched UCR course database as the authoritative source for UCR course selection and feasibility.

Use course content rather than administrative cluster or unit labels. Give particular weight to outline-derived `profile` information where available, alongside name, discipline, topics, methods, descriptions, prerequisites and planned semester availability.

Each UCR programme must contain:

- exactly **24 unique courses**;
- exactly **4 courses in each of six semesters**;
- at least **6 courses at 300 level**;
- **Personal & Professional Development** during Year 1.

In addition:

- every prerequisite must have been completed in an earlier semester;
- every selected course must actually be available in the semester in which it is placed;
- courses may not be duplicated.

Do not invent additional requirements concerning clusters, units, concentrations, breadth or disciplinary distributions.

Validate all UCR feasibility rules mechanically against the enriched UCR course database.

---

# 7. Comparison principles and credits

Construct and validate all four programmes before designing the comparison.

Apply the same substantive classification principles to the external programme and UCR programmes. Use content rather than titles alone.

Do not assume that one comparator component equals one UCR course.

Preserve actual component weights. **Show EC credits consistently on both the external and UCR sides** when displaying curriculum components; do not show comparator EC while leaving equivalent UCR components unlabelled.

Do not use proportional course-box scaling as a general encoding of credit weight.

Within comparison blocks:

- align genuinely comparable components horizontally;
- retain meaningful blank cells;
- do not fill gaps merely for visual symmetry;
- preserve structural differences neutrally;
- do not introduce special research-seminar callouts merely to reduce gaps;
- do not add exchange opportunities merely to fill open space;
- do not create a new special rule for elective-space symmetry.

Do not use numerical depth or breadth scores.

## 7.1 UCR links

Digital comparison interfaces must provide an appropriate link to UCR curriculum information in addition to the comparator's official programme link.

The exact destination may be configured centrally and updated without changing academic records.

---

# 8. Reusable explanatory notes

Explanatory notes should be generated from evidenced comparison facts using reusable semantic templates rather than written manually for every programme-provider case.

The Production Instructions define the executable note taxonomy and generation rules.

A note is warranted only when it helps prevent a material misunderstanding. Do not add boilerplate beneath every comparison merely because a template exists.

Preserve warranted limitation notes in every representation of the comparison, including single-programme/mobile views and PDFs. Switching views must not hide a material limitation of the UCR match.

---

# 9. Canonical comparison records

Create one canonical structured comparison record before rendering any surface.

The record must identify its origin, normally either:

- `student` — personalized from an actual student's interest statement; or
- `counselor` — fixed to one programme-provider record.

The shared comparison core should preserve:

- origin and stable record identity;
- comparator programme name, institution and official source URL;
- four programme identities and semantic roles;
- complete 24-course sets and six-semester schedules for the three UCR programmes;
- component EC credits where applicable;
- comparison blocks, alignments and deliberate gaps;
- explanatory-note type and parameters or rendered text where required;
- academic validation status and internal source/verification metadata.

Student-origin records additionally preserve the original interest statement and academic interpretation.

Counselor-origin records additionally preserve the programme-provider identifiers needed to join back to the programme registry and programme-interest index.

The canonical record contains content and semantic structure, not renderer-specific coordinates, CSS or page geometry.

Renderers may ignore fields they do not need, but they must not reinterpret or invent programme facts.

---

# 10. Public website

The public website is a **curated communication and showcase layer**, not the exhaustive counselor database and not the private student app.

It should:

- use UCR branding without visible Pathways branding;
- present a deliberately selected set of examples or stories;
- explain programme possibilities through concrete comparisons rather than an exhaustive catalogue;
- provide a clear route for prospective students toward the student intake/personalized experience;
- provide a clear route for school counselors toward the counselor comparison tool;
- provide the Program Builder CTA where appropriate.

Most public examples will normally be selected from approved counselor comparisons because they are stable and privacy-safe. A student-origin case may be used only after explicit public-use approval and removal of identifying information.

The website remains data-driven. Programme-specific content must come from approved structured publication records rather than being hardcoded into the renderer.

---

# 11. LinkedIn

LinkedIn is an editorial distribution channel, not a separate academic source.

Use selected approved publication records from either:

- the counselor corpus, normally; or
- an explicitly approved privacy-safe student case.

The LinkedIn PDF and public website example should continue to consume the same approved public programme content when they present the same case.

Editorial framing belongs in the LinkedIn post commentary rather than in a second hand-edited copy of programme content.

Existing editorial scenarios may continue, including:

- the degree that does not exist;
- what do you have to give up?;
- start with the question;
- same interest, surprisingly different programmes;
- findings from the Dutch bachelor market.

The larger deterministic counselor corpus and programme-interest index may supply examples and evidence for these scenarios.

Publication remains human-controlled unless a later decision explicitly changes that rule.

---

# 12. Public curation and privacy

Neither the student app nor the counselor app automatically publishes a case to the public website or LinkedIn.

A comparison becomes public only after:

1. substantive human review;
2. explicit approval for public use; and
3. creation of a publication-safe record conforming to the current repository contract.

Do not maintain separate hand-edited programme-content copies for website and LinkedIn.

---

# 13. Optional event/PDF outputs

Existing Open Day and other PDF renderers may continue to use the same canonical academic records where useful.

They are output formats, not separate academic products. Their existence must not force the student app, counselor app, website or LinkedIn to maintain separate programme content.

---

# 14. Visual identity

All user-facing surfaces should follow the settled UCR visual identity.

Approved palette:

- Heritage Plum: `#491E34`
- Foundation White: `#F8F5EE`
- Academic Black: `#2E2D2D`
- Thoughtful Grey: `#5C606B`
- Reflective Lilac: `#D0B7D0`
- Clarity Blue: `#C8DFE6`
- Open Yellow: `#FFE1A4`
- Grounded Green: `#4A6857`

Use **IvyMode** for display headings and **Inter** for body text in the configured UCR rendering environment.

Use colour primarily for identity, navigation and orientation rather than as the main substantive classification of courses.

Use the UCR logo without redundant institutional naming beside it. Keep text readable against its actual background, including link, visited, hover, selected and keyboard-focus states. Check narrow screens and enlarged text as well as desktop layouts.

If required brand fonts are unavailable, treat that as a rendering limitation to fix or report rather than silently inventing a different visual identity.

---

# 15. Document ownership and implementation boundary

Maintain three authoritative project documents:

1. **Master Specification** — durable product, academic, content and architectural decisions.
2. **Production Instructions** — executable academic generation, validation and record-creation procedure for both student and counselor workflows.
3. **Web and LinkedIn Workflow** — operational public curation, website and LinkedIn publication workflow.

Exact schema fields, storage paths, search implementation, Shiny code, hosting choice and deployment commands belong to the repository implementation unless a durable architectural decision explicitly promotes them into this specification.

In particular, **Shiny/Shinylive is an implementation candidate, not an authoritative product requirement** at this stage.

Do not use these documents to record successful or failed runs, temporary bugs, deployment status or routine next steps.