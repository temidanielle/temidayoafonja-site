# -*- coding: utf-8 -*-
"""Short-form documents for the new scripts."""
import os
import masters23b as M
import shorts23b as SH
from docs23 import (base_doc, title_block, h, kv, para, callout, sub, caption,
                    table, bullets, footer_note, page_break, spoken, mono,
                    hr, head)


def bank(n, path, stamp):
    d = base_doc()
    title_block(d, "capability formation | v%d shorts" % n, M.title(n),
                "Six candidate Shorts. A selection bank, not six uploads.")
    kv(d, "Cadence", "About three Shorts per long-form video. Choose from "
                     "these six.")
    kv(d, "Generated", stamp)
    callout(d, "Rebuilt from the September 13 FINAL script. Every spoken "
               "line below is a whole paragraph of that script, in its own "
               "words. No Short from the previous package survives whose "
               "source wording disappeared.")
    table(d, ["Candidate", "Stop scroll", "Words", "At 165 wpm"],
          [[r["key"].split("_", 2)[2].replace("_", " "), r["hook"],
            format(r["words"], ","), "0:%02d" % r["secs"]]
           for r in SH.rows(n)],
          widths=[2.2, 2.4, 0.9, 1.0], size=8.5)
    caption(d, "Lengths are arithmetic, not measured. Each Short still has "
               "to satisfy stop scroll, hold attention, one ask.")
    for r in SH.rows(n):
        page_break(d)
        _one(d, r)
    d.save(path)
    return path


def _one(d, r):
    h(d, r["key"].split("_", 2)[2].replace("_", " "))
    kv(d, "Stop scroll", r["hook"])
    kv(d, "Length", "%d words, about 0:%02d at 165 words per minute"
       % (r["words"], r["secs"]))
    sub(d, "Spoken")
    for l in r["lines"]:
        spoken(d, l)
    sub(d, "One ask")
    spoken(d, r["ask"])
    sub(d, "Boundary that travels with this Short")
    para(d, r["boundary"], size=10.5)
    sub(d, "Editor note")
    para(d, r["note"], size=10.5)


def single(n, r, path, stamp):
    d = base_doc()
    title_block(d, "capability formation | v%d short" % n,
                r["key"].split("_", 2)[2].replace("_", " ").title(),
                "Candidate Short from %s" % M.title(n))
    kv(d, "Generated", stamp)
    _one(d, r)
    footer_note(d, "Vertical. Shorts captions are set at upload.")
    d.save(path)
    return path


def editor_notes(n, path):
    L = head("VIDEO %d  |  SHORTS VISUAL AND EDITOR INSTRUCTIONS" % n)
    L += [M.title(n), "",
          "Six candidates. Current cadence is about three per long-form",
          "video, so three of these six ship.",
          "", hr(), "", "SHARED RULES", "",
          "  9:16. The same navy, cream and warm gold system as the video.",
          "  Large type. One idea per card. Generous margins.",
          "  Reuse the long-form card where one exists, reframed to 9:16,",
          "  rather than rebuilding a different-looking version of it.",
          "  Every evidence boundary in the source video travels with the",
          "  line that needs it. A Short may not be the place the boundary",
          "  gets dropped.",
          "  One ask at the end. Never two.",
          "", hr(), ""]
    for r in SH.rows(n):
        L += ["%s" % r["key"],
              "    STOP SCROLL:  %s" % r["hook"],
              "    LENGTH:       %d words, about 0:%02d at 165 wpm"
              % (r["words"], r["secs"]),
              "    ONE ASK:      %s" % r["ask"],
              "    BOUNDARY:"]
        L += ["        %s" % x for x in _wrap(r["boundary"], 62)]
        L += ["    EDITOR:"]
        L += ["        %s" % x for x in _wrap(r["note"], 62)]
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
