# UCR Pathways

This repository stores and renders approved public **UCR Pathways** examples.

The repository is still temporarily named `ucr-program-builder`. The repository and GitHub Pages path will be renamed in a later implementation step after the content, data contract and documentation are aligned.

UCR Pathways compares:

1. one disciplinary bachelor programme; and
2. three feasible UCR pathways that progressively move from greater disciplinary depth toward broader combinations of interests and themes.

The academic construction and feasibility validation happen upstream using the UCR Pathways instructions. This repository stores the approved public representation and renders it consistently for the website and LinkedIn PDF.

## Public flow

```text
approved canonical comparison
        ↓
publication example record
        ↓
data/examples/<id>.json
+ data/catalog.json
        ↓
        ├── GitHub Pages interactive example
        └── GitHub Actions LinkedIn PDF
```

The website and LinkedIn PDF use the same publication example record. Programme content is not maintained separately in HTML or PDF-specific files.

## Repository structure

```text
ucr-program-builder/
├── index.html
├── assets/
│   ├── brand/
│   ├── css/
│   │   ├── web.css
│   │   └── linkedin.css
│   ├── fonts/
│   └── js/
│       └── app.js
├── data/
│   ├── catalog.json
│   ├── examples/
│   │   └── p-001.json
│   └── schema/
│       └── example.schema.json
├── publication/
│   └── linkedin/
├── scripts/
│   ├── example-utils.mjs
│   ├── validate-example.mjs
│   ├── build-linkedin-html.mjs
│   └── render-linkedin-pdf.mjs
├── .github/
│   └── workflows/
│       └── build-linkedin-pdf.yml
├── .gitattributes
├── .gitignore
└── README.md
```

`publication/linkedin/` is currently a legacy/reserved directory. It is not part of the pilot publication workflow.

## Publication data contract

`data/schema/example.schema.json` defines the public example data contract.

A public UCR Pathways example contains exactly four programmes in this semantic order:

1. `comparator`
2. `ucr-depth`
3. `ucr-balanced`
4. `ucr-thematic`

`role` is the semantic source of truth. Programme IDs remain flexible but must be unique. Visible programme labels and subtitles remain example-specific data.

`family` may remain as compatibility metadata but does not determine the programme's semantic role.

Rows store cells by programme ID rather than by column position. A cell may be a string, `null`, or an object such as:

```json
{
  "text": "Applied Economics Research Course",
  "note": "15 EC incl. thesis",
  "emphasis": true
}
```

Blank cells are deliberate: they indicate that there is no sufficiently comparable named component in that position.

## Academic validation versus repository validation

The repository performs publication-structure checks. Its custom validator checks items such as:

- required publication fields;
- exactly four programmes with the settled semantic roles;
- unique programme IDs;
- valid block and row structure;
- references to known programme IDs;
- basic UCR schedule shape and duplicate scheduled courses when schedules are supplied.

The JSON Schema defines the data contract; the current custom validator does not constitute full JSON Schema-engine validation.

Academic feasibility remains upstream. In particular, the repository does not establish:

- prerequisites;
- actual semester availability;
- Personal & Professional Development placement;
- substantive course fit;
- the full academic validity of a UCR programme.

The enriched UCR course database and UCR Pathways instructions are authoritative for those checks.

## Schedules

Complete six-semester schedules remain mandatory in the canonical pathway record created upstream.

Schedules are optional in the public example record. When a UCR schedule is supplied publicly, it must contain six semesters with four courses in each semester and no duplicate scheduled course.

The current comparison website and LinkedIn PDF do not require schedules in order to render the comparison.

## Landing page and example URLs

The GitHub Pages root loads `data/catalog.json` and displays the catalog of approved public examples.

The current public root is:

```text
https://solmyr1980.github.io/ucr-program-builder/
```

An individual example is addressed with:

```text
https://solmyr1980.github.io/ucr-program-builder/?example=p-001
```

These paths will change when the repository is renamed to `ucr-pathways`.

## Adding another public example

After human substantive review and explicit approval for public use:

1. add the approved publication record under `data/examples/<id>.json`;
2. add or update its discovery entry in `data/catalog.json`;
3. validate the example;
4. commit and push the approved public data.

Adding an example should not require programme-specific changes to `index.html`, CSS or JavaScript.

The catalog contains discovery metadata only. It should not duplicate the substantive programme comparison.

## Website behavior

The website renderer is generic and data-driven.

For an individual example:

- wide screens show all four programmes side by side by default;
- narrow screens show one programme at a time;
- wide screens can switch between `Compare all` and `One at a time`;
- one-at-a-time mode supports forward/back controls, keyboard arrows and touch swiping.

Programme titles, subtitles, blocks, rows, cells and notes come from the example data.

## LinkedIn PDF generation

The LinkedIn renderer consumes the same approved example record as the website.

The PDF uses one programme per page so the four-programme progression can be swiped through on a phone.

The GitHub Action:

1. runs the custom example validator;
2. installs the PDF-rendering dependencies;
3. builds LinkedIn-specific print HTML;
4. renders PDFs with Playwright;
5. uploads the finished PDFs as a GitHub Actions artifact.

On a push affecting relevant example or rendering files, the Action builds all examples. A manual workflow run may request one example ID or all examples.

Generated files under `output/` are build artifacts and are ignored by Git.

## LinkedIn publication

For the pilot, publication to LinkedIn is manual.

After substantive approval and a final visual check:

1. create the LinkedIn document post;
2. upload the finished PDF;
3. add the approved post text;
4. include the URL of the corresponding interactive UCR Pathways example;
5. place the post in LinkedIn's native scheduled-post queue.

Several approved posts may be prepared and scheduled for different days or weeks.

**Make is not part of the current pilot workflow.** It may be reconsidered later only if automating the mechanical handoff to LinkedIn creates clear value.

## UCR Pathways and the UCR Program Builder

UCR Pathways and the UCR Program Builder are separate products.

The public website and LinkedIn posts present **UCR Pathways** comparisons.

The separate **UCR Program Builder** is the downstream tool where a prospective student can build a programme themselves. Open Day QR codes should lead there.

## Visual identity

The current web and LinkedIn CSS use the settled UCR visual identity:

- Heritage Plum `#491E34`
- Foundation White `#F8F5EE`
- Academic Black `#2E2D2D`
- Thoughtful Grey `#5C606B`
- Reflective Lilac `#D0B7D0`
- Clarity Blue `#C8DFE6`
- Open Yellow `#FFE1A4`
- Grounded Green `#4A6857`

Display headings use IvyMode and body text uses Inter.

Colour supports identity, navigation and orientation rather than serving as the main substantive classification system.

## Local testing

The website loads JSON with `fetch()`, so opening `index.html` directly through a `file://` URL will normally fail because of browser security rules.

The normal workflow is to test the pushed GitHub Pages version. If local browser testing is needed, serve the repository through a local HTTP server.
