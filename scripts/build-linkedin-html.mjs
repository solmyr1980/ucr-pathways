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
const css = fs.readFileSync(path.join(root, 'assets', 'css', 'linkedin.css'), 'utf8');
const outputDir = path.join(root, 'output', 'linkedin');
fs.mkdirSync(outputDir, { recursive: true });

for (const file of exampleFiles(root, target)) {
  const example = readExample(file);
  const { errors, warnings } = validateExample(example, path.basename(file));
  warnings.forEach(message => console.warn(`WARNING: ${message}`));
  if (errors.length) throw new Error(errors.join('\n'));

  const interestLabel = example.display?.interestLabel || 'Your interests';
  const meta = [example.id.toUpperCase(), example.cohort].filter(Boolean).join(' | ');

  const pages = example.programmes.map((programme, index) => {
    const sections = example.blocks.map(block => {
      const items = block.rows
        .map(row => normalizeCell(row.cells?.[programme.id]))
        .filter(Boolean);
      if (!items.length) return '';
      return `<section class="section">
        <h2>${escapeHtml(block.title)}</h2>
        <ul>${items.map(item => `<li>${escapeHtml(item.text)}${item.note ? `<span class="item-note">${escapeHtml(item.note)}</span>` : ''}</li>`).join('')}</ul>
      </section>`;
    }).join('\n');

    return `<article class="page${isComparator(programme) ? ' comparator' : ''}">
      <header class="card-head">
        <div class="kicker">${escapeHtml(meta)}</div>
        <h1>${escapeHtml(programme.label)}</h1>
        ${programme.subtitle ? `<p>${escapeHtml(programme.subtitle)}</p>` : ''}
      </header>
      <div class="interest">${escapeHtml(interestLabel)}: <strong>${escapeHtml(example.interests)}</strong></div>
      <div class="content">${sections}</div>
      ${programme.note ? `<div class="programme-note">${escapeHtml(programme.note)}</div>` : ''}
      <footer>${index + 1} / ${example.programmes.length} &nbsp; · &nbsp; UCR Program Builder</footer>
    </article>`;
  }).join('\n');

  const html = `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>${escapeHtml(example.id.toUpperCase())} - UCR Program Builder - LinkedIn PDF</title>
<style>${css}</style>
</head>
<body>${pages}</body>
</html>`;

  const out = path.join(outputDir, `${example.id}.html`);
  fs.writeFileSync(out, html, 'utf8');
  console.log(`Created ${path.relative(root, out)}`);
}
