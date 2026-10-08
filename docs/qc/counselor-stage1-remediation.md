# First-stage counselor corrections

The completed audit remains the evidence baseline. This report records implementation only; its live register is `data/counselor/qc/stage1-remediation.json`. UCR comparability is not reassessed here.

## Batch 1 — five representative cases

Status: completed.

| Target | Implemented correction | Remaining work |
|---|---|---|
| cp-000333 — Academic Primary Teacher Education (ALPO) | double-bachelor classification; UU and HU participant identities; four-year full-time entry; withdrawal from standard-only counselor scope with evidence preserved | Verify current combined study load and credit sharing before replacing the embedded 180-EC study_load_ec field. |
| cp-000095 — Pharmaceutical Sciences (Farmaceutische Wetenschappen) | Corrected narrative to 150 EC required major + 30 EC profiling = 180 EC | None within this correction; UCR reassessment remains separate. |
| cp-000293 — Tax Law | Removed outgoing third year from revised curriculum; Replaced unsupported no-match outcome with external-programme-unresolved; Retained independently verified 120 EC without inferred filler | Obtain the revised third-year requirements and applicable cohort/delivery sequence when officially published. |
| cp-000301 — Japanese Studies (Japanstudies) | Normalized instruction metadata now includes documented ENG alongside NLD; Preserved the complete 180-EC Japanese pathway and raw Dutch offering metadata | None within this correction; UCR reassessment remains separate. |
| cp-000244 — Theology | Replaced semester placeholders with individual official course units; Resolved the alleged credit gap using Torah and Prophetic Literature at 6 EC; Corrected neutral delivery selection and conditional language-replacement context | None within this correction; UCR reassessment remains separate. |

## cp-000333

- [Academische lerarenopleiding primair onderwijs current official programme](https://www.uu.nl/bachelors/academische-lerarenopleiding-primair-onderwijs/studieprogramma) — Current identity, curriculum overview and cohort/choice context. Checked 8 October 2026.
- [HU ALPO current entry](https://www.hu.nl/voltijd-opleidingen/academische-lerarenopleiding-primair-onderwijs) — Duration, award/provider and mode facts. Checked 8 October 2026.
- [Official accreditation report BSc Onderwijswetenschappen](https://publicaties.nvao.net/prd/AV-2153_20240415_Rapport_2023%20Rapport%20FSW_%20BSc%20Onderwijswetenschappen_incl%20aanvulling%20v09042024.pdf) — PDF pp.8–9 and12; submitted2023, supplementary report2024. Checked 8 October 2026.
- [ALPO current student programme](https://students.uu.nl/fsw/alpo/mijn-studie/studieprogramma-0) — Integration/award statements and linked2026–2027 timetable. Checked 8 October 2026.
- [ALPO current qualitative curriculum](https://students.uu.nl/sites/default/files/fsw-alpo-curriculum_0.pdf) — Two-page four-year table linked as2026–2027. Checked 8 October 2026.

Verification: Current UU/HU entry pages independently confirm two awards, four years and full-time delivery. Raw offerings, source rows, permanent IDs and production order preserved. Archived decision and comparison retain their original SHA-256 hashes. Full 440-record counselor validation and generated-index checks passed. Replay from the baseline registry reproduced the corrected CSV; other 459 targets remained identical. Conflicting refreshed values and changed provenance were rejected.

## cp-000095

- [OER Bachelor Farmaceutische Wetenschappen 2026–2027](https://assets-us-01.kc-usercontent.com/f55d3574-6c6d-0002-e968-70643a2e365a/38be6b3d-dbda-46a0-8097-8bf01e72a7fe/B%20Farmaceutische%20Wetenschappen%20OER%202026-2027.pdf) — Articles 10.2, 11.3 and 12.1, printed pp. 16–18. Checked 8 October 2026.
- [VU Studiegids — Farmaceutische Wetenschappen](https://studiegids.vu.nl/nl/Bachelor/2026-2027/farmaceutische-wetenschappen) — Programme facts and linked current OER. Checked 8 October 2026.

Verification: Re-read formal OER Articles 11.3 and 12.1; required course weights total 60 + 60 + 30 = 150 EC. Existing components, choices and original UCR assessment remain unchanged. Deterministic canonical regeneration and full counselor validation passed.

The first-stage narrative defect is closed. This does not establish that the retained UCR no-match judgment is correct.

## cp-000293

- [Tax Law current study-guide product](https://studiegids.universiteitleiden.nl/api/product?code=BA-FIS&type=STUDY&year=2261&language=en) — Year 2261; degree description, annual group rules and module membership. Checked 8 October 2026.

Verification: Re-read explicit cohort notices in the current official BA-FIS product. Fetched each of the 24 positive-credit revised modules: every unit is 5 EC, closing 60 + 60 = 120 EC. Regenerated canonical exception through the unchanged compiler; all three record validators and generated-index check passed.

The unsupported claim of a complete current 180-EC curriculum is corrected. Complete external reconstruction remains blocked by the university's unpublished revised third year; the old UCR no-match conclusion is no longer the active exception outcome.

## cp-000301

- [Japanese Studies current study-guide product](https://studiegids.universiteitleiden.nl/api/product?code=BA-JAP&type=STUDY&year=2261&language=en) — Year 2261; programme, annual/group rules, membership and choices. Checked 8 October 2026.
- [japanstudies OER2026–2027](https://www.organisatiegids.universiteitleiden.nl/binaries/content/assets/geesteswetenschappen/oer/2026-2027/ba-oso-japanstudies-2026-2027.pdf) — Articles2.2/2.9/4.2; pp.2,4–7. Checked 8 October 2026.
- [Japan in the 21st Century: Sociological Perspectives current module](https://studiegids.universiteitleiden.nl/api/product?code=5691VGMY&type=MODULE&year=2261&language=en) — Credit and EDUCATION_LANGUAGE; required programme membership. Checked 8 October 2026.
- [Arts and Material Culture of Japan current module](https://studiegids.universiteitleiden.nl/api/product?code=5691ITAMY&type=MODULE&year=2261&language=en) — Credit and EDUCATION_LANGUAGE; required programme membership. Checked 8 October 2026.
- [Introduction to Modern Japanese History current module](https://studiegids.universiteitleiden.nl/api/product?code=5691VMGS1Y&type=MODULE&year=2261&language=en) — Credit and EDUCATION_LANGUAGE; required programme membership. Checked 8 October 2026.
- [Power, Development and Conflict in Asia current module](https://studiegids.universiteitleiden.nl/api/product?code=5691VPDCAY&type=MODULE&year=2261&language=en) — Credit and EDUCATION_LANGUAGE; required programme membership. Checked 8 October 2026.

Verification: Four required first-year MODULE records explicitly specify EDUCATION_LANGUAGE = ENG; no inference from course title or studied language. Permanent ID, source row, offering ID, delivery modes and all 24 comparator components are unchanged. Both registry corrections replay from the pre-correction baseline; other 458 targets and raw offerings are unchanged. Deterministic canonical regeneration, all record validators, registry replay check and generated review-index check passed.

NLD remains the formal main programme classification. NLD + ENG represents documented instruction across required courses, not universal English teaching or Japanese-medium instruction. The adopted OER remains audited provenance; direct fresh PDF retrieval returned an HTML verification wall.

## cp-000244

- [Theology programme and courses](https://www.tilburguniversity.edu/education/bachelors-programs/theology/program-and-courses) — 2026 entrant tables and delivery facts. Checked 8 October 2026.
- [Published TST Education and Examination Regulations 2026–2027](https://oer.tilburguniversity.edu/183b1eaf-bb6b-4ff0-bee5-e9b4e5a536e9/) — Public university reader; published version 14 September 2026 and degree-specific Appendix I §11. Checked 8 October 2026.
- [Appendix I: programme-specific Theology requirements 2026–2027](https://api.docfield.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6IjNmNjY5NTUwLTViNjQtNDkwNy1iZGIyLTFhNGU3ZTdhMjJhYSIsInB1ciI6ImJsb2JfaWQifX0=--371a54676e9e4f62ebdd3edf5837e2b96baf014d/Appendix%20I%202026-2027.pdf) — §§3–5, 10–11; appendix PDF pp. 12–16, printed pp. 55–59. Checked 8 October 2026.

Verification: Downloaded and visually inspected the formal September 2026 cohort table and mandatory/rotating-course legend, printed pages 58–59. Individual course weights close 60 + 60 + 60 = 180 EC, with 30 EC genuine mobility/minor space and thesis 9 counted once. All 12 EC of embedded skills remain within credited courses; no inferred missing unit or duplicated parent block. Deterministic canonical regeneration, all record validators, full 440-record counselor validation and generated-index checks passed.

The explicitly dated cohort appendix takes precedence over the general webpage's 3-EC course label. The general published reader's stale effective-date clause remains documented. External correction closure does not validate the retained UCR no-match conclusion.

## Batch 1 validation and population at completion

All five cases are processed. Three first-stage findings are resolved; ALPO retains a current credit-sharing question, and Tax Law awaits its revised third year. Full-corpus validation and generated-index checks passed. Registry overrides replay from the initial correction baseline and preserve all other targets and raw provenance. Each repaired active decision deterministically regenerates its committed canonical record.

At the completion of batch 1, the registry retained 460 permanent targets: 440 are in scope and have canonical records (301 comparisons and 139 exceptions); 20 are outside scope. Exception types: 116 no-defensible-ucr-match, 21 external-programme-unresolved and 2 registry-exception. No in-scope record is missing. Original audit population counts remain historical. Independent UCR reassessment remains pending.

## Batch 2 — next five cases in audit order

Status: completed. Independent UCR reassessment remains separate.

| Target | Implemented correction | Remaining work |
|---|---|---|
| cp-000040 — German Language and Culture | Corrected prospective academic-year labels and current formal authority; Restored year-two genuine free 30 and formal restrictions; Removed unverified duplicated third-year 15; published explicit external-programme-unresolved outcome | Obtain a current ordinary-route single-cohort repeat/replacement rule for LET-DTCB229, LET-DTCB225 and LET-DTCB235, or verify an applicable approved Article6 alternative. |
| cp-000050 — Classics (Greek and Latin Language and Culture) | Updated year-three label to 2029–2030 and stated the prospective 2027-entry sequence; Retained the supported 180-EC domestic pathway and prospective-cohort qualification | None within this correction; UCR reassessment remains separate. |
| cp-000051 — Human Neuroscience | Removed the unsupported current 66-EC prospectus claim; Refreshed the unresolved rationale to the present development notice and adopted OER | Obtain the remaining 16 EC third-year requirements and final applicable second-/third-year allocation when officially published. |
| cp-000061 — Notarial Law | Replaced broken English EER reference with accessible adopted Dutch 2026–2027 OER and index; Made current formal source primary and distinguished prospective pages | None within this correction; UCR reassessment remains separate. |
| cp-000070 — Chemistry (Scheikunde) | Reconstructed current ordinary formal allocation: 126 required + 36 conditioned choice + 12 research + 6 genuinely free EC; Removed extra compulsory Writing about Science and retained one 3-EC writing requirement; Instantiated the 36-EC restricted choice, preserving two valid prior selections and adding 24 EC by formal list order; Corrected prospective-year context and removed an unsupported formal-route label | None within this correction; UCR reassessment remains separate. |

### cp-000040

- [Studieprogramma Duitse Taal en Cultuur jaar 1](https://www.ru.nl/opleidingen/bachelors/duitse-taal-en-cultuur/studieprogramma-duitse-taal-en-cultuur-jaar-1) — Indicative year label and required-course table. Checked 8 October 2026.
- [Studieprogramma Duitse Taal en Cultuur jaar 2](https://www.ru.nl/opleidingen/bachelors/duitse-taal-en-cultuur/studieprogramma-duitse-taal-en-cultuur-jaar-2) — Required courses, Studeren in het buitenland and Vrije ruimte. Checked 8 October 2026.
- [Studieprogramma Duitse Taal en Cultuur jaar 3](https://www.ru.nl/opleidingen/bachelors/duitse-taal-en-cultuur/studieprogramma-duitse-taal-en-cultuur-jaar-3) — Required-course and minor tables. Checked 8 October 2026.
- [German Language and Culture programme-specific OER 2026–2027](https://www.ru.nl/ru-bestanden/oerbdtc2627) — Articles 5–7 and 10, pp.6–9. Checked 8 October 2026.
- [Faculty of Arts general bachelor OER 2026–2027](https://www.ru.nl/ru-bestanden/oeralgemeenbachelor2627) — Article10, pp.8–9. Checked 8 October 2026.

Verification: Fresh downloads of current prospectus pages and both adopted OERs. Visually inspected OER p.7: three identical codes repeat in B2 and B3; 60 + 60 + 45 = 165 without counting them twice. Target validators, deterministic regeneration and generated-index check passed.

The original audit confirmed the prospectus field basis, not an independently verified current formal pathway. The newly retrieved 2026–2027 OER exposes a separate cohort/repeat question; a future prospectus or conditional alternative is not substituted silently.

### cp-000050

- [Studieprogramma Griekse en Latijnse Taal en Cultuur jaar 1](https://www.ru.nl/opleidingen/bachelors/griekse-en-latijnse-taal-en-cultuur/studieprogramma-griekse-en-latijnse-taal-en-cultuur-jaar-1) — Indicative year label; compulsory-course and minor/free-space tables. Checked 8 October 2026.
- [Studieprogramma Griekse en Latijnse Taal en Cultuur jaar 2](https://www.ru.nl/opleidingen/bachelors/griekse-en-latijnse-taal-en-cultuur/studieprogramma-griekse-en-latijnse-taal-en-cultuur-jaar-2) — Indicative year label; compulsory-course and minor/free-space tables. Checked 8 October 2026.
- [Studieprogramma Griekse en Latijnse Taal en Cultuur jaar 3](https://www.ru.nl/opleidingen/bachelors/griekse-en-latijnse-taal-en-cultuur/studieprogramma-griekse-en-latijnse-taal-en-cultuur-jaar-3) — Indicative year label; compulsory-course and minor/free-space tables. Checked 8 October 2026.

Verification: Fresh current year-page downloads show 2027–2028/2028–2029/2029–2030. All 25 credited components, domestic selection and existing UCR assessment retained unchanged. Deterministic regeneration, target validators and generated-index check passed.

This closes the source-context finding. No historical page archive establishes when the label changed, so the correction does not retrospectively classify the original production as outdated or erroneous.

### cp-000051

- [Humane Neurowetenschappen — OER Bachelor 2026–2027](https://www.ru.nl/ru-bestanden/fsw-oer-2026-2027-hnw-bachelor) — Articles 9.4–9.6, printed pp. 16–18. Checked 8 October 2026.
- [Studieprogramma bachelor Humane Neurowetenschappen jaar 2](https://www.ru.nl/opleidingen/bachelors/humane-neurowetenschappen/studieprogramma-van-deze-opleiding/studieprogramma-bachelor-humane-neurowetenschappen-jaar-2) — Development caveat and required-course table. Checked 8 October 2026.
- [Studieprogramma bachelor Humane Neurowetenschappen jaar 3](https://www.ru.nl/opleidingen/bachelors/humane-neurowetenschappen/studieprogramma-van-deze-opleiding/studieprogramma-bachelor-humane-neurowetenschappen-jaar-3) — Over dit studieprogramma and total EC. Checked 8 October 2026.

Verification: Fresh OER download and current year-two/year-three pages. Visually inspected OER p.18: research 18 and genuine free 26; supported 60 + 60 + 44 = 164. All 23 component weights preserved; provisional learning lines remain explicit. Deterministic regeneration, target validators and generated-index check passed.

The revised current rationale closes the stale-source claim; it does not resolve the university’s unpublished third-year allocation. The historical 66-EC calculation remains provenance only.

### cp-000061

- [OER Faculteit der Rechtsgeleerdheid 2026–2027](https://www.ru.nl/sites/default/files/2026-09/oer_2026-2027-fdr.pdf) — Annex VI, Article 4, printed pp. 56–57. Checked 8 October 2026.
- [OER Faculteit der Rechtsgeleerdheid](https://www.ru.nl/studenten/onderwijs-volgen/regels-en-richtlijnen/onderwijs-en-examenregelingen/rechtsgeleerdheid) — Current-year OER link and annual-regulation notice. Checked 8 October 2026.

Verification: Fresh current Dutch OER and official index downloads. Inspected formal Annex VI Article 4, printed pp.56–57; 60 + 60 + 55 + 5 = 180 matches all 32 retained component weights. No courses, choice instantiation, route or UCR assessment changed. Deterministic regeneration, target validators and generated-index check passed.

The historical availability of the replaced English URL remains unverified. Its former access failure does not establish a substantive curriculum error.

### cp-000070

- [Bachelor OER 2026–2027 — Chemistry (Dutch)](https://www.ru.nl/ru-bestanden/oer-25-26-ba-chemistry-nl) — Articles 7.3–7.5, printed pp. 16–19. Checked 8 October 2026.
- [EER 2026–2027 — Bachelor Chemistry (English translation)](https://www.ru.nl/sites/default/files/2026-09/20260905-oer-26-27-ba-chemistry_eng-gb-juiste-tabellen.pdf) — Articles 7.4 and 8.1, later-course table and transitional provisions. Checked 8 October 2026.
- [OER — Faculteit der Natuurwetenschappen, Wiskunde en Informatica](https://www.ru.nl/studenten/onderwijs-volgen/regels-en-richtlijnen/onderwijs-en-examenregelingen/natuurwetenschappen-wiskunde-en-informatica) — Current 2026–2027 regulations links; precedence notice. Checked 8 October 2026.
- [Chemistry — jaar 1](https://www.ru.nl/opleidingen/bachelors/scheikunde/studieprogramma/studieprogramma-bachelor-chemistry-jaar-1) — Year label; required-course, placement and choice tables. Checked 8 October 2026.
- [Chemistry — jaar 2](https://www.ru.nl/opleidingen/bachelors/scheikunde/studieprogramma/studieprogramma-bachelor-chemistry-jaar-2) — Year label; required-course, placement and choice tables. Checked 8 October 2026.
- [Chemistry — jaar 3](https://www.ru.nl/opleidingen/bachelors/scheikunde/studieprogramma/studieprogramma-bachelor-chemistry-jaar-3) — Year label; required-course, placement and choice tables. Checked 8 October 2026.

Verification: Fresh adopted Dutch/English OER and current index downloads; Dutch index confirms precedence. Visually inspected formal p.17 and re-read Articles 7.3–7.5: 60 + 66 + 36 + 12 + 6 = 180. All first-/second-year weights retained; duplicate mandatory writing 3 removed, free 27 corrected to 6, and six BC1 selections add 24. All eight selected BC1 options are distinct; alternate magnetic-resonance and philosophy units are not stacked. Deterministic regeneration, target validators, generated-index checks, compiler regression tests and full-corpus validation passed.

The formal degree allocation and one neutral credited choice example are verified. The BC1 annual-offering caveat remains explicit; no enrolment or timetable guarantee is claimed. Closure of the external defect does not validate the retained UCR no-match judgment.

### Batch 2 validation

All five corrections are implemented. 3 findings are resolved; 2 cases retain explicit external research questions. Target validators, deterministic compiler comparisons, generated-index checks, compiler regression tests and full-corpus validation passed. The original audit evidence and batch 1 decisions remain preserved.

The live corpus still contains 440 in-scope records: 301 comparisons and 139 exceptions. Exception types: 22 external-programme-unresolved, 115 no-defensible-ucr-match, 2 registry-exception. No registry identities, scope or permanent IDs changed in batch 2.

The compiler and app regression tests now use frozen historical exception fixtures. Their checks still reject incomplete no-match curricula and verify both no-match and unresolved app messages. Production validators were not changed.

## Batch 3 — next five cases in audit order

Status: completed. Independent UCR assessment remains separate.

| Target | First-stage outcome | Remaining external question |
|---|---|---|
| cp-000076 — Mathematics (Wiskunde) | Rebuilt current ordinary OER pathway at 180 EC with 54+6+24+36+48+12 allocation; Instantiated restricted choices with 6 EC from year three; removed old-cohort and universal supplementary-mathematics assumptions; Corrected source labels and marked separate UCR assessment pending | None; UCR assessment remains separate. |
| cp-000097 — Medicine (Geneeskunde) | Replaced empty external reconstruction with adopted 180-EC Compas curriculum; Verified minor 24 EC and thesis 6 EC; embedded clinical/research activities counted once; Removed unsupported external inaccessibility claim and recorded UCR assessment pending | None; UCR assessment remains separate. |
| cp-000098 — History (Geschiedenis) | Expanded supported 60-EC subset into complete adopted Dutch general 180-EC pathway; Instantiated two year-two choices and one additional research seminar without stacking alternatives; Closed external evidence gap and marked UCR assessment pending | None; UCR assessment remains separate. |
| cp-000099 — Health and Life Sciences (Gezondheid en Leven) | Corrected normalized language ENG to NLD from formal OER and current study guide; Preserved raw ENG provenance and the supported 90-EC subset | Applicable 2026-entry year-two/year-three course EC and complete restricted-choice/research allocation remain unpublished in the checked sources. |
| cp-000100 — Health Sciences (Gezondheidswetenschappen) | Rechecked current formal evidence and confirmed existing supported 150-EC subset and exception require no correction | Applicable new-cohort third-year Methodologie 5, professional preparation and placement/thesis EC and choice rules remain unspecified in the checked sources. |

The explicit `ucr-assessment-pending` handoff requires a verified complete 180-EC external reconstruction and shows that UCR assessment has not yet been completed. It prevents resolved external evidence gaps from being presented as unresolved, or superseded UCR judgments from appearing current. Existing no-match requirements remain unchanged. This state is for authorized remediation, not a shortcut for new production.

### cp-000076

- [radboud_mathematics_dutch_oer_b4](https://www.ru.nl/sites/default/files/2026-08/bachelor-oer-26-27-wiskunde_20260818.pdf) — Articles 7.3–7.4, printed pp. 15–18; Article 8.1, printed pp. 24–25. Checked 8 October 2026. SHA-256: `0a67c12172a8fe40e0ef9197694c1aa7887cfc1d2b3f56d6817f1fc763e818bd`.
- [radboud_science_dutch_index_b4](https://www.ru.nl/studenten/onderwijs-volgen/regels-en-richtlijnen/onderwijs-en-examenregelingen/natuurwetenschappen-wiskunde-en-informatica) — Current 2026–2027 regulations links; precedence notice. Checked 8 October 2026. SHA-256: `91467f69162719dee523e7d270420d593a6eb591b46cacb0357bb1e2672e697a`.
- [radboud_mathematics_y1_b4](https://www.ru.nl/opleidingen/bachelors/wiskunde/studieprogramma/studieprogramma-bachelor-wiskunde-jaar-1) — Indicative label, required table and free-space explanation. Checked 8 October 2026. SHA-256: `b9da3f65e0444fcad133f8808ed6b4e1d0a0f2ca7129dd78a1d19457ca0c8def`.
- [radboud_mathematics_y2_b4](https://www.ru.nl/opleidingen/bachelors/wiskunde/studieprogramma/studieprogramma-bachelor-wiskunde-jaar-2) — Indicative label and Mathematics-line explanation. Checked 8 October 2026. SHA-256: `f555ae312337e88503e7bd730faf3d45115c40385e519165ca4c6c04ec26adc1`.
- [radboud_mathematics_y3_b4](https://www.ru.nl/opleidingen/bachelors/wiskunde/studieprogramma/studieprogramma-bachelor-wiskunde-jaar-3) — Required table and thesis description. Checked 8 October 2026. SHA-256: `e9cfeb1b22fefe987b816bdef0928873d5f84d4559fe8d83a28ae490ebed4254`.

Verification: Formal OER articles 7.3–7.5 and 8.1 reread; restricted table visually checked. All credited components total 180 EC; zero-credit RADAr excluded from the credit total. Target validation and deterministic compiler regeneration passed.

Current OER governs formal requirements. Indicative public offerings do not guarantee the timetable of a 2026 entrant; the original UCR conclusion is preserved as superseded provenance.

### cp-000097

- [vu_medicine_guide_b5](https://studiegids.vu.nl/nl/Bachelor/2026-2027/geneeskunde) — Programme facts, current OER link and embedded-stage descriptions. Checked 8 October 2026. SHA-256: `ac0eb385b8ffee3792d10e1478f178327e052ae29d9141f2d5a443d198b146e5`.
- [vu_medicine_oer_b5](https://assets-us-01.kc-usercontent.com/f55d3574-6c6d-0002-e968-70643a2e365a/151c0dc2-797e-46fb-b61c-ac16761ceb04/1%20OER%20Ba%20VUmc-compas%202026-2027%20DEF.pdf) — Articles 11.1–11.5, PDF pp. 15–18; Articles 12.1–12.3, PDF pp. 21–23 (repeated printed footer numbering). Checked 8 October 2026. SHA-256: `104096617472d5d1f9e7391e7df1bd4ed5f921b658a701e0b15a2dd8434b4d11`.
- [vu_medicine_transition_b5](https://vu.nl/nl/student/studenten-bachelor-geneeskunde/overgangsregeling-vumed360) — Publication update 26 August 2026; final teaching and validity dates. Checked 8 October 2026. SHA-256: `3f0b5d55e55676eb3ab3f11ba1ac152e7553406dc1805db320940a04d47fabb6`.

Verification: Current OER tables articles 11.3–12.3 independently read; first-year table visually checked. Twenty-six major units at 6 EC plus 24-EC minor total 180 EC. Current transition rules confirm the Fall 2026 Compas sequence. Target validation and deterministic compiler regeneration passed.

Minor selection is subject to university admission/capacity; current listing is not a guaranteed future enrolment offer. No independent clinical/UCR reassessment performed.

### cp-000098

- [vu_history_guide_b5](https://studiegids.vu.nl/nl/Bachelor/2026-2027/geschiedenis) — Programme facts and linked current regulations. Checked 8 October 2026. SHA-256: `6a1be9e568f767a104b0ccbcaa161d93d587e0fc31073bdcbe1bf168c5182195`.
- [vu_history_oer_b5](https://assets-us-01.kc-usercontent.com/f55d3574-6c6d-0002-e968-70643a2e365a/60718e0d-72f7-4581-85a0-a015b1d5063f/OER%2026-27%20BA%20Geschiedenis%20NL%2027.08.2026.pdf) — Annex, PDF pp. 22–23: Dutch trajectory and Algemeen third year; adoption statement p. 19. Checked 8 October 2026. SHA-256: `1dddd595135db458ac58a6d02c809b6ad0bfb009b0c52e26f733bad692795251`.

Verification: Adopted Dutch annual plans pp. 22–23 reread; general year-three table visually checked. 60 first + 48 required second + 12 selected second + 30 profiling + 9 research + 9 selected seminar + 3 colloquium + 9 thesis = 180 EC. Target validation and deterministic compiler regeneration passed.

UCR History plausibility in the historical record is not a completed feasibility assessment. No UCR schedule or comparison is generated in this first-stage correction.

### cp-000099

- [vu_health_life_guide_b5](https://studiegids.vu.nl/nl/Bachelor/2026-2027/gezondheid-en-leven) — Programme facts and curriculum change notice. Checked 8 October 2026. SHA-256: `d1f30392babe1005d82df4738431ca4b22381d38215bc97f0ca32459add9cd54`.
- [vu_health_life_oer_b5](https://assets-us-01.kc-usercontent.com/f55d3574-6c6d-0002-e968-70643a2e365a/ede76ee3-4e16-41c8-8ccc-ce484951eac1/B%20Gezondheid%20en%20Leven%20OER%202026-2027.pdf) — Articles 10.2/10.4, PDF pp. 15/18; 11.3, pp. 19–22; 12.1, pp. 22–23. Checked 8 October 2026. SHA-256: `65a1bc9b2119af5da6b34e408b57dd13254910c644b5992d38006b0a15ea05a4`.
- [vu_health_life_revision_b5](https://assets-eu-01.kc-usercontent.com/ff31ad68-341e-015e-fb52-24df7a00ecea/f4d7310d-6aba-45d8-aa25-ab026e822f74/Toelichting%20Curriculumherziening%20website%20G_L.pdf) — PDF pp. 1–2 and 4–6; year diagram visually checked. Checked 8 October 2026. SHA-256: `14085ef69beb61154eb7dfdaa9528aa5d02a9bbfe01d81951ef8f074fdc1186f`.

Verification: Formal OER article 10.4.1 explicitly says instruction is Dutch. Current first-year ten 6-EC units and minimum minor 30 unchanged; no outgoing thesis weights imported. Guarded registry replay, metadata regeneration and target validation passed.

No regular monitoring is scheduled; this correction pass is complete with a specific unresolved external question.

### cp-000100

- [vu_health_sciences_guide_b5](https://studiegids.vu.nl/nl/Bachelor/2026-2027/gezondheidswetenschappen) — Programme facts and linked current OER. Checked 8 October 2026. SHA-256: `fbfa908ef79af381b23d15fca1bb560be8f8d549e39bf9f5678d55c2f112eeb5`.
- [vu_health_sciences_oer_b5](https://assets-us-01.kc-usercontent.com/f55d3574-6c6d-0002-e968-70643a2e365a/4d43408f-790d-4f02-94d4-8aa29ae358d5/B%20Gezondheidswetenschappen%20OER%202026-2027.pdf) — Article 9.1, PDF p. 13; Articles 11.3–12.1, pp. 19–22; Article 15.2, p. 22. Checked 8 October 2026. SHA-256: `9cb56edc7a48cbadfd4a9a4c7ec42ea1293e2a7e976fa22b4fecd4289083b233`.
- [vu_health_sciences_prospectus_b5](https://vu.nl/nl/onderwijs/bachelor/gezondheidswetenschappen/inhoud) — Third-year description. Checked 8 October 2026. SHA-256: `d583b11eb34ed2fa2936062e46e016acf489a6465c0cadf45c6aa0eea248e1f7`.

Verification: Fresh 2026–2027 OER and current prospectus checked against the existing decision. Existing decision and canonical comparison retained byte-for-byte; 120 EC years one/two plus 30-EC minor remains supported. No unknown weights inferred by subtraction and no outgoing-cohort units imported.

This is a completed no-change verification within batch 3, not an instruction for ongoing monitoring.

### Batch 3 validation

Five cases processed: three external findings resolved; two retain specific external factual questions. Health Sciences required no academic change. Mathematics, Medicine and History have complete 180-EC external reconstructions and explicitly await separate UCR assessment. No recurring monitoring was created.

Target validators, deterministic compiler comparisons, guarded registry replay, generated-index checks, compiler regressions and full-corpus validation passed. GitHub build, review and Shiny results are verified after publication. The original audit remains unchanged.

The live corpus contains 440 in-scope records: 301 comparisons and 139 exceptions. Exception types: 20 external-programme-unresolved, 114 no-defensible-ucr-match, 2 registry-exception, 3 ucr-assessment-pending. The normalized Health and Life Sciences language is NLD; its raw ENG provenance remains unchanged. No identity or production-scope change.

## Batch 4 — next five cases in audit order

Status: in-progress. Independent UCR assessment remains separate.

| Target | First-stage outcome | Remaining external question |
|---|---|---|
| cp-000119 — Bachelor Theologie en Religiewetenschappen | Reconstructed 26 official components totaling 180 EC with neutral restricted choices and 30 EC profiling; Corrected route, adopted-year context and six-year part-time pacing; Supplemented normalized instruction languages; replaced obsolete source-access exception with UCR-assessment-pending | None within this correction. |
| cp-000134 — Bachelor Fiscal Economics | Corrected lifecycle to teach-out-only and removed active eligibility/production order; Archived prior decision and canonical record unchanged with SHA-256 hashes; Corrected normalized instructional languages to Dutch and English; preserved permanent identity and raw provenance | None within this correction. |
| cp-000149 — General Cultural Studies (Algemene Cultuurwetenschappen) | Added the dated programme-specific OER and corrected the claim that only general regulations exist; Reconfirmed the current guide conflict; narrowed the unresolved reason to current-cohort applicability | Obtain the controlling 2026–2027 programme-specific OER/implementation rules or university clarification reconciling the current diagram and course roster. |
| cp-000156 | Pending | Pending |
| cp-000175 | Pending | Pending |

### cp-000119

- [VU current Theology and Religious Studies study guide](https://studiegids.vu.nl/nl/Bachelor/2026-2027/theologie-en-religiewetenschappen) — Programme facts and linked adopted OER. Checked 8 October 2026. SHA-256: `281fbc95c85eadff7932d93eb2e5953a9c2d4006b0e6988f6c831e6e461c4741`.
- [VU Theology and Religious Studies OER 2026–2027](https://assets-us-01.kc-usercontent.com/f55d3574-6c6d-0002-e968-70643a2e365a/110b4a0f-1fe1-40b1-a797-60a6aab14bd4/OER%2026-27%20B%20TRS%20NL.pdf) — Article 10.4, 11–12 and Annex 1, physical PDF p.26 (appendix 5/34). Checked 8 October 2026. SHA-256: `7a22c65e3c53237a0abed4575d8a26b25afcbf98fbf963fca4c91425edf11694`.
- [VU future Zingeving, geestelijke verzorging en samenleving track](https://vu.nl/nl/onderwijs/bachelor/theologie-en-religiewetenschappen/traject/zingeving-geestelijke-verzorging-en-samenleving/inhoud) — Programme starting in 2027 label. Checked 8 October 2026. SHA-256: `dfa5fdb88a340c0c1d36be01919423067131af2350fe081da87d7cb6e7001723`.

Verification: Fresh current OER retrieved and Annex 1 visually inspected. Independent component arithmetic closes 60+60+60; part-time pacing closes 36+24 across each pair. Deterministic compiler, target validators, generated-index checks and guarded registry replay passed.

Original access report is historical evidence, not a claim about present retrieval. The corrected external pathway is not independently assessed against UCR.

### cp-000134

- [Maastricht SBE Bachelor EER 2026–2027](https://www.maastrichtuniversity.nl/file/sbe-bsc-eer-2026-2027pdf) — Article 16.8, printed pp.60–61; Appendix I Article 17, printed pp.100–102. Checked 8 October 2026. SHA-256: `8ba56bbf673871af380c3436f2d409807628b17369ec1e55f56271e42d244c95`.

Verification: Fresh adopted EER confirms lifecycle, deadlines and languages. Archived files are byte-identical to their pre-correction versions. Guarded registry replay, scope reconciliation, full-corpus validation and generated-index checks passed.

A historical 180-EC award does not supply a current intake pathway. No UCR assessment is needed under active-production exclusion.

### cp-000149

- [OU General Cultural Studies 2026–2027 programme](https://www.ou.nl/en/-/bcw-2026-2027_bachelor-algemene-cultuurwetenschappen) — Degree facts and themes. Checked 8 October 2026. SHA-256: `e42645257af0c579c5a3e05ae66ff2b43ee875700afef2252ae6c326ecb5e48f`.
- [OU General Cultural Studies study guide 2026–2027](https://www.ou.nl/digitaldownloads/BD476.pdf) — Curriculum diagram, physical PDF p.7; annual roster and regulations notice. Checked 8 October 2026. SHA-256: `ac4f2b76ed5462800fe4a66e3257a7d48479c115c14a720c58669ef7b71d90ea`.
- [OU official documents page](https://www.ou.nl/documenten) — Redirect to official regulations FAQ. Checked 8 October 2026. SHA-256: `d2d20431824986eda623080329ed22605adf8cc358a750b64cd4c18bf8b0e2fd`.
- [OU programme-specific General Cultural Studies OER 2025–2026](https://vraagenantwoord.ou.nl/privatedata/docs/OER_WO_bacheloropleiding_Algemene_cultuurwetenschappen.pdf) — Two-page programme-specific curriculum allocation recorded by the original audit. Content/dated allocation preserved from the 7 October audit. Current direct retrieval returned HTTP 502 and web retrieval timed out; no fresh local PDF or hash is claimed.

Verification: Fresh current degree page and study guide retrieved; diagram arithmetic is 50+135=185 against 180 stated. Older allocation retained as dated audit evidence; fresh older-PDF retrieval failure is recorded honestly. Empty component list retained; deterministic compiler, target validators and generated-index checks passed.

The older coherent allocation is not used to invent a current restricted-choice block or override changed course membership. This finite source check is complete; no monitoring is scheduled.
