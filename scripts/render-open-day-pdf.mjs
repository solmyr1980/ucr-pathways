import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { exampleFiles, readExample } from './example-utils.mjs';

const root = process.cwd();
const target = process.argv[2] || 'all';
const outputDir = path.join(root, 'output', 'open-day');
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
    if (!fs.existsSync(htmlPath)) {
      throw new Error(`Missing ${path.relative(root, htmlPath)}. Run build-open-day-html.mjs first.`);
    }

    const page = await browser.newPage({ viewport: { width: 1200, height: 1600 } });
    await page.goto(pathToFileURL(htmlPath).href, { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);

    const layout = await page.evaluate(() => {
      const pages = [...document.querySelectorAll('.od-page')];
      const issues = [];
      const tolerance = 1;

      pages.forEach((pageEl, pageIndex) => {
        const pageRect = pageEl.getBoundingClientRect();
        if (pageEl.scrollHeight > pageEl.clientHeight + tolerance || pageEl.scrollWidth > pageEl.clientWidth + tolerance) {
          issues.push(`page ${pageIndex + 1} scroll overflow (${pageEl.scrollWidth}x${pageEl.scrollHeight} vs ${pageEl.clientWidth}x${pageEl.clientHeight})`);
        }

        [...pageEl.querySelectorAll('*')].forEach(el => {
          const rect = el.getBoundingClientRect();
          if (rect.width === 0 && rect.height === 0) return;
          if (rect.right > pageRect.right + tolerance || rect.bottom > pageRect.bottom + tolerance || rect.left < pageRect.left - tolerance || rect.top < pageRect.top - tolerance) {
            issues.push(`page ${pageIndex + 1}: ${el.tagName.toLowerCase()}.${el.className || ''} extends outside page`);
          }
        });
      });

      return { pageCount: pages.length, issues: [...new Set(issues)] };
    });

    if (layout.pageCount !== 2) {
      throw new Error(`${example.id}: Open Day HTML must contain exactly 2 pages; found ${layout.pageCount}.`);
    }
    if (layout.issues.length) {
      throw new Error(`${example.id}: Open Day layout overflow detected:\n${layout.issues.join('\n')}`);
    }

    await page.pdf({
      path: pdfPath,
      printBackground: true,
      preferCSSPageSize: true,
      margin: { top: 0, right: 0, bottom: 0, left: 0 }
    });
    await page.close();

    const pdfPages = countPdfPages(pdfPath);
    if (pdfPages !== 2) {
      throw new Error(`${example.id}: rendered Open Day PDF must contain exactly 2 pages; found ${pdfPages}.`);
    }

    console.log(`Created ${path.relative(root, pdfPath)} (2 pages, no detected overflow)`);
  }
} finally {
  await browser.close();
}
