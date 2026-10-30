import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { stripOptionalIndependentResearch } from './optional-independent-research.mjs';

const root = process.cwd();
const validationRoot = fs.mkdtempSync(path.join(os.tmpdir(), 'ucr-counselor-validation-'));

try {
  // Only these inputs are read by the operational validators. Screenshots,
  // private records and unrelated publication assets need no temporary copy.
  for (const relative of ['scripts', 'assets/js', 'package.json', 'data/counselor/comparisons',
    'data/registry/programmes.csv', 'data/registry/programme_interests.csv']) {
    const destination = path.join(validationRoot, relative);
    fs.mkdirSync(path.dirname(destination), { recursive: true });
    fs.cpSync(path.join(root, relative), destination, { recursive: true });
  }

  const comparisonsDir = path.join(validationRoot, 'data', 'counselor', 'comparisons');
  for (const name of fs.readdirSync(comparisonsDir).filter(name => /^cp-[0-9]{6}\.json$/.test(name))) {
    const file = path.join(comparisonsDir, name);
    const record = JSON.parse(fs.readFileSync(file, 'utf8'));
    const stripped = stripOptionalIndependentResearch(record);
    fs.writeFileSync(file, `${JSON.stringify(stripped, null, 2)}\n`);
  }

  for (const script of [
    'scripts/validate-counselor-comparison.mjs',
    'scripts/validate-counselor-structural-rules.mjs',
    'scripts/validate-counselor-final-rules.mjs'
  ]) {
    execFileSync(process.execPath, [script, 'all'], { cwd: validationRoot, stdio: 'inherit' });
  }
} finally {
  fs.rmSync(validationRoot, { recursive: true, force: true });
}
