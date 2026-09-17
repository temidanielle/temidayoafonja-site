# -*- coding: utf-8 -*-
"""Regression fixtures for the one-clear-action and standalone rules.

Every compound ending and every dangling opening named in the third review
is replayed against the checks. A check that stays silent on the delivered
wording is decoration, and the all-pass result it produces is worthless.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shortsync as SH
import recon as R

# The endings as delivered, each with the number of audience actions the
# review counted in it.
COMPOUND = [
 ("V5 S1", 2, u"Ask for one piece of work that builds a new decision, a "
              u"new problem, or new proof, and set a date to review what "
              u"changed."),
 ("V7 S3", 2, u"Pick one kind of next-level work you want to be trusted "
              u"with. Ask what decision, problem, stakeholder, or risk "
              u"would let you practice it where someone can see the "
              u"result."),
 ("V8 S1", 2, u"Pick one project and write five things in your own words: "
              u"baseline, scope, the decision that was yours, the result, "
              u"and how the result was judged. Then ask what you are "
              u"allowed to keep or say outside the company."),
 ("V9 S3", 2, u"Take one job you are thinking about. Make four columns: "
              u"TRAVELS. DOES NOT TRAVEL. PROOF. RELEARN."),
 ("V10 S2", 4, u"Read the context. Test what traveled. Build new proof. "
               u"And read the role back."),
 ("V11 S3", 2, u"Name one real cost. Then choose one next action: "
               u"clarify, negotiate, test for a defined period, or begin "
               u"planning another option."),
]

# Endings that are one task in two steps, and must not be flagged.
SINGLE = [
 ("V8 S1 corrected", u"Pick one project and write five things in your own "
                     u"words: baseline, scope, the decision that was "
                     u"yours, the result, and how the result was judged."),
 ("V8 S3", u"Once a month, take ten minutes and write down: What changed? "
           u"What was mine? What was hard? What proof do I have? What "
           u"would I be allowed to say outside this company?"),
 ("V11 S1", u"If those two versions are different, name the difference "
            u"before you normalize it."),
 ("V6 S1", u"But do not only ask, “Is this senior?” Ask, "
           u"“What is this person actually trusted to decide?”"),
 ("V6 S3", u"So if a title confuses you, do not automatically skip the "
           u"job. Read the work."),
]

# Openings as delivered, each pointing at something not yet said.
DANGLING = [
 (10, 1, u"And now you feel this pressure to prove they made the right "
         u"decision."),
 (10, 3, u"Around this point, I would have a very simple conversation "
         u"with your manager."),
 (11, 3, u"What does the difference actually cost you? Not every mismatch "
         u"deserves the same response."),
]


def main():
    fail = 0
    print("COMPOUND ENDINGS, REPLAYED\n")
    for tag, want, text in COMPOUND:
        got = SH.actions(R.S._norm(text))
        ok = len(got) > 1
        print("  %-16s counted %d %-28s %s"
              % (tag, len(got), "(" + ", ".join(got) + ")",
                 "FIRES" if ok else "HELD  <-- missed"))
        fail += 0 if ok else 1

    print("\nONE TASK IN TWO STEPS, WHICH MUST NOT BE FLAGGED\n")
    for tag, text in SINGLE:
        got = SH.actions(R.S._norm(text))
        ok = len(got) <= 1
        print("  %-16s counted %d %-28s %s"
              % (tag, len(got), "(" + ", ".join(got) + ")",
                 "allowed" if ok else "FLAGGED  <-- too blunt"))
        fail += 0 if ok else 1

    print("\nDANGLING OPENINGS, REPLAYED\n")
    for n, num, text in DANGLING:
        keep = SH.SHORTS[(n, num)]["stop"]
        SH.SHORTS[(n, num)]["stop"] = [text]
        bad = [b for b in SH.audit(n)
               if b.startswith("V%d S%d " % (n, num)) and "STANDALONE" in b]
        SH.SHORTS[(n, num)]["stop"] = keep
        print("  V%-2d S%d  %s" % (n, num, "FIRES" if bad else
                                   "HELD  <-- missed"))
        fail += 0 if bad else 1

    print("\nTHE BANK AS IT STANDS\n")
    over = []
    for n in R.VIDEOS:
        for r in SH.rows(n):
            a = SH.actions(R.S._norm(" ".join(
                SH.SHORTS[(n, r["num"])]["ask"])))
            if len(a) > 1 or r["words"] >= 150:
                over.append((n, r["num"], len(a), r["words"]))
    print("  24 candidates, %d with more than one action or 150 words or "
          "more" % len(over))
    fail += len(over)
    bad = [b for n in R.VIDEOS for b in SH.audit(n)]
    print("  editorial audit failures: %d" % len(bad))
    fail += len(bad)
    print("\nfindings not caught: %d" % fail)
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
