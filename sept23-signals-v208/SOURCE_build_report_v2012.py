# -*- coding: utf-8 -*-
"""Change Log and QA Report, v2.0.11 -> v2.0.12.

Records the Signals Worth Watching section and the v2.0.9 re-cut, corrects the
three statements the report made that are no longer true, and adds twelve
verification items for the new work. Em dashes are swept out of the whole
document.

The three corrections matter more than the new section:

  - The workbook line said UNCHANGED FROM v2.0.2 THROUGH v2.0.10. The workbook
    has now changed twice, and its Acrobat behaviour test does not carry over.
  - The deck line named v2.0.7 as current.
  - The source-of-truth map named PowerPoint v2.0.7 and workbook v2.0.1.

A QA report that names the wrong current artifact is worse than one that says
nothing, because someone will pick up the file it names.
"""
import copy, hashlib, os, re, shutil
import docx
from docx.text.paragraph import Paragraph

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join("sept23-v208-assets",
                   "Free_Flagship_60MIN_v2.0.11_Change_Log_and_QA_Report.docx")
DST = os.path.join(HERE,
                   "Free_Flagship_60MIN_v2.0.12_Change_Log_and_QA_Report.docx")

EM = "—"
OLD_STAMP = "Saturday, September 19, 2026 at 2:05 PM CT"
NEW_STAMP = "Friday, September 25, 2026 at 9:10 AM CT"

SECTION_HEAD = "Signals Worth Watching and the v2.0.9 re-cut"
SECTION_BODY = (
 "A new section and six owner decisions. The deck is v2.0.9, the workbook is "
 "v2.0.3 and the SOP is v2.0.11. The base was the owner's own working copy, "
 "not the repository deck, so the numerals on the four states and the bold "
 "seven-categories promise were already present and only the minute had to be "
 "added to the boundary slide.")

CHANGES = [
 ("Where", "Change"),
 ("New slides 22, 23 and 24",
  "Signals Worth Watching, Signals around your role, and Signals when things "
  "feel fine. Placed after What Each State Costs and before Seven Categories "
  "of Move. Content promoted and expanded from the Position Exposure Signals "
  "appendix and from the state-costs line about renewal. Every signal is "
  "phrased as something to examine. No forecast, no statistic, no claim about "
  "the job market or any employer."),
 ("Timing",
  "The section runs sixty seconds a slide, not the two minutes the brief asked "
  "for, because six minutes do not exist in this session. Calibration gives "
  "1:00, the re-total 0:30, the sensitivity check 0:30 and the close buffer "
  "1:00. The twelve-minute rescore is SHIFTED to 18:00-30:00, never shortened. "
  "Q&A still starts at 50:00. Each note carries about two minutes of material "
  "and says which part is the live read."),
 ("Opening five minutes",
  "The welcome slide claimed 1:00-3:00 and overlapped four slides. The opening "
  "block is now 0:00-1:00, with slide 1 holding 0:00-0:30 and the welcome slide "
  "0:30-1:00. The reframe, the boundary slide and the two definitions are "
  "re-cut behind it and still hand off at 5:00. The two definition slides go "
  "from ninety seconds to seventy-five."),
 ("Poll slide",
  "What moved when you tested your first read leaves the timed core and sits "
  "last in the appendix, hidden. A near-duplicate of it was already hidden in "
  "the appendix; both are now there and one can be retired."),
 ("Dividers",
  "The Definitions and Matrix dividers had speaker notes copied from the "
  "closing slide, claiming 47:00-50:00. Both now read: Divider. Advance "
  "immediately. No time claim."),
 ("Move categories",
  "Two renamed to the approved carousel wording on the deck and in the "
  "workbook: Repair the conditions, and Seek an outside perspective. The other "
  "five already matched the carousel exactly and were not touched. All seven "
  "descriptions are unchanged."),
 ("Next-Move Note",
  "The closing band drops its not-X-it-is-Y construction and reads: This note "
  "records what your evidence supports testing next. The slide and workbook "
  "page 8 both carry the new line: Two signals I will watch before my rescore "
  "date, with two blanks. In the workbook those are real form fields, signal_1 "
  "and signal_2, taking the count from 68 to 70."),
 ("Em dashes",
  "All 43 removed from the deck, on faces and in notes, each replaced with a "
  "period, comma or colon chosen for that sentence. 28 removed from the SOP and "
  "every one in this report. Zero remain in any of the four documents."),
 ("US English",
  "13 British spellings replaced in the deck: travelled, travelling, "
  "neighbouring six times, centre, totalling, favourites, recognises and "
  "organisational."),
 ("Footer numbers",
  "Renumbered sequentially across the 28 numbered core slides. This was not "
  "cosmetic: the welcome slide had been inserted without renumbering, so two "
  "slides both read 1 and every number after them was one low. Nineteen slides "
  "changed number."),
 ("Retention Read and Transition Read",
  "The Retention Read deck does not exist in this repository, in either "
  "edition, so the section could not be added to it. A build spec was written "
  "instead. The Transition Read is excluded by decision and the exclusion is "
  "recorded in that spec."),
]

NEW_CHECKS = [
 ("247", "Signals content", "PASS",
  "All ten signals appear on the faces, once each, in the order written."),
 ("248", "Signals boundary", "PASS",
  "No forecast, statistic or market claim on any of the three faces or in "
  "their notes. Both notes state that a signal is a reason to gather evidence, "
  "not a reason to panic or leave."),
 ("249", "Placement", "PASS",
  "The section sits after What Each State Costs and before Seven Categories "
  "of Move, verified by reading the neighbouring slides."),
 ("250", "Protected block", "PASS",
  "The rescore still reads TWELVE MINUTES, PROTECTED AND NON-NEGOTIABLE, at "
  "18:00-30:00. Shifted, not shortened."),
 ("251", "Q&A boundary", "PASS", "Q&A still reads 50:00-60:00."),
 ("252", "Opening overlap", "PASS",
  "The six opening windows tile 0:00 to 5:00 with no gap and no overlap, "
  "asserted by the build."),
 ("253", "Dividers", "PASS",
  "Both divider notes read Divider. Advance immediately, and contain no time."),
 ("254", "Poll slide", "PASS",
  "Last in the deck and hidden, out of the timed core."),
 ("255", "Em dashes", "PASS",
  "Zero in the deck, zero in the SOP, zero in this report."),
 ("256", "US English", "PASS",
  "No British spelling survives anywhere in the deck, asserted by the build."),
 ("257", "Move categories", "PASS",
  "All seven carousel names appear once on the deck slide and once on workbook "
  "page 8. Neither retired name appears anywhere."),
 ("258", "Workbook fidelity", "PASS",
  "v2.0.1 was rebuilt from source and reproduced the distributed PDF exactly, "
  "zero text-position differences on eight pages and 68 identical fields, "
  "before any change was made. v2.0.3 differs from it only in the pacing cues, "
  "the page 8 line, the two category names and two new fields."),
]

FIXES = [
 ("UNCHANGED FROM v2.0.2 THROUGH v2.0.10. The workbook was not regenerated",
  "CHANGED IN v2.0.2 AND v2.0.3, AND ITS ACROBAT BEHAVIOUR TEST DOES NOT CARRY "
  "OVER. Through v2.0.10 the workbook was not regenerated"),
 ("DECK IS NOW v2.0.7.", "DECK IS NOW v2.0.9."),
 ("PowerPoint v2.0.7, workbook v2.0.",
  "PowerPoint v2.0.9, workbook v2.0.3, SOP v2.0.11. Superseded: workbook v2.0."),
]


def carrier(para):
    runs = para.runs
    return next((r for r in runs if r.text.strip()), runs[0]) if runs else None


def set_para(para, text):
    keep = carrier(para)
    assert keep is not None
    keep.text = text
    for r in para.runs:
        if r._r is not keep._r:
            r._r.getparent().remove(r._r)


def set_cell(cell, text):
    p = cell.paragraphs[0]
    for extra in cell.paragraphs[1:]:
        extra._element.getparent().remove(extra._element)
    set_para(p, text)


def every_run(doc):
    for p in doc.paragraphs:
        for r in p.runs:
            yield r
    for t in doc.tables:
        for row in t.rows:
            for c in row.cells:
                for p in c.paragraphs:
                    for r in p.runs:
                        yield r


def count_em(doc):
    return (sum(p.text.count(EM) for p in doc.paragraphs)
            + sum(c.text.count(EM) for t in doc.tables for row in t.rows
                  for c in row.cells))


def find_para(doc, needle):
    hits = [i for i, p in enumerate(doc.paragraphs) if needle in p.text]
    assert len(hits) == 1, f"{needle!r} found {len(hits)} times"
    return hits[0]


def build():
    shutil.copyfile(SRC, DST)
    d = docx.Document(DST)
    before_em = count_em(d)

    # 1. counts and stamps, done first so the corrections below can
    #    name SOP v2.0.11 without this pass rewriting it
    for r in every_run(d):
        t = (r.text.replace("246 of 246 PASS", "258 of 258 PASS")
                   .replace("Verification ", "Verification ")
                   .replace("246 items", "258 items")
                   .replace("v2.0.11", "v2.0.12")
                   .replace(OLD_STAMP, NEW_STAMP))
        if t != r.text:
            r.text = t

    # 2. the three corrections
    hits = {old: 0 for old, _ in FIXES}
    for r in every_run(d):
        t = r.text
        for old, new in FIXES:
            if old in t:
                hits[old] += t.count(old)
                t = t.replace(old, new)
        if t != r.text:
            r.text = t
    for old, n in hits.items():
        assert n == 1, f"correction matched {n} times: {old[:50]!r}"

    # 3. the new section, inserted before the verification heading
    anchor_i = find_para(d, "Verification ")
    anchor = d.paragraphs[anchor_i]
    head_src = d.paragraphs[find_para(d, "September 19 revision ")]
    body_src = d.paragraphs[find_para(d, "A focused revision of an approved")]

    head_el = copy.deepcopy(head_src._element)
    anchor._element.addprevious(head_el)
    set_para(Paragraph(head_el, anchor._parent), SECTION_HEAD)
    body_el = copy.deepcopy(body_src._element)
    head_el.addnext(body_el)
    set_para(Paragraph(body_el, anchor._parent), SECTION_BODY)

    tbl_src = d.tables[9]._element        # a Where / Change table
    tbl_el = copy.deepcopy(tbl_src)
    body_el.addnext(tbl_el)
    d = docx.Document(DST) if False else d
    new_tbl = [t for t in d.tables if t._element is tbl_el][0]
    template = copy.deepcopy(new_tbl.rows[1]._element)
    while len(new_tbl.rows) > 1:
        new_tbl._element.remove(new_tbl.rows[-1]._element)
    for ci, v in enumerate(CHANGES[0]):
        set_cell(new_tbl.rows[0].cells[ci], v)
    for row in CHANGES[1:]:
        new_tbl._element.append(copy.deepcopy(template))
        for ci, v in enumerate(row):
            set_cell(new_tbl.rows[-1].cells[ci], v)

    # 4. twelve new verification items on the last QA table
    qa = d.tables[-1]
    assert [c.text for c in qa.rows[0].cells] == ["#", "Category", "Status",
                                                  "Notes"], "last QA table"
    qtemplate = copy.deepcopy(qa.rows[-1]._element)
    for row in NEW_CHECKS:
        qa._element.append(copy.deepcopy(qtemplate))
        for ci, v in enumerate(row):
            set_cell(qa.rows[-1].cells[ci], v)

    # 5. em dashes
    for r in every_run(d):
        if EM in r.text:
            t = re.sub(r"\s*" + EM + r"\s*", ". ", r.text)
            r.text = re.sub(r"\.\s*\.", ".", t)

    d.save(DST)

    out = docx.Document(DST)
    assert count_em(out) == 0, f"{count_em(out)} em dashes left"
    body = ("\n".join(p.text for p in out.paragraphs) + "\n"
            + "\n".join(c.text for t in out.tables for row in t.rows
                        for c in row.cells))
    assert "258 of 258 PASS" in body, "the pass count was not updated"
    assert "258 items" in body, "the verification heading was not updated"
    assert SECTION_HEAD in body, "the new section is missing"
    assert "DECK IS NOW v2.0.9." in body
    assert "PowerPoint v2.0.9, workbook v2.0.3, SOP v2.0.11" in body
    for stale in ("246 of 246", "DECK IS NOW v2.0.7", OLD_STAMP):
        assert stale not in body, f"stale: {stale}"
    for n, _, _, _ in NEW_CHECKS:
        assert n in body, f"check {n} missing"

    print("built", os.path.basename(DST))
    print(f"  new change rows: {len(CHANGES) - 1}   new checks: {len(NEW_CHECKS)}")
    print(f"  em dashes: {before_em} -> {count_em(out)}")
    print("  sha256", hashlib.sha256(open(DST, "rb").read()).hexdigest())
    return DST


if __name__ == "__main__":
    build()
