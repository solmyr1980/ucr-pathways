import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const dir = path.join(root, 'data', 'examples');
const roleToKind = new Map([
  ['ucr-depth', 'closest-match'],
  ['ucr-balanced', 'related-direction'],
  ['ucr-thematic', 'question-led']
]);

let changed = 0;

for (const name of fs.readdirSync(dir).filter(name => name.endsWith('.json')).sort()) {
  const file = path.join(dir, name);
  const record = JSON.parse(fs.readFileSync(file, 'utf8'));
  let dirty = false;

  if (record.schemaVersion !== '2.0') {
    record.schemaVersion = '2.0';
    dirty = true;
  }

  (record.programmes || []).forEach((programme, index) => {
    if (index === 0 || programme.role === 'comparator') {
      if (programme.family !== 'comparator') {
        programme.family = 'comparator';
        dirty = true;
      }
      return;
    }

    const legacyKind = roleToKind.get(programme.role);
    const expectedKind = legacyKind || programme.alternativeKind || (index === 1 ? 'closest-match' : 'other-defensible');

    if (programme.role !== 'ucr-alternative') {
      programme.role = 'ucr-alternative';
      dirty = true;
    }
    if (programme.family !== 'ucr') {
      programme.family = 'ucr';
      dirty = true;
    }
    if (programme.alternativeKind !== expectedKind) {
      programme.alternativeKind = expectedKind;
      dirty = true;
    }
  });

  if (dirty) {
    fs.writeFileSync(file, `${JSON.stringify(record, null, 2)}\n`, 'utf8');
    changed += 1;
    console.log(`Migrated ${path.relative(root, file)}`);
  }
}

console.log(`Public example migration complete: ${changed} file(s) changed.`);
