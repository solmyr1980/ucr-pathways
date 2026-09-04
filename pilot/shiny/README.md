# UCR Pathways — Shiny pilot

This is a deliberately small proof of concept for code-based delivery of the five existing public UCR Pathways examples.

## What the pilot tests

- the Shiny app itself can remain generic;
- a user enters a pathway-specific code;
- the app retrieves the matching current pathway JSON directly from GitHub;
- the app retrieves current UCR course descriptions from a separate GitHub-hosted lookup;
- pathway data can therefore change without republishing the Shiny app;
- UCR course names in the semester view can be clicked/tapped to reveal current descriptions;
- the same interface works on desktop and narrower screens.

This pilot does **not** test production privacy. The five examples and the code-to-example mapping are public test data.

## Requirements

Install R and RStudio if they are not already installed. In R, install the two required packages once:

```r
install.packages(c("shiny", "jsonlite"))
```

## Run locally

From the repository root:

```r
shiny::runApp("pilot/shiny")
```

Or open `pilot/shiny/app.R` in RStudio and click **Run App**.

An internet connection is required because the app deliberately retrieves the current data from GitHub rather than bundling pathway data into the app.

## Pilot codes

| Example | Code |
|---|---|
| `p-001` | `UCR-RV7V-7MAM-METB-AGJ3` |
| `p-002` | `UCR-7KBP-82TM-E5B2-K52F` |
| `p-003` | `UCR-LH8L-72WZ-3JMG-3ZVL` |
| `p-004` | `UCR-78ZN-L8Z4-MS5J-3CH2` |
| `p-005` | `UCR-ZHZ2-BSCN-74VA-866L` |

Formatting is forgiving: spaces and hyphens are ignored and letter case does not matter.

## Live data sources

The app reads pathway records from:

`data/examples/p-001.json` through `data/examples/p-005.json`

It reads pilot access codes and the course lookup from:

`pilot/shiny/data/`

A cache-busting query parameter is added to each fetch so a new app session does not intentionally reuse stale GitHub/CDN data.

## Production boundary

If this pilot is accepted, private participant pathway records should move to private server-side storage. The public GitHub access-code file used here must **not** become the production privacy mechanism.
