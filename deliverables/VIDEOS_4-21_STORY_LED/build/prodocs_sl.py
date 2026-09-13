# -*- coding: utf-8 -*-
"""Production documents: the camera and full-screen spine, and the run of show.

The trigger map is not a list of graphics. It is the whole spine of the
video, because the thing this pass has to protect is the camera-led moment,
and a document that only lists graphics cannot show you where those are.

So the map walks the spoken script in order and marks every stretch:

  CAMERA        Temidayo. Recognition, lived experience, tension, reflective
                transition, bringing the idea back to the viewer
  FULL SCREEN   a frame the viewer now needs to see, with its treatment
  CALLOUT       a short overlay on an otherwise camera-led moment

Nothing is invented here. Every full-screen row is an asset that exists, and
every cue is a sentence the September 13 script says.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                "VIDEOS_4-21_CORRECTED_RUNTIME/build")
import masters_sl as M
import visualdir_sl as V
from frames_sl import SETS
from docs421f import mono, hr, head


def spine(n):
    """[(kind, ...)] over the whole script, in spoken order."""
    cue = {}
    for f in SETS[n]:
        q = M._norm(f["trigger"])
        # A few trigger sentences are spoken twice. "Capture the contribution."
        # opens the habit in V10's hook and is repeated as the action, and V13
        # says "Define." in both places. The card belongs at the first spoken
        # occurrence, where the idea arrives. Placing it again in the action
        # section would cue the same graphic twice, directly after that
        # section's own CTA card. Stop at the first match.
        placed = False
        for li, (label, ps) in enumerate(M.sections(n)):
            for pi, p in enumerate(ps):
                if q in M._norm(p):
                    cue.setdefault((li, pi), []).append(f)
                    placed = True
                    break
            if placed:
                break
    out = []
    for li, (label, ps) in enumerate(M.sections(n)):
        out.append(("SECTION", label))
        run = []
        for pi, p in enumerate(ps):
            if (li, pi) in cue:
                if run:
                    out.append(("CAMERA", run))
                    run = []
                for f in cue[(li, pi)]:
                    out.append(("FRAME", f, p))
            else:
                run.append(p)
        if run:
            out.append(("CAMERA", run))
    return out


def trigger_map(n, path):
    L = head("VIDEO %d  |  CAMERA AND FULL-SCREEN TRIGGER MAP" % n)
    L += [M.title(n), "",
          "Every stretch of this video is marked. A row that says CAMERA is "
          "a stretch",
          "where Temidayo carries the moment and no graphic should appear.",
          "", hr(), "",
          "HOW TO READ THIS", "",
          "  CAMERA        stay on Temidayo. Recognition, lived experience,",
          "                tension, a reflective turn, or bringing the idea",
          "                back to the viewer.",
          "  FULL SCREEN   a true full-screen frame. No camera behind it and",
          "                no shrinking it into a corner.",
          "", "  Do not alternate mechanically. Several camera stretches in "
          "a row are",
          "  correct where the script is telling a story.", "", hr(), ""]
    cam = full = 0
    for item in spine(n):
        if item[0] == "SECTION":
            L += ["", "=" * 74, item[1], "=" * 74, ""]
        elif item[0] == "CAMERA":
            cam += 1
            words = sum(len(p.split()) for p in item[1])
            L += ["  [ CAMERA ]  %d spoken paragraph%s, about %d words"
                  % (len(item[1]), "" if len(item[1]) == 1 else "s", words),
                  "              opens: %s" % item[1][0][:64],
                  "              stay on Temidayo through this stretch.", ""]
        else:
            full += 1
            f, para = item[1], item[2]
            tr, lay = V.treatment(f["key"])
            L += ["  [ FULL SCREEN ]  %s" % f["key"],
                  "      cue, exact words: %s" % f["trigger"],
                  "      treatment:  %s" % tr,
                  "      purpose:    %s" % f["purpose"],
                  "      reveal:     %s" % f["reveal"]]
            for d in V.DIRECTION[tr]:
                L += ["                  %s" % d]
            L += ["      hold:       %s" % f["hold"],
                  "      sound:      %s" % f["sound"],
                  "      after:      %s" % f["after"],
                  "      status:     %s" % f["status"], ""]
    L += ["", hr(), "",
          "SPINE SUMMARY", "",
          "  %d camera stretches, %d full-screen frames." % (cam, full),
          "  The video stays on Temidayo for most of its length, which is "
          "the point",
          "  of the story-led pass.", ""]
    return mono(path, L)


def visual_build_map(n, path):
    L = head("VIDEO %d  |  VISUAL BUILD AND MOTION REVEAL MAP" % n)
    L += [M.title(n), "", hr(), "", "STANDING DIRECTION", ""]
    for s in V.STANDING:
        L += ["  %s" % s]
    L += ["", hr(), "", "PALETTE", "",
          "  Deep navy %s carries authority and is the usual ground."
          % V.NAVY,
          "  Warm cream is breathing room, and the light ground where "
          "legibility needs it.",
          "  Muted gold marks the ACTIVE idea only: the selected item, the "
          "number,",
          "  the underline, the one distinction that matters. Never "
          "decoration.",
          "  No other color system is introduced.", "", hr(), "",
          "FRAME BY FRAME", ""]
    for f in SETS[n]:
        tr, lay = V.treatment(f["key"])
        L += ["  %s" % f["key"],
              "      treatment %s, built on the %s layout" % (tr, lay),
              "      cue: %s" % f["trigger"][:88],
              "      reveal: %s" % f["reveal"],
              "      hold: %s" % f["hold"],
              "      sound: %s" % f["sound"], ""]
    return mono(path, L)


def run_of_show(n, path, stamp):
    from docs421f import (base_doc, para, title_block, h, kv, callout, table,
                          bullets, footer_note, numbered, caption,
                          NAVY, GOLD, DIM, RED)
    w, fast, slow = M.estimate(n)
    d = base_doc()
    footer_note(d, "Video %d run of show  |  story-led" % n)
    title_block(d, "Capability Formation  |  Video %d" % n,
                "Recording Run of Show", M.title(n))
    kv(d, "Generated", stamp)
    kv(d, "Spoken source", "%s  ·  SHA-256 %s" % (M.read(n)["file"],
                                                  M.read(n)["sha"]))
    kv(d, "Recording copy", M.BLOCKS % n)
    kv(d, "Runtime class", M.mode(n))
    kv(d, "Estimated speech", "%s to %s at 130 to 145 words per minute, from "
                              "%d spoken words" % (fast, slow, w))
    caption(d, "That range is arithmetic on the script. It is not a runtime "
               "and not a target. The actual length is whatever Temidayo's "
               "natural delivery produces, and it is observed after "
               "recording, not before.")
    callout(d, "Read one thought block silently. Look toward the lens. "
               "Deliver it naturally. Stop. Reset posture and hands. Take "
               "the next block. The section labels are production aids and "
               "are never spoken.")
    h(d, "Before the take")
    numbered(d, [
      "Read the whole script once, out loud, without recording.",
      "Light from in front, not beside. This outranks every production "
      "change.",
      "Frame 16:9 horizontal, minimum 1920 by 1080, headroom preserved.",
      "Record a level check and listen back on headphones.",
      "Have the thought-block recording copy open, not this document.",
    ])
    h(d, "The story-led shape")
    bullets(d, [
      "The opening is a recognition moment. Deliver it to the lens and do "
      "not rush it. Nothing covers it.",
      "The bridges between the scene and the teaching are spoken, not "
      "edited. Let them breathe.",
      "The application moments, where the idea comes back to one real role "
      "or decision, are part of the viewer outcome. They are not filler and "
      "they are not cut.",
      "Frameworks arrive after the viewer recognizes the situation, not in "
      "the second sentence.",
    ])
    h(d, "Sections in order")
    table(d, ["#", "Section", "Spoken words"],
          [[str(i), lbl, str(sum(len(p.split()) for p in ps))]
           for i, (lbl, ps) in enumerate(M.sections(n), 1)],
          widths=[0.4, 4.6, 1.2], size=9)
    h(d, "Boundaries carried from the source")
    bullets(d, [
      "Section labels are never read aloud.",
      "No spoken Subscribe request. The Subscribe cue is visual only.",
      "Watch Next is full screen and final. Do not return to camera after "
      "it.",
      "Nothing is added to the spoken script at the desk. If a line does "
      "not work, stop and raise it rather than improvising a replacement.",
    ])
    d.save(path)
    return path
