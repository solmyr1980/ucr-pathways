import fs from 'node:fs';
import path from 'node:path';
import {
  exampleFiles,
  readExample,
  validateExample,
  normalizeCell,
  isComparator,
  escapeHtml
} from './example-utils.mjs';

const root = process.cwd();
const target = process.argv[2] || 'all';
const css = fs.readFileSync(path.join(root, 'assets', 'css', 'open-day.css'), 'utf8');
const outputDir = path.join(root, 'output', 'open-day');
fs.mkdirSync(outputDir, { recursive: true });

const builderUrl = 'https://program.ucr.nl/';
const logoPath = '../../assets/brand/ucr-primary-white-on-plum.png';
const qrPath = '../../assets/brand/program-builder-qr.png';

function cohortLabel(cohort) {
  if (!cohort) return '';
  return String(cohort).replace(/\s+cohort\s*$/i, '').trim();
}

function renderHeader(example, subtitle) {
  const start = cohortLabel(example.cohort);
  return `<header class="od-header">
    <img class="od-logo" src="${logoPath}" alt="University College Roosevelt">
    <div class="od-header-copy">
      <h1 class="od-product">UCR Pathways</h1>
      <p class="od-subtitle">${escapeHtml(subtitle)}</p>
    </div>
    <div class="od-meta">
      <div class="od-id">${escapeHtml(example.id)}</div>
      ${start ? `<div>Start: ${escapeHtml(start)}</div>` : ''}
    </div>
  </header>`;
}

function renderInterest(example) {
  const label = example.display?.interestLabel || 'Your interests';
  return `<div class="od-interest">
    <span class="od-interest-label">${escapeHtml(label)}</span>
    <span class="od-interest-text">${escapeHtml(example.interests)}</span>
  </div>`;
}

function renderBuilder() {
  return `<a class="od-builder" href="${builderUrl}">
    <img src="${qrPath}" alt="QR code for the UCR Program Builder">
    <span class="od-builder-text"><strong>Build your own programme</strong>${builderUrl}</span>
  </a>`;
}

function renderFooter(copy) {
  return `<footer class="od-footer">
    <div class="od-footer-copy">${copy}</div>
    ${renderBuilder()}
  </footer>`;
}

function renderComparison(example) {
  const programmeHeads = example.programmes.map(programme => `<th class="programme-head${isComparator(programme) ? ' comparator' : ''}">
    <span class="programme-label">${escapeHtml(programme.label)}</span>
    ${programme.subtitle ? `<span class="programme-subtitle">${escapeHtml(programme.subtitle)}</span>` : ''}
  </th>`).join('');

  const blockRows = example.blocks.map(block => {
    const rows = block.rows.map(row => {
      const cells = example.programmes.map(programme => {
        const cell = normalizeCell(row.cells?.[programme.id]);
        if (!cell) return '<td class="comparison-cell empty"></td>';
        return `<td class="comparison-cell">${escapeHtml(cell.text)}${cell.note ? `<span class="cell-note">${escapeHtml(cell.note)}</span>` : ''}</td>`;
      }).join('');
      return `<tr>${cells}</tr>`;
    }).join('');
    return `<tr class="block-title"><td colspan="4">${escapeHtml(block.title)}</td></tr>${rows}`;
  }).join('');

  const intro = example.display?.title || 'See how your interests could take shape in a disciplinary degree and three progressively broader UCR pathways.';
  const comparisonNote = example.display?.comparisonNote || '';
  const provenance = example.referenceProgramme?.provenance || '';
  const sourceUrl = example.referenceProgramme?.primarySourceUrl || '';
  const source = provenance && sourceUrl
    ? `<a href="${escapeHtml(sourceUrl)}">${escapeHtml(provenance)}</a>`
    : escapeHtml(provenance);

  return `<section class="od-page" data-page="comparison">
    ${renderHeader(example, 'Four ways your interests could take shape')}
    <main class="od-body">
      ${renderInterest(example)}
      <p class="od-intro">${escapeHtml(intro)}</p>
      <table class="comparison-table">
        <colgroup><col><col><col><col></colgroup>
        <thead><tr>${programmeHeads}</tr></thead>
        <tbody>${blockRows}</tbody>
      </table>
      ${(comparisonNote || source) ? `<div class="od-page-note">${source}${source && comparisonNote ? ' · ' : ''}${escapeHtml(comparisonNote)}</div>` : ''}
    </main>
    ${renderFooter('<strong>UCR Pathways</strong> shows illustrative academic possibilities. The disciplinary programme and UCR pathways are compared on the same substantive basis.')}
  </section>`;
}

function renderSchedule(example) {
  const ucrProgrammes = example.programmes.filter(programme => !isComparator(programme));
  const heads = ucrProgrammes.map(programme => `<div class="schedule-programme-head">
    <span class="programme-label">${escapeHtml(programme.label)}</span>
    ${programme.subtitle ? `<span class="programme-subtitle">${escapeHtml(programme.subtitle)}</span>` : ''}
  </div>`).join('');

  const semesterCells = [];
  for (let semesterIndex = 0; semesterIndex < 6; semesterIndex += 1) {
    ucrProgrammes.forEach(programme => {
      const semester = programme.schedule.semesters[semesterIndex];
      const courses = semester.courses.map(course => `<li>${escapeHtml(course.name)}${course.level !== undefined ? ` <span class="course-level">· L${escapeHtml(course.level)}</span>` : ''}</li>`).join('');
      semesterCells.push(`<div class="schedule-cell${semesterIndex % 2 ? ' alt' : ''}">
        <h3 class="semester-label">${escapeHtml(semester.label)}</h3>
        <ul class="course-list">${courses}</ul>
      </div>`);
    });
  }

  const levelCounts = ucrProgrammes.map(programme => programme.schedule.semesters
    .flatMap(semester => semester.courses)
    .filter(course => Number(course.level) === 3).length);

  return `<section class="od-page" data-page="schedule">
    ${renderHeader(example, 'Your three feasible UCR programmes - semester by semester')}
    <main class="od-body schedule-body">
      ${renderInterest(example)}
      <p class="od-intro schedule-intro">The same three UCR pathways shown on page 1, arranged across six semesters with four courses in each semester.</p>
      <div class="schedule-grid">
        ${heads}
        ${semesterCells.join('')}
      </div>
      <div class="validation-strip"><strong>Structure checked</strong><span>24 unique courses per pathway · 4 per semester · level-3 courses: ${levelCounts.join(' · ')}</span></div>
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
<title>${escapeHtml(example.id)} - UCR Pathways - Open Day PDF</title>
<style>${css}</style>
</head>
<body>${renderComparison(example)}${renderSchedule(example)}</body>
</html>`;

  const out = path.join(outputDir, `${example.id}.html`);
  fs.writeFileSync(out, html, 'utf8');
  console.log(`Created ${path.relative(root, out)}`);
}
