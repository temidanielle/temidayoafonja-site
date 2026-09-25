#!/usr/bin/env node
/**
 * The gate. It fails rather than ships.
 *
 *   node source/verify.mjs
 *
 * The same floor and the same margin checks the later carousels hold, plus the
 * voice rules in voice.mjs and a check that the three revised lines are in and
 * the three they replaced are gone.
 */
import { chromium } from 'playwright';
import { readFile, readdir } from 'node:fs/promises';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { execFileSync } from 'node:child_process';
import { voiceFaults } from './voice.mjs';

const HERE = fileURLToPath(new URL('.', import.meta.url));
const ROOT = join(HERE, '..');
const OUT = join(ROOT, 'slides');
const C = JSON.parse(await readFile(join(HERE, 'copy.json'), 'utf8'));
const { w: W, h: H, inset: I, pad: P } = C.canvas;
const TOTAL = C.slides.length;
const problems = [], notes = [];

const files = (await readdir(OUT)).filter(f => /^slide-\d\d\.svg$/.test(f)).sort();
if (files.length !== TOTAL) problems.push(`${files.length} slides, expected ${TOTAL}`);

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: W, height: H } });
const slides = [];
for (const f of files) {
  const svg = await readFile(join(OUT, f), 'utf8');
  await page.setContent(`<!doctype html><meta charset="utf-8"><style>html,body{margin:0}</style>${svg}`,
    { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  slides.push(await page.evaluate(({ I, P, W, H }) => {
    const out = { text: [], sizes: [], offGrid: [], outside: [], marks: [], boxes: [],
                  ring: 0, images: 0, size: null };
    const svg = document.querySelector('svg');
    out.size = [svg.getAttribute('width'), svg.getAttribute('height')].join('x');
    for (const el of svg.querySelectorAll('text')) {
      const cs = getComputedStyle(el);
      const cls = el.getAttribute('class');
      out.text.push(el.textContent);
      out.sizes.push({ px: parseFloat(cs.fontSize), t: el.textContent.slice(0, 28) });
      const pen = parseFloat(el.getAttribute('x'));
      // The pagination and the note sit on their own columns by design.
      const onMargin = cs.textAnchor === 'start' && !/^counter/.test(cls) && cls !== 'note';
      if (onMargin && Math.abs(pen - (I + P)) > 1)
        out.offGrid.push(`${el.textContent.slice(0, 24)} at x=${pen}`);
      if (cls && !/^counter/.test(cls)) out.marks.push(`${cls}@${el.getAttribute('y')}`);
      // getBoundingClientRect, not getBBox: getBBox reports the element's own
      // user space and ignores ancestor transforms, so a element inside a
      // translated group and one outside it came back in different coordinate
      // systems. The SVG is rendered 1:1 in a viewport of its own size, so
      // client coordinates are slide coordinates.
      const b = el.getBoundingClientRect();
      out.boxes.push({ x: b.x, y: b.y, w: b.width, h: b.height,
                       t: el.textContent.trim().slice(0, 30) });
      if (b.x < I + 6 || b.x + b.width > W - I - 6 || b.y < I || b.y + b.height > H - I)
        out.outside.push(`${el.textContent.trim().slice(0, 26)} [${Math.round(b.x)},${Math.round(b.y)} ${Math.round(b.width)}x${Math.round(b.height)}]`);
    }
    for (const c of svg.querySelectorAll('circle'))
      if (c.getAttribute('stroke') && +c.getAttribute('r') < 40) out.ring++;
    out.images = svg.querySelectorAll('image').length;
    return out;
  }, { I, P, W, H }));
}
await browser.close();

/* ── size ─────────────────────────────────────────────────────────────── */
const sizes = new Set(slides.map(s => s.size));
if (sizes.size !== 1 || !sizes.has(`${W}x${H}`))
  problems.push(`slide sizes: ${[...sizes].join(', ')}, expected only ${W}x${H}`);
else notes.push(`all ${TOTAL} slides ${W}x${H}`);

/* ── the copy, and nothing but the copy ───────────────────────────────── */
const pad2 = n => String(n).padStart(2, '0');
const EXPECT = C.slides.map((s, i) => {
  const v = [];
  if (s.kicker) v.push(s.kicker);
  if (s.number) v.push(s.number);
  if (s.headline) v.push(s.headline);
  if (s.headlineLines) v.push(...s.headlineLines);
  if (s.body) v.push(...s.body);
  if (s.supporting) v.push(s.supporting);
  if (s.closing) v.push(s.closing);
  if (s.footer) v.push(s.footer);
  v.push(pad2(i + 1), `/ ${pad2(TOTAL)}`);
  return v;
});
const norm = v => v.replace(/\s+/g, '').toLowerCase();
slides.forEach((s, i) => {
  const inked = s.text.map(norm).join('');
  const copied = EXPECT[i].map(norm).join('');
  for (const v of EXPECT[i]) if (!inked.includes(norm(v)))
    problems.push(`slide ${i + 1} is missing "${v}"`);
  if (inked.length !== copied.length)
    problems.push(`slide ${i + 1}: ${inked.length} characters of ink against ${copied.length} of copy`);
});
if (!problems.length) notes.push('every slide carries its copy exactly, and carries nothing else');

/* ── the three revised lines are in, and the three they replaced are out ─ */
const all = slides.flatMap(s => s.text).join(' ');
const REVISED = [
  ['Adjacent experience is not automatic qualification.', 'Adjacent experience still has to be read.'],
  ['Your job is not to pretend the gap does not exist.', 'Name the gap before someone else does.'],
  ['Being capable of learning them is not the same as already knowing them.',
   'Learning them takes time, even when you are capable of it.'],
];
for (const [was, now] of REVISED) {
  if (all.includes(was)) problems.push(`the replaced line is still rendered: "${was}"`);
  if (!all.includes(now)) problems.push(`the revised line is missing: "${now}"`);
}
if (!problems.length) notes.push('all three revised lines are set, and none of the three they replaced survive');

/* ── em dashes and the voice rules ────────────────────────────────────── */
for (const [ch, name] of [['—', 'em dash'], ['–', 'en dash']]) {
  const n = [...all].filter(c => c === ch).length;
  if (n) problems.push(`${n} ${name}${n > 1 ? 's' : ''} in the rendered text`);
}
notes.push('no em dashes and no en dashes anywhere in the rendered text');

const faults = slides.flatMap((s, i) =>
  voiceFaults(s.text.join(' ')).map(f => `slide ${i + 1}: ${f}`));
if (faults.length) problems.push(...faults);
else notes.push('no "not X, it is Y" constructions, and none of the hedging adverbs');

/* ── the 28px floor ───────────────────────────────────────────────────── */
const smallest = Math.min(...slides.flatMap(s => s.sizes.map(x => x.px)));
const under = slides.flatMap((s, i) => s.sizes.filter(x => x.px < C.minType)
  .map(x => `slide ${i + 1} "${x.t}" at ${x.px}px`));
if (under.length) problems.push(`below the ${C.minType}px floor: ${under.join('; ')}`);
else notes.push(`smallest type anywhere ${smallest}px (floor is ${C.minType}px), ` +
  `which is ${(smallest * 0.389).toFixed(1)}px at LinkedIn mobile width`);

/* ── the four question slides share one grid ──────────────────────────── */
const qIdx = C.slides.map((s, i) => s.mode === 'question' ? i : -1).filter(i => i >= 0);
const grids = new Set(qIdx.map(i =>
  slides[i].marks.filter(m => /^(numeral|say)@/.test(m)).join('|')));
if (grids.size !== 1) problems.push(`the question slides do not share one grid: ${[...grids].join(' / ')}`);
else notes.push(`the numeral and the question sit at one height on all ${qIdx.length} question slides`);

/* ── the pagination, and its ring ─────────────────────────────────────── */
const noRing = slides.map((s, i) => s.ring < 1 ? i + 1 : 0).filter(Boolean);
if (noRing.length) problems.push(`the pagination ring is missing on slide ${noRing.join(', ')}`);
else notes.push(`the gold pagination ring is on all ${TOTAL} slides, carried over from the previous version`);

/* ── the portrait ─────────────────────────────────────────────────────── */
const withArt = slides.map((s, i) => s.images ? i + 1 : 0).filter(Boolean);
if (withArt.join() !== '1') problems.push(`images appear on slide ${withArt.join(', ') || 'none'}, expected slide 1 only`);
else notes.push('the approved portrait is on slide 1 only');

/* ── the footer appears once ──────────────────────────────────────────── */
const foot = C.slides.at(-1).footer;
const footOn = slides.map((s, i) => s.text.join(' ').includes(foot) ? i + 1 : 0).filter(Boolean);
if (footOn.join() !== String(TOTAL)) problems.push(`the footer appears on slides ${footOn.join(', ') || 'none'}, expected slide ${TOTAL} only`);
else notes.push(`the footer appears on slide ${TOTAL} only`);

/* ── the margin ───────────────────────────────────────────────────────── */
const off = slides.flatMap((s, i) => s.offGrid.map(v => `slide ${i + 1}: ${v}`));
const out = slides.flatMap((s, i) => s.outside.map(v => `slide ${i + 1}: ${v}`));
if (off.length) problems.push(`off the margin: ${off.join('; ')}`);
if (out.length) problems.push(`ink crossing the card edge: ${out.join('; ')}`);
if (!off.length && !out.length)
  notes.push('every left aligned element sits on the margin, and no ink crosses the card edge');

/* ── nothing sits on top of anything else ────────────────────────────────
   Added after the signature was moved up the close slide and landed on the
   pagination. Both elements were inside the card and on the margin, so every
   check that existed passed while the two were printed over each other. Boxes
   are compared pairwise; a small overlap is tolerated because glyph boxes of
   adjacent lines in one block can touch. */
{
  const hits = [];
  slides.forEach((s, i) => {
    for (let a = 0; a < s.boxes.length; a++)
      for (let b = a + 1; b < s.boxes.length; b++) {
        const p = s.boxes[a], q = s.boxes[b];
        const ox = Math.min(p.x + p.w, q.x + q.w) - Math.max(p.x, q.x);
        const oy = Math.min(p.y + p.h, q.y + q.h) - Math.max(p.y, q.y);
        if (ox > 4 && oy > 4)
          hits.push(`slide ${i + 1}: "${p.t}" over "${q.t}" by ${Math.round(ox)}x${Math.round(oy)}px`);
      }
  });
  if (hits.length) problems.push(`text printed over text: ${hits.join('; ')}`);
  else notes.push('no text element overlaps another on any slide');
}

/* ── US English, and the paragraph that was removed ──────────────────────── */
{
  // A generic "ends in ise" rule flags precise, concise and wise, so this is
  // an explicit list of British forms whose US spelling differs.
  const BRITISH = ['colour', 'behaviour', 'favour', 'honour', 'labour', 'neighbour',
    'centre', 'metre', 'theatre', 'fibre', 'licence', 'defence', 'offence',
    'organise', 'organised', 'organisation', 'recognise', 'recognised',
    'realise', 'realised', 'prioritise', 'prioritised', 'specialise', 'specialised',
    'analyse', 'analysed', 'emphasise', 'emphasised', 'apologise',
    'travelled', 'travelling', 'labelled', 'labelling', 'modelling', 'cancelled',
    'programme', 'whilst', 'amongst', 'learnt', 'spelt', 'practise'];
  const found = BRITISH.filter(b => new RegExp(`\\b${b}\\b`, 'i').test(all));
  if (found.length) problems.push(`British spelling in the rendered text: ${found.join(', ')}`);
  else notes.push(`US English: none of the ${BRITISH.length} British forms checked appear`);

  const gone = C._removed_from_close;
  if (gone) {
    if (all.includes(gone)) problems.push(`the removed paragraph is still rendered: "${gone}"`);
    else notes.push('the paragraph removed from the close slide does not appear anywhere');
  }
}

/* ── the PDF ──────────────────────────────────────────────────────────── */
const pdf = join(ROOT, 'LinkedIn_Start_Here_Capability_Formation_V3.pdf');
const info = execFileSync('pdfinfo', [pdf], { encoding: 'utf8' });
const pages = +(/Pages:\s+(\d+)/.exec(info) || [])[1];
const dim = (/Page size:\s+([\d.]+) x ([\d.]+)/.exec(info) || []).slice(1).map(Number);
if (pages !== TOTAL) problems.push(`the PDF has ${pages} pages, expected ${TOTAL}`);
if (Math.abs(dim[0] - W * 0.75) > 1 || Math.abs(dim[1] - H * 0.75) > 1)
  problems.push(`PDF page ${dim.join(' x ')} pt, expected ${W * 0.75} x ${H * 0.75}`);
if (pages === TOTAL) notes.push(`PDF ${pages} pages, ${dim[0]} by ${dim[1]} pt (${W} by ${H} px), ` +
  `${Math.round((await readFile(pdf)).length / 1024)} KB`);

// One raster image is expected, the portrait, and it must be on page 1.
const imgs = execFileSync('pdfimages', ['-list', pdf], { encoding: 'utf8' })
  .trim().split('\n').slice(2).filter(Boolean);
if (imgs.length !== 1 || !/^\s*1\s/.test(imgs[0]))
  problems.push(`expected exactly one raster image on page 1, found ${imgs.length}`);
else notes.push('one raster image in the PDF, the portrait on page 1; every other page is vector text');

for (const n of notes) console.log(`  ${n}`);
if (problems.length) { console.error('\nFAILED:'); for (const p of problems) console.error(`  ${p}`); process.exit(1); }
console.log('\nAll checks passed.');
