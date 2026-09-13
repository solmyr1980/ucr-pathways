import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const registryDir = path.join(root, 'data', 'registry');
const interestsFile = path.join(registryDir, 'programme_interests.csv');
const programmesFile = path.join(registryDir, 'programmes.csv');
const reportFile = path.join(registryDir, 'step3_report.json');

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
      } else {
        field += ch;
      }
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
    } else {
      field += ch;
    }
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

function fail(message) {
  console.error(`ERROR: ${message}`);
  process.exitCode = 1;
}

for (const file of [interestsFile, programmesFile, reportFile]) {
  if (!fs.existsSync(file)) fail(`missing required registry file: ${path.relative(root, file)}`);
}
if (process.exitCode) process.exit(process.exitCode);

const interestsText = fs.readFileSync(interestsFile, 'utf8');
if (!interestsText.trim()) {
  fail('data/registry/programme_interests.csv is empty');
  process.exit(process.exitCode);
}

const interests = parseCsv(interestsText);
const programmes = parseCsv(fs.readFileSync(programmesFile, 'utf8'));
const report = JSON.parse(fs.readFileSync(reportFile, 'utf8'));
const programmeIds = new Set(programmes.map(row => row.counselor_programme_id).filter(Boolean));

const expectedRows = Number(report?.outputs?.normalized_programme_interest_rows);
const expectedOriginal = Number(report?.inputs?.original_programme_interest_records);
const expectedWithoutTarget = Number(report?.outputs?.original_interest_records_without_current_target);

if (!Number.isInteger(expectedRows)) fail('step3_report.json lacks outputs.normalized_programme_interest_rows');
else if (interests.length !== expectedRows) fail(`programme_interests.csv has ${interests.length} rows; expected ${expectedRows}`);

const requiredHeaders = [
  'source_interest_excel_row',
  'source_excel_row',
  'student_interest',
  'interest_relationship',
  'counselor_programme_id',
  'target_mapping_status'
];
const first = interests[0] || {};
for (const header of requiredHeaders) {
  if (!Object.hasOwn(first, header)) fail(`programme_interests.csv is missing required column ${header}`);
}

const originalIds = new Set();
let blankTargets = 0;
let badMappings = 0;
const allowedStatuses = new Set(['mapped', 'inherited-across-split-targets', 'excluded-no-current-target']);

for (const [index, row] of interests.entries()) {
  const rowNumber = index + 2;
  const sourceId = String(row.source_interest_excel_row || '').trim();
  const targetId = String(row.counselor_programme_id || '').trim();
  const status = String(row.target_mapping_status || '').trim();

  if (!sourceId) fail(`programme_interests.csv row ${rowNumber} has no source_interest_excel_row`);
  else originalIds.add(sourceId);
  if (!String(row.student_interest || '').trim()) fail(`programme_interests.csv row ${rowNumber} has no student_interest`);
  if (!String(row.interest_relationship || '').trim()) fail(`programme_interests.csv row ${rowNumber} has no interest_relationship`);
  if (!allowedStatuses.has(status)) fail(`programme_interests.csv row ${rowNumber} has unexpected target_mapping_status ${JSON.stringify(status)}`);

  if (targetId) {
    if (!programmeIds.has(targetId)) {
      badMappings += 1;
      fail(`programme_interests.csv row ${rowNumber} references unknown counselor_programme_id ${targetId}`);
    }
    if (status === 'excluded-no-current-target') fail(`programme_interests.csv row ${rowNumber} has a target but status excluded-no-current-target`);
  } else {
    blankTargets += 1;
    if (status !== 'excluded-no-current-target') fail(`programme_interests.csv row ${rowNumber} has no target but status is ${JSON.stringify(status)}`);
  }
}

if (Number.isInteger(expectedOriginal) && originalIds.size !== expectedOriginal) {
  fail(`programme_interests.csv represents ${originalIds.size} unique original interest records; expected ${expectedOriginal}`);
}
if (Number.isInteger(expectedWithoutTarget) && blankTargets !== expectedWithoutTarget) {
  fail(`programme_interests.csv has ${blankTargets} rows without a current target; expected ${expectedWithoutTarget}`);
}

if (!process.exitCode) {
  console.log(`Valid programme-interest registry: ${interests.length} normalized rows, ${originalIds.size} original records, ${blankTargets} excluded/no-target rows, ${badMappings} bad target mappings.`);
}
