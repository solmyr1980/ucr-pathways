import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const counselorDir = path.join(root, 'data', 'counselor');
const comparisonDir = path.join(counselorDir, 'comparisons');
const registryDir = path.join(root, 'data', 'registry');
const programmeFile = path.join(registryDir, 'programmes.csv');
const interestFile = path.join(registryDir, 'programme_interests.csv');
const reviewProgrammeFile = path.join(counselorDir, 'review-programmes.json');
const reviewInterestFile = path.join(counselorDir, 'review-interests.json');
const checkOnly = process.argv.includes('--check');

function parseCsv(text) {
  const rows = [];
  let row = [];
  let field = '';
  let quoted = false;

  for (let i = 0; i < text.length; i += 1) {
    const ch = text[i];
    if (quoted) {
      if (ch === '"') {
        if (text[i + 1] === '"') {
          field += '"';
          i += 1;
        } else {
          quoted = false;
        }
      } else field += ch;
      continue;
    }

    if (ch === '"') quoted = true;
    else if (ch === ',') {
      row.push(field);
      field = '';
    } else if (ch === '\n') {
      row.push(field.replace(/\r$/, ''));
      rows.push(row);
      row = [];
      field = '';
    } else field += ch;
  }

  if (quoted) throw new Error('CSV ends inside a quoted field');
  if (field.length || row.length) {
    row.push(field.replace(/\r$/, ''));
    rows.push(row);
  }
  if (!rows.length) return [];

  const headers = rows[0].map((value, index) => index === 0 ? value.replace(/^\uFEFF/, '') : value);
  return rows.slice(1)
    .filter(values => values.some(value => String(value).trim()))
    .map((values, rowIndex) => {
      if (values.length !== headers.length) {
        throw new Error(`CSV row ${rowIndex + 2} has ${values.length} fields; expected ${headers.length}`);
      }
      return Object.fromEntries(headers.map((header, index) => [header, values[index] ?? '']));
    });
}

function jsonCell(value, fallback = []) {
  if (!String(value || '').trim()) return fallback;
  return JSON.parse(value);
}

function readJson(file) {
  return JSON.parse(fs.readFileSync(file, 'utf8'));
}

function stableJson(value) {
  return `${JSON.stringify(value, null, 2)}\n`;
}

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

for (const required of [comparisonDir, programmeFile, interestFile]) {
  assert(fs.existsSync(required), `Missing required input: ${path.relative(root, required)}`);
}

const registry = parseCsv(fs.readFileSync(programmeFile, 'utf8'));
const registryById = new Map(registry.map(row => [row.counselor_programme_id, row]));
const comparisonFiles = fs.readdirSync(comparisonDir)
  .filter(name => /^cp-\d{6}\.json$/.test(name))
  .sort();

assert(comparisonFiles.length > 0, 'No completed normalized counselor comparison records found.');

const completed = comparisonFiles.map(name => {
  const record = readJson(path.join(comparisonDir, name));
  const id = record.id;
  const registryRow = registryById.get(id);
  assert(registryRow, `${name}: ${id} is not present in data/registry/programmes.csv`);
  assert(registryRow.production_eligible === 'true', `${id}: registry target is not production eligible`);
  assert(registryRow.programme_type === 'standard', `${id}: registry target is outside current counselor production scope`);
  assert(String(registryRow.production_order || '').trim(), `${id}: registry target has no production_order`);
  assert(String(registryRow.display_name_en || '').trim(), `${id}: registry target has no display_name_en`);
  assert(record.programmeProvider?.counselorProgrammeId === id, `${id}: comparison/provider identity mismatch`);

  return { record, registryRow };
}).sort((a, b) => Number(a.registryRow.production_order) - Number(b.registryRow.production_order));

const selectedIds = new Set(completed.map(({ record }) => record.id));
const productionOrder = new Map(completed.map(({ record, registryRow }) => [record.id, Number(registryRow.production_order)]));

const programmes = completed.map(({ record, registryRow }) => {
  const provider = record.programmeProvider || {};
  const comparator = record.comparator || {};
  const languages = jsonCell(registryRow.languages_json, provider.languages || []);
  const unitCodes = jsonCell(registryRow.programme_unit_codes_json, provider.programmeUnitCodes || []);
  const recognizedCodes = jsonCell(registryRow.recognized_programme_codes_json, provider.recognizedProgrammeCodes || []);
  const sourceRows = jsonCell(registryRow.source_excel_rows_json, provider.sourceExcelRows || []);

  return {
    comparisonId: record.id,
    sourceExcelRow: sourceRows[0] ?? null,
    programmeProviderId: record.id,
    opleidingseenheidcode: unitCodes[0] ?? null,
    recognizedProgrammeId: recognizedCodes[0] ?? null,
    registryName: registryRow.canonical_name,
    displayName: registryRow.display_name_en,
    institution: comparator.institution || '',
    degree: 'BACHELOR',
    language: languages.length === 1 ? languages[0] : languages.join(' / '),
    studyLoad: String(registryRow.study_load_ec || 180),
    officialUrl: comparator.primarySourceUrl || jsonCell(registryRow.registry_urls_json, [])[0] || ''
  };
});

const interestRows = parseCsv(fs.readFileSync(interestFile, 'utf8'))
  .filter(row => selectedIds.has(row.counselor_programme_id))
  .sort((a, b) => {
    const orderDifference = productionOrder.get(a.counselor_programme_id) - productionOrder.get(b.counselor_programme_id);
    if (orderDifference) return orderDifference;
    return Number(a.source_interest_excel_row) - Number(b.source_interest_excel_row);
  });

const interests = interestRows.map(row => ({
  programmeProviderId: row.counselor_programme_id,
  interest: row.student_interest,
  relationship: row.interest_relationship,
  strength: row.strength,
  sourceInterestExcelRow: Number(row.source_interest_excel_row),
  targetMappingStatus: row.target_mapping_status
}));

const programmePayload = { schemaVersion: '0.1-review', programmes };
const interestPayload = { schemaVersion: '0.1-review', interests };

function verify(file, expected, label) {
  assert(fs.existsSync(file), `${label} is missing; run npm run build:counselor-review`);
  const actual = readJson(file);
  assert(JSON.stringify(actual) === JSON.stringify(expected), `${label} is stale; run npm run build:counselor-review`);
}

if (checkOnly) {
  verify(reviewProgrammeFile, programmePayload, 'review-programmes.json');
  verify(reviewInterestFile, interestPayload, 'review-interests.json');
  console.log(`Current counselor review indexes: ${programmes.length} programmes, ${interests.length} interest rows.`);
} else {
  fs.writeFileSync(reviewProgrammeFile, stableJson(programmePayload));
  fs.writeFileSync(reviewInterestFile, stableJson(interestPayload));
  console.log(`Wrote counselor review indexes: ${programmes.length} programmes, ${interests.length} interest rows.`);
}
