# UCR Pathways — Web and LinkedIn Workflow

## Purpose and boundary

This document governs the operational handoff from an **approved public UCR Pathways publication record** to:

1. the public UCR Pathways website;
2. the LinkedIn PDF;
3. Make-assisted LinkedIn publication.

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

### `publication/linkedin/`

Contains the public copies of generated LinkedIn PDFs used for downstream publication.

For example `p-001` is published as:

`publication/linkedin/p-001.pdf`

and is available through GitHub Pages at:

`https://solmyr1980.github.io/ucr-pathways/publication/linkedin/p-001.pdf`

These PDFs are generated publication outputs. They are not independent sources of programme content and must not be hand-edited.

### `publication/queue/current.json`

This is the stable publication-control record read by Make.

Its repository path and base raw GitHub URL remain fixed between posts. HTTP 14 appends a per-run cache-busting query parameter so the GitHub/CDN cache cannot return stale control data:

`?cb={{formatDate(now; "x")}}`

Before each approved LinkedIn publication, replace the contents of `current.json` with the three values for the post to be published:

```json
{
  "example_id": "p-001",
  "title": "...",
  "commentary": "..."
}
```

The fields mean:

- `example_id`: the approved example whose generated PDF will be posted;
- `title`: the LinkedIn document title;
- `commentary`: the LinkedIn post text.

The file is intentionally overwritten for each approved post. Git commit history provides the audit trail of prior values, so separate per-post control files are not required for the manual pilot.

When no approved post is staged, keep `current.json` in the inert placeholder state:

```json
{
  "example_id": "__not_set__",
  "title": "Not ready for publication",
  "commentary": "Replace this control record with an approved LinkedIn post before running Make."
}
```

This placeholder deliberately resolves to no real LinkedIn PDF, so an accidental Make run stops before the final LinkedIn publication step. It is a safety state, not a queue-status mechanism.

Do not add publication status, scheduling or automatic queue-selection fields until queue semantics are deliberately designed and approved.

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
          publication/linkedin/<id>.pdf
                    ↓
             stable GitHub Pages URL
                    ↓
              human visual review
                    ↓
          prepare/review LinkedIn text
                    ↓
     update publication/queue/current.json
                    ↓
          run approved Make scenario
                    ↓
             LinkedIn document post
                    ↓
      reset current.json to inert state
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
4. retains the PDF as a downloadable workflow artifact;
5. copies the generated LinkedIn PDF to `publication/linkedin/<id>.pdf` on `main` so GitHub Pages exposes it at a stable public URL.

The public PDF URL therefore follows this pattern:

`https://solmyr1980.github.io/ucr-pathways/publication/linkedin/<id>.pdf`

Exact dependency-install commands, Playwright versions and build commands belong in the GitHub Actions configuration and repository scripts, not in this workflow document.

Generated PDFs are publication outputs, not sources of programme content. Do not hand-edit them.

After generation, conduct a human visual review before publication.

---

## 8. LinkedIn post preparation

For an approved example, prepare and approve:

- the finished LinkedIn PDF at its stable public URL;
- the LinkedIn post text;
- the LinkedIn document title.

After approval, update `publication/queue/current.json` with the three variable publication inputs:

- `example_id`;
- `title`;
- `commentary`.

The PDF URL is not stored separately. Make derives it from `example_id` using:

`https://solmyr1980.github.io/ucr-pathways/publication/linkedin/<example_id>.pdf`

The post text may be written separately from the programme data, but it must describe the same approved example accurately.

Where the post text links to the interactive UCR Pathways example, use the specific example URL rather than merely the landing page.

---

## 9. LinkedIn publication

For the pilot, publication uses the tested Make scenario but remains under manual human control.

The Make scenario requires no post-specific editing. It always retrieves the same stable GitHub control record, `publication/queue/current.json`, parses `example_id`, `title` and `commentary`, and maps those values into the otherwise fixed LinkedIn publication flow.

The scenario performs these operations:

1. retrieve `publication/queue/current.json` from GitHub using the fixed raw URL plus a per-run `cb` query parameter;
2. parse `example_id`, `title` and `commentary`;
3. initialize a LinkedIn document upload and obtain an upload URL and document URN;
4. construct `https://solmyr1980.github.io/ucr-pathways/publication/linkedin/<example_id>.pdf` and download the PDF;
5. upload the PDF bytes to LinkedIn using the temporary upload URL;
6. create the LinkedIn post using the returned document URN, mapped `title` and mapped `commentary`.

The following infrastructure remains fixed between posts:

- the raw GitHub URL for `publication/queue/current.json`, with a per-run cache-busting `cb` query parameter;
- LinkedIn person URN;
- `/rest/documents?action=initializeUpload`;
- the mapped LinkedIn upload URL;
- binary PDF upload handling;
- the mapped LinkedIn document URN;
- `/rest/posts`;
- distribution and publication settings.

For the manual pilot, update `current.json` for one approved post and run the scenario once. After a successful publication, reset `current.json` to the inert placeholder state. Do not yet implement automatic queue selection, status transitions, duplicate prevention or scheduled publication.

After substantive and visual approval, run the scenario manually. The scenario should remain switched off as a scheduled automation unless a separate decision is made to automate publication timing.

Human control remains mandatory over:

- suitability for public use;
- final visual check;
- LinkedIn text;
- publication timing;
- final decision to publish.

---

## 10. Source-of-truth rules

To prevent maintenance drift:

- academic facts and feasibility come from the upstream canonical process;
- approved public programme content comes from `data/examples/<id>.json`;
- the executable public-data contract comes from the repository schema;
- landing-page discovery metadata comes from `data/catalog.json`;
- exact build mechanics come from GitHub Actions and repository scripts;
- generated public LinkedIn PDFs come from `publication/linkedin/<id>.pdf` and are never edited as sources;
- the currently staged LinkedIn publication inputs come from `publication/queue/current.json`;
- Make derives the PDF URL from `example_id` rather than storing or editing a separate per-post PDF URL;
- Git commit history records prior `current.json` values for the manual pilot;
- current deployment/build status comes from GitHub;
- durable public behavior and branding requirements come from the Master Specification.

Do not copy implementation status or build history into this document.

Do not copy full academic-generation rules into this document.

Do not create additional hand-maintained programme-content representations.