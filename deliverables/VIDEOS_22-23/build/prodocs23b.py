# -*- coding: utf-8 -*-
"""Production documents for the new scripts.

The new scripts carry section labels and no timing markers, so the run of
show uses the section sequence and says plainly that a sequence position is
not a runtime.
"""
import os
import masters23b as M
import frames23b as F
import spine23b as SP
from docs23 import (base_doc, title_block, h, kv, para, callout, sub, caption,
                    table, bullets, footer_note, mono, hr, head)

EDIT = [
 ("Camera emphasis beats", "3 to 5 across the video",
  "A gentle push-in or an occasional pull-back. Nothing that pulses."),
 ("Full-screen B-roll moments", "2 to 4, only where useful",
  "Substantive B-roll is full screen, never an overlay behind Temidayo."),
 ("Sound accents", "4 to 7, restrained",
  "Not every reveal gets one. Silence is part of the grammar."),
 ("Subscribe cue", "One, briefly, after value has landed",
  "Never before the first example has paid off."),
 ("Burned-in captions", "None in the long-form video",
  "Riverside generates the SRT after the final edit."),
]


def run_of_show(n, path, stamp):
    d = base_doc()
    title_block(d, "capability formation | v%d" % n, M.title(n),
                "Run of show")
    lo, hi = M.estimate(n)
    h(d, "Locked packaging")
    para(d, "Title", size=9, bold=True, after=2)
    para(d, M.title(n), size=13, bold=True, after=8)
    para(d, "Thumbnail", size=9, bold=True, after=2)
    para(d, M.script_header_thumbnail(n), size=13, bold=True, after=12)
    caption(d, "Both are exact. Thumbnail artwork is approved separately and "
               "is not part of this package.")
    kv(d, "Spoken words", "%s by whitespace count, %s as supplied"
       % (format(M.word_count(n), ","),
          format(M.DECLARED_WORDS[n], ",")))
    kv(d, "Arithmetic estimate", "%s to %s. Not a runtime." % (lo, hi))
    kv(d, "Generated", stamp)
    callout(d, "The numbers in the first column are sequence positions, not "
               "times. These scripts carry no timing markers at all. "
               "Chapters are cut after the final edit, from real export "
               "timing.")
    rows = []
    for i, (label, ps) in enumerate(M.sections(n), 1):
        keys = [f["key"] for f in F.SETS[n]
                if any(M._norm(f["trigger"]) == M._norm(p) for p in ps)]
        rows.append(["%d" % i, label,
                     format(sum(len(p.split()) for p in ps), ","),
                     "%d" % len(ps),
                     ", ".join(k.split("_", 2)[2].replace("_", " ").lower()
                               for k in keys) or "camera throughout"])
    table(d, ["#", "Section", "Words", "Paragraphs", "Full-screen cues"],
          rows, widths=[0.35, 1.9, 0.6, 0.85, 3.0], size=8.5)
    cam, full = SP.counts(n)
    on_cam = sum(len(p.split()) for x in SP.spine(n) if x[0] == "CAMERA"
                 for p in x[1])
    kv(d, "Balance", "%d camera stretches against %d full-screen cues. "
                     "%d of %s spoken words are delivered on camera."
       % (cam, full, on_cam, format(M.word_count(n), ",")))

    h(d, "Editing restraint")
    table(d, ["Element", "Target", "Note"], [[a, b, c] for a, b, c in EDIT],
          widths=[1.5, 1.7, 3.5], size=8.5)

    h(d, "The CTA card and the Watch Next card")
    bullets(d, [
      "The CTA card is full screen.",
      "The Watch Next card is full screen and final. There is no return to "
      "camera after it, and no outro, sting or sign-off follows it.",
      "The Watch Next card is silent. Nothing in the spoken script was "
      "changed to introduce it, and nothing needs to be.",
    ])

    h(d, "What is not decided here")
    bullets(d, [
      "Runtime. Every figure in this package is arithmetic on the script.",
      "Chapters. Created after the final edit, from actual export timing.",
      "SRT. Generated in Riverside after the final edit and verified "
      "against the final export.",
      "Thumbnail artwork. Only the thumbnail wording is locked.",
    ])
    footer_note(d, "Camera-led. Story, recognition, consequence and "
                   "interpretation stay on Temidayo.")
    d.save(path)
    return path


def camera_map(n, path):
    L = head("VIDEO %d  |  CAMERA AND FULL-SCREEN MAP" % n)
    L += [M.title(n), "",
          "Every stretch of this video is marked. CAMERA means Temidayo",
          "carries the moment and no graphic should appear over her.",
          "FULL SCREEN means the idea takes the screen, with no presenter",
          "moving behind it and no semi-transparent overlay.",
          "", hr(), ""]
    cam, full = SP.counts(n)
    L += ["  %d camera stretches" % cam,
          "  %d full-screen cues, one per active card" % full, "", hr(), ""]
    for kind, *rest in SP.spine(n):
        if kind == "SECTION":
            seq, label = rest
            L += ["", hr(), "SECTION %d  %s" % (seq, label.upper()), hr(), ""]
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
    L += [hr(), "", "RETIRED FROM THE ACTIVE EDIT", ""]
    for k, why in sorted(F.RETIRED.items()):
        if k.startswith("V%d" % n):
            L += ["  %s" % k] + ["      %s" % x for x in _wrap(why, 68)] + [""]
    return mono(path, L)


def motion_map(n, path):
    L = head("VIDEO %d  |  MOTION AND REVEAL MAP" % n)
    L += [M.title(n), "",
          "Reveal order for every card that has more than one state, and the",
          "emphasis state of each. Because YouTube is not interactive, a",
          "numbered point is a reading order, never a button.",
          "", hr(), ""]
    for f in F.SETS[n]:
        L += ["%s   (%s)" % (f["key"], f["cls"]),
              "    TRIGGER:    %s" % " ".join(f["trigger"].split()),
              "    LAYOUT:     %s" % f["layout"],
              "    TREATMENT:  %s" % f["treatment"],
              "    BUILD:      %s" % f["build"]]
        for i, s in enumerate(f["states"], 1):
            L.append("    %d. %-42s %s" % (i, s["name"], s["reveal"]))
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
    L = head("VIDEO %d  |  AUDIO AND SOUND CUE MAP" % n)
    L += [M.title(n), "",
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
            L += ["  %-44s %s" % (f["key"], f["sound"])]
    L += ["", hr(), "",
          "  Music: no track is licensed or selected in this package.",
          "  Loudness, balance and picture quality are final-export QA.", ""]
    return mono(path, L)


def asset_index(n, path, files, extra=None):
    L = head("VIDEO %d  |  ASSET INDEX" % n)
    L += [M.title(n), "",
          "%d active families, %d image states, plus %d Watch Next candidate "
          "cards." % (len(F.SETS[n]), len(F.states(n)), len(extra or [])),
          "PNG is 1920 x 1080. An SVG is provided where a designer may need",
          "to re-time or recolor the card; its text is live and the brand",
          "faces are embedded.",
          "", hr(), ""]
    for f in list(F.SETS[n]) + list(extra or []):
        L += ["%s" % f["key"],
              "    CLASS:      %s" % f["cls"],
              "    PURPOSE:    %s" % f["purpose"],
              "    TREATMENT:  %s" % f["treatment"]]
        for s in f["states"]:
            got = [x for x in files if x.startswith(s["name"] + ".")]
            L.append("    %-44s %s" % (s["name"] + ".png",
                                       ", ".join(sorted(got))))
        if f["source"]:
            L.append("    SOURCE:     %s" % f["source"])
        L.append("")
    L += [hr(), "", "RETIRED FROM THE ACTIVE EDIT", "",
          "  These families were in the previous package. The new script",
          "  does not teach them, so they carry no cue and no file here.", ""]
    for k, why in sorted(F.RETIRED.items()):
        if k.startswith("V%d" % n):
            L += ["  %s" % k] + ["      %s" % x for x in _wrap(why, 68)] + [""]
    return mono(path, L)


BROLL = {
 22: [("Reading on a laptop, over the shoulder, no screen legible",
       "Under the promise section only. The postings themselves are shown "
       "as built cards, never as a filmed screen.",
       "Full screen if used at all. Never behind a framework card."),
      ("Hands and a notebook, writing four short words",
       "Under the CTA, or under the method recap in the boundary section.",
       "Full screen. No text overlay."),
      ("A quiet desk at the end of a working day",
       "Under the boundary section, where the video admits what the method "
       "cannot do.",
       "Full screen, short. Do not use it to soften the boundary.")],
 23: [("Hands writing four lines on paper",
       "Under the CTA, or under the sentence about the second line taking "
       "the longest.",
       "Full screen. The written words must not be legible as a different "
       "example."),
      ("A whiteboard being wiped clean",
       "Only if the cut between the judgment beat and the proof beat needs "
       "air.",
       "Full screen, brief.")],
}


def broll(n, path):
    L = head("VIDEO %d  |  B-ROLL RECOMMENDATIONS" % n)
    L += [M.title(n), "",
          "Two to four full-screen moments at most, and only where the cut",
          "needs them. Nothing here is required for the video to work.",
          "", hr(), ""]
    for shot, where, how in BROLL[n]:
        L += ["  %s" % shot, "      WHERE:  %s" % where,
              "      HOW:    %s" % how, ""]
    L += [hr(), "",
          "  No stock footage of an office that implies a named employer.",
          "  No screen recording of a live job board.",
          "  No filmed posting page: the postings appear as built cards",
          "  from the preserved capture, not from a page reopened later.", ""]
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
