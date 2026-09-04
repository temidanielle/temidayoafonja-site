/* Career Evidence Starter: build the fillable PDF.
 *
 * Two stages, deliberately separated:
 *   1. Chromium prints starter-source.html to a US Letter PDF. The page uses the
 *      site's own woff2 faces through /fonts.css, so the type in the PDF is the
 *      real brand type rather than a substitute.
 *   2. pdf-lib adds AcroForm fields at coordinates measured from the placeholder
 *      boxes in that same HTML, so the fields land exactly on the printed rules.
 *
 * Measured, not assumed: the CSS px -> PDF pt factor and the page height are
 * both read back from the produced PDF and asserted before any field is placed.
 */
const { chromium } = require('playwright');
const { PDFDocument, StandardFonts, rgb } = require('pdf-lib');
const fs = require('fs');
const path = require('path');

const OUT_DIR = __dirname;
const SRC = 'http://127.0.0.1:8899/_build/career-evidence-starter/starter-source.html';
const FLAT = path.join(OUT_DIR, 'starter-flat.pdf');
const FINAL = path.join(OUT_DIR, 'Keep_the_Proof_Career_Evidence_Starter_v1.0_CANDIDATE.pdf');

const NAVY = rgb(0x0F / 255, 0x23 / 255, 0x47 / 255);
const WHITE = rgb(1, 1, 1);

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const page = await browser.newPage({ viewport: { width: 816, height: 1056 } });
  await page.goto(SRC, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  // Wait for every raster asset, then refuse to print if one of them is missing.
  // A 404 on the portrait or the Keep the Proof cover renders as an empty box,
  // which is exactly the kind of defect a silent build would ship.
  const images = await page.evaluate(async () => {
    await Promise.all([...document.images].map(i => i.complete ? null : i.decode().catch(() => null)));
    return [...document.images].map(i => ({ src: i.getAttribute('src'), w: i.naturalWidth, h: i.naturalHeight }));
  });
  const broken = images.filter(i => !i.w);
  if (broken.length) {
    throw new Error('image failed to load: ' + broken.map(i => i.src).join(', '));
  }
  images.forEach(i => console.error(`  image ok  ${i.src}  ${i.w}x${i.h}`));
  await page.waitForTimeout(700);

  // ── measure the placeholders, in CSS px, relative to their own page ──
  const measured = await page.evaluate(() => {
    const pages = [...document.querySelectorAll('.page')];
    const out = [];
    pages.forEach((pg, i) => {
      const pr = pg.getBoundingClientRect();
      pg.querySelectorAll('[data-field]').forEach(el => {
        const r = el.getBoundingClientRect();
        out.push({ kind: 'text', page: i, name: el.dataset.field,
          lines: +(el.dataset.lines || 1),
          x: r.left - pr.left, y: r.top - pr.top, w: r.width, h: r.height });
      });
      pg.querySelectorAll('[data-check]').forEach(el => {
        const r = el.getBoundingClientRect();
        out.push({ kind: 'check', page: i, name: el.dataset.check,
          x: r.left - pr.left, y: r.top - pr.top, w: r.width, h: r.height });
      });
    });
    return { fields: out, pageCount: pages.length,
             pageW: pages[0].getBoundingClientRect().width,
             pageH: pages[0].getBoundingClientRect().height };
  });

  await page.pdf({ path: FLAT, width: '8.5in', height: '11in', printBackground: true,
                   margin: { top: 0, right: 0, bottom: 0, left: 0 }, scale: 1 });
  await browser.close();

  // ── stage 2: fields ──
  const pdf = await PDFDocument.load(fs.readFileSync(FLAT));
  const pages = pdf.getPages();

  if (pages.length !== measured.pageCount) {
    throw new Error(`page count drifted: html ${measured.pageCount}, pdf ${pages.length}`);
  }
  const { width: ptW, height: ptH } = pages[0].getSize();
  const kx = ptW / measured.pageW;
  const ky = ptH / measured.pageH;
  if (Math.abs(kx - 0.75) > 0.005 || Math.abs(ky - 0.75) > 0.005) {
    throw new Error(`px->pt factor is not 0.75 (kx ${kx.toFixed(4)}, ky ${ky.toFixed(4)}); coordinates would be wrong`);
  }

  const form = pdf.getForm();
  const helv = await pdf.embedFont(StandardFonts.Helvetica);

  let textCount = 0, checkCount = 0;
  for (const f of measured.fields) {
    const pg = pages[f.page];
    const x = f.x * kx;
    const w = f.w * kx;
    const h = f.h * ky;
    const y = ptH - (f.y * ky) - h;   // HTML top-left origin -> PDF bottom-left

    if (f.kind === 'text') {
      const tf = form.createTextField(f.name);
      if (f.lines > 1) tf.enableMultiline();
      // addToPage must come first: it writes the /DA entry that setFontSize needs.
      tf.addToPage(pg, { x, y, width: w, height: h,
        borderWidth: 0, textColor: NAVY, backgroundColor: undefined });
      tf.setFontSize(f.lines > 1 ? 10 : 11);
      tf.updateAppearances(helv);
      textCount++;
    } else {
      const cb = form.createCheckBox(f.name);
      // The widget draws the box the reader sees, printed and on screen, so the
      // source HTML no longer draws one underneath it.
      cb.addToPage(pg, { x, y, width: w, height: h,
        borderWidth: 1, borderColor: NAVY, backgroundColor: WHITE });
      // For a checkbox this argument is an appearance-provider function, not a
      // font, so it is left to pdf-lib's default tick.
      cb.updateAppearances();
      checkCount++;
    }
  }

  // Readers must show what is typed even before they regenerate appearances.
  form.updateFieldAppearances(helv);
  // Do NOT flatten: the whole point is that it stays fillable and re-savable.

  pdf.setTitle('Keep the Proof: The 10-Minute Career Evidence Starter');
  pdf.setSubject('Free Career Accomplishment Tracker');
  pdf.setAuthor('Temidayo Afonja');
  pdf.setProducer('The Density Group');
  pdf.setCreator('The Density Group');
  pdf.setLanguage('en-US');

  fs.writeFileSync(FINAL, await pdf.save());
  console.log(JSON.stringify({
    pages: pages.length,
    pageSizePt: [ptW, ptH],
    pxToPt: +kx.toFixed(4),
    textFields: textCount,
    checkboxes: checkCount,
    bytes: fs.statSync(FINAL).size,
  }, null, 1));
})();
