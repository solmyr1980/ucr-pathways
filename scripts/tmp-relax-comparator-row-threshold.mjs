import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const docsPath = path.join(root, 'docs', 'UCR_Pathways_Production_Instructions.md');

const oldText = `- a shared comparator/UCR row asserts substantive correspondence. Prefer a direct same-subject match over a looser thematic association (for example, Developmental Psychology belongs with Lifespan Developmental Psychology rather than with an unrelated social-science course);\n- when no sufficiently direct UCR counterpart exists, give the comparator component its own row with blank UCR cells. Never preserve or invent a weak match merely to reduce blank space;`;

const newText = `- a shared comparator/UCR row asserts **substantial curricular correspondence**, not full course equivalence. Place components on the same row when they address materially the same primary academic subject, method or educational function, even when their disciplinary framing, breadth or emphasis differs;\n- prefer the strongest defensible counterpart and use actual component/course content rather than title similarity alone. A direct same-subject match remains preferable to a looser thematic association (for example, Developmental Psychology belongs with Lifespan Developmental Psychology rather than with an unrelated social-science course);\n- keep components on separate rows when the overlap is only partial, adjacent, incidental or merely methodological rather than substantively the same area. When no substantial curricular counterpart exists, give the comparator component its own row with blank UCR cells. Never preserve or invent a weak match merely to reduce blank space;`;

let docs = fs.readFileSync(docsPath, 'utf8');
if (!docs.includes(oldText)) throw new Error('Expected production-instruction threshold text not found');
docs = docs.replace(oldText, newText);
fs.writeFileSync(docsPath, docs);

const changes = [
  {
    file: 'cp-000001.json',
    componentId: 'pa-administrative-law',
    courseCode: 'GOSLAWJ213',
    rationale: 'Staats- en Bestuursrecht and UCR Comparative Constitutional Law have substantial curricular correspondence in public/constitutional legal structures, including administrative-law territory; the overlap is sufficient for shared-row comparison even though the courses are not equivalent.'
  },
  {
    file: 'cp-000001.json',
    componentId: 'pa-organisation-management',
    courseCode: 'BENLEAD311',
    rationale: 'Organisation & Management and UCR Psychology of Organizations & Leadership both address the functioning and management of organisations. Their framing differs, but the substantive organisational domain is sufficiently shared for row alignment.'
  },
  {
    file: 'cp-000002.json',
    componentId: 'misoc-people-management',
    courseCode: 'BENLEAD211',
    rationale: 'People Management in Complex Organisations and UCR Leadership & Diversity Management substantially overlap in leading and managing people in complex organisational settings, so they belong on the same comparison row despite different emphasis.'
  }
];

function moveComparator(record, componentId, courseCode, rationale) {
  const component = (record.comparator?.components || []).find(c => c.id === componentId);
  if (!component) throw new Error(`${record.id}: missing comparator component ${componentId}`);

  let sourceBlock = null;
  let sourceRow = null;
  let targetRow = null;
  let targetBlock = null;

  for (const block of record.blocks || []) {
    for (const row of block.rows || []) {
      if (row?.cells?.comparator?.componentId === componentId) {
        sourceBlock = block;
        sourceRow = row;
      }
      const ucrCells = Object.entries(row?.cells || {}).filter(([key]) => key !== 'comparator');
      if (ucrCells.some(([, cell]) => cell?.courseCode === courseCode)) {
        if (targetRow && targetRow !== row) throw new Error(`${record.id}: course ${courseCode} appears in multiple rows`);
        targetRow = row;
        targetBlock = block;
      }
    }
  }

  if (!sourceRow) throw new Error(`${record.id}: comparator component ${componentId} is not displayed`);
  if (!targetRow) throw new Error(`${record.id}: target UCR course ${courseCode} is not displayed`);
  if (targetRow.cells.comparator && targetRow.cells.comparator.componentId !== componentId) {
    throw new Error(`${record.id}: target row ${courseCode} already has comparator ${targetRow.cells.comparator.componentId}`);
  }

  delete sourceRow.cells.comparator;
  targetRow.cells.comparator = {
    text: component.name,
    credits: component.credits,
    componentId: component.id,
    ...(component.note ? { note: component.note } : {})
  };

  if (Object.keys(sourceRow.cells).length === 0) {
    sourceBlock.rows = sourceBlock.rows.filter(row => row !== sourceRow);
  }
  if (sourceBlock.rows.length === 0) {
    record.blocks = record.blocks.filter(block => block !== sourceBlock);
  }

  const alignment = (record.comparisonAlignment || []).find(item => item.componentId === componentId);
  if (!alignment) throw new Error(`${record.id}: missing comparisonAlignment for ${componentId}`);
  alignment.matchType = 'substantive-match';
  alignment.ucrCourseCode = courseCode;
  alignment.rationale = rationale;
}

for (const change of changes) {
  const filePath = path.join(root, 'data', 'counselor', 'comparisons', change.file);
  const record = JSON.parse(fs.readFileSync(filePath, 'utf8'));
  moveComparator(record, change.componentId, change.courseCode, change.rationale);
  fs.writeFileSync(filePath, JSON.stringify(record, null, 2) + '\n');
}

// Explicitly preserve the agreed separate-row judgment for Pedagogical Sciences psychometrics.
const pedPath = path.join(root, 'data', 'counselor', 'comparisons', 'cp-000003.json');
const ped = JSON.parse(fs.readFileSync(pedPath, 'utf8'));
const psychometrics = (ped.comparisonAlignment || []).find(item => item.componentId === 'ped-psychometrics');
if (!psychometrics || psychometrics.matchType !== 'unmatched') throw new Error('Psychometrics must remain unmatched');
psychometrics.rationale = 'Psychometrie overlaps with statistics and measurement, but UCR Statistics & Experimental Methods is broader methodological training rather than a substantial counterpart in psychometric measurement. Keep these on separate rows.';
fs.writeFileSync(pedPath, JSON.stringify(ped, null, 2) + '\n');

console.log('Comparator row threshold and agreed alignments updated.');
