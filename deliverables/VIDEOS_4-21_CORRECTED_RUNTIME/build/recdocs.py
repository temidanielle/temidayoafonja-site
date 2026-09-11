# -*- coding: utf-8 -*-
"""01_Recording_Master and 02_Recording documents."""
import os, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import masters421 as M
from docs421f import (base_doc, para, title_block, rule, h, kv, callout,
                       table, bullets, sub, field, page_break, footer_note,
                       block, section_label, notspoken, numbered,
                       NAVY, GOLD, DIM, RED)


def copy_master(n, outdir):
    """The spoken source of truth, copied byte for byte. Never written to.

    For V6, V7 and V8 that is the restored derivative. The supplied
    September 11 master is copied in beside it, unchanged, so the package
    carries the file it superseded rather than pretending it never existed.
    """
    dst = os.path.join(outdir, M.filename(n))
    shutil.copy2(M.path(n), dst)
    if M.sha256(dst) != M.verify(n):
        raise SystemExit("V%d master copy does not match the source" % n)
    if n in M.RESTORED:
        sup = os.path.join(outdir, "SUPERSEDED_" + M.FILES[n])
        shutil.copy2(M.supplied_path(n), sup)
        if M.sha256(sup) != M.read(n)["supplied_sha"]:
            raise SystemExit("V%d supplied master copy does not match" % n)
    return dst


def reading_reference(n, out_path, stamp):
    """A reading copy for the desk, generated from the locked master.

    Section labels and any bracketed direction are marked as production
    instructions so they are never read aloud.
    """
    m = M.read(n)
    w, fast, slow = M.estimate(n)
    d = base_doc()
    footer_note(d, "Video %d approved recording master reference  |  generated "
                   "from the locked master  |  do not read the labels aloud"
                   % n)
    title_block(d, "Capability Formation  |  Video %d" % n, M.title(n),
                "Approved recording master reference")
    kv(d, "Generated", stamp)
    kv(d, "From", "%s  ·  SHA-256 %s" % (m["file"], m["sha"]))
    kv(d, "Status", "LOCKED SPOKEN SOURCE. This reference is generated from "
                    "the master and adds nothing to it.")
    kv(d, "Thumbnail", M.thumbnail(n))
    kv(d, "Framework", M.framework(n) or "None stated by the master.")
    kv(d, "Primary CTA", M.cta(n))
    kv(d, "Resource", M.resource(n) or
       "None. This master names no resource route and none is added.")
    kv(d, "Watch Next", M.watch_next(n))
    kv(d, "Speech-only estimate", "%s to %s from %s spoken words at 130 to "
       "145 words per minute" % (fast, slow, "{:,}".format(w)))
    callout(d, "The gold labels are section names from the master. They are "
               "production instructions and are never spoken. Everything in "
               "black is the approved spoken text, unchanged.")
    para(d, "The runtime figure is arithmetic on the script. It excludes "
            "pauses and visual holds, and it is not a timed read.",
         size=9.5, color=DIM)
    rule(d)
    for name, blocks in m["sections"]:
        if name:
            section_label(d, name)
        for b in blocks:
            block(d, b)
    rule(d)
    para(d, "END OF SPOKEN SCRIPT. Nothing is recorded after the final line "
            "above.", size=10, bold=True, color=RED)
    d.save(out_path)
    return out_path


def script_only(n, out_path):
    """The MacBook recording copy. Spoken script and nothing else."""
    m = M.read(n)
    d = base_doc()
    footer_note(d, "Video %d recording copy  |  spoken script only" % n)
    para(d, "CAPABILITY FORMATION  |  VIDEO %d" % n, size=9, bold=True,
         color=GOLD, after=4)
    para(d, M.title(n), size=18, bold=True, color=NAVY, after=6)
    rule(d, after=10)
    para(d, "Read one block silently. Look toward the lens. Deliver it "
            "naturally. Stop. Reset posture and hands, then take the next "
            "block. The small gold labels are for finding your place and are "
            "not spoken.", size=10, color=DIM, after=4)
    rule(d, after=12)
    for name, blocks in m["sections"]:
        if name:
            section_label(d, name)
        for b in blocks:
            block(d, b, size=13.5)
    d.save(out_path)
    return out_path
