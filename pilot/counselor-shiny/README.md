# Counselor comparison Shiny pilot

This pilot tests the deterministic counselor-app architecture with five existing comparisons and now uses the same runtime pattern intended for production.

## What it tests

- one search box can find programmes by programme name, institution or student-facing interest;
- institution and teaching-language filters refine that search; matching interests retain their relationship classification;
- interest signals rank programme-provider records using the existing `interest_relationship` classification;
- search always resolves to a programme-provider record;
- opening a result loads a **pre-produced fixed comparison** rather than generating a personalized comparison;
- the same comparison can therefore be reached through programme-driven or interest-driven discovery;
- external programme provenance is integrated into the comparator heading and links to the approved official source;
- UCR comparison headings use the approved descriptive labels;
- UCR components display EC information and link to the UCR course overview;
- material explanatory notes remain visible, and returning to search preserves the query and filters;
- the interface uses UCR branding without a visible Pathways sub-brand.

## Runtime data architecture

GitHub is the authoritative source and deployment source, but the running app does **not** fetch counselor data from GitHub.

The deployed app reads version-matched JSON files from its own local deployment bundle:

- programme metadata/index;
- programme-interest discovery index;
- deterministic comparison records.

The programme and interest indexes are read and prepared **once when the R process starts**, then shared by all counselor sessions handled by that process. Search uses this in-memory prepared structure. Search text is normalized once at startup, interests are grouped by programme-provider ID, and user typing is debounced by 250 ms.

A selected comparison is read on demand from a small local JSON file. The app does not maintain a separate application-level comparison cache; the files are small and the operating system can cache frequently read files naturally.

## Data files

When production files exist, the app automatically uses:

- `data/counselor/programmes.json`;
- `data/counselor/interests.json`;
- `data/counselor/comparisons/<comparison-id>.json` (with `comparisonId` in the programme index; provider ID is the fallback stable identifier).

Until those production files are created, the pilot falls back to:

- `data/counselor/pilot-programmes.json`;
- `data/counselor/pilot-interests.json`;
- the five existing comparison fixtures in `data/examples/`.

The fallback exists only to keep the five-case pilot runnable while the full deterministic counselor corpus is produced. Once the production index files are present, no application-code change is required to use them.

## Run locally

Install the two required R packages once:

```r
install.packages(c("shiny", "jsonlite"))
```

Then, from the repository root:

```r
shiny::runApp("pilot/counselor-shiny")
```

Run from a complete repository checkout or equivalent deployment bundle. The app serves the shared UCR logo, fonts and CSS from the local `assets/` directory and loads `pilot/shared.R`. Counselor search and comparison data are also local, so normal use does not require GitHub availability after deployment.

BA/BSc, discipline and location filters are not claimed as implemented: the current fixture metadata does not reliably supply those distinctions. `degree = BACHELOR` is not a BA/BSc classification.

## Production boundary

Shiny remains the current implementation candidate. Hosting technology can still change later without changing the counselor data contracts: programme metadata, interest discovery index and fixed comparison records remain separate concerns.
