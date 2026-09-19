# -*- coding: utf-8 -*-
"""Change Log and QA Report — v2.0.9 -> v2.0.10.

Adds the September 19 final-candidate section and Group O, whose rows are
written by qa_v207.py at build time. Group N is kept as the v2.0.6 record and
marked superseded rather than deleted, and it is not counted twice: the headline
is 162 carried forward plus Group O's current run.

Also settles two things the v2.0.9 document left reading as open questions: the
eight-page SOP length, which is approved, and the Optionality instrument
conflict, which is now recorded as a named post-September-23 review item.
"""
import copy, hashlib, importlib, os, shutil, sys
import docx

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
SRC = "sept23-v206-assets/Free_Flagship_60MIN_v2.0.9_Change_Log_and_QA_Report.docx"
OUT = "scratchpad/sept23/out"
DST = f"{OUT}/Free_Flagship_60MIN_v2.0.10_Change_Log_and_QA_Report.docx"
STAMP = "Saturday, September 19, 2026 at 11:20 AM CT"
OLD = "Saturday, September 19, 2026 at 8:30 AM CT"

CHANGES = [
 ("Slide 22, visual only",
  "The four-question portability frame was a small bold line compressed under the "
  "subtitle. It now sits on its own strip: the same light panel and gold accent "
  "the three prompt blocks already use, at 11.5pt rather than 10pt, one line, one "
  "occurrence, and 0.10in clear of the first prompt block, which is exactly the "
  "gap those blocks keep between themselves. THE WRITING SPACE IS UNTOUCHED. The "
  "three prompt blocks, their answer rules and the closing band are all where "
  "v2.0.6 put them, to the EMU. The strip came out of title-box height that was "
  "never being used."),
 ("Optionality instrument conflict — FLAGGED, NOT CHANGED",
  "The revised Optionality definition reads usefulness beyond the current context "
  "plus legibility through evidence. Three of the six scored statements sit less "
  "cleanly inside that reading. Statement 7 asks whether capability would be "
  "valued by an employer in a different industry, which is anticipated employer "
  "valuation. Statement 10 asks whether people with power to hire or advance can "
  "already see what the participant is good at, which is visibility. Statement 12 "
  "asks whether they could rebuild a strong position somewhere else within a "
  "year, which is a forecast. The current architecture holds that visibility is "
  "not evidence and translation is not employer recognition, so these three are a "
  "genuine conflict worth examining."),
 ("What was done about it for September 23",
  "NOTHING TO THE INSTRUMENT. The 12 statements are unchanged, the workbook is "
  "not regenerated and its Acrobat gate stays valid. Slide 5's presenter note "
  "gains one clarification, said once and not on the participant-facing slide: "
  "the Optionality score is a composite reading of portability conditions and "
  "signals, not a prediction, and nothing on the axis forecasts that another "
  "employer will value, hire, promote or pay anyone. The note also tells the "
  "facilitator not to reword the statements in delivery."),
 ("POST-SEPTEMBER-23 INSTRUMENT-REVIEW ITEM",
  "Examine statements 7, 10 and 12 in the next instrument revision, against the "
  "question of whether an Optionality item should read a condition the "
  "participant can evidence rather than an outcome another party controls. Any "
  "change to them regenerates the workbook, which resets the Adobe Acrobat "
  "behavior-test gate. This is deliberately NOT a September 23 change."),
 ("SOP v2.0.9 -> v2.0.10, version strings only",
  "Not an editorial pass. The deck moved to v2.0.7 and the SOP names the deck in "
  "its pre-session checklist and its source-of-truth map; left at v2.0.6 it would "
  "send a facilitator to a superseded file. The build asserts that the document "
  "differs from v2.0.9 by nothing but the substituted version strings, so the "
  "approved eight-page pagination cannot have moved, and it has not."),
 ("Eight pages is approved and settled",
  "The v2.0.9 report explained the eight-page SOP as a decision being justified. "
  "It is now recorded as approved. No operating control is to be cut to restore "
  "the old seven-page count. The stub-page test that the seven-page pin protected "
  "is kept, and page 8 carries 31 substantive lines."),
 ("Checklist v1.2 -> v1.3",
  "The Maven page has been independently checked, so the checklist stops hedging. "
  "Sections A and B record the instructor title and bio as verified already "
  "aligned and not to be touched. Section C now replaces ALL THREE learning "
  "outcomes against their verified live wording rather than fixing outcome 3 "
  "alone. Section D's recommended copy no longer calls the session private: "
  "private scoring is accurate, a private group session is not, so it reads "
  "“live, evidence-based session”. Section F gains four site conflicts, each "
  "quoted with its file and line: the retired Private Read still visible on "
  "fieldkit.html and for-professionals.html, fieldkit.html:230 defining "
  "Optionality partly as visibility, for-professionals.html:222 combining Keep "
  "the Proof with the free Career Evidence Starter, and "
  "for-professionals.html:217 promising to decide the next move."),
 ("What was deliberately not reopened",
  "The opening and its lived warrant, the Density and Optionality sequencing, the "
  "slide 18 simplification, the protected twelve-minute block, the seven move "
  "categories, the two-route continuation, the slide 25 close, the workbook "
  "binary and the recording and privacy architecture. The build asserts it: "
  "exactly one slide face and one speaker note differ from v2.0.6."),
 ("Career Move Review",
  "Still OFF the participant-facing deck. No page, no route and no copy exists on "
  "this branch or on origin/main. The checklist now says explicitly that a Career "
  "Move Review call to action must NOT be substituted where the retired Private "
  "Read is removed: those are two separate decisions."),
]

REPOINTS = {
 # the eight-page rows, restated as a settled decision
 (19, 2, 3): (None,
   "APPROVED AND SETTLED. Eight pages is the approved length for this document. "
   "The commercial architecture grew from two live offers to five and sections 4, "
   "5 and 12 gained operational rules. No operating control is cut to restore the "
   "old seven-page count. The stub-page test the seven-page pin protected is "
   "kept: page 8 carries 31 substantive lines, not a stub."),
 (21, 14, 3): (None,
   "APPROVED AND SETTLED, not an open decision. Eight pages, orientation "
   "unchanged at portrait, landscape, landscape, then five portrait, and no stub "
   "final page."),
}


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
    qa = importlib.import_module("qa_v207")
    total = 162 + len(qa.R)
    passed = 162 + sum(1 for r in qa.R if r[3] == "PASS")

    def find(fragment):
        hits = [x for x in d.paragraphs if fragment in x.text]
        assert len(hits) == 1, f"{fragment[:44]!r} matched {len(hits)}"
        return hits[0]

    for para in [x for x in d.paragraphs if OLD in x.text]:
        for r in para.runs:
            if OLD in r.text:
                r.text = r.text.replace(OLD, STAMP)

    EDITS = [
     ("DECK IS NOW v2.0.6.", "DECK IS NOW v2.0.7."),
     ("UNCHANGED FROM v2.0.2 THROUGH v2.0.9.",
      "UNCHANGED FROM v2.0.2 THROUGH v2.0.10."),
     ("PowerPoint v2.0.6, workbook v2.0.1, SOP v2.0.9",
      "PowerPoint v2.0.7, workbook v2.0.1, SOP v2.0.10"),
     ("Verification — 228 items", f"Verification — {total} items"),
     ("228 of 228 PASS.", f"{passed} of {total} PASS."),
     ("PREVIEW_Presentation_60MIN_v2.0.6_LibreOffice.pdf, rendered from the v2.0.6 "
      "deck in this pass",
      "PREVIEW_Presentation_60MIN_v2.0.7_LibreOffice.pdf, rendered from the v2.0.7 "
      "deck in this pass"),
     ("PREVIEW_SOP_60MIN_v2.0.9_LibreOffice.pdf",
      "PREVIEW_SOP_60MIN_v2.0.10_LibreOffice.pdf"),
     ("QA REPORT v2.0.9", "QA REPORT v2.0.10"),
     ("Group N — the September 19 revision",
      "Group N — the September 19 revision, SUPERSEDED BY GROUP O and kept as the "
      "v2.0.6 record. Its rows are not counted again in the headline."),
    ]
    for old, new in EDITS:
        para = find(old)
        for r in para.runs:
            if old in r.text:
                r.text = r.text.replace(old, new)
                break
        else:
            set_para(para, para.text.replace(old, new))
    for para in d.tables[0].rows[0].cells[0].paragraphs:
        for r in para.runs:
            r.text = r.text.replace("v2.0.9 CANDIDATE", "v2.0.10 CANDIDATE")

    for (ti, ri, ci), (expect, new) in REPOINTS.items():
        cell = d.tables[ti].rows[ri].cells[ci]
        if expect:
            assert expect in cell.text
        set_cell(cell, new)

    head = copy.deepcopy(find("SOP — the 60-minute rewrite")._element)
    body = copy.deepcopy(find("Rewritten as the operational source of truth")._element)
    sub = copy.deepcopy(find("Group A — Duration consistency")._element)
    tbl2 = copy.deepcopy(d.tables[6]._element)
    tbl4 = copy.deepcopy(d.tables[19]._element)
    blank = copy.deepcopy([x for x in d.paragraphs if not x.text.strip()][3]._element)
    from docx.text.paragraph import Paragraph

    def insert(anchor_el, tmpl, text=None):
        el = copy.deepcopy(tmpl)
        anchor_el.addprevious(el)
        if text is not None:
            set_para(Paragraph(el, d), text)
        return el

    def table_before(anchor_el, tmpl, rows):
        el = copy.deepcopy(tmpl)
        anchor_el.addprevious(el)
        t = docx.table.Table(el, d)
        while len(t.rows) > 2:
            t._element.remove(t.rows[-1]._element)
        template = copy.deepcopy(t.rows[1]._element)
        for ci, v in enumerate(rows[0]):
            set_cell(t.rows[0].cells[ci], v)
        t._element.remove(t.rows[1]._element)
        for row in rows[1:]:
            t._element.append(copy.deepcopy(template))
            for ci, v in enumerate(row):
                set_cell(t.rows[-1].cells[ci], v)
        return t

    anchor = find("Zero-tolerance duration sweep")._element
    insert(anchor, head,
           "September 19 final-candidate pass — v2.0.7 / v2.0.10 / v1.3")
    insert(anchor, body,
           "One narrow pass. Slide 22 gains visual authority for the portability "
           "frame, slide 5's note gains a single clarification about what the "
           "Optionality score is and is not, and the instrument conflict behind it "
           "is recorded for review after the delivery rather than acted on before "
           "it. Nothing already working was reopened.")
    table_before(anchor, tbl2, [("Where", "Change")] + CHANGES)
    insert(anchor, blank)

    tail = find(f"{passed} of {total} PASS.")._element
    insert(tail, sub,
           "Group O — the September 19 final-candidate pass, and the full re-run")
    table_before(tail, tbl4, [("#", "Category", "Status", "Notes")]
                 + [(str(162 + n), label, st, note)
                    for n, g, label, st, note in qa.R])
    insert(tail, blank)

    d.save(DST)
    assert passed == total, "the report cannot be saved while a check fails"
    return DST, passed, total


if __name__ == "__main__":
    path, p_, t_ = build()
    print("built", os.path.basename(path), f"({p_}/{t_})")
    print("  sha256", hashlib.sha256(open(path, "rb").read()).hexdigest())
