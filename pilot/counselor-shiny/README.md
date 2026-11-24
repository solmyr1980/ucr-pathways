# Counselor comparison Shiny pilot

This pilot tests the deterministic counselor-app architecture and uses the same runtime pattern intended for production.

## What it tests

- one search box can find programmes by programme name, institution or student-facing interest;
- institution and teaching-language filters refine that search; result cards show the student-facing matching interest phrases while relationship classifications remain internal ranking metadata;
- interest signals rank programme-provider records using the existing `interest_relationship` classification;
- search always resolves to a programme-provider record;
- opening a result loads a **pre-produced fixed counselor record** rather than generating a personalized comparison;
- the same comparison can therefore be reached through programme-driven or interest-driven discovery;
- each normal comparison shows exactly one external comparator and between one and three UCR alternatives; a completed exception shows the supported external programme and a reason, with no artificial UCR column;
- the programme identity and one reviewed paragraph lead directly to the table;
- qualified comparisons link to their reviewed assessed and excluded scope;
- the first UCR alternative is the closest feasible match, while additional alternatives appear only when upstream production found them evidence-backed, coherent, substantively distinct and feasible;
- the interface does not imply that every target has the same number of UCR alternatives;
- external programme provenance is integrated into the comparator heading and links to the approved official source;
- UCR comparison headings use descriptive case-specific labels;
- UCR components display EC information and link to the UCR course overview;
- material qualifications appear in the introduction, and returning to search preserves the query and filters;
- the interface uses UCR branding without a visible Pathways sub-brand.

## Comparison presentation

The shared renderer follows Master Specification §4.4. It opens at the external programme title after a selection from search. On ordinary pages the next elements are the common introduction, mobile column controls where applicable, and the table. The external title and institution come from the programme index and comparator metadata. Column headings use the existing case-specific labels.

The opening paragraph identifies the closest feasible option and ends with the shared sentences about course content and blank cells. When the approved record warrants a qualification, case-specific sentences replace the default opening. The optional `introduction` in `data/counselor/presentation-overrides.json` is the only per-case text used for this purpose. The historical `message` stays internal. Caution and qualified comparisons require individually reviewed copy. Qualified paragraphs include `{credits}` once. The renderer inserts the documented and nominal totals and links to the single collapsed disclosure of `audience.comparisonScope.assessed` and `.excluded`. The text identifies which part was actually assessed, even when all 180 EC are listed.

Ordinary and caution pages end with the table and Program Builder link. Academic narratives remain in the canonical records. Table cells show course or component names and credits, and the UCR course buttons open their descriptions. The closing section groups research with open choices where the academic pairings allow it. Exception and external-only pages introduce the external degree before giving any applicable reason for the missing comparison.

Search remains discovery rather than personalization. Relationship classifications such as `Direct programme interest`, `Stable study direction` and `Curricular topic` continue to affect search ranking internally, but counselor-facing result cards display only the matching interest phrases.

## Reversible counselor presentation controls

Academic comparison decisions and UCR course selections remain unchanged. The counselor app reads
`data/counselor/presentation-overrides.json` as a separate, versioned display policy.
With no case entry, an existing comparison defaults to its full presentation. The accepted historical baseline now gives every currently indexed case an explicit mode; omitting a future case still defaults to normal unless it is a canonical exception.

Edit the entry for the permanent counselor ID to change how an existing comparison is displayed. The example uses the reviewed CP043 paragraph.

```json
{
  "schemaVersion": 1,
  "cases": {
    "cp-000043": {
      "mode": "caution",
      "message": "UCR offers related literature and cultural study, but not the English-language training or specialist linguistics sequence of this degree.",
      "introduction": "The closest feasible UCR combination approaches English through literature, stylistics and cultural history. Radboud gives more sustained attention to English proficiency, structural and historical linguistics, and British literary history."
    },
    "cp-000046": {
      "mode": "external-only",
      "message": "A related-fields comparison exists but is withheld while its relevance to French-language study is reconsidered."
    }
  }
}
```

The modes shown here illustrate how the configuration works. Valid modes are:

- `normal`: display the full comparison (also the default if no entry exists);
- `caution`: display one qualification above the table, combined with the scope statement for a qualified comparison. The settings file retains `message` for provenance and uses the reviewed `introduction` for display;
- `external-only`: show the external programme and its verified curriculum under the external-only status.

Search and discovery remain unchanged. An external-only result displays a "View programme" button. All original
decision/canonical records, academic rationale, schedules, comparisons and QC reports remain untouched.
Switching an entry to `normal` restores an academically valid comparison on the next deployment. Retain its reviewed introduction where the qualification still applies.
The app validates the settings on startup and the deployment bundle includes the file.
A true canonical exception still uses its own academic reason and is never reclassified by a display override.

### Initial historical classification (17 October 2026)

The complete 438-case review index was reconciled with the finished QC histories. Its initial presentation settings are:

| Mode | Count | Mechanical source |
|---|---:|---|
| `normal` | 302 | Comparisons already accepted outside the subsequent reassessment groups |
| `caution` | 89 | 54 previous no-match judgments converted by the fixed 55-case review, plus 35 comparisons in the separate 50-case stage-two assessment |
| `external-only` | 47 | All still-existing canonical exceptions: 15 completed no-match outcomes and 32 unresolved external curricula |

The 54 revised no-matches come from `docs/qc/counselor-stage2-preexisting-no-match-review.md`. The 35 assessed comparisons come from `data/counselor/qc/stage2-ucr-assessment.json`; the status and completeness reconciliation uses `data/counselor/review-programmes.json`. The 55-case review had one retained exception (cp-000301). The two comparison lists have no overlap.

This is a **historical provenance flag**, not a fresh substantive judgment that each comparison is academically strong or weak. All 89 initial caution settings recorded the same agreed warning:

> UCR offers programmes in related academic fields, but these may differ substantially from the disciplinary programme shown. Important specialist subjects or forms of training may not be available at UCR.

The configuration explicitly lists all 438 permanent case IDs so individual cases can be reassigned by editing one entry; no academic record or comparison has been changed. `external-only` entries for existing canonical exceptions document the category, but the exception renderer already shows only the external curriculum. Changing such an entry to `normal` cannot create an absent comparison: academic generation would be needed first. For existing comparisons, changing the mode back to `normal` immediately restores the full comparison at the next deployment.

## Runtime data architecture

GitHub is the authoritative source. Deployment uploads a version-matched runtime bundle from those repository files, but the running app does **not** fetch counselor data from GitHub.

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

Production and review modes load comparison or exception records from `data/counselor/comparisons/<comparison-id>.json`. Pilot mode loads the five approved fixtures from `data/examples/`.

Review mode exists so completed counselor-production records can be inspected in the real app during incremental corpus production **without creating the final production discovery indexes early**. The review indexes are derived artifacts: they contain exactly the normalized `cp-*.json` completed comparisons and exceptions currently in `data/counselor/comparisons/` and their linked programme-interest rows. Exception results remain searchable; opening one displays the source, supported external curriculum and reason instead of a comparison table.

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

## Deploy to shinyapps.io

Shinyapps.io does not deploy directly from GitHub. The repository therefore contains one deployment script that asks `rsconnect` to build and upload a temporary counselor-only bundle from the authoritative files. It does not create or maintain a second copy of the app.

Install the deployment package once:

```r
install.packages("rsconnect")
```

In the shinyapps.io dashboard, open **Account > Tokens**, reveal the token, and run the displayed `rsconnect::setAccountInfo(...)` command in R. Keep the token and secret out of GitHub.

From the repository root, check the exact runtime selection and package dependencies without publishing:

```bash
Rscript scripts/deploy-counselor-shiny.R --check-bundle
```

Then deploy:

```bash
Rscript scripts/deploy-counselor-shiny.R
```

The default shinyapps.io application name is `ucr-counselor`. If the configured account contains several accounts or a different app name is required, specify them explicitly:

```bash
Rscript scripts/deploy-counselor-shiny.R --account=ACCOUNT --app-name=APP-NAME
```

The upload contains only the counselor `app.R`, `pilot/shared.R`, the required UCR logo, fonts and CSS, the available counselor indexes, their comparison records and the pilot fallback records. It excludes the student app, counselor decision files, registry source data and unrelated website assets.

The script validates every available data mode before deployment. At runtime the app still selects production, review or pilot data in the order documented above. When counselor data changes, update the repository normally, pull the current `main` checkout and run the same deployment command again. Shinyapps.io installs the detected R dependencies and replaces the existing application release.

BA/BSc, discipline and location filters are not claimed as implemented: the current fixture metadata does not reliably supply those distinctions. `degree = BACHELOR` is not a BA/BSc classification.

## Production boundary

Shiny remains the current implementation candidate. Hosting technology can still change later without changing the counselor data contracts: programme metadata, interest discovery index and fixed comparison records remain separate concerns.

## Reviewed audience content and mobile comparisons

The optional canonical `audience` contract is documented in Production Instructions §7.4. Only selected audience prose and ordinary academic facts reach the counselor view. Internal research/context, arbitrary notes and legacy presentation messages are never narrative fallbacks. Unreviewed external-only records retain a status explanation and official link while their component lists are withheld. A reviewed partial list must explicitly identify its verified subset and incompleteness. Existing concepts remain canonical and inform the editorial review.

At widths up to 700px, the original table scrolls between full-width columns. Previous/next, programme selection, current name/position and sticky block titles preserve the row/block structure and deliberate gaps. Back to overview returns to the programme title; desktop keeps the side-by-side table.

Run `npm run test:counselor-audience`, `Rscript scripts/test-counselor-audience.R`, `python scripts/validate-course-descriptions.py` and the existing Shiny/compiler/bundle checks. `node scripts/test-counselor-rendered.mjs` starts local Shiny servers and tests real records plus isolated runtime-only fixtures; it requires Rscript and Playwright Chromium. `UCR_RSCRIPT`, `UCR_PLAYWRIGHT_MODULE` and `UCR_RENDERED_EVIDENCE_DIR` can select local test dependencies/output. The fixtures never write canonical records or presentation settings. This test does not deploy the app or approve academic cases.
