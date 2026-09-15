import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const dir = path.join(root, 'data', 'counselor', 'comparisons');
const out = [];
for (const name of fs.readdirSync(dir).filter(n => /^cp-00000[1-4]\.json$/.test(n)).sort()) {
  const record = JSON.parse(fs.readFileSync(path.join(dir, name), 'utf8'));
  const ucr = (record.programmes || []).filter(p => p.family === 'ucr');
  const courses = new Map();
  for (const p of ucr) for (const sem of p.schedule?.semesters || []) for (const c of sem.courses || []) {
    if (!courses.has(c.code)) courses.set(c.code, { code: c.code, name: c.name, programmes: [] });
    courses.get(c.code).programmes.push(p.id);
  }
  out.push({
    id: record.id,
    programme: record.comparator?.name,
    comparatorComponents: (record.comparator?.components || []).map(c => ({ id: c.id, name: c.name, credits: c.credits })),
    ucrCourses: [...courses.values()].sort((a,b) => a.name.localeCompare(b.name))
  });
}
fs.writeFileSync(path.join(root, 'data', 'counselor', 'tmp-alignment-inventory.json'), JSON.stringify(out, null, 2) + '\n');
