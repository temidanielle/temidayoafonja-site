# -*- coding: utf-8 -*-
"""The reconciled V4 to V11 spoken source.

The September 16 early-edit intake carries the current BEAST MODE body but
omits six previously approved topic-specific introductions. This module
restores them, and nothing else.

WHAT IS RESTORED
Only the exact approved intro passages, taken verbatim from the September 16
recovery reference. The BEAST MODE hook, story loop, teaching, examples,
frameworks, activities, outcomes, boundaries and Watch Next are untouched,
as are the V6 public employer substitution and the three spoken-framework
derivative repairs.

WHERE IT GOES, AND WHY THAT BOUNDARY
For all six videos the recovery reference's preceding source passage ends
the last paragraph of the HOOK, and its named next section exists in the
current master with the BEAST MODE STORY LOOP sitting between the two. The
recovery reference anticipates exactly this and says to retain the story
loop and identify the boundary. So the intro is restored after the STORY
LOOP and immediately before that named section, giving the intended order:

    recognition and tension  ->  early value  ->  introduction  ->  teaching

V6 and V8 intentionally have no personal introduction and receive none.

WORD COUNTING METHOD
Whitespace-delimited tokens of the spoken stream only. Section labels,
block labels, document headers, recording direction and any bracketed
production note are excluded before counting. The same method is used for
the master and for the thought-block copy, so the two are comparable.
"""
import os, re, sys, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.insert(0, DELIV + "V4-V11_EDIT_SYNC/build")
import src916 as S

RECOVERY = os.path.join(OUT, "_source", "files",
                        "V4-V11_Approved_Natural_Intro_Recovery_2026-09-16.txt")
UPLOAD_SHA = "80c4b3655cda395aae1114ac2ad9521962c84bc38a335f6714dee754ee0ca57e"
RECOVERY_SHA = None            # filled by verify()

VIDEOS = S.VIDEOS
INTRO_LABEL = "INTRODUCTION"
# Videos that carry a personal introduction. V6 and V8 intentionally do not.
HAS_INTRO = (4, 5, 7, 9, 10, 11)

# The section each intro is restored immediately before, from the recovery
# reference's NEXT SOURCE SECTION field.
BEFORE = {4: "THE PROBLEM",
          5: "THE TRAP",
          7: "WHAT HAPPENS BEFORE THE TITLE",
          9: "WHY TRANSFERABLE-SKILLS ADVICE HELPS",
          10: "WHY THIS FEELS STRANGE WHEN YOU ARE EXPERIENCED",
          11: "1 | EXPECTED"}

# The recovery reference's PRECEDING SOURCE PASSAGE, used to prove the
# boundary rather than assume it.
PRECEDING = {
 4: "Because we still need experienced people later. And somehow, they "
    "have to become experienced.",
 5: "That is the problem I want to unpack, because being needed and being "
    "developed are not the same thing.",
 7: "So if you keep getting told you are doing great but someone else "
    "keeps getting the bigger opportunity, “work harder” may be "
    "the wrong diagnosis.",
 9: "Because changing industries without starting over does not mean "
    "pretending you have nothing left to learn.",
 10: "And before the 90 days are over, I want you to check one more thing: "
     "Is this actually the job I thought I accepted?",
 11: "By the end of this video, you should be able to tell whether you are "
     "still adjusting, whether the role has drifted and needs a "
     "conversation, or whether the job has changed enough that you need to "
     "make a bigger decision.",
}

_INTRO = {}


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h.update(b)
    return h.hexdigest()


def intros():
    """Parse the exact approved passages out of the recovery reference."""
    if _INTRO:
        return _INTRO
    txt = open(RECOVERY, encoding="utf-8").read().splitlines()
    n = None
    grab = False
    for line in txt:
        t = line.rstrip()
        m = re.match(r"^NEW PUBLIC V(\d+)\s*$", t)
        if m:
            n = int(m.group(1))
            continue
        if t == "EXACT INTRO START":
            grab = True
            _INTRO[n] = []
            continue
        if t == "EXACT INTRO END":
            grab = False
            continue
        if grab and t.strip():
            _INTRO[n].append(t.strip())
    return _INTRO


def sections(n):
    """The reconciled sections, with the approved intro restored in place."""
    base = S.sections(n)
    if n not in HAS_INTRO:
        return list(base)
    want = BEFORE[n]
    labs = [l for l, _ in base]
    if want not in labs:
        raise SystemExit("V%d: section %r not in the current master"
                         % (n, want))
    at = labs.index(want)
    out = list(base[:at])
    out.append((INTRO_LABEL, list(intros()[n])))
    out += list(base[at:])
    return out


def paragraphs(n):
    return [p for _, ps in sections(n) for p in ps]


def spoken_text(n):
    return "\n".join(paragraphs(n))


def word_count(n):
    """Whitespace-delimited tokens of the spoken stream only."""
    return len(spoken_text(n).split())


def intro_paragraphs(n):
    return list(intros()[n]) if n in HAS_INTRO else []


def boundary(n):
    """Where the intro was inserted, for the log."""
    if n not in HAS_INTRO:
        return None
    base = S.sections(n)
    labs = [l for l, _ in base]
    at = labs.index(BEFORE[n])
    return dict(after=labs[at - 1], before=BEFORE[n], index=at,
                paragraphs=len(intros()[n]),
                words=len(" ".join(intros()[n]).split()))


def verify():
    """Prove the boundary and the restoration rather than assume them."""
    global RECOVERY_SHA
    RECOVERY_SHA = sha256(RECOVERY)
    out = []

    def ck(name, ok, detail=""):
        out.append((name, bool(ok), detail))

    I = intros()
    ck("Six approved intros parsed from the recovery reference",
       sorted(I) == list(HAS_INTRO), "V%s" % ", V".join(str(x)
                                                        for x in sorted(I)))
    for n in HAS_INTRO:
        ck("V%d intro is absent from the intake, as the reference states"
           % n,
           all(S._norm(p).lower() not in S._norm(S.spoken_text(n)).lower()
               for p in I[n]), "%d paragraphs" % len(I[n]))
        q = S._norm(PRECEDING[n]).lower()
        hook = S.sections(n)[0]
        ck("V%d preceding source passage ends the hook" % n,
           S._norm(hook[1][-1]).lower().endswith(q), hook[0])
        labs = [l for l, _ in S.sections(n)]
        at = labs.index(BEFORE[n])
        ck("V%d story loop sits between the hook and %s"
           % (n, BEFORE[n]), labs[at - 1] == "STORY LOOP", labs[at - 1])
    for n in VIDEOS:
        base = [S._norm(p) for p in S.paragraphs(n)]
        now = [S._norm(p) for p in paragraphs(n)]
        added = [p for p in now if p not in base]
        want = [S._norm(p) for p in intro_paragraphs(n)]
        ck("V%d adds only the approved intro paragraphs" % n,
           added == want, "%d added" % len(added))
        ck("V%d keeps every BEAST MODE paragraph" % n,
           all(p in now for p in base), "%d preserved" % len(base))
    for n in (6, 8):
        ck("V%d has no personal intro, intentionally" % n,
           n not in HAS_INTRO, "none restored")
    ck("V6 public employer substitution preserved",
       "GiveDirectly" not in spoken_text(6)
       and "A global nonprofit was hiring a Director of Global Talent "
           "Acquisition" in spoken_text(6), "anonymous")
    for n, w in ((4, "BEFORE AI. WITH AI. STILL MINE."),
                 (6, "PROBLEM. AUTHORITY. PROOF. REAL GAP."),
                 (9, "TRAVELS. DOES NOT TRAVEL. PROOF. RELEARN.")):
        ck("V%d spoken framework words retained" % n,
           S._norm(w) in S._norm(spoken_text(n)), w)
    return out


if __name__ == "__main__":
    rows = verify()
    bad = [r for r in rows if not r[1]]
    for nm, ok, det in rows:
        if not ok:
            print("FAIL  %s  %s" % (nm, det))
    print("source reconciliation checks: %d of %d passed"
          % (len(rows) - len(bad), len(rows)))
    print("\n%-5s %8s %8s %7s  %s" % ("", "intake", "reconciled", "added",
                                      "intro boundary"))
    for n in VIDEOS:
        b = boundary(n)
        print("V%-4d %8d %10d %7d  %s"
              % (n, S.word_count(n), word_count(n),
                 word_count(n) - S.word_count(n),
                 ("after %s, before %s" % (b["after"], b["before"]))
                 if b else "no personal intro, intentionally"))
