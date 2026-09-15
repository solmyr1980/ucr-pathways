import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

const SCHEMA = '2.0';
const RECORD_SCHEMA = '2.0';
const CP_PATTERN = /^cp-[0-9]{6}$/;
const KINDS = new Set(['closest-match', 'related-direction', 'question-led', 'other-defensible']);
const SEMESTERS = [
  ['Year 1 · Semester 1', '2026h2'], ['Year 1 · Semester 2', '2027h1'],
  ['Year 2 · Semester 1', '2027h2'], ['Year 2 · Semester 2', '2028h1'],
  ['Year 3 · Semester 1', '2028h2'], ['Year 3 · Semester 2', '2029h1']
];

function fail(message) { throw new Error(`V2 decision is invalid: ${message}`); }
function requireCondition(condition, message) { if (!condition) fail(message); }
function text(value) { return typeof value === 'string' && value.trim(); }

function parseCsv(value) {
  const rows = []; let row = []; let field = ''; let quoted = false;
  for (let index = 0; index < value.length; index += 1) {
    const character = value[index];
    if (quoted) {
      if (character === '"') {
        if (value[index + 1] === '"') { field += '"'; index += 1; }
        else quoted = false;
      } else field += character;
    } else if (character === '"') quoted = true;
    else if (character === ',') { row.push(field); field = ''; }
    else if (character === '\n') { row.push(field.replace(/\r$/, '')); rows.push(row); row = []; field = ''; }
    else field += character;
  }
  if (field.length || row.length) { row.push(field.replace(/\r$/, '')); rows.push(row); }
  const headers = rows[0].map((item, index) => index ? item : item.replace(/^\uFEFF/, ''));
  return rows.slice(1).filter(values => values.some(item => item.trim())).map((values, index) => ({
    ...Object.fromEntries(headers.map((header, column) => [header, values[column] || ''])),
    __registryRow: index + 2
  }));
}

function jsonArray(value, field) {
  try { const parsed = JSON.parse(value || '[]'); requireCondition(Array.isArray(parsed), `${field} is not an array`); return parsed; }
  catch (error) { if (String(error.message).startsWith('V2 decision')) throw error; fail(`${field} is invalid JSON`); }
}

function constructionRole(row) {
  if (row.target_mapping_status === 'inherited-across-split-targets') return 'excluded-inherited';
  if (['Direct programme interest', 'Stable study direction'].includes(row.interest_relationship)) return 'generator-eligible';
  if (row.interest_relationship === 'Curricular topic') return 'support-only';
  if (['Illustrative or temporary topic', 'Outcome or individual trajectory'].includes(row.interest_relationship)) return 'search-only';
  fail(`unsupported interest relationship at registry row ${row.__registryRow}`);
}

function provider(row) {
  requireCondition(row.production_eligible === 'true' && row.production_order && row.programme_type === 'standard', `${row.counselor_programme_id} is outside production scope`);
  return {
    counselorProgrammeId: row.counselor_programme_id,
    registryName: row.canonical_name,
    registryOrder: Number(row.registry_order),
    productionOrder: Number(row.production_order),
    normalizedInstitutionIds: jsonArray(row.institution_ids_json, 'institution_ids_json'),
    programmeType: row.programme_type,
    currentStatus: row.current_status,
    productionEligible: true,
    languages: jsonArray(row.languages_json, 'languages_json'),
    modes: jsonArray(row.modes_json, 'modes_json'),
    sourceExcelRows: jsonArray(row.source_excel_rows_json, 'source_excel_rows_json'),
    offeredProgrammeIds: jsonArray(row.offering_ids_json, 'offering_ids_json'),
    programmeUnitCodes: jsonArray(row.programme_unit_codes_json, 'programme_unit_codes_json'),
    recognizedProgrammeCodes: jsonArray(row.recognized_programme_codes_json, 'recognized_programme_codes_json'),
    variantOfCodes: jsonArray(row.variant_of_codes_json, 'variant_of_codes_json')
  };
}

function expandSources(decision) {
  requireCondition(Array.isArray(decision.sources) && decision.sources.every(text), 'sources must be non-empty URL strings');
  requireCondition(new Set(decision.sources).size === decision.sources.length, 'sources must not contain duplicate URLs');
  return token => {
    if (Number.isInteger(token)) return { sourceType: 'programme-interest', reference: `programme_interests.csv:${token}` };
    const match = typeof token === 'string' && token.match(/^s(\d+)$/);
    requireCondition(match && decision.sources[Number(match[1])], `unknown evidence token ${JSON.stringify(token)}`);
    return { sourceType: 'official-source', reference: decision.sources[Number(match[1])] };
  };
}

export function compileV2(decision, repositoryRoot) {
  requireCondition(decision && typeof decision === 'object' && !Array.isArray(decision), 'top level must be an object');
  requireCondition(decision.decisionSchemaVersion === SCHEMA, `decisionSchemaVersion must be ${SCHEMA}`);
  requireCondition(CP_PATTERN.test(decision.id), 'id must use cp-000001 format');
  const expandEvidenceToken = expandSources(decision);
  const expandEvidence = values => { requireCondition(Array.isArray(values), 'evidence must be an array'); return values.map(expandEvidenceToken); };

  const programmeRows = parseCsv(fs.readFileSync(path.join(repositoryRoot, 'data/registry/programmes.csv'), 'utf8'));
  const registry = programmeRows.find(row => row.counselor_programme_id === decision.id);
  requireCondition(registry, `${decision.id} is absent from programmes.csv`);
  const interestRows = parseCsv(fs.readFileSync(path.join(repositoryRoot, 'data/registry/programme_interests.csv'), 'utf8'))
    .filter(row => row.counselor_programme_id === decision.id);
  const assessedInterests = interestRows.map(row => ({
    registryRow: row.__registryRow,
    sourceInterestExcelRow: Number(row.source_interest_excel_row),
    studentInterest: row.student_interest,
    interestRelationship: row.interest_relationship,
    targetMappingStatus: row.target_mapping_status,
    constructionRole: constructionRole(row)
  }));
  const assessedByRow = new Map(assessedInterests.map(item => [item.registryRow, item]));

  const comparatorInput = decision.comparator;
  requireCondition(comparatorInput && text(comparatorInput.name) && text(comparatorInput.institution), 'comparator name and institution are required');
  requireCondition(Array.isArray(comparatorInput.components) && comparatorInput.components.length, 'comparator components are required');
  const componentIds = new Set();
  const components = comparatorInput.components.map((tuple, index) => {
    requireCondition(Array.isArray(tuple) && tuple.length >= 3, `comparator component ${index + 1} must be [id,name,credits,note]`);
    const [id, name, credits, note] = tuple;
    requireCondition(text(id) && text(name) && typeof credits === 'number' && credits > 0, `comparator component ${index + 1} is incomplete`);
    requireCondition(!componentIds.has(id), `duplicate comparator component ${id}`); componentIds.add(id);
    return { id, name, credits, ...(note ? { note } : {}) };
  });
  requireCondition(Math.abs(components.reduce((sum, item) => sum + item.credits, 0) - 180) < 0.001, 'comparator components must total 180 EC');
  const sourceFor = token => expandEvidenceToken(token).reference;
  const comparator = {
    name: comparatorInput.name, institution: comparatorInput.institution,
    primarySourceUrl: sourceFor(comparatorInput.primarySource), academicYear: comparatorInput.academicYear,
    ...(comparatorInput.route ? { route: comparatorInput.route } : {}),
    additionalSourceUrls: (comparatorInput.additionalSources || []).map(sourceFor),
    sourceNotes: comparatorInput.sourceNotes, components
  };
  requireCondition(Object.hasOwn(decision, 'routeSelection'), 'routeSelection must explicitly contain the route decision or null');
  if (comparator.route) {
    requireCondition(decision.routeSelection && typeof decision.routeSelection === 'object' && !Array.isArray(decision.routeSelection), 'routeSelection must explain the selected comparator route');
    requireCondition(decision.routeSelection.route === comparator.route, 'routeSelection.route must match comparator.route');
  } else requireCondition(decision.routeSelection === null, 'routeSelection must be null when the comparator has no selected route');

  requireCondition(Array.isArray(decision.courses), 'courses must be an array');
  const courseFacts = new Map();
  for (const [index, tuple] of decision.courses.entries()) {
    requireCondition(Array.isArray(tuple) && tuple.length === 4, `course ${index + 1} must be [code,name,level,credits]`);
    const [code, name, level, credits] = tuple;
    requireCondition(text(code) && text(name) && Number.isInteger(level) && level > 0 && typeof credits === 'number' && credits > 0, `course ${index + 1} has incomplete verified facts`);
    requireCondition(!courseFacts.has(code), `duplicate course facts for ${code}`);
    courseFacts.set(code, { name, level, credits });
  }

  const basisById = new Map();
  const expandedBasis = {};
  for (const key of ['core', 'adjacent', 'questions']) {
    const tuples = decision.basis?.[key];
    requireCondition(Array.isArray(tuples), `basis.${key} must be an array`);
    expandedBasis[key] = tuples.map((tuple, index) => {
      requireCondition(Array.isArray(tuple) && tuple.length === 3, `basis.${key}[${index}] must be [id,label,evidence]`);
      const [id, label, evidence] = tuple;
      requireCondition(text(id) && text(label) && !basisById.has(id), `basis.${key}[${index}] has an invalid or duplicate id`);
      basisById.set(id, label);
      return { label, evidence: expandEvidence(evidence) };
    });
  }
  const labelsFor = ids => { requireCondition(Array.isArray(ids), 'basis references must be an array'); return ids.map(id => { requireCondition(basisById.has(id), `unknown basis id ${id}`); return basisById.get(id); }); };

  requireCondition(Array.isArray(decision.trace), 'course traceability map is required');
  const defaultTrace = new Map();
  for (const [index, tuple] of decision.trace.entries()) {
    requireCondition(Array.isArray(tuple) && tuple.length === 3, `trace ${index + 1} must be [course,basis,reason]`);
    const [code, basisIds, reason] = tuple;
    requireCondition(text(code) && !defaultTrace.has(code), `trace ${index + 1} has an invalid or duplicate course code`);
    requireCondition(text(reason), `trace for ${code} requires a substantive reason`);
    labelsFor(basisIds);
    defaultTrace.set(code, [basisIds, reason]);
  }

  requireCondition(Array.isArray(decision.alternatives) && decision.alternatives.length >= 1 && decision.alternatives.length <= 3, 'alternatives must contain one to three decisions');
  const selectedSets = new Map();
  const programmes = [{ id: 'comparator', role: 'comparator', family: 'comparator', label: `${comparator.name} at ${comparator.institution}` }];
  const rationaleAlternatives = [];
  const auditAlternatives = [];
  const allSelected = new Set();
  decision.alternatives.forEach((alternative, altIndex) => {
    const programmeId = `ucr-${altIndex + 1}`;
    requireCondition(KINDS.has(alternative.kind), `${programmeId} kind is missing or invalid`);
    requireCondition(altIndex || alternative.kind === 'closest-match', 'the first alternative must be closest-match');
    requireCondition(text(alternative.label), `${programmeId} label is required`);
    requireCondition(text(alternative.concept), `${programmeId} alternative concept is required`);
    requireCondition(alternative.labelReviewed === true, `${programmeId} must explicitly confirm final-label review`);
    requireCondition(Array.isArray(alternative.progression) && alternative.progression.length === 2 && alternative.progression[0] === 'passed' && text(alternative.progression[1]), `${programmeId} progression judgment is required`);
    if (altIndex > 0) requireCondition(text(alternative.distinctness), `${programmeId} distinctness rationale is required`);
    requireCondition(Array.isArray(alternative.semesters) && alternative.semesters.length === 6, `${programmeId} requires six explicit semesters`);
    const codes = [];
    const semesters = alternative.semesters.map((group, semesterIndex) => {
      requireCondition(Array.isArray(group) && group.length === 4, `${programmeId} semester ${semesterIndex + 1} must explicitly contain four courses`);
      const courses = group.map(code => {
        requireCondition(courseFacts.has(code), `${programmeId} selected course ${code} lacks verified course facts`);
        codes.push(code); allSelected.add(code);
        return { code, ...courseFacts.get(code) };
      });
      return { label: SEMESTERS[semesterIndex][0], term: SEMESTERS[semesterIndex][1], courses };
    });
    requireCondition(new Set(codes).size === 24, `${programmeId} must schedule 24 unique courses`);
    requireCondition(alternative.semesters.slice(0, 2).flat().includes('ACCPPDE101'), `${programmeId} must schedule ACCPPDE101 in Year 1`);
    requireCondition(Math.abs(codes.reduce((sum, code) => sum + courseFacts.get(code).credits, 0) - 180) < 0.001, `${programmeId} must total 180 EC`);
    requireCondition(codes.filter(code => courseFacts.get(code).level >= 3).length >= 6, `${programmeId} requires six level-3 courses`);
    selectedSets.set(programmeId, new Set(codes));
    programmes.push({ id: programmeId, role: 'ucr-alternative', family: 'ucr', alternativeKind: alternative.kind, label: alternative.label, schedule: { semesters } });
    rationaleAlternatives.push({
      programmeId, concept: alternative.concept, basisLabels: labelsFor(alternative.basis), evidence: expandEvidence(alternative.evidence),
      labelRationale: text(alternative.labelReason)
        ? alternative.labelReason
        : `The explicit final label “${alternative.label}” was supplied after review of the completed curriculum.`,
      ...(alternative.distinctness ? { distinctnessRationale: alternative.distinctness } : {})
    });
    const expectedTrace = codes.filter(code => code !== 'ACCPPDE101');
    const overrides = new Map();
    for (const [traceIndex, tuple] of (alternative.traceOverrides || []).entries()) {
      requireCondition(Array.isArray(tuple) && tuple.length === 3, `${programmeId} trace override ${traceIndex + 1} must be [course,basis,reason]`);
      const [code, basisIds, reason] = tuple;
      requireCondition(expectedTrace.includes(code) && !overrides.has(code), `${programmeId} has an invalid or duplicate trace override for ${code}`);
      requireCondition(text(reason), `${programmeId} trace override for ${code} requires a substantive reason`);
      labelsFor(basisIds);
      overrides.set(code, [basisIds, reason]);
    }
    const courseTraceability = expectedTrace.map(code => {
      const choice = overrides.get(code) || defaultTrace.get(code);
      requireCondition(choice, `${programmeId} selected course ${code} lacks required academic traceability`);
      const [basisIds, reason] = choice;
      const basisLabels = labelsFor(basisIds);
      return { courseCode: code, basisLabels, rationale: `${courseFacts.get(code).name} ${reason}. It implements the explicit academic basis ${basisLabels.map(label => `“${label}”`).join(' and ')}.` };
    });
    auditAlternatives.push({ programmeId, progressionAssessment: { status: alternative.progression[0], rationale: alternative.progression[1] }, courseTraceability });
  });
  const unusedFacts = [...courseFacts.keys()].filter(code => !allSelected.has(code));
  requireCondition(!unusedFacts.length, `verified course facts contain unselected courses: ${unusedFacts.join(', ')}`);
  const unusedTrace = [...defaultTrace.keys()].filter(code => code !== 'ACCPPDE101' && !allSelected.has(code));
  requireCondition(!unusedTrace.length, `course traceability contains unselected courses: ${unusedTrace.join(', ')}`);

  requireCondition(Array.isArray(decision.candidates), 'candidate directions are required');
  const generatorOwner = new Map();
  const candidateDirections = [];
  const candidateAssessments = [];
  const candidateLabels = new Set();
  const includedCandidates = new Map();
  for (const [index, candidate] of decision.candidates.entries()) {
    requireCondition(text(candidate.label), `candidate ${index + 1} requires a label`);
    requireCondition(!candidateLabels.has(candidate.label), `candidate label ${JSON.stringify(candidate.label)} is duplicated`);
    candidateLabels.add(candidate.label);
    requireCondition(['programme-interest-cluster', 'official-structure', 'combined'].includes(candidate.basisType), `candidate ${candidate.label} has invalid basisType`);
    requireCondition(Array.isArray(candidate.generating) && Array.isArray(candidate.supporting), `candidate ${candidate.label} requires explicit interest-row groups`);
    requireCondition(new Set(candidate.generating).size === candidate.generating.length, `candidate ${candidate.label} has duplicate generating rows`);
    requireCondition(new Set(candidate.supporting).size === candidate.supporting.length, `candidate ${candidate.label} has duplicate supporting rows`);
    for (const row of [...candidate.generating, ...candidate.supporting]) requireCondition(assessedByRow.has(row), `candidate ${candidate.label} references unknown interest row ${row}`);
    for (const row of candidate.generating) {
      requireCondition(assessedByRow.get(row).constructionRole === 'generator-eligible', `candidate ${candidate.label} cannot generate from row ${row}`);
      requireCondition(!generatorOwner.has(row), `generator-eligible row ${row} has multiple construction owners`);
      generatorOwner.set(row, candidate.label);
    }
    for (const row of candidate.supporting) requireCondition(['generator-eligible', 'support-only'].includes(assessedByRow.get(row).constructionRole), `candidate ${candidate.label} cannot use ${assessedByRow.get(row).constructionRole} row ${row} as support`);
    requireCondition(!candidate.generating.some(row => candidate.supporting.includes(row)), `candidate ${candidate.label} lists an interest row as both generating and supporting`);
    const included = /^ucr-[123]$/.test(candidate.outcome);
    requireCondition(included || ['covered-by-closest-match', 'insufficient-evidence', 'not-coherent', 'not-substantively-distinct', 'not-feasible', 'maximum-reached'].includes(candidate.outcome), `candidate ${candidate.label} has invalid outcome`);
    if (included) {
      requireCondition(selectedSets.has(candidate.outcome) && candidate.outcome !== 'ucr-1', `candidate ${candidate.label} must identify an included additional alternative`);
      includedCandidates.set(candidate.outcome, (includedCandidates.get(candidate.outcome) || 0) + 1);
    }
    candidateDirections.push({
      label: candidate.label, basisType: candidate.basisType,
      generatingInterestRows: candidate.generating, supportingInterestRows: candidate.supporting,
      ...(candidate.evidence ? { evidence: expandEvidence(candidate.evidence) } : {}),
      disposition: included ? 'included' : 'rejected',
      ...(included ? { programmeId: candidate.outcome } : { rejectionReason: candidate.outcome })
    });
    candidateAssessments.push({
      candidateLabel: candidate.label,
      organisingLogic: `The explicitly supplied candidate direction is “${candidate.label}”; its interest-row basis and disposition remain explicit in interestSelection.`,
      assessment: included
        ? `The academic decision includes this candidate as ${candidate.outcome}.`
        : `The academic decision excludes this candidate for the explicit reason ${candidate.outcome}.`
    });
  }
  requireCondition(Array.isArray(decision.closestOwnedInterests), 'closestOwnedInterests must explicitly identify construction-owned generator rows');
  requireCondition(new Set(decision.closestOwnedInterests).size === decision.closestOwnedInterests.length, 'closestOwnedInterests must not contain duplicates');
  for (const row of decision.closestOwnedInterests) {
    requireCondition(assessedByRow.get(row)?.constructionRole === 'generator-eligible', `closest-match cannot own non-generator row ${row}`);
    requireCondition(!generatorOwner.has(row), `generator-eligible row ${row} has multiple construction owners`);
    generatorOwner.set(row, 'closest-match');
  }
  const generatorRows = assessedInterests.filter(item => item.constructionRole === 'generator-eligible').map(item => item.registryRow);
  const unowned = generatorRows.filter(row => !generatorOwner.has(row));
  requireCondition(!unowned.length, `generator-eligible interests lack construction ownership: ${unowned.join(', ')}`);
  for (const programmeId of [...selectedSets.keys()].slice(1)) requireCondition(includedCandidates.get(programmeId) === 1, `${programmeId} must have exactly one included candidate direction`);

  requireCondition(Array.isArray(decision.blocks) && decision.blocks.length, 'thematic block assignments are required');
  const seenCourses = new Set(); const seenComponents = new Set(); const alignment = [];
  const blocks = decision.blocks.map((tuple, blockIndex) => {
    requireCondition(Array.isArray(tuple) && tuple.length === 3 && text(tuple[1]) && Array.isArray(tuple[2]), `block ${blockIndex + 1} must be [id,title,rows]`);
    const [id, title, rows] = tuple;
    return {
      ...(id ? { id } : {}), title,
      rows: rows.map((row, rowIndex) => {
        requireCondition(Array.isArray(row) && row.length === 3, `block ${title} row ${rowIndex + 1} must explicitly state [course|null,component|null,rationale|null]`);
        const [courseCode, componentId, rationale] = row;
        requireCondition(courseCode || componentId, `block ${title} row ${rowIndex + 1} is empty`);
        const cells = {};
        if (courseCode) {
          requireCondition(allSelected.has(courseCode), `block ${title} assigns unselected course ${courseCode}`);
          requireCondition(!seenCourses.has(courseCode), `selected course ${courseCode} has more than one thematic block assignment`); seenCourses.add(courseCode);
          for (const programme of programmes.slice(1)) if (selectedSets.get(programme.id).has(courseCode)) cells[programme.id] = { text: courseFacts.get(courseCode).name, credits: courseFacts.get(courseCode).credits, courseCode };
        }
        if (componentId) {
          requireCondition(componentIds.has(componentId), `block ${title} references unknown comparator component ${componentId}`);
          requireCondition(!seenComponents.has(componentId), `comparator component ${componentId} lacks one unique explicit match status`); seenComponents.add(componentId);
          const component = components.find(item => item.id === componentId);
          cells.comparator = { text: component.name, credits: component.credits, componentId, ...(component.note ? { note: component.note } : {}) };
          const standardizedRationale = text(rationale)
            ? rationale
            : courseCode
              ? `Matched explicitly after semantic review: ${component.name} corresponds to ${courseFacts.get(courseCode).name}.`
              : `Explicitly unmatched after semantic review: no scheduled UCR course was judged a sufficiently direct counterpart to ${component.name}.`;
          alignment.push({ componentId, matchType: courseCode ? 'substantive-match' : 'unmatched', ...(courseCode ? { ucrCourseCode: courseCode } : {}), rationale: standardizedRationale });
        } else requireCondition(!rationale, `course-only row ${courseCode} must not carry a comparator rationale`);
        return { cells };
      })
    };
  });
  const omittedCourses = [...allSelected].filter(code => !seenCourses.has(code));
  requireCondition(!omittedCourses.length, `selected UCR courses lack thematic block assignments: ${omittedCourses.join(', ')}`);
  const omittedComponents = [...componentIds].filter(id => !seenComponents.has(id));
  requireCondition(!omittedComponents.length, `comparator components lack explicit matched or unmatched status: ${omittedComponents.join(', ')}`);

  requireCondition(decision.selection && text(decision.selection.stoppingReason) && text(decision.selection.assessment), 'alternative stopping decision is required');
  const finalMethodologyAudit = {
    ...(decision.routeSelection ? { comparatorRouteSelection: structuredClone(decision.routeSelection) } : {}),
    coveredByClosestMatchInterestRows: decision.closestOwnedInterests,
    candidateAssessments,
    alternatives: auditAlternatives
  };
  return {
    schemaVersion: RECORD_SCHEMA, origin: 'counselor', id: decision.id, cohort: 'Fall 2026 UCR start',
    programmeProvider: provider(registry), comparator, programmes,
    academicRationale: {
      coreField: expandedBasis.core, adjacentDirections: expandedBasis.adjacent, questionsApplications: expandedBasis.questions,
      alternatives: rationaleAlternatives,
      interestSelection: { assessedInterests, candidateDirections },
      finalMethodologyAudit
    },
    alternativeSelection: { includedCount: decision.alternatives.length, stoppingReason: decision.selection.stoppingReason, assessment: decision.selection.assessment },
    comparisonAlignment: alignment, blocks, notes: structuredClone(decision.notes || [])
  };
}

function parseArguments(argv) {
  const input = argv[0];
  requireCondition(input, 'usage: node scripts/build-counselor-comparison-v2.mjs <decision.json> [--output <comparison.json>]');
  let output;
  for (let index = 1; index < argv.length; index += 1) {
    if (argv[index] === '--output') {
      output = argv[index + 1];
      requireCondition(output, '--output requires a path');
      index += 1;
    } else fail(`unknown argument ${JSON.stringify(argv[index])}`);
  }
  return { input, output };
}

function main() {
  const { input, output } = parseArguments(process.argv.slice(2));
  const inputPath = path.resolve(input);
  requireCondition(fs.existsSync(inputPath), `decision file not found: ${inputPath}`);
  const record = compileV2(JSON.parse(fs.readFileSync(inputPath, 'utf8')), process.cwd());
  const outputPath = path.resolve(output || path.join('data', 'counselor', 'comparisons', `${record.id}.json`));
  requireCondition(!fs.existsSync(outputPath), `refusing to overwrite existing canonical comparison: ${outputPath}`);
  fs.mkdirSync(path.dirname(outputPath), { recursive: true });
  fs.writeFileSync(outputPath, `${JSON.stringify(record, null, 2)}\n`, { flag: 'wx' });
  console.log(`Built ${record.id} from ${inputPath} at ${outputPath}`);
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  try { main(); } catch (error) { console.error(error.message); process.exit(1); }
}
