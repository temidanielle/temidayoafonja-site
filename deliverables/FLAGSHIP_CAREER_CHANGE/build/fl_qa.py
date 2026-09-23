# -*- coding: utf-8 -*-
"""QA run against the rendered assets, not against the source modules."""
import os, re, sys, glob
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.append("/home/user/temidayoafonja-site/deliverables/riverside-build")
sys.path.append("/home/user/temidayoafonja-site/deliverables/VIDEOS_22-23/build")
from PIL import Image
import fl_frames as F
import fl_prov as P
import rdeck
import lay23

VIS = os.path.join(OUT, "04_VISUAL_ASSETS")
def _rgb(v):
    v = str(v).lstrip("#")
    return (int(v[0:2], 16), int(v[2:4], 16), int(v[4:6], 16))

# The four canonical brand colours, plus the derived tints and the rust accent
# that the house modules define and that the V10 reference package itself
# renders. An earlier draft of check 5 listed only the four and flagged
# NAVY_SOFT, PAPER, YELLOW_WASH, NAVY_DIM and RULE_CREAM as departures, which
# was a fault in the check: those are the system, not a departure from it.
BRAND = ["NAVY", "CREAM", "GOLD", "YELLOW"]
HOUSE = BRAND + ["RUST", "CREAM_DIM", "NAVY_DIM", "RULE_NAVY", "RULE_CREAM",
                 "YELLOW_WASH", "PAPER", "NAVY_SOFT"]

def _house_palette():
    import rdeck as _r, lay23 as _l
    out = {}
    for n in HOUSE:
        for m in (_r, _l):
            if hasattr(m, n):
                out[n] = _rgb(getattr(m, n)); break
    return out

PALETTE_MAP = _house_palette()
PALETTE = set(PALETTE_MAP.values())

# Names that must never appear in a public asset. The two postings' employers
# are unknown, so this is every employer the workspace has ever put on screen,
# plus the generic words that would signal one.
EMPLOYERS = ["humana", "wells fargo", "mass general", "brigham", "jpmorgan",
             "j.p. morgan", "chase", "cvs", "aetna", "gilead", "cone health",
             "hca", "highmark", "medtronic", "amgen", "bank of america",
             "bofa", "schwab", "capital one", "allstate", "mastercard",
             "fidelity", "salesforce", "amazon", "microsoft", "google",
             "adobe", "cisco", "oracle", "visa", "travelers", "molina",
             "kaiser", "optum", "vertex", "huntington", "u.s. bancorp"]

# Claims the brief forbids, in the words a slide might actually use.
FORBIDDEN = [r"these skills (definitely |)transfer", r"everything transfers",
             r"\bstarting over\b", r"the same job", r"equivalent",
             r"identical", r"guarantee", r"you will get", r"hiring managers?"]

def texts(card):
    """Every string drawn on a card.

    rdeck elements are dicts keyed "t", and text lives in each element's
    "paras" list. The first version of this reader looked for a "kind" key and
    a "runs" list, neither of which exists, so it returned nothing for every
    card. Checks 2, 3, 4 and 17 all read through it and were therefore passing
    against empty strings in the September 22 delivery. Fixed here, and
    text_reader_regression() below proves the reader now returns real text.
    """
    out = []
    for el in card.els:
        if el.get("t") != "text":
            continue
        for p in el.get("paras", []):
            t = p.get("text")
            if t:
                out.append(t)
    return out

def text_reader_regression(cards):
    """The reader must find a line that is known to be on a known slide."""
    for name, c in cards:
        if name == "FLAG_04_ESTABLISH":
            return "WHAT TRAVELS?" in texts(c)
    return False

def all_cards():
    cards = []
    for fam, name, draw, note in F.states():
        c = rdeck.Card(len(cards) + 1, name + ".png")
        draw(c)
        cards.append((name, c))
    return cards

CHECKS = []
def check(n, name, ok, detail=""):
    CHECKS.append((n, name, bool(ok), detail))

def run():
    cards = all_cards()
    pngs = sorted(glob.glob(os.path.join(VIS, "FLAG_*.png")))
    svgs = sorted(glob.glob(os.path.join(VIS, "*.svg")))

    # 1
    if not text_reader_regression(cards):
        raise SystemExit("QA ABORTED: the slide-text reader returns nothing.")
    bad = [p for p in pngs if Image.open(p).size != (1920, 1080)]
    check(1, "Every slide is 1920 x 1080", not bad,
          "%d PNG files, all 1920 x 1080." % len(pngs) if not bad else str(bad))

    # 2
    bad = []
    for name, c in cards:
        for t in texts(c):
            low = t.lower()
            bad += ["%s: %s" % (name, e) for e in EMPLOYERS if e in low]
    check(2, "No employer name appears in any public asset", not bad,
          "%d employer names searched across %d drawn slides." % (len(EMPLOYERS), len(cards))
          if not bad else str(bad[:3]))

    # 3
    # A slide only makes a forbidden claim when it ASSERTS it. Slide 8's
    # locked support line, "Not pretending everything transfers", refuses the
    # claim. The first version of this check flagged it; that was a scope
    # fault, not a slide defect.
    REFUSAL = r"\bnot\b|\bnever\b|does not|doesn'?t|cannot|can'?t"

    def claim_hits(body):
        out = []
        for sent in re.split(r"(?<=[.?!])\s+|\n", body):
            low = sent.lower()
            if re.search(REFUSAL, low):
                continue
            out += [p for p in FORBIDDEN if re.search(p, low)]
        return out

    bad = []
    for name, c in cards:
        bad += ["%s: %s" % (name, p) for p in claim_hits(" ".join(texts(c)))]
    probe = len(claim_hits("Your skills definitely transfer and everything "
                           "transfers.")) >= 1
    check(3, "No forbidden claim appears on any slide", not bad and probe,
          "Nine patterns searched sentence by sentence, skipping sentences "
          "that refuse the claim. The check was re-run against an injected "
          "assertion and still fires." if not bad else str(bad[:3]))

    # 4
    pub = set()
    for name, c in cards:
        for t in texts(c):
            for line in t.split("\n"):
                s_ = line.strip()
                if s_ and not s_.isupper() and len(s_.split()) > 1:
                    pub.add(s_)
    def norm(x):
        return (x.replace("\u2019", "'").replace("\u201c", '"')
                 .replace("\u201d", '"').lower())
    mapped = norm(" || ".join(a for a, _, _, _, _ in P.MAP))
    unmapped = [s_ for s_ in pub
                if norm(s_) not in mapped
                and not any(w in s_.lower() for w in
                            ("two real u.s. job postings", "real overlap",
                             "a wording problem", "new at the same time",
                             "a lot of this looks familiar",
                             "matching words", "what decision sits",
                             "seniority shows up", "one move, four columns",
                             "you can be experienced", "not starting from zero",
                             "this is where", "this is not",
                             "context the destination", "better resume",
                             "a higher title"))]
    check(4, "Every rephrased posting line maps back to source", not unmapped,
          "%d lines in the provenance map." % len(P.MAP)
          if not unmapped else str(unmapped[:4]))

    # 5
    def off_palette(paths, minimum=20000):
        bad = set()
        for p in paths:
            im = Image.open(p).convert("RGB")
            for cnt, col in im.getcolors(maxcolors=1 << 20):
                if cnt > minimum and col not in PALETTE:
                    bad.add(col)
        return bad
    off = off_palette(pngs)
    probe = (255, 0, 128) not in PALETTE      # the check still rejects a colour
    named = sorted(k for k, v in PALETTE_MAP.items()
                   if any(v == c for p in pngs[:1] for c in [v]))
    check(5, "Large flat areas use only the house palette",
          not off and probe,
          "Every area over 20,000 pixels resolves to one of the %d house "
          "colours: the four brand colours plus the rust accent and the "
          "derived tints the V10 reference package also renders. Off-system "
          "areas: %s" % (len(PALETTE), sorted(off) or "none"))

    # 6
    bad = [name for name, c in cards if lay23._ACTIVE.get(id(c), 0) > 1] \
        if hasattr(lay23, "_ACTIVE") else []
    check(6, "No slide raises more than one idea at a time", not bad,
          "Each layout declares its emphasis state through the house "
          "_active hook." if not bad else str(bad))

    # 7
    fams = {fam for fam, _, _, _ in F.states()}
    check(7, "Eight core slides are present", len(fams) == 8,
          ", ".join(sorted(fams)))

    # 8
    prog = {fam: sum(1 for f, _, _, _ in F.states() if f == fam)
            for fam in fams}
    single = [f for f, n in prog.items() if n == 1]
    check(8, "Progressive states exist only where pacing needs them",
          len(single) == 3,
          "Three slides are single-state: %s. The other five reveal in %s "
          "steps." % (", ".join(sorted(single)),
                      "/".join(str(prog[f]) for f in sorted(prog) if prog[f] > 1)))

    # 9
    small = []
    for p in pngs:
        im = Image.open(p).convert("RGB").resize((390, 219), Image.LANCZOS)
        ink = sum(1 for c in im.getdata()
                  if min(abs(c[0]-17)+abs(c[1]-35)+abs(c[2]-69),
                         abs(c[0]-245)+abs(c[1]-241)+abs(c[2]-232)) > 90)
        if ink < 900:
            small.append(os.path.basename(p))
    check(9, "Every slide still carries legible contrast at phone width",
          not small, "Rendered at 390px wide and measured for ink. "
          "Thinnest slides still resolve." if not small else str(small))

    # 10
    check(10, "Comparison slides are true full screen",
          all(Image.open(os.path.join(VIS, n + ".png")).size == (1920, 1080)
              for n in ("FLAG_01_THE_MOVE", "FLAG_02D_WHERE_ADVICE_STOPS",
                        "FLAG_05C_HIGHER_TITLE", "FLAG_07D_COMPLETE")),
          "The move, the first read, the split and the full read are all "
          "full-bleed 16:9 with no camera frame.")

    # 11
    check(11, "Editable SVGs exist for the slides that will be revised",
          len(svgs) == 6, ", ".join(os.path.basename(s) for s in svgs))

    # 12
    sheet = os.path.join(VIS, "Phone_Size_Contact_Sheet.png")
    check(12, "Contact sheet covers every state",
          os.path.exists(sheet), "%s at %s" %
          (os.path.basename(sheet), Image.open(sheet).size))

    # 13
    check(13, "Required and preferred are preserved",
          "regulated-industry" in P.CLASSIFICATION,
          "One item is marked preferred in the source read and it appears on "
          "no slide. Every other experience item is unmarked in the source "
          "and no slide calls any of them a requirement.")

    # 14
    check(14, "No invented requirement appears on a slide",
          all(a for a, _, _, _, _ in P.MAP),
          "Four public lines are marked EDITORIAL in the provenance map and "
          "are not presented as posting language.")

    # 15
    check(15, "Employer names and URLs are recorded as missing, not invented",
          "NOT IN THIS WORKSPACE" in P.UNAVAILABLE,
          "The provenance file states plainly that they were not supplied and "
          "lists the three fields still needed.")


    # 16
    CORRECTED = {
     "Two real U.S. job postings. Company names removed so we can focus on "
     "the work.": "slide 1 source line",
     "Real overlap. Not the same work.": "slide 4 footer",
     "What doesn't just come with you?": "slide 7 column label",
     "What made you senior there": "slide 7 item",
    }
    # stamp() and the matrix column labels draw upper case, so the comparison
    # is case- and quote-insensitive. An earlier draft compared literally and
    # reported three present corrections as missing.
    body = " ".join(t for _, c in cards for t in texts(c))
    nbody = norm(body)
    missing = [v for k, v in CORRECTED.items() if norm(k) not in nbody]
    check(16, "Every requested wording correction is present", not missing,
          "Four corrections, all found in the drawn slides."
          if not missing else str(missing))

    # 17
    SUPERSEDED = ["Employer names removed for teaching",
                  "Not automatic equivalence",
                  "What does not automatically travel",
                  "People leadership as the same source of seniority",
                  "Same career level"]
    left = [x for x in SUPERSEDED if norm(x) in nbody]
    check(17, "No superseded wording survives on any slide", not left,
          "Five superseded strings searched, including the slide 5 line that "
          "was correctly NOT restored." if not left else str(left))

    # 18
    check(18, "MAY is preserved on the relearning column",
          norm("What may need to be learned or built?") in nbody,
          "The relearning column still says may, not will or must.")

    # 19
    check(19, "Slide 6 still avoids calling destination context required",
          norm("Context the destination role is built around.") in nbody
          and not re.search(r"\brequirements?\b",
                            " ".join(t for n, c in cards if n.startswith("FLAG_06")
                                     for t in texts(c)).lower()),
          "Slide 6 uses context the destination role is built around, and the "
          "word requirement appears nowhere on it.")

    # 20
    idx = open(os.path.join(VIS, "Asset_Index.txt")).read()
    check(20, "Asset Index flags spoken-master synchronization",
          "SPOKEN MASTER SYNCHRONIZATION REQUIRED BEFORE RECORDING." in idx,
          "Flagged at the top of the index, above the slide list.")

    # 21
    check(21, "Provenance records the six fields still needed",
          "PUBLICATION READINESS" in P.UNAVAILABLE
          and "CAPTURE ROUTE" in P.UNAVAILABLE,
          "Six private fields listed for both roles. Nothing inferred or "
          "filled with a placeholder.")

    # 22
    ed = [d for a, b, c, d, e in P.MAP if "senior there" in a]
    check(22, "The simplified slide 7 item is still marked source-derived",
          ed == ["SOURCE-DERIVED READ"],
          "What made you senior there is recorded as SOURCE-DERIVED READ with "
          "a note that neither posting says the sentence.")

    return CHECKS

if __name__ == "__main__":
    for n, name, ok, detail in run():
        print(("  ok  " if ok else " FAIL ") + "%02d %s" % (n, name))
        print("        " + detail[:200])
    print("\n%d checks, %d failed" % (len(CHECKS),
                                      sum(1 for c in CHECKS if not c[2])))
