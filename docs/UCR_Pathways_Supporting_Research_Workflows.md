# UCR Pathways — Supporting Research Workflows

**Status:** Supporting workflow reference

## Purpose and boundary

This document governs two supporting research activities that are useful to UCR Pathways but are **not part of routine student or counselor comparison production**:

1. Dutch bachelor programme-interest enrichment;
2. synthetic interest portfolios for testing, demonstrations or curated-example development.

Routine academic generation is governed by `UCR_Pathways_Production_Instructions.md`. Do not retrieve or load this supporting document for an ordinary counselor production batch unless the task itself concerns enrichment, synthetic interests or maintenance of these supporting datasets.

This document does not govern counselor comparison construction, UCR course selection, public website operations or LinkedIn publication.

---

# 1. Dutch bachelor programme-interest enrichment

Maintain Dutch bachelor programme enrichment as two linked tables within the same working workbook or data artefact:

- `Pathways_programmes` — one row per programme-provider record;
- `programme_interests` — one row per programme-provider × candidate interest signal.

Use a reliable programme-provider key during the historical enrichment stage. A CROHO/recognized-programme code alone is not sufficient where the same programme is offered by multiple providers.

For counselor production and discovery, use the normalized derivative in `data/registry/programme_interests.csv`, linked by permanent `counselor_programme_id`. Original workbook rows remain provenance.

Where `target_mapping_status=inherited-across-split-targets`, historical interest evidence came from a source row later split into distinct normalized targets. Such a row may remain as provenance and general discovery context, but it is not target-specific academic evidence for either split target unless independently corroborated by current official evidence for that exact target.

## 1.1 High-recall research objective

For each programme preserve a high-recall set of distinct, evidence-backed candidate interest signals associated with the programme.

A signal may concern:

- a discipline or field;
- a substantive question;
- a phenomenon or real-world problem;
- a practical, analytical or research skill;
- a meaningful combination of fields;
- a stable route, track, specialization or thematic direction;
- an illustrative/changing curricular topic;
- a career, alumni or further-study direction demonstrating plausible application/outcome.

Prefer current official programme-facing sources.

Do not create signals from isolated course titles when richer programme-facing evidence exists.

Exclude generic preferences about teaching method, group work, campus life, location, class size, workload or similar non-academic features.

## 1.2 Relationship classification

Assign exactly one `interest_relationship` category:

1. **Direct programme interest**;
2. **Stable study direction**;
3. **Curricular topic**;
4. **Illustrative or temporary topic**;
5. **Outcome or individual trajectory**.

Classify the relationship between the signal and the bachelor, not merely the webpage type.

For conservative counselor search ranking, categories 1–2 are the default core. Category 3 may broaden discovery. Categories 4–5 remain searchable but receive lower confidence/priority.

Retain `strength` for compatibility/provenance where present, but use `interest_relationship` as the principal downstream distinction.

## 1.3 Discovery use

The programme-interest data supports the discovery path:

`interest query → ranked in-scope normalized counselor programme targets → fixed counselor comparison`

An interest query does not regenerate or personalize the comparison.

The Production Instructions determine how existing normalized programme-interest rows may be used as academic evidence when constructing a counselor comparison.

---

# 2. Synthetic interest portfolios

Synthetic interests may be used for testing, demonstrations or curated public-example development.

Generate candidates independently of the UCR catalogue. Use the enriched UCR course database only afterward as a feasibility filter rather than as the generator of the wording.

Prefer realistic prospective-student language and vary statement form and specificity.

Avoid catalogue leakage and repetitive combinations.

Synthetic interests are not a substitute for actual student input in the production student app.

---

# 3. Maintenance boundary

Changes to programme-interest research methodology or synthetic-interest generation belong in this supporting document.

Changes to how a counselor or student comparison is actually generated belong in the Production Instructions instead.

Changes to durable product meaning belong in the Master Specification. Changes to website/LinkedIn publication belong in the Web and LinkedIn Workflow.

Do not duplicate full counselor-production methodology here.