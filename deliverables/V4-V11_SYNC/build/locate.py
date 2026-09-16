# -*- coding: utf-8 -*-
"""Resolve every cue to one location, by section AND narrative purpose.

Two defects in the previous pass are fixed here at the root.

FIRST, section numbers. The sound map numbered sections against the
early-edit intake while the camera map used the reconciled script. The
reconciled script has an extra INTRODUCTION section in six of the eight
videos, so every section after the insertion point was off by one in
exactly those six. Everything now numbers against the reconciled script.

SECOND, occurrence choice. Taking the first textual match is not
disambiguation. A story-loop payoff and the opening question that set it up
share wording on purpose, and the payoff is the later one. Each beat names
its own treatment, and where that treatment names a real section the
occurrence inside that section is the one meant.
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, "/home/user/temidayoafonja-site/deliverables/"
                   "V4-V11_EDIT_SYNC/build")
import recon as R
import briefs as B


def norm(t):
    return R.S._norm(t).lower()


# Triggers the approved V4 opening replacement moved.
#
# The brief was written against the old opening, so two of its exact
# triggers no longer exist in the reconciled script. The review called
# this out: S1's anchor contained "those three hours". Both are remapped
# to the approved wording rather than left dangling, and the remap is
# recorded here so the change is visible rather than silent.
TRIGGER_REMAP = {
 (4, "AI can do in 30 seconds what used to take someone three hours."):
   "Imagine a task that takes someone hours.",
 (4, "But those three hours were not always wasted."):
   "But those hours were not always wasted.",
}


def remap(n, trigger):
    return TRIGGER_REMAP.get((n, (trigger or "").strip()), trigger)


def occurrences(n, trigger):
    """Every reconciled paragraph containing this wording."""
    q = norm(trigger)
    out = []
    for li, (lab, ps) in enumerate(R.sections(n)):
        for pi, p in enumerate(ps):
            if q in norm(p):
                out.append((li, lab, pi, p))
    return out


def _purpose(head):
    """The section a beat names, if it names one."""
    t = re.sub(r"^\d+\.\s*", "", head or "").strip()
    t = re.sub(r"\s*\|\s*S\d.*$", "", t).strip()
    return t


def resolve(n, trigger, head=None):
    """One location: (section index, label, paragraph index, note)."""
    trigger = remap(n, trigger)
    hits = occurrences(n, trigger)
    if not hits:
        return None
    if len(hits) == 1:
        li, lab, pi, p = hits[0]
        return dict(section=li, label=lab, para=pi, paragraph=p,
                    trigger=trigger, occurrences=1,
                    note="appears once in the reconciled script")
    want = _purpose(head)
    labs = [lab for lab, _ in R.sections(n)]
    if want and want in labs:
        for li, lab, pi, p in hits:
            if lab == want:
                return dict(section=li, label=lab, para=pi, paragraph=p,
                            trigger=trigger, occurrences=len(hits),
                            note="appears %d times; this is the occurrence "
                                 "in %s, which is the treatment this beat "
                                 "names" % (len(hits), lab))
    li, lab, pi, p = hits[0]
    return dict(section=li, label=lab, para=pi, paragraph=p,
                trigger=trigger, occurrences=len(hits),
                note="appears %d times; the brief's treatment does not name "
                     "a section, so the first occurrence is used"
                     % len(hits))


# The exact word a sound accent lands on, where the brief's own direction
# names one. A scene-entry cue and the accent word are different things and
# are reported separately.
ACCENT_WORD = re.compile(
    r"\baccent (?:at|on)\s+([A-Z][A-Z \-]{2,30})|"
    r"\bSound on\s+([A-Z][A-Z \-]{2,30})", re.M)


def accent_word(beat):
    """The exact word the brief says the accent falls on, if it says."""
    for t in [beat.get("head", "")] + list(beat.get("note", [])):
        m = ACCENT_WORD.search(t or "")
        if m:
            return (m.group(1) or m.group(2)).strip().rstrip(".,")
    return None


def accent_location(n, beat):
    """Where the accent word actually sits, separate from scene entry."""
    w = accent_word(beat)
    if not w:
        return None
    hits = occurrences(n, w)
    if not hits:
        return dict(word=w, section=None, label=None, para=None,
                    note="the brief names this accent word but it does not "
                         "appear in the reconciled script; place it by ear")
    entry = resolve(n, beat.get("trigger"), beat.get("head"))
    if entry:
        same = [h for h in hits if h[0] == entry["section"]]
        if same:
            li, lab, pi, p = same[0]
            return dict(word=w, section=li, label=lab, para=pi,
                        note="inside the same section as the scene entry")
    li, lab, pi, p = hits[0]
    return dict(word=w, section=li, label=lab, para=pi,
                note="first occurrence of the accent word")


if __name__ == "__main__":
    print("REGRESSION FIXTURES FROM THE INDEPENDENT REVIEW\n")
    b4 = B.read(4)
    s5 = [x for x in b4["beats"] if "S5" in x["head"]][0]
    r = resolve(4, s5["trigger"], s5["head"])
    print("  V4 S5  %-28s -> section %d %s"
          % (_purpose(s5["head"]), r["section"] + 1, r["label"]))
    b10 = B.read(10)
    s4 = [x for x in b10["beats"] if "S4" in x["head"]][0]
    r = resolve(10, s4["trigger"], s4["head"])
    print("  V10 S4 %-28s -> section %d %s"
          % (_purpose(s4["head"])[:28], r["section"] + 1, r["label"]))
    for tag, n, key in (("V4 S2", 4, "S2"), ("V4 S4", 4, "S4")):
        bt = [x for x in B.read(n)["beats"] if key in x["head"]][0]
        a = accent_location(n, bt)
        e = resolve(n, bt["trigger"], bt["head"])
        print("  %-6s scene entry: section %d %s, para %d"
              % (tag, e["section"] + 1, e["label"], e["para"] + 1))
        print("         accent word: %s"
              % (("%s, section %d %s, para %d"
                  % (a["word"], a["section"] + 1, a["label"], a["para"] + 1))
                 if a and a["section"] is not None else
                 ("%s, not located" % a["word"] if a else "none named")))
    print("\n  section numbering now against the reconciled script")
    for n in R.VIDEOS:
        labs = [l for l, _ in R.sections(n)]
        print("     V%-3d %2d sections, INTRODUCTION at %s"
              % (n, len(labs),
                 (labs.index(R.INTRO_LABEL) + 1) if R.INTRO_LABEL in labs
                 else "none"))
