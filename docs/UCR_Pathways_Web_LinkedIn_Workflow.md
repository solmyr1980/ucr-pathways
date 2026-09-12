# UCR Pathways — Web and LinkedIn Workflow

## Purpose and boundary

This document governs the **public communication layer** for the UCR Pathways project:

1. selection and preparation of approved public examples;
2. the curated public website;
3. LinkedIn PDF generation;
4. Make-assisted LinkedIn publication.

It does **not** define student personalization, counselor corpus production, UCR course selection, external-programme reconstruction or academic validation. Those belong to the UCR Pathways Production Instructions.

The internal project/repository name remains UCR Pathways, but user-facing website and publication interfaces must not present `UCR Pathways` or `Pathways` as a visible product/sub-brand.

Implementation history, temporary bugs and deployment status belong in GitHub rather than in this document.

---

# 1. Public communication architecture

The public website and LinkedIn are **not additional academic-generation products**.

They sit above the two academic workflows:

```text
student workflow ───────┐
                        ├── editorial/public selection ── approved public record
counselor workflow ─────┘                                  │
                                                           ├── curated website example
                                                           └── LinkedIn PDF/post
```

The counselor corpus will normally provide the majority of public examples because it is deterministic and privacy-safe.

A student-origin case may be used only after explicit public-use approval and confirmation that the record contains no identifying private information beyond an interest statement intentionally approved for publication.

Neither the student app nor the counselor app automatically publishes content.

---

# 2. Entry condition for public use

A record enters this workflow only when:

- the canonical academic comparison has been completed and validated upstream;
- substantive human review has occurred;
- explicit approval for public use has been given;
- a publication-safe structured record has been prepared in conformity with the current repository schema.

For student-origin cases, confirm privacy separately before public export.

For counselor-origin cases, public approval is still required even though the underlying comparison is part of the deterministic counselor library.

---

# 3. Single public content source

Use one approved structured public record as the single programme-content source for both:

- the corresponding curated website example; and
- the LinkedIn PDF.

Do not maintain separate hand-edited programme-content versions for HTML and PDF.

The public record is derived upstream from a validated canonical student or counselor record. This workflow does not reconstruct programmes, reselect UCR courses or reinterpret academic facts.

Editorial website copy and LinkedIn commentary may frame the example differently, but they must describe the same approved programme content accurately.

---

# 4. Repository responsibilities

Current repository:

`https://github.com/solmyr1980/ucr-pathways`

The repository name and technical GitHub Pages paths may retain `ucr-pathways`; this is internal/technical identity rather than visible user-facing branding.

## `data/examples/`

Contains approved **public** comparison records selected for website/LinkedIn use.

It is **not** the complete counselor comparison corpus and must not be repurposed as the full counselor database. Its scope comes from the current approved registry, not a fixed count in this workflow.

## `data/catalog.json`

Contains editorial discovery metadata for the curated public website examples.

It may contain items such as:

- public example ID;
- short title;
- short description;
- optional editorial category/source type.

It does not duplicate the complete comparison content.

## `data/schema/`

Contains executable public-data contracts.

The schema should support approved records derived from either student or counselor origin while preserving one shared four-programme comparison core.

## Counselor data

Programme metadata, programme-interest search indexes and the deterministic counselor comparison library belong in implementation data structures separate from `data/catalog.json` and the curated public-example directory.

## Website renderer

Provides a generic UCR-branded public showcase and comparison renderer.

Programme-specific academic facts must come from approved structured records rather than hardcoded HTML/JavaScript.

## LinkedIn rendering scripts

Consume the same approved public records used by the website when publishing the same case.

## `publication/linkedin/`

Contains generated LinkedIn PDFs used for downstream publication.

These are generated outputs and must not be hand-edited as sources of programme content.

## `publication/queue/current.json`

Remains the stable manual publication-control record read by Make.

Before each approved LinkedIn publication, set:

```json
{
  "example_id": "p-001",
  "title": "...",
  "commentary": "..."
}
```

When no approved post is staged, keep the inert placeholder state:

```json
{
  "example_id": "__not_set__",
  "title": "Not ready for publication",
  "commentary": "Replace this control record with an approved LinkedIn post before running Make."
}
```

The placeholder is a safety state, not a queue-status mechanism.

---

# 5. Public website purpose and structure

The public website is a **curated UCR communication layer**, not:

- the private/personalized student app;
- the exhaustive counselor search tool;
- a dump of all student cases;
- a dump of all counselor cases.

The public landing page should:

- use UCR visual identity without visible Pathways branding;
- explain the idea through a small deliberately selected set of examples/stories;
- provide a clear route for prospective students toward the personalized student intake/experience;
- provide a clear route for school counselors toward the counselor comparison tool;
- provide the Program Builder destination where appropriate.

A curated example may illustrate, for example:

- how a named Dutch bachelor compares with UCR options;
- where UCR closely matches a field and where it does not;
- how related subjects broaden a disciplinary programme;
- a student-origin combination for which no obvious disciplinary degree exists;
- a pattern observed across the Dutch bachelor market.

Do not treat example count as a coverage objective. Selection is editorial.

## 5.1 Website example behavior

An individual approved example should render the four-programme comparison from structured data.

Use the visible programme-label rules from the Master Specification:

- comparator as `[Programme] at [Institution]`;
- case-specific closest-match UCR label;
- field + related-subjects UCR label;
- broader-programme UCR label.

The comparator heading/source link must resolve to the approved official external programme page.

Provide an appropriate UCR curriculum link from the UCR side.

Show EC credits consistently on comparator and UCR components.

Do not add research-seminar, exchange or elective-space boilerplate merely to fill perceived gaps.

## 5.2 Website navigation onward

Where implementation destinations exist, provide clear calls to action such as:

- **For prospective students** → approved student intake/personalized experience;
- **For school counselors** → counselor comparison tool;
- **Build/tweak your programme** → canonical Program Builder destination.

When a curated counselor example is shown, the site may link into the counselor tool pre-focused on that programme or a relevant interest if technically supported.

When a curated student-origin example is shown, the site may invite prospective students to submit their own interests or use the Program Builder.

Do not claim a deep-link/prefill capability until it actually exists.

---

# 6. Public example preparation

For an approved source record:

1. identify whether the origin is `counselor` or `student`;
2. confirm academic validation status;
3. confirm explicit public-use approval;
4. for student-origin cases, confirm privacy-safe content;
5. derive the publication-safe structured record without changing programme facts;
6. write/update `data/examples/<id>.json`;
7. add/update the editorial entry in `data/catalog.json`;
8. run repository validation;
9. verify the website rendering;
10. generate/review the LinkedIn PDF when the case is intended for LinkedIn.

Do not hand-edit renderer code to fix one example's academic content. Correct the approved data upstream.

---

# 7. LinkedIn PDF workflow

The LinkedIn PDF is rendered from the same approved public record as the website example when both present the same case.

The approved record retains the complete four-programme comparison.

The PDF may, as an editorial presentation choice:

- show comparator + three UCR pages; or
- omit the comparator page and show the three UCR pages only.

This choice changes presentation only; it does not change the underlying academic record.

Editorial framing belongs in LinkedIn commentary rather than in a second academic-content copy.

At a high level, GitHub Actions may continue to:

1. validate selected public example data;
2. build LinkedIn print HTML;
3. render the PDF;
4. retain a workflow artifact;
5. copy the generated PDF to `publication/linkedin/<id>.pdf` on `main` for a stable public URL.

Generated PDFs are outputs, not sources.

Conduct human visual review before publication.

Check the website and PDFs against the same approved record: programme headings, component credits, source links and material explanatory notes must agree. Review website links and buttons in their normal, visited, hover and keyboard-focus states, and inspect both the four-column and single-programme views. Confirm that the UCR logo and fonts load, text contrasts with its background, and narrow screens or enlarged text do not clip content. PDF checks must include overflow, font loading, page count and visual inspection. Keep run results and unresolved implementation items in a dated repository audit, outside these authoritative workflow instructions.

---

# 8. LinkedIn editorial scenarios

Retain the five approved starting scenarios, but source them from the redesigned project architecture.

| Scenario | Likely source | Editorial framing |
|---|---|---|
| **1. The degree that doesn't exist** | Often student-origin | Show an unusual combination that no obvious disciplinary bachelor captures. |
| **2. What do you have to give up?** | Counselor-origin | Use one named bachelor and show the trade-off between disciplinary depth and broader UCR combinations. |
| **3. Start with the question** | Counselor interest index or approved student case | Start from a student-facing question/interest and connect it to study options. |
| **4. Same interest, surprisingly different programmes** | Counselor interest index | Use one interest linked to several Dutch programmes to show different disciplinary interpretations. |
| **5. We looked at the Dutch bachelor market** | Counselor corpus/registry | Lead with a defensible market pattern and connect it to UCR possibilities. |

The counselor corpus gives scenarios 2–5 a broader evidence base. Do not imply that an interest-search result is a personalized counselor comparison.

For scenario 5, do not automatically create a separate market-chart pipeline. Add analytical visuals only after a deliberate later decision.

---

# 9. LinkedIn post preparation and Make publication

For an approved example prepare and approve:

- the finished LinkedIn PDF at its stable public URL;
- the LinkedIn document title;
- the LinkedIn commentary.

Update `publication/queue/current.json` with `example_id`, `title` and `commentary`.

Make continues to derive the PDF URL from `example_id` using the stable repository pattern.

The tested Make scenario may continue to:

1. retrieve `publication/queue/current.json` using the fixed raw URL plus cache-busting query parameter;
2. parse `example_id`, `title` and `commentary`;
3. initialize LinkedIn document upload;
4. download the generated PDF;
5. upload PDF bytes to LinkedIn;
6. create the LinkedIn post using the returned document URN.

For the current workflow, publication remains under manual human control.

After a successful publication, reset `current.json` to the inert placeholder state.

Do not implement automatic queue selection, duplicate prevention, status transitions or scheduled publication unless separately approved.

Human control remains mandatory over:

- public suitability;
- privacy where relevant;
- final visual check;
- LinkedIn text;
- publication timing;
- final decision to publish.

---

# 10. Source-of-truth rules

To prevent maintenance drift:

- academic facts and feasibility come from upstream canonical student/counselor production;
- counselor discovery comes from programme metadata + programme-interest indexes;
- deterministic counselor comparisons come from the counselor comparison library;
- approved public programme content comes from `data/examples/<id>.json`;
- public landing-page editorial metadata comes from `data/catalog.json`;
- executable contracts come from repository schemas;
- exact build mechanics come from GitHub Actions and scripts;
- generated LinkedIn PDFs are never edited as sources;
- staged LinkedIn publication inputs come from `publication/queue/current.json`;
- durable public behavior and branding rules come from the Master Specification.

Do not duplicate complete academic content across student app, counselor app, website and LinkedIn.

Do not use this document to record temporary implementation state, build history or deployment incidents.
