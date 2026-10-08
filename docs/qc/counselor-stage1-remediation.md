# First-stage counselor corrections

The completed audit remains the evidence baseline. This report records implementation only; its live register is `data/counselor/qc/stage1-remediation.json`. UCR comparability is not reassessed here.

## Batch 1 — five representative cases

Status: in-progress.

| Target | Implemented correction | Remaining work |
|---|---|---|
| cp-000333 — Academic Primary Teacher Education (ALPO) | double-bachelor classification; UU and HU participant identities; four-year full-time entry; withdrawal from standard-only counselor scope with evidence preserved | Verify current combined study load and credit sharing before replacing the embedded 180-EC study_load_ec field. |
| cp-000095 — Pharmaceutical Sciences (Farmaceutische Wetenschappen) | Corrected narrative to 150 EC required major + 30 EC profiling = 180 EC | None within this correction; UCR reassessment remains separate. |

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
