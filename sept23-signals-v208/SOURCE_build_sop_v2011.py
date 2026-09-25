# -*- coding: utf-8 -*-
"""Free Flagship SOP, v2.0.10 -> v2.0.11 CANDIDATE.

The SOP is re-cut to deck v2.0.9's timeline. Nothing editorial is reopened: this
pass changes times, slide numbers, workbook pages and the prose that cites them,
plus the version and revision stamps, plus the em dashes.

What moved, and why:

  - The Signals Worth Watching section takes three minutes, so calibration, the
    re-total and the sensitivity check each give some back and the close buffer
    gives the last minute. The twelve-minute rescore is SHIFTED, never shortened.
  - The welcome slide now holds a real window instead of overlapping four slides,
    so the opening five minutes are re-cut around it.
  - The deck's printed slide numbers changed, because the welcome slide had been
    inserted without renumbering and the Signals section added three more. Every
    slide reference in this SOP uses the new printed numbers.
  - The poll slide left the timed core for the appendix, so it is no longer in
    the run of show.

Em dashes are swept out of the whole document, including ones that predate this
change, because the standing check is no em dash anywhere.
"""
import copy, hashlib, os, re, shutil
import docx

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(
    "sept23-v208-assets",
    "Capability_Formation_Free_Flagship_SOP_Sept23_2026_60MIN_v2.0.10_CANDIDATE.docx")
DST = os.path.join(
    HERE,
    "Capability_Formation_Free_Flagship_SOP_Sept23_2026_60MIN_v2.0.11_CANDIDATE.docx")

EM = "—"
OLD_STAMP = "Saturday, September 19, 2026 at 11:20 AM CT"
NEW_STAMP = "Friday, September 25, 2026 at 9:10 AM CT"

HEAD = ["Time", "Block", "Slides", "WB", "Facilitator action",
        "Participant action", "Recording"]

# The run of show, re-cut. Slide numbers are the deck's printed numbers.
RUN_A = [
 ("0:00–1:00", "Welcome, why this lesson, and the question", "1–2", "—",
  "Start the recording on slide 1. Name the session, the method and the "
  "duration. Biography is two sentences. Advance at 1:00.",
  "Listen. Nothing written yet.", "RECORDING ON. Start on slide 1"),
 ("1:00–1:50", "The reframe and the lived warrant", "3", "—",
  "Fifteen seconds on the reframe, then the audit into cybersecurity story. "
  "Recognition before terminology.",
  "Listen.", "RECORDING ON"),
 ("1:50–2:30", "Boundary, recording and privacy disclosure", "4", "1",
  "Deliver the disclosure once and do not expand it. Name the boundary. Point "
  "at the workbook. Forty seconds.",
  "Open the workbook at page 1.", "RECORDING ON"),
 ("2:30–5:00", "Density and Optionality", "5–6", "—",
  "Define each axis in ordinary language first, then name it. Seventy-five "
  "seconds each.",
  "Listen. Nothing written yet.", "RECORDING ON"),
 ("5:00–12:00", "Initial read of all 12 statements and totals", "7–12", "2–3",
  "Read each statement once, then stay silent. Do not fill the silence.",
  "Score 1 to 12 privately. Add both totals. No evidence line yet.",
  "RECORDING ON"),
 ("12:00–14:00", "The four states and a first provisional position", "13–14", "3",
  "Name each square once. The squares are numbered 1 to 4 by how much is "
  "accruing. Say the 17 to 21 boundary rule. Do not ask who is where.",
  "Cross the two totals. Mark a square or a boundary. Hold it lightly.",
  "RECORDING ON"),
 ("14:00–16:00", "The evidence protocol", "15", "4",
  "Teach the protocol. It is symmetric: low scores need evidence too.",
  "Follow along.", "RECORDING ON"),
 ("16:00–18:00", "Three ways a self-score goes wrong", "16", "4",
  "All three misreadings, forty seconds each. No questions here.",
  "Run the three checks against their own scoring.", "RECORDING ON"),
 ("18:00–30:00", "Evidence-backed rescore of all 12 statements. PROTECTED",
  "17", "5–6",
  "Hold this slide and stay silent. Midpoint cue at about 24:00. Two-minute "
  "warning at 28:00, thirty-second warning at 29:30.",
  "Rescore all twelve with a short evidence phrase for each.", "RECORDING ON"),
 ("30:00–33:00", "Corrected totals, sensitivity and corrected position",
  "18–20", "5–7",
  "Insist on the re-total. Run the sensitivity check. A boundary reading is a "
  "legitimate result.",
  "Re-total both axes. Run sensitivity if 1 to 2 items are marked. Place again "
  "and rate confidence.", "RECORDING ON"),
]
RUN_B = [
 ("33:00–36:00", "Four states and their immediate costs", "21", "—",
  "The block climbs: Stagnant, Depth Trap, Fragile, Compounding. Forty-five "
  "seconds per state. Do not deepen one for the room.",
  "Listen. Read their own square's cost.", "RECORDING ON"),
 ("36:00–39:00", "Signals Worth Watching", "22–24", "—",
  "Sixty seconds per slide. Frame, then the role signals, then the signals "
  "when things feel fine. Questions to investigate, never predictions.",
  "Listen. Choose two signals to watch.", "RECORDING ON"),
 ("39:00–42:00", "Seven categories of move", "25", "8",
  "Read each category and its one-line reading. About twenty-five seconds "
  "each. Direction, not a plan.",
  "Identify the category their evidence supports testing.", "RECORDING ON"),
 ("42:00–46:00", "Complete the Next-Move Note", "26", "8",
  "Read the four portability questions once, read the prompts once, then stop "
  "talking. Sixty-second warning at 45:00.",
  "Write the three lines and name two signals to watch.", "RECORDING ON"),
 ("46:00–48:00", "Continuation routes and the Field Kit", "27–28", "8",
  "Two routes, sixty seconds each, no pressure. This is the first place to "
  "take time from if you are behind.",
  "Choose a route, or none.", "RECORDING ON"),
 ("48:00–50:00", "Evergreen close, buffer and recording stop",
  "close slide", "8",
  "Deliver the close 48:00–49:00. Hold the slide 49:00–50:00 as buffer. At "
  "50:00 STOP the recording and verify on screen.",
  "Finish writing. Set a rescore date.", "RECORDING ON, STOPS AT 50:00"),
 ("50:00–60:00", "Live-only Q&A, never recorded", "Q&A slide", "—",
  "Confirm aloud that recording has stopped. Method questions only. Hard stop "
  "at 60:00.",
  "Ask method questions. No scores, states or employers.", "RECORDING OFF"),
]

PROSE = [
 ("The 19:00–31:00 evidence-backed rescore is PROTECTED",
  "The 18:00–30:00 evidence-backed rescore is PROTECTED"),
 ("Recover from 45:00–48:00 first, then the 48:00–50:00 b",
  "Recover from 46:00–48:00 first, then the 49:00–50:00 b"),
 ("it sits on slide 3 at minute 1:20", "it sits on slide 4 at minute 1:50"),
 ("without shortening the 19:00–31:00 rescore",
  "without shortening the 18:00–30:00 rescore"),
 ("cut from 45:00–48:00 first, then the buffer, then compress the four-states "
  "block", "cut from 46:00–48:00 first, then the buffer, then compress the "
  "four-states block"),
]


def carrier(para):
    runs = para.runs
    return next((r for r in runs if r.text.strip()), runs[0]) if runs else None


def set_para(para, text):
    keep = carrier(para)
    assert keep is not None, "cannot write into an empty paragraph"
    keep.text = text
    for r in para.runs:
        if r._r is not keep._r:
            r._r.getparent().remove(r._r)


def set_cell(cell, text):
    p = cell.paragraphs[0]
    for extra in cell.paragraphs[1:]:
        extra._element.getparent().remove(extra._element)
    set_para(p, text)


def fill(table, head, rows):
    template = copy.deepcopy(table.rows[1]._element)
    while len(table.rows) > 1:
        table._element.remove(table.rows[-1]._element)
    for ci, v in enumerate(head):
        set_cell(table.rows[0].cells[ci], v)
    for row in rows:
        table._element.append(copy.deepcopy(template))
        for ci, v in enumerate(row):
            set_cell(table.rows[-1].cells[ci], v)


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


def build():
    shutil.copyfile(SRC, DST)
    d = docx.Document(DST)
    before_em = count_em(d)

    # 1. the run of show
    assert [c.text for c in d.tables[2].rows[0].cells] == HEAD, "table 2 header"
    assert [c.text for c in d.tables[3].rows[0].cells] == HEAD, "table 3 header"
    fill(d.tables[2], HEAD, RUN_A)
    fill(d.tables[3], HEAD, RUN_B)

    # 2. the prose that cites times and slides
    hits = {old: 0 for old, _ in PROSE}
    for r in every_run(d):
        t = r.text
        for old, new in PROSE:
            if old in t:
                hits[old] += t.count(old)
                t = t.replace(old, new)
        if t != r.text:
            r.text = t
    for old, n in hits.items():
        assert n >= 1, f"prose not found: {old[:50]!r}"

    # 3. version and revision stamps
    for r in every_run(d):
        t = r.text.replace("v2.0.10", "v2.0.11").replace(OLD_STAMP, NEW_STAMP)
        if t != r.text:
            r.text = t

    # 4. em dashes, including ones that predate this change
    for r in every_run(d):
        if EM in r.text:
            t = re.sub(r"\s*" + EM + r"\s*", ". ", r.text)
            t = re.sub(r"\.\s*\.", ".", t)
            r.text = t

    d.save(DST)

    out = docx.Document(DST)
    assert count_em(out) == 0, f"{count_em(out)} em dashes left in the SOP"
    body = ("\n".join(p.text for p in out.paragraphs) + "\n"
            + "\n".join(c.text for t in out.tables for row in t.rows
                        for c in row.cells))
    for stale in ("19:00–31:00", "35:00–38:00", "38:00–41:00", "41:00–45:00",
                  "45:00–48:00", "v2.0.10", OLD_STAMP):
        assert stale not in body, f"stale reference survived: {stale}"
    for fresh in ("18:00–30:00", "36:00–39:00", "Signals Worth Watching",
                  "v2.0.11", NEW_STAMP):
        assert fresh in body, f"missing: {fresh}"
    times = [r[0] for r in RUN_A + RUN_B]
    for a, b in zip(times, times[1:]):
        assert a.split("–")[1] == b.split("–")[0], f"run of show gap: {a} {b}"
    assert times[0].startswith("0:00") and times[-1].endswith("60:00")

    print("built", os.path.basename(DST))
    print(f"  run of show rows: {len(RUN_A)} + {len(RUN_B)}")
    print(f"  em dashes: {before_em} -> {count_em(out)}")
    print("  sha256", hashlib.sha256(open(DST, "rb").read()).hexdigest())
    return DST


if __name__ == "__main__":
    build()
