# -*- coding: utf-8 -*-
"""Structural QA on every Word document, plus page images to look at.

The rendering runs from the saved .docx XML, not from the data that produced
it, so what gets inspected is what is actually inside the delivered file.
"""
import os, sys, glob, math, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                "VIDEOS_4-21_CORRECTED_RUNTIME/build")
import render_check as RC
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn
from PIL import Image


def docs():
    return sorted(glob.glob(os.path.join(OUT, "V2*", "**", "*.docx"),
                            recursive=True)
                  + glob.glob(os.path.join(OUT, "Shared", "*.docx")))


def section_width(d):
    """The real text column of this document, in inches."""
    from docx.shared import Emu
    s = d.sections[0]
    return Emu(int(s.page_width) - int(s.left_margin)
               - int(s.right_margin)).inches


def check(path):
    """Structural problems, measured against this document's own geometry."""
    d = Document(path)
    probs, w = [], section_width(d)
    for c in d.element.body.iterchildren():
        if c.tag == qn("w:tbl"):
            t = Table(c, d)
            for r in t.rows:
                total = sum(cell.width.inches for cell in r.cells
                            if cell.width is not None)
                if total > w + 0.02:
                    probs.append("table row %.2fin wide against a %.2fin "
                                 "text column" % (total, w))
                    break
            if not t.rows:
                probs.append("empty table")
        elif c.tag == qn("w:p"):
            p = Paragraph(c, d)
            for run in p.runs:
                if run.font.size is not None and run.font.size.pt < 7.5:
                    probs.append("type at %.1fpt: %r"
                                 % (run.font.size.pt, run.text[:32]))
    return probs


def render(paths, outdir, cols=3, w=560):
    os.makedirs(outdir, exist_ok=True)
    from playwright.sync_api import sync_playwright
    shots = []
    with sync_playwright() as pw:
        b = pw.chromium.launch(
            executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/"
                            "chrome", args=["--no-sandbox"])
        pg = b.new_page(viewport={"width": 900, "height": 1100})
        for p in paths:
            name = os.path.splitext(os.path.basename(p))[0]
            html = RC.to_html(p).replace(
                "@page { size: 8.5in 11in; margin: 0.8in 0.9in; }",
                "@page { size: 8.5in 11in; margin: 0.8in 0.9in; }\n"
                "body { width: 6.7in; padding: 0.7in 0; background:#fff; "
                "margin:0 auto; }")
            hp = os.path.join(outdir, name + ".html")
            open(hp, "w").write(html)
            pg.goto("file://" + os.path.abspath(hp))
            pg.wait_for_timeout(120)
            total = pg.evaluate("document.body.scrollHeight")
            for i in range(int(math.ceil(total / 1100.0))):
                pg.evaluate("window.scrollTo(0, %d)" % (i * 1100))
                sp = os.path.join(outdir, "%s_p%02d.png" % (name, i + 1))
                pg.screenshot(path=sp)
                shots.append(sp)
        b.close()
    return shots


def sheet(paths, path, cols=5, w=330):
    h = int(w * 1100 / 900.0)
    rows = int(math.ceil(len(paths) / float(cols)))
    sh = Image.new("RGB", (cols * w + (cols + 1) * 10,
                           rows * h + (rows + 1) * 10), (222, 218, 210))
    for i, p in enumerate(paths):
        im = Image.open(p).convert("RGB").resize((w, h), Image.LANCZOS)
        sh.paste(im, (10 + (i % cols) * (w + 10), 10 + (i // cols) * (h + 10)))
    sh.save(path)
    return path


if __name__ == "__main__":
    paths = docs()
    bad = 0
    for p in paths:
        probs = check(p)
        bad += len(probs)
        if probs:
            print("%s" % os.path.relpath(p, OUT))
            for x in probs:
                print("    %s" % x)
    print("%d documents checked, %d structural problems" % (len(paths), bad))
    if len(sys.argv) > 1:
        d = sys.argv[1]
        shots = render(paths, d)
        print("%d page images" % len(shots))
        for i in range(0, len(shots), 25):
            print(sheet(shots[i:i + 25], os.path.join(d, "sheet%02d.png"
                                                      % (i // 25 + 1))))
