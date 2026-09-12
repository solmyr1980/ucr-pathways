# Personalized student Shiny pilot

This pilot tests code-based delivery of a personalized UCR programme experience using the five existing comparison records as development fixtures.

The user-facing interface intentionally uses UCR branding without a visible Pathways sub-brand.

## What the pilot tests

- a student enters a student-specific access code;
- the app retrieves the matching structured comparison record from GitHub;
- the welcome view preserves the student's original wording and provides a separate place for the academic interpretation;
- the first substantive view is the closest-match personalized UCR semester programme;
- the student can switch to the four-programme comparison without regenerating content;
- comparison headings use the new descriptive labels;
- the external programme heading links to its approved official source;
- UCR content links to the current UCR course overview;
- UCR courses show EC information and can be clicked/tapped for descriptions;
- the student receives Admissions and Program Builder calls to action;
- the temporary disclaimer placeholder is visible until approved final disclaimer copy is supplied.

## Legacy-fixture limitation

The five current example records predate the new `interestInterpretation` field. The pilot therefore shows an explicit development placeholder in the interpretation panel when that field is absent. Production student records must store the interpretation separately from the original interest statement.

## Requirements

Install R and RStudio if needed. Install the two R packages once:

```r
install.packages(c("shiny", "jsonlite"))
```

## Run locally

From the repository root:

```r
shiny::runApp("pilot/shiny")
```

Run from a complete repository checkout. Both pilots serve the shared UCR logo, fonts and CSS from the local `assets/` directory and load shared presentation helpers from `pilot/shared.R`. An internet connection is required for normal retrieval of current data from GitHub. For offline development/tests, set `Sys.setenv(UCR_PILOT_LOCAL_DATA = "true")` before starting the app; this uses the checkout's fixtures instead.

## Pilot codes

| Example | Code |
|---|---|
| `p-001` | `UCR-RV7V-7MAM-METB-AGJ3` |
| `p-002` | `UCR-7KBP-82TM-E5B2-K52F` |
| `p-003` | `UCR-LH8L-72WZ-3JMG-3ZVL` |
| `p-004` | `UCR-78ZN-L8Z4-MS5J-3CH2` |
| `p-005` | `UCR-ZHZ2-BSCN-74VA-866L` |

Formatting is forgiving: spaces and hyphens are ignored and letter case does not matter.

## Data sources

The pilot reads comparison fixtures from `data/examples/`, access codes from `pilot/shiny/data/access_codes.json`, and course descriptions from department files under `pilot/shiny/data/courses/`.

Both views preserve material comparison notes. The programme view shows course levels as 100/200/300-level, and “Speak to Admissions” links to UCR's meeting-booking page.

## Production privacy boundary

This pilot **does not test production privacy**. The five examples and their code mapping are public development data.

Production student-specific codes or links must resolve through appropriate private storage/access control. The public GitHub access-code mapping used here must never become the production privacy mechanism.
