# -*- coding: utf-8 -*-
"""One complete, self-contained Riverside Co-Creator master prompt per video.

Each prompt is usable on its own after Temidayo uploads the new recording. It
never assumes the editor has read anything else in the package.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import masters1421 as M
from frames1421 import SETS
from docs1421f import mono, hr, head
from prodocs import (CAMERA, SOUND, BROLL, CAPTIONS, FULLSCREEN, SUBSCRIBE,
                     AUDIO)


def wrap(text, width=76, indent=""):
    out, line = [], indent
    for word in text.split():
        if len(line) + len(word) + 1 > width and line.strip():
            out.append(line.rstrip())
            line = indent + word + " "
        else:
            line += word + " "
    if line.strip():
        out.append(line.rstrip())
    return out


def build(n, out_path):
    m = M.read(n)
    w, fast, slow = M.estimate(n)
    res = M.resource(n)
    L = head("VIDEO %d  |  RIVERSIDE CO-CREATOR MASTER PROMPT" % n)
    L += [M.title(n), "",
          "Paste this whole file into Riverside Co-Creator after uploading the",
          "new recording. It is self-contained.", "", hr(), ""]

    L += ["1. WHAT THIS IS", ""]
    L += wrap("I am giving you a new recording. Create the visual and audio "
              "editing layer from this recording and its transcript. Do not "
              "look for existing graphics to convert, and do not treat any "
              "supplied reference asset as a mandatory slideshow.", indent="  ")
    L += [""]
    L += wrap("The approved Recording Master controls intended meaning. The "
              "actual recorded performance controls timing. If the recorded "
              "speech materially differs from the approved master, FLAG IT "
              "and tell me where. Do not manufacture missing speech, and do "
              "not write new lines to bridge a gap.", indent="  ")
    L += ["", hr(), ""]

    L += ["2. THE VIDEO", "",
          "  Title:      %s" % M.title(n),
          "  Thumbnail:  %s" % M.thumbnail(n),
          "  Framework:  %s" % (M.framework(n) or "none stated"),
          "  CTA:        %s" % M.cta(n),
          "  Resource:   %s" % (res or
                                "NONE. This video names no resource. Do not "
                                "add one."),
          "  Watch Next: %s" % M.watch_next(n),
          "  Estimate:   %s to %s from %s spoken words. Planning arithmetic, "
          "not a runtime." % (fast, slow, "{:,}".format(w)), "",
          "  The exact final spoken line:", ""]
    L += wrap(M.final_line(n), indent="    ")
    L += ["", "  Nothing appears after Watch Next.", "", hr(), ""]

    L += ["3. EDIT SHAPE", ""]
    for t in ["Horizontal 16:9. Minimum 1920 by 1080.",
              "Camera-led teaching edit. Thoughtful pacing, not hyperactive.",
              "Intentional jump cuts. Clean up false starts and restarts.",
              "Do not over-shorten a thoughtful explanation to raise pace.",
              "Preserve the approved structure. Do not manufacture an extra "
              "hook, reorder the teaching, or move the opening."]:
        L += wrap("- " + t, indent="  ")
    L += ["", hr(), ""]

    L += ["4. FULL-SCREEN RULE", ""] + wrap(FULLSCREEN, indent="  ")
    L += ["", hr(), ""]
    L += ["5. CAMERA MOVEMENT", ""] + wrap(CAMERA, indent="  ")
    L += ["", hr(), ""]
    L += ["6. B-ROLL", ""] + wrap(BROLL, indent="  ")
    L += ["", hr(), ""]
    L += ["7. CAPTIONS AND SRT", ""] + wrap(CAPTIONS, indent="  ")
    L += ["", hr(), ""]
    L += ["8. SUBSCRIBE CUE", ""] + wrap(SUBSCRIBE, indent="  ")
    L += ["", hr(), ""]

    L += ["9. AUDIO AND VISUAL TRANSITION HOOKS", "",
          "  Apply this only after the final recorded footage is uploaded.",
          ""]
    L += wrap("Use restrained sound design to make important visual changes "
              "feel intentional. When a key full-screen graphic, comparison, "
              "image, framework step, or important text reveal appears, "
              "consider a subtle click, a soft tick, a light tap, a "
              "restrained whoosh, or a clean transition sound.", indent="  ")
    L += [""]
    L += wrap("Prefer subtle click or tick sounds when a new item appears, a "
              "comparison changes from one side to the other, a framework "
              "advances a step, a card or image replaces the previous one, or "
              "one important word or result is revealed.", indent="  ")
    L += [""]
    L += wrap("The sound reinforces the visual change. It is not the "
              "attraction. Do NOT add a click to every bullet, every cut, "
              "every sentence or every screen change.", indent="  ")
    L += [""] + wrap(SOUND, indent="  ")
    L += [""]
    L += wrap("Pair sound with a small visual action wherever possible: text "
              "appearing, a divider moving, a number changing, a card "
              "switching, a phrase highlighting. Sound and movement land "
              "together. The treatment should feel polished, modern and "
              "editorial, not gamified, cartoonish or hyperactive. If no "
              "sound improves the moment, leave it silent.", indent="  ")
    L += ["", hr(), ""]

    L += ["10. AUDIO FINISHING", ""] + wrap(AUDIO, indent="  ")
    L += ["", hr(), ""]

    L += ["11. LOOK", ""]
    for t in ["Natural skin tone. Do not push saturation or warmth.",
              "Subtle music, well under the voice, with a natural final fade "
              "where useful.",
              "Voice dominant over music and effects at every point.",
              "No black tail. No dead footage after the ending."]:
        L += wrap("- " + t, indent="  ")
    L += ["", hr(), ""]

    L += ["12. SCENE BY SCENE", "",
          "  Reference assets are supplied in 03_Visuals as 1920 by 1080 PNGs",
          "  and as an editable deck. Use them as references or as fallback",
          "  assets. Build the motion version where you can do better.", ""]
    for i, f in enumerate(SETS[n], 1):
        L += ["  SCENE %d  |  %s" % (i, f["key"])]
        L += wrap("TRIGGER: " + f["trigger"].replace("\n", " "), indent="    ")
        L += wrap("MODE: " + f["mode"], indent="    ")
        L += wrap("PURPOSE: " + f["purpose"], indent="    ")
        L += wrap("REVEAL: " + f["reveal"], indent="    ")
        L += wrap("EMPHASIS: " + f["emphasis"], indent="    ")
        L += wrap("HOLD: " + f["hold"], indent="    ")
        L += wrap("CAPTIONS: " + f["captions"], indent="    ")
        L += wrap("SOUND CANDIDATE: " + (f["sound"] or
                                         "None. Leave it silent."),
                  indent="    ")
        L += wrap("AFTER: " + f["after"], indent="    ")
        L += [""]
    L += [hr(), ""]

    L += ["13. WHAT TO FLAG RATHER THAN FIX", ""]
    for t in ["Recorded speech that materially differs from the approved "
              "master.",
              "A scene where the trigger sentence was not spoken.",
              "Any effect or scene you cannot build. Name the specific item "
              "for manual completion rather than substituting something.",
              "Audio you cannot clean without artifacts.",
              "Anything that would require inventing speech, a statistic, an "
              "employer, a person or an outcome."]:
        L += wrap("- " + t, indent="  ")
    L += ["", hr(), ""]

    L += ["14. DELIVER", ""]
    for t in ["The edited video, clean export, no persistent burned-in "
              "subtitles.",
              "A complete final transcript.",
              "An SRT generated against the FINAL edited timeline, "
              "synchronization checked after every cut and removal.",
              "A list of anything you flagged."]:
        L += wrap("- " + t, indent="  ")
    L += [""]
    return mono(out_path, L)
