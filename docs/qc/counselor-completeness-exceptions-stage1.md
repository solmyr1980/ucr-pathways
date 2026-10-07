# Counselor completeness and exceptions: first-stage audit

Status: in progress. Batches 1–3 completed on 7 October 2026: all 19 scope exclusions and 11 exceptions audited within the first-stage scope. 129 exceptions remain pending.

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
| Completed exceptions | 140 | 11 | 129 |
| Excluded normalized targets | 19 | 19 | 0 |
| First-stage audit cases | 159 | 30 | 129 |

All 441 in-scope IDs have a canonical filename; there are no missing in-scope IDs, duplicate record filenames or out-of-scope canonical records. The review-index ID set matches both registry scope and canonical filenames. Status totals use that current generated index; all 140 indexed exceptions were additionally read directly to verify ID, exception status and formal type. Enumeration does not constitute a substantive exception audit.

| Formal exception type | Corpus total | Substantively audited |
|---|---:|---:|
| external-programme-unresolved | 20 | 1 |
| no-defensible-ucr-match | 117 | 10 |
| registry-exception | 3 | 0 |

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

## Remaining work and next batch

All 19 scope exclusions are complete. Eleven of 140 exceptions have received the first-stage audit; 129 remain pending. The next batch is: cp-000063, cp-000068, cp-000070, cp-000072, cp-000073, cp-000074, cp-000075, cp-000076, cp-000079, cp-000095.

Completed and pending entries reconcile exactly to 159 cases by audit_population + counselor_programme_id: 30 unique completed keys and 129 unique pending keys, with no overlap or omissions. All 20 earlier case objects are preserved. Pending entries have no audit finding. An audited still-unresolved case is a completed research finding, not a pending inventory entry.

Stage two will independently assess UCR feasibility for every current no-defensible-ucr-match record. Confirmation in this report establishes only the external-programme basis. The exhaustive first-stage audit remains in progress.

## Production-data boundary

Only this report and data/counselor/qc/stage1-completeness-exceptions.json are written. No registry file, comparison, exception decision, production rule or other existing production data is changed.
