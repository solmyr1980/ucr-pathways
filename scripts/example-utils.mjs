import fs from 'node:fs';
import path from 'node:path';

export function exampleFiles(root, target = 'all') {
  const dir = path.join(root, 'data', 'examples');
  if (target !== 'all') {
    const id = target.toLowerCase().replace(/\.json$/i, '');
    if (!/^[a-z0-9-]+$/.test(id)) throw new Error(`Invalid example id: ${target}`);
    const file = path.join(dir, `${id}.json`);
    if (!fs.existsSync(file)) throw new Error(`Example not found: ${id}`);
    return [file];
  }
  return fs.readdirSync(dir)
    .filter(name => name.endsWith('.json'))
    .sort()
    .map(name => path.join(dir, name));
}

export function readExample(file) {
  return JSON.parse(fs.readFileSync(file, 'utf8'));
}

export function normalizeCell(cell) {
  if (cell === null || cell === undefined || cell === '') return null;
  if (typeof cell === 'string') return { text: cell };
  if (typeof cell === 'object' && typeof cell.text === 'string' && cell.text.trim()) return cell;
  return null;
}

export function isComparator(programme) {
  return programme.role === 'comparator' || programme.family === 'comparator' || programme.accent === 'comparator';
}

export function escapeHtml(value = '') {
  return String(value).replace(/[&<>"']/g, c => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
  }[c]));
}

export function validateExample(example, sourceName = 'example') {
  const errors = [];
  const warnings = [];
  const fail = message => errors.push(`${sourceName}: ${message}`);
  const warn = message => warnings.push(`${sourceName}: ${message}`);

  if (!example || typeof example !== 'object') return { errors: [`${sourceName}: root must be an object`], warnings };
  if (typeof example.schemaVersion !== 'string') fail('schemaVersion is required');
  if (typeof example.id !== 'string' || !/^[a-z0-9-]+$/.test(example.id)) fail('id must use lowercase letters, numbers and hyphens');
  if (typeof example.interests !== 'string' || !example.interests.trim()) fail('interests must be a non-empty string');
  if (!Array.isArray(example.programmes) || example.programmes.length === 0) fail('programmes must be a non-empty array');
  if (!Array.isArray(example.blocks) || example.blocks.length === 0) fail('blocks must be a non-empty array');

  const programmes = Array.isArray(example.programmes) ? example.programmes : [];
  const ids = programmes.map(p => p?.id).filter(Boolean);
  if (new Set(ids).size !== ids.length) fail('programme ids must be unique');

  programmes.forEach((programme, index) => {
    if (!programme || typeof programme !== 'object') return fail(`programme ${index + 1} must be an object`);
    if (typeof programme.id !== 'string' || !/^[a-z0-9-]+$/.test(programme.id)) fail(`programme ${index + 1} has an invalid id`);
    if (typeof programme.label !== 'string' || !programme.label.trim()) fail(`programme ${programme.id || index + 1} needs a label`);

    const semesters = programme.schedule?.semesters;
    if (semesters !== undefined) {
      if (!Array.isArray(semesters)) {
        fail(`programme ${programme.id} schedule.semesters must be an array`);
      } else {
        if (programme.family === 'ucr' && semesters.length !== 6) fail(`UCR programme ${programme.id} must have six semesters when a schedule is supplied`);
        const seen = new Set();
        let advanced = 0;
        semesters.forEach((semester, semesterIndex) => {
          if (!Array.isArray(semester?.courses)) return fail(`programme ${programme.id}, semester ${semesterIndex + 1}: courses must be an array`);
          if (programme.family === 'ucr' && semester.courses.length !== 4) fail(`UCR programme ${programme.id}, semester ${semesterIndex + 1}: expected four courses`);
          semester.courses.forEach(course => {
            const key = course.code || course.name;
            if (!key) return fail(`programme ${programme.id}: every scheduled course needs a name or code`);
            if (seen.has(key)) fail(`programme ${programme.id}: duplicate scheduled course ${key}`);
            seen.add(key);
            const level = Number(course.level);
            if (Number.isFinite(level) && level >= 300) advanced += 1;
          });
        });
        if (programme.family === 'ucr' && advanced > 0 && advanced < 6) fail(`UCR programme ${programme.id}: fewer than six 300-level courses in supplied schedule`);
      }
    }
  });

  if (programmes.length && !programmes.some(isComparator)) warn('no programme is marked as comparator');

  const knownIds = new Set(ids);
  (Array.isArray(example.blocks) ? example.blocks : []).forEach((block, blockIndex) => {
    if (!block || typeof block !== 'object') return fail(`block ${blockIndex + 1} must be an object`);
    if (typeof block.title !== 'string' || !block.title.trim()) fail(`block ${blockIndex + 1} needs a title`);
    if (!Array.isArray(block.rows)) return fail(`block ${block.title || blockIndex + 1}: rows must be an array`);
    block.rows.forEach((row, rowIndex) => {
      if (!row?.cells || typeof row.cells !== 'object' || Array.isArray(row.cells)) return fail(`block ${block.title}, row ${rowIndex + 1}: cells must be an object`);
      const keys = Object.keys(row.cells);
      keys.forEach(key => { if (!knownIds.has(key)) fail(`block ${block.title}, row ${rowIndex + 1}: unknown programme id ${key}`); });
      const nonEmpty = keys.map(key => normalizeCell(row.cells[key])).filter(Boolean);
      if (!nonEmpty.length) warn(`block ${block.title}, row ${rowIndex + 1} is empty`);
    });
  });

  return { errors, warnings };
}
