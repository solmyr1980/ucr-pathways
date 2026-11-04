const { test } = require('node:test');
const assert = require('node:assert/strict');
const { payload, publish } = require('./github-publication.cjs');
const parent = 'a'.repeat(40), tree = 'b'.repeat(40), blob = 'c'.repeat(40), commit = 'd'.repeat(40);
const envelope = value => ({ structuredContent: { structuredContent: value } });

test('decodes actual nested and text response formats and rejects incomplete responses', () => {
  assert.equal(payload(envelope({ sha: blob })).sha, blob);
  assert.equal(payload({ structuredContent: { content: JSON.stringify({ sha: blob }) } }).sha, blob);
  assert.equal(payload({ content: [{ type: 'text', text: JSON.stringify({ sha: blob }) }] }).sha, blob);
  assert.throws(() => payload({ structuredContent: { content: '{"sha":' } }), /invalid GitHub JSON/);
  assert.throws(() => payload({ content: [{ type: 'text', text: 'Action completed.' }] }), /structured/);
  assert.throws(() => payload({ isError: true, content: [] }), /operation failed/);
});

function fixture({ mismatch = false, advanced = false, lostUpdate = false } = {}) {
  let head = advanced ? blob : parent;
  const calls = [];
  return {
    calls,
    mcp__codex_apps__github_fetch: async ({ url }) => envelope(url.includes('/ref/')
      ? { object: { sha: head } }
      : { sha: url.endsWith(parent) ? parent : commit, tree: { sha: tree }, parents: [{ sha: parent }] }),
    mcp__codex_apps__github_create_blob: async () => { calls.push('blob'); return envelope({ sha: mismatch ? parent : blob }); },
    mcp__codex_apps__github_create_tree: async args => { calls.push('tree'); assert.equal(args.tree_elements[0].sha, blob); return envelope({ sha: tree }); },
    mcp__codex_apps__github_create_commit: async () => { calls.push('commit'); return envelope({ sha: commit }); },
    mcp__codex_apps__github_update_ref: async args => {
      calls.push('ref'); assert.equal(args.expected_sha, parent); assert.equal(args.force, false);
      head = commit;
      if (lostUpdate) throw new Error('Response lost');
      return envelope({ object: { sha: commit } });
    }
  };
}
const request = { repository: 'owner/repo', parentSha: parent, baseTreeSha: tree, message: 'test', entries: [{ path: 'data/test.json', content: 'e30K', sha: blob }] };

test('publishes verified blobs in one guarded commit', async () => {
  const tools = fixture();
  assert.equal((await publish(tools, request)).sha, commit);
  assert.deepEqual(tools.calls, ['blob', 'tree', 'commit', 'ref']);
});
test('rejects blob corruption before creating a tree or updating main', async () => {
  const tools = fixture({ mismatch: true });
  await assert.rejects(publish(tools, request), /integrity mismatch/);
  assert.deepEqual(tools.calls, ['blob']);
});
test('rejects stale parent before any write', async () => {
  const tools = fixture({ advanced: true });
  await assert.rejects(publish(tools, request), /Main advanced/);
  assert.deepEqual(tools.calls, []);
});
test('recognizes a successful ref update when its response was lost', async () => {
  const tools = fixture({ lostUpdate: true });
  assert.equal((await publish(tools, request)).sha, commit);
  assert.equal(tools.calls.filter(call => call === 'ref').length, 1);
});
