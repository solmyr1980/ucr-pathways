import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

const DECISION_SCHEMA = '1.0';
const RECORD_SCHEMA = '2.0';
const COHORT = 'Fall 2026 UCR start';
const SEMESTERS = [
  { label: 'Year 1 · Semester 1', term: '2026h2' },
  { label: 'Year 1 · Semester 2', term: '2027h1' },
  { label: 'Year 2 · Semester 1', term: '2027h2' },
  { label: 'Year 2 · Semester 2', term: '2028h1' },
  { label: 'Year 3 · Semester 1', term: '2028h2' },
  { label: 'Year 3 · Semester 2', term: '2029h1' }
];
const CP_PATTERN = /^cp-[0-9]{6}$/;
const ALTERNATIVE_KINDS = new Set(['closest-match', 'related-direction', 'question-led', 'other-defensible']);

function fail(message) {
  throw new Error(`Counselor decision is invalid: ${message}`);
}

function requireCondition(condition, message) {
  if (!condition) fail(message);
}

function parseCsv(text) {
  const rows = [];
  let row = [];
  let field = '';
  let quoted = false;

  for (let index = 0; index < text.length; index += 1) {
    const character = text[index];
    if (quoted) {
      if (character === '"') {
        if (text[index + 1] === '"') {
          field += '"';
          index += 1;
        } else quoted = false;
      } else field += character;
      continue;
    }
    if (character === '"') quoted = true;
    else if (character === ',') {
      row.push(field);
      field = '';
    } else if (character === '\n') {
      row.push(field.replace(/\r$/, ''));
      rows.push(row);
      row = [];
      field = '';
    } else field += character;
  }

  if (field.length || row.length) {
    row.push(field.replace(/\r$/, ''));
    rows.push(row);
  }
  requireCondition(rows.length > 0, 'CSV source is empty');
  const headers = rows[0].map((value, index) => index === 0 ? value.replace(/^\uFEFF/, '') : value);
  return rows.slice(1)
    .filter(values => values.some(value => String(value).trim()))
    .map((values, index) => ({
      ...Object.fromEntries(headers.map((header, column) => [header, values[column] ?? ''])),
      __registryRow: index + 2
    }));
}

function parseJsonArray(value, fieldName) {
  try {
    const parsed = JSON.parse(value || '[]');
    requireCondition(Array.isArray(parsed), `registry field ${fieldName} is not a JSON array`);
    return parsed;
  } catch (error) {
    if (String(error.message).startsWith('Counselor decision is invalid:')) throw error;
    fail(`registry field ${fieldName} is not valid JSON`);
  }
}

function expectedConstructionRole(row) {
  if (row.target_mapping_status === 'inherited-across-split-targets') return 'excluded-inherited';
  switch (row.interest_relationship) {
    case 'Direct programme interest':
    case 'Stable study direction':
      return 'generator-eligible';
    case 'Curricular topic':
      return 'support-only';
    case 'Illustrative or temporary topic':
    case 'Outcome or individual trajectory':
      return 'search-only';
    default:
      fail(`unsupported interest relationship ${JSON.stringify(row.interest_relationship)} at programme_interests.csv:${row.__registryRow}`);
  }
}

function programmeProviderFromRegistry(row) {
  requireCondition(row.production_eligible === 'true', `${row.counselor_programme_id} is not production_eligible=true`);
  requireCondition(Boolean(row.production_order), `${row.counselor_programme_id} has no production_order`);
  requireCondition(row.programme_type === 'standard', `${row.counselor_programme_id} has programme_type ${JSON.stringify(row.programme_type)}, not standard`);
  return {
    counselorProgrammeId: row.counselor_programme_id,
    registryName: row.canonical_name,
    registryOrder: Number(row.registry_order),
    productionOrder: Number(row.production_order),
    normalizedInstitutionIds: parseJsonArray(row.institution_ids_json, 'institution_ids_json'),
    programmeType: row.programme_type,
    currentStatus: row.current_status,
    productionEligible: true,
    languages: parseJsonArray(row.languages_json, 'languages_json'),
    modes: parseJsonArray(row.modes_json, 'modes_json'),
    sourceExcelRows: parseJsonArray(row.source_excel_rows_json, 'source_excel_rows_json'),
    offeredProgrammeIds: parseJsonArray(row.offering_ids_json, 'offering_ids_json'),
    programmeUnitCodes: parseJsonArray(row.programme_unit_codes_json, 'programme_unit_codes_json'),
    recognizedProgrammeCodes: parseJsonArray(row.recognized_programme_codes_json, 'recognized_programme_codes_json'),
    variantOfCodes: parseJsonArray(row.variant_of_codes_json, 'variant_of_codes_json')
  };
}

function assessedInterestsFromRegistry(rows, id) {
  return rows
    .filter(row => row.counselor_programme_id === id)
    .map(row => ({
      registryRow: row.__registryRow,
      sourceInterestExcelRow: Number(row.source_interest_excel_row),
      studentInterest: row.student_interest,
      interestRelationship: row.interest_relationship,
      targetMappingStatus: row.target_mapping_status,
      constructionRole: expectedConstructionRole(row)
    }));
}

function validateCourseFacts(courseFacts) {
  requireCondition(courseFacts && typeof courseFacts === 'object' && !Array.isArray(courseFacts), 'ucrCourseFacts must be an object keyed by exact UCR course code');
  for (const [code, course] of Object.entries(courseFacts)) {
    requireCondition(code.trim() === code && code.length > 0, 'ucrCourseFacts contains a blank or padded course code');
    requireCondition(course && typeof course === 'object' && !Array.isArray(course), `ucrCourseFacts.${code} must be an object`);
    requireCondition(typeof course.name === 'string' && course.name.trim(), `ucrCourseFacts.${code}.name is required`);
    requireCondition(Number.isInteger(course.level) && course.level >= 1, `ucrCourseFacts.${code}.level must be a positive integer`);
    requireCondition(typeof course.credits === 'number' && course.credits > 0, `ucrCourseFacts.${code}.credits must be a positive number`);
  }
}

function buildProgrammes(decision) {
  const alternatives = decision.alternatives;
  requireCondition(Array.isArray(alternatives) && alternatives.length >= 1 && alternatives.length <= 3, 'alternatives must contain one to three academic decisions');
  validateCourseFacts(decision.ucrCourseFacts);
  const usedCourseCodes = new Set();
  const programmes = [{
    id: 'comparator',
    role: 'comparator',
    family: 'comparator',
    label: `${decision.comparator.name} at ${decision.comparator.institution}`
  }];

  alternatives.forEach((alternative, alternativeIndex) => {
    const programmeId = `ucr-${alternativeIndex + 1}`;
    requireCondition(ALTERNATIVE_KINDS.has(alternative.alternativeKind), `${programmeId}.alternativeKind is invalid`);
    requireCondition(alternativeIndex !== 0 || alternative.alternativeKind === 'closest-match', 'the first alternative must be closest-match');
    requireCondition(typeof alternative.label === 'string' && alternative.label.trim(), `${programmeId}.label is required`);
    requireCondition(Array.isArray(alternative.semesters) && alternative.semesters.length === 6, `${programmeId}.semesters must contain six explicit semester assignments`);
    const programmeCodes = [];
    const semesters = alternative.semesters.map((codes, semesterIndex) => {
      requireCondition(Array.isArray(codes) && codes.length === 4, `${programmeId} semester ${semesterIndex + 1} must contain four course codes`);
      const courses = codes.map(code => {
        requireCondition(typeof code === 'string' && code.trim(), `${programmeId} semester ${semesterIndex + 1} contains an invalid course code`);
        const fact = decision.ucrCourseFacts[code];
        requireCondition(Boolean(fact), `${programmeId} references ${code}, which is absent from ucrCourseFacts`);
        programmeCodes.push(code);
        usedCourseCodes.add(code);
        return { code, name: fact.name, level: fact.level, credits: fact.credits };
      });
      return { ...SEMESTERS[semesterIndex], courses };
    });
    requireCondition(new Set(programmeCodes).size === 24, `${programmeId} must contain 24 unique courses`);
    requireCondition(programmeCodes.includes('ACCPPDE101'), `${programmeId} must contain ACCPPDE101`);
    requireCondition(alternative.semesters.slice(0, 2).flat().includes('ACCPPDE101'), `${programmeId} must place ACCPPDE101 in Year 1`);
    const totalCredits = programmeCodes.reduce((sum, code) => sum + decision.ucrCourseFacts[code].credits, 0);
    requireCondition(Math.abs(totalCredits - 180) < 0.001, `${programmeId} totals ${totalCredits} EC rather than 180 EC`);
    const advancedCourses = programmeCodes.filter(code => decision.ucrCourseFacts[code].level >= 3).length;
    requireCondition(advancedCourses >= 6, `${programmeId} has ${advancedCourses} courses at level 3 or above; at least 6 are required`);
    programmes.push({
      id: programmeId,
      role: 'ucr-alternative',
      family: 'ucr',
      alternativeKind: alternative.alternativeKind,
      label: alternative.label,
      schedule: { semesters }
    });
  });

  const unusedFacts = Object.keys(decision.ucrCourseFacts).filter(code => !usedCourseCodes.has(code));
  requireCondition(unusedFacts.length === 0, `ucrCourseFacts contains unused courses: ${unusedFacts.join(', ')}`);
  return programmes;
}

function buildComparison(decision, programmes) {
  const components = decision.comparator.components;
  requireCondition(Array.isArray(components) && components.length > 0, 'comparator.components must be non-empty');
  const componentsById = new Map();
  let comparatorCredits = 0;
  for (const component of components) {
    requireCondition(component && typeof component === 'object' && !Array.isArray(component), 'each comparator component must be an object');
    requireCondition(typeof component.id === 'string' && component.id.trim(), 'each comparator component requires an id');
    requireCondition(!componentsById.has(component.id), `duplicate comparator component id ${component.id}`);
    requireCondition(typeof component.name === 'string' && component.name.trim(), `comparator component ${component.id} requires a name`);
    requireCondition(typeof component.credits === 'number' && component.credits > 0, `comparator component ${component.id} requires positive numeric credits`);
    componentsById.set(component.id, component);
    comparatorCredits += component.credits;
  }
  requireCondition(Math.abs(comparatorCredits - 180) < 0.001, `comparator components total ${comparatorCredits} EC rather than 180 EC`);

  const programmeCourseSets = new Map(programmes.slice(1).map(programme => [
    programme.id,
    new Set(programme.schedule.semesters.flatMap(semester => semester.courses.map(course => course.code)))
  ]));
  const selectedCourseCodes = new Set([...programmeCourseSets.values()].flatMap(set => [...set]));
  const layout = decision.comparisonLayout;
  requireCondition(layout && Array.isArray(layout.blocks) && layout.blocks.length > 0, 'comparisonLayout.blocks must be non-empty');
  requireCondition(layout.alignmentRationales && typeof layout.alignmentRationales === 'object' && !Array.isArray(layout.alignmentRationales), 'comparisonLayout.alignmentRationales must be an object');

  const seenCourses = new Set();
  const seenComponents = new Set();
  const componentPlacements = new Map();
  const blocks = layout.blocks.map((block, blockIndex) => {
    requireCondition(block && typeof block === 'object' && !Array.isArray(block), `comparison block ${blockIndex + 1} must be an object`);
    requireCondition(typeof block.title === 'string' && block.title.trim(), `comparison block ${blockIndex + 1} requires a title`);
    requireCondition(Array.isArray(block.rows) && block.rows.length > 0, `comparison block ${blockIndex + 1} requires rows`);
    const built = { title: block.title };
    if (block.id !== undefined) {
      requireCondition(typeof block.id === 'string' && block.id.trim(), `comparison block ${blockIndex + 1}.id must be non-empty when supplied`);
      built.id = block.id;
    }
    built.rows = block.rows.map((row, rowIndex) => {
      requireCondition(row && typeof row === 'object' && !Array.isArray(row), `comparison block ${blockIndex + 1}, row ${rowIndex + 1} must be an object`);
      const courseCode = row.courseCode;
      const componentId = row.componentId;
      requireCondition(Boolean(courseCode || componentId), `comparison block ${blockIndex + 1}, row ${rowIndex + 1} must identify a UCR course or comparator component`);
      const cells = {};

      if (componentId) {
        requireCondition(componentsById.has(componentId), `comparison row references unknown comparator component ${componentId}`);
        requireCondition(!seenComponents.has(componentId), `comparator component ${componentId} appears in more than one comparison row`);
        seenComponents.add(componentId);
        const component = componentsById.get(componentId);
        cells.comparator = { text: component.name, credits: component.credits, componentId };
        if (component.note !== undefined) cells.comparator.note = component.note;
        componentPlacements.set(componentId, courseCode || null);
      }

      if (courseCode) {
        requireCondition(selectedCourseCodes.has(courseCode), `comparison row references unselected UCR course ${courseCode}`);
        requireCondition(!seenCourses.has(courseCode), `UCR course ${courseCode} appears in more than one comparison row`);
        seenCourses.add(courseCode);
        const fact = decision.ucrCourseFacts[courseCode];
        for (const programme of programmes.slice(1)) {
          if (programmeCourseSets.get(programme.id).has(courseCode)) {
            cells[programme.id] = { text: fact.name, credits: fact.credits, courseCode };
          }
        }
      }
      return { cells };
    });
    return built;
  });

  const missingCourses = [...selectedCourseCodes].filter(code => !seenCourses.has(code));
  const missingComponents = [...componentsById.keys()].filter(id => !seenComponents.has(id));
  requireCondition(missingCourses.length === 0, `comparison layout omits selected UCR courses: ${missingCourses.join(', ')}`);
  requireCondition(missingComponents.length === 0, `comparison layout omits comparator components: ${missingComponents.join(', ')}`);
  const extraRationales = Object.keys(layout.alignmentRationales).filter(id => !componentsById.has(id));
  requireCondition(extraRationales.length === 0, `alignmentRationales contains unknown comparator components: ${extraRationales.join(', ')}`);

  const comparisonAlignment = components.map(component => {
    const rationale = layout.alignmentRationales[component.id];
    requireCondition(typeof rationale === 'string' && rationale.trim(), `alignment rationale is required for comparator component ${component.id}`);
    const courseCode = componentPlacements.get(component.id);
    if (courseCode) return { componentId: component.id, matchType: 'substantive-match', ucrCourseCode: courseCode, rationale };
    return { componentId: component.id, matchType: 'unmatched', rationale };
  });
  return { blocks, comparisonAlignment };
}

export function compileCounselorDecision(decision, root = process.cwd()) {
  requireCondition(decision && typeof decision === 'object' && !Array.isArray(decision), 'decision file must contain a JSON object');
  requireCondition(decision.decisionSchemaVersion === DECISION_SCHEMA, `decisionSchemaVersion must be ${JSON.stringify(DECISION_SCHEMA)}`);
  requireCondition(CP_PATTERN.test(String(decision.id || '')), 'id must use cp-000001 format');
  requireCondition(decision.comparator && typeof decision.comparator === 'object' && !Array.isArray(decision.comparator), 'comparator must be an object');
  requireCondition(typeof decision.comparator.name === 'string' && decision.comparator.name.trim(), 'comparator.name is required');
  requireCondition(typeof decision.comparator.institution === 'string' && decision.comparator.institution.trim(), 'comparator.institution is required');
  requireCondition(decision.academicRationale && typeof decision.academicRationale === 'object' && !Array.isArray(decision.academicRationale), 'academicRationale must be an object');
  requireCondition(decision.alternativeSelection && typeof decision.alternativeSelection === 'object' && !Array.isArray(decision.alternativeSelection), 'alternativeSelection must be an object');

  const registryRows = parseCsv(fs.readFileSync(path.join(root, 'data', 'registry', 'programmes.csv'), 'utf8'));
  const registry = registryRows.find(row => row.counselor_programme_id === decision.id);
  requireCondition(Boolean(registry), `${decision.id} is absent from data/registry/programmes.csv`);
  const interestRows = parseCsv(fs.readFileSync(path.join(root, 'data', 'registry', 'programme_interests.csv'), 'utf8'));
  const programmes = buildProgrammes(decision);
  const { blocks, comparisonAlignment } = buildComparison(decision, programmes);

  const academicRationale = structuredClone(decision.academicRationale);
  requireCondition(academicRationale.interestSelection && typeof academicRationale.interestSelection === 'object' && !Array.isArray(academicRationale.interestSelection), 'academicRationale.interestSelection must be an object');
  requireCondition(!Object.hasOwn(academicRationale.interestSelection, 'assessedInterests'), 'assessedInterests is compiler-generated and must be omitted from the decision file');
  academicRationale.interestSelection = {
    assessedInterests: assessedInterestsFromRegistry(interestRows, decision.id),
    ...academicRationale.interestSelection
  };

  return {
    schemaVersion: RECORD_SCHEMA,
    origin: 'counselor',
    id: decision.id,
    cohort: COHORT,
    programmeProvider: programmeProviderFromRegistry(registry),
    comparator: structuredClone(decision.comparator),
    programmes,
    academicRationale,
    alternativeSelection: {
      includedCount: programmes.length - 1,
      stoppingReason: decision.alternativeSelection.stoppingReason,
      assessment: decision.alternativeSelection.assessment
    },
    comparisonAlignment,
    blocks,
    notes: structuredClone(decision.notes || [])
  };
}

function parseArguments(argv) {
  const input = argv[0];
  requireCondition(Boolean(input), 'usage: node scripts/build-counselor-comparison.mjs <decision.json> [--output <comparison.json>]');
  let output;
  for (let index = 1; index < argv.length; index += 1) {
    if (argv[index] === '--output') {
      output = argv[index + 1];
      requireCondition(Boolean(output), '--output requires a path');
      index += 1;
    } else fail(`unknown argument ${JSON.stringify(argv[index])}`);
  }
  return { input, output };
}

function main() {
  const { input, output } = parseArguments(process.argv.slice(2));
  const inputPath = path.resolve(input);
  requireCondition(fs.existsSync(inputPath), `decision file not found: ${inputPath}`);
  const decision = JSON.parse(fs.readFileSync(inputPath, 'utf8'));
  const record = compileCounselorDecision(decision);
  const outputPath = path.resolve(output || path.join('data', 'counselor', 'comparisons', `${record.id}.json`));
  requireCondition(!fs.existsSync(outputPath), `refusing to overwrite existing canonical comparison: ${outputPath}`);
  fs.mkdirSync(path.dirname(outputPath), { recursive: true });
  fs.writeFileSync(outputPath, `${JSON.stringify(record, null, 2)}\n`, { flag: 'wx' });
  console.log(`Built ${record.id} from ${inputPath} at ${outputPath}`);
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  try {
    main();
  } catch (error) {
    console.error(error.message);
    process.exit(1);
  }
}
