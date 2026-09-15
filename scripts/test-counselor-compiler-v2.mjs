import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { compileV2 } from './build-counselor-comparison-v2.mjs';

const root = process.cwd();
const fixtureDirectory = path.join(root, 'data', 'counselor', 'decisions', '_regression', 'v2');
const comparisonDirectory = path.join(root, 'data', 'counselor', 'comparisons');
const ids = ['cp-000004', 'cp-000005'];

function normalizedEvidence(evidence) {
  return (evidence || []).map(item => {
    if (item.sourceType === 'official-source') return ['official', item.reference];
    const row = String(item.reference).match(/(\d+)$/)?.[1];
    return ['interest', Number(row)];
  });
}

function normalizedBlocks(blocks) {
  const copy = structuredClone(blocks);
  for (const block of copy) {
    for (const row of block.rows || []) {
      for (const [key, cell] of Object.entries(row.cells || {})) {
        if (!cell || typeof cell !== 'object' || !Object.keys(cell).length) delete row.cells[key];
      }
    }
  }
  return copy;
}

function semanticProjection(record) {
  const rationale = record.academicRationale;
  return {
    identity: [record.schemaVersion, record.origin, record.id, record.cohort],
    programmeProvider: record.programmeProvider,
    comparator: record.comparator,
    programmes: record.programmes,
    evidenceMap: ['coreField', 'adjacentDirections', 'questionsApplications'].map(key =>
      (rationale[key] || []).map(item => [item.label, normalizedEvidence(item.evidence)])
    ),
    alternatives: rationale.alternatives.map(item => ({
      programmeId: item.programmeId,
      concept: item.concept,
      basisLabels: item.basisLabels,
      evidence: normalizedEvidence(item.evidence),
      hasLabelRationale: Boolean(item.labelRationale),
      hasDistinctnessRationale: Boolean(item.distinctnessRationale)
    })),
    assessedInterests: rationale.interestSelection.assessedInterests,
    candidates: rationale.interestSelection.candidateDirections.map(item => ({
      label: item.label,
      basisType: item.basisType,
      generatingInterestRows: item.generatingInterestRows,
      supportingInterestRows: item.supportingInterestRows,
      evidence: item.evidence ? normalizedEvidence(item.evidence) : null,
      disposition: item.disposition,
      programmeId: item.programmeId || null,
      rejectionReason: item.rejectionReason || null
    })),
    routeSelection: rationale.finalMethodologyAudit.comparatorRouteSelection || null,
    closestOwnedInterests: rationale.finalMethodologyAudit.coveredByClosestMatchInterestRows,
    candidateAuditLabels: rationale.finalMethodologyAudit.candidateAssessments.map(item => item.candidateLabel),
    courseAudit: rationale.finalMethodologyAudit.alternatives.map(item => ({
      programmeId: item.programmeId,
      progressionStatus: item.progressionAssessment.status,
      hasProgressionRationale: Boolean(item.progressionAssessment.rationale),
      trace: item.courseTraceability.map(trace => [trace.courseCode, trace.basisLabels, Boolean(trace.rationale)])
    })),
    alternativeSelection: record.alternativeSelection,
    alignment: record.comparisonAlignment
      .map(item => [item.componentId, item.matchType, item.ucrCourseCode || null, Boolean(item.rationale)])
      .sort((left, right) => left[0].localeCompare(right[0])),
    blocks: normalizedBlocks(record.blocks),
    notes: record.notes
  };
}

const generated = new Map();
for (const id of ids) {
  const fixturePath = path.join(fixtureDirectory, `${id}.json`);
  const canonicalPath = path.join(comparisonDirectory, `${id}.json`);
  const fixtureSize = fs.statSync(fixturePath).size;
  const canonicalSize = fs.statSync(canonicalPath).size;
  assert.ok(fixtureSize <= 20_000, `${id} v2 fixture is ${fixtureSize} bytes; maximum is 20,000`);
  assert.ok(fixtureSize / canonicalSize <= 0.30, `${id} v2 fixture exceeds 30% of canonical size`);

  const decision = JSON.parse(fs.readFileSync(fixturePath, 'utf8'));
  const actual = compileV2(decision, root);
  const expected = JSON.parse(fs.readFileSync(canonicalPath, 'utf8'));
  assert.deepEqual(semanticProjection(actual), semanticProjection(expected), `${id} v2 compiler regression changed a substantive decision`);
  generated.set(id, actual);
  console.log(`${id}: ${fixtureSize} bytes; semantic v2 regression PASS`);
}

const validationRoot = fs.mkdtempSync(path.join(os.tmpdir(), 'ucr-counselor-v2-validation-'));
try {
  fs.cpSync(root, validationRoot, {
    recursive: true,
    filter: source => !source.includes(`${path.sep}.git${path.sep}`) && !source.endsWith(`${path.sep}.git`)
  });
  for (const [id, record] of generated) {
    fs.writeFileSync(path.join(validationRoot, 'data', 'counselor', 'comparisons', `${id}.json`), `${JSON.stringify(record, null, 2)}\n`);
  }
  execFileSync('npm', ['run', 'validate:counselor'], { cwd: validationRoot, stdio: 'inherit' });
  console.log('Generated v2 regression records pass the unchanged counselor validators.');
} finally {
  fs.rmSync(validationRoot, { recursive: true, force: true });
}

const base = JSON.parse(fs.readFileSync(path.join(fixtureDirectory, 'cp-000005.json'), 'utf8'));
function expectFailure(name, mutate, pattern) {
  const malformed = structuredClone(base);
  mutate(malformed);
  assert.throws(() => compileV2(malformed, root), pattern);
  console.log(`${name}: PASS`);
}

const firstScheduled = base.alternatives[0].semesters[0][0];
expectFailure('missing course facts', value => {
  value.courses = value.courses.filter(tuple => tuple[0] !== firstScheduled);
}, /lacks verified course facts/);

expectFailure('course without explicit semester placement', value => {
  value.alternatives[0].semesters.pop();
}, /requires six explicit semesters/);

const traceTarget = base.alternatives[0].semesters.flat().find(code => code !== 'ACCPPDE101');
expectFailure('missing traceability', value => {
  value.trace = value.trace.filter(tuple => tuple[0] !== traceTarget);
  value.alternatives[0].traceOverrides = (value.alternatives[0].traceOverrides || []).filter(tuple => tuple[0] !== traceTarget);
}, /lacks required academic traceability/);

expectFailure('missing comparator match or unmatched decision', value => {
  const component = value.blocks.flatMap(block => block[2]).find(row => !row[0] && row[1])[1];
  for (const block of value.blocks) block[2] = block[2].filter(row => row[1] !== component);
}, /lack explicit matched or unmatched status/);

const courseOnlyRow = base.blocks.flatMap(block => block[2]).find(row => row[0] && !row[1]);
expectFailure('missing thematic block', value => {
  for (const block of value.blocks) block[2] = block[2].filter(row => row[0] !== courseOnlyRow[0]);
}, /lack thematic block assignments/);

const ownedRow = base.closestOwnedInterests[0];
expectFailure('incomplete generator-interest ownership', value => {
  value.closestOwnedInterests = value.closestOwnedInterests.filter(row => row !== ownedRow);
}, /lack construction ownership/);

expectFailure('missing label', value => { value.alternatives[0].label = ''; }, /label is required/);
expectFailure('missing alternative concept', value => { value.alternatives[0].concept = ''; }, /alternative concept is required/);
expectFailure('missing progression judgment', value => { value.alternatives[0].progression = null; }, /progression judgment is required/);
expectFailure('missing stopping decision', value => { delete value.selection; }, /stopping decision is required/);
expectFailure('unknown basis ID', value => { value.alternatives[0].basis[0] = 'unknown-basis'; }, /unknown basis id/);
expectFailure('unknown source token', value => { value.basis.core[0][2][0] = 's999'; }, /unknown evidence token/);

const overwriteRoot = fs.mkdtempSync(path.join(os.tmpdir(), 'ucr-counselor-v2-overwrite-'));
try {
  const occupied = path.join(overwriteRoot, 'cp-000005.json');
  fs.writeFileSync(occupied, 'occupied\n');
  assert.throws(() => execFileSync(process.execPath, [
    path.join(root, 'scripts', 'build-counselor-comparison-v2.mjs'),
    path.join(fixtureDirectory, 'cp-000005.json'),
    '--output',
    occupied
  ], { cwd: root, stdio: 'pipe' }), error => String(error.stderr).includes('refusing to overwrite existing canonical comparison'));
  console.log('attempt to overwrite canonical comparison: PASS');
} finally {
  fs.rmSync(overwriteRoot, { recursive: true, force: true });
}

console.log('V2 negative-side-effect tests: PASS');
