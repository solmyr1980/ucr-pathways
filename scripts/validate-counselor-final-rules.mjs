import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const target = process.argv[2] || 'all';
const comparisonsDir = path.join(root, 'data', 'counselor', 'comparisons');
const cpPattern = /^cp-[0-9]{6}$/;
const ppdCode = 'ACCPPDE101';
const legacyPendingReaudit = new Set();
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

let failed = false;
for (const file of recordFiles()) {
  const sourceName = path.basename(file);
  const record = JSON.parse(fs.readFileSync(file, 'utf8'));
  const errors = [];
  const fail = message => errors.push(`${sourceName}: ${message}`);
  const rationale = record?.academicRationale;
  const audit = rationale?.finalMethodologyAudit;

  if (legacyPendingReaudit.has(record.id) && !audit) {
    console.warn(`WARNING: ${sourceName}: legacy pre-final-methodology record; final-rule audit deferred until the four-case re-audit phase`);
    continue;
  }

  if (!audit || typeof audit !== 'object' || Array.isArray(audit)) {
    fail('academicRationale.finalMethodologyAudit is required for every new or re-audited counselor record');
  } else {
    const comparator = record?.comparator || {};
    const routeAudit = audit.comparatorRouteSelection;
    if (nonEmptyString(comparator.route)) {
      if (!routeAudit || typeof routeAudit !== 'object' || Array.isArray(routeAudit)) {
        fail('finalMethodologyAudit.comparatorRouteSelection is required when comparator.route is set');
      } else {
        if (routeAudit.route !== comparator.route) fail('comparatorRouteSelection.route must equal comparator.route');
        if (!routeRules.has(routeAudit.selectionRule)) fail('comparatorRouteSelection.selectionRule must use an approved neutral route-selection rule');
        if (!nonEmptyString(routeAudit.basis)) fail('comparatorRouteSelection.basis is required');
      }
    } else if (routeAudit) {
      fail('comparatorRouteSelection must not be present when comparator.route is absent');
    }

    const mapLabels = new Set();
    for (const field of ['coreField', 'adjacentDirections', 'questionsApplications']) {
      for (const item of Array.isArray(rationale?.[field]) ? rationale[field] : []) {
        if (nonEmptyString(item?.label)) mapLabels.add(item.label.trim());
      }
    }

    const ucrProgrammes = (record.programmes || []).filter(programme => programme?.family === 'ucr');
    const rationaleAlternatives = Array.isArray(rationale?.alternatives) ? rationale.alternatives : [];
    const rationaleByProgramme = new Map(rationaleAlternatives.map(item => [item?.programmeId, item]));
    const programmeById = new Map(ucrProgrammes.map(programme => [programme.id, programme]));
    const alternativeAudits = Array.isArray(audit.alternatives) ? audit.alternatives : [];
    const auditByProgramme = new Map();

    for (const [index, alternativeAudit] of alternativeAudits.entries()) {
      const label = `finalMethodologyAudit.alternatives[${index}]`;
      const programmeId = String(alternativeAudit?.programmeId || '').trim();
      if (!programmeId) {
        fail(`${label}.programmeId is required`);
        continue;
      }
      if (auditByProgramme.has(programmeId)) fail(`finalMethodologyAudit.alternatives duplicates programmeId ${programmeId}`);
      auditByProgramme.set(programmeId, alternativeAudit);
      if (!programmeById.has(programmeId)) fail(`${label}.programmeId ${programmeId} is not an included UCR programme`);
    }

    for (const programme of ucrProgrammes) {
      const alternativeAudit = auditByProgramme.get(programme.id);
      const rationaleAlternative = rationaleByProgramme.get(programme.id);
      const label = `finalMethodologyAudit alternative ${programme.id}`;
      if (!alternativeAudit) {
        fail(`${label} is required`);
        continue;
      }
      if (!rationaleAlternative) {
        fail(`${programme.id} has no matching academicRationale.alternatives entry`);
        continue;
      }

      const scheduled = scheduledCourseCodes(programme).filter(code => code !== ppdCode);
      const expectedCodes = new Set(scheduled);
      const trace = Array.isArray(alternativeAudit.courseTraceability) ? alternativeAudit.courseTraceability : null;
      if (!trace) {
        fail(`${label}.courseTraceability is required`);
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
              if (!Array.isArray(rationaleAlternative?.basisLabels) || !rationaleAlternative.basisLabels.includes(basis)) {
                fail(`${entryLabel} basis label ${JSON.stringify(basis)} is not part of ${programme.id}'s evidence-map basis`);
              }
            }
          }
          if (!nonEmptyString(entry?.rationale)) fail(`${entryLabel}.rationale is required`);
        }
        for (const code of expectedCodes) {
          if (!traceByCode.has(code)) fail(`${label}.courseTraceability must explain scheduled non-PPD course ${code}`);
        }
        if (trace.length !== expectedCodes.size) {
          fail(`${label}.courseTraceability must contain exactly one entry for each of the ${expectedCodes.size} scheduled non-PPD courses`);
        }
      }

      const progression = alternativeAudit.progressionAssessment;
      if (!progression || typeof progression !== 'object' || Array.isArray(progression)) {
        fail(`${label}.progressionAssessment is required`);
      } else {
        if (progression.status !== 'passed') fail(`${label}.progressionAssessment.status must be "passed"`);
        if (!nonEmptyString(progression.rationale)) fail(`${label}.progressionAssessment.rationale is required`);
      }
    }

    if (alternativeAudits.length !== ucrProgrammes.length) {
      fail(`finalMethodologyAudit.alternatives must contain exactly one audit for each of the ${ucrProgrammes.length} included UCR alternatives`);
    }

    const selection = rationale?.interestSelection;
    if (!selection || typeof selection !== 'object' || Array.isArray(selection)) {
      fail('academicRationale.interestSelection is required');
    } else {
      const assessed = Array.isArray(selection.assessedInterests) ? selection.assessedInterests : [];
      const assessedByRow = new Map(assessed.filter(item => Number.isInteger(item?.registryRow)).map(item => [item.registryRow, item]));
      const generatorRows = new Set(assessed.filter(item => item?.constructionRole === 'generator-eligible').map(item => item.registryRow));
      const coverageCounts = new Map([...generatorRows].map(row => [row, 0]));

      const covered = Array.isArray(audit.coveredByClosestMatchInterestRows)
        ? audit.coveredByClosestMatchInterestRows
        : null;
      if (!covered) {
        fail('finalMethodologyAudit.coveredByClosestMatchInterestRows is required');
      } else {
        if (new Set(covered).size !== covered.length) fail('finalMethodologyAudit.coveredByClosestMatchInterestRows must be unique');
        for (const row of covered) {
          const item = assessedByRow.get(row);
          if (!item) fail(`coveredByClosestMatchInterestRows references unassessed row ${row}`);
          else if (item.constructionRole !== 'generator-eligible') fail(`coveredByClosestMatchInterestRows may contain only generator-eligible rows; row ${row} is ${item.constructionRole}`);
          else coverageCounts.set(row, (coverageCounts.get(row) || 0) + 1);
        }
      }

      const candidates = Array.isArray(selection.candidateDirections) ? selection.candidateDirections : [];
      const candidateLabels = new Set(candidates.map(candidate => candidate?.label).filter(nonEmptyString));
      const candidateAssessments = Array.isArray(audit.candidateAssessments) ? audit.candidateAssessments : [];
      const assessmentByLabel = new Map();
      for (const [index, candidateAudit] of candidateAssessments.entries()) {
        const label = `finalMethodologyAudit.candidateAssessments[${index}]`;
        const candidateLabel = String(candidateAudit?.candidateLabel || '').trim();
        if (!candidateLabel) {
          fail(`${label}.candidateLabel is required`);
          continue;
        }
        if (assessmentByLabel.has(candidateLabel)) fail(`finalMethodologyAudit.candidateAssessments duplicates candidate ${JSON.stringify(candidateLabel)}`);
        assessmentByLabel.set(candidateLabel, candidateAudit);
        if (!candidateLabels.has(candidateLabel)) fail(`${label} references unknown candidate direction ${JSON.stringify(candidateLabel)}`);
        if (!nonEmptyString(candidateAudit?.organisingLogic)) fail(`${label}.organisingLogic is required`);
        if (!nonEmptyString(candidateAudit?.assessment)) fail(`${label}.assessment is required`);
      }

      for (const candidate of candidates) {
        const candidateLabel = String(candidate?.label || '').trim();
        if (candidateLabel && catchAllLabelPattern.test(candidateLabel)) {
          fail(`candidate direction ${JSON.stringify(candidateLabel)} appears to be an omnibus residual category; use a specific coherent academic direction instead`);
        }
        if (candidateLabel && !assessmentByLabel.has(candidateLabel)) {
          fail(`finalMethodologyAudit.candidateAssessments must assess candidate direction ${JSON.stringify(candidateLabel)}`);
        }
        for (const row of Array.isArray(candidate?.generatingInterestRows) ? candidate.generatingInterestRows : []) {
          const item = assessedByRow.get(row);
          if (item?.constructionRole === 'generator-eligible') coverageCounts.set(row, (coverageCounts.get(row) || 0) + 1);
        }
      }
      if (candidateAssessments.length !== candidateLabels.size) {
        fail('finalMethodologyAudit.candidateAssessments must contain exactly one audit for every candidate direction');
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
