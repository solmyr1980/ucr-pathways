# UCR Pathways — Master Specification and Decision Record

**Status:** Authoritative product specification

## Purpose and document boundary

This document contains the durable product, academic, content and architectural decisions for the UCR Pathways project.

It does **not** contain the detailed procedure for generating academic records, public-publication operations, implementation status, completed work, temporary problems, exact build commands or a running backlog.

Use the following sources of truth:

- **UCR Pathways Production Instructions** — academic generation, validation and record creation;
- **UCR Pathways Web and LinkedIn Workflow** — public curation, website and LinkedIn publication operations;
- the enriched UCR course database — UCR course evidence and availability;
- `data/registry/` — normalized counselor identity, production order, provenance and programme-interest discovery data;
- repository schemas and validators — executable data contracts and mechanical record checks;
- GitHub repository state, Actions and commit history — implementation state and build mechanics;
- **UCR Pathways Supporting Research Workflows** — programme-interest enrichment and synthetic-interest work only, not routine student/counselor academic production.

A rule should be stated in the document that owns it rather than repeated across documents. A batch assignment may invoke authoritative instructions but must not redefine them.

---

# 1. Project identity and four-surface architecture

## 1.1 UCR Pathways is the internal project name

**UCR Pathways** remains the internal project name and the name of the GitHub repository.

It is **not** a user-facing product or sub-brand. Student-facing, counselor-facing and public interfaces must use UCR branding without displaying `UCR Pathways`, `Pathways` or equivalent project identifiers as a visible product identity.

Technical repository paths and internal identifiers may continue to contain `ucr-pathways` where changing them would add no user value.

## 1.2 Four user/public surfaces

The project supports four distinct surfaces that share academic comparison content but serve different purposes:

1. **Student app** — a personalized experience generated from an actual prospective student's submitted interests.
2. **Counselor app** — a deterministic searchable library of pre-produced comparisons, one per normalized counselor programme target in the current production scope.
3. **Public website** — a curated communication and showcase layer, not an exhaustive comparison database.
4. **LinkedIn** — an editorial distribution channel using selected approved comparisons and stories.

The website and LinkedIn are downstream communication surfaces. They do not regenerate academic content.

## 1.3 UCR Program Builder

The **UCR Program Builder** is a separate downstream experience in which a prospective student can build or modify a programme.

Canonical destination:

`https://program.ucr.nl/`

Do not imply that a displayed programme transfers automatically into the Program Builder unless that functionality has actually been implemented.

---

# 2. Core comparison model

The project should make curriculum choices and trade-offs visible rather than explain Liberal Arts and Sciences primarily in abstract language.

Every comparison contains:

1. exactly one `comparator` — one external Dutch bachelor programme; and
2. between **one and three UCR alternatives**.

The UCR alternatives are ordered from the closest feasible response to progressively broader alternatives where such broader alternatives are genuinely defensible. The first UCR alternative is the closest feasible match. A second or third alternative is included only when it represents another coherent, evidence-backed and substantively distinct way of pursuing the relevant field, interests, question or application at UCR.

There is **no requirement to reach three UCR alternatives**. Three is the maximum, not a quota. Do not manufacture additional interests, domains, questions or curricular differences merely to fill a fixed number of programme slots. One strong alternative is preferable to one strong alternative plus weak or redundant ones.

Concepts such as **closest match**, **related direction** and **question-led/thematic programme** remain useful analytical types, but they are not mandatory programme roles and not every record must instantiate all three types.

Neither the external bachelor nor UCR should be presented as inherently superior. Genuine strengths of the external programme and genuine limitations of UCR must remain visible.

## 2.1 Visible programme labels

Use ordinary, case-specific labels rather than internal taxonomy.

- comparator: **[Programme] at [Institution]**;
- first UCR alternative: normally **Closest match to [programme or field]** or another accurate case-specific label;
- additional UCR alternatives: descriptive labels that state the actual direction, combination, question or application represented.

Do not expose internal implementation names such as `ucr-alternative`, `closest-match`, `related-direction` or `question-led` as user-facing product taxonomy unless a later design decision explicitly does so.

The comparator heading or an adjacent clear source link should lead to the approved official programme/curriculum source.

---

# 3. Student app

## 3.1 Input and generation model

The student app is **organic and personalized**. It is generated from actual prospective-student input received through the approved intake route.

The standard question remains:

**“What are your interests?”**

The answer may contain disciplines, topics, questions, problems, practical interests, skills or phenomena in any combination.

Production must preserve the student's original wording, interpret it academically, avoid assuming that the first-mentioned interest is more important, and avoid manufacturing weak curricular matches. For a student who supplies one interest, broaden through meaningful subfields, questions and neighbouring perspectives rather than inventing a second interest.

The student's full submitted interest statement is valid evidence for constructing and differentiating UCR alternatives. Where a student supplies several interests, alternatives may legitimately vary their relative emphasis or organise them differently. Where the input supports only one defensible programme, do not invent additional alternatives.

## 3.2 Student app journey

The student experience should begin with a personalized welcome screen showing both:

> **You told us that…**
>
> [student's original wording]

and:

> **For us, this means that…**
>
> [concise academic interpretation]

The welcome screen should provide access to two views of the same approved personalized record:

- **View my personalized programme options** — semester-by-semester views of every included UCR alternative, in record order;
- **See how these options compare** — the external comparator alongside the same one to three UCR alternatives.

The interface must not promise a fixed number of UCR options. Appropriate framing is that these are the UCR programmes that best fit what the student told us.

## 3.3 Student calls to action

After the substantive programme content, provide two distinct next steps where supported:

- **Speak to Admissions** — to the approved Admissions contact or booking route;
- **Tweak this programme to your liking** — to the canonical UCR Program Builder destination.

Exact Admissions destination is implementation/configuration data.

## 3.4 Student disclaimer

Each personalized programme option must carry an approved disclaimer explaining its illustrative status and the relevance of actual curriculum rules and course availability.

Until the approved text from the printed butterfly is supplied, use the explicit placeholder:

> **[PLACEHOLDER — insert approved student-program disclaimer from the printed butterfly.]**

The placeholder must be visibly distinguishable in development and must not be mistaken for approved final copy.

## 3.5 Student privacy and access

Names and unnecessary personal information remain outside academic pathway records.

Student-specific access codes or links must not expose private pathway records through a public code-to-record mapping. A student case is not automatically approved for public website or LinkedIn use.

---

# 4. Counselor app

## 4.1 Deterministic corpus and current production scope

The counselor app is **deterministic**, not a live personalization engine.

Produce one fixed comparison for every normalized counselor programme target in the current production scope. A target is currently in scope only when `data/registry/programmes.csv` shows:

- `production_eligible=true`;
- nonblank `production_order`; and
- `programme_type=standard`.

Targets with `programme_type=joint-degree`, `double-bachelor` or `dual-degree-route` remain legitimate normalized registry targets but are temporarily excluded from comparison production until an approved presentation method exists. Do not change their permanent identity, lifecycle fields, institutions or normalization decisions merely to implement this presentation-scope exclusion.

The permanent production identity is `counselor_programme_id`. Source worksheet rows, offered-programme UUIDs, programme-unit codes, recognized-programme codes, language, mode and campus registrations are provenance/join information rather than independent counselor comparison identities.

Permanent counselor target IDs must be preserved across later registry refreshes. Production proceeds in `production_order` after applying the current scope filter; do not prioritize by UCR fit, popularity or marketing value.

## 4.2 Two discovery routes, one comparison library

The counselor may discover the same fixed comparison through either programme identity or student-facing interests associated with programmes in the programme-interest data.

Use one search experience where practical:

> **Search by programme or interest**

Interest search is a discovery mechanism only. Entering an interest does not regenerate or personalize the selected comparison.

## 4.3 Interest-search ranking

Use `interest_relationship` as the principal evidence distinction for deterministic search ranking:

1. direct programme interest;
2. stable study direction;
3. curricular topic;
4. illustrative or temporary topic;
5. outcome or individual trajectory.

Categories 1–2 form the conservative core; category 3 may broaden discovery; categories 4–5 should receive lower confidence/priority.

Where `target_mapping_status=inherited-across-split-targets`, the inherited interest record is provenance/general discovery evidence only. It is not target-specific academic evidence unless independently corroborated for that exact normalized target.

## 4.4 Counselor alternatives and transparency

A counselor comparison contains the comparator plus one to three UCR alternatives under the common architecture in Section 2.

The external programme and valid target-specific programme-interest evidence establish the evidence boundary. They may justify neighbouring directions or broader questions, but they do not justify assuming that an imagined student has unrelated additional interests.

The interface must explain that comparisons are pre-produced at normalized target level, interest search does not personalize them, and UCR programmes are illustrative feasible compositions rather than official tracks or guaranteed future schedules. It should not imply that every comparison contains the same number of UCR alternatives.

---

# 5. Durable academic comparison principles

Detailed execution belongs exclusively to the **Production Instructions**. The durable principles are:

## 5.1 External programme fairness

Reconstruct comparators from current official university evidence. Represent compulsory, restricted-choice, route/specialization, open-elective, methods/research, thesis/capstone and EC structure fairly. Where choices must be instantiated, use one coherent valid pathway.

Never present optional material as compulsory, combine mutually exclusive choices, invent components, violate programme rules, deliberately choose weak options to favour UCR, or make the external programme artificially narrow.

## 5.2 UCR feasibility

Use the enriched UCR course database as the authoritative source for course content, prerequisites and planned semester availability.

Each included UCR programme must contain exactly 24 unique courses, four courses in each of six semesters, at least six 300-level courses, and Personal & Professional Development during Year 1. Prerequisites must precede dependent courses and every course must be available in its assigned semester.

Do not invent additional cluster, unit, concentration, breadth or disciplinary-distribution requirements. Validate mechanical feasibility against the enriched database.

## 5.3 Alternative-selection integrity

Construct the closest feasible UCR alternative first. Consider additional alternatives sequentially. Include another alternative only when it passes all four tests:

1. **evidence** — its organising basis is supported by the applicable evidence boundary;
2. **coherence** — it is a coherent programme concept rather than an assortment of attractive courses;
3. **distinctness** — it represents a substantively different educational choice rather than cosmetic reshuffling;
4. **feasibility** — it can be built as a valid UCR programme under Section 5.2.

Stop when the next alternative cannot pass these tests. Do not skip a failed second alternative in order to manufacture a third. Record-level production rules must make the stopping decision auditable.

## 5.4 Comparison integrity

Construct and validate the comparator and every included UCR programme before designing comparison blocks. Use actual content rather than titles alone and preserve actual EC weights.

The comparison is a **lossless 180-EC representation of each completed programme**, organised into meaningful substantive blocks. Every included UCR course must appear exactly once in the comparison, including Personal & Professional Development. The external programme must likewise account for its complete 180 EC; genuine open-elective, profiling or restricted-choice space must be represented explicitly rather than disappearing from the comparison.

Blocks classify and align programme components; they do not replace them with selective summaries. Preserve meaningful blank cells and structural differences, and do not force row-by-row symmetry, equal block sizes, identical credit allocations or one-to-one course equivalence. The number and size of blocks should follow the curricula rather than a fixed template. Do not use numerical depth/breadth scores.

Detailed block construction, stable component references and anti-template checks belong to the Production Instructions and executable validators.

---

# 6. Explanatory notes and canonical records

Explanatory notes should use reusable semantic templates defined in the Production Instructions and appear only when needed to prevent a material misunderstanding. A warranted limitation note must remain visible across representations.

Create one canonical structured comparison record before rendering any surface. The record must identify its origin (`student` or `counselor`) and preserve the comparator identity, between one and three ordered UCR alternative identities, complete UCR schedules, the complete reconstructed comparator curriculum, comparator evidence, lossless comparison structure, deliberate gaps, credits, validation status and source/verification metadata.

Student-origin records additionally preserve the original interest statement and academic interpretation.

Counselor-origin records additionally preserve the permanent `counselor_programme_id`, normalized provenance required to audit the target and connect it to programme-interest discovery, and the evidence/rationale supporting each included UCR alternative and the decision to stop before three where applicable. Under the current counselor contract, the stable record `id` equals the same permanent `counselor_programme_id`.

Canonical records contain semantic content, not renderer coordinates, CSS or page geometry. Renderers may ignore fields they do not need, but they must not reinterpret or invent programme facts.

---

# 7. Public website

The public website is a **curated communication and showcase layer**, not the exhaustive counselor database and not the private student app.

It should:

- use UCR branding without visible Pathways branding;
- present a deliberately selected set of examples or stories;
- explain programme possibilities through concrete comparisons rather than an exhaustive catalogue;
- provide clear routes toward the student experience, counselor tool and Program Builder where appropriate.

Most public examples will normally be selected from approved counselor comparisons because they are stable and privacy-safe. A student-origin case may be used only after explicit public-use approval and removal of identifying information.

Programme-specific content must come from approved structured publication records rather than being hardcoded into the renderer. A public example retains the same comparator plus one-to-three-UCR-alternative architecture as its approved source record; public presentation must not invent extra alternatives to fill a layout.

---

# 8. LinkedIn

LinkedIn is an editorial distribution channel, not a separate academic source.

Use selected approved publication records from the counselor corpus or an explicitly approved privacy-safe student case. When website and LinkedIn present the same case, both should consume the same approved public programme content.

Editorial framing belongs in LinkedIn commentary rather than in a second hand-edited academic-content copy. LinkedIn may omit the comparator page as an editorial presentation choice, but it must not add, remove or substitute UCR alternatives relative to the approved public record.

Existing editorial scenarios may continue, including:

- the degree that does not exist;
- what do you have to give up?;
- start with the question;
- same interest, surprisingly different programmes;
- findings from the Dutch bachelor market.

Publication remains human-controlled unless a later decision explicitly changes that rule.

---

# 9. Public curation and privacy

Neither the student app nor the counselor app automatically publishes a case.

A comparison becomes public only after substantive human review, explicit approval for public use, and creation of a publication-safe record conforming to the current repository contract.

Do not maintain separate hand-edited programme-content copies for website and LinkedIn.

---

# 10. Optional event/PDF outputs

Existing Open Day and other PDF renderers may continue to use canonical academic records where useful. They are output formats, not separate academic products, and must not force separate programme-content copies or a fixed number of UCR alternatives.

---

# 11. Visual identity

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

Use colour primarily for identity, navigation and orientation rather than as the main substantive classification of courses. Use the UCR logo without redundant institutional naming beside it. Keep text readable against its actual background, including link, visited, hover, selected and keyboard-focus states, and check narrow screens and enlarged text.

If required brand fonts are unavailable, treat that as a rendering limitation to fix or report rather than silently inventing a different visual identity.

---

# 12. Document ownership and implementation boundary

Maintain three **authoritative** project documents:

1. **Master Specification** — durable product, academic, content and architectural decisions.
2. **Production Instructions** — the single authoritative procedure for academic generation, validation and record creation for student and counselor workflows.
3. **Web and LinkedIn Workflow** — operational public curation, website and LinkedIn publication workflow.

Maintain **UCR Pathways Supporting Research Workflows** as a supporting reference for programme-interest enrichment and synthetic-interest work. It is not part of the routine context for student or counselor comparison production.

`Counselor_Batch_Assignment.md` is an execution wrapper. It selects and runs a batch under the Production Instructions; it must not duplicate or redefine academic methodology.

Exact schema fields, storage paths, search implementation, Shiny code, hosting choice and deployment commands belong to repository implementation unless a durable architectural decision explicitly promotes them into this specification. **Shiny/Shinylive remains an implementation candidate, not an authoritative product requirement.**

If wording conflicts across layers, resolve it according to ownership: this Master governs durable product decisions; Production Instructions govern academic generation; Web and LinkedIn Workflow governs public publication; schemas/validators govern executable data contracts; batch assignments cannot override those sources unless the user explicitly changes the underlying decision.

Do not use authoritative documents to record successful or failed runs, temporary bugs, deployment status or routine next steps.