# -*- coding: utf-8 -*-
"""07_Viewer_Exercise. One script-aligned exercise per video.

Each exercise is the artifact the master's own CTA asks for. Nothing is added
beyond what the script already teaches.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import masters421 as M
from docs421f import (base_doc, para, title_block, rule, h, kv, callout,
                       table, bullets, sub, footer_note, numbered,
                       NAVY, GOLD, DIM, RED)

from content421 import EX, ROUTES
from publish421 import route, primary_cta


def build(n, out_path, stamp):
    name, steps, limits = EX[n]
    d = base_doc()
    footer_note(d, "Video %d viewer exercise  |  aligned to the locked final "
                   "master" % n)
    title_block(d, "Capability Formation  |  Video %d" % n, name,
                M.title(n))
    kv(d, "Generated", stamp)
    ask, cue = primary_cta(n)
    kv(d, "The video's own CTA", ask)
    kv(d, "Spoken where", cue)
    res = route(n)
    kv(d, "Resource", "%s: https://%s" % (res, ROUTES[res]) if res else
       "None. This video names no resource and none is added.")
    callout(d, "This exercise is the artifact the script already asks for. It "
               "adds no new claim, no new framework and no new offer.")
    h(d, "Do this")
    numbered(d, steps)
    h(d, "What this exercise cannot do")
    bullets(d, limits)
    h(d, "Where it goes")
    para(d, "Keep it somewhere you will reread it. The value is in having "
            "written it down, not in the format.")
    d.save(out_path)
    return out_path
