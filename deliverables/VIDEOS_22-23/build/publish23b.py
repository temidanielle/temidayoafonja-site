# -*- coding: utf-8 -*-
"""Publishing materials for the new V22 and V23 scripts.

No chapters and no SRT: both are made after the final edit from real export
timing. The only resource URL is the one the script speaks, on the route the
V4 to V21 system already locked.
"""
import os, sys
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.append(DELIV + "VIDEOS_4-21_STORY_LED/build")
sys.path.append(DELIV + "VIDEOS_4-21_CORRECTED_RUNTIME/build")

import masters23b as M
from content421 import ROUTES, PLAYLIST

RESOURCE = {22: None, 23: "Career Evidence Starter"}

WATCH_NEXT = {
 22: [(14, "V22 reads the destination. This one reads your own side of the "
           "same question, which is the natural next move for a viewer who "
           "has just decoded a posting."),
      (21, "V22 ends on stated gates a candidate has to meet. This one is "
           "the whole video about what you have to relearn, so it continues "
           "the last teaching beat rather than repeating the method.")],
 23: [(8, "V23 reconstructs one accomplishment into evidence. This one is "
          "the same evidence problem for work that had no precedent, so the "
          "viewer arrives with the four lines already in hand."),
      (10, "V23 ends on proof another person can trust. This one is about "
           "capturing that proof while you still have access to it.")],
}
FUTURE = {22: (23, "Once V23 is publicly live it becomes the strongest Watch "
                   "Next for V22: the destination read, then the evidence "
                   "read. No spoken wording was changed to manufacture the "
                   "connection."),
          23: None}

KEYWORDS = {
 22: ["how to read a job description", "decode a job description",
      "job description verbs", "what a job title really means",
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
    if n == 22:
        L = ["Senior Divisional Strategy Consultant, Governance. The bottom "
             "of the published range was $61,500, and one of the required "
             "qualifications was the ability to accept direction and "
             "feedback.",
             "",
             "That is why I do not start with the title anymore.",
             "",
             "I read 15 postings from 11 employers for this research, and "
             "this is the four-part read I use: Problem. Authority. Proof. "
             "Real gap.",
             "",
             "It will not tell you who gets hired, whether the authority on "
             "paper exists in practice, or whether a manager would flex. "
             "Reading better does not guarantee a better outcome. It gives "
             "you a cleaner read.",
             "",
             "Take one job description you are actually considering, write "
             "the four lines, and find the strongest verb in the posting."]
    else:
        L = ["“Led a cross-functional transformation that improved "
             "on-time delivery by 18 percent.”",
             "",
             "It has a verb, scope and a number, and a stranger still cannot "
             "tell what you actually did.",
             "",
             "Four lines rebuild it: Problem before. What was mine to "
             "decide. Judgment. Proof and how I know.",
             "",
             "Good proof does not make your role sound bigger than it was. "
             "It makes what you actually carried easier to judge. And where "
             "an employer still requires domain knowledge, a credential, "
             "regulated experience or direct exposure, that stays true. "
             "Change the emphasis, not the truth.",
             "",
             "The worked example in this video is illustrative, not a real "
             "employer or client."]
    L += ["", "WATCH NEXT"]
    for dest, _ in WATCH_NEXT[n]:
        L.append(titles[dest])
    L += ["", "PLAYLIST", PLAYLIST]
    if RESOURCE[n]:
        L += ["", "RESOURCE",
              "%s  %s" % (RESOURCE[n], ROUTES[RESOURCE[n]])]
    L += ["", "[ EDITOR: paste the real video and playlist URLs here after "
              "upload. No URL in this package is a live link except the "
              "resource route above, which is already locked. ]"]
    return L


def pinned(n):
    if n == 22:
        return ("Take one job description you are actually considering. Do "
                "not start with the title. Write four lines: Problem. "
                "Authority. Proof. Real gap. Then find the strongest verb in "
                "the posting. That verb may tell you more about the job than "
                "the title does.")
    return ("Pick one accomplishment you remember clearly. Not your best "
            "one. Just one. Write four lines: Problem before. What was mine "
            "to decide. Judgment. Proof and how I know. The second line "
            "usually takes the longest.")


UPLOAD_QA = [
 "Title is exact and matches the script header.",
 "Thumbnail wording is exact. Artwork is approved separately and is not "
 "part of this package.",
 "No superseded title or thumbnail appears anywhere in the upload.",
 "Description carries no invented URL. Video and playlist links are pasted "
 "after upload.",
 "Chapters are created from the final export timing. The scripts carry no "
 "timing markers to copy.",
 "SRT generated in Riverside after the final edit and checked against the "
 "final export.",
 "No burned-in captions in the long-form upload.",
 "Watch Next card is full screen and final. Nothing returns to camera "
 "after it.",
 "Every synthetic figure that appears on screen carries its label. (V23)",
 "No employer comparison appears in the V23 edit: the script no longer "
 "makes one.",
 "Audio loudness, music balance and picture quality checked on the final "
 "export.",
]
