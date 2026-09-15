import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { compileCounselorDecision } from './build-counselor-comparison.mjs';

const root = process.cwd();
const fixtureDirectory = path.join(root, 'data', 'counselor', 'decisions', '_regression');
const comparisonDirectory = path.join(root, 'data', 'counselor', 'comparisons');
const ids = ['cp-000004', 'cp-000005'];

function normalizedSubstantiveRecord(record) {
  const copy = structuredClone(record);
  delete copy.validation;
  for (const block of copy.blocks || []) {
    for (const row of block.rows || []) {
      for (const [programmeId, cell] of Object.entries(row.cells || {})) {
        if (!cell || typeof cell !== 'object' || Object.keys(cell).length === 0) delete row.cells[programmeId];
      }
    }
  }
  copy.comparisonAlignment = [...(copy.comparisonAlignment || [])].sort((left, right) => left.componentId.localeCompare(right.componentId));
  return copy;
}

const generated = new Map();
for (const id of ids) {
  const decision = JSON.parse(fs.readFileSync(path.join(fixtureDirectory, `${id}.json`), 'utf8'));
  const actual = compileCounselorDecision(decision, root);
  const expected = JSON.parse(fs.readFileSync(path.join(comparisonDirectory, `${id}.json`), 'utf8'));
  assert.deepStrictEqual(
    normalizedSubstantiveRecord(actual),
    normalizedSubstantiveRecord(expected),
    `${id} compiler regression changed a substantive decision`
  );
  generated.set(id, actual);
  console.log(`${id}: semantic regression reconstruction OK`);
}

const temporaryRoot = fs.mkdtempSync(path.join(os.tmpdir(), 'ucr-counselor-compiler-'));
try {
  fs.cpSync(root, temporaryRoot, {
    recursive: true,
    filter: source => !source.includes(`${path.sep}.git${path.sep}`) && !source.endsWith(`${path.sep}.git`)
  });
  for (const [id, record] of generated) {
    fs.writeFileSync(path.join(temporaryRoot, 'data', 'counselor', 'comparisons', `${id}.json`), `${JSON.stringify(record, null, 2)}\n`);
  }
  execFileSync('npm', ['run', 'validate:counselor'], { cwd: temporaryRoot, stdio: 'inherit' });
  console.log('Generated regression records pass the unchanged counselor validators.');
} finally {
  fs.rmSync(temporaryRoot, { recursive: true, force: true });
}
