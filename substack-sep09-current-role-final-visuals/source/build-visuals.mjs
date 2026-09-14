#!/usr/bin/env node
/**
 * Renders the three Substack visuals for "What Your Current Role Should Be
 * Doing for Your Future" from visuals.html and copy.json.
 *
 *   node substack-sep09-current-role-final-visuals/source/build-visuals.mjs
 *
 * The page is served over http rather than opened from disk so that the
 * /fonts/ URLs inside fonts.css and the real Career Evidence Starter page
 * renders in the repository root both resolve.
 */
import { chromium } from 'playwright';
import { createServer } from 'node:http';
import { readFile, mkdir } from 'node:fs/promises';
import { extname, join, normalize } from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = fileURLToPath(new URL('.', import.meta.url));
const OUT = join(HERE, '..');
const ROOT = join(HERE, '..', '..');

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.woff2': 'font/woff2',
  '.png': 'image/png',
};

const server = createServer(async (req, res) => {
  const path = normalize(decodeURIComponent(new URL(req.url, 'http://x').pathname));
  const file = join(ROOT, path);
  if (!file.startsWith(ROOT)) return void res.writeHead(403).end();
  try {
    res.writeHead(200, { 'content-type': MIME[extname(file)] ?? 'application/octet-stream' });
    res.end(await readFile(file));
  } catch { res.writeHead(404).end(); }
});
const port = await new Promise(r => server.listen(0, '127.0.0.1', () => r(server.address().port)));

const copy = JSON.parse(await readFile(join(HERE, 'copy.json'), 'utf8'));
const SHEETS = [
  ['cover', copy.cover],
  ['threeps', copy.threePs],
  ['starter', copy.starter],
];

await mkdir(OUT, { recursive: true });
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1600, height: 1000 } });
await page.goto(`http://127.0.0.1:${port}/substack-sep09-current-role-final-visuals/source/visuals.html`,
                { waitUntil: 'networkidle' });
await page.waitForFunction(() => document.documentElement.dataset.ready === 'true');

// Each sheet is captured on its own: the three stack to 2900px on one page, and
// an element screenshot of a sheet taller than the viewport truncates.
for (const [id, spec] of SHEETS) {
  await page.setViewportSize({ width: spec.canvas.w, height: spec.canvas.h });
  await page.evaluate(only => {
    for (const el of document.querySelectorAll('.sheet')) el.style.display = el.id === only ? '' : 'none';
  }, id);
  await page.evaluate(() => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r))));
  await page.screenshot({ path: join(OUT, spec.file), type: 'png' });
  console.log(`wrote ${spec.file}  ${spec.canvas.w}x${spec.canvas.h}`);
}
await page.evaluate(() => { for (const el of document.querySelectorAll('.sheet')) el.style.display = ''; });

// Contact sheet: all three together, so the set can be judged as one.
await page.setViewportSize({ width: 1240, height: 1500 });
await page.setContent(`<style>
  body { margin: 0; background: #FFFFFF; font-family: system-ui, sans-serif; width: 1240px; }
  .wrap { padding: 56px 56px 48px; }
  h1 { font-size: 26px; font-weight: 600; color: #0F2347; margin-bottom: 6px; }
  .sub { font-size: 15px; color: rgba(15,35,71,0.6); margin-bottom: 40px; }
  figure { margin: 0 0 40px; }
  img { width: 100%; display: block; border: 1px solid rgba(15,35,71,0.14); }
  figcaption { margin-top: 12px; font-size: 14px; color: rgba(15,35,71,0.7); }
  b { color: #0F2347; }
</style>
<div class="wrap">
  <h1>What Your Current Role Should Be Doing for Your Future</h1>
  <div class="sub">Substack visual package, September 9, 2026. Three assets: one cover, two in body.</div>
  ${SHEETS.map(([, s], i) => `<figure>
    <img src="http://127.0.0.1:${port}/substack-sep09-current-role-final-visuals/${s.file}">
    <figcaption><b>${s.file}</b> &nbsp;·&nbsp; ${s.canvas.w} x ${s.canvas.h} &nbsp;·&nbsp; ${
      i === 0 ? 'cover and social preview only, not inside the essay' : 'in body'
    }</figcaption>
  </figure>`).join('')}
</div>`, { waitUntil: 'networkidle' });
await page.screenshot({ path: join(OUT, 'contact-sheet.png'), fullPage: true });
console.log('wrote contact-sheet.png');

await browser.close();
server.close();
