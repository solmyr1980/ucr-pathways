# Counselor completeness and exceptions: first-stage audit

Status: in progress. Batches 1–9 completed on 7 October 2026: all 19 scope exclusions and 71 exceptions audited within the first-stage scope. 69 exceptions remain pending.

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
| Completed exceptions | 140 | 71 | 69 |
| Excluded normalized targets | 19 | 19 | 0 |
| First-stage audit cases | 159 | 90 | 69 |

All 441 in-scope IDs have a canonical filename; there are no missing in-scope IDs, duplicate record filenames or out-of-scope canonical records. The review-index ID set matches both registry scope and canonical filenames. Status totals use that current generated index; all 140 indexed exceptions were additionally read directly to verify ID, exception status and formal type. Enumeration does not constitute a substantive exception audit.

| Formal exception type | Corpus total | Substantively audited |
|---|---:|---:|
| external-programme-unresolved | 20 | 7 |
| no-defensible-ucr-match | 117 | 62 |
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

## Cumulative findings after batch 8

| Finding | Count |
|---|---:|
| confirmed | 59 |
| incorrect | 17 |
| outdated | 0 |
| still-unresolved | 4 |

| Required action | Count |
|---|---:|
| none | 54 |
| reprocess-as-comparison | 0 |
| reassess-exception | 18 |
| correct-registry-and-reprocess | 5 |
| research-again-later | 3 |

## Batch 8 findings

Three findings are confirmed within the external-programme scope; seven are incorrect in the stated allocation, narrative, source or normalized-language facts. Groningen Theology and Mathematics and joint Delft/Leiden Life Science and Technology are supported. Tilburg Theology’s alleged missing three credits are resolved by the current cohort appendix: Torah/Prophetic Literature carries 6, not the webpage’s 3. Current Delft Architecture modules, Civil Engineering restrictions and Electrical Engineering weights/options are now explicit. Industrial Design components are accurate but its compulsory-study narrative overstates year two. Aerospace Engineering’s supported pre-2027 curriculum is retained; its normalized NLD-only language must be corrected to ENG.

Clinical Technology’s old chart repeats year-two codes and implies a 15 minor; current regulations prescribe minor 30 and four final-year major units. The current rules themselves print 61 credits in year two and 181 overall, including placement 4.5. The duplicate/minor/title correction is established, while complete 180 reconstruction remains blocked on official one-credit reconciliation. This is recorded as a secondary unresolved finding rather than an additional primary case. No UCR feasibility outcome is inferred, no weight is silently adjusted, and no outdated finding is assigned without dated support for an earlier valid decision.

Official webpages and PDFs were retrieved directly where web retrieval returned 403 or application shells. Formal tables and figures were visually reviewed. Tilburg’s public reader was inspected through its own public document API; its current cohort appendix governs despite stale general-body effective-date text.

| ID | Programme | Formal type | Finding | Required action |
|---|---|---|---|---|
| cp-000216 | Theology | no-defensible-ucr-match | confirmed | none |
| cp-000217 | Mathematics | no-defensible-ucr-match | confirmed | none |
| cp-000244 | Theology | no-defensible-ucr-match | incorrect | reassess-exception |
| cp-000246 | Bachelor Architecture, Urbanism and Building Sciences | no-defensible-ucr-match | incorrect | reassess-exception |
| cp-000247 | Bachelor Civil Engineering | no-defensible-ucr-match | incorrect | reassess-exception |
| cp-000248 | Bachelor Electrical Engineering | no-defensible-ucr-match | incorrect | reassess-exception |
| cp-000249 | Bachelor Industrial Design Engineering | no-defensible-ucr-match | incorrect | reassess-exception |
| cp-000250 | Bachelor Clinical Technology | no-defensible-ucr-match | incorrect | reassess-exception |
| cp-000251 | Bachelor Life Science and Technology | no-defensible-ucr-match | confirmed | none |
| cp-000252 | Bachelor Aerospace Engineering | no-defensible-ucr-match | incorrect | correct-registry-and-reprocess |

## Batch 8 evidence and implementation plans

### cp-000216 — Theology

Institution: University of Groningen. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-06.

Existing substantive reason: The selected Groningen pathway is defined by sustained disciplinary Theology: theology-specific concepts and methods; biblical Hebrew and Greek; the Hebrew Bible, New Testament and their exegesis; the history and thought of Christianity; practical and systematic theology; dogmatics; biblical, historical, intercultural and ethical theology; Islam and Judaism in theological context; a dedicated specialization; and a 10-ECTS Theology thesis. UCR offers adjacent philosophy, ethics, sociology, history, politics, literature, art history and cultural analysis, but no course or sequence in Theology, biblical languages, scriptural exegesis, dogmatics, systematic or practical theology, or theological research. A 24-course humanities and social-science programme could examine ideas, culture and institutions around religion, but it would erase the target's defining theological formation and would not be a defensible comparison.

Current adopted rules support the representative PThU-with-Greek 180-EC pathway, its replacements and neutral specialisation choice. The specific theological/language requirements are correctly scoped to the selected route.

Provenance: data/counselor/comparisons/cp-000216.json; source worksheet row(s) 229. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [TER BA Theology 2026–2027](https://www.rug.nl/rcs/education/studyguide/oer-26-27/ter-ba-th-26-27.pdf) — Adoption, articles 3.4–3.6, 4.1, 7.1; PDF pp. 2, 9–10, 14–16; Current 2026–2027. Adopted 27 August 2026, approved 8 July; Dutch, full/part-time, 180 EC. Selected PThU-with-Greek variant has eight 7.5-EC first-year units, substituting Practical Theology; eight 7.5-EC second-year units, substituting Psychology/Sociology and Dogmatics; third year four PThU units 30, specialisation 7.5, seminar 7.5, science communication 5 and thesis 10. Origins of Religion is first-listed. Other Greek/PThU variants and approved replacements remain alternatives. Tables visually inspected.
- [Theology prospectus](https://www.rug.nl/bachelors/theology/) — Dutch degree facts and four variants, year-two representative table; Current undated official prospectus. Current 180-EC Theology, 56109, Dutch. Public description calls PThU with Greek the most chosen year-two variant, and describes both the outside academic perspective and PThU theological perspective. This supports the stored representative choice for the generic degree; PThU and Greek are selected-route requirements, not universal requirements of every variant.

External credit structure: Selected current route 60+60+60=180; four PThU third-year units total 30; final remainder 30.

Result: confirmed; required action: none.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000217 — Mathematics

Institution: University of Groningen. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-06.

Existing substantive reason: The Groningen bachelor is a full disciplinary Mathematics degree. Its 150-ECTS major develops proof-based analysis, sets and numbers, graph theory, two courses in both calculus and linear algebra, probability, programming, mechanics and linear systems into group theory, topology, complex and functional analysis, multivariable analysis, geometry, partial differential equations, numerical analysis, dynamical systems, algebraic structures, specialist mathematical projects and a 15-ECTS Mathematics research project. UCR offers a useful six-course mathematics sequence plus programming, algorithms, data science and quantitative applications, but it does not provide the breadth, theoretical depth, proof progression or research spine required for a Mathematics bachelor. A UCR programme assembled from mathematics, computing and data science would be a coherent quantitative pathway, not a defensible substitute for the target degree.

Current formal 150-major/30-minor structure and all selected requirements agree. Statistical Reasoning is annotated 2027/28, which fits year two of the 2026 entrant; no fabricated current-year availability or yearly upper-major split is needed.

Provenance: data/counselor/comparisons/cp-000217.json; source worksheet row(s) 230. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [TER appendix BSc Mathematics 2026–2027](https://www.rug.nl/fse/education/ter/ter-2627-bsc/12-ter-bsc-mathematics-26-27.pdf) — Appendices II–IV; PDF pp. 5–9; Current 2026–2027. Major 150, minor 30: common first year 60, later major 90. Named-degree first-year project; Dynamical Systems and Algebraic Structures are first two in choose-two group. First next-group Project Statistical Reasoning is explicitly 2027/28, appropriate for year two of a September 2026 entrant; Cryptography/Chaos alternatives are 2026/27. First unused elective is Project Systems Theory. Research preparation 5 and project 15 are separate; project requires 150 EC. Minor excludes research traineeship/internship. Current FSE index links exact appendix. Table visually inspected.
- [Mathematics prospectus](https://www.rug.nl/bachelors/mathematics/?lang=en) — Facts and theoretical curriculum; Current official prospectus. English, full-time, 180 EC, 56980. Proof-based algebra, topology, analysis and probability form the degree identity; first year shared with Applied Mathematics. Undated public overview does not override the formal alternate-year choice annotations.

External credit structure: Major 150 including first 60 and later 90, plus minor 30. Statistical Reasoning 27/28 is reachable after first year 2026/27; no unsupported second/third-year 60/60 placement invented.

Result: confirmed; required action: none.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000244 — Theology

Institution: Tilburg University. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-09-29.

Existing substantive reason: The programme's defining academic identity is Catholic theology and theology-specific method: biblical Hebrew, Greek and Latin; Old and New Testament exegesis; fundamental and systematic theology; dogmatics; spirituality; practical theology; liturgy and sacraments; church history; canon law; Judaism; Catholic ethics; patristics; and an independent Theology thesis. Only the 30-ECTS mobility/minor window is broadly open. UCR offers adjacent philosophy, ethics, history, sociology, politics, law, literature and cultural analysis, but no sustained theology, scripture, source-language, liturgical or pastoral curriculum. Constructing a 24-course UCR programme from those neighbouring fields would remove the target's defining theological sequence and misrepresent it as a substantive match.

Current cohort appendix resolves the alleged missing three credits: Torah and Prophetic Literature is 6 EC, not the webpage’s 3. Complete course-level 180 reconstruction is available. Preserve generic mobility space, embedded skills and conditional language replacements.

Provenance: data/counselor/comparisons/cp-000244.json; source worksheet row(s) 257. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Fresh rc-0034 merges ordinary Tilburg/English and Utrecht/Dutch full/part-time deliveries. Current facts corroborate 180,locations,languages and modes; English display translation does not exclusively name English delivery.

Current official sources (checked 7 October 2026):

- [Theology programme and courses](https://www.tilburguniversity.edu/education/bachelors-programs/theology/program-and-courses) — 2026 entrant tables and delivery facts; Current 2026–2027. English Tilburg and Dutch Utrecht; ordinary full-time 180 EC, ordinary part-time 180 at slower pace; separate prior-degree shortened pathway. Public tables show Old Testament: Torah and Prophetic Literature as 3 EC, producing a 27-EC year-two first semester. Minor/mobility 30 and thesis 9 are supported. This display gap is resolved by the current formal cohort appendix, where the same course is 6 EC.
- [Published TST Education and Examination Regulations 2026–2027](https://oer.tilburguniversity.edu/183b1eaf-bb6b-4ff0-bee5-e9b4e5a536e9/) — Public university reader; published version 14 September 2026 and degree-specific Appendix I §11; Published 14 September 2026; cohort appendix 2026–2027. Current university reader exposes the published English TST 2026–2027 document and Appendix I for Theology cohort 2026–2027. The general HTML body retains a stale 2025–2026 entry-into-force clause; use the explicitly current cohort appendix for reconstruction and retain that publication caveat. Public reader data were retrieved through its documented public API, without login.
- [Appendix I: programme-specific Theology requirements 2026–2027](https://api.docfield.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6IjNmNjY5NTUwLTViNjQtNDkwNy1iZGIyLTFhNGU3ZTdhMjJhYSIsInB1ciI6ImJsb2JfaWQifX0=--371a54676e9e4f62ebdd3edf5837e2b96baf014d/Appendix%20I%202026-2027.pdf) — §§3–5, 10–11; appendix PDF pp. 12–16, printed pp. 55–59; Explicit September 2026 cohort. English full-time cohort 9A201-2026 is explicitly sequenced 2026/27, 2027/28, 2028/29. Torah/Prophetic Literature U20074-B-6 is 6 EC, yielding 30 in each semester and 180 overall. Minor/mobility 30, final semester 21 taught plus thesis 9. Skills 12 are embedded in named courses, not extra credits. Latin replacement for intended teacher-training master requires Board request; Greek exemptions also conditional. Rotating units appear once in the cohort schedule. Tables and legend visually inspected.

External credit structure: Stored blocks 180, but their year-two note lists only 27 in first semester. Formal Torah 6 resolves that to 30; exact current cohort 60+60+60=180.

Verified reconstruction for later external remediation (audit evidence only):

| Study year | Component | EC | Status / qualification |
|---|---|---:|---|
| 1 | Biblical Hebrew 1 (U10108-B-3) | 3 | required |
| 1 | Theological Seminar (U10102-B-3) | 3 | required |
| 1 | Bible and Exegesis (introduction) (U10103-B-6) | 6 | required |
| 1 | Comparative Religion (U10106-B-6) | 6 | required |
| 1 | History of Philosophy (U10105-B-6) | 6 | required |
| 1 | History of European Christianity: theological, cultural and philosophical currents (U10104-B-6) | 6 | required |
| 1 | Biblical Hebrew 2 (U10116-B-3) | 3 | required |
| 1 | Greek 1 (U10101-B-3) | 3 | required |
| 1 | Fundamental Theology and Dogmatics (U10109-B-6) | 6 | required |
| 1 | Ethics and Character (U11012-B-3) | 3 | required |
| 1 | Spirituality (introduction) (U11013-B-3) | 3 | required |
| 1 | Systematic Philosophy (U10110-B-6) | 6 | required |
| 1 | Practical Theology (introduction) (U10111-B-6) | 6 | required |
| 2 | Greek 2 (U10107-B-3) | 3 | required |
| 2 | Latin 1 (U20079-B-3) | 3 | required |
| 2 | Dogmatics: Christ and Trinity (U20095-B-6) | 6 | required |
| 2 | Sociology and Psychology of Religion (U20083-B-6) | 6 | required |
| 2 | Canon Law (introduction) (U20080-B-3) | 3 | required |
| 2 | Judaism (introduction) (U20081-B-3) | 3 | required |
| 2 | Old Testament: Torah and Prophetic Literature (U20074-B-6) | 6 | required |
| 2 | Latin 2 (U20077-B-3) | 3 | required |
| 2 | New Testament: Synoptic Gospel and Johannine Literature (U20068-B-6) | 6 | required |
| 2 | Church History: Middle Ages and Modernity (U20070-B-6) | 6 | required |
| 2 | Dogmatics: Creation, Church and Completion (U20093-B-6) | 6 | required |
| 2 | Judaism: Reading Rabbinic Texts (U20082-B-3) | 3 | required |
| 2 | New Testament: Acts and Letters (U20069-B-3) | 3 | required |
| 2 | Old Testament: Wisdom Literature and Psalms (U20073-B-3) | 3 | required |
| 3 | Mobility window / minor | 30 | open-choice |
| 3 | Bachelor Thesis in Theology (U30021-B-9) | 9 | required |
| 3 | Catholic Ethics in Practice (U11011-B-6) | 6 | required |
| 3 | Liturgy and Sacraments (U20097-B-6) | 6 | required |
| 3 | Philosophy of Religion and Metaphysics (U20072-B-3) | 3 | required |
| 3 | Moral Philosophy (U20076-B-3) | 3 | required |
| 3 | Patristics (U20071-B-3) | 3 | required |

Total: **180 EC**; study-year totals **60 + 60 + 60**. Verified external reconstruction for later remediation; production unchanged and UCR fit unassessed.

Choice and source-context rules:

- Torah/Prophetic Literature 6 resolves the webpage gap; no invented extra methods unit.
- Embedded skills 12 are included in course weights.
- Cohort schedule places rotating compulsory units once; other deliveries/paces and conditional language replacements are alternatives.

Result: incorrect; required action: reassess-exception.

Incorrect applies to the stated external allocation, narrative, source-context or normalized metadata issue; no independent UCR conclusion or unsupported dated-change inference.

Recommended follow-up: Replace unsupported gap inference with the formal 6-EC course and reconstruct the ordinary cohort at course level; align source/choice notes and delivery-selection rationale.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

Implementation plan — **not implemented; audit only**:

- `data/counselor/decisions/cp-000244.json`, fields: `sources`, `comparator.components tuples`, `comparator.primarySource/additionalSources`, `comparator.sourceNotes`, `routeSelection where applicable`, `exception.curriculumContext`, `exception.reason where a factual correction is needed`, `exception.checkedOn`. Apply the case-specific correction below first in its existing version-2 compact academic decision, then compile canonical record. Preserve prior UCR evidence as historical provenance pending separate feasibility assessment.
- `data/counselor/comparisons/cp-000244.json`, fields: `comparator.components`, `comparator.sourceNotes`, `comparator.academicYear`, `comparator.primarySourceUrl/additionalSourceUrls`, `comparator.routeSelection where applicable`, `exception.curriculumContext`, `exception.reason where needed`, `exception.checkedOn`. Replace unsupported gap inference with the formal 6-EC course and reconstruct the ordinary cohort at course level; align source/choice notes and delivery-selection rationale. Use U20074-B-6 for Torah/Prophetic Literature 6 and all explicitly scheduled cohort courses. Drop missing-three-credit inference and any suggestion of an unidentified extra research-skills course; embedded skills 12 add no credits. Retain English full-time as an ordinary representative delivery, rather than claiming English translation of the combined registry display names an exclusive English target. Qualify Latin replacement and Greek exemptions, keeping ordinary language pathway selected. Record stale general-body effective dates separately from the explicitly 2026 cohort appendix.
- `data/counselor/review-programmes.json and existing generated counselor artifacts`, fields: `affected curriculum/source/choice summaries`. Regenerate affected summaries after canonical compilation through the existing production workflow.

Dependencies:

- Current official evidence resolves the stated ordinary allocation, except any explicit case-specific blockers recorded below.
- Final UCR feasibility remains a separate stage-two task.

Verification and closure checks:

- Compact decision recompiles to corrected canonical record; run exception-specific schema/record checks when implementing.
- Reconcile every mandatory/restricted/open component to 180 without duplicated alternatives, embedded skills or project credits.
- Canonical and generated summaries agree; close external correction separately from UCR feasibility.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000246 — Bachelor Architecture, Urbanism and Building Sciences

Institution: Delft University of Technology. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-09-29.

Existing substantive reason: The defining academic identity of TU Delft's bachelor is a sustained, cumulative spatial-design and building-science education. Its centre is architectural and urban design studios supported by drawing and representation, structural design, applied mechanics, building physics, materials and construction, architectural technology, urbanism, landscape architecture, geo-information and built-environment management. Design alone occupies 60 EC in the official programme framework, and the remaining curriculum integrates technical and historical knowledge into projects at building, neighbourhood and city scales. UCR offers isolated adjacent courses in sustainability, spatial planning, GIS, heritage, consumer-product design and nature-based engineering, but it has no architecture or urban-design studio sequence, no building-technology and structural-mechanics sequence, and no progressive education in construction, architectural representation or integrated building design. A 24-course UCR programme assembled from adjacent liberal-arts, sustainability and data courses would therefore remove the target's defining design-studio and engineering spine and misrepresent it as an academic match.

The 180 arithmetic and broad design identity are supported, but three year-total placeholders hide the documented 150-EC required module structure, 30-minor and four-part final synthesis. Current formal module/weight schedule is accessible.

Provenance: data/counselor/comparisons/cp-000246.json; source worksheet row(s) 259. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [Bouwkunde: what will I learn?](https://www.tudelft.nl/onderwijs/opleidingen/bachelors/bk/bsc-bouwkunde/over-de-opleiding/wat-ga-ik-leren) — Programme structure, modules and final-year work; Current official prospectus. Broad Dutch bachelor 180, five prescribed semesters and minor semester. Design modules 10 EC, other modules 5 EC. Foundations, technology, science/skills, society and architecture/urban design culminate in integrated final project with technical support and two written reflection texts. Current portal labels its schedule 2026–2027.
- [Onderwijsregelgeving Bacheloropleiding Bouwkunde 2026–2027](https://filelist.tudelft.nl/Studentenportal/Faculteitspecifiek/Bouwkunde/Onderwijs/Regulations/Onderwijsregelgeving%20Bachelor%202026-2027.pdf) — Articles 1.8–1.10, 2.24–2.28; Appendix II printed pp. 40–41; Current 2026–2027. Current formal rules: required 150 plus minor 30. Twenty-four required modules: design ON1–4/IOP1–2 six times 10=60; science/skills WV1–6 six times 5=30; technology TE1–5 five times 5=25; foundations GR1–4 four times 5=20; society MA1–3 three times 5=15. Semester chart places all modules. Final BEP consists of IOP1, IOP2, TE5, WV6=30; no extra thesis credits. This replaces the need for only three generic 60-EC year blocks. Figure visually inspected.

External credit structure: Stored three 60 blocks total 180 but conceal required modules 150 and minor 30. Verified module schedule independently totals 60+60+60.

Verified reconstruction for later external remediation (audit evidence only):

| Study year | Component | EC | Status / qualification |
|---|---|---:|---|
| 1 | Technology module TE1 (TE1) | 5 | required |
| 1 | Foundations module GR1 (GR1) | 5 | required |
| 1 | Science and skills module WV1 (WV1) | 5 | required |
| 1 | Design module ON1 (ON1) | 10 | required |
| 1 | Science and skills module WV2 (WV2) | 5 | required |
| 1 | Technology module TE2 (TE2) | 5 | required |
| 1 | Foundations module GR2 (GR2) | 5 | required |
| 1 | Science and skills module WV3 (WV3) | 5 | required |
| 1 | Design module ON2 (ON2) | 10 | required |
| 1 | Technology module TE3 (TE3) | 5 | required |
| 2 | Design module ON3 (ON3) | 10 | required |
| 2 | Society module MA1 (MA1) | 5 | required |
| 2 | Technology module TE4 (TE4) | 5 | required |
| 2 | Science and skills module WV4 (WV4) | 5 | required |
| 2 | Society module MA2 (MA2) | 5 | required |
| 2 | Design module ON4 (ON4) | 10 | required |
| 2 | Foundations module GR3 (GR3) | 5 | required |
| 2 | Society module MA3 (MA3) | 5 | required |
| 2 | Foundations module GR4 (GR4) | 5 | required |
| 2 | Science and skills module WV5 (WV5) | 5 | required |
| 3 | Minor | 30 | open-choice |
| 3 | Integrated design module IOP1 (IOP1) | 10 | required |
| 3 | Integrated design module IOP2 (IOP2) | 10 | required |
| 3 | Technology module TE5 (TE5) | 5 | required |
| 3 | Science and skills module WV6 (WV6) | 5 | required |

Total: **180 EC**; study-year totals **60 + 60 + 60**. Verified external reconstruction for later remediation; production unchanged and UCR fit unassessed.

Choice and source-context rules:

- 24 compulsory modules 150 plus minor 30.
- Final BEP consists of four existing modules 30; no extra thesis.
- Descriptive code/learning-line labels do not claim unverified official course titles.

Result: incorrect; required action: reassess-exception.

Incorrect applies to the stated external allocation, narrative, source-context or normalized metadata issue; no independent UCR conclusion or unsupported dated-change inference.

Recommended follow-up: Replace generic year blocks with current formal modules, explicit minor and integrated BEP components; add current regulation and preserve thematic descriptions without invented catalogue titles.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

Implementation plan — **not implemented; audit only**:

- `data/counselor/decisions/cp-000246.json`, fields: `sources`, `comparator.components tuples`, `comparator.primarySource/additionalSources`, `comparator.sourceNotes`, `routeSelection where applicable`, `exception.curriculumContext`, `exception.reason where a factual correction is needed`, `exception.checkedOn`. Apply the case-specific correction below first in its existing version-2 compact academic decision, then compile canonical record. Preserve prior UCR evidence as historical provenance pending separate feasibility assessment.
- `data/counselor/comparisons/cp-000246.json`, fields: `comparator.components`, `comparator.sourceNotes`, `comparator.academicYear`, `comparator.primarySourceUrl/additionalSourceUrls`, `comparator.routeSelection where applicable`, `exception.curriculumContext`, `exception.reason where needed`, `exception.checkedOn`. Replace generic year blocks with current formal modules, explicit minor and integrated BEP components; add current regulation and preserve thematic descriptions without invented catalogue titles. Use 24 required modules by official codes: ON1–4/IOP1–2 at 10; WV1–6,TE1–5,GR1–4,MA1–3 at 5; plus minor 30. Module labels may be descriptive code/learning-line labels without claiming unverified exact catalogue titles. Keep IOP1/IOP2/TE5/WV6 final 30; do not add a standalone thesis. Current programme thematic descriptions support the substantive module context.
- `data/counselor/review-programmes.json and existing generated counselor artifacts`, fields: `affected curriculum/source/choice summaries`. Regenerate affected summaries after canonical compilation through the existing production workflow.

Dependencies:

- Current official evidence resolves the stated ordinary allocation, except any explicit case-specific blockers recorded below.
- Final UCR feasibility remains a separate stage-two task.

Verification and closure checks:

- Compact decision recompiles to corrected canonical record; run exception-specific schema/record checks when implementing.
- Reconcile every mandatory/restricted/open component to 180 without duplicated alternatives, embedded skills or project credits.
- Canonical and generated summaries agree; close external correction separately from UCR feasibility.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000247 — Bachelor Civil Engineering

Institution: Delft University of Technology. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-09-29.

Existing substantive reason: TU Delft's Civil Engineering bachelor is built around a cumulative engineering spine: three structural-mechanics courses, construction materials, concrete and steel structures, soil mechanics, fluid mechanics, hydrology, hydraulic engineering, surveying, road and railway design, foundation design, dynamics and two large Bouwplaats project courses. UCR offers strong environmental, delta, water, earth-science and spatial-planning content plus useful mathematics, but it does not offer the structural, materials, geotechnical, hydraulic, transport or construction-engineering sequence on which the degree's integrated projects depend. A 24-course UCR response would therefore be an environmental-sustainability or delta-studies programme with quantitative tools, not Civil Engineering.

Current cohort requires two categorised 4-EC choices and three fixed 4-EC units, not the stored unrestricted 12-EC three-specialisation block plus old Road/Rail title. Current Water/Technology code and source-year context also require correction.

Provenance: data/counselor/comparisons/cp-000247.json; source worksheet row(s) 260. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [Civil Engineering prospectus](https://www.tudelft.nl/onderwijs/opleidingen/bachelors/civiele-techniek/bsc-civiele-techniek) — Language, three years and construction/water/transport identity; Current official prospectus. Dutch, three-year bachelor integrates construction, water and transport, mechanics, materials, foundations, fluid/soil systems and engineering projects. Minor and final research are explicit. Current faculty portal now links September 2026 curriculum and current formal regulations.
- [OER and Annex BSc Civiele Techniek 2026–2027](https://filelist.tudelft.nl/Studentenportal/Faculteitspecifiek/CiTG/Onderwijs/OER%20regels%20en%20richtlijnen%20CiTG/BSC/2026-2027%20TER%20Annex_BoE/OER_Annex%20BSc%20CT%202026-2027.pdf) — Cohort 2026–2027 Annex articles 2–4, 12; PDF pp. 20–21, 23–26; Current 2026–2027. First/second year 60 each. Water en Techniek CTB1215-26 replaces the stored Schone Watersystemen code/title. Third year minor 30, Surveying 4, Urban Water/Environmental Engineering CTB3315 4, Traffic/Transport Infrastructure CTB3325 4, bachelor project 10, one Q3 deep-dive 4 and one Q4 design choice 4. Three unrestricted specialisations are allowed only pre-2024 cohorts. First choices Climate Impacts and Engineering / Design of Water Treatment are neutral. No elective/minor overlap. Current formal code CTB1420-25 controls older code on chart. Tables visually inspected.
- [Bachelor Civiele Techniek September 2026 chart](https://filelist.tudelft.nl/Studentenportal/Faculteitspecifiek/CiTG/Onderwijs/Curriculumkaarten/2026-2027/TU%20Delft-20715-07-07-Flyers%20CT-V02.pdf) — Year tables, footer September 2026; September 2026. Current chart corroborates 60+60+60 and the 30-minor/10-project/three required four-credit units/two four-credit choice structure. It retains CTB1420-17 for Transport/Planning while formal rules prescribe CTB1420-25; formal current code controls. Bouwplaats quarter subdivisions share one aggregate 8 EC per year, not four times 8.

External credit structure: Stored 180 masks incorrect compulsory/choice classification. Current third 60=minor 30+Surveying 4+UrbanWater 4+TrafficInfrastructure 4+oneDeepDive 4+oneDesign 4+project 10.

Verified reconstruction for later external remediation (audit evidence only):

| Study year | Component | EC | Status / qualification |
|---|---|---:|---|
| 1 | Bouwplaats 1 (CTB1000) | 8 | required |
| 1 | Analyse voor Civiele Techniek (CTB1001-16) | 6 | required |
| 1 | Lineaire algebra voor Civiele Techniek (CTB1002) | 6 | required |
| 1 | Constructiemechanica 1 (CTB1110-17) | 5 | required |
| 1 | Inleiding Civiele en Milieu Techniek (CTB1120-17) | 5 | required |
| 1 | Water en Techniek (CTB1215-26) | 5 | required |
| 1 | Integraal ontwerpen (CTB1220-17) | 5 | required |
| 1 | Constructiemechanica 2 (CTB1310) | 5 | required |
| 1 | Bouwmaterialen en milieu (CTB1320-24) | 5 | required |
| 1 | Ontwerpen van constructies en funderingen 1 (CTB1410-20) | 5 | required |
| 1 | Transport en planning (CTB1420-25) | 5 | required |
| 2 | Bouwplaats 2 (CTB2000-25) | 8 | required |
| 2 | Differentiaalvergelijkingen voor Civiele Techniek (CTB2105) | 3 | required |
| 2 | Constructiemechanica 3 (CTB2210) | 5 | required |
| 2 | Dynamica en modelvorming (CTB1210) | 5 | required |
| 2 | Kansrekening en statistiek (CTB2200) | 3 | required |
| 2 | Grondmechanica (CTB2310) | 5 | required |
| 2 | Beton- en staalconstructies (CTB2220-25) | 5 | required |
| 2 | Dynamica van systemen (CTB2300) | 3 | required |
| 2 | Vloeistofmechanica (CTB2110) | 5 | required |
| 2 | Ontwerpen van constructies en funderingen 2 (CTB2320-17) | 5 | required |
| 2 | Numerieke Wiskunde (CTB2400) | 3 | required |
| 2 | Waterbouwkunde (CTB2410) | 5 | required |
| 2 | Hydrologie (CTB2420-17) | 5 | required |
| 3 | Minor | 30 | open-choice |
| 3 | Surveying and Mapping (CTB3310) | 4 | required |
| 3 | Urban Water and Environmental Engineering (CTB3315) | 4 | required |
| 3 | Traffic and Transport Infrastructure (CTB3325) | 4 | required |
| 3 | Climate Impacts and Engineering (CTB3311) | 4 | restricted-choice; First Q3 deep-dive option. |
| 3 | Design of Water Treatment (CTB3465) | 4 | restricted-choice; First Q4 design option. |
| 3 | Bachelor Final Project (CTB3000-16) | 10 | required |

Total: **180 EC**; study-year totals **60 + 60 + 60**. Verified external reconstruction for later remediation; production unchanged and UCR fit unassessed.

Choice and source-context rules:

- Exactly one deep-dive and one design choice, first listed in each category; no minor overlap.
- Three unrestricted specialisations belong only to pre-2024 cohorts.
- Bouwplaats 8 per year, not 8 per quarter.
- Current formal Transport/Planning code 25 controls stale chart 17.

Result: incorrect; required action: reassess-exception.

Incorrect applies to the stated external allocation, narrative, source-context or normalized metadata issue; no independent UCR conclusion or unsupported dated-change inference.

Recommended follow-up: Reconstruct 2026 cohort from controlling Annex: update water course; three fixed third-year units; one neutral first Q3 and one first Q4 choice; preserve 30-minor and 10-project.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

Implementation plan — **not implemented; audit only**:

- `data/counselor/decisions/cp-000247.json`, fields: `sources`, `comparator.components tuples`, `comparator.primarySource/additionalSources`, `comparator.sourceNotes`, `routeSelection where applicable`, `exception.curriculumContext`, `exception.reason where a factual correction is needed`, `exception.checkedOn`. Apply the case-specific correction below first in its existing version-2 compact academic decision, then compile canonical record. Preserve prior UCR evidence as historical provenance pending separate feasibility assessment.
- `data/counselor/comparisons/cp-000247.json`, fields: `comparator.components`, `comparator.sourceNotes`, `comparator.academicYear`, `comparator.primarySourceUrl/additionalSourceUrls`, `comparator.routeSelection where applicable`, `exception.curriculumContext`, `exception.reason where needed`, `exception.checkedOn`. Reconstruct 2026 cohort from controlling Annex: update water course; three fixed third-year units; one neutral first Q3 and one first Q4 choice; preserve 30-minor and 10-project. Replace CTB1215-25 with CTB1215-26 Water en Techniek 5. Replace CTB3320 Road/Rail 4 and generic specialisation 12 with CTB3315 Urban Water 4, CTB3325 Traffic/Transport Infrastructure 4, CTB3311 Climate Impacts 4 and CTB3465 Design Water Treatment 4; Surveying 4 retained. First two selected alternatives belong to distinct Q3/Q4 categories, fixed in official order, not UCR ease. Formal CTB1420-25 retained despite stale chart CTB1420-17. Other first/second-year weights unchanged.
- `data/counselor/review-programmes.json and existing generated counselor artifacts`, fields: `affected curriculum/source/choice summaries`. Regenerate affected summaries after canonical compilation through the existing production workflow.

Dependencies:

- Current official evidence resolves the stated ordinary allocation, except any explicit case-specific blockers recorded below.
- Final UCR feasibility remains a separate stage-two task.

Verification and closure checks:

- Compact decision recompiles to corrected canonical record; run exception-specific schema/record checks when implementing.
- Reconcile every mandatory/restricted/open component to 180 without duplicated alternatives, embedded skills or project credits.
- Canonical and generated summaries agree; close external correction separately from UCR feasibility.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000248 — Bachelor Electrical Engineering

Institution: Delft University of Technology. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-09-29.

Existing substantive reason: TU Delft's bachelor is a cumulative electrical-engineering education in circuit theory, analogue and digital electronics, electricity and magnetism, electrical energy, signals and systems, telecommunications and sensing, electromagnetics, semiconductor devices, mixed-signal systems, control, signal processing, computer architecture and repeated hardware-focused integrated projects before a 15-EC Electrical Engineering graduation project. UCR offers a useful mathematics, computing, data-science, robotics and renewable-energy-adjacent set, but it has no electricity-and-magnetism physics course, circuit or electronics sequence, semiconductor-device course, electrical measurements laboratory, telecommunications/sensing sequence or electrical-engineering hardware project sequence. A 24-course UCR response would be a mathematics-and-computing programme with some energy and robotics applications, not Electrical Engineering.

Current formal table exposes course-level EC and bounded choose-two electives. Stored quarter aggregation and generic electives do not reconstruct those restrictions; source claim that within-quarter weights are unavailable is incorrect. Current periods/prerequisites differ from old chart.

Provenance: data/counselor/comparisons/cp-000248.json; source worksheet row(s) 261. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [Electrical Engineering programme](https://www.tudelft.nl/onderwijs/opleidingen/bachelors/ee/bsc-electrical-engineering) — Degree facts, language requirement and defining content; Current official prospectus. The programme requires Dutch proficiency, while books and lectures are mostly English; formal course tables likewise list English and mixed project instruction. Retain the distinction between programme admission/language classification and course teaching language rather than describing every class as Dutch. Full-time electrical engineering integrates circuits, digital systems, mathematics, electromagnetism, telecommunications, energy and repeated practical projects.
- [Electrical Engineering curriculum chart 2025–2026](https://filelist.tudelft.nl/EWI/Studeren/Bacheloropleidingen/modulekaarten/BSc%20EE%20modulekaart%202025-2026%20inclusief%20kalender.pdf) — Credit axis, elective footnote, entry requirements; 2025–2026 chart still linked; current TER controls. Still linked by current EEMCS portal. Each axis block prints its EC through aligned boundaries: mostly 5-EC courses, EE2G1 10, minor 30 and graduation 15. Two electives are from five named EEX01–05 options, not unrestricted profiling. Eight early 15-EC quarters are not wholly compulsory: year two includes 5-EC elective. Current formal table supplies exact weights and controls period/prerequisite differences.
- [EEMCS bachelor OER 2026–2027: Electrical Engineering](https://filelist.tudelft.nl/Studentenportal/Faculteitspecifiek/EWI/Studeren/Reglementen/Onderwijs-%20en%20Examenregeling%20EWI%202026-2027.pdf) — Electrical Engineering articles 6–7; PDF pp. 25–29; Current 2026–2027. Complete 180: first year twelve required 5-EC units; second year nine 5-EC units, Next Generation 10 and one restricted 5; third minor 30, Signal Processing 5, Computer Architecture 5, one restricted 5 and graduation 15. Choose two distinct EEX01–05, one year two/one year three, without minor overlap; first two options are ML and Communication Networks. EE2C2 shown Q3 in formal table versus old chart Q4; current catalogue required before asserting precise timetable. Updated project prerequisites also control. Tables visually inspected.

External credit structure: Stored 180 quarter blocks conceal required 5/10 weights and two restricted 5 choices. Current selected structure 60+60+60=180; quarter placement conflict retained.

Verified reconstruction for later external remediation (audit evidence only):

| Study year | Component | EC | Status / qualification |
|---|---|---:|---|
| 1 | Introduction to Electrical Engineering (EE1G1) | 5 | required |
| 1 | Linear Circuits A (EE1C1) | 5 | required |
| 1 | Digital Systems A (EE1D1) | 5 | required |
| 1 | Linear Circuits B (EE1C2) | 5 | required |
| 1 | Calculus (EE1M1) | 5 | required |
| 1 | Integrated Project 1 (EE1L1) | 5 | required |
| 1 | Electricity and Magnetism (EE1P1) | 5 | required |
| 1 | Digital Systems B (EE1D2) | 5 | required |
| 1 | Calculus and Linear Algebra (EE1M2) | 5 | required |
| 1 | Electrical Energy Fundamentals (EE1E1) | 5 | required |
| 1 | Linear Algebra and Differential Equations (EE1M3) | 5 | required |
| 1 | Integrated Project 2 (EE1L2) | 5 | required |
| 2 | Probability and Statistics (EE2M1) | 5 | required |
| 2 | Signals and Systems (EE2S1) | 5 | required |
| 2 | Transistor Circuits (EE2C1) | 5 | required |
| 2 | Electromagnetics (EE2P1) | 5 | required |
| 2 | Telecommunication and Sensing (EE2T1) | 5 | required |
| 2 | Integrated Project 3 (EE2L1) | 5 | required |
| 2 | Systems and Control (EE2S2) | 5 | required |
| 2 | Semiconductor Physics and Devices (EE2P2) | 5 | required |
| 2 | Mixed-Signal Circuits and Systems (EE2C2) | 5 | required |
| 2 | Electrical Engineering for the Next Generation (EE2G1) | 10 | required |
| 2 | Introduction to Machine Learning (EEX01) | 5 | restricted-choice |
| 3 | Minor | 30 | open-choice |
| 3 | Signal Processing (EE3S1) | 5 | required |
| 3 | Computer Architecture and Organisation (EE3D1) | 5 | required |
| 3 | Communication Networks and Algorithms (EEX02) | 5 | restricted-choice |
| 3 | Bachelor Graduation Project Electrical Engineering (EE3L1) | 15 | required |

Total: **180 EC**; study-year totals **60 + 60 + 60**. Verified external reconstruction for later remediation; production unchanged and UCR fit unassessed.

Choice and source-context rules:

- First two distinct of five EEX options, one year 2 and one year 3; no overlap with minor.
- Known yearly totals 60; precise quarter timing remains subject to current catalogue resolving EE2C2 table/chart conflict.
- Current article 7 prerequisites replace older chart statements.

Result: incorrect; required action: reassess-exception.

Incorrect applies to the stated external allocation, narrative, source-context or normalized metadata issue; no independent UCR conclusion or unsupported dated-change inference.

Recommended follow-up: Use 2026 OER course weights; select first two distinct EEX options independently of UCR; preserve minor; explain period/prerequisite conflicts and validate current scheduling if asserted.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

Implementation plan — **not implemented; audit only**:

- `data/counselor/decisions/cp-000248.json`, fields: `sources`, `comparator.components tuples`, `comparator.primarySource/additionalSources`, `comparator.sourceNotes`, `routeSelection where applicable`, `exception.curriculumContext`, `exception.reason where a factual correction is needed`, `exception.checkedOn`. Apply the case-specific correction below first in its existing version-2 compact academic decision, then compile canonical record. Preserve prior UCR evidence as historical provenance pending separate feasibility assessment.
- `data/counselor/comparisons/cp-000248.json`, fields: `comparator.components`, `comparator.sourceNotes`, `comparator.academicYear`, `comparator.primarySourceUrl/additionalSourceUrls`, `comparator.routeSelection where applicable`, `exception.curriculumContext`, `exception.reason where needed`, `exception.checkedOn`. Use 2026 OER course weights; select first two distinct EEX options independently of UCR; preserve minor; explain period/prerequisite conflicts and validate current scheduling if asserted. Replace quarter blocks with all named formal courses; most 5, NextGeneration 10, minor 30, project 15. Choose EEX01 Introduction to Machine Learning 5 for year 2 and EEX02 Communication Networks and Algorithms 5 for year 3 as first two distinct listed options. Generic minor must exclude those selections. Replace obsolete project/prerequisite context with current article 7. OER puts Mixed-Signal Q3 whereas old chart puts Q4; avoid forcing a 15-EC quarter allocation from contradictory calendars. Retrieve applicable catalogue before asserting exact periods; yearly 60/60/60 is established.
- `data/counselor/review-programmes.json and existing generated counselor artifacts`, fields: `affected curriculum/source/choice summaries`. Regenerate affected summaries after canonical compilation through the existing production workflow.

Dependencies:

- Current official evidence resolves the stated ordinary allocation, except any explicit case-specific blockers recorded below.
- Final UCR feasibility remains a separate stage-two task.
- If a precise quarter timetable is retained, resolve formal/older-chart EE2C2 period discrepancy from current catalogue. This does not block verified course weights and yearly totals.

Verification and closure checks:

- Compact decision recompiles to corrected canonical record; run exception-specific schema/record checks when implementing.
- Reconcile every mandatory/restricted/open component to 180 without duplicated alternatives, embedded skills or project credits.
- Canonical and generated summaries agree; close external correction separately from UCR feasibility.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000249 — Bachelor Industrial Design Engineering

Institution: Delft University of Technology. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-03.

Existing substantive reason: TU Delft's bachelor is a cumulative design education built around five substantial design projects, including a 15-EC bachelor final project, and a compulsory progression through design methods and research, human-centred design, digital interfaces, intelligent products, product engineering, sustainability, futures and organisational value. UCR offers one strong consumer-product-design course and useful adjacent courses in entrepreneurship, consumer research, psychology, data, software, robotics, sustainability and creative communication. It does not offer the repeated studio/project spine, industrial-design visualisation and form-giving sequence, ergonomics and usability sequence, materials and manufacturing progression, physical and digital prototyping sequence, or integrated product-engineering formation needed to represent Industrial Design Engineering. A 24-course UCR response would therefore be a liberal-arts programme with one product-design experience and several adjacent subjects, not a defensible disciplinary comparator.

All stored components and their 180 total agree with current image, but source/context narrative overstates compulsory second-year study: semester four includes 20 EC of four category-specific elective slots.

Provenance: data/counselor/comparisons/cp-000249.json; source worksheet row(s) 262. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [Industrial Design: what will I learn?](https://www.tudelft.nl/onderwijs/opleidingen/bachelors/industrieel-ontwerpen/bsc-industrieel-ontwerpen/over-de-opleiding/wat-ga-ik-leren) — People, organisations, technology; electives and programme chart; Current official prospectus. Current Dutch bachelor integrates design projects with people, organisations and technology; second-year semester four offers choices within People, Technology, Organisations and Skills. Genuine profiling categories may remain generic, with required category allocation retained. Current page links the exact 2026–2027 image.
- [Industrial Design Engineering curriculum 2026–2027](https://filelist.tudelft.nl/IO/Studeren/Bacheloropleiding/BSc%20Curriculum_2026_2027_met%20code%20en%20slots.png?hash=37c0a865d7) — All semester blocks and credits; Current 2026–2027. First year required 60. Year two required semester three 30 plus Design Project 4 ten, and four distinct category electives of 5 each. Third year minor 30 plus elective slots 15 and final design project 15. Five design projects total 55; other required study 60; total required 115 and profiling/choice 65. Stored component list is accurate; describing all first four semesters as compulsory is not. Image visually inspected.

External credit structure: Stored component list 180 is supported. Required 115, four category choices 20, final elective 15 and minor 30. Year 2 compulsory 40 plus category choices 20.

Verified reconstruction for later external remediation (audit evidence only):

| Study year | Component | EC | Status / qualification |
|---|---|---:|---|
| 1 | Design Project 1 (IOB1-1-26) | 10 | required |
| 1 | Understanding Product Engineering (IOB1-2) | 5 | required |
| 1 | Understanding Design (IOB1-3) | 5 | required |
| 1 | Understanding Organisations (IOB1-4) | 5 | required |
| 1 | Understanding Humans (IOB1-5-24) | 5 | required |
| 1 | Design Project 2 (IOB2-1-26) | 10 | required |
| 1 | Digital Interfaces (IOB2-2-24) | 5 | required |
| 1 | Research for Design (IOB2-3) | 5 | required |
| 1 | Understanding Values (IOB2-4) | 5 | required |
| 1 | Intelligent Products (IOB2-5-24) | 5 | required |
| 2 | Design Project 3 (IOB3-1-24) | 10 | required |
| 2 | Sustainable Impact (IOB3-2-23) | 5 | required |
| 2 | Data Foundations (IOB3-3-22) | 5 | required |
| 2 | Envisioning Futures (IOB3-4-25) | 5 | required |
| 2 | Product Engineering (IOB3-5-23) | 5 | required |
| 2 | Design Project 4 (IOB4-1-24) | 10 | required |
| 2 | Elective Organisations (IOB4-Bx) | 5 | profiling-choice |
| 2 | Elective Skills (IOB4-Sx) | 5 | profiling-choice |
| 2 | Elective Technology (IOB4-Tx) | 5 | profiling-choice |
| 2 | Elective People (IOB4-Px) | 5 | profiling-choice |
| 3 | Minor | 30 | open-choice |
| 3 | Elective slot A (IOB6-Ex-A) | 5 | profiling-choice |
| 3 | Elective slot B (IOB6-Ex-B) | 5 | profiling-choice |
| 3 | Elective slot D (IOB6-Ex-D) | 5 | profiling-choice |
| 3 | Design Project 5 – Bachelor Final Project (IOB6-1-22) | 15 | required |

Total: **180 EC**; study-year totals **60 + 60 + 60**. Verified external reconstruction for later remediation; production unchanged and UCR fit unassessed.

Choice and source-context rules:

- Keep genuine minor and named profiling slots explicit; no invented optional contents.

Result: incorrect; required action: reassess-exception.

Incorrect applies to the stated external allocation, narrative, source-context or normalized metadata issue; no independent UCR conclusion or unsupported dated-change inference.

Recommended follow-up: Correct compulsory/profiling narrative; retain accurate component weights, all four category slots, 30-minor, 15 final electives and 15 final project.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

Implementation plan — **not implemented; audit only**:

- `data/counselor/decisions/cp-000249.json`, fields: `sources`, `comparator.components tuples`, `comparator.primarySource/additionalSources`, `comparator.sourceNotes`, `routeSelection where applicable`, `exception.curriculumContext`, `exception.reason where a factual correction is needed`, `exception.checkedOn`. Apply the case-specific correction below first in its existing version-2 compact academic decision, then compile canonical record. Preserve prior UCR evidence as historical provenance pending separate feasibility assessment.
- `data/counselor/comparisons/cp-000249.json`, fields: `comparator.components`, `comparator.sourceNotes`, `comparator.academicYear`, `comparator.primarySourceUrl/additionalSourceUrls`, `comparator.routeSelection where applicable`, `exception.curriculumContext`, `exception.reason where needed`, `exception.checkedOn`. Correct compulsory/profiling narrative; retain accurate component weights, all four category slots, 30-minor, 15 final electives and 15 final project. Keep the 25 accurate stored components. Describe year 1 required 60, year 2 required 40 plus four separate 5-EC category choices. Later 15 elective slots and 30-minor remain generic profiling; do not invent their content or present them as compulsory specialist courses. SourceNotes/context must agree on required 115 andchoice 65 overall.
- `data/counselor/review-programmes.json and existing generated counselor artifacts`, fields: `affected curriculum/source/choice summaries`. Regenerate affected summaries after canonical compilation through the existing production workflow.

Dependencies:

- Current official evidence resolves the stated ordinary allocation, except any explicit case-specific blockers recorded below.
- Final UCR feasibility remains a separate stage-two task.

Verification and closure checks:

- Compact decision recompiles to corrected canonical record; run exception-specific schema/record checks when implementing.
- Reconcile every mandatory/restricted/open component to 180 without duplicated alternatives, embedded skills or project credits.
- Canonical and generated summaries agree; close external correction separately from UCR feasibility.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000250 — Bachelor Clinical Technology

Institution: Delft University of Technology, Leiden University and Erasmus University Rotterdam. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-03.

Existing substantive reason: Clinical Technology is an integrated medical-engineering and clinical-practice degree. Its compulsory spine combines organ-system medicine with biomechanics, thermodynamics, waves, biomedical instrumentation, signals, imaging, medical-image processing, bioinformatics, computer simulation and medical-technology design, alongside three levels of clinical skills and safety, a healthcare placement, complex diagnosis–therapy training and a 15-EC clinical-technology research project. UCR has meaningful biomedical science, anatomy, physiology, pathology, pharmacology, laboratory, mathematics, data, imaging and robotics courses. It does not have the required physics and biomedical-engineering progression, biomedical instrumentation laboratories, integrated organ-system engineering modules, clinical skills and safety training, supervised patient-facing placement, medical-device practice, or diagnosis-and-treatment formation. Combining UCR's biomedical and computational courses would create a strong health-and-data liberal-arts programme, but it would not be a defensible Clinical Technology comparator.

Copying repeated chart codes as new third-year requirements and using minor 15 misrepresents current regulations, which require minor 30 and four third-year major units. Current formal rows themselves total 181; external closure remains blocked on one-credit clarification.

Provenance: data/counselor/comparisons/cp-000250.json; source worksheet row(s) 263. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [Clinical Technology programme](https://www.tudelft.nl/onderwijs/opleidingen/bachelors/klinische-technologie/bsc-klinische-technologie/over-de-opleiding) — Joint degree, credits, instruction and placement; Current official prospectus. Dutch joint TU Delft/Leiden/Erasmus bachelor, 180 EC, medicine and technology integrated. Second-year healthcare placement and clinical skills are explicit. The live page still links the older 2024–2025 module chart, whose duplicated year-two codes cannot establish three additional third-year requirements. Current published OER controls.
- [Clinical Technology module map 2024–2025](https://filelist.tudelft.nl/me/Onderwijs/Bacheloropleidingen/KT/Modulekaart-Bsc-KT%202024-2025.pdf) — Second/third-year duplicate codes and minor; 2024–2025; diagnostic older chart. Old chart lists KT2555 3.5, KT2355 3 and KT2655 6.5 in both years two and three, plus third-year AV/essay 2 and minor 15. Copying those printed positions gives 180, but does not establish distinct credit-bearing units. Repeated identifiers need formal reconciliation; simply adding year suffixes is insufficient. Chart visually inspected.
- [OER BSc Klinische Technologie 2026–2027](https://filelist.tudelft.nl/Studentenportal/Faculteitspecifiek/ME/Onderwijs/GERELATEERD/Reglementen/Archief%20Onderwijsreglementen/2026-2027/OER%20BSc%20KT%202026-2027_DEFINITIEF.pdf) — Articles 7, 32, Appendix 3; PDF pp. 6, 25–27; Current 2026–2027. Adopted/effective 31 August 2026. Minor 30. First-year rows total 60; second-year rows total 61 including healthcare placement KT2755 printed 4.5; third required units KT3405 6.5, KT3505 6.5, KTO 15 and skills 2 total 30, with minor 30. Thus printed complete requirement sum 181 conflicts with statutory 180. Duplicate bioinformatics/image/informatics and AV3 are absent from third-year requirement list. Heart/lung titles also changed. Tables visually inspected; no one-credit adjustment invented.

External credit structure: Stored 180 reproduces older chart repeats. Current required rows 60+61+[major 30+minor 30]=181; no verified current 180 reconstruction claimed.

Result: incorrect; required action: reassess-exception.

Incorrect applies to the stated external allocation, narrative, source-context or normalized metadata issue; no independent UCR conclusion or unsupported dated-change inference.

Secondary attribute finding(s):

- Current statutory 180 versus printed 181 requirements: still-unresolved; stored "not applicable", verified "see case evidence". Separate closure: Known duplicate/minor/title errors are established; complete current credit allocation remains blocked.

Recommended follow-up: Replace older duplicated allocation with current requirements after resolving printed 181-versus 180 conflict; correct known minor, duplicate and title issues without silently adjusting a weight.

Unresolved factual question / historical limitation: Does current KT2755 carry 4.5 or 3.5 EC, or is another printed year-two weight/credit-sharing rule responsible for the 61-EC second year and 181-EC complete total?

Implementation plan — **not implemented; audit only**:

- `data/counselor/decisions/cp-000250.json`, fields: `sources`, `comparator.components tuples`, `comparator.primarySource/additionalSources`, `comparator.sourceNotes`, `routeSelection where applicable`, `exception.curriculumContext`, `exception.reason where a factual correction is needed`, `exception.checkedOn`. Apply the case-specific correction below first in its existing version-2 compact academic decision, then compile canonical record. Preserve prior UCR evidence as historical provenance pending separate feasibility assessment.
- `data/counselor/comparisons/cp-000250.json`, fields: `comparator.components`, `comparator.sourceNotes`, `comparator.academicYear`, `comparator.primarySourceUrl/additionalSourceUrls`, `comparator.routeSelection where applicable`, `exception.curriculumContext`, `exception.reason where needed`, `exception.checkedOn`. Replace older duplicated allocation with current requirements after resolving printed 181-versus 180 conflict; correct known minor, duplicate and title issues without silently adjusting a weight. Known current corrections: minor 15→30; remove duplicate third-year KT2555/KT2355/KT2655 entries and unsupported separate AV3/essay 2; use current KT1605 Heart and Lung: the Foundation and KT2605 Heart and Lung: Homeostasis names. Current KT2755 printed 4.5 creates year 2 total 61; do not change it to 3.5 or another unit to force 180 without official authority. Mark complete current allocation unresolved until the one-credit issue is resolved, preserving independently supported clinical/engineering identity.
- `data/counselor/review-programmes.json and existing generated counselor artifacts`, fields: `affected curriculum/source/choice summaries`. Regenerate affected summaries after canonical compilation through the existing production workflow.

Dependencies:

- Current applicable catalogue/corrected OER or university clarification resolving printed 61/year 2 and 181/degree versus statutory 180. Known minor/duplicate/title corrections can be specified now, but complete 180 closure must wait.
- No double counting of repeated identifiers; determine credit sharing if officially documented.
- UCR feasibility remains stage two and cannot be inferred from this correction.

Verification and closure checks:

- Compact decision recompiles to corrected canonical record; run exception-specific schema/record checks when implementing.
- Reconcile every mandatory/restricted/open component to 180 without duplicated alternatives, embedded skills or project credits.
- Canonical and generated summaries agree; close external correction separately from UCR feasibility.
- Close only when official authority reconciles 60+60+60 or an explicitly permitted unequal-year allocation to 180. Record the source of any one-credit correction.
- Check statutory 30-minor, four current final major units, unique course credit, placement and changed heart/lung titles; do not restore obsolete chart repeats merely to make totals fit.

Research trigger: Corrected 2026 OER, accessible current KT2755/course allocation or explicit university credit-reconciliation clarification.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000251 — Bachelor Life Science and Technology

Institution: Delft University of Technology and Leiden University. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-03.

Existing substantive reason: Life Science and Technology is an integrated biotechnology and bioprocess-engineering degree. Its compulsory spine combines molecular and cellular biology with bio-organic and chemical biology, molecular analytical methods, thermodynamics and transport phenomena, microbial physiology and biotechnology, genetic engineering, biocatalysis, bioinformatics, bioprocess modelling, basic biotechnology techniques, a microbial-biotechnology practicum, sustainable process design and a 20-EC final project. UCR offers meaningful molecular biology, biochemistry, immunology, genetics, pharmacology, laboratory, calculus, programming and data-science courses. It does not offer the required chemistry and bioprocess-engineering progression, including bio-organic and chemical biology, bioprocess thermodynamics, transport phenomena, microbial process engineering, biocatalysis, reactor/process modelling and sustainable biotechnological process design, nor an equivalent advanced biotechnology laboratory and capstone sequence. Combining UCR's strongest life-science, mathematics and computational courses would create a substantial molecular-biomedicine pathway, but not a defensible Life Science and Technology comparator.

Current September 2026 chart confirms every selected component, all 180 credits,30-minor and 20 final project. Joint degree identity and defining laboratory/bioprocess progression are supported.

Provenance: data/counselor/comparisons/cp-000251.json; source worksheet row(s) 264. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [Life Science and Technology programme](https://www.tudelft.nl/onderwijs/opleidingen/bachelors/lst/bsc-life-science-and-technology/over-de-opleiding) — Joint degree, study load and cell/bioprocess identity; Current official prospectus. Dutch TU Delft/Leiden joint bachelor 180. Biology, chemistry, mathematics, biophysics, biotechnology and bioprocess design are integrated; ordinary third-year minor and experimental/final project are explicit. Current page links September 2026 chart.
- [Life Science and Technology September 2026 curriculum](https://filelist.tudelft.nl/TUDelft/Onderwijs/Opleidingen/Bachelor/Life_Science_Technology/02._Opleiding/2026_LST_DEF_web_pag2.pdf) — All year tables and footer; September 2026. First year ten 5-EC units plus Biotechnology Theory 6 and LST/Society 4=60; second twelve times 5=60; third minor 30, disease-process research 5, sustainable-bioprocess design 5 and final project 20=60. Exact stored names/translations and all 28 weights agree. No restricted discipline route is required; open minor remains generic. Chart visually inspected.

External credit structure: Verified 60+60+[minor 30+disease 5+processDesign 5+final 20]=180.

Verified reconstruction for later external remediation (audit evidence only):

| Study year | Component | EC | Status / qualification |
|---|---|---:|---|
| 1 | Molecular Cell Biology | 5 | required |
| 1 | Biotechnology, Theory | 6 | required |
| 1 | Immunology and Health 1 | 5 | required |
| 1 | Molecular and Cellular Biophysics | 5 | required |
| 1 | Biochemistry | 5 | required |
| 1 | Thermodynamics of Bioprocesses | 5 | required |
| 1 | Calculus 1 | 5 | required |
| 1 | Bio-organic Chemistry | 5 | required |
| 1 | Life Sciences Practicum | 5 | required |
| 1 | Life Science and Technology and Society | 4 | required |
| 1 | Basic Biotechnology Techniques | 5 | required |
| 1 | Programming and Modelling | 5 | required |
| 2 | Immunology and Health 2 | 5 | required |
| 2 | Chemical Biology | 5 | required |
| 2 | Structural Biology | 5 | required |
| 2 | Genetic Engineering | 5 | required |
| 2 | Calculus 2 | 5 | required |
| 2 | Microbial Physiology | 5 | required |
| 2 | Modelling of Bioprocesses | 5 | required |
| 2 | Biocatalysis | 5 | required |
| 2 | Molecular Analytical Methods | 5 | required |
| 2 | Microbial Biotechnology Practicum | 5 | required |
| 2 | Bioinformatics | 5 | required |
| 2 | Transport Phenomena in the Life Sciences | 5 | required |
| 3 | Minor | 30 | open-choice |
| 3 | Investigation of Disease Processes in Humans | 5 | required |
| 3 | Design of Sustainable Biotechnological Processes | 5 | required |
| 3 | Bachelor Final Project | 20 | required |

Total: **180 EC**; study-year totals **60 + 60 + 60**. Verified external reconstruction for later remediation; production unchanged and UCR fit unassessed.

Choice and source-context rules:

- Keep genuine minor and named profiling slots explicit; no invented optional contents.

Result: confirmed; required action: none.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000252 — Bachelor Aerospace Engineering

Institution: Delft University of Technology. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-03.

Existing substantive reason: Aerospace Engineering is a tightly sequenced professional engineering degree. Its compulsory spine combines calculus, differential equations, probability, physics, engineering mechanics, materials and structures, aerospace design and construction, aerodynamics with wind-tunnel testing, structural and vibration analysis, flight and orbital mechanics, propulsion and power, signals and control, numerical modelling, aerospace systems engineering and production, flight dynamics and flight testing, and a 15-EC aerospace Design Synthesis Exercise. UCR offers useful mathematics, programming, numerical methods, linear systems, statistics, AI, robotics, sustainability and general product-design courses. It has no equivalent progression in classical mechanics, aerospace materials and structures, fluid mechanics and aerodynamics, propulsion, orbital mechanics, aircraft stability and flight dynamics, aerospace production, wind-tunnel and flight-test practice, or integrated aircraft/spacecraft design. The available quantitative and computational courses can support an engineering-adjacent liberal-arts pathway, but cannot form a defensible Aerospace Engineering comparator.

The selected pre-2027 180 curriculum is supported by current IR and linked chart. Normalized NLD-only language conflicts with official English instruction and requires correction.

Provenance: data/counselor/comparisons/cp-000252.json; source worksheet row(s) 265. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [Aerospace Engineering programme](https://www.tudelft.nl/onderwijs/opleidingen/bachelors/ae/bsc-aerospace-engineering) — Degree facts and language; Current official prospectus. Current programme explicitly states English instruction. Registry languages_json contains only NLD and has no resolution correction. This is a normalized language error; retain Dutch-coded raw offering as provenance and correct the normalized/canonical metadata with official support.
- [Aerospace Engineering Implementation Regulations 2026–2027](https://filelist.tudelft.nl/Studentenportal/Faculteitspecifiek/LR/Onderwijs/Education/AE%20IR%202026-2027%20final.pdf) — Articles 1–2; PDF p. 3; Current 2026–2027. Bachelor 180: first 60, second 60, minor 30, final major 15, Design Synthesis Exercise 15. Current student overview links the older module chart; revised public curriculum is explicitly September 2027 onward, so is excluded for 2026 entrant. Existing selected pre-2027 180 structure is supported.
- [Aerospace Engineering BSc modules and courses](https://filelist.tudelft.nl/Studentenportal/Faculteitspecifiek/LR/Onderwijs/BSc%20Curriculum%202022-2023.pdf) — Whole chart, July 2022 footer, thick module versus subcomponent boundaries; July 2022 chart; current pre-2027 applicability corroborated. Official chart still linked by live student overview. Twenty-two stored modules total 60+60+60. Wind-tunnel 1 is inside Aerodynamics 7; AI3 inside Test/Analysis/Simulation 8; zero-credit English/reporting skills do not add credits. Research/design/test progression and DSE15 preserved without duplication. Chart visually inspected.

External credit structure: Supported pre-2027 structure 60+60+[minor 30+major 15+DSE15]=180; language correction does not require a curriculum redesign.

Result: incorrect; required action: correct-registry-and-reprocess.

Incorrect applies to the stated external allocation, narrative, source-context or normalized metadata issue; no independent UCR conclusion or unsupported dated-change inference.

Secondary attribute finding(s):

- Selected external curriculum: confirmed; stored "not applicable", verified "see case evidence". Separate closure: Normalized language correction.

Recommended follow-up: Correct normalized language to ENG and compile affected canonical/provider summaries while retaining raw Dutch-coded offering provenance. Preserve supported curriculum and exclude September 2027 redesign.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

Implementation plan — **not implemented; audit only**:

- `data/registry/programmes.csv`, fields: `languages_json`, `corrected_attributes_json`, `official_source_ids_json/official_source_urls_json`, `normalization_basis and decision_case_ids_json as required by existing correction workflow`. Correct CP252 language from NLD-only to ENG using official instruction evidence. Preserve raw programme_offerings.csv language NLD, source rows and offering ID as upstream provenance; record correction authority through existing registry resolution workflow.
- `data/registry/resolution_cases.csv, resolution_decisions.csv and resolution_sources.csv`, fields: `case/decision/source fields required by existing registry correction workflow`. Record auditable language correction and current official source, retaining old/raw language context. Do not create duplicate programme identity or renumber target.
- `data/counselor/decisions/cp-000252.json and data/counselor/comparisons/cp-000252.json`, fields: `source support`, `programmeProvider normalized language after rebuild`, `exception checked/source context where needed`. Refresh normalized provider through registry build; retain accurate pre-2027 comparator components and current IR, then recompile academic decision/canonical record. Exclude previewed 2027 redesign.
- `data/counselor/review-programmes.json and generated registry/counselor artifacts`, fields: `CP252 language/source summaries`. Regenerate affected metadata and summaries after correction, leaving original audit provenance intact.

Dependencies:

- Official English instruction establishes correction; no external curriculum prerequisite.
- Final UCR feasibility remains independently pending.

Verification and closure checks:

- Normalized language ENG matches current official programme; raw NLD preserved and correction authority traceable.
- Provider/source-row/offering key reconciliation unchanged; no duplicate/renumbered record.
- Current 180 pre-2027 structure remains 60+60+30+15+15; do not substitute future redesign.
- Run registry validation/rebuild and exception-specific compilation checks; generated summaries agree.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### Batch 8 additional source and closure qualifications

- CP217: Statistical Reasoning is formally marked 2027/28 and is reachable in year two of the September 2026 cohort; it is not claimed available in 2026/27. Minor excludes internships/research traineeships.
- CP244: Current reader publication is 14 September 2026; the generic HTML still carries 2025 effective dates. Appendix I explicitly schedules the 2026 entrant across 2026/27–2028/29 and controls the credit correction. English is an ordinary representative delivery of a combined normalized target, not an exclusive target named by an English display translation.
- CP248: The old chart places Mixed-Signal Circuits inQ4; current OER table saysQ3. Exact quarter timetable requires current catalogue confirmation. Yearly requirements and credits are established.
- CP250: Current adopted OER printed totals are 60+61+60=181. KT2755 is visibly 4.5; minor 30 and final required 6.5+6.5+15+2 are established. The complete current 180 pathway remains unresolved; the implementation plan has an explicit research trigger and closure blocker.
- CP252: Current official language ENG; upstream offering NLD remains raw provenance. Curriculum secondary finding confirmed; normalized-language primary finding incorrect.

## Cumulative findings after batch 9

| Finding | Count |
|---|---:|
| confirmed | 60 |
| incorrect | 26 |
| outdated | 0 |
| still-unresolved | 4 |

| Required action | Count |
|---|---:|
| none | 55 |
| reprocess-as-comparison | 0 |
| reassess-exception | 25 |
| correct-registry-and-reprocess | 7 |
| research-again-later | 3 |

## Batch 9 findings

One external basis is confirmed; nine cases require corrections to stated external credit, choice, compulsory-content, source-context or normalized-language facts. Delft Applied Physics matches its current September 2026 entrant chart. Marine Technology requires current 14-credit final project and formal course allocation; Applied Mathematics requires exactly one non-mathematical elective; Mechanical Engineering retains accurate components but has four formal year-two projects, not three. Nanobiology has English instruction, assigned mixed practical pairs and 2.5-credit specialist elective options. TU/e Automotive and Electrical Engineering require 125 core/10 ITEC/45 elective rather than 120/15/45, with optional course examples qualified. Biomedical Engineering requires Dutch+English metadata and currentBBT125/10/45 allocation. Industrial Design exact printed courses/projects/PPD/ITEC/profiling replace unsupported generic year aggregates.

TU/e Architecture needs a neutral AUDE main-track selection. Its current formal core/table 125 and article elective 45 conflict with Appendix 2 elective 40 and webpage 130/10/40; project 7P1B30 is printed 5. This five-credit conflict is recorded as secondary still-unresolved, with a concrete official-clarification trigger. Industrial Design separately has a coherent 180 diagram but formal core 125+ITEC10+Appendix 2 profiling 50=185; that aggregate conflict also requires clarification. No credit is invented and complete formal credit closure remains blocked for these two cases. Incorrect primary findings are scoped factual corrections, not an independent verdict on the historical UCR conclusions. No outdated classification is inferred from discovery alone.

Sources were retrieved directly from official sites and public programme endpoints. Material PDF tables/figures were visually inspected. Current formal requirements control ambiguity; prospective entrant charts and explicitly outgoing-cohort schedules are kept distinct. All changes here are audit evidence/plans only.

| ID | Programme | Formal type | Finding | Required action |
|---|---|---|---|---|
| cp-000253 | Bachelor Marine Technology | no-defensible-ucr-match | incorrect | reassess-exception |
| cp-000254 | Bachelor Nanobiology | no-defensible-ucr-match | incorrect | correct-registry-and-reprocess |
| cp-000258 | Bachelor Applied Physics | no-defensible-ucr-match | confirmed | none |
| cp-000259 | Bachelor Applied Mathematics | no-defensible-ucr-match | incorrect | reassess-exception |
| cp-000260 | Bachelor Mechanical Engineering | no-defensible-ucr-match | incorrect | reassess-exception |
| cp-000261 | Bachelor Automotive Technology | no-defensible-ucr-match | incorrect | reassess-exception |
| cp-000262 | Bachelor Biomedical Engineering | no-defensible-ucr-match | incorrect | correct-registry-and-reprocess |
| cp-000263 | Bachelor Architecture, Urbanism and Building Sciences | no-defensible-ucr-match | incorrect | reassess-exception |
| cp-000265 | Bachelor Electrical Engineering | no-defensible-ucr-match | incorrect | reassess-exception |
| cp-000266 | Bachelor Industrial Design | no-defensible-ucr-match | incorrect | reassess-exception |

## Batch 9 evidence and implementation plans

### cp-000253 — Bachelor Marine Technology

Institution: Delft University of Technology. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-03.

Existing substantive reason: Marine Technology is a cumulative naval-architecture and marine-engineering degree. Its compulsory spine combines analysis, linear algebra, differential equations, probability, numerical mathematics, statics, dynamics, strength of materials, thermodynamics, rigid-body and continuum mechanics, hydromechanics, hydrostatics, marine structures, resistance, propulsion and drive systems, ship design, complex loads and vibration, electrical systems and control, ship production, integrated maritime projects and a final marine research or design project. UCR offers meaningful mathematics, programming, sustainability, water-management and general design courses. It does not offer the required engineering-mechanics, hydrodynamics, naval-architecture, marine propulsion, structural, production, control and vessel-design progression or equivalent experimental and project facilities. A UCR pathway could study sustainable maritime systems from environmental, policy and quantitative perspectives, but it would not be a defensible Marine Technology comparator.

Current formal course-level requirements conflict with the live older category breakdown: final project 14 rather than 12, exact integration/course allocation and three different final-year course names. A source-backed 180 reconstruction is available.

Provenance: data/counselor/comparisons/cp-000253.json; source worksheet row(s) 266. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [Marine Technology: what will I learn?](https://www.tudelft.nl/onderwijs/opleidingen/bachelors/maritieme-techniek/bsc-maritieme-techniek/over-de-opleiding/wat-ga-ik-leren) — Degree structure and linked older diagram; Current official programme. Dutch three-year maritime engineering degree. Live category breakdown still totals 24 mathematics +36 mechanics +58 specialist +20 projects +30 minor +12 final project. Current formal regulations instead establish course weights, a 14-EC final project and different final-year titles. The live older breakdown is not controlling for current formal requirements.
- [OER BSc Mechanical Engineering and Marine Technology 2026–2027](https://filelist.tudelft.nl/Studentenportal/Faculteitspecifiek/ME/Onderwijs/GERELATEERD/Reglementen/Archief%20Onderwijsreglementen/2026-2027/OER%20BSc%20WB-MT_DEFINITIEF.pdf) — Mechanical curriculum PDF p.25; Marine curriculum p.30; BEP conditions pp.26/31; Current 2026–2027. Mechanical: first and second years ten 6-EC units each; third minor 30, control 6, integrated systems 6, engineer/society 4 and final project 14. Four year-two units are formally grouped as projects, including Process Engineering and Thermodynamics. Marine: year 1 mathematics 12 + mechanics 24 + maritime theory 16 + integration 8=60; year 2 mathematics 12 + advanced mechanics 6 + control 6 + maritime theory 18 + ship-design project 6 + integration 12=60; year 3 minor 30 + dynamics maritime structures 6 + electric drive/conversion 4 + ship motions/manoeuvring 6 + BEP14=60. Mathematical/advanced-mechanics subparts are embedded, not additional courses. MT1466-26 supersedes MT1466. BEP requires all first year and at least 54 second-year credits. Tables visually inspected.

External credit structure: Stored component arithmetic totals 180 EC. Current formal course-level requirements conflict with the live older category breakdown: final project 14 rather than 12, exact integration/course allocation and three different final-year course names. A source-backed 180 reconstruction is available.

Verified reconstruction for later external remediation (audit evidence only):

| Study year | Component | EC | Status / qualification |
|---|---|---:|---|
| 1 | Mathematics 1 (WBMT1050-24) | 6 | required |
| 1 | Mathematics 2 (WBMT1051) | 6 | required |
| 1 | Statics (WB1630-20) | 6 | required |
| 1 | Strength of Materials (WB1631-24) | 6 | required |
| 1 | Dynamics (WB1135) | 6 | required |
| 1 | Thermodynamics (WB1530-14) | 6 | required |
| 1 | Introduction to Marine Technology (MT1461-25) | 4 | required |
| 1 | Hydrostatics (MT1462) | 4 | required |
| 1 | Mechanics of Marine Structures 1 (MT1464) | 4 | required |
| 1 | Resistance, Propulsion and Drive 1 (MT1465) | 4 | required |
| 1 | Integration and Skills 1 (MT1463) | 4 | required |
| 1 | Integration and Skills 2 (MT1466-26) | 4 | required |
| 2 | Mathematics 3 (WBMT2048) | 6 | required |
| 2 | Mathematics 4 (WBMT2049) | 6 | required |
| 2 | Advanced Mechanics (WB2630) | 6 | required |
| 2 | Systems and Control Engineering (WB3240-24) | 6 | required |
| 2 | Hydromechanics (MT2461-25) | 6 | required |
| 2 | Resistance, Propulsion and Drive 2 (MT2463) | 6 | required |
| 2 | Mechanics of Marine Structures 2 (MT2464) | 6 | required |
| 2 | Ship Design (MT2462) | 6 | required |
| 2 | Integration and Skills 3 (MT2465) | 12 | required |
| 3 | Minor | 30 | open-choice |
| 3 | Dynamics of Marine Structures (MT3461) | 6 | required |
| 3 | Electrical Drive and Conversion (MT3462) | 4 | required |
| 3 | Ship Motions and Manoeuvring (MT3463) | 6 | required |
| 3 | Bachelor Final Project (WBMT3BEP) | 14 | required |

Total: **180 EC**; study-year totals **60 + 60 + 60**. Source-backed requirement reconstruction for later remediation; production unchanged and UCR fit unassessed.

Choice and source-context rules:

- Use current course weights; mathematical and mechanics subparts are embedded.
- Integration 1/2/3 total 20; Ship Design is an additional required 6-credit project, not extra beyond the course list.
- Minor 30 remains approved open choice; no optional minor invented.
- BEP14, not older webpage 12; first-year completion and 54 second-year credits prerequisite.

Result: incorrect; required action: reassess-exception.

Incorrect applies only to the stated external allocation, narrative, choice, source context or normalized-language facts. No independent UCR conclusion or unsupported dated-change inference.

Recommended follow-up: Use current formal course weights, final project 14 and current final-year names; replace six aggregates with explicit courses/projects, preserve minor 30 and embedded subparts.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

Implementation plan — **not implemented; audit only**:

- `data/counselor/decisions/cp-000253.json`, fields: `sources`, `comparator.components tuples`, `comparator.academicYear`, `comparator.primarySource/additionalSources`, `comparator.sourceNotes`, `comparator.route and routeSelection where applicable`, `exception.curriculumContext`, `exception.reason external factual clauses`, `exception.checkedOn`. Use current formal course weights, final project 14 and current final-year names; replace six aggregates with explicit courses/projects, preserve minor 30 and embedded subparts. Apply in existing version 2 compact decision; update sources and source indexes consistently. Preserve existing UCR claims only as historical provenance.
- `data/counselor/comparisons/cp-000253.json`, fields: `comparator.components`, `comparator.sourceNotes`, `comparator.academicYear`, `comparator.primarySourceUrl/additionalSourceUrls`, `comparator.routeSelection where applicable`, `exception.curriculumContext`, `exception.reason`, `exception.checkedOn`. Compile the amended compact decision using current normalized provider; canonical external facts must agree with case evidence and preserve precise choice/optional scope. Do not automatically change exception type or create a comparison.
- `data/counselor/review-programmes.json and existing generated counselor artifacts`, fields: `affected metadata, curriculum, source and route summaries`. Regenerate affected outputs after targeted remediation; keep this audit evidence and immutable provenance.

Dependencies:

- Validate applicable current cohort and sources when implementing; no broad repeated research required for established facts.
- Final UCR feasibility remains a separate stage-two dependency.

Verification and closure checks:

- Every included course counted once; total 180 from source-backed weights, with restricted choices instantiated and genuine open profiling explicit.
- Required-versus-optional claims, route, source context and cohort agree across compact and canonical records.
- Run applicable registry/exception compiler/schema validation and refresh generated summaries; close external fixes independently of UCR feasibility.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000254 — Bachelor Nanobiology

Institution: Delft University of Technology and Erasmus University Rotterdam. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-03.

Existing substantive reason: Nanobiology is an intentionally integrated quantitative life-science degree whose compulsory spine combines molecular and cellular biology with calculus, linear algebra, differential equations, Fourier methods, statistics, mechanics, optics, electricity and magnetism, molecular biophysics, soft matter, scientific programming, computational science, bioinformatics, electronic instrumentation, nanotechnology, two stages of imaging, two stages of laboratory techniques and a 20-EC laboratory research project. UCR offers substantial life science, mathematics, programming, data science and one introductory life-science laboratory course. It does not offer the required physics progression, nanoscale and biophysical integration, scientific instrumentation, experimental biophysics, advanced microscopy and imaging laboratory sequence, nanotechnology practical work, or a comparable 20-EC nanobiology laboratory project. A UCR pathway could study quantitative molecular life science, but it would not be a defensible Nanobiology comparator.

Official instruction is English, while normalized language is NLD-only. The 180 aggregate weights are supported, but practical pairing is assigned and mixed, and bounded specialist choices must be instantiated using actual 2.5-credit formal units.

Provenance: data/counselor/comparisons/cp-000254.json; source worksheet row(s) 267. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [Nanobiology degree facts](https://www.tudelft.nl/en/education/programmes/bachelors/nb/bsc-nanobiology) — Working language and joint institutional setting; Current official programme. Working language explicitly English, standard full-time three-year 180-EC joint TU Delft/Erasmus MC programme. Current normalized NLD-only language is incorrect; institutional participation is distinct from permanent normalized target identity.
- [Nanobiology September 2026 curriculum](https://filelist.tudelft.nl/TUDelft/Onderwijs/Opleidingen/Bachelor/Nanobiology/02._Opleiding/2026_NB_DEF_web_pag2.pdf) — All year tables and specialist list; September 2026. First-year twelve positions 60, second-year fourteen positions 60, third minor 30 + laboratory BEP20 + electives 10. Practical positions display alternatives; current formal appendix controls the assigned mixed pair. Overview specialist list omits some formal options and does not print their individual weights; do not infer two 5-EC electives.
- [Programme-specific Appendix Nanobiology TER 2026–2027](https://filelist.tudelft.nl/Studentenportal/Faculteitspecifiek/TNW/Onderwijs/Opleidingsreglementen/2026-2027/BSc%20NB%20Appendix%20TER%202026-2027.pdf) — Articles 3–5 and 8; PDF pp.5–8; Current 2026–2027. Programme assigns either NB1430 Molecular Biology Techniques A + NB1445 Biophysics Techniques B, or NB1435 Biophysics Techniques A + NB1440 Molecular Biology Techniques B; 4 EC each. It is not an unconstrained or same-discipline A/B choice. Required first/second units match stored weights. Article 4 and current chart Nanotechnology NB2430 carry 3; outgoing-cohort transition Article 11.7 prints 4 for the same replacement code. Apply current requirement-table 3 for the new entrant; retain the transition discrepancy for any older-cohort reconstruction. Article 5.2 restricted elective table starts A Primer in Neuroscience NB3015, Advanced Math Topics NB3024, Biomolecular Ultrasound NB3026, Computational Neuroscience NB3014, all 2.5 EC: four distinct choices total 10. Other choices/outside courses require stated approval; capacity/prerequisites remain catalogue conditions. Year 3 minor 30 + electives 10 + BEP20. Tables visually inspected.

External credit structure: Stored component arithmetic totals 180 EC. Official instruction is English, while normalized language is NLD-only. The 180 aggregate weights are supported, but practical pairing is assigned and mixed, and bounded specialist choices must be instantiated using actual 2.5-credit formal units.

Verified reconstruction for later external remediation (audit evidence only):

| Study year | Component | EC | Status / qualification |
|---|---|---:|---|
| 1 | Molecular Genetics (NB1310) | 5 | required |
| 1 | Math 1 for Nanobiologists (NB1315) | 6 | required |
| 1 | Introduction to Nanobiology (NB1410) | 4 | required |
| 1 | Chemistry (NB1320) | 5 | required |
| 1 | Mechanics and Optics (NB1325) | 5 | required |
| 1 | Programming Foundations (NB1420) | 5 | required |
| 1 | Biochemistry and Structural Biology (NB1330) | 6 | required |
| 1 | Math 2 for Nanobiologists (NB1335) | 5 | required |
| 1 | Molecular Biology Techniques A (NB1430) | 4 | assigned-pair; First formally listed permissible programme-assigned mixed pair; not a free student choice. |
| 1 | Molecular Biophysics (NB1340) | 6 | required |
| 1 | Math 3 for Nanobiologists (NB1345) | 5 | required |
| 1 | Biophysics Techniques B (NB1445) | 4 | assigned-pair; Companion to NB1430; other assigned pair is NB1435+NB1440. |
| 2 | Electricity and Magnetism (NB2310) | 5 | required |
| 2 | Differential Equations and Fourier (NB2315) | 4 | required |
| 2 | Computational Sciences (NB2410) | 5 | required |
| 2 | Molecular Cellular Biology (NB2320) | 6 | required |
| 2 | Statistics (NB2325) | 4 | required |
| 2 | Electronic Instruments (NB2420) | 4 | required |
| 2 | Science, Technology and Society 1 (NB2510) | 2 | required |
| 2 | Evolutionary and Developmental Biology (NB2335) | 6 | required |
| 2 | Imaging 1 (NB2330) | 5 | required |
| 2 | Nanotechnology (NB2430) | 3 | required |
| 2 | Bioinformatics (NB2340) | 6 | required |
| 2 | Introduction to Soft Matter (NB2345) | 4 | required |
| 2 | Imaging 2 (NB2440) | 4 | required |
| 2 | Science, Technology and Society 2 (NB2520) | 2 | required |
| 3 | Minor | 30 | open-choice |
| 3 | Bachelor End Project | 20 | required |
| 3 | A Primer in Neuroscience (NB3015) | 2.5 | restricted-choice; First four formal-table options; precise octal availability/capacity and catalogue prerequisites must be checked before an exact timetable. |
| 3 | Advanced Math Topics (NB3024) | 2.5 | restricted-choice; First four formal-table options; precise octal availability/capacity and catalogue prerequisites must be checked before an exact timetable. |
| 3 | Biomolecular Ultrasound (NB3026) | 2.5 | restricted-choice; First four formal-table options; precise octal availability/capacity and catalogue prerequisites must be checked before an exact timetable. |
| 3 | Computational Neuroscience (NB3014) | 2.5 | restricted-choice; First four formal-table options; precise octal availability/capacity and catalogue prerequisites must be checked before an exact timetable. |

Total: **180 EC**; study-year totals **60 + 60 + 60**. Source-backed requirement reconstruction for later remediation; production unchanged and UCR fit unassessed.

Choice and source-context rules:

- First permissible mixed practical assignment represented, not both assignments or a same-discipline A+B sequence.
- Four first-listed distinct 2.5 electives instantiate 10 without UCR-fit selection; outside options require approval.
- Course membership/credits verified; do not assert exact future elective timetable or individual programme assignment in advance.
- Joint degree institutional participation retained; normalized language ENG.

Result: incorrect; required action: correct-registry-and-reprocess.

Incorrect applies only to the stated external allocation, narrative, choice, source context or normalized-language facts. No independent UCR conclusion or unsupported dated-change inference.

Recommended follow-up: Correct normalized language to ENG with preserved rawNLD provenance. Choose the first formally permitted assigned practical pair as representative, explicitly qualified, and four first-listed 2.5 electives; retain joint institutional context.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

Implementation plan — **not implemented; audit only**:

- `data/registry/programmes.csv`, fields: `languages_json`, `corrected_attributes_json`, `official_source_ids_json/official_source_urls_json`, `normalization_basis and decision_case_ids_json as required by correction workflow`. Set normalized languages_json=["ENG"] using the official language evidence. Preserve permanent ID, original source rows and immutable raw NLD offering language. Use the documented post-build registry correction workflow.
- `data/registry/resolution_cases.csv, resolution_decisions.csv and resolution_sources.csv`, fields: `documented language correction and authority linkage`. Record auditable current language correction through repository-supported resolution workflow; keep raw/old language as provenance and retain correction across rebuilds. Do not duplicate or renumber target.
- `data/counselor/decisions/cp-000254.json`, fields: `sources`, `comparator.components tuples`, `comparator.academicYear`, `comparator.primarySource/additionalSources`, `comparator.sourceNotes`, `comparator.route and routeSelection where applicable`, `exception.curriculumContext`, `exception.reason external factual clauses`, `exception.checkedOn`. Correct normalized language to ENG with preserved rawNLD provenance. Choose the first formally permitted assigned practical pair as representative, explicitly qualified, and four first-listed 2.5 electives; retain joint institutional context. Apply in existing version 2 compact decision; update sources and source indexes consistently. Preserve existing UCR claims only as historical provenance.
- `data/counselor/comparisons/cp-000254.json`, fields: `comparator.components`, `comparator.sourceNotes`, `comparator.academicYear`, `comparator.primarySourceUrl/additionalSourceUrls`, `comparator.routeSelection where applicable`, `exception.curriculumContext`, `exception.reason`, `exception.checkedOn`. Compile the amended compact decision using current normalized provider; canonical external facts must agree with case evidence and preserve precise choice/optional scope. Do not automatically change exception type or create a comparison.
- `data/counselor/review-programmes.json and existing generated counselor artifacts`, fields: `affected metadata, curriculum, source and route summaries`. Regenerate affected outputs after targeted remediation; keep this audit evidence and immutable provenance.

Dependencies:

- Validate applicable current cohort and sources when implementing; no broad repeated research required for established facts.
- Final UCR feasibility remains a separate stage-two dependency.

Verification and closure checks:

- Every included course counted once; total 180 from source-backed weights, with restricted choices instantiated and genuine open profiling explicit.
- Required-versus-optional claims, route, source context and cohort agree across compact and canonical records.
- Run applicable registry/exception compiler/schema validation and refresh generated summaries; close external fixes independently of UCR feasibility.
- Normalized/provider language ["ENG"]; raw offering NLD preserved. Source-row and offering-ID crosswalks still reconcile exactly.
- Use representative mixed assignment NB1430+NB1445, not same-discipline A+B. Four distinct 2.5 electives=10; verify octal availability, capacity and formal catalogue prerequisites before asserting detailed scheduling.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000258 — Bachelor Applied Physics

Institution: Delft University of Technology. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-03.

Existing substantive reason: Applied Physics is a cumulative physics-and-engineering degree whose compulsory spine combines classical and advanced mechanics, thermodynamics, electromagnetism, waves, quantum mechanics, statistical physics, transport phenomena and solid-state physics with analysis, linear algebra, differential equations, Fourier methods, probability, computational science, systems and signals, circuits, electronics, instrumentation, three design courses, three laboratory courses and a 15-EC individual physics research project. UCR offers a useful mathematics and computational-modelling sequence and two broad sustainability gateways that touch on selected physical concepts. It does not offer the required university-level physics core, experimental-physics laboratory and measurement progression, electronic instrumentation, materials and quantum sequence, or comparable applied-physics research environment. A UCR pathway could study mathematical modelling and technology in an interdisciplinary way, but it would not be a defensible Applied Physics comparator.

All 29 stored components and 180 credits match the current September 2026 entrant diagram. The formal outgoing-cohort year 3 schedule is explicitly different and does not invalidate this prospective entrant chart. No formal route is required.

Provenance: data/counselor/comparisons/cp-000258.json; source worksheet row(s) 271. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [Applied Physics programme](https://filelist.tudelft.nl/TUDelft/Onderwijs/Opleidingen/Bachelor/Technische_Natuurkunde/02._Opleiding/TN_flyer_DEF_web_pag2.pdf) — Degree identity, core themes and laboratories; Current official programme. Dutch ordinary full-time degree. Mechanics, thermodynamics, electromagnetism and quantum mechanics are core themes; maths, laboratory work and design accompany the progression. Current prospectus links September 2026 chart; official proposed future curriculum material marked draft is excluded.
- [Applied Physics September 2026 curriculum](https://www.tudelft.nl/onderwijs/opleidingen/bachelors/tn/bsc-technische-natuurkunde/over-de-opleiding/wat-ga-ik-leren) — Whole chart and footer; September 2026 entrant overview. Stored 29 components and every credit agree: twelve 5-EC first-year units, twelve 5-EC second-year units; third minor 30 + two elective slots 5 each + critical reflection 5 + BEP15. Chart supports prospective 2026 entrant outline. It does not publish a bounded list for the two profiling slots; preserve these genuine unspecified electives. Figure visually inspected.
- [Applied Physics OER programme appendix 2026–2027](https://filelist.tudelft.nl/Studentenportal/Faculteitspecifiek/TNW/Onderwijs/Opleidingsreglementen/2026-2027/BSc%20TN%20OER-bijlage%202026-2027.pdf) — Articles 3–4 and 7; PDF pp.5,7–8,12; Current 2026–2027. Article 3 first-year 2026 requirements agree. Article 4 explicitly applies year 2 to cohort 2025 and year 3 to cohort 2024; its older final-year table has BEP12, reflection 3, optics 3, quantum 3, solid-state 6 and stochastic signals 3, plus minor 30. This is not a same-cohort contradiction with prospective 2026 chart BEP15/reflection 5/electives 10. Individual minor requires approval, no overlap, max 10 first-year credits and max 3 language-course credits. Do not substitute outgoing year 3 or mix cohorts into the chart route.

External credit structure: Stored component arithmetic totals 180 EC. All 29 stored components and 180 credits match the current September 2026 entrant diagram. The formal outgoing-cohort year 3 schedule is explicitly different and does not invalidate this prospective entrant chart. No formal route is required.

Verified reconstruction for later external remediation (audit evidence only):

| Study year | Component | EC | Status / qualification |
|---|---|---:|---|
| 1 | Mechanics | 5 | required |
| 1 | Introduction to Analysis | 5 | required |
| 1 | Introductory Laboratory 1 | 5 | required |
| 1 | Thermodynamics | 5 | required |
| 1 | Multivariable Analysis | 5 | required |
| 1 | Introductory Laboratory 2 | 5 | required |
| 1 | Electromagnetism | 5 | required |
| 1 | Vector and Fourier Analysis | 5 | required |
| 1 | Design Engineering for Physicists: Design | 5 | required |
| 1 | Waves | 5 | required |
| 1 | Linear Algebra 1 | 5 | required |
| 1 | Design Engineering for Physicists: Engineering | 5 | required |
| 2 | Advanced Mechanics | 5 | required |
| 2 | Advanced Linear Algebra and Differential Equations | 5 | required |
| 2 | Research Laboratory | 5 | required |
| 2 | Quantum Mechanics | 5 | required |
| 2 | Probability and Statistical Physics | 5 | required |
| 2 | Computational Science | 5 | required |
| 2 | Systems and Signals | 5 | required |
| 2 | Circuits, Electronics and Instrumentation | 5 | required |
| 2 | Design Engineering for Physicists: Physics | 5 | required |
| 2 | Physical Transport Phenomena | 5 | required |
| 2 | Solid-State Physics | 5 | required |
| 2 | Technology Management | 5 | required |
| 3 | Minor | 30 | open-choice |
| 3 | Applied Physics Elective 1 | 5 | required |
| 3 | Applied Physics Elective 2 | 5 | required |
| 3 | Critical Reflection on Science and Argumentation | 5 | required |
| 3 | Bachelor Final Project | 15 | required |

Total: **180 EC**; study-year totals **60 + 60 + 60**. Source-backed requirement reconstruction for later remediation; production unchanged and UCR fit unassessed.

Choice and source-context rules:

- Keep accurate current components; open minor/profiling retains approval/no-overlap requirements.
- Prospective September 2026 chart; older cohort 2024 third-year weights do not apply to this entrant outline.

Result: confirmed; required action: none.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000259 — Bachelor Applied Mathematics

Institution: Delft University of Technology. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-03.

Existing substantive reason: TU Delft Applied Mathematics is a cumulative proof-based mathematics degree. Its compulsory spine includes two analysis courses followed by real and complex analysis, two linear-algebra courses, algebra, discrete mathematics, ordinary and partial differential equations, numerical methods, optimisation, probability, statistics and measure-theoretic probability, alongside four modelling courses, programming and proof techniques. Restricted upper-level mathematics electives and a 15-EC mathematics bachelor project complete that formation. UCR offers a useful applied mathematics, statistics, programming and data-science sequence, but it does not provide the proof-intensive real/complex analysis, measure theory, abstract algebra and PDE depth or the mathematics-specific capstone environment required to preserve this degree's academic identity. A 24-course UCR response would become an interdisciplinary quantitative and data-science pathway rather than Applied Mathematics.

Stored 180 course weights are supported, but exactly one of the five electives must be non-mathematical. Generic restricted-elective blocks do not instantiate those choices and the narrative omits this requirement. Current cohort table supersedes older public course-list context.

Provenance: data/counselor/comparisons/cp-000259.json; source worksheet row(s) 272. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [Applied Mathematics programme](https://www.tudelft.nl/onderwijs/opleidingen/bachelors/tw/bsc-technische-wiskunde/over-de-opleiding/wat-ga-ik-leren) — Mathematical identity and public named courses; Current official programme. Dutch three-year degree in analysis, stochastics, optimisation/discrete mathematics, numerical methods/differential equations and modelling. Broad public overview retains older AM codes and elective material; current EEMCS formal cohort 2024+ table controls names, restrictions and credits.
- [Public current study-guide programme data](https://curriculum.tudelft.nl/publisher/api/v0/opleidingen/items/33234) — 2026–2027 record; cohort 2024+ description; Current 2026–2027. B-TW, CROHO56965, Dutch, full-time, three years 180. Cohort 2024+ first year twelve 5 units; second ten required 5 + two electives 5; third minor 30 + three electives 5 + project 15. Stored study-guide education URL returned 404; current public programme endpoint retrieved successfully. It does not negate the formal exact-one non-mathematical requirement.
- [EEMCS OER 2026–2027: Applied Mathematics](https://filelist.tudelft.nl/Studentenportal/Faculteitspecifiek/EWI/Studeren/Reglementen/Onderwijs-%20en%20Examenregeling%20EWI%202026-2027.pdf) — Article 14A/15; PDF pp.45–47; Current 2026–2027. Standard cohort 2024+ table supports stored taught-course weights, proof theory 3 + practical 2 counted once. Exactly one of five electives must be non-mathematical. First four mathematical choices TW-E01 Advanced Statistics, E02 Machine Learning, E03 Markov Processes, E04 Graph Theory are 5 each, Q3; first non-mathematical TW-E99 Algorithm Design 5 isQ4. Neutral annual placement: year 2 E01 + E99; year 3 E02 + E03 + E04 and project 15. Prerequisite knowledge must be considered; project requires first year and at least 40 major credits from years 2/3. Tables visually inspected; no minor/elective double counting.

External credit structure: Stored component arithmetic totals 180 EC. Stored 180 course weights are supported, but exactly one of the five electives must be non-mathematical. Generic restricted-elective blocks do not instantiate those choices and the narrative omits this requirement. Current cohort table supersedes older public course-list context.

Verified reconstruction for later external remediation (audit evidence only):

| Study year | Component | EC | Status / qualification |
|---|---|---:|---|
| 1 | Proof Techniques (theory and practical) (TW1-11T/P) | 5 | required; Combined theory 3 + practical 2; code notation denotes two existing subparts, not a catalogue code. |
| 1 | Calculus (TW1-12) | 5 | required |
| 1 | Introduction to Programming (TW1-13) | 5 | required |
| 1 | Modelling 1 (TW1-21) | 5 | required |
| 1 | Analysis 1 (TW1-22) | 5 | required |
| 1 | Linear Algebra 1 (TW1-23) | 5 | required |
| 1 | Discrete Mathematics (TW1-31) | 5 | required |
| 1 | Analysis 2 (TW1-32) | 5 | required |
| 1 | Linear Algebra 2 (TW1-33) | 5 | required |
| 1 | Modelling 2 (TW1-41) | 5 | required |
| 1 | Ordinary Differential Equations (TW1-42) | 5 | required |
| 1 | Introduction to Probability (TW1-43) | 5 | required |
| 2 | Introduction to Statistics (TW2-11) | 5 | required |
| 2 | Real Analysis (TW2-12) | 5 | required |
| 2 | Optimisation (TW2-13) | 5 | required |
| 2 | Modelling 3 (TW2-21) | 5 | required |
| 2 | Complex Function Theory (TW2-22) | 5 | required |
| 2 | Partial Differential Equations (TW2-23) | 5 | required |
| 2 | Numerical Methods (TW2-31) | 5 | required |
| 2 | Measure Theory and Probability (TW2-32) | 5 | required |
| 2 | Modelling 4 (TW2-41) | 5 | required |
| 2 | Algebra (TW2-42) | 5 | required |
| 2 | Advanced Statistics (TW-E01) | 5 | restricted-choice; Q3 first-listed mathematics option. |
| 2 | Algorithm Design (TW-E99) | 5 | restricted-choice; Q4 first-listed non-mathematical option; exactly one such choice overall. |
| 3 | Minor | 30 | open-choice |
| 3 | Machine Learning (TW-E02) | 5 | restricted-choice |
| 3 | Markov Processes (TW-E03) | 5 | restricted-choice |
| 3 | Graph Theory (TW-E04) | 5 | restricted-choice |
| 3 | Bachelor Project (TW3-01) | 15 | required |

Total: **180 EC**; study-year totals **60 + 60 + 60**. Source-backed requirement reconstruction for later remediation; production unchanged and UCR fit unassessed.

Choice and source-context rules:

- Exactly one non-mathematical plus four distinct mathematical choices; first formal options neutral.
- Place E01Q3 and E99Q4 in year 2, remaining three mathematicalQ3 in year 3. Project may occupyQ4 under formal periods 3/4; do not assert exact future timeslots.
- Required prior knowledge, project-entry threshold and minor no-overlap must be checked when implementing; no prerequisites invented.

Result: incorrect; required action: reassess-exception.

Incorrect applies only to the stated external allocation, narrative, choice, source context or normalized-language facts. No independent UCR conclusion or unsupported dated-change inference.

Recommended follow-up: Instantiate four distinct first-listed mathematical options and one first-listed non-mathematical option; preserve current taught courses, proof 3+2 aggregate, minor 30 and project 15. Refresh accessible authority and source-year context.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

Implementation plan — **not implemented; audit only**:

- `data/counselor/decisions/cp-000259.json`, fields: `sources`, `comparator.components tuples`, `comparator.academicYear`, `comparator.primarySource/additionalSources`, `comparator.sourceNotes`, `comparator.route and routeSelection where applicable`, `exception.curriculumContext`, `exception.reason external factual clauses`, `exception.checkedOn`. Instantiate four distinct first-listed mathematical options and one first-listed non-mathematical option; preserve current taught courses, proof 3+2 aggregate, minor 30 and project 15. Refresh accessible authority and source-year context. Apply in existing version 2 compact decision; update sources and source indexes consistently. Preserve existing UCR claims only as historical provenance.
- `data/counselor/comparisons/cp-000259.json`, fields: `comparator.components`, `comparator.sourceNotes`, `comparator.academicYear`, `comparator.primarySourceUrl/additionalSourceUrls`, `comparator.routeSelection where applicable`, `exception.curriculumContext`, `exception.reason`, `exception.checkedOn`. Compile the amended compact decision using current normalized provider; canonical external facts must agree with case evidence and preserve precise choice/optional scope. Do not automatically change exception type or create a comparison.
- `data/counselor/review-programmes.json and existing generated counselor artifacts`, fields: `affected metadata, curriculum, source and route summaries`. Regenerate affected outputs after targeted remediation; keep this audit evidence and immutable provenance.

Dependencies:

- Validate applicable current cohort and sources when implementing; no broad repeated research required for established facts.
- Final UCR feasibility remains a separate stage-two dependency.

Verification and closure checks:

- Every included course counted once; total 180 from source-backed weights, with restricted choices instantiated and genuine open profiling explicit.
- Required-versus-optional claims, route, source context and cohort agree across compact and canonical records.
- Run applicable registry/exception compiler/schema validation and refresh generated summaries; close external fixes independently of UCR feasibility.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000260 — Bachelor Mechanical Engineering

Institution: Delft University of Technology. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-03.

Existing substantive reason: TU Delft Mechanical Engineering is an integrated engineering sequence in statics, mechanics of materials, dynamics, thermodynamics, advanced mechanics, materials science, fluid flow and heat transfer, process engineering, signals, systems and control, robotics and integrated mechanical systems. Four consecutive first-year design projects and three further second-year engineering projects culminate in a 14-EC mechanical-engineering final project. UCR offers useful mathematics, programming, product-design and sustainability courses, but it does not offer the mechanical-science core, engineering laboratory and workshop progression, or cumulative mechanical design and research sequence on which the degree depends. A 24-course response would be an applied mathematics, computing and sustainable-design programme, not Mechanical Engineering.

All 25 stored components and credits are confirmed. The reason understates the formal second-year project group as three projects; it has four, including Process Engineering and Thermodynamics. Full-curriculum authority should be the accessible current OER, rather than an unavailable study-guide URL or an endpoint without a course table.

Provenance: data/counselor/comparisons/cp-000260.json; source worksheet row(s) 273. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [OER BSc Mechanical Engineering and Marine Technology 2026–2027](https://filelist.tudelft.nl/Studentenportal/Faculteitspecifiek/ME/Onderwijs/GERELATEERD/Reglementen/Archief%20Onderwijsreglementen/2026-2027/OER%20BSc%20WB-MT_DEFINITIEF.pdf) — Mechanical curriculum PDF p.25; Marine curriculum p.30; BEP conditions pp.26/31; Current 2026–2027. Mechanical: first and second years ten 6-EC units each; third minor 30, control 6, integrated systems 6, engineer/society 4 and final project 14. Four year-two units are formally grouped as projects, including Process Engineering and Thermodynamics. Marine: year 1 mathematics 12 + mechanics 24 + maritime theory 16 + integration 8=60; year 2 mathematics 12 + advanced mechanics 6 + control 6 + maritime theory 18 + ship-design project 6 + integration 12=60; year 3 minor 30 + dynamics maritime structures 6 + electric drive/conversion 4 + ship motions/manoeuvring 6 + BEP14=60. Mathematical/advanced-mechanics subparts are embedded, not additional courses. MT1466-26 supersedes MT1466. BEP requires all first year and at least 54 second-year credits. Tables visually inspected.
- [Mechanical Engineering programme](https://www.tudelft.nl/onderwijs/opleidingen/bachelors/wb/bsc-werktuigbouwkunde) — Engineering projects and current identity; Current official programme. Dutch ordinary mechanical-engineering degree 180; stored 25 course/choice units and all weights agree with current formal OER. Exception reason says three later projects; formal project group has four, including Process Engineering/Thermodynamics. Correct that factual scope and refresh source evidence without rebuilding the accurate component list.
- [Public current study-guide Mechanical Engineering entry](https://curriculum.tudelft.nl/publisher/api/v0/opleidingen/items/32108) — Degree facts and access limitation; Current 2026–2027. Current 2026–2027 B-WB entry, CROHO56966, Dutch, full-time, three years 180 retrieved. Stored education URL returned 404. This endpoint supplies programme facts/description, not the full course table in its returned payload; use accessible formal OER for full curriculum authority.

External credit structure: Stored component arithmetic totals 180 EC. All 25 stored components and credits are confirmed. The reason understates the formal second-year project group as three projects; it has four, including Process Engineering and Thermodynamics. Full-curriculum authority should be the accessible current OER, rather than an unavailable study-guide URL or an endpoint without a course table.

Verified reconstruction for later external remediation (audit evidence only):

| Study year | Component | EC | Status / qualification |
|---|---|---:|---|
| 1 | Mathematics 1 | 6 | required |
| 1 | Mathematics 2 | 6 | required |
| 1 | Statics | 6 | required |
| 1 | Mechanics of Materials | 6 | required |
| 1 | Dynamics | 6 | required |
| 1 | Thermodynamics | 6 | required |
| 1 | Mechanical Engineering Design Project 1 | 6 | required |
| 1 | Mechanical Engineering Design Project 2 | 6 | required |
| 1 | Mechanical Engineering Design Project 3A | 6 | required |
| 1 | Mechanical Engineering Design Project 3B | 6 | required |
| 2 | Mathematics 3 | 6 | required |
| 2 | Mathematics 4 | 6 | required |
| 2 | Signals and Systems | 6 | required |
| 2 | Materials Science | 6 | required |
| 2 | Advanced Mechanics | 6 | required |
| 2 | Fluid Flow and Heat | 6 | required |
| 2 | Project Advanced Engineering Design | 6 | required |
| 2 | Process Engineering and Thermodynamics | 6 | required |
| 2 | Robotics Project | 6 | required |
| 2 | Materials Science Project | 6 | required |
| 3 | Minor | 30 | open-choice |
| 3 | Systems and Control Engineering | 6 | required |
| 3 | Integrated Mechanical Systems | 6 | required |
| 3 | Engineer and Society | 4 | required |
| 3 | Bachelor Final Project | 14 | required |

Total: **180 EC**; study-year totals **60 + 60 + 60**. Source-backed requirement reconstruction for later remediation; production unchanged and UCR fit unassessed.

Choice and source-context rules:

- Keep accurate current components; open minor/profiling retains approval/no-overlap requirements.
- Four formal second-year projects, including Process Engineering/Thermodynamics, are counted within existing ten 6-credit units.

Result: incorrect; required action: reassess-exception.

Incorrect applies only to the stated external allocation, narrative, choice, source context or normalized-language facts. No independent UCR conclusion or unsupported dated-change inference.

Recommended follow-up: Retain accurate 180 components; correct project-status/count narrative to four year-two projects and refresh full-curriculum source support.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

Implementation plan — **not implemented; audit only**:

- `data/counselor/decisions/cp-000260.json`, fields: `sources`, `comparator.components tuples`, `comparator.academicYear`, `comparator.primarySource/additionalSources`, `comparator.sourceNotes`, `comparator.route and routeSelection where applicable`, `exception.curriculumContext`, `exception.reason external factual clauses`, `exception.checkedOn`. Retain accurate 180 components; correct project-status/count narrative to four year-two projects and refresh full-curriculum source support. Apply in existing version 2 compact decision; update sources and source indexes consistently. Preserve existing UCR claims only as historical provenance.
- `data/counselor/comparisons/cp-000260.json`, fields: `comparator.components`, `comparator.sourceNotes`, `comparator.academicYear`, `comparator.primarySourceUrl/additionalSourceUrls`, `comparator.routeSelection where applicable`, `exception.curriculumContext`, `exception.reason`, `exception.checkedOn`. Compile the amended compact decision using current normalized provider; canonical external facts must agree with case evidence and preserve precise choice/optional scope. Do not automatically change exception type or create a comparison.
- `data/counselor/review-programmes.json and existing generated counselor artifacts`, fields: `affected metadata, curriculum, source and route summaries`. Regenerate affected outputs after targeted remediation; keep this audit evidence and immutable provenance.

Dependencies:

- Validate applicable current cohort and sources when implementing; no broad repeated research required for established facts.
- Final UCR feasibility remains a separate stage-two dependency.

Verification and closure checks:

- Every included course counted once; total 180 from source-backed weights, with restricted choices instantiated and genuine open profiling explicit.
- Required-versus-optional claims, route, source context and cohort agree across compact and canonical records.
- Run applicable registry/exception compiler/schema validation and refresh generated summaries; close external fixes independently of UCR feasibility.
- Keep all 25 correct components unchanged; count Process Engineering/Thermodynamics in the formal four-project year 2 group.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000261 — Bachelor Automotive Technology

Institution: Eindhoven University of Technology. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-03.

Existing substantive reason: Automotive Technology is an integrated electrical, mechanical, computational and control-engineering degree. Its compulsory formation moves from mathematics, computation, signals, systems, dynamics, electromagnetics, electronics and electromechanics into power electronics, sensing and actuation, electric and hybrid powertrain design, road-vehicle dynamics, vehicle networking, control systems, automotive software engineering, autonomous driving, automotive projects and a Bachelor Final Project. UCR offers useful mathematics, programming, data science, image processing, AI, robotics, linear systems, consumer-product design and sustainable-energy courses. It does not provide the required physics and electrical-engineering progression, vehicle mechanics and dynamics, electric-powertrain engineering, embedded and real-time automotive systems, vehicle communications, engineering laboratories, staged automotive design projects or an equivalent automotive capstone. A UCR pathway could address intelligent mobility, vehicle data and sustainable transport as an interdisciplinary theme, but it would not be a defensible Automotive Technology comparator.

Current common-plus-AT curriculum yields 125 core/10 ITEC/45 electives, not 120/15/45. Full current course weights and 10 final project are available; autonomous-vehicle/design-project examples in the elective list are not universal compulsory requirements.

Provenance: data/counselor/comparisons/cp-000261.json; source worksheet row(s) 274. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [Automotive Technology programme](https://studiegids.tue.nl/opleidingen/bachelor-college/majors/automotive-technology) — English degree and automotive identity; Current official programme. English full-time three-year bachelor 180. Overview describes integrated automotive/electrical/mechanical formation. Actual current compulsory-versus-optional status must be taken from current curriculum rows; thematic autonomous-vehicle examples are not universal requirements.
- [EE and Automotive after-revision curriculum 2026–2027](https://assets.w3.tue.nl/w/fileadmin/Education_Guide/Content/Programs/Bachelor%20College/Major%20Electrical%20Engineering/Curriculum/Curriculum%202026-2027/Latest%20version%2020260702%20Bachelor%20curriculum%20EE%20and%20AT%20After%20Revision%202026-2027.pdf) — PDF pp.1–4; version 2 July 2026; Current 2026–2027. Common rows plus only the selected EE or AT rows yield major/core 125 including 10 final project, ITEC Ethics 5 + Society 5, and free electives 45. First year 60; second required major 40 + ITEC5 + electives 15=60; third major 25 + ITEC5 + electives 30=60. AT Propulsion Systems 4AUB10 is current name; Computer Architecture is AT year 2 / EE year 1. Autonomous Vehicles 5AID0 and Automotive Design Project 5XSC0 are optional. Semiconductor Technology 5XPG0 is optional. No stacking EE and AT alternatives. Tables visually inspected.

External credit structure: Stored component arithmetic totals 180 EC. Current common-plus-AT curriculum yields 125 core/10 ITEC/45 electives, not 120/15/45. Full current course weights and 10 final project are available; autonomous-vehicle/design-project examples in the elective list are not universal compulsory requirements.

Verified reconstruction for later external remediation (audit evidence only):

| Study year | Component | EC | Status / qualification |
|---|---|---:|---|
| 1 | Calculus variant 2 (2WBB0) | 5 | required |
| 1 | Programming Engineering Challenge (5EWC0) | 10 | required |
| 1 | Circuits (5EPC0) | 5 | required |
| 1 | Math 1 (5EZA0) | 5 | required |
| 1 | Signals and Systems (5ESF0) | 5 | required |
| 1 | Electronic Circuits 1 (5ECD0) | 5 | required |
| 1 | Physics for AT (5EPE0) | 5 | required |
| 1 | Spectrum of Automotive (5ATB0) | 5 | required |
| 1 | Math 2 (5EZB0) | 5 | required |
| 1 | Engineering Challenge for Venus (5EID0) | 5 | required |
| 1 | Communication 1 (5ETC0) | 5 | required |
| 2 | Road Vehicle Dynamics (4AUB20) | 5 | required |
| 2 | Electric Circuits for Energy Conversion (5EWE0) | 5 | required |
| 2 | Propulsion Systems (4AUB10) | 5 | required |
| 2 | Computer Architecture (5EIC0) | 5 | required |
| 2 | Sensing, Computing and Actuating (5AIB0) | 5 | required |
| 2 | Electromagnetics 1 (5EPF0) | 5 | required |
| 2 | Multidisciplinary CBL (4CBLW00) | 5 | required |
| 2 | Control Systems (5ESH0) | 5 | required |
| 2 | ITEC Ethics (0LVX30) | 5 | required-ITEC |
| 2 | Free elective space | 15 | open-choice |
| 3 | Electromechanics 1 (5EWF0) | 5 | required |
| 3 | Power Electronics (5APB0) | 5 | required |
| 3 | Vehicle Networking (5AIC0) | 5 | required |
| 3 | Final Bachelor Project (5XEC0) | 10 | required |
| 3 | ITEC Society (0LVX40) | 5 | required-ITEC |
| 3 | Free elective space | 30 | open-choice |

Total: **180 EC**; study-year totals **60 + 60 + 60**. Source-backed requirement reconstruction for later remediation; production unchanged and UCR fit unassessed.

Choice and source-context rules:

- Select common rows plus AT rows only; no EE/AT double counting.
- Core 125 including BEP10, ITEC10, elective 45. Genuine free space stays generic under approval/level conditions.
- Optional autonomous-vehicle/semiconductor/project examples are not universal required core.

Result: incorrect; required action: reassess-exception.

Incorrect applies only to the stated external allocation, narrative, choice, source context or normalized-language facts. No independent UCR conclusion or unsupported dated-change inference.

Recommended follow-up: Reconstruct current AT rows only, correct ITEC/core allocation, current Propulsion Systems name, final project 10 and compulsory-versus-optional narrative; update academic-year/source context.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

Implementation plan — **not implemented; audit only**:

- `data/counselor/decisions/cp-000261.json`, fields: `sources`, `comparator.components tuples`, `comparator.academicYear`, `comparator.primarySource/additionalSources`, `comparator.sourceNotes`, `comparator.route and routeSelection where applicable`, `exception.curriculumContext`, `exception.reason external factual clauses`, `exception.checkedOn`. Reconstruct current AT rows only, correct ITEC/core allocation, current Propulsion Systems name, final project 10 and compulsory-versus-optional narrative; update academic-year/source context. Apply in existing version 2 compact decision; update sources and source indexes consistently. Preserve existing UCR claims only as historical provenance.
- `data/counselor/comparisons/cp-000261.json`, fields: `comparator.components`, `comparator.sourceNotes`, `comparator.academicYear`, `comparator.primarySourceUrl/additionalSourceUrls`, `comparator.routeSelection where applicable`, `exception.curriculumContext`, `exception.reason`, `exception.checkedOn`. Compile the amended compact decision using current normalized provider; canonical external facts must agree with case evidence and preserve precise choice/optional scope. Do not automatically change exception type or create a comparison.
- `data/counselor/review-programmes.json and existing generated counselor artifacts`, fields: `affected metadata, curriculum, source and route summaries`. Regenerate affected outputs after targeted remediation; keep this audit evidence and immutable provenance.

Dependencies:

- Validate applicable current cohort and sources when implementing; no broad repeated research required for established facts.
- Final UCR feasibility remains a separate stage-two dependency.

Verification and closure checks:

- Every included course counted once; total 180 from source-backed weights, with restricted choices instantiated and genuine open profiling explicit.
- Required-versus-optional claims, route, source context and cohort agree across compact and canonical records.
- Run applicable registry/exception compiler/schema validation and refresh generated summaries; close external fixes independently of UCR feasibility.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000262 — Bachelor Biomedical Engineering

Institution: Eindhoven University of Technology. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-03.

Existing substantive reason: Biomedical Engineering at TU/e is an integrated engineering-and-life-science degree. Its compulsory formation connects chemistry, cell biology, physiology and pathology with mathematics, physics, programming and biomedical data analysis, biomechanics and mechanobiology, biomedical imaging and measurement, biomaterials and tissue engineering, modelling, laboratory experimentation, challenge-based design and a 15-EC research project. UCR has substantial biomedical science, molecular and cellular biology, physiology, pathology, pharmacology, one life-science laboratory, mathematics, programming, data science, image processing and robotics. It does not offer the required mechanics and biomechanics progression, continuum and material modelling, biomaterials and tissue-engineering sequence, biomedical instrumentation and signal-acquisition laboratories, imaging physics, engineering-design and fabrication progression, staged biomedical laboratory programme or an equivalent 15-EC biomedical-engineering research project. A UCR pathway could form a strong quantitative biomedical-science curriculum, but it would not be a defensible Biomedical Engineering comparator.

Normalized ENG-only language omits official Dutch instruction. Current formal BBT core 125 includes final project 15: taught/project core 110 plus ITEC10 and electives 45, not 105/15/15/45. Current cohort BBT core must be distinguished from MWT alternatives and elective recommendations.

Provenance: data/counselor/comparisons/cp-000262.json; source worksheet row(s) 275. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [Biomedical Engineering degree facts and two core programmes](https://www.tue.nl/studeren/bachelor-college/bachelor-biomedische-technologie) — Language, standard degree and BMT/MWT alternatives; Current official programme. Official page explicitly states Nederlands en Engels, three years 180. BMT and MWT are separate alternative core programmes after common first year, not cumulative requirements. Current normalized ENG-only language omits Dutch. BMT target is retained; do not substitute the separately normalized MWT target.
- [Biomedical Engineering PER after revision 2026–2027](https://assets.w3.tue.nl/w/fileadmin/Education_Guide/Biomedical%20Engineering/OER%20en%20ER/2026-2027/BSc%20OER%20BME%202026-2027%20AR.pdf) — Articles 3.3–3.5; Appendix 2, PDF pp.20–23,76–79; Current 2026–2027. Partially Dutch/partially English. Core 125 includes BEP15 and multidisciplinary CBL5; ITEC5+5; free 45, at least 30 level 2/3 including at least 15 level 3. First-year Skills Experience 8BA050 spans two 5-credit quarter positions and counts 10 once. BBT and MWT tables are alternatives. BBT year 2eight 5 required + electives 20; year 3three 5 taught + ITEC5 + BEP15 + electives 25. PPD embedded in existing core; MyFuture activities have no extra credits; ITEC requires five Studium Generale activities. BEP prerequisites include 120 total, first-year requirements, PPD and stated later core/CBL/elective completion. Table visually inspected. Formal 8BA020 title Engineering a Tissue differs from gen 26 diagram Organs on Chip; preserve code and check catalogue before asserting an exact renamed title.
- [Biomedical Engineering generation 26 curriculum](https://assets.w3.tue.nl/w/fileadmin/Education_Guide/Biomedical%20Engineering/Bachelor/Programma%27s%20en%20curricula/Curriculum%20gen26.pdf) — Whole diagram; first column BBT versus second MWT; Generation 26; version 12 August 2026. Explicit cohort progression 26/27,27/28,28/29. BBT current codes agree with formal core table. Pink courses are recommendations in elective slots; MWT-specific Heart/Blood, Regenerative Engineering, Mechanobiology and Cancer Cell Biology are not all compulsory BBT. Materials Science remains compulsory BBT. Diagram names 8BA020 CBL: Organs on Chip versus formal Engineering a Tissue; code/role unchanged, exact title needs catalogue confirmation. Figure visually inspected.
- [Biomedical Engineering elective space](https://studiegids.tue.nl/opleidingen/bachelor-college/majors/biomedische-technologie/curriculum/keuzeruimte) — Open study space, level requirements and approval; Current official programme. 45 EC free elective space permits multiple departments/other universities under applicable approval and level conditions. Preserve generic profiling rather than forcing the example biomedical recommendations. Current PER controls credit/level requirements.

External credit structure: Stored component arithmetic totals 180 EC. Normalized ENG-only language omits official Dutch instruction. Current formal BBT core 125 includes final project 15: taught/project core 110 plus ITEC10 and electives 45, not 105/15/15/45. Current cohort BBT core must be distinguished from MWT alternatives and elective recommendations.

Verified reconstruction for later external remediation (audit evidence only):

| Study year | Component | EC | Status / qualification |
|---|---|---:|---|
| 1 | Calculus (2MCALCBM) | 5 | required |
| 1 | Organic Chemistry (8BA010) | 5 | required |
| 1 | First-year biomedical CBL project (8BA020) | 5 | required |
| 1 | Physics for Biomedical Engineering (8BA030) | 5 | required |
| 1 | Biochemistry (8BA040) | 5 | required |
| 1 | Skills Experience (8BA050) | 10 | required |
| 1 | Linear Algebra and Multivariable Calculus (8BA060) | 5 | required |
| 1 | Molecular Cell Biology (8BA070) | 5 | required |
| 1 | Programming and Data (8BA080) | 5 | required |
| 1 | Biomechanics (8BA090) | 5 | required |
| 1 | ITEC Engineering Ethics (0LVX10) | 5 | required-ITEC |
| 2 | Dynamic Systems (8BB010) | 5 | required |
| 2 | Introduction to Machine Learning (8BB020) | 5 | required |
| 2 | Clinical Measurement (8BB030) | 5 | required |
| 2 | Project Year 2 (8BA100) | 5 | required |
| 2 | Thermodynamics and Kinetics (8BB040) | 5 | required |
| 2 | Imaging (8BB050) | 5 | required |
| 2 | Flow and Diffusion (8BB060) | 5 | required |
| 2 | Interdisciplinary CBL (4CBLW00) | 5 | required |
| 2 | Free elective space | 20 | open-choice |
| 3 | NAC (8BB070) | 5 | required |
| 3 | Materials Science (8BA110) | 5 | required |
| 3 | Applied Biostatistical Models (2DBM90) | 5 | required |
| 3 | ITEC Engineering for Society (0LVX20) | 5 | required-ITEC |
| 3 | Bachelor Final Project (8FINAL) | 15 | required |
| 3 | Free elective space | 25 | open-choice |

Total: **180 EC**; study-year totals **60 + 60 + 60**. Source-backed requirement reconstruction for later remediation; production unchanged and UCR fit unassessed.

Choice and source-context rules:

- Core 125=110 taught/projects+15 BEP, ITEC10, free 45.
- Skills Experience 10 occupies two quarter positions, counted once; PPD embedded, no extra credits.
- BBT only; MWT core and pink recommended electives remain alternatives.
- 8BA020 formal/current-cohort diagram titles conflict; generic source-backed descriptive name avoids claiming a verified catalogue rename. Verify current title before implementation.
- Electives at least 30 level 2/3 including 15 level 3; mandatory noncredit MyFuture/StudiumGenerale preserved.

Result: incorrect; required action: correct-registry-and-reprocess.

Incorrect applies only to the stated external allocation, narrative, choice, source context or normalized-language facts. No independent UCR conclusion or unsupported dated-change inference.

Recommended follow-up: Correct language to NLD+ENG with rawENG preserved; reconstruct generation 26 BBT current code/credit allocation and PPD embedded status; qualify title discrepancy and optional/MWT-only examples.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

Implementation plan — **not implemented; audit only**:

- `data/registry/programmes.csv`, fields: `languages_json`, `corrected_attributes_json`, `official_source_ids_json/official_source_urls_json`, `normalization_basis and decision_case_ids_json as required by correction workflow`. Set normalized languages_json=["NLD", "ENG"] using the official language evidence. Preserve permanent ID, original source rows and immutable raw ENG offering language. Use the documented post-build registry correction workflow.
- `data/registry/resolution_cases.csv, resolution_decisions.csv and resolution_sources.csv`, fields: `documented language correction and authority linkage`. Record auditable current language correction through repository-supported resolution workflow; keep raw/old language as provenance and retain correction across rebuilds. Do not duplicate or renumber target.
- `data/counselor/decisions/cp-000262.json`, fields: `sources`, `comparator.components tuples`, `comparator.academicYear`, `comparator.primarySource/additionalSources`, `comparator.sourceNotes`, `comparator.route and routeSelection where applicable`, `exception.curriculumContext`, `exception.reason external factual clauses`, `exception.checkedOn`. Correct language to NLD+ENG with rawENG preserved; reconstruct generation 26 BBT current code/credit allocation and PPD embedded status; qualify title discrepancy and optional/MWT-only examples. Apply in existing version 2 compact decision; update sources and source indexes consistently. Preserve existing UCR claims only as historical provenance.
- `data/counselor/comparisons/cp-000262.json`, fields: `comparator.components`, `comparator.sourceNotes`, `comparator.academicYear`, `comparator.primarySourceUrl/additionalSourceUrls`, `comparator.routeSelection where applicable`, `exception.curriculumContext`, `exception.reason`, `exception.checkedOn`. Compile the amended compact decision using current normalized provider; canonical external facts must agree with case evidence and preserve precise choice/optional scope. Do not automatically change exception type or create a comparison.
- `data/counselor/review-programmes.json and existing generated counselor artifacts`, fields: `affected metadata, curriculum, source and route summaries`. Regenerate affected outputs after targeted remediation; keep this audit evidence and immutable provenance.

Dependencies:

- Validate applicable current cohort and sources when implementing; no broad repeated research required for established facts.
- Final UCR feasibility remains a separate stage-two dependency.

Verification and closure checks:

- Every included course counted once; total 180 from source-backed weights, with restricted choices instantiated and genuine open profiling explicit.
- Required-versus-optional claims, route, source context and cohort agree across compact and canonical records.
- Run applicable registry/exception compiler/schema validation and refresh generated summaries; close external fixes independently of UCR feasibility.
- Normalized/provider language ["NLD", "ENG"]; raw offering ENG preserved. Source-row and offering-ID crosswalks still reconcile exactly.
- Confirm exact current 8BA020 title; retain core role 5. Skills Experience 10, final project 15, PPD embedded; free 45 level rules preserved.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000263 — Bachelor Architecture, Urbanism and Building Sciences

Institution: Eindhoven University of Technology. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-03.

Existing substantive reason: TU/e's AUBS bachelor is a project- and studio-intensive built-environment engineering degree. Its common first year integrates calculus, architecture and the city, urban systems, healthy and sustainable environments, structural statics, circularity and energy performance, and structure and architecture with four successive design or research projects. The later programme requires one of four coherent tracks and its project sequence: architectural and urban design, building physics and services, structural engineering and design, or urban systems and real estate. All routes culminate in multidisciplinary project work and a discipline-specific Bachelor End Project. UCR offers useful adjacent courses in spatial planning, GIS and earth observation, sustainable energy and life-cycle analysis, nature-based design, product design, heritage and quantitative methods. It has no architecture or urban-design studio sequence, building-physics and building-services sequence, structural statics and materials progression, construction-technology education, architectural drawing and modelmaking formation, or built-environment engineering capstone. A 24-course UCR programme would therefore replace the target's defining studio, technical and project spine with adjacent liberal-arts and sustainability study and would not be an academically defensible comparison.

A compulsory main track is left unspecified, so generic 130-core does not identify a coherent required programme. AUDE can be selected neutrally. Current formal article/table 125 conflicts with appendix 40-electives and webpage 130; credit closure remains unresolved rather than silently adding five credits.

Provenance: data/counselor/comparisons/cp-000263.json; source worksheet row(s) 276. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [Architecture, Urbanism and Building Sciences after-revision curriculum](https://educationguide.tue.nl/programs/bachelor-college/majors/architecture-urbanism-and-building-sciences/curriculum-start-year-20232024) — Current degree allocation, four main tracks and profiles; Current official programme. Current webpage states core 130, ITEC10, electives 40. A main track must be instantiated: AUDE is first in current formal order, with no evidenced broadest/default route. Binder/Climber/Digger are indicative profiles, not additional compulsory formal tracks. Formal document contains conflicting allocation text; webpage 130 is not sufficient to settle it.
- [Built Environment Bachelor College Course Guide 2026–2027](https://assets.w3.tue.nl/w/fileadmin/Education_Guide/Content/Programs/Bachelor%20College/Major%20Architecture%2C%20Urbanism%20and%20Building%20Sciences/Curriculum/Built%20Environment%20Bachelor%20College%20CourseGuide%202026-2027.pdf) — Printed pp.52–59,64–65,74–77; PDF sheets 27–30,33,38–39; Current official programme. First-year core and four Q4 project alternatives, mandatory later track course/project lines. AUDE year 2 four subjects/four 5-credit projects + multidisciplinary CBL; year 3 Quantitative Methods, Architecture/Technology, Multidisciplinary Project and BEP10. Open profiling remains, with recommendations distinguishable from required bold courses. Spanning a pair of quarters does not itself establish 10 EC. Main track selected independently of UCR. Tables visually inspected.
- [AUBS PER after revision 2026–2027](https://assets.w3.tue.nl/w/fileadmin/Education_Guide/Content/Programs/Bachelor%20College/Major%20Architecture%2C%20Urbanism%20and%20Building%20Sciences/Regulations/PER%20AUBS%20After%20Revision%202026-2027%20%28Curriculum%20start%20year%202023-2024%29.pdf) — Article 3.4, core tables and Appendix 2/3; PDF pp.21–24,81,87; Current 2026–2027. Article 3.4 says core 125 + ITEC10 + at least 45 elective; named AUDE table supports core 125 with Multidisciplinary Project 7P1B30 printed 5, BEP10. Appendix 2 instead says elective 40 (15 year 2/25 year 3), which produces 175 with those named weights; webpage says 130/10/40. Appendix 3 pilot changes level distribution, requiring 45 level 3 overall, at least 30 elective level 2/3, at least 5 elective level 3; it does not explain this five-credit allocation conflict. Do not silently change Multidisciplinary Project 5→10 or elective 40→45. Main trackAUDE first official list, Q4Architectural Design coherent; subjects/projects within track required. Tables visually inspected.

External credit structure: Stored component arithmetic totals 180 EC. A compulsory main track is left unspecified, so generic 130-core does not identify a coherent required programme. AUDE can be selected neutrally. Current formal article/table 125 conflicts with appendix 40-electives and webpage 130; credit closure remains unresolved rather than silently adding five credits.

Result: incorrect; required action: reassess-exception.

Incorrect applies only to the stated external allocation, narrative, choice, source context or normalized-language facts. No independent UCR conclusion or unsupported dated-change inference.

Secondary attribute finding(s):

- Current formal degree credit reconciliation: still-unresolved; stored "130 core +10 ITEC +40 elective", verified "Article/table 125 core +10 ITEC +45 elective; Appendix 2 instead says 40 elective, with project 7P1B30 printed 5.". Separate closure: Track-selection and factual scope corrections can be prepared; full 180 closure needs official reconciliation.

Recommended follow-up: Record exact AUDE track and selection basis; use its named required subjects/projects, distinguish indicative profiles, then reconcile formal project/elective credit conflict before claiming verified 180.

Unresolved factual question / historical limitation: Does applicable AUDE Multidisciplinary Project 7P1B30 carry 5 or 10 EC, and is elective space 40 or 45? Current formal table/article and appendix do not reconcile; obtain corrected regulation/catalogue authority or official clarification.

Implementation plan — **not implemented; audit only**:

- `data/counselor/decisions/cp-000263.json`, fields: `sources`, `comparator.components tuples`, `comparator.academicYear`, `comparator.primarySource/additionalSources`, `comparator.sourceNotes`, `comparator.route and routeSelection where applicable`, `exception.curriculumContext`, `exception.reason external factual clauses`, `exception.checkedOn`. Record exact AUDE track and selection basis; use its named required subjects/projects, distinguish indicative profiles, then reconcile formal project/elective credit conflict before claiming verified 180. Apply in existing version 2 compact decision; update sources and source indexes consistently. Preserve existing UCR claims only as historical provenance.
- `data/counselor/comparisons/cp-000263.json`, fields: `comparator.components`, `comparator.sourceNotes`, `comparator.academicYear`, `comparator.primarySourceUrl/additionalSourceUrls`, `comparator.routeSelection where applicable`, `exception.curriculumContext`, `exception.reason`, `exception.checkedOn`. Compile the amended compact decision using current normalized provider; canonical external facts must agree with case evidence and preserve precise choice/optional scope. Do not automatically change exception type or create a comparison.
- `data/counselor/review-programmes.json and existing generated counselor artifacts`, fields: `affected metadata, curriculum, source and route summaries`. Regenerate affected outputs after targeted remediation; keep this audit evidence and immutable provenance.

Dependencies:

- Current corrected OER/course catalogue or official university clarification reconciling core 125/130, elective 40/45 and Multidisciplinary Project 5/10. Do not manufacture the missing five credits.
- Track selection and optional-versus-required narrative can be corrected independently; complete credit closure must wait.
- Final UCR feasibility remains separately pending.

Verification and closure checks:

- Every included course counted once; total 180 from source-backed weights, with restricted choices instantiated and genuine open profiling explicit.
- Required-versus-optional claims, route, source context and cohort agree across compact and canonical records.
- Run applicable registry/exception compiler/schema validation and refresh generated summaries; close external fixes independently of UCR feasibility.
- AUDE exact name Architectural Urban Design and Engineering; first current formal track in absence of a representative/general route, independently of UCR fit. Preserve mandatory later subject/project line and one coherent first-year project.
- Record controlling authority for any 5/10 project or 40/45 elective correction. Current pilot concerns levels, not an explained five-credit substitution; preserve its 45 level 3 overall /30 elective level 2/3 /5 elective level 3 qualifications.

Research trigger: Applicable official clarification/corrected regulation or current 7P1B30 course entry that also reconciles the degree allocation.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000265 — Bachelor Electrical Engineering

Institution: Eindhoven University of Technology. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-03.

Existing substantive reason: Electrical Engineering at TU/e is a cumulative engineering degree built around electrical and electromagnetic theory, analogue and digital circuits, electronic devices, signal processing, communication, control, embedded systems, measurement, electrical-energy conversion and distribution, engineering laboratories and challenge-based hardware projects before a discipline-specific Bachelor Final Project. UCR offers relevant mathematics, programming, data science, AI, robotics, linear systems, renewable-energy systems and consumer-product design. It does not offer the compulsory electromagnetics, circuit and electronics sequence, semiconductor-device formation, measurement and instrumentation laboratories, communication-hardware sequence, electrical machines and power-electronics progression, embedded-hardware laboratories or integrated electrical-engineering project spine. A 24-course UCR response would be a mathematics-and-computing programme with energy and robotics applications, not a defensible Electrical Engineering comparator.

Current common-plus-EE curriculum yields 125 core/10 ITEC/45 electives, not 120/15/45. Course weights and 10 final project are published; Semiconductor Technology is an optional course, not universal compulsory formation.

Provenance: data/counselor/comparisons/cp-000265.json; source worksheet row(s) 279. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [Electrical Engineering programme](https://www.tue.nl/en/education/bachelor-college/bachelor-electrical-engineering) — English degree and integrated engineering identity; Current official programme. English full-time three-year 180 electrical-engineering bachelor. Current curriculum includes circuits, electronics, electromagnetism, signals, control, communication, energy and projects. Optional semiconductor and medical-instrumentation courses must not be universalised as compulsory.
- [EE and Automotive after-revision curriculum 2026–2027](https://assets.w3.tue.nl/w/fileadmin/Education_Guide/Content/Programs/Bachelor%20College/Major%20Electrical%20Engineering/Curriculum/Curriculum%202026-2027/Latest%20version%2020260702%20Bachelor%20curriculum%20EE%20and%20AT%20After%20Revision%202026-2027.pdf) — PDF pp.1–4; version 2 July 2026; Current 2026–2027. Common rows plus only the selected EE or AT rows yield major/core 125 including 10 final project, ITEC Ethics 5 + Society 5, and free electives 45. First year 60; second required major 40 + ITEC5 + electives 15=60; third major 25 + ITEC5 + electives 30=60. AT Propulsion Systems 4AUB10 is current name; Computer Architecture is AT year 2 / EE year 1. Autonomous Vehicles 5AID0 and Automotive Design Project 5XSC0 are optional. Semiconductor Technology 5XPG0 is optional. No stacking EE and AT alternatives. Tables visually inspected.

External credit structure: Stored component arithmetic totals 180 EC. Current common-plus-EE curriculum yields 125 core/10 ITEC/45 electives, not 120/15/45. Course weights and 10 final project are published; Semiconductor Technology is an optional course, not universal compulsory formation.

Verified reconstruction for later external remediation (audit evidence only):

| Study year | Component | EC | Status / qualification |
|---|---|---:|---|
| 1 | Calculus variant 2 (2WBB0) | 5 | required |
| 1 | Programming Engineering Challenge (5EWC0) | 10 | required |
| 1 | Circuits (5EPC0) | 5 | required |
| 1 | Math 1 (5EZA0) | 5 | required |
| 1 | Signals and Systems (5ESF0) | 5 | required |
| 1 | Electronic Circuits 1 (5ECD0) | 5 | required |
| 1 | Physics for EE (5EPD0) | 5 | required |
| 1 | Computer Architecture (5EIC0) | 5 | required |
| 1 | Math 2 (5EZB0) | 5 | required |
| 1 | Engineering Challenge for Venus (5EID0) | 5 | required |
| 1 | Communication 1 (5ETC0) | 5 | required |
| 2 | Electronic Circuits 2 (5ECE0) | 5 | required |
| 2 | Electrical Power Systems for EE (5EWD0) | 5 | required |
| 2 | Introduction Photonics (5EPG0) | 5 | required |
| 2 | Math 3 (5EZC0) | 5 | required |
| 2 | Signal Processing (5ESG0) | 5 | required |
| 2 | Electromagnetics 1 (5EPF0) | 5 | required |
| 2 | Multidisciplinary CBL (4CBLW00) | 5 | required |
| 2 | Control Systems (5ESH0) | 5 | required |
| 2 | ITEC Ethics (0LVX30) | 5 | required-ITEC |
| 2 | Free elective space | 15 | open-choice |
| 3 | Electromechanics 1 (5EWF0) | 5 | required |
| 3 | Electromagnetics 2 (5EPB0) | 5 | required |
| 3 | Communication 2 (5ETD0) | 5 | required |
| 3 | Final Bachelor Project (5XEC0) | 10 | required |
| 3 | ITEC Society (0LVX40) | 5 | required-ITEC |
| 3 | Free elective space | 30 | open-choice |

Total: **180 EC**; study-year totals **60 + 60 + 60**. Source-backed requirement reconstruction for later remediation; production unchanged and UCR fit unassessed.

Choice and source-context rules:

- Select common rows plus EE rows only; no EE/AT double counting.
- Core 125 including BEP10, ITEC10, elective 45. Genuine free space stays generic under approval/level conditions.
- Optional autonomous-vehicle/semiconductor/project examples are not universal required core.

Result: incorrect; required action: reassess-exception.

Incorrect applies only to the stated external allocation, narrative, choice, source context or normalized-language facts. No independent UCR conclusion or unsupported dated-change inference.

Recommended follow-up: Reconstruct only current common+EE rows and correct ITEC/core allocation, final project 10 and semiconductor/optional scope narrative.

No material external factual question remains within this scope. Final registry/currentness reconciliation and UCR decisions remain subject to the dependencies below where applicable.

Implementation plan — **not implemented; audit only**:

- `data/counselor/decisions/cp-000265.json`, fields: `sources`, `comparator.components tuples`, `comparator.academicYear`, `comparator.primarySource/additionalSources`, `comparator.sourceNotes`, `comparator.route and routeSelection where applicable`, `exception.curriculumContext`, `exception.reason external factual clauses`, `exception.checkedOn`. Reconstruct only current common+EE rows and correct ITEC/core allocation, final project 10 and semiconductor/optional scope narrative. Apply in existing version 2 compact decision; update sources and source indexes consistently. Preserve existing UCR claims only as historical provenance.
- `data/counselor/comparisons/cp-000265.json`, fields: `comparator.components`, `comparator.sourceNotes`, `comparator.academicYear`, `comparator.primarySourceUrl/additionalSourceUrls`, `comparator.routeSelection where applicable`, `exception.curriculumContext`, `exception.reason`, `exception.checkedOn`. Compile the amended compact decision using current normalized provider; canonical external facts must agree with case evidence and preserve precise choice/optional scope. Do not automatically change exception type or create a comparison.
- `data/counselor/review-programmes.json and existing generated counselor artifacts`, fields: `affected metadata, curriculum, source and route summaries`. Regenerate affected outputs after targeted remediation; keep this audit evidence and immutable provenance.

Dependencies:

- Validate applicable current cohort and sources when implementing; no broad repeated research required for established facts.
- Final UCR feasibility remains a separate stage-two dependency.

Verification and closure checks:

- Every included course counted once; total 180 from source-backed weights, with restricted choices instantiated and genuine open profiling explicit.
- Required-versus-optional claims, route, source context and cohort agree across compact and canonical records.
- Run applicable registry/exception compiler/schema validation and refresh generated summaries; close external fixes independently of UCR feasibility.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### cp-000266 — Bachelor Industrial Design

Institution: Eindhoven University of Technology. Audit scope: External-programme identity, defining curriculum, credit/choice reconstruction and source context; no independent UCR feasibility assessment.

Existing formal type: `no-defensible-ucr-match`; existing check date: 2026-10-03.

Existing substantive reason: TU/e Industrial Design is a cumulative studio- and project-based technology-design degree. Students repeatedly integrate user and society research, technology realisation, mathematics/data/computing, business and entrepreneurship, and creativity and aesthetics while building and testing intelligent interactive products, reflecting on competency growth and developing an individual designer identity before a Bachelor Final Project. UCR offers one substantive consumer-product-design course and useful adjacent study in entrepreneurship, consumer research, psychology, computing, data, AI, robotics, sustainability and creative communication. It does not offer the repeated industrial- and interaction-design studio spine, physical-computing and interactive-electronics sequence, sensor integration and digital-fabrication laboratories, interaction aesthetics and visualisation progression, iterative user-testing studios, coached design-competency portfolio or equivalent Industrial Design final project. A 24-course UCR response would be an interdisciplinary liberal-arts programme with one product-design experience and several adjacent subjects, not a defensible Industrial Design comparator.

Current official overview prints exact component credits; its 180 diagram is supported, though formal core 125 versus Appendix 2 elective 50 creates a separate unresolved 185 aggregate. the claim that they are unavailable and three generic 60-year placeholders are inadequate. An old pre 2023 curriculum source is mixed into current context. Current course/project/PPD/ITEC/external-learning structure can be reconstructed.

Provenance: data/counselor/comparisons/cp-000266.json; source worksheet row(s) 280. Canonical provider, normalized registry, source-row and offering-ID sets agree; the current stored target is in scope. This set reconciliation does not itself verify its lifecycle/language attributes.

Current official sources (checked 7 October 2026):

- [Industrial Design programme](https://www.tue.nl/en/education/bachelor-college/bachelor-industrial-design) — Degree facts and integrated expertise areas; Current official programme. English three-year 180 design degree with five expertise areas, recurring design projects and professional/individual designer development. Genuine individual profiling is not a separately mandated formal specialisation.
- [Industrial Design curriculum start 2023/2024 and after](https://studiegids.tue.nl/opleidingen/bachelor-college/majors/industrial-design/curriculum-start-year-20232024) — Current cohort diagram links and exception for 2025 starters; Current 2026–2027. Current programme page links 2627 ordinary after 2023 diagram and a distinct September 2025 variant. Stored /curriculum page is explicitly September 2022 and earlier; replace that source context with applicable current cohort. Do not combine cohort variants.
- [Industrial Design 2627 Bachelor Program ID-BC2.0 overview](https://assets.w3.tue.nl/w/fileadmin/Education_Guide/Content/Programs/Bachelor%20College/Major%20Industrial%20Design/Forms%20and%20Files/2627%20Bachelor%20Program%20ID-BC%202.0%20Overview.pdf) — Whole one-page printed-credit diagram; Current 2026–2027. Year 1 six taught units 5, ITEC Ethics 5, two CBL projects 10 each, PPD5=60. Year 2 four taught units 5 + Project 3 ten + multidiscCBL5 + PPD5 + electives 20=60. Year 3 external learning 25 + ITEC Society 5 + elective 5 + final project 20 + PPD5=60. Required design projects 50 and separately credited PPD15; core 120, ITEC10, profiling 50. ELA is open approved internship/exchange/minor/elective space, not universal internship. Figure visually inspected.
- [Industrial Design PER after revision 2026–2027](https://assets.w3.tue.nl/w/fileadmin/Education_Guide/Content/Programs/Bachelor%20College/Major%20Industrial%20Design/Forms%20and%20Files/ID%20BSc%20model%20OER%202026-2027%20AR.pdf) — Article 3.4 and Appendix 2; PDF pp.20–24,76–81; Current 2026–2027. Article 3.4 prints core 125 and ITEC10, while programme-specific Appendix 2 explicitly prescribes elective 50 (20 year 2/30 year 3). These sum 185 against statutory 180. Current printed-credit diagram instead supports core 120 + ITEC10 + profiling 50=180. Appendix 3 explicitly credits PPD learning line 5 and embeds MyFuture activities there rather than requiring separate MyFuture completion. The diagram 180 is evidence, but formal aggregate conflict remains unresolved; no silent five-credit adjustment. BEP20 and 120-credit start threshold, external-learning approval and prerequisites retained.

External credit structure: Stored component arithmetic totals 180 EC. Current official overview prints exact component credits; its 180 diagram is supported, though formal core 125 versus Appendix 2 elective 50 creates a separate unresolved 185 aggregate. the claim that they are unavailable and three generic 60-year placeholders are inadequate. An old pre 2023 curriculum source is mixed into current context. Current course/project/PPD/ITEC/external-learning structure can be reconstructed.

Result: incorrect; required action: reassess-exception.

Incorrect applies only to the stated external allocation, narrative, choice, source context or normalized-language facts. No independent UCR conclusion or unsupported dated-change inference.

Secondary attribute finding(s):

- Industrial Design formal aggregate reconciliation: still-unresolved; stored "Three 60-year placeholders; no individual-credit evidence claimed", verified "Current diagram explicitly 180; formal core 125+ITEC10+Appendix 2 profiling 50 totals 185.". Separate closure: Known source/component-detail correction is established; formal aggregate needs official reconciliation.

Recommended follow-up: Replace three aggregates with current taught courses,10+10+10+20 project sequence,15 separately credited PPD,10 ITEC and 50 profiling; use applicable ordinary 2026 after-revision diagram, not old 2022 or special 2025 variant.

Unresolved factual question / historical limitation: How does applicable ID Article 3.4 core 125 reconcile with Appendix 2 profiling 50, ITEC10 and the printed-credit diagram core 120/ITEC10/profiling 50? Obtain corrected PER or official clarification; preserve every explicitly printed component credit.

Implementation plan — **not implemented; audit only**:

- `data/counselor/decisions/cp-000266.json`, fields: `sources`, `comparator.components tuples`, `comparator.academicYear`, `comparator.primarySource/additionalSources`, `comparator.sourceNotes`, `comparator.route and routeSelection where applicable`, `exception.curriculumContext`, `exception.reason external factual clauses`, `exception.checkedOn`. Replace three aggregates with current taught courses,10+10+10+20 project sequence,15 separately credited PPD,10 ITEC and 50 profiling; use applicable ordinary 2026 after-revision diagram, not old 2022 or special 2025 variant. Apply in existing version 2 compact decision; update sources and source indexes consistently. Preserve existing UCR claims only as historical provenance.
- `data/counselor/comparisons/cp-000266.json`, fields: `comparator.components`, `comparator.sourceNotes`, `comparator.academicYear`, `comparator.primarySourceUrl/additionalSourceUrls`, `comparator.routeSelection where applicable`, `exception.curriculumContext`, `exception.reason`, `exception.checkedOn`. Compile the amended compact decision using current normalized provider; canonical external facts must agree with case evidence and preserve precise choice/optional scope. Do not automatically change exception type or create a comparison.
- `data/counselor/review-programmes.json and existing generated counselor artifacts`, fields: `affected metadata, curriculum, source and route summaries`. Regenerate affected outputs after targeted remediation; keep this audit evidence and immutable provenance.

Dependencies:

- Corrected applicable PER or official clarification reconciling Article 3.4 core 125 with programme-specific 50 profiling and current diagram 120 core; retain diagram 180 as evidence without claiming the formal 185 aggregate is settled.
- Known obsolete-source/unavailable-credit claim and component detail corrections can be prepared independently.
- Final UCR feasibility remains independently pending.

Verification and closure checks:

- Every included course counted once; total 180 from source-backed weights, with restricted choices instantiated and genuine open profiling explicit.
- Required-versus-optional claims, route, source context and cohort agree across compact and canonical records.
- Run applicable registry/exception compiler/schema validation and refresh generated summaries; close external fixes independently of UCR feasibility.
- Resolve five-credit formal aggregate discrepancy before complete external closure; do not change an explicitly printed diagram course or PPD weight merely to fit core 125.
- Appendix 3 makes MyFuture embedded in creditedPI&V; do not import another degree’s separate MyFuture requirement.

Research trigger: Corrected 2026–2027 ID PER or official explanation of core 125 versus diagram 120 with 50 profiling.

UCR-side assessment pending: **yes**. Existing UCR claims are preserved as provenance only; no independent UCR fit conclusion is drawn. Registry/current-cohort prerequisites must be resolved before any later UCR comparison.

### CP266 diagram credit diagnostic — formal aggregate still unresolved

This is the current printed-credit diagram, not a claim that the conflicting formal aggregate is reconciled.

| Study year | Component | EC | Role |
|---|---|---:|---|
| 1 | Human-centred Design (DDB200) | 5 | required |
| 1 | Calculus (2MCALCID) | 5 | required |
| 1 | Foundations of Data Analytics (2IAB1) | 5 | required |
| 1 | Design <> Research (DDB100) | 5 | required |
| 1 | Creative Programming (DBB100) | 5 | required |
| 1 | Making Sense of Sensors (DAB100) | 5 | required |
| 1 | CBL Project1 (DPB110) | 10 | required |
| 1 | CBL Project2 (DPB120) | 10 | required |
| 1 | Professional and Personal Development learning line1 (DLB384) | 5 | required |
| 1 | ITEC Ethics of Technology and Engineering (0LVX10) | 5 | required-ITEC |
| 2 | Aesthetics of Interaction (DCB200) | 5 | required |
| 2 | Physics for Engineers (3PHYS) | 5 | required |
| 2 | Sustainability and Design (DEB100) | 5 | required |
| 2 | Design Innovation Methods (DAB200) | 5 | required |
| 2 | CBL Project3 (DPB240) | 10 | required |
| 2 | Multidisciplinary CBL (4CBLW00) | 5 | required |
| 2 | Professional and Personal Development learning line2 (DLB385) | 5 | required |
| 2 | Free elective space | 20 | open-choice |
| 3 | External Learning Activities | 25 | approved-profiling |
| 3 | ITEC Engineering for Society (0LVX20) | 5 | required-ITEC |
| 3 | Free elective space | 5 | open-choice |
| 3 | CBL Final Bachelor Project (DPB390) | 20 | required |
| 3 | Professional and Personal Development learning line3 (DLB386) | 5 | required |

Diagram total 180; yearly 60+60+60. Formal aggregate 125+10+50=185 remains blocked on the stated clarification.

### Batch 9 additional source and closure qualifications

- CP254: programme-assigned mixed pairing is NB1430+NB1445 or NB1435+NB1440. First allowed pair is only a qualified representative assignment. Four first-listed formal electives carry 2.5 each; no 5-credit guess. Exact future octal availability, capacity and prerequisites require catalogue verification before detailed scheduling.
- CP258: formal year 3 is explicitly cohort 2024; current prospective September 2026 chart has a different final-year structure. They are not combined or treated as a same-cohort contradiction.
- CP262: formal article 3.3 and prospectus both state Dutch and English. RawENG offering provenance remains. Formal 8BA020 and gen 26 diagram differ in title, with same code and required role; current catalogue title must be checked during implementation.
- CP266: current diagram is explicitly 180 with core 120/ITEC10/profiling 50 and separately creditedPPD15. Article 3.4 core 125 plus 10 ITEC and Appendix 2 profiling 50 totals 185. Component detail is supported; complete formal closure awaits the stated official clarification. Appendix 3 embeds MyFuture inPI&V, not separate extra credits.
- CP263: named formal AUDE core 125 plus 10 ITEC plus appendix 40 elective=175, whereas article minimum 45 would yield 180. The pilot changes level requirements, not an explained five-credit course allocation. The audit keeps this diagnostic conflict and official clarification dependency rather than claiming one inferred allocation as verified.

## Remaining work and next batch

All19 exclusions are complete. Seventy-one of140 exceptions have received the first-stage audit;69 remain pending. Next batch: cp-000267, cp-000270, cp-000273, cp-000274, cp-000275, cp-000276, cp-000277, cp-000278, cp-000280, cp-000283.

Completed/pending reconcile exactly to 159 composite case keys:90 completed,69 pending, no overlap or omissions. All 80 prior cases, source objects and batch evidence sections are preserved. Pending entries have no findings. Secondary unresolved attributes do not change pending case count; production populations and status counts remain unchanged.

After the exhaustive audit, consolidate and execute the targeted action queue. These nine actionable cases contain exact compact/canonical/registry targets, field corrections, dependencies and closure checks. Close established metadata/narrative corrections separately from research-blocked credit reconciliation and subsequent UCR feasibility. Stage two remains independent.

## Production-data boundary

Only this report and data/counselor/qc/stage1-completeness-exceptions.json are changed. No registry correction, compact decision, canonical record, production summary, governing rule or UCR comparison has been implemented.
