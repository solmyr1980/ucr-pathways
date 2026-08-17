import path from 'node:path';
import { exampleFiles, readExample, validateExample } from './example-utils.mjs';

const root = process.cwd();
const target = process.argv[2] || 'all';
let failed = false;

for (const file of exampleFiles(root, target)) {
  const example = readExample(file);
  const { errors, warnings } = validateExample(example, path.basename(file));
  warnings.forEach(message => console.warn(`WARNING: ${message}`));
  if (errors.length) {
    failed = true;
    errors.forEach(message => console.error(`ERROR: ${message}`));
  } else {
    console.log(`Valid: ${path.basename(file)}`);
  }
}

if (failed) process.exit(1);
