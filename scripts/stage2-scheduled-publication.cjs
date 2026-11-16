/* Enforce the run token at the actual branch update, including after expiry.
 * Acquisition of a new claim uses github-publication.cjs directly, on its
 * checked fresh parent. Every subsequent worker write uses this wrapper.
 */
const publication = require('./github-publication.cjs');
const claimRoot = 'data/counselor/qc/stage2-scheduled-2026-11-16';

function claimFrom(result) {
  if (result.isError) throw new Error('Cannot verify scheduled run claim');
  let value = result.structuredContent;
  if (typeof value?.content !== 'string' || !value.content) {
    throw new Error('Incomplete scheduled run claim response');
  }
  return JSON.parse(value.content).activeClaim;
}

async function guard(tools, { repository, parentSha, worker, token, entries }) {
  if (!['A', 'B'].includes(worker) || !token) throw new Error('Missing scheduled worker/token');
  const claim = claimFrom(await tools.mcp__codex_apps__github_fetch_file({
    repository_full_name: repository, path: `${claimRoot}/${worker}.json`, ref: parentSha
  }));
  if (!claim || claim.worker !== worker || claim.token !== token
      || !Number.isFinite(Date.parse(claim.expiresAt)) || Date.parse(claim.expiresAt) <= Date.now()) {
    throw new Error('Lost or expired scheduled run claim; no publication allowed');
  }
  for (const entry of entries) {
    if (entry.path.startsWith(`${claimRoot}/`) && entry.path !== `${claimRoot}/${worker}.json`) {
      throw new Error('Cannot modify the other scheduled worker claim');
    }
    const ids = entry.path.match(/cp-\d{6}/g) || [];
    if (ids.some(id => !claim.caseIds.includes(id))) {
      throw new Error(`Publication path outside claimed cases: ${entry.path}`);
    }
  }
  return claim;
}

async function publish(tools, options) {
  await guard(tools, options);
  const guarded = Object.create(tools);
  Object.defineProperty(guarded, 'mcp__codex_apps__github_update_ref', { value: async args => {
      if (args.expected_sha !== options.parentSha || args.force !== false) {
        throw new Error('Scheduled publication requires its checked parent and non-forced update');
      }
      await guard(tools, options);
      return tools.mcp__codex_apps__github_update_ref(args);
    }
  });
  return publication.publish(guarded, options);
}

module.exports = { guard, publish };
