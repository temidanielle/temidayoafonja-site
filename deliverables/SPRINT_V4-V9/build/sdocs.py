# -*- coding: utf-8 -*-
"""Document builders for the sprint packages.

Every major document states both numbers: the new public number and the
former roadmap number it came from.
"""
import os, sys
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.append(DELIV + "VIDEOS_22-23/build")
sys.path.append(DELIV + "VIDEOS_4-21_CORRECTED_RUNTIME/build")

import sprint as S
import frames as F
import spine as SP
from docs23 import (base_doc, para, title_block, rule, h, kv, callout, table,
                    bullets, sub, field, page_break, footer_note, caption,
                    spoken, marker, cue, mono, hr, head, NAVY, GOLD, DIM, RED)

EYEBROW = "capability formation | two-week sprint"


def label(n):
    return "NEW V%d  ·  FORMER ROADMAP V%d" % (n, S.NUMBERS[n])


def header(d, n, kind, stamp):
    title_block(d, EYEBROW, S.title(n), kind)
    kv(d, "New public number", "V%d" % n)
    kv(d, "Former roadmap number", "V%d" % S.NUMBERS[n])
    kv(d, "Thumbnail", S.thumbnail(n))
    kv(d, "Spoken words", format(S.word_count(n), ","))
    lo, hi = S.estimate(n)
    kv(d, "Arithmetic estimate", "%s to %s at 130 to 145 words per minute. "
                                 "Not a runtime." % (lo, hi))
    kv(d, "Source", S.read(n)["file"])
    kv(d, "Source SHA-256", S.read(n)["sha"])
    kv(d, "Generated", stamp)


def recording_master(n, path, stamp):
    d = base_doc()
    header(d, n, "Final sprint recording master", stamp)
    callout(d, "This is the approved sprint script, word for word. The "
               "headings are section labels, not timing markers: this script "
               "carries no timestamps. Nothing in a bracketed cue is spoken, "
               "and the three candidate Shorts are not part of this "
               "recording.")
    for kind, *rest in SP.spine(n):
        if kind == "SECTION":
            seq, lab = rest
            marker(d, "%d" % seq, lab)
        elif kind == "CAMERA":
            for p in rest[0]:
                spoken(d, p)
        else:
            f, p = rest
            cue(d, "full screen", f["states"][0]["name"],
                "%d state%s. %s" % (len(f["states"]),
                                    "" if len(f["states"]) == 1 else "s",
                                    f["purpose"]))
            spoken(d, p)
    sub(d, "Watch Next, spoken")
    para(d, S.watch_next(n), size=12, bold=True, color=NAVY)
    caption(d, "The spoken Watch Next wording above is preserved exactly. "
               "The end card is full screen and final; nothing returns to "
               "camera after it.")
    footer_note(d, "Runtime is observed at Temidayo's natural delivery pace. "
                   "Chapters are created after the final edit, from real "
                   "export timing.")
    d.save(path)
    return path


def run_of_show(n, path, stamp):
    d = base_doc()
    title_block(d, EYEBROW, S.title(n), "Run of show")
    kv(d, "New public number", "V%d" % n)
    kv(d, "Former roadmap number", "V%d" % S.NUMBERS[n])
    h(d, "Locked packaging")
    para(d, "Title", size=9, bold=True, after=2)
    para(d, S.title(n), size=13, bold=True, after=8)
    para(d, "Thumbnail", size=9, bold=True, after=2)
    para(d, S.thumbnail(n), size=13, bold=True, after=12)
    caption(d, "Both are exact. Thumbnail artwork is approved separately and "
               "is not part of this package.")
    lo, hi = S.estimate(n)
    kv(d, "Spoken words", format(S.word_count(n), ","))
    kv(d, "Arithmetic estimate", "%s to %s. Not a runtime." % (lo, hi))
    kv(d, "Generated", stamp)
    callout(d, "The numbers in the first column are sequence positions, not "
               "times. This script carries no timing markers. Chapters are "
               "cut after the final edit, from real export timing.")
    rows = []
    for i, (lab, ps) in enumerate(S.sections(n), 1):
        keys = [f["key"] for f in F.SETS[n] if f["trigger"]
                and any(S._norm(f["trigger"]) == S._norm(p) for p in ps)]
        rows.append(["%d" % i, lab,
                     format(sum(len(p.split()) for p in ps), ","),
                     "%d" % len(ps),
                     ", ".join(k.split("_", 3)[-1].replace("_", " ").lower()
                               for k in keys) or "camera throughout"])
    table(d, ["#", "Section", "Words", "Paragraphs", "Full-screen cues"],
          rows, widths=[0.35, 1.9, 0.6, 0.85, 3.0], size=8.5)
    cam, full = SP.counts(n)
    kv(d, "Balance", "%d camera stretches against %d full-screen cues. %d of "
                     "%s spoken words are delivered on camera."
       % (cam, full, SP.on_camera_words(n), format(S.word_count(n), ",")))

    h(d, "Recording and editing intent")
    table(d, ["Element", "Target", "Note"],
          [["Camera emphasis beats", "3 to 5 across the video",
            "A gentle push-in or an occasional pull-back. Nothing that "
            "pulses."],
           ["B-roll moments", "2 to 4, only where useful",
            "Substantive B-roll is full screen, never an overlay behind "
            "Temidayo."],
           ["Sound accents", "4 to 7, restrained",
            "Not every reveal gets one. Silence is part of the grammar."],
           ["Subscribe cue", "One, briefly, after value has landed",
            "Never before the first teaching beat has paid off."],
           ["Burned-in captions", "None in the long-form video",
            "Riverside generates the SRT after the final edit."]],
          widths=[1.5, 1.7, 3.5], size=8.5)

    h(d, "The CTA card and the Watch Next card")
    bullets(d, [
      "The CTA card is full screen.",
      "The Watch Next card is full screen and final. There is no return to "
      "camera after it, and no outro or sign-off follows it.",
      "The spoken Watch Next wording is the script's own and was not "
      "changed. The destination is %s." % S.watch_next(n),
    ])

    h(d, "What is not decided here")
    bullets(d, [
      "Runtime. Every figure in this package is arithmetic on the script.",
      "Chapters. Created after the final edit, from actual export timing.",
      "SRT. Generated in Riverside after the final edit.",
      "Thumbnail artwork. Only the thumbnail wording is locked.",
      "Whether the intended Watch Next destination is publicly live on "
      "launch day. That is confirmed before upload.",
    ])
    footer_note(d, "Camera-led. Story, recognition, consequence and "
                   "interpretation stay on Temidayo.")
    d.save(path)
    return path


def camera_map(n, path):
    L = head("NEW V%d  (FORMER ROADMAP V%d)  |  CAMERA AND FULL-SCREEN MAP"
             % (n, S.NUMBERS[n]))
    L += [S.title(n), "",
          "Every stretch of this video is marked. CAMERA means Temidayo",
          "carries the moment and no graphic should appear over her.",
          "FULL SCREEN means the idea takes the screen, with no presenter",
          "moving behind it and no semi-transparent overlay.",
          "", hr(), ""]
    cam, full = SP.counts(n)
    L += ["  %d camera stretches" % cam,
          "  %d full-screen cues, one per card" % full,
          "  %d of %d spoken words delivered on camera"
          % (SP.on_camera_words(n), S.word_count(n)), "", hr(), ""]
    for kind, *rest in SP.spine(n):
        if kind == "SECTION":
            seq, lab = rest
            L += ["", hr(), "SECTION %d  %s" % (seq, lab.upper()), hr(), ""]
        elif kind == "CAMERA":
            ps = rest[0]
            L.append("  [ CAMERA ]  %d paragraph%s, %d words"
                     % (len(ps), "" if len(ps) == 1 else "s",
                        sum(len(p.split()) for p in ps)))
            for p in ps:
                flat = " ".join(p.split())
                L.append("      %s" % (flat[:96]
                                       + ("..." if len(flat) > 96 else "")))
            L.append("")
        else:
            f, p = rest
            L.append("  [ FULL SCREEN ]  %s   (%s)" % (f["key"], f["cls"]))
            L.append("      TRIGGER:  %s" % " ".join(f["trigger"].split()))
            L.append("      STATES:   %s"
                     % ", ".join(s["name"] for s in f["states"]))
            L.append("      HOLD:     %s" % f["hold"])
            L.append("")
    wn = [f for f in F.SETS[n] if f["treatment"] == "WATCH NEXT"][0]
    L += ["", hr(), "WATCH NEXT  |  FULL SCREEN AND FINAL", hr(), "",
          "  [ FULL SCREEN ]  %s" % wn["key"],
          "      SPOKEN LINE: %s" % " ".join(S.paragraphs(n)[-1].split()),
          "      DESTINATION: %s" % S.watch_next(n),
          "      Nothing returns to camera after this card.", ""]
    return mono(path, L)


def motion_map(n, path):
    L = head("NEW V%d  (FORMER ROADMAP V%d)  |  MOTION AND REVEAL MAP"
             % (n, S.NUMBERS[n]))
    L += [S.title(n), "",
          "Reveal order for every card with more than one state, and the",
          "emphasis state of each. A numbered point is a reading order,",
          "never a button.",
          "", hr(), ""]
    for f in F.SETS[n]:
        L += ["%s   (%s)" % (f["key"], f["cls"]),
              "    TRIGGER:    %s" % (" ".join(f["trigger"].split())
                                      if f["trigger"] else
                                      "the spoken Watch Next line"),
              "    LAYOUT:     %s" % f["layout"],
              "    TREATMENT:  %s" % f["treatment"],
              "    BUILD:      %s" % f["build"]]
        for i, s in enumerate(f["states"], 1):
            L.append("    %d. %-44s %s" % (i, s["name"], s["reveal"]))
        L += ["    HOLD:       %s" % f["hold"], ""]
    L += [hr(), "", "STANDING RULES", "",
          "  One active idea at a time. When a framework is being taught,",
          "  one component is warm and the rest are quiet.",
          "",
          "  Establish the whole structure before activating any part of it.",
          "",
          "  No animation whose only purpose is to keep the screen moving.",
          "  Stillness is allowed when the viewer needs to read or think.",
          "",
          "  No fake buttons, progress bars, quiz interfaces or dashboards.",
          "",
          "  A card never moves while the presenter moves behind it.", ""]
    return mono(path, L)


def sound_map(n, path):
    L = head("NEW V%d  (FORMER ROADMAP V%d)  |  AUDIO AND SOUND CUE MAP"
             % (n, S.NUMBERS[n]))
    L += [S.title(n), "",
          "Four to seven restrained accents across the video. Not every",
          "reveal gets one, and nothing is scored to keep energy up.",
          "", hr(), ""]
    for f in F.SETS[n]:
        if f["sound"].lower().startswith("no accent"):
            continue
        L += ["%s" % f["key"], "    %s" % f["sound"], ""]
    L += [hr(), "", "SILENT BY DESIGN", ""]
    for f in F.SETS[n]:
        if f["sound"].lower().startswith("no accent"):
            L += ["  %-46s %s" % (f["key"], f["sound"])]
    L += ["", hr(), "",
          "  Music: no track is licensed or selected in this package.",
          "  Loudness, balance and picture quality are final-export QA.", ""]
    return mono(path, L)


BROLL = {
 4: [("Hands writing three column headings on paper",
      "Under the audit section, if the cut needs a breath.",
      "Full screen. The words must not be legible as a different example."),
     ("A quiet desk with a laptop closed",
      "Under the boundary section, where the video refuses a single "
      "outcome.",
      "Full screen, short. No glowing interface, no robot imagery.")],
 5: [("Hands and a notebook, writing a single question",
      "Under the review-point section.",
      "Full screen. No text overlay."),
     ("An empty meeting room after a meeting",
      "Under the hook or the close, if the cut needs air.",
      "Full screen, brief. Nothing that implies a specific employer.")],
 6: [("Reading on a laptop, over the shoulder, no screen legible",
      "Under the promise section only. The postings are shown as built "
      "cards, never as a filmed screen.",
      "Full screen if used at all. Never behind a framework card."),
     ("Hands and a notebook, writing four short words",
      "Under the CTA.", "Full screen. No text overlay.")],
 7: [("A corridor or doorway outside a meeting",
      "Under the hook, where two capable people are described.",
      "Full screen, short. No identifiable workplace."),
     ("Hands writing three past assignments on paper",
      "Under the read-your-own-situation section.",
      "Full screen. The writing must not be legible as a real employer.")],
 8: [("A notebook page with a short handwritten entry",
      "Under the ten-minute habit section.",
      "Full screen. Handwriting only. No screen, no document, no file."),
     ("A desk at the end of a working day",
      "Under the close.",
      "Full screen, short. Nothing that depicts a system or a login.")],
 9: [("Sorting objects into groups on a table",
      "Under the sorting image in the story section.",
      "Full screen. The sorting is the point; nothing needs labels."),
     ("Hands drawing four columns on paper",
      "Under the application section.",
      "Full screen. No text overlay.")],
}
BROLL_LIMITS = {
 4: "No glowing robots, no futuristic stock, no server rooms. AI imagery "
    "only where it is substantive, and this video needs none.",
 5: "Nothing that implies a specific employer or a specific manager.",
 6: "No screen recording of a live job board. No filmed posting page.",
 7: "No identifiable workplace, no reenacted promotion conversation.",
 8: "Never depict taking a file, a screenshot, a download, or any "
    "circumvention of access control. No fake internal system.",
 9: "No luggage or airport metaphors. The sorting image is the script's own.",
}


def broll(n, path):
    L = head("NEW V%d  (FORMER ROADMAP V%d)  |  B-ROLL NOTES"
             % (n, S.NUMBERS[n]))
    L += [S.title(n), "",
          "Two to four full-screen moments at most, and only where the cut",
          "needs them. Nothing here is required for the video to work.",
          "", hr(), ""]
    for shot, where, how in BROLL[n]:
        L += ["  %s" % shot, "      WHERE:  %s" % where,
              "      HOW:    %s" % how, ""]
    L += [hr(), "", "DO NOT", ""]
    L += ["  %s" % x for x in _wrap(BROLL_LIMITS[n], 70)]
    L += ["", "  No stock footage that implies a named employer.",
          "  Substantive B-roll is full screen, never an overlay.", ""]
    return mono(path, L)


def asset_index(n, path, files):
    L = head("NEW V%d  (FORMER ROADMAP V%d)  |  ASSET INDEX"
             % (n, S.NUMBERS[n]))
    L += [S.title(n), "",
          "%d families, %d image states." % (len(F.SETS[n]),
                                             len(F.states(n))),
          "PNG is 1920 x 1080. An SVG is provided where a designer may need",
          "to re-time or recolor the card; its text is live and the brand",
          "faces are embedded.",
          "", hr(), ""]
    for f in F.SETS[n]:
        L += ["%s" % f["key"],
              "    CLASS:      %s" % f["cls"],
              "    PURPOSE:    %s" % f["purpose"],
              "    TREATMENT:  %s" % f["treatment"]]
        for s in f["states"]:
            got = [x for x in files if x.startswith(s["name"] + ".")]
            L.append("    %-46s %s" % (s["name"] + ".png",
                                       ", ".join(sorted(got))))
        if f["source"]:
            L += ["    SOURCE:"]
            L += ["        %s" % x for x in _wrap(f["source"], 62)]
        L.append("")
    return mono(path, L)


def _wrap(t, w):
    out, cur = [], ""
    for x in t.split():
        s = (cur + " " + x).strip()
        if len(s) > w and cur:
            out.append(cur)
            cur = x
        else:
            cur = s
    if cur:
        out.append(cur)
    return out
