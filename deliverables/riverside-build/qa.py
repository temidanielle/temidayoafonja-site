# -*- coding: utf-8 -*-
"""Geometry QA for the Riverside assets, measured in the browser.

PIL and the browser do not always break a line in the same place, so layout is
verified against the rendered DOM rather than against the predicted line count.
Every text block reports its true box, and the checks below are the ones that
would otherwise only be caught by eye.
"""
import json

CAPTION_LIMIT = 860                 # nothing important may extend below this
EDGE = 120                          # nothing may sit closer than this to an edge

JS = """
() => {
  const out = [];
  document.querySelectorAll('.slide').forEach((sl, i) => {
    const sb = sl.getBoundingClientRect();
    const els = [];
    sl.querySelectorAll('.el').forEach(el => {
      const r = el.getBoundingClientRect();
      const isText = el.classList.contains('tx');
      let t = '';
      if (isText) t = Array.from(el.querySelectorAll('p'))
                         .map(p => p.innerText).join(' | ');
      els.push({text: t, isText,
                x: r.left - sb.left, y: r.top - sb.top,
                w: r.width, h: r.height});
    });
    out.push({slide: i + 1, els});
  });
  return out;
}
"""


def measure(html_path):
    from playwright.sync_api import sync_playwright
    CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path=CHROME, args=["--no-sandbox"])
        pg = b.new_page(viewport={"width": 1920, "height": 1080},
                        device_scale_factor=1)
        pg.goto("file://" + html_path, wait_until="load")
        pg.wait_for_timeout(800)
        data = pg.evaluate(JS)
        b.close()
    return data


def check(data, names, caption_limit=CAPTION_LIMIT):
    """Return a list of problems. An empty list means the geometry is clean."""
    problems = []
    for sl in data:
        name = names[sl["slide"] - 1]
        texts = [e for e in sl["els"] if e["isText"] and e["text"].strip()]
        # 1. no two text blocks may overlap
        for i in range(len(texts)):
            for j in range(i + 1, len(texts)):
                a, b = texts[i], texts[j]
                ox = min(a["x"] + a["w"], b["x"] + b["w"]) - max(a["x"], b["x"])
                oy = min(a["y"] + a["h"], b["y"] + b["h"]) - max(a["y"], b["y"])
                if ox > 2 and oy > 2:
                    problems.append(
                        "%s: text overlap (%.0f x %.0f px) between %r and %r"
                        % (name, ox, oy, a["text"][:44], b["text"][:44]))
        # 2. nothing important below the caption line
        for e in texts:
            bottom = e["y"] + e["h"]
            if bottom > caption_limit:
                problems.append("%s: text reaches y=%.0f, below the caption line "
                                "at %d: %r" % (name, bottom, caption_limit,
                                               e["text"][:44]))
        # 3. safe margins
        for e in texts:
            if e["x"] < EDGE - 1:
                problems.append("%s: text starts at x=%.0f, inside the %dpx margin: %r"
                                % (name, e["x"], EDGE, e["text"][:44]))
            if e["x"] + e["w"] > 1920 - EDGE + 1:
                problems.append("%s: text reaches x=%.0f, inside the right margin: %r"
                                % (name, e["x"] + e["w"], e["text"][:44]))
            if e["y"] < EDGE - 1:
                problems.append("%s: text starts at y=%.0f, above the top margin: %r"
                                % (name, e["y"], e["text"][:44]))
    return problems
