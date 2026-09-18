# Personalized student Shiny pilot

This app supports two explicit server-side data modes:

- **public development** — the five tracked public comparison records and public pilot access codes;
- **private bundled** — ignored local student records and a private access index included only in the shinyapps.io deployment bundle.

The user-facing interface intentionally uses UCR branding without a visible Pathways sub-brand.

## What the pilot tests

- a student enters a student-specific access code;
- the server resolves the code and reads only the matching structured comparison record;
- the welcome view preserves the student's original wording and provides a separate place for the academic interpretation;
- the first substantive view presents every included personalized UCR programme option in semester-by-semester format, ordered from the closest feasible match toward broader alternatives where those are genuinely supported;
- records may contain between one and three UCR programme options; the interface does not manufacture empty or weak slots merely to reach three;
- the student can switch to the comparison view without regenerating content;
- comparison headings use descriptive case-specific labels;
- the external programme heading links to its approved official source;
- UCR content links to the current UCR course overview;
- UCR courses show EC information and can be clicked/tapped for descriptions;
- the student receives Admissions and Program Builder calls to action;
- the temporary disclaimer placeholder is visible until approved final disclaimer copy is supplied.

## Data-mode boundary

Without a private mode marker, the app runs in public-development mode from the tracked checkout fixtures. When `private/student-mode.json` is present, it starts in private mode and validates the private index and every referenced record. Missing or malformed private data prevent startup; an unknown private code never triggers public fallback.

The private tree is not mounted as a Shiny resource path and is never placed under `www/`. The browser receives the selected record's rendered content after a valid lookup, but not the private access index or other student records.

## Requirements

Install R and RStudio if needed. For local development, initialization and deployment checks, install these packages once:

```r
install.packages(c("shiny", "jsonlite", "openssl", "rsconnect"))
```

## Run locally

From the repository root:

```r
shiny::runApp("pilot/shiny")
```

Run from a complete repository checkout. Both pilots serve the shared UCR logo, fonts and CSS from the local `assets/` directory and load shared presentation helpers from `pilot/shared.R`. Public-development data and course descriptions are read from the checkout, so normal local use does not depend on GitHub at runtime.

## Pilot codes

| Example | Code |
|---|---|
| `p-001` | `UCR-RV7V-7MAM-METB-AGJ3` |
| `p-002` | `UCR-7KBP-82TM-E5B2-K52F` |
| `p-003` | `UCR-LH8L-72WZ-3JMG-3ZVL` |
| `p-004` | `UCR-78ZN-L8Z4-MS5J-3CH2` |
| `p-005` | `UCR-ZHZ2-BSCN-74VA-866L` |

Formatting is forgiving: spaces and hyphens are ignored and letter case does not matter. Other punctuation is rejected.

## Data sources

Public-development mode reads comparison fixtures from `data/examples/`, access codes from `pilot/shiny/data/access_codes.json`, and course descriptions from department files under `pilot/shiny/data/courses/`.

Both views preserve material comparison notes. Each programme-option tab shows the full six-semester schedule with course levels as 100/200/300-level, and “Speak to Admissions” links to UCR's meeting-booking page.

## Private five-case deployment test

From the repository root:

```text
Rscript scripts/init-student-private-test.R
Rscript scripts/deploy-student-shiny.R --check
Rscript scripts/deploy-student-shiny.R --check-bundle
Rscript scripts/deploy-student-shiny.R
```

The initializer creates `private/student-records/`, `private/student-access.json`, `private/student-mode.json` and `private/student-test-codes.txt`. The complete `private/` tree is ignored by Git. Generated records preserve the five original interest statements, add fixed test interpretations, and use newly generated 80-bit access codes. The deployment bundle excludes the local code-reference text file, the public access map and the public example records.

The default deployment name is `ucr-student-private-test`. Use `--account=...` and `--app-name=...` to override it. The deployment computer must already have the relevant shinyapps.io account authorized through `rsconnect`.

No standalone Git command-line executable is required. Initialization and deployment validate the root-anchored `/private/` rule directly from the repository `.gitignore`.

This test demonstrates the local-file-to-private-bundle architecture with public development content. Real prospective-student data require separate institutional approval for the hosting and privacy arrangements.
