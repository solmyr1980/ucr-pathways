const { test } = require('node:test');
const assert = require('node:assert/strict');
const { guard, publish } = require('./stage2-scheduled-publication.cjs');
const options = { repository: 'owner/repo', parentSha: 'a'.repeat(40), worker: 'A', token: 'current',
  entries: [{ path: 'data/counselor/decisions/cp-000051.json' }] };
function tools(overrides = {}) {
  const claim = { worker: 'A', token: 'current', expiresAt: new Date(Date.now() + 60000).toISOString(),
    caseIds: ['cp-000051'], ...overrides };
  return { mcp__codex_apps__github_fetch_file: async () => ({ structuredContent: { content: JSON.stringify({ activeClaim: claim }) } }) };
}
test('current owner may publish only claimed cases', async () => {
  assert.equal((await guard(tools(), options)).token, 'current');
});
test('superseded owner is fenced', async () => {
  await assert.rejects(guard(tools({ token: 'replacement' }), options), /Lost or expired/);
});
test('expired owner is fenced', async () => {
  await assert.rejects(guard(tools({ expiresAt: '2000-01-01T00:00:00Z' }), options), /Lost or expired/);
});
test('other case publication is rejected', async () => {
  await assert.rejects(guard(tools(), { ...options, entries: [{ path: 'data/counselor/decisions/cp-000052.json' }] }), /outside claimed cases/);
});
test('other worker claim is protected', async () => {
  await assert.rejects(guard(tools(), { ...options, entries: [{ path: 'data/counselor/qc/stage2-scheduled-2026-11-16/B.json' }] }), /other scheduled worker/);
});
test('claim replaced during upload cannot reach the branch update', async () => {
  let replaced = false, refCalls = 0;
  const parent = 'a'.repeat(40), tree = 'b'.repeat(40), blob = 'c'.repeat(40), commit = 'd'.repeat(40);
  const envelope = x => ({ structuredContent: { content: JSON.stringify(x) } });
  const t = {
    mcp__codex_apps__github_fetch_file: async () => ({ structuredContent: { content: JSON.stringify({ activeClaim: {
      worker: 'A', token: replaced ? 'replacement' : 'current', caseIds: ['cp-000051'],
      expiresAt: new Date(Date.now() + 60000).toISOString()
    } }) } }),
    mcp__codex_apps__github_fetch: async ({ url }) => envelope(url.includes('/ref/')
      ? { object: { sha: parent } } : { tree: { sha: tree }, parents: [{ sha: parent }] }),
    mcp__codex_apps__github_create_blob: async () => envelope({ sha: blob }),
    mcp__codex_apps__github_create_tree: async () => envelope({ sha: tree }),
    mcp__codex_apps__github_create_commit: async () => { replaced = true; return envelope({ sha: commit }); },
    mcp__codex_apps__github_update_ref: async () => { refCalls++; return envelope({ sha: commit }); }
  };
  await assert.rejects(publish(t, { ...options, baseTreeSha: tree, message: 'test',
    entries: [{ ...options.entries[0], content: 'e30K', sha: blob }] }), /Lost or expired/);
  assert.equal(refCalls, 0);
});
