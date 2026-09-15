# -*- coding: utf-8 -*-
"""Documents for the three candidate Shorts per video."""
import v1011 as S
from shorts1011 import rows, lines, verify, BOUNDARY, EDITOR, ANGLE, WPM
from docs1011 import (base_doc, title_block, h, kv, para, callout, sub,
                      caption, table, bullets, footer_note, page_break,
                      spoken, mono, hr, head, _wrap, EYEBROW)


def bank(n, path, stamp):
    d = base_doc()
    title_block(d, EYEBROW, S.title(n),
                "Three candidate Shorts, built from the script's own words")
    kv(d, "New public number", "V%d" % n)
    kv(d, "Former roadmap number", "None. This is a new concept.")
    kv(d, "Count", "Three. This is the current selection bank and was not "
                   "expanded.")
    kv(d, "Generated", stamp)
    callout(d, "Neither FINAL script carries a Shorts section, so nothing "
               "here was invented to fill one. Every line below is a whole "
               "sentence lifted verbatim from this video's spoken script, "
               "checked against it rather than assumed. Three means three: "
               "the bank was not expanded to six, and not all three have "
               "to be published. Each must stand alone without the "
               "long-form video.")
    table(d, ["#", "Stop scroll", "Words", "At 165 wpm"],
          [["%d" % r["num"], r["title"], format(r["words"], ","),
            "0:%02d" % r["secs"]] for r in rows(n)],
          widths=[0.35, 3.6, 0.8, 1.0], size=8.5)
    caption(d, "Lengths are arithmetic, not measured.")
    for r in rows(n):
        page_break(d)
        _one(d, n, r)
    d.save(path)
    return path


def _one(d, n, r):
    h(d, "Short %d  |  %s" % (r["num"], r["title"]))
    kv(d, "Length", "%d words, about 0:%02d at 165 words per minute"
       % (r["words"], r["secs"]))
    sub(d, "Stop scroll")
    for l in r["stop"]:
        para(d, l, size=13, bold=True, after=4)
    sub(d, "Hold attention")
    for l in r["hold"]:
        para(d, l, size=11, after=4)
    sub(d, "One ask")
    for l in r["ask"]:
        para(d, l, size=11, bold=True, after=4)
    sub(d, "Every line above")
    para(d, "Verbatim from the parent video's spoken script. No Short "
            "wording was invented and no claim was added to strengthen "
            "the hook.", size=10.5)
    sub(d, "Evidence boundary inherited from the long-form video")
    para(d, BOUNDARY[n], size=10.5)
    sub(d, "Editor note")
    para(d, EDITOR[n], size=10.5)
    sub(d, "Stands alone")
    para(d, "This Short is understandable without watching the long-form "
            "video. It is not a trailer, and the ask is the only ask.",
        size=10.5)


def single(n, r, path, stamp):
    d = base_doc()
    title_block(d, EYEBROW, "Short %d" % r["num"],
                "Candidate Short from NEW PUBLIC V%d" % n)
    kv(d, "Parent video", S.title(n))
    kv(d, "Generated", stamp)
    _one(d, n, r)
    footer_note(d, "Vertical. Shorts captions are set at upload.")
    d.save(path)
    return path


def editor_notes(n, path):
    L = head("NEW PUBLIC V%d  |  SHORTS VISUAL AND EDITOR NOTES" % n)
    L += [S.title(n), "",
          "Three candidates, built from the script's own sentences.",
          "The bank was not expanded.",
          "Not all three have to be published.",
          "", hr(), "", "SHARED RULES", "",
          "  9:16. The same navy, cream and warm gold system as the video.",
          "  Large type. One idea per card. Generous margins.",
          "  Reuse the long-form card where one exists, reframed to 9:16,",
          "  rather than building a different-looking version of it.",
          "  Each Short stands alone. It is not a trailer and it does not",
          "  require the long-form video to make sense.",
          "  One ask at the end. Never two.",
          "  No claim is added to strengthen a hook.",
          "", hr(), "", "EVIDENCE BOUNDARY FOR EVERY SHORT FROM THIS VIDEO",
          ""]
    L += ["  %s" % x for x in _wrap(BOUNDARY[n], 68)]
    L += ["", hr(), ""]
    for r in rows(n):
        L += ["SHORT %d  |  %s" % (r["num"], r["title"]),
              "    LENGTH:   %d words, about 0:%02d at 165 wpm"
              % (r["words"], r["secs"]),
              "    ONE ASK:  %s" % r["ask"][0],
              "    EDITOR:"]
        L += ["        %s" % x for x in _wrap(EDITOR[n], 62)]
        L.append("")
    return mono(path, L)


def boundary_notes(n, path, stamp):
    d = base_doc()
    title_block(d, EYEBROW, S.title(n),
                "Shorts evidence-boundary notes")
    kv(d, "New public number", "V%d" % n)
    kv(d, "Former roadmap number", "None. This is a new concept.")
    kv(d, "Generated", stamp)
    para(d, "Every Short inherits the research and evidence boundaries of "
            "its parent video. A Short is often where a boundary gets "
            "dropped for pace. It may not be dropped here.", size=11)
    h(d, "The boundary")
    callout(d, BOUNDARY[n])
    h(d, "Per Short")
    table(d, ["#", "Stop scroll", "The boundary it must carry"],
          [["%d" % r["num"], r["title"], BOUNDARY[n]] for r in rows(n)],
          widths=[0.35, 2.6, 3.75], size=8)
    footer_note(d, "No Short adds a claim to strengthen a hook, and none "
                   "introduces research the long-form video does not make.")
    d.save(path)
    return path
