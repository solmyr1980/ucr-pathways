/* Load with require in Node, or evaluate with a CommonJS module in Work code mode.
 * Read full files from a Git checkout verified against parentSha. Pass their
 * base64 bytes and git hash-object SHA. Large files never pass through chat text.
 */
function payload(result) {
  let value = result;
  for (let depth = 0; depth < 8; depth += 1) {
    if (!value || typeof value !== 'object') break;
    if (value.isError || value.error || value.status === 'ERROR') {
      throw new Error(`GitHub operation failed: ${JSON.stringify(value.error || value.content || value)}`);
    }
    if (value.structuredContent) {
      value = value.structuredContent;
      continue;
    }
    if (value.sha || value.object || value.tree) return value;
    if (typeof value.content === 'string') {
      try { value = JSON.parse(value.content); }
      catch { throw new Error('Incomplete or invalid GitHub JSON response'); }
      continue;
    }
    if (Array.isArray(value.content)) {
      const text = value.content.filter(item => item.type === 'text').map(item => item.text).join('\n');
      try { value = JSON.parse(text); }
      catch { throw new Error('Missing or invalid structured GitHub response'); }
      continue;
    }
    break;
  }
  throw new Error('GitHub response has no usable object or SHA');
}

async function prepareEntries(tools, root, entries) {
  const quote = value => `'${String(value).replace(/'/g, "'\\''")}'`;
  const chunkSize = 786432; // Divisible by three, so base64 chunks concatenate exactly.
  const program = 'import base64,hashlib,pathlib,sys; b=pathlib.Path(sys.argv[1]).read_bytes(); actual=hashlib.sha1(b"blob "+str(len(b)).encode()+b"\\0"+b).hexdigest(); assert actual==sys.argv[4], "Local blob changed"; start=int(sys.argv[2]); size=int(sys.argv[3]); print(base64.b64encode(b[start:start+size]).decode(),end="")';
  const prepared = [];
  for (const entry of entries) {
    if (!entry.path || entry.path.startsWith('/') || entry.path.split('/').includes('..') || !Number.isSafeInteger(entry.size) || entry.size < 1) {
      throw new Error(`Invalid local file descriptor: ${entry.path}`);
    }
    const chunks = [];
    for (let offset = 0; offset < entry.size; offset += chunkSize) {
      const result = await tools.exec_command({
        cmd: `python3 -c ${quote(program)} ${quote(entry.path)} ${offset} ${chunkSize} ${quote(entry.sha)}`,
        workdir: root, max_output_tokens: 600000
      });
      const expected = 4 * Math.ceil(Math.min(chunkSize, entry.size - offset) / 3);
      if (result.exit_code !== 0 || result.output?.length !== expected || !/^[A-Za-z0-9+/]*={0,2}$/.test(result.output)) {
        throw new Error(`Incomplete or invalid local byte transfer: ${entry.path}`);
      }
      chunks.push(result.output);
    }
    prepared.push({ ...entry, content: chunks.join('') });
  }
  return prepared;
}

async function publish(tools, { repository, parentSha, baseTreeSha, entries, message }) {
  if (!/^[a-f0-9]{40}$/.test(parentSha) || !/^[a-f0-9]{40}$/.test(baseTreeSha)) {
    throw new Error('Publication requires verified parent and base tree SHAs');
  }
  const paths = new Set();
  for (const entry of entries) {
    if (!entry.path || entry.path.startsWith('/') || entry.path.split('/').includes('..') || paths.has(entry.path)) {
      throw new Error(`Invalid or duplicate publication path: ${entry.path}`);
    }
    paths.add(entry.path);
    if (!/^[a-f0-9]{40}$/.test(entry.sha) || typeof entry.content !== 'string' || !entry.content) {
      throw new Error(`Missing verified file bytes or blob SHA: ${entry.path}`);
    }
  }
  if (!entries.length) throw new Error('No publication entries');
  const head = async () => payload(await tools.mcp__codex_apps__github_fetch({
    url: `https://api.github.com/repos/${repository}/git/ref/heads/main`
  })).object?.sha;
  if (await head() !== parentSha) throw new Error('Main advanced; refresh, merge own delta and revalidate');
  const base = payload(await tools.mcp__codex_apps__github_fetch({
    url: `https://api.github.com/repos/${repository}/git/commits/${parentSha}`
  }));
  if (base.tree?.sha !== baseTreeSha) throw new Error('Base tree does not belong to the verified parent');
  const elements = [];
  for (const entry of entries) {
    const blob = payload(await tools.mcp__codex_apps__github_create_blob({
      repository_full_name: repository, content: entry.content, encoding: 'base64'
    }));
    if (blob.sha !== entry.sha) throw new Error(`Blob integrity mismatch: ${entry.path}`);
    elements.push({ path: entry.path, mode: '100644', type: 'blob', sha: blob.sha });
  }
  const tree = payload(await tools.mcp__codex_apps__github_create_tree({
    repository_full_name: repository, base_tree_sha: baseTreeSha, tree_elements: elements
  }));
  const commit = payload(await tools.mcp__codex_apps__github_create_commit({
    repository_full_name: repository, parent_sha: parentSha, tree_sha: tree.sha, message
  }));
  const stored = payload(await tools.mcp__codex_apps__github_fetch({
    url: `https://api.github.com/repos/${repository}/git/commits/${commit.sha}`
  }));
  if (stored.tree?.sha !== tree.sha || stored.parents?.length !== 1 || stored.parents[0].sha !== parentSha) {
    throw new Error('Created commit failed tree/parent verification');
  }
  try {
    payload(await tools.mcp__codex_apps__github_update_ref({
      repository_full_name: repository, branch_name: 'main', sha: commit.sha,
      expected_sha: parentSha, force: false
    }));
  } catch (error) {
    // A lost response may follow a successful update. Inspect before retrying.
    if (await head() !== commit.sha) throw error;
  }
  if (await head() !== commit.sha) throw new Error(`Verify publication at ${commit.sha}; main has since advanced`);
  return { sha: commit.sha, treeSha: tree.sha, paths: [...paths] };
}

module.exports = { payload, prepareEntries, publish };
