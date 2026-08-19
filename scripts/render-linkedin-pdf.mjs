import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { exampleFiles, readExample } from './example-utils.mjs';

const root = process.cwd();
const target = process.argv[2] || 'all';
const outputDir = path.join(root, 'output', 'linkedin');
fs.mkdirSync(outputDir, { recursive: true });

function countPdfPages(pdfPath) {
  const raw = fs.readFileSync(pdfPath).toString('latin1');
  return (raw.match(/\/Type\s*\/Page\b/g) || []).length;
}

const browser = await chromium.launch({ headless: true });

try {
  for (const file of exampleFiles(root, target)) {
    const example = readExample(file);
    const htmlPath = path.join(outputDir, `${example.id}.html`);
    const pdfPath = path.join(outputDir, `${example.id}.pdf`);
    if (!fs.existsSync(htmlPath)) throw new Error(`Missing ${path.relative(root, htmlPath)}. Run build-linkedin-html.mjs first.`);

    const page = await browser.newPage();
    await page.goto(pathToFileURL(htmlPath).href, { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);

    const layout = await page.evaluate(() => {
      const pages = [...document.querySelectorAll('.page')];
      const tolerance = 1;
      const densityModes = [
        { name: 'normal', className: null },
        { name: 'compact', className: 'density-compact' },
        { name: 'dense', className: 'density-dense' }
      ];

      function applyDensity(pageEl, className) {
        pageEl.classList.remove('density-compact', 'density-dense');
        if (className) pageEl.classList.add(className);
        void pageEl.offsetHeight;
      }

      function findIssues(pageEl, pageIndex) {
        const issues = [];
        const pageRect = pageEl.getBoundingClientRect();

        if (pageEl.scrollHeight > pageEl.clientHeight + tolerance || pageEl.scrollWidth > pageEl.clientWidth + tolerance) {
          issues.push(`page ${pageIndex + 1} overflow (${pageEl.scrollWidth}x${pageEl.scrollHeight} vs ${pageEl.clientWidth}x${pageEl.clientHeight})`);
        }

        [...pageEl.querySelectorAll('*')].forEach(el => {
          const rect = el.getBoundingClientRect();
          if (rect.width === 0 && rect.height === 0) return;
          if (rect.right > pageRect.right + tolerance || rect.bottom > pageRect.bottom + tolerance || rect.left < pageRect.left - tolerance || rect.top < pageRect.top - tolerance) {
            issues.push(`page ${pageIndex + 1}: ${el.tagName.toLowerCase()}.${el.className || ''} extends outside page`);
          }
        });

        return [...new Set(issues)];
      }

      const results = pages.map((pageEl, pageIndex) => {
        let finalIssues = [];
        for (const mode of densityModes) {
          applyDensity(pageEl, mode.className);
          finalIssues = findIssues(pageEl, pageIndex);
          if (!finalIssues.length) return { page: pageIndex + 1, density: mode.name, issues: [] };
        }
        return { page: pageIndex + 1, density: 'dense', issues: finalIssues };
      });

      return { pageCount: pages.length, results };
    });

    if (layout.pageCount !== example.programmes.length) {
      throw new Error(`${example.id}: LinkedIn HTML must contain ${example.programmes.length} pages; found ${layout.pageCount}.`);
    }

    const failures = layout.results.filter(result => result.issues.length);
    if (failures.length) {
      const messages = failures.flatMap(result => result.issues);
      throw new Error(`${example.id}: LinkedIn layout still overflows at maximum density:\n${messages.join('\n')}`);
    }

    await page.pdf({
      path: pdfPath,
      printBackground: true,
      preferCSSPageSize: true,
      margin: { top: 0, right: 0, bottom: 0, left: 0 }
    });
    await page.close();

    const pdfPages = countPdfPages(pdfPath);
    if (pdfPages !== example.programmes.length) {
      throw new Error(`${example.id}: rendered LinkedIn PDF must contain ${example.programmes.length} pages; found ${pdfPages}.`);
    }

    const densities = layout.results.map(result => `page ${result.page}: ${result.density}`).join(', ');
    console.log(`Created ${path.relative(root, pdfPath)} (${pdfPages} pages; ${densities}; no detected clipping)`);
  }
} finally {
  await browser.close();
}
