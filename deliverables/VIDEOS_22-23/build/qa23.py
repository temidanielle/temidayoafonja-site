# -*- coding: utf-8 -*-
"""Package QA for V22 and V23.

Every check reads the built package from disk, not the intent that produced
it. Where a check reads across the whole package it only ever asks the
package to be consistent with the approved script; it never asks approved
copy to change.
"""
import os, re, glob, hashlib
import masters23 as M
import frames23 as F
import spine23 as SP
import recdocs23 as R
import shorts23 as SH
import publish23 as PUB
import evidence23 as EV

from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn

EM_DASH = "—"
BRITISH = ("labelled", "programme", "organise", "organisation", "analyse",
           "behaviour", "colour", "favour", "recognise", "prioritise",
           "utilise", "licence fee", "travelled", "modelling", "centre of "
           "excellence", "defence", "practise")


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h.update(b)
    return h.hexdigest()


def _docx_units(path):
    d = Document(path)
    out = []
    for c in d.element.body.iterchildren():
        if c.tag == qn("w:p"):
            t = Paragraph(c, d).text.strip()
            if t:
                out.append(t)
        elif c.tag == qn("w:tbl"):
            for r in Table(c, d).rows:
                for cell in r.cells:
                    t = cell.text.strip()
                    if t:
                        out.append(t)
    return out


def units(path):
    if path.endswith(".docx"):
        return _docx_units(path)
    if path.endswith(".txt"):
        return [l for l in open(path, encoding="utf-8").read().split("\n")
                if l.strip()]
    return []


def all_units(pkg):
    out = []
    for root, _, names in os.walk(pkg):
        for nm in sorted(names):
            if nm.endswith((".docx", ".txt")):
                out.extend(units(os.path.join(root, nm)))
    return out


def _flat(s):
    return " ".join(str(s).split())


# A package that documents its own boundaries necessarily contains the
# sentences it forbids. "Never: highest in the market" is the rule working,
# not the rule broken, so a hit inside a prohibition does not count.
NEG = ("no ", "not ", "never", "nothing", "without", "cannot", "avoid",
       "absent", "must not", "do not", "does not", "neither", "nor ",
       "may not", "is not", "are not", "none of", "rather than",
       "instead of", "invented", "superseded", "forbid", "prohibit")


def negated(text, at, window=140):
    """Does the hit at this offset sit inside a prohibition?

    The lookback stops at a sentence end, not at a colon or semicolon: a
    boundary note reads "Never: representative of the labor market", and
    treating the colon as a break would hide the word that makes it a rule.
    """
    start = max(text.rfind(". ", max(0, at - window), at), at - window, 0)
    return any(w in text[start:at] for w in NEG)


def forbidden(n, us, phrases):
    """Places the package asserts one of these, rather than forbidding it.

    Measured across the joined document text rather than unit by unit,
    because the text documents wrap their lines and a wrapped line can carry
    a phrase away from the word that forbids it.
    """
    body = _flat(" ".join(us)).lower()
    hits = []
    for ph in phrases:
        for m in re.finditer(re.escape(ph), body):
            if negated(body, m.start()):
                continue
            frag = body[max(0, m.start() - 60):m.end() + 40]
            if quoted(n, frag, ph):
                continue
            hits.append((ph, frag))
    return hits


def near(us, pattern, qualifier, window=220):
    """Every occurrence of pattern must have qualifier within `window`
    characters of it in the same document. Measured across the document text,
    because a wrapped line in a .txt file is not a sentence."""
    body = _flat(" ".join(us)).lower()
    q = qualifier.lower()
    for m in re.finditer(pattern, body):
        seg = body[max(0, m.start() - window):m.end() + window]
        if q not in seg:
            return False, body[max(0, m.start() - 60):m.end() + 60]
    return True, "every occurrence carries it"


def source_corpus(n):
    """Everything the approved sources actually say, for quoting checks."""
    parts = [M.spoken_text(n), M.title(n), M.thumbnail(n)]
    parts += [lab for _, lab, _ in M.sections(n)]
    parts += M.packet_lines() + M.overview_lines()
    return _flat(" ".join(parts)).lower()


def quoted(n, unit, hit, window=40):
    """Is this hit inside wording the approved sources already carry?"""
    u, corpus = _flat(unit).lower(), source_corpus(n)
    i = u.find(_flat(hit).lower())
    if i < 0:
        return False
    frag = u[max(0, i - window):i + len(_flat(hit)) + window].strip()
    while len(frag) > 16:
        if frag in corpus:
            return True
        frag = frag[2:-2].strip() if len(frag) > 22 else frag[1:].strip()
    return False


def run(n, pkg, geo_problems, assets):
    R_ = []

    def ck(name, ok, detail):
        R_.append((name, bool(ok), detail))

    us = all_units(pkg)
    flat_us = [_flat(u) for u in us]

    # ---------------------------------------------------- source integrity
    rec = os.path.join(pkg, "01_Recording")
    master = os.path.join(rec, "Recording_Master.docx")
    blocks = os.path.join(rec, "Thought_Block_Recording_Copy.docx")
    ck("The updated 50CHAR script is the source used",
       M.read(n)["sha"] == M.sha256(M.path(n)),
       "SHA-256 %s" % M.read(n)["sha"])
    ck("Recording master carries every spoken word, unchanged",
       _spoken_present(master, n), "%s words" % format(M.word_count(n), ","))
    ok, detail = R.matches_script(n)
    ck("Thought-block copy matches the script exactly", ok, detail)
    stray = _superseded_outside_the_index(pkg)
    ck("Superseded packaging appears only where it is marked superseded",
       not stray, stray or "absent from every production document; listed "
                           "only in the source hierarchy, so nobody "
                           "restores it")
    ck("Advisor rationale never overrides spoken wording",
       all(M._norm(f["trigger"]) in M._norm(M.spoken_text(n))
           for f in F.SETS[n]),
       "every cue is a sentence of the script itself")

    # ---------------------------------------------------------- packaging
    ck("Title exact", any(u.strip() == M.title(n) for u in us), M.title(n))
    ck("Thumbnail exact, stated on its own line",
       any(u.strip() == M.thumbnail(n) for u in us), M.thumbnail(n))
    ck("Title is under 50 characters", len(M.title(n)) < 50,
       "%d characters" % len(M.title(n)))

    # ------------------------------------------------------------ triggers
    bad = [f["key"] for f in F.SETS[n] if not M.trigger_ok(n, f["trigger"])]
    ck("Every cue is a whole spoken paragraph, found once", not bad,
       bad or "%d cues" % len(F.SETS[n]))
    pl = SP.placements(n)
    twice = sorted({k for k in pl if pl.count(k) > 1})
    ck("Every card is cued once and only once",
       not twice and len(pl) == len(F.SETS[n]),
       twice or "%d cards, %d placements" % (len(F.SETS[n]), len(pl)))

    # ------------------------------------------------- camera and visuals
    cam, full = SP.counts(n)
    ck("The video stays camera-led", cam >= full,
       "%d camera stretches against %d full-screen cues" % (cam, full))
    ck("The opening human recognition is not covered",
       _opening_camera(n),
       "the strongest opening line plays on camera")
    mp = os.path.join(pkg, "03_Riverside", "Camera_and_Full_Screen_Map.txt")
    t = open(mp, encoding="utf-8").read() if os.path.exists(mp) else ""
    ck("The map distinguishes camera from full screen",
       "[ CAMERA ]" in t and "[ FULL SCREEN ]" in t,
       "both are marked throughout the spine")
    ck("Substantive teaching is true full screen",
       all(f["mode"] == "FULL SCREEN" for f in F.SETS[n]),
       "no overlay, no corner placement, no presenter behind a card")
    ck("Every card is 1920 x 1080", _all_1080(assets), "%d PNG" % len(assets))
    ck("Geometry is clean against the rendered DOM", not geo_problems,
       geo_problems or "%d states measured" % len(F.states(n)))
    multi, bad_active = _active_states(n)
    ck("One active idea at a time where a structure is taught",
       not bad_active,
       bad_active or "%d multi-state families, each measured against its "
                     "declared build shape. Never two active at once."
                     % multi)
    ext = forbidden(n, us, ("articulate", "lms", "progress bar",
                            "quiz interface", "fake button",
                            "training icon"))
    ck("No external branding, interface or icon set is used", not ext,
       ext or "the screenshots informed the information design only")

    # ------------------------------------------------------ CTA and finish
    urls = set()
    for u in us:
        urls |= set(re.findall(r"temidayoafonja\.com/[\w\-/]+", u))
    allowed = ({PUB.ROUTES[PUB.RESOURCE[n]]} if PUB.RESOURCE[n] else set())
    ck("Only a resource the script speaks appears", urls <= allowed,
       (urls - allowed) or (PUB.RESOURCE[n] or "this script names no "
                            "resource"))
    ck("CTA is a single ask" if n == 22 else "One action and one resource",
       _cta_shape(n), "as the script states it")
    ck("Watch Next is full screen and final",
       any("full screen and final" in u.lower() for u in us)
       and any("no return to camera" in u.lower() for u in us),
       "stated in the production documents")
    ck("Watch Next destinations exist in V4 to V21",
       all(4 <= dst <= 21 for dst, _ in PUB.WATCH_NEXT[n]),
       ", ".join("V%d" % dst for dst, _ in PUB.WATCH_NEXT[n]))
    ck("No chapters are created before the final edit",
       not re.search(r"\n\s*0:00\s+[A-Z].{0,60}\n\s*\d+:\d\d\s+[A-Z]",
                     "\n".join(us))
       and any("after the final edit" in u.lower() for u in us),
       "chapters deferred to real export timing")
    ck("No SRT is created before the final edit",
       not glob.glob(os.path.join(pkg, "**", "*.srt"), recursive=True)
       and any("srt" in u.lower() and "after the final edit" in u.lower()
               for u in us),
       "SRT deferred to Riverside after the cut")

    # ------------------------------------------------------------- shorts
    ck("Six candidate Shorts", len(SH.rows(n)) == 6,
       "a selection bank, not six uploads")
    ck("Every Short line is in the source script", not SH.verify(n),
       SH.verify(n) or "%d lines verified"
       % sum(len(r["lines"]) for r in SH.rows(n)))
    ck("Every Short carries its boundary",
       all(r["boundary"].strip() for r in SH.rows(n)),
       "six of six")

    # ---------------------------------------------------------- integrity
    ck("U.S. English throughout what this build authored",
       not _british(n, us), _british(n, us) or "clean")
    ck("No em dashes in what this build authored",
       not _emdash(n, us), _emdash(n, us) or "clean")
    ck("No measured runtime is stated anywhere",
       not any(re.search(r"\b(measured|final|actual)\s+runtime\s+(is|of)\s+"
                         r"\d", u.lower()) for u in us)
       and any("not a runtime" in u.lower() or
               "arithmetic" in u.lower() for u in us),
       "every figure is arithmetic on the script")
    ck("No invented research", _research_bounded(n, us),
       "fifteen postings, eleven employers" if n == 22 else
       "nine of fifteen, kept with its denominator")
    perf = forbidden(n, us, ("music license", "licensed track",
                             "click-through rate", "impressions",
                             "views expected"))
    ck("No music license, thumbnail result or performance claim", not perf,
       perf or "none claimed")

    # ------------------------------------------------------- per-video set
    if n == 22:
        ck("Fifteen postings and eleven employers preserved",
           M.contains(22, "fifteen postings from eleven employers"),
           "stated in the script and carried on the sample card")
        gen = forbidden(22, us, ("most employers", "the market wants",
                                 "all employers", "titles are meaningless",
                                 "titles never matter",
                                 "representative of the labor market"))
        ck("No labor-market generalization", not gen, gen or "none present")
        ck("The two HCSC examples stay distinct",
           _flat("same employer, different department").lower()
           in _flat(" ".join(us)).lower(),
           "the second is marked as the same company, different department")
        mkt = forbidden(22, us, ("highest in the market",
                                 "highest published ceiling in the market"))
        ck("The ceiling claim is bounded to this sample",
           M.contains(22, "in this sample")
           and any("in this sample" in u.lower() for u in us) and not mkt,
           mkt or "highest published ceiling in this sample")
        _b = _flat(" ".join(us)).lower()
        who = [_b[max(0, m.start() - 50):m.end() + 20]
               for m in re.finditer(r"(someone|somebody|another person|else)"
                                    r"\s+(made|created|wrote)\s+"
                                    r"(those|the)\s+predefined", _b)
               if not negated(_b, m.start())]
        ck("No claim about who wrote the predefined decisions", not who,
           who or "the posting establishes them, and nothing says who made "
                  "them")
        ck("Execution is not treated as lack of seriousness",
           M.contains(22, "And that is not a criticism.")
           and any("not a criticism" in u.lower() for u in us),
           "the defense of the role is in the master and the cue notes")
        ck("GiveDirectly boundaries preserved",
           M.contains(22, "unlikely to be a strong fit")
           and M.contains(22, "at least three hours"),
           "both stated constraints are in the script and on the card")
        ok_ct, det = near(us, r"\b(7 or 8|seven or eight) a\.?m\.?",
                          "central time")
        ck("The Central Time qualifier travels with the 7 or 8 a.m. figure",
           ok_ct, det)
        ck("The $65,000 figure is bounded to these two jobs",
           any("these two jobs" in u.lower() for u in us),
           "the boundary card follows the reveal immediately")
    else:
        ck("The synthetic example is controlled",
           any("synthetic" in u.lower() and "not a client" in u.lower()
               for u in us),
           "labeled as invented, not a client, employer or posting")
        ck("Every card showing a synthetic figure carries the label",
           not _unlabeled_synthetic(), "checked state by state")
        ck("No invented personal experience",
           not any(re.search(r"\bI (once|personally) (ran|led|managed)\b",
                             u) for u in us),
           "the depot example is never attributed to Temidayo")
        ck("The employer in the comparison is anonymized",
           "mercury" not in _flat(" ".join(us)).lower(),
           "no name, no logo, no URL, no identifying styling")
        ck("Nine of fifteen stays sample-bounded",
           M.contains(23, "Nine of the fifteen job descriptions")
           and any("9 of 15" in u.lower() or "nine of the fifteen" in u.lower()
                   for u in us),
           "the denominator is on the card")
        ck("Execution is not treated as lack of judgment",
           M.contains(23, "Execution still contains choices.")
           and any("execution still contains choices" in u.lower()
                   for u in us),
           "the line is in the script and on a card")
        ck("Real gaps are preserved",
           M.contains(23, "learn, earn, or experience")
           and any("better proof does not erase" in u.lower() for u in us),
           "the closing limit is on screen")
        ck("Career Evidence Starter is the only resource CTA",
           urls == {PUB.ROUTES["Career Evidence Starter"]},
           "one resource, not stacked")
    return R_


# ------------------------------------------------------------- predicates
def _spoken_present(path, n):
    if not os.path.exists(path):
        return False
    body = _flat(" ".join(units(path)))
    return all(_flat(p) in body for p in M.paragraphs(n))


def _opening_camera(n):
    """The strongest human line of the opening must not sit under a card."""
    line = {22: "That is a real posting. And if you trusted the title, you "
                "would probably misread the job.",
            23: "You did the work. I believe you. The sentence does not."}[n]
    return not any(M._norm(f["trigger"]) == M._norm(line)
                   for f in F.SETS[n])


def _active_states(n):
    """Read the emphasis off the drawn cards and hold each family to its
    declared build shape.

    Every layout declares how many items it emphasizes, so this measures the
    card rather than trusting the reveal note beside it.
    """
    import sys
    sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                    "riverside-build")
    import rdeck
    built, bad = 0, []
    for f in F.SETS[n]:
        seen = []
        for st in f["states"]:
            c = rdeck.Card(1, st["name"])
            st["draw"](c)
            a = getattr(c, "active_items", None)
            if a is None:
                bad.append("%s: the layout declares no emphasis state"
                           % st["name"])
                a = 0
            if a > 1:
                bad.append("%s: %d items active at once" % (st["name"], a))
            seen.append(a)
        if len(f["states"]) < 2:
            continue
        built += 1
        if f["build"] == "ESTABLISH":
            if seen[0] != 0:
                bad.append("%s: declared ESTABLISH but the first state "
                           "already emphasizes a component" % f["key"])
            if sum(1 for x in seen[1:] if x == 1) != len(seen) - 1:
                bad.append("%s: declared ESTABLISH but not every later "
                           "state activates exactly one" % f["key"])
        elif f["build"] == "ARRIVE":
            if any(x != 1 for x in seen):
                bad.append("%s: declared ARRIVE but a state emphasizes "
                           "none or several" % f["key"])
        elif f["build"] == "BUILD":
            if sum(seen) and max(seen) > 1:
                bad.append("%s: declared BUILD but a state emphasizes "
                           "several" % f["key"])
    return built, bad


def _superseded_outside_the_index(pkg):
    """Superseded packaging may be named only where it is marked superseded."""
    allowed = ("Source_Hierarchy_and_Manifest.txt", "Source_Hierarchy.txt",
               "V22-V23_MASTER_CHANGELOG_AND_SOURCE_HIERARCHY.docx")
    stray = []
    for root, _, names in os.walk(pkg):
        for nm in sorted(names):
            if not nm.endswith((".docx", ".txt")) or nm in allowed:
                continue
            body = _flat(" ".join(units(os.path.join(root, nm)))).lower()
            for t in M.SUPERSEDED_TITLES:
                if _flat(t).lower() in body:
                    stray.append("%s: superseded title" % nm)
            if "one win" in body and "proof" in body and "\u2192" in body:
                stray.append("%s: superseded thumbnail" % nm)
    return stray


def _all_1080(assets):
    from PIL import Image
    for p in assets:
        if p.endswith(".png") and Image.open(p).size != (1920, 1080):
            return False
    return bool(assets)


def _cta_shape(n):
    cta = [f for f in F.SETS[n] if f["treatment"] == "CTA"]
    if len(cta) != 1:
        return False
    if n == 22:
        return not any("temidayoafonja.com" in s["name"].lower()
                       for s in cta[0]["states"])
    return True


def _british(n, us):
    hits = []
    for u in us:
        for w in BRITISH:
            if re.search(r"\b%s\b" % w, u.lower()) and not quoted(n, u, w):
                hits.append((w, u[:46]))
    return hits


def _emdash(n, us):
    return [u[:60] for u in us if EM_DASH in u and not quoted(n, u, EM_DASH)]


def _research_bounded(n, us):
    if n == 22:
        return M.contains(22, "fifteen postings from eleven employers")
    return M.contains(23, "Nine of the fifteen job descriptions")


def _unlabeled_synthetic():
    """A state that draws a synthetic figure must register the badge."""
    import sys
    sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                    "riverside-build")
    import rdeck
    FIGS = ("18 percent", "71 percent", "89 percent", "seven months")
    bad = []
    for f in F.SETS[23]:
        for s in f["states"]:
            c = rdeck.Card(1, s["name"])
            s["draw"](c)
            text = " ".join(p["text"].lower() for el in c.els
                            if el["t"] == "text" for p in el["paras"])
            shows = any(x in text for x in FIGS)
            badged = any("synthetic example" in t.lower()
                         for t in getattr(c, "foot_texts", []))
            if shows and not badged:
                bad.append(s["name"])
    return bad
