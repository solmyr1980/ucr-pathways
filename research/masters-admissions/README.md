# Dutch master's admissions and UCR curriculum feasibility

This research pilot examines whether official Dutch WO master's admissions requirements can be collected systematically and used to plan undergraduate preparation at University College Roosevelt. It is separate from Pathways production. It covers 40 master's programmes and six worked curricula, with admissions evidence checked on 7 November 2026.

| File | Contents |
| --- | --- |
| [PILOT_PROTOCOL.md](PILOT_PROTOCOL.md) | Sample design, source rules, matching method and quality checks |
| [programmes.csv](programmes.csv) | Forty programme identities, registry provenance, selected specialisations and sampling rationale |
| [admission_requirements.csv](admission_requirements.csv) | Structured admissions criteria and routes |
| [sources.csv](sources.csv) | Official links, published criteria cycles, verification dates and source notes |
| [feasibility.csv](feasibility.csv) | UCR academic judgments, candidates, gaps, open questions and applicant-specific conditions |
| [CURRICULUM_EXAMPLES.md](CURRICULUM_EXAMPLES.md) and [curriculum_schedules.csv](curriculum_schedules.csv) | Six 180 EC examples, admissions mappings and schedules |
| [PILOT_EVALUATION.md](PILOT_EVALUATION.md) | Findings from the initial 24-programme pilot |
| [EXPANSION_REVIEW.md](EXPANSION_REVIEW.md) | Results for 40 programmes, source rechecks and questions for admissions teams |

## Data guide

Join the tables on `programme_id`. The pilot IDs are stable within this dataset. The university and `rio_unit_code` identify the corresponding programme unit in the 21 August 2026 DUO/RIO higher education export. `rio_recognised_or_parent_code` holds the recognised programme code or the parent code for a registered variant. `rio_name` and `rio_study_load_ec` reflect the registry row. `degree`, `degree_type` and `selected_specialisation` describe the university offering. `identity_note` documents material differences between the registry and the university's public offering.

Each `requirement_id` identifies one statement. The `route` field distinguishes the assessed Dutch WO route used for the UCR judgment, common conditions marked `all`, named-degree and bridge alternatives, and institution-specific routes. The `category` identifies what is assessed. The `condition_type` distinguishes requirements, alternatives, conditions, selection factors, recommendations, illustrative benchmarks, unavailable routes and unresolved statements. For an explicit EC quantity, `ects_operator` is `min`, `max`, `range` or `approx` and `ects_value` records the quantity. Use `approx` for figures the university describes as approximate or indicative. Read the statement for route and conditions. A blank quantity means the row carries no separately coded threshold. Requirements in the same applicable route normally apply together. The statement specifies any subminimum, cap, choice, exemption or dependency.

Join `source_id` to `sources.csv`. The `source_location` identifies the relevant heading, article or table on that URL. The `criteria_cycle` is `unstated` when the criteria are undated. An application timetable can name an intake year without separately dating the criteria. `verified_on` records when the pilot checked the source. `source_note` describes material limits or source conflicts.

The `outcome` in the feasibility table uses A for apparently satisfiable published academic requirements, B for identified academic gaps and C for eligibility unresolved on current evidence. `evidence_specificity` rates the published criteria independently of the outcome. `ucr_candidate_courses` is a space-separated list of candidate Osiris codes. It records relevant evidence, not a credit allocation. `rationale` explains the academic judgment, `unresolved_academic_requirements` lists questions that remain open, and `identified_academic_gaps` records gaps supported by the comparison. `non_curricular_conditions` records applicant-dependent or administrative requirements. Blank gap cells carry no separate finding of a demonstrated gap.

The curriculum CSV uses one row per course placement. It records the curriculum name, ordinal semester, YearPlan term, course code, official title and EC. The examples use Fall 2026 through Spring 2029, the last six consecutive fall-entry terms in the current workbook. The course reference is read directly from [the authoritative workbook](../../data/reference/ucr_courses_enriched.xlsx). The workbook's [reference notes](../../data/reference/README.md) explain fields and provenance.

Run `python research/masters-admissions/validate_pilot.py` from the repository root with `openpyxl` available. It checks dataset relationships and delegates schedule checks to the shared validator. Revisit source currency and academic matching separately.

## Finding other Dutch master's programmes

Use [Studiekeuze123's WO master's search](https://opleidingenwidget.studiekeuze123.nl/?niveau=wo-master) or the [Study in NL Studyfinder for English-taught programmes](https://www.studyinnl.org/dutch-education/studies?okp_qualified=yes) to find other destinations, then open the university's own admissions page for the relevant prior degree and intake. Use [DUO/RIO](https://onderwijsdata.duo.nl/datasets/ho_opleidingsoverzicht) to reconcile names and registrations for publicly funded programmes. The structured UCR feasibility judgments cover the 40 programmes in this dataset.
