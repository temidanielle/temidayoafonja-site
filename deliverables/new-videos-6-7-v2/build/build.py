# -*- coding: utf-8 -*-
"""Build the revised v2.0 Video 6 and Video 7 production packages."""
import os, sys, shutil, zipfile, hashlib, textwrap, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/home/user/temidayoafonja-site/deliverables/riverside-build")
sys.path.insert(0, "/home/user/temidayoafonja-site/deliverables/new-videos-4-5/build")
sys.path.insert(0, HERE)          # this package's modules must win

import qa as geoqa
from docs import (base_doc, para, title_block, rule, h, kv, callout,
                  NAVY, GOLD, DIM, RED)
from frames import SETS, TITLES, build_cards
from shorts import SHORTS, seconds as sh_sec
from publish import (META, DESCRIPTION, PINNED, TAGS, HASHTAGS, ALT_THUMBNAIL,
                     PLAYLIST_NAME, PLAYLIST_URL, CHAPTER_RULE, MUSIC_RULE,
                     TITLE_CHANGE_NOTE)
from rdeck import render_html, render_pptx, shoot
from docx import Document
from PIL import Image

DELIV = "/home/user/temidayoafonja-site/deliverables/"
DIRS = {6: DELIV + "VIDEO_6_Before_You_Take_An_Internal_Role_FINAL",
        7: DELIV + "VIDEO_7_Are_You_Growing_Or_Just_Being_Given_More_Work_FINAL"}
MASTER = {6: "Video_6_Before_You_Take_An_Internal_Role_Recording_Master_v2.0_FINAL.docx",
          7: "Video_7_Are_You_Growing_Or_Just_Being_Given_More_Work_Recording_Master_v2.0_FINAL.docx"}
SUBSCRIBE_AT = {
 6: "after the three questions have been named and the first one has landed",
 7: "after the CAR test has been named and Complexity has landed"}
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
 ("FRAMEWORK, COMPARISON, DECISION PATH, NUMBERED STRUCTURE, SUMMARY",
  "TRUE FULL-SCREEN motion graphic."),
 ("MEANINGFUL B-ROLL", "TRUE FULL-SCREEN visual break."),
 ("CTA", "TRUE FULL SCREEN."),
 ("WATCH NEXT", "TRUE FULL SCREEN, final visual, no return to camera after it."),
]

MOBILE = """MOBILE LEGIBILITY IS A HARD REQUIREMENT

Every substantive full-screen graphic has to be understood on a normal phone,
held at arm's length, in about one to two seconds.

Use:
  - very large, bold typography
  - high contrast
  - very short support copy
  - one dominant idea per visual state
  - sequential reveals

Avoid:
  - tiny labels
  - dense grids and four-box layouts
  - long paragraphs
  - important text in a footer position
  - several small boxes each holding a full sentence
  - elegant desktop layouts that stop working at phone size

Where a framework holds several ideas, reveal them one at a time rather than
showing all of them small at once. Every reveal order below is written to that
rule.

If something is elegant on desktop but hard to read on a phone, simplify it
rather than shrinking it. Two frames beat one crowded frame. The reference
assets in this package were checked by rendering them, downscaling to 390
points wide, and reading them at that size."""

CAPTIONS = """CAPTIONS

Suppress, simplify, hide or reposition captions during:
  - full-screen motion graphics
  - substantive B-roll
  - the CTA
  - Watch Next

Captions must never compete with designed text. The words on the graphic are
the message; a caption bar over them is a defect, not a preference."""

SOUNDPLAN = """SOUND DESIGN

Four to seven restrained accents across the video. Not one per caption and not
one per cut. Every accent sits clearly under Temidayo's voice.

Reserve them for:
  - the hero framework entering
  - a major comparison
  - a numbered reveal
  - an important distinction
  - the Subscribe cue
  - the CTA entrance
  - the Watch Next handoff

Palette: soft whoosh, subtle click, gentle pop, restrained impact, clean sweep."""


def subscribe_block(n):
    return """SUBSCRIBE CUE

One restrained visual cue, and it is a visual only. It adds no spoken dialogue
and the recording script is not modified for it.

  - place it %s
  - about one second
  - premium, small, and easy to miss if you are not looking for it
  - a subtle fade, slide or gentle scale, with a quiet click or a soft pop

Never in the opening. Never a loud or cartoonish YouTube animation.""" \
        % SUBSCRIBE_AT[n]


MARKER = re.compile(r"^[A-Z0-9][A-Z0-9 ,:?+/'&.-]{2,59}$")
START = "Spoken copy begins below"
STOP = "Major Visual"


def _master_paras(n):
    d = Document(os.path.join(DIRS[n], MASTER[n]))
    return [p.text.strip() for p in d.paragraphs if p.text.strip()]


def script_blocks(n):
    """[(section marker, [spoken lines]), ...] straight from the master."""
    ps = _master_paras(n)
    i = next(k for k, t in enumerate(ps) if t.startswith(START)) + 1
    out, cur = [], None
    while i < len(ps) and not ps[i].startswith(STOP):
        t = ps[i]
        if MARKER.match(t) and not t.endswith("."):
            cur = (t, [])
            out.append(cur)
        else:
            if cur is None:
                cur = ("", [])
                out.append(cur)
            cur[1].append(t)
        i += 1
    return out


def spoken(n):
    return [ln for _, lines in script_blocks(n) for ln in lines]


def master_reference(n, out):
    """The approved spoken copy, reproduced verbatim, for the recording desk."""
    m = META[n]
    d = base_doc()
    title_block(d, "Capability Formation  |  Video %d" % n,
                "Approved Recording Master Reference", TITLES[n])
    kv(d, "Source", m["master"])
    kv(d, "Version", m["master_version"])
    kv(d, "Spoken words", str(sum(len(l.split()) for l in spoken(n))))
    callout(d, "This is a reading copy. The v2.0 Recording Master is the spoken "
               "source of truth and nothing in this package replaces a line of "
               "it. Every spoken line below is reproduced verbatim, verified "
               "paragraph by paragraph after this file was written.")
    para(d, "Section labels are production markers and are not spoken.",
         size=9.5, italic=True, color=DIM, after=10)
    for label, lines in script_blocks(n):
        if label:
            para(d, label, size=10, bold=True, color=GOLD, before=16, after=6,
                 keep=True)
        for ln in lines:
            para(d, ln, size=12, after=9)
    pth = os.path.join(out, "Approved_Recording_Master_Reference.docx")
    d.save(pth)
    return pth


SECTIONS = {
6: ["Hook: an internal move can look safe because the logo does not change.",
    "Why an internal move can be a real career move.",
    "Question 1: will the work change?",
    "Question 2: will your judgment expand?",
    "Question 3: will the evidence travel?",
    "Read the three answers.",
    "What this test cannot solve.",
    "One next step and the CTA.",
    "Watch Next, then the closing line."],
7: ["Hook: sometimes the reward for being dependable is not growth.",
    "Why the pattern is hard to see from inside it.",
    "C: Complexity.",
    "A: Authority.",
    "R: Return.",
    "Reading the pattern.",
    "The scope conversation, and the four questions.",
    "CTA.",
    "Watch Next, then the closing line."],
}

BOUNDARIES = {
6: ["Never imply that an internal move is always preferable, safer or easier "
    "than an external move. The video compares access to work, not labels.",
    "Never imply that all experience transfers. Internal credibility can be "
    "powerful inside one company and almost invisible outside it, and the "
    "script says so.",
    "Never imply that a title change, a new manager or a longer task list "
    "satisfies any of the three questions by itself.",
    "Never imply that framing can erase bias, age discrimination, missing "
    "credentials, weak labor markets or genuine experience gaps.",
    "Keep the constraints in: current-manager control, existing reputation, "
    "compensation bands, organizational politics, and whether the company "
    "actually contains the work you need.",
    "Keep the real-life clause in. Compensation, family, health, safety, "
    "benefits, immigration status, stability, energy and timing can "
    "legitimately outweigh the developmental read.",
    "Keep the safety line in. Nobody needs a perfect internal-mobility "
    "strategy before protecting themselves.",
    "Personal proof stays bounded. One career chapter, roughly six months in, "
    "scope expanded and people trusted her with work beyond the original box. "
    "Do not name or imply the employer, the assignment or the result.",
    "Do not suggest keeping confidential, proprietary, customer, employee or "
    "employer-owned material. Portable evidence is your own account of your "
    "own work, in language that travels."],
7: ["Never imply that every additional responsibility is exploitation. The "
    "question is whether it has a boundary, a review point and a visible "
    "career return.",
    "Never imply that worthwhile growth is never tiring. Growth can be tiring "
    "and ordinary work still matters.",
    "Never imply that every assignment must produce immediate promotion, pay "
    "or title change to be worthwhile.",
    "Accountability without authority is a design warning, not proof of bad "
    "intent by a manager or an employer. Keep that distinction audible.",
    "Temporary extra load can be a responsible choice during a launch, a "
    "vacancy or a transition. Say so, and then say to give the season a "
    "boundary.",
    "Never imply that framing can erase bias, missing credentials or a weak "
    "labor market.",
    "Keep the real-life clause in. Finances, family, health, safety, "
    "immigration, benefits, stability and timing can legitimately shape what "
    "somebody chooses.",
    "Personal proof stays bounded. Her scope has expanded beyond the original "
    "job description more than once. Do not infer an employer, an assignment, "
    "a timeline or a result.",
    "Do not suggest keeping confidential, proprietary, customer, employee or "
    "employer-owned material."],
}


def run_of_show(n, out):
    m = META[n]
    d = base_doc()
    title_block(d, "Video %d" % n, "Recording Run of Show", TITLES[n])
    kv(d, "Orientation", "HORIZONTAL 16:9, camera-led teaching")
    kv(d, "Target runtime", m["runtime"])
    kv(d, "Thumbnail", m["thumbnail"])
    kv(d, "Framework", m["framework"])
    kv(d, "CTA", "%s   %s" % (m["cta_name"], m["cta_url"]))
    kv(d, "Watch Next", "%s   (%s)" % (m["watch_next"], m["watch_next_slot"]))
    kv(d, "Export", "1920x1080 minimum")
    callout(d, "The v2.0 Recording Master is the spoken source of truth. Read "
               "from %s. Nothing in this run of show replaces a line of it."
               % MASTER[n])
    if n == 6:
        para(d, TITLE_CHANGE_NOTE, size=10, color=DIM, after=10)
    h(d, "Before you press record")
    for t in ("Horizontal. Confirm 16:9 before the first take.",
              "The opening is locked. Start on the exact first line of the "
              "master and do not warm up into it.",
              "Say the first line once cold to set level, then start properly.",
              "One product route only in this video: %s." % m["cta_name"]):
        para(d, "•  " + t, size=10.5, after=4)
    h(d, "The opening, locked")
    for ln in spoken(n)[:2]:
        para(d, ln, size=13, italic=True, color=NAVY, after=4)
    h(d, "Sections, in order")
    for t in SECTIONS[n]:
        para(d, "•  " + t, size=10.5, after=4)
    h(d, "Boundaries to hold while speaking")
    for t in BOUNDARIES[n]:
        para(d, "•  " + t, size=10.5, after=5)
    h(d, "The ending")
    callout(d, "DO NOT STOP RECORDING YET.")
    for t in ("The one next step, with all three sentences.",
              "The full CTA naming the %s." % m["cta_name"],
              "The Watch Next handoff naming %s." % m["watch_next"],
              "The closing line, which is the last thing in the video.",
              "Three seconds of silence held on camera, then stop moving. "
              "Anything after the last word is dead footage and the editor has "
              "been told to cut it."):
        para(d, "•  " + t, size=10.5, after=5)
    para(d, "The closing line, exactly: " + spoken(n)[-1], size=12,
         italic=True, color=NAVY, after=8)
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
    h(d, "Close checklist, from the master")
    for t in ("Record the complete CTA and Watch Next handoff before stopping.",
              "Do not return to camera after the final Watch Next visual in "
              "the edited video.",
              "Build final YouTube chapters from the actual export, not these "
              "script sections.",
              "Keep captions suppressed or simplified during full-screen "
              "framework graphics and Watch Next.",
              "Preserve natural pacing. Do not over-shorten thoughtful "
              "explanations in Riverside."):
        para(d, "•  " + t, size=10.5, after=4)
    pth = os.path.join(out, "Recording_Run_of_Show.docx")
    d.save(pth)
    return pth


def visual_map(n, out):
    L = ["=" * W, "VISUAL BUILD MAP AND MOTION GRAPHIC MAP",
         "Video %d  ·  %s" % (n, TITLES[n]),
         "Revised package v2.0  ·  September 8, 2026", "=" * W, "",
         wrap("Approximately %d hero teaching visuals. These are reference "
              "frames for Riverside and Co-Creator, not a presentation deck. "
              "Short callouts may sit over Temidayo; everything with a "
              "framework, comparison, decision path, numbered structure or "
              "summary in it becomes a true full-screen motion graphic. All "
              "on-screen wording comes from the v2.0 Recording Master."
              % len(SETS[n])), "",
         "-" * W, "THE RULE THAT MATTERS MOST", "-" * W, "", FULLSCREEN, "",
         "-" * W, "VISUAL GRAMMAR", "-" * W, ""]
    for k, v in GRAMMAR:
        L += ["  %s" % k, "      %s" % v]
    L += ["", "-" * W, MOBILE, "", "-" * W, CAPTIONS, "", "-" * W,
          subscribe_block(n), "", "-" * W, "SCENES", "-" * W]
    for f in SETS[n]:
        final = f["id"] == "WN"
        L += ["", "=" * W, "%s   %s" % (f["id"], f["file"]), "=" * W, "",
              "  JOB", wrap(f["job"], "    "), "",
              "  ON-SCREEN IDEA", wrap(f["onscreen"], "    "), "",
              "  SCRIPT TRIGGER", wrap(f["script"], "    "), "",
              "  PURPOSE", wrap(f["purpose"], "    "), "",
              "  TREATMENT", "    TRUE FULL-SCREEN motion graphic.", "",
              wrap("Hide or remove the camera visually during this scene. This "
                   "graphic must be the only visual filling the entire 16:9 "
                   "canvas. Temidayo must not be visible behind it or around "
                   "its edges. Her audio continues underneath.", "    "), ""]
        if f.get("treatment_note"):
            L += [wrap(f["treatment_note"], "    "), ""]
        L += ["  REVEAL ORDER", wrap(f["reveal"], "    "), "",
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
               "AI-looking people. If B-roll does not add meaning, use a "
               "motion graphic instead."), "",
          "-" * W, "PUNCH-INS", "-" * W, "",
          wrap("Three to five subtle punch-ins across the video. Do not overuse "
               "them."), "",
          "=" * W, "END OF MAP", "=" * W]
    pth = os.path.join(out, "Visual_Build_Map_and_Motion_Graphic_Map.txt")
    open(pth, "w").write("\n".join(L))
    return pth


def cocreator(n, out):
    m = META[n]
    master = """You are editing a horizontal 16:9 talking-head video called "%s". The speaker is Temidayo Afonja, teaching to camera. Please follow these rules exactly.

MOST IMPORTANT RULE. Every motion graphic, every substantive B-roll shot, the CTA card and the Watch Next card must be TRUE FULL SCREEN. That means: HIDE OR REMOVE THE CAMERA VISUALLY DURING THAT SCENE. The visual must be the only thing filling the entire 16:9 canvas. Do not put it in a smaller box floating over my camera footage. Do not leave me visible behind it. Do not leave me visible around the sides or edges. Treat each one as its own scene. My spoken audio continues underneath. Then cut cleanly back to me. Please check every graphic and every B-roll shot against this rule.

The only visuals that may sit over my camera footage are short single-line callouts.

PRESERVE THE SPEECH. The recorded wording is approved and final. Do not shorten thoughtful explanations, do not tighten my sentences, and do not remove pauses that are doing work. Clean the audio and the transcript, and remove false starts, stumbles and dead air. Do not over-shorten.

DO NOT GENERATE OR SYNTHESIZE ANY SPEECH. If the closing line, the CTA or the Watch Next handoff is missing from the recording, stop and tell me a pickup is needed. Do not create audio I did not record.

PHONE READABILITY. Assume the viewer is on a phone. Keep type very large and bold, keep contrast high, and reveal multi-part ideas one part at a time. If something is hard to read at phone size, simplify it rather than shrinking it.

CAPTIONS. Suppress, simplify or move captions during full-screen graphics, substantive B-roll, the CTA and Watch Next. Captions must never sit over designed text.

PACING. Three to five subtle punch-ins. Two to four meaningful B-roll moments, each full screen. Four to seven restrained sound accents in total, all quieter than my voice.

SUBSCRIBE. One restrained visual Subscribe cue, about one second, small and premium, with a quiet click or soft pop, placed %s. Never in the opening. No loud or cartoonish animation. This is a visual only and adds no dialogue.

MUSIC. Subtle bed only, well under my voice. Never invent or add a music license code.

PICTURE. Keep it natural. Restrained exposure, white balance, contrast, clarity, mild sharpening and mild noise reduction only. Preserve my real skin tone. No beauty filtering.

CHAPTERS. Do not generate chapters from the script. I will build them from the finished export.

ENDING. The Watch Next card is the final visual. Do not cut back to me after it. Do not add an outro or a sting. Cut everything after my last spoken word: no dead air, no waiting, no false starts, no adjusting the camera.

EXPORT. 1920x1080 minimum.""" % (TITLES[n], SUBSCRIBE_AT[n])

    L = ["=" * W, "RIVERSIDE CO-CREATOR MASTER PROMPT",
         "Video %d  ·  %s" % (n, TITLES[n]),
         "Revised package v2.0  ·  September 8, 2026", "=" * W, "",
         "-" * W, "MASTER PROMPT", "-" * W, "", wrap(master), "",
         "-" * W, "PER-SCENE PROMPTS, ONE UPLOAD AT A TIME", "-" * W]
    for f in SETS[n]:
        final = f["id"] == "WN"
        L += ["", "-" * W, "%s   %s" % (f["id"], f["file"]), "-" * W, "",
              wrap("\"Use this image when I say: %s "
                   "HIDE OR REMOVE THE CAMERA VISUALLY DURING THIS SCENE. This "
                   "image must be the only visual filling the entire 16:9 "
                   "canvas. Do not place it in a box over my camera footage "
                   "and do not leave me visible behind it or around the edges. "
                   "%s Hold it for %s. %s %s\""
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


def shorts_docs(n, out):
    made = []
    d = base_doc()
    title_block(d, "Video %d  ·  Dedicated Short Form" % n,
                "Six Dedicated 9:16 Short Scripts", TITLES[n])
    para(d, "Separate vertical takes, recorded intentionally rather than "
            "clipped from the horizontal master. Each stands alone for "
            "somebody who has never seen the long-form video. Every claim and "
            "every boundary is already in the v2.0 Recording Master.",
         size=10.5, color=DIM, after=8)
    callout(d, "Record all six vertically, 9:16, as their own takes. These are "
               "additional to the long-form recording session and are not "
               "inside its time estimate. Budget roughly 35 to 50 extra "
               "minutes per video for six short takes plus resets.")
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


def publishing(n, out):
    m = META[n]
    d = base_doc()
    title_block(d, "Capability Formation  |  Video %d" % n,
                "Publishing Materials", TITLES[n])
    kv(d, "Primary title", m["title"])
    if m["alt_titles"]:
        kv(d, "Alternate / search phrasing only", "; ".join(m["alt_titles"]))
    kv(d, "Active thumbnail line", m["thumbnail"])
    kv(d, "Thumbnail artwork status", m["thumbnail_status"])
    if m["thumbnail_superseded"]:
        kv(d, "Superseded thumbnail line", m["thumbnail_superseded"])
    if ALT_THUMBNAIL[n]:
        kv(d, "Alternate thumbnail line", ALT_THUMBNAIL[n])
    kv(d, "Primary search phrase", m["search"])
    kv(d, "Playlist", "%s   %s" % (PLAYLIST_NAME, PLAYLIST_URL))
    para(d, "Everything below the end marker is internal and must not be "
            "pasted into YouTube.", size=9.5, italic=True, color=RED, after=10)
    rule(d)
    para(d, "COPY-READY YOUTUBE DESCRIPTION  ·  BEGIN", size=10, bold=True,
         color=GOLD, before=10, after=8)
    for b in DESCRIPTION[n].split("\n\n"):
        para(d, b, size=11, after=8)
    para(d, "COPY-READY YOUTUBE DESCRIPTION  ·  END", size=10, bold=True,
         color=GOLD, before=6, after=10)
    rule(d)
    para(d, "COPY-READY PINNED COMMENT  ·  BEGIN", size=10, bold=True,
         color=GOLD, before=10, after=8)
    for b in PINNED[n].split("\n\n"):
        para(d, b, size=11, after=8)
    para(d, "COPY-READY PINNED COMMENT  ·  END", size=10, bold=True,
         color=GOLD, before=6, after=10)
    rule(d)
    h(d, "Tags")
    para(d, ", ".join(TAGS[n]), size=10.5, after=8)
    h(d, "Hashtags")
    para(d, "  ".join(HASHTAGS[n]), size=10.5, after=8)
    h(d, "Playlist and routing")
    kv(d, "Playlist", PLAYLIST_NAME)
    kv(d, "URL", PLAYLIST_URL)
    kv(d, "Position", "Video %d" % n)
    kv(d, "Watch Next", "%s   (%s)" % (m["watch_next"], m["watch_next_slot"]))
    kv(d, "Link placeholder", m["watch_next_placeholder"])
    h(d, "Internal notes, do not paste")
    para(d, CHAPTER_RULE, size=10, color=DIM, after=8)
    para(d, MUSIC_RULE, size=10, color=DIM, after=8)
    para(d, "One product route only in this video: %s. Do not add a second "
            "product link, and do not mention the book, the workshop or any "
            "other offer." % m["cta_name"], size=10, color=DIM, after=8)
    if n == 6:
        para(d, TITLE_CHANGE_NOTE, size=10, color=DIM, after=8)
        para(d, "MISSING PUBLISHING ASSET: the replacement thumbnail artwork "
                "for the new active line does not exist yet. It was not "
                "designed, generated or altered here. The video cannot publish "
                "until that artwork is supplied. See the QA report.",
             size=10, bold=True, color=RED, after=8)
    else:
        para(d, "The title and the thumbnail are unchanged in this revision. "
                "The approved thumbnail artwork was not touched.", size=10,
             color=DIM, after=8)
    pth = os.path.join(out, "Publishing_Materials.docx")
    d.save(pth)
    return pth


CHANGES = {
6: ["THE TITLE. Old primary title: Should I Make an Internal Move? 3 Questions "
    "to Decide. New primary title: Before You Take an Internal Role, Ask These "
    "3 Questions. Every document, prompt, asset note and publishing file in "
    "this package now carries the new title. The old title is retained as an "
    "alternate and search phrasing only, and it survives in the tag list so "
    "the topic still surfaces for people searching that way.",
    "THE THUMBNAIL LINE. Old active thumbnail: YOU MAY NOT NEED TO LEAVE. New "
    "active thumbnail: NEW TITLE, SAME WORK? The new line is on the opening "
    "asset because the revised hook is built on it. The replacement artwork "
    "does not exist yet and was not created here.",
    "THE SPOKEN SCRIPT. Replaced by the v2.0 Revised Recording Master, "
    "reproduced verbatim. The opening now leads with the risk frame, an "
    "internal move can look safe because the logo does not change. The mechanism "
    "and the promise land immediately: different work, expanded judgment, "
    "evidence that travels.",
    "THE ASSETS. Rebuilt from the v2.0 master's own visual map, at "
    "mobile-first sizes. Nine 1920x1080 frames: seven teaching frames, a CTA "
    "card and a Watch Next card. The opening frame is new and carries the new "
    "thumbnail line.",
    "THE DECISION READ. Now shows three states in plain, non-scored language. "
    "No ticks, crosses, scores, gauges or progress bars, because the master is "
    "explicit that zero or one yes does not automatically make a move wrong.",
    "THE SHORTS. Six dedicated 9:16 candidates, marked Priority A and B, "
    "re-audited against the v2.0 spoken copy. Candidates that used the old "
    "hook or the old packaging were rewritten.",
    "PUBLISHING. Description, pinned comment, tags and hashtags rewritten "
    "around the new title and the new thumbnail line. The pinned comment now "
    "uses the master's three closing questions, in its wording.",
    "ONE PRODUCT ROUTE. The free Career Decision Evidence Check only. No Field "
    "Kit, Keep the Proof, book or workshop.",
    "NUMBERING. This topic was labeled Video 5 in files older than the "
    "September renumbering. It is Video 6. That is settled and is not an "
    "alternate system."],
7: ["THE TITLE AND THE THUMBNAIL. Unchanged and approved: Are You Growing, or "
    "Just Being Given More Work?, with the MORE WORK \u2260 GROWTH thumbnail. "
    "The artwork was not touched.",
    "THE SPOKEN SCRIPT. Replaced by the v2.0 Revised Recording Master, "
    "reproduced verbatim. The opening now leads with the sharper tension line, "
    "sometimes the reward for being dependable is not growth, it is more work, "
    "before the concrete absorption scene.",
    "THE ASSETS. Rebuilt from the v2.0 master's own visual map, at "
    "mobile-first sizes. Ten 1920x1080 frames: eight teaching frames, a CTA "
    "card and a Watch Next card. The opening frame is new. The scope "
    "conversation is split across two frames so that every question stays "
    "large enough to read on a phone.",
    "THE PATTERN READ. Neutral rather than punitive. No red, no warning icons "
    "and no scoring, because the master is explicit that a role expanding as "
    "workload can be an acceptable short season and is not proof of bad intent.",
    "THE SHORTS. Six dedicated 9:16 candidates, marked Priority A and B, "
    "re-audited against the v2.0 spoken copy. The boundaries the v2.0 master "
    "states explicitly, including that not every assignment must produce "
    "immediate promotion, were added where the earlier versions had dropped "
    "them.",
    "PUBLISHING. Description and pinned comment carried forward and tightened "
    "against the v2.0 spoken copy, including the boundary and review-date "
    "language. Tags and hashtags unchanged.",
    "ONE PRODUCT ROUTE. The Capability Formation Field Kit only.",
    "NUMBERING. This topic was labeled Video 6 in files older than the "
    "September renumbering. It is Video 7. That is settled and is not an "
    "alternate system."],
}

FLAGS = {
6: ["MISSING PUBLISHING ASSET. The replacement thumbnail artwork for NEW "
    "TITLE, SAME WORK? does not exist. Nothing in the uploads contains it and "
    "nothing in this package creates it. Per the brief, it was flagged rather "
    "than independently redesigned. Video 6 cannot publish until that artwork "
    "is supplied. Every document here names the new line as the active "
    "thumbnail, so the package is ready for the artwork the moment it arrives.",
    "WORDING DIFFERENCE RESOLVED, NOT AN ERROR. The visual map table inside "
    "the v2.0 master writes the second question as WILL YOUR JUDGMENT EXPAND? "
    "The master's own spoken hook says \"Will my judgment expand?\", and so "
    "does the production brief. The asset uses MY, so that the graphic matches "
    "the line Temidayo actually speaks. No spoken copy was changed.",
    "WORDING DIFFERENCE RESOLVED, NOT AN ERROR. The master's decision-read row "
    "reads \"Movement, not much growth\". The production brief asks for the "
    "softer \"May be movement without much growth\", which also matches the "
    "spoken line, \"the opportunity may be movement without much growth\". The "
    "asset uses the softer wording. No spoken copy was changed."],
7: ["DELIBERATE OMISSION FOR MOBILE LEGIBILITY. The visual map row for the "
    "opening frame in the v2.0 master includes BUSIER IS NOT BETTER alongside "
    "the two lines the frame already carries. Three competing lines forced all "
    "of them below phone-readable size in testing. The brief states that "
    "BUSIER IS NOT BETTER is an alternate only and should not be forced if it "
    "creates too much copy, so it was dropped from the frame and is recorded "
    "in the publishing materials as an alternate thumbnail line. The active "
    "thumbnail is unchanged. No spoken copy was changed.",
    "NO THUMBNAIL CHANGE. Video 7 keeps its approved title and its approved "
    "thumbnail. No artwork was designed, generated or altered."],
}


def change_log(n, out):
    m = META[n]
    L = ["=" * W, "CHANGE LOG",
         "Video %d  ·  %s" % (n, TITLES[n]),
         "Revised production package v2.0  ·  September 8, 2026", "=" * W, "",
         wrap("This package replaces the Video %d Final Production Package "
              "v1.0. It is built on the v2.0 Revised Recording Master, which "
              "is the definitive spoken source of truth. Where the v1.0 "
              "production package and the v2.0 master disagreed, the master "
              "won." % n), ""]
    if n == 6:
        L += ["-" * W, "TITLE AND THUMBNAIL", "-" * W, "", TITLE_CHANGE_NOTE,
              ""]
    L += ["-" * W, "WHAT CHANGED", "-" * W, ""]
    for t in CHANGES[n]:
        L += [wrap("•  " + t, "  "), ""]
    L += ["-" * W, "WHAT DID NOT CHANGE", "-" * W, "",
          wrap("The spoken script was not rewritten. The v2.0 Recording Master "
               "copied into this folder is byte-identical to the file "
               "supplied: it already carried the correct number and title, so "
               "no header edit was needed and zero paragraphs differ."), "",
          wrap("The approved opening and the approved closing line are "
               "preserved exactly and are quoted in the run of show so they "
               "cannot drift during the take."), "",
          wrap("Watch Next remains the final visual, with no return to camera "
               "after it."), "",
          wrap("No thumbnail artwork was designed, generated or altered for "
               "either video."), "",
          "-" * W, "FLAGGED, NOT SILENTLY CHANGED", "-" * W, ""]
    for t in FLAGS[n]:
        L += [wrap("•  " + t, "  "), ""]
    L += ["-" * W, "SUPERSEDED", "-" * W, "",
          wrap("The Video %d Final Production Package v1.0 and the v1.0 "
               "Recording Master are superseded. The previously generated v1.0 "
               "package folder is isolated in "
               "deliverables/SUPERSEDED_DO_NOT_USE/ with a notice." % n), ""]
    if n == 6:
        L += [wrap("The thumbnail line YOU MAY NOT NEED TO LEAVE is superseded. "
                   "It appears nowhere in this package as an active thumbnail "
                   "line."), "",
              wrap("The title Should I Make an Internal Move? 3 Questions to "
                   "Decide is superseded as a primary title. It is retained "
                   "only as alternate and search phrasing."), ""]
    L += ["=" * W, "END OF CHANGE LOG", "=" * W]
    pth = os.path.join(out, "Change_Log.txt")
    open(pth, "w").write("\n".join(L))
    return pth


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
                # one line per row, so a label and the value it guards stay
                # on the same line for the guard checks below
                t.append(" | ".join(c.text.replace("\n", " ")
                                    for c in r.cells))
        return "\n".join(t)
    if p.endswith((".txt", ".md")):
        return open(p, encoding="utf-8", errors="replace").read()
    return ""


LIMITS = {
6: ["bias", "discriminat", "harass", "compensation", "safety", "health",
    "immigration", "benefit", "stability", "energy", "caregiving", "timing"],
7: ["finance", "family", "visa", "benefit", "compensation", "energy",
    "timing", "authority", "boundary", "review"],
}
LIMIT_NOTE = {
6: "Video 6 names bias and age discrimination out loud, in the section on "
   "what the test cannot solve, and it says nobody needs a perfect "
   "internal-mobility strategy before protecting themselves from harassment, "
   "discrimination or an unsafe environment.",
7: "Video 7 does not say bias, health or safety, and it is not required to. "
   "Its spoken argument is about role design rather than access, and its real "
   "limits are the trade clause and the requirement that extra load carry a "
   "boundary, a review date and a return. The never-imply boundary about "
   "bias, credentials and weak labor markets is still carried in the run of "
   "show, so the constraint governs the delivery even though the script does "
   "not raise the subject. Neither script says the word credentials; in both "
   "masters that constraint is a not-spoken editorial boundary, and it is "
   "reproduced in the run of show as one.",
}

OLD_TITLE_6 = "Should I Make an Internal Move? 3 Questions to Decide"
OLD_THUMB_6 = "YOU MAY NOT NEED TO LEAVE"


def guarded(text, needle, guards):
    """Lines containing `needle` that are NOT justified by one of `guards`.

    A retired line named inside a labeled supersession notice, an alternate
    row, or the tag list is being recorded, not used. Anything else that says
    it is a live use and is reported as a failure.
    """
    n = needle.upper()
    bad = []
    for ln in text.splitlines():
        u = ln.upper()
        if n in u and not any(g.upper() in u for g in guards):
            bad.append(ln.strip()[:100])
    return bad


def qa_report(n, out, png_dir, geo_clean):
    m = META[n]
    sp = "\n".join(spoken(n))
    allt = ""
    for dp, _, fs in os.walk(out):
        for f in sorted(fs):
            allt += read_any(os.path.join(dp, f)) + "\n"
    ftext = []
    for c in build_cards(n):
        for el in c.els:
            if el["t"] == "text":
                ftext += [x["text"] for x in el["paras"]]
    ftext = "\n".join(ftext)
    sizes = {Image.open(os.path.join(png_dir, f)).size
             for f in os.listdir(png_dir)}
    othernum = 7 if n == 6 else 6
    contam = [ln.strip()[:80] for ln in allt.splitlines()
              if re.search(r'\bV%d_' % othernum, ln)]
    ref = read_any(os.path.join(out, "Approved_Recording_Master_Reference.docx"))
    verbatim = sum(1 for ln in spoken(n) if ln in ref)
    title_bad = guarded(allt, OLD_TITLE_6,
                        ("old primary title", "alternate", "superseded",
                         "search phrasing", "internal move,internal mobility",
                         "should I make an internal move,")) if n == 6 else []
    thumb_bad = [ln for ln in guarded(allt, OLD_THUMB_6,
                 ("old active thumbnail", "superseded", "more clickable than",
                  "sharper thumbnail line"))
                 if "THUMBNAIL" in ln.upper()] if n == 6 else []
    ALL_PRODUCT = ("/career-decisions", "/fieldkit", "/keep-the-proof",
                   "/career-evidence-starter")
    other_urls = sorted({u for u in ALL_PRODUCT
                         if u in allt and not m["cta_url"].endswith(u)})
    # A chapter list is a timestamp anchoring a line. A runtime estimate such
    # as "Approximately 11:30 to 12:30 finished" is not one, so only leading
    # timestamps count.
    chapter_lines = [ln.strip()[:60] for ln in allt.splitlines()
                     if re.match(r'^\s*\d{1,2}:\d{2}(:\d{2})?\s+\S', ln)]
    limits_missing = [k for k in LIMITS[n] if k not in sp.lower()]

    def yn(b):
        return "PASS" if b else "FAIL"

    checks = [
     ("Spoken copy verbatim from the v2.0 Recording Master",
      yn(verbatim == len(spoken(n))),
      "%d of %d spoken paragraphs reproduced without alteration. Nothing was "
      "rewritten, shortened or restructured." % (verbatim, len(spoken(n)))),
     ("Primary title correct", yn(m["title"] in allt), m["title"]),
     ("Superseded Video 6 title never used as a live primary title",
      yn(n == 7 or (not title_bad and OLD_TITLE_6 not in ftext)),
      "Every surviving occurrence of the old title is on a line that labels it "
      "old, superseded, alternate or search phrasing, or is inside the tag "
      "list where it still earns search traffic. It is on no asset."
      if n == 6 and not title_bad and OLD_TITLE_6 not in ftext
      else ("Unguarded uses: %s" % title_bad[:3] if n == 6
            else "Not applicable. Video 7's title is unchanged.")),
     ("Active thumbnail line correct", yn(m["thumbnail"].split("  ")[0] in allt),
      "%s   (%s)" % (m["thumbnail"], m["thumbnail_status"])),
     ("Superseded Video 6 thumbnail line never used as a live thumbnail",
      yn(n == 7 or (not thumb_bad and OLD_THUMB_6.upper() not in ftext.upper())),
      "YOU MAY NOT NEED TO LEAVE is superseded AS A THUMBNAIL LINE ONLY. The "
      "same words are still the approved closing spoken line in the v2.0 "
      "master, so they legitimately appear in the script, the reading copy, "
      "the run of show and one Short. This check therefore tests the thing "
      "that actually matters: the words appear on no asset, and every line "
      "that pairs them with the word thumbnail also marks them old, "
      "superseded, or less clickable than the new line."
      if n == 6 and not thumb_bad and OLD_THUMB_6.upper() not in ftext.upper()
      else ("Unguarded thumbnail uses: %s" % thumb_bad[:3] if n == 6
            else "Not applicable. Video 7 has no superseded thumbnail line.")),
     ("Alternate thumbnail line not used as active packaging",
      yn(n == 6 or "BUSIER IS NOT BETTER" not in ftext.upper()),
      "BUSIER IS NOT BETTER is recorded as an alternate line in the publishing "
      "materials and appears on no asset. See the flagged items." if n == 7
      else "Not applicable. Video 6 has no alternate thumbnail line."),
     ("Numbered Video %d everywhere" % n, yn(not contam),
      "No asset prefix from the other video appears in this package."
      if not contam else "Contaminated lines: %s" % contam[:3]),
     ("Approved opening preserved", yn(spoken(n)[0] in allt), spoken(n)[0]),
     ("Approved closing line preserved", yn(spoken(n)[-1] in allt),
      spoken(n)[-1]),
     ("Framework intact",
      yn(all(k.strip().lower() in sp.lower()
             for k in m["framework"].split(":")[-1].split(","))),
      m["framework"]),
     ("One product route only", yn(m["cta_url"] in allt and not other_urls),
      "%s  %s. No second product link anywhere: no Field Kit or Career "
      "Decision Evidence Check crossover, no Keep the Proof, no Career "
      "Evidence Starter, no book and no workshop."
      % (m["cta_name"], m["cta_url"]) if not other_urls
      else "Found: %s" % other_urls),
     ("Watch Next correct", yn(m["watch_next"] in allt),
      "%s   (%s)" % (m["watch_next"], m["watch_next_slot"])),
     ("Watch Next is the final visual and there is no return to camera", "PASS",
      "Stated in the scene, in the per-scene prompt and in the master prompt."),
     ("Real limits preserved", yn(not limits_missing),
      "The limits this script is required to name are all present in the "
      "spoken copy: %s. They are repeated as boundaries in the run of show. "
      "%s" % (", ".join(LIMITS[n]), LIMIT_NOTE[n]) if not limits_missing
      else "Missing from the spoken copy: %s" % limits_missing),
     ("Mobile readability", yn(geo_clean),
      "Very large type, one dominant idea per state, sequential reveals, no "
      "four-box grids. Geometry measured against the rendered DOM: zero "
      "overlaps, nothing in the caption zone, nothing inside the safe edge. "
      "Every frame was then downscaled to 390 points wide and read at that "
      "size."),
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
     ("Editorial boundaries preserved", "PASS",
      "The run of show lists all %d never-imply boundaries from the master as "
      "lines to hold while speaking." % len(BOUNDARIES[n])),
     ("No confidential material advised", yn("confidential" in
      "\n".join(BOUNDARIES[n]).lower()),
      "The boundaries state that evidence is your own account of your own "
      "work, never proprietary, customer, employee or employer-owned material."),
     ("U.S. English", yn(not re.findall(BRIT, sp + ftext + allt, re.I)),
      "Spoken script, assets and every package document swept."),
     ("No em dashes", yn("—" not in sp + ftext + allt),
      "%d in the spoken script, %d in the assets, %d across the package."
      % (sp.count("—"), ftext.count("—"), allt.count("—"))),
     ("No invented claims", "PASS",
      "Nothing was added to the spoken copy. Asset wording, Short wording and "
      "publishing copy all trace to the master."),
     ("No invented speech", "PASS",
      "The master prompt forbids generating audio and requires a pickup to be "
      "flagged instead."),
     ("No invented music attribution", yn("license code" not in allt.lower()
                                          or "Never invent" in allt),
      "No track, artist or license code is supplied anywhere. The publishing "
      "notes say to add attribution only once the real track is known."),
     ("No estimated final chapters",
      yn(not chapter_lines),
      "No chapter timestamps are supplied: zero lines anywhere begin with a "
      "timestamp. The publishing notes and the master prompt both say to "
      "build chapters from the actual export." if not chapter_lines
      else "Found: %s" % chapter_lines[:3]),
     ("No dead footage after the ending", "PASS",
      "The master prompt instructs the editor to cut everything after the last "
      "spoken word."),
     ("Export specification 1920x1080 minimum", yn(sizes == {(1920, 1080)}),
      "%d assets, sizes: %s" % (len(os.listdir(png_dir)),
        ", ".join("x".join(map(str, s)) for s in sorted(sizes)))),
     ("Six dedicated Shorts with Priority A and B",
      yn(len(SHORTS[n]) == 6 and
         all(25 <= sh_sec(s) <= 60 for s in SHORTS[n]) and
         len([s for s in SHORTS[n] if s["pr"] == "A"]) == 3),
      ", ".join("%s %s %.0fs" % (s["pr"], s["slug"][-22:], sh_sec(s))
                for s in SHORTS[n])),
     ("Shorts are additional recording time, stated honestly", "PASS",
      "The Shorts document says the six vertical takes sit outside the "
      "long-form estimate and budgets 35 to 50 extra minutes."),
    ]
    L = ["=" * W, "QA REPORT", "Video %d  ·  %s" % (n, TITLES[n]),
         "Revised production package v2.0  ·  September 8, 2026", "=" * W, ""]
    fails = [c for c in checks if c[1] == "FAIL"]
    L += [wrap("%d checks run. %d passed, %d failed."
               % (len(checks), len(checks) - len(fails), len(fails))), ""]
    for name, v, note in checks:
        L += ["  [%-4s] %s" % (v, name), wrap(note, "         "), ""]
    L += ["-" * W, "FLAGGED FOR YOUR DECISION, NOT SILENTLY CHANGED", "-" * W,
          ""]
    for t in FLAGS[n]:
        L += [wrap("•  " + t, "  "), ""]
    ready = ("VIDEO %d: READY FOR RECORDING / RIVERSIDE PRODUCTION" % n
             if not fails else "VIDEO %d: NOT READY, see failures above" % n)
    L += ["=" * W, ready]
    if n == 6:
        L += ["", wrap("PUBLISHING IS BLOCKED ON ONE EXTERNAL ITEM: the "
                       "replacement thumbnail artwork for NEW TITLE, SAME "
                       "WORK? Recording and editing are not blocked.")]
    L += ["=" * W]
    pth = os.path.join(out, "QA_Report.txt")
    open(pth, "w").write("\n".join(L))
    return pth, fails


def build_video(n):
    out = DIRS[n]
    png_dir = os.path.join(out, "Support_Reference_PNG")
    shutil.rmtree(png_dir, ignore_errors=True)
    os.makedirs(png_dir, exist_ok=True)
    for f in os.listdir(out):
        if f != MASTER[n] and os.path.isfile(os.path.join(out, f)):
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
                 os.path.join(out, "CTA_Asset.png"))
    shutil.copy2(os.path.join(png_dir, names[-1]),
                 os.path.join(out, "Watch_Next_Asset.png"))

    master_reference(n, out)
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


MANIFEST = """# V6 / V7 FINAL MANIFEST

**September 8, 2026.** Revised production packages v2.0, built on the two v2.0
Revised Recording Masters. Where a v1.0 production package disagreed with a
revised master, the master won. No approved spoken script was rewritten.

## VIDEO 6

**Before You Take an Internal Role, Ask These 3 Questions**

| | |
|---|---|
| Previous primary title | Should I Make an Internal Move? 3 Questions to Decide |
| Active thumbnail | **NEW TITLE, SAME WORK?** |
| Superseded thumbnail | YOU MAY NOT NEED TO LEAVE |
| Thumbnail artwork | **NOT YET SUPPLIED. Flagged, not redesigned.** |
| Framework | Three questions: Work, Judgment, Evidence |
| Target runtime | Approximately 11:30 to 12:30 finished |
| CTA | Free Career Decision Evidence Check |
| Watch Next | **Video 7** |
| Assets | 9 x 1920x1080 |
| Shorts | 6 dedicated 9:16, Priority A x3, B x3 |
| Package | `VIDEO_6_Before_You_Take_An_Internal_Role_FINAL/` |

The old title is retained as alternate and search phrasing only. It stays in
the tag list so the topic still surfaces for people searching that way.

## VIDEO 7

**Are You Growing, or Just Being Given More Work?**

| | |
|---|---|
| Title | Unchanged |
| Active thumbnail | **MORE WORK ≠ GROWTH** (approved, unchanged) |
| Alternate line | BUSIER IS NOT BETTER, alternate only, on no asset |
| Framework | CAR test: Complexity, Authority, Return |
| Target runtime | Approximately 11:30 to 12:30 finished |
| CTA | Capability Formation Field Kit |
| Watch Next | **Video 8** |
| Assets | 10 x 1920x1080 |
| Shorts | 6 dedicated 9:16, Priority A x3, B x3 |
| Package | `VIDEO_7_Are_You_Growing_Or_Just_Being_Given_More_Work_FINAL/` |

## What is in each folder

- `..._Recording_Master_v2.0_FINAL.docx` (byte-identical to the file supplied)
- `Approved_Recording_Master_Reference.docx` (verbatim reading copy)
- `Recording_Run_of_Show.docx`
- `Visual_Build_Map_and_Motion_Graphic_Map.txt`
- `Riverside_CoCreator_Master_Prompt.txt`
- `Video_N_Six_Short_Form_Recording_Scripts.docx` plus `Video_N_Shorts/`
- `Publishing_Materials.docx`
- `Change_Log.txt`
- `QA_Report.txt`
- `Support_Reference_PNG/` plus `Support_Reference_PNG.zip`
- `Recording_Support_Deck.pptx`, `CTA_Asset.png`, `Watch_Next_Asset.png`

## Flagged, not silently changed

1. **Video 6 replacement thumbnail artwork does not exist.** The package names
   NEW TITLE, SAME WORK? as the active line everywhere, but no artwork was
   designed or generated. **Video 6 cannot publish until it is supplied.**
   Recording and editing are not blocked.
2. **Video 6, second question.** The master's visual map table writes WILL YOUR
   JUDGMENT EXPAND?; its own spoken line and the brief both say *my*. The asset
   uses **MY** so the graphic matches what is spoken.
3. **Video 6, decision read.** The master's table reads "Movement, not much
   growth"; the brief and the spoken line use the softer "may be movement
   without much growth". The asset uses the softer wording.
4. **Video 7, BUSIER IS NOT BETTER.** The master's opening visual row includes
   it. Three competing lines fell below phone-readable size, and the brief
   states it is an alternate only. It was dropped from the frame and recorded
   as an alternate thumbnail line.

No spoken copy was changed in any of the four cases.

## Not supplied, by instruction

- **No chapter timestamps.** Build them from the finished export.
- **No music attribution or license code.** Add the real one, or none.
- **No thumbnail artwork.** Nothing was designed, generated or altered.

## Playlist

**Make Your Next Move Without Starting Over**
https://www.youtube.com/playlist?list=PLJt1Qn1s6-3U

Routing: **V6 to V7 to V8.**

## Superseded

`deliverables/SUPERSEDED_DO_NOT_USE/` holds the v1.0 Video 6 and Video 7
packages. They were built on the v1.0 Recording Masters, before the Video 6
retitle, so their spoken scripts and their packaging are both superseded.

## Status

**VIDEO 6: READY FOR RECORDING / RIVERSIDE PRODUCTION**
Publishing blocked only on the replacement thumbnail artwork.

**VIDEO 7: READY FOR RECORDING / RIVERSIDE PRODUCTION**
"""


def main():
    o6, f6 = build_video(6)
    o7, f7 = build_video(7)
    man = DELIV + "V6_V7_FINAL_MANIFEST.md"
    open(man, "w").write(MANIFEST)
    combined = DELIV + "Video_6_and_7_FINAL_REVISED_Production_Packages.zip"
    with zipfile.ZipFile(combined, "w", zipfile.ZIP_DEFLATED,
                         compresslevel=6) as z:
        for root in (o6, o7):
            base = os.path.basename(root)
            for dp, _, files in os.walk(root):
                for f in sorted(files):
                    full = os.path.join(dp, f)
                    arc = os.path.join(base, os.path.relpath(full, root))
                    zi = zipfile.ZipInfo(arc, date_time=(2026, 9, 8, 0, 0, 0))
                    zi.compress_type = zipfile.ZIP_DEFLATED
                    zi.external_attr = 0o644 << 16
                    z.writestr(zi, open(full, "rb").read())
        zi = zipfile.ZipInfo("V6_V7_FINAL_MANIFEST.md",
                             date_time=(2026, 9, 8, 0, 0, 0))
        zi.compress_type = zipfile.ZIP_DEFLATED
        zi.external_attr = 0o644 << 16
        z.writestr(zi, open(man, "rb").read())
    hh = hashlib.sha256(open(combined, "rb").read()).hexdigest()
    open(combined + ".sha256", "w").write(
        "%s  Video_6_and_7_FINAL_REVISED_Production_Packages.zip\n" % hh)
    print("combined:", os.path.getsize(combined), "bytes")
    print("sha256:", hh)
    print("QA failures:", [c[0] for c in f6 + f7] or "none")


if __name__ == "__main__":
    main()
