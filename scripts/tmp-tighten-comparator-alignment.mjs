import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const corrections = {
  'cp-000001': ['pa-administrative-law', 'pa-organisation-management', 'pa-institutions-policy-society'],
  'cp-000002': ['misoc-organisation-management', 'misoc-institutions-policy-society', 'misoc-people-management'],
  'cp-000003': ['ped-orthopedagogy'],
  'cp-000004': ['psy-communication1', 'psy-communication2', 'psy-mental2', 'psy-neuropsych']
};

function nonEmptyCell(cell) {
  return cell && typeof cell === 'object' && !Array.isArray(cell) && Object.keys(cell).length > 0;
}

for (const [id, toUnmatch] of Object.entries(corrections)) {
  const file = path.join(root, 'data', 'counselor', 'comparisons', `${id}.json`);
  const record = JSON.parse(fs.readFileSync(file, 'utf8'));
  const ucrProgrammes = (record.programmes || []).filter(p => p.family === 'ucr');
  const ucrNames = new Map();
  for (const p of ucrProgrammes) for (const sem of p.schedule?.semesters || []) for (const c of sem.courses || []) ucrNames.set(c.code, c.name);

  const decisions = new Map((record.comparisonAlignment || []).map(item => [item.componentId, item.matchType === 'substantive-match' ? item.ucrCourseCode : null]));
  for (const componentId of toUnmatch) {
    if (!decisions.has(componentId)) throw new Error(`${id}: missing alignment ${componentId}`);
    decisions.set(componentId, null);
  }

  const comparatorCells = new Map();
  const originalBlockByComponent = new Map();
  for (const block of record.blocks || []) {
    for (const row of block.rows || []) {
      const cell = row?.cells?.comparator;
      if (!nonEmptyCell(cell)) continue;
      comparatorCells.set(cell.componentId, { ...cell });
      originalBlockByComponent.set(cell.componentId, block.id);
    }
  }

  for (const block of record.blocks || []) {
    for (const row of block.rows || []) delete row.cells.comparator;
    block.rows = (block.rows || []).filter(row => Object.values(row.cells || {}).some(nonEmptyCell));
  }

  const rowByUcrCode = new Map();
  for (const block of record.blocks || []) for (const row of block.rows || []) {
    const codes = new Set();
    for (const p of ucrProgrammes) {
      const cell = row?.cells?.[p.id];
      if (nonEmptyCell(cell) && cell.courseCode) codes.add(cell.courseCode);
    }
    if (codes.size === 1) rowByUcrCode.set([...codes][0], row);
  }
  const blockById = new Map((record.blocks || []).map(block => [block.id, block]));

  record.comparisonAlignment = [];
  for (const component of record.comparator.components || []) {
    const code = decisions.get(component.id) || null;
    const cell = comparatorCells.get(component.id);
    if (!cell) throw new Error(`${id}: missing comparator cell ${component.id}`);
    if (code) {
      const row = rowByUcrCode.get(code);
      if (!row) throw new Error(`${id}: missing UCR row ${code}`);
      if (nonEmptyCell(row.cells.comparator)) throw new Error(`${id}: collision on UCR row ${code}`);
      row.cells.comparator = cell;
      record.comparisonAlignment.push({
        componentId: component.id,
        matchType: 'substantive-match',
        ucrCourseCode: code,
        rationale: `${component.name} is most directly comparable to UCR ${ucrNames.get(code)}; this row was selected by semantic review after fixing the canonical UCR rows.`
      });
    } else {
      const block = blockById.get(originalBlockByComponent.get(component.id)) || record.blocks[0];
      block.rows.push({ cells: { comparator: cell } });
      record.comparisonAlignment.push({
        componentId: component.id,
        matchType: 'unmatched',
        rationale: 'No single UCR course provides a sufficiently direct counterpart; this comparator component is intentionally retained on its own row rather than forced into a weak match.'
      });
    }
  }
  record.blocks = (record.blocks || []).filter(block => (block.rows || []).length > 0);
  fs.writeFileSync(file, JSON.stringify(record, null, 2) + '\n');
}

console.log('Tightened weak comparator-to-UCR alignments.');
