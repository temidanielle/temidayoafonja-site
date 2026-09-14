#!/usr/bin/env node
/**
 * Quality gate for the three essay visuals.
 *
 *   node verify-visuals.mjs [path/to/v5.2-extract.txt]
 *
 * Checks the rendered text against copy.json, checks copy.json against the
 * essay text when an extract is supplied, sweeps for em and en dashes, reports
 * the smallest type size on each sheet, and confirms the Career Evidence
 * Starter images are the untouched repository renders.
 */
import { chromium } from 'playwright';
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import { extname, join, normalize } from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = fileURLToPath(new URL('.', import.meta.url));
const ROOT = join(HERE, '..', '..');
const EM = '—', EN = '–';

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
const problems = [], notes = [];

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1600, height: 1000 } });
await page.goto(`http://127.0.0.1:${port}/substack-sep09-current-role-final-visuals/source/visuals.html`,
                { waitUntil: 'networkidle' });
await page.waitForFunction(() => document.documentElement.dataset.ready === 'true');

const sheets = await page.evaluate(() => [...document.querySelectorAll('.sheet')].map(s => ({
  id: s.id,
  text: [...s.querySelectorAll('*')].filter(e => !e.children.length && e.textContent.trim())
          .map(e => ({ t: e.textContent.trim(), size: parseFloat(getComputedStyle(e).fontSize) })),
  images: [...s.querySelectorAll('img')].map(i => ({
    src: new URL(i.src).pathname,
    natural: `${i.naturalWidth}x${i.naturalHeight}`,
    shown: `${Math.round(i.getBoundingClientRect().width)}x${Math.round(i.getBoundingClientRect().height)}`,
  })),
})));

// 1. every string in copy.json is on the sheet it belongs to, and nothing is clipped
const expected = {
  cover: [...copy.cover.titleLines, copy.cover.supporting, copy.cover.footer],
  threeps: [copy.threePs.title, ...copy.threePs.cards.flatMap(c => [c.label, c.question]), copy.threePs.supporting],
  starter: [copy.starter.caption],
};
for (const s of sheets) {
  const rendered = s.text.map(t => t.t).join(' | ');
  for (const want of expected[s.id]) {
    if (!rendered.includes(want)) problems.push(`${s.id}: missing or altered copy "${want.slice(0, 48)}"`);
  }
  const min = Math.min(...s.text.map(t => t.size));
  notes.push(`${s.id}: smallest type ${min}px (${(min * 600 / 1600).toFixed(1)}px in a 600px column)`);
}
// Genuine clipping means ink leaving the sheet. Comparing scrollHeight against
// clientHeight only reports that the serif's ascender exceeds a tight line box,
// which is normal and cuts nothing.
const clipped = await page.evaluate(() => {
  const out = [];
  for (const sheet of document.querySelectorAll('.sheet')) {
    const s = sheet.getBoundingClientRect();
    for (const el of sheet.querySelectorAll('*')) {
      if (el.children.length || !el.textContent.trim()) continue;
      const r = el.getBoundingClientRect();
      if (r.left < s.left - 1 || r.right > s.right + 1 || r.top < s.top - 1 || r.bottom > s.bottom + 1) {
        out.push(`${sheet.id}: "${el.textContent.trim().slice(0, 30)}"`);
      }
    }
  }
  return out;
});
if (clipped.length) problems.push(`text outside the sheet: ${clipped.join('; ')}`);

// 2. dash sweep across the rendered text and the copy file
for (const s of sheets) {
  for (const { t } of s.text) {
    if (t.includes(EM)) problems.push(`${s.id}: em dash in "${t.slice(0, 40)}"`);
    if (t.includes(EN)) problems.push(`${s.id}: en dash in "${t.slice(0, 40)}"`);
  }
}
const copyRaw = await readFile(join(HERE, 'copy.json'), 'utf8');
if (copyRaw.includes(EM) || copyRaw.includes(EN)) problems.push('dash in copy.json');

// 3. the Starter images must be the repository renders, byte for byte
const starter = sheets.find(s => s.id === 'starter');
for (const im of starter.images) {
  const bytes = await readFile(join(ROOT, im.src.replace(/^\//, '')));
  const hash = createHash('sha256').update(bytes).digest('hex').slice(0, 12);
  notes.push(`artifact ${im.src} natural ${im.natural}, shown ${im.shown}, sha256 ${hash}`);
  const [nw] = im.natural.split('x').map(Number);
  const [sw] = im.shown.split('x').map(Number);
  if (sw > nw) problems.push(`${im.src} is upscaled (${im.shown} from ${im.natural})`);
}
if (starter.images.length !== 2) problems.push('starter sheet should show exactly two real pages');

// 4. copy against the essay, when an extract is supplied
const extract = process.argv[2];
if (extract) {
  const body = (await readFile(extract, 'utf8')).replace(/\s+/g, ' ');
  const check = [
    ['cover title', copy.cover.titleLines.join(' ')],
    ...copy.threePs.cards.map(c => [`${c.label} question`, c.question]),
  ];
  for (const [what, str] of check) {
    if (!body.includes(str)) problems.push(`${what} not found verbatim in the essay: "${str}"`);
  }
  for (const anchor of ['That is what the 3 Ps help you see.',
                        'Practice: What are you becoming better able to handle?',
                        'That is exactly where the Starter begins.',
                        'Get the free 10-Minute Career Evidence Starter:']) {
    if (!body.includes(anchor)) problems.push(`placement anchor missing from the essay: "${anchor}"`);
    else notes.push(`anchor present and unaltered: "${anchor}"`);
  }
}

await browser.close();
server.close();

for (const n of notes) console.log('  ' + n);
if (problems.length) {
  console.error(`\nFAIL (${problems.length}):`);
  for (const p of problems) console.error('  ' + p);
  process.exit(1);
}
console.log('\nAll checks passed.');
