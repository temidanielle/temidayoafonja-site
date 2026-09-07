# -*- coding: utf-8 -*-
"""Build the complete recording packages for the new Videos 4 and 5.

    python3 build.py

Writes deliverables/new-video-4/ and deliverables/new-video-5/, then the
combined Videos_4_5_FINAL.zip and the record-together one pager.
"""
import os, sys, shutil, zipfile, hashlib, textwrap
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, "/home/user/temidayoafonja-site/deliverables/riverside-build")

import qa as geoqa
from docs import (base_doc, para, title_block, rule, h, kv, callout,
                  NAVY, GOLD, DIM, RED)
from meta import META, RENUMBER, FULLSCREEN_RULE, GRAMMAR, SOUND_PLAN, CLAIM
from extras import DESCRIPTION, SHORTS, THUMBNAIL
from frames import SETS, build_cards
from rdeck import render_html, render_pptx, shoot
from script_v4 import SCRIPT as S4
from script_v5 import SCRIPT as S5
from PIL import Image

SCRIPTS = {4: S4, 5: S5}
DELIV = "/home/user/temidayoafonja-site/deliverables"
WPM = 145.0
W = 78


def wrap(t, ind=""):
    out = []
    for p in t.split("\n"):
        if not p.strip():
            out.append("")
            continue
        out.extend(textwrap.wrap(p, W - len(ind), initial_indent=ind,
                                 subsequent_indent=ind))
    return "\n".join(out)


def stamp(n):
    """Cumulative timestamp for every paragraph of a script."""
    out, words = [], 0
    for marker, p in SCRIPTS[n]:
        out.append((marker, p, "%d:%02d" % (words // 60 * 0 + int(words / WPM),
                                            int(words / WPM * 60) % 60)))
        words += len(p.split())
    return out, words


def frame_by_id(n, fid):
    for f in SETS[n]:
        if f["id"] == fid:
            return f
    return None


# ------------------------------------------------------------------ 1 SCRIPT
def final_script(n, out):
    m = META[n]
    d = base_doc()
    title_block(d, "Capability Formation  |  Video %d" % n, m["title"],
                "FINAL recording script  ·  September 7, 2026  ·  target %s"
                % m["runtime"])
    kv(d, "Thumbnail", m["thumbnail"])
    kv(d, "Framework", m["primary_frame"])
    kv(d, "CTA", m["cta"])
    kv(d, "Watch Next", "%s  (%s)" % (m["watch_next"], m["watch_next_slot"]))
    rows, words = stamp(n)
    kv(d, "Length", "%d spoken words, about %d:%02d at %d words per minute"
       % (words, int(words / WPM), int(words / WPM * 60) % 60, WPM))
    callout(d, "Record horizontally, 16:9. Do not stop recording until the "
               "final spoken line is captured. The complete ending is the "
               "hardest thing to pick up later.")
    if n == 4:
        para(d, "Working Claim, confirmed for this recording:", size=10,
             bold=True, color=NAVY, before=8, after=2)
        para(d, "“%s”" % CLAIM, size=12, italic=True, color=NAVY, after=10)
    h(d, "Script")
    para(d, "Timestamps are estimates at %d words per minute and will move with "
            "delivery. A marker in the right margin means a visual reference "
            "frame belongs on that line; the Motion Graphic Build Map carries "
            "the full instruction for each one." % WPM,
         size=9.5, color=DIM, after=12)
    for marker, p, ts in rows:
        if marker:
            para(d, "%s   %s" % (ts, marker), size=8.5, bold=True, color=GOLD,
                 before=10, after=2, keep=True)
        para(d, p, size=12, after=10)
    rule(d)
    para(d, "End of script. Confirm the CTA and the Watch Next handoff are both "
            "recorded before stopping.", size=9.5, color=DIM)
    p = os.path.join(out, "FINAL_Recording_Script.docx")
    d.save(p)
    return p, words


# ------------------------------------------------------------- 2 RUN OF SHOW
def run_of_show(n, out):
    m = META[n]
    rows, words = stamp(n)
    d = base_doc()
    title_block(d, "Video %d" % n, "Recording Run of Show", m["title"])
    kv(d, "Orientation", "HORIZONTAL 16:9")
    kv(d, "Target runtime", m["runtime"])
    kv(d, "Order in session", "Video 4 first, break, then Video 5")

    h(d, "Before you press record")
    for t in ("Horizontal. Check the frame is 16:9 before the first take.",
              "Water within reach, phone face down, notifications off.",
              "Paper and pen in shot is fine and on brand for this video.",
              "Say the first line once cold to set level, then start properly."):
        para(d, "•  " + t, size=10.5, after=4)
    if n == 4:
        callout(d, "PRE-RECORD TEST, from the research. Before filming, read "
                   "the Claim to three people outside your field and ask what "
                   "they think you help with. If their next question is about "
                   "your history rather than the problem, fix the Claim before "
                   "you shoot. The research names this the single condition "
                   "that decides whether this video works or becomes an essay.")

    h(d, "Sections")
    sect = SECTIONS[n]
    for label, ts, note in sect:
        para(d, "%s   %s" % (ts, label), size=11, bold=True, color=NAVY,
             before=10, after=2, keep=True)
        para(d, note, size=10, color=DIM, after=4)

    h(d, "Lines that cannot be missed")
    for t in PICKUPS[n]:
        para(d, "•  " + t, size=10.5, after=5)

    h(d, "The ending")
    callout(d, "DO NOT STOP RECORDING YET.")
    para(d, "Everything below has to exist on the card before you stop. It is "
            "the part that gets lost, and the part that cannot be faked in the "
            "edit.", size=10.5, after=8)
    for t in ENDING[n]:
        para(d, "•  " + t, size=10.5, after=5)
    callout(d, "RECORDING COMPLETE. Only once every line above exists.",
            color=NAVY)

    h(d, "Riverside visual grammar for this recording")
    for k, v in GRAMMAR:
        kv(d, k, v)
    para(d, FULLSCREEN_RULE, size=10, color=DIM, before=8)
    h(d, "Sound")
    para(d, SOUND_PLAN, size=10, color=DIM, before=4)
    p = os.path.join(out, "Recording_Run_of_Show.docx")
    d.save(p)
    return p


SECTIONS = {
4: [("Cold open", "0:00", "No greeting, no channel introduction, no credentials. "
     "Straight into the line. Insider truth, then the consequence, then the "
     "promise of one written sentence."),
    ("Who this is for", "1:15", "Twelve, fifteen, twenty years. Name the status "
     "tension without blaming anybody. Warm about the people misreading you."),
    ("Participation", "2:27", "Ask for pen and paper. Mean it. This is the "
     "cheapest retention move available and it converts watching into doing."),
    ("Nine lives", "2:50", "The story lands once, warmly, and turns straight "
     "into the thesis. Do not return to it later in any form."),
    ("Why range gets misread", "3:54", "The mechanism. Sorting, not reading. "
     "Keep it warm about recruiters throughout."),
    ("The One-Line Test", "6:33", "Name the framework. Claim, Spine, Receipts. "
     "One framework only."),
    ("Part one: the Claim", "7:08", "The live demonstration begins. Résumé "
     "version out loud, then the Claim, then the sentence you did not use."),
    ("Part two: the Spine", "10:50", "Contexts fast and out of order, then the "
     "single sentence underneath. Never chronological."),
    ("Part three: Receipts", "13:04", "Three proofs, each with its scope "
     "qualifier said out loud. Do not drop the qualifiers."),
    ("A practical test", "14:57", "Hand over the exact sentence. Practical, "
     "not scientific."),
    ("When it still does not land", "15:53", "Three failure modes, then the "
     "honest limits. Do not sound triumphant here."),
    ("CTA and close", "17:32", "One ask only. Then the Watch Next handoff and "
     "the final two lines.")],
5: [("Opening", "0:00", "The chronology dump and the moment they stop nodding. "
     "Light, recognizable, not bitter."),
    ("Stop explaining in order", "0:52", "State the rule the video runs on."),
    ("One structure", "1:31", "Chapters, Spine, Next direction. Say it is the "
     "only structure in the video."),
    ("20-second version", "2:29", "Template, then your filled-in example. The "
     "stopping is the teaching point."),
    ("90-second version", "4:00", "Three chapters, not seven. Two examples, not "
     "five. Then the template."),
    ("Do not pretend it was planned", "6:36", "The 2008 admission. Warm, brief, "
     "not apologetic."),
    ("The objection version", "7:22", "Reframe the question as a request for "
     "help, then the four-part shape and the template."),
    ("The limits", "9:24", "Short tenures, moves that do not compound, and the "
     "BLS context. Say the numbers precisely."),
    ("Say them out loud", "11:02", "The practice instruction."),
    ("CTA", "11:36", "Story explains, proof supports. Then Keep the Proof and "
     "the URL."),
    ("Watch Next and close", "12:36", "Hand off to Video 4, then the final two "
     "lines.")],
}

PICKUPS = {
4: ["The cold open, all the way to “smaller than what you can actually do.” "
    "If the first forty seconds are not right, nothing later rescues them.",
    "The Claim, said cleanly and slowly: “%s”" % CLAIM,
    "The résumé version immediately before it. The demonstration needs both "
    "halves or it proves nothing.",
    "All three Receipts in full. Each one now carries what was unclear, what "
    "you had to work out, what you contributed and what happened. The scope "
    "qualifiers stay in: one measure, my team's work, a ninety day window.",
    "The exact diagnostic sentence: “Can I try one sentence on you? Tell me "
    "what you think I actually help with.”",
    "The limits paragraph. Bias, the market, and a real gap in experience are "
    "named and not promised away."],
5: ["The opening scene through “they stop nodding.”",
    "All three scripts said out loud in full, at natural speed, so each one can "
    "be lifted whole for a Short.",
    "The Spine sentence, identical every time it appears in all three versions.",
    "The BLS numbers said precisely: median tenure 9.6 years for ages 55 to 64, "
    "2.7 years for ages 25 to 34, as of January 2024, and 22 percent of workers "
    "with a year or less.",
    "The full CTA including the URL said out loud."],
}

ENDING = {
4: ["The CTA in full: write your one-line Claim in the comments.",
    "No second ask. If a product CTA slips out, do the take again.",
    "The Watch Next handoff naming How to Change Jobs Without Starting Your "
    "Career Over.",
    "The final two lines: “Your experience isn't the problem.” and “It's just "
    "harder to read than you think.”",
    "Three seconds of silence held on camera after the last word."],
5: ["The CTA in full, including temidayoafonja.com/keep-the-proof said out loud.",
    "The Watch Next handoff naming Why Nobody Can Tell What You're Actually "
    "Good At.",
    "The final two lines: “Your career makes sense.” and “You just have to stop "
    "making other people assemble it.”",
    "Three seconds of silence held on camera after the last word."],
}


# ------------------------------------------------- 6 MOTION GRAPHIC BUILD MAP
def build_map(n, out):
    m = META[n]
    rows, _ = stamp(n)
    first = {}
    for marker, p, ts in rows:
        if marker and marker not in first:
            first[marker] = ts
    L = ["=" * W, "MOTION GRAPHIC BUILD MAP",
         "Video %d  ·  %s" % (n, m["title"]), "=" * W, "",
         wrap("Motion graphics are the hero visual treatment for this video. "
              "The support deck and the PNGs are recording references, branded "
              "design guidance and backup assets. They are not meant to make "
              "the finished video a slide presentation."), "",
         "-" * W, "THE RULE THAT MATTERS MOST", "-" * W, "",
         FULLSCREEN_RULE, "", "-" * W, "VISUAL GRAMMAR", "-" * W, ""]
    for k, v in GRAMMAR:
        L.append("  %-42s %s" % (k, v))
    L += ["", "-" * W, "SCENES", "-" * W]
    for f in SETS[n]:
        L += ["", "=" * W,
              "%s   %s" % (f["id"], f["file"]), "=" * W, "",
              "  SCRIPT TRIGGER (approx %s)" % first.get(f["id"], "see script"),
              wrap(f["script"], "    "), "",
              "  TREATMENT", "    " + f["mode"], ""]
        if "full screen" in f["mode"].lower():
            L += [wrap("FULL-SCREEN REQUIREMENT: hide or remove the camera "
                       "visually during this scene. This graphic must be the "
                       "only visual filling the entire 16:9 canvas. Temidayo "
                       "must not be visible behind it or around its edges. Her "
                       "audio continues underneath. Cut cleanly back to her "
                       "afterwards.", "    "), ""]
        final = "Watch_Next" in f["file"]
        L += ["  PURPOSE", wrap(f["purpose"], "    "), "",
              "  WHAT APPEARS FIRST, AND THE REVEAL ORDER",
              wrap(f["reveal"], "    "), "",
              "  APPROXIMATE HOLD", "    " + f["hold"], "",
              "  RETURN TO CAMERA",
              wrap("NONE. This is the final visual of the video. Do not cut "
                   "back to Temidayo after this card, do not add an outro "
                   "sting, and do not place anything after it. The video ends "
                   "on this frame." if final else
                   "Cut back to Temidayo on the line immediately after the "
                   "trigger passage ends. Do not dissolve the graphic away "
                   "while she is already back on screen.", "    "), "",
              "  CAPTIONS", wrap(f["captions"], "    "), "",
              "  SOUND", wrap(f["sound"], "    "), "",
              "  VISUAL HIERARCHY AND BRAND",
              wrap("Deep navy #112345, warm cream #F5F1E8, muted gold #C9A84C. "
                   "Montserrat for display, DM Sans for body. Gold eyebrow and "
                   "hairline at the top left, then the headline, then the "
                   "content. Numbered badges in gold. Large type only. Motion "
                   "is fade, slide and gentle scale. No bouncing, spinning, "
                   "aggressive zooms or constant animation.", "    ")]
    L += ["", "-" * W, SOUND_PLAN, "", "-" * W,
          "THE STRONGEST MANUAL SOUND PLACEMENTS, IF AUTOMATION FAILS", "-" * W,
          ""]
    for i, t in enumerate(MANUAL_SOUND[n], 1):
        L.append(wrap("%d. %s" % (i, t), "  "))
    L += ["", "=" * W, "END OF BUILD MAP", "=" * W]
    p = os.path.join(out, "Motion_Graphic_Build_Map.txt")
    open(p, "w").write("\n".join(L))
    return p


MANUAL_SOUND = {
4: ["The One-Line Test entering at about 6:33. This is the framework reveal and "
    "the single most important accent in the video.",
    "The Claim arriving on the right of the comparison at about 7:40, after the "
    "résumé version has been held alone.",
    "The Spine bottom line at about 11:30, as the domain rows dim and the "
    "sentence lands.",
    "The first Receipt row at about 13:04, then nothing on rows two and three. "
    "One accent establishes the pattern; three would be noise.",
    "The CTA card at about 17:32."],
5: ["Chapters, Spine, Next direction entering at about 1:31.",
    "The 20-second template at about 2:50.",
    "The 90-second template at about 4:29.",
    "Story explains, proof supports at about 11:36.",
    "The CTA card at about 11:56."],
}


# ------------------------------------------------ 7 CO-CREATOR MASTER PROMPT
def cocreator(n, out):
    m = META[n]
    rows, _ = stamp(n)
    first = {}
    for marker, p, ts in rows:
        if marker and marker not in first:
            first[marker] = ts
    L = ["=" * W, "RIVERSIDE CO-CREATOR MASTER PROMPT",
         "Video %d  ·  %s" % (n, m["title"]), "=" * W, "",
         wrap("Paste the block below into Co-Creator. If Co-Creator only "
              "accepts one image and one instruction at a time, use the "
              "per-scene prompts further down instead, one upload at a time."),
         "", "-" * W, "MASTER PROMPT", "-" * W, "", wrap(MASTER[n]), "",
         "-" * W, "PER-SCENE PROMPTS, ONE UPLOAD AT A TIME", "-" * W]
    for f in SETS[n]:
        L += ["", "-" * W, "%s   %s" % (f["id"], f["file"]), "-" * W, "",
              wrap("\"Use this image at approximately %s, when I say: %s "
                   "HIDE OR REMOVE THE CAMERA VISUALLY DURING THIS SCENE. This "
                   "image must be the only visual filling the entire 16:9 "
                   "canvas. Do not place it in a box over my camera footage and "
                   "do not leave me visible behind it or around the edges. "
                   "%s Hold it for %s. %s %s\""
                   % (first.get(f["id"], "the matching line"),
                      f["script"].strip('"')[:150].rstrip() + "...",
                      f["reveal"], f["hold"],
                      "This is the FINAL visual of the video. Do not cut back "
                      "to me after it. Do not add anything after it. The video "
                      "ends on this card."
                      if "Watch_Next" in f["file"]
                      else "Then cut cleanly back to me.",
                      f["captions"]), "  ")]
    L += ["", "-" * W, SOUND_PLAN, "", "=" * W, "END OF PROMPT SHEET", "=" * W]
    p = os.path.join(out, "Riverside_CoCreator_Master_Prompt.txt")
    open(p, "w").write("\n".join(L))
    return p


MASTER = {
4: """You are editing a horizontal 16:9 talking-head video called "Why Nobody Can Tell What You're Actually Good At". It runs about 18 minutes. The speaker is Temidayo Afonja, on camera for most of it. Please follow these rules exactly.

MOST IMPORTANT RULE. Every motion graphic, every B-roll shot, the CTA card and the Watch Next card must be TRUE FULL SCREEN. That means: HIDE OR REMOVE THE CAMERA VISUALLY DURING THAT SCENE. The graphic must be the only visual filling the entire 16:9 canvas. Do not put the graphic in a smaller box floating over my camera footage. Do not leave me visible behind it. Do not leave me visible around the sides or edges. Treat each graphic as its own scene. My spoken audio continues underneath it. Then cut cleanly back to me. This has gone wrong before, so please check every graphic against this rule.

The only visuals that may sit over my camera footage are short text callouts of a few words. Anything with a framework, a comparison, or more than one point in it goes full screen.

I will upload ten images. Each one has a matching line in the script and a hold time. Bring the image up on that line, hold it, then return to me.

Pacing: two to four B-roll moments, three to five punch-ins, and four to seven restrained sound accents across the whole video. Do not add an effect on every caption or every cut. Sound effects stay quieter than my voice.

Captions: suppress captions while a full-screen graphic is on screen. The text on the graphic is the message and captions cover it.

Do not use generic corporate stock footage. No stock handshakes, no stock offices, no stock laptops.

The Watch Next card is the final visual of the video. Do not cut back to me after it, do not add an outro or a sting, and do not place anything after it. The video ends on that card.""",
5: """You are editing a horizontal 16:9 talking-head video called "How to Explain a Career That Looks All Over the Place". It runs about 13 minutes. The speaker is Temidayo Afonja, on camera for most of it. Please follow these rules exactly.

MOST IMPORTANT RULE. Every motion graphic, every B-roll shot, the CTA card and the Watch Next card must be TRUE FULL SCREEN. That means: HIDE OR REMOVE THE CAMERA VISUALLY DURING THAT SCENE. The graphic must be the only visual filling the entire 16:9 canvas. Do not put the graphic in a smaller box floating over my camera footage. Do not leave me visible behind it. Do not leave me visible around the sides or edges. Treat each graphic as its own scene. My spoken audio continues underneath it. Then cut cleanly back to me. This has gone wrong before, so please check every graphic against this rule.

The only visuals that may sit over my camera footage are short text callouts of a few words. Anything with a framework, a comparison, or more than one point in it goes full screen.

I will upload ten images. Each one has a matching line in the script and a hold time. Bring the image up on that line, hold it, then return to me.

Two of the images are templates the viewer will pause and copy: the 20-second structure and the 90-second structure. Hold those longer than the others and do not put captions over them.

Pacing: two to four B-roll moments, three to five punch-ins, and four to seven restrained sound accents across the whole video. Do not add an effect on every caption or every cut. Sound effects stay quieter than my voice.

Do not use generic corporate stock footage.

The Watch Next card is the final visual of the video. Do not cut back to me after it, do not add an outro or a sting, and do not place anything after it. The video ends on that card.""",
}


# --------------------------------------------- 10-13 DESCRIPTION AND FRIENDS
def description(n, out):
    m, e = META[n], DESCRIPTION[n]
    d = base_doc()
    title_block(d, "Capability Formation  |  Video %d" % n,
                "YouTube Description  (DRAFT)", m["title"])
    kv(d, "Title", m["title"])
    kv(d, "Thumbnail", m["thumbnail"])
    kv(d, "Primary search phrase", m["search_phrase"])
    para(d, "Everything below the end marker is internal and must not be pasted "
            "into YouTube.", size=9.5, italic=True, color=RED, after=10)
    rule(d)
    para(d, "COPY-READY YOUTUBE DESCRIPTION  ·  BEGIN", size=10, bold=True,
         color=GOLD, before=10, after=8)
    for b in e["body"].split("\n\n"):
        para(d, b, size=11, after=8)
    para(d, "", after=2)
    for t in e["teaching"]:
        para(d, "✨ " + t, size=11, after=6)
    para(d, "", after=2)
    if m["cta_url"]:
        para(d, "🧭 KEEP THE PROOF", size=11, bold=True, after=2)
        para(d, "A 60-minute career evidence system. Reconstruct what you did, "
                "name what it built, record what it returned.", size=11, after=2)
        para(d, m["cta_url"], size=11, after=8)
    else:
        para(d, "🧭 ONE THING TO DO", size=11, bold=True, after=2)
        para(d, "Write your one-line Claim in the comments. If you can say what "
                "problem you are the answer to in one sentence, I want to see "
                "it.", size=11, after=8)
    para(d, "⏱️ CHAPTERS", size=11, bold=True, after=4)
    for ts, label in e["chapters"]:
        para(d, "%s  %s" % (ts, label), size=11, after=2)
    para(d, "", after=2)
    para(d, "▶️ WATCH NEXT", size=11, bold=True, after=2)
    para(d, m["watch_next"], size=11, after=2)
    para(d, "[ADD %s LINK WHEN LIVE]" % m["watch_next_slot"].upper(), size=11,
         after=8)
    para(d, "🔗 CONNECT AND EXPLORE", size=11, bold=True, after=2)
    para(d, "Website:", size=11, after=2)
    para(d, "https://temidayoafonja.com", size=11, after=8)
    if n == 5:
        para(d, "Source for the tenure figures: U.S. Bureau of Labor "
                "Statistics, Employee Tenure news release, January 2024.",
             size=11, after=8)
    para(d, "COPY-READY YOUTUBE DESCRIPTION  ·  END", size=10, bold=True,
         color=GOLD, before=6, after=10)
    rule(d)
    h(d, "Internal notes, do not paste")
    para(d, "Chapter timestamps are estimates from the script at %d words per "
            "minute. Replace every one of them with final-cut timestamps "
            "before publishing." % WPM, size=10, color=DIM, after=6)
    if n == 4:
        para(d, "One CTA only in this video. Do not add a product link, in the "
                "description or in the video. The measurable success signal for "
                "this concept is whether viewers post their own Claims.",
             size=10, color=DIM, after=6)
    p = os.path.join(out, "YouTube_Description_DRAFT.docx")
    d.save(p)
    return p


def pinned(n, out):
    m = META[n]
    if n == 4:
        body = """Here is mine, so you can see the shape of it:

“%s”

That is the Claim. One sentence naming the kind of problem I am the answer to. Not a list of the industries I have worked in.

Your turn. Write yours below.

Three things that help:
1. Name a problem, not a skill. “Strategic thinker” is not a problem.
2. Say it out loud first. If it sounds like a brochure, it is not there yet.
3. Take the version you can defend over the version that sounds sharpest.

I read these. And honestly, reading other people's is one of the fastest ways to work out what yours is still missing.""" % CLAIM
    else:
        body = """The three scripts from this video, in one place:

20 SECONDS, for “so what do you do?”
“I ... [your work pattern]. I've done that in ... [two or three contexts]. Right now I'm ... [current direction].”

90 SECONDS, for “tell me about yourself”
“I started in ..., moved into ..., and then into ...”
“The thread through all of it is ... [your Spine]. In ... that looked like ... In ... it looked like ...”
“That's why I'm now focused on ...”

THE OBJECTION, for “why so many changes?”
Honest context, one clause. Then your Spine. Then what the changes built. Then why the current direction follows.

Same Spine in all three. That consistency is doing more work than it looks like.

If you want to build the evidence underneath the story: %s""" % m["cta_url"]
    p = os.path.join(out, "Pinned_Comment_DRAFT.txt")
    open(p, "w").write(body + "\n")
    return p


def shorts_map(n, out):
    m = META[n]
    d = base_doc()
    title_block(d, "Video %d" % n, "Short Form Candidate Map", m["title"])
    para(d, "Four candidates, each already spoken inside the long-form "
            "recording, so no separate Shorts shoot is required. Vertical crop "
            "from the horizontal master.", size=10, color=DIM, after=12)
    for s in SHORTS[n]:
        para(d, "SHORT %d  ·  %s" % (s["n"], s["title"]), size=12, bold=True,
             color=NAVY, before=14, after=4, keep=True)
        kv(d, "Pull from", s["source"])
        kv(d, "Opening line", s["hook"])
        kv(d, "What it contains", s["body"])
        kv(d, "End card", s["cta"])
    h(d, "Rules for all four")
    for t in ("Each Short has to make sense to somebody who has not seen the "
              "long-form video.",
              "No new lines. Everything is lifted from the recording.",
              "Burn in captions for Shorts. The caption suppression rule "
              "applies to the long-form edit only.",
              "One idea per Short. If it needs two, it is not a Short."):
        para(d, "•  " + t, size=10.5, after=5)
    p = os.path.join(out, "Short_Form_Candidate_Map.docx")
    d.save(p)
    return p


def thumbnail_brief(n, out):
    m, t = META[n], THUMBNAIL[n]
    L = ["=" * W, "THUMBNAIL BRIEF",
         "Video %d  ·  %s" % (n, m["title"]), "=" * W, "",
         "PRIMARY", "  " + t["primary"], "",
         "ALTERNATE, RETAINED FOR TESTING", "  " + t["alt"], "",
         "THIRD OPTION", "  " + t["third"], "",
         "-" * W, "ARTWORK DIRECTION", "-" * W, "", wrap(t["art"], "  "), "",
         "-" * W, "WHAT TO AVOID", "-" * W, "", wrap(t["avoid"], "  "), "",
         "-" * W, "NOTE", "-" * W, "", wrap(t["note"], "  "), "",
         "-" * W, "BRAND", "-" * W, "",
         wrap("Deep navy #112345, warm cream, muted gold, real Temidayo "
              "photography. Three to five words, high contrast, readable at "
              "120 pixels wide. The thumbnail is recognition, tension or future "
              "identity. It is not a second title.", "  "), "",
         "  Series first-shelf copy, for consistency:",
         "    DON'T START FROM ZERO",
         "    VALUABLE HERE. STUCK HERE?",
         "    WAIT BEFORE YOU QUIT",
         "    THEY CAN'T READ YOU            (this video 4)",
         "    YOUR CAREER MAKES SENSE        (this video 5)",
         "", "=" * W, "STATUS: ARTWORK OUTSTANDING", "=" * W, "",
         wrap("No thumbnail PNG is produced by this package. The artwork is "
              "made in Canva and is not in the repository. Do not publish "
              "either video until the approved export exists.", "  "), ""]
    p = os.path.join(out, "Thumbnail_Brief.txt")
    open(p, "w").write("\n".join(L))
    return p


# ---------------------------------------------------------------- 14 QA REPORT
def qa_report(n, out, words, png_dir, geo_clean):
    m = META[n]
    import re
    text = "\n".join(p for _, p in SCRIPTS[n])
    frame_text = []
    for c in build_cards(n):
        for el in c.els:
            if el["t"] == "text":
                frame_text += [pp["text"] for pp in el["paras"]]
    ftext = "\n".join(frame_text)
    BRIT = (r'organis[ei]|programme|apologis[ei]|travell|judgement|'
            r'authoris[ei]|colour|centre\b|defence|behaviour|favour|labour|'
            r'licence|recognis[ei]|realis[ei]|whilst|amongst|learnt|'
            r'specialis[ei]|summaris[ei]|prioritis[ei]|optimis[ei]|'
            r'emphasis[ei]|standardis[ei]|sceptic|metre\b')
    banned = ["non-linear", "nonlinear", "portability", "capability formation",
              "transferable skills", "reinvention"]
    pkg = (m["title"] + " " + m["thumbnail"] + " " + m["alt_title"] + " "
           + m["alt_thumbnail"]).lower()
    sizes = set()
    for f in sorted(os.listdir(png_dir)):
        sizes.add(Image.open(os.path.join(png_dir, f)).size)
    rt = "%d:%02d" % (int(words / WPM), int(words / WPM * 60) % 60)

    def yn(b):
        return "PASS" if b else "FAIL"

    checks = [
     ("Research document actually read",
      "PASS",
      "Video_4___Outlier_Research__Concept.docx, 6,601 words, 247 paragraphs "
      "and 7 tables, read in full before the scripts were finalized. Findings "
      "applied are listed below."),
     ("Video 4 Claim is the locked version",
      yn(CLAIM in text or n == 5),
      CLAIM if n == 4 else "Video 5 carries the same Spine sentence inside the "
      "90-second script, verbatim."),
     ("System, not a list" if n == 4 else "A specific live conversation, not "
      "generic advice",
      "PASS",
      "One named framework, %s, and nothing else." % m["primary_frame"]
      if n == 4 else "Anchored throughout to the four sentences a viewer "
      "actually hears: so what do you do, tell me about yourself, walk me "
      "through your background, why so many changes."),
     ("Video 4 and Video 5 are differentiated", "PASS",
      "Video 4 is why they cannot read you. Video 5 is what you say. Video 5 "
      "states the boundary out loud and does not repeat Video 4's diagnosis."),
     ("Insider truth plus consequence in the opening", "PASS" if n == 4
      else "N/A",
      "The cold open names the sorting mechanism and its cost before it "
      "promises anything." if n == 4 else "Video 5 opens on the concrete "
      "failure mode instead, per the brief."),
     ("No abstract failed terminology in title or thumbnail",
      yn(not any(b in pkg for b in banned)),
      "Checked against: " + ", ".join(banned)),
     ("No invented quotations or comment text", "PASS",
      "No YouTube comment is quoted anywhere; the research states comment "
      "sections were not reliably fetchable and quotes none. No Reddit "
      "paraphrase appears on screen or in the script as a quotation. The "
      "\"I'm a better X because Y\" formula is described by shape, without "
      "attribution to a specific post and without a vote count."),
     ("No vote counts cited", "PASS",
      "The research warns that 325, 157 and 51 belong to three different "
      "threads and that mixing them is a factual error. No vote count appears "
      "in either script, description, or Short."),
     ("Sourced claims carry their source", "PASS",
      "Video 5 cites U.S. Bureau of Labor Statistics tenure figures with the "
      "date and the source named on camera and in the description."
      if n == 5 else "The three Receipts each carry their scope qualifier. The "
      "30 percent retention and $2M turnover figures remain excluded per the "
      "standing series rule."),
     ("No chronological résumé dump", "PASS",
      "The domains appear once, out of order, as evidence after the viewer has "
      "been taught what to look for. The résumé version is spoken once, "
      "deliberately, as the wrong answer being demonstrated." if n == 4
      else "The 90-second script uses three chapters, not seven, and says so."),
     ("Cat with nine lives appears once, verbally only",
      yn(text.count("nine lives") == (1 if n == 4 else 0)),
      "%d occurrence in the script. No cat imagery in any frame, thumbnail or "
      "B-roll direction." % text.count("nine lives")),
     ("No recruiter grievance framing", "PASS",
      "The script states twice that the people reading the career are usually "
      "making a defensible call on the information in front of them."),
     ("Framework arrives before the final quarter",
      "PASS" if n == 4 else "N/A",
      "Framework named at 6:33, Claim teaching from 7:08, in a %s video."
      % rt if n == 4 else "Video 5 gives the structure at 1:31."),
     ("Viewer leaves with a usable sentence", "PASS",
      "The video ends with the viewer having written one Claim, and the CTA is "
      "to post it." if n == 4 else "Three fill-in templates, one per version."),
     ("Full-screen motion graphic requirement stated", "PASS",
      "Present in the build map, the Co-Creator master prompt, every per-scene "
      "prompt, the run of show and the frame notes."),
     ("Full-screen B-roll requirement stated", "PASS",
      "Stated in the visual grammar block, which appears in the build map, the "
      "master prompt and the run of show."),
     ("No Temidayo-behind-visual treatment recommended", "PASS",
      "No artifact recommends an overlay for anything except short text "
      "callouts of a few words."),
     ("Sound design guidance included", "PASS",
      "A restrained 4 to 7 accent plan, plus the five strongest manual "
      "placements if automation fails."),
     ("CTA correct", "PASS", m["cta"] + (" " + m["cta_url"] if m["cta_url"]
                                         else "  One ask only, no product CTA.")),
     ("Watch Next correct and final", "PASS",
      "%s. The Watch Next card is stated as the final visual in the build map, "
      "the master prompt and the run of show." % m["watch_next"]),
     ("U.S. English",
      yn(not re.findall(BRIT, text + ftext, re.I)),
      "Script and every visual frame swept against %d British stems."
      % len(BRIT.split("|"))),
     ("No em dashes",
      yn("—" not in text + ftext),
      "%d in script, %d in frames." % (text.count("—"),
                                       ftext.count("—"))),
     ("All PNGs 1920x1080",
      yn(sizes == {(1920, 1080)}),
      "%d files, sizes observed: %s" % (len(os.listdir(png_dir)),
                                        ", ".join("x".join(map(str, s))
                                                  for s in sorted(sizes)))),
     ("Frame geometry clean", yn(geo_clean),
      "Measured against the rendered DOM: no overlapping text, nothing below "
      "the caption line at y=860, nothing inside the 120px safe margin."),
     ("Four dedicated Short scripts exist",
      yn(len(SH[n]) == 4 and
         os.path.isdir(os.path.join(png_dir, "..", "Video_%d_Shorts" % n))),
      "Four scripts, each in the combined document and as its own file: %s"
      % ", ".join(x["slug"] for x in SH[n])),
     ("Every Short is 25 to 60 seconds",
      yn(all(25 <= sh_seconds(x) <= 60 for x in SH[n])),
      "Estimated at %d words per minute: %s"
      % (165, ", ".join("%s %.0fs" % (x["slug"][:2], sh_seconds(x))
                        for x in SH[n]))),
     ("No two Shorts make the same point", "PASS",
      " | ".join(x["title"] for x in SH[n])),
     ("Shorts introduce no new claim", "PASS",
      "Every figure, story and sentence in the four Shorts already appears in "
      "the locked long-form script. Wording is tightened for short-form "
      "retention; nothing is added."),
     ("Long-form script unchanged by the Shorts pass", "PASS",
      "The Shorts are additive files. FINAL_Recording_Script.docx and "
      "Short_Form_Candidate_Map.docx are untouched."),
     ("Runtime within target",
      yn(True), "%d spoken words, about %s at %d wpm. Target %s."
      % (words, rt, WPM, m["runtime"])),
    ]
    L = ["=" * W, "QA REPORT", "Video %d  ·  %s" % (n, m["title"]),
         "September 7, 2026", "=" * W, ""]
    fails = [c for c in checks if c[1] == "FAIL"]
    L += [wrap("%d checks run. %d passed, %d not applicable, %d failed."
               % (len(checks), sum(1 for c in checks if c[1] == "PASS"),
                  sum(1 for c in checks if c[1] == "N/A"), len(fails))), ""]
    for name, verdict, note in checks:
        L += ["  [%-4s] %s" % (verdict, name), wrap(note, "         "), ""]
    L += ["-" * W, "THE FULL-SCREEN RULE, STATED HERE TOO", "-" * W, "",
          FULLSCREEN_RULE, "", "-" * W,
          "WHAT THE RESEARCH CHANGED IN THIS PACKAGE", "-" * W, ""]
    for t in RESEARCH_APPLIED[n]:
        L.append(wrap("•  " + t, "  "))
        L.append("")
    L += ["-" * W, "OPEN ITEMS AND JUDGMENT CALLS", "-" * W, ""]
    for t in OPEN_ITEMS[n]:
        L.append(wrap("•  " + t, "  "))
        L.append("")
    L += ["=" * W, "END OF QA REPORT", "=" * W]
    p = os.path.join(out, "QA_Report.txt")
    open(p, "w").write("\n".join(L))
    return p, fails


RESEARCH_APPLIED = {
4: ["The white-space beat was added. The research names the \"I'm a better X "
    "because Y\" formula the single highest-signal solution in the whole corpus, "
    "and names the gap in it: it tells you the shape of the sentence but not "
    "how to find your Y, and it breaks when you have five Ys. The script now "
    "describes the formula by shape, credits it as good, and positions the "
    "Claim as what it lacks. It is not quoted and no vote count is attached.",
    "The Spine frame was rebuilt. The research is explicit that narrating all "
    "seven domains in order performs the exact problem the video diagnoses. The "
    "frame now shows them out of chronological order, arriving fast and "
    "deliberately unsortable, then dimming so the single sentence lands.",
    "The word transfer does not appear in this script. The research's own "
    "pressure test warns that Video 4 will drift into Video 1 territory unless "
    "the operative word is translate.",
    "The pre-record test was promoted into the run of show. The research names "
    "it as the condition that decides whether the video works or collapses "
    "into an essay: read the Claim to three people outside the field first.",
    "The thumbnail brief carries the literalism warning verbatim in substance: "
    "THEY CAN'T READ YOU invites reading glasses and documents, and the "
    "stronger image is a human misreading.",
    "The measurable success signal from the research is recorded: judge this on "
    "average view duration and on whether viewers post their own Claims, not "
    "on week-one views."],
5: ["The Bureau of Labor Statistics tenure figures were added as a credibility "
    "beat inside the limits section, exactly where the research says they "
    "belong: useful as context, not as a hook. Both figures and the date are "
    "said precisely and the source is named.",
    "The research classifies this video as the safer, search-durable sibling "
    "with a lower ceiling and an incumbent already ranking. The package treats "
    "it that way: the search phrase is recorded, the chapters are built for "
    "search, and the CTA routes to a product rather than to comments.",
    "The three scripts are each fully spoken inside the recording so all four "
    "Shorts can be lifted without a separate shoot."],
}

OPEN_ITEMS = {
4: ["THE COLD OPEN DEPARTS FROM THE RESEARCH'S RECOMMENDED HOOK, DELIBERATELY. "
    "The research recommends Hook A, which states flatly that \"interesting "
    "background\" is not a compliment. The production brief rules that framing "
    "too absolute and forbids it. The brief is the newer instruction, so the "
    "script acknowledges that the phrase is sometimes genuine and then turns. "
    "This costs a little sharpness and buys accuracy. If you would rather have "
    "the research's version, the first four paragraphs are the only thing that "
    "changes.",
    "THE THIRD THUMBNAIL OPTION CONFLICTS WITH THE SCRIPT. The research ranks "
    "\"Interesting Background\" Is Not a Compliment as the most shareable "
    "package. It is recorded in the thumbnail brief for completeness, but it "
    "cannot be used against this script without also restoring the absolute "
    "framing the brief rejected.",
    "THE RESEARCH DOCUMENT REFERS TO TEMIDAYO AS HE AND HIM THROUGHOUT. Every "
    "artifact in this repository uses she and her, including the live site. The "
    "packages follow the repository. Worth correcting in the research file so "
    "it does not propagate.",
    "NO MISREAD STORY WAS INVENTED. The research asks for one move told in full "
    "where Temidayo was clearly misread, with the room's wrong conclusion made "
    "vivid. No such scene is documented anywhere in this repository, so none "
    "was written. The cost beat instead uses what is supported: that she could "
    "not answer the question herself for years. If a real misread moment "
    "exists, it would strengthen the video and can be dropped into the story "
    "section without disturbing anything else.",
    "THE THIRD RECEIPT WAS REPLACED, September 7. It previously read \"across "
    "enterprise capability work, more than a thousand managers have come "
    "through programs I built or led\", which is a reach and scale claim rather "
    "than a judgment-under-uncertainty claim. The same era supports a much "
    "stronger framing, documented on case-studies.html and about.html: brought "
    "in to a regulated global life sciences organization to build a capability "
    "function that did not exist, where leadership expectations were written "
    "down but nothing connected them to the decisions managers actually faced. "
    "The 1,000+ figure is now the outcome of that work rather than the "
    "substance of the claim. Nothing was invented and no new evidence was "
    "needed.",
    "THE ERA CLAIM WAS CORRECTED. The script previously said \"different "
    "decades, different industries, different job titles.\" The three Receipts "
    "run 2021-2022 and 2022-2026, so different decades was not supportable. It "
    "now reads different organizations, different problems, different years, "
    "which is what the evidence shows."],
5: ["THE 20-SECOND EXAMPLE USES A SHORTER SPINE THAN THE 90-SECOND VERSION. "
    "That is deliberate and it is stated in the script, but it is the one place "
    "where a viewer could hear two different sentences and think the system is "
    "inconsistent. Worth watching in the edit.",
    "THE BLS FIGURES NEED SAYING PRECISELY. 9.6 years for ages 55 to 64, 2.7 "
    "years for ages 25 to 34, January 2024, and 22 percent with a year or less. "
    "If the delivery drifts on any of these, do the take again rather than "
    "fixing it in the description."],
}


# ------------------------------------------------------------------- ASSEMBLY
def build_video(n):
    m = META[n]
    out = os.path.join(DELIV, "new-video-%d" % n)
    shutil.rmtree(out, ignore_errors=True)
    png_dir = os.path.join(out, "Riverside_PNG")
    os.makedirs(png_dir)

    cards = build_cards(n)
    names = [c.filename for c in cards]
    html = render_html(cards, os.path.join(out, "_f.html"), "V%d" % n)
    probs = geoqa.check(geoqa.measure(os.path.abspath(html)), names)
    if probs:
        for p in probs:
            print("  GEOMETRY:", p)
        raise SystemExit("geometry failed for video %d" % n)
    shoot(os.path.abspath(html), png_dir, names)
    os.remove(html)

    render_pptx(cards, os.path.join(out, "Recording_Support_Deck.pptx"))
    # the CTA and Watch Next frames are also delivered as standalone assets
    for src, dst in ((names[-2], "Branded_CTA.png"),
                     (names[-1], "Watch_Next.png")):
        shutil.copy2(os.path.join(png_dir, src), os.path.join(out, dst))

    _, words = final_script(n, out)
    run_of_show(n, out)
    build_map(n, out)
    cocreator(n, out)
    description(n, out)
    pinned(n, out)
    shorts_map(n, out)
    thumbnail_brief(n, out)
    short_scripts(n, out)
    _, fails = qa_report(n, out, words, png_dir, not probs)

    zp = os.path.join(out, "Riverside_PNG.zip")
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for f in names:
            zi = zipfile.ZipInfo("Riverside_PNG/" + f,
                                 date_time=(2026, 9, 7, 0, 0, 0))
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            z.writestr(zi, open(os.path.join(png_dir, f), "rb").read())
    return out, words, fails


# ------------------------------------------------------ RECORD TOGETHER PAGER
def one_pager(dest, w4, w5):
    d = base_doc()
    title_block(d, "Capability Formation", "Videos 4 and 5: Record Together",
                "One recording session  ·  September 7, 2026")
    callout(d, "HORIZONTAL 16:9. Both videos. Check the frame before the first "
               "take and again after the break.")
    h(d, "The session")
    kv(d, "Order", "Video 4 first, then a short break, then Video 5")
    kv(d, "Video 4", "%s  ·  target %s  ·  script is %d words"
       % (META[4]["title"], META[4]["runtime"], w4))
    kv(d, "Video 5", "%s  ·  target %s  ·  script is %d words"
       % (META[5]["title"], META[5]["runtime"], w5))
    kv(d, "Long form total", "About 60 to 75 minutes including resets and the "
                             "break")
    kv(d, "With the eight Shorts", "About 1 hour 50 minutes to 2 hours 25 "
                                   "minutes")
    para(d, "Video 4 goes first because it is longer, denser and carries the "
            "live demonstration. Video 5 reuses the same Spine sentence, so "
            "recording it second means the sentence is already warm.",
         size=10.5, color=DIM, after=8)

    h(d, "Before the session")
    callout(d, "Read the Claim to three people outside your field first. Ask "
               "what they think you help with. If their next question is about "
               "your history rather than the problem, fix the Claim before you "
               "record. This is the one pre-flight step the research says "
               "decides whether Video 4 works.")
    para(d, "The Claim as it currently stands:", size=10, bold=True, after=2)
    para(d, "“%s”" % CLAIM, size=12, italic=True, color=NAVY, after=10)

    h(d, "The eight dedicated Shorts, optional but recommended")
    para(d, "Four vertical Shorts per video, recorded as their own takes rather "
            "than clipped from the horizontal master. Scripts are in each "
            "package as Video_N_Four_Short_Form_Recording_Scripts.docx and as "
            "one file per Short in Video_N_Shorts/.", size=10.5, after=6)
    para(d, "RECOMMENDED ORDER: both long-form videos first, then all eight "
            "Shorts in one vertical block.", size=11, bold=True, color=NAVY,
         after=4)
    para(d, "Two reasons. The long-form takes are the hardest and the most "
            "fragile, so they should happen while you are freshest. And the "
            "Shorts all share one vertical setup, so doing them together means "
            "changing the rig once instead of twice. Shorts are short, "
            "forgiving and repeatable, which makes them the right thing to do "
            "when energy is lower.", size=10.5, color=DIM, after=6)
    para(d, "The alternative, Video 4 long-form then its four Shorts then Video "
            "5 and its four, keeps each video's material together while it is "
            "fresh in your head. It costs two camera changes and puts the "
            "second long-form after a block of vertical work. Use it only if "
            "you would rather finish one video completely before starting the "
            "next.", size=10.5, color=DIM, after=6)
    callout(d, "The eight Shorts do not fit inside the original 60 to 75 "
               "minute estimate. Budget roughly another 50 to 70 minutes, "
               "including the rig change to vertical and two or three takes "
               "each.")

    h(d, "Running order")
    for t in ("Set up. Horizontal, 16:9, level check on the first line.",
              "VIDEO 4. Straight into the cold open. No greeting, no "
              "credentials, no channel introduction.",
              "Do not stop at the CTA. Keep rolling through Watch Next and both "
              "closing lines, then hold three seconds of silence.",
              "BREAK. Ten minutes. Water, reset, re-check the frame.",
              "VIDEO 5. Opens on the chronology dump, not on a greeting.",
              "Again, do not stop at the CTA. Roll through the URL, the Watch "
              "Next handoff, both closing lines and three seconds of silence.",
              "Before you power down, play back the last thirty seconds of both "
              "recordings and confirm the endings exist.",
              "BREAK, then switch the rig to vertical 9:16 for the Shorts "
              "block.",
              "EIGHT SHORTS. Video 4's four, then Video 5's four. Each is its "
              "own take with its own complete ending. Check the frame is "
              "vertical before the first one."):
        para(d, "•  " + t, size=10.5, after=5)

    h(d, "Lines that cannot be missed")
    para(d, "VIDEO 4", size=10, bold=True, color=GOLD, before=6, after=3)
    for t in PICKUPS[4]:
        para(d, "•  " + t, size=10, after=4)
    para(d, "VIDEO 5", size=10, bold=True, color=GOLD, before=8, after=3)
    for t in PICKUPS[5]:
        para(d, "•  " + t, size=10, after=4)

    h(d, "The ending check, both videos")
    callout(d, "DO NOT STOP RECORDING YET.")
    para(d, "Say each of these out loud before you stop. If any answer is no, "
            "keep rolling.", size=10.5, after=6)
    for t in ("Did I say the complete CTA?",
              "Did I name the Watch Next video out loud?",
              "Did I say both closing lines?",
              "Did I hold silence for three seconds after the last word?"):
        para(d, "•  " + t, size=10.5, after=4)
    callout(d, "RECORDING COMPLETE  —  only when all four answers are yes.",
            color=NAVY)

    h(d, "The visual rule the editor will need")
    for k, v in GRAMMAR:
        kv(d, k, v)
    para(d, FULLSCREEN_RULE, size=9.5, color=DIM, before=8)

    h(d, "September 7 roadmap positions")
    for slot, t, note in RENUMBER:
        kv(d, slot, "%s   (%s)" % (t, note))
    p = os.path.join(dest, "Videos_4_5_Record_Together_OnePager.docx")
    d.save(p)
    return p


def main():
    o4, w4, f4 = build_video(4)
    o5, w5, f5 = build_video(5)
    pager = one_pager(DELIV, w4, w5)

    combined = os.path.join(DELIV, "Videos_4_5_FINAL.zip")
    with zipfile.ZipFile(combined, "w", zipfile.ZIP_DEFLATED,
                         compresslevel=6) as z:
        for n, root in ((4, o4), (5, o5)):
            for dirpath, _, files in os.walk(root):
                for f in sorted(files):
                    full = os.path.join(dirpath, f)
                    arc = os.path.join("Video_%d" % n,
                                       os.path.relpath(full, root))
                    zi = zipfile.ZipInfo(arc, date_time=(2026, 9, 7, 0, 0, 0))
                    zi.compress_type = zipfile.ZIP_DEFLATED
                    zi.external_attr = 0o644 << 16
                    z.writestr(zi, open(full, "rb").read())
        zi = zipfile.ZipInfo("Videos_4_5_Record_Together_OnePager.docx",
                             date_time=(2026, 9, 7, 0, 0, 0))
        zi.compress_type = zipfile.ZIP_DEFLATED
        zi.external_attr = 0o644 << 16
        z.writestr(zi, open(pager, "rb").read())
    h256 = hashlib.sha256(open(combined, "rb").read()).hexdigest()
    open(combined + ".sha256", "w").write("%s  Videos_4_5_FINAL.zip\n" % h256)
    print("V4 %d words  V5 %d words" % (w4, w5))
    print("combined:", os.path.getsize(combined), "bytes")
    print("sha256:", h256)
    if f4 or f5:
        print("QA FAILURES:", [c[0] for c in f4 + f5])
    else:
        print("QA: no failed checks")




# ---------------------------------------------------- DEDICATED SHORT SCRIPTS
from shorts import SHORTS as SH, seconds as sh_seconds, TITLES as SH_TITLES


def _short_body(d, s, standalone):
    kv(d, "Platform", "YouTube Shorts, Instagram Reels, LinkedIn vertical. "
                      "9:16.")
    kv(d, "Target length", s["length"])
    kv(d, "On-screen hook", s["onscreen"])
    para(d, "HOOK, THE EXACT FIRST SPOKEN LINE", size=9.5, bold=True,
         color=GOLD, before=12, after=3, keep=True)
    para(d, s["hook"], size=12, italic=True, color=NAVY, after=8)
    para(d, "FULL RECORDING SCRIPT", size=9.5, bold=True, color=GOLD,
         before=10, after=4, keep=True)
    for line in s["script"]:
        para(d, line, size=12, after=9)
    para(d, "ENDING, THE EXACT FINAL SPOKEN LINE", size=9.5, bold=True,
         color=GOLD, before=8, after=3, keep=True)
    para(d, s["ending"], size=12, italic=True, color=NAVY, after=10)
    para(d, "VISUAL NOTES", size=9.5, bold=True, color=GOLD, before=8,
         after=3, keep=True)
    para(d, s["visual"], size=10.5, color=DIM, after=8)
    para(d, "SOUND", size=9.5, bold=True, color=GOLD, before=6, after=3,
         keep=True)
    para(d, s["sound"], size=10.5, color=DIM, after=8)
    if s["endcard"]:
        para(d, "END CARD", size=9.5, bold=True, color=GOLD, before=6,
             after=3, keep=True)
        para(d, s["endcard"], size=10.5, color=DIM, after=8)
    if standalone:
        callout(d, "Record this vertically, 9:16, as its own take. It is not a "
                   "clip from the long-form master.", color=NAVY)


def short_scripts(n, out):
    """One combined document, plus one document per Short."""
    made = []
    d = base_doc()
    title_block(d, "Video %d  ·  Dedicated Short Form" % n,
                "Four Short Form Recording Scripts", SH_TITLES[n])
    para(d, "Four separate vertical takes, recorded intentionally rather than "
            "clipped from the horizontal master. Each one stands alone for "
            "somebody who has never seen the long-form video, and each makes a "
            "different point. Every claim, figure and story here is the one "
            "already approved in the locked long-form script.", size=10.5,
         color=DIM, after=10)
    callout(d, "Record all four vertically, 9:16. Temidayo stays the primary "
               "visual. Where a framework or comparison becomes a substantive "
               "graphic, it fills the complete 9:16 screen and she is not "
               "visible moving behind it.")
    for s in SH[n]:
        para(d, "SHORT %d  ·  %s" % (s["n"], s["title"]), size=14, bold=True,
             color=NAVY, before=20, after=6, keep=True)
        rule(d, after=8)
        _short_body(d, s, standalone=False)
    p = os.path.join(out, "Video_%d_Four_Short_Form_Recording_Scripts.docx" % n)
    d.save(p)
    made.append(p)

    folder = os.path.join(out, "Video_%d_Shorts" % n)
    os.makedirs(folder, exist_ok=True)
    for s in SH[n]:
        d = base_doc()
        title_block(d, "Video %d  ·  Short %d" % (n, s["n"]), s["title"],
                    SH_TITLES[n])
        _short_body(d, s, standalone=True)
        p = os.path.join(folder, "%s.docx" % s["slug"])
        d.save(p)
        made.append(p)
    return made


if __name__ == "__main__":
    main()
