#!/usr/bin/env node
/**
 * Renders the LinkedIn Featured carousel from carousel.html and copy.json.
 *
 *   node linkedin-start-here-carousel/source/build-carousel.mjs
 *
 * Same production method as the rest of the Capability Formation visuals: the
 * page is served over http so the /fonts/ URLs in fonts.css and the approved
 * portrait in /images/ resolve, each slide is captured on its own, and the PDF
 * is printed from the same DOM so its text stays vector.
 */
import { chromium } from 'playwright';
import { createServer } from 'node:http';
import { readFile, mkdir } from 'node:fs/promises';
import { extname, join, normalize } from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = fileURLToPath(new URL('.', import.meta.url));
const OUT = join(HERE, '..');
const ROOT = join(HERE, '..', '..');
const PDF_NAME = 'LinkedIn_Start_Here_Capability_Formation.pdf';

const MIME = {
  '.html': 'text/html; charset=utf-8', '.css': 'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8', '.woff2': 'font/woff2', '.png': 'image/png',
};
const server = createServer(async (req, res) => {
  const f = join(ROOT, normalize(decodeURIComponent(new URL(req.url, 'http://x').pathname)));
  if (!f.startsWith(ROOT)) return void res.writeHead(403).end();
  try { res.writeHead(200, { 'content-type': MIME[extname(f)] ?? 'application/octet-stream' }); res.end(await readFile(f)); }
  catch { res.writeHead(404).end(); }
});
const port = await new Promise(r => server.listen(0, '127.0.0.1', () => r(server.address().port)));

const copy = JSON.parse(await readFile(join(HERE, 'copy.json'), 'utf8'));
const { w: W, h: H } = copy.canvas;

await mkdir(join(OUT, 'slides'), { recursive: true });
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: W, height: H } });
const url = `http://127.0.0.1:${port}/linkedin-start-here-carousel/source/carousel.html`;
await page.goto(url, { waitUntil: 'networkidle' });
await page.waitForFunction(() => document.documentElement.dataset.ready === 'true');

const count = await page.evaluate(() => document.querySelectorAll('.slide').length);
if (count !== copy.slides.length) throw new Error(`rendered ${count} slides, copy has ${copy.slides.length}`);

// One slide per capture: eight stacked slides are taller than the viewport, and
// an element screenshot of a slide taller than the viewport truncates.
for (let i = 0; i < count; i++) {
  await page.evaluate(n => {
    document.querySelectorAll('.slide').forEach((el, k) => { el.style.display = k === n ? '' : 'none'; });
  }, i);
  await page.evaluate(() => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r))));
  await page.screenshot({ path: join(OUT, 'slides', `slide-${String(i + 1).padStart(2, '0')}.png`), type: 'png' });
}
await page.evaluate(() => { document.querySelectorAll('.slide').forEach(el => { el.style.display = ''; }); });
console.log(`wrote slides/slide-01.png to slide-${String(count).padStart(2, '0')}.png  ${W}x${H}`);

await page.addStyleTag({ content: `@page { size: ${W}px ${H}px; margin: 0; }` });
await page.pdf({ path: join(OUT, PDF_NAME), width: `${W}px`, height: `${H}px`,
                 printBackground: true, pageRanges: `1-${count}` });
console.log(`wrote ${PDF_NAME}  ${count} pages`);

// Contact sheet: all eight slides in order, four across.
await page.setViewportSize({ width: 1240, height: 1400 });
await page.setContent(`<style>
  body { margin: 0; background: #fff; width: 1240px; font-family: system-ui, sans-serif; }
  .wrap { padding: 48px 48px 40px; }
  h1 { font-size: 24px; color: #0F2347; margin-bottom: 4px; }
  .sub { font-size: 14px; color: rgba(15,35,71,.6); margin-bottom: 32px; }
  .grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 22px; }
  figure { margin: 0; }
  img { width: 100%; display: block; border: 1px solid rgba(15,35,71,.15); }
  figcaption { margin-top: 8px; font-size: 12px; color: rgba(15,35,71,.65); }
</style>
<div class="wrap">
  <h1>START HERE: Does what you have already done still count?</h1>
  <div class="sub">LinkedIn Featured carousel, ${count} slides, ${W} x ${H} portrait.</div>
  <div class="grid">${Array.from({ length: count }, (_, i) => {
    const n = String(i + 1).padStart(2, '0');
    return `<figure><img src="http://127.0.0.1:${port}/linkedin-start-here-carousel/slides/slide-${n}.png">
            <figcaption>slide-${n}.png</figcaption></figure>`;
  }).join('')}</div>
</div>`, { waitUntil: 'networkidle' });
await (await page.$('.wrap')).screenshot({ path: join(OUT, 'contact-sheet.png') });
console.log('wrote contact-sheet.png');

await browser.close();
server.close();
