// Bounded exceptions to external completeness only. This never certifies academic truth.
const text = x => typeof x === 'string' && x.trim().length > 0;
const refs = x => Array.isArray(x) && x.length > 0 && x.every(text);
export function validateAcceptance(record) {
  const a = record.acceptance;
  if (a === undefined) return [];
  const errors = [];
  const check = (ok, message) => { if (!ok) errors.push(`acceptance: ${message}`); };
  if (!a || typeof a !== 'object' || Array.isArray(a)) return ['acceptance must be an object'];
  check(Object.keys(a).every(k => ['standard','basis','scope','claim','targetContext','reviewedOn','verifiedComponentIds','externalEvidenceRefs','ucrEvidenceRefs','challengeEvidenceRefs','challengeMethod','uncertainties'].includes(k)), 'unknown field');
  check(record.origin === 'counselor', 'counselor only');
  check(a.standard === 'bounded-materiality-2026-11-15', 'unsupported standard');
  check(['qualified-comparison', 'robust-no-match'].includes(a.basis), 'invalid basis');
  check(['documented-curriculum', 'academic-core'].includes(a.scope), 'invalid scope');
  check(text(a.claim) && text(a.targetContext) && /^\d{4}-\d{2}-\d{2}$/.test(a.reviewedOn || ''), 'claim, target context and review date required');
  const ids = (record.comparator?.components || []).map(c => c.id);
  check((record.comparator?.components || []).every(c => Number.isFinite(c.credits) && c.credits > 0) && (record.comparator?.components || []).reduce((n,c) => n+c.credits,0) <= 180, 'only supported credits up to nominal degree size may be represented');
  check(ids.length > 0 && new Set(ids).size === ids.length, 'documented components required');
  check(Array.isArray(a.verifiedComponentIds) && a.verifiedComponentIds.length === ids.length && new Set(a.verifiedComponentIds).size === ids.length && a.verifiedComponentIds.every(id => ids.includes(id)), 'verified boundary must cover exactly the stored components');
  for (const key of ['externalEvidenceRefs', 'ucrEvidenceRefs', 'challengeEvidenceRefs']) check(refs(a[key]), `${key} required`);
  check(text(a.challengeMethod), 'separately identified source-first challenge method required');
  check(Array.isArray(a.uncertainties) && a.uncertainties.length > 0, 'bounded uncertainties required');
  for (const u of Array.isArray(a.uncertainties) ? a.uncertainties : []) {
    check(text(u.fact) && refs(u.evidenceRefs), 'uncertainty fact and source evidence required');
    check(Array.isArray(u.adverseResolutions) && u.adverseResolutions.length > 0, 'adverse resolutions required');
    for (const r of u.adverseResolutions || []) check(text(r.resolution) && text(r.effectOnClaim) && r.claimSurvives === true, 'each adverse resolution must preserve the explicit claim');
  }
  const c = record.audience?.curriculum;
  const s = record.audience?.comparisonScope;
  check(c?.status === 'partial' && text(c.limitation) && c.componentIds?.length === ids.length && c.componentIds.every(id => ids.includes(id)), 'reviewed partial curriculum must select the complete verified boundary');
  check(text(record.audience?.programmeDescription) && text(record.audience?.comparisonExplanation), 'reviewed audience explanations required');
  check(s && text(s.label) && text(s.assessed) && text(s.excluded), 'visible assessed and excluded scope required');
  check(s?.label === (a.basis === 'robust-no-match' ? 'Academic no-match: documented substance' : a.scope === 'academic-core' ? 'Qualified academic-core comparison' : 'Qualified academic comparison'), 'scope label must state the acceptance boundary');
  check(Number.isFinite(s?.nominalCredits) && s.nominalCredits === 180, 'nominal external degree is 180 EC');
  if (a.basis === 'qualified-comparison') {
    check(record.recordStatus !== 'exception' && !record.exception, 'qualified comparison cannot be an exception');
    const programmes = (record.programmes || []).filter(p => p.family === 'ucr');
    check(programmes.length >= 1 && programmes.length <= 3, 'fully scheduled UCR response required');
    check(programmes.every(p => (p.schedule?.semesters || []).length === 6 && p.schedule.semesters.every(s => s.courses?.length === 4) && new Set(p.schedule.semesters.flatMap(s => s.courses.map(c => c.code))).size === 24 && p.schedule.semesters.flatMap(s => s.courses).reduce((n,c) => n + c.credits, 0) === 180), 'UCR 24-course/180-EC schedules required');
  } else check(record.recordStatus === 'exception' && record.exception?.type === 'no-defensible-ucr-match' && text(record.exception.ucrCourseEvidence), 'robust negative proof requires a no-match exception');
  return errors;
}
export function hasBoundedAcceptance(record) {
  return record.acceptance !== undefined && validateAcceptance(record).length === 0;
}
