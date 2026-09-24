#!/usr/bin/env node
/** All eight slides on one sheet, four across. */
import { chromium } from 'playwright';
import { readFile } from 'node:fs/promises';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = fileURLToPath(new URL('.', import.meta.url));
const ROOT = join(HERE, '..');
const REPO = '/home/user/temidayoafonja-site';
const C = JSON.parse(await readFile(join(HERE, 'copy.json'), 'utf8'));

const uri = async f => `data:image/png;base64,${(await readFile(join(ROOT, 'slides', f))).toString('base64')}`;
const LABELS = C.slides.map(s => s.mode === 'cover' ? 'Cover'
  : s.mode === 'close' ? 'Close' : s.number ? `${s.number} ${s.headline}` : 'Statement');

const cells = (await Promise.all(LABELS.map(async (label, i) => {
  const n = `0${i + 1}`;
  return `<figure><img src="${await uri(`slide-${n}.png`)}">
    <figcaption><b>${n}</b><span>${label}</span></figcaption></figure>`;
}))).join('');

const font = f => `url(file://${REPO}/fonts/${f})`;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1420, height: 1080 } });
await page.setContent(`<!doctype html><meta charset="utf-8"><style>
  @font-face{font-family:'DM Sans';src:${font('DMSans-600-normal-latin-1c49a6.woff2')};font-weight:600}
  @font-face{font-family:'DM Sans';src:${font('DMSans-400-normal-latin-1c49a6.woff2')};font-weight:400}
  body{margin:0;background:#FFFDF8;font-family:'DM Sans',sans-serif;padding:42px 38px;color:#112345}
  h1{font-size:25px;font-weight:600;margin:0 0 4px;letter-spacing:-.01em}
  .sub{font-size:14px;color:#5D6676;font-weight:400;margin:0 0 24px}
  .grid{display:grid;grid-template-columns:repeat(4,1fr);gap:26px 20px}
  figure{margin:0}
  img{width:100%;display:block;border:1px solid rgba(17,35,69,.16)}
  figcaption{margin-top:9px;font-size:12px;color:#5D6676;font-weight:400;
             display:flex;gap:7px;align-items:baseline}
  figcaption b{color:#7F6A30;font-weight:600;letter-spacing:.09em}
</style>
<h1>START HERE</h1>
<p class="sub">Eight slides, 1080 &times; 1350. Cover with the portrait, two statements, the four questions, close.</p>
<div class="grid">${cells}</div>`, { waitUntil: 'load' });
await page.evaluate(() => document.fonts.ready);
await page.screenshot({ path: join(ROOT, 'contact-sheet.png'), fullPage: true });
await browser.close();
console.log(`wrote contact-sheet.png with ${LABELS.length} slides`);
