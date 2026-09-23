# -*- coding: utf-8 -*-
"""One-page facilitator run sheet for September 23, 2026.

Timings, slide numbers and workbook pages only, sized to print on US Letter and
read at arm's length on a second screen. It is a companion to the deck's own
speaker notes, not a replacement for them: every time and page below is read
from the delivered presenting copy's notes, not from memory.

Built with PyMuPDF because it gives exact control of a single dense page.
Helvetica is used throughout since it is a PDF base font and needs no embedding,
so the sheet prints identically anywhere.
"""
import hashlib, os
import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
DST = os.path.join(HERE, "RUN_SHEET_Sept23_2026_60MIN_onepage.pdf")

NAVY = (0x0F / 255, 0x23 / 255, 0x47 / 255)
GOLD = (0xC9 / 255, 0xA8 / 255, 0x4C / 255)
PANEL = (0xE9 / 255, 0xED / 255, 0xF3 / 255)
MUTED = (0x5A / 255, 0x6B / 255, 0x84 / 255)
WHITE = (1, 1, 1)
RUST = (0xC1 / 255, 0x44 / 255, 0x0E / 255)

PAGE_W, PAGE_H = 612, 792          # US Letter portrait
M = 30                             # side margin
W = PAGE_W - 2 * M

COL_MIN, COL_NO, COL_WB = 58, 16, 30
COL_WHAT = W - COL_MIN - COL_NO - COL_WB - 18

BODY = 8.0
LEAD = 9.6

RULES = [
    "The twelve minutes at 19:00 are not yours to spend. Take time back on slides 20 and 21, never here.",
    "Never ask who is in which square. Their score stays theirs.",
    "Stop the recording before Q&A. Not pause. Confirm on screen, then say so aloud.",
    "No square is a goal. Compounding is a fact about the grid, not a destination.",
]

# (part heading) or (slide no, minutes, what, workbook page)
ROWS = [
    ("PART 1   SET UP",),
    (1, "0:00-0:30", "START THE RECORDING. Welcome, name the session, the method, the length. Bio is two sentences.", ""),
    (2, "0:30-1:20", "Reframe for fifteen seconds, then the audit into cybersecurity story. The story earns the method.", ""),
    (3, "1:20-2:00", "Recording and privacy disclosure. Say it once, do not expand it. Workbook is open from the start.", "1"),
    (4, "2:00-3:30", "DENSITY. Is the work still building you? Ordinary language first, then the word.", ""),
    (5, "3:30-5:00", "OPTIONALITY. Will what you build still travel? Ordinary language first, then the word.", ""),

    ("PART 2   FIRST READ, FROM MEMORY",),
    (6, "5:00-6:40", "Statements 1 to 3. Read each once, then stay silent. Do not fill the silence.", "2"),
    (7, "6:40-8:10", "Statements 4 to 6.", "2"),
    (8, "8:10-8:40", "Density total.", "2"),
    (9, "8:40-10:10", "Statements 7 to 9.", "3"),
    (10, "10:10-11:40", "Statements 10 to 12.", "3"),
    (11, "11:40-12:00", "Optionality total.", "3"),
    (12, "12:00-13:00", "The four states. Name each square once. No state costs here, no asking who is where. "
                        "Say: Fragile is not worst, Stagnant is where neither axis is moving. Screen only, not page 7.", ""),
    (13, "13:00-14:00", "First placement. Cross the two totals, tick one square. Privately, and provisionally.", "3"),

    ("PART 3   TEACH THE EVIDENCE RULE",),
    (14, "14:00-16:00", "The evidence protocol. The rule that turns a feeling into a reading.", "4"),
    (15, "16:00-19:00", "Three ways a self-score goes wrong. This is what makes the second read honest.", "4"),

    ("PART 4   SECOND READ, AGAINST EVIDENCE",),
    (16, "19:00-31:00", "RESCORE ALL TWELVE, WITH AN EVIDENCE LINE. PROTECTED AND NON-NEGOTIABLE. Do not shorten this.", "5-6"),
    (17, "31:00-32:30", "Re-total both axes.", "5-6"),
    (18, "32:30-34:00", "When the evidence is still uncertain. Sensitivity check. A boundary reading is a legitimate result.", "7"),
    (19, "34:00-35:00", "Corrected placement and confidence. They compare it with the tick they made on page 3.", "7"),

    ("PART 5   SO WHAT",),
    (20, "35:00-38:00", "What each state costs. Stagnant, Depth Trap, Fragile, Compounding. Forty-five seconds each, "
                        "then move. Do not go deeper on whichever square the room seems to be sitting in.", ""),
    (21, "38:00-41:00", "Seven categories of move. Directions, not plans. About twenty-five seconds each.", "8"),
    (22, "41:00-45:00", "THE NEXT-MOVE NOTE. Four minutes of real writing. Protect it like the twelve.", "8"),

    ("PART 6   CLOSE",),
    (23, "45:00-46:00", "Two routes to continue the read. Sixty seconds, no pressure.", ""),
    (24, "46:00-47:00", "The session against the Field Kit. Say it as a difference, not a pitch.", ""),
    (25, "47:00-48:00", "The close. Then hold 48:00 to 50:00 as buffer. LAST RECORDED SLIDE.", ""),

    ("Q&A   LIVE ONLY, NEVER DISTRIBUTED",),
    (26, "50:00-60:00", "STOP THE RECORDING. Confirm on screen, say so aloud, then take the first question. "
                        "Clarify method, evidence rule, boundary readings, move categories. HARD STOP AT 60:00.", ""),
]

WB_MAP = ("WORKBOOK RUNS FRONT TO BACK AND NEVER JUMPS BACK.    "
          "p1 at 1:20    p2 at 5:00    p3 at 8:40    p4 at 14:00    "
          "p5-6 at 19:00    p7 at 32:30    p8 at 38:00")


def wrap(text, font, size, width):
    """Greedy wrap, returning the lines that fit the given width."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if pymupdf.get_text_length(trial, fontname=font, fontsize=size) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def build():
    doc = pymupdf.open()
    pg = doc.new_page(width=PAGE_W, height=PAGE_H)
    y = M

    # ---- title band ----------------------------------------------------
    pg.draw_rect(pymupdf.Rect(M, y, M + W, y + 40), color=None, fill=NAVY)
    pg.insert_text((M + 12, y + 18), "STAY OR LEAVE?   60-MINUTE RUN SHEET",
                   fontname="hebo", fontsize=13, color=WHITE)
    pg.insert_text((M + 12, y + 31),
                   "Wednesday, September 23, 2026   .   6:00 PM CT   .   "
                   "Live Career Growth Assessment   .   Temidayo Afonja",
                   fontname="helv", fontsize=7.5, color=GOLD)
    y += 48

    # ---- rules -----------------------------------------------------------
    pg.insert_text((M, y), "FOUR RULES THAT NEVER BEND",
                   fontname="hebo", fontsize=7.5, color=RUST)
    y += 10
    for r in RULES:
        pg.draw_rect(pymupdf.Rect(M, y - 5.5, M + 2.2, y + 2), color=None, fill=GOLD)
        pg.insert_text((M + 8, y), r, fontname="helv", fontsize=8, color=NAVY)
        y += 11
    y += 8

    # ---- table header -----------------------------------------------------
    pg.draw_rect(pymupdf.Rect(M, y, M + W, y + 14), color=None, fill=NAVY)
    x = M + 6
    for label, w in (("MINUTES", COL_MIN), ("#", COL_NO)):
        pg.insert_text((x, y + 10), label, fontname="hebo", fontsize=7, color=WHITE)
        x += w + 6
    pg.insert_text((x, y + 10), "ON SCREEN, AND WHAT YOU DO",
                   fontname="hebo", fontsize=7, color=WHITE)
    pg.insert_text((M + W - COL_WB - 2, y + 10), "WB",
                   fontname="hebo", fontsize=7, color=GOLD)
    y += 14

    # ---- rows --------------------------------------------------------------
    shade = False
    for row in ROWS:
        if len(row) == 1:
            y += 3
            pg.insert_text((M + 6, y + 7.5), row[0],
                           fontname="hebo", fontsize=7.2, color=RUST)
            pg.draw_line(pymupdf.Point(M + 6 + pymupdf.get_text_length(
                row[0], fontname="hebo", fontsize=7.2) + 8, y + 5),
                pymupdf.Point(M + W, y + 5), color=GOLD, width=0.6)
            y += 11
            shade = False
            continue

        no, mins, what, wb = row
        lines = wrap(what, "helv", BODY, COL_WHAT)
        h = max(15, len(lines) * LEAD + 5)
        if shade:
            pg.draw_rect(pymupdf.Rect(M, y, M + W, y + h), color=None, fill=PANEL)
        shade = not shade

        pg.insert_text((M + 6, y + 10), mins, fontname="hebo", fontsize=8, color=NAVY)
        pg.insert_text((M + 6 + COL_MIN + 6, y + 10), str(no),
                       fontname="hebo", fontsize=8, color=MUTED)
        tx = M + 6 + COL_MIN + 6 + COL_NO + 6
        for i, ln in enumerate(lines):
            pg.insert_text((tx, y + 10 + i * LEAD), ln,
                           fontname="helv", fontsize=BODY, color=NAVY)
        if wb:
            pg.insert_text((M + W - COL_WB - 2, y + 10), wb,
                           fontname="hebo", fontsize=8, color=RUST)
        y += h

    # ---- footer band --------------------------------------------------------
    y += 8
    assert y + 34 <= PAGE_H - 20, f"run sheet overflows one page: y={y:.1f}"
    pg.draw_rect(pymupdf.Rect(M, y, M + W, y + 30), color=None, fill=PANEL)
    pg.insert_text((M + 8, y + 12), WB_MAP, fontname="hebo", fontsize=7, color=NAVY)
    pg.insert_text((M + 8, y + 24),
                   "Say the page number out loud BEFORE you start talking, not after. "
                   "People who are writing are not listening.",
                   fontname="helv", fontsize=7.5, color=MUTED)

    doc.save(DST, deflate=True)
    doc.close()

    out = pymupdf.open(DST)
    assert out.page_count == 1, f"run sheet is {out.page_count} pages"
    print("built", os.path.basename(DST))
    print("  pages", out.page_count, " last row ended at y =", round(y, 1))
    print("  sha256", hashlib.sha256(open(DST, "rb").read()).hexdigest())
    return DST


if __name__ == "__main__":
    build()
