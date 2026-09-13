import fs from 'node:fs';
import path from 'node:path';
import { normalizeCell, readExample, validateExample } from './example-utils.mjs';

const root = process.cwd();
const target = process.argv[2] || 'all';
const dir = path.join(root, 'data', 'counselor', 'comparisons');
const registryFile = path.join(root, 'data', 'registry', 'programmes.csv');
const cpPattern = /^cp-[0-9]{6}$/;
const ucrRoles = ['ucr-depth', 'ucr-balanced', 'ucr-thematic'];

function counselorFiles() {
  if (target !== 'all') {
    const id = target.toLowerCase().replace(/\.json$/i, '');
    if (!cpPattern.test(id)) throw new Error(`Invalid counselor production id: ${target}`);
    const file = path.join(dir, `${id}.json`);
    if (!fs.existsSync(file)) throw new Error(`Counselor comparison not found: ${id}`);
    return [file];
  }
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir).filter(name => /^cp-[0-9]{6}\.json$/.test(name)).sort().map(name => path.join(dir, name));
}

function parseCsv(text) {
  const rows = []; let row = []; let field = ''; let quoted = false;
  for (let i = 0; i < text.length; i += 1) {
    const ch = text[i];
    if (quoted) {
      if (ch === '"') {
        if (text[i + 1] === '"') { field += '"'; i += 1; } else quoted = false;
      } else field += ch;
      continue;
    }
    if (ch === '"') quoted = true;
    else if (ch === ',') { row.push(field); field = ''; }
    else if (ch === '\n') { row.push(field.replace(/\r$/, '')); rows.push(row); row = []; field = ''; }
    else field += ch;
  }
  if (field.length || row.length) { row.push(field.replace(/\r$/, '')); rows.push(row); }
  if (!rows.length) return [];
  const headers = rows[0].map((value, index) => index === 0 ? value.replace(/^\uFEFF/, '') : value);
  return rows.slice(1).filter(values => values.some(value => String(value).trim())).map(values => Object.fromEntries(headers.map((header, index) => [header, values[index] ?? ''])));
}

function parseJsonArray(value, fieldName, errors, sourceName) {
  try { const parsed = JSON.parse(value || '[]'); if (!Array.isArray(parsed)) throw new Error('not an array'); return parsed; }
  catch { errors.push(`${sourceName}: registry field ${fieldName} is not valid JSON array data`); return []; }
}

function comparableArray(values) { return [...values].map(value => typeof value === 'number' ? value : String(value)).sort((a, b) => String(a).localeCompare(String(b), undefined, { numeric: true })); }
function arraysEqual(left, right) { const a = comparableArray(Array.isArray(left) ? left : []); const b = comparableArray(Array.isArray(right) ? right : []); return a.length === b.length && a.every((value, index) => value === b[index]); }
function creditNumber(value) { if (typeof value === 'number' && Number.isFinite(value)) return value; if (typeof value !== 'string') return null; const match = value.replace(',', '.').match(/-?\d+(?:\.\d+)?/); return match ? Number(match[0]) : null; }
function blockCredit(block, programmeId) { let total = 0; let found = false; for (const row of Array.isArray(block?.rows) ? block.rows : []) { const cell = normalizeCell(row?.cells?.[programmeId]); if (!cell) continue; const credits = creditNumber(cell.credits); if (credits === null) return null; total += credits; found = true; } return found ? total : null; }
function programmeByRole(record, role) { return (Array.isArray(record?.programmes) ? record.programmes : []).find(programme => programme?.role === role); }
function scheduledCourseCodes(record, role) { const programme = programmeByRole(record, role); const semesters = Array.isArray(programme?.schedule?.semesters) ? programme.schedule.semesters : []; return semesters.flatMap(semester => Array.isArray(semester?.courses) ? semester.courses : []).map(course => String(course?.code || '').trim()).filter(Boolean); }
function allBlocksHaveUniformPositiveCredits(record, role) { const blocks = Array.isArray(record?.blocks) ? record.blocks : []; if (blocks.length < 3) return false; const totals = blocks.map(block => blockCredit(block, role)); if (totals.some(value => value === null || value <= 0)) return false; return totals.every(value => Math.abs(value - totals[0]) < 0.001); }

function validateEvidence(evidence, label, fail) {
  if (!Array.isArray(evidence) || evidence.length === 0) { fail(`${label} requires at least one evidence reference`); return; }
  evidence.forEach((item, index) => {
    if (!item || typeof item !== 'object' || Array.isArray(item)) { fail(`${label} evidence ${index + 1} must be an object`); return; }
    if (!['official-source', 'programme-interest'].includes(item.sourceType)) fail(`${label} evidence ${index + 1} sourceType must be official-source or programme-interest`);
    if (typeof item.reference !== 'string' || !item.reference.trim()) fail(`${label} evidence ${index + 1} requires a reference`);
  });
}

function validateMapItems(items, fieldName, fail, { allowEmpty = false } = {}) {
  if (!Array.isArray(items) || (!allowEmpty && items.length === 0)) { fail(`academicRationale.${fieldName} must be ${allowEmpty ? 'an array' : 'a non-empty array'}`); return []; }
  const labels = [];
  items.forEach((item, index) => {
    const label = `${fieldName}[${index}]`;
    if (!item || typeof item !== 'object' || Array.isArray(item)) { fail(`academicRationale.${label} must be an object`); return; }
    if (typeof item.label !== 'string' || !item.label.trim()) { fail(`academicRationale.${label}.label is required`); return; }
    labels.push(item.label.trim()); validateEvidence(item.evidence, `academicRationale.${label}`, fail);
  });
  if (new Set(labels).size !== labels.length) fail(`academicRationale.${fieldName} labels must be unique`);
  return labels;
}

function validateCourseAlignment(record, rationale, labelSets, fail) {
  const courseAlignment = rationale?.courseAlignment;
  if (!courseAlignment || typeof courseAlignment !== 'object' || Array.isArray(courseAlignment)) { fail('academicRationale.courseAlignment is required'); return; }
  for (const role of ucrRoles) {
    const entries = courseAlignment[role];
    if (!Array.isArray(entries) || entries.length !== 24) { fail(`academicRationale.courseAlignment.${role} must contain exactly 24 course entries`); continue; }
    const scheduled = scheduledCourseCodes(record, role);
    const alignedCodes = entries.map(entry => String(entry?.courseCode || '').trim()).filter(Boolean);
    if (new Set(alignedCodes).size !== alignedCodes.length) fail(`academicRationale.courseAlignment.${role} courseCode values must be unique`);
    if (!arraysEqual(scheduled, alignedCodes)) fail(`academicRationale.courseAlignment.${role} must cover exactly the 24 courses scheduled for ${role}`);
    const allowedLabels = labelSets[role] || new Set();
    entries.forEach((entry, index) => {
      const prefix = `academicRationale.courseAlignment.${role}[${index}]`;
      if (!entry || typeof entry !== 'object' || Array.isArray(entry)) { fail(`${prefix} must be an object`); return; }
      const code = String(entry.courseCode || '').trim(); const reason = String(entry.reason || '').trim(); const basisType = entry.basisType; const basisLabels = Array.isArray(entry.basisLabels) ? entry.basisLabels : null;
      if (!code) fail(`${prefix}.courseCode is required`); if (!reason) fail(`${prefix}.reason is required`);
      if (!['academic-map', 'ucr-required'].includes(basisType)) fail(`${prefix}.basisType must be academic-map or ucr-required`);
      if (!basisLabels) { fail(`${prefix}.basisLabels must be an array`); return; }
      if (new Set(basisLabels).size !== basisLabels.length) fail(`${prefix}.basisLabels must be unique`);
      if (code === 'ACCPPDE101') {
        if (basisType !== 'ucr-required') fail(`${prefix}: ACCPPDE101 must use basisType ucr-required`);
        if (basisLabels.length !== 0) fail(`${prefix}: ACCPPDE101 must not claim academic-map basis labels`);
      } else {
        if (basisType !== 'academic-map') fail(`${prefix}: only ACCPPDE101 may use basisType ucr-required`);
        if (basisLabels.length === 0) fail(`${prefix}: non-PPD courses require at least one basisLabel`);
        basisLabels.forEach(label => { if (!allowedLabels.has(label)) fail(`${prefix}: basis label ${JSON.stringify(label)} is not permitted for ${role}`); });
      }
    });
  }
}

const registryRows = parseCsv(fs.readFileSync(registryFile, 'utf8'));
const registryById = new Map(registryRows.map(row => [row.counselor_programme_id, row]));
let failed = false;
const files = counselorFiles();
const thematicCourseUse = new Map();
const depthCourseUse = new Map();

if (target === 'all' && files.length === 0) console.log('No normalized counselor production records found. Legacy pre-normalization comparison files are intentionally ignored.');

for (const file of files) {
  const sourceName = path.basename(file); const record = readExample(file); const generic = validateExample(record, sourceName); const errors = [...generic.errors]; const warnings = [...generic.warnings]; const fail = message => errors.push(`${sourceName}: ${message}`); const warn = message => warnings.push(`${sourceName}: ${message}`);
  if (record.schemaVersion !== '1.3') fail('schemaVersion must be "1.3" for current counselor production records');
  if (record.origin !== 'counselor') fail('origin must be "counselor"');
  if (!cpPattern.test(String(record.id || ''))) fail('id must use permanent cp-000001 format');
  const provider = record?.programmeProvider; const counselorProgrammeId = String(provider?.counselorProgrammeId || '');
  if (!cpPattern.test(counselorProgrammeId)) fail('programmeProvider.counselorProgrammeId is required and must use permanent cp-000001 format');
  if (cpPattern.test(String(record.id || '')) && cpPattern.test(counselorProgrammeId) && record.id !== counselorProgrammeId) fail('id must equal programmeProvider.counselorProgrammeId');
  if (record.id !== path.basename(file, '.json')) fail('filename must equal the permanent counselor programme id');

  const registry = registryById.get(record.id);
  if (!registry) fail('id does not exist in data/registry/programmes.csv');
  else if (provider && typeof provider === 'object' && !Array.isArray(provider)) {
    if (registry.production_eligible !== 'true') fail('registry target is not production_eligible=true');
    if (!registry.production_order) fail('registry target has no production_order');
    if (registry.programme_type !== 'standard') fail(`registry programme_type is ${registry.programme_type}; current production requires standard`);
    for (const [field, expected] of [['registryName', registry.canonical_name], ['programmeType', registry.programme_type], ['currentStatus', registry.current_status]]) if (provider[field] !== expected) fail(`programmeProvider.${field} must match registry value ${JSON.stringify(expected)}`);
    if (Number(provider.registryOrder) !== Number(registry.registry_order)) fail('programmeProvider.registryOrder must match registry_order');
    if (Number(provider.productionOrder) !== Number(registry.production_order)) fail('programmeProvider.productionOrder must match production_order');
    if (provider.productionEligible !== true) fail('programmeProvider.productionEligible must be true');
    for (const [recordField, registryField] of [['normalizedInstitutionIds','institution_ids_json'],['languages','languages_json'],['modes','modes_json'],['sourceExcelRows','source_excel_rows_json'],['offeredProgrammeIds','offering_ids_json'],['programmeUnitCodes','programme_unit_codes_json'],['recognizedProgrammeCodes','recognized_programme_codes_json'],['variantOfCodes','variant_of_codes_json']]) {
      const expected = parseJsonArray(registry[registryField], registryField, errors, sourceName); if (!arraysEqual(provider[recordField], expected)) fail(`programmeProvider.${recordField} must match registry ${registryField}`);
    }
    if (Object.hasOwn(provider, 'language') || Object.hasOwn(provider, 'mode')) fail('use normalized programmeProvider.languages and programmeProvider.modes arrays; scalar language/mode fields are not current production metadata');
  }

  const rationale = record?.academicRationale;
  if (!rationale || typeof rationale !== 'object' || Array.isArray(rationale)) fail('academicRationale is required');
  else {
    const coreLabels = validateMapItems(rationale.coreField, 'coreField', fail); const adjacentLabels = validateMapItems(rationale.adjacentDirections, 'adjacentDirections', fail); const questionLabels = validateMapItems(rationale.questionsApplications, 'questionsApplications', fail, { allowEmpty: true });
    if (!Array.isArray(rationale.balancedDirections) || rationale.balancedDirections.length < 1 || rationale.balancedDirections.length > 2) fail('academicRationale.balancedDirections must select one or two adjacent directions');
    else {
      if (new Set(rationale.balancedDirections).size !== rationale.balancedDirections.length) fail('academicRationale.balancedDirections must be unique');
      rationale.balancedDirections.forEach(direction => { if (!adjacentLabels.includes(direction)) fail(`balanced direction ${JSON.stringify(direction)} is not present in academicRationale.adjacentDirections`); });
    }
    const thematic = rationale.thematicQuestion; let thematicBasis = [];
    if (!thematic || typeof thematic !== 'object' || Array.isArray(thematic)) fail('academicRationale.thematicQuestion is required');
    else {
      if (typeof thematic.text !== 'string' || !thematic.text.trim()) fail('academicRationale.thematicQuestion.text is required');
      if (!Array.isArray(thematic.basisLabels) || thematic.basisLabels.length === 0) fail('academicRationale.thematicQuestion.basisLabels must identify at least one map item');
      else { thematicBasis = thematic.basisLabels; const mapLabels = new Set([...coreLabels, ...adjacentLabels, ...questionLabels]); thematic.basisLabels.forEach(label => { if (!mapLabels.has(label)) fail(`thematic basis label ${JSON.stringify(label)} is not present in the academic interest map`); }); }
      validateEvidence(thematic.evidence, 'academicRationale.thematicQuestion', fail);
    }
    validateCourseAlignment(record, rationale, {'ucr-depth':new Set(coreLabels),'ucr-balanced':new Set([...coreLabels,...(Array.isArray(rationale.balancedDirections)?rationale.balancedDirections:[])]),'ucr-thematic':new Set(thematicBasis)}, fail);
  }

  if (Array.isArray(record.blocks) && record.blocks.length >= 3 && ucrRoles.every(role => allBlocksHaveUniformPositiveCredits(record, role))) fail('comparison assigns the same positive UCR credit total to every block for all three UCR programmes; rebuild blocks as analytical alignments rather than a fixed allocation template');
  if (Array.isArray(record.blocks) && record.blocks.length) {
    let rows = 0; let completeRows = 0;
    for (const block of record.blocks) for (const row of Array.isArray(block?.rows) ? block.rows : []) { rows += 1; if (['comparator', ...ucrRoles].every(id => normalizeCell(row?.cells?.[id]))) completeRows += 1; }
    if (rows >= 3 && completeRows === rows) warn('every comparison row is populated for all four programmes; review whether genuine gaps have been suppressed for visual symmetry');
  }
  for (const code of new Set(scheduledCourseCodes(record, 'ucr-thematic'))) if (code !== 'ACCPPDE101') thematicCourseUse.set(code, (thematicCourseUse.get(code) || 0) + 1);
  for (const code of new Set(scheduledCourseCodes(record, 'ucr-depth'))) if (code !== 'ACCPPDE101') depthCourseUse.set(code, (depthCourseUse.get(code) || 0) + 1);
  warnings.forEach(message => console.warn(`WARNING: ${message}`));
  if (errors.length) { failed = true; errors.forEach(message => console.error(`ERROR: ${message}`)); } else console.log(`Valid counselor production record: ${sourceName}`);
}

if (target === 'all' && files.length >= 10) {
  const threshold = Math.ceil(files.length * 0.4);
  for (const [code, thematicCount] of [...thematicCourseUse.entries()].sort((a,b)=>b[1]-a[1])) { const depthCount = depthCourseUse.get(code) || 0; if (thematicCount >= threshold && depthCount * 2 < thematicCount) console.warn(`WARNING: thematic course ${code} appears in ${thematicCount}/${files.length} records but only ${depthCount}/${files.length} depth programmes; review for generic thematic-palette reuse`); }
}

if (failed) process.exit(1);
