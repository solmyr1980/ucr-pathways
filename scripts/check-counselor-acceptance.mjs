import fs from 'node:fs';
import {validateAcceptance} from './counselor-acceptance.mjs';
const record = JSON.parse(fs.readFileSync(0, 'utf8'));
const errors = validateAcceptance(record);
if (errors.length) { console.error(errors.join('\n')); process.exit(1); }
