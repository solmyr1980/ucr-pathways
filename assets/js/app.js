const params = new URLSearchParams(window.location.search);
const requestedId = (params.get('example') || 'p-001').toLowerCase();
const safeId = /^[a-z0-9-]+$/.test(requestedId) ? requestedId : 'p-001';

let example;
let current = 0;
let lastWide = window.innerWidth > 980;

const esc = (value = '') => String(value).replace(/[&<>"']/g, c => ({
  '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
}[c]));

function normalizeCell(cell) {
  if (cell === null || cell === undefined || cell === '') return null;
  if (typeof cell === 'string') return { text: cell };
  if (typeof cell === 'object' && typeof cell.text === 'string' && cell.text.trim()) return cell;
  return null;
}

function isComparator(programme) {
  return programme.role === 'comparator' || programme.family === 'comparator' || programme.accent === 'comparator';
}

function cellsForProgramme(block, programmeId) {
  return block.rows
    .map(row => normalizeCell(row.cells?.[programmeId]))
    .filter(Boolean);
}

function renderMeta() {
  const display = example.display || {};
  document.title = `${example.id.toUpperCase()} | UCR Program Builder`;
  document.getElementById('programmeMeta').textContent = [example.id.toUpperCase(), example.cohort].filter(Boolean).join(' | ');
  document.getElementById('pageTitle').textContent = display.title || 'Four ways to study the same interests';
  document.getElementById('interestLabel').textContent = `${display.interestLabel || 'Your interests'}:`;
  document.getElementById('interestText').textContent = ` ${example.interests}`;
  document.getElementById('spectrumLeft').textContent = display.spectrum?.left || 'more disciplinary depth';
  document.getElementById('spectrumRight').textContent = display.spectrum?.right || 'more interdisciplinary breadth';
  document.documentElement.style.setProperty('--programme-count', example.programmes.length);
}

function renderCompare() {
  const el = document.getElementById('compareView');
  let html = '<div class="compare-content"><div class="program-heads">';

  example.programmes.forEach(programme => {
    const cls = isComparator(programme) ? 'program-head comparator' : 'program-head';
    html += `<div class="${cls}"><strong>${esc(programme.label)}</strong>${programme.subtitle ? `<span>${esc(programme.subtitle)}</span>` : ''}</div>`;
  });

  html += '</div>';
  if (example.display?.comparisonNote) {
    html += `<div class="compare-note">${esc(example.display.comparisonNote)}</div>`;
  }

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
        html += `<div class="${classes.join(' ')}">${esc(cell.text)}${cell.note ? `<span class="cell-note">${esc(cell.note)}</span>` : ''}</div>`;
      });
      html += '</div>';
    });
    html += '</div>';
  });

  const notes = (example.notes || []).filter(note => !note.placement || note.placement === 'comparison');
  notes.forEach(note => { html += `<div class="source-note">${esc(note.text)}</div>`; });

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

  let html = `<div class="single-header"><h2>${esc(programme.label)}</h2>${programme.subtitle ? `<p>${esc(programme.subtitle)}</p>` : ''}</div>`;

  example.blocks.forEach(block => {
    const items = cellsForProgramme(block, programme.id);
    if (!items.length) return;
    html += `<section class="single-section"><h3>${esc(block.title)}</h3><ul class="single-courses">`;
    items.forEach(item => {
      html += `<li>${esc(item.text)}${item.note ? `<span class="single-course-note">${esc(item.note)}</span>` : ''}</li>`;
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
  document.getElementById('prevBtn').addEventListener('click', () => {
    if (current > 0) { current -= 1; renderSingle(); }
  });
  document.getElementById('nextBtn').addEventListener('click', () => {
    if (current < example.programmes.length - 1) { current += 1; renderSingle(); }
  });

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

function showLoadError(error) {
  document.getElementById('compareView').hidden = true;
  document.getElementById('singleView').hidden = true;
  document.querySelector('.spectrum').hidden = true;
  const box = document.getElementById('loadError');
  box.hidden = false;
  const localHint = window.location.protocol === 'file:'
    ? ' This data-driven version must be opened through a web server; GitHub Pages will serve it correctly after you push the repository.'
    : '';
  box.textContent = `Could not load example “${safeId}”.${localHint}`;
  console.error(error);
}

async function init() {
  try {
    const response = await fetch(`./data/examples/${safeId}.json`, { cache: 'no-store' });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    example = await response.json();
    renderMeta();
    renderCompare();
    renderSingle();
    bindInteractions();
    setView(window.innerWidth <= 980 ? 'single' : 'compare');
  } catch (error) {
    showLoadError(error);
  }
}

init();
