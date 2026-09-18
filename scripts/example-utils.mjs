import { comparatorMetadata, visibleProgrammeLabel } from '../assets/js/comparison.js';
export { comparatorMetadata, visibleProgrammeLabel, comparisonNotes } from '../assets/js/comparison.js';
import fs from 'node:fs';
import path from 'node:path';

export const UCR_DEFAULT_COURSE_EC = 7.5;
export const UCR_MIN_DISTINCT_EC = 30;
export const UCR_MIN_DISTINCT_COURSES = 4;

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
  return programme?.role === 'comparator' || programme?.family === 'comparator';
}

export function isUcrProgramme(programme) {
  if (programme?.family === 'ucr') return true;
  return ['ucr-alternative', 'ucr-depth', 'ucr-balanced', 'ucr-thematic'].includes(programme?.role);
}

export function comparatorLabel(example) {
  const comparator = comparatorMetadata(example);
  if (comparator.name && comparator.institution) {
    return `${comparator.name} at ${comparator.institution}`;
  }
  return comparator.name || 'External bachelor programme';
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

export function creditNumber(value) {
  if (typeof value === 'number' && Number.isFinite(value)) return value;
  if (typeof value !== 'string' || !value.trim()) return null;
  const match = value.replace(',', '.').match(/-?\d+(?:\.\d+)?/);
  return match ? Number(match[0]) : null;
}

function normalizedLabel(value) {
  return String(value || '').trim().toLowerCase().replace(/\s+/g, ' ');
}

function approximatelyEqual(left, right, tolerance = 0.001) {
  return Number.isFinite(left) && Number.isFinite(right) && Math.abs(left - right) < tolerance;
}

function comparisonEntries(blocks, programmeId) {
  const entries = [];
  (Array.isArray(blocks) ? blocks : []).forEach((block, blockIndex) => {
    (Array.isArray(block?.rows) ? block.rows : []).forEach((row, rowIndex) => {
      const cell = normalizeCell(row?.cells?.[programmeId]);
      if (cell) entries.push({ cell, block, blockIndex, rowIndex });
    });
  });
  return entries;
}

function scheduledCourses(programme) {
  return (programme?.schedule?.semesters || []).flatMap(semester => semester?.courses || []);
}

function courseKey(course) {
  return String(course?.code || course?.name || '').trim().toLowerCase();
}

function distinctCourseCredits(courses, otherKeys) {
  return courses
    .filter(course => !otherKeys.has(courseKey(course)))
    .reduce((sum, course) => {
      const credits = creditNumber(courseCredits(course));
      return credits === null ? sum : sum + credits;
    }, 0);
}

function validateComparisonCoverage(example, programmes, fail) {
  const comparator = comparatorMetadata(example);

  for (const programme of programmes) {
    if (!programme?.id) continue;
    const entries = comparisonEntries(example.blocks, programme.id);
    let total = 0;
    let numericCredits = true;

    for (const { cell, block, rowIndex } of entries) {
      const credits = creditNumber(cell.credits);
      if (credits === null || credits <= 0) {
        numericCredits = false;
        fail(`comparison ${programme.id}, block ${block?.title || 'untitled'}, row ${rowIndex + 1}: explicit numeric credits are required`);
      } else {
        total += credits;
      }
    }

    if (numericCredits && !approximatelyEqual(total, 180)) {
      fail(`comparison ${programme.id} totals ${total} EC; every programme comparison must total 180 EC`);
    }

    if (isUcrProgramme(programme)) {
      const courses = scheduledCourses(programme);
      const byCode = new Map();
      const byName = new Map();
      for (const course of courses) {
        if (typeof course?.code === 'string' && course.code.trim()) byCode.set(course.code.trim().toLowerCase(), course);
        const nameKey = normalizedLabel(course?.name);
        if (!byName.has(nameKey)) byName.set(nameKey, []);
        byName.get(nameKey).push(course);
      }

      const seen = new Set();
      for (const { cell, block, rowIndex } of entries) {
        let course = null;
        if (typeof cell.courseCode === 'string' && cell.courseCode.trim()) {
          course = byCode.get(cell.courseCode.trim().toLowerCase()) || null;
          if (!course) {
            fail(`comparison ${programme.id}, block ${block?.title || 'untitled'}, row ${rowIndex + 1}: courseCode ${JSON.stringify(cell.courseCode)} is not in the scheduled programme`);
            continue;
          }
        } else {
          const matches = byName.get(normalizedLabel(cell.text)) || [];
          if (matches.length === 1) course = matches[0];
          else if (matches.length === 0) {
            fail(`comparison ${programme.id}, block ${block?.title || 'untitled'}, row ${rowIndex + 1}: ${JSON.stringify(cell.text)} is not a scheduled UCR course`);
            continue;
          } else {
            fail(`comparison ${programme.id}, block ${block?.title || 'untitled'}, row ${rowIndex + 1}: course name ${JSON.stringify(cell.text)} is ambiguous; use courseCode`);
            continue;
          }
        }

        if (normalizedLabel(cell.text) !== normalizedLabel(course.name)) {
          fail(`comparison ${programme.id}: displayed text ${JSON.stringify(cell.text)} does not match referenced course ${JSON.stringify(course.name)}`);
        }

        const cellCredits = creditNumber(cell.credits);
        const canonicalCredits = creditNumber(courseCredits(course));
        if (cellCredits !== null && canonicalCredits !== null && !approximatelyEqual(cellCredits, canonicalCredits)) {
          fail(`comparison ${programme.id}: ${course.code || course.name} shows ${cellCredits} EC but the scheduled course has ${canonicalCredits} EC`);
        }

        const key = (course.code || course.name).trim().toLowerCase();
        if (seen.has(key)) fail(`comparison ${programme.id}: duplicate course ${course.code || course.name}`);
        seen.add(key);
      }

      const missing = courses.filter(course => !seen.has((course.code || course.name).trim().toLowerCase()));
      if (missing.length) {
        fail(`comparison ${programme.id}: scheduled courses missing from comparison: ${missing.map(course => course.code || course.name).join(', ')}`);
      }

      const ppd = courses.find(course => String(course?.code || '').toUpperCase() === 'ACCPPDE101');
      if (ppd && !seen.has((ppd.code || ppd.name).trim().toLowerCase())) {
        fail(`comparison ${programme.id}: Personal & Professional Development must appear exactly once in the comparison`);
      }
      continue;
    }

    if (isComparator(programme) && Array.isArray(comparator?.components) && comparator.components.length) {
      const byId = new Map();
      let componentTotal = 0;
      for (const component of comparator.components) {
        const id = String(component?.id || '').trim();
        if (!id) {
          fail('comparator.components entries require stable ids');
          continue;
        }
        if (byId.has(id)) fail(`comparator.components contains duplicate id ${id}`);
        byId.set(id, component);
        const credits = creditNumber(component?.credits);
        if (credits === null || credits <= 0) fail(`comparator component ${id} requires positive numeric credits`);
        else componentTotal += credits;
      }
      if (!approximatelyEqual(componentTotal, 180)) {
        fail(`comparator.components total ${componentTotal} EC; reconstructed comparator must total 180 EC`);
      }

      const seen = new Set();
      for (const { cell, block, rowIndex } of entries) {
        const componentId = String(cell.componentId || '').trim();
        if (!componentId) {
          fail(`comparison comparator, block ${block?.title || 'untitled'}, row ${rowIndex + 1}: componentId is required when comparator.components is present`);
          continue;
        }
        const component = byId.get(componentId);
        if (!component) {
          fail(`comparison comparator: componentId ${JSON.stringify(componentId)} is not in comparator.components`);
          continue;
        }
        if (seen.has(componentId)) fail(`comparison comparator: duplicate component ${componentId}`);
        seen.add(componentId);
        if (normalizedLabel(cell.text) !== normalizedLabel(component.name)) {
          fail(`comparison comparator: displayed text ${JSON.stringify(cell.text)} does not match component ${JSON.stringify(component.name)}`);
        }
        const cellCredits = creditNumber(cell.credits);
        const componentCredits = creditNumber(component.credits);
        if (cellCredits !== null && componentCredits !== null && !approximatelyEqual(cellCredits, componentCredits)) {
          fail(`comparison comparator: component ${componentId} shows ${cellCredits} EC but canonical component has ${componentCredits} EC`);
        }
      }
      const missing = comparator.components.filter(component => !seen.has(String(component?.id || '').trim()));
      if (missing.length) fail(`comparison comparator: canonical components missing from comparison: ${missing.map(component => component.id).join(', ')}`);
    }
  }
}

function validateAlternativeSelection(example, programmes, fail) {
  const selection = example?.alternativeSelection;
  if (selection === undefined) return;
  if (!selection || typeof selection !== 'object' || Array.isArray(selection)) {
    fail('alternativeSelection must be an object when supplied');
    return;
  }

  const ucrCount = programmes.filter(isUcrProgramme).length;
  if (!Number.isInteger(selection.includedCount) || selection.includedCount < 1 || selection.includedCount > 3) {
    fail('alternativeSelection.includedCount must be an integer from 1 to 3');
  } else if (selection.includedCount !== ucrCount) {
    fail(`alternativeSelection.includedCount is ${selection.includedCount} but record contains ${ucrCount} UCR alternatives`);
  }

  const reasons = ['maximum-reached', 'insufficient-evidence', 'not-substantially-distinct', 'not-substantively-distinct', 'not-feasible'];
  if (!reasons.includes(selection.stoppingReason)) {
    fail('alternativeSelection.stoppingReason is invalid');
  } else if (ucrCount === 3 && selection.stoppingReason !== 'maximum-reached') {
    fail('three UCR alternatives require alternativeSelection.stoppingReason = "maximum-reached"');
  } else if (ucrCount < 3 && selection.stoppingReason === 'maximum-reached') {
    fail('alternativeSelection.stoppingReason cannot be "maximum-reached" when fewer than three UCR alternatives are included');
  }

  if (typeof selection.assessment !== 'string' || !selection.assessment.trim()) {
    fail('alternativeSelection.assessment must be a non-empty string');
  }
}

function validateAcademicRationale(example, programmes, fail) {
  const rationale = example?.academicRationale;
  const studentLike = example?.origin === 'student' || example?.origin === undefined;
  if (rationale === undefined) {
    if (studentLike) fail('student-origin and legacy examples require academicRationale with one concept per UCR alternative');
    return;
  }
  if (!rationale || typeof rationale !== 'object' || Array.isArray(rationale)) {
    fail('academicRationale must be an object');
    return;
  }
  if (!Array.isArray(rationale.alternatives)) {
    fail('academicRationale.alternatives must be an array');
    return;
  }

  const programmeIds = new Set(programmes.map(programme => programme?.id).filter(Boolean));
  const comparatorIds = new Set(programmes.filter(isComparator).map(programme => programme.id));
  const ucrIds = programmes.filter(isUcrProgramme).map(programme => programme.id);
  const rationaleIds = [];
  rationale.alternatives.forEach((alternative, index) => {
    if (!alternative || typeof alternative !== 'object' || Array.isArray(alternative)) {
      fail(`academicRationale.alternatives[${index}] must be an object`);
      return;
    }
    const programmeId = typeof alternative.programmeId === 'string' ? alternative.programmeId.trim() : '';
    if (!programmeId) {
      fail(`academicRationale.alternatives[${index}].programmeId is required`);
    } else {
      rationaleIds.push(programmeId);
      if (!programmeIds.has(programmeId)) fail(`academicRationale references unknown programmeId ${programmeId}`);
      if (comparatorIds.has(programmeId)) fail('academicRationale must not assign a programme concept to the comparator');
    }
    if (typeof alternative.concept !== 'string' || !alternative.concept.trim()) {
      fail(`academicRationale.alternatives[${index}].concept is required`);
    }
  });

  if (new Set(rationaleIds).size !== rationaleIds.length) fail('academicRationale programmeId values must be unique');
  const rationaleIdSet = new Set(rationaleIds);
  if (rationaleIds.length !== ucrIds.length || ucrIds.some(id => !rationaleIdSet.has(id))) {
    fail('academicRationale.alternatives must contain exactly one concept for every UCR alternative');
  }
}

function validateDistinctUcrCourseSets(programmes, report) {
  const alternatives = programmes.filter(isUcrProgramme)
    .map(programme => ({
      programme,
      courses: scheduledCourses(programme)
    }))
    .filter(({ courses }) => courses.length);

  for (let i = 0; i < alternatives.length; i += 1) {
    for (let j = i + 1; j < alternatives.length; j += 1) {
      const left = alternatives[i];
      const right = alternatives[j];
      const leftKeys = new Set(left.courses.map(courseKey).filter(Boolean));
      const rightKeys = new Set(right.courses.map(courseKey).filter(Boolean));
      const shared = [...leftKeys].filter(key => rightKeys.has(key)).length;
      const leftDistinctCourses = [...leftKeys].filter(key => !rightKeys.has(key)).length;
      const rightDistinctCourses = [...rightKeys].filter(key => !leftKeys.has(key)).length;
      const leftDistinctEc = distinctCourseCredits(left.courses, rightKeys);
      const rightDistinctEc = distinctCourseCredits(right.courses, leftKeys);

      const courseFloorFails = leftDistinctCourses < UCR_MIN_DISTINCT_COURSES || rightDistinctCourses < UCR_MIN_DISTINCT_COURSES;
      const ecFloorFails = leftDistinctEc + 0.001 < UCR_MIN_DISTINCT_EC || rightDistinctEc + 0.001 < UCR_MIN_DISTINCT_EC;
      if (courseFloorFails || ecFloorFails) {
        report(
          `UCR alternatives ${left.programme.id} and ${right.programme.id} are not substantively distinct: ` +
          `${shared} courses are shared; each alternative must differ by at least ${UCR_MIN_DISTINCT_COURSES} courses / ${UCR_MIN_DISTINCT_EC} EC ` +
          `(actual distinct content: ${leftDistinctCourses} courses / ${leftDistinctEc} EC versus ${rightDistinctCourses} courses / ${rightDistinctEc} EC)`
        );
      }
    }
  }
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

  if (example.origin === 'student' && !example.interestInterpretation?.trim()) fail('student-origin records require a separate interestInterpretation');

  if (example.origin === 'counselor') {
    const provider = example.programmeProvider;
    if (!provider || typeof provider !== 'object' || Array.isArray(provider)) {
      fail('counselor-origin records require programmeProvider metadata');
    } else {
      const normalizedId = String(provider.counselorProgrammeId || '').trim();
      const legacyId = String(provider.programmeProviderId || '').trim();
      if (!normalizedId && !legacyId) {
        fail('programmeProvider requires counselorProgrammeId for normalized records or programmeProviderId for legacy records');
      }
      if (normalizedId && !/^cp-[0-9]{6}$/.test(normalizedId)) {
        fail('programmeProvider.counselorProgrammeId must use cp-000001 format');
      }
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

  if (!Array.isArray(example.programmes) || example.programmes.length < 2 || example.programmes.length > 4) {
    fail('programmes must contain one comparator followed by one to three UCR alternatives');
  }

  if (!Array.isArray(example.blocks) || example.blocks.length === 0) {
    fail('blocks must be a non-empty array');
  }

  const programmes = Array.isArray(example.programmes) ? example.programmes : [];
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

    if (index === 0) {
      if (!isComparator(programme)) fail('programme 1 must be the comparator');
    } else {
      if (!isUcrProgramme(programme) || isComparator(programme)) {
        fail(`programme ${index + 1} must be a UCR alternative`);
      }
      if (example.schemaVersion === '2.0' && programme.role !== 'ucr-alternative') {
        fail(`programme ${index + 1} must use role "ucr-alternative" in schema 2.0`);
      }
      if (index === 1 && example.schemaVersion === '2.0' && programme.alternativeKind !== 'closest-match') {
        fail('the first UCR alternative must use alternativeKind "closest-match" in schema 2.0');
      }
    }

    if (typeof programme.label !== 'string' || !programme.label.trim()) {
      fail(`programme ${programme.id || index + 1} needs a stored label`);
    }

    if (programme.alternativeKind !== undefined && !['closest-match', 'related-direction', 'question-led', 'other-defensible'].includes(programme.alternativeKind)) {
      fail(`programme ${programme.id || index + 1} has invalid alternativeKind`);
    }

    if (programme.family !== undefined) {
      const expectedFamily = index === 0 ? 'comparator' : 'ucr';
      if (programme.family !== expectedFamily) {
        fail(`programme ${programme.id || index + 1} family must be "${expectedFamily}" when supplied`);
      }
    }

    const schedule = programme.schedule;
    if (schedule === undefined) {
      if (index > 0) fail(`UCR programme ${programme.id} must include a six-semester schedule`);
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

    if (index > 0 && semesters.length !== 6) {
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

      if (index > 0 && semester.courses.length !== 4) {
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

  validateAcademicRationale(example, programmes, fail);
  validateAlternativeSelection(example, programmes, fail);
  const currentProductionRecord = example.origin === 'student' || example.origin === 'counselor' || example.alternativeSelection !== undefined;
  validateDistinctUcrCourseSets(programmes, currentProductionRecord ? fail : warn);

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
        if (cell?.courseCode !== undefined && (typeof cell.courseCode !== 'string' || !cell.courseCode.trim())) {
          fail(`block ${block.title}, row ${rowIndex + 1}, programme ${key}: courseCode must be a non-empty string when supplied`);
        }
        if (cell?.componentId !== undefined && (typeof cell.componentId !== 'string' || !cell.componentId.trim())) {
          fail(`block ${block.title}, row ${rowIndex + 1}, programme ${key}: componentId must be a non-empty string when supplied`);
        }
      });

      const nonEmpty = keys.map(key => normalizeCell(row.cells[key])).filter(Boolean);
      if (!nonEmpty.length) fail(`block ${block.title}, row ${rowIndex + 1}: row contains no substantive cell`);
    });
  });

  validateComparisonCoverage(example, programmes, fail);

  if (Array.isArray(example.notes)) {
    example.notes.forEach((note, index) => {
      if (!note || typeof note !== 'object' || Array.isArray(note)) {
        fail(`note ${index + 1} must be an object`);
        return;
      }
      const hasText = typeof note.text === 'string' && note.text.trim();
      if (!hasText) fail(`note ${index + 1} requires rendered text; expand semantic templates before public export`);
    });
  }

  return { errors, warnings };
}
