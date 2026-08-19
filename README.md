# UCR Pathways

This repository stores and renders approved public **UCR Pathways** examples.

UCR Pathways compares one disciplinary reference programme with three feasible UCR pathways that move from greater disciplinary depth toward broader combinations of interests and themes.

Academic construction and feasibility validation happen upstream. This repository contains the approved public representation and the generic renderers used for the website, LinkedIn PDFs and Open Day PDF regression testing.

## Content flow

```text
canonical academic comparison
        ↓
substantive human review
        ↓
approved public example record
        ↓
data/examples/<id>.json
        ↓
        ├── GitHub Pages interactive example
        ├── GitHub Actions LinkedIn PDF
        └── GitHub Actions Open Day PDF test output
```

Programme content is not maintained separately in HTML or PDF-specific files.

Real Open Day participant records remain non-public. `canonical/` is reserved for local canonical records and is excluded from Git. The public examples in this repository are also used as regression cases for the Open Day renderer.

## Current public examples

The repository currently contains five deliberately different stress-test examples (`p-001` through `p-005`). They exercise different disciplinary reference programmes, comparison structures, gaps, component sizes and UCR course combinations.

The public catalog is at:

```text
https://solmyr1980.github.io/ucr-pathways/
```

An individual example is addressed with:

```text
https://solmyr1980.github.io/ucr-pathways/?example=p-001
```

## Publication data contract

`data/schema/example.schema.json` defines the executable public example contract.

Each example contains exactly four programmes in this semantic order:

1. `comparator`
2. `ucr-depth`
3. `ucr-balanced`
4. `ucr-thematic`

The three UCR programmes must each include a complete six-semester schedule with four courses per semester. The current Open Day renderer consumes those schedules.

Rows store comparison cells by programme ID. Blank cells are deliberate and indicate that no sufficiently comparable named component is shown in that position.

The approved disciplinary source is recorded under `referenceProgramme`, including the exact student-facing provenance line and primary official source URL.

## Validation boundary

Repository validation checks the publication structure, including:

- required fields and semantic programme roles;
- unique programme IDs;
- comparison block and row structure;
- references to known programme IDs;
- complete UCR schedule shape;
- four courses per semester;
- duplicate scheduled courses.

Academic feasibility remains upstream. In particular, repository validation does not establish prerequisites, actual semester availability, PPD placement or substantive course fit. Those are checked against the enriched UCR course database during academic production.

## Website

The website renderer is generic and data-driven.

For an individual example:

- wide screens show all four programmes side by side by default;
- narrow screens show one programme at a time;
- wide screens can switch between `Compare all` and `One at a time`;
- one-at-a-time mode supports forward/back controls, keyboard arrows and touch swiping.

Adding an approved example should normally require only a new `data/examples/<id>.json` record and a catalog entry, not programme-specific renderer changes.

## PDF generation

The GitHub Actions workflow validates the selected example data, installs Playwright/Chromium, builds the print HTML and generates two artifact sets:

- `linkedin-pdfs` — one programme per page for LinkedIn document posts;
- `open-day-pdfs` — two-page A4 portrait handouts used to test the Open Day renderer.

On relevant pushes, the workflow builds all examples. A manual workflow run can build one example or all examples.

The Open Day renderer uses adaptive fitting. Page 1 retains the established comparison density logic. On page 2, the renderer first tries substantially larger semester-course typography and steps down only if a cell or page would overflow. The existing normal/compact/dense layouts remain as safe fallbacks.

Generated files under `output/` are build artifacts and are ignored by Git.

## LinkedIn publication

For the pilot, LinkedIn publication remains human-controlled. The finished post uses the corresponding specific UCR Pathways example URL and may be published immediately or placed in LinkedIn's native scheduled-post queue.

## UCR Program Builder

UCR Pathways and the **UCR Program Builder** are separate products. The downstream Program Builder destination is:

```text
https://program.ucr.nl/
```

Open Day QR codes and public `Build your own programme` calls to action point there.

## Visual identity

The website and PDF renderers use the settled UCR palette, IvyMode for display headings and Inter for body text. Colour supports identity, navigation and orientation rather than serving as the primary classification of programme content.
