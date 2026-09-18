# Counselor decision files

Counselor production separates academic judgment from deterministic record construction.

## Active production contract

New production targets use `decisionSchemaVersion: "2.0"`. The AI production agent creates one compact academic decision file at:

`data/counselor/decisions/<counselor_programme_id>.json`

The v2 compiler creates a canonical counselor record with `schemaVersion: "2.0"`. The decision and canonical schema versions are independent even though both are currently 2.0.

Decision files and expected outputs under `_regression/` are test fixtures. They must never be published as production decisions or overwrite canonical comparisons.

## Academic responsibility

The v2 decision file must state every academic choice explicitly:

- comparator route, complete components, credits and official sources;
- alternative concepts, included alternatives and final labels;
- selected UCR courses and six explicit semester assignments;
- programme-interest construction ownership and candidate outcomes;
- course-to-basis relationships and substantive traceability reasons;
- progression and distinctness judgments;
- thematic block assignment;
- every comparator-component match or explicit unmatched decision;
- the alternative stopping decision and substantive notes.

The compiler may derive only mechanical expression and bookkeeping:

- normalized provider metadata and complete assessed-interest objects from current registry files;
- canonical evidence objects from compact tokens;
- fixed semester labels and term codes;
- programme IDs, counts and totals;
- repeated verified course metadata;
- canonical rows, cells, same-course horizontal alignment and alignment objects;
- standardized audit prose and repeated methodology bookkeeping.

The compiler must fail when an academic decision is missing or invalid. It must not select courses, schedule them, design or label alternatives, assign interests or blocks, judge matches, assess progression or distinctness, or decide when to stop.

## Compact v2 conventions

- `sources` declares each official URL once. String tokens such as `s0` refer to zero-based entries in that array.
- Integer evidence tokens refer to stable `programme_interests.csv` registry rows.
- `courses` contains verified tuples: `[courseCode, name, level, credits]`.
- Each alternative supplies six arrays of four exact course codes in `semesters`.
- `basis` assigns short stable IDs such as `c0`, `a0` and `q0` to evidence-backed core, adjacent and question/application items.
- `trace` supplies shared `[courseCode, basisIds, substantiveReason]` decisions. `traceOverrides` records an explicit alternative-specific relationship when the shared decision does not apply.
- A block row `[courseCode, componentId, rationale]` explicitly matches that comparator component to that UCR course. `[null, componentId, rationale]` explicitly leaves the component unmatched. `[courseCode, null, null]` assigns a UCR course without forcing comparator symmetry.
- `researchComponentId` is required in every new v2 production decision. Set it to the stable comparator component ID for the bachelor thesis, capstone, research project or equivalent independent-research component; set it explicitly to `null` when no such comparator component exists. It controls only placement of the standardized **Optional independent research — 15 EC** comparison element.
- `routeSelection` contains the explicit route judgment or `null` when no comparator route is selected.
- `progression` contains the explicit status and concise academic rationale.
- Every additional alternative requires a substantive `distinctness` rationale.

For UCR course selection and feasibility checking, follow `data/reference/README.md`. The human operator must make the current `ucr_courses_enriched.xlsx` available to the AI production agent before production begins. The active compiler deliberately does not make academic course-selection or feasibility decisions from that workbook. The AI verifies those decisions before compilation, and the verified selected-course facts therefore remain explicit compact input rather than compiler lookup data.

## Production workflow

Run locally with:

`npm run build:counselor -- data/counselor/decisions/cp-XXXXXX.json`

The production workflow accepts exactly one newly added root decision file, runs the v2 compiler, validates the proposed canonical record with the unchanged counselor validators, and publishes it only after validation succeeds. Decision files are immutable and the compiler refuses to overwrite an existing canonical comparison.

## V1 fallback

Decision schema v1 remains available temporarily for regression and manual recovery:

- compiler: `scripts/build-counselor-comparison.mjs`;
- fixtures: `data/counselor/decisions/_regression/cp-000004.json` and `cp-000005.json`;
- stable expected outputs shared by the v1 and v2 regression suites: `data/counselor/decisions/_regression/expected/cp-000004.json` and `cp-000005.json`;
- command: `npm run build:counselor:v1 -- <decision-file>`;
- test: `npm run test:counselor-compiler:v1`.

V1 is not accepted for new production through the active workflow. Retain it until at least the first new v2 production target has completed successfully.
