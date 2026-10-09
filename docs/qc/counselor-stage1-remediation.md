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

Status: completed. Independent UCR assessment remains separate.

| Target | First-stage outcome | Remaining external question |
|---|---|---|
| cp-000119 — Bachelor Theologie en Religiewetenschappen | Reconstructed 26 official components totaling 180 EC with neutral restricted choices and 30 EC profiling; Corrected route, adopted-year context and six-year part-time pacing; Supplemented normalized instruction languages; replaced obsolete source-access exception with UCR-assessment-pending | None within this correction. |
| cp-000134 — Bachelor Fiscal Economics | Corrected lifecycle to teach-out-only and removed active eligibility/production order; Archived prior decision and canonical record unchanged with SHA-256 hashes; Corrected normalized instructional languages to Dutch and English; preserved permanent identity and raw provenance | None within this correction. |
| cp-000149 — General Cultural Studies (Algemene Cultuurwetenschappen) | Added the dated programme-specific OER and corrected the claim that only general regulations exist; Reconfirmed the current guide conflict; narrowed the unresolved reason to current-cohort applicability | Obtain the controlling 2026–2027 programme-specific OER/implementation rules or university clarification reconciling the current diagram and course roster. |
| cp-000156 — Theologie | Scoped language/exegesis requirements to the selected language pathway and predikantsmaster exit profile; Documented the mutually exclusive language-free replacements; preserved selected Systematische Theologie route and all 180 EC | None within this correction. |
| cp-000175 — Medicine | Moved Bachelor Project execution/thesis context to Competency Development 3.2 and retained preparation/proposal in 3.1; Preserved the 10/20-EC competency split, complete 180 EC and selected community; no extra thesis credit | None within this correction. |

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

### cp-000156

- [PThU Bachelor Theology OER 2026–2027](https://www.pthu.nl/over-pthu/organisatie/regelingen-en-rechtspositie/oer-bachelor-theologie-2026-2027.pdf) — Article 8.1 and Annex 2, printed pp.45–46. Checked 8 October 2026. SHA-256: `2ac1be172c9b8373181a99d239d173f849fd5290c3bb1f1ede81e2b97acd3e76`.
- [PThU current Utrecht Theology bachelor](https://www.pthu.nl/onderwijs/bachelor/theologie-utrecht/) — Programme identity and language options. Checked 8 October 2026. SHA-256: `fb3cf94c117edfa950267cd4ac942e7dfaec9d9a465e5bec2e8eeaa09904c631`.

Verification: Fresh adopted OER retrieved; replacement footnotes visually inspected. All component IDs, titles, weights and selected route are unchanged. Original UCR evidence and assessment date retained; target validators, deterministic compiler and index checks passed.

This closes the external overgeneralization only. The existing UCR no-match reason is scoped to the unchanged selected pathway, not asserted for every alternative; its substantive correctness remains for separate UCR reassessment.

### cp-000175

- [Groningen Bachelor Medicine TER 2026–2027](https://www.rug.nl/umcg/education/geneeskunde/belangrijkedocumentengnk/documentenbachelor/terbachelormedicine2627.pdf) — Required annual curriculum and Learning Community tables. Checked 8 October 2026. SHA-256: `7f78d61fd5dbd83dad5b8d679424c72805daee04f22579d4e7fd029b2292a736`.
- [Groningen Bachelor Medicine study guide 2026–2027](https://www.rug.nl/umcg/education/geneeskunde/belangrijkedocumentengnk/documentenbachelor/studyguidebachelorgnk2627.pdf) — Bachelor Project, physical PDF p.36. Checked 8 October 2026. SHA-256: `fedee668fd7e1da9c29f47c6c15af4d2d0b06fb52af21d2fd5fbabfeb1b0336a`.

Verification: Fresh TER and guide retrieved; project page visually inspected. All component identities/weights and original UCR reason, evidence and assessment date remain unchanged. Target validators, deterministic compiler, index checks, compiler regressions and full-corpus validation passed.

This is an embedded-project sequencing correction, not a change to the medical curriculum credit totals or an independent UCR assessment.

### Batch 4 validation

Five cases processed: four first-stage findings resolved; OU retains one current curriculum question. VU has a complete 180-EC external reconstruction and awaits separate UCR assessment. Maastricht Fiscal Economics is archived outside active production scope. PThU and Groningen retain their selected 180-EC routes and original UCR assessment dates/evidence; those UCR judgments were not independently reassessed. No recurring monitoring was created.

Target validators, deterministic compiler comparisons, guarded registry replay, generated-index checks, compiler regressions and full-corpus validation passed. Publication checks are verified separately after each commit. The original audit and raw provenance remain unchanged.

Live corpus: 439 in-scope records, 301 comparisons and 138 exceptions; 21 excluded permanent targets. Exception types: 19 external-programme-unresolved, 114 no-defensible-ucr-match, 1 registry-exception, 4 ucr-assessment-pending. No in-scope record is missing.

## Batch 5 — next five cases in audit order

Status: completed. Independent UCR assessment remains separate.

| Target | First-stage outcome | Remaining external question |
|---|---|---|
| cp-000198 — Dutch Languages and Cultures — Dutch Language and Culture | Corrected the formal route count to two; preserved the named Dutch pathway and all 180 EC; Consolidated duplicate CP199 source/interest ownership under CP198 while retaining raw evidence and permanent IDs | None within this correction. |
| cp-000199 — Dutch Language and Culture — track within Dutch Languages and Cultures | Retained CP199 permanently as an ineligible alias of CP198; Archived its original decision/comparison unchanged and redirected current crosswalk and interest ownership | None within this correction. |
| cp-000205 — Religious Studies | Replaced the unqualified 30-EC open minor with the ordinary 15-EC minor and two restricted 7.5-EC faculty choices; Retained the selected specialisation and research/communication credits; verified a complete 180-EC ordinary pathway; Updated the formal authority and source/cohort qualifications; handed the corrected external basis to separate UCR assessment | None within this correction. |
| cp-000246 — Bachelor Architecture, Urbanism and Building Sciences | Replaced three year-total placeholders with 24 required coded modules and the 30-EC minor; Verified 150 required + 30 minor = 180; kept the four-part final project inside existing credits; Recorded current source context and retrieval qualification; handed the explicit external reconstruction to separate UCR assessment | None within this correction. |
| cp-000247 — Bachelor Civil Engineering | Corrected current Water en Techniek and formal Transport/Planning code context; Replaced the unrestricted 12-EC block/old Road and Railway unit with three fixed 4-EC units and two categorized 4-EC choices; Retained 30-EC minor and 10-EC project; verified 180 EC and handed the corrected external basis to separate UCR assessment | None within this correction. |

### cp-000198

- [Groningen Dutch Languages and Cultures OER 2026–2027](https://www.rug.nl/let/onze-faculteit/organisatie/diensten-en-voorzieningen/onderwijsinstituut/oeren/2026-2027/bacheloropleidingen/delen-b/ba-oer-ntc-2627.pdf) — Cover; Articles 2.5, 4.1, 5.1 and 8.3. Checked 8 October 2026. SHA-256: `795ccb578b52ad30eead0b6ce5e9dd0659addafc1fb17010f9a75c6878ff0037`.
- [Groningen current Dutch Language and Culture programme](https://www.rug.nl/bachelors/dutch-language-and-culture/) — Degree title, CROHO, language and named route. Checked 8 October 2026. SHA-256: `64842d4bffc08de3868a31e35ca166fd11a4718cbf1e82de4d762603c2094711`.

Verification: Fresh adopted OER cover and degree identity verified; two-track cover visually inspected. Selected components and original UCR exception/date/evidence are unchanged. Guarded alias replay, conflict regressions, deterministic owner reconstruction, corpus validators and generated-index checks passed.

The identity correction is limited to the two specifically named Dutch-track registrations. CP200 remains the broader generic umbrella. No UCR feasibility conclusion is updated.

### cp-000199

- [Groningen Dutch Languages and Cultures OER 2026–2027](https://www.rug.nl/let/onze-faculteit/organisatie/diensten-en-voorzieningen/onderwijsinstituut/oeren/2026-2027/bacheloropleidingen/delen-b/ba-oer-ntc-2627.pdf) — Cover; Articles 2.5, 4.1, 5.1 and 8.3. Checked 8 October 2026. SHA-256: `795ccb578b52ad30eead0b6ce5e9dd0659addafc1fb17010f9a75c6878ff0037`.
- [Groningen current Dutch Language and Culture programme](https://www.rug.nl/bachelors/dutch-language-and-culture/) — Degree title, CROHO, language and named route. Checked 8 October 2026. SHA-256: `64842d4bffc08de3868a31e35ca166fd11a4718cbf1e82de4d762603c2094711`.

Verification: Historical archive hashes and byte identity to the pre-correction commit verified. All source/interest records and raw fields are retained; stable token row order is unchanged. All 460 permanent IDs remain; guarded alias replay and exact-scope validation passed.

Resolving the duplicate does not assert a UCR match. There is one active named Dutch track, while CP200 keeps its broader identity.

### cp-000205

- [Religious Studies](https://www.rug.nl/bachelors/religious-studies/?lang=en) — Identity, years one/two and third-year alternatives, thesis and science communication. Checked 8 October 2026. SHA-256: `3056bcd9cd7048427de42bb7c932a1dc23a9becd301d598997f8908ec5a30ba7`.
- [TER BA Religious Studies 2026–2027](https://www.rug.nl/rcs/education/studyguide/oer-26-27/ter-ba-rs-26-27.pdf) — Articles 3.5/3.6, 4.1 and 7.1.1–7.1.6; PDF pp. 2, 9–10, 14–15. Checked 8 October 2026. SHA-256: `81fed04224de39e749ee986a83abef1afe8cc9745f30a837dd474ba1be520fec`.

Verification: Fresh adopted TER retrieved; Article 7.1 visually inspected, including alternatives and approval conditions. Independent ordinary-route arithmetic closes 60+60+60; no third faculty option or Arabic alternative is added. Deterministic compiler, target validators and generated-index checks passed.

The current official source resolves external allocation. This first-stage correction makes no new UCR fit judgment.

### cp-000246

- [Bouwkunde: what will I learn?](https://www.tudelft.nl/onderwijs/opleidingen/bachelors/bk/bsc-bouwkunde/over-de-opleiding/wat-ga-ik-leren) — Programme structure, modules and final-year work. Checked 8 October 2026. SHA-256: `4bbbdff75762012c6507465ec3b43dc2c8f131fa8f636f06da98dcaf565714d7`.
- [Onderwijsregelgeving Bacheloropleiding Bouwkunde 2026–2027](https://filelist.tudelft.nl/Studentenportal/Faculteitspecifiek/Bouwkunde/Onderwijs/Regulations/Onderwijsregelgeving%20Bachelor%202026-2027.pdf) — Articles 1.8–1.10, 2.24–2.28; Appendix II printed pp. 40–41. Adopted 2026–2027 source content and visual verification are preserved in the completed 7 October audit. Fresh retrieval on 8 October returned HTTP Error 502: Bad Gateway; no new PDF retrieval or hash is claimed.

Verification: Fresh programme page corroborates module counts and weights: 60+30+25+20+15 required EC. The completed audit supplies the adopted formal module placement; independent year totals each equal 60. Final project is IOP1 10 + IOP2 10 + TE5 5 + WV6 5, counted once. Deterministic compiler, target validators and generated-index checks passed.

The prior audit is substantive current-year evidence, not a new download. Current programme-page corroboration does not substitute for a newly inspected formal PDF. No UCR feasibility assessment is performed.

### cp-000247

- [Civil Engineering prospectus](https://www.tudelft.nl/onderwijs/opleidingen/bachelors/civiele-techniek/bsc-civiele-techniek) — Language, three years and construction/water/transport identity. Checked 8 October 2026. SHA-256: `beb4eeadfd813afde799f03a91bb6a444613eee705c8746ebad3ff65a935571e`.
- [OER and Annex BSc Civiele Techniek 2026–2027](https://filelist.tudelft.nl/Studentenportal/Faculteitspecifiek/CiTG/Onderwijs/OER%20regels%20en%20richtlijnen%20CiTG/BSC/2026-2027%20TER%20Annex_BoE/OER_Annex%20BSc%20CT%202026-2027.pdf) — Cohort 2026–2027 Annex articles 2–4, 12; PDF pp. 20–21, 23–26. Adopted 2026–2027 source content and visual verification are preserved in the completed 7 October audit. Fresh retrieval on 8 October returned HTTP Error 502: Bad Gateway; no new PDF retrieval or hash is claimed.
- [Bachelor Civiele Techniek September 2026 chart](https://filelist.tudelft.nl/Studentenportal/Faculteitspecifiek/CiTG/Onderwijs/Curriculumkaarten/2026-2027/TU%20Delft-20715-07-07-Flyers%20CT-V02.pdf) — Year tables, footer September 2026. Adopted 2026–2027 source content and visual verification are preserved in the completed 7 October audit. Fresh retrieval on 8 October returned HTTP Error 502: Bad Gateway; no new PDF retrieval or hash is claimed.

Verification: Fresh programme page confirms disciplinary identity; adopted current Annex/chart details are retained from the completed audit. Current formal code takes precedence over the stale chart; Bouwplaats credit aggregation is preserved. Neutral Q3 and Q4 choices plus three fixed units, minor and project close the third year at 60 EC. Deterministic compiler, target validators and generated-index checks passed.

Dated adopted-current-year evidence establishes the corrected structure despite present retrieval failures. No unsupported current course or filler is supplied, and no independent UCR judgment is drawn.

### Batch 5 validation

Five cases processed and all first-stage findings resolved. CP198 owns the Dutch track; CP199 is a retained permanent alias with unchanged archived records and consolidated active crosswalk/interest ownership. The generic CP200 umbrella remains distinct. Religious Studies, Architecture and Civil Engineering now contain explicit current 180-EC external reconstructions and await separate UCR assessment. No recurring monitoring was created.

Target validators, deterministic compiler comparisons, guarded registry/alias replay, generated-index checks, meaningful alias conflict regressions, compiler regressions and full-corpus validation passed. Final GitHub publication checks are verified after publication. The original audit, upstream source evidence and earlier batch histories remain unchanged.

Live corpus: 438 in-scope records, 301 comparisons and 137 exceptions; 22 excluded permanent targets. Exception types: 19 external-programme-unresolved, 111 no-defensible-ucr-match, 7 ucr-assessment-pending. No in-scope record is missing.

## Batch 6 — next five cases in audit order

Status: completed. Independent UCR assessment remains separate.

| Target | First-stage outcome | Remaining external question |
|---|---|---|
| cp-000248 — Bachelor Electrical Engineering | Replaced quarter aggregates with 28 course/choice components and exact current weights; Instantiated two distinct restricted EEX choices; retained the 30-EC minor; Corrected current prerequisite, language and period-conflict context; verified 180 EC | None within this correction. |
| cp-000249 — Bachelor Industrial Design Engineering | Corrected the compulsory-study narrative to 115 required EC and 65 EC of profiling/choice; Preserved all 25 accurate components, four distinct category slots, 30-EC minor and 15-EC final project | None within this correction. |
| cp-000250 — Bachelor Clinical Technology | Corrected minor from 15 to 30 EC and removed three duplicated third-year courses and the unsupported AV3/essay entry; Updated current heart/lung titles and the printed placement weight; recorded 27 unique components; Replaced unsupported no-match closure with an explicit external credit-conflict exception | Obtain authoritative clarification of KT2755 or another current credit/credit-sharing rule reconciling the printed 60+61+60 requirements with the 180-EC degree. |
| cp-000252 — Bachelor Aerospace Engineering | Added ENG to normalized instruction metadata while retaining currently advertised Dutch–English delivery; Preserved raw NLD offering, permanent identity and the 22-component 180-EC pre-2027 curriculum; Recompiled canonical provider metadata and generated summaries | None within this correction. |
| cp-000253 — Bachelor Marine Technology | Replaced six older aggregates with 26 current course/project/minor components; Corrected final project from 12 to 14 EC and current final-year course names; Preserved 30-EC minor and embedded subparts; verified 180 EC | None within this correction. |

### cp-000248

- [Electrical Engineering programme](https://www.tudelft.nl/onderwijs/opleidingen/bachelors/ee/bsc-electrical-engineering) — Degree facts, language requirement and defining content. Checked 8 October 2026. SHA-256: `f8b65a4971171bab8ee096f6f2ec9e697805e534d304717fa9948f17219d6ac4`.
- [Electrical Engineering curriculum chart 2025–2026](https://filelist.tudelft.nl/EWI/Studeren/Bacheloropleidingen/modulekaarten/BSc%20EE%20modulekaart%202025-2026%20inclusief%20kalender.pdf) — Credit axis, elective footnote, entry requirements. Checked 8 October 2026. SHA-256: `1eaff147630c94b2d565cf3ce4c056c44952e5fe38716440f66c78a0badf4a06`.
- [EEMCS bachelor OER 2026–2027: Electrical Engineering](https://filelist.tudelft.nl/Studentenportal/Faculteitspecifiek/EWI/Studeren/Reglementen/Onderwijs-%20en%20Examenregeling%20EWI%202026-2027.pdf) — Electrical Engineering articles 6–7; PDF pp. 25–29. Checked 8 October 2026. SHA-256: `c592f1a06ce7315d9492d93475981c15dee6d3d74e337788084a55d8682ade47`.

Verification: Fresh current OER tables and articles 6–7 visually inspected. Independent year totals are 60+60+60; selected electives count once and remain distinct. Deterministic compilation, target validators and generated-index checks passed.

The formal yearly requirement structure is resolved. No exact quarter timetable is asserted; the old-chart/current-table discrepancy remains explicitly qualified. No new UCR judgment is made.

### cp-000249

- [Industrial Design: what will I learn?](https://www.tudelft.nl/onderwijs/opleidingen/bachelors/industrieel-ontwerpen/bsc-industrieel-ontwerpen/over-de-opleiding/wat-ga-ik-leren) — People, organisations, technology; electives and programme chart. Checked 8 October 2026. SHA-256: `ee1fc71293ace12fd938043c0a2638950b8b0762fc8b5bfe958c1101c5db2735`.
- [Industrial Design Engineering curriculum 2026–2027](https://filelist.tudelft.nl/IO/Studeren/Bacheloropleiding/BSc%20Curriculum_2026_2027_met%20code%20en%20slots.png?hash=37c0a865d7) — All semester blocks and credits. Checked 8 October 2026. SHA-256: `5d84fd787250dceb77de86eeeb8e6590a4375138aa18d21b136387dc5960d0f9`.

Verification: Fresh 2026–2027 curriculum image visually inspected; all components and credit weights match. Independent allocation is 60 + (40 required + 20 categorized choices) + (30 minor + 15 electives + 15 project) = 180. The stored curriculum and historical UCR assessment date/evidence remain unchanged. Deterministic compilation, target validators and generated-index checks passed.

This correction changes the external compulsory/choice narrative only. It does not revalidate the historical UCR no-match judgment.

### cp-000250

- [Clinical Technology programme](https://www.tudelft.nl/onderwijs/opleidingen/bachelors/klinische-technologie/bsc-klinische-technologie/over-de-opleiding) — Joint degree, credits, instruction and placement. Checked 8 October 2026. SHA-256: `6dd4ee5f3ad4c9e22a637db21fb3685a1e6672e1ea058ac04664a7aa75612109`.
- [Clinical Technology module map 2024–2025](https://filelist.tudelft.nl/me/Onderwijs/Bacheloropleidingen/KT/Modulekaart-Bsc-KT%202024-2025.pdf) — Second/third-year duplicate codes and minor. Checked 8 October 2026. SHA-256: `b8bcee01f7f5a64bf358c94c57a3340c4f7d43d2a94370a51bd4591c39b0e1ef`.
- [OER BSc Klinische Technologie 2026–2027](https://filelist.tudelft.nl/Studentenportal/Faculteitspecifiek/ME/Onderwijs/GERELATEERD/Reglementen/Archief%20Onderwijsreglementen/2026-2027/OER%20BSc%20KT%202026-2027_DEFINITIEF.pdf) — Articles 7, 32, Appendix 3; PDF pp. 6, 25–27. Checked 8 October 2026. SHA-256: `97cfb84ca74a1c735b1b98cbc86c955134e875f8db5b5c2c410461502cc6933d`.

Verification: Fresh adopted OER tables visually inspected; placement is printed 4.5 EC and final-year major is exactly four units totaling 30. Independent printed year totals are 60, 61 and 60; all 27 component identifiers are unique. No duplicate alternatives, inferred weight adjustment or extra thesis/skills credit is used. Deterministic compilation, target validators and generated-index checks passed.

Known factual errors are corrected. The published one-credit contradiction remains an external question; the diagnostic component total is explicitly 181, not asserted as a valid pathway. This finite check is complete; no monitoring is scheduled.

### cp-000252

- [Aerospace Engineering programme](https://www.tudelft.nl/onderwijs/opleidingen/bachelors/ae/bsc-aerospace-engineering) — Degree facts and language. Checked 8 October 2026. SHA-256: `96a23e41ba788fdd0400a1f88b28ca3146fb5014a50677655b9eaf93cfae3c5a`.
- [Aerospace Engineering Implementation Regulations 2026–2027](https://filelist.tudelft.nl/Studentenportal/Faculteitspecifiek/LR/Onderwijs/Education/AE%20IR%202026-2027%20final.pdf) — Articles 1–2; PDF p. 3. Checked 8 October 2026. SHA-256: `e865d9f6352ecdb1d598a496b95497821f98a7c028bfe0a7fd24f7901a1d1260`.
- [Aerospace Engineering BSc modules and courses](https://filelist.tudelft.nl/Studentenportal/Faculteitspecifiek/LR/Onderwijs/BSc%20Curriculum%202022-2023.pdf) — Whole chart, July 2022 footer, thick module versus subcomponent boundaries. Checked 8 October 2026. SHA-256: `c0f87f8733c73b703c1a564fdabb9e5611b3c075b50cae7c6b9ef8424a93c1f0`.
- [Aerospace Engineering current English programme page](https://www.tudelft.nl/en/onderwijs/opleidingen/bachelors/ae/bsc-aerospace-engineering) — Language facts panel; admission deadline 15 January 2027. Checked 8 October 2026. SHA-256: `d38d5df1958a4fb742dd0131eb8f204142f5e735ecab5ceea0abd678ef520275`.

Verification: Fresh Dutch and English official programme pages both state English or Dutch–English; bilingual context explicitly recorded. Current IR and linked module chart retrieved; degree allocation remains 60+60+30+15+15 = 180. Guarded registry replay reproduces the language correction; raw offerings/source rows are unchanged. Deterministic compilation, target validators and generated-index checks passed.

Fresh evidence narrows the correction to adding ENG, rather than removing NLD as the prior audit proposed. Current prospectus delivery options are not used to alter the selected 2026-cohort curriculum. The original audit remains immutable.

### cp-000253

- [Marine Technology: what will I learn?](https://www.tudelft.nl/onderwijs/opleidingen/bachelors/maritieme-techniek/bsc-maritieme-techniek/over-de-opleiding/wat-ga-ik-leren) — Degree structure and linked older diagram. Checked 8 October 2026. SHA-256: `11f996f25ec8812083adb606402844d30fe49309e7edd519aae62a607bd29fb1`.
- [OER BSc Mechanical Engineering and Marine Technology 2026–2027](https://filelist.tudelft.nl/Studentenportal/Faculteitspecifiek/ME/Onderwijs/GERELATEERD/Reglementen/Archief%20Onderwijsreglementen/2026-2027/OER%20BSc%20WB-MT_DEFINITIEF.pdf) — Mechanical curriculum PDF p.25; Marine curriculum p.30; BEP conditions pp.26/31. Checked 8 October 2026. SHA-256: `8289710a9241a02af7d4ff65b899a5488a9d2582c49d0eb8fbb4d909ec8d7053`.

Verification: Fresh current formal curriculum table and final-project rules visually inspected. Independent course weights total 60+60+60; integration projects total 20 and Ship Design is counted once. Current final project 14 EC and first-year/54-second-year-credit entry condition verified. Deterministic compilation, target validators and generated-index checks passed.

Current adopted requirements resolve the external reconstruction. The older webpage allocation is retained only as discrepancy context. No new UCR fit judgment is made.

### Batch 6 validation

Five cases processed: four first-stage findings resolved; Clinical Technology retains the published 181-versus-180 credit conflict. Electrical Engineering and Marine Technology have corrected course-level external reconstructions and await separate UCR assessment. Industrial Design and Aerospace retain their previously verified component allocations and historical UCR assessment dates/evidence. No recurring monitoring was created.

Target validators, deterministic compiler comparisons, guarded registry replay, generated-index checks, compiler regressions and full-corpus validation passed. GitHub checks are verified after each publication. The original audit, raw provenance and earlier batch histories remain unchanged.

Live corpus: 438 in-scope records, 301 comparisons and 137 exceptions; 22 excluded permanent targets. Exception types: 20 external-programme-unresolved, 108 no-defensible-ucr-match, 9 ucr-assessment-pending. No in-scope record is missing.

## Batch 7 — next five cases in audit order

Status: completed. Independent UCR assessment remains separate.

| Target | First-stage outcome | Remaining external question |
|---|---|---|
| cp-000254 — Bachelor Nanobiology | Corrected normalized instruction language to ENG while preserving raw NLD provenance; Replaced ambiguous practical alternatives with one formal assigned mixed pair; Instantiated four first-listed 2.5-EC specialist electives and verified 32 components totaling 180 EC | None within this correction. |
| cp-000259 — Bachelor Applied Mathematics | Instantiated four mathematical and exactly one non-mathematical elective using neutral formal ordering; Preserved 30-EC minor, 15-EC project and combined 3+2-EC Proof Techniques unit; Verified 29 components totaling 180 EC and current project-entry rules | None within this correction. |
| cp-000260 — Bachelor Mechanical Engineering | Corrected the second-year narrative from three to four formal projects, including Process Engineering and Thermodynamics; Made the adopted OER the curriculum authority and preserved all 25 accurate component weights | None within this correction. |
| cp-000261 — Bachelor Automotive Technology | Replaced older aggregates with 27 current common/AT course and open-space positions; Corrected allocation to core 125 including project 10, ITEC 10 and electives 45; Removed optional autonomous-vehicle/design-project claims from compulsory formation; updated Propulsion Systems title | None within this correction. |
| cp-000262 — Bachelor Biomedical Engineering | Corrected normalized language to NLD and ENG while preserving raw ENG provenance; Reconstructed 26 current BBT positions: core 125 including project 15, ITEC 10, electives 45; Counted Skills Experience once at 10 EC; preserved embedded PPD and elective level rules; Documented 8BA020 title variation using the current cohort chart and official course profile | None within this correction. |

### cp-000254

- [Nanobiology degree facts](https://www.tudelft.nl/en/education/programmes/bachelors/nb/bsc-nanobiology) — Working language and joint institutional setting. Checked 8 October 2026. SHA-256: `6f7ac1d5440e2f0e4c277e61014a10513c0fb99c6356f4f7d2ef918aee505ea4`.
- [Nanobiology September 2026 curriculum](https://filelist.tudelft.nl/TUDelft/Onderwijs/Opleidingen/Bachelor/Nanobiology/02._Opleiding/2026_NB_DEF_web_pag2.pdf) — All year tables and specialist list. Checked 8 October 2026. SHA-256: `c0d494119a5dd7dde9f29f93ba061bc1f71cb3e34ca5c63a037f5c4c65a6bd0b`.
- [Programme-specific Appendix Nanobiology TER 2026–2027](https://filelist.tudelft.nl/Studentenportal/Faculteitspecifiek/TNW/Onderwijs/Opleidingsreglementen/2026-2027/BSc%20NB%20Appendix%20TER%202026-2027.pdf) — Articles 3–5 and 8; PDF pp.5–8. Checked 8 October 2026. SHA-256: `e7e206d4aa61466c9e04081966de803c3be8eabf33912c009643518af48b3ab1`.

Verification: Fresh current official requirement tables inspected, including visual PDF checks. Each component counted once; independently verified year totals 60+60+60=180 EC. Deterministic compilation, all three target validators and generated-index checks passed.

The external correction is complete. UCR fit awaits separate assessment; the superseded judgment is preserved in this register. No recurring monitoring is scheduled.

### cp-000259

- [Applied Mathematics programme](https://www.tudelft.nl/onderwijs/opleidingen/bachelors/tw/bsc-technische-wiskunde/over-de-opleiding/wat-ga-ik-leren) — Mathematical identity and public named courses. Checked 8 October 2026. SHA-256: `148da6989000c5cd0c9e4ec66dafcf65ed6299c13958ca30d23f542f790452f4`.
- [Public current study-guide programme data](https://curriculum.tudelft.nl/publisher/api/v0/opleidingen/items/33234) — 2026–2027 record; cohort 2024+ description. Checked 8 October 2026. SHA-256: `26469e9042e09304a61b2b841b122b496075f6b2148a73ac0406ca43d434768c`.
- [EEMCS OER 2026–2027: Applied Mathematics](https://filelist.tudelft.nl/Studentenportal/Faculteitspecifiek/EWI/Studeren/Reglementen/Onderwijs-%20en%20Examenregeling%20EWI%202026-2027.pdf) — Article 14A/15; PDF pp.45–47. Checked 8 October 2026. SHA-256: `c592f1a06ce7315d9492d93475981c15dee6d3d74e337788084a55d8682ade47`.

Verification: Fresh current official requirement tables inspected, including visual PDF checks. Each component counted once; independently verified year totals 60+60+60=180 EC. Deterministic compilation, all three target validators and generated-index checks passed.

The external correction is complete. UCR fit awaits separate assessment; the superseded judgment is preserved in this register. No recurring monitoring is scheduled.

### cp-000260

- [OER BSc Mechanical Engineering and Marine Technology 2026–2027](https://filelist.tudelft.nl/Studentenportal/Faculteitspecifiek/ME/Onderwijs/GERELATEERD/Reglementen/Archief%20Onderwijsreglementen/2026-2027/OER%20BSc%20WB-MT_DEFINITIEF.pdf) — Mechanical curriculum PDF p.25; Marine curriculum p.30; BEP conditions pp.26/31. Checked 8 October 2026. SHA-256: `8289710a9241a02af7d4ff65b899a5488a9d2582c49d0eb8fbb4d909ec8d7053`.
- [Mechanical Engineering programme](https://www.tudelft.nl/onderwijs/opleidingen/bachelors/wb/bsc-werktuigbouwkunde) — Engineering projects and current identity. Checked 8 October 2026. SHA-256: `4573d5ca35e2b30b36a564f84c046dddef5f21dc90628f79bd2302c240b56a01`.
- [Public current study-guide Mechanical Engineering entry](https://curriculum.tudelft.nl/publisher/api/v0/opleidingen/items/32108) — Degree facts and access limitation. Checked 8 October 2026. SHA-256: `a1b0715e923d83fbeb4579dfca481ebe352df96f62c9766981b6a5936ad41241`.

Verification: Fresh current official requirement tables inspected, including visual PDF checks. Each component counted once; independently verified year totals 60+60+60=180 EC. All 25 components are byte-equivalent as data; historical checkedOn and ucrCourseEvidence remain unchanged. Deterministic compilation, all three target validators and generated-index checks passed.

This is a narrow external narrative/source correction. All component allocations and historical UCR assessment date/evidence remain unchanged; no new UCR judgment is made.

### cp-000261

- [Automotive Technology programme](https://studiegids.tue.nl/opleidingen/bachelor-college/majors/automotive-technology) — English degree and automotive identity. Checked 8 October 2026. SHA-256: `5f459e81f478966dfd5e8e41a52f159a000badf426f1be1f1860bb3683b44c05`.
- [EE and Automotive after-revision curriculum 2026–2027](https://assets.w3.tue.nl/w/fileadmin/Education_Guide/Content/Programs/Bachelor%20College/Major%20Electrical%20Engineering/Curriculum/Curriculum%202026-2027/Latest%20version%2020260702%20Bachelor%20curriculum%20EE%20and%20AT%20After%20Revision%202026-2027.pdf) — PDF pp.1–4; version 2 July 2026. Checked 8 October 2026. SHA-256: `196b4664ac03682725b0b386f1695282f6f8f5f66c4b5cfbf17462097952c009`.

Verification: Fresh current official requirement tables inspected, including visual PDF checks. Each component counted once; independently verified year totals 60+60+60=180 EC. Deterministic compilation, all three target validators and generated-index checks passed.

The external correction is complete. UCR fit awaits separate assessment; the superseded judgment is preserved in this register. No recurring monitoring is scheduled.

### cp-000262

- [Biomedical Engineering degree facts and two core programmes](https://www.tue.nl/studeren/bachelor-college/bachelor-biomedische-technologie) — Language, standard degree and BMT/MWT alternatives. Checked 8 October 2026. SHA-256: `f36e4620e41375113a4e99f6b18be8b830882d729b939d9c7cceee3b43a5d7b1`.
- [Biomedical Engineering PER after revision 2026–2027](https://assets.w3.tue.nl/w/fileadmin/Education_Guide/Biomedical%20Engineering/OER%20en%20ER/2026-2027/BSc%20OER%20BME%202026-2027%20AR.pdf) — Articles 3.3–3.5; Appendix 2, PDF pp.20–23,76–79. Checked 8 October 2026. SHA-256: `4b5925c19a89ce4ab3afc9957212a12214532ef5a085bf54a4f93b2c025a8860`.
- [Biomedical Engineering generation 26 curriculum](https://assets.w3.tue.nl/w/fileadmin/Education_Guide/Biomedical%20Engineering/Bachelor/Programma%27s%20en%20curricula/Curriculum%20gen26.pdf) — Whole diagram; first column BBT versus second MWT. Checked 8 October 2026. SHA-256: `e9d657132339a28666126c1ae5a5340abf43e1080ef19880d1354787eaf8ace0`.
- [Biomedical Engineering elective space](https://studiegids.tue.nl/opleidingen/bachelor-college/majors/biomedische-technologie/curriculum/keuzeruimte) — Open study space, level requirements and approval. Checked 8 October 2026. SHA-256: `b754e0e214ed7ec45ad8b28c3cc849813821828448108d699cbde2d49eb99d24`.
- [TU/e official course profile: Engineering organs on a chip](https://research.tue.nl/nl/courses/engineering-organs-on-a-chip/) — Title, course code 8BA020 study-guide link and course period. Checked 8 October 2026. SHA-256: `f027df0c2f854fa3533e5b1c248bb787578b5b8718563df902aa37efcb817c8e`.

Verification: Fresh current official requirement tables inspected, including visual PDF checks. Each component counted once; independently verified year totals 60+60+60=180 EC. Deterministic compilation, all three target validators and generated-index checks passed.

The external correction is complete. UCR fit awaits separate assessment; the superseded judgment is preserved in this register. No recurring monitoring is scheduled.

### Batch 7 validation

Five first-stage cases resolved. Nanobiology, Applied Mathematics, Automotive Technology and Biomedical Engineering have corrected external reconstructions and await separate UCR assessment. Mechanical Engineering retains all previously verified component allocations and its historical UCR assessment date/evidence; only external narrative and source context changed. No recurring monitoring was created.

Target validators, deterministic compiler comparisons, guarded registry replay, generated-index checks, full-corpus validation and CI compiler regressions passed. GitHub checks are verified after each publication. The original audit, raw provenance and earlier batch histories remain unchanged.

Live corpus: 438 in-scope records, 301 comparisons and 137 exceptions; 22 excluded permanent targets. Exception types: 20 external-programme-unresolved, 104 no-defensible-ucr-match, 13 ucr-assessment-pending. No in-scope record is missing.

## Batch 8 — next five cases in audit order

Status: completed. Independent UCR assessment remains separate.

| Target | First-stage outcome | Remaining external question |
|---|---|---|
| cp-000263 — Bachelor Architecture, Urbanism and Building Sciences | Instantiated one coherent AUDE route using formal ordering independently of UCR fit; Replaced generic 130-EC core with 28 named requirement/open-space positions; preserved printed 5-EC multidisciplinary project; Recorded the 175-EC diagnostic and conflict between Article 3.4, Appendix 2 and webpage aggregates | Official reconciliation of AUDE core/project credits and elective volume: printed named core125 + ITEC10 + Appendix2 electives40 = 175, versus Article3.4 electives45 and webpage core130/electives40. |
| cp-000265 — Bachelor Electrical Engineering | Reconstructed 27 current common/EE course and open-space positions totaling 180 EC; Corrected core 125 including project 10, ITEC 10 and electives 45; counted 5EWC0 once at 10; Removed optional semiconductor/alternative-programme courses from universal compulsory formation | None within this correction. |
| cp-000266 — Bachelor Industrial Design | Replaced generic annual 60 blocks with all 23 source-printed positions; diagram total 180 EC; Preserved separately credited PPD15, design projects 50, multidisciplinary CBL5 and approved ELA25 alternatives; Recorded unresolved formal 185 versus diagram 180 conflict without altering printed weights | Official reconciliation of current PER core 125 + ITEC 10 + profiling 50 =185 versus ordinary current diagram core 120 + ITEC 10 + profiling 50 =180. |
| cp-000267 — Bachelor Mechanical Engineering | Corrected normalized instruction language to ENG while preserving raw NLD provenance; Reconstructed 28 current positions totaling 180: core 125 including project 10, ITEC10, electives 45; Instantiated two restricted core choices by formal quarter-group order; kept optional summer precision course distinct | None within this correction. |
| cp-000270 — Bachelor Chemical Engineering and Chemistry | Reconstructed 27 current positions totaling 180: core 125 including project 15, ITEC10, electives 45; Updated current calculus and compulsory CBL Process Technology; kept optional examples outside universal core; Recorded precise 120-total/40-post-propaedeutic-core BEP entry rules and current English cohort | None within this correction. |

### cp-000263

- [Architecture, Urbanism and Building Sciences after-revision curriculum](https://educationguide.tue.nl/programs/bachelor-college/majors/architecture-urbanism-and-building-sciences/curriculum-start-year-20232024) — Current degree allocation, four main tracks and profiles. Checked 8 October 2026. SHA-256: `bd3e09e4b94fce5c415c27be325ed1b710c5a7fed5f3fef0a6d167cb06fd4e78`.
- [Built Environment Bachelor College Course Guide 2026–2027](https://assets.w3.tue.nl/w/fileadmin/Education_Guide/Content/Programs/Bachelor%20College/Major%20Architecture%2C%20Urbanism%20and%20Building%20Sciences/Curriculum/Built%20Environment%20Bachelor%20College%20CourseGuide%202026-2027.pdf) — Printed pp.52–59,64–65,74–77; PDF sheets 27–30,33,38–39. Checked 8 October 2026. SHA-256: `5e86dcccd968361bf72be93e13ccf1a1dbee5b923b04d360bf5e736396417296`.
- [AUBS PER after revision 2026–2027](https://assets.w3.tue.nl/w/fileadmin/Education_Guide/Content/Programs/Bachelor%20College/Major%20Architecture%2C%20Urbanism%20and%20Building%20Sciences/Regulations/PER%20AUBS%20After%20Revision%202026-2027%20%28Curriculum%20start%20year%202023-2024%29.pdf) — Article 3.4, core tables and Appendix 2/3; PDF pp.21–24,81,87. Checked 8 October 2026. SHA-256: `ab3dfb922261d67e6f69008e9404b563f6b6ee7b2321bed349ca640101bfd753`.

Verification: Fresh current official requirement tables inspected, including visual PDF checks. Each component counted once; verified 28 positions totaling175 EC. Deterministic compilation, all three target validators and generated-index checks passed.

The established route and course corrections are published. Conflicting current official credit requirements prevent a verified 180-EC closure. The 175-EC diagnostic is deliberate; no missing credit is invented. No recurring monitoring is scheduled.

### cp-000265

- [Electrical Engineering programme](https://www.tue.nl/en/education/bachelor-college/bachelor-electrical-engineering) — English degree and integrated engineering identity. Evidence preserved from the completed first-stage audit; this source was not freshly retrieved: <urlopen error timed out>
- [EE and Automotive after-revision curriculum 2026–2027](https://assets.w3.tue.nl/w/fileadmin/Education_Guide/Content/Programs/Bachelor%20College/Major%20Electrical%20Engineering/Curriculum/Curriculum%202026-2027/Latest%20version%2020260702%20Bachelor%20curriculum%20EE%20and%20AT%20After%20Revision%202026-2027.pdf) — PDF pp.1–4; version 2 July 2026. Checked 8 October 2026. SHA-256: `196b4664ac03682725b0b386f1695282f6f8f5f66c4b5cfbf17462097952c009`.

Verification: Fresh current official requirement tables inspected, including visual PDF checks. Each component counted once; verified 27 positions totaling180 EC. Deterministic compilation, all three target validators and generated-index checks passed.

The external correction is complete. UCR fit awaits separate assessment; the superseded judgment is preserved in this register. No recurring monitoring is scheduled.

### cp-000266

- [Industrial Design programme](https://www.tue.nl/en/education/bachelor-college/bachelor-industrial-design) — Degree facts and integrated expertise areas. Evidence preserved from the completed first-stage audit; this source was not freshly retrieved: <urlopen error timed out>
- [Industrial Design curriculum start 2023/2024 and after](https://studiegids.tue.nl/opleidingen/bachelor-college/majors/industrial-design/curriculum-start-year-20232024) — Current cohort diagram links and exception for 2025 starters. Checked 8 October 2026. SHA-256: `0d84c38e1f6b639c5a95bfebb092a435a468c367b860ba778516e1db25169a08`.
- [Industrial Design 2627 Bachelor Program ID-BC2.0 overview](https://assets.w3.tue.nl/w/fileadmin/Education_Guide/Content/Programs/Bachelor%20College/Major%20Industrial%20Design/Forms%20and%20Files/2627%20Bachelor%20Program%20ID-BC%202.0%20Overview.pdf) — Whole one-page printed-credit diagram. Checked 8 October 2026. SHA-256: `64d59d953786b8924cd5f77046234a7d6201d86a853acc0d06a5593f69c8473a`.
- [Industrial Design PER after revision 2026–2027](https://assets.w3.tue.nl/w/fileadmin/Education_Guide/Content/Programs/Bachelor%20College/Major%20Industrial%20Design/Forms%20and%20Files/ID%20BSc%20model%20OER%202026-2027%20AR.pdf) — Article 3.4 and Appendix 2; PDF pp.20–24,76–81. Checked 8 October 2026. SHA-256: `2696c05f3080fcff3717ac517c0dbf6da6c4d752f770c3ff06687d0a77d51a06`.

Verification: Fresh current official requirement tables inspected, including visual PDF checks. Each component counted once; verified 23 positions totaling180 EC. Deterministic compilation, all three target validators and generated-index checks passed.

The diagram reconstruction and required formation are corrected. The current formal aggregate remains inconsistent with it, so external-programme-unresolved is retained until an authoritative reconciliation is available. No recurring monitoring is scheduled.

### cp-000267

- [Mechanical Engineering programme](https://www.tue.nl/en/education/bachelor-college/bachelor-mechanical-engineering) — Degree facts and language. Evidence preserved from the completed first-stage audit; this source was not freshly retrieved: <urlopen error timed out>
- [Mechanical Engineering PER after revision 2026–2027](https://assets.w3.tue.nl/w/fileadmin/Education_Guide/Mechanical%20Engineering/Bachelor%20College/2026-2027/BSc%20PER%20AR%202026-2027.pdf) — Articles 3.3–3.4; Appendix 2, PDF pp.72–77. Checked 8 October 2026. SHA-256: `737d0f3e9549d25f973bfc4a44ef8ea00114d159cde906777f4a56eb4364a919`.

Verification: Fresh current official requirement tables inspected, including visual PDF checks. Each component counted once; verified 28 positions totaling180 EC. Deterministic compilation, all three target validators and generated-index checks passed.

The external correction is complete. UCR fit awaits separate assessment; the superseded judgment is preserved in this register. No recurring monitoring is scheduled.

### cp-000270

- [Chemical Engineering and Chemistry programme](https://www.tue.nl/en/education/bachelor-college/bachelor-chemical-engineering-and-chemistry) — Present degree identity and future language notice. Evidence preserved from the completed first-stage audit; this source was not freshly retrieved: <urlopen error timed out>
- [Chemical Engineering and Chemistry PER after revision 2026–2027](https://assets.w3.tue.nl/w/fileadmin/Education_Guide/Chemical%20Engineering%20and%20Chemistry/Regulations/BSc%20OER%202026-2027%20AR.pdf) — Article 3.4; Appendix 2, PDF pp.72–76; Appendix 3 pilot. Checked 8 October 2026. SHA-256: `2f590b1d796f43fb11ab5bf0f25cd13a4e83b4e714f551b919a6b0e5ce56aa88`.

Verification: Fresh current official requirement tables inspected, including visual PDF checks. Each component counted once; verified 27 positions totaling180 EC. Deterministic compilation, all three target validators and generated-index checks passed.

The external correction is complete. UCR fit awaits separate assessment; the superseded judgment is preserved in this register. No recurring monitoring is scheduled.

### Batch 8 validation

Five cases processed: three external reconstructions resolved; Architecture and Industrial Design retain documented conflicts between current official credit requirements. Electrical Engineering, Mechanical Engineering and Chemical Engineering and Chemistry await separate UCR assessment of their corrected 180-EC curricula. No recurring monitoring was created.

Target validators, deterministic compiler comparisons, guarded registry replay, generated-index checks, full-corpus validation and CI compiler regressions passed. GitHub checks are verified after each publication. The original audit, raw provenance and earlier batch histories remain unchanged.

Live corpus: 438 in-scope records, 301 comparisons and 137 exceptions; 22 excluded permanent targets. Exception types: 22 external-programme-unresolved, 99 no-defensible-ucr-match, 16 ucr-assessment-pending. No in-scope record is missing.


## Batch 9 — next five cases in audit order

Corrections proceed individually; UCR comparability remains outside scope.

### cp-000273 — Bachelor Applied Physics

Implemented: Replaced aggregate core with 27 source-backed course/project/open-space positions totaling 180 EC; Replaced generic capstone range with exact 15 EC and current project/safety prerequisites; Preserved 45 EC genuine elective space, 125/10/45 allocation and embedded/noncredit formation.

- [Applied Physics programme](https://www.tue.nl/en/education/bachelor-college/bachelor-applied-physics) — Present degree facts. Checked 9 October 2026. Programme orientation retained from original audit; formal source independently freshly retrieved.
- [Applied Physics PER after revision 2026–2027 BC2.0](https://assets.w3.tue.nl/w/fileadmin/Education_Guide/Content/Programs/Bachelor%20College/Major%20Applied%20Physics/Regulations/OER%202026-2027%20BC2.0.pdf) — Article 3.4; Appendix 2, PDF pp.72–76; calculus pilot appendix. Checked 9 October 2026. Fresh official source retrieved and inspected during this correction.

Verification: Fresh PER downloaded; requirement grid visually inspected and named course table independently checked. Credit arithmetic closes 60+60+60; all component identifiers are unique and no embedded/noncredit formation is added. Deterministic canonical regeneration, all three target validators and generated-index checks passed.

External correction complete; separate UCR assessment pending. The prior no-match judgment remains historical provenance in the register. No recurring monitoring is scheduled.

### cp-000274 — Bachelor Applied Mathematics

Implemented: Replaced aggregate core with 28 named requirement/project/open-space positions totaling 180 EC; Specified ordinary BEP10 and distinguished optional Innovation Space project15; Preserved 45 EC genuine electives and embedded SCOP/e, PPD and CBL formation.

- [Applied Mathematics programme](https://www.tue.nl/en/education/bachelor-college/bachelor-applied-mathematics) — Present degree facts. Checked 9 October 2026. Programme orientation retained from original audit; formal source independently freshly retrieved.
- [Mathematics and Computer Science PER after revision 2026–2027](https://assets.w3.tue.nl/w/fileadmin/Education_Guide/Mathematics%20_%20Computer%20Science/Bachelor/MC_S%20-%20general%20bachelor/MCS%20PER%20Bachelor%20AR%202026-2027%20%28BC%202.0%29.pdf) — Article 3.4; Appendix 2, PDF pp.78,82–85; Appendix 3 p.90. Checked 9 October 2026. Fresh official source retrieved and inspected during this correction.

Verification: Fresh current PER downloaded; Applied Mathematics p.78 requirement grid visually inspected. Every counted course or project occurs once; required totals independently close 60+60+60. Deterministic canonical regeneration, all target validators and generated-index checks passed.

External correction complete; separate UCR assessment pending. The prior no-match judgment remains historical provenance. No recurring monitoring is scheduled.

### cp-000275 — Bachelor Theology

Implemented: Replaced unsupported annual aggregates with ten source-backed first-year rows totaling 60 EC; Separated the published second-year 60 from a certified single-cohort pathway and documented Greek4 overlap; Removed outgoing thesis10/minor27.5 from current-entrant claims and clarified minor replacement/PPV treatment.

- [Apeldoorn Bachelor Theology](https://www.tua.nl/nl/onderwijs/o/bachelor-theologie) — Degree facts and optional Bible Translation route. Checked 9 October 2026. Fresh official source retrieved and inspected during this correction.
- [Apeldoorn Bachelor/Master study guide 2026–2027](https://www.tua.nl/media/studiegids-2026-2027/documents/studiegids_20262027_extern.pdf) — Printed pp.29–36,55,77; PDF pp.9–16,35,57. Checked 9 October 2026. Fresh official source retrieved and inspected during this correction.

Verification: Fresh study guide retrieved; printed pp.33,36,37,55,77 independently inspected, with visual overview and second-year checks. First-year positive rows total60; second-year table is documented separately and not added to the counted subset. Deterministic canonical regeneration, all target validators and generated-index checks passed.

Known cohort and compulsory-versus-replaceable claims are corrected. External-programme-unresolved records the precise new-cohort questions; no 180-EC total or missing credits are invented. Prior UCR judgment is historical only. No recurring monitoring is scheduled.

Remaining external questions: Clarify applicable new-cohort second-year sequence/caption and Greek4 overlap before counting it with the first-year 60 EC. Provide the new-cohort third-year course weights, thesis and PPV allocation, and exact requirements replaced by the 30-EC minor; outgoing cohort2024 rules cannot establish these.

### cp-000277 — African Studies

Implemented: Resolved duplicated SwahiliII counting through adopted cohort transition rules; outgoing second entry excluded; Confirmed no formal specialisations and corrected new SwahiliIII/third-year placement and requirements; Preserved open30 and thesis10; published explicit175-EC named-subset diagnostic with T.B.A.5 unresolved.

- [Leiden African Studies current study-guide product](https://studiegids.universiteitleiden.nl/api/product?code=BA-AFR&type=STUDY) — BA-AFR, year 2261; all annual groups. Checked 9 October 2026. Fresh official source retrieved and inspected during this correction.
- [Swahili II current module 5731V015Y](https://studiegids.universiteitleiden.nl/api/product?code=5731V015Y&type=MODULE&year=2261&language=en) — Credits, admission requirement, objectives and level. Checked 9 October 2026. Fresh official source retrieved and inspected during this correction.
- [Swahili II current module 5733V005Y](https://studiegids.universiteitleiden.nl/api/product?code=5733V005Y&type=MODULE&year=2261&language=en) — Credits, admission requirement, objectives and level. Checked 9 October 2026. Fresh official source retrieved and inspected during this correction.
- [African Studies programme-specific OER 2026–2027](https://www.organisatiegids.universiteitleiden.nl/binaries/content/assets/geesteswetenschappen/oer/2026-2027/ba-oso-african-studies-2026-2027.pdf) — Articles2.2/4.2 and Appendix F, PDF pp.2,4–7. Checked 9 October 2026. Fresh official PDF retrieved from current regulatory index; transition tables visually inspected.
- [African Studies current regulatory index](https://www.organisatiegids.universiteitleiden.nl/en/regulations/humanities/oer/african-studies-ba) — Current2026–2027 OER link. Checked 9 October 2026. Fresh official index retrieved.

Verification: Fresh programme API and all22 linked module records checked; both SwahiliII descriptions/admission/outcomes match exactly. Fresh current programme-specific OER found through official index; AppendixF pp.6–7 visually inspected. Named current-cohort requirements close60+55+60=175; omitted T.B.A.5 is explicit, and no repeated Swahili credits are counted. Deterministic canonical regeneration, all target validators and generated-index checks passed.

The original Swahili and route ambiguities are resolved by freshly obtained formal authority. Full external closure remains blocked by T.B.A.5 and mixed-cohort catalogue reconciliation; no speculative course is supplied. Prior UCR judgment remains historical only. No recurring monitoring is scheduled.

Remaining external questions: Identify the exact new-cohort second-year T.B.A.5-EC course and applicable course conditions; it is not genuine open elective space. Reconcile the current API mixed-cohort Swahili and third-year choice membership with the adopted new-programme AppendixF; confirm applicable future module codes/delivery before complete180-EC certification.

### cp-000278 — Archaeology

Implemented: Corrected normalized instruction language toNLD+ENG while preserving rawNLD provenance; Freshly verified current adopted OER and first-year replacement codes; retained twelve5-EC first-year units; Preserved permitted30-EC genuine elective space, bringing the supported partial reconstruction to90 without outgoing specialisation credits.

- [Leiden Archaeology current study-guide product](https://studiegids.universiteitleiden.nl/api/product?code=BA-ARCH&type=STUDY&year=2261&language=en) — Year 2261 first-year and outgoing specialisation groups. Checked 9 October 2026. Fresh official source retrieved and inspected during this correction.
- [Leiden Archaeology current programme overview](https://www.universiteitleiden.nl/onderwijs/opleidingen/bachelor/archeologie/over-de-opleiding) — Voertaal; degree structure. Checked 9 October 2026. Fresh official source retrieved and inspected during this correction.
- [Leiden Archaeology programme structure](https://www.universiteitleiden.nl/en/education/study-programmes/bachelor/archaeology/about-the-programme1/programme-structure) — Current degree outline and first-year table. Checked 9 October 2026. Fresh official source retrieved and inspected during this correction.
- [Archaeology adopted Bachelor OER2026–2027](https://www.organisatiegids.universiteitleiden.nl/binaries/content/assets/archeologie/onderwijs--en-examenreglementen/2026-2027/oer-ba-en-2026-2027.pdf) — Adopted14July2026; Articles2.2,2.9,3.1–3.3; pp.6,9–11. Checked 9 October 2026. Fresh official PDF downloaded and visually inspected; prior audit retrieval limitation is resolved.
- [Archaeology2026–2027 replacement table](https://www.student.universiteitleiden.nl/binaries/content/assets/archeologie/onderwijsgerelateerd/replacement-table-archaeology-26-27.pdf) — Bachelor old/new course-code table, PDFp.1. Checked 9 October 2026. Fresh official replacement table downloaded and text checked.

Verification: Fresh current OER visually inspected at cohort/language clauses; all19 current first-year product/module entries independently checked. Twelve unique5-EC current units total60; zero/superseded items excluded; permitted elective30 counted once and unknown compulsory90 not filled. Deterministic canonical regeneration, all target validators, registry idempotence and generated-index checks passed.

Language correction and source-access/cohort findings are closed. External-programme-unresolved remains for the missing generic later-year requirements. No recurring monitoring is scheduled.

Remaining external questions: Provide an applicable complete new-cohort weighted second-/third-year generic curriculum, including bounded choices, internship and thesis requirements, accounting for the remaining90 compulsory EC without outgoing WA/HS blocks.

### Batch 9 completion

Five cases processed; two resolved external reconstructions and three with remaining external questions. No UCR reassessment or recurring research was performed. Deterministic compilation, all target validators, registry replay, generated-index checks and final full-corpus validation passed. GitHub checks are verified after each publication.

Current totals: {'processed_cases': 45, 'fully_resolved_first_stage_findings': 32, 'cases_with_remaining_external_research': 13}; corpus {'normalized_targets': 460, 'in_scope_targets': 438, 'excluded_targets': 22, 'comparisons': 301, 'exceptions': 137, 'exception_types': {'external-programme-unresolved': 24, 'no-defensible-ucr-match': 95, 'ucr-assessment-pending': 18}, 'missing_in_scope_ids': []}; unprocessed actionable cases 52.

## Batch 10 — next five cases in audit order

Each case is published and verified before proceeding. Independent UCR reassessment remains separate.

### cp-000280 — Bio-Pharmaceutical Sciences

Implemented: Removed falsely compulsory Pharmacy route and restored30 EC genuine approved elective space; Preserved all120 common plus14 finalyear skills/drug-development and16 research credits counted once; Changed active outcome to ucr-assessment-pending and preserved superseded UCR judgment.

- [Leiden Bio-Pharmaceutical Sciences current study guide](https://studiegids.universiteitleiden.nl/api/product?code=BA-BFW&type=STUDY&year=2261&language=en) — Year2261; required annual groups and year3 ordinary/Pharmacy distinction. Checked 9 October 2026.
- [Bachelor research practical work](https://studiegids.universiteitleiden.nl/api/product?code=4012BOO12Y&type=MODULE&year=2261&language=en) — MODULE credits and admission requirements. Checked 9 October 2026.
- [Bachelor research thesis](https://studiegids.universiteitleiden.nl/api/product?code=4012BTHESY&type=MODULE&year=2261&language=en) — MODULE credit field. Checked 9 October 2026.
- [Bachelor research presentation](https://studiegids.universiteitleiden.nl/api/product?code=4012BMOPRY&type=MODULE&year=2261&language=en) — MODULE credit field. Checked 9 October 2026.

Verification: Fresh programme and all54 linked module records checked; selected ordinary requirements independently total60+60+60=180 EC. All37 counted components are unique; project parent and optional Pharmacy modules excluded. Deterministic canonical regeneration, all target validators and generated-index checks passed.

External first-stage finding resolved. Separate UCR assessment remains pending; no recurring monitoring is scheduled.

### cp-000283 — Chinese Studies

Implemented: Removed unsupported certified180-EC/no-match claim and published external-programme-unresolved; Preserved first120 EC, prerequisite-valid choices, open30 and thesis10; Instantiated both semester choice instructions as an explicit190-EC diagnostic and retained the conflicting numeric180 interpretation.

- [Chinese Studies current official study guide](https://studiegids.universiteitleiden.nl/api/product?code=BA-CHI&type=STUDY&year=2261&language=en) — Year2261; year2 choices, year3 groups BA-CHI-3-K2/K3 and general narrative. Checked 9 October 2026.
- [Chinese Studies programme-specific OER2026–2027](https://www.organisatiegids.universiteitleiden.nl/binaries/content/assets/geesteswetenschappen/oer/2026-2027/ba-oso-chinastudies-2026-2027.pdf) — Articles2.2/4.2; pp.2,4–5; AppendixF. Checked 9 October 2026.
- [Chinese Labor Migration in Historical Perspective](https://studiegids.universiteitleiden.nl/api/product?code=5683KCAHPY&type=MODULE&year=2261&language=en) — MODULE credit/admission conditions and programme semester membership. Checked 9 October 2026.
- [China and the Global Political Economy](https://studiegids.universiteitleiden.nl/api/product?code=5683ICWEY&type=MODULE&year=2261&language=en) — MODULE credit/admission conditions and programme semester membership. Checked 9 October 2026.
- [Reading Chinese News](https://studiegids.universiteitleiden.nl/api/product?code=5683VCKL1Y&type=MODULE&year=2261&language=en) — MODULE credit/admission conditions and programme semester membership. Checked 9 October 2026.
- [Internet Chinese](https://studiegids.universiteitleiden.nl/api/product?code=5683VTICY&type=MODULE&year=2261&language=en) — MODULE credit/admission conditions and programme semester membership. Checked 9 October 2026.

Verification: Fresh programme and all linked module records retrieved; current OER prerequisite/transition table visually inspected. Selected current module credits and semesters verified; diagnostic total60+60+70=190 and no duplication or invented credits. Deterministic canonical regeneration, all target validators and generated-index checks passed.

Known source conflict is explicit; complete external reconstruction remains unresolved. Prior UCR judgment is historical only. No recurring monitoring is scheduled.

Remaining external questions: Clarify whether year3 requires one content and one language option overall or one of each in each semester; reconcile numeric5+5 with textual10+10. If the semester instructions are intended, provide an authoritative changed allocation closing180 without an inferred reduction of open30.

### cp-000284 — Criminology

Implemented: Retained and independently verified all24 revised first-/second-year5-EC modules; Made current cohort boundary explicit and excluded outgoing third-year35+15+10; Distinguished extracurricular30-EC minor from uncertified revised degree credits; removed future monitoring instructions.

- [Criminology current official study guide](https://studiegids.universiteitleiden.nl/api/product?code=BA-CRIM&type=STUDY&year=2261&language=en) — Year2261; annual groups BA-CRIM-1/2/3 and cohort notices. Checked 9 October 2026.
- [Criminology current programme overview](https://www.universiteitleiden.nl/onderwijs/opleidingen/bachelor/criminologie/over-de-opleiding/studieprogramma) — Curriculum15 EC; explicitly extracurricular30-EC minor; study-guide link. Checked 9 October 2026.

Verification: Fresh programme and all37 linked module records retrieved; each of the24 counted modules verifies5 EC. The supported sequence totals120 EC; outgoing year3 and zero-credit formation units are not counted. Deterministic canonical regeneration, all target validators and generated-index checks passed.

Published partial record remains externally unresolved, with precise cohort questions and no invented180-EC completion. Prior exception preserved. No recurring monitoring is scheduled.

Remaining external questions: Obtain an applicable revised-cohort third-year60-EC schedule with exact compulsory, bounded-choice, open-elective, research/thesis and progression requirements. Current university notice specifies the2027–2028 guide; no recurring monitoring is authorised.

### cp-000286 — Cybersecurity & Cybercrime

Implemented: Independently verified all22 first-/second-year units totaling120 EC; Restored explicitly published30-EC genuine third-year open elective space; supported partial total150; Kept missing compulsory third-year details explicit and removed future monitoring instructions.

- [Cybersecurity & Cybercrime current official study guide](https://studiegids.universiteitleiden.nl/api/product?code=BA-BACC&type=STUDY&year=2261&language=en) — Year2261; programme notice and year1/2 groups. Checked 9 October 2026.
- [Cybersecurity & Cybercrime current programme structure](https://www.universiteitleiden.nl/onderwijs/opleidingen/bachelor/fgga-cybersecurity--cybercrime/over-de-opleiding/studieprogramma) — Published22June2026; keuzeruimte30 EC in jaar3; annual integration description. Checked 9 October 2026.

Verification: Fresh programme and all22 linked module responses independently checked; required year totals60+60 match exactly. Fresh programme overview confirms open30; partial total150 preserves genuine space and excludes aggregate double counting or speculative modules. Deterministic canonical regeneration, all target validators and generated-index checks passed.

Known open-space omission is corrected; full external reconstruction remains unresolved. Prior exception preserved. No recurring monitoring is scheduled.

Remaining external questions: Establish the remaining30 EC compulsory third-year units, their credit/choice and progression rules, exact integration project and final assessment/thesis conditions from applicable official programme evidence. The guide specifies visibility fromJune2027; no recurring monitoring is authorised.

### cp-000288 — German Language and Culture

Implemented: Corrected normalized instruction languages toNLD+DEU+ENG through guarded replay while preserving rawNLD; Instantiated20-EC bounded choices as distinct10-EC literature and linguistics courses with valid literature-thesis progression; Preserved abroad25, thesis10 and genuine open30; retained175 unique credits with no repeated course or alternative variant.

- [German Language and Culture current study guide](https://studiegids.universiteitleiden.nl/api/product?code=BA-DUI&type=STUDY&year=2261&language=en) — Year2261; duplicate5631VB35Y and third-year20/10/30 rules. Checked 9 October 2026.
- [German Language and Culture programme-specific OER2026–2027](https://www.organisatiegids.universiteitleiden.nl/binaries/content/assets/geesteswetenschappen/oer/2026-2027/ba-oso-duitse-taal-en-cultuur-2026-2027.pdf) — Articles2.2/2.9/3.2.9/4.2; pp.2–4. Checked 9 October 2026.
- [Alte Neue Welt —10-EC module](https://studiegids.universiteitleiden.nl/api/product?code=5633K003Y&type=MODULE&year=2261&language=en) — MODULE credits, content and assessment. Checked 9 October 2026.
- [Sprachvariation und Ideologien —10-EC module](https://studiegids.universiteitleiden.nl/api/product?code=5633KSID1Y&type=MODULE&year=2261&language=en) — MODULE credits, content and assessment. Checked 9 October 2026.
- [German Language and Culture thesis](https://studiegids.universiteitleiden.nl/api/product?code=5633VB21Y&type=MODULE&year=2261&language=en) — MODULE credits and admission. Checked 9 October 2026.
- [Compulsory German-speaking study abroad](https://studiegids.universiteitleiden.nl/api/product?code=5632VBUITY&type=MODULE&year=2261&language=en) — MODULE credit and requirements. Checked 9 October 2026.

Verification: Fresh current OER language/prerequisite pages visually inspected; all29 linked current module responses independently retrieved. Counted modules verified; totals60+55+60=175. Specific20-EC choices satisfy same-discipline10 condition and thesis paper progression; no alternative variants counted. Deterministic canonical regeneration, all target validators, registry idempotence and generated-index checks passed. Final438-record full-corpus validation and guarded baseline registry replay passed; other459 normalized targets, original audit, raw provenance, unrelated records and all prior remediation histories unchanged. Language/provenance conflicts rejected.

Language and bounded-choice defects are closed. Full external reconstruction remains unresolved; no speculative5-EC replacement or UCR assessment is introduced. No recurring monitoring is scheduled.

Remaining external questions: Identify the applicable new-cohort replacement or allocation rule supplying the missing5 EC when5631VB35Y is counted once. Provide a corrected official programme table or authoritative cohort rule; language and known third-year choice corrections do not close this gap.

### Batch 10 completion

Five cases processed. Deterministic compilation, all target validators, guarded registry replay, generated-index checks and final full-corpus validation passed. GitHub checks are verified after each publication. No UCR reassessment or recurring research was performed.

Current totals: {'processed_cases': 50, 'fully_resolved_first_stage_findings': 33, 'cases_with_remaining_external_research': 17}; corpus {'normalized_targets': 460, 'in_scope_targets': 438, 'excluded_targets': 22, 'comparisons': 301, 'exceptions': 137, 'exception_types': {'external-programme-unresolved': 25, 'no-defensible-ucr-match': 93, 'ucr-assessment-pending': 19}, 'missing_in_scope_ids': []}; unprocessed actionable cases 47.

## Batch 11 — next five cases in audit order

Status: completed. Independent UCR reassessment remains separate.

### cp-000289 — Economics & Society

- [BA-ECS current 2026–2027 study-guide product](https://studiegids.universiteitleiden.nl/api/product?code=BA-ECS&type=STUDY&year=2261&language=en) — Fresh current official product verifies twelve first-year and twelve selected second-year 5-EC units. The 10-EC Package A (European Law and Social Law) is instantiated by published order; Package B is excluded. The guide explicitly defers Year 3 to 2027–2028, so only 120 EC are retained and no advanced, elective or thesis credit is invented. Checked 9 October 2026.

Verification: Counted comparator components total 120 EC with alternatives, parent/submodule overlaps and zero-credit items excluded. Deterministic canonical regeneration and target validation passed.

The current guide publishes complete Years 1 and 2 but explicitly defers the applicable Year 3 to the 2027–2028 guide. The missing 60 EC cannot be reconstructed without inventing route, choice, elective or final-project requirements.

### cp-000290 — English Language and Culture

- [BA-ENG current 2026–2027 study-guide product](https://studiegids.universiteitleiden.nl/api/product?code=BA-ENG&type=STUDY&year=2261&language=en) — Fresh current official product verifies nine first-year and eleven selected second-year units totaling 60+60 EC. The displayed-first British literature option is instantiated independently in each semester, and Early Modern Everyday English is selected by published order. Outgoing Language Acquisition 5/6 is explicitly last offered in 2026–2027 while the entrant third year changes significantly in 2027–2028; it is excluded. Checked 9 October 2026.

Verification: Counted comparator components total 120 EC with alternatives, parent/submodule overlaps and zero-credit items excluded. Deterministic canonical regeneration and target validation passed.

The current guide publishes complete Years 1 and 2, but states that the third year changes significantly in 2027–2028. Outgoing Language Acquisition 5/6 is last offered in 2026–2027 and cannot certify the Fall 2026 cohort's final 60 EC.

### cp-000294 — French Language and Culture

- [French Language and Culture programme-specific OER 2026–2027](https://www.organisatiegids.universiteitleiden.nl/binaries/content/assets/geesteswetenschappen/oer/2026-2027/ba-oso-franse-taal-en-cultuur-2026-2027.pdf) — No formal specialisation; Dutch and French instruction/assessment; thesis prerequisites and cohort-specific three/five seminar rules. The transition table separates September 2026 replacements from universal entrant requirements. Checked 9 October 2026.
- [BA-FRA current 2026–2027 study-guide product](https://studiegids.universiteitleiden.nl/api/product?code=BA-FRA&type=STUDY&year=2261&language=en) — Current allocation is reconstructed as first year60 + fixed upper-year35 + four alternating-cycle units30 + three concrete seminars15 + thesis10 + genuine open30 =180 EC. The selected legal-French practical seminar and two research seminars meet the current three-seminar/two-research rule. Alternants are counted once across the two-year cycle; Poetry and Theatre10 and Metamorphoses of the Novel5 are explicitly not offered in 2026–2027, so this is a degree allocation rather than a claim that all units run in one year. The adopted formal rules state no specialisation and Dutch/French instruction. Checked 9 October 2026.

Verification: Counted comparator components total 180 EC with alternatives, parent/submodule overlaps and zero-credit items excluded. Deterministic canonical regeneration and target validation passed.

The external curriculum and bound choices are now complete at 180 EC, but the prior UCR no-match judgment relied on superseded external facts and is not carried forward without the separately excluded UCR reassessment.

### cp-000295 — Medicine

- [BA-GEN current 2026–2027 study-guide product](https://studiegids.universiteitleiden.nl/api/product?code=BA-GEN&type=STUDY&year=2261&language=en) — Current provisional first and second years are retained as 60+60 EC. Parent packages are counted once; zero-credit submodules and the exchange-only AWV variant are not stacked. Required Mechanisms of Disease 1 and 2 are English-medium while Dutch remains the main programme language, supporting normalized NLD+ENG. The product says the new third-year programme will follow; outgoing third-year courses and the historical distributed endpoint are not attached to this cohort. Checked 9 October 2026.

Verification: Counted comparator components total 120 EC with alternatives, parent/submodule overlaps and zero-credit items excluded. Deterministic canonical regeneration and target validation passed.

The current guide labels Years 1 and 2 provisional and states that the revised third year will follow. The publicly linked adopted regulations remain 2025–2026. A complete new-cohort 180-EC pathway cannot be certified from the historical third year.

### cp-000297 — Classics

- [Classics programme-specific OER 2026–2027](https://www.organisatiegids.universiteitleiden.nl/binaries/content/assets/geesteswetenschappen/oer/2026-2027/ba-oso-griekse-en-latijnse-taal-en-cultuur-2026-2027.pdf) — Four formal specialisations in order: Antieke wijsbegeerte, Grieks, Latijn and Oude geschiedenis; Dutch instruction; route and Greek/Latin workshop/read-list prerequisites. Checked 9 October 2026.
- [BA-GRL current 2026–2027 study-guide product](https://studiegids.universiteitleiden.nl/api/product?code=BA-GRL&type=STUDY&year=2261&language=en) — Current 180-EC Classics is reconstructed as 60+60+60. The formal first-listed specialisation Antieke wijsbegeerte is selected independently of UCR fit. The representative admitted profile uses Greek A and Latin B placement (no Greek school exam, Latin at school-exam level), not stacked placement levels. Year2 selects the Stoa philosophy workshop and current Greek language seminar. Year3 selects Greek Reading List and Latin Silius Italicus workshop, preserving both languages, followed by a philosophy-aligned thesis and genuine open30. Zero-credit thesis seminar and alternative options are excluded. Checked 9 October 2026.

Verification: Counted comparator components total 180 EC with alternatives, parent/submodule overlaps and zero-credit items excluded. Deterministic canonical regeneration and target validation passed.

The external programme and formal route are now complete at 180 EC, but the prior UCR no-match judgment was based on an outdated route/course reconstruction and requires the separately excluded UCR reassessment.


### Batch 11 completion

Five cases processed. Deterministic regeneration matched all five committed canonical records; target validators, compiler suites, guarded registry replay, generated-index checks, registry-interest checks and final 438-record full-corpus validation passed. The original audit, permanent IDs, raw provenance, unrelated records and prior remediation history were preserved. No UCR reassessment or recurring research was performed.

Current totals: 55 processed cases; 35 fully resolved first-stage findings; 20 cases retaining external research questions. The live corpus contains 460 normalized targets, 438 in-scope records, 301 comparisons and 137 exceptions (26 external-programme-unresolved, 90 no-defensible-ucr-match and 21 ucr-assessment-pending), with no missing in-scope IDs. There are 42 unprocessed actionable first-stage cases.

## Batch 12 — next five cases in audit order

Status: completed. Independent UCR reassessment remains separate.

### cp-000299 — International Studies

- [BA-INT current 2026–2027 study-guide product](https://studiegids.universiteitleiden.nl/api/product?code=BA-INT&type=STUDY&year=2261&language=en) — Current official programme verifies a 60+60+60 Africa/Arabic pathway. The revised first year uses Introduction to International Studies10 and Humanities in a Digital World5; former Academic Literacy and Foundations of Political Economy are not added. Communicating Across Cultures is one selected bound option, not universal. Africa/Arabic, historical methods, Nomos–Paranomos, PRINS10, Language and Culture in Practice5, area thesis15 and genuine open30 are each counted once. Checked 9 October 2026.

Verification: Counted comparator components total 180 EC; alternatives, duplicate modules, parent/submodule overlaps and zero-credit items are excluded. Deterministic regeneration and target validation passed.

The corrected external pathway is complete at 180 EC, but the prior no-match judgment was made against a superseded external reconstruction and requires the separately excluded UCR reassessment.

### cp-000300 — Italian Language and Culture

- [BA-ITA current 2026–2027 study-guide product](https://studiegids.universiteitleiden.nl/api/product?code=BA-ITA&type=STUDY&year=2261&language=en) — Current Years 1 and 2 verify 60+60 EC. Year3 nominally requires Laboratorio Rinascimento5 + restricted15 + thesis10 + open30, but four of five restricted options duplicate compulsory Year2 modules; only Linguistica Italiana5 is distinct. The supported nonduplicated diagnostic is therefore170 EC, with10 EC unresolved. Italian and required English-taught core units support normalized NLD+ITA+ENG; raw NLD remains unchanged. Checked 9 October 2026.
- [Italian Language and Culture programme-specific OER 2026–2027](https://www.organisatiegids.universiteitleiden.nl/binaries/content/assets/geesteswetenschappen/oer/2026-2027/ba-oso-italiaanse-taal-en-cultuur-2026-2027.pdf) — No formal directions; Dutch/Italian instruction; transition and thesis rules. It does not authorize repeated credit or automatically replace discontinued upper-year courses. Checked 9 October 2026.

Verification: Counted comparator components total 170 EC; alternatives, duplicate modules, parent/submodule overlaps and zero-credit items are excluded. Deterministic regeneration and target validation passed.

The current restricted-choice menu cannot supply15 distinct third-year EC without repeating compulsory Year2 modules. Only170 nonduplicated EC are retained; no alternating-course or replacement rule is invented.

### cp-000302 — Korean Studies

- [BA-KOR current 2026–2027 study-guide product](https://studiegids.universiteitleiden.nl/api/product?code=BA-KOR&type=STUDY&year=2261&language=en) — Current weighted requirements close 60+60+60. Themes and Approaches counts10 because the current group and module agree despite prose saying5. Korean3 is the15-EC Leiden option; Business Korean is selected because its published prerequisites are met, whereas the earlier Academic Purposes option additionally requires thesis eligibility. Topical work and seminar precede the final paper10; genuine open30 is preserved. Required current courses document English instruction, supporting NLD+ENG while Korean remains the subject language. Checked 9 October 2026.
- [Korean Studies programme-specific OER 2026–2027](https://www.organisatiegids.universiteitleiden.nl/binaries/content/assets/geesteswetenschappen/oer/2026-2027/ba-oso-koreastudies-2026-2027.pdf) — No formal specialisations; Dutch formal classification; current Korean progression and final-paper prerequisites. Checked 9 October 2026.

Verification: Counted comparator components total 180 EC; alternatives, duplicate modules, parent/submodule overlaps and zero-credit items are excluded. Deterministic regeneration and target validation passed.

The external curriculum is complete at180 EC and instruction metadata are corrected, but the prior UCR judgment used incomplete metadata and is handed off for the separately excluded UCR reassessment.

### cp-000304 — Latin American Studies

- [BA-LAS current 2026–2027 study-guide product](https://studiegids.universiteitleiden.nl/api/product?code=BA-LAS&type=STUDY&year=2261&language=en) — Current Spanish pathway closes 60+60+60. Spanish is selected for the broad regional identity; Portuguese/Brazil is an alternative, not a universal requirement. Required approved Latin America study abroad30 remains an approved package without invented host units. Public Policies5 is the first bound choice, research methods precedes thesis10, and genuine open30 is preserved. Formal current rules specify Dutch, English, Spanish and Portuguese instruction. Checked 9 October 2026.
- [Latin American Studies programme-specific OER 2026–2027](https://www.organisatiegids.universiteitleiden.nl/binaries/content/assets/geesteswetenschappen/oer/2026-2027/ba-oso-latijns-amerikastudies-2026-2027.pdf) — No formal graduation directions; Dutch, English, Spanish and Portuguese instruction; abroad, research-methods and thesis progression rules. Checked 9 October 2026.

Verification: Counted comparator components total 180 EC; alternatives, duplicate modules, parent/submodule overlaps and zero-credit items are excluded. Deterministic regeneration and target validation passed.

The selected external pathway is complete at180 EC and language metadata are corrected, but the prior UCR judgment requires the separately excluded reassessment against this corrected basis.

### cp-000306 — Middle Eastern Studies

- [BA-MOS-MMO current 2026–2027 study-guide product](https://studiegids.universiteitleiden.nl/api/product?code=BA-MOS-MMO&type=STUDY&year=2261&language=en) — Current Modern Middle East Studies with Arabic retains 60+60+55=175 unique EC. The same 5852VCAAY History of Central Asia & Afghanistan course appears as compulsory in Year2 and again in the Year3 route; it is counted once and no historical replacement is imported. Comparative Literatures10, thesis seminar5, thesis10 and genuine open30 remain distinct. Current OER confirms Modern Middle East Studies as a formal direction and marks Islam Studies no intake. Required English-taught regional courses support normalized NLD+ENG. Checked 9 October 2026.
- [Middle Eastern Studies programme-specific OER 2026–2027](https://www.organisatiegids.universiteitleiden.nl/binaries/content/assets/geesteswetenschappen/oer/2026-2027/ba-oso-midden-oostenstudies-2026-2027.pdf) — Current directions include Modern Middle East Studies; Islam Studies has no intake. Dutch formal classification and thesis prerequisites; no replacement for duplicated5852VCAAY. Checked 9 October 2026.

Verification: Counted comparator components total 175 EC; alternatives, duplicate modules, parent/submodule overlaps and zero-credit items are excluded. Deterministic regeneration and target validation passed.

The current guide repeats identical5-EC module5852VCAAY across Years2 and3. Counting once leaves175 EC; no distinct replacement or changed choice rule is currently established.

### Batch 12 completion

Five cases processed. Three first-stage external findings were resolved; Italian Language and Culture and Middle Eastern Studies retain precise external-programme questions. Deterministic regeneration matched all five canonical records; target validators, compiler suites, guarded registry replay, generated-index checks, registry-interest checks and final 438-record full-corpus validation passed. The original audit, permanent IDs, raw provenance, unrelated records and prior remediation history were preserved. No UCR reassessment or recurring research was performed.

Current totals: 60 processed cases; 38 fully resolved first-stage findings; 22 cases retaining external research questions. The live corpus contains 460 normalized targets, 438 in-scope records, 301 comparisons and 137 exceptions (27 external-programme-unresolved, 86 no-defensible-ucr-match and 24 ucr-assessment-pending), with no missing in-scope IDs. There are 37 unprocessed actionable first-stage cases.


## Batch 13 — next five cases in audit order

Status: completed. Independent UCR reassessment remains separate.

### cp-000308 — Physics

- [BA-NTK current 2026–2027 study-guide product](https://studiegids.universiteitleiden.nl/api/product?code=BA-NTK&type=STUDY&year=2261&language=en) — Current requirements close 60+60+60. The second-year 9-EC restricted choice uses Experimental Projects6, whose team/lecturer preparation is retained, plus semester-2 Fluid Phenomena3; Astro-Particle Physics is excluded because its expected preparation includes compulsory courses taught later in the same year. Year3 preserves genuine open30, separate Relativistic Electrodynamics3 and the 27-EC research project split20+3+1+3. Required current upper-year modules support normalized NLD+ENG. Checked 9 October 2026.

Verification: Counted comparator components total 180 EC; alternatives, repeated modules, duplicate content, parent/submodule overlaps and zero-credit items are excluded. Deterministic regeneration and target validation passed.

The corrected external curriculum is complete at 180 EC and language metadata are corrected; the superseded UCR no-match judgment is handed off for the separately excluded UCR reassessment.

### cp-000309 — Dutch Studies

- [BA-DST current 2026–2027 study-guide product](https://studiegids.universiteitleiden.nl/api/product?code=BA-DST&type=STUDY&year=2261&language=en) — The current allocation is nominally 60+60+60 after adding the explicit second-year Philosophy of Science requirement and selecting one linguistics option in each semester. The applicable Philosophy module code is unresolved because programme prose, membership and the formal transition table conflict. The revised third-year notice says semester1 is entirely open, while the displayed membership places Academic Reading and Writing and split elective space there. Formal rules verify Dutch and English instruction. The 180-EC figure is an allocation diagnostic, not a certified coherent timetable. Checked 9 October 2026.
- [Dutch Studies programme-specific OER effective 2026–2027](https://www.organisatiegids.universiteitleiden.nl/binaries/content/assets/geesteswetenschappen/oer/2026-2027/ba-oso-dutch-studies-2025-2026.pdf) — Formal Dutch/English instruction and transition table; the table retains Humanities in a Digital World and does not resolve the current product conflict. Checked 9 October 2026.

Verification: Counted comparator components total 180 EC; alternatives, repeated modules, duplicate content, parent/submodule overlaps and zero-credit items are excluded. Deterministic regeneration and target validation passed.

Current official sources support a nominal 180-EC allocation but conflict on the Philosophy module identity and the revised third-year semester/choice structure; no exact module code or reconciled timetable is invented.

Remaining external questions: Obtain the actual Dutch Studies Philosophy of Science module code/version and a reconciled applicable third-year timetable/choice allocation: one notice says first semester wholly open with a second-semester in-depth module, while the displayed choice rule still spans both semesters and Academic Reading/Writing is offered in semester 1.

### cp-000311 — Notarial Law

- [BA-NOT current 2026–2027 study-guide product](https://studiegids.universiteitleiden.nl/api/product?code=BA-NOT&type=STUDY&year=2261&language=en) — Current Years1 and2 close 60+60, including the first published technology/law restricted option and genuine10-EC notarial optional space. The displayed Year3 is expressly for entrants in 2024 or earlier; the revised entrant Year3 will appear in the 2027–2028 guide. Outgoing third-year courses are not attached to the current cohort. Checked 9 October 2026.

Verification: Counted comparator components total 120 EC; alternatives, repeated modules, duplicate content, parent/submodule overlaps and zero-credit items are excluded. Deterministic regeneration and target validation passed.

The applicable new-cohort curriculum is verified only through 120 EC. The published third year belongs to entrants in 2024 or earlier, while the revised third year is deferred to the 2027–2028 guide.

Remaining external questions: Obtain the revised third-year curriculum from the 2027–2028 guide. Verify current full/part-time pacing from applicable regulations without treating a future offering end date as current programme closure.

### cp-000312 — Ancient Near Eastern Studies

- [BA-ONO-NOP current 2026–2027 study-guide product](https://studiegids.universiteitleiden.nl/api/product?code=BA-ONO-NOP&type=STUDY&year=2261&language=en) — The formal broad route The Ancient Near Eastern World remains current. Four repeated module codes already reduce the catalogue allocation to160 nominal EC. The two Philosophy of Science codes carry identical core descriptions/objectives; counting that content once leaves155 supported unique-content EC. No replacement or distinct-credit rule is invented. Required current heritage and modern-regional history modules support normalized NLD+ENG. Checked 9 October 2026.
- [Ancient Near Eastern Studies programme-specific OER 2026–2027](https://www.organisatiegids.universiteitleiden.nl/binaries/content/assets/geesteswetenschappen/oer/2026-2027/ba-oso-oude-nabije-oosten-studies-2026-2027.pdf) — Formal routes include The Ancient Near Eastern World; Dutch is the formal programme language. The OER does not supply replacements for the repeated catalogue modules. Checked 9 October 2026.

Verification: Counted comparator components total 155 EC; alternatives, repeated modules, duplicate content, parent/submodule overlaps and zero-credit items are excluded. Deterministic regeneration and target validation passed.

Only 155 EC of distinct current content are supported after repeated module codes and the duplicate-content Philosophy versions are counted once. A single-cohort replacement/choice table is still missing.

Remaining external questions: Obtain a single-cohort replacement/choice table for repeated 5532VGONOY, 5531VATY, 5531VMCEY and 5851VHMMEY, and establish whether 5000VWF2Y/5000VWFY are alternative semester/cohort versions. Resolve the Ancient History workshop prerequisite to the relevant Themacollege when instantiating the current route.

### cp-000314 — Political Science

- [BA-POWE-NIP current 2026–2027 study-guide product](https://studiegids.universiteitleiden.nl/api/product?code=BA-POWE-NIP&type=STUDY&year=2261&language=en) — The new Dutch-taught Leiden route National and International Politics has ten current first-year requirements totaling60 EC. The formal annex publishes later years for IRO and for the outgoing Political Science/International Politics routes, whose intake ended with 2025–2026; those curricula are not substituted for the new route. Applicable Years2 and3 remain unpublished. Checked 9 October 2026.
- [Political Science bachelor annex 2026–2027](https://www.organisatiegids.universiteitleiden.nl/binaries/content/assets/sociale-wetenschappen/politieke-wetenschap/reglementen/oeren-2026-2027/2026-2027-oer-powe-bsc-annex-eng.pdf) — Formal NIP first-year table totals60 EC. Separate later-year tables apply to IRO or phased-out POL/IP cohorts admitted by 2025–2026. Checked 9 October 2026.

Verification: Counted comparator components total 60 EC; alternatives, repeated modules, duplicate content, parent/submodule overlaps and zero-credit items are excluded. Deterministic regeneration and target validation passed.

Only the applicable new-route first year of 60 EC is published. Outgoing POL/IP later years and the distinct English IRO programme cannot be spliced into the NIP pathway.

Remaining external questions: Obtain the applicable NIP second- and third-year curricula when published in subsequent guides/formal annexes. Require one coherent new-route 180-EC sequence, not an outgoing POL/IP continuation.

### Batch 13 completion

Five cases processed. Physics is externally resolved; Dutch Studies, Notarial Law, Ancient Near Eastern Studies and Political Science retain precise current-source or new-cohort publication questions. Deterministic regeneration matched all five canonical records; target validators, compiler suites, guarded registry replay, generated-index checks, registry-interest checks and final 438-record full-corpus validation passed. The original audit, permanent IDs, raw provenance, unrelated records and prior remediation history were preserved. No UCR reassessment or recurring research was performed.

Current totals: 65 processed cases; 39 fully resolved first-stage findings; 26 cases retaining external research questions. The live corpus contains 460 normalized targets, 438 in-scope records, 301 comparisons and 137 exceptions (28 external-programme-unresolved, 84 no-defensible-ucr-match and 25 ucr-assessment-pending), with no missing in-scope IDs. There are 32 unprocessed actionable first-stage cases.


## Batch 14 — next five cases in audit order

Status: in progress. Independent UCR reassessment remains separate.

### cp-000317 — Law

- [BA-RGH current 2026–2027 study-guide product](https://studiegids.universiteitleiden.nl/api/product?code=BA-RGH&type=STUDY&year=2261&language=en) — The current product publishes the revised first and second years only: twelve 5-EC first-year requirements and eleven 5-EC second-year requirements plus the first-listed 5-EC technology/law choice. Its displayed third year is expressly restricted to entrants in 2024 or earlier; the revised third year is deferred to the 2027–2028 guide. Checked 9 October 2026.
- [Law bachelor OER 2026–2027](https://www.organisatiegids.universiteitleiden.nl/binaries/content/assets/rechtsgeleerdheid/reglementen/oeren/2026-2027/oer-bachelor-nl-rgl.pdf) — Formal current entry is full-time, 180 EC, Dutch with some English, and allocated as 150 EC compulsory/bound plus 30 EC free choice; those aggregates do not supply the missing revised course-level third year. Checked 9 October 2026.
- [Law bachelor current entry page](https://www.universiteitleiden.nl/onderwijs/opleidingen/bachelor/rechtsgeleerdheid) — Current ordinary entry independently lists the three-year full-time programme and Dutch/English instruction. Checked 9 October 2026.

Verification: Counted comparator components total 120 EC; alternatives, repeated modules, duplicate content, parent/submodule overlaps and zero-credit items are excluded. Deterministic regeneration and target validation passed.

Current official sources support the revised entrant curriculum only through 120 EC. The outgoing third year cannot be combined with it, and the formal aggregate 150/30 allocation is not a course-level substitute.

Remaining external questions: Obtain revised third year from the 2027–2028 guide; reconcile any outgoing part-time continuation with current full-time-only OER and admissions before displaying historical delivery modes as currently available.

### cp-000318 — Religious Studies

- [BA-REL current 2026–2027 study-guide product](https://studiegids.universiteitleiden.nl/api/product?code=BA-REL&type=STUDY&year=2261&language=en) — The revised current-entry first year contains ten positive-credit modules totaling 60 EC. The displayed second year and formal transition table apply to students who entered in 2025–2026 or earlier; no new-cohort later years are published. Checked 9 October 2026.
- [Religious Studies programme-specific OER 2026–2027](https://www.organisatiegids.universiteitleiden.nl/binaries/content/assets/geesteswetenschappen/oer/2026-2027/ba-oso-religiewetenschappen-2026-2027.pdf) — The new curriculum starts on 1 September 2026; its published second-year transition programme is expressly limited to 2025–2026-or-earlier entrants. Checked 9 October 2026.
- [Required Islam module](https://studiegids.universiteitleiden.nl/api/product?code=5071VITSIY&type=MODULE&year=2261&language=en) — This required revised first-year module specifies English instruction, establishing ordinary required English alongside the formal Dutch programme classification. Checked 9 October 2026.
- [Required Religion in the World module](https://studiegids.universiteitleiden.nl/api/product?code=5071VRWY&type=MODULE&year=2261&language=en) — This required revised first-year module specifies English instruction, establishing ordinary required English alongside the formal Dutch programme classification. Checked 9 October 2026.
- [Required Hindu Religions module](https://studiegids.universiteitleiden.nl/api/product?code=5481KIHRY&type=MODULE&year=2261&language=en) — This required revised first-year module specifies English instruction, establishing ordinary required English alongside the formal Dutch programme classification. Checked 9 October 2026.
- [Required Qualitative Research module](https://studiegids.universiteitleiden.nl/api/product?code=5071VMT02Y&type=MODULE&year=2261&language=en) — This required revised first-year module specifies English instruction, establishing ordinary required English alongside the formal Dutch programme classification. Checked 9 October 2026.

Verification: Counted comparator components total 60 EC; alternatives, repeated modules, duplicate content, parent/submodule overlaps and zero-credit items are excluded. Deterministic regeneration and target validation passed.

Only the revised 60-EC first year is currently applicable to a 2026 entrant. Later-year transition material belongs to an earlier cohort, so a coherent current-entry 180-EC pathway cannot yet be certified.

Remaining external questions: Obtain applicable new-cohort second/third-year requirements and a current full/part-time pacing rule. Apply qualitative-methods progression from the required first-year source-research course; no outgoing later-year substitution without transition authority.

### cp-000319 — Russian Studies (Russische studies)

- [BA-RUS current 2026–2027 study-guide product](https://studiegids.universiteitleiden.nl/api/product?code=BA-RUS&type=STUDY&year=2261&language=en) — The selected Politics, History and Economics route closes 60+60+60, preserves the prescribed language-abroad units, thesis and genuine open 30 EC, and does not count the zero-credit thesis seminar. Checked 9 October 2026.
- [Russian Studies programme-specific OER 2026–2027](https://www.organisatiegids.universiteitleiden.nl/binaries/content/assets/geesteswetenschappen/oer/2026-2027/ba-oso-russische-studies-2026-2027.pdf) — The OER confirms the two formal routes, language progression and thesis gates; Politics, History and Economics is the first-listed broad route. Checked 9 October 2026.
- [Required Introduction to Russian Studies module](https://studiegids.universiteitleiden.nl/api/product?code=5641V011Y&type=MODULE&year=2261&language=en) — This required 5-EC module specifies English instruction, establishing required English alongside Dutch. Checked 9 October 2026.

Verification: Counted comparator components total 180 EC; alternatives, repeated modules, duplicate content, parent/submodule overlaps and zero-credit items are excluded. Deterministic regeneration and target validation passed.

The corrected external curriculum is complete at 180 EC and normalized language metadata are corrected. The superseded UCR no-match judgment is preserved in remediation history for the separately excluded UCR reassessment.

### cp-000322 — South and Southeast Asian Studies

- [BA-ZZO current 2026–2027 study-guide product](https://studiegids.universiteitleiden.nl/api/product?code=BA-ZZO&type=STUDY&year=2261&language=en) — The Hindi/modern thematic/Leiden selection allocates 60+60+60, preserves genuine open 15+15 EC and nonoverlapping Buddhist options, but its required Reading course points to an absent first-year Area Studies prerequisite. Checked 9 October 2026.
- [South and Southeast Asian Studies OER 2026–2027](https://www.organisatiegids.universiteitleiden.nl/binaries/content/assets/geesteswetenschappen/oer/2026-2027/ba-oso-south-and-southeast-asian--studies-2026-2027.pdf) — The OER states that formal specialisations are not applicable, instruction is English, and at least 40 EC of language acquisition is required; it supplies no waiver or replacement for the Reading prerequisite. Checked 9 October 2026.
- [Required Reading South and Southeast Asia module](https://studiegids.universiteitleiden.nl/api/product?code=5482V000Y&type=MODULE&year=2261&language=en) — The required 5-EC course explicitly requires prior completion of the faculty Area Studies core, which does not appear in the current first year. Checked 9 October 2026.
- [Required Philosophy of Science module](https://studiegids.universiteitleiden.nl/api/product?code=5000VPHSCY&type=MODULE&year=2261&language=en) — The shared required module metadata specify Dutch, conflicting with the programme OER's English-only instruction rule. Checked 9 October 2026.
- [Tantric Buddhism module](https://studiegids.universiteitleiden.nl/api/product?code=5482KTB1Y&type=MODULE&year=2261&language=en) — Prior Buddhist background is advantageous but not a hard admission gate; this option does not create the material conflict. Checked 9 October 2026.

Verification: Counted comparator components total 180 EC; alternatives, repeated modules, duplicate content, parent/submodule overlaps and zero-credit items are excluded. Deterministic regeneration and target validation passed.

Current sources conflict on an applicable prerequisite and required-module language. The weighted 180-EC allocation is retained only as a diagnostic reconstruction; a coherent eligible pathway is not certified.

Remaining external questions: Obtain an applicable replacement/waiver rule for Reading5482V000Y prerequisite Area Studies, and the actual SSEAS English-medium version/offer of Philosophy5000VPHSCY. Verify cohort authority without adding an uncredited prerequisite to180 or treating recommended Buddhist background as a hard gate.
