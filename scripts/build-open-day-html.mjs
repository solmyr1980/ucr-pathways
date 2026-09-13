import fs from 'node:fs';
import path from 'node:path';
import {
  comparisonNotes,
  exampleFiles,
  readExample,
  validateExample,
  normalizeCell,
  isComparator,
  isUcrProgramme,
  comparatorMetadata,
  visibleProgrammeLabel,
  escapeHtml,
  UCR_DEFAULT_COURSE_EC
} from './example-utils.mjs';

const root = process.cwd();
const target = process.argv[2] || 'all';
const css = fs.readFileSync(path.join(root, 'assets', 'css', 'open-day.css'), 'utf8');
const outputDir = path.join(root, 'output', 'open-day');
fs.mkdirSync(outputDir, { recursive: true });

const builderUrl = 'https://program.ucr.nl/';
const ucrCoursesUrl = 'https://ucr.nl/education/courses/';
const logoPath = '../../assets/brand/ucr-primary-white-on-plum.png';
const qrPath = '../../assets/brand/program-builder-qr.png';
const disclaimer = '[PLACEHOLDER — insert approved student-program disclaimer from the printed butterfly.]';

function cohortLabel(cohort) {
  if (!cohort) return '';
  return String(cohort).replace(/\s+cohort\s*$/i, '').trim();
}

function renderHeader(example, title) {
  const start = cohortLabel(example.cohort);
  return `<header class="od-header">
    <a href="https://ucr.nl/"><img class="od-logo" src="${logoPath}" alt="University College Roosevelt"></a>
    <div class="od-header-copy">
      <h1 class="od-product">${escapeHtml(title)}</h1>
    </div>
    <div class="od-meta">
      <div class="od-id">${escapeHtml(example.id)}</div>
      ${start ? `<div>Start: ${escapeHtml(start)}</div>` : ''}
    </div>
  </header>`;
}

function renderInterest(example) {
  if (!example.interests) return '';
  return `<div class="od-interest">
    <span class="od-interest-label">You told us that…</span>
    <span class="od-interest-text">${escapeHtml(example.interests)}</span>
  </div>`;
}

function renderInterpretation(example) {
  if (!example.interestInterpretation) return '';
  return `<div class="od-interest">
    <span class="od-interest-label">For us, this means that…</span>
    <span class="od-interest-text">${escapeHtml(example.interestInterpretation)}</span>
  </div>`;
}

function renderBuilder() {
  return `<a class="od-builder" href="${builderUrl}">
    <img src="${qrPath}" alt="QR code for the UCR Program Builder">
    <span class="od-builder-text"><strong>Tweak this programme to your liking</strong>${builderUrl}</span>
  </a>`;
}

function renderFooter(copy) {
  return `<footer class="od-footer">
    <div class="od-footer-copy">${copy}</div>
    ${renderBuilder()}
  </footer>`;
}

function cellCredit(cell, programme) {
  if (cell?.credits !== undefined && cell?.credits !== null && String(cell.credits).trim()) return `${cell.credits} EC`;
  return isUcrProgramme(programme) ? `${UCR_DEFAULT_COURSE_EC} EC` : '';
}

function renderComparison(example) {
  const comparator = comparatorMetadata(example);
  const programmeHeads = example.programmes.map(programme => {
    const sourceUrl = isComparator(programme) ? comparator.primarySourceUrl : ucrCoursesUrl;
    const sourceLabel = isComparator(programme) ? 'Official programme' : 'UCR courses';
    return `<th class="programme-head${isComparator(programme) ? ' comparator' : ''}">
      <span class="programme-label">${escapeHtml(visibleProgrammeLabel(example, programme))}</span>
      ${sourceUrl ? `<span class="programme-subtitle"><a href="${escapeHtml(sourceUrl)}">${escapeHtml(sourceLabel)} ↗</a></span>` : ''}
    </th>`;
  }).join('');

  const blockRows = example.blocks.map(block => {
    const rows = block.rows.map(row => {
      const cells = example.programmes.map(programme => {
        const cell = normalizeCell(row.cells?.[programme.id]);
        if (!cell) return '<td class="comparison-cell empty"></td>';
        const ec = cellCredit(cell, programme);
        return `<td class="comparison-cell">${escapeHtml(cell.text)}${ec ? ` · ${escapeHtml(ec)}` : ''}${cell.note ? `<span class="cell-note">${escapeHtml(cell.note)}</span>` : ''}</td>`;
      }).join('');
      return `<tr>${cells}</tr>`;
    }).join('');
    return `<tr class="block-title"><td colspan="${example.programmes.length}">${escapeHtml(block.title)}</td></tr>${rows}`;
  }).join('');

  const colgroup = `<colgroup>${example.programmes.map(() => '<col>').join('')}</colgroup>`;
  const ucrCount = example.programmes.filter(isUcrProgramme).length;

  return `<section class="od-page" data-page="comparison" style="--programme-count:${example.programmes.length}">
    ${renderHeader(example, 'Your personalized programme options')}
    <main class="od-body">
      ${renderInterest(example)}
      ${renderInterpretation(example)}
      <p class="od-intro">See how another Dutch bachelor compares with ${ucrCount === 1 ? 'the UCR programme' : 'the UCR programmes'} that can be defensibly composed around this case.</p>
      <table class="comparison-table">
        ${colgroup}
        <thead><tr>${programmeHeads}</tr></thead>
        <tbody>${blockRows}</tbody>
      </table>
      ${comparisonNotes(example).map(note => `<div class="od-page-note">${escapeHtml(note)}</div>`).join('')}
      <div class="od-page-note">Blank cells indicate that no sufficiently comparable named component is shown in that position.</div>
    </main>
    ${renderFooter('<strong>Illustrative programme:</strong> the options shown here are examples of feasible academic possibilities, not official tracks.')}
  </section>`;
}

function renderSchedule(example) {
  const ucrProgrammes = example.programmes.filter(isUcrProgramme);
  const heads = ucrProgrammes.map(programme => `<div class="schedule-programme-head">
    <span class="programme-label">${escapeHtml(visibleProgrammeLabel(example, programme))}</span>
    <span class="programme-subtitle"><a href="${ucrCoursesUrl}">UCR courses ↗</a></span>
  </div>`).join('');

  const semesterCells = [];
  for (let semesterIndex = 0; semesterIndex < 6; semesterIndex += 1) {
    ucrProgrammes.forEach(programme => {
      const semester = programme.schedule.semesters[semesterIndex];
      const courses = semester.courses.map(course => {
        const ec = course.credits || UCR_DEFAULT_COURSE_EC;
        return `<li>${escapeHtml(course.name)}${course.level !== undefined ? ` <span class="course-level">· L${escapeHtml(Number(course.level) < 10 ? Number(course.level) * 100 : course.level)}</span>` : ''}<span class="course-level"> · ${escapeHtml(ec)} EC</span></li>`;
      }).join('');
      semesterCells.push(`<div class="schedule-cell${semesterIndex % 2 ? ' alt' : ''}">
        <h3 class="semester-label">${escapeHtml(semester.label)}</h3>
        <ul class="course-list">${courses}</ul>
      </div>`);
    });
  }

  const levelCounts = ucrProgrammes.map(programme => programme.schedule.semesters
    .flatMap(semester => semester.courses)
    .filter(course => Number(course.level) === 3).length);

  return `<section class="od-page" data-page="schedule" style="--ucr-count:${ucrProgrammes.length}">
    ${renderHeader(example, 'Possible UCR programmes — semester by semester')}
    <main class="od-body schedule-body">
      ${renderInterest(example)}
      <p class="od-intro schedule-intro">The same UCR ${ucrProgrammes.length === 1 ? 'programme' : 'programmes'} shown on page 1, arranged across six semesters with four courses in each semester.</p>
      <div class="schedule-grid">
        ${heads}
        ${semesterCells.join('')}
      </div>
      <div class="validation-strip"><strong>Structure checked</strong><span>24 unique courses per programme · 4 per semester · 300-level courses: ${levelCounts.join(' · ')}</span></div>
      <div class="od-page-note">${escapeHtml(disclaimer)}</div>
    </main>
    ${renderFooter('<strong>Next step:</strong> use the UCR Program Builder to explore and build your own programme.')}
  </section>`;
}

for (const file of exampleFiles(root, target)) {
  const example = readExample(file);
  const { errors, warnings } = validateExample(example, path.basename(file));

  warnings.forEach(message => console.warn(`WARNING: ${message}`));
  if (errors.length) throw new Error(errors.join('\n'));

  const html = `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>${escapeHtml(example.id)} - UCR personalized programme - PDF</title>
<link rel="stylesheet" href="../../assets/css/brand.css">
<style>${css}</style>
</head>
<body>${renderComparison(example)}${renderSchedule(example)}</body>
</html>`;

  const out = path.join(outputDir, `${example.id}.html`);
  fs.writeFileSync(out, html, 'utf8');
  console.log(`Created ${path.relative(root, out)}`);
}
