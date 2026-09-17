import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { stripOptionalIndependentResearch } from './optional-independent-research.mjs';

const root = process.cwd();
const validationRoot = fs.mkdtempSync(path.join(os.tmpdir(), 'ucr-counselor-validation-'));

try {
  fs.cpSync(root, validationRoot, {
    recursive: true,
    filter: source => !source.includes(`${path.sep}.git${path.sep}`) && !source.endsWith(`${path.sep}.git`)
  });

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
