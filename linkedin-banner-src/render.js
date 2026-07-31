// Renders banner.html to a high-resolution PNG using headless Chromium.
//
// Usage:
//   node render.js [input.html] [output.png] [scale]
// Defaults:
//   input  = ./banner.html
//   output = ../linkedin-banner.png
//   scale  = 2   (1584x396 layout -> 3168x792 PNG)
//
// Requires: `npm i playwright` (or a globally installed playwright), and the
// Cormorant Garamond + DM Sans fonts available to the system (see README).

const path = require('path');

// Resolve playwright whether it's a local dep or a global install.
let chromium;
try {
  ({ chromium } = require('playwright'));
} catch (e) {
  const { execSync } = require('child_process');
  const globalRoot = execSync('npm root -g').toString().trim();
  ({ chromium } = require(path.join(globalRoot, 'playwright')));
}

(async () => {
  const htmlPath = path.resolve(process.argv[2] || path.join(__dirname, 'banner.html'));
  const outPath = path.resolve(process.argv[3] || path.join(__dirname, '..', 'linkedin-banner.png'));
  const scale = parseFloat(process.argv[4] || '2');

  // Let Playwright use its own bundled Chromium by default; allow an override
  // via CHROMIUM_PATH for locked-down environments that ship their own binary.
  const launchOpts = {};
  if (process.env.CHROMIUM_PATH) launchOpts.executablePath = process.env.CHROMIUM_PATH;

  const browser = await chromium.launch(launchOpts);
  const page = await browser.newPage({
    viewport: { width: 1584, height: 396 },
    deviceScaleFactor: scale,
  });
  await page.goto('file://' + htmlPath);
  await page.evaluate(() => document.fonts.ready);
  const el = await page.$('.canvas');
  await el.screenshot({ path: outPath, type: 'png' });
  await browser.close();
  console.log('rendered', outPath, `(scale ${scale})`);
})();
