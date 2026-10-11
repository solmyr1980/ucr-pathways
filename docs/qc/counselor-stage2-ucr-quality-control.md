# Independent QC of the ten October 10 UCR assessments

This report and `data/counselor/qc/stage2-ucr-quality-control.json` track the fixed ten-case review separately from ongoing pending-case assessment. The earlier stage-two report records the original decisions; findings here supersede those decisions where explicitly corrected. First-stage history and corrected external curricula remain preserved.

Review order: cp-000076, cp-000097, cp-000098, cp-000119, cp-000205, cp-000246, cp-000247, cp-000248, cp-000253, cp-000254. Each batch contains two whole cases and reviews every included alternative. Subsequent runs use these same files and select the first two IDs without completed QC entries. A partial or blocked review must remain incomplete.

## Batch 1 — Mathematics and Medicine, 11 October 2026

Reviewed against the current Production Instructions, Master Specification, normalized registry and all target-linked interest rows, decision and canonical records, and the GitHub workbook at source commit `aec42fd1a72fc3b1e5ae76fa1f9995f5421dfda4`. Workbook SHA-256: `7bf6c2ae9de0837086ec741c27bd94ed7e85dff2d25bde619ecd50cc4d685879`. Every selected non-PPD course was reviewed against its actual profile or description; existing rationales and prior validation were not treated as proof.

### cp-000076 — Mathematics (Wiskunde)

**Outcome: corrected; three defensible alternatives.** The original computational/statistical and economic-decision alternatives remain accepted with their original course selections and schedules. Their methods are cumulative and substantive: calculus, linear algebra, numerical differential-equation methods, signals/transforms, probability, algorithms and statistical inference. Economic courses supply defined applications in consumer/firm decisions, macroeconomic dynamics and econometric estimation. In the economic alternative, accounting supplies financial measurement, finance supplies risk and investment decisions, and business foundations supplies venture validation/planning as a specific complementary business contribution. These courses are not presented as pure mathematics. The five differing courses implement a coherent economic/business emphasis, rather than arbitrary breadth.

The material error was the stopping decision. The mathematical-medicine interest at registry row 3530 was rejected without adequately testing available connections. The [current official Radboud description](https://www.ru.nl/opleidingen/bachelors/wiskunde), checked 11 October 2026, explicitly supports theoretical solutions to practical medical-sector problems. More decisively, the workbook's Image Processing & Computer Vision course names medical imaging, while Pharmacology explicitly teaches quantitative pharmacological, pharmacokinetic and statistical models, including concentration-response and time-response relationships. A separately named mathematical-medicine sequence is not a prerequisite for a defensible related-fields response.

The added third alternative, **Mathematics, computation & biomedical modelling**, combines the existing mathematical/computational/statistical methods with seven biomedical courses. The life-science gateway, cell biology, physiology and biochemistry supply the biological objects and mechanisms needed to interpret models; the laboratory course supplies understanding of biomedical measurements; anatomy supplies structure/function and imaging interpretation; pharmacology supplies an explicit quantitative medical application. The record distinguishes biological foundations and general computational methods from dedicated medical modelling. It does not claim that every computational course is medical or that the programme provides clinical training.

The third alternative differs by seven courses / 52.5 EC from the first and nine / 67.5 EC from the second. These differences follow its biomedical purpose. Its six advanced courses meet the minimum without counting optional independent research. All three retain the six available mathematical-methods courses and explicit gaps in specialist pure mathematics. The note now identifies both economic and biomedical applications.

All 37 target-linked interest rows were reviewed, including all 14 generator-eligible rows. The medical candidate now generates ucr-3. Physics/astronomy still lacks a cumulative physics/astronomy sequence; mathematics education still lacks mathematics-specific teaching and didactics. Neither rejection depends on professional accreditation or a course title alone. Search-only sustainability, career and communication interests do not generate further curricula. Three accepted alternatives now justify `maximum-reached`.

A smaller evidence correction removes an unsupported reference to convolution from the image-processing trace and uses its documented filtering, segmentation and feature-detection content. The original external components, 54 EC of genuine open space, selected Wiskunde line, neutral route rationale and provider provenance are unchanged. The new biomedical courses have their own UCR rows; no weak counterpart was imposed on the external pure-mathematics requirements. Existing material alignments were reviewed and retained.

### cp-000097 — Medicine (Geneeskunde)

**Outcome: retained; two defensible alternatives.** The decision and canonical record remain unchanged. Both contain a substantial biological foundation: cell biology, physiology, biochemistry, laboratory work, pathology/genetics, anatomy, pharmacology, immunity and organ-system disease mechanisms. Brain/behaviour, abnormal psychology and health psychology address the person experiencing illness. Research design, multivariate inference and systematic review provide specifically relevant methods for evaluating medical and psychological evidence.

The first alternative adds neurobiology, higher cognitive functions, psychodiagnostics/psychotherapies and lifespan development. The second replaces these four courses with social psychology, qualitative inquiry, civil-society theory and human rights. This is a substantive 30-EC change towards the target's evidenced diversity and socially grounded medicine interests. Sociology provides race/gender/institutional analysis; qualitative methods investigate lived social experience; the advanced civil-society course addresses solidarity, trust and migrant inclusion through an organisation project; human rights supplies the legal/ethical framework for liberty, equality and inclusion. These are specific complementary contributions to the social-inclusion concept, not substitutes for medical treatment or specialist health law. Ethics supplies moral reasoning and obligations; it is not represented as specialist medical ethics.

All 39 target-linked interest rows were reviewed, including all eight generator-eligible rows. The person/body/research interests are substantially implemented by the core; the diversity interest generates the second alternative. The patient-contact candidate remains infeasible: academic anatomy encounters, laboratory cases and psychodiagnostics do not supply supervised medical history-taking, diagnostic/therapy decisions or care placements. Career/outcome rows do not independently justify a third alternative.

Every comparator alignment was reviewed. Integrated modules are aligned only where a UCR course addresses an important identifiable subject, with differences in medical scope explicit; additional clinical units remain separate. Development retains its direct lifespan-psychology relationship. The Compas reconstruction for Fall 2026, 24-EC Global Health minor, 6-EC thesis and neutral choices remain unchanged. No new external reconstruction was undertaken.

## Checks and limits

| Case | Alternative | Unique courses / EC | Advanced courses | Different courses from earlier alternatives |
|---|---|---|---|---|
| cp-000076 | ucr-1 | 24 / 180 | 7 | — |
| cp-000076 | ucr-2 | 24 / 180 | 8 | 5 from ucr-1 |
| cp-000076 | ucr-3 | 24 / 180 | 6 | 7 from ucr-1; 9 from ucr-2 |
| cp-000097 | ucr-1 | 24 / 180 | 9 | — |
| cp-000097 | ucr-2 | 24 / 180 | 7 | 4 from ucr-1 |

Every schedule passes workbook names/levels/credits, exact Fall-2026-start availability, formal prerequisites in earlier semesters, four courses per semester and Year-1 PPD. Advisory progression was reviewed; timetable-driven advanced-calculus placement is permitted, and no advisory sequence was converted into a new prerequisite. Medicine's second alternative retains its valid sequence rather than being rearranged for preference alone.

Corrected Mathematics was deterministically compiled through the production builder. Medicine compiler replay was identical to its existing canonical record. Full-corpus comparison, structural and final-rule validators passed, as did both compiler versions, optional-research placement and exception tests, eight repository quality tests, registry-interest validation, and review-index regeneration/replay. All programme columns retain a lossless 180-EC representation; optional research remains a separate 15-EC comparison opportunity, absent from schedules and degree totals. Public examples passed with the existing unrelated p-003 distinctness warning; that example was outside this review.

Academic coherence and comparative contribution remain reasoned review judgments, not outputs proven by validators. Semester feasibility uses planned workbook availability, not guaranteed future delivery. No selected case remains blocked.

Publication uses one atomic connector commit on the latest main, with message `QC first two UCR assessments: recover Mathematics biomedical alternative`. Its hash is resolved from this report/register's Git history and reported with the batch outcome. Shared review indexes were regenerated from the current 438-record corpus; their contents did not change because target identity and comparison/exception status did not change. The separate ongoing assessment register and first-stage files remain unchanged.

**Progress: 2 of 10 cases completed; 8 remain.** Next QC batch: cp-000098 and cp-000119.
