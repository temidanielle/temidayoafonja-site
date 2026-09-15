# -*- coding: utf-8 -*-
"""Publishing materials for NEW V10 and V11.

One approved resource per description and no stacking: the handoff names
exactly one for each video and nothing else appears. The resource lives in
the description only. Neither script speaks a product ask, so none was added
to the spoken stream or to any card.

Runtime, chapters, SRT timing, upload date, public URLs and performance are
all decided after the final edit and none is invented here.
"""
import os, sys
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.append(DELIV + "VIDEOS_22-23/build")
import v1011 as S
import frames1011 as F
import shorts1011 as SH
from docs1011 import (base_doc, title_block, h, kv, para, callout, sub,
                      caption, table, bullets, footer_note, mono, hr, head,
                      _wrap, EYEBROW, GOLD as GOLD_LABEL, DIM as DIM_LABEL)

PLAYLIST = "Capability Formation: career pivots and internal moves"
PLAYLIST_URL = "[PASTE PLAYLIST URL AFTER UPLOAD]"
VIDEO_URL = "[PASTE VIDEO URL AFTER UPLOAD]"

WATCH = "\U0001F3A5 Watch next"
PLAY = "\U0001F4FA Playlist"

# One relevant resource each, exactly as the handoff assigns them.
RESOURCE = {
 10: dict(emoji="\U0001F9F0", label="Free evidence starter",
          name="Career Evidence Starter",
          blurb="Turn one accomplishment into proof you can use in a "
                "performance review, interview, internal move, or career "
                "pivot.",
          url="https://temidayoafonja.com/career-evidence-starter"),
 11: dict(emoji="\U0001F9ED", label="Free career decision check",
          name="Career Decision Evidence Check",
          blurb="Use this free check to look at what your current work is "
                "building, what may be narrowing, and what deserves a "
                "closer decision.",
          url="https://temidayoafonja.com/career-decisions"),
}

DESCRIPTION = {
 10: ["You finally got the job. Maybe it is a bigger role. Maybe you "
      "changed companies. Maybe you changed industries. And now you feel "
      "this pressure to prove they made the right decision.",
      "You can be experienced and still be new to the context. Those two "
      "things can be true at the same time.",
      "Three things to figure out in your first 90 days: READ. TEST. "
      "PROVE. Then one more line: ROLE CHECK.",
      "This video does not ask you to produce a giant visible win by day "
      "90. Some work has a long learning curve. Some is regulated. Some "
      "senior roles require context before intervention. The evidence does "
      "not have to be dramatic. It needs to be real."],
 11: ["You accepted one job. Then you started doing another. Maybe the "
      "title is the same. Maybe the salary is the same. But the work "
      "itself feels materially different from what you thought you were "
      "saying yes to.",
      "Before you call it a bait-and-switch, slow the read down. Roles "
      "change. Priorities move. Managers inherit new problems. "
      "Organizations reorganize.",
      "Four questions for reading role drift: EXPECTED. ACTUAL. COST. "
      "CHOICE.",
      "This framework does not tell you whether to leave. Sometimes the "
      "right choice is to stay. Your constraints are real, and the goal is "
      "to make the decision from the job that actually exists."],
}

PINNED = {
 10: "By the end of your first 90 days, try to finish these: I came in "
     "assuming X, I learned Y. The part of my previous experience that "
     "helped most was X. The part I had to relearn was Y. One decision I "
     "can now make with more confidence is X.",
 11: "Write two columns. EXPECTED: what you reasonably believed you were "
     "accepting, based on the description, the interviews and the offer. "
     "ACTUAL: what the recurring pattern is now. Then read the cost across "
     "capability, evidence, compensation and life.",
}

KEYWORDS = {
 10: ["first 90 days new job", "starting a new job experienced",
      "new role onboarding plan", "experienced but new to the company",
      "what to do in a new job", "90 day plan career"],
 11: ["job is not what i was told", "role drift at work",
      "job description does not match the job", "new job different from offer",
      "should i stay in this role", "renegotiate scope at work"],
}

UPLOAD_QA = [
 "Title is exact and matches the FINAL script header.",
 "Thumbnail wording is exact. Artwork is approved separately and is not "
 "part of this package.",
 "The new public number is correct and no former-roadmap number appears "
 "anywhere: this is a new concept.",
 "Description carries one resource, and only one. No other product "
 "appears.",
 "The resource URL is exact. Video and playlist links are pasted after "
 "upload.",
 "INTENDED WATCH NEXT destination confirmed publicly live before upload. "
 "If it is not, flag EDITORIAL FALLBACK REQUIRED and do not substitute "
 "one.",
 "End-screen destination matches the Watch Next card that actually cut.",
 "Chapters created from the final export timing. The script carries no "
 "timing markers to copy.",
 "SRT generated in Riverside after the final edit and checked against the "
 "final export.",
 "No burned-in captions in the long-form upload.",
 "Watch Next card is full screen and final. Nothing returns to camera "
 "after it.",
 "Audio loudness, music balance and picture quality checked on the final "
 "export.",
]


def lines(n):
    """The copy-ready description, in order."""
    r = RESOURCE[n]
    out = list(DESCRIPTION[n])
    out += ["", r["emoji"] + " " + r["label"], r["name"], r["blurb"],
            r["url"]]
    out += ["", WATCH, S.watch_next(n), VIDEO_URL]
    out += ["", PLAY, PLAYLIST, PLAYLIST_URL]
    return out


def materials(n, path, stamp):
    d = base_doc()
    title_block(d, EYEBROW, S.title(n), "Publishing materials")
    kv(d, "New public number", "V%d" % n)
    kv(d, "Former roadmap number", "None. This is a new concept.")
    kv(d, "Final title", S.title(n))
    kv(d, "Final thumbnail wording", S.thumbnail(n))
    kv(d, "Playlist", PLAYLIST)
    kv(d, "Generated", stamp)
    callout(d, "CHAPTERS: create after final edit using actual export "
               "timing.  SRT: generate in Riverside after final edit and "
               "verify against the final export. Neither exists in this "
               "package, and this script carries no timing markers to copy.")

    h(d, "Watch Next")
    para(d, "INTENDED WATCH NEXT", size=9, bold=True, color=GOLD_LABEL,
         after=2)
    para(d, S.watch_next(n), size=13, bold=True, after=8)
    caption(d, "Named on the script's final full-screen card and preserved "
               "exactly. It was not replaced.")
    para(d, "LAUNCH-DAY END-SCREEN STATUS", size=9, bold=True,
         color=GOLD_LABEL, before=8, after=2)
    para(d, "PENDING LIVE AVAILABILITY until verified before upload.",
         size=13, bold=True, after=8)
    callout(d, "If the intended destination is not publicly live at publish "
               "time, flag EDITORIAL FALLBACK REQUIRED for Temidayo and "
               "ChatGPT approval. Do not rewrite the script to accommodate "
               "availability, and do not invent a fallback destination.")

    h(d, "Description")
    caption(d, "Copy-ready. The resource block is the one approved for this "
               "video and is the only offer in it.")
    r = RESOURCE[n]
    for line in lines(n):
        if not line:
            para(d, "", after=2)
        elif line in (WATCH, PLAY) or line.startswith(r["emoji"]):
            para(d, line, size=10.5, bold=True, before=4, after=2)
        elif line.startswith("http") or line.startswith("[PASTE"):
            para(d, line, size=10.5, color=GOLD_LABEL, after=6)
        else:
            para(d, line, size=10.5, after=6)
    para(d, "[ EDITOR: paste the real video and playlist URLs here after "
            "upload. No video URL in this package is a live link. The "
            "resource URL above is the approved destination. ]", size=9,
         color=DIM_LABEL, before=6)

    h(d, "Resource block")
    kv(d, "Resource", r["name"])
    kv(d, "Label", r["emoji"] + " " + r["label"])
    kv(d, "URL", r["url"])
    caption(d, "One relevant resource, and only one. No other product "
               "appears in this description. The resource and Watch Next "
               "are kept apart: optional deeper help is not the next "
               "content path.")

    h(d, "Pinned comment")
    para(d, PINNED[n], size=10.5)

    h(d, "CTA notes")
    bullets(d, [
      "The closing tool card is full screen.",
      "The script speaks no product ask, so none was added. The resource "
      "appears in the description only.",
      "There is one brief Subscribe cue after value lands. It is an edit "
      "cue, not a spoken line, and no spoken wording was added for it.",
    ])

    h(d, "Search language")
    para(d, "Discovery input only. None of this changes the title, the "
            "thumbnail or a spoken line.", size=10)
    bullets(d, KEYWORDS[n], size=10)

    h(d, "Shorts")
    table(d, ["#", "Stop scroll", "About"],
          [["%d" % r_["num"], r_["stop"][0], "0:%02d" % r_["secs"]]
           for r_ in SH.rows(n)], widths=[0.35, 4.4, 0.9], size=8.5)
    caption(d, "Three candidates, as a selection bank. The bank was not "
               "expanded, and not all three have to be published.")

    h(d, "Upload checklist")
    bullets(d, UPLOAD_QA, size=10)
    footer_note(d, "No runtime, chapter timing, SRT timing, upload date, "
                   "public URL or performance figure appears in this "
                   "package. Every one of them is decided after the edit.")
    d.save(path)
    return path
