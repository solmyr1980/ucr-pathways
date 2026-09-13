# Counselor comparison Shiny pilot

This pilot tests the deterministic counselor-app architecture and uses the same runtime pattern intended for production.

## What it tests

- one search box can find programmes by programme name, institution or student-facing interest;
- institution and teaching-language filters refine that search; matching interests retain their relationship classification;
- interest signals rank programme-provider records using the existing `interest_relationship` classification;
- search always resolves to a programme-provider record;
- opening a result loads a **pre-produced fixed comparison** rather than generating a personalized comparison;
- the same comparison can therefore be reached through programme-driven or interest-driven discovery;
- each comparison shows exactly one external comparator and between one and three UCR alternatives;
- the first UCR alternative is the closest feasible match, while additional alternatives appear only when upstream production found them evidence-backed, coherent, substantively distinct and feasible;
- the interface does not imply that every target has the same number of UCR alternatives;
- external programme provenance is integrated into the comparator heading and links to the approved official source;
- UCR comparison headings use descriptive case-specific labels;
- UCR components display EC information and link to the UCR course overview;
- material explanatory notes remain visible, and returning to search preserves the query and filters;
- the interface uses UCR branding without a visible Pathways sub-brand.

## Runtime data architecture

GitHub is the authoritative source and deployment source, but the running app does **not** fetch counselor data from GitHub.

The app reads version-matched JSON files from its own local repository/deployment bundle:

- programme metadata/index;
- programme-interest discovery index;
- deterministic comparison records.

The programme and interest indexes are read and prepared **once when the R process starts**, then shared by all counselor sessions handled by that process. Search uses this in-memory prepared structure. Search text is normalized once at startup, interests are grouped by programme-provider ID, and user typing is debounced by 250 ms.

A selected comparison is read on demand from a small local JSON file. The app does not maintain a separate application-level comparison cache; the files are small and the operating system can cache frequently read files naturally.

## Data modes

The app selects the first complete data mode available in this order:

1. **production** — `data/counselor/programmes.json` plus `data/counselor/interests.json`;
2. **review** — `data/counselor/review-programmes.json` plus `data/counselor/review-interests.json`;
3. **pilot** — `data/counselor/pilot-programmes.json` plus `data/counselor/pilot-interests.json`.

Production and review modes load comparison records from `data/counselor/comparisons/<comparison-id>.json`. Pilot mode loads the five approved fixtures from `data/examples/`.

Review mode exists so completed counselor-production records can be inspected in the real app during incremental corpus production **without creating the final production discovery indexes early**. The review indexes are derived artifacts: they contain exactly the normalized `cp-*.json` comparisons currently completed in `data/counselor/comparisons/` and their linked programme-interest rows.

Refresh them from the repository root with:

```bash
npm run build:counselor-review
```

Check that committed review indexes are current with:

```bash
npm run validate:counselor-review
```

The `Refresh counselor review indexes` GitHub workflow performs this refresh automatically after relevant counselor comparison or registry changes. These review files are not the final `programmes.json` and `interests.json` production indexes.

Current production comparison records use the schema 2.0 variable-alternative contract documented in `data/counselor/README.md` and the Production Instructions. The renderer remains compatible with the approved public fixtures used during pilot fallback.

## Run locally

Install the two required R packages once:

```r
install.packages(c("shiny", "jsonlite"))
```

Then, from the repository root:

```r
shiny::runApp("pilot/counselor-shiny")
```

Run from a complete repository checkout or equivalent deployment bundle. The app serves the shared UCR logo, fonts and CSS from the local `assets/` directory and loads `pilot/shared.R`. Counselor search and comparison data are also local, so normal use does not require GitHub availability after the repository/deployment bundle is present.

BA/BSc, discipline and location filters are not claimed as implemented: the current fixture metadata does not reliably supply those distinctions. `degree = BACHELOR` is not a BA/BSc classification.

## Production boundary

Shiny remains the current implementation candidate. Hosting technology can still change later without changing the counselor data contracts: programme metadata, interest discovery index and fixed comparison records remain separate concerns.
