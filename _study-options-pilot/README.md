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

| Review example | Search | Historical tracks | Postgraduate programmes / employers |
| --- | --- | --- | --- |
| Politics, law and public institutions | government and law | POLI, LAWJ, SOCI | 20 / 20 |
| Economics, business and data | business and data | ECON, DATA | 2 / 0 |
| AI, language and the brain | AI and neuroscience | COGN, COMP, LING | 20 / 17 |
| Biomedical science and health | genetics and pharmacology | BIOM, LIFE | 20 / 20 |
| Earth, climate and economics | climate and economics | EART, ENVI, ECON | 20 / 19 |
| Environmental modelling and data science | climate and machine learning | EART, COMP, DATA | 15 / 11 |
| Film, literature and visual culture | film | FTME, LITR, THEA | 17 / 12 |

Try `film and aerospace engineering` for a partial match and `veterinary dentistry` for an empty result. The two environmental options share one counselor source but use distinct approved schedules and track selections.

## Alumni destinations

The public selection comes from the **Shortlists** sheet of the private reviewed curriculum coverage workbook. Match each pilot option by comparison ID and UCR alternative ID. The underlying review uses eligible first postgraduate degrees (deg1) and eligible jobs from job1–job5 for alumni who completed at least two related historical tracks. It checks how the recorded programme or role relates to the scheduled UCR courses. Treat the destinations as historical examples.

After public-use approval, run the following commands from the repository root with the workbook outside the checkout. The first updates the pilot selection. The second checks the labels and counts against the workbook. Then rebuild and verify the HTML as described above.

```sh
python _study-options-pilot/alumni.py "/private/path/UCR Alumni Curriculum Coverage.xlsx" --write
python _study-options-pilot/alumni.py "/private/path/UCR Alumni Curriculum Coverage.xlsx"
```

Publish only the selected programme–institution pairs and employer names. Keep sparse lists short and omit empty groups. Where a list includes a professional doctorate, the page uses “Postgraduate programmes”. Lists containing only master’s-level awards use “Master’s programmes”.

## Scale and delivery checks

`python _study-options-pilot/benchmark.py` creates an in-memory fixture with one entry per canonical counselor UCR alternative. It assigns proxy topics from course overlap solely to approximate full-catalogue size and lookup cost. It does not export the fixture or confer academic approval. `python _study-options-pilot/verify.py --browser --benchmark` runs the same fixture in Chromium.

27 November 2026 measurements: the seven-option index was 3,764 bytes uncompressed. The fixture covered 866 alternatives and was 149,005 bytes. On headless Chromium 156, parsing and matcher initialization took 0.6 ms. Across 500 searches spanning ten queries after 40 warm-up searches, median lookup was 0.1 ms and the 95th percentile was 0.2 ms. These are matcher timings on the test machine. Network transfer and rendering hundreds of result cards were outside the measurement.

The browser checks exercise all seven demonstration searches, partial and empty results, shared query URLs, reset, course disclosures and alumni navigation. They check 320-, 390- and 1,280-pixel viewports with and without JavaScript. The HTML verifier compares each course, description, semester and selected destination to the source, checks the allowlisted public file inventory and compares the live homepage with its repository copy.
