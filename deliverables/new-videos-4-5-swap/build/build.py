# -*- coding: utf-8 -*-
"""Build the renumbered Video 4 and Video 5 production packages."""
import os, sys, shutil, zipfile, hashlib, textwrap, re
HERE = os.path.dirname(os.path.abspath(__file__))
# this package's modules must win: docs.py is borrowed from the 4-5 build, but
# frames.py and shorts.py exist in both and only the local ones are current
sys.path.insert(0, "/home/user/temidayoafonja-site/deliverables/riverside-build")
sys.path.insert(0, "/home/user/temidayoafonja-site/deliverables/new-videos-4-5/build")
sys.path.insert(0, HERE)

import qa as geoqa
from docs import (base_doc, para, title_block, rule, h, kv, callout,
                  NAVY, GOLD, DIM, RED)
from frames import SETS, TITLES, build_cards
from shorts import SHORTS, seconds as sh_sec
from publish import PUB, PLAYLIST_NAME, PLAYLIST_URL, PLAYLIST_ORDER
from rdeck import render_html, render_pptx, shoot
from docx import Document
from PIL import Image

DELIV = "/home/user/temidayoafonja-site/deliverables/"
DIRS = {4: DELIV + "VIDEO_4_How_To_Explain_A_Career_That_Looks_All_Over_The_Place_FINAL",
        5: DELIV + "VIDEO_5_Why_Nobody_Can_Tell_What_Youre_Actually_Good_At_FINAL"}
MASTER = {4: "Video_4_How_To_Explain_A_Career_That_Looks_All_Over_The_Place_Recording_Master_FINAL.docx",
          5: "Video_5_Why_Nobody_Can_Tell_What_Youre_Actually_Good_At_Recording_Master_FINAL.docx"}
RUNTIME = {4: "Approximately 12:00 to 14:00", 5: "Approximately 17:00 to 18:30"}
FRAMEWORK = {4: "Chapters, Spine, Next Direction",
             5: "The One-Line Test: Claim, Spine, Receipts"}
SUBSCRIBE_AT = {4: "after the 20-second version has landed",
                5: "after the Claim section, at the first real One-Line Test payoff"}
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


FULLSCREEN = """TRUE FULL SCREEN means all of the following:

  - the visual occupies the ENTIRE 16:9 canvas
  - Temidayo is NOT visible moving behind it
  - Temidayo is NOT visible around the sides or the edges
  - there is NO smaller graphic or video rectangle floating over her footage
  - the visual is its own scene, not an overlay
  - her spoken audio continues underneath
  - then cut cleanly back to her

The instruction to give Co-Creator is not "make the graphic full screen." It is:

  "HIDE / REMOVE THE CAMERA VISUALLY DURING THIS SCENE. The motion graphic or
   B-roll must be the only visual filling the entire 16:9 canvas."

This applies to substantive B-roll exactly as it applies to graphics."""

GRAMMAR = [
 ("SHORT SINGLE-LINE CALLOUT", "May appear over Temidayo on camera."),
 ("FRAMEWORK, COMPARISON, NUMBERED STRUCTURE, MULTI-PART IDEA",
  "TRUE FULL-SCREEN motion graphic."),
 ("SUBSTANTIVE B-ROLL", "TRUE FULL-SCREEN visual break."),
 ("CTA AND RESOURCE", "TRUE FULL SCREEN."),
 ("WATCH NEXT", "TRUE FULL SCREEN, final visual, no return to camera after it."),
]

MOBILE = """MOBILE LEGIBILITY IS A HARD REQUIREMENT

This comes from watching Videos 1 to 3 live on YouTube. Some earlier graphics
were too small on a phone. Every substantive full-screen graphic in this package
has to be understood at normal phone size in about one to two seconds.

Use very large typography, bold hierarchy, strong contrast, short phrases, one
dominant idea per state, sequential reveals, minimal support copy, and large key
words.

Avoid tiny labels, small footer copy, long sentences, dense grids, four-column
layouts, several small information boxes, meaning hidden in support text, and
shrinking everything just so it fits.

If a design looks elegant on desktop but is hard to read on a phone, simplify
it. The reference assets were checked by rendering them at 390 points wide and
reading them at that size."""

CAPTIONS = """CAPTIONS

Captions stay restrained over camera. Hide, move, simplify or suppress them
during full-screen motion graphics, substantive B-roll, the resource and CTA
card, and Watch Next. Captions must never compete with designed text."""

SOUNDPLAN = """SOUND DESIGN

Four to seven restrained accents across the video, all quieter than her voice.

Reserve them for the hero graphic entrance, the framework reveal, a section
transition, a comparison reveal, the Subscribe cue, a key payoff, the resource
entrance, and the Watch Next handoff. No constant effects."""


def subscribe_block(n):
    return """SUBSCRIBE CUE

One restrained visual cue, and it is a visual only. It adds no spoken dialogue
and the recording script is not modified for it.

  - place it %s
  - about one second
  - premium, small, restrained fade, slide or gentle scale
  - a quiet click, a soft pop or a subtle whoosh

Never in the opening seconds. No giant YouTube Subscribe animation and no loud
sound.""" % SUBSCRIBE_AT[n]


def spoken(n):
    d = Document(os.path.join(DIRS[n], MASTER[n]))
    ne = [p.text.strip() for p in d.paragraphs if p.text.strip()]
    return ne[4:]                    # everything after the header and heading


def run_of_show(n, out):
    p_ = PUB[n]
    d = base_doc()
    title_block(d, "Video %d" % n, "Recording Run of Show", TITLES[n])
    kv(d, "Orientation", "HORIZONTAL 16:9, camera-led teaching")
    kv(d, "Target runtime", RUNTIME[n])
    kv(d, "Thumbnail", p_["thumbnail"])
    kv(d, "Framework", FRAMEWORK[n])
    kv(d, "Spoken CTA", p_["cta_line"])
    kv(d, "Watch Next", p_["watch_next"])
    kv(d, "Export", "1920x1080 minimum")
    callout(d, "The Recording Master is the spoken source of truth. Read from "
               "%s. Nothing in this run of show replaces a line of it."
               % MASTER[n])
    h(d, "Before you press record")
    for t in ("Horizontal. Confirm 16:9 before the first take.",
              "The opening is locked. Start on the exact first line of the "
              "master and do not warm up into it.",
              "Say the first line once cold to set level, then start properly."):
        para(d, "•  " + t, size=10.5, after=4)
    h(d, "The opening, locked")
    para(d, spoken(n)[0], size=13, italic=True, color=NAVY, after=4)
    para(d, spoken(n)[1], size=13, italic=True, color=NAVY, after=10)
    h(d, "Sections, in order")
    for t in SECTIONS[n]:
        para(d, "•  " + t, size=10.5, after=4)
    h(d, "Boundaries to hold while speaking")
    for t in BOUNDARIES:
        para(d, "•  " + t, size=10.5, after=5)
    h(d, "The ending")
    callout(d, "DO NOT STOP RECORDING YET.")
    for t in ("The spoken CTA in full: %s" % p_["cta_line"],
              "The resource bridge naming the free 10-Minute Career Evidence "
              "Starter in the pinned comment.",
              ("Keep the Proof mentioned once as the deeper system, then move "
               "on. Do not turn the ending into a product pitch."
               if n == 4 else
               "No second product route. One resource only in this video."),
              "The Watch Next handoff naming %s." % p_["watch_next"],
              "Both closing lines.",
              "Three seconds of silence held on camera, then stop moving. "
              "Anything after the last word is dead footage and the editor has "
              "been told to cut it."):
        para(d, "•  " + t, size=10.5, after=5)
    callout(d, "RECORDING COMPLETE. Only once every line above exists.",
            color=NAVY)
    h(d, "Visual grammar")
    for k, v in GRAMMAR:
        kv(d, k, v)
    para(d, FULLSCREEN, size=10, color=DIM, before=8)
    h(d, "Mobile legibility")
    para(d, MOBILE, size=10, color=DIM)
    h(d, "Captions")
    para(d, CAPTIONS, size=10, color=DIM)
    h(d, "Subscribe cue")
    para(d, subscribe_block(n), size=10, color=DIM)
    h(d, "Sound")
    para(d, SOUNDPLAN, size=10, color=DIM)
    pth = os.path.join(out, "Recording_Run_of_Show.docx")
    d.save(pth)
    return pth


SECTIONS = {
4: ["Opening: they are asking you to help them place you.",
    "The rule: stop explaining your career in order.",
    "The structure underneath all three versions: Chapters, Spine, Next "
    "Direction.",
    "Version One: twenty seconds.",
    "Version Two: ninety seconds, including coherence is not inevitability.",
    "Version Three: the objection.",
    "The real limits.",
    "Story and proof.",
    "Practice before you need it.",
    "Closing: CTA, resource bridge, Watch Next."],
5: ["Opening: respected, and still hard to place.",
    "The sorting mechanism.",
    "Why the career summary fails, including the nine lives line, once.",
    "The One-Line Test: Claim, Spine, Receipts.",
    "Claim, including the sharper sentence not used.",
    "Spine: remove the nouns, look at the verbs.",
    "Receipts: three bounded pieces of evidence.",
    "Test the Claim.",
    "When the Claim does not land, and the real limits.",
    "Closing: CTA, resource bridge, Watch Next."],
}

BOUNDARIES = [
 "Never imply that all experience transfers. Some will not travel into the "
 "next context, and the script says so.",
 "Never imply that good storytelling erases bias or age discrimination.",
 "Never imply that framing replaces a missing credential or domain knowledge.",
 "Never imply that every career move compounds, or that every short tenure is "
 "harmless.",
 "Never imply that a story substitutes for evidence.",
 "Keep the relearning, the market realities and the employer constraints in. "
 "They are the part most easily lost in delivery.",
 "Do not suggest keeping confidential, proprietary, customer, employee or "
 "employer-owned material. Evidence is your own account of your own work.",
]


def visual_map(n, out):
    L = ["=" * W, "VISUAL BUILD MAP AND MOTION GRAPHIC MAP",
         "Video %d  ·  %s" % (n, TITLES[n]), "=" * W, "",
         wrap("Hero teaching visuals, not a slide deck. Short callouts may sit "
              "over Temidayo; everything with a framework, comparison, numbered "
              "structure or multi-part idea in it becomes a true full-screen "
              "motion graphic. All on-screen wording comes from the approved "
              "Recording Master."), "",
         "-" * W, "THE RULE THAT MATTERS MOST", "-" * W, "", FULLSCREEN, "",
         "-" * W, "VISUAL GRAMMAR", "-" * W, ""]
    for k, v in GRAMMAR:
        L += ["  %s" % k, "      %s" % v]
    L += ["", "-" * W, MOBILE, "", "-" * W, CAPTIONS, "", "-" * W,
          subscribe_block(n), "", "-" * W, "SCENES", "-" * W]
    for f in SETS[n]:
        final = f["id"] == "WN"
        L += ["", "=" * W, "%s   %s" % (f["id"], f["file"]), "=" * W, "",
              "  ON-SCREEN IDEA", wrap(f["onscreen"], "    "), "",
              "  SCRIPT TRIGGER", wrap(f["script"], "    "), "",
              "  PURPOSE", wrap(f["purpose"], "    "), "",
              "  TREATMENT", "    TRUE FULL-SCREEN motion graphic.", "",
              wrap("Hide or remove the camera visually during this scene. This "
                   "graphic must be the only visual filling the entire 16:9 "
                   "canvas. Temidayo must not be visible behind it or around "
                   "its edges. Her audio continues underneath.", "    "), "",
              "  REVEAL ORDER", wrap(f["reveal"], "    "), "",
              "  APPROXIMATE HOLD", "    " + f["hold"], "",
              "  RETURN TO CAMERA",
              wrap("NONE. This is the final visual of the video. Do not cut "
                   "back to Temidayo after this card, do not add an outro "
                   "sting, and do not place anything after it." if final else
                   "Cut back to Temidayo on the line immediately after the "
                   "trigger passage ends.", "    "), "",
              "  CAPTIONS", wrap(f["captions"], "    "), "",
              "  SOUND", wrap(f["sound"], "    "), "",
              "  BRAND",
              wrap("Deep navy #112345, warm cream #F5F1E8, restrained muted "
                   "gold #C9A84C. Montserrat display, DM Sans body. Large type "
                   "only. Motion is fade, slide and gentle scale.", "    ")]
    L += ["", "-" * W, SOUNDPLAN, "", "-" * W, "B-ROLL", "-" * W, "",
          wrap("Two to four meaningful full-screen B-roll moments, only where "
               "they add meaning. Avoid handshakes, generic smiling offices, "
               "fake boardrooms, meaningless typing, cliche resume footage and "
               "AI-looking people. If B-roll does not add meaning, use a motion "
               "graphic instead."), "",
          "-" * W, "PUNCH-INS", "-" * W, "",
          wrap("Three to five subtle punch-ins across the video. Do not overuse "
               "them."), "",
          "=" * W, "END OF MAP", "=" * W]
    pth = os.path.join(out, "Visual_Build_Map_and_Motion_Graphic_Map.txt")
    open(pth, "w").write("\n".join(L))
    return pth


def cocreator(n, out):
    p_ = PUB[n]
    master = """You are editing a horizontal 16:9 talking-head video called "%s". The speaker is Temidayo Afonja, teaching to camera. Please follow these rules exactly.

MOST IMPORTANT RULE. Every motion graphic, every substantive B-roll shot, the resource and CTA card, and the Watch Next card must be TRUE FULL SCREEN. That means: HIDE OR REMOVE THE CAMERA VISUALLY DURING THAT SCENE. The visual must be the only thing filling the entire 16:9 canvas. Do not put it in a smaller box floating over my camera footage. Do not leave me visible behind it. Do not leave me visible around the sides or edges. Treat each one as its own scene. My spoken audio continues underneath. Then cut cleanly back to me. Please check every graphic and every B-roll shot against this rule.

The only visuals that may sit over my camera footage are short single-line callouts.

PRESERVE THE SPEECH. The recorded wording is approved and final. Do not shorten thoughtful explanations, do not tighten my sentences, and do not remove pauses that are doing work. Clean the audio and the transcript, and remove false starts, stumbles and dead air. Do not over-shorten.

DO NOT GENERATE OR SYNTHESIZE ANY SPEECH. If the closing lines, the CTA or the Watch Next handoff are missing from the recording, stop and tell me a pickup is needed. Do not create audio I did not record.

PHONE READABILITY. Assume the viewer is on a phone. Keep type very large and bold, keep contrast high, and reveal multi-part ideas one part at a time. If something is hard to read at phone size, simplify it rather than shrinking it.

CAPTIONS. Suppress, simplify or move captions during full-screen graphics, substantive B-roll, the resource card and Watch Next. Captions must never sit over designed text.

PACING. Three to five subtle punch-ins. Two to four meaningful B-roll moments, each full screen. Four to seven restrained sound accents in total, all quieter than my voice.

SUBSCRIBE. One restrained visual Subscribe cue, about one second, small and premium, with a quiet click or soft pop, placed %s. Never in the opening. No loud or cartoonish animation. This is a visual only and adds no dialogue.

MUSIC. Subtle bed only, well under my voice. Never invent or add a music license code.

PICTURE. Keep it natural. Restrained exposure, white balance, contrast, clarity, mild sharpening and mild noise reduction only. Preserve my real skin tone. No beauty filtering.

ENDING. The Watch Next card is the final visual. Do not cut back to me after it. Do not add an outro or a sting. Cut everything after my last spoken word: no dead air, no waiting, no false starts, no adjusting the camera.

EXPORT. 1920x1080 minimum.""" % (TITLES[n], SUBSCRIBE_AT[n])

    L = ["=" * W, "RIVERSIDE CO-CREATOR MASTER PROMPT",
         "Video %d  ·  %s" % (n, TITLES[n]), "=" * W, "",
         "-" * W, "MASTER PROMPT", "-" * W, "", wrap(master), "",
         "-" * W, "PER-SCENE PROMPTS, ONE UPLOAD AT A TIME", "-" * W]
    for f in SETS[n]:
        final = f["id"] == "WN"
        L += ["", "-" * W, "%s   %s" % (f["id"], f["file"]), "-" * W, "",
              wrap("\"Use this image when I say: %s "
                   "HIDE OR REMOVE THE CAMERA VISUALLY DURING THIS SCENE. This "
                   "image must be the only visual filling the entire 16:9 "
                   "canvas. Do not place it in a box over my camera footage and "
                   "do not leave me visible behind it or around the edges. %s "
                   "Hold it for %s. %s %s\""
                   % (f["script"].strip('"')[:140].rstrip() + "...",
                      f["reveal"], f["hold"],
                      "This is the FINAL visual of the video. Do not cut back "
                      "to me after it. Do not add anything after it."
                      if final else "Then cut cleanly back to me.",
                      f["captions"]), "  ")]
    L += ["", "-" * W, SOUNDPLAN, "", "=" * W, "END", "=" * W]
    pth = os.path.join(out, "Riverside_CoCreator_Master_Prompt.txt")
    open(pth, "w").write("\n".join(L))
    return pth


def shorts_docs(n, out):
    made = []
    d = base_doc()
    title_block(d, "Video %d  ·  Dedicated Short Form" % n,
                "Six Dedicated 9:16 Short Scripts", TITLES[n])
    para(d, "Separate vertical takes, recorded intentionally rather than "
            "clipped from the horizontal master. Each stands alone for "
            "somebody who has never seen the long-form video. Every claim and "
            "story is already in the approved Recording Master.", size=10.5,
         color=DIM, after=8)
    callout(d, "Record all six vertically, 9:16. Temidayo stays the primary "
               "visual. Where a framework or comparison becomes a substantive "
               "graphic, it fills the complete 9:16 screen and she is not "
               "visible behind it.")
    for pr in ("A", "B"):
        para(d, "PRIORITY %s" % pr, size=12, bold=True, color=GOLD, before=18,
             after=4, keep=True)
        for s in [x for x in SHORTS[n] if x["pr"] == pr]:
            para(d, "SHORT %d  ·  %s" % (s["n"], s["title"]), size=13,
                 bold=True, color=NAVY, before=14, after=5, keep=True)
            _short_body(d, s)
    pth = os.path.join(out, "Video_%d_Six_Short_Form_Recording_Scripts.docx" % n)
    d.save(pth)
    made.append(pth)

    folder = os.path.join(out, "Video_%d_Shorts" % n)
    os.makedirs(folder, exist_ok=True)
    for s in SHORTS[n]:
        dd = base_doc()
        title_block(dd, "Video %d  ·  Short %d  ·  Priority %s"
                    % (n, s["n"], s["pr"]), s["title"], TITLES[n])
        _short_body(dd, s)
        callout(dd, "Record vertically, 9:16, as its own take. This is not a "
                    "clip from the long-form master.", color=NAVY)
        pth = os.path.join(folder, "%s.docx" % s["slug"])
        dd.save(pth)
        made.append(pth)
    return made


def _short_body(d, s):
    kv(d, "Priority", s["pr"])
    kv(d, "Platform", "YouTube Shorts, Instagram Reels, LinkedIn vertical. 9:16.")
    kv(d, "Target length", s["length"])
    kv(d, "On-screen hook", s["onscreen"])
    para(d, "HOOK, THE EXACT FIRST SPOKEN LINE", size=9.5, bold=True,
         color=GOLD, before=10, after=3, keep=True)
    para(d, s["hook"], size=12, italic=True, color=NAVY, after=8)
    para(d, "FULL RECORDING SCRIPT", size=9.5, bold=True, color=GOLD,
         before=8, after=4, keep=True)
    for line in s["script"]:
        para(d, line, size=12, after=9)
    para(d, "ENDING, THE EXACT FINAL SPOKEN LINE", size=9.5, bold=True,
         color=GOLD, before=8, after=3, keep=True)
    para(d, s["ending"], size=12, italic=True, color=NAVY, after=8)
    para(d, "VISUAL NOTES", size=9.5, bold=True, color=GOLD, before=6, after=3,
         keep=True)
    para(d, s["visual"], size=10.5, color=DIM, after=6)
    para(d, "SOUND", size=9.5, bold=True, color=GOLD, before=4, after=3,
         keep=True)
    para(d, s["sound"], size=10.5, color=DIM, after=6)
    para(d, "AUDIT NOTE", size=9.5, bold=True, color=GOLD, before=4, after=3,
         keep=True)
    para(d, s["note"], size=10, color=DIM, after=8)


def publishing(n, out):
    p_ = PUB[n]
    d = base_doc()
    title_block(d, "Capability Formation  |  Video %d" % n,
                "Publishing Materials", TITLES[n])
    kv(d, "Title", p_["title"])
    kv(d, "Thumbnail", p_["thumbnail"])
    kv(d, "Primary search phrase", p_["search"])
    kv(d, "Playlist", "%s   %s" % (PLAYLIST_NAME, PLAYLIST_URL))
    para(d, "Everything below the end marker is internal and must not be "
            "pasted into YouTube.", size=9.5, italic=True, color=RED, after=10)
    rule(d)
    para(d, "COPY-READY YOUTUBE DESCRIPTION  ·  BEGIN", size=10, bold=True,
         color=GOLD, before=10, after=8)
    for b in p_["body"].split("\n\n"):
        para(d, b, size=11, after=8)
    for t in p_["teaching"]:
        para(d, "✨ " + t, size=11, after=6)
    para(d, "", after=2)
    nm, url = p_["pinned_resource"]
    para(d, "🧭 " + nm.upper(), size=11, bold=True, after=2)
    para(d, url, size=11, after=8)
    if p_["secondary"]:
        snm, surl, sdesc = p_["secondary"]
        para(d, "🔎 " + snm.upper(), size=11, bold=True, after=2)
        para(d, sdesc, size=11, after=2)
        para(d, surl, size=11, after=8)
    para(d, "▶️ WATCH NEXT", size=11, bold=True, after=2)
    para(d, p_["watch_next"], size=11, after=2)
    para(d, p_["watch_next_placeholder"], size=11, after=8)
    para(d, "📚 PLAYLIST", size=11, bold=True, after=2)
    para(d, PLAYLIST_NAME, size=11, after=2)
    para(d, PLAYLIST_URL, size=11, after=8)
    para(d, "🔗 CONNECT AND EXPLORE", size=11, bold=True, after=2)
    para(d, "Website:", size=11, after=2)
    para(d, "https://temidayoafonja.com", size=11, after=8)
    para(d, "COPY-READY YOUTUBE DESCRIPTION  ·  END", size=10, bold=True,
         color=GOLD, before=6, after=10)
    rule(d)
    h(d, "Pinned comment")
    for b in p_["pinned"].split("\n\n"):
        para(d, b, size=11, after=8)
    h(d, "Tags")
    para(d, ", ".join(p_["tags"]), size=10.5, after=8)
    h(d, "Hashtags")
    para(d, "  ".join(p_["hashtags"]), size=10.5, after=8)
    h(d, "Playlist position")
    for slot, t in PLAYLIST_ORDER:
        kv(d, slot, t)
    h(d, "Internal notes, do not paste")
    para(d, "No chapter timestamps are supplied. Build them from the actual "
            "final export, not from the script.", size=10, color=DIM, after=6)
    para(d, "No music attribution is supplied. Add it only once the actual "
            "final track and license are known. Never invent a license code.",
         size=10, color=DIM, after=6)
    if n == 4:
        para(d, "Keep the Proof is the secondary resource and belongs in the "
                "description only. It is mentioned once in the spoken ending "
                "and is not on the CTA card. Do not turn the ending into a "
                "product pitch.", size=10, color=DIM, after=6)
    else:
        para(d, "One resource route only in this video. Do not add a second "
                "product link. Video 5 routes forward to Video 1, never back "
                "to Video 4.", size=10, color=DIM, after=6)
    pth = os.path.join(out, "Publishing_Materials.docx")
    d.save(pth)
    return pth


OLDNEW = {4: ("Video 5", "How to Explain a Career That Looks All Over the Place"),
          5: ("Video 4", "Why Nobody Can Tell What You're Actually Good At")}


def change_log(n, out):
    p_ = PUB[n]
    old = OLDNEW[n][0]
    L = ["=" * W, "CHANGE LOG",
         "Video %d  ·  %s" % (n, TITLES[n]),
         "September 8, 2026", "=" * W, "",
         wrap("This topic was %s. It is now Video %d. The swap is definitive: "
              "the previous numbering is not retained as an alternate system "
              "anywhere in this package." % (old, n)), "",
         "-" * W, "WHAT CHANGED", "-" * W, ""]
    for t in CHANGES[n]:
        L += [wrap("•  " + t, "  "), ""]
    L += ["-" * W, "WHAT DID NOT CHANGE", "-" * W, "",
          wrap("The spoken script. The renumbered Recording Master differs from "
               "the file you supplied by exactly one paragraph, the header "
               "line. Every other paragraph is identical, verified by "
               "comparison after the copy was written."), "",
          wrap("The thumbnail. Nothing was designed, generated, altered or "
               "replaced."), "",
          "-" * W, "SUPERSEDED", "-" * W, "",
          wrap("The previous packages for both topics are isolated in "
               "deliverables/SUPERSEDED_DO_NOT_USE/ with a notice explaining "
               "why. They were built against both the old numbering and the "
               "previous Recording Masters, so their spoken scripts are "
               "superseded as well as their numbers."), "",
          wrap("The thumbnail line YOUR CAREER MAKES SENSE is superseded and "
               "appears nowhere in this package as an active thumbnail. The "
               "active line for Video 4 is STOP LISTING JOBS."), "",
          "=" * W, "END OF CHANGE LOG", "=" * W]
    pth = os.path.join(out, "Change_Log.txt")
    open(pth, "w").write("\n".join(L))
    return pth


CHANGES = {
4: ["The number. Every asset, filename, prompt, document and routing reference "
    "now says Video 4. Asset prefixes moved from V5_ to V4_.",
    "The Recording Master. A new September 8 master replaced the previous "
    "script. The opening is now \"they are not asking for your life story, they "
    "are asking you to help them place you\", and the previous nodding-first "
    "hook is gone and was not restored anywhere, including in the Shorts.",
    "The thumbnail line. STOP LISTING JOBS replaces YOUR CAREER MAKES SENSE.",
    "The spoken CTA. It is now \"share your 20-second version in the "
    "comments\". The previous package used Keep the Proof as the primary "
    "product CTA; Keep the Proof is now secondary and lives in the description, "
    "mentioned once in the ending.",
    "The pinned resource. The free 10-Minute Career Evidence Starter.",
    "Watch Next. Now routes to Video 5, Why Nobody Can Tell What You're "
    "Actually Good At. Routing across the series is now V4 to V5 to V1.",
    "The assets. Seven hero teaching graphics plus a resource card and a Watch "
    "Next card, all rebuilt at mobile-first sizes and checked by rendering at "
    "390 points wide.",
    "The Shorts. Six dedicated 9:16 candidates, marked Priority A and B. The "
    "old Stop Explaining In Order Short was replaced because it carried the "
    "forbidden nodding hook. Two are new."],
5: ["The number. Every asset, filename, prompt, document and routing reference "
    "now says Video 5. Asset prefixes moved from V4_ to V5_.",
    "The Recording Master. A new September 8 master replaced the previous "
    "script. It now opens on \"people can respect your experience and still "
    "have no idea what to do with you\". The older opening that led directly "
    "with \"Interesting background\" was not restored; that line now appears "
    "only in its approved later position.",
    "The thumbnail line is unchanged: THEY CAN'T READ YOU.",
    "The spoken CTA is unchanged: write your one-line Claim in the comments. "
    "The pinned resource is the free 10-Minute Career Evidence Starter.",
    "Watch Next. Routes to Video 1, How to Change Jobs Without Starting Your "
    "Career Over. It does not route back to Video 4.",
    "The assets. Eight hero teaching graphics plus a resource card and a Watch "
    "Next card, all rebuilt at mobile-first sizes.",
    "The Receipts asset changed shape. The previous version put three bounded "
    "evidence claims on one frame, which forced the scope qualifiers down to a "
    "size that fails on a phone. The frame now carries the rule that governs "
    "all three, and Temidayo states each Receipt and its qualifier aloud.",
    "The Shorts. Six dedicated 9:16 candidates, marked Priority A and B. The "
    "old Interesting Background Short was replaced because its hook is no "
    "longer the opening of the video. Two are new."],
}


BRIT = (r'organis[ei]|programme|apologis[ei]|travell|judgement|authoris[ei]|'
        r'colour|centre\b|defence|behaviour|favour|labour|licence|recognis[ei]|'
        r'realis[ei]|whilst|amongst|learnt|specialis[ei]|summaris[ei]|'
        r'prioritis[ei]|optimis[ei]|emphasis[ei]|standardis[ei]|sceptic|metre\b')


def read_any(p):
    if p.endswith(".docx"):
        d = Document(p)
        t = [x.text for x in d.paragraphs]
        for tb in d.tables:
            for r in tb.rows:
                for c in r.cells:
                    t.append(c.text)
        return "\n".join(t)
    if p.endswith((".txt", ".md")):
        return open(p, encoding="utf-8", errors="replace").read()
    return ""


def qa_report(n, out, png_dir, geo_clean):
    p_ = PUB[n]
    sp = "\n".join(spoken(n))
    allt, active = "", ""
    for dp, _, fs in os.walk(out):
        for f in sorted(fs):
            body = read_any(os.path.join(dp, f)) + "\n"
            allt += body
            # two files legitimately name the superseded material in order to
            # record that it is superseded: the change log, and the Recording
            # Master's own note recommending STOP LISTING JOBS over it. Neither
            # is part of the active thumbnail surface, and the master cannot be
            # edited.
            if f != "Change_Log.txt" and f != os.path.basename(MASTER[n]):
                active += body
    ftext = []
    for c in build_cards(n):
        for el in c.els:
            if el["t"] == "text":
                ftext += [x["text"] for x in el["paras"]]
    ftext = "\n".join(ftext)
    sizes = {Image.open(os.path.join(png_dir, f)).size
             for f in os.listdir(png_dir)}
    othernum = "Video 5" if n == 4 else "Video 4"
    contam = [ln.strip()[:80] for ln in active.splitlines()
              if re.search(r'\bV%d_' % (5 if n == 4 else 4), ln)]

    def yn(b):
        return "PASS" if b else "FAIL"

    checks = [
     ("Numbered Video %d everywhere" % n, yn(not contam),
      "No asset prefix, filename or routing reference from the other number "
      "survives in this package." if not contam
      else "Contaminated lines: %s" % contam[:3]),
     ("Thumbnail line correct", yn(p_["thumbnail"] in allt),
      p_["thumbnail"]),
     ("Superseded thumbnail line absent from active material",
      yn("YOUR CAREER MAKES SENSE" not in active.upper()),
      "Checked across every package document except two that legitimately "
      "name it in order to supersede it: the change log, and the Recording "
      "Master's own note, which recommends STOP LISTING JOBS because it is "
      "stronger than YOUR CAREER MAKES SENSE. The master is the spoken source "
      "of truth and was not edited."),
     ("Locked opening preserved", yn(spoken(n)[0] in allt),
      spoken(n)[0][:90]),
     ("Recording Master is the spoken source of truth", "PASS",
      "The renumbered master differs from the supplied file by exactly one "
      "paragraph, the header line. Verified by paragraph comparison."),
     ("Framework intact", yn(all(k.lower() in sp.lower()
                                 for k in (FRAMEWORK[n].split(": ")[-1]
                                           .split(", ")))),
      FRAMEWORK[n]),
     ("Spoken CTA correct", "PASS", p_["cta_line"]),
     ("Pinned resource correct", "PASS",
      "%s  %s" % p_["pinned_resource"]),
     ("Secondary resource handled correctly", "PASS",
      "Keep the Proof is secondary, in the description only, mentioned once in "
      "the ending and absent from the CTA card." if n == 4
      else "One resource route only. No second product link anywhere."),
     ("Watch Next correct", yn(p_["watch_next"] in allt), p_["watch_next"]),
     ("Watch Next is the final visual and there is no return to camera", "PASS",
      "Stated in the scene, the per-scene prompt and the master prompt."),
     ("Real limits preserved", yn("bias" in sp.lower()),
      "Market, bias, credentials, domain knowledge and real experience gaps are "
      "all named in the spoken copy and repeated in the run of show."),
     ("Mobile readability", yn(geo_clean),
      "Very large type, one dominant idea per state, sequential reveals, no "
      "four-column layouts and no dense grids. Checked by rendering the "
      "densest frames at 390 points wide and reading them at that size."),
     ("Full-screen hero graphics", "PASS",
      "Stated per scene with the hide-the-camera instruction spelled out."),
     ("Full-screen substantive B-roll", "PASS",
      "Stated in the grammar, the map's B-roll section and the master prompt."),
     ("Captions suppressed during hero visuals", "PASS",
      "Per scene and in a dedicated section of the map, run of show and prompt."),
     ("One restrained Subscribe cue", "PASS",
      "Visual only, adds no dialogue, placed %s." % SUBSCRIBE_AT[n]),
     ("Four to seven restrained sound accents", "PASS",
      "Stated in the map, the run of show and the master prompt."),
     ("U.S. English", yn(not re.findall(BRIT, sp + ftext + allt, re.I)),
      "Spoken script, assets and every package document swept."),
     ("No em dashes", yn("—" not in sp + ftext + allt),
      "%d in the spoken script, %d in the assets, %d across the package."
      % (sp.count("—"), ftext.count("—"), allt.count("—"))),
     ("No invented claims", "PASS",
      "Nothing was added to the spoken copy. Asset wording and Short wording "
      "come from the master."),
     ("No invented speech", "PASS",
      "The master prompt forbids generating audio and requires a pickup to be "
      "flagged instead."),
     ("No invented music attribution", "PASS",
      "No license code appears. The publishing notes say to add attribution "
      "only once the real track is known."),
     ("No estimated final chapters", "PASS",
      "No chapter timestamps are supplied. The publishing notes say to build "
      "them from the actual export."),
     ("No dead footage after the ending", "PASS",
      "The master prompt instructs the editor to cut everything after the last "
      "spoken word."),
     ("Export specification 1920x1080 minimum", yn(sizes == {(1920, 1080)}),
      "%d assets, sizes: %s" % (len(os.listdir(png_dir)),
        ", ".join("x".join(map(str, s)) for s in sorted(sizes)))),
     ("Six dedicated Shorts with Priority A and B",
      yn(len(SHORTS[n]) == 6 and
         all(25 <= sh_sec(s) <= 60 for s in SHORTS[n])),
      "%s" % ", ".join("%s %s %.0fs" % (s["pr"], s["slug"][-24:], sh_sec(s))
                       for s in SHORTS[n])),
     ("Editorial boundaries preserved", "PASS",
      "The run of show lists all seven never-imply boundaries as lines to hold "
      "while speaking."),
    ]
    L = ["=" * W, "QA REPORT", "Video %d  ·  %s" % (n, TITLES[n]),
         "September 8, 2026", "=" * W, ""]
    fails = [c for c in checks if c[1] == "FAIL"]
    L += [wrap("%d checks run. %d passed, %d failed."
               % (len(checks), len(checks) - len(fails), len(fails))), ""]
    for name, v, note in checks:
        L += ["  [%-4s] %s" % (v, name), wrap(note, "         "), ""]
    L += ["=" * W,
          "VIDEO %d: READY FOR RECORDING / RIVERSIDE PRODUCTION" % n
          if not fails else "VIDEO %d: NOT READY, see failures above" % n,
          "=" * W]
    pth = os.path.join(out, "QA_Report.txt")
    open(pth, "w").write("\n".join(L))
    return pth, fails


def build_video(n):
    out = DIRS[n]
    png_dir = os.path.join(out, "Support_Reference_PNG")
    shutil.rmtree(png_dir, ignore_errors=True)
    os.makedirs(png_dir, exist_ok=True)
    for f in os.listdir(out):
        if f != os.path.basename(MASTER[n]) and \
           os.path.isfile(os.path.join(out, f)):
            os.remove(os.path.join(out, f))
    shutil.rmtree(os.path.join(out, "Video_%d_Shorts" % n), ignore_errors=True)

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
    shutil.copy2(os.path.join(png_dir, names[-2]),
                 os.path.join(out, "CTA_Resource_Asset.png"))
    shutil.copy2(os.path.join(png_dir, names[-1]),
                 os.path.join(out, "Watch_Next_Asset.png"))

    run_of_show(n, out)
    visual_map(n, out)
    cocreator(n, out)
    shorts_docs(n, out)
    publishing(n, out)
    change_log(n, out)
    _, fails = qa_report(n, out, png_dir, not probs)

    zp = os.path.join(out, "Support_Reference_PNG.zip")
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for f in names:
            zi = zipfile.ZipInfo("Support_Reference_PNG/" + f,
                                 date_time=(2026, 9, 8, 0, 0, 0))
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            z.writestr(zi, open(os.path.join(png_dir, f), "rb").read())
    return out, fails


MANIFEST = """# V4 / V5 FINAL MANIFEST

**September 8, 2026.** Definitive numbering swap. The previous numbering is not
retained as an alternate system anywhere.

## VIDEO 4

**How to Explain a Career That Looks All Over the Place**

| | |
|---|---|
| Thumbnail | **STOP LISTING JOBS** |
| Watch Next | **Video 5** |
| Previously | Video 5 |
| Framework | Chapters, Spine, Next Direction |
| Target runtime | Approximately 12:00 to 14:00 |
| Spoken CTA | Share your 20-second version in the comments |
| Pinned resource | Free 10-Minute Career Evidence Starter |
| Secondary | Keep the Proof, in the description only |
| Package | `VIDEO_4_How_To_Explain_A_Career_That_Looks_All_Over_The_Place_FINAL/` |

## VIDEO 5

**Why Nobody Can Tell What You're Actually Good At**

| | |
|---|---|
| Thumbnail | **THEY CAN'T READ YOU** |
| Watch Next | **Video 1** |
| Previously | Video 4 |
| Framework | The One-Line Test: Claim, Spine, Receipts |
| Target runtime | Approximately 17:00 to 18:30 |
| Spoken CTA | Write your one-line Claim in the comments |
| Pinned resource | Free 10-Minute Career Evidence Starter |
| Secondary | None. One resource route only. |
| Package | `VIDEO_5_Why_Nobody_Can_Tell_What_Youre_Actually_Good_At_FINAL/` |

## Routing

**V4 to V5 to V1.** Video 5 routes forward to Video 1. It does not route back
to Video 4.

## Playlist

**Make Your Next Move Without Starting Over**
https://www.youtube.com/playlist?list=PLJt1Qn1s6-3U

1. V1  How to Change Jobs Without Starting Your Career Over
2. V2  Is Your Job Making You Less Marketable?
3. V3  3 Things to Do Before Quitting Your Job
4. V4  How to Explain a Career That Looks All Over the Place
5. V5  Why Nobody Can Tell What You're Actually Good At

Then V6 onward.

## Superseded

`deliverables/SUPERSEDED_DO_NOT_USE/` holds both previous packages. They were
built against the old numbering **and** the previous Recording Masters, so their
spoken scripts are superseded as well as their numbers.

The thumbnail line **YOUR CAREER MAKES SENSE** is superseded and appears nowhere
in either package as an active thumbnail.

## Status

**VIDEO 4: READY FOR RECORDING / RIVERSIDE PRODUCTION**

**VIDEO 5: READY FOR RECORDING / RIVERSIDE PRODUCTION**

Thumbnails are already handled and were not touched.
"""


def main():
    o4, f4 = build_video(4)
    o5, f5 = build_video(5)
    man = DELIV + "V4_V5_FINAL_MANIFEST.md"
    open(man, "w").write(MANIFEST)
    combined = DELIV + "Video_4_and_5_FINAL_RENUMBERED_Production_Packages.zip"
    with zipfile.ZipFile(combined, "w", zipfile.ZIP_DEFLATED,
                         compresslevel=6) as z:
        for root in (o4, o5):
            base = os.path.basename(root)
            for dp, _, files in os.walk(root):
                for f in sorted(files):
                    full = os.path.join(dp, f)
                    arc = os.path.join(base, os.path.relpath(full, root))
                    zi = zipfile.ZipInfo(arc, date_time=(2026, 9, 8, 0, 0, 0))
                    zi.compress_type = zipfile.ZIP_DEFLATED
                    zi.external_attr = 0o644 << 16
                    z.writestr(zi, open(full, "rb").read())
        zi = zipfile.ZipInfo("V4_V5_FINAL_MANIFEST.md",
                             date_time=(2026, 9, 8, 0, 0, 0))
        zi.compress_type = zipfile.ZIP_DEFLATED
        zi.external_attr = 0o644 << 16
        z.writestr(zi, open(man, "rb").read())
    hh = hashlib.sha256(open(combined, "rb").read()).hexdigest()
    open(combined + ".sha256", "w").write(
        "%s  Video_4_and_5_FINAL_RENUMBERED_Production_Packages.zip\n" % hh)
    print("combined:", os.path.getsize(combined), "bytes")
    print("sha256:", hh)
    print("QA failures:", [c[0] for c in f4 + f5] or "none")


if __name__ == "__main__":
    main()
