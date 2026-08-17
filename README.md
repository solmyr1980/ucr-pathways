# UCR Program Builder

This repository renders approved Program Builder examples from one shared data source into:

1. an interactive GitHub Pages page;
2. a LinkedIn PDF carousel.

The academic construction and substantive validation of an example happen upstream. This repository stores the approved public representation and renders it consistently.

## Repository structure

```text
ucr-program-builder/
├── index.html
├── assets/
│   ├── css/
│   │   ├── web.css
│   │   └── linkedin.css
│   └── js/
│       └── app.js
├── data/
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

## Core design

`data/examples/*.json` is the source for published examples. The renderers do not assume fixed visible labels, fixed block names, a fixed number of blocks, or a fixed number of rows within a block.

The current example still contains four programmes, but the rendering code iterates over the `programmes` array rather than naming columns in code. Programme labels and subtitles are data. A comparator is identified semantically through fields such as `role`, `family`, or `accent`, so its visible wording can change without changing the renderer.

Rows store cells by programme id rather than by column position. This means programme order can change without rewriting all rows.

A cell may be either a simple string or an object such as:

```json
{
  "text": "Applied Economics Research Course",
  "note": "15 EC incl. thesis",
  "emphasis": true
}
```

Schedules are optional in the public record for now. If an approved UCR example includes a schedule, the validator checks the basic six-semester/four-courses-per-semester structure and duplicate courses. Course availability and prerequisites still require the upstream enriched UCR database and should not be inferred from this public repository.

## Adding another example

Add one file such as:

```text
data/examples/p-002.json
```

No change to `index.html`, CSS, or JavaScript should be needed merely because the new example has different programme labels, block names, block counts, or row counts.

The interactive page is then addressed as:

```text
https://solmyr1980.github.io/ucr-program-builder/?example=p-002
```

If no `example` parameter is supplied, the site displays `p-001`.

## LinkedIn PDF generation

The GitHub Action validates the example data, builds one print HTML file per selected example, renders the PDF with Playwright, and uploads the PDFs as a GitHub Actions artifact.

On a normal push affecting examples or rendering code, it builds all examples. A manual workflow run can specify one example id, such as `p-002`.

Generated local/build files live under `output/` and are ignored by Git. They should not accumulate in the repository.

## Future LinkedIn publication

`publication/linkedin/` is intentionally reserved but not yet given a rigid format. The later Make workflow can use it for the handoff between an approved example and LinkedIn publication—for example, publication state, approved post text, the interactive URL, and a reference to the finished PDF.

The repository deliberately does not yet decide the exact publication manifest because the Make workflow has not been implemented. GitHub Actions generates assets; Make will publish only after explicit human approval.

## Clean replacement of the existing repository

Keep the existing repository itself. In particular, keep the hidden `.git` folder inside your local repository root.

For the current local location:

```text
C:\Github\ucr-program-builder
```

replace the working-tree contents with the contents of this package. Do not copy the outer package folder itself into the repository; copy the files and folders inside it so that `index.html` remains directly in `C:\Github\ucr-program-builder`.

Then open GitHub Desktop and inspect the complete change set before committing. A suitable single commit message is:

```text
Restructure Program Builder around shared example data
```

Push only after the complete replacement is visible as one coherent change.

## Local testing note

Because the web page loads JSON with `fetch()`, opening `index.html` directly with a `file://` URL will normally be blocked by browser security rules. The normal workflow is to test the pushed GitHub Pages version. If local browser testing is ever needed, serve the repository through a small local HTTP server rather than double-clicking `index.html`.
