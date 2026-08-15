#!/usr/bin/env node
/**
 * Checks the exported covers against each other.
 *
 *   node covers/verify-covers.mjs
 *
 * Reads the pixels back out of every PNG in covers/output/ and reports where the
 * title ink actually sits. A cover rendered at the wrong size, or an export left
 * behind by an interrupted build, shows up here as an outlier — the covers only
 * work as a family if the title block lands in the same place on each one.
 *
 * Exits non-zero if any cover's title width or top edge is off the group by more
 * than the tolerance below.
 */
import { chromium } from 'playwright';
import { createServer } from 'node:http';
import { readFile, readdir } from 'node:fs/promises';
import { extname, join, normalize } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = fileURLToPath(new URL('..', import.meta.url));

// Titles are set at one shared size but the copy differs, so the longest line of
// each cover lands within a few px of the others rather than exactly on it.
const WIDTH_TOLERANCE = 60;
const TOP_TOLERANCE = 6;

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.png': 'image/png',
  '.woff2': 'font/woff2',
};

const server = createServer(async (req, res) => {
  const path = normalize(decodeURIComponent(new URL(req.url, 'http://localhost').pathname));
  const file = join(ROOT, path);
  if (!file.startsWith(ROOT)) return void res.writeHead(403).end();
  try {
    const body = await readFile(file);
    res.writeHead(200, { 'content-type': MIME[extname(file)] ?? 'application/octet-stream' });
    res.end(body);
  } catch {
    res.writeHead(404).end();
  }
});

const port = await new Promise(resolve =>
  server.listen(0, '127.0.0.1', () => resolve(server.address().port)));

const files = (await readdir(join(ROOT, 'covers', 'output')))
  .filter(f => f.endsWith('.png'))
  .sort();

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 200, height: 200 } });
// Same origin as the PNGs, so the canvas is readable.
await page.goto(`http://127.0.0.1:${port}/covers/brief-cover.html`);

const results = [];
for (const file of files) {
  const box = await page.evaluate(async url => {
    const img = new Image();
    img.src = url;
    await img.decode();
    const canvas = document.createElement('canvas');
    canvas.width = img.width;
    canvas.height = img.height;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(img, 0, 0);
    const data = ctx.getImageData(0, 0, canvas.width, canvas.height).data;

    // Scan the title band only: below the masthead, above the gold divider.
    let minX = Infinity, maxX = -1, minY = Infinity, maxY = -1;
    for (let y = 180; y < 560; y++) {
      for (let x = 0; x < canvas.width; x++) {
        const i = (y * canvas.width + x) * 4;
        if (data[i] > 150 && data[i + 1] > 150 && data[i + 2] > 150) {
          if (x < minX) minX = x;
          if (x > maxX) maxX = x;
          if (y < minY) minY = y;
          if (y > maxY) maxY = y;
        }
      }
    }
    return { size: `${img.width}x${img.height}`, left: minX, width: maxX - minX, top: minY };
  }, `http://127.0.0.1:${port}/covers/output/${file}`);
  results.push({ file, ...box });
}

await browser.close();
server.close();

const widths = results.map(r => r.width);
const tops = results.map(r => r.top);
const widthSpread = Math.max(...widths) - Math.min(...widths);
const topSpread = Math.max(...tops) - Math.min(...tops);

for (const r of results) {
  console.log(`${r.file.padEnd(64)} ${r.size}  title ${r.width}px wide, top ${r.top}`);
}
console.log(`\ntitle width spread ${widthSpread}px (tolerance ${WIDTH_TOLERANCE})`);
console.log(`title top spread   ${topSpread}px (tolerance ${TOP_TOLERANCE})`);

if (widthSpread > WIDTH_TOLERANCE || topSpread > TOP_TOLERANCE) {
  console.error('\nFAIL: a cover is out of family. Re-run covers/build-covers.mjs.');
  process.exit(1);
}
console.log('\nOK: the covers are one family.');
