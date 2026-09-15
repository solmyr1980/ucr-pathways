import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const base = path.join(root, 'data', 'counselor', 'comparisons');

const changes = [
  {
    file: 'cp-000001.json', componentId: 'pa-skills', courseCode: 'ACCPPDE101',
    rationale: 'Bestuurskunde Vaardigheden develops academic and professional skills, including scientific reading, literature-study writing and research presentation. UCR Personal & Professional Development likewise develops core academic and professional skills through source analysis, academic writing, presentation, reflection and independent learning; the educational function substantially corresponds.'
  },
  {
    file: 'cp-000001.json', componentId: 'pa-network-governance', courseCode: 'ENSDELT312',
    rationale: 'Network Governance and UCR Governance of Sustainability both center governance as multi-actor collective decision-making involving public and non-public actors around public problems. UCR applies the governance framework to sustainability, but the primary governance content substantially corresponds.'
  },
  {
    file: 'cp-000002.json', componentId: 'misoc-organisation-management', courseCode: 'BENLEAD311',
    rationale: 'Organisation & Management and UCR Psychology of Organizations & Leadership both address the functioning and management of organisations. Their framing differs, but the substantive organisational domain is sufficiently shared for row alignment.'
  },
  {
    file: 'cp-000002.json', componentId: 'misoc-skills', courseCode: 'ACCPPDE101',
    rationale: 'MISOC Skills serves academic and professional skill development, while UCR Personal & Professional Development develops core academic, communication, reflection and independent-learning skills. Their educational function substantially corresponds despite different programme framing.'
  },
  {
    file: 'cp-000002.json', componentId: 'misoc-network-governance', courseCode: 'ENSDELT312',
    rationale: 'Network Governance and UCR Governance of Sustainability both center governance as multi-actor collective decision-making involving public and non-public actors around public problems. UCR applies the governance framework to sustainability, but the primary governance content substantially corresponds.'
  },
  {
    file: 'cp-000002.json', componentId: 'misoc-research-project', courseCode: 'ENSSUST313',
    rationale: 'Both are dedicated project-based research courses. UCR Research in a Sustainable Delta has students conduct an externally grounded research project in teams; the sustainability theme changes the application domain, not the central research-project educational function.'
  },
  {
    file: 'cp-000003.json', componentId: 'ped-orthopedagogy', courseCode: 'HCBPSYC212',
    rationale: 'Verdieping in Orthopedagogiek studies developmental, internalising, externalising and learning problems with a diagnostic and clinical-cycle focus; UCR Abnormal Psychology studies psychopathology across the lifespan together with assessment, diagnosis, classification and treatment. The disciplinary framing differs, but the problem domain and diagnostic focus substantially correspond.'
  },
  {
    file: 'cp-000003.json', componentId: 'ped-specialisation-support', courseCode: 'HCBPSYC312',
    rationale: 'Pedagogische Ondersteuning spans escalating support and intervention together with an action-oriented diagnostic cycle across youth and family contexts; UCR Psychodiagnostics & Psychotherapies covers assessment, diagnostics and psychological intervention across ages. The pedagogical versus clinical framing differs, but the assessment-and-intervention content substantially corresponds.'
  },
  {
    file: 'cp-000004.json', componentId: 'psy-neuropsych', courseCode: 'HCBCOGN112',
    rationale: 'Neuropsychology concerns brain-behaviour and cognitive consequences of neurological functioning and disorder, while UCR Neurobiology covers brain biology, anatomy, behaviour and disorders. The clinical-cognitive versus biological emphasis differs, but the primary brain-behaviour and neuroscience domain substantially corresponds.'
  }
];

function moveComparator(record, componentId, courseCode, rationale) {
  const component = (record.comparator?.components || []).find(c => c.id === componentId);
  if (!component) throw new Error(`${record.id}: missing comparator component ${componentId}`);

  let sourceBlock = null;
  let sourceRow = null;
  let targetBlock = null;
  let targetRow = null;

  for (const block of record.blocks || []) {
    for (const row of block.rows || []) {
      if (row?.cells?.comparator?.componentId === componentId) {
        sourceBlock = block;
        sourceRow = row;
      }
      for (const [key, cell] of Object.entries(row?.cells || {})) {
        if (key !== 'comparator' && cell?.courseCode === courseCode) {
          if (targetRow && targetRow !== row) throw new Error(`${record.id}: UCR course ${courseCode} occurs in multiple rows`);
          targetBlock = block;
          targetRow = row;
        }
      }
    }
  }

  if (!sourceRow) throw new Error(`${record.id}: source comparator row missing for ${componentId}`);
  if (!targetRow) throw new Error(`${record.id}: target UCR row missing for ${courseCode}`);
  if (sourceRow === targetRow) throw new Error(`${record.id}: ${componentId} is already on ${courseCode}`);
  if (targetRow.cells?.comparator) throw new Error(`${record.id}: target row ${courseCode} already has comparator ${targetRow.cells.comparator.componentId}`);

  delete sourceRow.cells.comparator;
  targetRow.cells.comparator = {
    text: component.name,
    credits: component.credits,
    componentId: component.id,
    ...(component.note ? { note: component.note } : {})
  };

  if (Object.keys(sourceRow.cells).length === 0) {
    sourceBlock.rows = sourceBlock.rows.filter(r => r !== sourceRow);
  }
  if (sourceBlock.rows.length === 0) {
    record.blocks = record.blocks.filter(b => b !== sourceBlock);
  }

  const alignment = (record.comparisonAlignment || []).find(a => a.componentId === componentId);
  if (!alignment) throw new Error(`${record.id}: missing comparisonAlignment for ${componentId}`);
  alignment.matchType = 'substantive-match';
  alignment.ucrCourseCode = courseCode;
  alignment.rationale = rationale;
}

const grouped = new Map();
for (const c of changes) {
  if (!grouped.has(c.file)) grouped.set(c.file, []);
  grouped.get(c.file).push(c);
}

for (const [file, fileChanges] of grouped) {
  const filePath = path.join(base, file);
  const record = JSON.parse(fs.readFileSync(filePath, 'utf8'));
  for (const c of fileChanges) moveComparator(record, c.componentId, c.courseCode, c.rationale);

  for (const a of record.comparisonAlignment || []) {
    if (a.matchType === 'unmatched' && a.rationale === 'No single UCR course provides a sufficiently direct counterpart; this comparator component is intentionally retained on its own row rather than forced into a weak match.') {
      a.rationale = 'Re-audited under the substantial-curricular-correspondence rule. No available UCR row provides a sufficiently substantial counterpart without overstating partial or adjacent overlap.';
    }
  }

  fs.writeFileSync(filePath, JSON.stringify(record, null, 2) + '\n');
}

console.log(`Applied ${changes.length} comparator row re-audit alignments.`);
