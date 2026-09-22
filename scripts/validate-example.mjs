import fs from 'node:fs';
import path from 'node:path';
import { isDeepStrictEqual } from 'node:util';
import { exampleFiles, readExample, validateExample } from './example-utils.mjs';

const root = process.cwd();
const args = process.argv.slice(2);
const explicitFile = args[0] === '--file';
if (explicitFile && args.length !== 2) {
  throw new Error('Use --file with exactly one student-record JSON path.');
}
const target = explicitFile ? null : (args[0] || 'all');
const files = explicitFile ? [path.resolve(args[1])] : exampleFiles(root, target);
let failed = false;

function legacyFixtureOptions(example) {
  if (example?.origin !== 'student' || !/^p-00[1-5]$/.test(String(example?.id || ''))) return {};
  const fixturePath = path.join(root, 'data', 'examples', `${example.id}.json`);
  if (!fs.existsSync(fixturePath)) return {};
  const fixture = readExample(fixturePath);
  const privateCore = structuredClone(example);
  const publicCore = structuredClone(fixture);
  delete privateCore.origin;
  delete privateCore.interestInterpretation;
  delete publicCore.origin;
  delete publicCore.interestInterpretation;
  if (!isDeepStrictEqual(privateCore, publicCore)) return {};
  return { strictDistinctness: false, retainedLegacyFixture: true };
}

for (const file of files) {
  const example = readExample(file);
  const options = explicitFile ? legacyFixtureOptions(example) : {};
  const { errors, warnings } = validateExample(example, path.basename(file), options);
  if (options.retainedLegacyFixture) {
    warnings.unshift(`${path.basename(file)}: unchanged retained p-001–p-005 fixture; current distinctness floor is advisory for this legacy record only`);
  }
  warnings.forEach(message => console.warn(`WARNING: ${message}`));
  if (errors.length) {
    failed = true;
    errors.forEach(message => console.error(`ERROR: ${message}`));
  } else {
    console.log(`Valid: ${path.basename(file)}`);
  }
}

if (failed) process.exit(1);
