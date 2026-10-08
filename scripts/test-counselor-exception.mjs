import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { buildProductionRecord } from './build-counselor-production.mjs';

const root = process.cwd();
// A fixed no-match fixture must not change when the live programme is corrected.
const decision = JSON.parse(fs.readFileSync('data/counselor/decisions/_regression/exceptions/cp-000040-no-match.json', 'utf8'));
const record = buildProductionRecord(decision, root);
assert.equal(record.recordStatus, 'exception');
assert.equal(record.programmes.length, 1);
assert.equal(record.comparator.components.reduce((sum, item) => sum + item.credits, 0), 180);
assert.ok(!Object.hasOwn(record, 'blocks'));

function rejectDecision(mutator, pattern) {
  const value = structuredClone(decision);
  mutator(value);
  assert.throws(() => buildProductionRecord(value, root), pattern);
}
rejectDecision(value => { value.comparator.components.pop(); }, /complete 180-EC comparator/);
rejectDecision(value => { value.exception.reason = ''; }, /substantive reason/);
rejectDecision(value => { value.exception.ucrCourseEvidence = ''; }, /substantive assessment/);
rejectDecision(value => { value.alternatives = []; }, /fabricated UCR alternative/);
rejectDecision(value => { value.exception.type = 'invented'; }, /approved type/);

const pendingDecision = structuredClone(decision);
pendingDecision.exception.type = 'ucr-assessment-pending';
delete pendingDecision.exception.ucrCourseEvidence;
const pendingRecord = buildProductionRecord(pendingDecision, root);
assert.equal(pendingRecord.exception.type, 'ucr-assessment-pending');
assert.equal(pendingRecord.programmes.length, 1);
const incompletePending = structuredClone(pendingDecision);
incompletePending.comparator.components.pop();
assert.throws(() => buildProductionRecord(incompletePending, root), /complete 180-EC comparator/);

const temp = fs.mkdtempSync(path.join(os.tmpdir(), 'ucr-counselor-exception-'));
const comparisonDir = path.join(temp, 'data/counselor/comparisons');
const registryDir = path.join(temp, 'data/registry');
fs.mkdirSync(comparisonDir, { recursive: true });
fs.mkdirSync(registryDir, { recursive: true });
fs.copyFileSync('data/registry/programmes.csv', path.join(registryDir, 'programmes.csv'));
const file = path.join(comparisonDir, 'cp-000040.json');
const validator = path.join(root, 'scripts/validate-counselor-comparison.mjs');
function validate(value) {
  fs.writeFileSync(file, `${JSON.stringify(value, null, 2)}\n`);
  return execFileSync(process.execPath, [validator, 'cp-000040'], { cwd: temp, encoding: 'utf8', stdio: 'pipe' });
}
function rejectRecord(mutator, pattern) {
  const value = structuredClone(record);
  mutator(value);
  assert.throws(() => validate(value), error => pattern.test(String(error.stderr)));
}
try {
  assert.match(validate(record), /Valid counselor production exception/);
  assert.match(validate(pendingRecord), /Valid counselor production exception/);
  const incompletePendingRecord = structuredClone(pendingRecord);
  incompletePendingRecord.comparator.components.pop();
  assert.throws(() => validate(incompletePendingRecord), error => /complete 180-EC external curriculum/.test(String(error.stderr)));
  rejectRecord(value => { value.exception.reason = ''; }, /exception.reason is required/);
  rejectRecord(value => { value.comparator.components.pop(); }, /complete 180-EC external curriculum/);
  rejectRecord(value => { value.programmes.push({ id: 'ucr-1', family: 'ucr', role: 'ucr-alternative' }); }, /only the external comparator/);
  rejectRecord(value => { value.programmeProvider.counselorProgrammeId = 'cp-000041'; }, /id must equal programmeProvider/);
  rejectRecord(value => { value.recordStatus = 'invalid'; }, /recordStatus must be comparison or exception/);
} finally {
  fs.rmSync(temp, { recursive: true, force: true });
}
console.log('Counselor exception compilation and validation: PASS');
