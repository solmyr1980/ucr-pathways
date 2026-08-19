# UCR Pathways — Master Specification and Decision Record

**Status:** Authoritative product specification

## Purpose and document boundary

This document contains the durable product, academic, content and architectural decisions for UCR Pathways.

It does **not** record implementation status, completed work, temporary problems, deployment history, exact build commands or a running backlog.

Use the following sources of truth for those matters:

- the **UCR Pathways Production Instructions** for academic generation and Open Day production;
- the **UCR Pathways Web and LinkedIn Workflow** for public publication operations;
- the enriched UCR course database for UCR course evidence and availability;
- the repository schema for the executable public-data contract;
- the GitHub repository, Actions configuration and commit history for implementation state and build mechanics.

A document should change only when a durable decision within its own domain changes.

---

# 1. Product identity and scope

## 1.1 UCR Pathways

**UCR Pathways** is the student-facing pathway-comparison experience. It shows how a prospective student's interests could translate into different undergraduate programmes.

It compares:

1. one disciplinary bachelor programme used as a reference programme; and
2. three feasible UCR programmes that progressively move from greater disciplinary depth toward broader combinations of interests and themes.

UCR Pathways has two pilot uses:

- personalized Open Day outputs for individual participants; and
- curated public examples used on the UCR Pathways website and in LinkedIn posts.

These uses share the same academic comparison logic. Open Day participant outputs are not automatically public examples.

### Meaning of “Pathways”

In this project, **pathways** means **illustrative academic possibilities**.

It does **not** mean official UCR tracks, prescribed routes or fixed curricular templates. The purpose is to make curricular possibilities visible without implying that UCR formally offers these pathways.

## 1.2 UCR Program Builder

The **UCR Program Builder** is a separate downstream experience in which a prospective student can actually build a programme.

UCR Pathways should therefore lead interested students toward the Program Builder rather than treating further pathway comparison as the final call to action.

Canonical destination:

`https://program.ucr.nl/`

## 1.3 Production instructions

For the pilot, the UCR Pathways production instructions are executed within this project. A separate configured Custom GPT is not required.

They govern academic generation, validation, canonical-record creation, Open Day output and preparation of an approved public example record. They do not publish directly to GitHub, the website or LinkedIn.

---

# 2. Core proposition and comparison model

UCR Pathways should make the curriculum trade-off visible rather than explain Liberal Arts and Sciences primarily in abstract language.

A disciplinary bachelor provides a clear endpoint of disciplinary depth. The three UCR programmes show progressively different ways of combining depth, multiple interests and broader themes.

Neither model should be presented as inherently superior. Genuine strengths of the disciplinary programme and genuine limitations of UCR should remain visible.

The programmes themselves should carry most of the argument.

## 2.1 Four programme roles

Every comparison contains exactly four programmes in this order:

1. disciplinary reference programme;
2. UCR — greatest feasible disciplinary depth;
3. UCR — balanced interests;
4. UCR — thematic breadth.

All four receive short participant-specific titles.

For public structured data, the four semantic roles are:

1. `comparator`;
2. `ucr-depth`;
3. `ucr-balanced`;
4. `ucr-thematic`.

The semantic role is the stable meaning. Visible titles remain example-specific.

---

# 3. Student input and privacy

The standard prospective-student question is:

**“What are your interests?”**

The answer may contain disciplines, topics, questions, problems, practical interests, skills or phenomena in any combination.

The production process must:

- preserve the participant's original wording;
- interpret the response academically;
- not assume that the first-mentioned interest is more important;
- not ask follow-up questions;
- not require the student to understand UCR's curriculum structure;
- not manufacture weak curricular matches where UCR represents an interest poorly.

For a participant who supplies one interest, broaden through meaningful subfields, questions and neighbouring perspectives rather than inventing an additional interest.

For Open Day production, the academic process receives:

- `participant_id`;
- `interest_statement`.

The UCR starting semester is configured for the batch rather than treated as participant-specific input.

Names and other personal information remain outside UCR Pathways.

Public examples must not expose an identifier in a way that links them back to an individual registration record.

---

# 4. Language, copy and visual identity

## 4.1 Disciplinary

Use **disciplinary** rather than **traditional** throughout UCR Pathways.

Do not describe the reference programme as a “traditional” degree.

## 4.2 Interdisciplinary

In student-facing material, avoid *interdisciplinary* when ordinary language communicates the idea more clearly.

Prefer wording such as:

- broader;
- combining interests;
- bringing different interests together.

Internal analytical work may use *interdisciplinary* where it is genuinely more precise.

## 4.3 Student-facing language

Write for a prospective undergraduate student, including a 17-year-old who does not know university curriculum terminology.

Prefer short, ordinary language. Do not expand otherwise clear wording merely to cover minor linguistic edge cases.

Do not use recruitment superlatives or imply that UCR is inherently superior.

## 4.4 Product identity line

The approved product-level identity line is:

> See how your interests can shape a UCR programme — and where it can lead.

## 4.5 Comparison-specific introductory sentence

The approved comparison sentence is:

> See how your interests could take shape in a disciplinary degree and three progressively broader UCR pathways.

Use **“your interest”** rather than **“your interests”** when the participant supplied one interest.

## 4.6 Reference programme provenance

The disciplinary bachelor used as the comparison point should be identified in student-facing materials with:

> Reference programme: *[programme name], [institution]*

The participant-facing title of the first programme remains separate and may be concise, for example:

> Disciplinary Economics

Do not use `Inspired by ...` or `Based on ...` as the default provenance wording.

Where the format supports links, the Reference programme line should link to the exact approved official programme or curriculum source used as the primary public reference.

If a future comparison genuinely depends on several formally separate programme sources, adapt the provenance wording rather than implying that the full comparison comes from one programme.

## 4.7 UCR visual identity

Student-facing web and PDF outputs should use the settled UCR visual identity.

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

If required brand fonts are unavailable, treat that as a rendering limitation to fix or report rather than silently inventing a different visual identity.

---

# 5. Disciplinary reference programme

## 5.1 Selection

Choose the disciplinary bachelor that provides the most useful depth endpoint for the participant's interests.

Do not automatically choose the discipline mentioned first.

For the pilot, prefer a current Dutch research-university bachelor where one is suitable.

## 5.2 Source basis

First check whether a suitable current verified reference-programme record exists.

If one exists, use it as the primary factual basis and consult current official sources when it is incomplete, ambiguous, outdated or materially conflicts with current information.

If no suitable verified record exists, reconstruct the programme from current official university sources.

Prefer, where available:

1. formal curriculum or graduation requirements;
2. official student-facing curriculum pages;
3. official route, track or specialization pages;
4. official course-catalogue entries;
5. general prospective-student programme pages.

Do not use rankings, aggregators or unofficial summaries to establish programme structure.

For the primary public reference, prefer a current official source that makes the selected programme and its structure easy for a reviewer to verify — ideally one curriculum or requirements page or document — over a marginally richer but unnecessarily fragmented source basis.

Use additional official sources where necessary and preserve them in internal verification metadata.

If the reference programme cannot be reconstructed with reasonable confidence, choose another defensible reference programme rather than guessing.

## 5.3 Fair reconstruction

Before selecting what to display, distinguish:

- compulsory components;
- restricted choices;
- tracks, routes or specializations;
- genuinely free elective or profiling space;
- methods and research training;
- thesis or capstone requirements;
- relevant credit weights.

Give the reference programme the same reasonable opportunity for personalization that UCR receives.

Where choices exist, select one coherent valid pathway that responds reasonably to the participant's interests.

Never:

- present optional components as compulsory;
- combine mutually exclusive choices;
- violate programme rules;
- deliberately choose weak options to make UCR look better;
- invent courses to fill genuinely open elective space;
- make the reference programme artificially narrow merely to sharpen the contrast with UCR.

Represent genuinely open space explicitly.

## 5.4 Verification metadata and approval

The canonical record should preserve, where relevant:

- programme name;
- institution;
- primary official source URL;
- additional official source URLs;
- academic or curriculum year;
- date checked;
- source notes;
- route, track or specialization selected;
- validation notes about the selected pathway;
- reviewer-approval status.

For a manually supervised production run, the proposed reference programme and authoritative source basis must be approved before full generation continues.

This is the only routine intermediate academic checkpoint. The final output remains subject to human checking before printing or publication.

A comprehensive reference-programme database is not required for the pilot.

---

# 6. UCR course evidence and feasibility

## 6.1 Course evidence

Use the enriched UCR course database as the authoritative source for UCR course selection and feasibility.

Use course content rather than administrative cluster or unit labels.

Give particular weight to outline-derived `profile` information where available, alongside:

- `name`;
- `discipline`;
- `topics`;
- `methods`;
- `description2`;
- prerequisites;
- planned semester availability.

Do not infer fit from a course title alone when richer course evidence points elsewhere.

## 6.2 Feasibility rules

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

Validate all UCR feasibility rules mechanically against the enriched course database. Repository validation is not a substitute for academic feasibility validation.

---

# 7. Comparison principles

Construct and validate all four programmes before designing the comparison.

Apply the same substantive classification principles to the reference programme and the UCR programmes.

Use course or component content rather than titles alone.

Methods, statistics, mathematics, econometrics, laboratory work and research training may contribute to disciplinary depth where they genuinely serve that role.

Do not assume that one reference-programme component equals one UCR course.

Preserve actual component weights, including 5, 7.5, 10 or other EC values, and do not distort either curriculum to force exact row-by-row or credit-by-credit correspondence.

Do not use proportional course-box scaling as a general encoding of credit weight. Where component size matters, show EC values or concise explanatory notes.

Derive meaningful substantive comparison blocks from the completed curricula.

Within blocks:

- align genuinely comparable components horizontally;
- retain meaningful blank cells;
- do not fill gaps merely for visual symmetry;
- label genuinely open elective or profiling space explicitly;
- show credit weights where omitting them would materially distort the comparison.

Do not use numerical depth or breadth scores.

---

# 8. Canonical and public content architecture

## 8.1 Canonical pathway record

For each completed case, create one **canonical pathway record** before rendering.

It is the authoritative academic representation of the comparison.

At minimum it should preserve:

- the original interest statement;
- relevant cohort or starting-semester context;
- four programme identities, roles and participant-specific titles;
- reference-programme components, notes and relevant credit weights;
- Reference programme provenance and internal verification metadata;
- the complete 24-course set for each UCR programme;
- the six-semester schedule for each UCR programme;
- substantive comparison blocks;
- horizontal alignments and deliberate gaps;
- explanatory or source notes needed for fair interpretation;
- academic validation status.

The canonical record contains content and semantic structure, not renderer-specific geometry, CSS or page coordinates.

Renderers may ignore fields they do not need, but they must not reinterpret or invent programme facts.

## 8.2 Public publication record

A comparison becomes public only after:

1. substantive human review; and
2. explicit approval for public use.

The publication record is derived from the canonical record. Do not reselect courses, reconstruct the comparison or rebuild alignments during publication export.

It should use a publication-safe example ID and contain no personal information beyond the interest statement explicitly approved for publication.

The approved publication record is the single programme-content source for both:

- the public website example; and
- the LinkedIn PDF.

The public record must conform to the repository's current executable schema.

The complete UCR schedules remain mandatory in the canonical record. They need only be included in the public record when required by the current public data contract or renderer.

Do not maintain separate hand-edited HTML, website content or LinkedIn/PDF programme content.

---

# 9. Open Day product requirements

The normal Open Day workflow is batch preparation before the event.

Registration supplies a participant ID and the participant's answer to **“What are your interests?”**. Before the event, cases are generated and validated in batch, the final outputs are human-checked, and the personalized PDFs are printed and organized for handover with the participant's entrance or registration materials.

The preparation itself is part of the value proposition: the participant supplies only a short statement of interests, yet UCR has already translated it into concrete academic possibilities. The handout can then support conversations with faculty, students and staff during the day.

Live generation is a fallback for walk-ins, missing inputs, failed generation or missing printed outputs and uses the same production instructions. No separate live-generation application is required for the pilot.

The personalized Open Day output is a **two-page A4 portrait PDF** derived from the canonical pathway record.

## 9.1 Page 1

Page 1 shows the four programmes side by side and is not organized by semester.

It should include:

- participant ID;
- original interest statement;
- the approved comparison sentence;
- the approved Reference programme provenance line;
- participant-specific programme titles;
- substantive blocks, alignments, deliberate gaps and relevant notes;
- EC information where needed for fair interpretation.

## 9.2 Page 2

Page 2 shows the same three UCR programmes semester by semester.

Each programme shows:

- six semesters;
- exactly four courses per semester;
- course level.

Course codes may be omitted visibly when they add clutter, but remain in the canonical record where available.

## 9.3 Call to action and handover

The Open Day QR code or link points to the UCR Program Builder:

the canonical UCR Program Builder destination defined in Section 1.2

The intended progression is:

**personalized UCR Pathways preview → build your own programme in the UCR Program Builder**

The QR code does not need to restore the participant's exact Open Day pathway. Do not imply persistence unless it has actually been implemented.

Use participant ID as the PDF filename, for example `P-037.pdf`.

The handover can remain:

> “You told us what interested you when you registered, so we prepared three possible UCR programmes around it. This one is yours.”

---

# 10. Public website requirements

The public website presents **curated examples**, not the full set of Open Day participant outputs.

The website is data-driven: programme-specific content comes from approved structured publication records rather than being hardcoded into the renderer.

The public root presents a catalog of approved examples.

For an individual example:

- wide screens show all four programmes side by side by default;
- narrow screens show one programme at a time;
- wide screens offer `Compare all | One at a time`;
- one-at-a-time mode supports forward/back controls, keyboard arrows and touch swiping.

The renderer should remain generic as examples are added.

## 10.1 Link hierarchy

Use this link logic:

- **UCR logo or UCR wordmark** → main UCR website;
- **UCR Pathways title/logo** → UCR Pathways landing page;
- **Reference programme line** → exact approved official reference-programme source;
- **Build your own programme** CTA → the canonical UCR Program Builder destination defined in Section 1.2;
- any UCR Program Builder logo or wordmark used as a CTA → the same Program Builder destination.

External destinations should normally open in a new tab. Internal UCR Pathways navigation should normally remain in the same tab.

Only elements with a clear useful destination should be clickable.

## 10.2 Public-site CTA

Use:

> Build your own programme

Do not imply that the displayed example will automatically transfer into the Program Builder unless that functionality has actually been implemented.

## 10.3 Compact first viewport

Substantive material should appear quickly.

The opening should normally contain:

- one compact identity/header area;
- UCR and UCR Pathways identities;
- the interest statement where relevant;
- essential actions and navigation;
- at most one short explanatory sentence before the comparison.

Avoid excessive non-informative vertical space above the comparison.

---

# 11. LinkedIn requirements

The LinkedIn PDF is derived from the same approved publication record as the public website.

Use one programme per PDF page so mobile users can swipe through the progression.

The disciplinary programme page uses the same approved Reference programme provenance as the website and Open Day output.

The LinkedIn renderer may use format-specific layout, but it must not maintain or reinterpret an independent copy of programme content.

For the pilot:

- publication remains human-controlled;
- the post links to the corresponding specific UCR Pathways example, not merely the landing page;
- several approved posts may be prepared and placed into LinkedIn's native scheduled-post queue.

Full automation of the transfer to LinkedIn is outside the pilot scope.

---

# 12. Document ownership and maintenance rule

Maintain three project documents:

1. **Master Specification** — durable product, academic, content and architectural decisions.
2. **Production Instructions** — executable academic generation, validation, Open Day output and public-export procedure.
3. **Web and LinkedIn Workflow** — operational handoff from an approved public record to GitHub, the website, LinkedIn PDF and manual LinkedIn publication.

Do not duplicate information merely because it is important.

Repeat a rule in another document only when that document needs the rule directly to execute its own task and the duplication is worth the maintenance cost.

Do not use these documents to record:

- successful or failed GitHub runs;
- implementation history;
- repository rename history;
- completed-task lists;
- temporary bugs;
- deployment status;
- routine next steps.

Those belong in the systems that actually execute or record the work.

---

# 13. Deferred beyond the pilot

The following remain outside pilot scope:

- a large reusable verified reference-programme database;
- a comprehensive Dutch bachelor-programme database;
- master's/alumni destination suggestions;
- full LinkedIn transfer automation;
- persistence that restores an exact UCR Pathways example in the UCR Program Builder.

The renderer may continue to evolve while the core data and content architecture remain stable.
