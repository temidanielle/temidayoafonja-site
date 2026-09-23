# -*- coding: utf-8 -*-
"""Locked sources and manifest authority for the V1-V3 complete-package pilot.

Nothing editorial is decided here. Spoken wording comes from the locked
masters in the V1-V14 final archive. Title, thumbnail, sticky realization,
viewer action, CTA and Watch Next come from the Source-of-Truth Manifest.

The manifest attached to this brief is the PRE-REPAIR copy: it still describes
the V2 and V3 section-label condition as open. The repaired manifest in the
workspace is newer and supersedes it, which is what DATE + PURPOSE controls
means here. The editorial fields are identical in both.
"""
import os, sys, hashlib
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.append(DELIV + "V1-V3_STICKY/build")
sys.path.append(DELIV + "V1-V14_FINAL_ARCHIVE/build")

import st_parse as SP          # the parsed locked masters, labels separated
import st_production as SPR    # cue map, already anchor-verified
import st_shorts as SS         # three verbatim Shorts per video
import st_desc as SD           # description copy, constructed and unapproved
import st_prov as SV           # provenance and boundaries
import st_frames as SF         # slide states

ARCHIVE = DELIV + "V1-V14_FINAL_ARCHIVE/"
LOCKED = {
 n: (ARCHIVE + "_repaired/V%d_FINAL_Sticky_Realization_Recording_Master.docx" % n,
     ARCHIVE + "_repaired/V%d_FINAL_Sticky_Realization_Thought_Blocks.docx" % n)
 for n in (2, 3)}
UP = "/root/.claude/uploads/f121668d-e262-5eb8-9b22-0eaa1006a361/"
LOCKED[1] = (UP + "6b3a6c6c-V1_FINAL_Sticky_Realization_Recording_Master.docx",
             UP + "315ff2f2-V1_FINAL_Sticky_Realization_Thought_Blocks.docx")

VIS = DELIV + "V1-V3_STICKY/V%d/04_VISUAL_ASSETS"

# From the Source-of-Truth Manifest. Carried, not re-derived.
META = {
1: dict(title="How to Change Careers After 10+ Years Without Starting Over",
        thumb="WHAT ACTUALLY TRANSFERS?",
        thinking="I have spent 10, 15 or 20 years building this career. If I "
                 "change direction, what actually comes with me?",
        realization="Your experience does not move as one big block. Some of it "
                    "travels, some belonged to the environment you were in, "
                    "some is real but still needs proof, and some of the new "
                    "context has to be learned.",
        memory="My experience does not move as one block.",
        action="Put your current work beside the destination and separate what "
               "travels, what does not, what can be proved, and what may need "
               "relearning.",
        cta="Career Evidence Starter",
        cta_url="https://temidayoafonja.com/career-evidence-starter",
        watch="Is Your Job Making You Harder to Hire?",
        next_line="Next time the viewer sees a role outside their current "
                  "field, I want them to remember that their experience does "
                  "not move as one block, and then put their current work "
                  "beside that destination and sort it into four columns."),
2: dict(title="Is Your Job Making You Harder to Hire?",
        thumb="HARDER TO HIRE?",
        thinking="I am good at my job and everyone here relies on me, so I "
                 "must be fine. But I cannot explain why without using company "
                 "language.",
        realization="Some of what makes you exceptional here genuinely belongs "
                    "to you, and some of it comes from knowing this "
                    "environment better than almost anyone else. Both are "
                    "valuable. They do not all leave with you.",
        memory="What part of this is me, and what part is my access to this "
               "environment?",
        action="Take one thing people rely on you for, remove the company "
               "language, explain the judgment underneath it, then look for "
               "evidence it works elsewhere.",
        cta="Career Evidence Starter",
        cta_url="https://temidayoafonja.com/career-evidence-starter",
        watch="Before You Quit Your Job, Save This First",
        next_line="Next time the viewer hears we cannot do this without you, I "
                  "want them to remember to ask what part of this is me and "
                  "what part is my access to this environment, and then take "
                  "one thing people rely on them for and strip the company "
                  "language out of it."),
3: dict(title="Before You Quit Your Job, Save This First",
        thumb="YOU CAN’T PROVE IT LATER",
        thinking="I will write all of this down later, before the next "
                 "interview. And I would never take company files anyway.",
        realization="Your evidence has an access problem. The accomplishment "
                    "does not disappear when you leave, but the context that "
                    "makes it easier to explain can.",
        memory="Keep the proof, not the property.",
        action="Before access ends, capture one permitted example: the "
               "problem, what was yours, what changed, and what permitted "
               "evidence supports it.",
        cta="Career Decision Evidence Check",
        cta_url="https://temidayoafonja.com/career-decisions",
        watch="How to Change Careers After 10+ Years Without Starting Over",
        next_line="Next time the viewer starts seriously thinking about "
                  "leaving, I want them to remember keep the proof, not the "
                  "property, and then capture one permitted example before "
                  "their access ends."),
}

VIEWER_EXERCISE = {
1: ("Put your current work beside the destination.",
    ["Write the role you are actually considering at the top. One role, not an "
     "industry.",
     "WHAT TRAVELS. What have you already shown you can do that this role also "
     "needs?",
     "WHAT DOES NOT. What belonged to the place rather than to you? "
     "Relationships, systems, reputation, positional authority.",
     "WHAT CAN I PROVE. Of the travels column, what could another person "
     "actually check?",
     "WHAT MAY NEED RELEARNING. What does the destination context require that "
     "you have not worked in?"],
    "Do not try to make every column look good. You are not trying to win an "
    "argument with yourself."),
2: ("Take one thing people rely on you for.",
    ["Write the sentence the way you would say it at work. Company nouns and "
     "all.",
     "Cross out every company noun: the system names, the acronyms, the "
     "internal process names.",
     "Write what is left as the judgment underneath it. What are you actually "
     "doing?",
     "Name one place that judgment has worked outside this context. Another "
     "function, a client, a former colleague, a different constraint.",
     "If you cannot name one, that is the useful answer, not a failure."],
    "You are not looking for a public brand or a job offer. You are looking for "
    "evidence that the usefulness was not completely trapped inside one "
    "environment."),
3: ("Capture one permitted example before your access ends.",
    ["THE PROBLEM. What was true before you got involved?",
     "WHAT WAS YOURS. What decision, judgment or influence was actually yours?",
     "WHAT CHANGED. What was different afterward?",
     "WHAT PERMITTED EVIDENCE SUPPORTS IT. What are you lawfully allowed to "
     "keep or say outside the company?",
     "Mark anything you cannot verify. That mark is worth more than a "
     "confident number you cannot stand behind."],
    "Keep the proof, not the property. Nothing here asks you to take "
    "confidential information, customer data, proprietary documents or "
    "anything you are not entitled to keep."),
}

def sha256(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def words(n):
    return SP.words(n)

def runtime(n, rate):
    w = words(n)
    return "%d:%02d" % (int(w / rate), round((w / rate % 1) * 60))

def locked_matches_parse(n):
    """The parsed spoken stream must equal the locked file's spoken stream."""
    sys.path.append(DELIV + "V1-V14_FINAL_ARCHIVE/build")
    import ar_parity as AP
    a = " ".join(p for _s, p in SP.spoken(n)).split()
    b = " ".join(AP.spoken(LOCKED[n][0], "sticky", "master")).split()
    return a == b

if __name__ == "__main__":
    for n in (1, 2, 3):
        print("V%d  %d words  %s  locked file matches the parse: %s"
              % (n, words(n), META[n]["thumb"], locked_matches_parse(n)))
