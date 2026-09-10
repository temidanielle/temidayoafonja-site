# -*- coding: utf-8 -*-
"""Script-only thought-block copies for Videos 15 to 21.

The recording copy. Spoken script only. No production notes, no visual map,
no CTA analysis, no strategy commentary, no research notes.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from docsx import (base_doc, para, title_block, rule, block, section_label,
                   footer_note, NAVY, GOLD, DIM)


def build(v, out_path):
    d = base_doc()
    footer_note(d, "Video %d recording copy  |  spoken script only" % v["num"])

    para(d, "CAPABILITY FORMATION  |  VIDEO %d" % v["num"],
         size=9, bold=True, color=GOLD, after=4)
    para(d, v["title"], size=18, bold=True, color=NAVY, after=6)
    rule(d, after=10)
    para(d, "Read one block silently. Look toward the lens. Deliver it "
            "naturally. Stop. Then reset before the next one. The small gold "
            "labels are for finding your place. They are not spoken.",
         size=10, color=DIM, after=4)
    rule(d, after=12)

    for name, blocks in v["script"]:
        section_label(d, name)
        for b in blocks:
            block(d, b, size=13.5)

    d.save(out_path)
    return out_path
