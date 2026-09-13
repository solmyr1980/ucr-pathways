import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import { isUcrProgramme, normalizeCell, validateExample } from './example-utils.mjs';
import { visibleProgrammeLabel, comparisonNotes } from '../assets/js/comparison.js';

const records = fs.readdirSync('data/examples').filter(f => f.endsWith('.json'))
  .map(f => JSON.parse(fs.readFileSync(`data/examples/${f}`)));

function comparisonCells(record, programmeId) {
  const cells = [];
  for (const block of record.blocks) {
    for (const row of block.rows) {
      const cell = normalizeCell(row.cells?.[programmeId]);
      if (cell) cells.push({ block, row, cell });
    }
  }
  return cells;
}

function ucrProgrammes(record) {
  return record.programmes.filter(isUcrProgramme);
}

function recordWithAlternativeCount(source, count) {
  const record = structuredClone(source);
  const comparator = record.programmes[0];
  const keptUcr = ucrProgrammes(record).slice(0, count);
  const keptIds = new Set([comparator.id, ...keptUcr.map(programme => programme.id)]);
  record.programmes = [comparator, ...keptUcr];
  record.blocks = record.blocks
    .map(block => ({
      ...block,
      rows: block.rows
        .map(row => ({
          ...row,
          cells: Object.fromEntries(Object.entries(row.cells || {}).filter(([id]) => keptIds.has(id)))
        }))
        .filter(row => Object.values(row.cells).some(cell => normalizeCell(cell)))
    }))
    .filter(block => block.rows.length > 0);

  record.alternativeSelection = {
    includedCount: count,
    stoppingReason: count === 3 ? 'maximum-reached' : 'not-substantively-distinct',
    assessment: count === 3
      ? 'Three defensible alternatives are represented in this regression fixture.'
      : 'The regression fixture intentionally stops before three to exercise variable cardinality.'
  };
  return record;
}

function makeNearDuplicate(source, changedCourses) {
  const record = structuredClone(source);
  const alternatives = ucrProgrammes(record);
  assert.ok(alternatives.length >= 2);
  alternatives[1].schedule = structuredClone(alternatives[0].schedule);
  const courses = alternatives[1].schedule.semesters.flatMap(semester => semester.courses);
  for (let i = 0; i < changedCourses; i += 1) {
    courses[i].code = `TESTDIST${String(i + 1).padStart(3, '0')}`;
    courses[i].name = `Distinctness test course ${i + 1}`;
  }
  return record;
}

test('public examples retain complete 180 EC comparisons and feasible UCR programme structure', () => {
  for (const record of records) {
    assert.deepEqual(validateExample(record).errors, []);
    const alternatives = ucrProgrammes(record);
    assert.ok(alternatives.length >= 1 && alternatives.length <= 3);
    for (const programme of alternatives) {
      const semesters = programme.schedule.semesters;
      const courses = semesters.flatMap(s => s.courses);
      assert.equal(new Set(courses.map(c => c.code)).size, 24);
      assert.ok(courses.filter(c => Number(c.code.slice(-3, -2)) === 3).length >= 6);
      assert.ok(semesters.slice(0, 2).flatMap(s => s.courses).some(c => c.code === 'ACCPPDE101'));
      assert.equal(comparisonCells(record, programme.id).length, 24);
    }
  }
});

test('shared validator accepts one, two and three UCR alternatives', () => {
  const golden = records[0];
  assert.ok(ucrProgrammes(golden).length >= 3, 'golden public example must provide three alternatives for cardinality regression');
  for (const count of [1, 2, 3]) {
    const fixture = recordWithAlternativeCount(golden, count);
    assert.deepEqual(validateExample(fixture).errors, [], `${count}-alternative fixture should validate`);
  }
});

test('comparison validation rejects missing, duplicate and unreferenced curriculum content', () => {
  const missingPpd = structuredClone(records[0]);
  const firstUcrId = ucrProgrammes(missingPpd)[0].id;
  const ppd = comparisonCells(missingPpd, firstUcrId).find(({ cell }) => cell.text === 'Personal & Professional Development');
  assert.ok(ppd, 'golden example must expose PPD in the comparison');
  delete ppd.row.cells[firstUcrId];
  const missingErrors = validateExample(missingPpd).errors;
  assert.ok(missingErrors.some(error => error.includes('ACCPPDE101')));
  assert.ok(missingErrors.some(error => error.includes('totals 172.5 EC')));

  const duplicate = structuredClone(records[0]);
  const duplicateUcrId = ucrProgrammes(duplicate)[0].id;
  const original = comparisonCells(duplicate, duplicateUcrId)[0].cell;
  duplicate.blocks[0].rows.push({ cells: { [duplicateUcrId]: structuredClone(original) } });
  const duplicateErrors = validateExample(duplicate).errors;
  assert.ok(duplicateErrors.some(error => error.includes('duplicate course')));
  assert.ok(duplicateErrors.some(error => error.includes('totals 187.5 EC')));

  const incompleteComparator = structuredClone(records[0]);
  const comparatorCell = comparisonCells(incompleteComparator, incompleteComparator.programmes[0].id)[0];
  delete comparatorCell.row.cells[incompleteComparator.programmes[0].id];
  assert.ok(validateExample(incompleteComparator).errors.some(error => error.includes('comparison comparator totals')));

  const badReference = structuredClone(records[0]);
  const badRefUcrId = ucrProgrammes(badReference)[0].id;
  comparisonCells(badReference, badRefUcrId)[0].cell.courseCode = 'NOT-A-UCR-COURSE';
  assert.ok(validateExample(badReference).errors.some(error => error.includes('is not in the scheduled programme')));
});

test('UCR alternatives require at least four courses / 30 EC of pairwise distinct content', () => {
  const exactDuplicate = makeNearDuplicate(records[0], 0);
  assert.ok(validateExample(exactDuplicate).errors.some(error => error.includes('24 courses are shared')));

  const oneDifferent = makeNearDuplicate(records[0], 1);
  assert.ok(validateExample(oneDifferent).errors.some(error => error.includes('23 courses are shared')));

  const threeDifferent = makeNearDuplicate(records[0], 3);
  assert.ok(validateExample(threeDifferent).errors.some(error => error.includes('21 courses are shared')));

  const fourDifferent = makeNearDuplicate(records[0], 4);
  assert.ok(
    !validateExample(fourDifferent).errors.some(error => error.includes('are not substantively distinct')),
    '20/24 shared courses is the minimum mechanically acceptable distinctness threshold'
  );
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
