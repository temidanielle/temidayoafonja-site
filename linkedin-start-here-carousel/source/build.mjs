#!/usr/bin/env node
/**
 * START HERE: an eight slide LinkedIn document carousel.
 *
 *   node source/build.mjs
 *
 * Rebuilt into the shared system used by the rest of the set: a cream card on
 * a navy field, DM Sans, gold hairlines, tracked gold capitals, and the cover
 * and the close inverted to a navy card. The approved portrait stays on the
 * cover.
 *
 * Two things changed in substance. Nothing is set below 28px, which is the
 * same floor the later carousels hold, and the body text was enlarged to fill
 * the card rather than headlines being shrunk to make room, which is what the
 * previous version did.
 *
 * The four question slides share one fixed grid, so the numeral, the question
 * and the rule do not move as the reader swipes through them.
 */
import { chromium } from 'playwright';
import { readFile, writeFile, mkdir } from 'node:fs/promises';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { styles, block, esc, wrapAll, PORTRAIT } from './lib.mjs';

const HERE = fileURLToPath(new URL('.', import.meta.url));
const ROOT = join(HERE, '..');
const OUT = join(ROOT, 'slides');
await mkdir(OUT, { recursive: true });
const C = JSON.parse(await readFile(join(HERE, 'copy.json'), 'utf8'));
const { w: W, h: H, inset: I, pad: P, radius: R } = C.canvas;
const t = C.tokens;
const X = I + P, CW = W - (I + P) * 2;
const CARD = { x: I, y: I, w: W - I * 2, h: H - I * 2 };
const TOTAL = C.slides.length;

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: W, height: H } });
await page.setContent('<!doctype html><meta charset="utf-8"><body></body>');

const rect = (x, y, w, h, fill, extra = '') =>
  `  <rect x="${x}" y="${y}" width="${w}" height="${h}" fill="${fill}"${extra}/>`;
const rule = (x, y, w, fill, h = 3, op = 1) =>
  `  <rect x="${x}" y="${y}" width="${w}" height="${h}" fill="${fill}" fill-opacity="${op}"/>`;
const pad2 = n => String(n).padStart(2, '0');

/* The pagination. The ring around the current number is carried over from the
   previous version deliberately: it was kept gold on purpose when the small
   text moved to navy, so it is not dropped here just because the later
   carousels in the set do not paginate at all. */
function counter(n, invert) {
  const cy = H - I - 72, r = 29, cx = X + r;
  return [
    `  <circle cx="${cx}" cy="${cy}" r="${r}" fill="none" stroke="${t.gold}" stroke-width="2"/>`,
    `  <text class="${invert ? 'counterUp' : 'counter'}" x="${cx}" y="${cy + 10}" ` +
      `text-anchor="middle">${pad2(n)}</text>`,
    `  <text class="${invert ? 'counterUp' : 'counter'}" x="${cx + r + 20}" y="${cy + 10}" ` +
      `fill-opacity=".72">/ ${pad2(TOTAL)}</text>`,
  ].join('\n');
}

function shell(inner, read, n, invert, extraDefs = '') {
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}"
     viewBox="0 0 ${W} ${H}" role="img" aria-label="${esc(read)}">
  <title>Slide ${n} of ${TOTAL}</title>
  <defs><style>${styles(t)}</style>${extraDefs}</defs>
  <rect width="${W}" height="${H}" fill="${invert ? t.cream : t.navy}"/>
  <rect x="${CARD.x}" y="${CARD.y}" width="${CARD.w}" height="${CARD.h}" rx="${R}"
        fill="${invert ? t.navy : t.card}"/>
${inner}
${counter(n, invert)}
</svg>
`;
}

function settle(parts, bottom, bias = 0.42) {
  const slack = (CARD.y + CARD.h - P - 74) - bottom;   // 74 keeps clear of the counter
  if (slack <= 0) return parts.join('\n');
  return `  <g transform="translate(0,${Math.round(slack * bias)})">\n` +
         parts.join('\n') + `\n  </g>`;
}

/** One body list: paragraphs at a fixed leading with a gap between them. */
function bodyList(lines, y, cls = 'body', lead = 52, gap = 30) {
  const o = [];
  for (const para of lines) {
    o.push(block(cls, X, y, para, lead));
    y += (para.length - 1) * lead + lead + gap;
  }
  return { markup: o.join('\n'), bottom: y - gap - lead };
}

/* ── the grid the four question slides share ──────────────────────────── */
const G = { NUM: 330, HEAD: 452, RULE: 502, BODY: 600 };

/* ── cover, navy card, with the approved portrait ─────────────────────────
   Set on a fixed grid rather than settled. The copy runs the full measure at
   the top and the portrait sits alone in the lower right, which keeps the two
   out of each other's way; the previous arrangement squeezed the supporting
   line into a narrow column beside the photograph. */
async function cover(s) {
  const w = await wrapAll(page, t, [
    { k: 'h', text: s.headline, cls: 'cover', width: CW },
    { k: 's', text: s.supporting, cls: 'coverSub', width: CW },
  ]);
  const o = [];
  o.push(block('kicker', X, 284, [s.kicker], 0));
  o.push(block('cover', X, 384, w.h, 86));
  const ruleY = 384 + (w.h.length - 1) * 86 + 62;
  o.push(rule(X, ruleY, 132, t.gold, 3));
  o.push(block('coverSub', X, ruleY + 92, w.s, 50));

  // The approved file, at its own resolution, circular, clear of the copy
  // above it and of the pagination below it.
  const D = 300, cx = W - I - P - D / 2, cy = H - I - 172 - D / 2;
  const art = `
    <clipPath id="p"><circle cx="${cx}" cy="${cy}" r="${D / 2}"/></clipPath>`;
  const img = `  <g clip-path="url(#p)">
    <image href="data:image/png;base64,${PORTRAIT}" x="${cx - D / 2}" y="${cy - D / 2 - 26}"
           width="${D}" height="${D * 1.17}" preserveAspectRatio="xMidYMin slice"/>
  </g>
  <circle cx="${cx}" cy="${cy}" r="${D / 2 + 8}" fill="none" stroke="${t.gold}"
          stroke-width="2" stroke-opacity=".5"/>`;

  return shell(o.join('\n') + '\n' + img,
    `${s.kicker}. ${s.headline} ${s.supporting}`, 1, true, art);
}

/* ── a statement slide, cream card ────────────────────────────────────── */
async function statement(s, n) {
  const w = await wrapAll(page, t, [
    { k: 'h', text: s.headline, cls: 'say', width: CW },
    ...s.body.map((text, i) => ({ k: `b${i}`, text, cls: 'body', width: CW })),
  ]);
  const o = [];
  let y = I + 270;
  o.push(block('say', X, y, w.h, 70));
  y += (w.h.length - 1) * 70 + 62;
  o.push(rule(X, y, 132, t.gold, 3));
  y += 104;
  const list = bodyList(s.body.map((_, i) => w[`b${i}`]), y);
  o.push(list.markup);
  return shell(settle(o, list.bottom), [s.headline, ...s.body].join(' '), n, false);
}

/* ── a question slide, cream card, all four on G ──────────────────────── */
async function question(s, n) {
  const reqs = [
    { k: 'h', text: s.headline, cls: 'say', width: CW },
    ...s.body.map((text, i) => ({ k: `b${i}`, text, cls: 'body', width: CW })),
  ];
  if (s.supporting) reqs.push({ k: 'n', text: s.supporting, cls: 'note', width: CW - 72 });
  const w = await wrapAll(page, t, reqs);

  const o = [];
  o.push(block('numeral', X, G.NUM, [s.number], 0));
  o.push(block('say', X, G.HEAD, w.h, 70));
  o.push(rule(X, G.RULE, 132, t.gold, 3));
  const list = bodyList(s.body.map((_, i) => w[`b${i}`]), G.BODY);
  o.push(list.markup);
  let bottom = list.bottom;
  if (s.supporting) {
    const top = bottom + 54, bh = 34 + w.n.length * 46 - 46 + 38 + 34;
    o.push(rect(X, top, CW, bh, t.paper, ` rx="6" stroke="${t.line}" stroke-width="1.5"`));
    o.push(rule(X, top, 5, t.gold, bh));
    o.push(block('note', X + 36, top + 34 + 34, w.n, 46));
    bottom = top + bh;
  }
  return shell(o.join('\n'),
    `${s.number}. ${s.headline} ${[...s.body, s.supporting || ''].join(' ')}`.trim(), n, false);
}

/* ── close, navy card ─────────────────────────────────────────────────── */
async function close(s, n) {
  const w = await wrapAll(page, t, [
    ...s.headlineLines.map((text, i) => ({ k: `h${i}`, text, cls: 'sayUp', width: CW })),
    { k: 'b', text: s.body[0], cls: 'bodyUp', width: CW },
    { k: 'c', text: s.closing, cls: 'closing', width: CW },
  ]);
  const o = [];
  let y = I + 250;
  s.headlineLines.forEach((_, i) => {
    o.push(block('sayUp', X, y, w[`h${i}`], 68));
    y += (w[`h${i}`].length - 1) * 68 + 76;
  });
  y += 4;
  o.push(rule(X, y, 132, t.gold, 3));
  y += 92;
  o.push(block('bodyUp', X, y, w.b, 50));
  y += (w.b.length - 1) * 50 + 96;
  o.push(block('closing', X, y, w.c, 54));
  y += (w.c.length - 1) * 54;
  return shell(settle(o, y, 0.30) +
    `\n${block('sig', X, H - I - 128, [s.footer], 0)}`,
    [...s.headlineLines, ...s.body, s.closing, s.footer].join(' '), n, true);
}

/* ── render ───────────────────────────────────────────────────────────── */
const svgs = [];
for (const [i, s] of C.slides.entries()) {
  const n = i + 1;
  svgs.push(s.mode === 'cover' ? await cover(s)
          : s.mode === 'close' ? await close(s, n)
          : s.mode === 'question' ? await question(s, n)
          : await statement(s, n));
}

for (const [i, svg] of svgs.entries()) {
  const name = `slide-0${i + 1}`;
  await writeFile(join(OUT, `${name}.svg`), svg);
  await page.setContent(
    `<!doctype html><meta charset="utf-8"><style>html,body{margin:0}svg{display:block}</style>${svg}`,
    { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: join(OUT, `${name}.png`), type: 'png' });
}
console.log(`wrote ${svgs.length} slides`);

await page.setContent(
  `<!doctype html><meta charset="utf-8"><style>
     @page { size: ${W}px ${H}px; margin: 0; }
     html,body{margin:0;padding:0}
     .pg{width:${W}px;height:${H}px;overflow:hidden;break-after:page;page-break-after:always}
     .pg:last-child{break-after:auto;page-break-after:auto}
     svg{display:block}
   </style>${svgs.map(s => `<div class="pg">${s}</div>`).join('')}`, { waitUntil: 'load' });
await page.evaluate(() => document.fonts.ready);
await page.pdf({ path: join(ROOT, 'LinkedIn_Start_Here_Capability_Formation_V3.pdf'),
  width: `${W}px`, height: `${H}px`, printBackground: true, pageRanges: `1-${svgs.length}` });
console.log('wrote LinkedIn_Start_Here_Capability_Formation_V3.pdf');
await browser.close();
