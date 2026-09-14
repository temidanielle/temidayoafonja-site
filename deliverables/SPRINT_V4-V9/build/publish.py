# -*- coding: utf-8 -*-
"""Publishing materials, evidence notes and the source hierarchy."""
import os, sys
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.append(DELIV + "VIDEOS_4-21_CORRECTED_RUNTIME/build")
import sprint as S
import frames as F
import sshorts as SH
from sdocs import (base_doc, title_block, h, kv, para, callout, sub, caption,
                   table, bullets, footer_note, mono, hr, head, _wrap,
                   EYEBROW, GOLD as GOLD_LABEL, DIM as DIM_LABEL)
from content421 import PLAYLIST
import descsrc as DS

# The previously authored descriptions were superseded by the approved
# revised package of September 14 and are not kept here: a stale copy
# beside the real one is a trap. See descsrc.py.
PINNED = {
 4: "Take one task AI now helps you with and write three columns: Before "
    "AI. With AI. Still mine. If the third column is rich, good. If it is "
    "almost empty, ask where the learning will come from next.",
 5: "If your company keeps proving how much it needs you, ask one more "
    "question: is it also helping you become more capable, more visible, or "
    "more portable?",
 6: "Take one job description you are actually considering. Do not start "
    "with the title. Write four lines: Problem. Authority. Proof. Real gap. "
    "Then find the strongest verb in the posting.",
 7: "Write down the last three times you were trusted with something bigger "
    "than your normal role. For each one: what problem was I trusted with, "
    "what decision was mine, who saw me handle it, and what changed because "
    "of it. Then look for the missing line.",
 8: "Once a month, take ten minutes and write down what changed, what was "
    "mine, what was hard, what evidence I have, and what I would be allowed "
    "to say outside the company. Keep the proof, not the property.",
 9: "Take one target role and make four columns: Travels. Does not travel. "
    "Proof. Relearn. Do not try to make every line land in the first "
    "column. The goal is accuracy.",
}

KEYWORDS = {
 4: ["ai and career development", "what ai does to junior work",
     "learning when ai does the task", "ai and professional judgment",
     "developmental experience at work", "ai career impact"],
 5: ["needed but not promoted", "no growth at work", "stuck but valued",
     "career development at work", "asking for developmental work",
     "internal move career growth"],
 6: ["how to read a job description", "decode a job description",
     "job description verbs", "what a job title really means",
     "job posting salary range", "internal move job posting"],
 7: ["why i did not get promoted", "who gets the bigger role",
     "career sponsorship at work", "readiness for larger scope",
     "overlooked at work", "visible proof at work"],
 8: ["career evidence before layoff", "what to save before you leave a job",
     "proving your work after you leave", "career records",
     "layoff preparation evidence", "keep the proof not the property"],
 9: ["transferable skills", "do skills transfer between industries",
     "changing industries", "what transfers career change",
     "career pivot without starting over", "relearning in a new industry"],
}

UPLOAD_QA = [
 "Title is exact and matches the FINAL sprint script header.",
 "Thumbnail wording is exact. Artwork is approved separately and is not "
 "part of this package.",
 "Both numbers are correct wherever the video is labeled: the new public "
 "number and the former roadmap number.",
 "Description carries no invented URL. Video and playlist links are pasted "
 "after upload.",
 "INTENDED WATCH NEXT destination confirmed publicly live before upload. If "
 "it is not, flag EDITORIAL FALLBACK REQUIRED and do not substitute one.",
 "End screen destination matches the Watch Next card that was actually cut.",
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


def materials(n, path, stamp):
    d = base_doc()
    title_block(d, EYEBROW, S.title(n), "Publishing materials")
    kv(d, "New public number", "V%d" % n)
    kv(d, "Former roadmap number", "V%d" % S.NUMBERS[n])
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
    caption(d, "Spoken in the FINAL sprint script and preserved exactly. It "
               "was not replaced.")
    para(d, "LAUNCH-DAY END-SCREEN STATUS", size=9, bold=True,
         color=GOLD_LABEL, before=8, after=2)
    para(d, "PENDING LIVE AVAILABILITY until verified before upload.",
         size=13, bold=True, after=8)
    callout(d, "If the intended destination is not publicly live at publish "
               "time, flag EDITORIAL FALLBACK REQUIRED for Temidayo and "
               "ChatGPT approval. Do not rewrite the script to accommodate "
               "availability, and do not invent a fallback destination.")

    h(d, "Description")
    caption(d, "Copy-ready, from the approved revised description package "
               "of September 14, 2026. Reproduced exactly: wording, emojis, "
               "resource name and URL are not edited here.")
    blk = DS.block(n)
    for line in DS.lines(n):
        if not line:
            para(d, "", after=2)
        elif line[:1] in DS.EMOJI or line in (DS.WATCH, DS.PLAYLIST):
            para(d, line, size=10.5, bold=True, before=4, after=2)
        elif line.startswith("http") or line.startswith("[PASTE"):
            para(d, line, size=10.5, color=GOLD_LABEL, after=6)
        else:
            para(d, line, size=10.5, after=6)
    para(d, "[ EDITOR: paste the real video and playlist URLs here after "
            "upload. No URL in this package is a live link. The resource "
            "URL above is the approved destination and is left as written. ]",
         size=9, color=DIM_LABEL, before=6)

    h(d, "Resource block")
    if blk["resource"]:
        r = blk["resource"]
        kv(d, "Resource", r["name"])
        kv(d, "Label", r["emoji"] + " " + r["label"])
        kv(d, "URL", r["url"])
        caption(d, "One relevant resource, and only one. No other product "
                   "appears in this description.")
    else:
        para(d, "No offer or resource block, intentionally.", size=11,
             bold=True)
        caption(d, blk["note"])

    h(d, "Pinned comment")
    para(d, PINNED[n], size=10.5)

    h(d, "CTA notes")
    bullets(d, [
      "The CTA card is full screen.",
      "There is one spoken ask and it is the script's own. No second CTA "
      "was added and no product CTA appears.",
      "The script names no resource, so no resource is spoken. The "
      "description carries one, and it is the approved one.",
      "The resource and Watch Next are kept apart. They do different jobs: "
      "the resource is optional deeper help, Watch Next is the next "
      "content path.",
    ])

    h(d, "Search language")
    para(d, "Discovery input only. None of this changes the title, the "
            "thumbnail or a spoken line.", size=10)
    bullets(d, KEYWORDS[n], size=10)

    h(d, "Shorts")
    table(d, ["#", "Stop scroll", "About"],
          [["%d" % r["num"], r["hook"], "0:%02d" % r["secs"]]
           for r in SH.rows(n)], widths=[0.35, 4.4, 0.9], size=8.5)
    caption(d, "Three candidates, as supplied. The bank was not expanded, "
               "and not all three have to be published.")

    h(d, "Upload checklist")
    bullets(d, UPLOAD_QA, size=10)
    footer_note(d, "No runtime, public URL, upload date, thumbnail result, "
                   "retention figure, music license, chapter time or SRT "
                   "time is invented anywhere in this package.")
    d.save(path)
    return path
