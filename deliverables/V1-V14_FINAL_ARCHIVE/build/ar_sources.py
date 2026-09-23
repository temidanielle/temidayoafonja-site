# -*- coding: utf-8 -*-
"""The approved source for every one of the fourteen videos.

Nothing here is regenerated. Each entry points at the file that was approved,
and the archive copies it byte for byte.

V1 to V3   the FINAL Sticky Realization uploads of September 23, 2026
V4 to V11  the reconciled masters and thought blocks in V4-V11_SYNC
V12        the locked V12-V14 pack
V13, V14   the public-employer anonymization patch, which supersedes the
           locked versions of those two
"""
import os

DELIV = "/home/user/temidayoafonja-site/deliverables/"
UP = "/root/.claude/uploads/f121668d-e262-5eb8-9b22-0eaa1006a361/"
EXTRACT = ("/tmp/claude-0/-home-user-temidayoafonja-site/"
           "f121668d-e262-5eb8-9b22-0eaa1006a361/scratchpad/arch/src/")

# n: (master path, blocks path, shape, provenance of the source)
SRC = {
1: (UP + "6b3a6c6c-V1_FINAL_Sticky_Realization_Recording_Master.docx",
    UP + "315ff2f2-V1_FINAL_Sticky_Realization_Thought_Blocks.docx", "sticky",
    "Uploaded September 23, 2026. Supersedes the published V1, the earlier "
    "refreshed master and all earlier thought blocks."),
2: (UP + "83f978da-V2_FINAL_Sticky_Realization_Recording_Master.docx",
    UP + "56807557-V2_FINAL_Sticky_Realization_Thought_Blocks.docx", "sticky",
    "Uploaded September 23, 2026. Supersedes the published V2, the earlier "
    "refreshed master and all earlier thought blocks."),
3: (UP + "0e3eb62b-V3_FINAL_Sticky_Realization_Recording_Master.docx",
    UP + "4b6a1e14-V3_FINAL_Sticky_Realization_Thought_Blocks.docx", "sticky",
    "Uploaded September 23, 2026. Supersedes the published V3, the earlier "
    "refreshed master and all earlier thought blocks."),
}
for n in range(4, 12):
    SRC[n] = (DELIV + "V4-V11_SYNC/INDIVIDUAL/Recording_Masters/"
                      "NEW_V%02d_Reconciled_Recording_Master.docx" % n,
              DELIV + "V4-V11_SYNC/INDIVIDUAL/Thought_Blocks/"
                      "NEW_V%02d_Thought_Block_Recording_Copy.docx" % n,
              "sync",
              "Reconciled master of September 19, 2026, named as the newest "
              "approved spoken master in the V4-V14 sticky-realization "
              "reconciliation. LOCKED AS-IS.")
SRC[12] = (EXTRACT + "locked/V12/V12_FINAL_RECORDING_MASTER.docx",
           EXTRACT + "locked/V12/V12_FINAL_THOUGHT_BLOCKS.docx", "built",
           "From the committed YOUTUBE_V12-V14_FINAL_LOCKED_PACK.zip. "
           "LOCKED AS-IS.")
for n in (13, 14):
    SRC[n] = (EXTRACT + "anon/CORRECTED_PUBLIC_ASSETS/V%d/V%d_FINAL_RECORDING_MASTER.docx" % (n, n),
              EXTRACT + "anon/CORRECTED_PUBLIC_ASSETS/V%d/V%d_FINAL_THOUGHT_BLOCKS.docx" % (n, n),
              "built",
              "From the committed V13-V14_PUBLIC_EMPLOYER_ANONYMIZATION_PATCH.zip, "
              "which supersedes the locked version of this video. LOCKED AS-IS.")

# The two authorized formatting repairs of September 23, 2026. V2 and V3 now
# point at the repaired files. The uploads they were made from are recorded
# below so the repair stays auditable: the only difference is that the section
# label became its own paragraph.
REPAIRED_DIR = os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), "V1-V14_FINAL_ARCHIVE", "_repaired")
if not os.path.isdir(REPAIRED_DIR):
    REPAIRED_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "_repaired")

PRE_REPAIR = {}
for _n in (2, 3):
    PRE_REPAIR[_n] = (SRC[_n][0], SRC[_n][1])
    SRC[_n] = (os.path.normpath(os.path.join(
                   REPAIRED_DIR,
                   "V%d_FINAL_Sticky_Realization_Recording_Master.docx" % _n)),
               os.path.normpath(os.path.join(
                   REPAIRED_DIR,
                   "V%d_FINAL_Sticky_Realization_Thought_Blocks.docx" % _n)),
               "sticky",
               SRC[_n][3] + " The fused section label was separated on "
               "September 23, 2026 as an authorized formatting-only repair. No "
               "spoken word changed.")

REPAIR_NOTE = ("RESOLVED SEPTEMBER 23, 2026 \u2014 FORMATTING ONLY. NO SPOKEN "
               "WORDING CHANGED.")

ZIP_SOURCES = [
 ("V12", DELIV + "V12-V14_LOCKED/YOUTUBE_V12-V14_FINAL_LOCKED_PACK.zip"),
 ("V13 and V14", DELIV + "V13-V14_ANON/V13-V14_PUBLIC_EMPLOYER_ANONYMIZATION_PATCH.zip"),
]

TITLES = {
1: ("How to Change Careers After 10+ Years Without Starting Over",
    "WHAT ACTUALLY TRANSFERS?"),
2: ("Is Your Job Making You Harder to Hire?", "HARDER TO HIRE?"),
3: ("Before You Quit Your Job, Save This First", "YOU CAN’T PROVE IT LATER"),
4: ("AI Took the Task. Who Gets the Experience?", "WHO LEARNS NOW?"),
5: ("If Your Company Needs You but Won’t Grow You", "USEFUL. STILL STUCK."),
6: ("Decode a Job Description in 10 Minutes", "IGNORE THE TITLE"),
7: ("I’ve Seen Who Gets the Bigger Role and Why", "THEY CHOSE SOMEONE ELSE"),
8: ("What Disappears When Your Work Access Ends", "YOU CAN’T PROVE IT LATER"),
9: ("Transferable Skills Advice Is Missing Something", "NOT EVERYTHING TRAVELS"),
10: ("Your First 90 Days in a New Job: What Really Matters",
     "DON’T SPEND YOUR FIRST 90 DAYS PROVING YOURSELF"),
11: ("What to Do When Your New Job Isn’t the Job You Accepted",
     "THIS ISN’T THE JOB"),
12: ("How to Turn One Accomplishment Into Proof in 10 Minutes",
     "CAN YOU PROVE IT?"),
13: ("Which Parts of Your Experience Actually Transfer to Another Industry?",
     "SAME WORDS. DIFFERENT WORK."),
14: ("I Read Two Similar Jobs. They Wanted Different Proof",
     "SAME WORK. DIFFERENT REQUIREMENTS."),
}

def missing():
    bad = []
    for n, (m, b, _s, _p) in sorted(SRC.items()):
        if not os.path.exists(m):
            bad.append("V%d master missing: %s" % (n, m))
        if not os.path.exists(b):
            bad.append("V%d blocks missing: %s" % (n, b))
    return bad

if __name__ == "__main__":
    bad = missing()
    print("sources missing:", bad or "none, all 28 files present")
