import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const htmlPath = path.join(root, 'output', 'linkedin.html');
const pdfPath = path.join(root, 'output', 'ucr-program-builder-linkedin.pdf');
const html = fs.readFileSync(htmlPath, 'utf8');

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage();
await page.setContent(html, { waitUntil: 'load' });
await page.pdf({
  path: pdfPath,
  printBackground: true,
  preferCSSPageSize: true,
  margin: { top: 0, right: 0, bottom: 0, left: 0 }
});
await browser.close();

console.log('Created output/ucr-program-builder-linkedin.pdf');
