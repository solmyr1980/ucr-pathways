import fs from 'node:fs';
import path from 'node:path';
import {
  exampleFiles,
  readExample,
  validateExample,
  normalizeCell,
  isComparator,
  isUcrProgramme,
  comparatorMetadata,
  visibleProgrammeLabel,
  linkedinProgrammes,
  escapeHtml,
  UCR_DEFAULT_COURSE_EC
} from './example-utils.mjs';

const root = process.cwd();
const target = process.argv[2] || 'all';
const ucrCoursesUrl = 'https://ucr.nl/education/courses/';

const css = [
  fs.readFileSync(path.join(root, 'assets', 'css', 'linkedin.css'), 'utf8'),
  fs.readFileSync(path.join(root, 'assets', 'css', 'linkedin-alignment.css'), 'utf8')
].join('\n');

const outputDir = path.join(root, 'output', 'linkedin');
fs.mkdirSync(outputDir, { recursive: true });

function creditLabel(item, programme) {
  if (item?.credits !== undefined && item?.credits !== null && String(item.credits).trim()) {
    return `${item.credits} EC`;
  }
  return isUcrProgramme(programme) ? `${UCR_DEFAULT_COURSE_EC} EC` : '';
}

for (const file of exampleFiles(root, target)) {
  const example = readExample(file);
  const { errors, warnings } = validateExample(example, path.basename(file));

  warnings.forEach(message => console.warn(`WARNING: ${message}`));
  if (errors.length) throw new Error(errors.join('\n'));

  const interestLabel = example.display?.interestLabel || 'Starting interests';
  const meta = example.cohort || '';
  const programmes = linkedinProgrammes(example);
  const comparator = comparatorMetadata(example);

  const pages = programmes.map((programme, index) => {
    const sections = example.blocks.map(block => {
      const items = block.rows
        .map(row => normalizeCell(row.cells?.[programme.id]))
        .filter(Boolean);

      if (!items.length) return '';

      return `<section class="section">
        <h2>${escapeHtml(block.title)}</h2>
        <ul>${items.map(item => {
          const ec = creditLabel(item, programme);
          return `<li>${escapeHtml(item.text)}${ec ? ` <span class="item-note">· ${escapeHtml(ec)}</span>` : ''}${item.note ? `<span class="item-note">${escapeHtml(item.note)}</span>` : ''}</li>`;
        }).join('')}</ul>
      </section>`;
    }).join('\n');

    const sourceUrl = isComparator(programme) ? comparator.primarySourceUrl : ucrCoursesUrl;
    const sourceLabel = isComparator(programme) ? 'Official programme' : 'UCR courses';
    const source = sourceUrl
      ? `<div class="reference-programme"><a href="${escapeHtml(sourceUrl)}">${escapeHtml(sourceLabel)} ↗</a></div>`
      : '';

    const interest = example.interests
      ? `<div class="interest">${escapeHtml(interestLabel)}: <strong>${escapeHtml(example.interests)}</strong></div>`
      : '';

    return `<article class="page${isComparator(programme) ? ' comparator' : ''}">
      <header class="card-head">
        ${meta ? `<div class="kicker">${escapeHtml(meta)}</div>` : ''}
        <h1>${escapeHtml(visibleProgrammeLabel(example, programme))}</h1>
      </header>
      ${interest}
      ${source}
      <div class="content">${sections}</div>
      ${programme.note ? `<div class="programme-note">${escapeHtml(programme.note)}</div>` : ''}
      <footer>${index + 1} / ${programmes.length} &nbsp; · &nbsp; University College Roosevelt</footer>
    </article>`;
  }).join('\n');

  const html = `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>${escapeHtml(example.id.toUpperCase())} - UCR comparison - LinkedIn PDF</title>
<style>${css}</style>
</head>
<body>${pages}</body>
</html>`;

  const out = path.join(outputDir, `${example.id}.html`);
  fs.writeFileSync(out, html, 'utf8');
  console.log(`Created ${path.relative(root, out)}`);
}
