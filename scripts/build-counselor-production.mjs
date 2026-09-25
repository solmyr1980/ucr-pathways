import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { compileV2 } from './build-counselor-comparison-v2.mjs';
import { applyOptionalIndependentResearch } from './optional-independent-research.mjs';

function fail(message) { throw new Error(`Counselor production build failed: ${message}`); }

function parseArguments(argv) {
  const input = argv[0];
  if (!input) fail('usage: node scripts/build-counselor-production.mjs <decision.json> [--output <comparison.json>]');
  let output;
  for (let index = 1; index < argv.length; index += 1) {
    if (argv[index] === '--output') {
      output = argv[index + 1];
      if (!output) fail('--output requires a path');
      index += 1;
    } else fail(`unknown argument ${JSON.stringify(argv[index])}`);
  }
  return { input, output };
}

export function buildProductionRecord(decision, repositoryRoot) {
  if (decision.recordStatus === 'exception') return compileV2(decision, repositoryRoot);
  if (!Object.hasOwn(decision, 'researchComponentId')) {
    fail('researchComponentId must be supplied explicitly as a comparator component ID or null');
  }
  const record = compileV2(decision, repositoryRoot);
  return applyOptionalIndependentResearch(record, decision.researchComponentId);
}

function main() {
  const { input, output } = parseArguments(process.argv.slice(2));
  const inputPath = path.resolve(input);
  if (!fs.existsSync(inputPath)) fail(`decision file not found: ${inputPath}`);
  const decision = JSON.parse(fs.readFileSync(inputPath, 'utf8'));
  const record = buildProductionRecord(decision, process.cwd());
  const outputPath = path.resolve(output || path.join('data', 'counselor', 'comparisons', `${record.id}.json`));
  if (fs.existsSync(outputPath)) fail(`refusing to overwrite existing canonical comparison: ${outputPath}`);
  fs.mkdirSync(path.dirname(outputPath), { recursive: true });
  fs.writeFileSync(outputPath, `${JSON.stringify(record, null, 2)}\n`, { flag: 'wx' });
  console.log(`Built ${record.id} counselor ${record.recordStatus || 'comparison'} record at ${outputPath}`);
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  try { main(); } catch (error) { console.error(error.message); process.exit(1); }
}
