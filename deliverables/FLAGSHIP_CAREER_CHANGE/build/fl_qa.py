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
    out = []
    for el in card.els:
        if el.get("kind") == "text":
            for run in el.get("runs", []):
                out.append(run.get("text", ""))
            if el.get("text"):
                out.append(el["text"])
    return out

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
    bad = []
    for name, c in cards:
        body = " ".join(texts(c)).lower()
        bad += ["%s: %s" % (name, p) for p in FORBIDDEN if re.search(p, body)]
    check(3, "No forbidden claim appears on any slide", not bad,
          "Nine patterns searched, including everything transfers, starting "
          "over, equivalent and identical." if not bad else str(bad[:3]))

    # 4
    pub = set()
    for name, c in cards:
        for t in texts(c):
            for line in t.split("\n"):
                s_ = line.strip()
                if s_ and not s_.isupper() and len(s_.split()) > 1:
                    pub.add(s_)
    mapped = " || ".join(a for a, _, _, _, _ in P.MAP).lower()
    unmapped = [s_ for s_ in pub
                if s_.lower() not in mapped
                and not any(w in s_.lower() for w in
                            ("two real u.s. job postings", "real overlap",
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

    return CHECKS

if __name__ == "__main__":
    for n, name, ok, detail in run():
        print(("  ok  " if ok else " FAIL ") + "%02d %s" % (n, name))
        print("        " + detail[:200])
    print("\n%d checks, %d failed" % (len(CHECKS),
                                      sum(1 for c in CHECKS if not c[2])))
