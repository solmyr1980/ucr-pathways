import assert from 'node:assert/strict';
import fs from 'node:fs';
import { buildProductionRecord } from './build-counselor-production.mjs';
import { validateAudience } from './counselor-audience.mjs';
const read = file => JSON.parse(fs.readFileSync(file, 'utf8'));
const decision = read('data/counselor/decisions/cp-000019.json');
assert.deepEqual(buildProductionRecord(decision, process.cwd()), read('data/counselor/comparisons/cp-000019.json'));
delete decision.audience; // Explicit legacy fixture, independent of progressive case content.
const original = structuredClone(decision);
const legacy = buildProductionRecord(decision, process.cwd());
assert.equal(Object.hasOwn(legacy, 'audience'), false);
const canonicalWithoutAudience = read('data/counselor/comparisons/cp-000019.json'); delete canonicalWithoutAudience.audience;
assert.deepEqual(legacy, canonicalWithoutAudience);
const a = {
  schemaVersion: '1.0', programmeDescription: 'Study art and culture in society.',
  comparisonExplanation: 'The specialist sequences and required placement differ.',
  conceptProgrammeIds: ['ucr-1'], noteTypes: [legacy.notes[0].type],
  curriculum: {status: 'complete', componentIds: legacy.comparator.components.map(c => c.id), yearLabel: '2026–2027', routeLabel: 'Culture and Economics; minor pathway'},
  cellNotes: [{programmeId: 'comparator', reference: legacy.comparator.components[0].id, text: 'A partial curricular correspondence.'}]
};
const corrected = buildProductionRecord({...decision, audience: a}, process.cwd());
assert.deepEqual(corrected.audience, a);
const noAudience = structuredClone(corrected); delete noAudience.audience;
assert.deepEqual(noAudience, legacy); assert.deepEqual(decision, original);
function reject(mutator) {
  const record = structuredClone(corrected); mutator(record);
  assert.ok(validateAudience(record).length, 'Invalid audience content accepted');
}
reject(r => r.audience.internalFallback = true);
reject(r => r.audience.curriculum.yearLabel = 'API/cohort investigation 2261');
reject(r => r.audience.curriculum.componentIds.pop());
reject(r => r.audience.curriculum.componentIds.push('invented'));
reject(r => r.audience.conceptProgrammeIds = ['unrelated']);
reject(r => r.audience.noteTypes = ['missing-note']);
reject(r => r.audience.cellNotes[0].reference = 'invented');
reject(r => r.audience.cellNotes[0] = {programmeId:'ucr-1',text:'Unreferenced note'});
reject(r => r.audience.curriculum.status = 'partial'); // explicit limitation required
reject(r => r.audience.curriculum.status = 'unresolved'); // cannot display requirements
reject(r => r.audience.programmeDescription = '');
const unresolved = read('data/counselor/decisions/cp-000099.json');
const record = buildProductionRecord(unresolved, process.cwd());
const partial = {...unresolved, audience: {schemaVersion: '1.0', curriculum: {status: 'partial', componentIds: record.comparator.components.map(c => c.id), limitation: 'Later required study remains unverified; this is not a complete degree.'}}};
assert.equal(buildProductionRecord(partial, process.cwd()).audience.curriculum.status, 'partial');
assert.throws(() => buildProductionRecord({...partial, audience: {...partial.audience, curriculum: {...partial.audience.curriculum, status: 'complete'}}}, process.cwd()), /cannot be marked complete|complete requires/);
console.log('Audience compiler compatibility, lossless pass-through, stable references and negative contract checks passed.');

// Also runs on data-only pushes, when CI skips the R/browser suite.
const settings = read('data/counselor/presentation-overrides.json').cases;
const directory = 'data/counselor/comparisons';
for (const file of fs.readdirSync(directory).filter(name => /^cp-\d{6}\.json$/.test(name))) {
  const record = read(`${directory}/${file}`);
  const setting = settings[record.id] ?? {};
  if (record.recordStatus === 'exception' || setting.mode === 'external-only') continue;
  const qualified = record.acceptance?.basis === 'qualified-comparison';
  if (!qualified && ['partial', 'unresolved'].includes(record.audience?.curriculum?.status)) continue;
  const intro = setting.introduction;
  if (qualified || setting.mode === 'caution') {
    assert.equal(typeof intro, 'string', `${record.id}: review the material limitation before release`);
  }
  if (intro === undefined) continue;
  assert.ok(typeof intro === 'string' && intro.trim().length && !/[\r\n]/.test(intro), `${record.id}: expected one paragraph`);
  const tokens = intro.match(/\{credits\}/g) ?? [];
  assert.equal(tokens.length, qualified ? 1 : 0, `${record.id}: check the introduction against the current scope`);
  assert.doesNotMatch(intro.replace('{credits}', ''), /[{}]/, record.id);
}
console.log('Production counselor introductions cover all visible caution and qualified comparisons.');
