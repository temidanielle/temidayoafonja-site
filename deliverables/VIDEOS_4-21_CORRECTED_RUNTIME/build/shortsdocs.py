# -*- coding: utf-8 -*-
"""05_Shorts documents: the combined Word file, one file per Short, and the
priority and source manifest."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import masters421 as M
from shorts421 import SHORTS, SPM
from docs421f import (base_doc, para, title_block, rule, h, kv, callout,
                       table, bullets, sub, field, page_break, footer_note,
                       block, section_label, numbered, mono, hr, head,
                       NAVY, GOLD, DIM, RED)


def words(s):
    return sum(len(l.split()) for l in s["lines"]) + len(s["cta"].split())


def seconds(s):
    return words(s) / SPM * 60.0


def _one(d, n, s, heading=True):
    if heading:
        para(d, "PRIORITY %s  ·  VIDEO %d SHORT" % (s["priority"], n),
             size=9, bold=True, color=GOLD, after=4)
        para(d, s["title"], size=16, bold=True, color=NAVY, after=4)
        para(d, "%s  ·  %d spoken words  ·  about %d seconds at 165 words per "
                "minute" % (s["slug"], words(s), round(seconds(s))),
             size=9, color=DIM, after=8)
        rule(d, after=10)
    sub(d, "First spoken line")
    para(d, s["lines"][0], size=12, bold=True)
    sub(d, "Full script")
    for line in s["lines"]:
        block(d, line, size=12.5, after=10)
    sub(d, "Final spoken line, which is the ask")
    para(d, s["cta"], size=12.5, bold=True, color=RED)
    sub(d, "Caption treatment")
    para(d, s["captions"], size=10.5)
    sub(d, "Visual treatment")
    para(d, s["visual"], size=10.5)
    sub(d, "Sound")
    para(d, s["sound"], size=10.5)
    sub(d, "Source in the locked master")
    para(d, s["source"], size=10.5)


def combined(n, out_path, stamp):
    d = base_doc()
    footer_note(d, "Video %d Shorts  |  vertical scripts, built against the "
                   "locked final master" % n)
    title_block(d, "Capability Formation  |  Video %d" % n,
                "Six Short-Form Recording Scripts", M.title(n))
    kv(d, "Generated", stamp)
    kv(d, "Source", "%s  ·  SHA-256 %s" % (M.FILES[n], M.read(n)["sha"]))
    kv(d, "Split", "4 Priority A, 2 Priority B")
    callout(d, "Each Short is a full vertical script, not an excerpt "
               "timestamp. A Short does not have to copy the long-form "
               "opening, but nothing here introduces a claim the locked "
               "master does not support. Timings are arithmetic at 165 words "
               "per minute, not timed reads.")
    h(d, "The six")
    table(d, ["Priority", "Short", "Words", "About"],
          [[s["priority"], s["title"], str(words(s)),
            "%d sec" % round(seconds(s))] for s in SHORTS[n]],
          widths=[0.8, 4.0, 0.8, 1.1], size=9)
    h(d, "Shorts treatment rules")
    bullets(d, [
      "Vertical. Designed captions are permitted on Shorts and Reels, unlike "
      "the long-form video.",
      "Tighter jump cuts, selective punch-ins and stronger visual movement "
      "are permitted.",
      "Still avoid clutter, constant zooming, excessive sound, and captions "
      "that cannot be read at phone size.",
      "One primary ask per Short. The final spoken line is that ask.",
      "No manufactured fear, fake vulnerability, unsupported social proof, "
      "artificial scarcity or promised outcomes.",
    ])
    for s in SHORTS[n]:
        page_break(d)
        _one(d, n, s)
    d.save(out_path)
    return out_path


def individual(n, s, out_path):
    d = base_doc()
    footer_note(d, "Video %d Short  |  %s" % (n, s["slug"]))
    para(d, "CAPABILITY FORMATION  |  VIDEO %d SHORT  |  PRIORITY %s"
         % (n, s["priority"]), size=9, bold=True, color=GOLD, after=4)
    para(d, s["title"], size=17, bold=True, color=NAVY, after=6)
    rule(d, after=10)
    _one(d, n, s, heading=False)
    d.save(out_path)
    return out_path


def manifest(n, out_path):
    L = head("VIDEO %d  |  SHORTS PRIORITY AND SOURCE MANIFEST" % n)
    L += [M.title(n), "",
          "Six Shorts. Four Priority A, two Priority B.",
          "Timings are arithmetic at 165 words per minute. Not timed reads.",
          "", hr(), ""]
    for s in SHORTS[n]:
        L += ["PRIORITY %s  %s" % (s["priority"], s["slug"]),
              "    TITLE:  %s" % s["title"],
              "    WORDS:  %d   ABOUT %d SECONDS" % (words(s),
                                                     round(seconds(s))),
              "    FIRST:  %s" % s["lines"][0],
              "    FINAL:  %s" % s["cta"],
              "    SOURCE: %s" % s["source"], ""]
    return mono(out_path, L)
