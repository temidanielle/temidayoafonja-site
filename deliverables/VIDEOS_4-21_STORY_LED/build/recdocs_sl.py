# -*- coding: utf-8 -*-
"""01_Recording_Master. The story-led script and its thought block."""
import os, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                "VIDEOS_4-21_CORRECTED_RUNTIME/build")
import masters_sl as M
from docs421f import (base_doc, para, title_block, h, kv, callout, table,
                      bullets, caption, footer_note, block, section_label,
                      notspoken, numbered, NAVY, GOLD, DIM, RED)


def copy_sources(n, outdir):
    """Both source files, byte for byte. Never written to."""
    out = []
    for blocks in (False, True):
        src = M.path(n, blocks)
        dst = os.path.join(outdir, os.path.basename(src))
        shutil.copy2(src, dst)
        if M.sha256(dst) != M.sha256(src):
            raise SystemExit("V%d source copy does not match" % n)
        out.append(dst)
    return out


def reading_reference(n, path, stamp):
    m = M.read(n)
    w, fast, slow = M.estimate(n)
    d = base_doc()
    footer_note(d, "Video %d reading reference  |  generated from the "
                   "story-led script" % n)
    title_block(d, m["eyebrow"], "Reading Reference", M.title(n))
    kv(d, "Generated", stamp)
    kv(d, "Spoken source", "%s  ·  SHA-256 %s" % (m["file"], m["sha"]))
    kv(d, "Recording copy", M.BLOCKS % n)
    kv(d, "Runtime class", M.mode(n))
    kv(d, "Estimated speech", "%s to %s at 130 to 145 words per minute, from "
                              "%d spoken words" % (fast, slow, w))
    caption(d, "Arithmetic on the script, not a runtime and not a target. "
               "The actual length is observed at Temidayo's natural pace.")
    callout(d, "The gold labels are production aids. They are never spoken. "
               "Record from the thought-block copy, not from this document.")
    for label, ps in M.sections(n):
        section_label(d, label)
        for p in ps:
            block(d, p)
    notspoken(d, "END OF SPOKEN SCRIPT")
    d.save(path)
    return path
