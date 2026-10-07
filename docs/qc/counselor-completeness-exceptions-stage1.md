# Counselor completeness and exceptions: first-stage audit

Status: in progress. Batches 1–7 completed on 7 October 2026: all 19 scope exclusions and 51 exceptions audited within the first-stage scope. 89 exceptions remain pending.

## Scope and method

This audit follows the current Master Specification §4.1 and Production Instructions §§4.1 and 4.4. A target belongs to counselor production only when production_eligible=true, production_order is nonblank, and programme_type=standard. Non-standard degree structures remain legitimate registry targets. The audit tests the factual attributes behind exclusion without reconsidering the presentation policy itself.

The starting population is the normalized registry, not the upstream DUO/RIO population. Existing normalization decisions, post-build corrections, source-row crosswalks and offering-ID crosswalks were inspected for every audited target, then checked against fresh official evidence. Exclusions were selected in ascending registry order, followed by exceptions in ascending programme-ID order. Future batches resume from the explicit pending queue in the JSON dataset.

The classification applies only to the stated audit scope. Resolving an external curriculum normally requires reassess-exception rather than automatically reprocess-as-comparison. An outdated finding requires historical evidence of a later change; temporal uncertainty must be retained where that distinction cannot be established. No UCR curriculum was rebuilt, and no mechanical production validation was repeated.

## Population and reconciliation

| Population | Total | Audited | Pending |
|---|---:|---:|---:|
| Normalized registry targets | 460 | — | — |
| In-scope targets with canonical records | 441 | — | — |
| Completed comparisons | 301 | Outside this stage | — |
| Completed exceptions | 140 | 51 | 89 |
| Excluded normalized targets | 19 | 19 | 0 |
| First-stage audit cases | 159 | 70 | 89 |

All 441 in-scope IDs have a canonical filename; there are no missing in-scope IDs, duplicate record filenames or out-of-scope canonical records. The review-index ID set matches both registry scope and canonical filenames. Status totals use that current generated index; all 140 indexed exceptions were additionally read directly to verify ID, exception status and formal type. Enumeration does not constitute a substantive exception audit.

| Formal exception type | Corpus total | Substantively audited |
|---|---:|---:|
| external-programme-unresolved | 20 | 7 |
| no-defensible-ucr-match | 117 | 42 |
| registry-exception | 3 | 2 |

## Batch 1 findings

| Finding | Count |
|---|---:|
| confirmed | 10 |
| incorrect | 0 |
| outdated | 0 |
| still-unresolved | 0 |

| Required action | Count |
|---|---:|
| none | 10 |
| reprocess-as-comparison | 0 |
| reassess-exception | 0 |
| correct-registry-and-reprocess | 0 |
| research-again-later | 0 |

All ten existing exclusions are confirmed within the current scope rules. No case requires a correction or reprocessing, and none is classified as outdated. Confirmation does not imply that UCR lacks relevant courses or that excluding every joint degree is academically necessary. Active joint degrees are excluded by the approved presentation rule.

For Groningen cases, the shared structural evidence establishes the combination bachelor and its credit-sharing structure. The 180-EC size of the philosophy award is not the total load of a standalone two-degree programme. Each named track was separately verified against the current bachelor documents.

| ID | Programme | Institution | Finding | Action |
|---|---|---|---|---|
| cp-000007 | Double bachelor BSc² in Econometrics and Economics | Erasmus University Rotterdam | confirmed | none |
| cp-000012 | RASL Dual Degree Philosophy and WdKA | Erasmus University Rotterdam | confirmed | none |
| cp-000015 | Economics and Taxation | Erasmus University Rotterdam | confirmed | none |
| cp-000120 | Liberal Arts and Sciences (joint degree) | University of Amsterdam | confirmed | none |
| cp-000147 | Urban Sustainability Studies (joint degree) | Maastricht University | confirmed | none |
| cp-000157 | Theology (joint degree) | Protestant Theological University | confirmed | none |
| cp-000164 | Philosophy of a Specific Discipline — Cognitive Sciences track | University of Groningen | confirmed | none |
| cp-000169 | Philosophy of a Specific Discipline — Economic and Social Sciences track | University of Groningen | confirmed | none |
| cp-000177 | Philosophy of a Specific Discipline — History track | University of Groningen | confirmed | none |
| cp-000186 | Philosophy of a Specific Discipline — Art and Cultural Studies track | University of Groningen | confirmed | none |

## Batch 1 evidence for each audited exclusion

### cp-000007 — Double bachelor BSc² in Econometrics and Economics

Institution: Erasmus University Rotterdam. Audit scope: Programme type, double-degree identity and merged source provenance.

Exclusion trigger: `programme_type='double-bachelor'`. The relevant rule is Master Specification §4.1 / Production Instructions §4.1.

Official evidence confirms the merged target is a 264-EC double bachelor. Its double-bachelor type correctly excludes it under the standard-only presentation rule.

Provenance: source worksheet row(s) 9, 10; normalization step2-resolved; decision cases rc-0001, rc-0002. Source-row and offering-ID sets exactly agree with the normalized target.

Current official sources (checked 7 October 2026):

- [Facts & Figures — Double bachelor BSc² in Econometrics and Economics](https://www.eur.nl/en/bachelor/double-bachelor-bsc2-econometrics-and-economics/facts-figures) — Programme facts: duration, study points and double degree; Current programme-facing page; includes 2027–2028 application information.

Result: confirmed; required action: none; exclusion should remain. No material factual question remains unresolved within this case’s audit scope.

### cp-000012 — RASL Dual Degree Philosophy and WdKA

Institution: Erasmus University Rotterdam; Willem de Kooning Academy. Audit scope: Exact Philosophy/WdKA route, dual-degree structure and current admissions.

Exclusion trigger: `programme_type='dual-degree-route'`. The relevant rule is Master Specification §4.1 / Production Instructions §4.1.

The exact Philosophy/WdKA route remains a five-year combination of two bachelors. Its dual-degree-route classification correctly excludes it.

Provenance: source worksheet row(s) 15; normalization step2-resolved; decision cases rc-0003. Source-row and offering-ID sets exactly agree with the normalized target.

Current official sources (checked 7 October 2026):

- [Dual Degree with Arts and Philosophy](https://www.eur.nl/en/esphil/education/dual-degree-arts-and-philosophy) — The Dual Degree — Philosophy with Arts; Current undated programme page.
- [Facts & Figures — Dual Degree in Arts and Sciences](https://www.eur.nl/en/bachelor/dual-degree-arts-and-sciences/facts-figures) — Programme facts; Current programme-facing page.
- [Application — Dual Degree in Arts and Sciences](https://www.eur.nl/en/bachelor/dual-degree-arts-and-sciences/application) — Application deadlines for academic year 2026–2027; 2026–2027.

Use this umbrella page for RASL scale only; exact Philosophy/WdKA identity comes from the dedicated Philosophy page and current admissions list. Evidence locator: Programme facts and CROHO names.

Result: confirmed; required action: none; exclusion should remain. No material factual question remains unresolved within this case’s audit scope.

### cp-000015 — Economics and Taxation

Institution: Erasmus University Rotterdam. Audit scope: Lifecycle, new enrolment and teach-out status.

Exclusion trigger: `production_eligible='false'; production_order=''`. The relevant rule is Master Specification §4.1 / Production Instructions §4.1.

EUR explicitly ends new applications and permits completion through 2028–2029. Retaining this target as teach-out-only with no production eligibility or order is justified.

Provenance: source worksheet row(s) 18; normalization step2-resolved; decision cases rc-0004. Source-row and offering-ID sets exactly agree with the normalized target.

Current official sources (checked 7 October 2026):

- [Bachelor Fiscale Economie](https://www.eur.nl/bachelor/fiscale-economie) — Bachelor Fiscale Economie stopt; Voor huidige studenten; Teach-out through 2028–2029.

Result: confirmed; required action: none; exclusion should remain. No material factual question remains unresolved within this case’s audit scope.

### cp-000120 — Liberal Arts and Sciences (joint degree)

Institution: University of Amsterdam; VU Amsterdam. Audit scope: Joint award, degree identity, institutional partners and study load.

Exclusion trigger: `programme_type='joint-degree'`. The relevant rule is Master Specification §4.1 / Production Instructions §4.1.

AUC awards its 180-ECTS bachelor jointly through UvA and VU. Exclusion follows the joint-degree rule despite its ordinary three-year study load.

Provenance: source worksheet row(s) 128; normalization step2-resolved; decision cases rc-0012. Source-row and offering-ID sets exactly agree with the normalized target.

Current official sources (checked 7 October 2026):

- [Graduation requirements — Amsterdam University College](https://www.auc.nl/academic-programme/graduation-requirements/graduation-requirements.html) — Opening paragraph and Academic Standards & Procedures link; 2026–2027.
- [Liberal Arts and Sciences Bachelor's programme — Amsterdam University College](https://www.auc.nl/academic-programme/liberal-arts-and-sciences/liberal-arts--sciences.html) — Summary of the study programme; Current programme page; September 2027 applications.

Result: confirmed; required action: none; exclusion should remain. No material factual question remains unresolved within this case’s audit scope.

### cp-000147 — Urban Sustainability Studies (joint degree)

Institution: Maastricht University. Audit scope: Joint award, current UM programme identity and local start-year context.

Exclusion trigger: `programme_type='joint-degree'`. The relevant rule is Master Specification §4.1 / Production Instructions §4.1.

UM remains a degree-awarding YUFE partner in this active joint bachelor. Its joint-degree exclusion is justified; the Heerlen start year differs from the alliance launch.

Provenance: source worksheet row(s) 160; normalization step2-resolved; decision cases rc-0014. Source-row and offering-ID sets exactly agree with the normalized target.

Current official sources (checked 7 October 2026):

- [Urban Sustainability Studies — Maastricht University](https://www.maastrichtuniversity.nl/education/bachelor/programmes/urban-sustainability-studies) — Programme identity and The right programme for you; Current programme-facing page.
- [Green light for UM participation in unique YUFE bachelor programme](https://www.maastrichtuniversity.nl/news/green-light-um-participation-unique-yufe-bachelor-programme) — Degree-awarding partners; final paragraph on Heerlen teaching; Published 2025-07-04; UM start 2026–2027.
- [Open applications for YUFE's joint bachelor in Urban Sustainability Studies 2026/2027](https://www.maastrichtuniversity.nl/nl/nieuws/open-applications-yufe%E2%80%99s-joint-bachelor-urban-sustainability-studies-20262027) — Opening paragraphs and accreditation footnote; 2026–2027; published 2025-11-11.

The alliance launch in 2025 and UM teaching start in 2026–2027 are distinct; the registry local start-year attribute is supported. Evidence locator: Opening and final substantive paragraphs.

Result: confirmed; required action: none; exclusion should remain. No material factual question remains unresolved within this case’s audit scope.

### cp-000157 — Theology (joint degree)

Institution: Protestant Theological University; VU Amsterdam. Audit scope: Joint-degree identity and phase-out versus replacement programme.

Exclusion trigger: `programme_type='joint-degree'; production_eligible='false'; production_order=''`. The relevant rule is Master Specification §4.1 / Production Instructions §4.1.

PThU identifies its VU joint bachelor as in phase-out; VU confirms closure from September 2025. Both lifecycle and joint-degree grounds support exclusion.

Provenance: source worksheet row(s) 170; normalization step2-resolved; decision cases rc-0017, rc-0018, rc-0019. Source-row and offering-ID sets exactly agree with the normalized target.

Current official sources (checked 7 October 2026):

- [Examencommissies — Protestantse Theologische Universiteit](https://www.pthu.nl/onderwijs/praktische-informatie/examencommissies.whlink/) — Examencommissie PThU; Examencommissie bachelor Theologie (joint degree, PThU/VU); Current examination-board page.
- [Joint Degrees — Vrije Universiteit Amsterdam](https://vu.nl/nl/onderwijs/meer-over/joint-degree) — Samenwerking VU-PThU; Closure effective 2025-09-01.
- [Regelingen en rechtspositie — PThU](https://www.pthu.nl/over-pthu/organisatie/regelingen-en-rechtspositie/) — OERen studiejaar 2026–2027, 2025–2026 and 2024–2025; 2026–2027.

Result: confirmed; required action: none; exclusion should remain. No material factual question remains unresolved within this case’s audit scope.

### cp-000164 — Philosophy of a Specific Discipline — Cognitive Sciences track

Institution: University of Groningen. Audit scope: Exact Cognitive Sciences bachelor-track identity and combination structure.

Exclusion trigger: `programme_type='double-bachelor'`. The relevant rule is Master Specification §4.1 / Production Instructions §4.1.

Cognitive Sciences is a current track within the combination degree described in the shared Groningen evidence below. Its double-bachelor exclusion is justified.

Provenance: source worksheet row(s) 177; normalization step1-no-ambiguity; decision cases none; post-build correction recorded in corrected_attributes_json and registry README. Source-row and offering-ID sets exactly agree with the normalized target. Variant-of code 57084 agrees with the official philosophy degree CROHO code; the original source label is retained.

Current official sources (checked 7 October 2026):

- [Philosophy of a specific discipline — University of Groningen](https://www.rug.nl/bachelors/philosophy-of-a-specific-discipline/?lang=en) — Programme introduction, components, Facts & Figures and registration; Current page links 2026–2027 study guide.
- [Study Guide Faculty of Philosophy 2026–2027](https://www.rug.nl/filosofie/education/prospectus/study-guide-philosophy-studiegids-filosofie-2026-2027.pdf) — Section 7.4, printed pp. 50–53 (PDF pp. 50–53); 2026–2027.
- [Tracks Bachelor Philosophy of a Specific Discipline 2026–2027](https://www.rug.nl/filosofie/education/prospectus/tracks-bachelor-fvew-2026-2027-def.pdf) — PDF pp. 1–3; 2026–2027.

Cognitive Sciences track explicitly listed. Evidence locator: Section 7.4, printed p. 52: registration-track list.
Current bachelor-track course table corroborates the identity. Evidence locator: PDF p. 1, heading Cognitive Sciences.

Result: confirmed; required action: none; exclusion should remain. No material factual question remains unresolved within this case’s audit scope.

### cp-000169 — Philosophy of a Specific Discipline — Economic and Social Sciences track

Institution: University of Groningen. Audit scope: Exact Economic and Social Sciences bachelor-track identity and combination structure.

Exclusion trigger: `programme_type='double-bachelor'`. The relevant rule is Master Specification §4.1 / Production Instructions §4.1.

Economic and Social Sciences is a current track within that combination degree. The record correctly excludes it as double-bachelor.

Provenance: source worksheet row(s) 182; normalization step1-no-ambiguity; decision cases none; post-build correction recorded in corrected_attributes_json and registry README. Source-row and offering-ID sets exactly agree with the normalized target. Variant-of code 57084 agrees with the official philosophy degree CROHO code; the original source label is retained.

Current official sources (checked 7 October 2026):

- [Philosophy of a specific discipline — University of Groningen](https://www.rug.nl/bachelors/philosophy-of-a-specific-discipline/?lang=en) — Programme introduction, components, Facts & Figures and registration; Current page links 2026–2027 study guide.
- [Study Guide Faculty of Philosophy 2026–2027](https://www.rug.nl/filosofie/education/prospectus/study-guide-philosophy-studiegids-filosofie-2026-2027.pdf) — Section 7.4, printed pp. 50–53 (PDF pp. 50–53); 2026–2027.
- [Tracks Bachelor Philosophy of a Specific Discipline 2026–2027](https://www.rug.nl/filosofie/education/prospectus/tracks-bachelor-fvew-2026-2027-def.pdf) — PDF pp. 1–3; 2026–2027.

Economic and Social Sciences track explicitly listed. Evidence locator: Section 7.4, printed p. 52: registration-track list.
Current bachelor-track course table corroborates the identity. Evidence locator: PDF p. 2, heading Economic and Social Sciences.

Result: confirmed; required action: none; exclusion should remain. No material factual question remains unresolved within this case’s audit scope.

### cp-000177 — Philosophy of a Specific Discipline — History track

Institution: University of Groningen. Audit scope: Exact History bachelor-track identity and combination structure.

Exclusion trigger: `programme_type='double-bachelor'`. The relevant rule is Master Specification §4.1 / Production Instructions §4.1.

History is a current track within that combination degree. The record correctly excludes it as double-bachelor.

Provenance: source worksheet row(s) 190; normalization step1-no-ambiguity; decision cases none; post-build correction recorded in corrected_attributes_json and registry README. Source-row and offering-ID sets exactly agree with the normalized target. Variant-of code 57084 agrees with the official philosophy degree CROHO code; the original source label is retained.

Current official sources (checked 7 October 2026):

- [Philosophy of a specific discipline — University of Groningen](https://www.rug.nl/bachelors/philosophy-of-a-specific-discipline/?lang=en) — Programme introduction, components, Facts & Figures and registration; Current page links 2026–2027 study guide.
- [Study Guide Faculty of Philosophy 2026–2027](https://www.rug.nl/filosofie/education/prospectus/study-guide-philosophy-studiegids-filosofie-2026-2027.pdf) — Section 7.4, printed pp. 50–53 (PDF pp. 50–53); 2026–2027.
- [Tracks Bachelor Philosophy of a Specific Discipline 2026–2027](https://www.rug.nl/filosofie/education/prospectus/tracks-bachelor-fvew-2026-2027-def.pdf) — PDF pp. 1–3; 2026–2027.

History track explicitly listed. Evidence locator: Section 7.4, printed p. 52: registration-track list.
Current bachelor-track course table corroborates the identity. Evidence locator: PDF p. 3, heading History.

Result: confirmed; required action: none; exclusion should remain. No material factual question remains unresolved within this case’s audit scope.

### cp-000186 — Philosophy of a Specific Discipline — Art and Cultural Studies track

Institution: University of Groningen. Audit scope: Exact Art and Cultural Studies bachelor-track identity and combination structure.

Exclusion trigger: `programme_type='double-bachelor'`. The relevant rule is Master Specification §4.1 / Production Instructions §4.1.

Art and Cultural Studies is a current registration track within that combination degree. Its double-bachelor exclusion is justified.

Provenance: source worksheet row(s) 199; normalization step1-no-ambiguity; decision cases none; post-build correction recorded in corrected_attributes_json and registry README. Source-row and offering-ID sets exactly agree with the normalized target. Variant-of code 57084 agrees with the official philosophy degree CROHO code; the original source label is retained.

Current official sources (checked 7 October 2026):

- [Philosophy of a specific discipline — University of Groningen](https://www.rug.nl/bachelors/philosophy-of-a-specific-discipline/?lang=en) — Programme introduction, components, Facts & Figures and registration; Current page links 2026–2027 study guide.
- [Study Guide Faculty of Philosophy 2026–2027](https://www.rug.nl/filosofie/education/prospectus/study-guide-philosophy-studiegids-filosofie-2026-2027.pdf) — Section 7.4, printed pp. 50–53 (PDF pp. 50–53); 2026–2027.
- [Tracks Bachelor Philosophy of a Specific Discipline 2026–2027](https://www.rug.nl/filosofie/education/prospectus/tracks-bachelor-fvew-2026-2027-def.pdf) — PDF pp. 1–3; 2026–2027.

Art and Cultural Studies track explicitly listed. Evidence locator: Section 7.4, printed p. 52: registration-track list.
Current bachelor-track course table corroborates the identity. Evidence locator: PDF p. 3, heading Arts and Culture.
Registration label Art and Cultural Studies; curricular table uses Arts and Culture. This wording difference does not identify a different bachelor. Evidence locator: Section 7.4, printed pp. 52 and 56–57.

Result: confirmed; required action: none; exclusion should remain. No material factual question remains unresolved within this case’s audit scope.

## Shared current-source facts

The following source facts supplement the per-case findings and are preserved once in the JSON source dictionary to avoid duplicating shared evidence.

- **eur_bsc2:** Four-year, 264-EC double degree. [Facts & Figures — Double bachelor BSc² in Econometrics and Economics](https://www.eur.nl/en/bachelor/double-bachelor-bsc2-econometrics-and-economics/facts-figures).
- **eur_rasl:** Philosophy and a WdKA bachelor are combined over five years. [Dual Degree with Arts and Philosophy](https://www.eur.nl/en/esphil/education/dual-degree-arts-and-philosophy).
- **eur_rasl_facts:** RASL umbrella: five years, 300 EC and a double degree. [Facts & Figures — Dual Degree in Arts and Sciences](https://www.eur.nl/en/bachelor/dual-degree-arts-and-sciences/facts-figures).
- **eur_rasl_admission:** Philosophy and WdKA remain participating admission routes. [Application — Dual Degree in Arts and Sciences](https://www.eur.nl/en/bachelor/dual-degree-arts-and-sciences/application).
- **eur_tax:** New applications have ended; current students may finish through 2028–2029. [Bachelor Fiscale Economie](https://www.eur.nl/bachelor/fiscale-economie).
- **auc_degree:** Degree awarded jointly by UvA and VU; links current 2026–2027 standards. [Graduation requirements — Amsterdam University College](https://www.auc.nl/academic-programme/graduation-requirements/graduation-requirements.html).
- **auc_facts:** Three years, 180 ECTS, joint BA/BSc; CROHO 55002. [Liberal Arts and Sciences Bachelor's programme — Amsterdam University College](https://www.auc.nl/academic-programme/liberal-arts-and-sciences/liberal-arts--sciences.html).
- **um_current:** Current programme offers a joint BSc and is based in Heerlen. [Urban Sustainability Studies — Maastricht University](https://www.maastrichtuniversity.nl/education/bachelor/programmes/urban-sustainability-studies).
- **um_award:** Seven universities award the degree; UM teaching in Heerlen starts in 2026–2027, distinct from the alliance launch in 2025. [Green light for UM participation in unique YUFE bachelor programme](https://www.maastrichtuniversity.nl/news/green-light-um-participation-unique-yufe-bachelor-programme).
- **um_admissions:** Joint three-year bachelor accepting applications for 2026–2027. [Open applications for YUFE's joint bachelor in Urban Sustainability Studies 2026/2027](https://www.maastrichtuniversity.nl/nl/nieuws/open-applications-yufe%E2%80%99s-joint-bachelor-urban-sustainability-studies-20262027).
- **pthu_phaseout:** PThU explicitly describes the Amsterdam PThU/VU joint bachelor as being phased out. [Examencommissies — Protestantse Theologische Universiteit](https://www.pthu.nl/onderwijs/praktische-informatie/examencommissies.whlink/).
- **vu_phaseout:** VU states that the Theology joint degree stops from 1 September 2025. [Joint Degrees — Vrije Universiteit Amsterdam](https://vu.nl/nl/onderwijs/meer-over/joint-degree).
- **pthu_regulations:** Current Utrecht bachelor regulations are distinguished from archived PThU/VU joint-degree regulations. [Regelingen en rechtspositie — PThU](https://www.pthu.nl/over-pthu/organisatie/regelingen-en-rechtspositie/).
- **rug_degree:** Combination bachelor awards two degrees; its 180-EC philosophy award incorporates 120 EC from the first bachelor and 60 EC philosophy. This is not a claim that the combined two-degree study load totals 180 EC. [Philosophy of a specific discipline — University of Groningen](https://www.rug.nl/bachelors/philosophy-of-a-specific-discipline/?lang=en).
- **rug_guide:** Lists the named bachelor tracks and the 120-plus-60-EC structure. [Study Guide Faculty of Philosophy 2026–2027](https://www.rug.nl/filosofie/education/prospectus/study-guide-philosophy-studiegids-filosofie-2026-2027.pdf).
- **rug_tracks:** Current track tables list Cognitive Sciences, Economic and Social Sciences, History, and Arts and Culture. [Tracks Bachelor Philosophy of a Specific Discipline 2026–2027](https://www.rug.nl/filosofie/education/prospectus/tracks-bachelor-fvew-2026-2027-def.pdf).

## Cumulative findings after batch 2

| Finding | Count |
|---|---:|
| confirmed | 20 |
| incorrect | 0 |
| outdated | 0 |
| still-unresolved | 0 |

| Required action | Count |
|---|---:|
| none | 19 |
| reprocess-as-comparison | 0 |
| reassess-exception | 1 |
| correct-registry-and-reprocess | 0 |
| research-again-later | 0 |

All 19 exclusions are confirmed and require no action. CP040 is confirmed only for its defining external curriculum; reassess-exception records a source-context and elective-description follow-up. Its UCR feasibility remains unassessed. A confirmed scoped finding can therefore still require a limited follow-up.

## Batch 2 findings and evidence

| ID | Programme | Finding | Action |
|---|---|---|---|
| cp-000190 | Philosophy of a Specific Discipline — Life Sciences track | confirmed | none |
| cp-000195 | Minorities & Multilingualism | confirmed | none |
| cp-000197 | Philosophy of a Specific Discipline — Natural Sciences track | confirmed | none |
| cp-000202 | Philosophy of a Specific Discipline — Political Science track | confirmed | none |
| cp-000234 | Data Science (joint degree Tilburg University + TU/e) | confirmed | none |
| cp-000307 | Molecular Science and Technology (joint degree) | confirmed | none |
| cp-000417 | Physics and Astronomy (joint degree) | confirmed | none |
| cp-000430 | Chemistry (joint degree) | confirmed | none |
| cp-000460 | Tourism (joint degree) | confirmed | none |
| cp-000040 | German Language and Culture | confirmed | reassess-exception |

### cp-000190 — Philosophy of a Specific Discipline — Life Sciences track

Institution(s): University of Groningen. Audit scope: Exact Life Sciences track identity and combination-degree structure.

Exclusion trigger: `programme_type='double-bachelor'`; Master Specification §4.1 / Production Instructions §4.1.

The current Groningen guide lists Life Sciences as a Philosophy of a Specific Discipline registration track, and the current track table corroborates it. The shared combination bachelor awards two degrees; double-bachelor exclusion is supported.

Provenance: source worksheet row(s) 203. Source-row and offering-ID sets exactly agree with the normalized target. Variant-of code 57084 agrees with the official philosophy degree code.

Normalization: step1-no-ambiguity; decision cases none; post-build correction retained in registry attributes and README.

Official sources checked 7 October 2026:

- [Philosophy of a specific discipline — University of Groningen](https://www.rug.nl/bachelors/philosophy-of-a-specific-discipline/?lang=en) — Programme introduction, components, Facts & Figures and registration; Current page links 2026–2027 study guide. Combination bachelor awards two degrees; its 180-EC philosophy award incorporates 120 EC from the first bachelor and 60 EC philosophy. This is not a claim that the combined two-degree study load totals 180 EC.
- [Study Guide Faculty of Philosophy 2026–2027](https://www.rug.nl/filosofie/education/prospectus/study-guide-philosophy-studiegids-filosofie-2026-2027.pdf) — Section 7.4, printed pp. 50–53 (PDF pp. 50–53); 2026–2027. Lists the named bachelor tracks and the 120-plus-60-EC structure.
- [Tracks Bachelor Philosophy of a Specific Discipline 2026–2027](https://www.rug.nl/filosofie/education/prospectus/tracks-bachelor-fvew-2026-2027-def.pdf) — PDF pp. 1–3; 2026–2027. Current track tables list Cognitive Sciences, Economic and Social Sciences, History, and Arts and Culture.

Life Sciences is explicitly listed as a registration track. Evidence locator: Section 7.4, printed p. 52.

The current course table corroborates this exact track identity. Evidence locator: PDF p. 1, heading Life Sciences.

Result: confirmed; required action: none; exclusion should remain. No material factual question remains unresolved within the exclusion scope.

### cp-000195 — Minorities & Multilingualism

Institution(s): University of Groningen. Audit scope: Lifecycle, new intake and continuing-student provision.

Exclusion trigger: `production_eligible='false'; production_order=''`; Master Specification §4.1 / Production Instructions §4.1.

The official discontinuation announcement, still published and modified in January 2026, confirms phase-out from 2025–2026 and completion rights for existing students. The 2026–2027 regulations do not reverse that closure. Teach-out-only status, false eligibility and blank production order are supported.

Provenance: source worksheet row(s) 208. Source-row and offering-ID sets exactly agree with the normalized target.

Normalization: step2-resolved; decision cases rc-0025.

Official sources checked 7 October 2026:

- [Bachelor Minorities & Multilingualism Discontinued](https://www.rug.nl/let/onze-faculteit/actueel/nieuwsberichten-2024/bachelor-minorities-multilingualism-discontinued?lang=en) — Opening and Last Cohort sections; last modified 6 January 2026; Published 2 February 2024; current page modified 2026. Phase-out starts in 2025–2026; existing students may obtain their diplomas.
- [Minorities & Multilingualism | Fries — Teaching and Examination Regulations, Part B 2026–2027](https://www.rug.nl/let/onze-faculteit/organisatie/diensten-en-voorzieningen/onderwijsinstituut/oeren/2026-2027/bacheloropleidingen/delen-b/ba-mm-partb-2627.pdf) — Cover and Article 1.1; 2026–2027. Current regulations still cover the programme. Their existence is consistent with continuing students and does not itself establish reopened new intake.

Continuing 2026–2027 regulations are not evidence of new admission; no reopening was found. The closure announcement remains the direct lifecycle evidence. Evidence locator: Cover and Article 1.1.

Result: confirmed; required action: none; exclusion should remain. No material factual question remains unresolved within the exclusion scope.

### cp-000197 — Philosophy of a Specific Discipline — Natural Sciences track

Institution(s): University of Groningen. Audit scope: Exact Natural Sciences track identity and combination-degree structure.

Exclusion trigger: `programme_type='double-bachelor'`; Master Specification §4.1 / Production Instructions §4.1.

Natural Sciences remains a named registration track in the current guide and track tables. It belongs to the combination bachelor, supporting its double-bachelor exclusion.

Provenance: source worksheet row(s) 210. Source-row and offering-ID sets exactly agree with the normalized target. Variant-of code 57084 agrees with the official philosophy degree code.

Normalization: step1-no-ambiguity; decision cases none; post-build correction retained in registry attributes and README.

Official sources checked 7 October 2026:

- [Philosophy of a specific discipline — University of Groningen](https://www.rug.nl/bachelors/philosophy-of-a-specific-discipline/?lang=en) — Programme introduction, components, Facts & Figures and registration; Current page links 2026–2027 study guide. Combination bachelor awards two degrees; its 180-EC philosophy award incorporates 120 EC from the first bachelor and 60 EC philosophy. This is not a claim that the combined two-degree study load totals 180 EC.
- [Study Guide Faculty of Philosophy 2026–2027](https://www.rug.nl/filosofie/education/prospectus/study-guide-philosophy-studiegids-filosofie-2026-2027.pdf) — Section 7.4, printed pp. 50–53 (PDF pp. 50–53); 2026–2027. Lists the named bachelor tracks and the 120-plus-60-EC structure.
- [Tracks Bachelor Philosophy of a Specific Discipline 2026–2027](https://www.rug.nl/filosofie/education/prospectus/tracks-bachelor-fvew-2026-2027-def.pdf) — PDF pp. 1–3; 2026–2027. Current track tables list Cognitive Sciences, Economic and Social Sciences, History, and Arts and Culture.

Natural Sciences is explicitly listed as a registration track. Evidence locator: Section 7.4, printed p. 52.

The current course table corroborates this exact track identity. Evidence locator: PDF p. 1, heading Natural Sciences.

Result: confirmed; required action: none; exclusion should remain. No material factual question remains unresolved within the exclusion scope.

### cp-000202 — Philosophy of a Specific Discipline — Political Science track

Institution(s): University of Groningen. Audit scope: Exact Political Science track identity and combination-degree structure.

Exclusion trigger: `programme_type='double-bachelor'`; Master Specification §4.1 / Production Instructions §4.1.

Political Science remains a named registration track in the current guide and track tables. Its double-bachelor classification and exclusion are supported.

Provenance: source worksheet row(s) 215. Source-row and offering-ID sets exactly agree with the normalized target. Variant-of code 57084 agrees with the official philosophy degree code.

Normalization: step1-no-ambiguity; decision cases none; post-build correction retained in registry attributes and README.

Official sources checked 7 October 2026:

- [Philosophy of a specific discipline — University of Groningen](https://www.rug.nl/bachelors/philosophy-of-a-specific-discipline/?lang=en) — Programme introduction, components, Facts & Figures and registration; Current page links 2026–2027 study guide. Combination bachelor awards two degrees; its 180-EC philosophy award incorporates 120 EC from the first bachelor and 60 EC philosophy. This is not a claim that the combined two-degree study load totals 180 EC.
- [Study Guide Faculty of Philosophy 2026–2027](https://www.rug.nl/filosofie/education/prospectus/study-guide-philosophy-studiegids-filosofie-2026-2027.pdf) — Section 7.4, printed pp. 50–53 (PDF pp. 50–53); 2026–2027. Lists the named bachelor tracks and the 120-plus-60-EC structure.
- [Tracks Bachelor Philosophy of a Specific Discipline 2026–2027](https://www.rug.nl/filosofie/education/prospectus/tracks-bachelor-fvew-2026-2027-def.pdf) — PDF pp. 1–3; 2026–2027. Current track tables list Cognitive Sciences, Economic and Social Sciences, History, and Arts and Culture.

Political Science is explicitly listed as a registration track. Evidence locator: Section 7.4, printed p. 52.

The current course table corroborates this exact track identity. Evidence locator: PDF p. 2, heading Political Science.

Result: confirmed; required action: none; exclusion should remain. No material factual question remains unresolved within the exclusion scope.

### cp-000234 — Data Science (joint degree Tilburg University + TU/e)

Institution(s): Tilburg University; Eindhoven University of Technology. Audit scope: Joint award, cross-provider identity and corrected study load.

Exclusion trigger: `programme_type='joint-degree'`; Master Specification §4.1 / Production Instructions §4.1.

The current examination-board page explicitly identifies one joint bachelor of Tilburg and TU/e. The current programme and 2026–2027 curriculum support the merged provider identity, three-year English structure and 180-EC load. Joint-degree exclusion is confirmed.

Provenance: source worksheet row(s) 247, 278. Source-row and offering-ID sets exactly agree with the normalized target.

Normalization: step2-resolved; decision cases rc-0031, rc-0032, rc-0035.

Official sources checked 7 October 2026:

- [Data Science BSc — Tilburg University](https://www.tilburguniversity.edu/education/bachelors-programs/data-science) — Opening, accreditation, programme content and tuition-fee sections; Current programme page with October 2026 and January 2027 events. Three-year English programme offered by Tilburg and TU/e; classes at both universities and application through TU/e.
- [Examencommissie Data Science — Tilburg University](https://www.tilburguniversity.edu/nl/studenten/studie/tentamens/examencommissie/data-science) — Opening and examination-board remit; Current undated examination-board page. Explicitly identifies the bachelor as a joint degree offered by Tilburg University and TU/e.
- [Program and courses Data Science BSc](https://www.tilburguniversity.edu/education/bachelors-programs/data-science/program-and-courses) — Curriculum BSc Data Science start September 2026–2027, years 1–3; 2026–2027 starting curriculum; subject to annual changes. Published three-year tables sum to 60 + 60 + 60 = 180 ECTS, including 45 elective credits.

Result: confirmed; required action: none; exclusion should remain. No material factual question remains unresolved within the exclusion scope.

### cp-000307 — Molecular Science and Technology (joint degree)

Institution(s): Leiden University; Delft University of Technology. Audit scope: Joint-degree identity and institutional partners.

Exclusion trigger: `programme_type='joint-degree'`; Master Specification §4.1 / Production Instructions §4.1.

The current Leiden programme page and TU Delft joint-degree timetable portal corroborate one shared bachelor. Article 1.1 of the 2025–2026 OER explicitly identifies its joint award. The exclusion remains supported without treating the dated OER as current-year regulations.

Provenance: source worksheet row(s) 321. Source-row and offering-ID sets exactly agree with the normalized target.

Normalization: step2-resolved; decision cases rc-0041.

Official sources checked 7 October 2026:

- [Molecular Science & Technology — Universiteit Leiden](https://www.universiteitleiden.nl/onderwijs/opleidingen/bachelor/molecular-science--technology) — Programme introduction and facts; Current undated programme page. Current three-year bachelor is offered with TU Delft in Leiden and Delft.
- [TNW Joint Degree Rooster — TU Delft / Universiteit Leiden](https://jointdegree.tnw.tudelft.nl/) — Opening and programme-selection list; Current undated operational portal; footer identifies 2023 design. Current joint-degree timetable portal explicitly lists Molecular Science and Technology.
- [Onderwijs- en examenregeling bacheloropleiding MST 2025–2026](https://www.organisatiegids.universiteitleiden.nl/binaries/content/assets/science/reglementen/onderwijs/2025-2026/onderwijs--en-examenregeling-mst-25-26.pdf) — Article 1.1, printed p. 3; programme description; Version 20 March 2025, effective 1 September 2025. Formal regulation identifies a single joint-degree bachelor of Leiden and TU Delft. Used as dated corroboration alongside current programme and timetable pages, not represented as a 2026–2027 OER.

A 2026–2027 OER was not located in this research. Current joint-degree identity is independently corroborated by the live programme and operational timetable pages; full current-year curriculum validation is outside this exclusion audit. Evidence locator: Article 1.1, printed p. 3.

Result: confirmed; required action: none; exclusion should remain. No material factual question remains unresolved within the exclusion scope.

### cp-000417 — Physics and Astronomy (joint degree)

Institution(s): University of Amsterdam; VU Amsterdam. Audit scope: Joint award and merged ordinary/free-programme source identity.

Exclusion trigger: `programme_type='joint-degree'`; Master Specification §4.1 / Production Instructions §4.1.

UvA currently identifies one 180-EC UvA/VU joint bachelor with RIO code 55013. Both normalized source rows belong to that identity; the administrative free-programme representation supplies no evidence of an additional student-facing bachelor. Joint-degree exclusion and a single target are supported.

Provenance: source worksheet row(s) 432, 433. Source-row and offering-ID sets exactly agree with the normalized target.

Normalization: step2-resolved; decision cases rc-0055, rc-0056, rc-0070.

Official sources checked 7 October 2026:

- [Bachelor Natuur- en Sterrenkunde — Universiteit van Amsterdam](https://www.uva.nl/programmas/bachelors/natuur--en-sterrenkunde/natuur--en-sterrenkunde.html) — Programme facts and diploma; Current programme page. One UvA/VU joint degree, 180 EC, 36 months and RIO code 55013.
- [Studieprogramma Natuur- en Sterrenkunde — UvA](https://www.uva.nl/programmas/bachelors/natuur--en-sterrenkunde/studieprogramma/studieprogramma.html) — Opening and programme structure; Current programme page. One bachelor taught across UvA and VU locations; no separate student-facing free-programme degree is identified.

Result: confirmed; required action: none; exclusion should remain. No material factual question remains unresolved within the exclusion scope.

### cp-000430 — Chemistry (joint degree)

Institution(s): University of Amsterdam; VU Amsterdam. Audit scope: Joint award and merged ordinary/free-programme source identity.

Exclusion trigger: `programme_type='joint-degree'`; Master Specification §4.1 / Production Instructions §4.1.

UvA currently identifies one 180-EC UvA/VU Chemistry joint bachelor with RIO code 55012, including coordinated registration at both universities. The normalized ordinary and administrative free-programme rows support one target; joint-degree exclusion remains correct.

Provenance: source worksheet row(s) 447, 448. Source-row and offering-ID sets exactly agree with the normalized target.

Normalization: step2-resolved; decision cases rc-0060, rc-0061, rc-0069.

Official sources checked 7 October 2026:

- [Bachelor Scheikunde — Universiteit van Amsterdam](https://www.uva.nl/programmas/bachelors/scheikunde/scheikunde.html) — Programme facts and diploma; Current programme page. One UvA/VU joint degree, 180 EC, 36 months and RIO code 55012.
- [Studieprogramma Scheikunde — UvA](https://www.uva.nl/programmas/bachelors/scheikunde/studieprogramma/studieprogramma.html) — Opening and registration; Current programme page. One programme at both universities; UvA registration includes VU registration.

Result: confirmed; required action: none; exclusion should remain. No material factual question remains unresolved within the exclusion scope.

### cp-000460 — Tourism (joint degree)

Institution(s): Wageningen University & Research; Breda University of Applied Sciences. Audit scope: Joint award, active intake and corrected language/duration.

Exclusion trigger: `programme_type='joint-degree'`; Master Specification §4.1 / Production Instructions §4.1.

WUR and BUas both confirm the current three-year English joint academic Tourism bachelor. BUas advertises 2027 entry through WUR. The normalized joint type, active lifecycle, English language and three-year duration remain supported.

Provenance: source worksheet row(s) 479. Source-row and offering-ID sets exactly agree with the normalized target.

Normalization: step2-resolved; decision cases rc-0064.

Official sources checked 7 October 2026:

- [Bachelor Tourism (joint degree) — WUR](https://www.wur.nl/en/education/bachelor/bachelors-tourism-joint-degree) — Programme overview and facts; Current programme page. Current three-year English joint academic degree of WUR and Breda University of Applied Sciences.
- [Bachelor of Science Tourism — BUas](https://www.buas.nl/opleidingen/bachelor-of-science-bsc-tourism) — Joint degree, facts and admissions; 2027–2028 intake information. BUas independently confirms the WUR joint degree, three years, full time and English; advertises a 30 August 2027 start and WUR application.

Result: confirmed; required action: none; exclusion should remain. No material factual question remains unresolved within the exclusion scope.

### cp-000040 — German Language and Culture

Institution(s): Radboud University. Audit scope: External-programme identity, compulsory German-studies core, immersion and published source context only; no independent UCR feasibility judgment.

Formal exception: `no-defensible-ucr-match`; existing check date: 2026-09-25.

Existing substantive reason: German-language proficiency, German linguistics and literature, German-speaking-country immersion and Dutch–German cultural exchange form the core of this bachelor. UCR currently offers no German-language course or specialist German-studies sequence. Related courses in general literature, history, communication and European politics cannot form a credible 24-course closest-match programme without treating them as substitutes for missing German-language study.

Current official pages support the defining German-language, linguistics, literature/culture, Dutch–German exchange and compulsory immersion basis. Confirmation applies to that external core only. The stored first/second-year labels (2026–2027) differ from the currently published indicative 2027–2028/2028–2029 pages. The current year-two page describes 30 EC free space with broader options, whereas component y2-minors restricts it to two Humanities minors. These source-context details need reassessment even though the external core is confirmed.

Provenance: source worksheet row(s) 43. Canonical provider source-row and offering-ID sets agree with the normalized standard target.

Official sources checked 7 October 2026:

- [Studieprogramma Duitse Taal en Cultuur — Radboud Universiteit](https://www.ru.nl/opleidingen/bachelors/duitse-taal-en-cultuur/studieprogramma) — Study-year descriptions and core subject axes; Current indicative prospectus. German proficiency, linguistics, literature/culture and Dutch–German exchange define the major; a German-speaking-country stay belongs to the required major.
- [Studieprogramma Duitse Taal en Cultuur jaar 1](https://www.ru.nl/opleidingen/bachelors/duitse-taal-en-cultuur/studieprogramma-duitse-taal-en-cultuur-jaar-1) — Indicative year label and required-course table; Indicative 2027–2028, not a guaranteed Fall 2026 cohort curriculum. Twelve compulsory 5-EC courses (60 EC), including German-context language study, literature, linguistics and Euregion work; zero-credit support is additional.
- [Studieprogramma Duitse Taal en Cultuur jaar 2](https://www.ru.nl/opleidingen/bachelors/duitse-taal-en-cultuur/studieprogramma-duitse-taal-en-cultuur-jaar-2) — Required courses, Studeren in het buitenland and Vrije ruimte; Indicative 2028–2029. Three compulsory 5-EC courses plus a required 15-EC German-speaking-country stay; 30 EC free space allows other programmes, extra study abroad or an internship.
- [Studieprogramma Duitse Taal en Cultuur jaar 3](https://www.ru.nl/opleidingen/bachelors/duitse-taal-en-cultuur/studieprogramma-duitse-taal-en-cultuur-jaar-3) — Required-course and minor tables; Indicative 2029–2030. Four compulsory 5-EC courses, 10-EC thesis/tutorial and 30-EC minor space. The page describes two 15-EC Humanities minors or the optional educational minor.

60 EC compulsory year-one curriculum contains the specific German-studies core. Evidence locator: Required-course table.

15 EC courses plus 15 EC compulsory German-speaking-country stay; free space is 30 EC. Evidence locator: Required-course table and foreign-study paragraph.

30 EC compulsory courses/thesis and 30 EC minors; educational minor is optional. Evidence locator: Required-course and minor tables.

Result: confirmed for the external core only; required action: reassess-exception.

| Stored field | Current official evidence |
|---|---|
| First- and second-year source labels: 2026–2027 | First year: indicative 2027–2028; second year: indicative 2028–2029. Third year remains indicative 2029–2030. |
| y2-minors: two restricted 15-EC Humanities minors | Year-two page: 30 EC free space, allowing other programmes, extra study abroad or an internship. |

Recommended follow-up: In a later authorized production task, determine the applicable academic/cohort year from the official education catalogue or programme regulations; refresh comparator.academicYear, sourceNotes, changed course labels and y2-minors. Describe 30 EC as free space if the applicable curriculum supports that. Retain the supported German core, preserve the indicative future-year caveat, and assess UCR feasibility independently in stage two. This audit does not edit the canonical exception.

Unresolved factual question: The currently published pages address a prospective 2027-entry sequence. Which formal curriculum and second-year elective restrictions apply to the intended Fall 2026 cohort? Historical page evidence was not established, so the observed source-context discrepancies do not distinguish an original error from a later change.

UCR-side reassessment pending: **yes**. The existing UCR claim is reproduced as provenance only. Neither its course evidence nor the no-defensible-match conclusion was independently validated in this stage.

## Cumulative findings after batch 3

| Finding | Count |
|---|---:|
| confirmed | 29 |
| incorrect | 0 |
| outdated | 0 |
| still-unresolved | 1 |

| Required action | Count |
|---|---:|
| none | 26 |
| reprocess-as-comparison | 0 |
| reassess-exception | 3 |
| correct-registry-and-reprocess | 0 |
| research-again-later | 1 |

## Batch 3 findings

Nine no-defensible-ucr-match cases have a confirmed defining external curriculum. CP051 remains externally unresolved. CP050 and CP061 require limited source-context follow-ups; CP051 needs renewed research when its third year is specified. These classifications do not validate any UCR no-match claim.

| ID | Programme | Formal type | Finding | Required action |
|---|---|---|---|---|
| cp-000043 | English Language and Culture | no-defensible-ucr-match | confirmed | none |
| cp-000046 | French Language and Culture | no-defensible-ucr-match | confirmed | none |
| cp-000050 | Classics (Greek and Latin Language and Culture) | no-defensible-ucr-match | confirmed | reassess-exception |
| cp-000051 | Human Neuroscience | external-programme-unresolved | still-unresolved | research-again-later |
| cp-000055 | Islam, Politics and Society | no-defensible-ucr-match | confirmed | none |
| cp-000057 | Molecular Life Sciences | no-defensible-ucr-match | confirmed | none |
| cp-000058 | Natural Sciences | no-defensible-ucr-match | confirmed | none |
| cp-000059 | Physics and Astronomy | no-defensible-ucr-match | confirmed | none |
| cp-000060 | Dutch Language and Culture | no-defensible-ucr-match | confirmed | none |
| cp-000061 | Notarial Law | no-defensible-ucr-match | confirmed | reassess-exception |

## Batch 3 evidence

### cp-000043 — English Language and Culture

Institution: Radboud University. Audit scope: External-programme identity, defining compulsory curriculum, choice structure and source context only; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-09-25.

Existing substantive reason: The programme integrates sustained English proficiency, English phonetics, syntax, historical and world English linguistics, British and American literary history, specialist research and a required thesis. UCR has literature, stylistics, rhetoric and media courses taught in English, but lacks dedicated English-language proficiency and phonology/syntax teaching and the multi-period English literature and linguistics sequence. Filling a 24-course closest match with general literature, history, art and media courses would misrepresent those gaps as English Studies training.

Current official pages corroborate the sustained English proficiency, phonetics/syntax, language history, British/American literature and specialist thesis basis. The reconstructed domestic route retains 60 EC of total minor/free space; this does not remove the compulsory English-studies core.

Provenance: data/counselor/comparisons/cp-000043.json; source worksheet row(s) 46. Canonical provider, normalized registry, source-row and offering-ID sets agree; current standard target is in scope.

Current official sources (checked 7 October 2026):

- [Study programme English Language and Culture jaar 1](https://www.ru.nl/en/education/bachelors/english-language-and-culture/study-programme-of-english-language-and-culture/study-programme-english-language-and-culture-year-1) — Indicative year label; compulsory-course and minor/free-space tables; Indicative 2027–2028. Twelve compulsory 5-EC courses include English writing/oral skills, phonetics, syntax, language history and British/American literature.
- [Study programme English Language and Culture jaar 2](https://www.ru.nl/en/education/bachelors/english-language-and-culture/study-programme-of-english-language-and-culture/study-programme-english-language-and-culture-year-2) — Indicative year label; compulsory-course and minor/free-space tables; Indicative 2028–2029. Six compulsory 5-EC courses in literature and linguistics plus two restricted 15-EC Faculty of Arts minors. Supplementary English minors are optional.
- [Study programme English Language and Culture jaar 3](https://www.ru.nl/en/education/bachelors/english-language-and-culture/study-programme-of-english-language-and-culture/study-programme-english-language-and-culture-year-3) — Indicative year label; compulsory-course and minor/free-space tables; Indicative 2029–2030. Domestic route: four 5-EC courses, a 10-EC literature/linguistics thesis and 30 EC free electives. The abroad route is an alternative.
- [Study programme of English Language and Culture](https://www.ru.nl/en/education/bachelors/english-language-and-culture/study-programme) — Track choice and language-acquisition description; Current undated overview. English Language and Culture and American Studies are separate tracks. The audited track integrates professional spoken/written English, language structure/history and literature.

External credit structure: Stored components total 180 EC; current sources support the required/choice structure described in this scoped audit.

Result: confirmed; required action: none.

No material factual question remains unresolved within the defining external-basis scope. Indicative future pages are not a guarantee of the entering cohort’s eventual timetable.

UCR-side reassessment pending: **yes**. Existing UCR claims are preserved as provenance only. Stage-two UCR feasibility assessment remains pending.

### cp-000046 — French Language and Culture

Institution: Radboud University. Audit scope: External-programme identity, defining compulsory curriculum, choice structure and source context only; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-09-25.

Existing substantive reason: French Language and Culture combines a four-course French proficiency progression through C1 with study of French-language structure, French–Dutch translation and creative writing, francophone literature and culture, a required period studying at a francophone university and a discipline-specific thesis. UCR has a substantial humanities, media, history and communication offer, but no French language course, francophone literary sequence, French linguistics or translation training. A 24-course selection of general culture and communication courses would be a valid different humanities curriculum but not a defensible closest response to this explicitly French-language programme; it would obscure the central language and region-specific requirements.

The official first-year table supports the four French proficiency units ending at C1. Later pages corroborate French linguistics/translation/culture, a required 15-EC francophone stay and thesis. Restricted year-two minors and open year-three space are correctly distinguished; the currently displayed indicative year labels agree with the record.

Provenance: data/counselor/comparisons/cp-000046.json; source worksheet row(s) 49. Canonical provider, normalized registry, source-row and offering-ID sets agree; current standard target is in scope.

Current official sources (checked 7 October 2026):

- [Studieprogramma Franse Taal en Cultuur jaar 1](https://www.ru.nl/opleidingen/bachelors/franse-taal-en-cultuur/studieprogramma-franse-taal-en-cultuur-jaar-1) — Indicative year label; compulsory-course and minor/free-space tables; Indicative 2027–2028. Twelve compulsory 5-EC courses include four French proficiency units progressing from B1/B2 to C1.
- [Studieprogramma Franse Taal en Cultuur jaar 2](https://www.ru.nl/opleidingen/bachelors/franse-taal-en-cultuur/studieprogramma-franse-taal-en-cultuur-jaar-2) — Indicative year label; compulsory-course and minor/free-space tables; Indicative 2028–2029. Six required 5-EC courses include French–Dutch translation, French-language study and culture; two 15-EC Faculty of Arts minors remain choices.
- [Studieprogramma Franse Taal en Cultuur jaar 3](https://www.ru.nl/opleidingen/bachelors/franse-taal-en-cultuur/studieprogramma-franse-taal-en-cultuur-jaar-3) — Indicative year label; compulsory-course and minor/free-space tables; Indicative 2028–2029. Required francophone-university study contributes 15 EC to the major, alongside a 5-EC professional unit, 30 EC free space and a 10-EC thesis.
- [Studieprogramma Franse Taal en Cultuur](https://www.ru.nl/opleidingen/bachelors/franse-taal-en-cultuur/studieprogramma-franse-taal-en-cultuur) — Year descriptions and studying abroad; Current undated overview. The French-specific language, culture and literature programme includes study at a francophone university.

External credit structure: Stored components total 180 EC; current sources support the required/choice structure described in this scoped audit.

Result: confirmed; required action: none.

No material factual question remains unresolved within the defining external-basis scope. Indicative future pages are not a guarantee of the entering cohort’s eventual timetable.

UCR-side reassessment pending: **yes**. Existing UCR claims are preserved as provenance only. Stage-two UCR feasibility assessment remains pending.

### cp-000050 — Classics (Greek and Latin Language and Culture)

Institution: Radboud University. Audit scope: External-programme identity, defining compulsory curriculum, choice structure and source context only; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-09-25.

Existing substantive reason: The Greek and Latin grammar, translation, linguistics and original-text literature sequence is integral to Classics across all three years. UCR offers Greek archaeology, ancient democracy and world mythology, but no ancient Greek or Latin language teaching or sustained primary-text sequence. A 24-course UCR programme built around adjacent cultural-history courses would conceal this defining gap rather than constitute a defensible closest match.

Greek/Latin grammar, translation, original-text literature and specialist research remain a defining compulsory core. The domestic structure still supports 180 EC. The stored year-three label 2028–2029 differs from the currently displayed indicative 2029–2030 label; this source-context detail needs refresh without changing the confirmed field basis.

Provenance: data/counselor/comparisons/cp-000050.json; source worksheet row(s) 53. Canonical provider, normalized registry, source-row and offering-ID sets agree; current standard target is in scope.

Current official sources (checked 7 October 2026):

- [Studieprogramma Griekse en Latijnse Taal en Cultuur jaar 1](https://www.ru.nl/opleidingen/bachelors/griekse-en-latijnse-taal-en-cultuur/studieprogramma-griekse-en-latijnse-taal-en-cultuur-jaar-1) — Indicative year label; compulsory-course and minor/free-space tables; Indicative 2027–2028. Twelve compulsory 5-EC courses include Greek and Latin grammar and original-text study. Optional intensification and zero-credit support are separate.
- [Studieprogramma Griekse en Latijnse Taal en Cultuur jaar 2](https://www.ru.nl/opleidingen/bachelors/griekse-en-latijnse-taal-en-cultuur/studieprogramma-griekse-en-latijnse-taal-en-cultuur-jaar-2) — Indicative year label; compulsory-course and minor/free-space tables; Indicative 2028–2029. Six required 5-EC Classics courses plus two restricted 15-EC Faculty of Arts minors; supplementary Classics minors are optional.
- [Studieprogramma Griekse en Latijnse Taal en Cultuur jaar 3](https://www.ru.nl/opleidingen/bachelors/griekse-en-latijnse-taal-en-cultuur/studieprogramma-griekse-en-latijnse-taal-en-cultuur-jaar-3) — Indicative year label; compulsory-course and minor/free-space tables; Indicative 2029–2030. Domestic route: four compulsory 5-EC courses, a 10-EC Classics thesis and 30 EC free space. The current indicative label is 2029–2030.
- [Studieprogramma Griekse en Latijnse Taal en Cultuur](https://www.ru.nl/opleidingen/bachelors/griekse-en-latijnse-taal-en-cultuur/studieprogramma) — Verleden en heden in theorie en praktijk; Current undated overview. Students translate classical source texts and analyse their language and literature; archaeology and cultural history complement this language core.

External credit structure: Stored components total 180 EC; current sources support the required/choice structure described in this scoped audit.

Result: confirmed; required action: reassess-exception.

Recommended follow-up: In a later production update, refresh comparator.academicYear and sourceNotes to the currently checked indicative year-three label, and retain the future-cohort caveat. Keep the supported Classics core and domestic/free-space structure; UCR feasibility requires stage two.

Unresolved factual question / limitation: Historical official page evidence was not established, so the label discrepancy does not prove whether the original description was erroneous or later superseded.

UCR-side reassessment pending: **yes**. Existing UCR claims are preserved as provenance only. Stage-two UCR feasibility assessment remains pending.

### cp-000051 — Human Neuroscience

Institution: Radboud University. Audit scope: Fresh official research into whether the external curriculum can now be reconstructed coherently.

Existing formal type: `external-programme-unresolved`; existing check date: 2026-09-25.

Existing substantive reason: A coherent year-three 60-EC route cannot be reconstructed from the current official evidence. The adopted 2026–27 OER says the third year is still in development and identifies only the required 18-EC research project and 26 EC of free space. The public prospectus labels the year 60 EC but lists an additional 1 + 9 + 12 EC of personal development, STEM and track choices, which yields 66 EC. Removing a 6-EC choice or reducing free space would be an unsupported curricular decision; a full 180-EC comparator and fair comparison must wait for Radboud to clarify the structure.

Fresh official research still cannot assign all third-year credits to a verified compulsory/choice structure. The OER leaves year three in development and specifies 18 EC research plus 26 EC free space; 16 EC remain structurally unspecified. The current prospectus now supplies no detailed year-three table. The stored 66-EC prospectus calculation cannot be repeated from the current page, while the underlying reconstruction obstacle persists.

Provenance: data/counselor/comparisons/cp-000051.json; source worksheet row(s) 54. Canonical provider, normalized registry, source-row and offering-ID sets agree; current standard target is in scope.

Current official sources (checked 7 October 2026):

- [Humane Neurowetenschappen — OER Bachelor 2026–2027](https://www.ru.nl/ru-bestanden/fsw-oer-2026-2027-hnw-bachelor) — Articles 9.4–9.6, printed pp. 16–18; Adopted 2026–2027, effective 1 September 2026. Degree load is 180 EC. First year is 60 EC; the provisional second-year allocations total 60 EC. Third year remains in development, with an 18-EC final project and 26 EC free space specified.
- [Studieprogramma bachelor Humane Neurowetenschappen jaar 2](https://www.ru.nl/opleidingen/bachelors/humane-neurowetenschappen/studieprogramma-van-deze-opleiding/studieprogramma-bachelor-humane-neurowetenschappen-jaar-2) — Development caveat and required-course table; Current provisional year-two page. The indicative second-year course table totals 60 EC; it explicitly remains in development.
- [Studieprogramma bachelor Humane Neurowetenschappen jaar 3](https://www.ru.nl/opleidingen/bachelors/humane-neurowetenschappen/studieprogramma-van-deze-opleiding/studieprogramma-bachelor-humane-neurowetenschappen-jaar-3) — Over dit studieprogramma and total EC; Current provisional year-three page. Current page gives a 60-EC heading and says the year remains in development, without the course/choice table underlying the stored 66-EC claim.

External credit structure: Incomplete 164-EC supported reconstruction; missing 16 EC remain unresolved.

Result: still-unresolved; required action: research-again-later.

Recommended follow-up: Retain the unresolved outcome pending official clarification of the remaining 16 EC and later-year requirements. At the next production update, replace the unsupported current-page 66-EC claim with the present development caveat and OER allocation. Research again when Radboud publishes a complete third-year programme; do not invent credits or infer UCR feasibility.

Unresolved factual question / limitation: What required and restricted-choice components fill the remaining 16 EC in year three, and which final second-/third-year structure will apply? The official catalogue could not be retrieved through the research tool; no accessible clarifying third-year source was found. Historical evidence for the former 66-EC page is unverified.

UCR feasibility was not assessed; a complete external reconstruction remains unresolved.

### cp-000055 — Islam, Politics and Society

Institution: Radboud University. Audit scope: External-programme identity, defining compulsory curriculum, choice structure and source context only; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-09-25.

Existing substantive reason: Radboud’s Islam, Politiek en Samenleving specialisation is defined by compulsory academic study of Islam’s history, prophetic sources, sacred texts, Islamic thought, lived religion, transnational Muslim communities and Islamic theology. The UCR course catalogue contains no Islam or religious-studies sequence, no Islamic theology or Qur’an-based textual training, and no Arabic. A 24-course schedule assembled from politics, sociology, history, law and philosophy would have substantial general social-science content but would omit the target’s defining field. Presenting that schedule as a closest UCR alternative would misstate what UCR teaches.

The exact IPS specialisation without Arabic is supported by the adopted OER: Islamic history/sources, sacred texts, lived Islam, transnational Islam and Islamic theology are compulsory within the 120-EC major. Two modules are restricted choices and the 30-EC minor space remains free. Arabic is optional and is not a requirement of the audited route.

Provenance: data/counselor/comparisons/cp-000055.json; source worksheet row(s) 58. Canonical provider, normalized registry, source-row and offering-ID sets agree; current standard target is in scope.

Current official sources (checked 7 October 2026):

- [OER Bachelor Religiewetenschappen 2026–2027](https://www.ru.nl/ru-bestanden/oer-2026-2027-bachelor-religiewetenschappen) — Article 13; Annex II IPS without Arabic, printed pp. 28–30; Adopted 2026–2027. The no-Arabic IPS route comprises 120 EC major courses, two restricted 15-EC THRW modules and 30 EC free minor space. Required Islam/text/theology content is explicit; the Arabic route is separate.
- [Studieprogramma Islam, politiek en samenleving](https://www.ru.nl/opleidingen/bachelors/islam-politiek-en-samenleving/studieprogramma) — Identity, four core themes and Arabic option; Current undated overview. IPS is the Islam specialisation within Religious Studies; Islamic origins/sources, history and society are central. Arabic is optional.

External credit structure: Stored components total 180 EC; current sources support the required/choice structure described in this scoped audit.

Result: confirmed; required action: none.

No material factual question remains unresolved within the defining external-basis scope. Indicative future pages are not a guarantee of the entering cohort’s eventual timetable.

UCR-side reassessment pending: **yes**. Existing UCR claims are preserved as provenance only. Stage-two UCR feasibility assessment remains pending.

### cp-000057 — Molecular Life Sciences

Institution: Radboud University. Audit scope: External-programme identity, defining compulsory curriculum, choice structure and source context only; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-09-25.

Existing substantive reason: The Radboud degree is an integrated molecular biology AND chemistry programme. Its compulsory first year already includes atoms and molecules, analytical chemistry and a chemical-analysis lab, organic chemistry and synthesis lab, biochemistry and its lab, thermodynamics, cell biophysics and a molecular-sciences lab. The later compulsory core deepens organic, inorganic and analytical chemistry, crystal structure, biomolecular mechanisms and structural bioinformatics, then requires a supervised 12-EC research internship. UCR offers valuable molecular-cell and biomedical courses but lacks a sequence in organic/inorganic/analytical/physical chemistry, molecular spectroscopy and synthesis, and has only one broad life-science laboratory course. A 24-course UCR schedule could sustain biomedical biology with data methods, but it would omit the defining chemistry and multi-lab spine and would misrepresent equivalence to this molecular-science degree.

Current programme pages and the adopted EER support a molecular biology/chemistry degree with compulsory analytical/organic/inorganic chemistry, several laboratory courses, biomolecular study and research internship. The 57-EC differentiation phase, minimum 18-EC ML1 choice and 6-EC open space are preserved rather than treating every optional molecular topic as mandatory.

Provenance: data/counselor/comparisons/cp-000057.json; source worksheet row(s) 60. Canonical provider, normalized registry, source-row and offering-ID sets agree; current standard target is in scope.

Current official sources (checked 7 October 2026):

- [Education and Examination Regulations 2026–2027 — Bachelor Molecular Life Sciences](https://www.ru.nl/sites/default/files/2026-09/20260908-oer-26-27-ba-molecular-life-sciences_eng-gb-juiste-tabellen.pdf) — Articles 7.3–7.5, printed pp. 19–22; Adopted 2026–2027 English translation. 60 EC first year, 45 EC later mandatory core, 57 EC differentiation (at least 18 EC ML1), 12 EC internship/report and 6 EC free electives. Chemistry and multiple laboratories remain mandatory.
- [Molecular Life Sciences — study programme](https://www.ru.nl/en/education/bachelors/molecular-life-sciences/study-programme) — Programme and year descriptions; Current programme overview. Molecular biology is combined with a strong chemistry, physics and mathematics foundation; the biomedical direction develops after that foundation.
- [EER Faculty of Science](https://www.ru.nl/en/students/studying/rules-and-guidelines/education-and-examination-regulations/science) — Current-year regulations and precedence statement; 2026–2027. Index links the three 2026–2027 regulations used here. Dutch versions take precedence in an interpretation conflict; the EER takes precedence over the course catalogue.

External credit structure: Stored components total 180 EC; current sources support the required/choice structure described in this scoped audit.

Result: confirmed; required action: none.

No material factual question remains unresolved within the defining external-basis scope. Indicative future pages are not a guarantee of the entering cohort’s eventual timetable.

UCR-side reassessment pending: **yes**. Existing UCR claims are preserved as provenance only. Stage-two UCR feasibility assessment remains pending.

### cp-000058 — Natural Sciences

Institution: Radboud University. Audit scope: External-programme identity, defining compulsory curriculum, choice structure and source context only; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-09-25.

Existing substantive reason: Radboud Natural Sciences teaches physics, chemistry, (molecular) biology and mathematics together. The compulsory first year includes chemical analysis and lab, organic chemistry and synthesis lab, atoms and molecules, biochemistry, thermodynamics, mechanics and lab, and electromagnetism; the shared later core adds quantum mechanics and vector calculus. The selected physical-chemistry route requires advanced mechanics, electromagnetism, spectroscopy, chemical bonding and physical organic chemistry. UCR has viable biology, environmental science, data and mathematics courses, but it has no taught sequence in chemistry or core mechanics/electromagnetism/quantum physics. Its few relevant biochemistry and broad life-science lab offerings cannot stand in for the missing experimental chemistry and physics. A 24-course environmental/biomedical/data curriculum would be a different degree, not a faithful closest response to this exact target.

The adopted EER supports the shared physics/chemistry/biochemistry/mathematics core and the exact Physical Chemistry route. Its 33-EC specified specialisation requirements and 39-EC restricted choice are distinct from 6 EC open space. Alternative specialisations retain the shared mandatory physics/chemistry core.

Provenance: data/counselor/comparisons/cp-000058.json; source worksheet row(s) 61. Canonical provider, normalized registry, source-row and offering-ID sets agree; current standard target is in scope.

Current official sources (checked 7 October 2026):

- [Education and Examination Regulations 2026–2027 — Bachelor Natural Sciences](https://www.ru.nl/sites/default/files/2026-09/20260905-oer-26-27-ba-natural-sciences_eng-gb-juiste-tabellen.pdf) — Articles 7.3–7.5, printed pp. 20–24; Adopted 2026–2027 English translation. 60 EC first year, 30 EC later common core, 72 EC specialisation, 6 EC free electives and 12 EC internship/report. Physical Chemistry has 33 EC named requirements and 39 EC choice; all routes retain common chemistry/physics requirements.
- [Natural Sciences — study programme](https://www.ru.nl/en/education/bachelors/natural-sciences/study-programme) — Programme and year descriptions; Current programme overview. Physics, biology and chemistry form the common foundation; biological-chemical, biological-physical and physical-chemical routes are alternatives.
- [EER Faculty of Science](https://www.ru.nl/en/students/studying/rules-and-guidelines/education-and-examination-regulations/science) — Current-year regulations and precedence statement; 2026–2027. Index links the three 2026–2027 regulations used here. Dutch versions take precedence in an interpretation conflict; the EER takes precedence over the course catalogue.

External credit structure: Stored components total 180 EC; current sources support the required/choice structure described in this scoped audit.

Result: confirmed; required action: none.

No material factual question remains unresolved within the defining external-basis scope. Indicative future pages are not a guarantee of the entering cohort’s eventual timetable.

UCR-side reassessment pending: **yes**. Existing UCR claims are preserved as provenance only. Stage-two UCR feasibility assessment remains pending.

### cp-000059 — Physics and Astronomy

Institution: Radboud University. Audit scope: External-programme identity, defining compulsory curriculum, choice structure and source context only; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-09-25.

Existing substantive reason: The Radboud bachelor requires a sustained physics and astronomy spine: mechanics, electromagnetism, optics, thermodynamics, quantum theory, relativity, laboratory physics and a survey of the universe in year one, followed by advanced mechanics, electromagnetism, two quantum courses, statistical mechanics, atomic and solid-state physics, subatomic physics and two further laboratory courses. The 12-EC final project is research in the same field. UCR offers relevant mathematics and programming but no mechanics, electromagnetism, quantum physics, astrophysics, modern physics or experimental physics laboratory sequence. A 24-course mathematics/data/environmental-science schedule could be coherent on its own but would leave virtually all of this target’s defining discipline absent. Calling it a closest Physics and Astronomy comparison would mislead prospective students.

The adopted EER confirms the mandatory physics/astronomy and experimental-laboratory sequence, including the combined 9-EC first-year practical/data course, 69 EC later compulsory study and 12-EC final project. The optional advanced astronomy minor and separate dual bachelor do not define all students’ ordinary route.

Provenance: data/counselor/comparisons/cp-000059.json; source worksheet row(s) 62. Canonical provider, normalized registry, source-row and offering-ID sets agree; current standard target is in scope.

Current official sources (checked 7 October 2026):

- [Education and Examination Regulations 2026–2027 — Bachelor Physics and Astronomy](https://www.ru.nl/sites/default/files/2026-09/20260905-oer-26-27-ba-natuur-en-sterrenkunde_eng-gb-juiste-tabellen.pdf) — Articles 7.3–7.5, printed pp. 20–22; Adopted 2026–2027 English translation. 60 EC first year, 69 EC later compulsory courses, 39 EC elective space and 12 EC final research internship. Physics laboratories and quantum/mechanics/electromagnetism sequences are mandatory; advanced astronomy minor and 225-EC dual degree are separate.
- [Physics and Astronomy — study programme](https://www.ru.nl/opleidingen/bachelors/natuur-en-sterrenkunde/studieprogramma) — Programme and year descriptions; Current programme overview. The ordinary bachelor covers experimental and theoretical physics and astronomy; later study retains a physics core alongside choice.
- [EER Faculty of Science](https://www.ru.nl/en/students/studying/rules-and-guidelines/education-and-examination-regulations/science) — Current-year regulations and precedence statement; 2026–2027. Index links the three 2026–2027 regulations used here. Dutch versions take precedence in an interpretation conflict; the EER takes precedence over the course catalogue.

External credit structure: Stored components total 180 EC; current sources support the required/choice structure described in this scoped audit.

Result: confirmed; required action: none.

No material factual question remains unresolved within the defining external-basis scope. Indicative future pages are not a guarantee of the entering cohort’s eventual timetable.

UCR-side reassessment pending: **yes**. Existing UCR claims are preserved as provenance only. Stage-two UCR feasibility assessment remains pending.

### cp-000060 — Dutch Language and Culture

Institution: Radboud University. Audit scope: External-programme identity, defining compulsory curriculum, choice structure and source context only; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-09-25.

Existing substantive reason: Dutch language, Dutch and Flemish literary history, Dutch linguistics, and advanced academic analysis and writing in Dutch define this programme. Its compulsory courses include Dutch literature before and after 1800, history of the Dutch language, historical and modern Dutch literary study, first-language acquisition, speech sounds, syntax, sociolinguistics, psycholinguistics and a Dutch-field bachelor thesis. UCR has one basic Dutch-language course for everyday communication and genuine broader courses in literature, communication, rhetoric and psycholinguistics. Those broader subjects do not supply a sustained advanced Dutch-language or Dutch-literature sequence. A 24-course English-taught literature and communication degree would address some methods and themes but would change the named academic field and leave much of the Dutch core uncovered.

The current OER corroborates Dutch-field learning outcomes, literary history, linguistics and research. The indicative entry sequence supports the stored coherent 180-EC route with Psycholinguïstiek counted once, and distinguishes 30 EC restricted minors from 30 EC open space. Its future third year remains provisional rather than adopted 2026–2027 content.

Provenance: data/counselor/comparisons/cp-000060.json; source worksheet row(s) 63. Canonical provider, normalized registry, source-row and offering-ID sets agree; current standard target is in scope.

Current official sources (checked 7 October 2026):

- [Studieprogramma Nederlandse Taal en Cultuur jaar 1](https://www.ru.nl/opleidingen/bachelors/nederlandse-taal-en-cultuur/studieprogramma-nederlandse-taal-en-cultuur-jaar-1) — Indicative year label; compulsory-course and minor/free-space tables; Indicative 2027–2028. Twelve compulsory 5-EC courses include Dutch literary history before/after 1800, language acquisition, sounds and literary analysis.
- [Studieprogramma Nederlandse Taal en Cultuur jaar 2](https://www.ru.nl/opleidingen/bachelors/nederlandse-taal-en-cultuur/studieprogramma-nederlandse-taal-en-cultuur-jaar-2) — Indicative year label; compulsory-course and minor/free-space tables; Indicative 2028–2029. Six compulsory 5-EC courses include Dutch-language history, historical literature, syntax and psycholinguistics; two restricted Arts minors total 30 EC.
- [Studieprogramma Nederlandse Taal en Cultuur jaar 3](https://www.ru.nl/opleidingen/bachelors/nederlandse-taal-en-cultuur/studieprogramma-nederlandse-taal-en-cultuur-jaar-3) — Indicative year label; compulsory-course and minor/free-space tables; Indicative 2029–2030. Domestic route: four 5-EC major courses, a 10-EC bachelor thesis and 30 EC open space; modern Dutch literature and sociolinguistics are compulsory in this indicative route.
- [Nederlandse Taal en Cultuur — OER 2026–2027](https://www.ru.nl/ru-bestanden/oerbntc2627) — Articles 3–5, printed pp. 5–8; Adopted 2026–2027. Formal Dutch-field learning outcomes and curriculum corroborate the named core. Concurrent B2 and B3 tables list the same Psycholinguïstiek code; the stored prospective route counts it once.

External credit structure: Stored components total 180 EC; current sources support the required/choice structure described in this scoped audit.

Result: confirmed; required action: none.

No material factual question remains unresolved within the defining external-basis scope. Indicative future pages are not a guarantee of the entering cohort’s eventual timetable.

UCR-side reassessment pending: **yes**. Existing UCR claims are preserved as provenance only. Stage-two UCR feasibility assessment remains pending.

### cp-000061 — Notarial Law

Institution: Radboud University. Audit scope: External-programme identity, defining compulsory curriculum, choice structure and source context only; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-09-25.

Existing substantive reason: The Notarial Law bachelor is a sustained Dutch-law curriculum: foundational Dutch constitutional and administrative, private, criminal and procedural law leads into civil law I and II, persons and family law, business law, succession and marital property law, private international law for notarial practice, notarial professional ethics and regulation, and multiple Dutch tax subjects. UCR has substantive general and comparative law courses, but no curricular sequence in Dutch civil and notarial law, Dutch family and succession law, Dutch taxation or notarial practice. Even a 24-course selection of UCR law and neighboring courses would omit defining compulsory content and cannot credibly be described as the named Notarial Law degree.

The indicative pages and accessible current Dutch OER corroborate sustained Dutch private/notarial law, family/succession law, taxation, professional regulation and thesis requirements. The 5-EC choice is restricted, not general electives. The stored August English OER URL returns 404; the current Dutch September OER supplies direct formal support.

Provenance: data/counselor/comparisons/cp-000061.json; source worksheet row(s) 64. Canonical provider, normalized registry, source-row and offering-ID sets agree; current standard target is in scope.

Current official sources (checked 7 October 2026):

- [Studieprogramma bachelor Notarieel Recht jaar 1](https://www.ru.nl/opleidingen/bachelors/rechtsgeleerdheid/studieprogramma-rechtsgeleerdheid/studieprogramma-bachelor-notarieel-recht-jaar-1) — Indicative year label and required/restricted-choice tables; Indicative 2027–2028. Shared law foundation totals 60 EC and covers Dutch public/private/criminal law, international/EU law and academic skills.
- [Studieprogramma bachelor Notarieel Recht jaar 2](https://www.ru.nl/opleidingen/bachelors/notarieel-recht/studieprogramma-notarieel-recht/studieprogramma-bachelor-notarieel-recht-jaar-2) — Indicative year label and required/restricted-choice tables; Indicative 2027–2028. Required 60-EC notarial year covers civil law I/II, civil procedure, persons/family law, taxation, business law and research skills.
- [Studieprogramma bachelor Notarieel Recht jaar 3](https://www.ru.nl/opleidingen/bachelors/notarieel-recht/studieprogramma/studieprogramma-bachelor-notarieel-recht-jaar-3) — Indicative year label and required/restricted-choice tables; Indicative 2027–2028. 55 EC compulsory notarial/tax/private-law courses and thesis plus one restricted 5-EC metajuridical option, paired as 4+1 EC.
- [OER Faculteit der Rechtsgeleerdheid 2026–2027](https://www.ru.nl/sites/default/files/2026-09/oer_2026-2027-fdr.pdf) — Annex VI, Article 4, printed pp. 56–57; Adopted 2026–2027. Current Dutch OER independently confirms the notarial bachelor curriculum, including Dutch succession/property, notarial ethics/regulation, taxation and a 5-EC thesis.
- [OER Faculteit der Rechtsgeleerdheid](https://www.ru.nl/studenten/onderwijs-volgen/regels-en-richtlijnen/onderwijs-en-examenregelingen/rechtsgeleerdheid) — Current-year OER link and annual-regulation notice; 2026–2027. Current Dutch index links the accessible September 2026 PDF and confirms the move to annual regulations. The stored August English PDF returned 404 when followed from the English index.

External credit structure: Stored components total 180 EC; current sources support the required/choice structure described in this scoped audit.

Result: confirmed; required action: reassess-exception.

Recommended follow-up: In a later production update, replace or supplement the inaccessible English regulations URL with the accessible Dutch 2026–2027 OER and its current index. Retain the supported notarial curriculum and the distinction between adopted regulations and indicative 2027–2028 pages. UCR feasibility remains a stage-two question.

Unresolved factual question / limitation: The historical availability of the stored English PDF was not verified. This is a source-reference follow-up, not evidence that the current external curriculum basis is wrong.

UCR-side reassessment pending: **yes**. Existing UCR claims are preserved as provenance only. Stage-two UCR feasibility assessment remains pending.

## Cumulative findings after batch 4

| Finding | Count |
|---|---:|
| confirmed | 36 |
| incorrect | 3 |
| outdated | 0 |
| still-unresolved | 1 |

| Required action | Count |
|---|---:|
| none | 33 |
| reprocess-as-comparison | 0 |
| reassess-exception | 6 |
| correct-registry-and-reprocess | 0 |
| research-again-later | 1 |

## Batch 4 findings

Seven records are confirmed within the external-programme scope. CP070, CP076 and CP095 have incorrect current credit, choice or narrative descriptions and require reassessment. All ten defining subject cores remain supported. The three incorrect findings concern only the identified external descriptions; they do not establish that any ultimate UCR exception decision is incorrect. No comparison conversion is recommended. Historical evidence does not justify an outdated finding for CP070 or CP076.

| ID | Programme | Formal type | Finding | Required action |
|---|---|---|---|---|
| cp-000063 | Pedagogical Sciences of Primary Education | no-defensible-ucr-match | confirmed | none |
| cp-000068 | Religion, Politics and Society (Religie, Politiek en Samenleving) | no-defensible-ucr-match | confirmed | none |
| cp-000070 | Chemistry (Scheikunde) | no-defensible-ucr-match | incorrect | reassess-exception |
| cp-000072 | Spanish Language and Culture (Spaanse Taal en Cultuur) | no-defensible-ucr-match | confirmed | none |
| cp-000073 | Linguistics (Taalwetenschap) | no-defensible-ucr-match | confirmed | none |
| cp-000074 | Dentistry (Tandheelkunde) | no-defensible-ucr-match | confirmed | none |
| cp-000075 | Theology (Theologie) | no-defensible-ucr-match | confirmed | none |
| cp-000076 | Mathematics (Wiskunde) | no-defensible-ucr-match | incorrect | reassess-exception |
| cp-000079 | Archaeology (Archeologie) | no-defensible-ucr-match | confirmed | none |
| cp-000095 | Pharmaceutical Sciences (Farmaceutische Wetenschappen) | no-defensible-ucr-match | incorrect | reassess-exception |

## Batch 4 evidence

### cp-000063 — Pedagogical Sciences of Primary Education

Institution: Radboud University. Audit scope: External-programme identity, defining compulsory curriculum, choice structure and source context only; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-09-25.

Existing substantive reason: PWPO is an integrated academic primary-teacher-education degree that confers primary-school teaching qualification. The core includes 33 EC in four supervised classroom placements, direct instruction, classroom management and pedagogical practice, plus sustained subject didactics in early reading, handwriting, spelling, speaking and writing, reading comprehension and literature, mathematics, world orientation, art and multilingual learning. UCR offers an academic cluster in development, cognition, psychology, research and society, and one communication project with primary-school pupils, but no sequence in primary subject didactics, classroom management, sustained supervised teaching or teacher qualification. A coherent 24-course developmental-psychology programme could respond to some child-development interests, but would omit the defining teaching practice and profession-specific academic preparation of this named degree. It cannot be presented as its closest defensible UCR response.

The exact PWPO standard route retains a required pedagogical/didactic core, primary-school teaching practice and teacher qualification. Its 33 EC of four placements and 16 EC total open choice are correctly separated from required university study and the thesis. Zero-credit support and the distinct ALPO route are not counted.

Provenance: data/counselor/comparisons/cp-000063.json; source worksheet row(s) 66. Canonical provider, normalized registry, source-row and offering-ID sets agree; current standard target is in scope.

Current official sources (checked 7 October 2026):

- [Pedagogische Wetenschappen van Primair Onderwijs — jaar 1](https://www.ru.nl/opleidingen/bachelors/pedagogische-wetenschappen-van-primair-onderwijs/studieprogramma/studieprogramma-pwpo-jaar-1) — Year label; required-course, placement and choice tables; Provisional 2026–2027. 52 EC required university courses and 8 EC primary-school placement; subject didactics and classroom practice are compulsory.
- [Pedagogische Wetenschappen van Primair Onderwijs — jaar 2](https://www.ru.nl/opleidingen/bachelors/pedagogische-wetenschappen-van-primair-onderwijs/studieprogramma/studieprogramma-pwpo-jaar-2) — Year label; required-course, placement and choice tables; Provisional 2026–2027. 48 EC required university courses, 8 EC placement and 4 EC open choice; Analyse 3 is one optional use of that space.
- [Pedagogische Wetenschappen van Primair Onderwijs — jaar 3](https://www.ru.nl/opleidingen/bachelors/pedagogische-wetenschappen-van-primair-onderwijs/studieprogramma/studieprogramma-pwpo-jaar-3) — Year label; required-course, placement and choice tables; Provisional 2026–2027. 31 EC required university study including a 10-EC thesis, 7 EC placement, 10 EC final placement and 12 EC open choice. Optional method/skills units do not define all students.
- [Pedagogische Wetenschappen van Primair Onderwijs](https://www.ru.nl/opleidingen/bachelors/pedagogische-wetenschappen-van-primair-onderwijs) — Programme facts and teaching qualification; Current programme facts. The ordinary full-time Dutch BSc is 180 EC, CROHO 59329, and combines pedagogical study with qualification to teach primary school. It is distinct from ALPO.

External credit structure: Stored components total 180 EC; current sources support the required/choice structure described in this scoped audit.

Result: confirmed; required action: none.

No material factual question remains unresolved within the defining external-basis scope. Indicative future pages are not a guarantee of the entering cohort’s eventual timetable.

UCR-side reassessment pending: **yes**. Existing UCR claims are preserved as provenance only. Stage-two UCR feasibility assessment remains pending.

### cp-000068 — Religion, Politics and Society (Religie, Politiek en Samenleving)

Institution: Radboud University. Audit scope: External-programme identity, defining compulsory curriculum, choice structure and source context only; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-09-25.

Existing substantive reason: The defining curriculum is religious studies: a full first year studying Judaism, Islam, Christianity, Hinduism, Buddhism, sacred texts, religious practices, theology, sociology and anthropology of religion; a further 45 EC of second-year work in philosophy of religious studies, spirituality, religious identity, migration, ritual and religious media; at least two 15-EC religion-based thematic modules; and an independent religion-politics-society final work. Even with the 30 EC genuinely free minor space, 150 EC remains in religious-studies and religion-linked practice, methods, modules and thesis. UCR lacks a dedicated course in the study of religion, religious traditions, theology or religion-specific research methods, let alone a coherent 24-course religious-studies progression. A programme in politics, philosophy and sociology could study surrounding social questions but would omit the target’s defining religion curriculum and would misrepresent a nearest academic match.

Current official pages corroborate the exact RPS Religious Studies specialisation, sustained religion/text/social-science methods and thesis. Required study is distinguished from two 15-EC thematic-module selections and 30 EC open space. Normalized full-time/part-time consolidation is consistent with the official identity.

Provenance: data/counselor/comparisons/cp-000068.json; source worksheet row(s) 71. Canonical provider, normalized registry, source-row and offering-ID sets agree; current standard target is in scope.

Normalization decision(s): rc-0009. Official identity supports the consolidated standard target and its delivery modes.

Current official sources (checked 7 October 2026):

- [Religie, Politiek en Samenleving — jaar 1](https://www.ru.nl/studieprogramma-bachelor-religie-politiek-en-samenleving-jaar-1) — Year label; required-course, placement and choice tables; Current undated year page. Eleven positive-credit required units total 60 EC, including a 10-EC questions/skills unit; world religions, sacred texts, religion/society and research methods are compulsory.
- [Religie, Politiek en Samenleving — jaar 2](https://www.ru.nl/studieprogramma-bachelor-religie-politiek-en-samenleving-jaar-2) — Year label; required-course, placement and choice tables; Current undated year page. 45 EC required study and one 15-EC thematic module; Religion and Care is a permitted selection rather than the only required module.
- [Religie, Politiek en Samenleving — jaar 3](https://www.ru.nl/studieprogramma-bachelor-religie-politiek-en-samenleving-jaar-3) — Year label; required-course, placement and choice tables; Current undated year page. 5 EC practice, 10 EC thesis, one 15-EC thematic module and 30 EC free space. Module alternatives and delivery variants must not be stacked.
- [Religie, Politiek en Samenleving](https://www.ru.nl/opleidingen/bachelors/religie-politiek-en-samenleving) — Programme facts and Religious Studies specialisation; Current programme facts. RPS is the Religious Studies specialisation under CROHO 50902: 180 EC, Dutch, full-time or part-time. Delivery modes do not create two different curricula.

External credit structure: Stored components total 180 EC; current sources support the required/choice structure described in this scoped audit.

Result: confirmed; required action: none.

No material factual question remains unresolved within the defining external-basis scope. Indicative future pages are not a guarantee of the entering cohort’s eventual timetable.

UCR-side reassessment pending: **yes**. Existing UCR claims are preserved as provenance only. Stage-two UCR feasibility assessment remains pending.

### cp-000070 — Chemistry (Scheikunde)

Institution: Radboud University. Audit scope: External-programme identity, defining compulsory curriculum, choice structure and source context only; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-09-25.

Existing substantive reason: The defining 120 EC in years one and two is chemistry and laboratory centred: analytical, organic and inorganic chemistry; molecular structure and bonding; thermodynamics, quantum mechanics and physics; successive chemical synthesis and analysis laboratories. In year three, at least 12 EC of chemistry electives and a 12-EC independent chemistry research internship/report remain required. Although 27 EC can be freely chosen, UCR lacks a chemistry gateway and any stand-alone introductory or advanced organic, inorganic, analytical, physical or synthetic chemistry sequence. A 24-course UCR route using biology, geoscience, statistics and programming would have too little chemistry and would misrepresent the programme’s academic core.

The chemistry and laboratory core is supported, but the stored current credit/choice description is incorrect within this scope. It counts Academic Writing and an additional mandatory Writing about Science, although the latter can be a replacement. The adopted OER has 66 EC later required courses and 36 EC conditioned choice plus 6 EC genuinely free, not an unconditional 27-EC open block. Current year pages are all indicative 2027–2028.

Provenance: data/counselor/comparisons/cp-000070.json; source worksheet row(s) 73. Canonical provider, normalized registry, source-row and offering-ID sets agree; current standard target is in scope.

Current official sources (checked 7 October 2026):

- [Chemistry — jaar 1](https://www.ru.nl/opleidingen/bachelors/scheikunde/studieprogramma/studieprogramma-bachelor-chemistry-jaar-1) — Year label; required-course, placement and choice tables; Indicative 2027–2028. Required first-year chemistry, physics, mathematics and laboratories total 60 EC.
- [Chemistry — jaar 2](https://www.ru.nl/opleidingen/bachelors/scheikunde/studieprogramma/studieprogramma-bachelor-chemistry-jaar-2) — Year label; required-course, placement and choice tables; Indicative 2027–2028. The 60-EC table includes Academic Writing Molecular Sciences alongside organic/inorganic chemistry, quantum mechanics, synthesis and analytical work.
- [Chemistry — jaar 3](https://www.ru.nl/opleidingen/bachelors/scheikunde/studieprogramma/studieprogramma-bachelor-chemistry-jaar-3) — Year label; required-course, placement and choice tables; Indicative 2027–2028. 6 EC taught requirements (Academic Skills and one philosophy unit), 12 EC research and 42 EC choice, including at least 12 EC Chemistry. Writing about Science is not an additional universal third-year requirement on this page.
- [Bachelor OER 2026–2027 — Chemistry (Dutch)](https://www.ru.nl/ru-bestanden/oer-25-26-ba-chemistry-nl) — Articles 7.3–7.5, printed pp. 16–19; Adopted 2026–2027 as stated in document; URL slug says 25–26. 60 EC first year, 66 EC later compulsory courses, 36 EC conditioned choice (at least 12 EC BC1 Chemistry), 12 EC research and 6 EC genuinely free choice total 180 EC. Other conditioned courses normally belong to Science, with approved-minor rules.
- [EER 2026–2027 — Bachelor Chemistry (English translation)](https://www.ru.nl/sites/default/files/2026-09/20260905-oer-26-27-ba-chemistry_eng-gb-juiste-tabellen.pdf) — Articles 7.4 and 8.1, later-course table and transitional provisions; Adopted 2026–2027 English translation; Dutch controls. Academic Writing is a single 3-EC requirement; Writing about Science can replace it under the transitional rule. It is not an additional universal requirement alongside Academic Writing.
- [OER — Faculteit der Natuurwetenschappen, Wiskunde en Informatica](https://www.ru.nl/studenten/onderwijs-volgen/regels-en-richtlijnen/onderwijs-en-examenregelingen/natuurwetenschappen-wiskunde-en-informatica) — Current 2026–2027 regulations links; precedence notice; 2026–2027. Official index identifies the current Dutch Chemistry and Mathematics OERs. Dutch regulations prevail over translations, and regulations prevail over the catalogue in a conflict.

External credit structure: Stored components sum to 180 EC but required/choice labels and the extra writing requirement are unsupported for the current ordinary route. Adopted structure: 60+66+36+12+6=180 EC; only the final 6 EC is unconditioned free choice.

Result: incorrect; required action: reassess-exception.

Incorrect applies only to the specified current external credit, choice or narrative description. The defining subject core is supported; the ultimate UCR exception decision was not assessed.

Recommended follow-up: In a later production update, reconstruct the current applicable-cohort external allocation from the adopted Dutch OER: 60 first-year + 66 later required + 36 conditioned choice + 12 research + 6 open = 180 EC. Count the writing requirement once, apply Science/approved-minor and minimum Chemistry conditions, and refresh source/year context. Preserve the supported disciplinary core; independently reassess UCR feasibility in stage two.

Unresolved factual question / limitation: Historical dated page evidence was not established. The finding identifies unsupported current descriptions; it does not determine whether the original page was erroneous or later changed. An outdated finding is not justified.

UCR-side reassessment pending: **yes**. Existing UCR claims are preserved as provenance only. Stage-two UCR feasibility assessment remains pending.

### cp-000072 — Spanish Language and Culture (Spaanse Taal en Cultuur)

Institution: Radboud University. Audit scope: External-programme identity, defining compulsory curriculum, choice structure and source context only; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-09-25.

Existing substantive reason: The programme is built around progressive Spanish-language proficiency (Español 1–6), Spanish-language study of literature, linguistic variation, media, culture and politics of Spain and Latin America, a credited 15-EC study period at a Spanish-speaking university, and an independent Hispanic studies thesis. Even after preserving 30 EC of third-year free space, there is no 24-course UCR curriculum with sustained Spanish language instruction and advanced Hispanic literature/culture/linguistics in the medium of Spanish. A general culture, communication or history programme would erase the defining language and regional specialisation.

The exact Spanish specialisation retains required language progression, Hispanic literature/culture/linguistics, 15 EC study at a Spanish university and a specialist thesis. Two restricted Arts minors total 30 EC and later open space totals 30 EC. The selected supplementary minor courses are valid options, not universally mandatory requirements.

Provenance: data/counselor/comparisons/cp-000072.json; source worksheet row(s) 75. Canonical provider, normalized registry, source-row and offering-ID sets agree; current standard target is in scope.

Current official sources (checked 7 October 2026):

- [Spaanse Taal en Cultuur — jaar 1](https://www.ru.nl/opleidingen/bachelors/spaanse-taal-en-cultuur/studieprogramma-spaanse-taal-en-cultuur-jaar-1) — Year label; required-course, placement and choice tables; Indicative 2027–2028. Twelve required 5-EC units include four Spanish proficiency courses and Hispanic culture, language and literature.
- [Spaanse Taal en Cultuur — jaar 2](https://www.ru.nl/opleidingen/bachelors/spaanse-taal-en-cultuur/studieprogramma-spaanse-taal-en-cultuur-jaar-2) — Year label; required-course, placement and choice tables; Indicative 2028–2029. 30 EC core study including Spanish proficiency plus two restricted Faculty of Arts minors of 15 EC each. Supplementary Spanish minors are options.
- [Spaanse Taal en Cultuur — jaar 3](https://www.ru.nl/opleidingen/bachelors/spaanse-taal-en-cultuur/studieprogramma-spaanse-taal-en-cultuur-jaar-3) — Year label; required-course, placement and choice tables; Indicative 2029–2030. 15 EC required study at a Spanish university, 5 EC Hispanofonia, a 10-EC Hispanic-field thesis and 30 EC free space.
- [Spaanse Taal en Cultuur](https://www.ru.nl/opleidingen/bachelors/spaanse-taal-en-cultuur) — Programme facts and specialisation; Current programme facts. The Spanish route belongs to Romance Languages and Cultures, CROHO 56074; the standard bachelor is 180 EC.

External credit structure: Stored components total 180 EC; current sources support the required/choice structure described in this scoped audit.

Result: confirmed; required action: none.

No material factual question remains unresolved within the defining external-basis scope. Indicative future pages are not a guarantee of the entering cohort’s eventual timetable.

UCR-side reassessment pending: **yes**. Existing UCR claims are preserved as provenance only. Stage-two UCR feasibility assessment remains pending.

### cp-000073 — Linguistics (Taalwetenschap)

Institution: Radboud University. Audit scope: External-programme identity, defining compulsory curriculum, choice structure and source context only; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-09-25.

Existing substantive reason: The bachelor requires 60 EC of first-year foundations in the structure, acquisition, processing and disorders of human language; another 30 EC of core corpus, phonetic, sociolinguistic, experimental, semantic and syntactic analysis in year two; and a 10-EC independent linguistics thesis. The selected two arts minors deepen speech/language disorders, language and thought, second-language teaching and linguistic methods for 30 EC. Even allowing a genuinely open 30 EC third year, UCR has no coherent foundational sequence in phonetics, phonology, morphology, syntax, semantic theory, corpus linguistics, sociolinguistics or language pathology. A 24-course response built mostly from communication, psychology, AI and data science would replace the subject with neighbouring fields.

Current sources support sustained theoretical/experimental linguistics, phonetics, corpus work, syntax/meaning and a specialist thesis. The stored explanation correctly treats two misleading minor headings as 15 EC each, corroborated by the adopted 30-EC minor total. Its domestic future route is coherent and explicitly indicative; concurrent OER third-year subjects are not silently substituted.

Provenance: data/counselor/comparisons/cp-000073.json; source worksheet row(s) 76. Canonical provider, normalized registry, source-row and offering-ID sets agree; current standard target is in scope.

Current official sources (checked 7 October 2026):

- [Taalwetenschap — jaar 1](https://www.ru.nl/opleidingen/bachelors/taalwetenschap/studieprogramma-taalwetenschap-jaar-1) — Year label; required-course, placement and choice tables; Indicative 2027–2028. Twelve required 5-EC units combine language structure, acquisition, phonetics, research, statistics and supporting AI.
- [Taalwetenschap — jaar 2](https://www.ru.nl/opleidingen/bachelors/taalwetenschap/studieprogramma-taalwetenschap-jaar-2) — Year label; required-course, placement and choice tables; Indicative 2028–2029. 30 EC required corpus/experimental/phonetic/sociolinguistic/meaning/syntax study and two restricted Arts minors of 15 EC each. Two misleading 30-EC minor headings are contradicted by the page prose and formal total.
- [Taalwetenschap — jaar 3](https://www.ru.nl/opleidingen/bachelors/taalwetenschap/studieprogramma-taalwetenschap-jaar-3) — Year label; required-course, placement and choice tables; Indicative 2029–2030. Domestic route: 5 EC language proficiency, 10 EC professional development, 5 EC language/norms, a 10-EC thesis and 30 EC free space. The abroad route is an alternative.
- [Taalwetenschap — opleidingsspecifieke OER 2026–2027](https://www.ru.nl/sites/default/files/2026-06/opleidingsspecifiek-bachelor-tw.pdf) — Articles 3–5, printed pp. 5–8; Adopted 2026–2027. Formal language-field learning outcomes and 30 EC of second-year minor space corroborate the core and minor total. The concurrent OER third-year table differs from the future indicative page; it does not adopt the latter for a 2026 entrant.

External credit structure: Stored components total 180 EC; current sources support the required/choice structure described in this scoped audit.

Result: confirmed; required action: none.

No material factual question remains unresolved within the defining external-basis scope. Indicative future pages are not a guarantee of the entering cohort’s eventual timetable.

UCR-side reassessment pending: **yes**. Existing UCR claims are preserved as provenance only. Stage-two UCR feasibility assessment remains pending.

### cp-000074 — Dentistry (Tandheelkunde)

Institution: Radboud University. Audit scope: External-programme identity, defining compulsory curriculum, choice structure and source context only; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-09-25.

Existing substantive reason: The defining curriculum is dental education with successive preclinical dentistry courses across all three years, dental knowledge and medical–dental interaction every year, supervised patient treatment beginning in year two (7 EC) and continuing in year three (11 EC), and dental research/professional formation. Of 180 EC, only a 3-EC year-two choice is unrestricted. UCR does not teach dentistry, dental simulation/preclinical procedures, restorative or oral clinical methods, or supervised treatment in a dental clinic. A 24-course programme in biomedical sciences, anatomy, psychology and health policy would omit the clinical and professional core.

Current year tables support the compulsory clinical/preclinical dental core and supervised patient treatment, with 60, 57+3 and 60 EC across the three years. Scientific formation includes thesis work and is counted once. The isolated 3-EC free choice does not alter the defining dental-practice requirements.

Provenance: data/counselor/comparisons/cp-000074.json; source worksheet row(s) 77. Canonical provider, normalized registry, source-row and offering-ID sets agree; current standard target is in scope.

Current official sources (checked 7 October 2026):

- [Tandheelkunde — jaar 1](https://www.ru.nl/opleidingen/bachelors/tandheelkunde/studieprogramma-van-tandheelkunde/studieprogramma-bachelor-tandheelkunde-jaar-1) — Year label; required-course, placement and choice tables; Current undated year page. 60 EC compulsory dental/medical knowledge, professional formation and preclinical practice.
- [Tandheelkunde — jaar 2](https://www.ru.nl/opleidingen/bachelors/tandheelkunde/studieprogramma-van-tandheelkunde/studieprogramma-bachelor-tandheelkunde-jaar-2) — Year label; required-course, placement and choice tables; Current undated year page. 57 EC compulsory study and 3 EC open choice; the 7-EC clinical unit introduces supervised patient treatment in the second semester.
- [Tandheelkunde — jaar 3](https://www.ru.nl/opleidingen/bachelors/tandheelkunde/studieprogramma-van-tandheelkunde/studieprogramma-bachelor-tandheelkunde-jaar-3) — Year label; required-course, placement and choice tables; Current undated year page. 60 EC compulsory study includes 11 EC clinical treatment, 4 EC preclinical practice and 10.5 EC scientific formation. Thesis work is embedded, not additional credit.

External credit structure: Stored components total 180 EC; current sources support the required/choice structure described in this scoped audit.

Result: confirmed; required action: none.

No material factual question remains unresolved within the defining external-basis scope. Indicative future pages are not a guarantee of the entering cohort’s eventual timetable.

UCR-side reassessment pending: **yes**. Existing UCR claims are preserved as provenance only. Stage-two UCR feasibility assessment remains pending.

### cp-000075 — Theology (Theologie)

Institution: Radboud University. Audit scope: External-programme identity, defining compulsory curriculum, choice structure and source context only; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-09-25.

Existing substantive reason: The programme’s defining 150-EC major is explicitly Christian theology and related methods: biblical Hebrew and Greek, Old and New Testament interpretation, doctrinal and fundamental theology, pastoral and liturgical practice, church history and law, theology-specific ethics and spirituality, a required religion-based module and an independent theology final work. Only 30 EC is genuinely free. UCR offers philosophy, history, ethics, sociology, literature and cultural analysis but no sustained biblical-language, scriptural exegesis, theology, liturgy or pastoral sequence. A 24-course schedule in neighbouring humanities/social-science fields would erase this bachelor’s Christian theological identity.

The adopted OER supports the ordinary 180-EC Theology route, required biblical languages/texts, doctrine, history/law, ethics, practice and thesis. The stored reconstruction correctly supplies the 5-EC Liturgiewetenschap missing from the public first-year table. One restricted 15-EC thematic module and 30 EC open choice remain distinct. Full-time/part-time consolidation matches the official identity.

Provenance: data/counselor/comparisons/cp-000075.json; source worksheet row(s) 78. Canonical provider, normalized registry, source-row and offering-ID sets agree; current standard target is in scope.

Normalization decision(s): rc-0010. Official identity supports the consolidated standard target and its delivery modes.

Current official sources (checked 7 October 2026):

- [OER Bachelor Theologie 2026–2027](https://www.ru.nl/sites/default/files/2026-07/oer-2026-2027-bachelor-theologie-def.pdf) — Articles 1 and 13; Annex II, printed pp. 24–25; Adopted 2026–2027. The standard 180-EC route comprises a 150-EC major including one 15-EC thematic module, plus 30 EC free space. Three 60-EC year tables include Liturgiewetenschap, Biblical Hebrew and Greek, exegesis, doctrine, church law/history, ethics, practice and thesis.
- [Theologie — jaar 1](https://www.ru.nl/opleidingen/bachelors/theologie/studieprogramma-van-bachelor-theologie/studieprogramma-bachelor-theologie-jaar-1) — 60-EC heading and course table; Current undated year page. Positive-credit entries on the public first-year page total 55 EC; the adopted OER supplies the omitted 5-EC Liturgiewetenschap requirement. The stored reconstruction already applies that formal correction.
- [Theologie](https://www.ru.nl/opleidingen/bachelors/theologie) — Programme facts; Current programme facts. The ordinary Dutch Theology bachelor is 180 EC, CROHO 56109, available full-time and part-time. The separate shortened route and delivery pacing do not redefine this standard target.

External credit structure: Stored components total 180 EC; current sources support the required/choice structure described in this scoped audit.

Result: confirmed; required action: none.

No material factual question remains unresolved within the defining external-basis scope. Indicative future pages are not a guarantee of the entering cohort’s eventual timetable.

UCR-side reassessment pending: **yes**. Existing UCR claims are preserved as provenance only. Stage-two UCR feasibility assessment remains pending.

### cp-000076 — Mathematics (Wiskunde)

Institution: Radboud University. Audit scope: External-programme identity, defining compulsory curriculum, choice structure and source context only; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-09-25.

Existing substantive reason: This mathematics degree requires a broad proof-based progression: 51 EC in a dense first-year mathematical core, an additional required 6 EC multivariable analysis and 18 EC in differential equations, rings/fields and topology in the selected line, then 30 EC more upper mathematics (18 restricted line electives and 12 additional mathematics electives), plus a 12-EC independent mathematics thesis, seminar and modelling work. UCR offers introductory and applied mathematics, statistics, programming and data science but lacks sustained stand-alone real/complex analysis, abstract algebra and topology at the required depth. Substituting AI and data-science courses for the upper mathematical sequence would misrepresent the defining Mathematics identity, despite substantial overlap in applied computational methods.

The mathematical/proof core remains supported, but the stored first-year 51+9 and later 48-EC line/36-EC free allocation does not describe the current ordinary route. Adopted regulations require 54+6 in year one and later 24 common + 36 line + 48 free + 12 thesis. The old 48-EC line is available under a dated cohort transition, while the public page still presents it generally. Current public year labels are all indicative 2027–2028.

Provenance: data/counselor/comparisons/cp-000076.json; source worksheet row(s) 79. Canonical provider, normalized registry, source-row and offering-ID sets agree; current standard target is in scope.

Current official sources (checked 7 October 2026):

- [Bachelor OER 2026–2027 — Wiskunde](https://www.ru.nl/sites/default/files/2026-08/bachelor-oer-26-27-wiskunde_20260818.pdf) — Articles 7.3–7.4, printed pp. 15–18; Article 8.1, printed pp. 24–25; Adopted 2026–2027. Current ordinary route: first year 54 EC required and 6 EC free; later 24 EC common courses, 36 EC Mathematics line (18 specified and 18 restricted, including at least 6 EC third-year courses), 48 EC free and 12 EC thesis. The older 48-EC line remains a transitional option for entrants in 2024–2025 or earlier.
- [OER — Faculteit der Natuurwetenschappen, Wiskunde en Informatica](https://www.ru.nl/studenten/onderwijs-volgen/regels-en-richtlijnen/onderwijs-en-examenregelingen/natuurwetenschappen-wiskunde-en-informatica) — Current 2026–2027 regulations links; precedence notice; 2026–2027. Official index identifies the current Dutch Chemistry and Mathematics OERs. Dutch regulations prevail over translations, and regulations prevail over the catalogue in a conflict.
- [Wiskunde — jaar 1](https://www.ru.nl/opleidingen/bachelors/wiskunde/studieprogramma/studieprogramma-bachelor-wiskunde-jaar-1) — Indicative label, required table and free-space explanation; Indicative 2027–2028. The current table requires 54 EC, including Statistics and Wiskundepracticum, and permits 6 EC free choice. The 9-EC elective menu is not a 9-EC allowance.
- [Wiskunde — jaar 2](https://www.ru.nl/opleidingen/bachelors/wiskunde/studieprogramma/studieprogramma-bachelor-wiskunde-jaar-2) — Indicative label and Mathematics-line explanation; Indicative 2027–2028. Public page still describes a 48-EC Mathematics line and 36 EC later free space. Adopted current regulations reduce the standard line to 36 EC; the old route is cohort-specific.
- [Wiskunde — jaar 3](https://www.ru.nl/opleidingen/bachelors/wiskunde/studieprogramma/studieprogramma-bachelor-wiskunde-jaar-3) — Required table and thesis description; Indicative 2027–2028. Seminar, modelling practical, portfolio and mathematical thesis corroborate a sustained mathematical/proof/research core. Choice rules must be taken from the adopted applicable-cohort regulations.

External credit structure: Stored components sum to 180 EC but mix an unsupported current first-year allocation with an older-cohort line. Current ordinary structure: 54+6+24+36+48+12=180 EC. Older-cohort transitional routes remain distinct.

Result: incorrect; required action: reassess-exception.

Incorrect applies only to the specified current external credit, choice or narrative description. The defining subject core is supported; the ultimate UCR exception decision was not assessed.

Recommended follow-up: In a later production update, select and state the applicable cohort before rebuilding external components. For the current ordinary route use 54 required + 6 free in year one, then 24 common + 36 line + 48 free + 12 thesis. Apply the restricted-course and third-year minima; do not impose the additional 12 EC Mathematics as universal. Preserve documented older-cohort alternatives and refresh labels. UCR feasibility remains stage two.

Unresolved factual question / limitation: Historical dated page evidence was not established. The finding identifies unsupported current descriptions; it does not determine whether the original page was erroneous or later changed. An outdated finding is not justified. The old line is valid for eligible older cohorts, not established as the default for a new entrant.

UCR-side reassessment pending: **yes**. Existing UCR claims are preserved as provenance only. Stage-two UCR feasibility assessment remains pending.

### cp-000079 — Archaeology (Archeologie)

Institution: Vrije Universiteit Amsterdam. Audit scope: External-programme identity, defining compulsory curriculum, choice structure and source context only; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-09-25.

Existing substantive reason: The external major devotes 138 specified EC to archaeological and ancient-world education before its separate 12-EC archaeology thesis, leaving 30 EC of free choice. Required study spans prehistoric, Roman, medieval and early-modern European material cultures, archaeological source and object analysis, scientific and digital archaeology, two credited field schools, excavation-to-publication training and disciplinary theory. UCR has a small, valuable archaeology and heritage group, including Introduction to World Archaeology, Greek Archaeology and Heritage & Ancient Democracy, but it has no excavation training sequence, archaeometric/materials laboratory sequence, European prehistoric-to-medieval archaeology sequence or archaeological thesis requirement. Filling 24 UCR courses with mostly modern history, art, cultural theory or generic research methods would present neighbouring subjects as an Archaeology bachelor. No defensible closest 24-course UCR programme can be formed.

The adopted 2026–2027 Dutch Archaeology route supports required excavation/field-school, material, digital, archaeological-method and specialist thesis study. Required 150 EC and open 30 EC are correctly reconstructed. Dutch/English alternatives and optional later field schools are not stacked. A future joint-degree notice in official search extracts does not overturn the verified current route.

Provenance: data/counselor/comparisons/cp-000079.json; source worksheet row(s) 82. Canonical provider, normalized registry, source-row and offering-ID sets agree; current standard target is in scope.

Current official sources (checked 7 October 2026):

- [OER Bachelor Archeologie 2026–2027](https://assets-us-01.kc-usercontent.com/f55d3574-6c6d-0002-e968-70643a2e365a/90c42b68-c609-4b9d-9123-3968f1e856be/OER%2026-27%20BA%20Archeologie%20NL.pdf) — Articles 10.2, 10.4 and 11.1–11.4, printed pp. 20–22; Adopted 2026–2027. Dutch and English routes are distinct. The Dutch route totals 180 EC: 60 EC first year, 78 EC later required units, 12 EC thesis and 30 EC free space. Field Schools 1/2, material study, digital archaeology and excavation/publication are required; additional field-school options are not universal requirements.
- [VU Studiegids — Archeologie](https://studiegids.vu.nl/nl/Bachelor/2026-2027/archeologie) — Programme facts and linked current OER; 2026–2027. Current guide identifies the 180-EC, three-year programme, Dutch/English routes and the adopted 2026–2027 OER.
- [VU Archeologie — toelating](https://vu.nl/nl/onderwijs/bachelor/archeologie/Toelating) — Official-page search extracts versus full-page retrieval; Future 2027–2028 announcement in search extract; full-page notice unverified. Official search extracts announce a joint VU/UvA degree from 2027–2028; the retrieved full-page text did not reproduce the notice. This is future identity context with retrieval uncertainty, not a conflict in the adopted 2026–2027 route.

External credit structure: Stored components total 180 EC; current sources support the required/choice structure described in this scoped audit.

Result: confirmed; required action: none.

Unresolved factual question / limitation: Search extracts announce a VU/UvA joint degree from 2027–2028, but full-page retrieval did not reproduce the notice. Verify that future identity at the next registry refresh; no current 2026–2027 identity conflict is established.

UCR-side reassessment pending: **yes**. Existing UCR claims are preserved as provenance only. Stage-two UCR feasibility assessment remains pending.

### cp-000095 — Pharmaceutical Sciences (Farmaceutische Wetenschappen)

Institution: Vrije Universiteit Amsterdam. Audit scope: External-programme identity, defining compulsory curriculum, choice structure and source context only; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-09-26.

Existing substantive reason: VU’s compulsory core centers on medicinal and organic chemistry, molecule design and synthesis, pharmacokinetics, bioanalysis, molecular pharmacology and toxicology laboratory work, followed by an 18-EC pharmaceutical research project. UCR offers relevant biology, biochemistry, pharmacology and disease courses, but no organic chemistry or synthesis sequence, pharmaceutical chemistry laboratory, ADME course, molecular toxicology practical or drug-design capstone. A 24-course biomedical path would represent a different field and obscure the chemical drug-discovery core of this target. The optional biology- or chemistry-focused minor does not remove that compulsory gap.

The adopted OER corroborates the stored components and chemistry/pharmacology laboratory core. However, exception.curriculumContext incorrectly says a 180-EC compulsory major plus 30 EC open space. The required major is 150 EC including the 18-EC project; 30 EC open space brings the total to 180. This narrative also contradicts the record’s own correct components and source notes.

Provenance: data/counselor/comparisons/cp-000095.json; source worksheet row(s) 101. Canonical provider, normalized registry, source-row and offering-ID sets agree; current standard target is in scope.

Current official sources (checked 7 October 2026):

- [OER Bachelor Farmaceutische Wetenschappen 2026–2027](https://assets-us-01.kc-usercontent.com/f55d3574-6c6d-0002-e968-70643a2e365a/38be6b3d-dbda-46a0-8097-8bf01e72a7fe/B%20Farmaceutische%20Wetenschappen%20OER%202026-2027.pdf) — Articles 10.2, 11.3 and 12.1, printed pp. 16–18; Adopted 2026–2027. Required courses total 150 EC: 60 EC first year, 60 EC second year, 12 EC third-year taught courses and an 18-EC project. The 30-EC profiling space brings the degree to 180 EC. Chemistry, synthesis, identification, pharmacokinetics, molecular pharmacology and toxicology laboratories remain compulsory.
- [VU Studiegids — Farmaceutische Wetenschappen](https://studiegids.vu.nl/nl/Bachelor/2026-2027/farmaceutische-wetenschappen) — Programme facts and linked current OER; 2026–2027. Guide confirms the 180-EC programme and links the adopted current regulations. Optional minors are not formal mandatory specialisations.

External credit structure: Stored components correctly total 180 EC: required major 150 EC plus 30 EC open space. The 180+30 narrative is incorrect.

Result: incorrect; required action: reassess-exception.

Incorrect applies only to the specified current external credit, choice or narrative description. The defining subject core is supported; the ultimate UCR exception decision was not assessed.

Recommended follow-up: In a later production update, correct exception.curriculumContext to 150 EC required major + 30 EC open profiling space = 180 EC. Retain the already correct component allocation and formal OER precedence for the modern-developments project. Preserve the supported subject core; reassess UCR feasibility independently in stage two.

No material factual question remains unresolved within the defining external-basis scope. Indicative future pages are not a guarantee of the entering cohort’s eventual timetable.

UCR-side reassessment pending: **yes**. Existing UCR claims are preserved as provenance only. Stage-two UCR feasibility assessment remains pending.

## Cumulative findings after batch 5

| Finding | Count |
|---|---:|
| confirmed | 39 |
| incorrect | 7 |
| outdated | 0 |
| still-unresolved | 4 |

| Required action | Count |
|---|---:|
| none | 35 |
| reprocess-as-comparison | 0 |
| reassess-exception | 10 |
| correct-registry-and-reprocess | 2 |
| research-again-later | 3 |

## Batch 5 findings

Three findings are confirmed, four are incorrect within their stated factual scope, and three remain externally unresolved. Current adopted regulations now supply complete external structures for CP097, CP098 and CP119; these require exception reassessment, not automatic comparison conversion. CP156 requires a route-dependent language/exegesis narrative correction. CP099 has a separately confirmed registry-language error while its curriculum remains unresolved. CP134’s existing registry exception is confirmed and requires a teach-out/language correction. These secondary attribute errors are recorded separately rather than double-counted in primary finding totals. No case is classified as outdated.

Every actionable batch-5 entry includes affected fields, proposed changes, dependencies, verification/closure checks and, where needed, a concrete research trigger. These prepare the later remediation pass; all plans remain unimplemented. Earlier audit objects are preserved.

| ID | Programme | Formal type | Finding | Required action |
|---|---|---|---|---|
| cp-000097 | Medicine (Geneeskunde) | external-programme-unresolved | incorrect | reassess-exception |
| cp-000098 | History (Geschiedenis) | external-programme-unresolved | incorrect | reassess-exception |
| cp-000099 | Health and Life Sciences (Gezondheid en Leven) | external-programme-unresolved | still-unresolved | correct-registry-and-reprocess |
| cp-000100 | Health Sciences (Gezondheidswetenschappen) | external-programme-unresolved | still-unresolved | research-again-later |
| cp-000119 | Bachelor Theologie en Religiewetenschappen | external-programme-unresolved | incorrect | reassess-exception |
| cp-000134 | Bachelor Fiscal Economics | registry-exception | confirmed | correct-registry-and-reprocess |
| cp-000140 | Circular Engineering | no-defensible-ucr-match | confirmed | none |
| cp-000149 | General Cultural Studies (Algemene Cultuurwetenschappen) | external-programme-unresolved | still-unresolved | research-again-later |
| cp-000156 | Theologie | no-defensible-ucr-match | incorrect | reassess-exception |
| cp-000159 | Archaeology | no-defensible-ucr-match | confirmed | none |

## Batch 5 evidence and implementation plans

### cp-000097 — Medicine (Geneeskunde)

Institution: Vrije Universiteit Amsterdam. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `external-programme-unresolved`; existing check date: 2026-09-26.

Existing substantive reason: The exact 2026-entry VUmc-Compas component credits, minor credit status and thesis weight cannot be verified from accessible current official VU sources. A complete 180-EC route would require guessed weights, so a canonical comparison cannot be made yet. Independently, the identified patient-centred clinical training, examination and diagnosis, professional practice and care/general-practice placements cannot be represented as a medical bachelor by UCR's academic biomedical and health courses.

Fresh public-HTML retrieval exposed the current Compas OER after web-tool failures. The current claim that component, minor and thesis credits cannot be verified is no longer supported: the adopted table supplies a complete 180-EC route, including a 24-EC minor and 6-EC thesis. The 2026-entry outgoing Compas sequence and clinical core are supported. Embedded clinical/research activities must not be credited twice.

Provenance: data/counselor/comparisons/cp-000097.json; source worksheet row(s) 104. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [VU Studiegids — Geneeskunde](https://studiegids.vu.nl/nl/Bachelor/2026-2027/geneeskunde) — Programme facts, current OER link and embedded-stage descriptions; Current 2026–2027 guide; retrieved directly as public HTML. Dutch, full-time, three-year, 180-EC VUmc-compas bachelor. Public HTML retrieval exposed the current OER link despite repeated web-retrieval failures. Clinical practice and research activities are partly embedded in the Arts en patiënt sequence.
- [OER Bachelor Geneeskunde VUmc-compas 2026–2027](https://assets-us-01.kc-usercontent.com/f55d3574-6c6d-0002-e968-70643a2e365a/151c0dc2-797e-46fb-b61c-ac16761ceb04/1%20OER%20Ba%20VUmc-compas%202026-2027%20DEF.pdf) — Articles 11.1–11.5, PDF pp. 15–18; Articles 12.1–12.3, PDF pp. 21–23 (repeated printed footer numbering); Adopted 2026–2027. Major 156 EC including a 6-EC thesis; minor 24 EC. Years one and two each have ten required 6-EC units. Year three has minor 24, thesis 6 and five required 6-EC clinical units. Care placement carries 6 EC; other practice/research lines are embedded rather than additional credit. External minors require approval, level conditions and no overlap. Medicine students do not add the extra 6-EC thesis required of visiting non-Medicine minor students.
- [Overgangsregeling VUMED360](https://vu.nl/nl/student/studenten-bachelor-geneeskunde/overgangsregeling-vumed360) — Publication update 26 August 2026; final teaching and validity dates; Current transition; future implementation dates. VUMED360 starts September 2027. Last complete old B1/B2/B3 teaching occurs in 2026–2027, 2027–2028 and 2028–2029 respectively; old results expire 31 August 2030. The Fall 2026 route is the outgoing Compas sequence.

External credit structure: Stored total 0 EC is intentionally partial. Current adopted Compas route is now verified at 60+60+60=180: required major 156 including thesis 6, plus minor 24. Embedded practice/research lines have no extra EC.

Verified reconstruction for later external remediation (audit evidence only):

| Study year | Component | EC | Status / qualification |
|---|---|---:|---|
| 1 | Binnenstebuiten (M_BBIBU22) | 6 | required |
| 1 | Bouw en bewegen (M_BBB15) | 6 | required |
| 1 | Metabole systemen (M_BMS15) | 6 | required |
| 1 | Medisch wetenschappelijk onderzoek 1 (M_BMWO115) | 6 | required |
| 1 | Arts en patiënt 1 (M_BAP115) | 6 | required |
| 1 | Homeostase (M_BHS15) | 6 | required |
| 1 | Circulatie en volumeregulatie (M_BCV15) | 6 | required |
| 1 | Hersenen en zintuigen (M_BHZ15) | 6 | required |
| 1 | Arts en patiënt 2 (M_BAP215) | 6 | required |
| 1 | Praktijkstage Zorg (M_BZS15) | 6 | required |
| 2 | Schade, afweer en herstel (M_BSAH15) | 6 | required |
| 2 | Start van het leven (M_BSVHL15) | 6 | required |
| 2 | Groei en ontwikkeling (M_BGO15) | 6 | required |
| 2 | Leefstijl, gezondheidszorg en het bewegingsapparaat (M_BLSGZ15) | 6 | required |
| 2 | Arts en patiënt 3 (M_BAP315) | 6 | required |
| 2 | Sekse, seksualiteit en relaties (M_BSSR15) | 6 | required |
| 2 | Infectie en inflammatie (M_BINF15) | 6 | required |
| 2 | Hematologie en oncologie (M_BHO15) | 6 | required |
| 2 | Medisch wetenschappelijk onderzoek 2 (M_BMWO215) | 6 | required |
| 2 | Arts en patiënt 4 (M_BAP415) | 6 | required |
| 3 | Approved minor | 24 | choice; Keep as one 24-EC block; approval/level/no-overlap rules apply. |
| 3 | Bachelorthesis (M_BBT16) | 6 | required |
| 3 | Spijsvertering en stofwisseling (M_BSS16) | 6 | required |
| 3 | Circulatie en vasculaire stoornissen (M_BCVS16) | 6 | required |
| 3 | Neurologie en oogheelkunde (M_BNO16) | 6 | required |
| 3 | Psychisch functioneren en cognitie (M_BPFC16) | 6 | required |
| 3 | Arts en patiënt 5 (M_BAP516) | 6 | required |

Total: **180 EC**; study-year totals **60 + 60 + 60**. Audit reconstruction only. Later taught requirements can change; retain transition/cohort context and verify applicable regulations when implementing.

Choice and source-context rules:

- 24-EC minor; outside faculty requires approval, maximum 6 EC at level 100 and minimum 12 EC at level 300; no overlap or placement-only minor.
- KWO1/KWO2 and general-practice placement are embedded; add no separate unverified EC.
- The additional visiting-student minor thesis is not an extra Medicine requirement.

Result: incorrect; required action: reassess-exception.

Incorrect concerns the current unavailable-credit basis, not the historical tool-access report or the ultimate UCR outcome.

Recommended follow-up: Reconstruct the external Compas route from the current OER, update sources and current unresolved rationale, and reassess the exception without automatically publishing a comparison.

Unresolved factual question / historical limitation: The prior tools’ access limitations are preserved as provenance. No dated historical evidence establishes that a previously valid curriculum changed into the present one; incorrect refers only to the current unsupported description or unresolved-source basis, not the truth of the original access report. An outdated classification is not justified.

Implementation plan — **not implemented; audit only**:

- `data/counselor/comparisons/cp-000097.json`, fields: `comparator.components`, `comparator.primarySourceUrl`, `comparator.additionalSourceUrls`, `comparator.academicYear`, `comparator.sourceNotes`, `exception.reason`, `exception.curriculumContext`, `exception.checkedOn`. Use verified_external_structure in this audit as the source-backed reconstruction; preserve its route, choice and cohort qualifiers. Refresh obsolete current access claims. Reassess the formal exception after external reconstruction; do not automatically change recordStatus/type.

Dependencies:

- No remaining broad external research prerequisite for the current adopted route; verify continued applicability at implementation.
- Final comparison-versus-no-match decision depends on independent UCR assessment, outside this audit/remediation preparation.

Verification and closure checks:

- One coherent adopted route totals 180 EC and 60 per study year; all choices and embedded requirements counted once.
- Record sources, years, route and delivery mode accurately; preserve prior access limitations in history.
- Close external-source remediation only after canonical fields and generated counselor outputs agree; keep ultimate UCR decision pending until separately assessed.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000098 — History (Geschiedenis)

Institution: Vrije Universiteit Amsterdam. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `external-programme-unresolved`; existing check date: 2026-09-26.

Existing substantive reason: The accessible current official VU prospectus is a thematic and partial course overview; it explicitly sends readers to the study guide for the complete programme. Individual VU 2026–27 course entries establish 60 EC of named components, but not the full compulsory sequence, the amount and restrictions of second-year free choice, the third-year minor/placement alternatives, or all third-year research-college credits. The applicable formal degree plan/OER is inaccessible to the available tools. Filling the other 120 EC or treating all displayed optional courses as mandatory would invent a 180-EC pathway. The UCR History response is academically plausible, but a fair lossless comparison must await a verified complete VU curriculum.

The adopted current OER now supplies the complete Dutch Geschiedenis/Algemeen route and its restrictions. The stored 60-EC subset remains valid partial evidence, but the current claim that a full official allocation is unavailable is no longer supported. Do not substitute History and International Studies or combine alternative research seminars.

Provenance: data/counselor/comparisons/cp-000098.json; source worksheet row(s) 105. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [VU Studiegids — Geschiedenis](https://studiegids.vu.nl/nl/Bachelor/2026-2027/geschiedenis) — Programme facts and linked current regulations; 2026–2027. The 180-EC programme has distinct Dutch Geschiedenis and English History and International Studies routes. The generic Dutch target must use the Dutch table.
- [OER Bachelor Geschiedenis 2026–2027](https://assets-us-01.kc-usercontent.com/f55d3574-6c6d-0002-e968-70643a2e365a/60718e0d-72f7-4581-85a0-a015b1d5063f/OER%2026-27%20BA%20Geschiedenis%20NL%2027.08.2026.pdf) — Annex, PDF pp. 22–23: Dutch trajectory and Algemeen third year; adoption statement p. 19; Adopted 2026–2027. Complete 180-EC Dutch general route: first year 60; second year 48 required plus 12 choice, with prior approval for other level-200 courses; third year 30 minor/approved abroad/placement choice plus 9 required research college, one of two 9-EC seminars, 3 colloquium and 9 thesis. A placement uses 12 EC plus 18 electives within the same 30-EC allowance. Regulations adopted 26 May 2026. Tables visually checked.

External credit structure: Stored total 60 EC is a supported partial subset. Current adopted Dutch general route now verifies 180 EC, with 12 second-year choice, 30 third-year choice, 9+9 research, 3 colloquium and 9 thesis.

Verified reconstruction for later external remediation (audit evidence only):

| Study year | Component | EC | Status / qualification |
|---|---|---:|---|
| 1 | De oorsprong van de geschiedenis: De globaliserende mediterrane wereld 3500 v.Chr.–1000 n.Chr. (L_GOBAGES114) | 9 | required |
| 1 | Modern Europa (L_GABAGES136) | 9 | required |
| 1 | Wereldgeschiedenis 1000–heden (L_GABAGES137) | 9 | required |
| 1 | Middeleeuws en Vroegmodern Europa (L_GABAGES138) | 9 | required |
| 1 | Academische vaardigheden voor historici (L_AABAGESACV) | 6 | required |
| 1 | Geschiedenis Schrijven (L_ETBAGES101) | 6 | required |
| 1 | Geschiedenis en Actualiteit (L_GABAGES126) | 6 | required |
| 1 | Key Texts in Philosophy (L_YABAALG008) | 6 | required |
| 2 | Religie en staatsvorming (L_GABAGES231) | 6 | required |
| 2 | Mondiale milieuvraagstukken (L_GABAGES233) | 6 | required |
| 2 | Capitalism and Inequality (L_GABAGES232) | 6 | restricted-choice; Selected period-1 option; other level-200 courses require prior approval. |
| 2 | Latin America in Modern History (L_GWBAGES214) | 6 | restricted-choice; Selected period-2 option; alternatives are not additional requirements. |
| 2 | Oral History (L_AABAGES223) | 3 | required |
| 2 | History by Numbers (L_AABAGES224) | 3 | required |
| 2 | Democratische revoluties (L_GABAGES235) | 6 | required |
| 2 | Onderzoekscollege 1 (L_GABAGES236) | 6 | required |
| 2 | Holocaust en Genocide (L_GCBAGES219) | 6 | required |
| 2 | Onderzoekscollege 2 (L_GABAGES238) | 6 | required |
| 2 | The Digital Historian (L_GABAGES240) | 6 | required |
| 3 | Minor / approved abroad / placement and electives | 30 | choice; Placement 12 plus electives 18 is one alternative within 30, not extra EC. |
| 3 | Onderzoekscollege Cultuur, Religie en Kennis 500–1800 (L_GABAGES317) | 9 | required |
| 3 | Research Seminar Global and Political History 1500–present (L_GABAGES318) | 9 | restricted-choice; One of this or Global Economic and Social History; never both. |
| 3 | Colloquium (L_GABAGESCOL) | 3 | required |
| 3 | Scriptie (L_GABAGESSCR) | 9 | required |

Total: **180 EC**; study-year totals **60 + 60 + 60**. Complete current adopted route, not a guarantee of unchanged future-year offerings for a new entrant.

Choice and source-context rules:

- Year-two 12 EC is preserved as two supported selections, not additional mandatory courses.
- Year-three 30-EC choice and alternative 9-EC seminar are counted once.
- Do not substitute English History and International Studies codes or a specialist Dutch third-year route.

Result: incorrect; required action: reassess-exception.

Incorrect concerns the current unavailable-credit basis, not the historical tool-access report or the ultimate UCR outcome.

Recommended follow-up: Expand the partial external reconstruction using the adopted Dutch general-route table and refresh its source context and exception rationale.

Unresolved factual question / historical limitation: The prior tools’ access limitations are preserved as provenance. No dated historical evidence establishes that a previously valid curriculum changed into the present one; incorrect refers only to the current unsupported description or unresolved-source basis, not the truth of the original access report. An outdated classification is not justified.

Implementation plan — **not implemented; audit only**:

- `data/counselor/comparisons/cp-000098.json`, fields: `comparator.components`, `comparator.primarySourceUrl`, `comparator.additionalSourceUrls`, `comparator.academicYear`, `comparator.sourceNotes`, `exception.reason`, `exception.curriculumContext`, `exception.checkedOn`. Use verified_external_structure in this audit as the source-backed reconstruction; preserve its route, choice and cohort qualifiers. Refresh obsolete current access claims. Reassess the formal exception after external reconstruction; do not automatically change recordStatus/type.

Dependencies:

- No remaining broad external research prerequisite for the current adopted route; verify continued applicability at implementation.
- Final comparison-versus-no-match decision depends on independent UCR assessment, outside this audit/remediation preparation.

Verification and closure checks:

- One coherent adopted route totals 180 EC and 60 per study year; all choices and embedded requirements counted once.
- Record sources, years, route and delivery mode accurately; preserve prior access limitations in history.
- Close external-source remediation only after canonical fields and generated counselor outputs agree; keep ultimate UCR decision pending until separately assessed.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000099 — Health and Life Sciences (Gezondheid en Leven)

Institution: Vrije Universiteit Amsterdam. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `external-programme-unresolved`; existing check date: 2026-09-26.

Existing substantive reason: For a Fall 2026 entrant the new curriculum has no old specialisations. The adopted 2026–27 OER gives exact first-year and minimum minor credits, but its detailed year-two and thesis-credit tables concern the outgoing specialisations. The current new-curriculum explanation names the six-plus-four second-year structure and third-year research and communication work without their applicable EC and full choice allocation. Importing the old 24-EC or 18-EC thesis weights, or treating both members of each restricted choice pair as compulsory, would misstate the 2026-cohort 180-EC route. A lossless external comparison therefore remains unresolved.

Fresh current OER and revision document corroborate the unresolved future-cohort credit gap: only first-year 60 and minimum minor 30 are securely allocated. Six-plus-four year-two positions and third-year research/communication are qualitative, not exact new-cohort EC. Independently, official Dutch instruction confirms a registry language error: ENG must be corrected to NLD. Correcting identity will not resolve the curriculum exception.

Provenance: data/counselor/comparisons/cp-000099.json; source worksheet row(s) 106. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [VU Studiegids — Gezondheid en Leven](https://studiegids.vu.nl/nl/Bachelor/2026-2027/gezondheid-en-leven) — Programme facts and curriculum change notice; 2026–2027. Current programme is Dutch, full-time and 180 EC. The 2026 entrants follow a new curriculum rather than the old BMW/DGZ/KW major routes. The registry ENG language conflicts with official programme facts.
- [OER Bachelor Gezondheid en Leven 2026–2027](https://assets-us-01.kc-usercontent.com/f55d3574-6c6d-0002-e968-70643a2e365a/ede76ee3-4e16-41c8-8ccc-ce484951eac1/B%20Gezondheid%20en%20Leven%20OER%202026-2027.pdf) — Articles 10.2/10.4, PDF pp. 15/18; 11.3, pp. 19–22; 12.1, pp. 22–23; Adopted 2026–2027. No formal specialisations apply to 2026 entrants; instruction language is Dutch. Ten first-year units total 60 EC. Old major/thesis tables do not establish new-cohort future requirements. Minimum minor/free space is 30 EC with level and approval conditions; old thesis alternatives of 18 or 24 EC cannot be borrowed.
- [Nieuw curriculum bachelor Gezondheid en Leven](https://assets-eu-01.kc-usercontent.com/ff31ad68-341e-015e-fb52-24df7a00ecea/f4d7310d-6aba-45d8-aa25-ab026e822f74/Toelichting%20Curriculumherziening%20website%20G_L.pdf) — PDF pp. 1–2 and 4–6; year diagram visually checked; Prospective curriculum for September 2026 entrants; undated PDF linked from current official prospectus. New curriculum begins September 2026. Year two has six mandatory courses and four choice positions, including one from Genomica/Kwalitatief onderzoek and one from Anatomie en fysiologie 2/Systeemtransformatie. Year three has minor, biomedical or societal research and science communication, with societal research preparation. The diagram and descriptions supply no exact EC; the diagram and prose use different preparation-course labels.

External credit structure: Stored total 90 EC remains a supported subset: first year 60 plus minimum minor 30. New-cohort later weights remain unresolved; no outgoing-track weights are substituted.

Result: still-unresolved; required action: correct-registry-and-reprocess.

Secondary attribute finding(s):

- normalized registry language: incorrect; stored ["ENG"], verified ["NLD"]. Separate closure: Future-cohort external curriculum remains unresolved.

Recommended follow-up: Correct normalized language to NLD through a documented registry correction, preserve the raw ENG provenance, refresh affected counselor metadata, and keep the external curriculum unresolved until applicable new-cohort credits are published.

Unresolved factual question / historical limitation: Obtain the 2026-entry year-two/year-three adopted credit and choice allocation, including preparation for societal research, research project/thesis and science communication; resolve differing preparation-course labels before assigning weights.

Implementation plan — **not implemented; audit only**:

- `data/registry/programmes.csv`, fields: `languages_json`, `corrected_attributes_json`, `official_source_ids_json`, `official_source_urls_json`, `normalization_basis`. For cp-000099 set normalized languages_json=["NLD"] using a documented researched correction and the current OER/guide. Preserve permanent ID, raw source rows and raw ENG offering provenance.
- `data/registry/resolution_decisions.csv; data/registry/resolution_sources.csv`, fields: `documented post-build correction and official evidence`. Record the language override without inventing an existing ambiguity case or rewriting immutable source/ambiguity tables; use the repository correction workflow and retain reproducible provenance.
- `data/counselor/comparisons/cp-000099.json`, fields: `programmeProvider.languages`, `comparator.sourceNotes`, `exception.reason`, `exception.curriculumContext`, `exception.checkedOn`. Refresh affected identity/context after registry correction; retain external-programme-unresolved and supported 90-EC subset pending current-cohort requirements.

Dependencies:

- Exact new-cohort year-two/year-three credits and choice rules remain unpublished in the retrieved current authority.
- A researched post-build correction must be retained by any registry rebuild; choose its existing workflow before implementation.

Verification and closure checks:

- Normalized language is NLD; canonical and generated identity agree while immutable ENG source provenance remains.
- Language correction is closed independently; curriculum exception remains open until a source-backed 180-EC route is established.
- Do not borrow 18/24-EC outgoing-track thesis weights or count both restricted-pair alternatives.

Research trigger: Current applicable new-cohort OER/degree table or official clarification of full credit and choice allocation.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000100 — Health Sciences (Gezondheidswetenschappen)

Institution: Vrije Universiteit Amsterdam. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `external-programme-unresolved`; existing check date: 2026-09-26.

Existing substantive reason: The new curriculum was phased in from 2025–26. For a Fall 2026 entrant, the 2026–27 OER securely specifies 120 EC across the first two years and at least 30 EC of third-year free choice, but its current third-year table (6 EC Epidemiologie & Biostatistiek III and 18 EC Bachelorstage) does not establish the full future new-cohort route. The same OER names Methodologie 5 for the new cohort with its code still unknown, while the prospective page describes professional work, research placement and bachelor thesis without applicable component credits. Even adding the two listed old-cohort third-year courses to the supported 150 EC reaches only 174 EC. Assigning the missing credits to a third-year elective, methodology, professional module or thesis by subtraction would invent the formal pathway.

Current formal evidence still supports 120 EC across years one/two plus minimum 30 minor. Outgoing-cohort 6+18 third-year units and optional courses do not establish the new entrant’s future third year. Methodologie 5, professional preparation and placement/thesis cannot receive weights inferred by subtraction.

Provenance: data/counselor/comparisons/cp-000100.json; source worksheet row(s) 107. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [VU Studiegids — Gezondheidswetenschappen](https://studiegids.vu.nl/nl/Bachelor/2026-2027/gezondheidswetenschappen) — Programme facts and linked current OER; 2026–2027. Dutch, full-time, 180-EC programme. Its new curriculum is being phased in, so a current third-year teaching table cannot automatically be assigned to a new entrant.
- [OER Bachelor Gezondheidswetenschappen 2026–2027](https://assets-us-01.kc-usercontent.com/f55d3574-6c6d-0002-e968-70643a2e365a/4d43408f-790d-4f02-94d4-8aa29ae358d5/B%20Gezondheidswetenschappen%20OER%202026-2027.pdf) — Article 9.1, PDF p. 13; Articles 11.3–12.1, pp. 19–22; Article 15.2, p. 22; Adopted 2026–2027. First two years total 120 EC, including two restricted 6-EC second-year choices. Minimum minor/free choice is 30 EC. The new curriculum starts in 2025–2026; Methodologie 5 is named with code unknown. Currently listed old third-year Epidemiologie & Biostatistiek III (6) and Bachelorstage (18) do not resolve the applicable future new-cohort allocation.
- [Gezondheidswetenschappen — inhoud](https://vu.nl/nl/onderwijs/bachelor/gezondheidswetenschappen/inhoud) — Third-year description; Current prospective undated page. Prospective third year includes a minor, professional preparation and a three-month research placement/bachelor thesis, without exact component EC. These qualitative descriptions do not fill the unresolved 30-EC later requirement by subtraction.

External credit structure: Stored total 150 EC remains a supported subset: first two years 120 plus minimum minor 30. The old-cohort 24-EC third-year listing is not a complete applicable new-cohort remainder.

Result: still-unresolved; required action: research-again-later.

Recommended follow-up: Retain the supported 150-EC subset and explicit exception; revisit only when applicable new-cohort year-three requirements or an official clarification resolves all credits and choice rules.

Unresolved factual question / historical limitation: What are the applicable new-cohort credits and requirements for Methodologie 5, professional preparation, placement/thesis and the remaining third-year structure?

Implementation plan — **not implemented; audit only**:

- `data/counselor/comparisons/cp-000100.json`, fields: `comparator.components`, `comparator.sourceNotes`, `comparator.academicYear`, `exception.reason`, `exception.curriculumContext`, `exception.checkedOn`. Retain the current 150-EC supported subset; update only documented source context now. Add later components only when an applicable new-cohort table resolves all requirements and weights.

Dependencies:

- Current new-cohort third-year adopted allocation or university clarification.

Verification and closure checks:

- All added requirements apply to the same cohort; methods, professional work and stage/thesis are counted once.
- Complete route reaches 180 EC from evidence, not subtraction; close external reconstruction then reassess exception.

Research trigger: Publication of the applicable new-cohort year-three credit table, especially Methodologie 5 and placement/thesis.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000119 — Bachelor Theologie en Religiewetenschappen

Institution: Vrije Universiteit Amsterdam. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `external-programme-unresolved`; existing check date: 2026-09-27.

Existing substantive reason: The exact EC weights and compulsory-versus-elective status of every curriculum component in the selected Religie en Levensbeschouwing route cannot be verified from any source accessible to available tools. VU's own current regulations page states the formal OER/TER is published only inside the dynamic studiegids.vu.nl study-guide application, which returned no extractable curriculum content to available retrieval tools, and the only standalone official OER document discoverable through reasonable search (2017-2018) predates the current three-route structure -- it still treats Islam as an elective minor rather than a parallel afstudeerrichting -- and does not reliably describe the current curriculum. A complete 180-EC comparator would require inventing credit weights and compulsory/elective status that no current or formally adopted source supports, so a canonical comparison cannot be made yet.

Current adopted regulations now expose the selected comparative Religie en Levensbeschouwing route, its full 180 EC, alternatives and six-year part-time pacing. The current credit-access rationale is no longer supported. Previously used prospectus course lists describe the programme starting in 2027, so they cannot substitute for the adopted 2026–2027 route.

Provenance: data/counselor/comparisons/cp-000119.json; source worksheet row(s) 127. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [VU Studiegids — Theologie en Religiewetenschappen](https://studiegids.vu.nl/nl/Bachelor/2026-2027/theologie-en-religiewetenschappen) — Programme facts and linked current OER; 2026–2027. 180-EC programme offered full-time and part-time, with Christian theology, Islam and comparative religious-studies directions. The selected Religie en Levensbeschouwing direction is supported by the current regulations.
- [OER Theologie en Religiewetenschappen 2026–2027](https://assets-us-01.kc-usercontent.com/f55d3574-6c6d-0002-e968-70643a2e365a/110b4a0f-1fe1-40b1-a797-60a6aab14bd4/OER%2026-27%20B%20TRS%20NL.pdf) — Articles 10.4 and 11–12, PDF pp. 16–18; Annex 1, physical PDF p. 26 (appendix printed 5/34); Adopted 2026–2027. Religie en Levensbeschouwing table defines 60+60+60 EC, with part-time pacing over six years. Ten 6-EC first-year units; ten 6-EC second-year positions with explicit choices; third year 30 minor plus two 6-EC research labs, two 6-EC profile units and 6 thesis. Minor/free choice needs approval and level rules. Initial instruction is Dutch; selected third year is English. Visual inspection confirms table position, alternatives and credits.
- [Zingeving, geestelijke verzorging en samenleving — inhoud](https://vu.nl/nl/onderwijs/bachelor/theologie-en-religiewetenschappen/traject/zingeving-geestelijke-verzorging-en-samenleving/inhoud) — Programme-start label above the three-year course overview; Prospective September 2027 route. The advertised qualitative course lists explicitly concern a programme starting in 2027. They are not the current 2026–2027 formal curriculum and cannot replace its credits or compulsory/choice structure.

External credit structure: Stored total 0 EC was intentionally empty. Current adopted comparative route now verifies 60+60+60=180, including 30 minor, two 6-EC research labs and 6 thesis; part-time pace changes duration, not total.

Verified reconstruction for later external remediation (audit evidence only):

| Study year | Component | EC | Status / qualification |
|---|---|---:|---|
| 1 | Research Lab 1: Onderzoek en Argumentatie in Theologie en Religiewetenschap (G_BATRSCC105) | 6 | required |
| 1 | World Religions (G_BATRSCC101) | 6 | required |
| 1 | Inleiding Religiewetenschappen (G_BATRSPC131) | 6 | required |
| 1 | Hedendaagse religieuze vraagstukken in historisch perspectief (G_BATRSCC106) | 6 | required |
| 1 | Geschiedenis van de Wereldfilosofie (G_BATRSCC107) | 6 | required |
| 1 | Geschiedenis van het Christendom (G_BATRSPC125) | 6 | required |
| 1 | Religious Myths and Rituals (G_BATRSPC105) | 6 | required |
| 1 | Judaism (G_BATRSPC111) | 6 | required |
| 1 | Hinduism (G_BATRSPC110) | 6 | required |
| 1 | Islam (G_BATRSPC116) | 6 | required |
| 2 | Psychology of Religion (G_BATRSAL058) | 6 | choice; Shown blue choice position instantiated with the displayed course; not universal common core. |
| 2 | Interreligieuze Hermeneutiek (G_BATRSCC204) | 6 | required |
| 2 | Religion, Violence and Fundamentalism (G_BATRSAL084) | 6 | restricted-choice; One of three displayed period-2 options. |
| 2 | Sociale wetenschappen (G_BATRSCC205) | 6 | required |
| 2 | Religions and Gender (G_BATRSAL054) | 6 | restricted-choice; Alternative: Geestelijke verzorging bij sterven en rouw. |
| 2 | Godsdienstfilosofie (G_BATRSCC206) | 6 | required |
| 2 | Geschiedenis van de Islam na 1800 (G_BATRSPC219) | 6 | restricted-choice; Alternative: Communicatie in Geestelijke Zorg. |
| 2 | Anthropology of Religion (G_BATRSPC205) | 6 | required |
| 2 | Islamitische filosofie (G_BATRSPC207) | 6 | restricted-choice; One of three displayed period-5 options. |
| 2 | Religions, Media and Popular Culture (G_BATRSPC214) | 6 | required |
| 3 | Approved minor/free-choice semester | 30 | choice; Five 6-EC positions; approved free courses or 12-EC placement plus 18 courses; level conditions apply. |
| 3 | Research Lab: Preparation Thesis (G_BATRSCC301) | 6 | required |
| 3 | Interreligious Relations: Mutual Perceptions and Interactions (G_BATRSPC301) | 6 | required |
| 3 | Research Lab: Exercise in Analytic Methodologies (G_BATRSCC302) | 6 | required |
| 3 | Comparative Religious Ethics (G_BATRSPC303) | 6 | required |
| 3 | Thesis (G_BATRSCCSCR) | 6 | required |

Total: **180 EC**; study-year totals **60 + 60 + 60**. Current adopted curriculum only; part-time pacing is six years in this table, not a distinct 360-EC route or a future-2027 reconstruction.

Choice and source-context rules:

- Preserve comparative general-route selection, independent of UCR fit.
- Part-time Annex table splits each 60-EC study year over two years; total remains 180 EC.
- Document the blue choice position and each OR selection separately; count no alternatives twice.
- Third-year minor/free choice requires approval and at least 12 EC level 300 for individually selected courses.
- Third-year instruction is English within the predominantly Dutch programme; prospective 2027 course lists are separate.

Result: incorrect; required action: reassess-exception.

Incorrect concerns the current unavailable-credit basis, not the historical tool-access report or the ultimate UCR outcome.

Recommended follow-up: Build the selected current comparative route from Annex 1, preserve part-time identity, document choice instantiations and update sources/year context and exception rationale.

Unresolved factual question / historical limitation: The prior tools’ access limitations are preserved as provenance. No dated historical evidence establishes that a previously valid curriculum changed into the present one; incorrect refers only to the current unsupported description or unresolved-source basis, not the truth of the original access report. An outdated classification is not justified.

Implementation plan — **not implemented; audit only**:

- `data/counselor/comparisons/cp-000119.json`, fields: `comparator.components`, `comparator.primarySourceUrl`, `comparator.additionalSourceUrls`, `comparator.academicYear`, `comparator.sourceNotes`, `exception.reason`, `exception.curriculumContext`, `exception.checkedOn`. Use verified_external_structure in this audit as the source-backed reconstruction; preserve its route, choice and cohort qualifiers. Refresh obsolete current access claims. Reassess the formal exception after external reconstruction; do not automatically change recordStatus/type.

Dependencies:

- No remaining broad external research prerequisite for the current adopted route; verify continued applicability at implementation.
- Final comparison-versus-no-match decision depends on independent UCR assessment, outside this audit/remediation preparation.

Verification and closure checks:

- One coherent adopted route totals 180 EC and 60 per study year; all choices and embedded requirements counted once.
- Record sources, years, route and delivery mode accurately; preserve prior access limitations in history.
- Close external-source remediation only after canonical fields and generated counselor outputs agree; keep ultimate UCR decision pending until separately assessed.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000134 — Bachelor Fiscal Economics

Institution: Maastricht University. Audit scope: Normalized identity/lifecycle conflict and current teach-out rules; no UCR feasibility assessment.

Existing formal type: `registry-exception`; existing check date: 2026-10-01.

Existing substantive reason: The normalized target is an active 180-EC Maastricht University bachelor, but the current official SBE regulations (2026-2027, article 16.8) state that the Bachelor Fiscal Economics is being phased out: no new education is offered beyond year-3 repeat education in 2026-2027, only examinations remain through 2027-2028, and degrees can no longer be issued from 1 November 2028. The regulations contain no current first- or second-year curriculum, so no current 180-EC pathway for a student starting in 2026 exists to reconstruct, and the registry's active, production-eligible status conflicts with that evidence. The reachable sources establish only a 60-EC third-year outline, and encoding it as a full programme or guessing the missing 120 EC would invent components. The target's lifecycle status must be reviewed against the university's current programme register before any UCR comparison is attempted.

The current adopted teach-out rules confirm the registry exception: no new 2026-entry route can be reconstructed. Third-year repeat teaching and later examinations/degree issuance remain available to existing students. The normalized active/eligible target therefore conflicts with new-entrant production scope; the existing exception correctly identifies that conflict. Partly Dutch/partly English instruction also contradicts the normalized ENG-only language description.

Provenance: data/counselor/comparisons/cp-000134.json; source worksheet row(s) 145. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [SBE Bachelor EER 2026–2027 — Fiscal Economics](https://www.maastrichtuniversity.nl/file/sbe-bsc-eer-2026-2027pdf) — Article 16.8, printed pp. 60–61 (PDF pp. 68–69); Appendix I, Article 17, printed pp. 100–102; Adopted 2026–2027. Last third-year repeat education is in 2026–2027; examinations only through 2027–2028; no degree certificates from 1 November 2028. No current new-intake first/second-year route is specified. The remaining third-year outline is 26 required taught + 8 thesis + 26 listed electives/study abroad = 60 EC. Teaching/examination language is partly English and partly Dutch; ENG-only provenance is incomplete.

External credit structure: Stored 60 EC is a third-year teach-out outline only: four 6.5-EC requirements plus 8 thesis and 26 elective/abroad. No current new-intake 180-EC route is established.

Result: confirmed; required action: correct-registry-and-reprocess.

Secondary attribute finding(s):

- normalized registry language: incorrect; stored ["ENG"], verified ["ENG", "NLD"]. Separate closure: Confirmed lifecycle conflict and teach-out correction.

Recommended follow-up: Record a researched lifecycle correction using the existing teach-out-only convention, set production_eligible=false and clear production_order, retain the permanent ID/history and partial third-year evidence, and refresh affected production inventories. Correct language metadata to include NLD and ENG with official provenance.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

Implementation plan — **not implemented; audit only**:

- `data/registry/programmes.csv`, fields: `current_status`, `production_eligible`, `production_order`, `languages_json`, `corrected_attributes_json`, `official_source_ids_json`, `official_source_urls_json`. For cp-000134 propose current_status="teach-out-only", production_eligible=false, production_order blank, languages_json=["ENG","NLD"]. Document no-new-entry scope, last teaching 2026–2027, last examinations 2027–2028 and certificate cutoff 2028-11-01. Retain permanent ID, standard type, 180-EC historical degree identity and all crosswalk provenance.
- `data/registry/resolution_decisions.csv; data/registry/resolution_sources.csv`, fields: `documented post-build lifecycle/language correction`. Use existing teach-out-only precedent with researched official evidence; preserve immutable source and ambiguity baselines and ensure rebuild retains the correction.
- `data/counselor/comparisons/cp-000134.json; data/counselor/review-programmes.json; other affected generated counselor inventories`, fields: `scope membership`, `exception source context`, `review/coverage counts`. Reconcile canonical-record handling for the newly out-of-scope permanent target with repository scope rules. Preserve historical registry/exception evidence; regenerate inventories so it is no longer a new-entrant production target. Do not construct a 180-EC intake route from the 60-EC teach-out table.

Dependencies:

- Confirm authoritative lifecycle/new-enrolment record or record why adopted EER controls; reconcile any register conflict before final lifecycle correction.
- Choose repository-supported retention/archive treatment for an existing canonical record that leaves scope, without losing its provenance.

Verification and closure checks:

- New-entrant production excludes cp-000134; history and crosswalks retain the same permanent ID.
- Teach-out is not mislabeled already nonexistent: existing-student teaching, examinations and certificate cutoff remain distinct.
- Registry rebuild and generated inventories reproduce eligibility/order changes and reconcile counts; language includes both official languages.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000140 — Circular Engineering

Institution: Maastricht University. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-03.

Existing substantive reason: The defining curriculum of the selected route is a chemical-engineering sequence built on physics and chemistry: Fundamentals of Engineering, Chemistry and Chemical Engineering, and Thermodynamics and Engineering Physics in the compulsory first year, physics, electronics, chemistry and biology laboratory skills, fluid mechanics and heat and mass transfer in year 2, and in year 3 chemical engineering thermodynamics and kinetics, separation processes, reactor engineering, chemical plant design, process design and control, unit-operations and industrial-process-design skills and a 25-EC engineering thesis. UCR offers circular-economy, life-cycle, energy and environmental-engineering-adjacent courses, a mathematics and numerical-methods line and biochemistry and cell-biology courses, but no physics, chemistry sequence, thermodynamics, transport phenomena, reactor or process engineering, mechanics or engineering design. A 24-course programme would be a sustainability-and-mathematics programme with a small circular-economy core padded with unrelated life-science or computing courses, and it would not reproduce the programme's engineering substance; the unmatched components include essentially all of the 25-EC concentration course sequence, the engineering physics and chemistry core and the thesis. The comparison would have to present adjacent sustainability courses as substitutes for engineering content that UCR does not teach.

Current adopted regulations corroborate the complete selected Circular Chemical Engineering route, engineering/science laboratories and design/thesis core. Second-year restricted choices form a coherent period-specific instantiation; their subject content is not a universal requirement for every concentration. No open allowance is invented.

Provenance: data/counselor/comparisons/cp-000140.json; source worksheet row(s) 152. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [EER BSc Circular Engineering 2026–2027](https://www.maastrichtuniversity.nl/sites/default/files/2026-09/EER%20BSC%20CE%2026-27.pdf) — Articles 3.5–3.9, PDF pp. 9–10; Appendix I, pp. 22–23; Adopted 2026–2027. 180 EC: first year 40 courses + 10 skills + 10 projects; second year 40 restricted course selections + 10 restricted skills + 10 projects; third year 5 common + 25 concentration + 5 skills + 25 thesis. The stored Chemical Engineering concentration and period-specific second-year selections are coherent. Field-specific electives are instantiated choices, not common requirements across all routes.

External credit structure: Stored and adopted selected route total 180 EC. Restricted year-two and concentration selections remain distinct from programme-wide common requirements.

Result: confirmed; required action: none.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000149 — General Cultural Studies (Algemene Cultuurwetenschappen)

Institution: Open Universiteit. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `external-programme-unresolved`; existing check date: 2026-10-06.

Existing substantive reason: Current official OU sources do not establish a consistent 180-EC pathway for 2026-27. The study guide's component table totals 185 EC and contradicts both the 60-EC propedeuse and the six portal-type courses in the annual schedule; the split of the 45 EC left between choice block and free space, the membership of the theme blocks and the make-up of the 15-EC skills block are not stated, and the programme-specific OER that would resolve them was not accessible. Fixing a 180-EC route would require guessing which figures are correct, so no canonical comparison is published.

Fresh current guide and programme facts retain the 50-versus-60, 135-versus-120 and 185-versus-180 conflicts. Newly located programme-specific regulations explain a coherent 2025–2026 allocation, but are explicitly older and cannot control the conflicting 2026–2027 guide. The current skills-course change prevents assuming unchanged membership. Broad research can now be narrowed to the current controlling document.

Provenance: data/counselor/comparisons/cp-000149.json; source worksheet row(s) 162. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [Bachelor Algemene Cultuurwetenschappen 2026–2027](https://www.ou.nl/en/-/bcw-2026-2027_bachelor-algemene-cultuurwetenschappen) — Degree facts and structure; 2026–2027. The standard Dutch part-time degree is 180 EC, with 60-EC propedeuse and 120-EC postpropedeuse. The separate Open Bachelor is not this target.
- [Studiegids Algemene Cultuurwetenschappen 2026–2027](https://www.ou.nl/digitaldownloads/BD476.pdf) — PDF p. 7 diagram; course/annual schedules; p. 43 regulations notice; 2026–2027. Diagram gives propedeuse 50 EC and postpropedeuse 135 EC, totalling 185 rather than the stated 180. Annual schedule gives twelve 5-EC propedeuse courses, including six portal courses rather than four. Choice/skills allocation therefore needs controlling current programme-specific regulations, not arithmetic repair.
- [OER — programme-specific Algemene Cultuurwetenschappen](https://vraagenantwoord.ou.nl/privatedata/docs/OER_WO_bacheloropleiding_Algemene_cultuurwetenschappen.pdf) — Both pages; explicit academic-year header; 2025–2026; older official evidence, not current authority. 2025–2026 regulations reconstruct 60 + 45 themes + 15 restricted choice + 30 free + 15 skills + 15 graduation = 180 EC. This narrows the current contradiction but does not control 2026–2027. Current guide changes a skills-course label/code; unchanged future requirements cannot be assumed.
- [OU documents / questions portal](https://www.ou.nl/documenten) — Guide-directed documents URL and public redirect; Access checked 7 October 2026; current programme-specific OER not retrieved. Current guide directs readers here for 2026–2027 OER and implementation rules. Retrieval redirects to the FAQ without exposing the current programme-specific document; reasonable official-domain searches retrieved only the older programme-specific OER.

External credit structure: Stored total 0 EC is intentional. Current schematic totals 185, conflicts with 60+120 degree facts, and cannot be repaired using older 2025–2026 rules without current authority.

Result: still-unresolved; required action: research-again-later.

Recommended follow-up: Obtain the 2026–2027 programme-specific OER/implementation schedule or a university clarification; reconcile the current portal, theme, choice, free-space, skills and graduation allocation before supplying any complete components.

Unresolved factual question / historical limitation: Does the current controlling regulation retain 15 EC restricted choice, 30 EC free space and the older skills allocation, and which current courses belong to each block? Resolve the six-versus-four portal count and the erroneous schematic totals.

Implementation plan — **not implemented; audit only**:

- `data/counselor/comparisons/cp-000149.json`, fields: `comparator.sourceNotes`, `comparator.additionalSourceUrls`, `comparator.components`, `exception.reason`, `exception.curriculumContext`, `exception.checkedOn`. Add the newly found 2025–2026 programme-specific OER only as older diagnostic evidence. Keep current reconstruction unresolved. When the current controlling document is available, build its exact block membership/weights and explain the 2026–2027 guide errors.

Dependencies:

- Current 2026–2027 programme-specific OER/implementation schedule or official clarification that controls the conflicting guide.

Verification and closure checks:

- Propedeuse 60 plus postpropedeuse 120 from current authority; portal count, theme membership, restricted choice, free space, skills and graduation reconcile.
- 2025–2026 rules and separate Open Bachelor are not silently substituted.
- Resolve current skills-course change and count 15-EC graduation once; close external reconstruction then reassess exception.

Research trigger: Accessible current programme-specific regulation or explicit university clarification of the guide/table contradictions.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000156 — Theologie

Institution: Protestantse Theologische Universiteit. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-09-29.

Existing substantive reason: The programme's defining academic identity is sustained Protestant Christian theology and theology-specific method: systematic, historical, practical and biblical theology; Greek and Hebrew; exegesis in the source languages; theology, aesthetics and culture; Reformation history; Judaism and Islam in theological context; personal worldview formation; and a 15-EC final theological project. Only the 30-EC minor is broadly open. UCR offers adjacent philosophy, ethics, history, sociology, politics, literature, art history and cultural analysis, but no sustained theology, scripture, source-language, exegesis or pastoral curriculum. A 24-course UCR schedule assembled from neighbouring humanities and social sciences would erase the target's defining theological sequence and would not be a defensible substantive match.

The selected 180-EC language route and sustained theological core are supported. However, exception.curriculumContext incorrectly universalises biblical languages and exegesis across all available routes. The OER permits language-free replacements, already acknowledged in comparator.sourceNotes. The current reason/context must distinguish the selected route from common requirements and the ministerial-master exit profile.

Provenance: data/counselor/comparisons/cp-000156.json; source worksheet row(s) 169. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

rc-0016 fills Dutch/Utrecht/180-EC metadata; fresh authoritative evidence corroborates that correction. Stale Groningen interests remain provenance only.

Current official sources (checked 7 October 2026):

- [PThU OER Bachelor Theologie 2026–2027](https://www.pthu.nl/over-pthu/organisatie/regelingen-en-rechtspositie/oer-bachelor-theologie-2026-2027.pdf) — Annex 2, PDF pp. 45–46 and alternative-path footnotes; Adopted 9 July 2026; effective 1 September 2026. Selected language route totals 180 EC: first year 60; second year 24 track + 15 Greek + 15 Hebrew + 6 worldview; third year 30 minor + 9 exegesis + 6 theology/media + 15 thesis. Footnotes allow replacing languages with four additional track courses and Interreligious Practices, and exegesis with an unused track unit plus a 3-EC recent-publication unit. Languages/exegesis are required for the ministerial-master exit profile, not every permitted bachelor route.
- [PThU Bachelor Theologie](https://www.pthu.nl/onderwijs/bachelor/theologie-utrecht/) — Current programme location and degree facts; Current undated programme page. The authoritative target is the current Utrecht bachelor; old Groningen partnership interests do not override its identity. Registry decision rc-0016 fills the same Dutch, Utrecht, 180-EC metadata.

External credit structure: Stored selected route totals 180 EC and remains valid. The error is universalising route-dependent language/exegesis content, not component arithmetic.

Result: incorrect; required action: reassess-exception.

Incorrect concerns the universal language/exegesis claim. The selected route and theological core are supported; the ultimate UCR decision was not assessed.

Recommended follow-up: Correct the universal language/exegesis claim while preserving the valid selected route and its 180 EC. Describe the documented replacement pathway and restrict Greek/Hebrew/exegesis claims to the selected or ministerial-profile route; reassess the exception on that corrected basis.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

Implementation plan — **not implemented; audit only**:

- `data/counselor/comparisons/cp-000156.json`, fields: `exception.curriculumContext`, `exception.reason`, `exception.checkedOn`, `comparator.sourceNotes`. Replace the universal language/exegesis statement with selected-language-route qualification. Explain permitted replacements and ministerial-master exit-profile requirements. Retain supported 180-EC components, neutral Systematic Theology track choice and Utrecht identity; sourceNotes already acknowledges the alternative.

Dependencies:

- No external-source prerequisite; final UCR feasibility decision remains a separate stage-two task.

Verification and closure checks:

- Context/reason/sourceNotes agree that Greek, Hebrew and source-language exegesis are route-dependent.
- Replacement pathway is described accurately and not stacked onto the 180-EC selected route.
- Close factual narrative correction when canonical and generated narratives agree; retain UCR reassessment pending.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000159 — Archaeology

Institution: University of Groningen. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-09-29.

Existing substantive reason: The Groningen programme devotes 120 EC in its first two years to archaeology and then adds archaeological theory, data analysis, research design and a 10-EC archaeology thesis. Required study spans Greek and Roman, north-west European and Arctic archaeology; material culture, conservation and archaeometry; GIS and geoarchaeology; archaeobotany, zooarchaeology and human osteoarchaeology; and two credited fieldwork sequences. UCR has a small but valuable archaeology and heritage group—Introduction to World Archaeology, Greek Archaeology, and Heritage & Ancient Democracy—but no supervised excavation sequence, archaeological-materials or conservation laboratory sequence, bioarchaeology sequence, GIS/geoarchaeology sequence or archaeology thesis. Filling 24 places mainly with history, art, environmental science and generic methods would present neighbouring disciplines as an Archaeology bachelor. No defensible closest 24-course UCR programme can therefore be formed.

Current official tables corroborate the complete archaeology route, compulsory fieldwork and material/bioarchaeological methods. Genuine minor and IMPACT choices remain distinct; regional module selections do not constitute separate formal degree routes. The defining external basis is supported.

Provenance: data/counselor/comparisons/cp-000159.json; source worksheet row(s) 172. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [RUG Bachelor Archaeology](https://www.rug.nl/bachelors/archaeology/?lang=en) — Programme facts and all three-year curriculum tables; Current programme page; no separate academic-year label on curriculum table. Complete 180-EC programme: first/second-year archaeology each 60 EC; third year minor 30, theory/data/research design 10, restricted IMPACT choice 10 and thesis 10. Required first/second-year fieldwork, material/conservation, GIS/geoarchaeology and bioarchaeology remain supported. Regional selections within modules are not separate degree routes.

External credit structure: Stored complete route totals 180 EC; current table supports 60+60+30+10+10+10 and keeps minor/IMPACT choices separate.

Result: confirmed; required action: none.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

## Cumulative findings after batch 6

| Finding | Count |
|---|---:|
| confirmed | 47 |
| incorrect | 9 |
| outdated | 0 |
| still-unresolved | 4 |

| Required action | Count |
|---|---:|
| none | 42 |
| reprocess-as-comparison | 0 |
| reassess-exception | 11 |
| correct-registry-and-reprocess | 4 |
| research-again-later | 3 |

## Batch 6 findings

Eight findings are confirmed and two are incorrect within the stated factual scope. CP175 needs a semester-specific bachelor-project annotation correction: preparation in 3.1, project conduct in 3.2, with credits unchanged. CP198 incorrectly states three formal routes where the current regulation defines two. CP199’s existing registry-exception is confirmed: it duplicates the current Dutch track already represented by CP198 through documented successor normalization. CP198 and CP199 require one coordinated registry correction, counted as two affected cases rather than two independent merges. No case is classified as outdated or externally unresolved in this batch.

All ten selected external pathways are supported at 180 EC. Confirmation applies to external requirements and identity only; existing UCR claims remain provenance and await stage two. Actionable entries include field-level changes, dependencies and closure checks. The proposed surviving Dutch owner is CP198; alias/history representation and canonical treatment must use the repository-supported model before implementation. All plans remain unimplemented.

| ID | Programme | Formal type | Finding | Required action |
|---|---|---|---|---|
| cp-000171 | BA European Languages and Cultures — German major, European Language and Society profile | no-defensible-ucr-match | confirmed | none |
| cp-000172 | Pharmacy | no-defensible-ucr-match | confirmed | none |
| cp-000174 | Frisian Language and Culture | no-defensible-ucr-match | confirmed | none |
| cp-000175 | Medicine | no-defensible-ucr-match | incorrect | reassess-exception |
| cp-000179 | Griekse en Latijnse Taal en Cultuur (Classics) | no-defensible-ucr-match | confirmed | none |
| cp-000192 | Bachelor Life Science and Technology | no-defensible-ucr-match | confirmed | none |
| cp-000194 | Middle Eastern Studies | no-defensible-ucr-match | confirmed | none |
| cp-000196 | Physics | no-defensible-ucr-match | confirmed | none |
| cp-000198 | Dutch Languages and Cultures — Dutch Language and Culture | no-defensible-ucr-match | incorrect | correct-registry-and-reprocess |
| cp-000199 | Dutch Language and Culture — track within Dutch Languages and Cultures | registry-exception | confirmed | correct-registry-and-reprocess |

## Batch 6 evidence and implementation plans

### cp-000171 — BA European Languages and Cultures — German major, European Language and Society profile

Institution: University of Groningen. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-03.

Existing substantive reason: The Groningen programme is defined by cumulative proficiency in a chosen European language and by language-specific study through that language. The neutral pathway contains 30 EC of staged German proficiency, 15 EC of German language-specific work across language and society, culture and literature, and politics and society, a further 10-EC interdisciplinary German module, and a thesis grounded in the selected language and profile. UCR's current catalogue contains no German course and no sustained sequence in any European language comparable to this requirement. Its single introductory Dutch course does not create a major-language pathway. UCR literature, media, history, politics, sociology and communication courses can support comparative European questions, but they cannot supply the language competence on which the defining profile and language-specific modules depend. A 24-course response would therefore be a broad European humanities and social-science programme without the programme's central language curriculum, not a defensible closest match.

Current formal and prospectus evidence supports the selected German/European Language and Society route, all 180 EC, major-language progression and restricted choice. rc-0021 language-variant merging remains supported. Its discipline/language requirements describe this selected ordinary route, not every approved Open Degree alternative.

Provenance: data/counselor/comparisons/cp-000171.json; source worksheet row(s) 184. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Fresh rc-0021 (12 September 2026) merges row 184 language variants into one 180-EC Dutch/English bachelor; current OER and prospectus corroborate the same ISAT identity.

Current official sources (checked 7 October 2026):

- [OER European Languages and Cultures 2026–2027](https://www.rug.nl/let/onze-faculteit/organisatie/diensten-en-voorzieningen/onderwijsinstituut/oeren/2026-2027/bacheloropleidingen/delen-b/ba-etc-partb-2627.pdf) — Articles 3.2, 4.1, 5.1–5.2 and language table, PDF pp. 5–8; Adopted 2026–2027. ISAT 56124. The selected German/European Language and Society pathway is 60+60+60 EC: German proficiency 30, three year-two language-specific units 15, year-three language-specific unit 10, restricted year-two choice 10, minor 30 and thesis 10. Three profiles and eight major languages are available. Lectures are English, seminars may be Dutch/English, and language-specific study uses the major language. Restricted choice is profile-plus, another profile or another language. An approved Open Degree can replace some language-specific units; it is a separate permitted alternative, not the selected ordinary route.
- [European Languages, Cultures and Politics](https://www.rug.nl/bachelors/european-languages-cultures-and-politics/?lang=en) — Programme facts, major-language list and profile order; Current official prospectus; formal 2026–2027 OER controls cohort requirements. Current Dutch/English bachelor, 180 EC, ISAT 56124. The marketing title includes Politics; adopted regulations retain European Languages and Cultures. German and European Language and Society appear first in the relevant option lists. This corroborates the neutral selected pathway and rc-0021 language-variant normalization without making its language requirements universal across approved alternatives.

External credit structure: Stored and adopted selected pathway total 180 EC, with 60+60+60 years. Year-two restricted choice 10 and minor 30 remain choice spaces; the selected ordinary route retains all required German-language study.

Result: confirmed; required action: none.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000172 — Pharmacy

Institution: University of Groningen. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-03.

Existing substantive reason: The programme's defining academic identity is a cumulative pharmaceutical-science and professional Pharmacy curriculum: pharmaceutical analysis, technology and biopharmacy; receptor and systems pharmacology; pharmacokinetics, pharmacoepidemiology and pharmacotherapy; drug-group study across major organ systems and diseases; medicinal and organic chemistry; bioanalysis and instrumental analysis; compounding and dosage-form knowledge; pharmaceutical microbiology; laboratory practice; patient care and communication; professional formation; and a pharmaceutical research project. UCR provides a useful biomedical foundation and one dedicated Pharmacology course, but no chemistry curriculum and no sustained pharmaceutical analysis, formulation, pharmacokinetics, pharmacoepidemiology, medicinal chemistry, drug-group, compounding, pharmaceutical-care or pharmacy-practice sequence. A 24-course UCR schedule built from adjacent life science, psychology, data and health courses would replace rather than reproduce the target's defining pharmaceutical progression and is therefore not a defensible substantive match.

The selected Pharmacy major is supported at 180 EC, with 165 required and 15 restricted elective EC. Its professional/pharmacological and laboratory spine is external evidence for the stored exception basis. The broader MPS alternative has a minor, but it is not the selected eponymous Pharmacy route.

Provenance: data/counselor/comparisons/cp-000172.json; source worksheet row(s) 185. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [TER BSc Pharmacy 2026–2027](https://www.rug.nl/fse/education/ter/ter-2627-bsc/13-ter-bsc-pharmacy-26-27.pdf) — Appendices II–IV, PDF pp. 5–9; Adopted 2026–2027. The eponymous Pharmacy major requires 165 EC plus 15 restricted elective EC, with no free minor. The alternative Medical Pharmaceutical Sciences major requires 135 EC plus 15 restricted electives and 30 minor. Shared first and second years each total 60. Selected Pharmacy year three has research 15, six required 5-EC units and restricted electives 15. Laboratory, pharmacological, patient-care and professional-development study are defining requirements; this bachelor alone is not pharmacist licensure. The Pharmacy route is supported independently of UCR fit; the no-minor statement is route-specific. The third-year table was visually inspected.

External credit structure: Stored selected Pharmacy major totals 180 EC: first year 60, second year 60, final-year research 15 plus six required 5-EC units plus restricted electives 15. The separate MPS route has a 30-EC minor; no alternatives are stacked.

Result: confirmed; required action: none.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000174 — Frisian Language and Culture

Institution: University of Groningen. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-03.

Existing substantive reason: The programme is defined by sustained study through and about Frisian: track-specific language use and variation, Frisian linguistics, historical and modern Frisian literature and language culture, research ateliers in Frisian literature and linguistics, a field internship and an independent thesis normally written in Frisian. UCR offers useful adjacent study in general communication, psycholinguistics, stylistics, literary analysis, media, cultural heritage, history, politics and sociology, but it offers no Frisian-language course and no cumulative sequence in Frisian proficiency, linguistics, literature or regional culture. Its one introductory Dutch course cannot replace that progression. A 24-course UCR response would therefore be a broad language-and-culture programme that omits the target's defining Frisian curriculum, not a defensible closest match.

The specifically named Frisian track is current under ISAT 50479 and has an adopted September 2026 180-EC continuation, including a 10-EC internship. Dutch or Frisian teaching and Frisian thesis requirements support the language/culture identity; the normalized Dutch language value is supported but not an exhaustive statement of track instruction.

Provenance: data/counselor/comparisons/cp-000174.json; source worksheet row(s) 187. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [OER Nederlandse Talen en Culturen 2026–2027](https://www.rug.nl/let/onze-faculteit/organisatie/diensten-en-voorzieningen/onderwijsinstituut/oeren/2026-2027/bacheloropleidingen/delen-b/ba-oer-ntc-2627.pdf) — Cover; Articles 2.5, 3.2, 4.1, 5.1 and 8.3; PDF pp. 1, 3, 6–9, 15; Adopted 2026–2027. One ISAT 50479 bachelor has two tracks: Nederlandse Taal en Cultuur and Friese Taal en Cultuur. Article 2.5 identifies predecessor Dutch ISAT 56804. For September 2026 entrants each track has 60+60+60 EC; the adopted later years enter OCASYS in 2027–2028 and 2028–2029. Both have minor 30, faculty-wide choice 10 and thesis 10 in year three; Dutch adds two 5-EC subject units, Frisian adds internship 10. Research ateliers require two subject domains, with literature and linguistics specified for Frisian. Dutch instruction is Dutch; Frisian is Dutch or Frisian, with track-language thesis unless approved otherwise. Adopted 7 July 2026. Cover and cohort tables visually inspected.
- [Friese taal en cultuur](https://www.rug.nl/bachelors/frisian-language-and-culture/) — Identity, facts, new curriculum and year-one description; Current official prospectus for September 2026 curriculum. Current Frisian track under Dutch Languages and Cultures, 180 EC, taught in Dutch and Frisian. The new cohort combines Frisian language/culture with shared literary and linguistic study. Supplemental proficiency assistance is not an extra credit-bearing requirement to add to the adopted 60-EC first year. Future later-year requirements are explicitly prescribed by the adopted OER, not inferred from concurrent older cohorts.

External credit structure: Stored September 2026 Frisian track totals 60+60+60=180. Final year is minor 30, faculty choice 10, thesis 10 and internship 10. Future OCASYS release dates do not leave credits unresolved: adopted OER prescribes the continuation.

Result: confirmed; required action: none.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000175 — Medicine

Institution: University of Groningen. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-03.

Existing substantive reason: The Groningen bachelor is the first professional phase of medical training and integrates broad biomedical and pathophysiological knowledge with longitudinal clinical reasoning, patient-centred problem-based learning, medical consultation, diagnosis and treatment decisions, communication with patients and professionals, supervised competency development, healthy-ageing and prevention work, scientific training, professional formation and recurring medical knowledge progression tests. UCR can build a strong biomedical-science curriculum and add psychology, population health and research methods, but it does not offer clinical medical education, supervised patient contact, medical consultation training, diagnostic and treatment practice, clinical placements, longitudinal physician competencies or a comprehensive medical progress-testing sequence. A 24-course UCR schedule would therefore be a defensible biomedical or health-sciences programme, but not a defensible closest match to Medicine.

The current 180-EC medical structure and selected Sustainable Care route are supported. The narrow error is project allocation: the 10-EC 3.1 component note names the bachelor project without distinguishing preparation, while the 20-EC 3.2 component note omits the project conducted in that semester. Current guide explicitly separates 3.1 preparation from 3.2 project conduct.

Provenance: data/counselor/comparisons/cp-000175.json; source worksheet row(s) 188. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [TER Bachelor Medicine 2026–2027](https://www.rug.nl/umcg/education/geneeskunde/belangrijkedocumentengnk/documentenbachelor/terbachelormedicine2627.pdf) — Articles 3.3, 4.1, 7.1, 15.4 and Appendix 3; PDF pp. 7–8, 11, 26, 30–31; Adopted 2026–2027. Compulsory 180 EC, no minor/free elective: year one Causes of Diseases 35, Knowledge Development 4, Competency Development 21; year two 36+4+20; year three 26+4+30. Final competency units are 3.1 at 10 EC and 3.2 at 20 EC. Sustainable Care is first among four Dutch learning communities; assignment is binding, not an unrestricted elective. Legacy English Global Health intake stopped in 2024–2025 and is phasing out; that does not remove the selected current Dutch route.
- [Study guide Bachelor Medicine 2026–2027](https://www.rug.nl/umcg/education/geneeskunde/belangrijkedocumentengnk/documentenbachelor/studyguidebachelorgnk2627.pdf) — PDF pp. 34–36, especially semester 3.2 heading and preparation note; version 21 July 2026; 2026–2027; version 21 July 2026. Competency Development 3.1 develops consultation/clinical reasoning, professional development, healthy ageing and scientific preparation. Bachelor project preparation and proposal begin in 3.1; project conduct, thesis, reflection and presentation belong to Competency Development 3.2. The project integrates competency pathways, including individual work within teams of three to five. Stored 3.1 note says it includes the project, while the 3.2 note omits the project. Correct the allocation descriptions, retain 10/20 EC and count no additional standalone thesis credits. Page 36 was visually inspected.

External credit structure: Stored and adopted credits total 180: year totals 35+4+21, 36+4+20 and 26+4+30, each 60. Final competency components remain 10 and 20 EC; project preparation/conduct descriptions need correction, not an extra thesis component.

Result: incorrect; required action: reassess-exception.

Incorrect concerns semester-specific project annotations only. The complete medical credit structure is supported; existing UCR claims were not independently checked.

Recommended follow-up: Correct semester-specific component notes, placing project preparation in 3.1 and project/thesis/presentation in 3.2. Preserve current component weights, overall medical structure and source-backed route; reassess exception narrative consistency without deciding UCR fit.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

Implementation plan — **not implemented; audit only**:

- `data/counselor/comparisons/cp-000175.json`, fields: `comparator.components[id=y3-competency-3-1].note`, `comparator.components[id=y3-competency-3-2].note`, `comparator.additionalSourceUrls`, `comparator.sourceNotes`, `exception.curriculumContext`, `exception.checkedOn`. Describe 3.1 as clinical/professional competency study including bachelor-project preparation and proposal; describe 3.2 as the integrated bachelor project with research, thesis, reflection and presentation. Add the current guide if absent and align any semester-specific context. Preserve 10/20-EC weights, 180 total and selected Sustainable Care route. Do not introduce standalone thesis credits or assert universal clinical placements based on these sources.
- `data/counselor/review-programmes.json and existing generated counselor artifacts`, fields: `affected CP175 summaries and source context`. Regenerate only affected derived context through the normal production workflow after the canonical factual note is corrected.

Dependencies:

- Current sources resolve the external allocation; any change to final UCR feasibility remains a separate stage-two decision.

Verification and closure checks:

- 3.1 project preparation is distinguished from 3.2 project conduct, and canonical/generated notes agree with guide pp. 34–36.
- Original 60+60+60 allocation and 10/20 final competency credits are unchanged; no project credit is double counted.
- Close factual annotation correction separately; record the final UCR fit judgment as pending until independent stage two.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000179 — Griekse en Latijnse Taal en Cultuur (Classics)

Institution: University of Groningen. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-05.

Existing substantive reason: The compulsory curriculum is organized around progressive proficiency and original-language reading in both Ancient Greek and Latin, followed by advanced Greek and Latin seminars, epigraphy and papyrology, original-language poetry analysis and a thesis in the field. UCR offers substantial adjacent work in archaeology, heritage, ancient history, philosophy, myth and comparative literature, but it offers neither Ancient Greek nor Latin language instruction and therefore no cumulative classical-philology sequence. A 24-course UCR programme assembled from those adjacent fields would omit the target's defining two-language core and would not be a defensible Classics match.

Current OER supports the complete Greek/Latin disciplinary sequence and 180 EC, including two separate 10-EC research seminars. The conditional transition modules replace corresponding proficiency rather than adding credit. Stale footer year does not supersede current cover, adoption and effective date.

Provenance: data/counselor/comparisons/cp-000179.json; source worksheet row(s) 192. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [OER Griekse en Latijnse Taal en Cultuur 2026–2027](https://www.rug.nl/let/onze-faculteit/organisatie/diensten-en-voorzieningen/onderwijsinstituut/oeren/2026-2027/bacheloropleidingen/delen-b/ba-gltc-deelb-2627.pdf) — Articles 3.2, 4.1, 5.1 and 8.3; PDF pp. 6–7, 9; cover p. 1; Adopted 2026–2027. Required Greek and Latin proficiency/reading and classical literature, history/archaeology, epigraphy/papyrology and philosophy establish the field. Year one totals 60; year two 60 including faculty choice 10; year three minor 30, Greek research seminar 10, Latin research seminar 10 and thesis 10. A 10-EC transition module replaces corresponding proficiency for an entrant lacking that school language; it is not extra credit. Cover and effective/adoption dates establish 2026–2027 (effective 1 September 2026; adopted 23 June 2026), despite stale 2025–2026 footers. Dutch full-time/part-time offerings share the normalized academic target.

External credit structure: Stored and adopted credits total 180: 60+60 plus minor 30, two research seminars of 10 each and thesis 10. Conditional language transition replaces, rather than augments, proficiency credit.

Result: confirmed; required action: none.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000192 — Bachelor Life Science and Technology

Institution: University of Groningen. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-05.

Existing substantive reason: The University of Groningen programme is an integrated life-science, chemistry, physics and experimental-technology degree. Its compulsory spine joins mammalian cell biology, biochemistry, physiology, genetics and evolution with a two-course organic-chemistry sequence, pharmaceutical analysis, bioinorganic chemistry, optics, thermodynamics, biophysics, quantum and classical mechanics, imaging and spectroscopy. That theory is reinforced by dedicated practical courses in optics and cell biology, microbiology and organic chemistry, then by applied microbiology, applied biotechnology and a 15-EC research project. UCR offers meaningful molecular biology, biochemistry, physiology, genetics, pharmacology, laboratory, calculus, linear-algebra, programming and data-science courses. It does not offer the chemistry, physics, imaging, spectroscopy, microbiology, biotechnology and staged laboratory progression that defines this degree. A UCR programme built from the closest available courses would be a credible molecular-biomedicine pathway, but it would not be a defensible Life Science and Technology comparator.

Current regulations support the complete 180-EC generic Life Science and Technology route, its substantial required chemistry/physics/mathematics/laboratory core and 30 minor plus 15 approved restricted electives. Specialisation guidance does not make an arbitrary additional route compulsory.

Provenance: data/counselor/comparisons/cp-000192.json; source worksheet row(s) 205. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [TER BSc Life Science and Technology 2026–2027](https://www.rug.nl/fse/education/ter/ter-2627-bsc/11-ter-bsc-life-science-and-technology-26-27.pdf) — Appendices II–IV, PDF pp. 3–6; Adopted 2026–2027. One current Life Science and Technology major. First and second years each contain twelve 5-EC required units, spanning chemistry, optics/physics, mathematics/programming, biology/physiology and several practicals. Third year is minor 30, bachelor research 15 and restricted electives 15. Electives require approval and come from Biology, Chemistry, Biomedical Engineering, Medical Pharmaceutical Sciences or Physics; later-master requirements also apply. Faculty/university minors and approved study at other universities are permitted. Specialisation guidance for master preparation does not require arbitrarily selecting a separate formal route for this generic bachelor. Restricted 15 EC is not unrestricted choice.

External credit structure: Stored and adopted credits total 180: required years 60+60, then minor 30, research 15 and approved restricted electives 15. Master-preparation specialisations are not added to that total.

Result: confirmed; required action: none.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000194 — Middle Eastern Studies

Institution: University of Groningen. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-05.

Existing substantive reason: The University of Groningen programme is an integrated area-studies degree anchored in a progressive 30-EC Arabic-language sequence and a compulsory 30-EC study-abroad semester in Cairo or Rabat. Its disciplinary spine then studies the modern Middle East through region-specific history, Judaism and Islam, politics and international relations, culture and soft power, empire and colonialism, Islam and modernity, conflict, and relations between Europe and the Middle East. UCR offers meaningful global history, empire, international relations, peace and conflict, public international law, migration, sociology, literature, media and cultural-heritage courses. It offers neither Arabic nor a Middle Eastern Studies, Islam, Judaism or regional religious-studies sequence, and it has no embedded regional semester equivalent. A UCR programme built from the closest courses would be a credible global-history or international-relations pathway, but not a defensible Middle Eastern Studies comparator.

Current formal requirements support 180 EC, including 30 Arabic progression and a 30-EC regional semester abroad. The programme’s own current Curriculum paragraph supports the stored Global Change/Cultural Heritage restriction for both faculty-wide units; no broader choices are imported from another programme.

Provenance: data/counselor/comparisons/cp-000194.json; source worksheet row(s) 207. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [OER Midden-Oosten Studies 2026–2027](https://www.rug.nl/let/onze-faculteit/organisatie/diensten-en-voorzieningen/onderwijsinstituut/oeren/2026-2027/bacheloropleidingen/delen-b/ba-mos-deelb-2627.pdf) — Articles 4.1 and 5.1; PDF pp. 6–7; Adopted 2026–2027. Year one 60 includes Arabic Beginner 10 and Intermediate 10; year two 60 includes Arabic Advanced 10 and the 30-EC semester abroad. First/second-year substantive Middle Eastern history, religion, politics, culture and research requirements remain distinct from choice space. Year three is minor 30, thesis 10, faculty-wide unit 10 and two 5-EC subject units. Both faculty-wide units are retained within the total, not double counted as extra electives.
- [Middle Eastern Studies](https://www.rug.nl/bachelors/middle-eastern-studies/?lang=en) — Year-two course table and Curriculum paragraph; Current official prospectus. Current table places the 30-EC abroad semester in Cairo or Rabat. The Curriculum paragraph explicitly restricts both first-year and third-year 10-EC faculty-wide choices to Global Change or Cultural Heritage. That supports the stored choice descriptions; a broader list of options on another programme’s page is not substituted. Arabic progression and regional study remain compulsory alongside minor choice.

External credit structure: Stored and adopted credits total 180: 60+60+60, with Arabic 10+10+10, regional semester 30, minor 30, thesis 10 and two separate faculty-wide 10-EC choice units.

Result: confirmed; required action: none.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000196 — Physics

Institution: University of Groningen. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-05.

Existing substantive reason: The University of Groningen programme is a full disciplinary Physics degree. Its 150-EC major integrates calculus, linear algebra, differential equations and computational methods with classical and relativistic mechanics, electromagnetism, quantum physics, thermal and statistical physics, waves and optics, atomic and solid-state physics, electronics, subatomic physics, nanophysics, advanced electrodynamics, multiple staged physics laboratories and a 15-EC physics research project. UCR offers a useful mathematics and computation sequence and some applications in energy, earth systems, imaging and robotics, but it offers no Physics or Astronomy courses and no experimental-physics laboratory sequence. A UCR programme assembled from mathematics, computing and sustainability courses would be a coherent quantitative or energy-systems pathway, not a defensible Physics comparator.

Current adopted Physics requirements support the selected 180-EC route, compulsory mathematical/physics/laboratory progression, restricted selections and 30-EC minor. Research is 15 EC, with a footnote marker; optional advanced lab and the separate double-degree research rule are not compulsory additions.

Provenance: data/counselor/comparisons/cp-000196.json; source worksheet row(s) 209. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [TER BSc Physics 2026–2027](https://www.rug.nl/fse/education/ter/ter-2627-bsc/14-ter-bsc-physics-26-27.pdf) — Appendices II–IV, PDF pp. 4–6; Appendix VI p. 11; Adopted 2026–2027. Physics major 150 plus minor 30. First year has 55 required plus one 5-EC choice; second year has 55 required plus one 5-EC choice. Year three has ethics/professional study 5, two distinct restricted 5-EC choices, bachelor research 15 and minor 30. Selected first-listed Astronomy, Biomaterials, Nanophysics and Advanced Electrodynamics are valid alternatives, not universally compulsory. Advanced Experiments 2 is an alternative, not an extra required lab. Research is 15 EC with superscript footnote 1, not 151 EC; the 20-EC combined Mathematics/Physics research rule concerns a separate double-degree alternative. Current cover/headers control over stale document metadata. Table visually inspected.

External credit structure: Stored and adopted credits total 180: 60+60+60. Final year is 30 minor, 15 research, 5 professional/ethical study and two 5-EC restricted selections. Superscript research footnote adds no EC.

Result: confirmed; required action: none.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000198 — Dutch Languages and Cultures — Dutch Language and Culture

Institution: University of Groningen. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-05.

Existing substantive reason: This is a discipline-specific Dutch Studies degree whose compulsory spine combines Dutch phonology, syntax, semantics and language acquisition with historical and present-day Dutch, medieval, early-modern and modern Dutch literature, advanced Dutch-language proficiency, research workshops and a Dutch Studies thesis. UCR offers one introductory Dutch course plus genuine general courses in literature, rhetoric, communication and psycholinguistics, but those courses do not provide a sustained advanced Dutch-language, Dutch-linguistics and Dutch-literature sequence. Constructing a 24-course UCR schedule from the broader adjacent subjects would change the named academic field and leave the defining Dutch core uncovered.

The September 2026 Dutch route is fully supported at 180 EC. Its sourceNotes incorrectly says the current regulation defines three routes; the cover defines two. rc-0026 already normalizes the old 56804 target to current 50479 Dutch Studies, confirming the coupled duplicate conflict with CP199. Correcting the identity duplication takes priority over the narrow route-count note.

Provenance: data/counselor/comparisons/cp-000198.json; source worksheet row(s) 211. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Fresh rc-0026 (12 September 2026) normalizes source row 211 from older Dutch Language and Culture into current Dutch Languages and Cultures, retaining Dutch Language and Culture as the route. Row 212 is the current VARIANT of that same route; current OER/prospectus corroborate the overlap.

Current official sources (checked 7 October 2026):

- [OER Nederlandse Talen en Culturen 2026–2027](https://www.rug.nl/let/onze-faculteit/organisatie/diensten-en-voorzieningen/onderwijsinstituut/oeren/2026-2027/bacheloropleidingen/delen-b/ba-oer-ntc-2627.pdf) — Cover; Articles 2.5, 3.2, 4.1, 5.1 and 8.3; PDF pp. 1, 3, 6–9, 15; Adopted 2026–2027. One ISAT 50479 bachelor has two tracks: Nederlandse Taal en Cultuur and Friese Taal en Cultuur. Article 2.5 identifies predecessor Dutch ISAT 56804. For September 2026 entrants each track has 60+60+60 EC; the adopted later years enter OCASYS in 2027–2028 and 2028–2029. Both have minor 30, faculty-wide choice 10 and thesis 10 in year three; Dutch adds two 5-EC subject units, Frisian adds internship 10. Research ateliers require two subject domains, with literature and linguistics specified for Frisian. Dutch instruction is Dutch; Frisian is Dutch or Frisian, with track-language thesis unless approved otherwise. Adopted 7 July 2026. Cover and cohort tables visually inspected.
- [Nederlandse Taal en Cultuur](https://www.rug.nl/bachelors/dutch-language-and-culture/) — Programme facts, degree title, CROHO and cohort curriculum; Current official prospectus; adopted OER establishes September 2026 cohort. The named Dutch route awards BA in Nederlandse Talen en Culturen, CROHO 50479, 180 EC, Dutch instruction. Together with the adopted OER and rc-0026 normalization of row 211 from old 56804 to this successor route, the row-212 VARIANT entry represents the same current route, not another independent bachelor. Route count in CP198 sourceNotes is three; current formal evidence is two. This is a current factual contradiction, with no dated evidence supporting an outdated classification.

External credit structure: Stored September 2026 Dutch track totals 60+60+60=180. Final year is minor 30, faculty choice 10, thesis 10 and two 5-EC subject units. The prescribed 2027–2028/2028–2029 continuation is distinct from older-cohort tables.

Result: incorrect; required action: correct-registry-and-reprocess.

Incorrect concerns the current three-route source note. The selected Dutch track and its credits are supported; duplicate identity is a separately confirmed conflict.

Secondary attribute finding(s):

- duplicate normalized current academic route: confirmed; stored ["cp-000198 and cp-000199 are separately eligible targets"], verified ["Both represent one current Dutch Language and Culture track"]. Separate closure: Two-track source-note correction and later UCR feasibility decision.

Recommended follow-up: Resolve CP198/CP199 together as one current Dutch route; prefer CP198 as owner because its earlier permanent ID already carries the documented successor normalization. Retain CP199 permanently as a supported historical alias/duplicate rather than deleting or renumbering it. Preserve raw source/old identifiers, reconcile crosswalk ownership and fix CP198 route count from three to two.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

Implementation plan — **not implemented; audit only**:

- `data/registry/programmes.csv`, fields: `cp-000198 canonical_name/current_status/production_eligible/production_order`, `source_excel_rows_json`, `offering_ids_json`, `corrected_attributes_json`, `official_source_ids_json`, `official_source_urls_json`, `normalization_basis`, `cp-000199 current_status/production_eligible/production_order`. Record one current Dutch Language and Culture track under umbrella ISAT 50479. Prefer CP198 as surviving production owner (earlier permanent ID; rc-0026 already maps it to the successor), subject to supported alias handling. Associate source rows 211 and 212 and their offering IDs with that one owner. Retain CP199 as a permanent historical alias/duplicate with production_eligible=false and blank production_order. Preserve old 56804 and both programme-unit identifiers as provenance, distinguish current umbrella code from raw historical identifiers, and never delete or renumber an ID.
- `data/registry/programme_source_rows.csv; data/registry/programme_offerings.csv`, fields: `counselor_programme_id ownership for source row 212 and its current offering`, `traceable linkage to former CP199 owner`. Use the schema-supported crosswalk/alias model to associate both raw sources and offerings with the one current owner, retaining the former CP199 relationship in history. Avoid both independent eligible routes and unexplained duplicated current ownership.
- `data/registry/resolution_decisions.csv; data/registry/resolution_sources.csv and existing post-build correction workflow`, fields: `documented successor/duplicate correction`, `current official identity evidence`, `historical decision retention`. Document the coordinated correction and sources through the existing researched correction workflow so rebuilds reproduce it. Preserve rc-0026 and its original evidence; append a supported correction/decision rather than rewriting immutable upstream source, offering or resolution-case tables. Do not invent a resolved case ID or unsupported decision enum.
- `data/counselor/comparisons/cp-000198.json`, fields: `programmeProvider source/offer/identity metadata`, `comparator.sourceNotes`, `comparator.additionalSourceUrls`, `exception.curriculumContext`, `exception.checkedOn`. Refresh provider provenance after normalized ownership is resolved. Replace three formal routes with two named tracks. Preserve the complete September 2026 Dutch curriculum and its later-year effective cohort dates; the final no-defensible-ucr-match decision remains pending independent UCR assessment.
- `data/counselor/comparisons/cp-000199.json; data/counselor/review-programmes.json and existing generated inventories`, fields: `duplicate canonical record retention/alias treatment`, `production scope/status summaries`, `route ownership and aggregate counts`. Apply repository-supported handling for a formerly eligible canonical target retained outside production. Preserve permanent ID, original registry-exception evidence and source history. Generate one independent current Dutch route; do not construct a second comparison or silently drop the original audit entry.

Dependencies:

- Confirm the repository-supported permanent alias/history and out-of-scope canonical retention mechanism before implementation; no new current_status or decision enum is proposed as already supported.
- Choose and document the surviving owner once for both entries; CP198 is the proposed owner, not an implemented decision.
- Retain the researched identity correction in the registry rebuild workflow; exact crosswalk representation must preserve raw provenance.
- Any final UCR fit decision for the surviving route is separate stage two.

Verification and closure checks:

- Exactly one independently production-eligible Dutch Language and Culture route exists under current 50479; CP174 Frisian remains a separate track.
- Both permanent IDs and the old/new programme-unit identifiers remain traceable; rows 211/212 and both offering UUIDs are retained without contradictory active ownership.
- Registry rebuild, canonical metadata and generated scope/count inventories agree; retained duplicate has production_eligible=false and blank production_order.
- CP198 sourceNotes says two tracks and its components remain 180 EC for the correct 2026 entrant continuation; old cohort tables are not substituted.
- Original audit entries, registry-exception reason and historical rc-0026 remain intact. Closing duplicate normalization does not assert UCR feasibility.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000199 — Dutch Language and Culture — track within Dutch Languages and Cultures

Institution: University of Groningen. Audit scope: Normalized duplicate academic identity and current cohort requirements; no UCR feasibility assessment.

Existing formal type: `registry-exception`; existing check date: 2026-10-05.

Existing substantive reason: Current official evidence does not support cp-000199 as an independent academic target distinct from cp-000198. The 2026–27 regulation defines a single current Dutch Languages and Cultures bachelor (ISAT 50479) with a Dutch Language and Culture track, while explicitly identifying Dutch Language and Culture ISAT 56804 as the predecessor programme. The registry has already normalized that predecessor into cp-000198 as the current successor route, but cp-000199 separately represents the same current Dutch Language and Culture track through a VARIANT record under the new programme. Publishing a second UCR comparison for cp-000199 would duplicate one academic route under two permanent counselor IDs. The registry normalization must determine which ID owns this route and merge or cross-reference the duplicate before a comparison is attempted.

Current OER/prospectus and rc-0026 confirm that CP199 is the same current Dutch Language and Culture track already represented by CP198, not a second independent target. The existing registry-exception rationale is supported. Full external credits are known; duplicate normalized academic identity remains the blocker.

Provenance: data/counselor/comparisons/cp-000199.json; source worksheet row(s) 212. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Fresh rc-0026 (12 September 2026) normalizes source row 211 from older Dutch Language and Culture into current Dutch Languages and Cultures, retaining Dutch Language and Culture as the route. Row 212 is the current VARIANT of that same route; current OER/prospectus corroborate the overlap.

Current official sources (checked 7 October 2026):

- [OER Nederlandse Talen en Culturen 2026–2027](https://www.rug.nl/let/onze-faculteit/organisatie/diensten-en-voorzieningen/onderwijsinstituut/oeren/2026-2027/bacheloropleidingen/delen-b/ba-oer-ntc-2627.pdf) — Cover; Articles 2.5, 3.2, 4.1, 5.1 and 8.3; PDF pp. 1, 3, 6–9, 15; Adopted 2026–2027. One ISAT 50479 bachelor has two tracks: Nederlandse Taal en Cultuur and Friese Taal en Cultuur. Article 2.5 identifies predecessor Dutch ISAT 56804. For September 2026 entrants each track has 60+60+60 EC; the adopted later years enter OCASYS in 2027–2028 and 2028–2029. Both have minor 30, faculty-wide choice 10 and thesis 10 in year three; Dutch adds two 5-EC subject units, Frisian adds internship 10. Research ateliers require two subject domains, with literature and linguistics specified for Frisian. Dutch instruction is Dutch; Frisian is Dutch or Frisian, with track-language thesis unless approved otherwise. Adopted 7 July 2026. Cover and cohort tables visually inspected.
- [Nederlandse Taal en Cultuur](https://www.rug.nl/bachelors/dutch-language-and-culture/) — Programme facts, degree title, CROHO and cohort curriculum; Current official prospectus; adopted OER establishes September 2026 cohort. The named Dutch route awards BA in Nederlandse Talen en Culturen, CROHO 50479, 180 EC, Dutch instruction. Together with the adopted OER and rc-0026 normalization of row 211 from old 56804 to this successor route, the row-212 VARIANT entry represents the same current route, not another independent bachelor. Route count in CP198 sourceNotes is three; current formal evidence is two. This is a current factual contradiction, with no dated evidence supporting an outdated classification.

External credit structure: The same September 2026 Dutch track has complete 180 EC. Identical supported academic structure establishes no separate route entitlement for this duplicate permanent ID; normalized ownership must be resolved first.

Result: confirmed; required action: correct-registry-and-reprocess.

Recommended follow-up: Execute the same coordinated identity correction recorded for CP198. Remove the retained duplicate from independent production eligibility, preserve its permanent ID and provenance through the repository-supported alias/history mechanism, regenerate affected inventories and retain the original registry-exception audit evidence.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

Implementation plan — **not implemented; audit only**:

- `data/registry/programmes.csv`, fields: `cp-000198 canonical_name/current_status/production_eligible/production_order`, `source_excel_rows_json`, `offering_ids_json`, `corrected_attributes_json`, `official_source_ids_json`, `official_source_urls_json`, `normalization_basis`, `cp-000199 current_status/production_eligible/production_order`. Record one current Dutch Language and Culture track under umbrella ISAT 50479. Prefer CP198 as surviving production owner (earlier permanent ID; rc-0026 already maps it to the successor), subject to supported alias handling. Associate source rows 211 and 212 and their offering IDs with that one owner. Retain CP199 as a permanent historical alias/duplicate with production_eligible=false and blank production_order. Preserve old 56804 and both programme-unit identifiers as provenance, distinguish current umbrella code from raw historical identifiers, and never delete or renumber an ID.
- `data/registry/programme_source_rows.csv; data/registry/programme_offerings.csv`, fields: `counselor_programme_id ownership for source row 212 and its current offering`, `traceable linkage to former CP199 owner`. Use the schema-supported crosswalk/alias model to associate both raw sources and offerings with the one current owner, retaining the former CP199 relationship in history. Avoid both independent eligible routes and unexplained duplicated current ownership.
- `data/registry/resolution_decisions.csv; data/registry/resolution_sources.csv and existing post-build correction workflow`, fields: `documented successor/duplicate correction`, `current official identity evidence`, `historical decision retention`. Document the coordinated correction and sources through the existing researched correction workflow so rebuilds reproduce it. Preserve rc-0026 and its original evidence; append a supported correction/decision rather than rewriting immutable upstream source, offering or resolution-case tables. Do not invent a resolved case ID or unsupported decision enum.
- `data/counselor/comparisons/cp-000198.json`, fields: `programmeProvider source/offer/identity metadata`, `comparator.sourceNotes`, `comparator.additionalSourceUrls`, `exception.curriculumContext`, `exception.checkedOn`. Refresh provider provenance after normalized ownership is resolved. Replace three formal routes with two named tracks. Preserve the complete September 2026 Dutch curriculum and its later-year effective cohort dates; the final no-defensible-ucr-match decision remains pending independent UCR assessment.
- `data/counselor/comparisons/cp-000199.json; data/counselor/review-programmes.json and existing generated inventories`, fields: `duplicate canonical record retention/alias treatment`, `production scope/status summaries`, `route ownership and aggregate counts`. Apply repository-supported handling for a formerly eligible canonical target retained outside production. Preserve permanent ID, original registry-exception evidence and source history. Generate one independent current Dutch route; do not construct a second comparison or silently drop the original audit entry.

Dependencies:

- Confirm the repository-supported permanent alias/history and out-of-scope canonical retention mechanism before implementation; no new current_status or decision enum is proposed as already supported.
- Choose and document the surviving owner once for both entries; CP198 is the proposed owner, not an implemented decision.
- Retain the researched identity correction in the registry rebuild workflow; exact crosswalk representation must preserve raw provenance.
- Any final UCR fit decision for the surviving route is separate stage two.

Verification and closure checks:

- Exactly one independently production-eligible Dutch Language and Culture route exists under current 50479; CP174 Frisian remains a separate track.
- Both permanent IDs and the old/new programme-unit identifiers remain traceable; rows 211/212 and both offering UUIDs are retained without contradictory active ownership.
- Registry rebuild, canonical metadata and generated scope/count inventories agree; retained duplicate has production_eligible=false and blank production_order.
- CP198 sourceNotes says two tracks and its components remain 180 EC for the correct 2026 entrant continuation; old cohort tables are not substituted.
- Original audit entries, registry-exception reason and historical rc-0026 remain intact. Closing duplicate normalization does not assert UCR feasibility.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

## Cumulative findings after batch 7

| Finding | Count |
|---|---:|
| confirmed | 56 |
| incorrect | 10 |
| outdated | 0 |
| still-unresolved | 4 |

| Required action | Count |
|---|---:|
| none | 51 |
| reprocess-as-comparison | 0 |
| reassess-exception | 12 |
| correct-registry-and-reprocess | 4 |
| research-again-later | 3 |

## Batch 7 findings

Nine findings are confirmed within the external-programme scope. CP205 is incorrect in its ordinary third-year choice classification: the current TER distinguishes 15-EC minor space from 15 EC of restricted faculty courses. Its 180-EC arithmetic is sound, and specific 30-EC alternatives exist, but the stored generic open-minor description does not establish their conditions. An explicit ordinary 180-EC reconstruction and field-level remediation plan are recorded. No current UCR feasibility outcome is inferred.

CP200 is the generic Dutch Languages and Cultures umbrella and retains a valid first-listed Dutch representative pathway. It is distinguished from the specifically named CP198/CP199 duplicate pair; common selected components alone do not prove duplicate normalized identity. Current formal tables control older public course lists for Astronomy, Linguistics and Applied Physics. Chemical Engineering’s internal-year discrepancy and today’s inaccessible Ocasys are preserved explicitly; the university’s current index links the exact appendix as 2026–2027. No case is classified as outdated or externally unresolved.

| ID | Programme | Formal type | Finding | Required action |
|---|---|---|---|---|
| cp-000200 | Dutch Languages and Cultures — Dutch Language and Culture route | no-defensible-ucr-match | confirmed | none |
| cp-000205 | Religious Studies | no-defensible-ucr-match | incorrect | reassess-exception |
| cp-000206 | Chemistry | no-defensible-ucr-match | confirmed | none |
| cp-000207 | Chemical Engineering | no-defensible-ucr-match | confirmed | none |
| cp-000210 | Astronomy | no-defensible-ucr-match | confirmed | none |
| cp-000211 | Linguistics | no-defensible-ucr-match | confirmed | none |
| cp-000212 | Dentistry (Tandheelkunde) | no-defensible-ucr-match | confirmed | none |
| cp-000213 | Industrial Engineering and Management | no-defensible-ucr-match | confirmed | none |
| cp-000214 | Applied Physics | no-defensible-ucr-match | confirmed | none |
| cp-000215 | Applied Mathematics | no-defensible-ucr-match | confirmed | none |

## Batch 7 evidence and implementation plans

### cp-000200 — Dutch Languages and Cultures — Dutch Language and Culture route

Institution: University of Groningen. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-05.

Existing substantive reason: The selected route is a discipline-specific Dutch Studies degree whose compulsory spine combines Dutch phonology, syntax, semantics and language acquisition with historical and present-day Dutch, medieval, early-modern and modern Dutch literature, advanced Dutch-language proficiency, research workshops and a Dutch Studies thesis. UCR offers one introductory Dutch course plus genuine general courses in literature, rhetoric, communication and psycholinguistics, but those courses do not provide a sustained advanced Dutch-language, Dutch-linguistics and Dutch-literature sequence. Constructing a 24-course UCR schedule from broader adjacent subjects would change the named academic field and leave the defining Dutch core uncovered.

Current official evidence supports the generic Dutch Languages and Cultures umbrella, its two tracks and the neutral first-listed Dutch pathway at 180 EC for September 2026 entrants. CP200 is the generic target, unlike the specifically named duplicate Dutch-track pair CP198/CP199. Identical selected components alone do not make this broader normalized identity a duplicate.

Provenance: data/counselor/comparisons/cp-000200.json; source worksheet row(s) 213. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [OER Nederlandse Talen en Culturen 2026–2027](https://www.rug.nl/let/onze-faculteit/organisatie/diensten-en-voorzieningen/onderwijsinstituut/oeren/2026-2027/bacheloropleidingen/delen-b/ba-oer-ntc-2627.pdf) — Cover; Articles 2.5, 3.2, 4.1, 5.1 and 8.3; PDF pp. 1, 3, 6–9, 15; Adopted 2026–2027. One ISAT 50479 bachelor has two tracks: Nederlandse Taal en Cultuur and Friese Taal en Cultuur. Article 2.5 identifies predecessor Dutch ISAT 56804. For September 2026 entrants each track has 60+60+60 EC; the adopted later years enter OCASYS in 2027–2028 and 2028–2029. Both have minor 30, faculty-wide choice 10 and thesis 10 in year three; Dutch adds two 5-EC subject units, Frisian adds internship 10. Research ateliers require two subject domains, with literature and linguistics specified for Frisian. Dutch instruction is Dutch; Frisian is Dutch or Frisian, with track-language thesis unless approved otherwise. Adopted 7 July 2026. Cover and cohort tables visually inspected.
- [Dutch Languages and Cultures](https://www.rug.nl/bachelors/dutch-languages-and-cultures/) — Facts, two programme options, degree title and CROHO; Current official prospectus; adopted September 2026 cohort rules. Current Dutch-taught, full-time, 180-EC umbrella bachelor under 50479. It offers Dutch Language and Culture and Frisian Language and Culture. This normalized target is the generic umbrella; the Dutch track is a valid first-listed representative pathway. It differs in identity/coverage from the specifically named Dutch-track targets in the CP198/CP199 duplicate pair. Sharing a neutrally selected curriculum does not by itself prove duplicate normalized identity. The current cohort OER was retrieved again and its Dutch continuation table visually inspected.

External credit structure: Stored/current Dutch representative pathway is 60+60+60=180. Final year is minor 30, faculty choice 10, thesis 10 and two 5-EC subject units. Adopted later years enter the catalogue as the September 2026 cohort progresses.

Result: confirmed; required action: none.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

Generic umbrella CP200 remains distinguishable from its specifically named track targets. The coordinated CP198/CP199 duplicate correction must preserve this distinction and avoid treating representative curriculum overlap alone as duplicate identity.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000205 — Religious Studies

Institution: University of Groningen. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-06.

Existing substantive reason: The Groningen bachelor is defined by sustained disciplinary study of Christianity, Judaism, Islam, Hinduism, Buddhism and indigenous South Asian traditions; comparative Religious Studies concepts and methods; anthropology, psychology and sociology of religion; ritual; sacred images and texts; religion, media, identity and politics; a dedicated specialisation; and a Religious Studies thesis. UCR has relevant courses in philosophy, sociology, politics, history, archaeology, literature, media and cultural analysis, but no course or sequence in Religious Studies, theology, comparative religion, sacred texts, lived religion or the history and practice of religious traditions. A 24-course UCR programme could examine culture, ideas and institutions around religion, yet most courses would treat religion only incidentally and would omit the target’s defining disciplinary core. Publishing it as a closest match would therefore misstate what UCR teaches.

The complete disciplinary Religious Studies core and English identity are supported. The stored third-year 30-EC generic open minor overstates ordinary choice freedom: adopted Article 7.1 separates 15 minor from 15 restricted faculty courses. Specific 30-EC alternatives/replacements are permitted, but the record does not identify the alternative and conditions needed to justify its unrestricted label. A complete ordinary 180-EC route is now explicitly verified.

Provenance: data/counselor/comparisons/cp-000205.json; source worksheet row(s) 218. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Fresh rc-0029, resolved 12 September 2026, merges offerings and corrects instruction language to English while retaining Dutch-coded offering as stale raw provenance. Current prospectus and adopted TER support the correction; permission to submit some assessments in Dutch does not change instruction language.

Current official sources (checked 7 October 2026):

- [Religious Studies](https://www.rug.nl/bachelors/religious-studies/?lang=en) — Identity, years one/two and third-year alternatives, thesis and science communication; Current undated prospectus; formal TER controls 2026–2027. English, 180 EC, 50902. First and second years each show eight compulsory 7.5-EC religion/methods units. Third year includes thesis seminar 7.5, thesis 10, science communication 5 and named specialisation alternatives 7.5. The webpage presents 30-EC minor options without explaining the ordinary formal 15-EC minor plus 15-EC faculty-course restriction. Its contemporary social/political emphasis supports the selected Cultural and Political Impact of Religion option; the current TER controls formal allocation. rc-0029’s English-language correction remains supported.
- [TER BA Religious Studies 2026–2027](https://www.rug.nl/rcs/education/studyguide/oer-26-27/ter-ba-rs-26-27.pdf) — Articles 3.5/3.6, 4.1 and 7.1.1–7.1.6; PDF pp. 2, 9–10, 14–15; Adopted 2026–2027; 27 August 2026. Adopted 27 August 2026; current official index links this TER. Cover academic year and interior headers are 2026–2027 despite a stale cover running line and concept metadata. Ordinary third year: minor/personal minor 15 (or Quranic Arabic plus optional module), two of three faculty units at 7.5 each, one of two specialisations 7.5, thesis seminar 7.5, science communication 5 and thesis 10. Faculty alternatives are Climate Change, End Times, Sustainability; Religion, Space and Place; optional module. Separate permitted abroad/education/spiritual-care alternatives and Board-approved replacements do not make every ordinary 30-EC block unrestricted. First two years are 60 each. Formal choice clauses visually inspected.

External credit structure: Stored components sum to 180 but misclassify the ordinary third-year choice space. Correct ordinary allocation is 60+60+[15 minor+15 restricted faculty+7.5 specialisation+7.5 thesis seminar+10 thesis+5 science communication]=180. Permitted named/approved 30-EC alternatives require their own conditions.

Verified reconstruction for later external remediation (audit evidence only):

| Study year | Component | EC | Status / qualification |
|---|---|---:|---|
| 1 | Christianity: History, Sources and Praxis | 7.5 | required |
| 1 | Concepts and Methods 1: Study of Religion | 7.5 | required |
| 1 | Anthropology of Religion | 7.5 | required |
| 1 | Religion in South Asia | 7.5 | required |
| 1 | Judaism: History, Sources and Praxis | 7.5 | required |
| 1 | Psychology and Sociology of Religion | 7.5 | required |
| 1 | Islam: History, Sources and Praxis | 7.5 | required |
| 1 | Philosophy of Religion and Spirituality | 7.5 | required |
| 2 | Concepts and Methods 2: Researching Religion | 7.5 | required |
| 2 | Rituals in Theory and Practice | 7.5 | required |
| 2 | Ethics, Religion and Care | 7.5 | required |
| 2 | The Sacred Image | 7.5 | required |
| 2 | Religion, Media and Popular Culture | 7.5 | required |
| 2 | The Text Awakens: Reading and Using of Religious Texts | 7.5 | required |
| 2 | Religion, Diversity and Identity | 7.5 | required |
| 2 | Religion and Politics | 7.5 | required |
| 3 | University or approved personal minor | 15 | open-choice; Ordinary route; Quranic Arabic 1 plus optional module is a mutually exclusive alternative. |
| 3 | Climate Change, End Times, Sustainability | 7.5 | restricted-choice; First of three faculty options; select two. |
| 3 | Religion, Space and Place | 7.5 | restricted-choice; Second faculty option; optional module is the unselected third alternative. |
| 3 | Cultural and Political Impact of Religion | 7.5 | restricted-choice; Existing broad-academic-identity specialisation retained; Origins of Religion is an alternative. |
| 3 | Thesis Seminar | 7.5 | required |
| 3 | Bachelor Thesis | 10 | required |
| 3 | Science Communication | 5 | required |

Total: **180 EC**; study-year totals **60 + 60 + 60**. A complete ordinary external reconstruction for later remediation; canonical production data remains unchanged and final UCR feasibility is unassessed.

Choice and source-context rules:

- Keep 15 ordinary minor separate from the 15-EC choose-two faculty requirement.
- Retain Cultural and Political Impact of Religion as the selected specialisation under the existing broad-identity rule; no UCR-based choice.
- The 30-EC abroad/education/spiritual-care opportunities and Board-approved replacements are alternatives with conditions, not proof that every ordinary 30-EC block is open.
- Do not add optional Quranic Arabic or a third faculty unit to the selected route.

Result: incorrect; required action: reassess-exception.

Incorrect concerns ordinary third-year credit/choice classification, not the stored arithmetic total or final UCR decision. Current formal rules permit distinct 30-EC alternatives, but the stored generic route does not establish their conditions. No dated evidence shows a supported earlier ordinary allocation later superseded, so outdated is not assigned.

Recommended follow-up: Replace the unqualified 30-EC minor component with 15-EC minor plus two 7.5-EC restricted faculty units; select the first two named faculty options neutrally. Retain the selected Cultural and Political Impact specialisation and all research/communication credits. Update source context and route-selection basis, explain separately permitted 30-EC alternatives, and reassess the exception narrative without deciding UCR fit.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

Implementation plan — **not implemented; audit only**:

- `data/counselor/decisions/cp-000205.json`, fields: `sources`, `comparator.primarySource/additionalSources`, `comparator.components tuples`, `comparator.sourceNotes`, `routeSelection.basis`, `exception.curriculumContext`, `exception.reason if it makes a choice-space claim`, `exception.checkedOn`. Correct the existing version-2 compact academic decision first: change the y3-minor tuple from 30 to 15 EC, add two stable-ID 7.5-EC faculty-course tuples using the verified ordinary pathway, add a source token for the adopted TER and align source/choice context. Preserve the broad-identity specialisation selection and original UCR evidence as historical provenance until the separate fit reassessment. Compile the canonical record from the corrected decision using the current exception workflow.
- `data/counselor/comparisons/cp-000205.json`, fields: `comparator.components[id=y3-minor]`, `comparator.components new restricted-faculty components`, `comparator.primarySourceUrl`, `comparator.additionalSourceUrls`, `comparator.sourceNotes`, `comparator.routeSelection.basis`, `exception.curriculumContext`, `exception.reason if it makes a choice-space claim`, `exception.checkedOn`. Reconstruct the ordinary current third year as minor 15, Climate Change/End Times/Sustainability 7.5 and Religion/Space/Place 7.5, selected as the first two of three faculty options independently of UCR. Retain Cultural and Political Impact 7.5 under the existing broad-identity rationale, thesis seminar 7.5, thesis 10 and science communication 5. Preserve first/second-year components. Add the controlling TER, replace unqualified 30-EC-open-minor language and explain permitted 30-EC alternatives and approval/replacement requirements. Keep the selected specialisation; do not choose a different option to ease UCR fit.
- `data/counselor/review-programmes.json and existing generated counselor artifacts`, fields: `affected CP205 curriculum/source summaries`. Regenerate affected external summaries after the canonical correction through the existing production workflow. Preserve the original audit provenance and the separate pending UCR decision.

Dependencies:

- Current TER resolves the ordinary 180-EC route; no further external-source prerequisite is needed for that reconstruction.
- If retaining the stored generic 30-EC minor instead, identify the exact permitted alternative and its replacement/approval conditions before claiming that pathway is valid.
- Final UCR feasibility remains independent stage two.

Verification and closure checks:

- First year 60, second year 60 and third year 60; ordinary minor is 15 and exactly two faculty choices total 15.
- Do not stack all three faculty choices, Quranic Arabic plus minor, or a 30-EC alternative plus the ordinary 15-EC faculty requirements.
- Source notes, route-selection basis and context accurately distinguish ordinary structure from named/approved alternatives; preserve specialisation, seminar, thesis and communication credits.
- Recompilation reproduces the corrected canonical record from its compact decision; run exception-specific schema/record validation at implementation.
- Canonical and generated summaries agree; close the external allocation correction separately from final UCR reassessment.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000206 — Chemistry

Institution: University of Groningen. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-06.

Existing substantive reason: The University of Groningen programme is a cumulative experimental Chemistry degree. Its defining spine includes molecular structure and reactivity, organic, inorganic, physical and quantum chemistry, spectroscopy, transport phenomena, materials, chemical safety, multiple synthesis and analysis laboratories, a 20-EC chemistry specialisation, a research practical and a 15-EC experimental research project. UCR offers valuable biology, biochemistry, biomedical science, mathematics, programming, data science and one life-science laboratory course, but no general, organic, inorganic or physical chemistry sequence, no spectroscopy or chemical-analysis sequence, no chemical-transport or quantum-chemistry course, and no staged synthesis/analysis laboratory formation. Even the selected Chemistry of Life specialisation rests on that missing chemistry core. A UCR programme assembled from biological and quantitative courses would therefore be a molecular-biomedicine programme, not a defensible Chemistry comparator.

The indexed current Chemistry appendix supports all 180 EC, staged experimental chemistry requirements and the selected 20-EC Chemistry of Life specialisation. Its dedicated Appendix II route list supports the neutral first-listed selection despite a later differently ordered summary. Minor 30 and research/practical credits remain separate.

Provenance: data/counselor/comparisons/cp-000206.json; source worksheet row(s) 219. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [TER appendix BSc Chemistry 2026–2027](https://www.rug.nl/fse/education/ter/ter-2627-bsc/8-ter-bsc-chemistry-26-27.pdf) — Appendices I–IV; PDF pp. 1–6, especially II p. 4 and course tables pp. 4–6; Current 2026–2027. Required first year is twelve 5-EC units. Upper years contain ten required 5-EC chemistry units, one 20-EC specialisation, research practical 5, research project 15 and minor 30: 60+120=180. Appendix II lists Chemistry of Life first; its four 5-EC units are Recombinant DNA and Biotechnology, Chemical Biology, (Bio)-catalysis and Cellular Chemistry. Appendix IV’s summary orders specialisations differently, but the earlier dedicated route list supports the stored neutral selection. Lab/synthesis, analysis, quantum/physical/organic/inorganic chemistry and chemical safety are substantive requirements. Project requires first year plus 130 EC and approval steps. Minor choices are deepening Chemistry, Industrial Chemistry or university minors. Table visually inspected.
- [FSE Teaching and Examination Regulations](https://www.rug.nl/fse/education/ter/?lang=en) — 2026–2027 bachelor appendix links and page modification date; Current official index; last modified 4 September 2026. Official index links the exact current appendix URLs for Chemistry, Chemical Engineering, Astronomy, Industrial Engineering and Management, Applied Physics and Applied Mathematics under 2026–2027. Index last modified 4 September 2026. This establishes current institutional publication context; it does not silently remove Chemical Engineering’s internal-year discrepancy or substitute a retrieved catalogue for an inaccessible one.

External credit structure: Stored/current total 180: first year 60; upper common chemistry 50, specialisation 20, research practical 5, research project 15 and minor 30. Formal appendix groups upper years together; no unsupported 60/60 split is invented.

Result: confirmed; required action: none.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000207 — Chemical Engineering

Institution: University of Groningen. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-06.

Existing substantive reason: The Groningen bachelor is an integrated chemistry-and-process-engineering degree. Its compulsory spine combines organic, inorganic and physical chemistry, spectroscopy and synthesis laboratories with thermodynamics, transport phenomena, reactor engineering, separation processes, process control, process equipment, polymer chemistry and engineering, product technology, numerical analysis, multiple engineering practicals, a 10-EC process-design project and a 15-EC research project. UCR offers useful sustainability, mathematics, programming, data, biology, biochemistry and one life-science laboratory course, but no chemistry sequence and no chemical/process-engineering curriculum. It lacks reactors, separations, process control, thermodynamics, transport engineering, process equipment, polymer engineering, synthesis laboratories and process design. A UCR programme assembled from adjacent science, sustainability and data courses would not be a defensible Chemical Engineering comparator.

The university currently publishes the exact appendix under 2026–2027; its tables support 60+105+15=180 and the chemistry/process-engineering spine. Its 2025/2026 running year is a real source-context discrepancy already disclosed in the record. Today’s inaccessible Ocasys does not disprove the original access claim; current index and programme evidence support applicability, with that limitation retained.

Provenance: data/counselor/comparisons/cp-000207.json; source worksheet row(s) 220. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [Current published TER appendix BSc Chemical Engineering](https://www.rug.nl/fse/education/ter/ter-2627-bsc/7-ter-bsc-chemical-engineering-26-27.pdf) — Appendices II–IV; PDF pp. 1, 4–6; official index labels document 2026–2027; Published as 2026–2027; internal running year 2025/2026. Ordinary bachelor: first year 60, upper-year compulsory study 105 and individually Board-approved elective study 15, total 180. Required process-engineering core includes reactors, transport, thermodynamics, separations, process control/equipment, polymer analysis/engineering practicals, Process Design 10 and research 15. Electives may come from bachelor programmes with individual approval; five listed chemical-engineering options are examples, not a licence to treat optional Polymer Engineering as an extra requirement. The PDF repeatedly says 2025/2026, while the official index links this exact file as 2026–2027. Keep that source conflict explicit. Today’s Ocasys retrieval exposed no curriculum; the original access claim was not reproduced. Table visually inspected.
- [FSE Teaching and Examination Regulations](https://www.rug.nl/fse/education/ter/?lang=en) — 2026–2027 bachelor appendix links and page modification date; Current official index; last modified 4 September 2026. Official index links the exact current appendix URLs for Chemistry, Chemical Engineering, Astronomy, Industrial Engineering and Management, Applied Physics and Applied Mathematics under 2026–2027. Index last modified 4 September 2026. This establishes current institutional publication context; it does not silently remove Chemical Engineering’s internal-year discrepancy or substitute a retrieved catalogue for an inaccessible one.
- [Chemical Engineering](https://www.rug.nl/bachelors/chemical-engineering/?lang=en) — Facts, course tables and curriculum; Current official prospectus. Current English, 180-EC BSc, 56960. Describes thermodynamics, transport, reactor/process engineering and industrial scale. Public tables corroborate substantial required study, the 10-EC process design and 15-EC research project, but omit some first-year units and mix later-year placement/listing; they do not independently resolve every credit or substitute for the indexed formal appendix. The current appendix controls the 60+105+15 structure, with its year-label caveat retained.

External credit structure: Stored/currently indexed total 180: compulsory first year 60, upper required study 105 and approved electives 15. The formal appendix groups upper years together; the public list is not an exact alternative credit allocation.

Result: confirmed; required action: none.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

Source-context limitations:

- Official index labels the retrieved appendix 2026–2027; internal running headers remain 2025/2026. Current publication context supports use with this disclosed caveat.
- Today’s Ocasys retrieval returned an empty application shell, so the prior current-catalogue access assertion was not independently reproduced. This access limitation is not classified as an incorrect historical claim.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000210 — Astronomy

Institution: University of Groningen. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-06.

Existing substantive reason: The University of Groningen programme is a full disciplinary Astronomy degree. Its compulsory 150-EC major combines calculus, linear algebra, differential equations, numerical methods and statistics with mechanics and relativity, electromagnetism, quantum physics, thermal physics, waves and optics, observational astronomy, planetary science, stellar and galactic physics, radiative processes, advanced electrodynamics, astrophysical hydrodynamics, the interstellar medium, laboratory skills and a 15-EC astronomy research project. UCR offers useful mathematics and computation plus adjacent study in Earth systems, imaging and robotics, but no Astronomy or Astrophysics course, no sustained physics core and no astronomical-observation or experimental-physics laboratory sequence. A UCR programme assembled from mathematics, computing and Earth science would be a coherent quantitative pathway, not a defensible Astronomy comparator.

Current formal Astronomy requirements support major 150 plus minor 30, required mathematics/physics/observation progression and a 15-EC research project. Stored components follow the current appendix rather than the older public summary. Deepening minors are optional; the university-wide 15-EC introductory minor is not available to this cohort of Astronomy students.

Provenance: data/counselor/comparisons/cp-000210.json; source worksheet row(s) 223. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [FSE Teaching and Examination Regulations](https://www.rug.nl/fse/education/ter/?lang=en) — 2026–2027 bachelor appendix links and page modification date; Current official index; last modified 4 September 2026. Official index links the exact current appendix URLs for Chemistry, Chemical Engineering, Astronomy, Industrial Engineering and Management, Applied Physics and Applied Mathematics under 2026–2027. Index last modified 4 September 2026. This establishes current institutional publication context; it does not silently remove Chemical Engineering’s internal-year discrepancy or substitute a retrieved catalogue for an inaccessible one.
- [TER appendix BSc Astronomy 2026–2027](https://www.rug.nl/fse/education/ter/ter-2627-bsc/4-ter-bsc-astronomy-26-27.pdf) — Appendices I–IV; PDF pp. 3–6; Current 2026–2027. Mandatory Astronomy major 150 plus free minor 30. First and second years each total 60; final major is Advanced Electrodynamics 5, Astrophysical Hydrodynamics 5, Interstellar Medium 5 and research 15. Mathematics, general physics, observations, computing and astronomical research establish the core. The two 30-EC deepening minors are optional ways to fill minor space; the 15-EC university minor Astronomy through space and time is explicitly unavailable to Astronomy/Physics/Applied Physics students. The selected generic 30-EC minor therefore remains valid without inventing a named minor. Current appendix differs from the older public summary (Mathematical Physics/Cosmology); stored components follow the current appendix. Table visually inspected.

External credit structure: Stored/current total 180: years 60+60, then 15 named advanced major study, research 15 and minor 30.

Result: confirmed; required action: none.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000211 — Linguistics

Institution: University of Groningen. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-06.

Existing substantive reason: The University of Groningen bachelor requires a cumulative scientific language sequence spanning phonology, syntax, morphology, semantics, pragmatics, language acquisition and change, psycholinguistics, neurolinguistics, clinical linguistics, language and speech disorders, dyslexia, neuroimaging, statistics and advanced graduation seminars. UCR offers one dedicated Psycholinguistics course and useful neighbouring study in cognition, psychology, communication, rhetoric, AI and data science, but it has no coherent foundation in structural linguistics and no clinical- or neurolinguistics progression. A 24-course response would replace most of the target discipline with adjacent fields rather than provide a defensible Linguistics comparator.

The adopted 2026 entrant table supports the recorded 60+60+30+30 structure, four faculty-wide alternatives and three selected 10-EC graduation portfolios. The selected ordinary route keeps new-cohort Statistics/Morphology/Psycholinguistics Project weights rather than the older public second-year list. Speech-Therapy exemptions and alternative portfolio rules are acknowledged as other permitted pathways, not additions to this route.

Provenance: data/counselor/comparisons/cp-000211.json; source worksheet row(s) 224. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [OER Taalwetenschap 2026–2027](https://www.rug.nl/let/onze-faculteit/organisatie/diensten-en-voorzieningen/onderwijsinstituut/oeren/2026-2027/bacheloropleidingen/delen-b/ba-taalwetenschap-deelb.pdf) — Articles 3.2, 4.1, 5.1 and 8.3; PDF pp. 4–6, 9; Current 2026–2027. Adopted 7 July 2026, effective 1 September 2026. September 2026 ordinary route: first year 60, second year 60 including Morphology 5, Statistics 5 and Psycholinguistics Project 10, minor 30 and three of five graduation-portfolio units at 10 each. First three formally listed portfolios are Neurolinguistics, Psycholinguistics/Developmental Language Disorders and Syntax. Speech-Therapy minor participants have specific second-year exemptions and mandatory portfolio selections; those are not the selected ordinary pathway. A standalone extra thesis is not prescribed beyond the graduation portfolio. Current webpage’s older second-year list differs; formal cohort table controls. Table and footnotes visually inspected.
- [Linguistics](https://www.rug.nl/bachelors/linguistics/?lang=en) — Facts, faculty-wide choices and first/second/third-year descriptions; Current official prospectus; adopted OER controls cohort. Dutch, 180 EC, 56803. Confirms a theoretical and neuro/clinical linguistic identity, four faculty-wide options and graduation research seminars. Cultural Heritage is first in the displayed faculty-wide choice list. Public second-year Morphology 10, Psycholinguistics 5 and Language/Neuroimaging 5 reflect a different listing from the adopted 2026 entrant table; they are not substituted for Morphology 5, Statistics 5 and Psycholinguistics Project 10. Selected portfolio choices remain restricted alternatives, not universally compulsory named tracks.

External credit structure: Stored/current ordinary 2026 entrant route totals 60+60+30 minor+three 10-EC graduation portfolios=180. Portfolios contain graduation research; no extra thesis is added.

Result: confirmed; required action: none.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000212 — Dentistry (Tandheelkunde)

Institution: University of Groningen. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-06.

Existing substantive reason: The defining 180-ECTS curriculum is entirely compulsory and integrates oral and general health science, oral diseases, radiation protection, dental diagnosis and treatment, progressive professional and technical skills, and supervised care of real patients in the 12-ECTS Bachelor Clinic. The current UCR catalogue provides relevant biomedical science, psychology, public health and research methods, but no dentistry, oral anatomy or biology, cariology, periodontology, dental materials, restorative procedures, endodontology, dental radiography, preclinical simulation, treatment planning or supervised clinical dental care. A 24-course UCR programme could reproduce parts of the biomedical and behavioural context but would omit the profession-defining dental science, manual skills and patient treatment. It would therefore not be a defensible closest match.

The adopted current Dentistry OER and published patient-care description support all 29 required components, 60+60+60 EC, staged skills and the 12-EC supervised clinic. No track, minor or elective space applies to the selected ordinary bachelor. Browser concept metadata does not negate explicit adoption/current publication. Thesis/scientific work is embedded; full professional qualification also requires the master.

Provenance: data/counselor/comparisons/cp-000212.json; source worksheet row(s) 225. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [OER Bachelor Tandheelkunde 2026–2027](https://www.rug.nl/umcg/education/tandheelkunde/belangrijkedocumententhk/documenten2627/oerthkbachelor2627.pdf) — Cover adoption; Articles 3.3–3.6, 4.1, 7.1 and 9.3; PDF pp. 1, 9–11, 15–16, 21–22; Adopted 2026–2027; 20 May 2026. Adopted 20 May 2026. Ordinary Dutch/full-time programme has no tracks, minor space or elective components. All 29 units total 60+60+60=180. Third year includes professional skills 12, scientific skills/research 8, supervised Bachelor Clinic 12 and other oral-health/diagnosis/radiation-protection/context study. Clinic entry requires completed first year, both second-year professional-skills units, oral-healthcare context 2, three of four theory units and scientific skills 2. Separate shortened-entry programmes are not stacked onto the ordinary bachelor. Scientific work/thesis is embedded, not extra credit. Current title and adopted text control over browser concept metadata. Table visually inspected.
- [Tandheelkunde](https://www.rug.nl/bachelors/dentistry/) — Facts and clinical progression; Current official prospectus. Dutch/full-time 180-EC bachelor, 56560. Practical training begins with artificial jaws/teeth, followed by diagnostics and supervised patient treatment; third-year students share a treatment chair and treat non-complex patients. Bachelor research/thesis is completed alongside the clinical sequence. The full professional qualification includes a subsequent three-year master, so bachelor clinical formation is not itself a claim of completed dentist licensure.
- [Belangrijke documenten Tandheelkunde](https://www.rug.nl/umcg/education/tandheelkunde/belangrijkedocumententhk/) — Current OER link and last-modified date; Current official index; last modified 21 September 2026. Official documents page links the exact 2026–2027 Bachelor Dentistry OER, current guide and assessment plan. Last modified 21 September 2026. The published governing OER’s explicit adoption statement resolves the concept metadata concern; no inaccessible draft is substituted.

External credit structure: Stored/current 29 compulsory units total 60+60+60=180. Clinical and scientific activities are integrated within those weights; no minor, elective or additional uncredited thesis is added.

Result: confirmed; required action: none.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000213 — Industrial Engineering and Management

Institution: University of Groningen. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-06.

Existing substantive reason: Groningen explicitly defines Industrial Engineering and Management as a predominantly technical engineering degree: two-thirds technical science and one-third business. The selected pathway combines calculus, linear algebra, statistics, programming, materials and transport phenomena with engineering-system dynamics, complex-system design, mechanics, signals, control, CAD and manufacturing, production techniques, construction, mechanical craftsmanship and a 20-ECTS industrial integration project. UCR can reproduce meaningful business, data, programming, mathematics, sustainability and product-design context, but it has no coherent mechanics, materials, transport, manufacturing, control-engineering, construction or workshop sequence and no comparable industrial-engineering capstone. A 24-course UCR programme would therefore shift the degree's centre of gravity from engineering to general business and data study rather than constitute a defensible closest match.

The current appendix supports the complete selected Production Technology and Logistics pathway: first year 60, common advanced core 30, specialisation 40, minor 30 and integration project 20. Its engineering/workshop/design core is supported. The official two-thirds technical description is contextual, not an extra credit partition; other specialisation/minor alternatives remain alternatives.

Provenance: data/counselor/comparisons/cp-000213.json; source worksheet row(s) 226. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [FSE Teaching and Examination Regulations](https://www.rug.nl/fse/education/ter/?lang=en) — 2026–2027 bachelor appendix links and page modification date; Current official index; last modified 4 September 2026. Official index links the exact current appendix URLs for Chemistry, Chemical Engineering, Astronomy, Industrial Engineering and Management, Applied Physics and Applied Mathematics under 2026–2027. Index last modified 4 September 2026. This establishes current institutional publication context; it does not silently remove Chemical Engineering’s internal-year discrepancy or substitute a retrieved catalogue for an inaccessible one.
- [TER appendix BSc Industrial Engineering and Management 2026–2027](https://www.rug.nl/fse/education/ter/ter-2627-bsc/10-ter-bsc-industrial-engineering-and-management-26-27.pdf) — Appendices II–IV; PDF pp. 2–6; Current 2026–2027. First year 60; common upper-year core 30; one specialisation 40; minor 30; integration project 20, total 180. Production Technology and Logistics is first and supplies eight required 5-EC units, including mechanics, systems/control, CAD/manufacturing, construction and mechanical craftsmanship. Sustainable Process Engineering is a distinct alternative, not an additional requirement. Minor permits deepening courses, university/teacher-training/business options and approved personal/abroad packages, with overlap and language-course limits. Project requires 140 EC including all first-year study and designated design-methodology study. The public second-year track total is 30, but complete formal specialisation is 40 across later years. Table visually inspected.
- [Industrial Engineering and Management](https://www.rug.nl/bachelors/industrial-engineering-and-management/?lang=en) — Facts, programme character and course tables; Current official prospectus. Current English, 180-EC BSc under 56994. University describes the programme as predominantly technical, approximately two-thirds technical science and one-third business. This describes academic character rather than a separately calculated credit partition for every minor choice. Public year tables split specialisation study across years; the formal 40-EC route total is retained.

External credit structure: Stored/current total 180: first year 60, upper common core 30, selected specialisation 40, minor 30 and integration project 20. Upper-year allocation is preserved as formally grouped rather than an invented yearly split.

Result: confirmed; required action: none.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000214 — Applied Physics

Institution: University of Groningen. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-06.

Existing substantive reason: Applied Physics is a cumulative experimental and engineering-physics degree. Its compulsory formation progresses through mechanics and relativity, electromagnetism, quantum and thermal physics, waves and optics, atomic and solid-state physics, fluid physics, materials science, electronics, signal processing, device physics, control engineering, instrumentation and nanofabrication. Four staged laboratory/design components and a 15-ECTS Applied Physics research project integrate that disciplinary sequence. UCR provides useful mathematics, programming, data, robotics and sustainable-energy applications, but no disciplinary physics sequence, experimental-physics laboratories, materials/device/instrumentation formation or physics research capstone. A UCR programme assembled from quantitative and adjacent technology courses would not be a defensible Applied Physics comparator.

Current adopted/published appendix supports the complete 180-EC Applied Physics pathway, compulsory laboratories, three coherent restricted choices and accepted bachelor-level control study. Its deepening minor does not create an omitted 30-EC open-choice entitlement. Current formal Differential Equations controls over the public Mathematical Physics label; the record already explains that source distinction.

Provenance: data/counselor/comparisons/cp-000214.json; source worksheet row(s) 227. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [FSE Teaching and Examination Regulations](https://www.rug.nl/fse/education/ter/?lang=en) — 2026–2027 bachelor appendix links and page modification date; Current official index; last modified 4 September 2026. Official index links the exact current appendix URLs for Chemistry, Chemical Engineering, Astronomy, Industrial Engineering and Management, Applied Physics and Applied Mathematics under 2026–2027. Index last modified 4 September 2026. This establishes current institutional publication context; it does not silently remove Chemical Engineering’s internal-year discrepancy or substitute a retrieved catalogue for an inaccessible one.
- [TER appendix BSc Applied Physics 2026–2027](https://www.rug.nl/fse/education/ter/ter-2627-bsc/2-ter-bsc-applied-physics-26-27.pdf) — Appendices I–IV; PDF pp. 3–7; Current 2026–2027. One Applied Physics major and a deepening Applied Physics minor, not generic free-minor space. Current tables give 60+60+60=180. Four laboratory/design units are compulsory. Final year has six compulsory 5-EC technical units, three restricted choices of 5 each and research 15. Selected Atoms and Molecules, Principles of Measurement Systems and Nanoprobing/Nanofabrication are first in their distinct groups. Control Engineering for BME is expressly accepted at appropriate bachelor level despite its master code. Current first-year Differential Equations controls over public Mathematical Physics summary and legacy browser metadata. Table visually inspected.

External credit structure: Stored/current total 180 with years 60+60+60. Final 60 is six required 5-EC units, three selected 5-EC choices and research 15; the deepening minor is represented within that technical structure, not added.

Result: confirmed; required action: none.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000215 — Applied Mathematics

Institution: University of Groningen. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-06.

Existing substantive reason: The Groningen bachelor is a full disciplinary Applied Mathematics degree. Its 165-ECTS major builds from proof-based analysis, calculus, sets and numbers, graph theory, two linear-algebra courses, probability, programming, mechanics and linear systems into topology, complex and functional analysis, multivariable analysis, ordinary and partial differential equations, numerical analysis, optimization, mathematical modelling, computational science, advanced systems and modelling projects, and a 15-ECTS Applied Mathematics research project. UCR offers a useful six-course mathematics sequence plus programming, data science and selected computational applications, but it does not provide the breadth, depth or staged project and research spine required for a 24-course Applied Mathematics programme. A UCR programme assembled from mathematics, AI, data science and applications would be a coherent quantitative or computational pathway, not a defensible substitute for the target degree.

Current requirements support the selected 165-major/15-minor Applied Mathematics pathway at 180 EC and all neutral restricted selections without duplication. Permitted 30-EC abroad/education alternatives replace 15 major EC; they do not undermine the chosen ordinary route. The third project option is marked for 2027–2028 and is not needed for the two selected available projects.

Provenance: data/counselor/comparisons/cp-000215.json; source worksheet row(s) 228. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [FSE Teaching and Examination Regulations](https://www.rug.nl/fse/education/ter/?lang=en) — 2026–2027 bachelor appendix links and page modification date; Current official index; last modified 4 September 2026. Official index links the exact current appendix URLs for Chemistry, Chemical Engineering, Astronomy, Industrial Engineering and Management, Applied Physics and Applied Mathematics under 2026–2027. Index last modified 4 September 2026. This establishes current institutional publication context; it does not silently remove Chemical Engineering’s internal-year discrepancy or substitute a retrieved catalogue for an inaccessible one.
- [TER appendix BSc Applied Mathematics 2026–2027](https://www.rug.nl/fse/education/ter/ter-2627-bsc/1-ter-bsc-applied-mathematics-26-27.pdf) — Appendices II–IV; PDF pp. 5–9; Current 2026–2027. Selected ordinary route is major 165 plus minor 15, total 180: first year 60 and later major requirements 105. Applied Mathematics first-year project matches the named degree. Project Mathematical Modelling/Systems Theory and Numerical Linear Algebra/Advanced Systems Theory are the first available selections in two distinct choose-two groups. Statistical Modelling fills the further 5-EC elective without duplication. Preparation 5 and research 15 remain distinct. Other approved electives are possible. A permitted 30-EC abroad/education minor replaces the 10-EC advanced-choice pair and 5-EC elective, reducing major to 150; it does not add 15 EC. Table visually inspected.

External credit structure: Stored/current ordinary route totals 180: first year 60, later major 105 and minor 15. Alternative 30-minor route reduces the major by the advanced pair 10 plus elective 5, preserving the same total.

Result: confirmed; required action: none.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

## Remaining work and next batch

All 19 scope exclusions are complete. Fifty-one of 140 exceptions have received the first-stage audit; 89 remain pending. The next batch is: cp-000216, cp-000217, cp-000244, cp-000246, cp-000247, cp-000248, cp-000249, cp-000250, cp-000251, cp-000252.

Completed and pending entries reconcile exactly to 159 cases by audit_population + counselor_programme_id: 70 unique completed keys and 89 unique pending keys, with no overlap or omissions. All 60 earlier case objects, source entries and batch evidence sections are preserved. Pending entries have no audit finding. A completed still-unresolved finding is a completed research result, not a pending inventory entry. Production population counts remain unchanged until later corrections are implemented.

After the exhaustive audit, consolidate the action queue and execute targeted remediation with exact field changes, source evidence, dependencies and closure checks. Batch-5/6/7 actionable entries already carry structured plans; earlier entries retain their original recommendations. Keep CP198/CP199 under one shared correction task, preserving the distinction from generic CP200. Close external/registry corrections independently of the later UCR feasibility stage. Research-dependent work resumes on its stated trigger.

Stage two will independently assess UCR feasibility for every current no-defensible-ucr-match record and any resolved external case requiring a final fit decision. Confirmation here establishes only the stated external/registry basis. The exhaustive first-stage audit remains in progress.

## Production-data boundary

Only this report and data/counselor/qc/stage1-completeness-exceptions.json are written. No registry file, comparison, exception decision, production rule or other existing production data is changed.
