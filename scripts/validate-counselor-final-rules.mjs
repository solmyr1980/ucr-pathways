import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const target = process.argv[2] || 'all';
const comparisonsDir = path.join(root, 'data', 'counselor', 'comparisons');
const cpPattern = /^cp-[0-9]{6}$/;
const ppdCode = 'ACCPPDE101';
const legacyPendingReaudit = new Set(['cp-000001', 'cp-000002', 'cp-000003', 'cp-000004']);
const routeRules = new Set([
  'target-named',
  'broad-academic-identity',
  'least-specialized-general',
  'official-order-tiebreak'
]);
const catchAllLabelPattern = /\b(other eligible|remaining interests?|residual interests?|miscellaneous interests?|other programme-interest directions?)\b/i;

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

function nonEmptyString(value) {
  return typeof value === 'string' && value.trim().length > 0;
}

function scheduledCourseCodes(programme) {
  const codes = [];
  for (const semester of programme?.schedule?.semesters || []) {
    for (const course of semester?.courses || []) {
      const code = String(course?.code || '').trim();
      if (code) codes.push(code);
    }
  }
  return codes;
}

function hasAnyFinalMethodologyFields(record) {
  const selection = record?.academicRationale?.interestSelection;
  const alternatives = Array.isArray(record?.academicRationale?.alternatives)
    ? record.academicRationale.alternatives
    : [];
  return Object.hasOwn(selection || {}, 'coveredByClosestMatchInterestRows') ||
    alternatives.some(alternative =>
      Object.hasOwn(alternative || {}, 'courseTraceability') ||
      Object.hasOwn(alternative || {}, 'progressionAssessment')
    ) ||
    (Array.isArray(selection?.candidateDirections) && selection.candidateDirections.some(candidate =>
      Object.hasOwn(candidate || {}, 'organisingLogic') || Object.hasOwn(candidate || {}, 'assessment')
    )) ||
    Object.hasOwn(record?.comparator || {}, 'routeSelectionRule') ||
    Object.hasOwn(record?.comparator || {}, 'routeSelectionBasis');
}

let failed = false;
for (const file of recordFiles()) {
  const sourceName = path.basename(file);
  const record = JSON.parse(fs.readFileSync(file, 'utf8'));
  const errors = [];
  const fail = message => errors.push(`${sourceName}: ${message}`);

  if (legacyPendingReaudit.has(record.id) && !hasAnyFinalMethodologyFields(record)) {
    console.warn(`WARNING: ${sourceName}: legacy pre-final-methodology record; final-rule audit deferred until the four-case re-audit phase`);
    continue;
  }

  const comparator = record?.comparator || {};
  if (nonEmptyString(comparator.route)) {
    if (!routeRules.has(comparator.routeSelectionRule)) {
      fail('comparator.routeSelectionRule is required when comparator.route is set and must use an approved neutral route-selection rule');
    }
    if (!nonEmptyString(comparator.routeSelectionBasis)) {
      fail('comparator.routeSelectionBasis is required when comparator.route is set');
    }
  } else if (comparator.routeSelectionRule || comparator.routeSelectionBasis) {
    fail('comparator route-selection metadata must not be present without comparator.route');
  }

  const rationale = record?.academicRationale;
  if (!rationale || typeof rationale !== 'object' || Array.isArray(rationale)) {
    fail('academicRationale is required');
  } else {
    const mapLabels = new Set();
    for (const field of ['coreField', 'adjacentDirections', 'questionsApplications']) {
      for (const item of Array.isArray(rationale[field]) ? rationale[field] : []) {
        if (nonEmptyString(item?.label)) mapLabels.add(item.label.trim());
      }
    }

    const ucrProgrammes = (record.programmes || []).filter(programme => programme?.family === 'ucr');
    const programmesById = new Map(ucrProgrammes.map(programme => [programme.id, programme]));
    const alternatives = Array.isArray(rationale.alternatives) ? rationale.alternatives : [];

    for (const [index, alternative] of alternatives.entries()) {
      const label = `academicRationale.alternatives[${index}]`;
      const programme = programmesById.get(alternative?.programmeId);
      if (!programme) {
        fail(`${label}.programmeId does not identify an included UCR programme`);
        continue;
      }

      const scheduled = scheduledCourseCodes(programme).filter(code => code !== ppdCode);
      const expectedCodes = new Set(scheduled);
      const trace = Array.isArray(alternative?.courseTraceability) ? alternative.courseTraceability : null;
      if (!trace) {
        fail(`${label}.courseTraceability is required under the final methodology`);
      } else {
        const traceByCode = new Map();
        for (const [traceIndex, entry] of trace.entries()) {
          const entryLabel = `${label}.courseTraceability[${traceIndex}]`;
          const code = String(entry?.courseCode || '').trim();
          if (!code) {
            fail(`${entryLabel}.courseCode is required`);
            continue;
          }
          if (code === ppdCode) fail(`${entryLabel} must not trace mandatory ${ppdCode}`);
          if (traceByCode.has(code)) fail(`${label}.courseTraceability duplicates ${code}`);
          traceByCode.set(code, entry);
          if (!expectedCodes.has(code)) fail(`${entryLabel} references ${code}, which is not a scheduled non-PPD course in ${programme.id}`);
          if (!Array.isArray(entry?.basisLabels) || entry.basisLabels.length === 0) {
            fail(`${entryLabel}.basisLabels must contain at least one evidence-map item`);
          } else {
            if (new Set(entry.basisLabels).size !== entry.basisLabels.length) fail(`${entryLabel}.basisLabels must be unique`);
            for (const basis of entry.basisLabels) {
              if (!mapLabels.has(basis)) fail(`${entryLabel} basis label ${JSON.stringify(basis)} is not present in the academic interest map`);
              if (!Array.isArray(alternative?.basisLabels) || !alternative.basisLabels.includes(basis)) {
                fail(`${entryLabel} basis label ${JSON.stringify(basis)} is not part of the alternative's evidence-map basis`);
              }
            }
          }
          if (!nonEmptyString(entry?.rationale)) fail(`${entryLabel}.rationale is required`);
        }
        for (const code of expectedCodes) {
          if (!traceByCode.has(code)) fail(`${label}.courseTraceability must explain scheduled non-PPD course ${code}`);
        }
        for (const code of traceByCode.keys()) {
          if (!expectedCodes.has(code)) continue;
        }
        if (trace.length !== expectedCodes.size) {
          fail(`${label}.courseTraceability must contain exactly one entry for each of the ${expectedCodes.size} scheduled non-PPD courses`);
        }
      }

      const progression = alternative?.progressionAssessment;
      if (!progression || typeof progression !== 'object' || Array.isArray(progression)) {
        fail(`${label}.progressionAssessment is required under the final methodology`);
      } else {
        if (progression.status !== 'passed') fail(`${label}.progressionAssessment.status must be "passed"`);
        if (!nonEmptyString(progression.rationale)) fail(`${label}.progressionAssessment.rationale is required`);
      }
    }

    const selection = rationale.interestSelection;
    if (!selection || typeof selection !== 'object' || Array.isArray(selection)) {
      fail('academicRationale.interestSelection is required');
    } else {
      const assessed = Array.isArray(selection.assessedInterests) ? selection.assessedInterests : [];
      const assessedByRow = new Map(assessed.filter(item => Number.isInteger(item?.registryRow)).map(item => [item.registryRow, item]));
      const generatorRows = new Set(assessed.filter(item => item?.constructionRole === 'generator-eligible').map(item => item.registryRow));

      const covered = Array.isArray(selection.coveredByClosestMatchInterestRows)
        ? selection.coveredByClosestMatchInterestRows
        : null;
      const coverageCounts = new Map([...generatorRows].map(row => [row, 0]));
      if (!covered) {
        fail('interestSelection.coveredByClosestMatchInterestRows is required under the final methodology');
      } else {
        if (new Set(covered).size !== covered.length) fail('interestSelection.coveredByClosestMatchInterestRows must be unique');
        for (const row of covered) {
          const item = assessedByRow.get(row);
          if (!item) fail(`coveredByClosestMatchInterestRows references unassessed row ${row}`);
          else if (item.constructionRole !== 'generator-eligible') fail(`coveredByClosestMatchInterestRows may contain only generator-eligible rows; row ${row} is ${item.constructionRole}`);
          else coverageCounts.set(row, (coverageCounts.get(row) || 0) + 1);
        }
      }

      const candidates = Array.isArray(selection.candidateDirections) ? selection.candidateDirections : [];
      for (const [index, candidate] of candidates.entries()) {
        const candidateLabel = `interestSelection.candidateDirections[${index}]`;
        if (!nonEmptyString(candidate?.organisingLogic)) fail(`${candidateLabel}.organisingLogic is required`);
        if (!nonEmptyString(candidate?.assessment)) fail(`${candidateLabel}.assessment is required`);
        if (nonEmptyString(candidate?.label) && catchAllLabelPattern.test(candidate.label)) {
          fail(`${candidateLabel}.label appears to be an omnibus residual category; use a specific coherent academic direction instead`);
        }
        const generating = Array.isArray(candidate?.generatingInterestRows) ? candidate.generatingInterestRows : [];
        for (const row of generating) {
          const item = assessedByRow.get(row);
          if (item?.constructionRole === 'generator-eligible') coverageCounts.set(row, (coverageCounts.get(row) || 0) + 1);
        }
      }

      for (const row of generatorRows) {
        const count = coverageCounts.get(row) || 0;
        if (count === 0) fail(`generator-eligible interest row ${row} is neither covered by the closest-match core nor assigned to a coherent candidate direction`);
        if (count > 1) fail(`generator-eligible interest row ${row} is construction-owned ${count} times; it must be accounted for exactly once`);
      }
    }
  }

  if (errors.length) {
    failed = true;
    errors.forEach(error => console.error(error));
  } else {
    console.log(`${sourceName}: final counselor methodology rules OK`);
  }
}

if (failed) process.exit(1);
