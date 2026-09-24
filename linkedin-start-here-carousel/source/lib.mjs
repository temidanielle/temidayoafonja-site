/** Fonts, the type scale, and a wrapper that measures in the real face. */
import { readFile } from 'node:fs/promises';
import { join } from 'node:path';

const REPO = '/home/user/temidayoafonja-site';
const b64 = async f => (await readFile(join(REPO, 'fonts', f))).toString('base64');
export const FONTS = {
  s400: await b64('DMSans-400-normal-latin-1c49a6.woff2'),
  s500: await b64('DMSans-500-normal-latin-1c49a6.woff2'),
  s600: await b64('DMSans-600-normal-latin-1c49a6.woff2'),
};
export const PORTRAIT = (await readFile(join(REPO, 'images', 'temidayo-gold-ivory.png')))
  .toString('base64');

export const esc = s => String(s)
  .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

/**
 * The shared system's scale with the 28px floor applied. The previous version
 * of this carousel set its tracked labels at 21px and shrank headlines to fit;
 * this one holds the floor and lets the body text fill the card instead.
 */
export function styles(t) {
  return `
      @font-face { font-family:'DM Sans'; font-weight:400; font-style:normal;
        src:url(data:font/woff2;base64,${FONTS.s400}) format('woff2'); }
      @font-face { font-family:'DM Sans'; font-weight:500; font-style:normal;
        src:url(data:font/woff2;base64,${FONTS.s500}) format('woff2'); }
      @font-face { font-family:'DM Sans'; font-weight:600; font-style:normal;
        src:url(data:font/woff2;base64,${FONTS.s600}) format('woff2'); }
      text { font-family:'DM Sans', system-ui, sans-serif; }

      /* The two navy cards, the cover and the close. */
      .kicker  { font-weight:600; font-size:30px; letter-spacing:.2em;    fill:${t.gold}; }
      .cover   { font-weight:600; font-size:74px; letter-spacing:-.016em; fill:${t.cream}; }
      .coverSub{ font-weight:400; font-size:36px;                         fill:${t.cream}; fill-opacity:.88; }
      .sayUp   { font-weight:600; font-size:58px; letter-spacing:-.014em; fill:${t.cream}; }
      .bodyUp  { font-weight:400; font-size:36px;                         fill:${t.cream}; fill-opacity:.9; }
      .closing { font-weight:500; font-size:40px;                         fill:${t.bright}; }
      .sig     { font-weight:600; font-size:28px; letter-spacing:.13em;   fill:${t.cream}; }

      /* The statements and the four questions, on the cream card. */
      .say     { font-weight:600; font-size:60px; letter-spacing:-.014em; fill:${t.navy}; }
      .numeral { font-weight:600; font-size:96px; letter-spacing:-.01em;  fill:${t.gold};
                 font-variant-numeric:tabular-nums; }
      .body    { font-weight:400; font-size:38px;                         fill:${t.ink}; }
      .note    { font-weight:400; font-size:34px;                         fill:${t.muted}; }
      .counter { font-weight:600; font-size:28px; letter-spacing:.14em;   fill:${t.goldInk}; }
      .counterUp{font-weight:600; font-size:28px; letter-spacing:.14em;   fill:${t.gold}; }`;
}

export function block(cls, x, baseline, lines, lead, extra = '') {
  const spans = lines.map((l, i) =>
    `<tspan x="${x}"${i ? ` dy="${lead}"` : ''}>` +
    `${esc(i < lines.length - 1 ? `${l} ` : l)}</tspan>`).join('');
  return `  <text class="${cls}" x="${x}" y="${baseline}"${extra}>${spans}</text>`;
}

export async function wrapAll(page, t, requests) {
  const css = styles(t);
  return page.evaluate(({ css, reqs }) => {
    const NS = 'http://www.w3.org/2000/svg';
    const svg = document.createElementNS(NS, 'svg');
    const style = document.createElementNS(NS, 'style');
    style.textContent = css; svg.appendChild(style);
    const probe = document.createElementNS(NS, 'text'); svg.appendChild(probe);
    svg.setAttribute('width', '4000'); document.body.appendChild(svg);
    const width = (s, cls) => { probe.setAttribute('class', cls); probe.textContent = s;
      return probe.getComputedTextLength(); };
    const out = {};
    for (const r of reqs) {
      const words = r.text.split(' ');
      const lines = []; let line = '';
      for (const w of words) {
        const next = line ? `${line} ${w}` : w;
        if (line && width(next, r.cls) > r.width) { lines.push(line); line = w; }
        else line = next;
      }
      if (line) lines.push(line);
      out[r.k] = lines;
    }
    svg.remove();
    return out;
  }, { css, reqs: requests });
}
