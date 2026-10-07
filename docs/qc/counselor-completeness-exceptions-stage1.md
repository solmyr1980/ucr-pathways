# Counselor completeness and exceptions: first-stage audit

Status: in progress. Batches 1 and 2 completed on 7 October 2026: all 19 scope exclusions and the external basis of one exception audited. 139 exceptions remain pending.

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
| Completed exceptions | 140 | 1 | 139 |
| Excluded normalized targets | 19 | 19 | 0 |
| First-stage audit cases | 159 | 20 | 139 |

All 441 in-scope IDs have a canonical filename; there are no missing in-scope IDs, duplicate record filenames or out-of-scope canonical records. The review-index ID set matches both registry scope and canonical filenames. Status totals use that current generated index; all 140 indexed exceptions were additionally read directly to verify ID, exception status and formal type. Enumeration does not constitute a substantive exception audit.

| Formal exception type | Corpus total | Substantively audited |
|---|---:|---:|
| external-programme-unresolved | 20 | 0 |
| no-defensible-ucr-match | 117 | 1 |
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

## Remaining work and next batch

No scope exclusions remain pending. The remaining 139 exception records are enumerated in the JSON pending queue. The next batch is: cp-000043, cp-000046, cp-000050, cp-000051, cp-000055, cp-000057, cp-000058, cp-000059, cp-000060, cp-000061.

Completed and pending entries reconcile exactly to 159 cases by audit_population + counselor_programme_id: 20 unique completed keys and 139 unique pending keys, with no overlap or omissions. All ten batch-one case objects are preserved. Pending entries carry no audit finding. The exhaustive first-stage audit is not yet complete.

The second-stage audit will independently assess UCR feasibility for every current no-defensible-ucr-match record. First-stage confirmation establishes only the external-programme basis. Scope-exclusion findings make no UCR feasibility judgment.

## Production-data boundary

Only this report and data/counselor/qc/stage1-completeness-exceptions.json are written. No registry file, comparison, exception decision, production rule or other existing production data is changed.
