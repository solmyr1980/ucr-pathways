import fs from 'node:fs';
import path from 'node:path';
import { isUcrProgramme, normalizeCell, readExample, validateExample } from './example-utils.mjs';

const root = process.cwd();
const target = process.argv[2] || 'all';
const dir = path.join(root, 'data', 'counselor', 'comparisons');
const registryFile = path.join(root, 'data', 'registry', 'programmes.csv');
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
    } else field += ch;
  }

  if (field.length || row.length) {
    row.push(field.replace(/\r$/, ''));
    rows.push(row);
  }

  if (!rows.length) return [];
  const headers = rows[0].map((value, index) => index === 0 ? value.replace(/^\uFEFF/, '') : value);
  return rows.slice(1)
    .filter(values => values.some(value => String(value).trim()))
    .map(values => Object.fromEntries(headers.map((header, index) => [header, values[index] ?? ''])));
}

function parseJsonArray(value, fieldName, errors, sourceName) {
  try {
    const parsed = JSON.parse(value || '[]');
    if (!Array.isArray(parsed)) throw new Error('not an array');
    return parsed;
  } catch {
    errors.push(`${sourceName}: registry field ${fieldName} is not valid JSON array data`);
    return [];
  }
}

function comparableArray(values) {
  return [...values].map(value => typeof value === 'number' ? value : String(value)).sort((a, b) => String(a).localeCompare(String(b), undefined, { numeric: true }));
}

function arraysEqual(left, right) {
  const a = comparableArray(Array.isArray(left) ? left : []);
  const b = comparableArray(Array.isArray(right) ? right : []);
  return a.length === b.length && a.every((value, index) => value === b[index]);
}

function creditNumber(value) {
  if (typeof value === 'number' && Number.isFinite(value)) return value;
  if (typeof value !== 'string') return null;
  const match = value.replace(',', '.').match(/-?\d+(?:\.\d+)?/);
  return match ? Number(match[0]) : null;
}

function blockCredit(block, programmeId) {
  let total = 0;
  let found = false;
  for (const row of Array.isArray(block?.rows) ? block.rows : []) {
    const cell = normalizeCell(row?.cells?.[programmeId]);
    if (!cell) continue;
    const credits = creditNumber(cell.credits);
    if (credits === null) return null;
    total += credits;
    found = true;
  }
  return found ? total : null;
}

function validateEvidence(evidence, label, fail) {
  if (!Array.isArray(evidence) || evidence.length === 0) {
    fail(`${label} requires at least one evidence reference`);
    return;
  }
  evidence.forEach((item, index) => {
    if (!item || typeof item !== 'object' || Array.isArray(item)) {
      fail(`${label} evidence ${index + 1} must be an object`);
      return;
    }
    if (!['official-source', 'programme-interest'].includes(item.sourceType)) {
      fail(`${label} evidence ${index + 1} sourceType must be official-source or programme-interest`);
    }
    if (typeof item.reference !== 'string' || !item.reference.trim()) {
      fail(`${label} evidence ${index + 1} requires a reference`);
    }
  });
}

function validateMapItems(items, fieldName, fail, { allowEmpty = false } = {}) {
  if (!Array.isArray(items) || (!allowEmpty && items.length === 0)) {
    fail(`academicRationale.${fieldName} must be ${allowEmpty ? 'an array' : 'a non-empty array'}`);
    return [];
  }
  const labels = [];
  items.forEach((item, index) => {
    const label = `${fieldName}[${index}]`;
    if (!item || typeof item !== 'object' || Array.isArray(item)) {
      fail(`academicRationale.${label} must be an object`);
      return;
    }
    if (typeof item.label !== 'string' || !item.label.trim()) {
      fail(`academicRationale.${label}.label is required`);
      return;
    }
    labels.push(item.label.trim());
    validateEvidence(item.evidence, `academicRationale.${label}`, fail);
  });
  if (new Set(labels).size !== labels.length) fail(`academicRationale.${fieldName} labels must be unique`);
  return labels;
}

function validateStableComparisonReferences(record, fail) {
  const comparatorComponents = record?.comparator?.components;
  if (!Array.isArray(comparatorComponents) || comparatorComponents.length === 0) {
    fail('comparator.components must contain the complete reconstructed 180-EC comparator curriculum');
  }

  for (const programme of record?.programmes || []) {
    if (!isUcrProgramme(programme)) continue;
    for (const semester of programme?.schedule?.semesters || []) {
      for (const course of semester?.courses || []) {
        if (typeof course?.code !== 'string' || !course.code.trim()) {
          fail(`scheduled course ${JSON.stringify(course?.name || '')} in ${programme.id} requires a course code in current production records`);
        }
      }
    }
  }

  for (const block of record?.blocks || []) {
    for (const [rowIndex, row] of (block?.rows || []).entries()) {
      for (const programme of record?.programmes || []) {
        const cell = normalizeCell(row?.cells?.[programme.id]);
        if (!cell) continue;
        if (programme.role === 'comparator') {
          if (typeof cell.componentId !== 'string' || !cell.componentId.trim()) {
            fail(`block ${block.title}, row ${rowIndex + 1}: comparator cell requires componentId`);
          }
        } else if (isUcrProgramme(programme)) {
          if (typeof cell.courseCode !== 'string' || !cell.courseCode.trim()) {
            fail(`block ${block.title}, row ${rowIndex + 1}, programme ${programme.id}: UCR cell requires courseCode`);
          }
        }
      }
    }
  }
}

function validateAlternativeRationales(record, rationale, mapLabels, fail) {
  const ucrProgrammes = (record.programmes || []).filter(isUcrProgramme);
  if (!Array.isArray(rationale.alternatives) || rationale.alternatives.length !== ucrProgrammes.length) {
    fail(`academicRationale.alternatives must contain exactly one rationale for each of the ${ucrProgrammes.length} included UCR alternatives`);
    return;
  }

  const seenIds = new Set();
  rationale.alternatives.forEach((alternative, index) => {
    const label = `academicRationale.alternatives[${index}]`;
    if (!alternative || typeof alternative !== 'object' || Array.isArray(alternative)) {
      fail(`${label} must be an object`);
      return;
    }

    const expectedId = ucrProgrammes[index]?.id;
    if (typeof alternative.programmeId !== 'string' || !alternative.programmeId.trim()) {
      fail(`${label}.programmeId is required`);
    } else {
      if (alternative.programmeId !== expectedId) fail(`${label}.programmeId must be ${JSON.stringify(expectedId)} to preserve UCR alternative order`);
      if (seenIds.has(alternative.programmeId)) fail('academicRationale.alternatives programmeId values must be unique');
      seenIds.add(alternative.programmeId);
    }

    if (typeof alternative.concept !== 'string' || !alternative.concept.trim()) fail(`${label}.concept is required`);
    if (!Array.isArray(alternative.basisLabels) || alternative.basisLabels.length === 0) {
      fail(`${label}.basisLabels must identify at least one evidence-map item`);
    } else {
      if (new Set(alternative.basisLabels).size !== alternative.basisLabels.length) fail(`${label}.basisLabels must be unique`);
      alternative.basisLabels.forEach(item => {
        if (!mapLabels.has(item)) fail(`${label} basis label ${JSON.stringify(item)} is not present in the academic interest map`);
      });
    }
    validateEvidence(alternative.evidence, label, fail);

    if (index > 0 && (typeof alternative.distinctnessRationale !== 'string' || !alternative.distinctnessRationale.trim())) {
      fail(`${label}.distinctnessRationale is required for every UCR alternative after the closest match`);
    }
  });
}

const registryRows = parseCsv(fs.readFileSync(registryFile, 'utf8'));
const registryById = new Map(registryRows.map(row => [row.counselor_programme_id, row]));

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
  const warn = message => warnings.push(`${sourceName}: ${message}`);

  if (record.schemaVersion !== '2.0') fail('schemaVersion must be "2.0" for current counselor production records');
  if (record.origin !== 'counselor') fail('origin must be "counselor"');
  if (!cpPattern.test(String(record.id || ''))) fail('id must use permanent cp-000001 format');

  const programmes = Array.isArray(record.programmes) ? record.programmes : [];
  const ucrProgrammes = programmes.filter(isUcrProgramme);
  if (ucrProgrammes.length < 1 || ucrProgrammes.length > 3) fail('record must contain one to three UCR alternatives');
  ucrProgrammes.forEach((programme, index) => {
    if (programme.role !== 'ucr-alternative') fail(`UCR programme ${programme.id || index + 1} must use role "ucr-alternative"`);
    if (!['closest-match', 'related-direction', 'question-led', 'other-defensible'].includes(programme.alternativeKind)) {
      fail(`UCR programme ${programme.id || index + 1} requires a valid alternativeKind`);
    }
    if (index === 0 && programme.alternativeKind !== 'closest-match') fail('the first UCR alternative must be alternativeKind "closest-match"');
  });

  const selection = record?.alternativeSelection;
  if (!selection || typeof selection !== 'object' || Array.isArray(selection)) {
    fail('alternativeSelection is required');
  } else if (selection.includedCount !== ucrProgrammes.length) {
    fail('alternativeSelection.includedCount must equal the number of included UCR alternatives');
  }

  validateStableComparisonReferences(record, fail);

  const provider = record?.programmeProvider;
  const counselorProgrammeId = String(provider?.counselorProgrammeId || '');
  if (!cpPattern.test(counselorProgrammeId)) {
    fail('programmeProvider.counselorProgrammeId is required and must use permanent cp-000001 format');
  }

  if (cpPattern.test(String(record.id || '')) && cpPattern.test(counselorProgrammeId) && record.id !== counselorProgrammeId) {
    fail('id must equal programmeProvider.counselorProgrammeId');
  }

  const filenameId = path.basename(file, '.json');
  if (record.id !== filenameId) fail('filename must equal the permanent counselor programme id');

  const registry = registryById.get(record.id);
  if (!registry) {
    fail('id does not exist in data/registry/programmes.csv');
  } else if (provider && typeof provider === 'object' && !Array.isArray(provider)) {
    if (registry.production_eligible !== 'true') fail('registry target is not production_eligible=true');
    if (!registry.production_order) fail('registry target has no production_order');
    if (registry.programme_type !== 'standard') fail(`registry programme_type is ${registry.programme_type}; current production requires standard`);

    const scalarChecks = [
      ['registryName', registry.canonical_name],
      ['programmeType', registry.programme_type],
      ['currentStatus', registry.current_status]
    ];
    scalarChecks.forEach(([field, expected]) => {
      if (provider[field] !== expected) fail(`programmeProvider.${field} must match registry value ${JSON.stringify(expected)}`);
    });

    if (Number(provider.registryOrder) !== Number(registry.registry_order)) fail('programmeProvider.registryOrder must match registry_order');
    if (Number(provider.productionOrder) !== Number(registry.production_order)) fail('programmeProvider.productionOrder must match production_order');
    if (provider.productionEligible !== true) fail('programmeProvider.productionEligible must be true');

    const arrayChecks = [
      ['normalizedInstitutionIds', 'institution_ids_json'],
      ['languages', 'languages_json'],
      ['modes', 'modes_json'],
      ['sourceExcelRows', 'source_excel_rows_json'],
      ['offeredProgrammeIds', 'offering_ids_json'],
      ['programmeUnitCodes', 'programme_unit_codes_json'],
      ['recognizedProgrammeCodes', 'recognized_programme_codes_json'],
      ['variantOfCodes', 'variant_of_codes_json']
    ];

    arrayChecks.forEach(([recordField, registryField]) => {
      const expected = parseJsonArray(registry[registryField], registryField, errors, sourceName);
      if (!arraysEqual(provider[recordField], expected)) {
        fail(`programmeProvider.${recordField} must match registry ${registryField}`);
      }
    });

    if (Object.hasOwn(provider, 'language') || Object.hasOwn(provider, 'mode')) {
      fail('use normalized programmeProvider.languages and programmeProvider.modes arrays; scalar language/mode fields are not current production metadata');
    }
  }

  const rationale = record?.academicRationale;
  if (!rationale || typeof rationale !== 'object' || Array.isArray(rationale)) {
    fail('academicRationale is required');
  } else {
    const coreLabels = validateMapItems(rationale.coreField, 'coreField', fail);
    const adjacentLabels = validateMapItems(rationale.adjacentDirections, 'adjacentDirections', fail, { allowEmpty: true });
    const questionLabels = validateMapItems(rationale.questionsApplications, 'questionsApplications', fail, { allowEmpty: true });
    const mapLabels = new Set([...coreLabels, ...adjacentLabels, ...questionLabels]);
    validateAlternativeRationales(record, rationale, mapLabels, fail);
  }

  const programmeIds = programmes.map(programme => programme?.id).filter(Boolean);
  if (Array.isArray(record.blocks) && record.blocks.length === 3 && programmeIds.length) {
    const exactlySixtyByProgramme = programmeIds.every(programmeId =>
      record.blocks.every(block => {
        const credits = blockCredit(block, programmeId);
        return credits !== null && Math.abs(credits - 60) < 0.001;
      })
    );
    if (exactlySixtyByProgramme) {
      warn('comparison uses an exact 3 × 60 EC structure for every included programme; confirm that the equality is independently justified by the curricula rather than imposed as a template');
    }
  }

  if (Array.isArray(record.blocks) && record.blocks.length && programmeIds.length) {
    let rows = 0;
    let completeRows = 0;
    for (const block of record.blocks) {
      for (const row of Array.isArray(block?.rows) ? block.rows : []) {
        rows += 1;
        if (programmeIds.every(id => normalizeCell(row?.cells?.[id]))) completeRows += 1;
      }
    }
    if (rows >= 3 && completeRows === rows) {
      warn(`every comparison row is populated for all ${programmeIds.length} programmes; review whether genuine gaps have been suppressed for visual symmetry`);
    }
  }

  warnings.forEach(message => console.warn(`WARNING: ${message}`));
  if (errors.length) {
    failed = true;
    errors.forEach(message => console.error(`ERROR: ${message}`));
  } else {
    console.log(`Valid counselor production record: ${sourceName}`);
  }
}

if (failed) process.exit(1);
