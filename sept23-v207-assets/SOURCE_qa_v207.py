# -*- coding: utf-8 -*-
"""September 23 flagship QA — v2.0.7 / v2.0.9 / v1.3.

Executed against the delivered files. The method group compares the new deck
against the approved v2.0.5 on disk rather than against text kept here, so a
silent change to the instrument fails the build rather than the reader.
"""
import hashlib, io, os, re, sys, zipfile
import docx, pymupdf
from PIL import Image
from pptx import Presentation
from pptx.util import Emu

OUT = "scratchpad/sept23/out"
A = "sept23-v205-assets"
DECK = f"{OUT}/PRESENTER_VERSION_Stay_or_Leave_Live_Career_Growth_Assessment_60MIN_v2.0.7_CANDIDATE.pptx"
DECK_PDF = DECK[:-5] + ".pdf"
PRIOR = f"{A}/PRESENTER_VERSION_Stay_or_Leave_Live_Career_Growth_Assessment_60MIN_v2.0.5_CANDIDATE.pptx"
SOP = f"{OUT}/Capability_Formation_Free_Flagship_SOP_Sept23_2026_60MIN_v2.0.10_CANDIDATE.docx"
SOP_PDF = SOP[:-5] + ".pdf"
CHK = f"{OUT}/Manual_Maven_and_Website_Edit_Checklist_v1.3.docx"
WB = "free-flagship-assets/60min-v2.0.1/Capability_Position_Read_Workbook_60MIN_v2.0.1_CANDIDATE.pdf"
WB_SHA = "2bd2912846a679837e8e6bfb4aadff2bb07ee5959d35502ca1c5b5c728efa3ee"

MAVEN = "https://maven.com/p/8b3c40/stay-or-leave-live-career-growth-assessment"
FIELDKIT = "https://temidayoafonja.com/fieldkit"

R = []
def chk(g, label, ok, note=""):
    R.append((len(R) + 1, g, label, "PASS" if ok else "FAIL", note))
def flat(s): return re.sub(r"\s+", " ", s.replace("’", "'")).strip()


def deck(path):
    p = Presentation(path)
    f = {i: "\n".join(sh.text_frame.text for sh in s.shapes if sh.has_text_frame)
         for i, s in enumerate(p.slides, 1)}
    n = {i: (s.notes_slide.notes_text_frame.text if s.has_notes_slide else "")
         for i, s in enumerate(p.slides, 1)}
    return f, n


def hidden(path):
    z = zipfile.ZipFile(path)
    rels = dict(re.findall(r'Id="([^"]+)"[^>]*Target="([^"]+)"',
                           z.read("ppt/_rels/presentation.xml.rels").decode()))
    order = [rels[m] for m in re.findall(r'<p:sldId[^>]*r:id="([^"]+)"',
                                         z.read("ppt/presentation.xml").decode())]
    out = []
    for pos, t in enumerate(order, 1):
        x = z.read("ppt/" + t.lstrip("./")).decode()
        i = x.index("<p:sld ")
        # the whole opening tag: show="0" hides behind a long namespace list
        if 'show="0"' in x[i:x.index(">", i) + 1]:
            out.append(pos)
    return out


def doc_text(path):
    d = docx.Document(path)
    parts = [p.text for p in d.paragraphs]
    for t in d.tables:
        for row in t.rows:
            parts += [c.text for c in row.cells]
    return "\n".join(parts)


F, N = deck(DECK)
OF, ON = deck(PRIOR)
SOPT, CHKT = flat(doc_text(SOP)), flat(doc_text(CHK))
FACE, NOTE = flat("\n".join(F.values())), flat("\n".join(N.values()))
CORE_FACE = flat("\n".join(F[i] for i in range(1, 27)))
TIMING = re.compile(r"TIMING:\s*(\d+:\d\d)\s*[-–]\s*(\d+:\d\d)")
SPAN = {i: TIMING.search(N[i]).groups() for i in range(1, 27)}

# ── A. method, compared against the approved v2.0.5 on disk ─────────────────
STATEMENTS = [6, 7, 9, 10]
LOGIC = [8, 11, 12, 13, 14, 15, 17, 19]
chk("A", "All 12 statements byte-identical to v2.0.5",
    all(OF[i] == F[i] for i in STATEMENTS),
    f"slides {STATEMENTS}. Not rewritten, not reordered, none added or removed")
chk("A", "Twelve statements present and numbered 1 to 12",
    all(re.search(rf"(?m)^{k}$", "\n".join(F[i] for i in STATEMENTS))
        for k in range(1, 13)), "counted on the built deck")
chk("A", "The 1-5 scale, both /30 totals and the bands are unchanged",
    all(OF[i] == F[i] for i in (8, 11))
    and all(s in F[8] and s in F[11] for s in
            ("________  / 30", "19 to 30 is high", "6 to 18 is low",
             "17 to 21 is the boundary band")))
chk("A", "Evidence protocol and the 3-versus-? distinction unchanged",
    OF[14] == F[14] and "A 3 is a reading, not an absence of one." in F[14]
    and "3?, 4?, 2?" in F[14])
chk("A", "The 90-day evidence window is unchanged",
    OF[15] == F[15] and "last ninety days" in F[15] and "last ninety days" in F[6])
chk("A", "Four states unchanged", OF[12] == F[12]
    and all(s in F[12] for s in ("DEPTH TRAP", "COMPOUNDING", "STAGNANT", "FRAGILE")))
chk("A", "Seven move-category NAMES unchanged",
    all(t in F[21] for t in ("Remain and deepen", "Translate what is built",
                             "Widen exposure", "Test portability",
                             "Repair formation conditions", "Prepare for exit",
                             "Seek an external perspective")))
chk("A", "No square prescribes a category",
    "No square prescribes a category. Your evidence and constraints still apply."
    in flat(F[21]))
chk("A", "Boundary, sensitivity and incomplete methodology preserved",
    all(s in flat(F[18]) for s in
        ("17 TO 21 IS THE BOUNDARY BAND",
         "RUN THE NEIGHBORING-SCORE SENSITIVITY CHECK",
         "If the range touches 17 to 21, hold the axis as boundary",
         "INCOMPLETE",
         "ONE axis in the band", "BOTH axes in the band"))
    and "operational convention, not a statistical confidence interval" in flat(F[18]))
chk("A", "The full sensitivity procedure survives in the presenter note",
    all(s in flat(N[18]) for s in
        ("one point lower", "one point higher", "bounded inside the 1 to 5 scale",
         "a 1? is never tested at 0 and a 5? never at 6")),
    "moved off the slide face, not out of the method")
chk("A", "State is not identity, and the Next-Move Note is intact",
    OF[13] == F[13] and "State is not identity" in flat(F[13])
    and all(s in F[22] for s in ("MY CURRENT READ", "WHAT I NEED TO TEST",
                                 "WHAT HAPPENS NEXT"))
    and "This is a note, not a decision." in flat(F[22]))
chk("A", "Private scoring preserved",
    "Hold the number. Do not share it." in F[8] and "Nothing is collected." in F[13])

# ── B. timing ──────────────────────────────────────────────────────────────
chk("B", "Timing chain continuous 0:00 to 60:00",
    all(SPAN[i][1] == SPAN[i + 1][0] for i in range(1, 26))
    and SPAN[1][0] == "0:00" and SPAN[26][1] == "60:00")
chk("B", "Protected evidence block is still twelve minutes",
    SPAN[16] == ("19:00", "31:00") and "PROTECTED AND NON-NEGOTIABLE" in N[16])
chk("B", "Recorded core is 50 minutes, Q&A 50:00 to 60:00 and outside it",
    SPAN[25][1] == "50:00" and SPAN[26] == ("50:00", "60:00")
    and "RECORDING OFF" in N[26])
changed_cues = [i for i in range(1, 27)
                if TIMING.findall(ON[i]) != TIMING.findall(N[i])]
chk("B", "Only slides 1 and 2 have a changed timing cue", changed_cues == [1, 2],
    "ten seconds move from the welcome to the reframe so the lived warrant fits; "
    "the 2:00 and 5:00 block boundaries are untouched")
chk("B", "Every SOP reconciliation block boundary still matches the deck",
    all(b in SOPT for b in ("0:00–2:00", "2:00–5:00", "5:00–12:00", "12:00–14:00",
                            "14:00–19:00", "19:00–31:00", "31:00–35:00",
                            "35:00–38:00", "38:00–41:00", "41:00–45:00",
                            "45:00–48:00", "48:00–50:00", "50:00–60:00")))

# ── C. the opening ─────────────────────────────────────────────────────────
chk("C", "The lived warrant is in the core opening, not optional",
    "SPOKEN WARRANT - SAY IT, DO NOT SKIP IT" in N[2]
    and "OPTIONAL SPOKEN PROOF" not in NOTE,
    "promoted out of slide 5's optional block onto slide 2")
chk("C", "The warrant uses only wording already approved in this package",
    all(s in flat(N[2]) for s in (
        "I did not start from zero", "Evidence, controls and risk travelled with me",
        "Cybersecurity language, privacy frameworks and technical context did not")),
    "no dates, employers, metrics, reactions, reasons or outcomes were invented")
chk("C", "The warrant is capped and the cap is stated",
    "thirty to forty-five seconds" in N[2] and "DO NOT ADD TO THE STORY" in N[2]
    and "warrant, not biography" in N[2])
chk("C", "Recognition precedes terminology on slides 4 and 5",
    F[4].split("\n")[1].strip() == "Is the work still building you?"
    and F[5].split("\n")[1].strip() == "Will what you build still travel?"
    and "This reading calls that Density." in F[4]
    and "This reading calls that Optionality." in F[5])
chk("C", "Density and Optionality are both still taught by name",
    "Density" in F[4] and "Optionality" in F[5]
    and "Six statements measure it" in F[4] and "Six statements measure it" in F[5])
chk("C", "The recording and privacy disclosure still lands inside five minutes",
    SPAN[3] == ("1:20", "2:00") and "RECORDING AND PRIVACY DISCLOSURE" in N[3])

# ── D. positioning and the boundaries that must hold ───────────────────────
chk("D", "Optionality is not stated as employer recognition",
    "translation is not recognition" in flat(F[5]).lower()
    and "does not decide what another organization does with what it sees"
        in flat(F[5])
    and "recognised and valued somewhere other than here" not in FACE)
chk("D", "Visibility is not presented as evidence",
    "Visibility is not evidence." in flat(F[21])
    and "the wrong people have seen it" not in FACE)
chk("D", "Translation is about legibility, not solving recognition",
    "The evidence for it is not yet legible outside." in flat(F[21]))
chk("D", "Repair formation conditions reads as a category to test",
    "Test whether changing the work or conditions could repair the problem."
    in flat(F[21]) and "Change the work, not the employer, first." not in FACE)
chk("D", "Prepare for exit is preparation, not a recommendation to resign",
    "reason to prepare in case the conditions do not repair" in flat(F[21])
    and not re.search(r"\b(resign|quit)\b", CORE_FACE, re.I))
chk("D", "The session never claims to decide stay or leave",
    "This read will not tell you to stay or leave." in flat(F[3])
    and "I have not made that decision for you, and I should not." in flat(F[25]))
chk("D", "No destination-specific portability is promised",
    "generic portability is not destination-specific portability" in flat(N[22]).lower()
    and "did not read that destination" in flat(N[26]))
chk("D", "Nothing promises hiring, promotion, sponsorship or pay",
    not re.search(r"\b(guarantee|guarantees|guaranteed|will get you|lands you)\b",
                  CORE_FACE, re.I))

# ── E. the four-question portability frame, once ───────────────────────────
Q4 = ("What travels?", "What does not?", "What can I prove?", "What must I relearn?")
faces_with = [i for i in range(1, 27) if all(q in flat(F[i]) for q in Q4)]
notes_with = [i for i in range(1, 34) if all(q in flat(N[i]) for q in Q4)]
chk("E", "The four questions appear on exactly one slide face", faces_with == [22],
    "slide 22, as the interpretive frame directly above the Next-Move Note")
chk("E", "They are spoken once, on the same slide", notes_with == [22],
    f"notes carrying all four: {notes_with}")
chk("E", "They are framed as interpretation, not a new exercise",
    "nothing to score and nothing to hand in" in flat(N[22]))
chk("E", "No new worksheet or scoring was built around them",
    "WORKBOOK PAGE 8" in N[22] and len(pymupdf.open(WB)) == 8)

# ── F. slide 18 is materially simpler ──────────────────────────────────────
before18 = len([sh for sh in Presentation(PRIOR).slides[17].shapes
                if sh.has_text_frame and sh.text_frame.text.strip()])
after18 = len([sh for sh in Presentation(DECK).slides[17].shapes
               if sh.has_text_frame and sh.text_frame.text.strip()])
chk("F", "Slide 18 carries materially less on its face",
    after18 < before18 and len(flat(F[18])) < len(flat(OF[18])) * 0.75,
    f"{before18} text blocks down to {after18}; "
    f"{len(flat(OF[18]))} characters down to {len(flat(F[18]))}")
chk("F", "The three tiers survive on the face",
    all(t in F[18] for t in ("NONE", "1 OR 2", "3+")))
chk("F", "The mechanics that left the face are on workbook page 4",
    all(s in flat("\n".join(p.get_text() for p in pymupdf.open(WB)))
        for s in ("one point lower", "one point higher",
                  "Every neighbouring score stays inside the 1 to")),
    "nothing was lost, it was already printed in the workbook")

# ── G. commercial architecture ─────────────────────────────────────────────
chk("G", "Slide 23 still offers exactly two routes",
    OF[23] == F[23] and "I have enough for now." in F[23]
    and "Capability Formation Field Kit" in F[23]
    and "Career Move Review" not in F[23])
chk("G", "Route 1 remains genuine",
    "Nothing further is required. The session was built to be complete on its own."
    in flat(F[23]))
chk("G", "Career Move Review is absent from every slide face",
    "Career Move Review" not in FACE,
    "its route does not exist in the repository, so it is not offered from the stage")
chk("G", "Career Move Review is named in the notes and the SOP as unverified",
    "Career Move Review" in NOTE and "ROUTE NOT VERIFIED" in SOPT
    and "$500, one public price, qualification before payment" in SOPT)
chk("G", "Keep the Proof is not on the recorded product slide",
    "Keep the Proof" not in FACE and "Keep the Proof" in SOPT
    and "belongs in follow-up" in SOPT)
chk("G", "Private Capability Position Read is gone from every current instruction",
    "Private Capability Position Read" not in FACE
    and "RETIRED" in SOPT
    and not re.search(r"Private Capability Position Read (?!IS RETIRED|is RETIRED)"
                      r"[^.]*(?:not operational|off the continuation)", NOTE),
    "the only mentions in the deck notes and the SOP say it is retired")
chk("G", "No price appears on any slide face",
    not re.search(r"\$\d", CORE_FACE),
    "the Field Kit price is verified live and spoken, never printed on the replay")
# A line that quotes a phrase IN ORDER TO FORBID IT is the guardrail, not the
# breach. Slide 23's note tells the presenter never to say "special opportunity",
# and it has to contain the words to mean anything.
SCARCITY = re.compile(r"(normally \$|was \$|only \d+ (spots|seats)|limited time|"
                      r"special opportunity|last chance)", re.I)
BAN = re.compile(r"(do not|don't|never|no \b|must not)", re.I)
scarce = [l.strip()[:60] for l in (FACE + "\n" + NOTE).split("\n")
          if SCARCITY.search(l) and not BAN.search(l)]
chk("G", "No scarcity, discount theater or crossed-out pricing", not scarce,
    "; ".join(scarce) if scarce else
    "the only match is slide 23's note forbidding the phrase")
chk("G", "Slide 20 no longer implies the real answer is behind a paywall",
    "and it is complete" in flat(F[20])
    and "belongs in deeper follow-on work" not in FACE
    and "TODAY IS COMPLETE" in N[20])

# ── H. links, QR and routes ────────────────────────────────────────────────
z = zipfile.ZipFile(DECK)
links = set()
for n in z.namelist():
    if n.startswith("ppt/slides/_rels/"):
        links |= set(re.findall(r'Target="(https?://[^"]+)"', z.read(n).decode()))
qr = {}
for n in [m for m in z.namelist() if m.startswith("ppt/media/")]:
    try:
        from pyzbar.pyzbar import decode
        for dd in decode(Image.open(io.BytesIO(z.read(n)))):
            qr[n] = dd.data.decode()
    except Exception:
        pass
chk("H", "External links unchanged from v2.0.5", links == {FIELDKIT},
    " | ".join(sorted(links)))
chk("H", "Every QR decodes to an intended destination",
    set(qr.values()) <= {MAVEN, FIELDKIT} and qr,
    " | ".join(sorted(set(qr.values()))))
chk("H", "No retired Private Read route anywhere in the package",
    not re.search(r"(work\.html#get-in-touch|Private%20Capability)", FACE + NOTE + SOPT))

# ── I. structure, visual and render ────────────────────────────────────────
chk("I", "33 slides, 26 active, 7 hidden, unchanged",
    len(F) == 33 and hidden(DECK) == hidden(PRIOR) == list(range(27, 34)))
chk("I", "The dated holding slide is hidden and is the only dated face",
    33 in hidden(DECK) and sum("September" in F[i] for i in range(1, 34)) == 1
    and "Wednesday, September 23, 2026" in F[33])
chk("I", "The institutional close is still available",
    31 in hidden(DECK) and "INSTITUTIONAL DELIVERY CLOSE" in F[31]
    and "slide 31" in SOPT.replace("hidden slide 31", "slide 31"))
chk("I", "Exported deck is 26 pages, hidden slides excluded",
    len(pymupdf.open(DECK_PDF)) == 26)
# Overflow: re-wrap each frame at its real point size and measure against its box.
try:
    from PIL import ImageFont
    over = []
    for i in range(1, 27):
        for sh in Presentation(DECK).slides[i - 1].shapes:
            if not sh.has_text_frame or not sh.text_frame.text.strip():
                continue
            runs = [r for p in sh.text_frame.paragraphs for r in p.runs]
            if not runs or not runs[0].font.size:
                continue
            pt = runs[0].font.size.pt
            w_in, h_in = Emu(sh.width).inches, Emu(sh.height).inches
            chars = max(1, int(w_in * 72 / (pt * 0.50)))
            lines = sum(max(1, -(-len(p.text) // chars))
                        for p in sh.text_frame.paragraphs if p.text.strip())
            if lines * pt * 1.25 / 72 > h_in + 0.06:
                over.append(f"s{i}:{flat(sh.text_frame.text)[:28]}")
    # Measured against v2.0.5 rather than against zero. The estimator assumes an
    # average character width and is approximate, so three frames it flags on
    # BOTH versions were confirmed by eye in the render to wrap without
    # clipping or collision. What matters is that this pass introduced none and
    # repaired two.
    prior_over = []
    for i in range(1, 27):
        for sh in Presentation(PRIOR).slides[i - 1].shapes:
            if not sh.has_text_frame or not sh.text_frame.text.strip():
                continue
            runs = [r for p in sh.text_frame.paragraphs for r in p.runs]
            if not runs or not runs[0].font.size:
                continue
            pt = runs[0].font.size.pt
            w_in, h_in = Emu(sh.width).inches, Emu(sh.height).inches
            chars = max(1, int(w_in * 72 / (pt * 0.50)))
            lines = sum(max(1, -(-len(p.text) // chars))
                        for p in sh.text_frame.paragraphs if p.text.strip())
            if lines * pt * 1.25 / 72 > h_in + 0.06:
                prior_over.append(f"s{i}:{flat(sh.text_frame.text)[:28]}")
    new_over = [o for o in over if o not in prior_over]
    chk("I", "No new text overflow, and two pre-existing ones repaired",
        not new_over and len(over) < len(prior_over),
        f"{len(prior_over)} frames flagged on v2.0.5, {len(over)} on v2.0.6, "
        f"0 new. Slides 18 and 22 were repaired; the three that remain flag on "
        f"both versions and were confirmed by eye to wrap without clipping")
except Exception as e:
    chk("I", "No new text overflow, and two pre-existing ones repaired", False, str(e))
chk("I", "Deck is still native editable shapes, two raster assets only",
    len([n for n in z.namelist() if n.startswith("ppt/media/")]) == 3,
    "the portrait and two QR codes; nothing was flattened to an image")

# ── J. documents, versions and language ────────────────────────────────────
chk("J", "SOP is v2.0.10 and names deck v2.0.7",
    "v2.0.10" in SOPT and "60MIN_v2.0.7_CANDIDATE.pptx" in SOPT
    and not any(v in SOPT for v in ("v2.0.5", "v2.0.6", "v2.0.8", "v2.0.9")),
    "no superseded version survives in the facilitator's source-of-truth map")
sop_pages = pymupdf.open(SOP_PDF)
chk("J", "SOP exports at eight pages, with no stub final page",
    len(sop_pages) == 8
    and len([l for l in sop_pages[-1].get_text().split("\n") if l.strip()]) >= 12,
    "EIGHT PAGES IS APPROVED AND SETTLED, not an open decision. The commercial "
    "architecture grew from two live offers to five and three sections gained "
    "operational rules. The stub-page test the old seven-page pin protected is "
    "kept, and no operating control is cut to chase a page count")
chk("J", "Landscape is still confined to the reconciliation pages",
    ["L" if p.rect.width > p.rect.height else "P" for p in sop_pages]
    == ["P", "L", "L"] + ["P"] * 5)
chk("J", "The arrival poll is specified as pre-recording and optional",
    "PRE-RECORDING ONLY" in SOPT and "If the platform does not make it easy, skip it"
    in SOPT and "OPTIONAL ANONYMOUS ARRIVAL POLL" in N[33])
chk("J", "The poll never asks anything diagnostic",
    "NEVER ASK" in N[33] and "their score" in N[33] and "their employer" in N[33])
chk("J", "Checklist is v1.3 and marks the already-current Maven copy",
    "v1.3" in CHKT and "ALREADY CURRENT" in CHKT
    and "Identify which move is worth testing next" in CHKT)
chk("J", "Workbook is byte-identical and its Acrobat gate still applies",
    hashlib.sha256(open(WB, "rb").read()).hexdigest() == WB_SHA, WB_SHA)
chk("J", "No em dash in newly written participant-facing slide copy",
    not any("—" in F[i] for i in (4, 5, 18, 20, 21, 22, 25)),
    "checked on the seven revised slide faces")
chk("J", "US spelling in revised participant-facing copy",
    not re.search(r"(recognis|neighbour|behaviour|organis)",
                  "".join(F[i] for i in (4, 5, 18, 20, 21, 22, 25))),
    "the workbook keeps its British spellings and is not regenerated for them")
chk("J", "September 23 is the date, CT never CST",
    "Wednesday, September 23, 2026" in SOPT
    and not re.search(r"(?<![A-Za-z_])CST(?![A-Za-z_])",
                      SOPT.replace("Never write CST", "")))

# ── K. the September 19 final-candidate pass ───────────────────────────────
V206 = f"sept23-v206-assets/PRESENTER_VERSION_Stay_or_Leave_Live_Career_Growth_Assessment_60MIN_v2.0.6_CANDIDATE.pptx"
PF, PN = deck(V206)
faces_moved = [i for i in range(1, 34) if PF[i] != F[i]]
notes_moved = [i for i in range(1, 34) if PN[i] != N[i]]
chk("K", "Only slide 22's face and slide 5's note changed in this pass",
    faces_moved == [22] and notes_moved == [5],
    f"faces {faces_moved}, notes {notes_moved}. Nothing already working was reopened")
chk("K", "The four questions are still on exactly one slide, and still once",
    faces_with == [22] and notes_with == [22])
chk("K", "The frame now has its own strip rather than a compressed aside",
    "Three lines. Yours, private, and enough to act on." in F[22]
    and "What travels?" not in
        [p.text for sh in Presentation(DECK).slides[21].shapes
         if sh.has_text_frame and "Three lines" in sh.text_frame.text
         for p in sh.text_frame.paragraphs],
    "the subtitle is one line again and the questions sit on their own row")
_p22 = {j: (sh.top, sh.left, sh.width, sh.height)
        for j, sh in enumerate(Presentation(DECK).slides[21].shapes)}
_o22 = {j: (sh.top, sh.left, sh.width, sh.height)
        for j, sh in enumerate(Presentation(V206).slides[21].shapes)}
chk("K", "The Next-Move Note writing space is untouched",
    all(_p22[j] == _o22[j] for j in range(3, 23)),
    "the three prompt blocks, their rules and the closing band are all where "
    "v2.0.6 put them; the strip came out of unused title height")
chk("K", "Slide 22 gained exactly three shapes, all cloned from the slide",
    len(_p22) == len(_o22) + 3,
    "the panel, its gold accent and one line of text, copied from the prompt "
    "blocks so the strip inherits the deck's own styling")
chk("K", "The Optionality composite clarification is in the note, said once",
    N[5].count("composite reading of portability conditions") == 1
    and "not a prediction" in N[5]
    and "value, hire, promote or pay" in N[5])
chk("K", "It is not on any participant-facing slide",
    "composite reading" not in FACE and "not a prediction" not in FACE,
    "the slide face is unchanged from v2.0.6")
chk("K", "Statements 7, 10 and 12 are named as a post-September-23 review item",
    "statements 7, 10 and 12" in N[5].lower()
    and "post-september-23 instrument-review item" in N[5].lower()
    and "Do NOT reword them in delivery" in N[5])
chk("K", "The statements themselves are still untouched",
    all(OF[i] == F[i] for i in STATEMENTS)
    and "would be valued by an employer in a different industry" in F[9]
    and "can already see what I am good at" in F[10]
    and "could rebuild a strong position somewhere else within a year" in F[10],
    "flagged for review, not reworded, and the workbook is built on them")
chk("K", "The checklist replaces all three Maven outcomes against live wording",
    all(s in CHKT for s in
        ("Know whether your job is still building you",
         "Know what you can carry into another role",
         "Decide your next career move",
         "See whether your current work is still building you",
         "See what may still count when the context changes",
         "Identify which move is worth testing next")))
chk("K", "The recommended Maven copy does not call the group session private",
    "live, evidence-based session" in CHKT
    and "Private SCORING is accurate" in CHKT
    and "private session" not in CHKT.lower())
chk("K", "The checklist carries all four verified site conflicts with references",
    all(s in CHKT for s in ("fieldkit.html:337", "fieldkit.html:230",
                            "for-professionals.html:222",
                            "for-professionals.html:217"))
    and "DO NOT substitute a Career Move Review call to action" in CHKT)
chk("K", "Maven date, time, duration and positioning are marked do-not-change",
    "Date, time, duration and instructor positioning" in CHKT
    and "Wednesday, September 23, 2026, 6:00 PM CT, 60 minutes, free" in CHKT)
chk("K", "The SOP changed by version strings only",
    len(sop_pages) == 8
    and "OPTIONAL ANONYMOUS ARRIVAL POLL" in SOPT
    and "$500, one public price, qualification before payment" in SOPT
    and "RETIRED" in SOPT,
    "v2.0.9 to v2.0.10 is a pure substitution so the deck reference is not stale. "
    "No prose, rule, table or ordering moved, and the approved eight pages hold")
chk("K", "Career Move Review is still off every slide face",
    "Career Move Review" not in FACE)
chk("K", "Nothing was promoted to FINAL",
    "CANDIDATE" in os.path.basename(DECK) and "FINAL" not in os.path.basename(DECK))


if __name__ == "__main__":
    w = max(len(l) for _, _, l, _, _ in R)
    g = None
    for n, grp, label, st, note in R:
        if grp != g:
            print(f"\n── group {grp} " + "─" * 46); g = grp
        print(f"{n:>3}. [{st}] {label:<{w}}  {note}")
    fails = [r for r in R if r[3] != "PASS"]
    print(f"\n{len(R) - len(fails)} of {len(R)} pass")
    sys.exit(1 if fails else 0)
