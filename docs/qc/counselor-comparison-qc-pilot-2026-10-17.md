# UCR Pathways — Counselor comparison quality-control pilot

**Audit date:** 17 October 2026  
**Status:** Read-only independent pilot; no GitHub records have been modified  
**Scope:** Six current canonical comparisons, 12 UCR alternatives, 168 external components (59 matched, 109 unmatched).  
**Decision standard:** `docs/UCR_Pathways_Production_Instructions.md`, especially Sections 5 and 9.1–9.2, and `docs/UCR_Pathways_Master_Specification.md` §5.4.  
**Core question:** Does a shared row represent an important, identifiable overlap of subject, disciplinary method or specific educational function—not just a general resemblance?

## Executive assessment

The six records pass the structural checks applied to their current canonical JSON: 180 EC per programme, 24 distinct UCR courses, six terms of four courses, mandatory PPD, at least six 300-level courses, complete and nonduplicated external component references, one UCR comparison row per selected course code, one comparison-only research opportunity per UCR alternative, complete course-traceability entries and compliant pairwise distinctness.

**Academic alignment is less reliable.** Of 59 existing positive alignments, the pilot judges **45 acceptable, eight debatable and six materially unsupported or misleading**. Among 109 currently unmatched external components, **one clear potential omission** deserves correction, yielding **seven actionable alignment findings**. These are qualitative review judgments, not an estimated corpus-wide error rate.

The strongest concentration is CP019 (the early Arts and Culture Studies comparison). Its four material positive-alignment problems suggest a systematic failure mode: pairing a specialized comparator course with a broad UCR course based on generic policy, economics, project or heritage vocabulary. Later records generally preserve more candid blank rows and disciplinary gaps. Programme concepts and course selections are mostly defensible as explicitly related fields, but some rationales deserve a narrower description.

## Case-by-case results

| Case | Group | UCR alternatives | Matched | Unmatched | Accepted / Debatable / Material positive matches | Overall |
|---|---|---:|---:|---:|---:|---|
| CP001 — Erasmus Bestuurskunde | Original | 2 | 14 | 8 | 14 / 0 / 0 | Accept with minor wording caution |
| CP019 — Erasmus Arts and Culture Studies | Original | 3 | 19 | 7 | 12 / 3 / 4 | Material corrections needed |
| CP330 — Twente Mechanical Engineering | Reassessment | 1 | 11 | 36 | 8 / 2 / 1 | One material alignment to reconsider |
| CP435 — UvA Spanish Language and Culture | Reassessment | 2 | 7 | 13 | 4 / 2 / 1 | One material alignment to reconsider |
| CP043 — Radboud English Language and Culture | No-match reversal | 1 | 3 | 22 | 3 / 0 / 0 | Accept |
| CP459 — WUR Food Technology | No-match reversal | 3 | 5 | 23 | 4 / 1 / 0 | One omitted alignment to reconsider |
| **Total** | | **12** | **59** | **109** | **45 / 8 / 6** | **7 actionable findings, including 1 missed match** |

### CP001 — Bachelor Bestuurskunde, Erasmus University Rotterdam

Both curricula are coherent. The closest UCR alternative combines public institutions, comparative politics, constitutional and international law, sociology, public economics, organization, quantitative and qualitative methods. The sustainability-governance route makes a genuine seven-course shift toward environmental science, climate, water, resource recovery and environmental justice. The shared comparator rows correspond to recognizable core content: political science/comparative politics, sociology, research methods, public economics, institutional governance, philosophy and EU politics. Unmatched policy projects, internship and specialist public administration remain visible.

**No materially erroneous row identified.** One rationale should avoid suggesting that `GOSLAWJ213` Comparative Constitutional Law teaches substantive administrative law. Its match with **Staats- en Bestuursrecht** remains justified by constitutional/state-organization content; the administrative-law portion of the external component is not independently established in the UCR course description.

The `ucr-1` visible label, “Closest match to Bestuurskunde,” is less informative than a curriculum-based label, but it is not a material false claim under the counselor-comparison use case. No change is required merely for style.

### CP019 — International Bachelor Arts and Culture Studies, Erasmus University Rotterdam

The three programmes are academically recognizable and differ by 11–18 courses per pair. Their art, cultural sociology, media, economics, heritage, communication and research components are genuinely relevant to distinct aspects of Arts and Culture Studies. Nevertheless, some external courses receive overly optimistic row alignments. **Four material positive alignments should be corrected:**

1. **Introduction to Cultural Policy → `GOSPOLI311` European Union Politics.** The external course teaches economic, sociological and historical accounts of state intervention in culture. UCR's course teaches EU political institutions, decision rules and policy processes, with no established focus on cultural policy. Shared generic governmental policymaking is insufficient. **Recommendation:** leave external component unmatched unless a genuinely culture-policy-oriented UCR course is demonstrated.
2. **Research Workshop: Management of Arts and Culture → `BENGATE101` Entrepreneurship & Business Foundations.** A specialist research workshop in cultural management is not substantively reproduced by a general entrepreneurship/startup venture project. The existing rationale treats generic applied project work as the common educational function. **Recommendation:** separate rows. The UCR course may remain in the UCR programme if its entrepreneurial contribution is justified independently.
3. **Advanced Economic Aspects of Cultural Industries → `BENECON311` Public Economics.** The external course applies economic reasoning to developments and predictions in specific cultural industries. UCR Public Economics is principally about taxation, public goods, externalities, spending and welfare policy. No material cultural-industry analysis is established. **Recommendation:** leave unmatched or obtain genuine course-specific evidence of a substantive shared topic; do not use generic economic methods alone.
4. **Cultural Heritage Studies → `MCCHEAM112` Introduction to World Archaeology.** The UCR course chiefly examines ancient making and craft production. Erasmus's contemporary heritage course concerns social and institutional construction, authorization and contestation of heritage. Shared interest in objects/pasts is not enough to substantiate the recorded heritage-studies rationale. **Recommendation:** examine `MCCHEAM211` African Art & Heritage, which teaches colonial collecting, heritage ethics and repatriation, as a potentially stronger already-scheduled UCR counterpart, then use a separate row if no substantial match can be justified.

**Three debatable positive matches (retain pending closer syllabus evidence, not automatic corrections):**

- **Contemporary Approaches in Cultural Sociology → `GOSSOCI311` New Issues in Contemporary Social Theory.** Both teach advanced sociology, but the external course's cognitive/production-of-culture approaches differ from UCR's civil-society/decolonial theory. The common content should be specified more tightly before asserting a strong match.
- **Introduction to Statistical Analysis → `DISDATA111` Introduction to Data Science.** Quantitative data preparation and visualization overlap, but the Erasmus course emphasizes descriptive statistics and SPSS; the UCR summary does not clearly establish comparable statistical instruction.
- **Bachelor Graduation Project → `MCCHEAM316` Writing Art's Histories.** Both involve disciplinary research and writing, but the external component is a required 15-EC individual empirical capstone. UCR's scheduled course must not be presented as an equivalent thesis; the separate optional research opportunity should remain conspicuous. Confirmation of the UCR course's independent-research tasks would clarify whether a shared row is defensible.

**Programme-level assessment:** All three 24-course concepts survive the initial academic-coherence review. A few course rationales push generic entrepreneurial and digital skills toward cultural-sector applications without documented assignments in culture; these should describe transferable contributions rather than pretend every course is explicitly about art or heritage. `MCCCOMM213` Rhetoric in Action is community/public-speaking practice, not intrinsically arts/cultural management. Its inclusion is plausible as public communication but the cultural link should not be exaggerated. No complete programme reconstruction is justified by this pilot alone.

### CP330 — Bachelor Mechanical Engineering, University of Twente

The single UCR alternative is well described as a **related computational systems, robotics and sustainable technology programme**, not mechanical engineering. Mathematical methods, programming, algorithms, robotics, product design, life-cycle assessment, circular materials and renewables provide a coherent composition. The record leaves the substantial mechanics, thermodynamics, materials, machining, manufacturing, thermal-fluid and build/test spine visibly unmatched. This restraint is a strength.

**One material positive alignment:** **Project Mechatronics & Academic Skills 8 → `DISDATA312` Robotics.** Twente's 6.5-EC project involves analysis and redesign of multifunctional mechanical/mechatronic systems, with examples such as fuel pumps, cruise control and wind turbines. UCR Robotics covers computational kinematics, motion planning, collision avoidance and robotic manipulation, not integrated hardware/mechanical redesign. The supplied evidence does not establish that robot-computation content is an important part of this particular project. **Recommendation:** separate rows unless current module-level evidence identifies a substantial overlap; do not delete Robotics from the UCR alternative.

**Two debatable matches:** **Introduction to Finite Element Method → `DISMATH213` Computational & Numerical Methods** (real numerical-analysis foundations, but no explicit finite-element discretization) and **Project Analysis of an Energy System & Academic Skills 2 → `ENSSUST311` Renewable System Design** (shared energy-system analysis but materially different project and engineering functions). Both need a narrower description of the covered part, not an assumption of full equivalence.

No substantive weakness was found in the overall curriculum concept or its explicit limitations.

### CP435 — Spanish Language and Culture, University of Amsterdam

The two UCR alternatives form coherent related-field pathways: (1) empire, migration, global literature, cultural heritage and memory; (2) literature, language, rhetoric and audiovisual expression. They differ by five courses each and explicitly do not claim Spanish-language proficiency, translation, or a sustained Spain/Latin America disciplinary sequence.

**One material positive alignment:** **De Spaanstalige wereld: historisch perspectief → `GOSHIST111` Modern History.** The external course is organized around the history of the Spanish-speaking world; UCR Modern History is a broad survey of nineteenth- and twentieth-century modern societies, mainly European and global processes, without established substantive Spain/Latin America content. The existing rationale relies on background historical context. **Recommendation:** leave separate unless a specific, important and identifiable Spanish-world course unit is verified.

**Two debatable positive matches:** **El español, lengua viva: multilingüismo y diversidad → `HCBCOGN312` Psycholinguistics** (bilingualism and language acquisition are direct components, but not necessarily social variation of Spanish), and **Latin America in the 21st Century → `GOSSOCI311` New Issues in Contemporary Social Theory** (the UCR syllabus genuinely includes Latin American civil-sphere examples, but these do not reproduce the external course's regional breadth). Both should retain explicit scope limitations if aligned.

The alternatives' labels and broad curricular content are defensible as *related* humanities and social-science routes. The first alternative's political/economic context courses must not be represented as dedicated Latin American history or Spanish regional study.

### CP043 — English Language and Culture, Radboud University

The UCR programme has a coherent core in literature, rhetoric, film/media, American cultural representation and modern cultural history. Its distinctive complementary courses have documented functions (e.g., source-based work on a British historical expedition; philosophical study of emotion in fiction/art). The three positive matches—introductory literary interpretation, oral rhetoric and an identifiable American-media portion of British/American popular culture—are defensible under the partial-overlap rule. The comparison preserves large, important gaps in advanced English proficiency, English linguistics, historical language, specialist British periods and a disciplinary thesis.

**No material positive alignment error identified.** The generic unmatched **Academic Communication Skills** could be revisited only after establishing whether the required course's primary function is transferable academic communication or specifically English-language advancement; current title-level evidence is insufficient to overturn the recorded decision.

### CP459 — Food Technology, Wageningen University & Research

All three alternatives are coherent **related-field** routes: biochemistry and circular products; health and eating/consumer behaviour; and environmental resources and sustainable food systems. The food-processing, safety, engineering, chemistry, sensory, packaging and compulsory food-technology thesis gaps remain explicit. The five positive alignments are mostly cautious. **Nutritional Aspects of Foods → `HCBLIFE212` Human Physiology** is debatable but potentially defensible through digestion, nutrient handling and metabolism, provided the record stresses that food composition and specialist nutrition are absent.

**One material missed match:** **Presentation Skills (BSc)** is currently unmatched, while every UCR alternative contains `ACCPPDE101` Personal & Professional Development. UCR explicitly teaches academic presentation and communication skills. The Wageningen programme identifies its presentation-skills component as first-year skills development. This is the kind of specific educational-function overlap accepted for Academic Skills in CP019 and Vaardigheden in CP001. **Recommendation:** align it with the canonical PPD row in each UCR alternative, subject to the component's current course-specific objectives. No extra UCR course, programme change or credit equivalence is implied.

No material failure was found in the existence or coherence of these three related-field programmes, but none should be described as a degree in Food Technology.

## Consolidated classification of problematic positive matches

| Case | External component | Current UCR counterpart | Assessment | Suggested action |
|---|---|---|---|---|
| CP019 | Introduction to Cultural Policy | `GOSPOLI311` EU Politics | Material | Unmatch unless direct cultural-policy overlap is evidenced |
| CP019 | Research Workshop: Management of Arts and Culture | `BENGATE101` Entrepreneurship & Business Foundations | Material | Unmatch; retain UCR course independently |
| CP019 | Advanced Economic Aspects of Cultural Industries | `BENECON311` Public Economics | Material | Unmatch unless industry-specific overlap is evidenced |
| CP019 | Cultural Heritage Studies | `MCCHEAM112` Introduction to World Archaeology | Material | Test `MCCHEAM211` African Art & Heritage as a stronger counterpart |
| CP330 | Project Mechatronics & Academic Skills 8 | `DISDATA312` Robotics | Material | Unmatch absent documented robotics/mechatronics project intersection |
| CP435 | De Spaanstalige wereld: historisch perspectief | `GOSHIST111` Modern History | Material | Unmatch absent specific Spanish-world content |
| CP019 | Contemporary Approaches in Cultural Sociology | `GOSSOCI311` Contemporary Social Theory | Debatable | Confirm specific common content |
| CP019 | Introduction to Statistical Analysis | `DISDATA111` Introduction to Data Science | Debatable | Confirm actual statistical content, distinguish from data cleaning |
| CP019 | Bachelor Graduation Project | `MCCHEAM316` Writing Art's Histories | Debatable | Clarify independent research versus thesis and use comparison-only research separately |
| CP330 | Introduction to Finite Element Method | `DISMATH213` Computational & Numerical Methods | Debatable | Limit rationale to differential-equation/numerical foundations |
| CP330 | Project Analysis of an Energy System & Academic Skills 2 | `ENSSUST311` Renewable System Design | Debatable | Confirm energy-project overlap |
| CP435 | El español, lengua viva: multilingüismo y diversidad | `HCBCOGN312` Psycholinguistics | Debatable | Identify bilingualism as limited overlap, not Spanish sociolinguistics |
| CP435 | Latin America in the 21st Century | `GOSSOCI311` Contemporary Social Theory | Debatable | Keep only if Latin American civil-society treatment is substantively important |
| CP459 | Nutritional Aspects of Foods | `HCBLIFE212` Human Physiology | Debatable | Limit to physiology of nutrient handling |
| CP459 | Presentation Skills (BSc) | PPD, currently unmatched | Potential material omission | Match on academic communication/presentation function if source confirmed |

## Programme-level conclusions

**Academic programme concepts:** All 12 pass an initial independent coherence and label review as described alternatives. The old CP019 pathways tend to rely more heavily on generic cross-disciplinary course-role explanations; CP043 and CP459 are markedly more explicit about what their programmes **do not** teach. No case currently warrants replacing an entire 24-course programme merely to improve row layout.

**Course contribution:** The current records contain 23 traceability statements per UCR alternative (276 total). These were checked against course names, available repository descriptions and the claimed alternative concept. No unequivocal instance of a wholly unrelated course was established in this sample. Several records merit narrower claims about cultural-sector applications, Spanish regional study, mechatronics and food-specific methods. Passing this review does not mean every plausible course choice is optimal.

**Mechanical feasibility:** JSON structure, EC totals, level counts, code identity, six-term placement, optional research and pairwise distinctness were independently recomputed. The stored production audits report that exact planned offerings and prerequisites pass. The GitHub `data/reference/ucr_courses_enriched.xlsx` source was retrieved, but this run could not complete an independent machine-readable extraction of its prerequisite and term fields; therefore the previous workbook-based availability/prerequisite result is **not independently re-certified by this pilot**. This is an evidence limitation, not an observed scheduling defect.

**External reconstruction:** This was primarily a comparison-accuracy pilot, not a fresh 180-EC external-curriculum audit. Current official university programme webpages were consulted for disputed components and degree-level scope. A potential current course-title change in CP019 (Cultural Heritage Studies versus Cultural Heritage in Contemporary Society) should be reconciled during any case-specific correction rather than assumed to establish an error in credited coursework.

## Implications for the full QC exercise

The pilot is not a statistically representative sample and should not be used to project a 6/59 material-alignment rate onto 391 comparisons. Still, it identifies a specific recurring mechanism: **generic or transferable course content is sometimes used as a substitute for the comparator's distinctive subject, rather than being described as complementary study.** This appeared mainly in an original comparison and once each in two later records. Conversely, over-conservative matching can miss a clear academic-skills relationship.

I recommend a **risk-based expansion**, not immediate rewriting of all records. Prioritise original records with unusually high ratios of substantive matches, broad external courses aligned to generic public-policy/business courses, specialized external research projects aligned to ordinary UCR coursework, and recent reversals where an obvious academic-skills match may have been omitted. Retain defensible partial alignments; don't optimize for matching percentages or force symmetry.

Before deciding between targeted and exhaustive corpus review, I would first remediate and recheck the six positive errors and the one missing match found here, then review another small set of original cases across different academic domains to see whether the same mechanisms recur. Any durable methodology change should be limited to the relevant substantive rule and adopted only if existing Section 5 is genuinely insufficient. The current rule already forbids these failures, so the principal problem is its application, not its wording.

## Sources and reproducibility

**Current canonical GitHub cases:**

- https://github.com/solmyr1980/ucr-pathways/blob/main/data/counselor/comparisons/cp-000001.json
- https://github.com/solmyr1980/ucr-pathways/blob/main/data/counselor/comparisons/cp-000019.json
- https://github.com/solmyr1980/ucr-pathways/blob/main/data/counselor/comparisons/cp-000330.json
- https://github.com/solmyr1980/ucr-pathways/blob/main/data/counselor/comparisons/cp-000435.json
- https://github.com/solmyr1980/ucr-pathways/blob/main/data/counselor/comparisons/cp-000043.json
- https://github.com/solmyr1980/ucr-pathways/blob/main/data/counselor/comparisons/cp-000459.json

**UCR evidence:** the current repository's `pilot/shiny/data/courses/{ACC,BEN,DIS,ENS,GOS,HCB,MCC}.json` content descriptions; the current `data/reference/ucr_courses_enriched.xlsx` was fetched but not fully decoded for independent mechanical re-verification; course-specific public UCR pages for PPD and contemporary social theory.

**External official/public course material:**

- Erasmus IBACS: https://www.eur.nl/en/bachelor/international-bachelor-arts-and-culture-studies/programme-overview
- Twente Mechanical Engineering: https://www.utwente.nl/en/bscme/curriculum/curriculum/
- UvA Spanish and Latin American Studies: https://www.uva.nl/programmas/bachelors/spaanse-en-latijns-amerikaanse-studies/studieprogramma/studieprogramma.html
- CEDLA UvA Latin American Studies course descriptions: https://www.cedla.nl/bachelor-courses-latin-american-studies
- WUR Food Technology: https://www.wur.nl/en/education/bachelor/bachelors-food-technology
- UCR PPD: https://ucr.nl/education/personal-professional-development/
- UCR Sociology: https://ucr.nl/education/courses/government-society/sociology/

**Version anchors:** Current canonical Git blob SHAs read at audit: CP001 `01f1b1d`, CP019 `a32347b`, CP330 `09e841e`, CP435 `f9b8c89`, CP043 `5d98d5c`, CP459 `19c2c93`. The GitHub enriched-workbook blob SHA was `c2bcc3b63ec7`.

**Important boundary:** This report is an assessment and proposed-change list, not a production commit or evidence that the flagged records have been revised, recompiled or republished.