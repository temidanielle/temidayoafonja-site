# -*- coding: utf-8 -*-
"""The Riverside Co-Creator prompt, rewritten for the story-led scripts.

This is not the previous prompt with a new filename. The pacing and the
scene structure changed, so the instructions changed: the prompt now tells
the editor where to stay on camera, and for every graphic it says what the
graphic actually is rather than "add a visual here".
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                "VIDEOS_4-21_CORRECTED_RUNTIME/build")
import masters_sl as M
import visualdir_sl as V
import prodocs_sl as P
from frames_sl import SETS
from docs421f import mono, hr, head


def build(n, path):
    w, fast, slow = M.estimate(n)
    L = head("VIDEO %d  |  RIVERSIDE CO-CREATOR MASTER PROMPT" % n)
    L += [M.title(n), "",
          "Source: %s" % M.read(n)["file"],
          "SHA-256 %s" % M.read(n)["sha"], "",
          "This prompt is written for the September 13 story-led script. The "
          "pacing",
          "and the scene structure are different from the previous version, "
          "so read it",
          "rather than assuming the old instructions still apply.", "",
          hr(), "", "WHAT THIS VIDEO IS", "",
          "  A story-led teaching video. The viewer meets a recognizable "
          "situation",
          "  first, then gets help making sense of it, then gets the "
          "framework.", "",
          "  %s. About %d spoken words, roughly %s to %s at 130 to 145 words"
          % (M.mode(n), w, fast, slow),
          "  per minute. That is arithmetic on the script, NOT a target "
          "runtime. Do",
          "  not speed up delivery or cut scenes to reach a number.", "",
          hr(), "", "THE ONE RULE THAT MATTERS MOST HERE", "",
          "  The opening is a recognition moment. Leave it on camera.", "",
          "  The story-led pass exists to make these videos feel human. "
          "Covering the",
          "  opening scene with an instructional graphic undoes exactly what "
          "it did.",
          "  Let the story establish tension before any framework appears.",
          "",
          "  Do not interrupt a human recognition moment with a graphic. Do "
          "not",
          "  alternate camera and graphics mechanically. Several camera "
          "stretches in",
          "  a row are correct where the script is telling a story.", "",
          hr(), "", "THE SHAPE TO EDIT TOWARD", "",
          "  CAMERA        Temidayo creates the problem or the tension",
          "  FULL SCREEN   the graphic makes the distinction visible",
          "  CAMERA        Temidayo interprets what it means",
          "  FULL SCREEN   the framework or example applies the idea",
          "  CAMERA        Temidayo brings it back to the viewer", "",
          "  Use judgment. This is a shape, not a metronome.", "",
          hr(), "", "STANDING VISUAL DIRECTION", ""]
    for s in V.STANDING:
        L += ["  %s" % s, ""]
    L += [hr(), "", "PALETTE", "",
          "  Deep navy %s carries authority and is the usual ground."
          % V.NAVY,
          "  Warm cream is breathing room and the light ground where "
          "legibility needs it.",
          "  Muted gold marks the ACTIVE idea only: the selected item, the "
          "number, the",
          "  underline, the one distinction that matters. Never decoration.",
          "  Do not introduce another color system.", "",
          hr(), "", "EVERY GRAPHIC IN THIS VIDEO, AND WHAT IT IS", "",
          "  Each of these is a true full-screen frame. The PNG is supplied "
          "in",
          "  03_Visuals. Build the reveal as described rather than showing "
          "the",
          "  finished card all at once.", ""]
    for i, f in enumerate(SETS[n], 1):
        tr, lay = V.treatment(f["key"])
        L += ["  %d. FULL-SCREEN %s" % (i, tr),
              "     file:   %s.png" % f["key"],
              "     cue:    %s" % f["trigger"],
              "     job:    %s" % f["purpose"],
              "     reveal: %s" % f["reveal"]]
        for d in V.DIRECTION[tr]:
            L += ["             %s" % d]
        L += ["     hold:   %s" % f["hold"],
              "     sound:  %s" % f["sound"],
              "     after:  %s" % f["after"], ""]
    L += [hr(), "", "WHERE TO STAY ON CAMERA", "",
          "  These stretches carry no graphic. They are the video.", ""]
    for item in P.spine(n):
        if item[0] == "CAMERA":
            words = sum(len(p.split()) for p in item[1])
            L += ["  about %3d words, opening: %s" % (words, item[1][0][:60])]
    L += ["", hr(), "", "CAMERA MOVEMENT", "",
          "  About 3 to 5 deliberate camera-emphasis beats for the ENTIRE "
          "video. One",
          "  combined budget, not per section.",
          "  Gentle push-ins, an occasional pull-back, and a return to base "
          "framing.",
          "  Do not pulse, do not zoom every sentence, and do not make the "
          "story",
          "  scenes hyperactive. The story-led script needs room to breathe.",
          "", hr(), "", "B-ROLL", "",
          "  About 2 to 4 meaningful full-screen B-roll moments where "
          "useful. Not a",
          "  quota. Substantive B-roll is TRUE FULL SCREEN.",
          "  Do not cut to B-roll simply because a story is being told.",
          "  No generic offices, handshakes, fake meetings, random typing, "
          "AI-looking",
          "  people, or stock footage that competes with Temidayo's "
          "delivery.",
          "  If the scene is stronger with Temidayo speaking, stay on her.",
          "", hr(), "", "SOUND", "",
          "  About 4 to 7 restrained audio accents for the ENTIRE video, "
          "including the",
          "  visual Subscribe cue. Candidates are not cumulative.",
          "  A soft click, a tick, a restrained whoosh, a light tap, a clean "
          "transition.",
          "  Do NOT add a click to every bullet or a sound to every cut. "
          "Voice stays",
          "  dominant. Stillness is allowed when the viewer needs to read or "
          "think.",
          "", hr(), "", "SUBSCRIBE", "",
          "  One brief visual Subscribe cue after meaningful value, about 1 "
          "to 3 seconds",
          "  including entrance and exit. Premium and restrained. There is "
          "no spoken",
          "  Subscribe request anywhere in this script and none is to be "
          "added.",
          "", hr(), "", "CAPTIONS", "",
          "  NO BURNED-IN OR OPEN CAPTIONS ANYWHERE IN THIS LONG-FORM VIDEO.",
          "  Deliver a clean final video, a complete transcript, and an SRT "
          "generated",
          "  against the FINAL edited timeline, not against the script.",
          "  Proofread names, frameworks, URLs and industry terminology in "
          "the SRT.",
          "  Text inside a graphic is instructional design. It is not "
          "captioning.",
          "", hr(), "", "CTA AND WATCH NEXT", "",
          "  The CTA card is full screen and simpler than the teaching "
          "graphics.",
          "  Watch Next is TRUE FULL SCREEN and FINAL. Nothing appears after "
          "it and",
          "  there is NO RETURN TO CAMERA afterward. No black tail, no dead "
          "footage.",
          "", hr(), "", "WHAT NOT TO DO", "",
          "  Do not add a framework, a claim, a figure or a lesson that the "
          "script does",
          "  not already teach, however good the graphic would look.",
          "  Do not add employer logos, fake screenshots, fake names, fake "
          "quotes or",
          "  real-company visuals to a constructed example. Where the script "
          "says",
          "  imagine, or maybe, or here is what this can look like, it is an "
          "illustration",
          "  and must not be dressed as a real record.",
          "  Do not re-cut the spoken script. If something does not work, "
          "raise it.",
          "", hr(), "", "EXPORT", "",
          "  Horizontal 16:9, minimum 1920 by 1080. Natural skin tone. "
          "Subtle music",
          "  under a dominant voice. Intentional jump cuts and false-start "
          "cleanup.",
          "  Clean ending with no black tail and no dead footage.", ""]
    return mono(path, L)
