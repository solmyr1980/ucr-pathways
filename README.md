# UCR Pathways

`UCR Pathways` is the internal project and repository name for a set of UCR programme-comparison workflows and interfaces.

The project name is **not** intended to appear as a user-facing sub-brand. Student, counselor and public interfaces use University College Roosevelt branding directly.

## Current architecture

The project has four distinct surfaces built on shared academic comparison content:

1. **Student app** — a personalized experience generated from an actual prospective student's submitted interests.
2. **Counselor app** — a deterministic searchable library of pre-produced comparisons, one per normalized counselor programme target in scope.
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

Every comparison contains:

1. exactly one external Dutch bachelor `comparator`; and
2. between **one and three ordered UCR alternatives**.

Student and counselor records use that structure differently. Student UCR programmes are generated directly from the student's interpreted interests; the external bachelor is selected later as a useful comparison point and does not define the first programme or its label. Counselor records start from an external target, so their first UCR alternative remains the closest feasible response to that target. Additional programmes are included only when they are evidence-backed, academically coherent, substantively distinct and mechanically feasible. Three is the maximum, not a quota, and later programmes do not have to become progressively broader.

Current production records use the generic UCR role `ucr-alternative`. Optional `alternativeKind` metadata may describe an analytical type, but those types are not mandatory slots and must not make student labels comparator-relative. Counselor records may continue to use `closest-match` where the external bachelor is the explicit target.

Visible programme headings use descriptive case-specific language rather than internal role names.

External programme provenance is integrated into the comparator heading as `[Programme] at [Institution]`, linked to the approved official source. UCR components link to the UCR course overview. EC information is shown on both sides where comparison components are displayed.

## Student workflow and app

The production student workflow begins with an actual interest statement and preserves both:

- the student's original wording;
- a separate academic interpretation.

The student app then offers:

- one to three complete UCR programmes constructed directly from the student's interpreted interests, each with a case-specific title describing the programme itself;
- sub-navigation that lets the student inspect each complete six-semester programme separately;
- a comparison of a relevant Dutch bachelor with the same included UCR programmes;
- Admissions and Program Builder next steps.

The current Shiny implementation is under:

`pilot/shiny/`

In public-development mode it uses five tracked public fixtures and public test access codes. Private test and production modes enforce a strict boundary:

- application code, schemas, branding and public fixtures remain in GitHub;
- student records, the private access index and locally generated codes live under the Git-ignored `private/` tree;
- the shinyapps.io deployment script bundles only the required application files and selected private records;
- the Shiny server performs code lookup and record reading; the private index and complete record collection are never exposed as static browser assets.

The private mode is selected once at application startup. A private deployment cannot fall back to the public access map or public records.

### Run the five-case private student deployment test

After pulling the repository, install the required R packages once:

```r
install.packages(c("shiny", "jsonlite", "openssl", "rsconnect"))
```

Then run these commands from the repository root:

```text
Rscript scripts/init-student-private-test.R
Rscript scripts/validate-and-deploy-student.R --check-only
```

The initializer clones `p-001` through `p-005` into ignored private test records, adds separate academic interpretations and generates new strong random access codes. It prints the codes and saves them in the ignored local file `private/student-test-codes.txt`. It refuses to overwrite existing private data. To replace only a previously generated five-case test dataset and rotate its codes, run:

```text
Rscript scripts/init-student-private-test.R --reset-test
```

The disposable five-case dataset cannot be deployed over the live app. Real production uses one cumulative ignored dataset and the single permanent shinyapps.io application name `ucr-student`. The complete operational command reference is in [`docs/operations/STUDENT_APP_COMMANDS.txt`](docs/operations/STUDENT_APP_COMMANDS.txt).

For routine production, place any number of completed student JSON records in one secure folder and import the folder with one command:

```text
Rscript scripts/add-students-private.R --folder="C:/secure/incoming/ready"
```

The import is all-or-nothing, preserves all existing records and codes, and creates one new cryptographically secure code per record. It does not deploy. Repeat imports as needed, then validate and deploy the complete accumulated dataset once:

```text
Rscript scripts/validate-and-deploy-student.R
```

Add `--account=YOUR_ACCOUNT` when the account is not already selected. The latest batch's codes are written to `private/student-last-batch-codes.csv`; distribute them only after deployment succeeds. For a single record, `Rscript scripts/add-student-private.R --record="C:/secure/incoming/p-006.json"` remains available as a fallback.

shinyapps.io is the approved target for this workflow. The deploying computer must first be authorized for the relevant account through `rsconnect`; account tokens and secrets remain outside this repository. The ignored local `private/` dataset is the authoritative operational copy and requires secure institutional backup.

The student initializer and deployment checks do not require a standalone Git command-line installation. They verify the root-anchored `/private/` rule directly in the repository `.gitignore` before creating or bundling private data.

## Counselor workflow and pilot

Counselor production is deterministic. The unit of production is one normalized target from the counselor programme registry, processed in `production_order` without prioritization by fit or marketing value.

For each target, production first builds the closest feasible UCR alternative, then considers a second and third sequentially. If the next alternative cannot pass the evidence, coherence, distinctness and feasibility gates, production stops and records why.

The counselor app supports two discovery routes into the same fixed comparison library:

- programme-driven search;
- interest-driven search using the programme-interest enrichment table.

An interest query locates relevant programmes; it does not regenerate or personalize the comparison.

Pilot implementation files are under:

- `data/counselor/` — five-case search/index fixtures;
- `pilot/counselor-shiny/` — deterministic search/retrieval Shiny proof of concept.

The complete normalized counselor corpus will replace the pilot fixtures as comparisons are produced and validated.

## Public website

The GitHub Pages site is a curated UCR showcase, not the complete counselor database and not the private student app.

Public examples are stored in:

`data/examples/`

Editorial landing-page metadata is stored in:

`data/catalog.json`

Most future public examples will normally be selected from the counselor corpus. A student-origin case may be used only after explicit public-use approval and privacy review.

Website examples preserve the same comparator + one-to-three-UCR-alternatives structure as their approved source records; the public renderer does not create additional alternatives to fill a layout.

## Data contracts

`data/schema/example.schema.json` defines the shared/public comparison contract.

It supports records derived from either student or counselor workflows with one comparator and one to three UCR alternatives.

`data/schema/counselor-comparison.schema.json` defines the stricter current counselor production contract. Counselor production uses `schemaVersion: "2.0"` and requires an auditable `alternativeSelection` decision plus evidence-backed rationale for every included UCR alternative.

The shared record model preserves:

- comparator identity/source;
- one to three ordered UCR alternatives;
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

Generated PDFs under `publication/linkedin/` are outputs, not programme-content sources. LinkedIn may omit the comparator page as an editorial presentation choice, but it retains every included UCR alternative from the approved public record.

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

The five public fixtures retain their approved academic content and now use the generic UCR-alternative structure. They remain demonstration/public records without asserted current counselor production provenance. New records with an explicit production origin must satisfy the applicable current production contract. Public explanatory notes must contain final rendered text.

Use `npm ci` and `npm run dev` for a local website preview; deployment remains the existing static GitHub Pages site. `npm test` and `npm run validate` check presentation contracts and fixture structure. `Rscript scripts/test-shiny.R` checks access-code handling, search, retrieval, comparison-note rendering and variable programme-option rendering with local fixtures. These checks do not replace course-database feasibility validation.
