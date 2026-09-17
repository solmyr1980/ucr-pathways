import fs from 'node:fs';
import path from 'node:path';
import { applyOptionalIndependentResearch } from './optional-independent-research.mjs';

const root = process.cwd();

function file(rel) { return path.join(root, rel); }
function read(rel) { return fs.readFileSync(file(rel), 'utf8'); }
function write(rel, value) { fs.writeFileSync(file(rel), value, 'utf8'); console.log(`Updated ${rel}`); }
function replaceOnce(value, before, after, label) {
  if (!value.includes(before)) throw new Error(`Migration anchor not found: ${label}`);
  return value.replace(before, after);
}

const currentPackage = JSON.parse(read('package.json'));
if (currentPackage.scripts?.['build:counselor:v2'] === 'node scripts/build-counselor-production.mjs') {
  console.log('Optional independent research migration is already applied; no changes needed.');
  process.exit(0);
}

{
  const rel = 'docs/UCR_Pathways_Master_Specification.md';
  let value = read(rel);
  value = replaceOnce(
    value,
    'The comparison is a **lossless 180-EC representation of each completed programme**, organised into meaningful substantive blocks. Every included UCR course must appear exactly once in the comparison, including Personal & Professional Development. The external programme must likewise account for its complete 180 EC; genuine open-elective, profiling or restricted-choice space must be represented explicitly rather than disappearing from the comparison.\n',
    'The academic comparison is a **lossless 180-EC representation of each completed programme**, organised into meaningful substantive blocks. Every included UCR course must appear exactly once in the comparison, including Personal & Professional Development. The external programme must likewise account for its complete 180 EC; genuine open-elective, profiling or restricted-choice space must be represented explicitly rather than disappearing from the comparison.\n\nIn addition to that 180-EC academic representation, every UCR alternative must display one standardized comparison-only opportunity: **Optional independent research — 15 EC**. This element is not one of the 24 scheduled UCR courses, is not included in the six-semester schedule, and does not count toward the displayed programme\'s 180 EC. Where the comparator contains an identifiable bachelor thesis, capstone, research project or equivalent independent-research component, show the UCR optional-research element in parallel with that comparator component. Where the comparator contains no such component, place the optional-research element in the same substantive block as Personal & Professional Development. The enriched UCR course database must not contain this comparison-only element.\n',
    'Master comparison-integrity paragraph'
  );
  write(rel, value);
}

{
  const rel = 'docs/UCR_Pathways_Production_Instructions.md';
  let value = read(rel);
  value = replaceOnce(
    value,
    '### Step 8 — Build the comparison\n\nOnly after the external curriculum and all included UCR curricula are complete and validated, construct comparison blocks under Section 5.\n',
    '### Step 8 — Build the comparison\n\nOnly after the external curriculum and all included UCR curricula are complete and validated, construct comparison blocks under Section 5.\n\nIdentify whether the comparator has one clear bachelor thesis, capstone, research project or equivalent independent-research component. Record that component\'s stable `componentId` as `researchComponentId`; record `researchComponentId: null` when no such comparator component exists. This decision controls only placement of the standardized UCR optional-research comparison element and does not alter comparator reconstruction, UCR course selection or scheduling.\n',
    'Production Step 8'
  );
  value = replaceOnce(
    value,
    'After all academic decisions and completion-gate judgments are finished, encode them using the active counselor decision contract, `decisionSchemaVersion: "2.0"`. The compact v2 decision must state every fact or judgment that the compiler cannot safely derive, including the comparator route and components, official sources, alternative concepts and outcomes, verified selected-course facts, six explicit semester assignments, final labels and label review, programme-interest construction ownership, course-to-basis relationships and substantive reasons, progression and distinctness judgments, block placement, comparator matches or explicit unmatched status, and the stopping decision.\n',
    'After all academic decisions and completion-gate judgments are finished, encode them using the active counselor decision contract, `decisionSchemaVersion: "2.0"`. The compact v2 decision must state every fact or judgment that the compiler cannot safely derive, including the comparator route and components, official sources, alternative concepts and outcomes, verified selected-course facts, six explicit semester assignments, final labels and label review, programme-interest construction ownership, course-to-basis relationships and substantive reasons, progression and distinctness judgments, block placement, comparator matches or explicit unmatched status, `researchComponentId` (a comparator component ID or explicit `null`), and the stopping decision.\n',
    'Production Step 9'
  );
  value = replaceOnce(
    value,
    '- the displayed components for every included programme column must total **180 EC**;\n- genuine open-elective, profiling or restricted-choice space in the external programme must appear explicitly as such and retain its actual EC value;\n',
    '- the scheduled/canonical components for every included programme column must total **180 EC**;\n- every UCR alternative additionally displays **Optional independent research — 15 EC** as a standardized comparison-only element; it is not a scheduled course, is excluded from the 24-course and 180-EC totals, and must never be added to the enriched UCR course database;\n- when `researchComponentId` identifies a comparator bachelor thesis, capstone, research project or equivalent independent-research component, place the UCR optional-research element in that comparator row in every UCR column when those cells are otherwise blank; if an existing substantive UCR course match already occupies that row, place the optional-research element in a separate row immediately adjacent within the same block rather than displacing the academic match;\n- when `researchComponentId` is `null`, add a separate optional-research row in the same block as `ACCPPDE101` Personal & Professional Development;\n- genuine open-elective, profiling or restricted-choice space in the external programme must appear explicitly as such and retain its actual EC value;\n',
    'Production comparison rules'
  );
  value = replaceOnce(
    value,
    '- comparison blocks that account for every canonical component exactly once while preserving deliberate gaps in horizontal alignment;\n- stable comparison references back to UCR course codes and comparator component IDs in current production records;\n',
    '- comparison blocks that account for every canonical 180-EC component exactly once while preserving deliberate gaps in horizontal alignment, plus the standardized UCR-only **Optional independent research — 15 EC** comparison element;\n- stable comparison references back to UCR course codes and comparator component IDs in current production records, with the optional-research element explicitly marked as comparison-only and excluded from programme-credit totals;\n',
    'Production canonical core'
  );
  value = replaceOnce(
    value,
    '5. **Comparison gate** — every included column accounts for exactly 180 EC; each canonical UCR course/external component appears exactly once; PPD is visible; stable references agree with canonical data; and block alignment preserves genuine gaps rather than imposing a symmetry template.\n',
    '5. **Comparison gate** — every included programme still accounts for exactly 180 EC of canonical curriculum; each canonical UCR course/external component appears exactly once; PPD is visible; **Optional independent research — 15 EC** appears once in every UCR column as a comparison-only element and is excluded from the 180-EC total; its placement follows `researchComponentId` or the PPD-block fallback; stable references agree with canonical data; and block alignment preserves genuine gaps rather than imposing a symmetry template.\n',
    'Production completion gate'
  );
  write(rel, value);
}

{
  const rel = 'data/counselor/decisions/README.md';
  let value = read(rel);
  value = replaceOnce(
    value,
    '- A block row `[courseCode, componentId, rationale]` explicitly matches that comparator component to that UCR course. `[null, componentId, rationale]` explicitly leaves the component unmatched. `[courseCode, null, null]` assigns a UCR course without forcing comparator symmetry.\n',
    '- A block row `[courseCode, componentId, rationale]` explicitly matches that comparator component to that UCR course. `[null, componentId, rationale]` explicitly leaves the component unmatched. `[courseCode, null, null]` assigns a UCR course without forcing comparator symmetry.\n- `researchComponentId` is required in every new v2 production decision. Set it to the stable comparator component ID for the bachelor thesis, capstone, research project or equivalent independent-research component; set it explicitly to `null` when no such comparator component exists. It controls only placement of the standardized **Optional independent research — 15 EC** comparison element.\n',
    'Decision README researchComponentId convention'
  );
  write(rel, value);
}

{
  const rel = 'package.json';
  const pkg = JSON.parse(read(rel));
  pkg.scripts['validate:counselor'] = 'node scripts/validate-counselor-production.mjs';
  pkg.scripts['build:counselor'] = 'node scripts/build-counselor-production.mjs';
  pkg.scripts['build:counselor:v2'] = 'node scripts/build-counselor-production.mjs';
  pkg.scripts['test:optional-research'] = 'node scripts/test-optional-independent-research.mjs';
  pkg.scripts['test:counselor-compiler'] = 'npm run test:counselor-compiler:v1 && npm run test:counselor-compiler:v2 && npm run test:optional-research';
  write(rel, `${JSON.stringify(pkg, null, 2)}\n`);
}

{
  const rel = 'scripts/test-counselor-compiler.mjs';
  let value = read(rel);
  value = replaceOnce(
    value,
    "import { compileCounselorDecision } from './build-counselor-comparison.mjs';\n",
    "import { compileCounselorDecision } from './build-counselor-comparison.mjs';\nimport { stripOptionalIndependentResearch } from './optional-independent-research.mjs';\n",
    'V1 regression import'
  );
  value = replaceOnce(
    value,
    "  const expected = JSON.parse(fs.readFileSync(path.join(comparisonDirectory, `${id}.json`), 'utf8'));\n",
    "  const expected = stripOptionalIndependentResearch(JSON.parse(fs.readFileSync(path.join(comparisonDirectory, `${id}.json`), 'utf8')));\n",
    'V1 regression expected record'
  );
  write(rel, value);
}

{
  const rel = 'scripts/test-counselor-compiler-v2.mjs';
  let value = read(rel);
  value = replaceOnce(
    value,
    "import { compileV2 } from './build-counselor-comparison-v2.mjs';\n",
    "import { compileV2 } from './build-counselor-comparison-v2.mjs';\nimport { stripOptionalIndependentResearch } from './optional-independent-research.mjs';\n",
    'V2 regression import'
  );
  value = replaceOnce(
    value,
    "  const expected = JSON.parse(fs.readFileSync(canonicalPath, 'utf8'));\n",
    "  const expected = stripOptionalIndependentResearch(JSON.parse(fs.readFileSync(canonicalPath, 'utf8')));\n",
    'V2 regression expected record'
  );
  write(rel, value);
}

const existingResearchComponents = {
  'cp-000001': 'pa-bachelor-project',
  'cp-000002': 'misoc-bachelor-project',
  'cp-000003': 'ped-bachelor-project',
  'cp-000004': 'psy-thesis',
  'cp-000005': 'soc-bachelor',
  'cp-000006': 'b3-project',
  'cp-000008': 'crim-analysis-reporting',
  'cp-000009': 'b3-thesis',
  'cp-000010': 'y3-thesis'
};
for (const [id, researchComponentId] of Object.entries(existingResearchComponents)) {
  const rel = `data/counselor/comparisons/${id}.json`;
  const record = JSON.parse(read(rel));
  if (record.optionalIndependentResearch) {
    console.log(`${rel} already contains optional independent research; leaving unchanged`);
    continue;
  }
  applyOptionalIndependentResearch(record, researchComponentId);
  write(rel, `${JSON.stringify(record, null, 2)}\n`);
}

console.log('Optional independent research migration prepared successfully.');
