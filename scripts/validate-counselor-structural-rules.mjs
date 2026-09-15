import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const target = process.argv[2] || 'all';
const comparisonsDir = path.join(root, 'data', 'counselor', 'comparisons');
const interestsFile = path.join(root, 'data', 'registry', 'programme_interests.csv');
const cpPattern = /^cp-[0-9]{6}$/;

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
        } else quoted = false;
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

  if (field.length || row.length) {
    row.push(field.replace(/\r$/, ''));
    rows.push(row);
  }
  if (!rows.length) return [];
  const headers = rows[0].map((value, index) => index === 0 ? value.replace(/^\uFEFF/, '') : value);
  return rows.slice(1)
    .filter(values => values.some(value => String(value).trim()))
    .map((values, index) => ({
      ...Object.fromEntries(headers.map((header, column) => [header, values[column] ?? ''])),
      __registryRow: index + 2
    }));
}

function recordFiles() {
  if (target !== 'all') {
    const id = target.toLowerCase().replace(/\.json$/i, '');
    if (!cpPattern.test(id)) throw new Error(`Invalid counselor production id: ${target}`);
    return [path.join(comparisonsDir, `${id}.json`)];
  }
  return fs.readdirSync(comparisonsDir)
    .filter(name => /^cp-[0-9]{6}\.json$/.test(name))
    .sort()
    .map(name => path.join(comparisonsDir, name));
}

function normalizeCell(cell) {
  if (!cell || typeof cell !== 'object' || Array.isArray(cell)) return null;
  if (!Object.keys(cell).length) return null;
  return cell;
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
      return null;
  }
}

const interestRows = parseCsv(fs.readFileSync(interestsFile, 'utf8'));
const interestsByProgramme = new Map();
for (const row of interestRows) {
  const id = row.counselor_programme_id;
  if (!id) continue;
  if (!interestsByProgramme.has(id)) interestsByProgramme.set(id, []);
  interestsByProgramme.get(id).push(row);
}

let failed = false;
for (const file of recordFiles()) {
  const sourceName = path.basename(file);
  const record = JSON.parse(fs.readFileSync(file, 'utf8'));
  const errors = [];
  const fail = message => errors.push(`${sourceName}: ${message}`);
  const ucrProgrammes = (record.programmes || []).filter(programme => programme?.family === 'ucr');
  const ucrIds = new Set(ucrProgrammes.map(programme => programme.id));

  // Exact UCR course identity is the only basis for sharing a row.
  const locationByCode = new Map();
  const comparisonCounts = new Map(ucrProgrammes.map(programme => [programme.id, new Map()]));
  for (const [blockIndex, block] of (record.blocks || []).entries()) {
    for (const [rowIndex, row] of (block.rows || []).entries()) {
      const codes = [];
      for (const programme of ucrProgrammes) {
        const cell = normalizeCell(row?.cells?.[programme.id]);
        if (!cell) continue;
        const code = String(cell.courseCode || '').trim();
        if (!code) continue;
        codes.push(code);
        const counts = comparisonCounts.get(programme.id);
        counts.set(code, (counts.get(code) || 0) + 1);
      }
      const uniqueCodes = [...new Set(codes)];
      if (uniqueCodes.length > 1) {
        fail(`block ${JSON.stringify(block.title)}, row ${rowIndex + 1} contains different UCR course codes (${uniqueCodes.join(', ')}); different UCR courses must occupy different rows`);
      }
      if (uniqueCodes.length === 1) {
        const code = uniqueCodes[0];
        const location = `${blockIndex}:${rowIndex}`;
        if (locationByCode.has(code) && locationByCode.get(code) !== location) {
          fail(`UCR course ${code} appears in more than one comparison row/block; every occurrence must use one canonical row and block`);
        } else locationByCode.set(code, location);
      }
    }
  }

  for (const programme of ucrProgrammes) {
    const scheduled = [];
    for (const semester of programme?.schedule?.semesters || []) {
      for (const course of semester?.courses || []) scheduled.push(String(course.code || '').trim());
    }
    const scheduledCounts = new Map();
    for (const code of scheduled) scheduledCounts.set(code, (scheduledCounts.get(code) || 0) + 1);
    for (const [code, count] of scheduledCounts) {
      if (!code) continue;
      if (count !== 1) fail(`${programme.id} schedules ${code} ${count} times; each UCR course must be unique within a programme`);
      const displayed = comparisonCounts.get(programme.id).get(code) || 0;
      if (displayed !== 1) fail(`${programme.id} must display scheduled course ${code} exactly once in the comparison; found ${displayed}`);
    }
    for (const [code, count] of comparisonCounts.get(programme.id)) {
      if (!scheduledCounts.has(code)) fail(`${programme.id} comparison contains unscheduled course ${code}`);
      if (count !== 1) fail(`${programme.id} displays ${code} ${count} times; each scheduled course must appear exactly once`);
    }
  }

  // Comparator placement is a separately audited semantic decision made after canonical UCR rows are fixed.
  const scheduledUcrCodes = new Set();
  for (const programme of ucrProgrammes) {
    for (const semester of programme?.schedule?.semesters || []) {
      for (const course of semester?.courses || []) scheduledUcrCodes.add(String(course.code || '').trim());
    }
  }

  const comparatorComponents = new Map((record?.comparator?.components || []).map(component => [component.id, component]));
  const comparatorLocation = new Map();
  for (const [blockIndex, block] of (record.blocks || []).entries()) {
    for (const [rowIndex, row] of (block.rows || []).entries()) {
      const comparatorCell = normalizeCell(row?.cells?.comparator);
      if (!comparatorCell) continue;
      const componentId = String(comparatorCell.componentId || '').trim();
      if (!componentId) continue;
      if (comparatorLocation.has(componentId)) {
        fail(`comparator component ${componentId} appears in more than one comparison row`);
        continue;
      }
      const rowCodes = new Set();
      for (const programme of ucrProgrammes) {
        const cell = normalizeCell(row?.cells?.[programme.id]);
        if (cell?.courseCode) rowCodes.add(String(cell.courseCode).trim());
      }
      if (rowCodes.size > 1) fail(`comparator component ${componentId} shares a row with multiple UCR course codes`);
      comparatorLocation.set(componentId, {
        location: `${blockIndex}:${rowIndex}`,
        ucrCourseCode: rowCodes.size === 1 ? [...rowCodes][0] : null
      });
    }
  }

  for (const componentId of comparatorComponents.keys()) {
    if (!comparatorLocation.has(componentId)) fail(`comparator component ${componentId} is missing from the comparison`);
  }
  for (const componentId of comparatorLocation.keys()) {
    if (!comparatorComponents.has(componentId)) fail(`comparison references unknown comparator component ${componentId}`);
  }

  const alignment = Array.isArray(record.comparisonAlignment) ? record.comparisonAlignment : [];
  const alignmentByComponent = new Map();
  for (const [index, item] of alignment.entries()) {
    const label = `comparisonAlignment[${index}]`;
    const componentId = String(item?.componentId || '').trim();
    if (!componentId) { fail(`${label}.componentId is required`); continue; }
    if (alignmentByComponent.has(componentId)) fail(`comparisonAlignment duplicates comparator component ${componentId}`);
    alignmentByComponent.set(componentId, item);
    if (!comparatorComponents.has(componentId)) fail(`${label} references unknown comparator component ${componentId}`);
    if (typeof item?.rationale !== 'string' || !item.rationale.trim()) fail(`${label}.rationale is required`);
    if (!['substantive-match', 'unmatched'].includes(item?.matchType)) fail(`${label}.matchType is invalid`);
    const actual = comparatorLocation.get(componentId);
    if (!actual) continue;
    if (item.matchType === 'substantive-match') {
      const code = String(item?.ucrCourseCode || '').trim();
      if (!code) fail(`${label}.ucrCourseCode is required for substantive-match`);
      else if (!scheduledUcrCodes.has(code)) fail(`${label}.ucrCourseCode ${code} is not scheduled in any UCR alternative`);
      if (actual.ucrCourseCode !== code) fail(`${componentId} declares semantic match to ${code} but is actually placed with ${actual.ucrCourseCode || 'no UCR course'}`);
    } else {
      if (item.ucrCourseCode) fail(`${label} is unmatched and must not carry ucrCourseCode`);
      if (actual.ucrCourseCode) fail(`${componentId} is declared unmatched but shares a row with ${actual.ucrCourseCode}`);
    }
  }
  for (const componentId of comparatorComponents.keys()) {
    if (!alignmentByComponent.has(componentId)) fail(`comparisonAlignment must assess comparator component ${componentId}`);
  }

  // Final labels describe the completed curriculum; the generating concept is preserved separately.
  const rationaleAlternatives = record?.academicRationale?.alternatives;
  if (!Array.isArray(rationaleAlternatives) || rationaleAlternatives.length !== ucrProgrammes.length) {
    fail('academicRationale.alternatives must align one-for-one with the included UCR alternatives');
  } else {
    rationaleAlternatives.forEach((alternative, index) => {
      const programme = ucrProgrammes[index];
      if (alternative?.programmeId !== programme?.id) fail(`academicRationale.alternatives[${index}].programmeId must be ${programme?.id}`);
      if (typeof alternative?.concept !== 'string' || !alternative.concept.trim()) fail(`academicRationale.alternatives[${index}].concept is required`);
      if (typeof programme?.label !== 'string' || !programme.label.trim()) fail(`${programme?.id || `UCR alternative ${index + 1}`} requires a visible label`);
      if (typeof alternative?.labelRationale !== 'string' || !alternative.labelRationale.trim()) fail(`academicRationale.alternatives[${index}].labelRationale is required after curriculum-based label review`);
    });
  }

  // Every linked interest is assessed; only approved relationship types may generate or support construction.
  const selection = record?.academicRationale?.interestSelection;
  const registryRows = interestsByProgramme.get(record.id) || [];
  if (!selection || typeof selection !== 'object' || Array.isArray(selection)) {
    fail('academicRationale.interestSelection is required');
  } else {
    const assessed = Array.isArray(selection.assessedInterests) ? selection.assessedInterests : [];
    const assessedByRow = new Map();
    for (const item of assessed) {
      if (!Number.isInteger(item?.registryRow)) {
        fail('every assessed interest requires integer registryRow');
        continue;
      }
      if (assessedByRow.has(item.registryRow)) fail(`interestSelection.assessedInterests duplicates registry row ${item.registryRow}`);
      assessedByRow.set(item.registryRow, item);
    }

    const expectedRows = new Map(registryRows.map(row => [row.__registryRow, row]));
    const expectedIds = [...expectedRows.keys()].sort((a, b) => a - b);
    const actualIds = [...assessedByRow.keys()].sort((a, b) => a - b);
    if (JSON.stringify(expectedIds) !== JSON.stringify(actualIds)) {
      fail(`assessedInterests must contain every programme_interests row linked to ${record.id} exactly once`);
    }

    for (const [registryRow, source] of expectedRows) {
      const item = assessedByRow.get(registryRow);
      if (!item) continue;
      const sourceExcelRow = Number(source.source_interest_excel_row);
      if (Number(item.sourceInterestExcelRow) !== sourceExcelRow) fail(`assessed interest ${registryRow} sourceInterestExcelRow does not match registry`);
      if (item.studentInterest !== source.student_interest) fail(`assessed interest ${registryRow} studentInterest does not match registry`);
      if (item.interestRelationship !== source.interest_relationship) fail(`assessed interest ${registryRow} interestRelationship does not match registry`);
      if ((item.targetMappingStatus || '') !== (source.target_mapping_status || '')) fail(`assessed interest ${registryRow} targetMappingStatus does not match registry`);
      const expectedRole = expectedConstructionRole(source);
      if (!expectedRole) fail(`registry interest ${registryRow} has unsupported relationship ${JSON.stringify(source.interest_relationship)}`);
      else if (item.constructionRole !== expectedRole) fail(`assessed interest ${registryRow} must use constructionRole ${expectedRole}`);
    }

    const candidates = Array.isArray(selection.candidateDirections) ? selection.candidateDirections : [];
    const generatedRows = new Set();
    const includedByProgramme = new Map();
    const candidateLabels = new Set();
    for (const [index, candidate] of candidates.entries()) {
      const label = `interestSelection.candidateDirections[${index}]`;
      if (typeof candidate?.label !== 'string' || !candidate.label.trim()) fail(`${label}.label is required`);
      else if (candidateLabels.has(candidate.label)) fail('candidate direction labels must be unique');
      else candidateLabels.add(candidate.label);
      if (!['programme-interest-cluster', 'official-structure', 'combined'].includes(candidate?.basisType)) fail(`${label}.basisType is invalid`);
      const generating = Array.isArray(candidate?.generatingInterestRows) ? candidate.generatingInterestRows : [];
      const supporting = Array.isArray(candidate?.supportingInterestRows) ? candidate.supportingInterestRows : [];
      if (new Set(generating).size !== generating.length) fail(`${label}.generatingInterestRows must be unique`);
      if (new Set(supporting).size !== supporting.length) fail(`${label}.supportingInterestRows must be unique`);
      if (candidate?.basisType === 'programme-interest-cluster' && generating.length === 0) fail(`${label} requires at least one generating interest`);
      for (const rowId of generating) {
        const item = assessedByRow.get(rowId);
        if (!item) fail(`${label} references unassessed generating interest row ${rowId}`);
        else if (item.constructionRole !== 'generator-eligible') fail(`${label} cannot use ${item.constructionRole} row ${rowId} as a generating interest`);
        generatedRows.add(rowId);
      }
      for (const rowId of supporting) {
        const item = assessedByRow.get(rowId);
        if (!item) fail(`${label} references unassessed supporting interest row ${rowId}`);
        else if (!['generator-eligible', 'support-only'].includes(item.constructionRole)) fail(`${label} cannot use ${item.constructionRole} row ${rowId} as construction support`);
        if (generating.includes(rowId)) fail(`${label} lists row ${rowId} as both generating and supporting`);
      }
      if (!['included', 'rejected'].includes(candidate?.disposition)) fail(`${label}.disposition must be included or rejected`);
      if (candidate?.disposition === 'included') {
        if (!ucrIds.has(candidate.programmeId) || candidate.programmeId === ucrProgrammes[0]?.id) fail(`${label}.programmeId must identify an included additional UCR alternative`);
        else includedByProgramme.set(candidate.programmeId, (includedByProgramme.get(candidate.programmeId) || 0) + 1);
        if (candidate.rejectionReason) fail(`${label} is included and must not carry rejectionReason`);
      } else {
        const allowed = ['covered-by-closest-match', 'insufficient-evidence', 'not-coherent', 'not-substantively-distinct', 'not-feasible', 'maximum-reached'];
        if (!allowed.includes(candidate?.rejectionReason)) fail(`${label}.rejectionReason is required and invalid`);
        if (candidate.programmeId) fail(`${label} is rejected and must not carry programmeId`);
      }
    }

    for (const item of assessed) {
      if (item.constructionRole === 'generator-eligible' && !generatedRows.has(item.registryRow)) {
        fail(`generator-eligible interest row ${item.registryRow} was not assessed within any candidate direction`);
      }
    }
    for (const programme of ucrProgrammes.slice(1)) {
      if ((includedByProgramme.get(programme.id) || 0) !== 1) fail(`${programme.id} must have exactly one included candidate direction in interestSelection`);
    }
  }

  if (errors.length) {
    failed = true;
    errors.forEach(error => console.error(error));
  } else console.log(`${sourceName}: structural production rules OK`);
}

if (failed) process.exit(1);
