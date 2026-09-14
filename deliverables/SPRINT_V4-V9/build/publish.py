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

DESCRIPTION = {
 4: ["The first draft used to be yours. The first analysis used to be "
     "yours. It was messy and slow, and doing it taught you what good "
     "looked like.",
     "",
     "Now AI does the first pass in seconds. That is not the problem. The "
     "question is what replaces the learning that used to come with the "
     "task.",
     "",
     "Three things to watch: exposure, ownership, feedback.",
     "",
     "Different jobs will answer this differently. In some work AI may "
     "increase learning. In regulated work human review may remain "
     "essential. In others the task may truly disappear. This video does "
     "not claim one outcome. It says the learning path should not be "
     "treated as automatic."],
 5: ["They call you when something breaks. They ask you to train the new "
     "person. Then a bigger opportunity opens and your name is not on it.",
     "",
     "Being needed and being developed are not the same thing. Your value "
     "to the current role and your value to your future are not always "
     "aligned, and that does not mean anyone is plotting against you.",
     "",
     "This video is about the difference between dependence and "
     "development, what to ask for instead of a promotion, and what to do "
     "when the answer is still no."],
 6: ["Senior Divisional Strategy Consultant, Governance. The bottom of the "
     "published range was $61,500, and one of the required qualifications "
     "was the ability to accept direction and feedback.",
     "",
     "That is why I do not start with the title anymore.",
     "",
     "I read 15 postings from 11 employers for this research. The read is "
     "four things: Problem. Authority. Proof. Real gap.",
     "",
     "It will not tell you who gets hired, whether the authority on paper "
     "exists in practice, or whether a manager would flex. Reading better "
     "does not guarantee a better outcome. It gives you a cleaner read."],
 7: ["I have sat in rooms where two people were both capable, both "
     "respected, and both doing good work. Then a bigger role opened, and "
     "the difference was not always who worked harder.",
     "",
     "Four things tend to matter: visible proof, judgment, trust, and "
     "sponsorship or access.",
     "",
     "That is not a formula, and this is not a video about working harder. "
     "Organizations are not clean systems. Politics, bias, timing, budget "
     "and manager behavior all shape who gets the shot. The point of "
     "reading the situation is to separate what you can build, what you "
     "can ask for, and what the organization may not be willing to give."],
 8: ["The day your access ends, your memory is still yours. Your work may "
     "not be. The dashboard is gone. The project folder is gone. And six "
     "months later somebody asks what exactly changed because of your "
     "work.",
     "",
     "Keep the proof. Not the property.",
     "",
     "This is not about taking company files. It is about keeping a lawful "
     "record of your own contribution: the baseline, the scope, the "
     "decision, the result, and how you know the result was real.",
     "",
     "Ten minutes a month, in your own words, while you are still "
     "employed."],
 9: ["When people talk about changing industries, the usual question is "
     "what skills transfer. It sounds sensible, and I think it is "
     "incomplete.",
     "",
     "Four questions instead: What travels? What does not? What can I "
     "prove? What must I relearn?",
     "",
     "This is not an argument that nothing transfers. It is an argument "
     "for accuracy. An employer may still prefer direct experience. A "
     "credential may be non-negotiable. Bias may affect how adjacent "
     "experience is read. None of that disappears because you can explain "
     "your capability well, and you make a better decision when you know "
     "exactly what you are asking the next employer to believe."],
}

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
    for line in DESCRIPTION[n]:
        para(d, line, size=10.5, after=6)
    para(d, "", after=4)
    para(d, "WATCH NEXT", size=9, bold=True, after=2)
    para(d, S.watch_next(n), size=10.5, after=6)
    para(d, "PLAYLIST", size=9, bold=True, after=2)
    para(d, PLAYLIST, size=10.5, after=6)
    para(d, "[ EDITOR: paste the real video and playlist URLs here after "
            "upload. No URL in this package is a live link. ]", size=9,
         color=DIM_LABEL)

    h(d, "Pinned comment")
    para(d, PINNED[n], size=10.5)

    h(d, "CTA notes")
    bullets(d, [
      "The CTA card is full screen.",
      "There is one spoken ask and it is the script's own. No second CTA "
      "was added and no product CTA appears.",
      "No resource URL appears in this package: the script names none.",
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
