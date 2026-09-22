# Personalized student Shiny app

This app supports two explicit server-side data modes:

- **public development** — the five tracked public comparison records and public development access codes;
- **private bundled** — ignored local student records and a private access index included only in the shinyapps.io deployment bundle.

The user-facing interface intentionally uses UCR branding without a visible Pathways sub-brand.

These are two data modes of one student app, not separate public, private, pilot or test applications.

Academic production is autonomous in the sense defined by the Production Instructions: the AI workflow proceeds from the submitted interest statement to a completed validated JSON record without an intermediate approval stop. The Shiny app does not generate programmes live. The private-data workflow described below begins with that completed record.

## Student journey

- a student enters a student-specific access code;
- the server resolves the code and reads only the matching structured comparison record;
- the welcome view preserves the student's original wording and provides a separate place for the academic interpretation;
- the first substantive view presents every included personalized UCR programme in semester-by-semester format, using case-specific titles derived from the student's interests and the completed curriculum;
- records may contain between one and three UCR programmes; the interface adapts its singular/plural wording and does not assume that later programmes are broader;
- the student can switch to the comparison view without regenerating content;
- the comparison uses a relevant Dutch bachelor as a concrete point of comparison, not as the generating reference for the student's UCR programmes;
- comparison headings use descriptive case-specific labels;
- the external programme heading links to its approved official source;
- UCR content links to the current UCR course overview;
- UCR courses show EC information and can be clicked/tapped for descriptions;
- the student receives Admissions and Program Builder calls to action near the top of the record;
- on narrow screens, each multi-option programme schedule links back to the programme selector;
- on narrow screens, the comparison shows one programme at a time with swipe, arrow and position controls, while wider screens retain the full comparison table;
- each programme option shows the approved student-program disclaimer;
- application-authored interface text uses American spelling apart from deliberately retained call-to-action labels, while source-data text remains unchanged.

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

Run from a complete repository checkout. Both Shiny apps serve the shared UCR logo, fonts and CSS from the local `assets/` directory and load shared presentation helpers from `pilot/shared.R`. Public-development data and course descriptions are read from the checkout, so normal local use does not depend on GitHub at runtime.

## Public development codes

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
Rscript scripts/validate-and-deploy-student.R --check-only
```

The initializer creates `private/student-records/`, `private/student-access.json`, `private/student-mode.json` and `private/student-test-codes.txt`. The complete `private/` tree is ignored by Git. Generated records preserve the five original interest statements, add fixed test interpretations, and use newly generated 80-bit access codes. The deployment bundle excludes the local code-reference text file, the public access map and the public example records.

The five-case dataset cannot be deployed over the live app while it is still marked as a test dataset. It can also serve as the starting contents of the cumulative private dataset when additional records are registered.

No standalone Git command-line executable is required. Initialization and deployment validate the root-anchored `/private/` rule directly from the repository `.gitignore`.

## Cumulative real-student production workflow

shinyapps.io is the approved deployment target for the real-student workflow. GitHub must contain no real student data. Completed records and access mappings remain beneath the ignored local `private/` tree.

For one central list of production, setup, diagnostic and test commands, see [`docs/operations/STUDENT_APP_COMMANDS.txt`](../../docs/operations/STUDENT_APP_COMMANDS.txt).

Put any number of completed student JSON records directly in `private/student-records/`. Register every new record with one command:

```text
Rscript scripts/add-students-private.R
```

Registration:

- detects files that are not yet present in the private access index;
- validates every new JSON record before changing that index;
- rejects the complete batch if a record is malformed, incorrectly named or has a duplicate ID;
- generates a stable cryptographically secure 80-bit code for each student;
- preserves all previously registered records and codes;
- updates the cumulative private index once; and
- writes the new codes to the ignored private file `private/student-last-batch-codes.csv`.

Registration does not deploy the app. You can therefore register one batch now, another batch later, and deploy all accumulated records once when you are ready. If a batch fails, its files remain in `private/student-records/` for correction, while the access index and existing codes remain unchanged. If the folder began as the five-case test dataset, the first additional record triggers a non-destructive metadata migration to cumulative production mode: all five existing records and their private access codes remain unchanged, the new record is appended, and registration continues in the same command.

Validate the full cumulative dataset and exact bundle, then deploy once:

```text
Rscript scripts/validate-and-deploy-student.R
```

Use `--account=...` when the shinyapps.io account is not already selected. The deployment computer must already have that account authorized through `rsconnect`. Distribute the access codes from `private/student-last-batch-codes.csv` only after the command reports that deployment completed successfully.

For compatibility, the original single-record import remains available for a record stored elsewhere:

```text
Rscript scripts/add-student-private.R --record="C:/path/to/p-006.json"
```

The first successful addition creates the production structure automatically. An explicit empty initialization remains available with `Rscript scripts/add-student-private.R --init`, but is not part of the routine workflow. Run only one addition process at a time. If a process is interrupted and no addition is still running, remove the reported stale lock directory before retrying.

For diagnostics without deployment, run:

```text
Rscript scripts/validate-and-deploy-student.R --check-only
```

The deploy command always targets the same `ucr-student` app. It refuses to deploy while any JSON file in `private/student-records/` remains unregistered. The bundle contains the private access index and only its referenced student records; it excludes the public examples, public development access map, local lock material and administrative code-reference files. A valid access code renders only its corresponding record.

The ignored local `private/` dataset is cumulative and is the authoritative operational copy. Back it up through an approved secure institutional method. Losing this directory also loses the authoritative record of stable student codes; backup design and automation are outside this repository.
