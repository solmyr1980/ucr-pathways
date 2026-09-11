# UCR Pathways — Colleague feedback archive (September 2026)

**Status:** Historical source/provenance record — non-authoritative

## Purpose and provenance

This file preserves the colleague feedback that informed the September 2026 redesign of UCR Pathways and records the decisions taken in response.

It is **not** a fourth specification and must not be used as a substitute for the current authoritative documents:

- `docs/UCR_Pathways_Master_Specification.md`
- `docs/UCR_Pathways_Production_Instructions.md`
- `docs/UCR_Pathways_Web_LinkedIn_Workflow.md`

On 11 September 2026, Alexei supplied the underlying colleague feedback text directly in the project conversation. It is now preserved separately as verbatim source material:

- `docs/source-feedback/2026-09-etienne-feedback-verbatim.txt` — signed by Etienne;
- `docs/source-feedback/2026-09-gerda-feedback-verbatim.txt` — the second feedback block, archived under Gerda because this feedback had already been attributed to Gerda in the project discussion.

The verbatim files preserve the supplied wording, spelling, punctuation and formatting quirks rather than silently correcting them. The summaries and decision mappings below are **project interpretations** of those source texts. Where there is any question about what a colleague actually wrote, consult the verbatim file. Where there is any question about the current project rule, consult the authoritative specifications.

---

# 1. Etienne — counselor-facing interface feedback

Feedback recorded in the project discussion:

- The counselor interface should visually resemble the UCR homepage more closely.
- Use a strong UCR visual identity, including a thick plum bar and the UCR logo at the top left.
- Remove the duplicated `University College Roosevelt` text next to/under the logo.
- Use a heading along the lines of: **“See how the UCR program compares to other bachelor's programs.”**
- The interface should provide access to the whole set of bachelor programmes.
- Filtering could include dimensions such as discipline, location, university and BSc/BA.
- Selecting a degree should open a comparison between that external degree and three UCR alternatives.

## Project decision

**Accepted / modified.**

Accepted:

- UCR branding rather than a separate Pathways visual identity;
- UCR logo and UCR-style visual treatment;
- removal of duplicated institutional naming;
- access to the full counselor corpus;
- programme selection leading to one external programme plus three UCR alternatives;
- filters where supported reliably by the registry.

Modified:

- The counselor tool is not limited to programme-first navigation. It uses one discovery experience that supports both **programme search and interest search**.
- Interest search resolves to a programme-provider record and then loads its fixed, pre-produced comparison. It does **not** generate a personalized comparison.
- The eventual heading/copy should explain the comparison function in ordinary language without making `UCR Pathways` a visible product identity.

Current authoritative location: Master Specification, sections 1, 2 and 4.

---

# 2. Etienne — student-facing interface feedback

Feedback recorded in the project discussion:

- The interface should use UCR branding and could remove visible UCR Pathways branding.
- Suggested welcome language included: **“We are happy to share your personalized program options.”**
- Show the student's original input together with an academic interpretation.
- Explain that, based on the interests, a possible UCR programme has been prepared.
- Offer a route to view the personalized programme and a route to compare it.
- Suggested fixed labels for the UCR options included language such as **“strong match”** and similar conversational judgments.
- Include calls to action for Admissions and the UCR Program Builder.

## Project decision

**Mostly accepted, with one important rejection.**

Accepted:

- UCR branding without visible Pathways branding;
- a personalized welcome stage;
- preservation of both the student's original wording and a separate academic interpretation;
- personalized programme first, with access to the comparison view;
- Admissions and Program Builder calls to action.

Rejected / superseded:

- Fixed evaluative labels such as **“strong match”** were rejected in favour of case-specific descriptive labels derived from Gerda's feedback.

Current authoritative location: Master Specification, sections 1, 2 and 3.

---

# 3. Gerda — student-facing comparison feedback

Feedback recorded in the project discussion:

- Suggested heading: **“See how your interests compare with study options at UCR.”**
- Preserve/show the student's original interests.
- Avoid unnecessary example-specific explanatory text about the external reference programme.
- Remove the visible label **“Reference programme.”**
- Show the actual external bachelor and institution directly.
- The first UCR programme should be the closest match, while the other UCR programmes should become progressively broader.
- Use **case-specific descriptive titles** for the UCR programmes rather than fixed generic judgments.
- Add a link to relevant UCR curriculum information.
- Suggested adding a research-seminar element.
- Suggested mentioning exchange possibilities through Utrecht University.
- Where comparator components show ECs, show ECs on the UCR side as well.
- Raised the issue of elective/open space in the comparison.

Examples of the case-specific title style subsequently discussed:

- **“Closest match to Astronomy”**
- **“Astronomy + related subjects”**
- **“A broader programme around your interests”**

## Project decision

**Accepted selectively.**

Accepted:

- preserve/show original student interests;
- remove the visible `Reference programme` label;
- identify the external comparator directly as programme + institution;
- preserve a link to the external programme's official page;
- use case-specific descriptive UCR titles;
- first UCR option = closest feasible match, followed by broader alternatives;
- add UCR curriculum links;
- display EC credits consistently on the external and UCR sides.

Rejected / explicitly not adopted:

- do **not** introduce research-seminar callouts merely to fill comparison gaps;
- do **not** add exchange possibilities as a comparison device;
- do **not** create a new special elective-space treatment or symmetry rule.

Current authoritative location: Master Specification, sections 2, 3, 5, 7 and 7.1; Production Instructions, sections 1 and 9.

---

# 4. Gerda — counselor-facing feedback

Feedback recorded in the project discussion:

- Frame the counselor experience around the student's interests/person rather than only a catalogue of degree names.
- Use interests as a way to help counselors find relevant study options.
- The feedback supported exploring programme comparisons from a counselor/student-interest perspective rather than relying only on a conventional programme list.

## Project decision

**Partially accepted and structurally modified.**

Accepted:

- counselor discovery should support student-facing interests;
- interest language should be a genuine route into the tool rather than an afterthought.

Modified:

- the counselor tool does **not** dynamically build a personalized comparison from the counselor's interest query;
- interests are a discovery/indexing layer over the deterministic programme-provider corpus;
- once a programme-provider record is selected, the displayed comparison is the same fixed pre-produced comparison regardless of which query led to it;
- programme-name search and interest search coexist in one search experience.

Current authoritative location: Master Specification, section 4; Production Instructions, sections 3 and 4.

---

# 5. Feedback on example comparisons and explanatory notes

During review of specific examples, the following substantive concerns were recorded.

## UvA / elective space

Feedback highlighted the presence of a 30-EC elective/open component and the visual effect of blank comparison cells.

### Project decision

Do not create a new elective-space symmetry rule. Preserve genuinely open space and meaningful gaps rather than filling them for visual balance.

## Erasmus Criminology

The comparison raised the problem that the external programme combines criminology with law, sociology, psychology and empirical methods, while UCR has much less explicit crime-focused curricular depth. A broader UCR programme may approach the same problem through related disciplines without reproducing a full criminology curriculum.

### Project decision

Use this as the model for the reusable explanatory-note type later named `related-fields-not-full-discipline`.

## Utrecht Mathematics / Climate-type comparison

The external curriculum offered more proof-based mathematics and specialist climate/fluid-dynamics depth, while UCR could combine quantitative methods, climate science, Earth systems, technology, governance and projects without reproducing the same specialist sequence.

### Project decision

Use this kind of case to explain genuine differences in specialist depth rather than presenting breadth as equivalent depth. This informed the reusable note types `less-disciplinary-depth` and `missing-specialist-components`.

Current authoritative location: Production Instructions, section 10.

---

# 6. Corpus scope and production-order feedback

A suggestion was discussed to prioritize cases with the strongest UCR fit and/or the fewest blank cells.

## Project decision

**Rejected.**

The counselor corpus is produced at **programme-provider level** for the full approved registry scope, in the **existing worksheet order**, with **no prioritization** by UCR fit, blank-cell count, popularity, institution, discipline or marketing value.

Current authoritative location: Master Specification, section 4.1; Production Instructions, section 3.1.

---

# 7. Consolidated decision table

| Feedback area | Resolution | Durable project decision |
|---|---|---|
| UCR branding | Accepted | User-facing interfaces use UCR branding; Pathways remains internal only. |
| Duplicate UCR naming near logo | Accepted | Avoid redundant institutional naming in interface chrome. |
| Counselor full programme list | Accepted | Full programme-provider corpus. |
| Counselor filters | Accepted conditionally | Use filters only where registry metadata supports them reliably. |
| Counselor programme search | Accepted | Programme/provider metadata is directly searchable. |
| Counselor interest search | Accepted, modified | Interests discover programme-provider records; they do not personalize comparisons. |
| Student original wording + interpretation | Accepted | Preserve and show both separately. |
| Student programme then comparison | Accepted | Personalized programme view precedes/links to comparison view. |
| Fixed labels such as “strong match” | Rejected | Use case-specific descriptive labels. |
| Visible “Reference programme” | Rejected | Show actual programme + institution directly. |
| External programme source link | Accepted | Comparator heading or adjacent source link points to approved official source. |
| UCR curriculum link | Accepted | Digital UCR comparisons provide curriculum link. |
| ECs on UCR side | Accepted | Show ECs consistently on both sides. |
| Research-seminar callout | Rejected | No special research-seminar device. |
| Exchange callout | Rejected | No exchange device to fill comparison gaps. |
| Elective-space symmetry rule | Rejected | Preserve open space/gaps; no new symmetry rule. |
| Prioritize strongest/easiest counselor cases | Rejected | Produce full corpus in source worksheet order. |
| Reusable explanatory notes | Accepted | Use parameterized semantic note types only where needed. |

---

# 8. Authority rule

This archive explains **where decisions came from**. It does not govern current behavior.

If this file conflicts with an authoritative specification, the current authoritative specification governs. If a future colleague provides new feedback, record it as a new dated verbatim source file rather than rewriting an earlier source, then update an authoritative document only if a durable project decision actually changes.
