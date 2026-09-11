import fs from 'node:fs';
import path from 'node:path';

export const UCR_DEFAULT_COURSE_EC = 7.5;

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
  if (typeof cell === 'string' && cell.trim()) return { text: cell };
  if (typeof cell === 'object' && typeof cell.text === 'string' && cell.text.trim()) return cell;
  return null;
}

export function isComparator(programme) {
  return programme?.role === 'comparator';
}

export function isUcrProgramme(programme) {
  return ['ucr-depth', 'ucr-balanced', 'ucr-thematic'].includes(programme?.role);
}

export function comparatorMetadata(example) {
  const comparator = example?.comparator || example?.referenceProgramme;
  return comparator && typeof comparator === 'object' ? comparator : {};
}

export function comparatorLabel(example) {
  const comparator = comparatorMetadata(example);
  if (comparator.name && comparator.institution) {
    return `${comparator.name} at ${comparator.institution}`;
  }
  return comparator.name || 'External bachelor programme';
}

export function visibleProgrammeLabel(example, programme) {
  if (!programme) return '';
  const comparator = comparatorMetadata(example);
  const name = comparator.name || 'this programme';

  if (programme.role === 'comparator') return comparatorLabel(example);
  if (programme.role === 'ucr-depth') return `Closest match to ${name}`;
  if (programme.role === 'ucr-balanced') return `${name} + related subjects`;
  if (programme.role === 'ucr-thematic') {
    return example?.origin === 'counselor'
      ? 'A broader programme around related interests'
      : 'A broader programme around your interests';
  }

  return programme.label || '';
}

export function courseCredits(course) {
  const raw = course?.credits;
  if (raw !== undefined && raw !== null && String(raw).trim() !== '') return raw;
  return UCR_DEFAULT_COURSE_EC;
}

export function linkedinProgrammes(example) {
  const programmes = Array.isArray(example?.programmes) ? example.programmes : [];
  return example?.display?.showComparatorOnLinkedIn === false
    ? programmes.filter(programme => !isComparator(programme))
    : programmes;
}

export function escapeHtml(value = '') {
  return String(value).replace(/[&<>"']/g, c => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
  }[c]));
}

function isHttpUrl(value) {
  if (typeof value !== 'string' || !value.trim()) return false;
  try {
    const url = new URL(value);
    return url.protocol === 'https:' || url.protocol === 'http:';
  } catch {
    return false;
  }
}

function validCreditValue(value) {
  if (value === undefined || value === null || value === '') return true;
  if (typeof value === 'number') return Number.isFinite(value) && value > 0;
  if (typeof value === 'string') return value.trim().length > 0;
  return false;
}

export function validateExample(example, sourceName = 'example') {
  const errors = [];
  const warnings = [];
  const fail = message => errors.push(`${sourceName}: ${message}`);
  const warn = message => warnings.push(`${sourceName}: ${message}`);

  if (!example || typeof example !== 'object' || Array.isArray(example)) {
    return { errors: [`${sourceName}: root must be an object`], warnings };
  }

  if (typeof example.schemaVersion !== 'string' || !example.schemaVersion.trim()) {
    fail('schemaVersion is required');
  }

  if (typeof example.id !== 'string' || !/^[a-z0-9-]+$/.test(example.id)) {
    fail('id must use lowercase letters, numbers and hyphens');
  }

  if (example.origin !== undefined && !['student', 'counselor'].includes(example.origin)) {
    fail('origin must be "student" or "counselor" when supplied');
  }

  const studentLike = example.origin === 'student' || example.origin === undefined;
  if (studentLike && (typeof example.interests !== 'string' || !example.interests.trim())) {
    fail('student-origin and legacy examples need a non-empty interests string');
  }

  if (example.interestInterpretation !== undefined && (
    typeof example.interestInterpretation !== 'string' || !example.interestInterpretation.trim()
  )) {
    fail('interestInterpretation must be a non-empty string when supplied');
  }

  if (example.origin === 'counselor') {
    const provider = example.programmeProvider;
    if (!provider || typeof provider !== 'object' || Array.isArray(provider)) {
      fail('counselor-origin records require programmeProvider metadata');
    } else if (
      provider.programmeProviderId === undefined &&
      provider.recognizedProgrammeId === undefined &&
      provider.sourceExcelRow === undefined
    ) {
      fail('programmeProvider must include at least one stable registry identifier');
    }
  }

  if (
    example?.display?.showComparatorOnLinkedIn !== undefined &&
    typeof example.display.showComparatorOnLinkedIn !== 'boolean'
  ) {
    fail('display.showComparatorOnLinkedIn must be a boolean when supplied');
  }

  const comparator = comparatorMetadata(example);
  if (!comparator || typeof comparator !== 'object' || Array.isArray(comparator)) {
    fail('comparator metadata is required');
  } else {
    if (typeof comparator.name !== 'string' || !comparator.name.trim()) {
      fail('comparator.name is required');
    }
    if (typeof comparator.institution !== 'string' || !comparator.institution.trim()) {
      fail('comparator.institution is required');
    }
    if (!isHttpUrl(comparator.primarySourceUrl)) {
      fail('comparator.primarySourceUrl must be an http(s) URL');
    }
  }

  if (!example.comparator && example.referenceProgramme) {
    warn('referenceProgramme is a legacy alias; new records should use comparator');
  }

  if (example.links && typeof example.links === 'object') {
    for (const [key, value] of Object.entries(example.links)) {
      if (value !== undefined && value !== null && value !== '' && !isHttpUrl(value)) {
        fail(`links.${key} must be an http(s) URL when supplied`);
      }
    }
  }

  if (!Array.isArray(example.programmes) || example.programmes.length !== 4) {
    fail('programmes must contain exactly four programmes');
  }

  if (!Array.isArray(example.blocks) || example.blocks.length === 0) {
    fail('blocks must be a non-empty array');
  }

  const programmes = Array.isArray(example.programmes) ? example.programmes : [];
  const expectedRoles = ['comparator', 'ucr-depth', 'ucr-balanced', 'ucr-thematic'];
  const ids = programmes.map(p => p?.id).filter(Boolean);

  if (new Set(ids).size !== ids.length) fail('programme ids must be unique');

  programmes.forEach((programme, index) => {
    if (!programme || typeof programme !== 'object' || Array.isArray(programme)) {
      fail(`programme ${index + 1} must be an object`);
      return;
    }

    if (typeof programme.id !== 'string' || !/^[a-z0-9-]+$/.test(programme.id)) {
      fail(`programme ${index + 1} has an invalid id`);
    }

    if (programme.role !== expectedRoles[index]) {
      fail(`programme ${index + 1} must have role "${expectedRoles[index]}"`);
    }

    if (typeof programme.label !== 'string' || !programme.label.trim()) {
      fail(`programme ${programme.id || index + 1} needs a stored label`);
    }

    if (programme.family !== undefined) {
      const expectedFamily = programme.role === 'comparator' ? 'comparator' : 'ucr';
      if (programme.family !== expectedFamily) {
        fail(`programme ${programme.id || index + 1} family must be "${expectedFamily}" when supplied`);
      }
    }

    const schedule = programme.schedule;
    if (schedule === undefined) {
      if (isUcrProgramme(programme)) fail(`UCR programme ${programme.id} must include a six-semester schedule`);
      return;
    }

    if (!schedule || typeof schedule !== 'object' || Array.isArray(schedule)) {
      fail(`programme ${programme.id} schedule must be an object`);
      return;
    }

    const semesters = schedule.semesters;
    if (!Array.isArray(semesters)) {
      fail(`programme ${programme.id} schedule.semesters must be an array`);
      return;
    }

    if (isUcrProgramme(programme) && semesters.length !== 6) {
      fail(`UCR programme ${programme.id} must have exactly six semesters`);
    }

    const seenCourses = new Set();
    const seenSemesterLabels = new Set();

    semesters.forEach((semester, semesterIndex) => {
      if (!semester || typeof semester !== 'object' || Array.isArray(semester)) {
        fail(`programme ${programme.id}, semester ${semesterIndex + 1}: semester must be an object`);
        return;
      }

      if (typeof semester.label !== 'string' || !semester.label.trim()) {
        fail(`programme ${programme.id}, semester ${semesterIndex + 1}: label is required`);
      } else {
        const labelKey = semester.label.trim().toLowerCase();
        if (seenSemesterLabels.has(labelKey)) fail(`programme ${programme.id}: duplicate semester label "${semester.label}"`);
        seenSemesterLabels.add(labelKey);
      }

      if (!Array.isArray(semester.courses)) {
        fail(`programme ${programme.id}, semester ${semesterIndex + 1}: courses must be an array`);
        return;
      }

      if (isUcrProgramme(programme) && semester.courses.length !== 4) {
        fail(`UCR programme ${programme.id}, semester ${semesterIndex + 1}: expected four courses`);
      }

      semester.courses.forEach((course, courseIndex) => {
        if (!course || typeof course !== 'object' || Array.isArray(course)) {
          fail(`programme ${programme.id}, semester ${semesterIndex + 1}, course ${courseIndex + 1}: course must be an object`);
          return;
        }

        if (typeof course.name !== 'string' || !course.name.trim()) {
          fail(`programme ${programme.id}, semester ${semesterIndex + 1}, course ${courseIndex + 1}: name is required`);
          return;
        }

        if (course.code !== undefined && typeof course.code !== 'string') {
          fail(`programme ${programme.id}, semester ${semesterIndex + 1}, course ${courseIndex + 1}: code must be a string when supplied`);
        }

        if (course.level !== undefined && typeof course.level !== 'string' && !Number.isInteger(course.level)) {
          fail(`programme ${programme.id}, semester ${semesterIndex + 1}, course ${courseIndex + 1}: level must be a string or integer when supplied`);
        }

        if (!validCreditValue(course.credits)) {
          fail(`programme ${programme.id}, semester ${semesterIndex + 1}, course ${courseIndex + 1}: credits must be positive or a non-empty string when supplied`);
        }

        const keySource = typeof course.code === 'string' && course.code.trim() ? course.code : course.name;
        const key = keySource.trim().toLowerCase();
        if (seenCourses.has(key)) fail(`programme ${programme.id}: duplicate scheduled course ${keySource}`);
        seenCourses.add(key);
      });
    });
  });

  const knownIds = new Set(ids);

  (Array.isArray(example.blocks) ? example.blocks : []).forEach((block, blockIndex) => {
    if (!block || typeof block !== 'object' || Array.isArray(block)) {
      fail(`block ${blockIndex + 1} must be an object`);
      return;
    }

    if (typeof block.title !== 'string' || !block.title.trim()) fail(`block ${blockIndex + 1} needs a title`);

    if (!Array.isArray(block.rows) || block.rows.length === 0) {
      fail(`block ${block.title || blockIndex + 1}: rows must be a non-empty array`);
      return;
    }

    block.rows.forEach((row, rowIndex) => {
      if (!row?.cells || typeof row.cells !== 'object' || Array.isArray(row.cells)) {
        fail(`block ${block.title}, row ${rowIndex + 1}: cells must be an object`);
        return;
      }

      const keys = Object.keys(row.cells);
      if (keys.length === 0) {
        fail(`block ${block.title}, row ${rowIndex + 1}: cells must not be empty`);
        return;
      }

      keys.forEach(key => {
        if (!knownIds.has(key)) fail(`block ${block.title}, row ${rowIndex + 1}: unknown programme id ${key}`);
        const raw = row.cells[key];
        const cell = normalizeCell(raw);
        if (raw !== null && cell === null) {
          fail(`block ${block.title}, row ${rowIndex + 1}, programme ${key}: invalid cell value`);
        }
        if (cell && !validCreditValue(cell.credits)) {
          fail(`block ${block.title}, row ${rowIndex + 1}, programme ${key}: invalid credits value`);
        }
      });

      const nonEmpty = keys.map(key => normalizeCell(row.cells[key])).filter(Boolean);
      if (!nonEmpty.length) fail(`block ${block.title}, row ${rowIndex + 1}: row contains no substantive cell`);
    });
  });

  if (Array.isArray(example.notes)) {
    example.notes.forEach((note, index) => {
      if (!note || typeof note !== 'object' || Array.isArray(note)) {
        fail(`note ${index + 1} must be an object`);
        return;
      }
      const hasText = typeof note.text === 'string' && note.text.trim();
      const hasTemplate = typeof note.type === 'string' && note.type.trim() && note.params && typeof note.params === 'object';
      if (!hasText && !hasTemplate) fail(`note ${index + 1} needs text or a template type with params`);
    });
  }

  return { errors, warnings };
}
