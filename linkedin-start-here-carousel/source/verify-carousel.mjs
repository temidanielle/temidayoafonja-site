#!/usr/bin/env node
/**
 * Quality gate for the Featured carousel.
 *
 *   node linkedin-start-here-carousel/source/verify-carousel.mjs
 *
 * Checks rendered copy against copy.json, sweeps for em and en dashes, confirms
 * both brand faces actually loaded rather than being substituted, confirms no
 * text leaves the safe area or is clipped, confirms the portrait is never
 * upscaled, and checks the exported PDF and PNGs.
 */
import { chromium } from 'playwright';
import { createServer } from 'node:http';
import { readFile, readdir, stat } from 'node:fs/promises';
import { extname, join, normalize } from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = fileURLToPath(new URL('.', import.meta.url));
const OUT = join(HERE, '..');
const ROOT = join(HERE, '..', '..');
const EM = '—', EN = '–';
const PDF_NAME = 'LinkedIn_Start_Here_Capability_Formation.pdf';

const MIME = { '.html': 'text/html; charset=utf-8', '.css': 'text/css; charset=utf-8',
               '.json': 'application/json; charset=utf-8', '.woff2': 'font/woff2', '.png': 'image/png' };
const server = createServer(async (req, res) => {
  const f = join(ROOT, normalize(decodeURIComponent(new URL(req.url, 'http://x').pathname)));
  if (!f.startsWith(ROOT)) return void res.writeHead(403).end();
  try { res.writeHead(200, { 'content-type': MIME[extname(f)] ?? 'application/octet-stream' }); res.end(await readFile(f)); }
  catch { res.writeHead(404).end(); }
});
const port = await new Promise(r => server.listen(0, '127.0.0.1', () => r(server.address().port)));

const copy = JSON.parse(await readFile(join(HERE, 'copy.json'), 'utf8'));
const { w: W, h: H, margin: MARGIN } = copy.canvas;
const problems = [], notes = [];

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: W, height: H } });
await page.goto(`http://127.0.0.1:${port}/linkedin-start-here-carousel/source/carousel.html`,
                { waitUntil: 'networkidle' });
await page.waitForFunction(() => document.documentElement.dataset.ready === 'true');

const report = await page.evaluate(margin => {
  const slides = [...document.querySelectorAll('.slide')];
  return {
    fontsLoaded: {
      serif: document.fonts.check('500 86px "Cormorant Garamond"'),
      sans: document.fonts.check('400 34px "DM Sans"'),
      families: [...document.fonts].map(f => f.family).filter((v, i, a) => a.indexOf(v) === i),
    },
    slides: slides.map(s => {
      const box = s.getBoundingClientRect();
      const leaves = [...s.querySelectorAll('*')].filter(e => !e.children.length && e.textContent.trim());
      return {
        size: `${Math.round(box.width)}x${Math.round(box.height)}`,
        text: leaves.map(e => ({
          t: e.textContent.trim(),
          size: parseFloat(getComputedStyle(e).fontSize),
          family: getComputedStyle(e).fontFamily.split(',')[0].replace(/["']/g, ''),
          outside: (() => {
            const r = e.getBoundingClientRect();
            return r.left < box.left + margin - 1 || r.right > box.right - margin + 1 ||
                   r.top < box.top + margin - 1 || r.bottom > box.bottom - margin + 1;
          })(),
        })),
        overflow: s.querySelector('.main').scrollHeight > s.querySelector('.main').clientHeight + 1,
        images: [...s.querySelectorAll('img')].map(i => ({
          src: new URL(i.src).pathname,
          natural: `${i.naturalWidth}x${i.naturalHeight}`,
          shown: `${Math.round(i.getBoundingClientRect().width)}x${Math.round(i.getBoundingClientRect().height)}`,
          upscaled: i.getBoundingClientRect().width > i.naturalWidth,
        })),
      };
    }),
  };
}, MARGIN);

// 1. fonts actually loaded, not substituted
if (!report.fontsLoaded.serif) problems.push('Cormorant Garamond did not load, type would be substituted');
if (!report.fontsLoaded.sans) problems.push('DM Sans did not load, type would be substituted');
notes.push(`fonts loaded: ${report.fontsLoaded.families.join(', ')}`);

// 2. copy is exact, and dash free
if (report.slides.length !== copy.slides.length) problems.push('slide count mismatch');
report.slides.forEach((s, i) => {
  const spec = copy.slides[i];
  const rendered = s.text.map(t => t.t).join(' | ');
  const want = [spec.kicker, spec.number, spec.headline, ...(spec.headlineLines ?? []),
                ...(spec.body ?? []), spec.supporting, spec.closing, spec.footer].filter(Boolean);
  for (const str of want) {
    if (!rendered.includes(str)) problems.push(`slide ${i + 1}: copy missing or altered "${str.slice(0, 44)}"`);
  }
  for (const { t } of s.text) {
    if (t.includes(EM)) problems.push(`slide ${i + 1}: em dash in "${t.slice(0, 36)}"`);
    if (t.includes(EN)) problems.push(`slide ${i + 1}: en dash in "${t.slice(0, 36)}"`);
  }
  // 3. safe area, clipping, sizes
  if (s.size !== `${W}x${H}`) problems.push(`slide ${i + 1}: rendered ${s.size}`);
  if (s.overflow) problems.push(`slide ${i + 1}: body overflows its column`);
  for (const t of s.text) {
    if (t.outside) problems.push(`slide ${i + 1}: "${t.t.slice(0, 30)}" sits outside the ${MARGIN}px safe area`);
  }
  // 4. imagery is never upscaled
  for (const im of s.images) {
    if (im.upscaled) problems.push(`slide ${i + 1}: ${im.src} upscaled from ${im.natural} to ${im.shown}`);
    else notes.push(`slide ${i + 1} portrait ${im.src}, natural ${im.natural}, shown ${im.shown}`);
  }
  const min = Math.min(...s.text.map(t => t.size));
  notes.push(`slide ${i + 1}: smallest type ${min}px (${(min * 420 / W).toFixed(1)}px at LinkedIn mobile width)`);
});

await browser.close();
server.close();

// 5. exports
const files = await readdir(join(OUT, 'slides'));
const pngs = files.filter(f => f.endsWith('.png')).sort();
if (pngs.length !== copy.slides.length) problems.push(`${pngs.length} PNGs for ${copy.slides.length} slides`);
const pdf = await readFile(join(OUT, PDF_NAME));
if (!pdf.subarray(0, 5).toString().startsWith('%PDF-')) problems.push('PDF header missing');
const pages = (pdf.toString('latin1').match(/\/Type\s*\/Page[^s]/g) ?? []).length;
if (pages !== copy.slides.length) problems.push(`PDF has ${pages} pages for ${copy.slides.length} slides`);
const mb = pdf.toString('latin1').match(/\/MediaBox\s*\[\s*0\s+0\s+([\d.]+)\s+([\d.]+)/);
if (mb) notes.push(`PDF page ${Math.round(+mb[1])} x ${Math.round(+mb[2])} pt (${W} x ${H} px)`);
notes.push(`PDF ${(await stat(join(OUT, PDF_NAME))).size / 1024 | 0} KB, ${pngs.length} slide PNGs`);

for (const n of notes) console.log('  ' + n);
if (problems.length) {
  console.error(`\nFAIL (${problems.length}):`);
  for (const p of problems) console.error('  ' + p);
  process.exit(1);
}
console.log('\nAll checks passed.');
