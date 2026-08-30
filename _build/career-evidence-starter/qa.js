/* QA: overflow check on the HTML source, then render the produced PDF page by
 * page through pdf.js and screenshot each canvas. Poppler and LibreOffice are
 * both unavailable in this container, so pdf.js is how the PDF actually gets
 * looked at rather than merely described. */
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const DIR = __dirname;
const PDF = path.join(DIR, 'Keep_the_Proof_Career_Evidence_Starter_v1.0_CANDIDATE.pdf');

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });

  // ── 1. overflow: does any page's content exceed its 11in box? ──
  const p = await browser.newPage({ viewport: { width: 816, height: 1056 } });
  await p.goto('http://127.0.0.1:8899/_build/career-evidence-starter/starter-source.html',
    { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(600);
  const overflow = await p.evaluate(() => {
    return [...document.querySelectorAll('.page')].map((pg, i) => {
      const style = getComputedStyle(pg);
      const padB = parseFloat(style.paddingBottom);
      const kids = [...pg.children].filter(c => !c.classList.contains('foot'));
      const contentBottom = kids.length
        ? Math.max(...kids.map(c => c.getBoundingClientRect().bottom))
        : 0;
      const foot = pg.querySelector('.foot');
      const footTop = foot ? foot.getBoundingClientRect().top : pg.getBoundingClientRect().bottom;
      return {
        page: i + 1,
        boxH: Math.round(pg.getBoundingClientRect().height),
        scrollH: Math.round(pg.scrollHeight),
        overflows: pg.scrollHeight > pg.getBoundingClientRect().height + 1,
        clearsFooter: contentBottom <= footTop + 1,
        slackPx: Math.round(footTop - contentBottom),
      };
    });
  });
  console.log('OVERFLOW CHECK');
  overflow.forEach(o => console.log('  page', o.page,
    'boxH', o.boxH, 'scrollH', o.scrollH,
    o.overflows ? '*** OVERFLOWS ***' : 'fits',
    '| clears footer:', o.clearsFooter, '| slack', o.slackPx + 'px'));
  await p.close();

  // ── 2. render the real PDF via pdf.js ──
  const viewer = `<!doctype html><meta charset="utf-8">
<body style="margin:0;background:#888">
<script src="/pdfjs/pdf.js"></script>
<script>
  window.__ready = false;
  pdfjsLib.GlobalWorkerOptions.workerSrc = '/pdfjs/pdf.worker.js';
  pdfjsLib.getDocument('/_build/career-evidence-starter/Keep_the_Proof_Career_Evidence_Starter_v1.0_CANDIDATE.pdf')
    .promise.then(async pdf => {
    window.__pages = pdf.numPages;
    for (let n=1;n<=pdf.numPages;n++) {
      const pg = await pdf.getPage(n);
      const vp = pg.getViewport({scale: 1.4});
      const c = document.createElement('canvas');
      c.id = 'pg'+n; c.width = vp.width; c.height = vp.height;
      c.style.display='block'; c.style.margin='0 0 12px';
      document.body.appendChild(c);
      await pg.render({canvasContext: c.getContext('2d'), viewport: vp}).promise;
    }
    window.__ready = true;
  }).catch(e => { window.__err = String(e); window.__ready = true; });
</script></body>`;
  fs.writeFileSync(path.join(DIR, 'viewer.html'), viewer);
  fs.writeFileSync('/home/user/temidayoafonja-site/_build/career-evidence-starter/viewer.html', viewer);

  const v = await browser.newPage({ viewport: { width: 900, height: 1200 } });
  v.on('console', m => console.log('   [viewer]', m.type(), m.text().slice(0,160)));
  v.on('pageerror', e => console.log('   [pageerror]', String(e).slice(0,200)));
  await v.goto('http://127.0.0.1:8899/_build/career-evidence-starter/viewer.html',
    { waitUntil: 'domcontentloaded' });
  await v.waitForFunction(() => window.__ready === true, { timeout: 60000 });
  const err = await v.evaluate(() => window.__err || null);
  if (err) throw new Error('pdf.js failed: ' + err);
  const n = await v.evaluate(() => window.__pages);
  console.log('\nPDF RENDER: pages =', n);
  for (let i = 1; i <= n; i++) {
    const c = await v.$('#pg' + i);
    await c.screenshot({ path: path.join(DIR, `page-${i}.png`) });
  }
  await v.close();
  await browser.close();
  console.log('rendered', n, 'page images');
})();
