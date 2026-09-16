# -*- coding: utf-8 -*-
"""Regression fixtures for the cue map, from the independent review.

Every defect the review named in the delivered camera, asset and sound maps
is replayed here against the new checks. A check that stays silent on the
delivered defect is decoration, not a check.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sequencing as Q
import locate as L
import recon as R
sys.path.insert(0, "/home/user/temidayoafonja-site/deliverables/"
                   "V4-V11_EDIT_SYNC/build")
import briefs as B

# The eight paragraphs the review listed as hosting more than one family,
# plus the two it called out by name.
DELIVERED_SHARED = [
 (4, "6 THREE THINGS TO WATCH", 1),
 (6, "3 THE FOUR THINGS I READ", 2),
 (6, "8 WHY TITLES CAN MISLEAD YOU", 2),
 (6, "9 THE REVERSE CAN HAPPEN TOO", 2),
 (8, "5 THE IMPORTANT BOUNDARY", 2),
 (8, "16 WATCH NEXT", 1),
 (9, "1 HOOK", 5),
 (10, "5 1 | READ", 4),
]


def replay_shared():
    """The delivered cue table, with no relocation, retirement or subrange."""
    keep_rel, keep_ret, keep_sub = Q.RELOCATE, Q.RETIRE, Q.SUBRANGE
    keep_early = Q.EARLY
    Q.RELOCATE, Q.RETIRE, Q.SUBRANGE, Q.EARLY = {}, {}, {}, {}
    try:
        bad = Q.verify()
    finally:
        Q.RELOCATE, Q.RETIRE, Q.SUBRANGE, Q.EARLY = (keep_rel, keep_ret,
                                                     keep_sub, keep_early)
    return bad


def main():
    fail = 0
    print("SHARED PARAGRAPHS AND END-SCREEN COMPETITION\n")
    bad = replay_shared()
    for n, lab, para in DELIVERED_SHARED:
        want = "V%d section %s paragraph %d" % (n, lab.split(" ", 1)[0],
                                                para)
        hit = [b for b in bad if b.startswith(want)]
        alt = [b for b in bad if ("V%d:" % n) in b and "end screen" in b]
        if hit or (lab == "16 WATCH NEXT" and alt):
            print("  FIRES  V%-2d %-32s para %d" % (n, lab[:32], para))
        else:
            print("  HELD   V%-2d %-32s para %d  <-- not caught"
                  % (n, lab[:32], para))
            fail += 1
    print("\n  delivered cue table raises %d findings in total" % len(bad))

    print("\nEARLY CUTAWAYS THAT HAD NO MAPPED STATE\n")
    for n, what in ((11, "NEW_V11_FS_00_ACCEPTED_AND_DOING"),
                    (8, "NEW_V8_FS_00_ACCESS_UNAVAILABLE"),
                    (4, "NEW_V4_FS_03_WHAT_THE_WORK_TAUGHT")):
        rows = Q.anchors(n)
        hook = [r for r in rows if r["section"] == 0 and r["key"] == what]
        if hook:
            r = hook[0]
            print("  MAPPED V%-2d %-38s section 1 paragraph %d"
                  % (n, what, r["para"] + 1))
        else:
            print("  MISSING V%-2d %s" % (n, what))
            fail += 1
    delivered = {r["key"] for r in Q.ANCHORS[11]}
    if "NEW_V11_FS_00_ACCEPTED_AND_DOING" in delivered:
        print("  unexpected: the delivered set already had the V11 card")
        fail += 1

    print("\nNARRATIVE OCCURRENCE AND SOUND WORD\n")
    cases = [(4, "S5", "STORY LOOP PAYOFF", 14),
             (10, "S4", "THE REVERSAL", 11)]
    for n, key, purpose, want in cases:
        bt = [x for x in B.read(n)["beats"] if key in x["head"]][0]
        first = L.occurrences(n, L.remap(n, bt["trigger"]))
        got = L.resolve(n, bt["trigger"], bt["head"])
        ok = got["section"] + 1 == want
        drift = first and first[0][0] + 1 != want
        print("  %-6s V%-2d first match section %-2d -> resolved section "
              "%-2d %s" % (key, n, first[0][0] + 1 if first else 0,
                           got["section"] + 1, "OK" if ok else "WRONG"))
        if not ok:
            fail += 1
        if not drift:
            print("         the first-match fixture no longer differs; "
                  "re-point it")
            fail += 1
    for n, key, word in ((4, "S2", "OWNERSHIP"), (4, "S4", "STILL MINE")):
        bt = [x for x in B.read(n)["beats"] if key in x["head"]][0]
        a = L.accent_location(n, bt)
        e = L.resolve(n, bt["trigger"], bt["head"])
        if not a or a["word"] != word:
            print("  %-6s V%-2d accent word not recovered from the brief"
                  % (key, n))
            fail += 1
        else:
            same = (a["section"] == e["section"] and a["para"] == e["para"])
            print("  %-6s V%-2d scene entry para %d, accent word %s in "
                  "para %d%s" % (key, n, e["para"] + 1, word, a["para"] + 1,
                                 "" if not same else "  (same paragraph)"))

    print("\nSTALE SECTION NUMBERS\n")
    stale = [(4, "THREE THINGS TO WATCH", 6), (4, "A SIMPLE EXAMPLE", 7),
             (4, "TRY THIS ON ONE TASK", 12),
             (5, "WHAT THIS CAN LOOK LIKE", 5),
             (5, "ASK FOR DEVELOPMENT, NOT ONLY MORE WORK", 8),
             (5, "SET A REVIEW POINT", 11), (5, "STORY LOOP PAYOFF", 14),
             (7, "FOUR THINGS I LOOK FOR", 6),
             (7, "A CONVERSATION YOU CAN HAVE", 9),
             (7, "STORY LOOP PAYOFF", 14), (9, "THE FOUR QUESTIONS", 5),
             (9, "THINK OF IT LIKE SORTING", 10),
             (9, "HOW TO TALK ABOUT THE GAP", 14),
             (9, "STORY LOOP PAYOFF", 16),
             (10, "THE CONVERSATION I WOULD HAVE", 8),
             (10, "THE FIRST-90-DAYS READ", 12),
             (11, "THE FOUR COST LENSES", 7), (11, "4 | CHOICE", 8),
             (11, "TAKEAWAY VALUE", 12)]
    wrong = 0
    for n, lab, want in stale:
        labs = [l for l, _ in R.sections(n)]
        got = labs.index(lab) + 1 if lab in labs else 0
        if got != want:
            print("  V%-2d %-40s expected %d, reconciled says %d"
                  % (n, lab, want, got))
            wrong += 1
    print("  all %d section numbers the review listed now agree: %s"
          % (len(stale), "yes" if not wrong else "NO, %d differ" % wrong))
    fail += wrong

    print("\nfindings not caught: %d" % fail)
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
