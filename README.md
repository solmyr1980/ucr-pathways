# UCR Pathways

`UCR Pathways` is the internal project and repository name for a set of UCR programme-comparison workflows and interfaces.

The project name is **not** intended to appear as a user-facing sub-brand. Student, counselor and public interfaces use University College Roosevelt branding directly.

## Current architecture

The project has four distinct surfaces built on shared academic comparison content:

1. **Student app** — a personalized experience generated from an actual prospective student's submitted interests.
2. **Counselor app** — a deterministic searchable library of pre-produced comparisons, one per programme-provider record in scope.
3. **Public website** — a curated showcase and communication layer rather than the complete counselor database.
4. **LinkedIn** — an editorial distribution layer using selected approved public records and generated PDFs.

The website and LinkedIn do not independently reconstruct academic content.

## Authoritative project documents

The authoritative maintained specifications are in `docs/`:

- `docs/UCR_Pathways_Master_Specification.md` — durable product, academic, content and architectural decisions;
- `docs/UCR_Pathways_Production_Instructions.md` — academic generation, validation and record creation for student and counselor workflows;
- `docs/UCR_Pathways_Web_LinkedIn_Workflow.md` — public curation, website and LinkedIn publication workflow.

Retrieve these current GitHub copies before substantive project work. Do not substitute old project-source copies or previous-conversation summaries.

## Repository operating rule

Routine approved work is performed directly on `main`.

- Do not create branches or pull requests for routine work.
- If isolation is genuinely needed for a risky exceptional change, explain why and obtain explicit approval first.
- After substantial work, check repository hygiene. The normal state is one active branch (`main`) and no open pull requests.
- Git commit history is the normal rollback mechanism.

## Shared comparison model

Every comparison has four stable semantic roles:

1. `comparator` — one external Dutch bachelor programme;
2. `ucr-depth` — closest feasible UCR match;
3. `ucr-balanced` — the field plus related subjects or additional student interests;
4. `ucr-thematic` — a broader UCR programme around relevant interests/questions/themes.

Visible programme headings use descriptive language rather than the internal role names.

External programme provenance is integrated into the comparator heading as `[Programme] at [Institution]`, linked to the approved official source. UCR components link to the UCR course overview. EC information is shown on both sides where comparison components are displayed.

## Student workflow and pilot

The production student workflow begins with an actual interest statement and preserves both:

- the student's original wording;
- a separate academic interpretation.

The student app then offers:

- a personalized UCR semester programme;
- a comparison with the external bachelor and two broader UCR alternatives;
- Admissions and Program Builder next steps.

The current Shiny proof of concept is under:

`pilot/shiny/`

It uses five public development fixtures and public test access codes. This is **not** a production privacy mechanism. Production student-specific records must use appropriate private storage/access control.

## Counselor workflow and pilot

Counselor production is deterministic. The unit of production is one programme-provider record from the Dutch bachelor registry, processed in source worksheet order without prioritization.

The counselor app supports two discovery routes into the same fixed comparison library:

- programme-driven search;
- interest-driven search using the programme-interest enrichment table.

An interest query locates relevant programmes; it does not regenerate or personalize the comparison.

Pilot implementation files are under:

- `data/counselor/` — five-case search/index fixtures;
- `pilot/counselor-shiny/` — deterministic search/retrieval Shiny proof of concept.

The complete programme-provider corpus will replace the pilot fixtures as comparisons are produced and validated.

## Public website

The GitHub Pages site is a curated UCR showcase, not the complete counselor database and not the private student app.

Public examples are stored in:

`data/examples/`

Editorial landing-page metadata is stored in:

`data/catalog.json`

Most future public examples will normally be selected from the counselor corpus. A student-origin case may be used only after explicit public-use approval and privacy review.

## Data contracts

`data/schema/example.schema.json` defines the current public comparison contract.

It supports records derived from either student or counselor workflows and retains temporary compatibility with the five legacy public examples during migration.

The shared record model preserves:

- comparator identity/source;
- four programme roles;
- UCR schedules;
- comparison blocks and deliberate gaps;
- EC credits;
- explanatory notes;
- optional student-origin or programme-provider metadata.

The counselor programme index and programme-interest discovery index remain separate from curated public-example data.

## Reusable explanatory notes

Counselor comparisons do not require hundreds of manually written bespoke notes.

The production instructions define reusable semantic note types for situations such as:

- less disciplinary depth at UCR;
- related fields rather than a full discipline;
- missing specialist components;
- similar territory organized through a different curricular structure.

Use a note only when it prevents a material misunderstanding.

## LinkedIn publication

LinkedIn retains the existing human-controlled publication architecture:

```text
approved public record
        ↓
website example + generated LinkedIn PDF
        ↓
human visual/editorial review
        ↓
publication/queue/current.json
        ↓
manual Make scenario
        ↓
LinkedIn document post
```

Generated PDFs under `publication/linkedin/` are outputs, not programme-content sources.

The existing editorial scenarios remain available, now drawing especially on the deterministic counselor corpus and programme-interest index.

## UCR Program Builder

The downstream UCR Program Builder remains a separate product:

`https://program.ucr.nl/`

The project may link students there to modify or build their own programme, but must not imply automatic transfer of a displayed comparison unless that functionality has actually been implemented.

## Visual identity

User-facing interfaces follow UCR's settled visual identity and do not display a Pathways sub-brand.

The website, both Shiny pilots and both PDF renderers load the same UCR fonts and palette from `assets/css/brand.css`. Shiny screen states share `assets/css/shiny.css`; the website and print formats retain their own layout styles. Colour supports identity, navigation and orientation rather than acting as the principal academic classification system.

## Quality control and current limitations

See `docs/quality-control/2026-09-11-audit.md` for the feedback-by-feedback implementation review, verification evidence and unresolved production requirements. This is an implementation record, not another specification.

The five public fixtures now store current descriptive labels and `comparator` metadata. They remain legacy demonstration records without asserted student/counselor production provenance. New records with an explicit production origin must provide a separate student interpretation or a programme-provider key, respectively. Public explanatory notes must contain final rendered text.

Use `npm ci` and `npm run dev` for a local website preview; deployment remains the existing static GitHub Pages site. `npm test` and `npm run validate` check presentation contracts and fixture structure. `Rscript scripts/test-shiny.R` checks access-code handling, search, retrieval and note rendering with local fixtures. These checks do not replace course-database feasibility validation.
