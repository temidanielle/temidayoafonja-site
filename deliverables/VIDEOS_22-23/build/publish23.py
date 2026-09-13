# -*- coding: utf-8 -*-
"""Publishing materials and Watch Next recommendations.

No chapters and no SRT are created here: both are made after the final edit
from real export timing. The only resource URL that appears is the one the
script speaks, and it is the route already locked by the V4 to V21 system.
"""
import os, sys
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.append(DELIV + "VIDEOS_4-21_STORY_LED/build")
sys.path.append(DELIV + "VIDEOS_4-21_CORRECTED_RUNTIME/build")

import masters23 as M
import shorts23 as SH
from content421 import ROUTES, PLAYLIST

RESOURCE = {22: None, 23: "Career Evidence Starter"}

# Two existing V4 to V21 destinations per video, with the reason each one is
# a real continuation rather than a related topic. V23 may not be public when
# V22 launches, so it is named only as a future option.
WATCH_NEXT = {
 22: [(14, "V22 reads the destination. This one reads your own side of the "
           "same question, which is the natural next move for a viewer who "
           "has just decoded a posting."),
      (21, "V22 ends on stated gates that a candidate has to meet. This one "
           "is the whole video about what you have to relearn, so it "
           "continues the last teaching beat rather than repeating the "
           "method.")],
 23: [(8, "V23 reconstructs one accomplishment into evidence. This one is "
          "the same evidence problem for work that had no precedent, so the "
          "viewer arrives with the four lines already in hand."),
      (10, "V23 ends on proof that survives scrutiny. This one is about "
           "capturing that proof while you still have access to it, which "
           "is the practical next step.")],
}

FUTURE = {22: (23, "Once V23 is live it becomes the strongest Watch Next for "
                   "V22: the destination read, then the evidence read."),
          23: None}

KEYWORDS = {
 22: ["how to read a job description", "decode a job description",
      "job description authority verbs", "what a job title really means",
      "job posting salary range", "career pivot job description",
      "internal move job posting", "reading job requirements"],
 23: ["how to write an accomplishment", "career proof",
      "resume accomplishment examples", "how to quantify accomplishments",
      "what was mine to decide", "career evidence", "proof of impact at work",
      "accomplishment statement"],
}


def watch_next_titles():
    import masters_sl
    return {n: masters_sl.title(n) for n in range(4, 22)}


def description(n, titles):
    L = []
    if n == 22:
        L += ["Four authority-sounding words in a title, and a published "
              "floor of $61,500.",
              "",
              "In September 2026 I read fifteen job postings from eleven "
              "employers and worked out where to look in a posting to answer "
              "three different questions: could I do this work, can I prove "
              "relevant evidence, and do I meet the stated gates.",
              "",
              "The method is four things. Problem. Authority. Proof. Real "
              "gap.",
              "",
              "This will not tell you who gets hired, and reading a posting "
              "better does not improve your odds by itself. It improves "
              "your aim.",
              "",
              "Take one job description you are actually considering, run it "
              "through the four questions, and tell me in the comments what "
              "the verb said and whether it matched the title.",
              ]
    else:
        L += ["“Led a cross-functional transformation that improved "
              "on-time delivery by eighteen percent.”",
              "",
              "That sentence has a verb, scope and a number, and it proves "
              "almost nothing. A stranger still cannot tell what you "
              "decided, what was hard about it, or where the number came "
              "from.",
              "",
              "Four lines fix it. Problem before. What was mine to decide. "
              "Judgment. Proof and how I know.",
              "",
              "Good proof does not make your role sound bigger than it was. "
              "It makes what you actually carried easier to judge.",
              "",
              "The worked example in this video is illustrative, not a real "
              "employer or client.",
              ]
    L += ["", "WATCH NEXT"]
    for dest, why in WATCH_NEXT[n]:
        L.append("%s" % titles[dest])
    L += ["", "PLAYLIST", PLAYLIST]
    res = RESOURCE[n]
    if res:
        L += ["", "RESOURCE", "%s  %s" % (res, ROUTES[res])]
    L += ["", "[ EDITOR: paste the real video and playlist URLs here after "
              "upload. No URL in this package is a live link except the "
              "resource route above, which is already locked. ]"]
    return L


def pinned(n):
    if n == 22:
        return ("Take one job description you are actually considering and "
                "run it through four questions: Problem. Authority. Proof. "
                "Real gap. Then find the verb, and tell me what it said and "
                "whether it matched the title. I read these.")
    return ("Pick one thing you did, not your best thing, and write four "
            "lines: Problem before. What was mine to decide. Judgment. "
            "Proof and how I know. The second line usually takes the "
            "longest. That is the point.")


UPLOAD_QA = [
 "Title is exact, under 50 characters, and matches the script header.",
 "Thumbnail wording is exact. Artwork is approved separately and is not "
 "part of this package.",
 "Description carries no invented URL. Video and playlist links are pasted "
 "after upload.",
 "Chapters are created from the final export timing, not from the "
 "navigation markers in the script.",
 "SRT generated in Riverside after the final edit and checked against the "
 "final export.",
 "No burned-in captions in the long-form upload.",
 "Watch Next card is full screen and final. Nothing returns to camera "
 "after it.",
 "End screen destination matches the Watch Next card that was actually cut.",
 "Every synthetic figure that appears on screen carries its label. (V23)",
 "No employer name, logo, URL or identifying styling in the anonymized "
 "comparison. (V23)",
 "Audio loudness, music balance and picture quality checked on the final "
 "export.",
]
