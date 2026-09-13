import fs from 'node:fs';
import path from 'node:path';
import { readExample, validateExample } from './example-utils.mjs';

const root = process.cwd();
const target = process.argv[2] || 'all';
const dir = path.join(root, 'data', 'counselor', 'comparisons');
const cpPattern = /^cp-[0-9]{6}$/;

function counselorFiles() {
  if (target !== 'all') {
    const id = target.toLowerCase().replace(/\.json$/i, '');
    if (!cpPattern.test(id)) throw new Error(`Invalid counselor production id: ${target}`);
    const file = path.join(dir, `${id}.json`);
    if (!fs.existsSync(file)) throw new Error(`Counselor comparison not found: ${id}`);
    return [file];
  }

  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir)
    .filter(name => /^cp-[0-9]{6}\.json$/.test(name))
    .sort()
    .map(name => path.join(dir, name));
}

let failed = false;
const files = counselorFiles();

if (target === 'all' && files.length === 0) {
  console.log('No normalized counselor production records found. Legacy pre-normalization comparison files are intentionally ignored.');
}

for (const file of files) {
  const sourceName = path.basename(file);
  const record = readExample(file);
  const generic = validateExample(record, sourceName);
  const errors = [...generic.errors];
  const warnings = [...generic.warnings];
  const fail = message => errors.push(`${sourceName}: ${message}`);

  if (record.origin !== 'counselor') fail('origin must be "counselor"');
  if (!cpPattern.test(String(record.id || ''))) fail('id must use permanent cp-000001 format');

  const counselorProgrammeId = String(record?.programmeProvider?.counselorProgrammeId || '');
  if (!cpPattern.test(counselorProgrammeId)) {
    fail('programmeProvider.counselorProgrammeId is required and must use permanent cp-000001 format');
  }

  if (cpPattern.test(String(record.id || '')) && cpPattern.test(counselorProgrammeId) && record.id !== counselorProgrammeId) {
    fail('id must equal programmeProvider.counselorProgrammeId');
  }

  const filenameId = path.basename(file, '.json');
  if (record.id !== filenameId) fail('filename must equal the permanent counselor programme id');

  warnings.forEach(message => console.warn(`WARNING: ${message}`));
  if (errors.length) {
    failed = true;
    errors.forEach(message => console.error(`ERROR: ${message}`));
  } else {
    console.log(`Valid counselor production record: ${sourceName}`);
  }
}

if (failed) process.exit(1);
