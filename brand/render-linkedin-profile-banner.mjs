// Renders brand/linkedin-profile-banner.html to /linkedin-profile-banner.png
// at exact LinkedIn personal-banner dimensions (1584 x 396).
//
//   node brand/render-linkedin-profile-banner.mjs
//
// Requires playwright with Chromium available (PLAYWRIGHT_BROWSERS_PATH).

import { fileURLToPath, pathToFileURL } from 'node:url';
import { createRequire } from 'node:module';
import path from 'node:path';

// Resolve playwright from the local install if there is one, otherwise from the
// global install (ESM ignores NODE_PATH, so the fallback has to be explicit).
const require = createRequire(import.meta.url);
let chromium;
try {
  ({ chromium } = await import('playwright'));
} catch {
  const globalRoot = require('node:child_process')
    .execSync('npm root -g', { encoding: 'utf8' })
    .trim();
  ({ chromium } = require(path.join(globalRoot, 'playwright')));
}

const here = path.dirname(fileURLToPath(import.meta.url));
const source = path.join(here, 'linkedin-profile-banner.html');
const out = path.join(here, '..', 'linkedin-profile-banner.png');

const browser = await chromium.launch();
const page = await browser.newPage({
  viewport: { width: 1584, height: 396 },
  deviceScaleFactor: 1,
});
await page.goto('file://' + source);
await page.evaluate(() => document.fonts.ready);
await page.screenshot({ path: out, clip: { x: 0, y: 0, width: 1584, height: 396 } });
await browser.close();

console.log('wrote', out);
