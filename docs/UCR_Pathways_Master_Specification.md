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

The relationship between those elements differs by workflow:

- **Student records:** UCR programmes are generated directly from the student's submitted interests and academic interpretation. The external bachelor is selected as a useful point of comparison only after the UCR programme concepts have been established. It is not the generating reference point, and the first UCR programme is not defined as the closest match to that comparator. The UCR programmes are ordered as needed for clear presentation.
- **Counselor records:** the external bachelor is the explicit production target. The first UCR alternative is therefore the closest feasible UCR response to that target, with any additional alternatives constructed from valid target-specific evidence.

Any second or third UCR programme is an additional defensible response with a genuinely different organising logic; it may be narrower, thematic, question-led, application-led or otherwise differently organised, and it does not need to be broader than the preceding programme. Include it only when it represents another coherent, evidence-backed and substantively distinct way of pursuing the applicable field, interests, question or application at UCR.

There is **no requirement to reach three UCR alternatives**. Three is the maximum, not a quota. Do not manufacture additional interests, domains, questions or curricular differences merely to fill a fixed number of programme slots. One strong alternative is preferable to one strong alternative plus weak or redundant ones.

Concepts such as **closest match**, **related direction** and **question-led/thematic programme** remain useful analytical types in the contexts where they apply, but they are not mandatory programme roles and not every record must instantiate all three types. Comparator-relative closest-match logic applies to counselor production, not to student programme generation.

Neither the external bachelor nor UCR should be presented as inherently superior. Genuine strengths of the external programme and genuine limitations of UCR must remain visible.

## 2.1 Visible programme labels

Use ordinary, case-specific labels rather than internal taxonomy.

- comparator: **[Programme] at [Institution]**;
- student UCR programmes: descriptive titles that name the actual programme direction and the particular way it responds to the student's interests; do not label the first programme as a closest match to the external comparator or define later programmes as progressively broader versions of it;
- counselor first UCR alternative: normally **Closest match to [programme or field]** or another accurate case-specific label;
- counselor additional UCR alternatives: descriptive labels that state the actual direction, combination, question or application represented.

Do not expose internal implementation names such as `ucr-alternative`, `closest-match`, `related-direction` or `question-led` as user-facing product taxonomy unless a later design decision explicitly does so.

For every UCR alternative, distinguish the **generating concept** from the **visible programme label**. The concept records why the alternative was constructed. Assign the final visible label only after the complete UCR curriculum has been built and validated. The label must describe the actual curricular composition broadly enough that it does not present one strand as though it defined the whole programme.

The comparator heading or an adjacent clear source link should lead to the approved official programme/curriculum source.

---

# 3. Student app

## 3.1 Input and generation model

The student app is **organic and personalized**. It is generated from actual prospective-student input received through the approved intake route.

The standard question remains:

**“What are your interests?”**

The answer may contain disciplines, topics, questions, problems, practical interests, skills or phenomena in any combination.

Production must preserve the student's original wording, interpret it academically, avoid assuming that the first-mentioned interest is more important, and avoid manufacturing weak curricular matches. For a student who supplies one interest, broaden through meaningful subfields, questions and neighbouring perspectives rather than inventing a second interest.

The student's full submitted interest statement is valid evidence for constructing and differentiating UCR programmes. Where a student supplies several interests, programmes may legitimately vary their relative emphasis or organise them differently. Where the input supports only one defensible programme, do not invent additional programmes. Select the external Dutch bachelor later as a useful comparison point; do not use it to generate or name the student's UCR programmes.

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

- **Explore my UCR programme/programmes** — dynamically singular or plural, with semester-by-semester views of every included UCR programme in record order;
- **Compare with a Dutch bachelor** — the external comparator alongside the same one to three UCR programmes.

The interface must not promise a fixed number of UCR programmes. Its singular/plural wording must adapt to the record without adding a heading that states how many programmes were prepared.

In the programme view, every UCR programme displays its canonical programme concept immediately below its title and before its six-semester schedule. The concept serves as a concise description of the programme's organising academic combination or emphasis and its response to the student's interests; it is not a separate renderer-specific description field.

On narrow screens, each programme schedule must provide a direct route back to the programme selector when the record contains more than one UCR programme. The comparison view must show one complete programme column at a time, with touch-swipe navigation and visible previous/next and position controls. Wider screens retain the full side-by-side comparison.

Student-app interface copy written within the application uses American spelling, apart from any deliberately retained call-to-action label. Text supplied by canonical records, the course database or other source data remains unchanged.

## 3.3 Student calls to action

Near the top of the student record, before the interest summary and substantive programme content, provide two distinct next steps where supported:

- **Speak to Admissions** — to the approved Admissions contact or booking route;
- **Build your own UCR program** — to the canonical UCR Program Builder destination, without implying that a displayed programme transfers automatically.

Exact Admissions destination is implementation/configuration data.

## 3.4 Student disclaimer

Each personalized programme option must carry an approved disclaimer explaining its illustrative status and the relevance of actual curriculum rules and course availability.

Use the following approved text:

> We’ve done our best to make sure this program is as complete and accurate a match to your interests as possible. But since our curriculum is as flexible and responsive as our students, things may change after you read this. By the time you start building your program online (or in Middelburg), some courses may have shifted, been added, or taken a well-deserved break. In short: things change and no rights may be derived from this document.

## 3.5 Student privacy and access

Names and unnecessary personal information remain outside academic pathway records.

Student-specific access codes or links must not expose private pathway records through a public code-to-record mapping. A student case is not automatically approved for public website or LinkedIn use.

GitHub contains no real student data. Completed records, access codes and code-to-record mappings belong in the ignored local `/private/` tree and the server-side shinyapps.io deployment bundle. Operators place completed records directly in `/private/student-records/`; the registration workflow validates and indexes new files before deployment. The public examples and their development codes remain tracked test fixtures and are not real student data.

The student app uses one cumulative private production dataset and one shinyapps.io application, `ucr-student`. Registering one or more completed student records adds one validated record and one new unique access mapping per student while preserving all existing records and codes. Registration does not deploy the app: operators may accumulate several batches locally and deploy the complete dataset once when ready. A student's code is generated once and remains stable across later registrations and redeployments. `student-access.json` remains the authoritative machine-readable index; the operator-facing private CSV is regenerated as a complete cumulative record-ID/code mapping after every registration. After a valid code is entered, the app renders only the corresponding record.

shinyapps.io is the approved deployment target for this private workflow. The local cumulative `/private/` dataset is the authoritative operational copy and requires secure institutional backup; backup design and automation remain outside the application repository.

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

The counselor interface and its discovery search operate in **English**. Every normalized counselor target must have a nonblank `display_name_en` in `data/registry/programmes.csv`; this is the user-facing programme name used for counselor display and programme-name search. `canonical_name` and aliases remain provenance/normalization data and must not be exposed or indexed merely to provide Dutch-language programme search. Teaching language remains separate metadata and may of course be Dutch.

Student-facing programme interests used for counselor discovery must likewise be in English.

Use one search experience where practical:

> **Search in English by programme or interest**

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

For counselor programme construction, programme-interest evidence is stricter than discovery search. All target-linked programme-interest rows must be assessed. `Direct programme interest` and `Stable study direction` rows may generate candidate directions; `Curricular topic` rows may support but not independently generate a direction; `Illustrative or temporary topic` and `Outcome or individual trajectory` rows remain discovery evidence and do not generate UCR alternatives. Eligible interests must be considered as evidence-backed substantive directions rather than selected ad hoc as isolated rows. Generator-eligible interests must not be placed in an omnibus residual category merely to prove that they were considered: each must either be substantively covered by the core/closest-match concept or belong to a genuinely coherent candidate direction.

## 4.4 Counselor alternatives and transparency

A counselor comparison contains the comparator plus one to three UCR alternatives under the common architecture in Section 2.

The external programme and valid target-specific programme-interest evidence establish the evidence boundary. They may justify neighbouring directions or broader questions, but they do not justify assuming that an imagined student has unrelated additional interests.

The interface must explain that comparisons are pre-produced at normalized target level, interest search does not personalize them, and UCR programmes are illustrative feasible compositions rather than official tracks or guaranteed future schedules. It should not imply that every comparison contains the same number of UCR alternatives.

---

# 5. Durable academic comparison principles

Detailed execution belongs exclusively to the **Production Instructions**. The durable principles are:

## 5.1 External programme fairness

Reconstruct comparators from current official university evidence. Represent compulsory, restricted-choice, route/specialization, open-elective, methods/research, thesis/capstone and EC structure fairly. Where choices must be instantiated, use one coherent valid pathway.

When a generic programme target contains several formal routes and one route must be instantiated, select the route that best represents the programme's broad academic identity. If no route is clearly more representative, use the least specialized or most general route available under the official curriculum. Never choose a route because it happens to improve the apparent UCR match. Preserve the selected route and the basis for the choice in the academic record when it materially shapes the comparator.

Never present optional material as compulsory, combine mutually exclusive choices, invent components, violate programme rules, deliberately choose weak options to favour UCR, or make the external programme artificially narrow.

## 5.2 UCR feasibility

Use the enriched UCR course database as the authoritative source for course content, prerequisites and planned semester availability.

Each included UCR programme must contain exactly 24 unique courses, four courses in each of six semesters, at least six 300-level courses, and Personal & Professional Development during Year 1. Prerequisites must precede dependent courses and every course must be available in its assigned semester.

For course sequencing, formal prerequisites and planned semester availability are hard constraints. Other progression signals in the course evidence, such as language that a course builds on or assumes earlier study, are advisory. Prefer to place relevant foundational study before advanced work that clearly builds on it when the formal constraints and programme concept allow, but do not reject or rebuild an otherwise valid programme merely because another academically reasonable sequence might be preferable. This reflects UCR's open curriculum: where no formal prerequisite exists, alternative sequencing is permitted within the remaining formal constraints.

Do not invent additional cluster, unit, concentration, breadth or disciplinary-distribution requirements. Validate mechanical feasibility against the enriched database.

## 5.3 Alternative-selection integrity

For a student record, construct the first UCR programme directly from the student's interpreted interests, without using the external comparator as its generating reference. For a counselor record, construct the closest feasible UCR alternative to the external target first. In both workflows, consider additional alternatives sequentially and include another only when it passes all four tests:

1. **evidence** — its organising basis is supported by the applicable evidence boundary;
2. **coherence** — it is a coherent programme concept rather than an assortment of attractive courses;
3. **distinctness** — it represents a substantively different educational choice rather than cosmetic reshuffling;
4. **feasibility** — it can be built as a valid UCR programme under Section 5.2.

Stop when the next alternative cannot pass these tests. Do not skip a failed second alternative in order to manufacture a third. Record-level production rules must make the stopping decision auditable.

## 5.4 Comparison integrity

Construct and validate the comparator and every included UCR programme before designing comparison blocks. Use actual content rather than titles alone and preserve actual EC weights.

The academic comparison is a **lossless 180-EC representation of each completed programme**, organised into meaningful substantive blocks. Every included UCR course must appear exactly once in the comparison, including Personal & Professional Development. The external programme must likewise account for its complete 180 EC; genuine open-elective, profiling or restricted-choice space must be represented explicitly rather than disappearing from the comparison.

In addition to that 180-EC academic representation, every UCR alternative must display one standardized comparison-only opportunity: **Optional independent research — 15 EC**. This element is not one of the 24 scheduled UCR courses, is not included in the six-semester schedule, and does not count toward the displayed programme's 180 EC. Where the comparator contains an identifiable bachelor thesis, capstone, research project or equivalent independent-research component, show the UCR optional-research element in parallel with that comparator component. Where the comparator contains no such component, place the optional-research element in the same substantive block as Personal & Professional Development. The enriched UCR course database must not contain this comparison-only element.

Blocks classify and align programme components; they do not replace them with selective summaries. Preserve meaningful blank cells and structural differences, and do not force row-by-row symmetry, equal block sizes, identical credit allocations or one-to-one course equivalence. The number and size of blocks should follow the curricula rather than a fixed template. Do not use numerical depth/breadth scores.

Within one comparison, **exact UCR course identity is the only basis for sharing a UCR comparison row**. A UCR course code has one canonical row and one canonical block. Every included UCR alternative containing that exact code populates that row; alternatives not containing it remain blank. Different UCR course codes occupy different rows even when their content is closely related. This identity rule does not require symmetry between different courses or between UCR and the external comparator.

After the canonical UCR rows are fixed, place each external comparator component independently according to a **meaningful curricular relationship**. Co-location in a row does not assert full equivalence: a UCR course may align when it directly addresses an important and identifiable part of the comparator component's subject, disciplinary method or specific educational function, even if it does not reproduce the component's full scope, level or disciplinary framing. For a broad integrated comparator component that cannot defensibly be divided into separately credited elements, alignment with the strongest directly relevant UCR course is acceptable when the relationship independently meets this standard and the rationale makes the difference in scope clear. Being the strongest available course is not by itself sufficient. Preserve a blank where the relationship is merely contextual, incidental, generally useful background, based mainly on title similarity or grounded only in a generic transferable method or function.

Detailed block construction, stable component references and anti-template checks belong to the Production Instructions and executable validators.

---

# 6. Explanatory notes and canonical records

Explanatory notes should use reusable semantic templates defined in the Production Instructions and appear only when needed to prevent a material misunderstanding. A warranted limitation note must remain visible across representations.

Create one canonical structured comparison record before rendering any surface. The record must identify its origin (`student` or `counselor`) and preserve the comparator identity, between one and three ordered UCR alternative identities, complete UCR schedules, the complete reconstructed comparator curriculum, comparator evidence, lossless comparison structure, deliberate gaps, credits, validation status and source/verification metadata.

Student-origin records additionally preserve the original interest statement and academic interpretation.

Counselor-origin records additionally preserve the permanent `counselor_programme_id`, normalized provenance required to audit the target and connect it to programme-interest discovery, the evidence/rationale supporting each included UCR alternative and the decision to stop before three where applicable, and enough course-level traceability to audit why every non-PPD UCR course belongs to its generating concept. Under the current counselor contract, the stable record `id` equals the same permanent `counselor_programme_id`.

Counselor production uses a two-stage record architecture. ChatGPT makes and records the academic decisions explicitly in a compact decision file. A deterministic compiler then adds only mechanically derivable registry, programme-interest, schedule and comparison scaffolding. Existing validators must pass before GitHub Actions publishes the canonical comparison. The compiler must not select courses, schedule them, define alternatives, name programmes, assign substantive blocks or decide comparator matches. A failed compilation or validation produces no canonical comparison, and production never overwrites a completed canonical record.

The active counselor decision contract is `decisionSchemaVersion: "2.0"`; compiled canonical counselor records remain `schemaVersion: "2.0"`. Decision schema v2 uses compact source tokens, programme-interest row references, tuple-form verified course facts, explicit semester groups, shared course-to-basis traceability with explicit overrides, and compact block-row assignments. The v1 compiler and regression fixtures remain available only as a temporary fallback and regression reference until v2 has succeeded on a new production target.

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

Exact schema fields, storage paths, search implementation and deployment commands belong to repository implementation unless a durable architectural decision explicitly promotes them into this specification. For the private student workflow, Section 3.5 records the current durable hosting decision: the approved architecture is the server-side Shiny app on shinyapps.io under the fixed application name `ucr-student`. Shinylive is not an approved private-data deployment architecture.

## 12.1 Human handoff for tool limitations

When a required repository or file operation cannot be completed safely and directly with the available tools, ChatGPT must not keep improvising increasingly fragile workarounds. It must stop and request the smallest specific human action needed to unblock the workflow.

Human escalation is mandatory when any of the following applies:

- an exact file must be preserved but the available tools cannot reliably download, edit or upload it without reconstruction risk;
- the operation would require reconstructing a large or complex file from partial responses;
- an integrity, hash or equivalent validation check fails;
- the required repository action is unavailable through the active connector or toolset;
- two reasonable attempts at the same repository or file operation fail; or
- a short human action would materially reduce the risk or complexity compared with continued automated workaround attempts.

The first integrity failure or the second failed attempt at the same operation is a mandatory stop-and-escalate point. Human assistance is a normal part of the workflow, not a failure state.

A handoff request must state exactly:

1. what ChatGPT cannot safely complete;
2. why continuing automatically is risky;
3. the minimum action the user needs to perform; and
4. what ChatGPT will verify and continue doing after the handoff.

After the user completes the requested action, ChatGPT must verify the resulting repository or file state before continuing.

If wording conflicts across layers, resolve it according to ownership: this Master governs durable product decisions; Production Instructions govern academic generation; Web and LinkedIn Workflow governs public publication; schemas/validators govern executable data contracts; batch assignments cannot override those sources unless the user explicitly changes the underlying decision.

Do not use authoritative documents to record successful or failed runs, temporary bugs, deployment status or routine next steps.
