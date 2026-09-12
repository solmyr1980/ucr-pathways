# Counselor comparison Shiny pilot

This pilot tests the deterministic counselor-app architecture with five existing comparisons.

## What it tests

- one search box can find programmes by programme name, institution or student-facing interest;
- institution and teaching-language filters refine that search; matching interests retain their relationship classification;
- interest signals rank programme-provider records using the existing `interest_relationship` classification;
- search always resolves to a programme-provider record;
- opening a result loads a **pre-produced fixed comparison** rather than generating a personalized comparison;
- the same comparison can therefore be reached through programme-driven or interest-driven discovery;
- external programme provenance is integrated into the comparator heading and links to the approved official source;
- UCR comparison headings use the new descriptive labels;
- UCR components display EC information and link to the UCR course overview;
- material explanatory notes remain visible, and returning to search preserves the query and filters;
- the interface uses UCR branding without a visible Pathways sub-brand.

## Pilot data

The pilot reads:

- `data/counselor/pilot-programmes.json`;
- `data/counselor/pilot-interests.json`;
- the five existing public comparison records in `data/examples/`.

The pilot data exists only to validate search and retrieval. The production app will use the complete programme-provider index, complete programme-interest index and the deterministic comparison corpus as those records are produced.

## Run locally

Install the two required R packages once:

```r
install.packages(c("shiny", "jsonlite"))
```

Then, from the repository root:

```r
shiny::runApp("pilot/counselor-shiny")
```

Run from a complete repository checkout. Both pilots serve the shared UCR logo, fonts and CSS from the local `assets/` directory and load `pilot/shared.R`. An internet connection is required for normal retrieval of current data from GitHub. For offline development/tests, set `Sys.setenv(UCR_PILOT_LOCAL_DATA = "true")` before starting the app.

BA/BSc, discipline and location filters are not claimed as implemented: the current fixture metadata does not reliably supply those distinctions. `degree = BACHELOR` is not a BA/BSc classification.

## Production boundary

This pilot does not decide final hosting technology. Shiny is the current implementation candidate; the authoritative project documents intentionally remain technology-neutral.
