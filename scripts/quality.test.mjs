import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import { validateExample } from './example-utils.mjs';
import { visibleProgrammeLabel, comparisonNotes } from '../assets/js/comparison.js';

const records = fs.readdirSync('data/examples').filter(f => f.endsWith('.json'))
  .map(f => JSON.parse(fs.readFileSync(`data/examples/${f}`)));

test('public examples retain four roles, 24 unique courses, advanced courses and PPD', () => {
  for (const record of records) {
    assert.deepEqual(validateExample(record).errors, []);
    for (const programme of record.programmes.slice(1)) {
      const semesters = programme.schedule.semesters;
      const courses = semesters.flatMap(s => s.courses);
      assert.equal(new Set(courses.map(c => c.code)).size, 24);
      assert.ok(courses.filter(c => Number(c.code.slice(-3, -2)) === 3).length >= 6);
      assert.ok(semesters.slice(0, 2).flatMap(s => s.courses).some(c => c.code === 'ACCPPDE101'));
    }
  }
});

test('case-specific labels and substantive notes survive presentation', () => {
  const record = structuredClone(records[0]);
  record.programmes[2].label = 'Economics, politics and institutions';
  assert.equal(visibleProgrammeLabel(record, record.programmes[2]), 'Economics, politics and institutions');
  for (const record of records.filter(r => ['p-002', 'p-004', 'p-005'].includes(r.id))) {
    assert.ok(comparisonNotes(record).length > 0, `${record.id} must retain its limitation note`);
  }
});

test('new production origins require interpretation or a provider-specific key', () => {
  const record = structuredClone(records[0]);
  record.origin = 'student';
  assert.ok(validateExample(record).errors.some(e => e.includes('interestInterpretation')));
  record.interestInterpretation = 'Economics and political institutions.';
  assert.deepEqual(validateExample(record).errors, []);
  record.origin = 'counselor';
  record.programmeProvider = { recognizedProgrammeId: '12345' };
  assert.ok(validateExample(record).errors.some(e => e.includes('programmeProviderId')));
  record.programmeProvider.programmeProviderId = 'provider-specific-id';
  assert.deepEqual(validateExample(record).errors, []);
});

test('unexpanded notes cannot silently disappear from a public export', () => {
  const record = structuredClone(records[0]);
  record.notes = [{ type: 'less-disciplinary-depth', params: { field: 'economics' } }];
  assert.ok(validateExample(record).errors.some(e => e.includes('rendered text')));
});
