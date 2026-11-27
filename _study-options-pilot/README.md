# Interest-led study-options pilot

[Open the pilot](https://solmyr1980.github.io/ucr-pathways/study-options-pilot/). GitHub Pages serves the checked-in static files in `study-options-pilot/`. The existing homepage has no link to this review pilot.

## Rebuild from the repository root

```sh
python _study-options-pilot/build.py
python _study-options-pilot/verify.py
npm run validate:counselor
python scripts/validate-course-descriptions.py
python scripts/validate-course-feasibility.py data/counselor/comparisons/cp-{000001,000010,000031,000036,000077,000291}.json
```

Build with Python 3. The HTML validator uses lxml. Workbook checks use openpyxl. The feasibility command above uses Bash brace expansion. Commit the source changes and rebuilt HTML/index together on main. After Pages deploys, run `python _study-options-pilot/verify.py --live --browser` to compare all served files with the checkout and exercise navigation. Browser checks use Python Playwright and Chromium. Install its browser with `python -m playwright install chromium` or set `UCR_BROWSER_EXECUTABLE` to a working Chromium executable.

## Academic and search selections

Edit `options.json` for source record, UCR alternative, stable slug, student-facing summary, subject mappings and historical tracks. Within each option, each searchable topic cites counselor interest rows and scheduled UCR course codes. The builder resolves the rows in the current counselor index, checks the canonical assessment and course membership, and obtains the six semesters and code-keyed descriptions directly from the academic sources. `aliases.json` holds student search language. Recheck aliases against every curriculum using that topic when editing them.

The public index contains topic aliases and each UCR option’s slug and topic list. The matcher recognizes phrases before single words and counts each interest once. An unrecognized interest stays in the query and prevents a full match. Results sort by coverage and then by the topic order in each option. The empty search restores ordinary curriculum links. The complete plans and destination lists are in the initial HTML.

| Review example | Search | Historical tracks | Master’s / employers |
| --- | --- | --- | --- |
| Politics, law and public institutions | government and law | POLI, LAWJ, SOCI | 20 / 20 |
| Economics, business and data | business and data | ECON, DATA | 2 / 0 |
| AI, language and the brain | AI and neuroscience | COGN, COMP, LING | 20 / 20 |
| Biomedical science and health | genetics and pharmacology | BIOM, LIFE | 20 / 20 |
| Earth, climate and economics | climate and economics | EART, ENVI, ECON | 20 / 20 |
| Environmental modelling and data science | climate and machine learning | EART, COMP, DATA | 20 / 15 |
| Film, literature and visual culture | film | FTME, LITR, THEA | 20 / 20 |

Try `film and aerospace engineering` for a partial match and `veterinary dentistry` for an empty result. The two environmental options share one counselor source but use distinct approved schedules and track selections.

## Alumni destinations

Use the private `alumni_destinations.xlsx` outside the checkout. `alumni.py` matches each graduate to a curriculum when at least two distinct selected track codes appear across track1–track6. For example, the Earth/climate/economics list uses Earth & Environmental Science, Environmental Studies and Economics. The computational environment plan uses Earth & Environmental Science, Computer Science and Data Science. For economics/business/data, the workbook has Economics and Data Science but no Business track. Broadening that filter to produce more destinations would change the academic basis.

To review a selection, run the first command locally, inspect the distinct destination labels, then edit the relevant entry in `destinations.json`. Verify every selected master's programme–institution pair and employer against the filtered workbook with the second command. Only the selected labels go into the generated pages. The audience sees programmes and employers in separate lists, with no job titles, people, linked histories or group counts.

```sh
python _study-options-pilot/alumni.py /private/path/alumni_destinations.xlsx --candidates film-literature
python _study-options-pilot/alumni.py /private/path/alumni_destinations.xlsx
```

The reader selects explicit master's degree types and expands “Uni” in labels. The editorial selection omits duplicates, ambiguous employers and personal names. Where possible it includes Dutch and international destinations across several countries. Keep sparse selections short and omit empty groups. These are historical examples, independent of current admissions or employment arrangements.

## Scale and delivery checks

`python _study-options-pilot/benchmark.py` creates an in-memory fixture with one entry per canonical counselor UCR alternative. It assigns proxy topics from course overlap solely to approximate full-catalogue size and lookup cost. It does not export the fixture or confer academic approval. `python _study-options-pilot/verify.py --browser --benchmark` runs the same fixture in Chromium.

27 November 2026 measurements: the seven-option index was 3,764 bytes uncompressed. The fixture covered 866 alternatives and was 149,005 bytes. On headless Chromium 156, parsing and matcher initialization took 0.6 ms. Across 500 searches spanning ten queries after 40 warm-up searches, median lookup was 0.1 ms and the 95th percentile was 0.2 ms. These are matcher timings on the test machine. Network transfer and rendering hundreds of result cards were outside the measurement.

The browser checks exercise all seven demonstration searches, partial and empty results, shared query URLs, reset, course disclosures and alumni navigation. They check 320-, 390- and 1,280-pixel viewports with and without JavaScript. The HTML verifier compares each course, description, semester and selected destination to the source, checks the allowlisted public file inventory and compares the live homepage with its repository copy.
