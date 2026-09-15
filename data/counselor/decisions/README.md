# Counselor decision files

Counselor production separates academic judgment from deterministic record construction.

For a new production target, ChatGPT creates one compact decision file at:

`data/counselor/decisions/<counselor_programme_id>.json`

The decision file uses `decisionSchemaVersion: "1.0"` and contains only the facts and judgments that the compiler cannot safely invent:

- the reconstructed comparator and its complete 180-EC component list;
- a verified snapshot of each selected UCR course's code, name, level and credits;
- each alternative's final label, kind and explicit six-semester course-code schedule;
- the evidence map, alternative concepts, labels and rationales;
- candidate-direction decisions and final-methodology audit;
- the comparison block/row layout and comparator-alignment rationales;
- the alternative stopping decision and any notes.

The compiler reads current GitHub registry files and generates the mechanical parts of schema 2.0:

- normalized `programmeProvider` metadata;
- the complete assessed-interest list and construction-role mapping;
- stable record, programme and semester scaffolding;
- expanded course/component cells;
- canonical same-course rows across UCR alternatives;
- comparator alignment objects;
- derived counts and fixed Fall 2026 term labels.

The compiler does not select courses, choose alternatives, schedule courses, name programmes, assign thematic blocks or decide substantive comparator matches. Course facts in the decision file must already have been checked against the enriched UCR course Project Source. The GitHub-side compiler does not access or duplicate that Project Source.

Run locally with:

`npm run build:counselor -- data/counselor/decisions/cp-XXXXXX.json`

The compiler refuses to overwrite an existing canonical comparison. After compilation, run `npm run validate:counselor`.

Files under `_regression/` reproduce existing canonical records for compiler tests only. They never publish or replace a canonical comparison.
