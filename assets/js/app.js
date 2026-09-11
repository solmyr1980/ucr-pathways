const params = new URLSearchParams(window.location.search);
const hasExample = params.has('example');
const requestedId = (params.get('example') || '').toLowerCase();
const safeId = /^[a-z0-9-]+$/.test(requestedId) ? requestedId : '';
const UCR_COURSES_URL = 'https://ucr.nl/education/courses/';
const UCR_COURSE_EC = 7.5;

document.body.classList.add(hasExample ? 'example-mode' : 'landing-mode');

let example;
let current = 0;
let lastWide = window.innerWidth > 980;

const esc = (value = '') => String(value).replace(/[&<>"']/g, c => ({
  '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
}[c]));

function normalizeCell(cell) {
  if (cell === null || cell === undefined || cell === '') return null;
  if (typeof cell === 'string' && cell.trim()) return { text: cell };
  if (typeof cell === 'object' && typeof cell.text === 'string' && cell.text.trim()) return cell;
  return null;
}

function isComparator(programme) {
  return programme?.role === 'comparator';
}

function isUcr(programme) {
  return ['ucr-depth', 'ucr-balanced', 'ucr-thematic'].includes(programme?.role);
}

function safeExternalUrl(value) {
  try {
    const url = new URL(value);
    return ['https:', 'http:'].includes(url.protocol) ? url.href : '';
  } catch {
    return '';
  }
}

function comparatorMeta(record = example) {
  return record?.comparator || record?.referenceProgramme || {};
}

function visibleLabel(programme) {
  const comparator = comparatorMeta();
  const name = comparator.name || 'this programme';
  const institution = comparator.institution || '';
  if (programme.role === 'comparator') return institution ? `${name} at ${institution}` : name;
  if (programme.role === 'ucr-depth') return `Closest match to ${name}`;
  if (programme.role === 'ucr-balanced') return `${name} + related subjects`;
  if (programme.role === 'ucr-thematic') {
    return example?.origin === 'counselor'
      ? 'A broader programme around related interests'
      : 'A broader programme around your interests';
  }
  return programme.label || '';
}

function cellCredits(cell, programme) {
  if (cell?.credits !== undefined && cell?.credits !== null && String(cell.credits).trim()) {
    return `${cell.credits} EC`;
  }
  return isUcr(programme) ? `${UCR_COURSE_EC} EC` : '';
}

function programmeSource(programme) {
  if (isComparator(programme)) return safeExternalUrl(comparatorMeta().primarySourceUrl);
  return UCR_COURSES_URL;
}

function cellsForProgramme(block, programmeId) {
  return block.rows
    .map(row => normalizeCell(row.cells?.[programmeId]))
    .filter(Boolean);
}

function renderLanding(catalog) {
  const display = catalog.display || {};
  document.title = 'Study options at UCR';
  document.getElementById('programmeMeta').textContent = '';
  document.getElementById('landingTitle').textContent =
    display.title || 'See how different interests and bachelor choices can take shape at UCR.';
  document.getElementById('landingIntro').textContent = display.intro || '';
  document.getElementById('examplesTitle').textContent = display.examplesTitle || 'Selected comparisons';
  document.getElementById('examplesIntro').textContent = display.examplesIntro || '';

  const audienceCards = document.getElementById('audienceCards');
  audienceCards.innerHTML = (catalog.audiences || []).map(item => {
    const href = safeExternalUrl(item.href || '');
    const action = href
      ? `<a href="${esc(href)}" target="_blank" rel="noopener">${esc(item.action || 'Open tool')} →</a>`
      : `<span class="audience-status">${esc(item.status || 'Tool in development')}</span>`;
    return `<article class="audience-card"><h3>${esc(item.title)}</h3><p>${esc(item.description || '')}</p>${action}</article>`;
  }).join('');

  const cards = document.getElementById('exampleCards');
  cards.innerHTML = (catalog.examples || []).map(item => `
    <article class="example-card">
      <h3>${esc(item.title)}</h3>
      ${item.description ? `<p>${esc(item.description)}</p>` : ''}
      <a href="?example=${encodeURIComponent(item.id)}">View comparison →</a>
    </article>
  `).join('');

  document.getElementById('exampleView').hidden = true;
  document.getElementById('landingView').hidden = false;
}

function renderMeta() {
  const comparator = comparatorMeta();
  document.title = comparator.name ? `${comparator.name} | UCR comparison` : 'Programme comparison | UCR';
  document.getElementById('programmeMeta').textContent = example.cohort || '';
  document.getElementById('pageTitle').textContent =
    example.display?.publicTitle || 'See how this bachelor compares with study options at UCR.';

  const interestRow = document.getElementById('interestRow');
  const interests = example.interests || '';
  if (interests) {
    document.getElementById('interestLabel').textContent = `${example.display?.interestLabel || 'Starting interests'}:`;
    document.getElementById('interestText').textContent = ` ${interests}`;
    interestRow.hidden = false;
  } else {
    interestRow.hidden = true;
  }

  document.documentElement.style.setProperty('--programme-count', example.programmes.length);
}

function renderHead(programme) {
  const cls = isComparator(programme) ? 'program-head comparator' : 'program-head';
  const source = programmeSource(programme);
  const label = visibleLabel(programme);
  const title = source
    ? `<a href="${esc(source)}" target="_blank" rel="noopener">${esc(label)}</a>`
    : esc(label);
  const sourceText = isComparator(programme) ? 'Official programme ↗' : 'UCR courses ↗';
  return `<div class="${cls}"><strong>${title}</strong>${source ? `<a class="program-source" href="${esc(source)}" target="_blank" rel="noopener">${sourceText}</a>` : ''}</div>`;
}

function renderCompare() {
  const el = document.getElementById('compareView');
  let html = '<div class="compare-content"><div class="program-heads">';
  example.programmes.forEach(programme => { html += renderHead(programme); });
  html += '</div>';

  example.blocks.forEach(block => {
    html += `<div class="section-label">${esc(block.title)}</div><div class="rows">`;
    block.rows.forEach(row => {
      html += '<div class="row">';
      example.programmes.forEach(programme => {
        const cell = normalizeCell(row.cells?.[programme.id]);
        if (!cell) {
          html += '<div class="cell empty">&nbsp;</div>';
          return;
        }
        const classes = ['cell'];
        if (cell.emphasis) classes.push('emphasis');
        const ec = cellCredits(cell, programme);
        html += `<div class="${classes.join(' ')}">${esc(cell.text)}${ec ? `<span class="ec-badge">${esc(ec)}</span>` : ''}${cell.note ? `<span class="cell-note">${esc(cell.note)}</span>` : ''}</div>`;
      });
      html += '</div>';
    });
    html += '</div>';
  });

  const notes = (example.notes || []).filter(note => (!note.placement || note.placement === 'comparison') && note.text);
  notes.forEach(note => { html += `<div class="source-note">${esc(note.text)}</div>`; });

  html += '<div class="public-note">Blank cells indicate that no sufficiently comparable named component is shown in that position. The UCR programmes are illustrative feasible compositions, not official tracks or guaranteed future schedules.</div>';
  html += '</div>';
  el.innerHTML = html;
}

function renderDots() {
  const dots = document.getElementById('dots');
  dots.innerHTML = example.programmes.map((_, i) =>
    `<button class="dot ${i === current ? 'active' : ''}" type="button" data-i="${i}" aria-label="Programme ${i + 1}"></button>`
  ).join('');

  dots.querySelectorAll('.dot').forEach(dot => dot.addEventListener('click', () => {
    current = Number(dot.dataset.i);
    renderSingle();
  }));
}

function renderSingle() {
  const programme = example.programmes[current];
  const card = document.getElementById('singleCard');
  card.className = `single-card${isComparator(programme) ? ' comparator' : ''}`;
  const source = programmeSource(programme);
  const sourceText = isComparator(programme) ? 'Official programme ↗' : 'UCR courses ↗';

  let html = `<div class="single-header"><h2>${esc(visibleLabel(programme))}</h2>${source ? `<a class="program-source" href="${esc(source)}" target="_blank" rel="noopener">${sourceText}</a>` : ''}</div>`;

  example.blocks.forEach(block => {
    const items = cellsForProgramme(block, programme.id);
    if (!items.length) return;
    html += `<section class="single-section"><h3>${esc(block.title)}</h3><ul class="single-courses">`;
    items.forEach(item => {
      const ec = cellCredits(item, programme);
      html += `<li>${esc(item.text)}${ec ? `<span class="ec-badge">${esc(ec)}</span>` : ''}${item.note ? `<span class="single-course-note">${esc(item.note)}</span>` : ''}</li>`;
    });
    html += '</ul></section>';
  });

  if (programme.note) html += `<div class="single-footer">${esc(programme.note)}</div>`;
  card.innerHTML = html;
  document.getElementById('positionTitle').textContent = `${current + 1} of ${example.programmes.length}`;
  document.getElementById('prevBtn').disabled = current === 0;
  document.getElementById('nextBtn').disabled = current === example.programmes.length - 1;
  renderDots();
}

function setView(mode) {
  const compare = document.getElementById('compareView');
  const single = document.getElementById('singleView');
  const compareBtn = document.getElementById('compareBtn');
  const singleBtn = document.getElementById('singleBtn');

  if (mode === 'single') {
    compare.style.display = 'none';
    single.style.display = 'block';
    compareBtn.classList.remove('active');
    singleBtn.classList.add('active');
  } else {
    compare.style.display = 'block';
    single.style.display = 'none';
    compareBtn.classList.add('active');
    singleBtn.classList.remove('active');
  }
}

function bindInteractions() {
  document.getElementById('compareBtn').addEventListener('click', () => setView('compare'));
  document.getElementById('singleBtn').addEventListener('click', () => setView('single'));
  document.getElementById('prevBtn').addEventListener('click', () => { if (current > 0) { current -= 1; renderSingle(); } });
  document.getElementById('nextBtn').addEventListener('click', () => { if (current < example.programmes.length - 1) { current += 1; renderSingle(); } });

  document.addEventListener('keydown', event => {
    const singleVisible = getComputedStyle(document.getElementById('singleView')).display !== 'none';
    if (!singleVisible) return;
    if (event.key === 'ArrowLeft' && current > 0) { current -= 1; renderSingle(); }
    if (event.key === 'ArrowRight' && current < example.programmes.length - 1) { current += 1; renderSingle(); }
  });

  let touchStartX = null;
  const card = document.getElementById('singleCard');
  card.addEventListener('touchstart', event => { touchStartX = event.changedTouches[0].clientX; }, { passive: true });
  card.addEventListener('touchend', event => {
    if (touchStartX === null) return;
    const dx = event.changedTouches[0].clientX - touchStartX;
    touchStartX = null;
    if (Math.abs(dx) < 45) return;
    if (dx < 0 && current < example.programmes.length - 1) { current += 1; renderSingle(); }
    if (dx > 0 && current > 0) { current -= 1; renderSingle(); }
  }, { passive: true });

  window.addEventListener('resize', () => {
    const wide = window.innerWidth > 980;
    if (wide !== lastWide) {
      lastWide = wide;
      setView(wide ? 'compare' : 'single');
    }
  });
}

function showLoadError(message, error) {
  document.getElementById('landingView').hidden = true;
  document.getElementById('exampleView').hidden = true;
  const box = document.getElementById('loadError');
  box.hidden = false;
  const localHint = window.location.protocol === 'file:'
    ? ' This data-driven version must be opened through a web server; GitHub Pages will serve it correctly.'
    : '';
  box.textContent = `${message}${localHint}`;
  console.error(error);
}

async function loadJson(path) {
  const response = await fetch(path, { cache: 'no-store' });
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  return response.json();
}

async function initLanding() {
  try {
    const catalog = await loadJson('./data/catalog.json');
    renderLanding(catalog);
  } catch (error) {
    showLoadError('Could not load the selected UCR comparisons.', error);
  }
}

async function initExample() {
  if (!safeId) {
    showLoadError(`Could not load comparison “${requestedId}”.`, new Error('Invalid example id'));
    return;
  }

  try {
    example = await loadJson(`./data/examples/${safeId}.json`);
    document.getElementById('landingView').hidden = true;
    document.getElementById('exampleView').hidden = false;
    renderMeta();
    renderCompare();
    renderSingle();
    bindInteractions();
    setView(window.innerWidth <= 980 ? 'single' : 'compare');
  } catch (error) {
    showLoadError(`Could not load comparison “${safeId}”.`, error);
  }
}

if (hasExample) initExample();
else initLanding();
