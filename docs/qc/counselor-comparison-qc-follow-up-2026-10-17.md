# Counselor comparison QC: pilot corrections and three-case expansion

Date: 17 October 2026. Baseline: `0e8ab8c405184a30ce72574a2a96ad5f72609cbe`.

This follow-up implements the [six-case pilot](counselor-comparison-qc-pilot-2026-10-17.md), adjudicates its eight debatable alignments, and examines three further original comparisons. The governing standard remains Production Instructions Section 5: a shared row needs an important, identifiable subject, disciplinary method or specific educational-function overlap. Full equivalence is not required. General background relevance is insufficient.

## Implemented results

Five decision/canonical record pairs are repaired: CP019, CP035, CP330, CP435 and CP459. Course selections, programme labels, concepts, six-semester schedules and external EC allocations are preserved. Each canonical record is regenerated deterministically from its decision file. The original pilot remains an unchanged historical assessment.

The pilot produces ten alignment changes: eight previously matched components become separate rows, one heritage component moves to a stronger existing UCR row, and one previously unmatched presentation-skills component gains a match. The eight debated matches resolve into three separations and five retained partial matches with narrower rationales. The additional sample produces one further rematch in Biology. Several course-contribution explanations are also corrected where they implied unverified specialist applications or research tasks.

| Pilot case and component | Final decision | Reason |
|---|---|---|
| CP019: Introduction to Cultural Policy | Separate from EU Politics | Institutional policymaking alone does not establish cultural-policy content. |
| CP019: Research Workshop: Management of Arts and Culture | Separate from Entrepreneurship & Business Foundations | Venture development does not establish specialist cultural-management research. |
| CP019: Advanced Economic Aspects of Cultural Industries | Separate from Public Economics | The evidenced economic applications concern public policy, rather than analysis of a cultural industry. |
| CP019: Cultural Heritage Studies | Move from World Archaeology to African Art & Heritage | Colonial collecting, museum acquisition and repatriation provide a direct institutional heritage relationship. |
| CP330: Project Mechatronics & Academic Skills 8 | Separate from Robotics | Computational robotics does not establish the specified mechanical/mechatronic redesign work. |
| CP435: Spanish-speaking world: historical perspective | Separate from Modern History | The UCR survey does not establish substantial Spain/Latin America history. |
| CP459: Presentation Skills (BSc) | Align with PPD | WUR's current skills guidance identifies the specific presentation/reflection function; PPD explicitly teaches academic speaking and presenting. |

For CP019, the formal-source heritage label and EC are retained; the source note records the different title currently used on the programme overview. The webpage title difference alone does not justify changing formal requirements.

### Decisions on the eight debatable matches

| Case and component | Decision | Evidenced boundary |
|---|---|---|
| CP019: Contemporary Approaches in Cultural Sociology | Separate | The specified cultural-sociology approaches are not established by a civil-sphere/social-theory course. |
| CP019: Introduction to Statistical Analysis | Retain, narrower rationale | Data organisation, analysis and visual presentation overlap directly. SPSS and the full descriptive-statistics syllabus are not claimed. |
| CP019: Bachelor Graduation Project | Separate | The UCR evidence establishes art historiography and interpretation, rather than independent empirical inquiry. The standardized optional research opportunity now sits alongside the external thesis. |
| CP330: Introduction to Finite Element Method | Separate | General numerical foundations do not establish finite-element discretisation or analysis. |
| CP330: Energy-system analysis project | Retain, narrower rationale | Both directly analyse energy systems. The material/thermodynamic engineering work remains a difference. |
| CP435: Spanish multilingualism and diversity | Retain, narrower rationale | Bilingualism is an explicit UCR topic. Spanish-specific sociolinguistics and language proficiency are not claimed. |
| CP435: Latin America in the 21st Century | Retain, narrower rationale | Explicit Latin American civil-sphere cases provide a limited regional relationship. They do not reproduce the comparator's regional breadth. |
| CP459: Nutritional Aspects of Foods | Retain, narrower rationale | Digestive physiology, energy handling and metabolism overlap directly. Food composition and specialist nutrition remain absent. |

The two CP435 retentions are qualified judgments from the available programme/course summaries. Detailed UvA catalogue objectives could not be retrieved; neither retention claims a complete syllabus comparison. CP001's minor wording caution does not independently meet the material-error threshold, and CP043 requires no correction.

## Three further original comparisons

The purposive sample comprises CP004 Psychology, CP009 Econometrics and Operations Research, and CP035 Biology. All have historical presentation mode `normal`, and together they cover behavioural science, quantitative economics and natural science. Their 44 positive and 47 unmatched component decisions were screened against current UCR workbook evidence, programme concepts and available official external evidence. This is a diagnostic sample, not a random sample or an error-rate estimate.

| Case | Alternatives | Positive / unmatched components | Outcome |
|---|---:|---:|---|
| CP004: Erasmus Psychology | 3 | 15 / 18 | No further confirmed material error; two detailed external-content checks remain open. |
| CP009: Erasmus Econometrics and Operations Research | 3 | 15 / 17 | No further confirmed material error; one detailed ethics-content check remains open. |
| CP035: Radboud Biology | 3 | 14 / 12 | Correct Human Biology's counterpart and narrow two research/data rationales; one ethics-content check remains open. |

In CP035, the old Human Biology alignment described the UCR life-science gateway as integrated human physiology. Its current enriched profile principally concerns cells, molecular biology and cellular physiology. Radboud's overview explicitly identifies organ systems and human physiology. The already-selected **HCBLIFE212 Human Physiology** therefore replaces **HCBGATE101** as the counterpart. This corrects an inaccurate content claim rather than rebuilding a programme to express a stylistic preference.

The Genomics and Big Data alignment is retained after a specific check: Radboud explicitly identifies large-dataset analysis as part of this component. Data analysis and visualisation can therefore support a partial relationship without claiming genome sequencing, genomic databases or genomic interpretation. The Biology Essay rationale now accurately identifies UCR's systematic-review/meta-analysis methods and removes the implication of primary empirical research.

The Psychology formal 2026–2027 EER explicitly retains **Memory & Language**, despite the recruitment webpage now saying Memory. The canonical name is therefore preserved. The Econometrics recruitment page explicitly describes 2027–2028; it is not substituted for the record's retained 2026–2027 formal sources. These checks illustrate why apparent webpage discrepancies require academic-year verification before correction.

### Four bounded evidence follow-ups

Detailed current external course objectives remain unavailable for CP004 Professional Ethics and Psychological Science; CP009 Ethics in Econometrics; and CP035 Philosophy and Ethics of Science. Their existing rows are retained because this review has not established a material error. They are **not independently certified** from detailed external syllabi. The questions concern professional-code versus general normative ethics, primary empirical investigation versus evidence synthesis, and the ethical content within a combined philosophy/science component. Record these as specific evidence needs, not automatic deletions or instructions to repeat unsuccessful catalogue requests.

## Independent verification

The current GitHub enriched workbook was retrieved through a fresh fetch of `main`, opened successfully and read in full. Its blob is recorded in the [machine-readable evidence](../../data/counselor/qc/alignment-review-2026-10-17.json).

For all nine cases, all **21 UCR programmes / 504 course placements** independently pass exact planned semester availability and formal prerequisites completed in an earlier semester. The check reads each `preq1` and assigned-term column directly from the workbook; it does not infer these results from stored production audits. It also confirms six four-course semesters, 24 distinct codes, Year-1 PPD and at least six 300-level courses. This closes the original pilot's UCR availability/prerequisite verification limitation.

All five repairs reproduce their committed canonical JSON byte for byte through the production compiler. The unchanged corpus-wide counselor validators pass, including complete 180-EC representation, stable references, UCR course-row identity, optional research and pairwise distinctness. Compiler, optional-research and exception regressions pass. No validator or academic-methodology rule is changed.

This remains an alignment/coherence review with independent UCR feasibility checks, not a fresh full reconstruction of every external 180-EC pathway. Inaccessible interactive catalogues limit detailed external-content certification. Passing mechanical checks cannot establish academic correspondence.

## Implication for further QC

The evidence supports continued targeted review of original records. Prioritise specialist projects or subjects paired with generic methods/context, inaccurate course-contribution claims, and rationales that do not identify the actual shared content. Preserve defensible methodological partial matches, including explicitly taught data analysis. The Biology correction also shows the value of comparing rationales with current enriched profiles rather than course titles or older summaries.

The present findings do not justify rebuilding all programmes, changing the matching rule or treating the historical presentation categories as quality scores. A further bounded sample can test whether the same failure recurs beyond the cases examined here. The four source-specific questions above remain explicit follow-up items.

## Implementation commits

- [CP019](https://github.com/solmyr1980/ucr-pathways/commit/87cf98fd85d5ce7c5f672de788beebdd95e2f5ef)
- [CP330](https://github.com/solmyr1980/ucr-pathways/commit/fd149425ab46dce2724b0a4b8abf744a64a1d80d)
- [CP435](https://github.com/solmyr1980/ucr-pathways/commit/f3a98ce4cbc6b7be73bccf1305e34f013767feed)
- [CP459](https://github.com/solmyr1980/ucr-pathways/commit/053546622f4c16c0b5ee7a630f1427f141e54164)
- [CP035](https://github.com/solmyr1980/ucr-pathways/commit/034dd4aab30728b9ebcd4fd8a80c98f980b3ed34)

## Sources

- Current repository `data/reference/ucr_courses_enriched.xlsx`; decision and canonical record pairs for CP019, CP035, CP330, CP435 and CP459; unchanged canonical CP001, CP004, CP009 and CP043.
- [Erasmus IBACS overview](https://www.eur.nl/en/bachelor/international-bachelor-arts-and-culture-studies/programme-overview).
- [Twente Mechanical Engineering module descriptions](https://www.utwente.nl/en/education/bachelor/programmes/mechanical-engineering/study-programme/).
- [UvA Spanish/Latin American Studies curriculum](https://www.uva.nl/programmas/bachelors/spaanse-en-latijns-amerikaanse-studies/studieprogramma/studieprogramma.html) and [CEDLA course descriptions](https://www.cedla.nl/bachelor-courses-latin-american-studies).
- [WUR Food Technology](https://www.wur.nl/en/education/bachelor/bachelors-food-technology) and [WUR course-specific skills guidance](https://support.wur.nl/esc/en/student-career-services/skills?id=kb_article&sysparm_article=KB0017087).
- [Erasmus Psychology EER 2026–2027, Appendix III](https://www.eur.nl/en/essb/media/2026-08-essb-bachelor-eer-26-27) and [programme overview](https://www.eur.nl/bachelor/psychologie/studieprogramma).
- [Econometrics 2026–2027 formal regulations](https://www.eur.nl/en/ese/media/2026-07-oer-bacheloropleidingen-2026-2027), [transition regulations](https://www.eur.nl/en/ese/media/2026-07-overgangsregelingen-bsc-econometrie-2026-2027), and [recruitment overview explicitly labelled 2027–2028](https://www.eur.nl/bachelor/econometrie-en-operationele-research/studieprogramma).
- [Radboud Biology overview](https://www.ru.nl/en/education/bachelors/biology/study-programme), with its linked year-by-year pages explicitly labelled provisional 2027–2028.
