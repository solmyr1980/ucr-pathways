import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();

function replaceOnce(file, before, after) {
  const text = fs.readFileSync(file, 'utf8');
  if (!text.includes(before)) throw new Error(`Expected text not found in ${file}`);
  if (text.split(before).length !== 2) throw new Error(`Expected text is not unique in ${file}`);
  fs.writeFileSync(file, text.replace(before, after));
}

// Durable product rule.
const master = path.join(root, 'docs', 'UCR_Pathways_Master_Specification.md');
const masterBefore = 'Within one comparison, **exact UCR course identity is the only basis for sharing a UCR comparison row**. A UCR course code has one canonical row and one canonical block. Every included UCR alternative containing that exact code populates that row; alternatives not containing it remain blank. Different UCR course codes occupy different rows even when their content is closely related. This identity rule does not require symmetry between different courses or between UCR and the external comparator.\n\nDetailed block construction, stable component references and anti-template checks belong to the Production Instructions and executable validators.';
const masterAfter = 'Within one comparison, **exact UCR course identity is the only basis for sharing a UCR comparison row**. A UCR course code has one canonical row and one canonical block. Every included UCR alternative containing that exact code populates that row; alternatives not containing it remain blank. Different UCR course codes occupy different rows even when their content is closely related. This identity rule does not require symmetry between different courses or between UCR and the external comparator.\n\nAfter the canonical UCR rows are fixed, place each external comparator component independently according to **substantive curricular correspondence**. Co-location in a row means that the external component and the UCR course are meaningfully comparable; it must never be inherited merely from an earlier row position. A strong direct subject match takes precedence over a weaker thematic resemblance. Where no sufficiently direct UCR counterpart exists, retain the comparator component on its own row and preserve the gap rather than force a misleading alignment.\n\nDetailed block construction, stable component references and anti-template checks belong to the Production Instructions and executable validators.';
replaceOnce(master, masterBefore, masterAfter);

// Detailed production procedure.
const production = path.join(root, 'docs', 'UCR_Pathways_Production_Instructions.md');
const productionBefore = '- assign the canonical block once for the course code within that comparison; the same course may not appear under different blocks in different UCR alternatives;\n- meaningful blank cells are legitimate when there is no sufficiently comparable component in another programme;';
const productionAfter = '- assign the canonical block once for the course code within that comparison; the same course may not appear under different blocks in different UCR alternatives;\n- **only after the UCR rows are fixed**, place every comparator component independently against the strongest defensible UCR counterpart, using actual component/course content rather than previous row position;\n- a shared comparator/UCR row asserts substantive correspondence. Prefer a direct same-subject match over a looser thematic association (for example, Developmental Psychology belongs with Lifespan Developmental Psychology rather than with an unrelated social-science course);\n- when no sufficiently direct UCR counterpart exists, give the comparator component its own row with blank UCR cells. Never preserve or invent a weak match merely to reduce blank space;\n- record the decision for every comparator component in `comparisonAlignment`: either `substantive-match` with the selected `ucrCourseCode`, or `unmatched`, together with a concise rationale. If the UCR row structure changes, comparator placement must be recomputed rather than carried over by row index;\n- meaningful blank cells are legitimate when there is no sufficiently comparable component in another programme;';
replaceOnce(production, productionBefore, productionAfter);

// Extend the counselor schema with explicit semantic-alignment audit data.
const schemaPath = path.join(root, 'data', 'schema', 'counselor-comparison.schema.json');
const schema = JSON.parse(fs.readFileSync(schemaPath, 'utf8'));
const contract = schema.allOf[1];
if (!contract.required.includes('comparisonAlignment')) contract.required.push('comparisonAlignment');
contract.properties.comparisonAlignment = { '$ref': '#/$defs/comparisonAlignment' };
schema.$defs.comparisonAlignmentEntry = {
  type: 'object',
  required: ['componentId', 'matchType', 'rationale'],
  properties: {
    componentId: { type: 'string', minLength: 1 },
    matchType: { type: 'string', enum: ['substantive-match', 'unmatched'] },
    ucrCourseCode: { type: 'string', minLength: 1 },
    rationale: { type: 'string', minLength: 1 }
  },
  additionalProperties: false
};
schema.$defs.comparisonAlignment = {
  type: 'array',
  minItems: 1,
  uniqueItems: true,
  items: { '$ref': '#/$defs/comparisonAlignmentEntry' }
};
fs.writeFileSync(schemaPath, JSON.stringify(schema, null, 2) + '\n');

// Strengthen structural validator: declared semantic decision must equal actual row placement.
const validatorPath = path.join(root, 'scripts', 'validate-counselor-structural-rules.mjs');
const validatorMarker = '  // Final labels describe the completed curriculum; the generating concept is preserved separately.\n';
const validatorInsert = `  // Comparator placement is a separately audited semantic decision made after canonical UCR rows are fixed.\n  const scheduledUcrCodes = new Set();\n  for (const programme of ucrProgrammes) {\n    for (const semester of programme?.schedule?.semesters || []) {\n      for (const course of semester?.courses || []) scheduledUcrCodes.add(String(course.code || '').trim());\n    }\n  }\n\n  const comparatorComponents = new Map((record?.comparator?.components || []).map(component => [component.id, component]));\n  const comparatorLocation = new Map();\n  for (const [blockIndex, block] of (record.blocks || []).entries()) {\n    for (const [rowIndex, row] of (block.rows || []).entries()) {\n      const comparatorCell = normalizeCell(row?.cells?.comparator);\n      if (!comparatorCell) continue;\n      const componentId = String(comparatorCell.componentId || '').trim();\n      if (!componentId) continue;\n      if (comparatorLocation.has(componentId)) {\n        fail(\`comparator component \${componentId} appears in more than one comparison row\`);\n        continue;\n      }\n      const rowCodes = new Set();\n      for (const programme of ucrProgrammes) {\n        const cell = normalizeCell(row?.cells?.[programme.id]);\n        if (cell?.courseCode) rowCodes.add(String(cell.courseCode).trim());\n      }\n      if (rowCodes.size > 1) fail(\`comparator component \${componentId} shares a row with multiple UCR course codes\`);\n      comparatorLocation.set(componentId, {\n        location: \`\${blockIndex}:\${rowIndex}\`,\n        ucrCourseCode: rowCodes.size === 1 ? [...rowCodes][0] : null\n      });\n    }\n  }\n\n  for (const componentId of comparatorComponents.keys()) {\n    if (!comparatorLocation.has(componentId)) fail(\`comparator component \${componentId} is missing from the comparison\`);\n  }\n  for (const componentId of comparatorLocation.keys()) {\n    if (!comparatorComponents.has(componentId)) fail(\`comparison references unknown comparator component \${componentId}\`);\n  }\n\n  const alignment = Array.isArray(record.comparisonAlignment) ? record.comparisonAlignment : [];\n  const alignmentByComponent = new Map();\n  for (const [index, item] of alignment.entries()) {\n    const label = \`comparisonAlignment[\${index}]\`;\n    const componentId = String(item?.componentId || '').trim();\n    if (!componentId) { fail(\`\${label}.componentId is required\`); continue; }\n    if (alignmentByComponent.has(componentId)) fail(\`comparisonAlignment duplicates comparator component \${componentId}\`);\n    alignmentByComponent.set(componentId, item);\n    if (!comparatorComponents.has(componentId)) fail(\`\${label} references unknown comparator component \${componentId}\`);\n    if (typeof item?.rationale !== 'string' || !item.rationale.trim()) fail(\`\${label}.rationale is required\`);\n    if (!['substantive-match', 'unmatched'].includes(item?.matchType)) fail(\`\${label}.matchType is invalid\`);\n    const actual = comparatorLocation.get(componentId);\n    if (!actual) continue;\n    if (item.matchType === 'substantive-match') {\n      const code = String(item?.ucrCourseCode || '').trim();\n      if (!code) fail(\`\${label}.ucrCourseCode is required for substantive-match\`);\n      else if (!scheduledUcrCodes.has(code)) fail(\`\${label}.ucrCourseCode \${code} is not scheduled in any UCR alternative\`);\n      if (actual.ucrCourseCode !== code) fail(\`\${componentId} declares semantic match to \${code} but is actually placed with \${actual.ucrCourseCode || 'no UCR course'}\`);\n    } else {\n      if (item.ucrCourseCode) fail(\`\${label} is unmatched and must not carry ucrCourseCode\`);\n      if (actual.ucrCourseCode) fail(\`\${componentId} is declared unmatched but shares a row with \${actual.ucrCourseCode}\`);\n    }\n  }\n  for (const componentId of comparatorComponents.keys()) {\n    if (!alignmentByComponent.has(componentId)) fail(\`comparisonAlignment must assess comparator component \${componentId}\`);\n  }\n\n`;
const validatorText = fs.readFileSync(validatorPath, 'utf8');
if (!validatorText.includes(validatorMarker)) throw new Error('Validator insertion marker not found');
fs.writeFileSync(validatorPath, validatorText.replace(validatorMarker, validatorInsert + validatorMarker));

const mappings = {
  'cp-000001': {
    'pa-introduction': null,
    'pa-sociology-1': 'GOSSOCI111',
    'pa-administrative-law': 'GOSLAWJ213',
    'pa-organisation-management': 'BENLEAD311',
    'pa-designing-social-research': 'BENGATE102',
    'pa-political-science': 'GOSPOLI112',
    'pa-economics-welfare-distribution': 'BENECON111',
    'pa-public-policy': null,
    'pa-skills': null,
    'pa-network-governance': null,
    'pa-qualitative-methods': 'GOSSOCI212',
    'pa-policy-analysis': null,
    'pa-quantitative-methods': 'BENECON312',
    'pa-internship': null,
    'pa-public-resources': 'BENECON311',
    'pa-research-project': null,
    'pa-minor': null,
    'pa-european-international-governance': 'GOSPOLI311',
    'pa-political-philosophy-democracy': 'GOSPOLI111',
    'pa-institutions-policy-society': 'GOSGATE102',
    'pa-people-management': 'BENLEAD211',
    'pa-bachelor-project': null
  },
  'cp-000002': {
    'misoc-global-challenges': null,
    'misoc-sociology-1': 'GOSSOCI111',
    'misoc-international-law': 'GOSLAWJ212',
    'misoc-organisation-management': 'BENLEAD311',
    'misoc-designing-social-research': 'BENGATE102',
    'misoc-political-science': 'GOSPOLI112',
    'misoc-economics-welfare-distribution': 'BENECON111',
    'misoc-public-policy': null,
    'misoc-skills': null,
    'misoc-network-governance': null,
    'misoc-qualitative-methods': 'GOSSOCI212',
    'misoc-policy-analysis': null,
    'misoc-quantitative-methods': 'BENECON312',
    'misoc-global-development': null,
    'misoc-international-migration': null,
    'misoc-public-resources': 'BENECON311',
    'misoc-research-project': null,
    'misoc-minor': null,
    'misoc-global-european-governance': 'GOSPOLI311',
    'misoc-political-philosophy-democracy': 'GOSPOLI111',
    'misoc-institutions-policy-society': 'GOSGATE102',
    'misoc-people-management': 'BENLEAD211',
    'misoc-bachelor-project': null
  },
  'cp-000003': {
    'ped-intro': null,
    'ped-socialisation-inequality': 'GOSSOCI214',
    'ped-methods-1': 'BENGATE102',
    'ped-development-personality': 'HCBPSYC314',
    'ped-complex-practice': null,
    'ped-biological-foundations': 'HCBCOGN112',
    'ped-methods-2': 'HCBPSYC211',
    'ped-parenting-issues': null,
    'ped-qualitative-learning': 'GOSSOCI212',
    'ped-education-design': null,
    'ped-quantitative-learning': null,
    'ped-orthopedagogy': 'HCBPSYC312',
    'ped-psychometrics': null,
    'ped-minor': null,
    'ped-methods-3': null,
    'ped-bachelor-project': null,
    'ped-specialisation-support': null
  },
  'cp-000004': {
    'psy-social': 'HCBPSYC111',
    'psy-personality': null,
    'psy-biological': 'HCBGATE102',
    'psy-methods1': 'BENGATE102',
    'psy-developmental': 'HCBPSYC314',
    'psy-clinical1': 'HCBPSYC212',
    'psy-history-methods': null,
    'psy-cross-cultural': null,
    'psy-thrive1': 'ACCPPDE101',
    'psy-psychodiag1': 'HCBPSYC312',
    'psy-communication1': 'MCCCOMM311',
    'psy-writing1': null,
    'psy-cognitive': 'HCBCOGN311',
    'psy-methods2': 'HCBPSYC211',
    'psy-ethics': 'GOSPHIL212',
    'psy-thrive2': null,
    'psy-educational': null,
    'psy-work': 'BENLEAD311',
    'psy-science-practical': 'HCBPSYC313',
    'psy-mental2': 'HCBPSYC311',
    'psy-psychometrics': null,
    'psy-communication2': 'BENLEAD112',
    'psy-writing2': null,
    'psy-psychodiag2': null,
    'psy-clinical-specialisation-y2': null,
    'psy-minor': null,
    'psy-elective': null,
    'psy-methods3': null,
    'psy-thrive3': null,
    'psy-thesis': null,
    'psy-clinical-interview': null,
    'psy-neuropsych': 'HCBCOGN112',
    'psy-neuropsych-assessment': null
  }
};

function nonEmptyCell(cell) {
  return cell && typeof cell === 'object' && !Array.isArray(cell) && Object.keys(cell).length > 0;
}

const comparisonsDir = path.join(root, 'data', 'counselor', 'comparisons');
for (const [id, decisionMap] of Object.entries(mappings)) {
  const file = path.join(comparisonsDir, `${id}.json`);
  const record = JSON.parse(fs.readFileSync(file, 'utf8'));
  const ucrProgrammes = (record.programmes || []).filter(p => p.family === 'ucr');
  const ucrNames = new Map();
  for (const p of ucrProgrammes) for (const sem of p.schedule?.semesters || []) for (const c of sem.courses || []) ucrNames.set(c.code, c.name);

  const componentIds = (record.comparator?.components || []).map(c => c.id);
  if (componentIds.length !== Object.keys(decisionMap).length || componentIds.some(id2 => !(id2 in decisionMap))) {
    throw new Error(`${id}: mapping does not cover comparator components exactly`);
  }
  const matchedCodes = Object.values(decisionMap).filter(Boolean);
  if (new Set(matchedCodes).size !== matchedCodes.length) throw new Error(`${id}: two comparator components target the same UCR row`);
  for (const code of matchedCodes) if (!ucrNames.has(code)) throw new Error(`${id}: mapping references missing UCR course ${code}`);

  const comparatorCells = new Map();
  const originalBlockByComponent = new Map();
  for (const block of record.blocks || []) {
    for (const row of block.rows || []) {
      const cell = row?.cells?.comparator;
      if (!nonEmptyCell(cell)) continue;
      if (comparatorCells.has(cell.componentId)) throw new Error(`${id}: duplicate comparator component ${cell.componentId}`);
      comparatorCells.set(cell.componentId, { ...cell });
      originalBlockByComponent.set(cell.componentId, block.id);
    }
  }
  for (const componentId of componentIds) if (!comparatorCells.has(componentId)) throw new Error(`${id}: missing comparator cell ${componentId}`);

  // Strip all comparator cells and remove rows that become entirely empty.
  for (const block of record.blocks || []) {
    for (const row of block.rows || []) delete row.cells.comparator;
    block.rows = (block.rows || []).filter(row => Object.values(row.cells || {}).some(nonEmptyCell));
  }

  const rowByUcrCode = new Map();
  for (const block of record.blocks || []) {
    for (const row of block.rows || []) {
      const codes = new Set();
      for (const p of ucrProgrammes) {
        const cell = row?.cells?.[p.id];
        if (nonEmptyCell(cell) && cell.courseCode) codes.add(cell.courseCode);
      }
      if (codes.size > 1) throw new Error(`${id}: UCR row contains multiple codes after previous migration`);
      if (codes.size === 1) rowByUcrCode.set([...codes][0], row);
    }
  }

  const blockById = new Map((record.blocks || []).map(block => [block.id, block]));
  record.comparisonAlignment = [];
  for (const component of record.comparator.components) {
    const code = decisionMap[component.id];
    const cell = comparatorCells.get(component.id);
    if (code) {
      const row = rowByUcrCode.get(code);
      if (!row) throw new Error(`${id}: canonical UCR row not found for ${code}`);
      if (nonEmptyCell(row.cells.comparator)) throw new Error(`${id}: UCR row ${code} already has comparator component`);
      row.cells.comparator = cell;
      record.comparisonAlignment.push({
        componentId: component.id,
        matchType: 'substantive-match',
        ucrCourseCode: code,
        rationale: `${component.name} is most directly comparable to UCR ${ucrNames.get(code)}; this row was selected by semantic review after fixing the canonical UCR rows.`
      });
    } else {
      const blockId = originalBlockByComponent.get(component.id);
      const block = blockById.get(blockId) || record.blocks[0];
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

console.log('Rebuilt comparator semantic alignment for cp-000001 through cp-000004.');
