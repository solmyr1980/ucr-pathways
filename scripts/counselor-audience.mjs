// Optional, progressively reviewed audience content. No academic facts are inferred.
const object = x => x && typeof x === 'object' && !Array.isArray(x);
const text = x => typeof x === 'string' && x.trim() && x.length <= 3000;
export function validateAudience(record) {
  const a = record.audience;
  if (a === undefined) return [];
  const errors = [];
  const check = (ok, message) => { if (!ok) errors.push(`audience: ${message}`); };
  if (!object(a)) return ['audience must be an object'];
  const keys = ['schemaVersion', 'programmeDescription', 'comparisonExplanation', 'curriculum', 'conceptProgrammeIds', 'noteTypes', 'componentNotes', 'cellNotes'];
  check(Object.keys(a).every(k => keys.includes(k)), 'unknown field');
  check(a.schemaVersion === '1.0', 'schemaVersion must be 1.0');
  for (const key of ['programmeDescription', 'comparisonExplanation']) if (key in a) check(text(a[key]), `${key} must be readable nonempty text (max 3000 characters)`);
  const components = record.comparator?.components || [];
  const ids = components.map(c => c.id);
  const programmes = record.programmes || [];
  const ucrIds = programmes.filter(p => p.family === 'ucr' || p.role?.startsWith('ucr-')).map(p => p.id);
  for (const [key, allowed] of [['conceptProgrammeIds', ucrIds], ['noteTypes', (record.notes || []).map(n => n.type)]]) {
    if (!(key in a)) continue;
    check(Array.isArray(a[key]) && new Set(a[key]).size === a[key].length && a[key].every(id => allowed.includes(id)), `${key} must uniquely reference existing content`);
  }
  for (const type of Array.isArray(a.noteTypes) ? a.noteTypes : []) check((record.notes || []).filter(n => n.type === type && text(n.text)).length === 1, 'noteTypes must select one unambiguous note');
  for (const id of Array.isArray(a.conceptProgrammeIds) ? a.conceptProgrammeIds : []) check((record.academicRationale?.alternatives || []).some(r => r.programmeId === id && text(r.concept)), 'concept reference needs existing canonical concept');
  if ('curriculum' in a) {
    const c = a.curriculum;
    if (!object(c)) errors.push('audience.curriculum must be an object');
    else {
      check(Object.keys(c).every(k => ['status', 'yearLabel', 'routeLabel', 'componentIds', 'limitation'].includes(k)), 'unknown curriculum field');
      check(['complete', 'partial', 'unresolved'].includes(c.status), 'invalid curriculum status');
      check(Array.isArray(c.componentIds) && new Set(c.componentIds).size === c.componentIds.length && c.componentIds.every(id => ids.includes(id)), 'componentIds must select unique existing components');
      if ('yearLabel' in c) check(typeof c.yearLabel === 'string' && /^20\d{2}[–-]20\d{2}$/.test(c.yearLabel), 'yearLabel must be a clean academic year');
      if ('routeLabel' in c) check(text(c.routeLabel) && c.routeLabel.length <= 180, 'routeLabel must be concise readable text');
      if ('limitation' in c) check(text(c.limitation), 'invalid curriculum limitation');
      if (c.status === 'complete') {
        check(record.exception?.type !== 'external-programme-unresolved', 'unresolved external basis cannot be marked complete');
        check(c.componentIds?.length === ids.length && Math.abs(components.reduce((n, x) => n + x.credits, 0) - 180) < 0.001, 'complete requires all 180 EC');
      } else if (c.status === 'partial') check(c.componentIds?.length > 0 && text(c.limitation), 'partial requires verified component IDs and explicit limitation');
      else if (c.status === 'unresolved') check(c.componentIds?.length === 0 && text(c.limitation), 'unresolved requires no displayed components and explicit limitation');
    }
  }
  if ('componentNotes' in a) check(object(a.componentNotes) && Object.entries(a.componentNotes).every(([id, note]) => ids.includes(id) && text(note)), 'componentNotes require existing component IDs and readable text');
  if ('cellNotes' in a) {
    check(Array.isArray(a.cellNotes), 'cellNotes must be an array');
    const seen = new Set();
    for (const note of Array.isArray(a.cellNotes) ? a.cellNotes : []) {
      if (!object(note)) { errors.push("audience: cell note must be an object"); continue; }
      const key = `${note.programmeId}/${note.reference}`;
      const cells = (record.blocks || []).flatMap(b => b.rows || []).map(r => r.cells?.[note.programmeId]).filter(Boolean);
      check(text(note.programmeId) && text(note.reference) && Object.keys(note).every(k => ['programmeId', 'reference', 'text'].includes(k)) && !seen.has(key) && text(note.text) && cells.some(cell => (cell.courseCode || cell.componentId || cell.elementId) === note.reference), 'cellNotes require unique stable existing cell references and readable text');
      seen.add(key);
    }
  }
  return errors;
}
export function withAudience(record, decision) {
  if (decision.audience !== undefined) record.audience = structuredClone(decision.audience);
  const errors = validateAudience(record);
  if (errors.length) throw new Error(errors.join('; '));
  return record;
}
