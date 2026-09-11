# -*- coding: utf-8 -*-
"""02_Recording, 03_Visuals and 04_Riverside documents."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import masters421 as M
from frames421 import SETS
from docs421f import (base_doc, para, title_block, rule, h, kv, callout,
                       table, bullets, sub, field, page_break, footer_note,
                       block, section_label, notspoken, numbered, mono, hr,
                       head, NAVY, GOLD, DIM, RED)

# The standing rules, from Video 4 onward. Stated once here and referenced
# everywhere else, so no document can drift from another.
CAMERA = ("About 3 to 5 deliberate camera-emphasis beats across the whole "
          "video. This is one combined budget: gentle push-ins on tension, "
          "insight or a reframe, with occasional pull-backs or a return to "
          "base framing to reset the rhythm. It is not 3 to 5 push-ins plus "
          "3 to 5 pull-backs. No aggressive zooms, no pulsing, no constant "
          "reframing, no unnecessary digital movement. Preserve headroom and "
          "source quality.")

SOUND = ("About 4 to 7 restrained audio accents for the ENTIRE video, "
         "including the one visual Subscribe cue. The per-frame sound "
         "candidates in the visual map are OPTIONAL and are not cumulative. "
         "Choose only the moments with the highest visual or intellectual "
         "payoff. Keep every effect clearly quieter than the voice. Pair the "
         "sound with a small visual action so both land together. If no sound "
         "improves the moment, leave it silent.")

BROLL = ("About 2 to 4 meaningful full-screen B-roll moments where useful. "
         "This is not a quota. No generic handshakes, fake boardrooms, "
         "smiling coworkers, meaningless typing, AI-looking people, or "
         "invented employer documents presented as real. Where an example is "
         "constructed, it carries its label.")

CAPTIONS = ("NO BURNED-IN OR OPEN CAPTIONS on the long-form video. Viewers "
            "use YouTube CC. Deliver a clean export with no persistent "
            "subtitles, a complete final transcript with names, frameworks, "
            "URLs and industry terms proofread, and an SRT generated against "
            "the FINAL edited timeline with synchronization checked after "
            "every jump cut and removal. Do not delete transcript words "
            "because the camera is hidden behind a graphic. Shorts and Reels "
            "may use designed captions.")

FULLSCREEN = ("Frameworks, comparisons, multi-point concepts, substantive "
              "demonstrations, the resource card and Watch Next are TRUE FULL "
              "SCREEN. No moving Temidayo behind or around a major visual. "
              "Substantive B-roll fills the entire frame. Short single-idea "
              "callouts may sit over camera. After a full-screen teaching "
              "visual, return to camera only where the scene map calls for "
              "it. THIS NEVER APPLIES TO WATCH NEXT: Watch Next is the final "
              "visual and there is no return to camera afterward.")

SUBSCRIBE = ("One brief visual Subscribe cue after meaningful value has "
             "already been delivered. Visual only. There is no spoken "
             "Subscribe request in the master and none is added. About 1 to 3 "
             "seconds including entrance and exit. Do not interrupt a useful "
             "pause or cover teaching content.")

AUDIO = ("Recorded on a Shure microphone and the source may sit quieter than "
         "the final publishing level. Even out the speaking volume gently, "
         "keep natural dynamics, and improve dialogue consistency before the "
         "final loudness pass. No aggressive compression. No over-processed "
         "noise reduction, and no metallic or underwater artifacts. Preserve "
         "breaths and natural pauses where they sound normal. Keep the voice "
         "clearly dominant over music and effects and prevent clipping on "
         "louder words. Check by listening through headphones for "
         "intelligibility, room echo, breath pops, clipping, noise-reduction "
         "artifacts, abrupt gain changes and music masking the voice. Do not "
         "record audio as verified until the actual exported file has been "
         "listened to.")


def run_of_show(n, out_path, stamp):
    m = M.read(n)
    w, fast, slow = M.estimate(n)
    d = base_doc()
    footer_note(d, "Video %d run of show  |  built against the locked final "
                   "master" % n)
    title_block(d, "Capability Formation  |  Video %d" % n,
                "Recording Run of Show", M.title(n))
    kv(d, "Generated", stamp)
    kv(d, "Spoken source", "%s  ·  SHA-256 %s" % (m["file"], m["sha"]))
    kv(d, "Speech-only estimate", "%s to %s from %s spoken words at 130 to "
       "145 words per minute. Arithmetic on the script, not a timed read."
       % (fast, slow, "{:,}".format(w)))

    h(d, "Before the take")
    numbered(d, [
      "Read the whole script once, out loud, without recording.",
      "Set the light in front, not behind or beside. This outranks every "
      "other production change.",
      "Frame 16:9 horizontal, minimum 1920 by 1080, headroom preserved.",
      "Record a level check and listen back on headphones before starting.",
      "Have the script-only recording copy open, not this document.",
    ])

    h(d, "The opening, exactly as locked")
    para(d, m["sections"][0][1][0] if m["sections"] and m["sections"][0][1]
         else "", size=11.5, bold=True)
    para(d, "This is the approved opening. It is not re-hooked, re-ordered or "
            "improved at the desk.", size=9.5, color=DIM)

    h(d, "Sections in order")
    table(d, ["#", "Section", "Blocks"],
          [[str(i + 1), name or "(opening)", str(len(bs))]
           for i, (name, bs) in enumerate(m["sections"])],
          widths=[0.45, 4.6, 1.65], size=9)

    h(d, "The thought-block method")
    numbered(d, [
      "Read the block silently.",
      "Look toward the lens.",
      "Deliver it naturally.",
      "Stop.",
      "Reset posture and hands.",
      "Advance to the next block.",
    ])
    para(d, "One complete idea per block. Do not split every sentence into "
            "its own take, and preserve the intentional pauses inside a "
            "block. A block that was rushed is recorded again rather than "
            "repaired in the edit.", size=10, color=DIM)

    h(d, "Boundaries carried from the master")
    bullets(d, [t for t in m["tail"] if t not in
                ("EDITOR / VISUAL PRIORITIES", "FINAL QA",
                 "MAJOR VISUAL AND MOTION-GRAPHIC MAP",
                 "RESEARCH INTEGRITY NOTES | NOT SPOKEN")] or
            ["The master states its boundaries in its own tail sections."])

    h(d, "The exact final spoken line")
    para(d, M.final_line(n), size=11.5, bold=True, color=RED)
    para(d, "Nothing is recorded after this line. Watch Next follows as a "
            "visual and there is no return to camera.", size=9.5, color=DIM)

    h(d, "Ending checklist")
    numbered(d, [
      "The final spoken line is recorded and is the last thing on the take.",
      "No spoken Subscribe request was added. The Subscribe cue is a visual "
      "placed in post-production.",
      "The single call to action was spoken once, in the master's wording.",
      "The resource was named once if the master names one, and not "
      "otherwise.",
      "Anything the master labels a constructed example was said aloud as "
      "one.",
      "Room tone recorded, at least thirty seconds, after the final take.",
      "Files named and backed up before the setup is broken down.",
    ])
    d.save(out_path)
    return out_path


def trigger_map(n, out_path):
    L = head("VIDEO %d  |  SENTENCE TRIGGER MAP" % n)
    L += [M.title(n), "",
          "Every graphic with the exact spoken sentence that cues it.",
          "Each trigger was verified to exist inside a single thought block of",
          "the locked master, so no cue is built from words that span two",
          "takes.", "", hr(), ""]
    for i, f in enumerate(SETS[n], 1):
        L += ["%2d. %s" % (i, f["key"]),
              "    TRIGGER: %s" % f["trigger"].replace("\n", " "),
              "    MODE:    %s" % f["mode"],
              "    AFTER:   %s" % f["after"], ""]
    L += [hr(), "",
          "BEATS THAT ARE DELIBERATELY NOT GRAPHICS", "",
          "  The real personal account in the opening, where the master has",
          "  one, stays camera-led.",
          "  Any moment where the master's honesty depends on the viewer",
          "  watching Temidayo say it.",
          "  Anything a graphic would only decorate.", ""]
    return mono(out_path, L)


def visual_build_map(n, out_path):
    L = head("VIDEO %d  |  VISUAL BUILD MAP AND MOTION REVEAL MAP" % n)
    L += [M.title(n), "",
          "Support and reference assets for the Riverside editor. This is not",
          "a deck that covers the script paragraph by paragraph, and it is not",
          "a mandatory slideshow.", "", hr(), ""]
    for i, f in enumerate(SETS[n], 1):
        L += ["%2d. %s.png" % (i, f["key"]),
              "    STATUS:    %s" % f["status"],
              "    WHY:       %s" % f["why"],
              "    PURPOSE:   %s" % f["purpose"],
              "    TRIGGER:   %s" % f["trigger"].replace("\n", " "),
              "    MODE:      %s" % f["mode"],
              "    REVEAL:    %s" % f["reveal"],
              "    EMPHASIS:  %s" % f["emphasis"],
              "    HOLD:      %s" % f["hold"],
              "    CAPTIONS:  %s" % f["captions"],
              "    SOUND:     %s" % (f["sound"] or
                                     "No candidate. Leave it silent."),
              "    AFTER:     %s" % f["after"], ""]
    L += [hr(), "", "STANDING RULES", "",
          "FULL SCREEN", "  " + FULLSCREEN, "",
          "CAMERA", "  " + CAMERA, "",
          "SOUND BUDGET", "  " + SOUND, "",
          "B-ROLL", "  " + BROLL, "",
          "CAPTIONS", "  " + CAPTIONS, "",
          "SUBSCRIBE", "  " + SUBSCRIBE, ""]
    return mono(out_path, L)
