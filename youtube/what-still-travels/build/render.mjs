/**
 * Renders the thumbnail master (and the feed simulations) to PNG with Chromium.
 *
 *   NODE_PATH=/opt/node22/lib/node_modules node build/render.mjs <src> <out> <w> <h> [dsf]
 *
 * The file is served over HTTP from the repository root so the SVG's relative
 * font and image references resolve exactly as they do on the site.
 */
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import { extname, join, resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createRequire } from 'node:module';

// createRequire honours NODE_PATH, so a globally installed playwright works.
const { chromium } = createRequire(import.meta.url)('playwright');

const [src, out, w, h, dsf = '1'] = process.argv.slice(2);
// repository root, resolved from this file's own location
const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '../../..');

const TYPES = {
  '.svg': 'image/svg+xml', '.html': 'text/html', '.png': 'image/png',
  '.woff2': 'font/woff2', '.css': 'text/css', '.jpg': 'image/jpeg',
};

const server = createServer(async (req, res) => {
  try {
    const p = join(ROOT, decodeURIComponent(req.url.split('?')[0]));
    const body = await readFile(p);
    res.writeHead(200, { 'Content-Type': TYPES[extname(p)] || 'application/octet-stream' });
    res.end(body);
  } catch {
    res.writeHead(404).end('not found');
  }
});
await new Promise((r) => server.listen(0, r));
const port = server.address().port;

const browser = await chromium.launch();
const page = await browser.newPage({
  viewport: { width: Number(w), height: Number(h) },
  deviceScaleFactor: Number(dsf),
});
await page.goto(`http://127.0.0.1:${port}/${src}`, { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);

// Report type metrics so the layout can be fitted against the real fonts.
const metrics = await page.evaluate(() => {
  const out = [];
  for (const t of document.querySelectorAll('text')) {
    const b = t.getBBox();
    out.push({
      text: t.textContent,
      x: Math.round(b.x), y: Math.round(b.y),
      w: Math.round(b.width), h: Math.round(b.height),
    });
  }
  return out;
});
if (metrics.length) console.log(JSON.stringify(metrics, null, 1));

await page.screenshot({ path: resolve(ROOT, out), type: 'png' });
await browser.close();
server.close();
console.log('wrote', out);
