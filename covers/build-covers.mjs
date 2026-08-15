#!/usr/bin/env node
/**
 * Renders The Capability Formation Brief covers from covers/brief-cover.html.
 *
 *   node covers/build-covers.mjs                 # all editions, pure typographic
 *   node covers/build-covers.mjs --motif         # also write the faint-motif variants
 *   node covers/build-covers.mjs --scale=2       # 3328 x 1872 for print or retina
 *   node covers/build-covers.mjs edition-four    # one edition, matched by slug
 *
 * The page is served over http rather than opened from disk so the /fonts/ URLs
 * inside fonts.css resolve to the site's self-hosted woff2 files.
 */
import { chromium } from 'playwright';
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import { mkdir } from 'node:fs/promises';
import { extname, join, normalize } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = fileURLToPath(new URL('..', import.meta.url));
const OUT_DIR = join(ROOT, 'covers', 'output');

const WIDTH = 1664;
const HEIGHT = 936;

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.woff2': 'font/woff2',
  '.png': 'image/png',
  '.svg': 'image/svg+xml',
};

function startServer() {
  const server = createServer(async (req, res) => {
    const path = normalize(decodeURIComponent(new URL(req.url, 'http://localhost').pathname));
    const file = join(ROOT, path);
    if (!file.startsWith(ROOT)) {
      res.writeHead(403).end();
      return;
    }
    try {
      const body = await readFile(file);
      res.writeHead(200, { 'content-type': MIME[extname(file)] ?? 'application/octet-stream' });
      res.end(body);
    } catch {
      res.writeHead(404).end();
    }
  });
  return new Promise(resolve => {
    server.listen(0, '127.0.0.1', () => resolve({ server, port: server.address().port }));
  });
}

const args = process.argv.slice(2);
const withMotif = args.includes('--motif');
const scaleArg = args.find(a => a.startsWith('--scale='));
const scale = scaleArg ? Number(scaleArg.split('=')[1]) : 1;
const filters = args.filter(a => !a.startsWith('--'));

const config = JSON.parse(await readFile(join(ROOT, 'covers', 'editions.json'), 'utf8'));
const editions = filters.length
  ? config.editions.filter(e => filters.some(f => e.slug.includes(f)))
  : config.editions;

if (!editions.length) {
  console.error(`No edition matched: ${filters.join(', ')}`);
  process.exit(1);
}

await mkdir(OUT_DIR, { recursive: true });
const { server, port } = await startServer();
const browser = await chromium.launch();
const page = await browser.newPage({
  viewport: { width: WIDTH, height: HEIGHT },
  deviceScaleFactor: scale,
});

const variants = withMotif ? [false, true] : [false];

function coverUrl(edition, { motif = false, size = null } = {}) {
  const params = new URLSearchParams({
    publication: config.publication,
    byline: config.byline,
    title: edition.titleLines.join('|'),
    edition: edition.edition,
    date: edition.date,
  });
  if (motif) params.set('motif', '1');
  if (size) params.set('size', String(size));
  return `http://127.0.0.1:${port}/covers/brief-cover.html?${params}`;
}

async function load(url) {
  await page.goto(url, { waitUntil: 'networkidle' });
  await page.waitForFunction(() => document.documentElement.dataset.ready === 'true');
}

// Pass one: find the title size each edition fits at, then hold the whole set to
// the smallest. One type size across the family is what makes the covers read as
// one publication rather than three separate designs.
const sizes = [];
for (const edition of config.editions) {
  await load(coverUrl(edition));
  sizes.push(await page.evaluate(() => window.__fittedSize));
}
const titleSize = Math.min(...sizes);
console.log(`title size ${titleSize}px (fitted per edition: ${sizes.join(', ')})`);

// Pass two: render at the shared size.
for (const edition of editions) {
  for (const motif of variants) {
    await load(coverUrl(edition, { motif, size: titleSize }));

    const suffix = motif ? '-motif' : '';
    const name = `capability-formation-brief-${edition.slug}${suffix}.png`;
    await page.screenshot({ path: join(OUT_DIR, name), type: 'png' });
    console.log(`wrote covers/output/${name}  ${WIDTH * scale}x${HEIGHT * scale}`);
  }
}

await browser.close();
server.close();
