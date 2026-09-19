# -*- coding: utf-8 -*-
"""Change Log and QA Report — v2.0.10 -> v2.0.11. Documentation correction only.

One paragraph was wrong and one claim was too broad.

  WRONG   The visual-QA paragraph still said "The v2.0.9 export is EXACTLY EIGHT
          PAGES" and described "pages 4 through 7 portrait". The shipped preview
          is v2.0.10, and its orientation is page 1 portrait, pages 2 and 3
          landscape, pages 4 through 8 portrait.

  TOO BROAD   It read as though the page count were a property of the document.
          It is not. A .docx has no fixed pagination; Word, Writer and other
          renderers break pages differently. The controlled claim is about the
          LibreOffice preview shipped in this package.

Nothing else changes. No slide, no workbook, no SOP content, no methodology. The
SOP is NOT edited to force a page count in any other renderer.
"""
import copy, hashlib, importlib, os, shutil, sys
import docx

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
SRC = "sept23-v207-assets/Free_Flagship_60MIN_v2.0.10_Change_Log_and_QA_Report.docx"
OUT = "scratchpad/sept23/out"
DST = f"{OUT}/Free_Flagship_60MIN_v2.0.11_Change_Log_and_QA_Report.docx"
STAMP = "Saturday, September 19, 2026 at 2:05 PM CT"
OLD = "Saturday, September 19, 2026 at 11:20 AM CT"

STALE = ("SOP. Exported with LibreOffice Writer as "
         "PREVIEW_SOP_60MIN_v2.0.10_LibreOffice.pdf")

CORRECTED = (
 "SOP. The shipped preview is PREVIEW_SOP_60MIN_v2.0.10_LibreOffice.pdf, exported "
 "with LibreOffice Writer from the delivered .docx and inspected page by page. IT "
 "IS EIGHT PAGES: page 1 portrait, pages 2 and 3 landscape carrying the "
 "reconciliation table seven rows then six, and pages 4 through 8 portrait. There "
 "is no blank, divider-only, transition-only or short spill page. The lightest is "
 "page 8, which carries thirty substantive lines once the repeated footer and "
 "revision stamp are discounted, with body ink reaching 42% down the page. Eight "
 "pages is the approved length and no operating control is cut to change it. THIS "
 "CLAIM IS ABOUT THE SHIPPED PREVIEW AND IS NOT ABOUT DOCX PAGINATION IN GENERAL. "
 "A .docx carries no fixed page count: Word, Writer and other renderers break "
 "pages differently, and nothing here asserts what any of them would produce. "
 "What is asserted is that the LibreOffice Writer export shipped in this package "
 "is eight pages, has no blank or stub final page, and has been visually "
 "inspected. The delivered preview was compared page by page against a fresh "
 "export of the delivered file: same page count, same orientation on each page, "
 "identical text. It is a genuine office-suite export, not a custom render of a "
 "parallel model. The SOP is NOT edited to force a particular pagination in any "
 "other renderer.")

CHANGE_ROW = (
 "Documentation correction, report v2.0.11",
 "The visual-QA paragraph still named the v2.0.9 export and described pages 4 "
 "through 7 as portrait. The shipped preview is v2.0.10 and its orientation runs "
 "page 1 portrait, pages 2 and 3 landscape, pages 4 through 8 portrait. The "
 "paragraph is corrected, and its claim is narrowed to the shipped LibreOffice "
 "preview rather than implying that a .docx has a renderer-independent page "
 "count. Documentation only: no slide, workbook, SOP content or methodology "
 "changed, and the SOP was not edited to force a page count elsewhere.")


def set_para(para, text):
    runs = para.runs
    keep = next((r for r in runs if r.text.strip()), runs[0])
    keep.text = text
    for r in runs:
        if r._r is not keep._r:
            r._r.getparent().remove(r._r)


def set_cell(cell, text):
    p = cell.paragraphs[0]
    for extra in cell.paragraphs[1:]:
        extra._element.getparent().remove(extra._element)
    set_para(p, text)


def build():
    os.makedirs(OUT, exist_ok=True)
    shutil.copyfile(SRC, DST)
    d = docx.Document(DST)

    def find(fragment):
        hits = [x for x in d.paragraphs if fragment in x.text]
        assert len(hits) == 1, f"{fragment[:44]!r} matched {len(hits)}"
        return hits[0]

    # the correction itself
    para = find(STALE)
    assert "The v2.0.9 export is EXACTLY EIGHT PAGES" in para.text
    assert "pages 4 through 7 portrait" in para.text
    set_para(para, CORRECTED)

    for x in [p for p in d.paragraphs if OLD in p.text]:
        for r in x.runs:
            if OLD in r.text:
                r.text = r.text.replace(OLD, STAMP)
    # The correction is written and saved BEFORE the checks run, because two of
    # them read this very paragraph back out of this very file. Importing the
    # check module first would have had it read the uncorrected copy that
    # shutil.copyfile just laid down, which is exactly what happened once.
    d.save(DST)
    qa = importlib.import_module("qa_v208")
    total = 162 + len(qa.R)
    passed = 162 + sum(1 for r in qa.R if r[3] == "PASS")

    for old, new in [("Verification — 244 items", f"Verification — {total} items"),
                     ("244 of 244 PASS.", f"{passed} of {total} PASS."),
                     ("QA REPORT v2.0.10", "QA REPORT v2.0.11")]:
        x = find(old)
        for r in x.runs:
            if old in r.text:
                r.text = r.text.replace(old, new)
                break
        else:
            set_para(x, x.text.replace(old, new))
    for x in d.tables[0].rows[0].cells[0].paragraphs:
        for r in x.runs:
            r.text = r.text.replace("v2.0.10 CANDIDATE", "v2.0.11 CANDIDATE")

    # one change-log row, in the September 19 section's table
    log = next(t for t in d.tables
               if t.rows[0].cells[0].text == "Where"
               and any("Slide 22, visual only" in r.cells[0].text for r in t.rows))
    template = copy.deepcopy(log.rows[1]._element)
    log._element.append(copy.deepcopy(template))
    for ci, v in enumerate(CHANGE_ROW):
        set_cell(log.rows[-1].cells[ci], v)

    # the two new checks join Group O rather than starting a group of their own
    group_o = [t for t in d.tables if t.rows[0].cells[0].text == "#"][-1]
    assert group_o.rows[-1].cells[0].text == "244", \
        f"Group O does not end at 244, it ends at {group_o.rows[-1].cells[0].text}"
    row_tmpl = copy.deepcopy(group_o.rows[1]._element)
    for n, g, label, st, note in qa.R[-2:]:
        group_o._element.append(copy.deepcopy(row_tmpl))
        for ci, v in enumerate((str(162 + n), label, st, note)):
            set_cell(group_o.rows[-1].cells[ci], v)

    d.save(DST)
    assert passed == total, "the report cannot be saved while a check fails"
    return DST, passed, total


if __name__ == "__main__":
    path, p_, t_ = build()
    print("built", os.path.basename(path), f"({p_}/{t_})")
    print("  sha256", hashlib.sha256(open(path, "rb").read()).hexdigest())
