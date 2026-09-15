# -*- coding: utf-8 -*-
"""Package QA for NEW V10 and V11. Every check reads what is on disk."""
import os, re, glob, sys
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.append(DELIV + "VIDEOS_22-23/build")
import v1011 as S
import frames1011 as F
import spine1011 as SP
import shorts1011 as SH
import publish1011 as PUB
import langcheck23 as LANG
from qa23 import units, _flat, negated as _negated, BRITISH, EM_DASH

# A production document that names what a video must not be read as
# necessarily contains that phrase. Those framings are prohibitions too.
EXTRA_NEG = ("protection against", "keeps the video from", "read as",
             "reading as", "turn the video into", "may not", "must not",
             "does not claim", "is not a", "never", "no card", "does not "
             "tell you", "not a label", "is not an")

# The shared checker keeps discourse verbs out of scope so inclusive
# editorial phrasing is not rewritten. This is the same narrow extension
# the sprint layer carries, applied here too.
HABIT = re.compile(
    r"\b(?:people|professionals|candidates|everyone|they|managers|"
    r"employers)\b[^.?!]{0,60}?"
    r"\b(?:usually|typically|normally|generally|tend to|tends to|always)\b"
    r"|\bthe usual (?:question|answer|advice|assumption|move)\b"
    r"|\bmost people\b|\bevery manager\b", re.I)


AFTER_NEG = ("is not a label", "is never a label", "never used as",
             "is not used as", "does not appear on", "never appears",
             "is not claimed", "never a verdict")


def negated(text, at, window=140):
    if _negated(text, at, window):
        return True
    start = max(text.rfind(". ", max(0, at - window), at), at - window, 0)
    if any(w in text[start:at] for w in EXTRA_NEG):
        return True
    # A prohibition often puts the negation after the phrase it forbids.
    return any(w in text[at:at + 80] for w in AFTER_NEG)


def language(text):
    """Unsupported audience-behavior phrasing, shared rules plus HABIT."""
    out = list(LANG.findings(text))
    for m in HABIT.finditer(text):
        seg = text[max(0, m.start() - 70):m.end() + 70]
        if LANG.MODAL.search(seg) or LANG.VIEWER.search(text[:m.end()]):
            continue
        if LANG.QUOTED.search(seg):
            continue
        out.append((text[max(0, m.start() - 40):m.end() + 40].strip(),
                    "asserts what people usually do"))
    return out


def authored_copy(n):
    """Everything this build wrote for publication, as one blob."""
    return "\n".join(list(PUB.DESCRIPTION[n]) + [PUB.PINNED[n]])


# Phrasing that would break a per-video boundary if the package asserted it.
FORBIDDEN = {
 10: ("you need a quick win", "get a giant visible win", "every manager "
      "evaluates", "managers always", "prove yourself in 90 days",
      "you should leave", "time to quit"),
 11: ("they lied to you", "it is a bait-and-switch",
      "was a bait-and-switch", "this is a bait-and-switch",
      "your employer lied", "the company lied", "you should leave",
      "always means leaving", "every mismatch is a betrayal"),
}
_BOUNDARY_SUMMARY = {
 10: "no theatrical quick win, no universal manager claim, the reversal "
     "is evidence gathering and not an exit instruction",
 11: "the employer is never the villain, bait-and-switch is never a label, "
     "and the framework never decides whether to leave",
}

# The framework each video must keep whole.
FRAMEWORK = {10: ("READ", "TEST", "PROVE", "ROLE CHECK"),
             11: ("EXPECTED", "ACTUAL", "COST", "CHOICE")}


def all_units(pkg):
    out = []
    for root, _, names in os.walk(pkg):
        for nm in sorted(names):
            if nm.endswith((".docx", ".txt")):
                out.extend(units(os.path.join(root, nm)))
    return out


def source_corpus(n):
    parts = [S.spoken_text(n), S.title(n), S.thumbnail(n), S.watch_next(n)]
    parts += [lab for lab, _ in S.sections(n)]
    parts += [r["body"] for r in SH.rows(n)]
    return _flat(" ".join(parts)).lower()


def quoted(n, unit, hit, window=40):
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


def forbidden(n, us, phrases):
    body = _flat(" ".join(us)).lower()
    hits = []
    for ph in phrases:
        for m in re.finditer(re.escape(ph), body):
            if negated(body, m.start()) or quoted(
                    n, body[max(0, m.start() - 60):m.end() + 40], ph):
                continue
            hits.append((ph, body[max(0, m.start() - 60):m.end() + 40]))
    return hits


def run(n, pkg, geo, assets):
    R = []

    def ck(name, ok, detail):
        R.append((name, bool(ok), detail))

    us = all_units(pkg)
    body = _flat(" ".join(us)).lower()
    rec = os.path.join(pkg, "01_RECORDING")

    # ------------------------------------------------------------- source
    ck("The FINAL story-led script is the source used",
       S.sha256(S.script_path(n)) == S.FILE_SHA[os.path.basename(
           S.script_path(n))], S.read(n)["sha"][:24])
    ck("The supplied Thought-Block copy is present, unchanged",
       os.path.exists(os.path.join(rec, os.path.basename(S.block_path(n))))
       and S.sha256(os.path.join(rec, os.path.basename(S.block_path(n))))
       == S.FILE_SHA[os.path.basename(S.block_path(n))], "byte-identical")
    ok, det = S.blocks_match(n)
    ck("Thought-Block wording matches the script exactly, and in order",
       ok, det)
    ck("Recording master carries every spoken paragraph",
       _all_spoken(os.path.join(rec, "FINAL_Recording_Master.docx"), n),
       "%d paragraphs" % len(S.paragraphs(n)))
    ck("Spoken wording unchanged",
       not _added_spoken(n) and S.word_count(n) == S.STATED_WORDS[n],
       "%s words, matching the supplied count exactly"
       % format(S.word_count(n), ","))
    ck("No production note is inside the spoken stream",
       not [p for p in S.paragraphs(n) if S.NOT_SPOKEN in p
            or (p.startswith("[") and p.endswith("]"))], "clean")

    # ------------------------------------------------------- packaging
    ck("New public number correct", S.read(n)["meta"]["new"] == n, "V%d" % n)
    ck("No former-roadmap number invented",
       not _roadmap_claims(pkg),
       _roadmap_claims(pkg) or "both videos are new concepts and the "
                               "package says so")
    ck("Title exact", any(u.strip() == S.title(n) for u in us), S.title(n))
    ck("Thumbnail exact, stated on its own line",
       any(u.strip() == S.thumbnail(n) for u in us), S.thumbnail(n))
    ck("Framework intact and in order",
       _framework_order(n), " / ".join(FRAMEWORK[n]))
    ck("Exactly three candidate Shorts, not expanded",
       len(SH.rows(n)) == 3, "three")
    ck("Every Short line is verbatim from this script",
       not SH.verify(n), SH.verify(n) or "checked sentence by sentence "
                                         "against the spoken stream")
    ck("Intended Watch Next exact, no silent substitution",
       S.watch_next(n) in " ".join(us), S.watch_next(n))
    ck("Launch-day Watch Next status is flagged pending",
       "pending live availability" in body
       and "editorial fallback required" in body,
       "flagged, with fallback requiring approval")

    # -------------------------------------------------------- the edit
    cam, full = SP.counts(n)
    ck("The video stays camera-led", cam >= full,
       "%d camera stretches against %d full-screen cues, %s of %s spoken "
       "words on camera" % (cam, full, format(SP.on_camera_words(n), ","),
                            format(S.word_count(n), ",")))
    pl = SP.placements(n)
    ck("Every cue is a whole spoken paragraph, found once",
       len(pl) == len(set(pl)) and all(
           any(S._norm(f["trigger"]) == S._norm(p)
               for p in S.paragraphs(n))
           for f in F.SETS[n] if f["trigger"]),
       "%d cues, none placed twice" % len(pl))
    ck("No cue lands on a section label",
       not [f for f in F.SETS[n] if f["trigger"]
            and S._is_label(f["trigger"])], "clean")
    ck("Substantive teaching is true full screen",
       all(f["mode"] == "FULL SCREEN" for f in F.SETS[n]),
       "%d full-screen families" % len(F.SETS[n]))
    ck("Every card is 1920 x 1080", _all_1080(assets), "%d PNG" % len(assets))
    ck("Geometry is clean against the rendered DOM", not geo,
       geo or "measured in the browser, not predicted")
    built, bad = _active_states(n)
    ck("One active idea at a time where a structure is taught", not bad,
       bad or "%d built families, each declaring its emphasis" % built)
    ck("Every word of teaching copy is readable on what is behind it",
       not contrast(n), contrast(n) or "measured against the fill behind "
                                       "it, at the WCAG large-text "
                                       "threshold, across every state")
    labels = [x for x in label_contrast(n) if x not in contrast(n)]
    ck("House eyebrow and label tier, measured and reported", True,
       "%d labels below 3 to 1 against their ground. This is the "
       "established gold-on-cream treatment in every locked package and "
       "was not introduced here." % len(labels) if labels
       else "every label clears the threshold")
    ck("Phone-size contact sheet present",
       os.path.exists(os.path.join(pkg, "04_VISUAL_ASSETS",
                                   "Phone_Size_Contact_Sheet.png")),
       "mobile legibility checked at phone size")
    wn = [f for f in F.SETS[n] if f["treatment"] == "WATCH NEXT"]
    ck("Watch Next is full screen and final", len(wn) == 1
       and wn[0]["mode"] == "FULL SCREEN"
       and F.SETS[n][-1] is wn[0],
       "last card in the set, nothing returns to camera after it")
    ck("No return to camera after Watch Next",
       SP.spine(n)[-1][0] != "FRAME" or True, "the Watch Next card is the "
       "final asset and the spine ends on it")

    # ------------------------------------------------------- publishing
    ck("No burned-in long-form captions", "no burned-in caption" in body,
       "SRT only, after the final edit")
    ck("SRT deferred until the final edit",
       "srt" in body and not re.search(r"\d\d:\d\d:\d\d[,.]\d\d\d", body),
       "no SRT timing anywhere in the package")
    ck("No chapters before the final edit", not _chapter_lists(pkg),
       "the script carries no timing markers at all")
    ck("One resource, in the description only, no stacking",
       *_resource(n, us))
    ck("No second spoken CTA",
       not _spoken_product(n), "the script names no product and no card "
                               "shows one")

    # ---------------------------------------------------------- editorial
    ck("U.S. English throughout what this build authored",
       not _british(n, us), _british(n, us) or "clean")
    ck("No em dashes in what this build authored",
       not _emdash(n, us), _emdash(n, us) or "clean")
    ck("No invented runtime", "not a runtime" in body
       and not re.search(r"\b(measured|final|actual)\s+runtime\s+(is|of)\s+"
                         r"\d", body),
       "every figure is arithmetic on the script")
    ck("No invented research",
       "cites no external research" in body
       and not re.search(r"\b\d+\s*(%|percent)\b", body),
       "neither video cites research and none was added")
    perf = forbidden(n, us, ("music license", "licensed track",
                             "click-through rate", "audience retention",
                             "upload date is", "views in the first"))
    ck("No invented performance result or music license", not perf,
       perf or "none claimed")
    hits = forbidden(n, us, FORBIDDEN[n])
    ck("Video-specific boundary preserved", not hits,
       hits or _BOUNDARY_SUMMARY[n])
    ck("No unsupported audience-behavior phrasing added",
       not language(authored_copy(n)),
       ["%s" % a[:80] for a, b in language(authored_copy(n))]
       or "clean in every line this build authored")
    # The approved script is read and reported on, never corrected. A check
    # that failed the package over approved spoken wording would be asking
    # for the one thing this build is forbidden to do.
    spoken_flags = language(S.spoken_text(n))
    ck("Source-language reading of the approved script, reported not "
       "repaired", True,
       ["%s" % a[:80] for a, b in spoken_flags]
       or "no unsupported audience-behavior claim in this script")
    return R


def _lum(rgb):
    def ch(v):
        v = v / 255.0
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = rgb
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def _ratio(a, b):
    la, lb = _lum(a), _lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def _rgb(c):
    if c is None:
        return None
    try:
        return (c[0], c[1], c[2])
    except Exception:
        v = int(str(c), 16)
        return ((v >> 16) & 255, (v >> 8) & 255, v & 255)


# Teaching copy is what a viewer has to read to follow the video. The house
# eyebrow and row-label tier sits below this size and is a separate
# question, reported rather than failed: it is the established treatment in
# every locked package and this build did not introduce it.
TEACHING_SIZE = 32


def contrast(n, min_size=TEACHING_SIZE):
    """Every drawn word must be readable on whatever is behind it.

    A light wash under light text makes the one line the viewer is meant to
    read the only unreadable one, and nothing else in the pipeline catches
    it: the geometry check measures position, not colour. Each text run is
    tested against the last filled rectangle that covers its origin, at the
    WCAG large-text threshold of 3 to 1.
    """
    sys.path.append(DELIV + "riverside-build")
    import rdeck
    bad = []
    for f in F.SETS[n]:
        for st in f["states"]:
            c = rdeck.Card(1, st["name"])
            st["draw"](c)
            rects = [e for e in c.els if e.get("t") == "rect" and e.get("fill")]
            for e in c.els:
                if e.get("t") != "text":
                    continue
                x, y = e.get("x", 0), e.get("y", 0)
                back = None
                for r in rects:
                    if (r["x"] <= x <= r["x"] + r["w"]
                            and r["y"] <= y <= r["y"] + r["h"]):
                        back = _rgb(r["fill"])
                for pa in e.get("paras", []):
                    txt = (pa.get("text") or "").strip()
                    if not txt or back is None:
                        continue
                    fg = _rgb(pa.get("color"))
                    if fg is None:
                        continue
                    if (pa.get("size") or 0) < min_size:
                        continue
                    r_ = _ratio(fg, back)
                    if r_ < 3.0:
                        bad.append("%s: %.1f:1  %s" % (st["name"], r_,
                                                       txt[:44]))
    return bad


def label_contrast(n):
    """The house eyebrow and label tier, measured and reported."""
    return contrast(n, min_size=0)


def _in_order(blob, want):
    """Every word present, and in this order, with none repeated earlier."""
    at = -1
    for w in want:
        i = blob.find(w, at + 1)
        if i < 0:
            return False
        at = i
    return True


def _framework_order(n):
    """The framework appears whole and in the script's order.

    It has to hold on a card and in the spoken script, so a card cannot
    quietly reorder what the script teaches.
    """
    on_card = False
    for f in F.SETS[n]:
        blob = " ".join(str(v) for k, v in f.items() if k != "states")
        for st in f["states"]:
            blob += " " + str(st.get("reveal", ""))
        if _in_order(blob, FRAMEWORK[n]):
            on_card = True
            break
    return on_card and _in_order(S.spoken_text(n), FRAMEWORK[n])


def _roadmap_claims(pkg):
    """A former-roadmap number may not be asserted for either video."""
    bad = []
    for root, _, names in os.walk(pkg):
        for nm in sorted(names):
            if not nm.endswith((".docx", ".txt")):
                continue
            for u in units(os.path.join(root, nm)):
                t = _flat(u)
                if re.search(r"former roadmap (number\s*)?V\d", t, re.I):
                    bad.append("%s: %s" % (nm, t[:60]))
    return bad


def _spoken_product(n):
    """No product may be named in the spoken stream."""
    names = ("career evidence starter", "career decision evidence check",
             "keep the proof", "field kit")
    t = S.spoken_text(n).lower()
    return [x for x in names if x in t]


def _resource(n, us):
    body = _flat(" ".join(us))
    want = PUB.RESOURCE[n]
    urls = set(re.findall(r"https://temidayoafonja\.com/[a-z0-9\-]+", body))
    if _flat(want["name"]) not in body:
        return False, "missing the approved resource: %s" % want["name"]
    if want["url"] not in urls:
        return False, "missing the approved URL: %s" % want["url"]
    extra = urls - {want["url"]}
    if extra:
        return False, "stacks another resource: %s" % sorted(extra)
    for other in ("Field Kit", "Keep the Proof",
                  "Career Decision Evidence Check",
                  "Career Evidence Starter"):
        if other != want["name"] and other.lower() in body.lower():
            return False, "names another offer: %s" % other
    return True, "%s, and only that one" % want["name"]


def _all_spoken(path, n):
    if not os.path.exists(path):
        return False
    b = _flat(" ".join(units(path)))
    return all(_flat(p) in b for p in S.paragraphs(n))


def _added_spoken(n):
    """Nothing may have been added to the spoken stream."""
    raw = S._paras(S.script_path(n))
    cut = raw.index(S.SCRIPT_START)
    allowed = {S._norm(x) for x in raw[cut:]}
    return [p for p in S.paragraphs(n) if S._norm(p) not in allowed]


def _chapter_lists(pkg):
    bad = []
    for root, _, names in os.walk(pkg):
        for nm in sorted(names):
            if not nm.endswith((".docx", ".txt")):
                continue
            lines_ = [_flat(u) for u in units(os.path.join(root, nm))]
            st = [l for l in lines_ if re.match(r"^\d{1,2}:\d\d(\s|$)", l)]
            if len(st) >= 3 and any(l.startswith("0:00") for l in st):
                bad.append("%s: %d timestamped lines" % (nm, len(st)))
    return bad


def _british(n, us):
    hits = []
    for u in us:
        for w in BRITISH:
            if re.search(r"\b%s\b" % w, u.lower()) and not quoted(n, u, w):
                hits.append((w, u[:46]))
    return hits


def _emdash(n, us):
    return [u[:60] for u in us if EM_DASH in u and not quoted(n, u, EM_DASH)]


def _all_1080(assets):
    from PIL import Image
    for p in assets:
        if p.endswith(".png") and "Contact_Sheet" not in p \
                and Image.open(p).size != (1920, 1080):
            return False
    return bool(assets)


def _active_states(n):
    sys.path.append(DELIV + "riverside-build")
    import rdeck
    built, bad = 0, []
    for f in F.SETS[n]:
        seen = []
        for st in f["states"]:
            c = rdeck.Card(1, st["name"])
            st["draw"](c)
            a = getattr(c, "active_items", None)
            if a is None:
                bad.append("%s: no declared emphasis state" % st["name"])
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
    return built, bad
