# -*- coding: utf-8 -*-
"""Recording Master DRAFT documents for Videos 15 to 21."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from docsx import (base_doc, para, title_block, rule, h, kv, callout, table,
                   bullets, sub, field, page_break, footer_note, block,
                   section_label, notspoken, numbered, NAVY, GOLD, DIM, RED)

WPM_FAST, WPM_SLOW = 145.0, 130.0


def word_count(v):
    return sum(len(b.split()) for _, blocks in v["script"] for b in blocks)


def estimate(v):
    w = word_count(v)
    def mmss(m):
        return "%d:%02d" % (int(m), round((m - int(m)) * 60))
    return w, mmss(w / WPM_FAST), mmss(w / WPM_SLOW)


def block_count(v):
    return sum(len(blocks) for _, blocks in v["script"])


CLOSE_CHECKLIST = [
 "The last spoken line is recorded and it is the last thing on the take. "
 "Nothing is recorded after it.",
 "Every thought block has one clean take with a settled start and a settled "
 "finish. A block that was rushed gets recorded again rather than fixed in "
 "the edit.",
 "The intentional pauses are performed, not left to be added afterward.",
 "The single call to action is spoken once, in the wording in this script. "
 "No second ask is added at the desk.",
 "No spoken Subscribe request was added. The Subscribe cue is a visual, "
 "placed in post-production.",
 "Anything labeled an illustration was said out loud as an illustration.",
 "Anything in the boundaries section that was going to be improvised was "
 "not improvised.",
 "Room tone recorded, at least thirty seconds, after the final take.",
 "Files named and backed up before the recording setup is broken down.",
]


def build(v, out_path, stamp):
    w, fast, slow = estimate(v)
    d = base_doc()
    footer_note(d, "Capability Formation  |  Video %d recording master  |  "
                   "SCRIPT DRAFT FOR EDITORIAL REVIEW. Not locked, not "
                   "approved for production." % v["num"])

    title_block(d, "Capability Formation  |  Video %d" % v["num"],
                v["title"],
                "Recording master, draft for editorial review")
    kv(d, "Created / revised", stamp)
    kv(d, "Status", "SCRIPT DRAFT FOR EDITORIAL REVIEW")
    kv(d, "Recommended title", v["title"])
    kv(d, "Recommended thumbnail", v["thumbnail"])
    kv(d, "Target runtime", v["runtime"])
    kv(d, "Speech-only estimate", "%s to %s from %s spoken words, at 130 to "
                                  "145 words per minute" % (fast, slow,
                                                            "{:,}".format(w)))
    kv(d, "Framework", v["framework"])
    kv(d, "Primary CTA", v["cta"])
    kv(d, "Resource", v["resource"])
    kv(d, "Watch Next", v["watchnext"])

    callout(d, "This is a draft for editorial review. It is not locked, not "
               "approved, and not a production instruction. No production "
               "package, Riverside prompt, Short, thumbnail, description or "
               "chapter list exists for this video.")

    para(d, "The runtime figure is arithmetic on the script at the roadmap's "
            "own 130 to 145 words per minute band, counting the spoken "
            "script only. It excludes pauses and visual holds. It is not a "
            "timed read and not a finished runtime.", size=9.5, color=DIM)

    h(d, "Editorial direction")
    notspoken(d, "Not spoken. Direction for the recording desk and the "
                 "editorial review.")
    bullets(d, v["direction"])

    h(d, "Factual and editorial boundaries")
    notspoken(d, "Not spoken. These are the lines this video does not cross. "
                 "If a line here conflicts with something improvised at the "
                 "desk, this section wins and the take is recorded again.")
    bullets(d, v["boundaries"])

    page_break(d)
    h(d, "Recording script")
    para(d, "%d thought blocks across %d sections. Section labels are working "
            "labels for the desk and are never spoken. Each block is one "
            "complete idea and one take."
            % (block_count(v), len(v["script"])), size=9.5, color=DIM)
    rule(d, after=8)
    for name, blocks in v["script"]:
        section_label(d, name)
        for b in blocks:
            block(d, b)

    h(d, "Major visual and motion-graphic map")
    para(d, "Planning guidance only, and reference for the eventual editor. "
            "These are the hero moments, not a shot list, and no asset is "
            "built or approved by this document.", size=9.5, color=DIM)
    table(d, ["Moment", "What it is"],
          [[a, b] for a, b in v["visual_map"]],
          widths=[1.95, 4.75], size=9)

    h(d, "Recording close checklist")
    numbered(d, CLOSE_CHECKLIST)

    rule(d)
    para(d, "SCRIPT DRAFT FOR EDITORIAL REVIEW. NOT LOCKED. NOT APPROVED FOR "
            "PRODUCTION.", size=10.5, bold=True, color=RED)
    d.save(out_path)
    return out_path
