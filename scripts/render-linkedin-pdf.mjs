import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';
import { exampleFiles, readExample } from './example-utils.mjs';

const root = process.cwd();
const target = process.argv[2] || 'all';
const outputDir = path.join(root, 'output', 'linkedin');
fs.mkdirSync(outputDir, { recursive: true });

const browser = await chromium.launch({ headless: true });

try {
  for (const file of exampleFiles(root, target)) {
    const example = readExample(file);
    const htmlPath = path.join(outputDir, `${example.id}.html`);
    const pdfPath = path.join(outputDir, `${example.id}.pdf`);
    if (!fs.existsSync(htmlPath)) throw new Error(`Missing ${path.relative(root, htmlPath)}. Run build-linkedin-html.mjs first.`);

    const html = fs.readFileSync(htmlPath, 'utf8');
    const page = await browser.newPage();
    await page.setContent(html, { waitUntil: 'load' });
    await page.pdf({
      path: pdfPath,
      printBackground: true,
      preferCSSPageSize: true,
      margin: { top: 0, right: 0, bottom: 0, left: 0 }
    });
    await page.close();
    console.log(`Created ${path.relative(root, pdfPath)}`);
  }
} finally {
  await browser.close();
}
