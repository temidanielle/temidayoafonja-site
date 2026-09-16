# -*- coding: utf-8 -*-
"""Hand adjudication of every line the automatic re-review left in doubt.

The automatic pass narrowed 153 flagged lines to 20 it could not place.
Coverage scoring is a weak signal on a short line, so each of those 20 was
read beside the reconciled passage and decided by hand. Each decision
records the supporting section, as the brief requires for anything
retained.

VERDICTS
  SUMMARY   a faithful compression of a passage still in the script
  EVIDENCE  a supported excerpt the script does not read aloud in full
  OBSOLETE  no passage and no approved evidence supports it, so the copy
            has to change
"""

SUMMARY, EVIDENCE, OBSOLETE = "SUMMARY", "EVIDENCE", "OBSOLETE"

# (video, family, line) -> (verdict, supporting section, note)
DECISIONS = {
 (4, "NEW_V4_FS_02_INEFFICIENT_AND_DEVELOPMENTAL",
  "Slow, repetitive, sometimes wrong."): (
    OBSOLETE, None,
    "No passage describes the old work this way any more. The reconciled "
    "hook says those hours were not always wasted and names mistakes and "
    "patterns, not slowness."),
 (4, "NEW_V4_FS_03_WHAT_THE_WORK_TAUGHT",
  "Why the eleventh one is different"): (
    OBSOLETE, None,
    "The ten-bad-examples image is gone. The script now says the person "
    "must see enough examples to learn the pattern."),
 (5, "NEW_V5_FS_02_NOT_ALIGNED",
  "Your value to the current role and your value to your future are not a"): (
    SUMMARY, "HOOK",
    "Compresses: how can I be valuable enough to carry all of this, but "
    "not the person you develop?"),
 (5, "NEW_V5_FS_05_INDISPENSABLE_AND_LESS_PORTABLE",
  "Fewer people can operate without you."): (
    SUMMARY, "WHAT THIS CAN LOOK LIKE",
    "Compresses: more things that only you know how to do."),
 (5, "NEW_V5_FS_05_INDISPENSABLE_AND_LESS_PORTABLE",
  "Your experience becomes tied to the internal system."): (
    OBSOLETE, None,
    "The reconciled V5 never names an internal system, so that half of "
    "the line has no support. Portability itself does survive in V5 and "
    "this record previously said otherwise: A SIMPLE EXAMPLE says you can "
    "become harder to replace there without becoming much easier to hire "
    "somewhere else, and WHEN TO BUILD OPTIONS says to get clearer about "
    "what parts of your experience travel. The line is replaced because "
    "of the internal system, not because the idea left the video."),
 (5, "NEW_V5_FS_10_CTA",
  "If not, usefulness may be the reason you are stuck."): (
    SUMMARY, "CLOSE",
    "Compresses: if not, being useful may be part of why you feel stuck."),
 (5, "NEW_V5_FS_10_CTA", "More portable."): (
    OBSOLETE, None,
    "The CLOSE asks whether the work is making you more capable, more "
    "visible, or more useful somewhere else. Portable is not the word it "
    "uses, and the card quoted a word rather than compressing the "
    "sentence. This record previously said no portability language "
    "remains in V5, which is wrong: A SIMPLE EXAMPLE and WHEN TO BUILD "
    "OPTIONS both carry the idea. The word is what was replaced."),
 (6, "NEW_V6_FS_03_THE_SAMPLE",
  "Read for this research. A bounded sample, not the labor market."): (
    EVIDENCE, "THE FOUR THINGS I READ",
    "Research-boundary note. Supported by: I reviewed 15 job postings from "
    "11 employers for this research, and by the story loop's in this "
    "sample. The brief names this case explicitly."),
 (6, "NEW_V6_FS_04_THREE_QUESTIONS", "Can I prove relevant evidence?"): (
    SUMMARY, "THE FOUR THINGS I READ",
    "Compresses: can I prove that I have done something close to it?"),
 (6, "NEW_V6_FS_06_POSTING_WALKTHROUGH",
  "Access is unusually specific. The role may be far more hands-on than t"): (
    SUMMARY, "3 | PROOF",
    "Compresses: even Microsoft Access, and that last detail suggests the "
    "job may be more hands-on than the title implies."),
 (6, "NEW_V6_FS_15_CEILING",
  "Of the 15 postings read for this research. Not a claim about the marke"): (
    EVIDENCE, "THE FOUR THINGS I READ",
    "Research-boundary note carrying the sample denominator. Supported by "
    "the same passage and by the approved capture record."),
 (6, "NEW_V6_FS_15_CEILING",
  "The range on this posting, revealed after the four postures."): (
    SUMMARY, "THE REVERSE CAN HAPPEN TOO",
    "Reveal-order note, not a claim. The reconciled reverse case does "
    "disclose the published range after the postures."),
 (7, "NEW_V7_FS_06_EVIDENCE_FOR_WHICH_ROLE",
  "The problem is not that you have done nothing."): (
    SUMMARY, "WHAT PEOPLE OFTEN TRY",
    "Compresses: that can help your reputation, but it does not "
    "automatically show that you are ready for the next kind of work."),
 (8, "NEW_V8_FS_01_MEMORY_NOT_PROOF", "You just cannot prove it cleanly."): (
    SUMMARY, "HOOK",
    "Compresses: you remember doing good work, but was the improvement 27 "
    "percent or 37 percent, and what was the baseline?"),
 (8, "NEW_V8_FS_11_A_FACTUAL_RECORD", "An award nomination every month."): (
    OBSOLETE, None,
    "No award or nomination appears anywhere in the reconciled V8."),
 (9, "NEW_V9_FS_04_DEMONSTRATED_NOT_CLAIMED",
  "Capability the next context can use."): (
    SUMMARY, "1 | WHAT TRAVELS",
    "Compresses: something you have already shown you can do, and the new "
    "place can actually use it."),
 (9, "NEW_V9_FS_05_TIED_TO_THE_OLD_CONTEXT", "Tied to the old context."): (
    SUMMARY, "2 | WHAT DOES NOT",
    "Compresses: then ask what belonged to the old place."),
 (9, "NEW_V9_FS_06_WHAT_CAN_ANOTHER_PERSON_SEE", "What was broken?"): (
    SUMMARY, "3 | WHAT CAN I PROVE",
    "Compresses: what was wrong before?"),
 (9, "NEW_V9_FS_10_BOUNDARY",
  "YOU MAKE A BETTER DECISION WHEN YOU KNOW WHAT YOU ARE ASKING AN EMPLOY"): (
    SUMMARY, "REAL LIMITS STILL MATTER",
    "Compresses the section's point that none of the real limits disappear "
    "because you can explain your experience well."),
 (10, "NEW_V10_FS_05_TWO_SENTENCES", "One assumes. One asks."): (
    SUMMARY, "WHAT READ DOES NOT MEAN",
    "Compresses the contrast between the two quoted sentences, both of "
    "which are still spoken verbatim in that section."),
}


def decide(video, key, line):
    return DECISIONS.get((video, key, line))


def obsolete_families():
    out = {}
    for (v, k, line), (verdict, sec, why) in DECISIONS.items():
        if verdict == OBSOLETE:
            out.setdefault((v, k), []).append(line)
    return out


if __name__ == "__main__":
    tally = {}
    for v in DECISIONS.values():
        tally[v[0]] = tally.get(v[0], 0) + 1
    print("hand-adjudicated lines: %d" % len(DECISIONS))
    for k in (SUMMARY, EVIDENCE, OBSOLETE):
        print("   %-9s %d" % (k, tally.get(k, 0)))
    print("\nfamilies whose copy genuinely has to change:")
    for (v, k), lines in sorted(obsolete_families().items()):
        print("   V%-2d %-44s %d line(s)" % (v, k, len(lines)))
