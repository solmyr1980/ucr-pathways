# Counselor comparison data

This directory is the implementation home for counselor-app discovery data and the deterministic comparison corpus.

It is separate from `data/examples/`, which contains only examples explicitly selected and approved for the public website and/or LinkedIn.

## Authoritative programme identity

The counselor corpus is keyed by the normalized registry in `data/registry/`.

The stable programme identity is `counselor_programme_id` from `data/registry/programmes.csv` (for example `cp-000001`). Source worksheet rows, `AANGEBODEN_OPLEIDINGCODE`, programme-unit codes and recognized-programme codes are retained as provenance/crosswalk identifiers and must not be used as the counselor comparison identity.

The normalized registry may merge several registrations into one academic target or split a legacy source representation into several genuine academic targets.

Registry eligibility and current counselor production scope are deliberately separate concepts. The current corpus includes only normalized targets with `production_eligible=true`, nonblank `production_order` and `programme_type=standard`. Targets classified as `joint-degree`, `double-bachelor` or `dual-degree-route` remain valid normalized targets but are temporarily excluded from counselor comparison production until an approved presentation method exists. Do not change the registry identity or lifecycle fields to implement that exclusion.

## Pilot files

The pilot files are deliberately small end-to-end test fixtures:

- `pilot-programmes.json` — discovery records linked to existing comparison examples;
- `pilot-interests.json` — a small set of classified interest signals for those fixtures.

They exist to prove the counselor search/retrieval architecture. They are not the production programme registry and must not be interpreted as complete coverage.

The five approved public website examples are also the current structural regression baseline: they demonstrate complete course/component-level comparisons rather than selective summaries. They are not counselor production records and must not be copied into the production corpus as academic substitutes.

## Production shape

Keep three concerns separate:

1. `programmes.json` — deployed programme discovery metadata, one record per normalized target in the current counselor production scope;
2. `interests.json` — deployed programme-interest discovery index linked by `counselor_programme_id`, limited to targets in the current counselor production scope;
3. `comparisons/<counselor_programme_id>.json` — one completed validated deterministic comparison per in-scope normalized target.

Current counselor production records use `schemaVersion: "2.0"`.

## Production compilation

Academic production begins with a compact explicit decision file under `decisions/`. The AI production agent completes the academic work first: comparator reconstruction, evidence mapping, alternative concepts, course selection, semester assignment, curriculum-based labels, block placement, substantive comparator matches and rationales.

For UCR course evidence, retrieve and use the current GitHub `main` version of `data/reference/ucr_courses_enriched.xlsx` under the rules in `data/reference/README.md`. Do not require a separate upload or human-provided copy. Retrieve the workbook once for the production workstream and use it throughout unless repository changes may have altered it. Selected-course facts are verified against that dataset and included explicitly in the decision input.

The deterministic compiler in `scripts/build-counselor-comparison.mjs` reads that decision file plus current GitHub registry data. It constructs normalized provider metadata, assessed programme interests, fixed semester scaffolding, canonical same-course rows and other mechanical schema 2.0 fields. It never makes an academic choice. The GitHub workflow runs the compiler and the existing counselor validators, then commits a new canonical comparison only after every check succeeds. It fails safely when a canonical target file already exists.

The decision-file contract and local command are documented in `decisions/README.md`. Regression fixtures for `cp-000004` and `cp-000005` run in temporary storage and cannot overwrite those canonical records.

Every comparison contains exactly one external comparator followed by **one to three ordered UCR alternatives**. The first UCR alternative is the closest feasible match. Additional alternatives are included only when they pass the evidence, coherence, substantive-distinctness and feasibility gates in the Production Instructions. Three is the maximum, not a quota.

For every current production record:

- top-level `id`, `programmeProvider.counselorProgrammeId` and registry `counselor_programme_id` must be identical;
- normalized registry metadata required by the counselor schema must match `data/registry/programmes.csv`, including canonical name, orders, institution IDs, programme type/status, eligibility, languages, modes and required provenance arrays;
- `academicRationale` must be present before the UCR schedules are treated as production-complete;
- `alternativeSelection` must record the included UCR count, why production stopped, and a concise assessment;
- `comparator.components` must contain one coherent complete 180-EC reconstruction of the external curriculum;
- every UCR comparison cell must carry `courseCode` matching its scheduled course;
- every comparator comparison cell must carry `componentId` matching a canonical comparator component.

`academicRationale` records the evidence-backed academic interest map and the concepts actually used:

- `coreField` — defining disciplinary content, methods, progression and specialist work;
- `adjacentDirections` — genuinely related academic directions supported by evidence; this may be empty;
- `questionsApplications` — evidenced questions, problems, phenomena and applications; this may be empty;
- `alternatives` — exactly one rationale object for every included UCR programme, in the same order as `programmes`.

Each alternative rationale identifies its `programmeId`, concept, evidence-map `basisLabels` and evidence references. Every alternative after the closest match also requires a concrete `distinctnessRationale` explaining the educational choice that differs from the preceding/other included alternatives.

Every production record must also contain `academicRationale.finalMethodologyAudit`. This supplemental audit records any neutral comparator-route choice, generator-eligible interests explicitly covered by the closest-match core, a coherence assessment for every candidate direction, one course-level evidence-map rationale for every scheduled non-PPD course, and a passed academic-progression assessment for every included UCR alternative. The first four counselor records (`cp-000001` through `cp-000004`) have been re-audited against this final methodology and no longer use a legacy exemption.

The academic interest map and each programme concept must be established before UCR course selection. The UCR course catalogue is used to implement those concepts, not to invent them.

`alternativeSelection.stoppingReason` is one of:

- `maximum-reached` — three defensible alternatives were included;
- `insufficient-evidence` — the evidence boundary did not support another coherent concept;
- `not-substantively-distinct` — another concept would be too similar to alternatives already included;
- `not-feasible` — the next concept could not be implemented as a valid UCR programme.

If Alternative 2 fails, production stops at one; do not skip ahead to invent Alternative 3.

Validate normalized production records with `npm run validate:counselor`. The validator intentionally ignores UUID-named pre-normalization comparison files; those files do not count as current production records.

The validator cross-checks normalized production metadata against `data/registry/programmes.csv`, checks the evidence map and per-alternative rationale structure, checks the stopping decision, checks stable component references, rejects duplicate or missing courses/components, rejects identical UCR course sets presented as different alternatives, requires every included programme column to account for exactly 180 EC, and enforces the final-methodology audit contract. Exact three-by-60 symmetry remains a review signal rather than a prohibition.

During incremental corpus production, do **not** create the production `programmes.json` or `interests.json` indexes. Leave pilot indexes unchanged until the comparison corpus is complete and quality-controlled; then build the production indexes in one finalisation step from `data/registry/programmes.csv` and `data/registry/programme_interests.csv`, applying the then-current counselor production-scope rules.

Interest search resolves to normalized counselor targets and then loads the fixed comparison. An interest query never regenerates or personalizes comparison content.

Where `target_mapping_status=inherited-across-split-targets`, the inherited interest row is provenance/general discovery context only. It must not be used as target-specific academic evidence unless independently corroborated by current official evidence for the exact normalized target.

## Comparison blocks

Comparison blocks are a **lossless classification and alignment of complete 180-EC programmes**.

There is no required number of blocks and no default 60/60/60 structure. Every course in every included UCR alternative, including Personal & Professional Development, must appear exactly once. Every canonical comparator component must likewise appear exactly once. Each included programme column must total 180 EC.

Blocks may have unequal sizes and may contain meaningful blank cells when no sufficiently comparable component exists in another programme. Complete coverage must never be confused with forced row-by-row equivalence or visual symmetry.

One cell represents one canonical course/component. Do not bundle several UCR courses into one prose summary. Current counselor production uses `courseCode` and `componentId` as stable validation references while renderers display ordinary names and EC values.

## Registry provenance

Use the crosswalks in `data/registry/` when traceability is needed:

- `programme_source_rows.csv` — legacy workbook row → normalized target;
- `programme_offerings.csv` — offered-programme UUID → normalized target;
- `institutions.csv` — normalized institution identity and source aliases/IDs;
- `resolution_decisions.csv` / `resolution_sources.csv` — identity-resolution evidence for ambiguous cases.

Existing comparison records created before registry normalization or before schema version 2.0 must not be treated as evidence that the corresponding normalized target is production-complete until they have been checked/migrated against the current target ID and production rules.

## Runtime and deployment

GitHub remains the version-controlled source of truth. A deployed counselor app should receive the programme index, interest index and comparison records as part of the same deployment release as the application code rather than retrieving them from `raw.githubusercontent.com` during counselor use.

At runtime, discovery indexes should be loaded and prepared once per application process. Individual comparison records should be read locally on demand. This keeps the app independent of GitHub latency or availability and ensures that code and data belong to the same release.

The authoritative academic production rules are in `docs/UCR_Pathways_Production_Instructions.md` and the reusable batch procedure is in `docs/Counselor_Batch_Assignment.md`. Exact renderer/search implementation remains repository implementation detail under the Master Specification's implementation boundary.
