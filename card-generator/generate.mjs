#!/usr/bin/env node
/**
 * Capability Audit card generator.
 *
 * Renders every social card from one template system so future runs are one
 * command:  node card-generator/generate.mjs
 *
 * Output: seven PNGs written to the repo root (where the other card/OG images
 * live). Fonts are bundled under card-generator/fonts and embedded as base64
 * so Cormorant Garamond and Montserrat always render — never a system fallback.
 */

import { chromium } from 'playwright';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = join(HERE, '..');

// ---- Brand tokens -------------------------------------------------------
const SAND = '#F5F0E8';
const NAVY = '#0F2347';
const GOLD = '#C9A84C';
const WHITE = '#FFFFFF';

// ---- Bundled fonts (embedded so rendering is deterministic) -------------
const b64 = (p) => readFileSync(join(HERE, 'fonts', p)).toString('base64');
const CORMORANT = b64('CormorantGaramond-Regular.woff2');
const MONTSERRAT = b64('Montserrat-Medium.woff2');

const FONT_FACES = `
@font-face {
  font-family: 'Cormorant Garamond';
  font-style: normal;
  font-weight: 400;
  src: url(data:font/woff2;base64,${CORMORANT}) format('woff2');
}
@font-face {
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 500;
  src: url(data:font/woff2;base64,${MONTSERRAT}) format('woff2');
}
`;

// ---- Cards --------------------------------------------------------------
const QUOTE_W = 2160;
const QUOTE_H = 2700;

// One consistent quote size across all six, chosen so the longest quote
// wraps comfortably inside the ~75% measure.
const QUOTE_FONT_PX = 128;

const quoteCards = [
  { file: 'quote_look_safe.png',           text: 'The people who look safe and the people who are safe are rarely the same list.' },
  { file: 'quote_compounding_corner.png',  text: 'You don’t hire compounding people. You build the corner they grow in.' },
  { file: 'quote_advice_kindness.png',     text: 'The most dangerous career advice sounds like kindness.' },
  { file: 'quote_retention_risk.png',      text: 'Your best expert may be your quietest retention risk.' },
  { file: 'quote_competitor_twice.png',    text: 'What a competitor will pay for twice.' },
  { file: 'quote_title_travel.png',        text: 'A title doesn’t travel.' },
];

function quoteHTML(text) {
  return `<!doctype html><html><head><meta charset="utf-8"><style>
    ${FONT_FACES}
    * { margin: 0; padding: 0; box-sizing: border-box; }
    html, body { width: ${QUOTE_W}px; height: ${QUOTE_H}px; }
    body {
      background: ${SAND};
      display: flex;
      align-items: center;
      justify-content: center;
      -webkit-font-smoothing: antialiased;
      text-rendering: geometricPrecision;
    }
    .block {
      width: 75%;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
    }
    .quote {
      font-family: 'Cormorant Garamond', serif;
      font-weight: 400;
      color: ${NAVY};
      font-size: ${QUOTE_FONT_PX}px;
      line-height: 1.3;
    }
    .rule {
      width: 180px;
      height: 4px;
      background: ${GOLD};
      margin: 96px 0;
      border: 0;
    }
    .attr {
      font-family: 'Montserrat', sans-serif;
      font-weight: 500;
      color: ${NAVY};
      text-transform: uppercase;
      letter-spacing: 0.34em;
      font-size: 38px;
      /* letter-spacing pushes the block optically right; nudge back */
      margin-right: -0.34em;
    }
  </style></head><body>
    <div class="block">
      <div class="quote">${text}</div>
      <hr class="rule">
      <div class="attr">The Capability Audit</div>
    </div>
  </body></html>`;
}

// ---- Density teaser -----------------------------------------------------
const TEASER_W = 2245;
const TEASER_H = 1587;

function teaserHTML() {
  const rectW = Math.round(TEASER_W * 0.55); // ~1235
  const rectH = Math.round(TEASER_H * 0.45); // ~714
  return `<!doctype html><html><head><meta charset="utf-8"><style>
    ${FONT_FACES}
    * { margin: 0; padding: 0; box-sizing: border-box; }
    html, body { width: ${TEASER_W}px; height: ${TEASER_H}px; }
    body {
      background: ${SAND};
      position: relative;
      -webkit-font-smoothing: antialiased;
      text-rendering: geometricPrecision;
    }
    .sans {
      font-family: 'Montserrat', sans-serif;
      font-weight: 500;
      text-transform: uppercase;
      letter-spacing: 0.34em;
      font-size: 34px;
      color: ${NAVY};
      position: absolute;
      left: 50%;
      transform: translateX(-50%);
      /* offset letter-spacing so text is optically centered */
      padding-left: 0.34em;
    }
    .kicker { top: 12%; }
    .footer { bottom: 10%; }
    .rect {
      position: absolute;
      left: 50%;
      top: 50%;
      transform: translate(-50%, -50%);
      width: ${rectW}px;
      height: ${rectH}px;
      background: ${NAVY};
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
    }
    .density {
      font-family: 'Cormorant Garamond', serif;
      font-weight: 400;
      text-transform: uppercase;
      color: ${WHITE};
      font-size: 220px;
      line-height: 1;
      letter-spacing: 0.04em;
      padding-left: 0.04em;
    }
    .subtitle {
      font-family: 'Cormorant Garamond', serif;
      font-weight: 400;
      color: ${GOLD};
      font-size: 64px;
      line-height: 1.2;
      margin-top: 28px;
    }
  </style></head><body>
    <div class="sans kicker">Toward the Next Book</div>
    <div class="rect">
      <div class="density">Density</div>
      <div class="subtitle">The mechanism behind The Capability Audit.</div>
    </div>
    <div class="sans footer">The Density Group</div>
  </body></html>`;
}

// ---- Render -------------------------------------------------------------
async function render(page, html, width, height, outFile) {
  await page.setViewportSize({ width, height });
  await page.setContent(html, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: join(ROOT, outFile), clip: { x: 0, y: 0, width, height } });
  console.log('  wrote', outFile);
}

const browser = await chromium.launch({ args: ['--force-color-profile=srgb'] });
const page = await browser.newPage({ deviceScaleFactor: 1 });

console.log('Quote cards (%dx%d):', QUOTE_W, QUOTE_H);
for (const c of quoteCards) {
  await render(page, quoteHTML(c.text), QUOTE_W, QUOTE_H, c.file);
}

console.log('Teaser card (%dx%d):', TEASER_W, TEASER_H);
await render(page, teaserHTML(), TEASER_W, TEASER_H, 'teaser_density.png');

await browser.close();
console.log('Done. 7 cards rendered.');
