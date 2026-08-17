import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';

const root = process.cwd();
const source = fs.readFileSync(path.join(root, 'index.html'), 'utf8');

function between(text, start, end) {
  const a = text.indexOf(start);
  if (a < 0) throw new Error(`Could not find: ${start}`);
  const b = text.indexOf(end, a + start.length);
  if (b < 0) throw new Error(`Could not find: ${end}`);
  return text.slice(a + start.length, b).trim();
}

const programmesLiteral = between(source, 'const programmes = ', ';\n\nconst sections = ');
const sectionsLiteral = between(source, 'const sections = ', ';\n\nfunction escapeHtml');
const programmes = vm.runInNewContext(`(${programmesLiteral})`);
const sections = vm.runInNewContext(`(${sectionsLiteral})`);

const interestMatch = source.match(/<p class="interests">([\s\S]*?)<\/p>/);
const metaMatch = source.match(/<div class="meta">([\s\S]*?)<\/div>/);
const interestHtml = interestMatch ? interestMatch[1].trim() : '';
const metaHtml = metaMatch ? metaMatch[1].trim() : '';

const esc = (value = '') => String(value).replace(/[&<>"']/g, c => ({
  '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
}[c]));

const pages = programmes.map((programme, i) => {
  const sectionHtml = sections.map(section => {
    const courses = section.rows.map(row => row[i]).filter(Boolean);
    if (!courses.length) return '';
    return `<section class="section">
      <h2>${esc(section.title)}</h2>
      <ul>${courses.map(course => `<li>${esc(course)}</li>`).join('')}</ul>
    </section>`;
  }).join('\n');

  return `<article class="page ${i === 0 ? 'traditional' : ''}">
    <header class="card-head">
      <div class="kicker">${metaHtml}</div>
      <h1>${esc(programme.title)}</h1>
      <p>${esc(programme.subtitle)}</p>
    </header>
    <div class="interest">${interestHtml}</div>
    <div class="content">${sectionHtml}</div>
    <footer>${i + 1} / ${programmes.length} &nbsp; · &nbsp; UCR Program Builder</footer>
  </article>`;
}).join('\n');

const html = `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>UCR Program Builder - LinkedIn PDF</title>
<style>
  @page { size: 8in 10in; margin: 0; }
  * { box-sizing: border-box; }
  html, body { margin: 0; padding: 0; font-family: Arial, Helvetica, sans-serif; color: #17212b; }
  body { background: white; }
  .page { width: 8in; height: 10in; break-after: page; page-break-after: always; overflow: hidden; display: flex; flex-direction: column; background: #fff; }
  .page:last-child { break-after: auto; page-break-after: auto; }
  .card-head { background: #2f78a5; color: white; padding: .34in .42in .28in; }
  .traditional .card-head { background: #173b5a; }
  .kicker { font-size: 9pt; opacity: .82; margin-bottom: .08in; }
  h1 { margin: 0; font-size: 25pt; line-height: 1.05; letter-spacing: -.4pt; }
  .card-head p { margin: .07in 0 0; font-size: 11pt; opacity: .92; }
  .interest { padding: .16in .42in; border-bottom: 1px solid #dbe3e9; font-size: 10.5pt; color: #687684; }
  .interest strong { color: #17212b; }
  .content { flex: 1; padding: .10in .42in .02in; display: flex; flex-direction: column; gap: .05in; }
  .section { break-inside: avoid; }
  .section h2 { margin: 0; padding: .055in .09in; background: #eef4f7; color: #29475e; font-size: 10pt; line-height: 1.15; }
  ul { list-style: none; margin: 0; padding: 0; }
  li { padding: .045in .09in; border-bottom: 1px solid #edf1f4; font-size: 8.7pt; line-height: 1.12; }
  footer { padding: .09in .42in .12in; border-top: 1px solid #dbe3e9; color: #687684; font-size: 8pt; }
</style>
</head>
<body>${pages}</body>
</html>`;

fs.mkdirSync(path.join(root, 'output'), { recursive: true });
fs.writeFileSync(path.join(root, 'output', 'linkedin.html'), html, 'utf8');
console.log('Created output/linkedin.html');
