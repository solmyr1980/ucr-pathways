# UCR Pathways — Web and LinkedIn Workflow

## Purpose and boundary

This document governs the operational handoff from an **approved public UCR Pathways publication record** to:

1. the public UCR Pathways website;
2. the LinkedIn PDF;
3. manual LinkedIn publication.

It does **not** define academic generation, reference-programme selection, UCR course selection, Open Day production or academic validation. Those belong to the UCR Pathways Production Instructions.

It does **not** record implementation history, successful or failed runs, temporary bugs or deployment status. GitHub is the source of truth for those matters.

The exact repository schema and exact GitHub Actions commands are executable implementation sources and take precedence over prose descriptions of mechanics.

---

## 1. Entry condition

This workflow starts only when:

- the canonical academic comparison has been completed and validated upstream;
- substantive human review has occurred;
- explicit approval for public use has been given;
- a publication-safe structured example record has been prepared in conformity with the current repository schema.

Open Day participant outputs do not enter this workflow automatically.

---

## 2. Single public content source

Use one approved structured publication record as the single programme-content source for both:

- the website example;
- the LinkedIn PDF.

Do not maintain separate hand-edited versions of the comparison for HTML or PDF.

The public record is derived upstream from the canonical academic record. This workflow does not reconstruct or reinterpret academic content.

---

## 3. Repository handoff

Current repository:

`https://github.com/solmyr1980/ucr-pathways`

Current public site:

`https://solmyr1980.github.io/ucr-pathways/`

Repository responsibilities:

### `data/examples/`

Contains one approved structured record per public example.

Programme-specific comparison content belongs here.

### `data/schema/example.schema.json`

Defines the current executable publication-data contract.

Do not duplicate the full schema in this workflow document.

### `data/catalog.json`

Contains discovery metadata used by the landing page.

It may contain:

- example ID;
- short title;
- short description.

It should not duplicate the substantive comparison.

### Website renderer and shared assets

Provide the generic website presentation.

Programme-specific content must not be hardcoded into the renderer.

### LinkedIn rendering scripts

Consume the same approved example records used by the website.

There is no independent LinkedIn content copy.

---

## 4. Publication flow

```text
approved publication record
        ↓
write/update data/examples/<id>.json
        ↓
add/update discovery entry in data/catalog.json
        ↓
commit approved public data
        ↓
        ├── GitHub Pages renders the website example
        │
        └── GitHub Actions validates and renders the LinkedIn PDF
        ↓
human visual review
        ↓
prepare/review LinkedIn post text
        ↓
manual LinkedIn document post
        ↓
LinkedIn native scheduling or publication
```

Do not update project specifications merely because a build succeeds or fails.

---

## 5. Repository validation

Repository validation is a publication-structure check, not a second academic validation step.

The repository may check matters such as:

- required fields and data types;
- programme IDs and semantic roles;
- block and row structure;
- references to known programme IDs;
- duplicate scheduled courses;
- six-semester/four-courses structure where schedules are present.

Prerequisites, actual UCR semester availability, PPD placement and substantive course fit remain upstream academic responsibilities.

The JSON Schema defines the public-data contract. Repository validation code enforces structural checks. Exact validation behavior belongs in the repository code, not this prose document.

---

## 6. Public website workflow

The public root displays the catalog of approved examples.

Selecting an example loads its structured publication record using the routing implemented by the current website. This workflow should use the resulting specific example URL rather than duplicate the site's routing pattern in prose.

The website renderer implements the public behavior, copy, visual identity, link hierarchy and CTA defined in the Master Specification.

Operationally, verify that:

- the correct example loads;
- visible content comes from the approved example record;
- the Reference programme source link resolves to the approved official source;
- the Program Builder CTA resolves to the canonical destination defined in the Master Specification;
- the specific example URL can be copied for use in LinkedIn.

Do not hand-edit programme content in the website renderer to fix an individual example. Correct the approved data upstream instead.

---

## 7. LinkedIn PDF workflow

The LinkedIn PDF is rendered from the same approved publication record as the website.

The renderer implements the LinkedIn presentation requirements defined in the Master Specification.

At a high level, GitHub Actions:

1. validates the selected public example data;
2. builds the LinkedIn print representation;
3. renders the PDF;
4. exposes the PDF as a workflow artifact.

Exact dependency-install commands, Playwright versions and build commands belong in the GitHub Actions configuration and repository scripts, not in this workflow document.

Generated outputs are build artifacts, not sources of programme content.

After generation, conduct a human visual review before publication.

---

## 8. LinkedIn post preparation

For an approved example, prepare:

- the finished LinkedIn PDF;
- the specific interactive UCR Pathways example URL;
- the LinkedIn post text.

The post text may be written separately from the programme data, but it must describe the same approved example accurately.

Use the specific example URL rather than merely the landing page.

---

## 9. LinkedIn publication

For the pilot, publication remains manual.

After substantive and visual approval:

1. create the LinkedIn document post;
2. upload the finished PDF;
3. add the approved post text;
4. include the specific interactive UCR Pathways example link;
5. publish immediately or place the post in LinkedIn's native scheduled-post queue.

Several finished posts may be prepared in one session and scheduled for different days or weeks.

Human control remains mandatory over:

- suitability for public use;
- final visual check;
- LinkedIn text;
- publication timing;
- final decision to publish.

Full transfer automation to LinkedIn is outside the current pilot workflow.

---

## 10. Source-of-truth rules

To prevent maintenance drift:

- academic facts and feasibility come from the upstream canonical process;
- approved public programme content comes from `data/examples/<id>.json`;
- the executable public-data contract comes from the repository schema;
- landing-page discovery metadata comes from `data/catalog.json`;
- exact build mechanics come from GitHub Actions and repository scripts;
- current deployment/build status comes from GitHub;
- durable public behavior and branding requirements come from the Master Specification.

Do not copy implementation status or build history into this document.

Do not copy full academic-generation rules into this document.

Do not create additional hand-maintained programme-content representations.
