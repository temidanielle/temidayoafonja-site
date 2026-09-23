# -*- coding: utf-8 -*-
"""Build the V4 to V14 sticky-realization reconciliation document."""
import os, sys, zipfile, hashlib, re
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.append("/home/user/temidayoafonja-site/deliverables/VIDEOS_22-23/build")
from docs23 import (base_doc, title_block, h, kv, para, callout, sub, caption,
                    table, bullets, footer_note, page_break)
import sa_data as S

NAME = "V4-V14_STICKY_REALIZATION_RECONCILIATION.docx"
EYEBROW = "capability formation | sticky realization pass"

def build(path):
    d = base_doc()
    title_block(d, EYEBROW, "V4 to V14 sticky realization",
                "Editorial reconciliation. No production assets were rebuilt.")
    kv(d, "Generated", S.STAMP)
    kv(d, "Videos read", "Eleven, each from its newest approved spoken master")
    kv(d, "Revised masters produced", "None")
    callout(d, S.VERDICT)

    h(d, "The required table")
    caption(d, "One row per video. Every row was written after reading that "
               "video's newest approved master end to end, not from its title "
               "or its package summary.")
    rows = []
    for n in sorted(S.ROWS):
        t, thumb, thinks, real, line, act, earns, change = S.ROWS[n]
        rows.append(["V%d" % n, t, thumb, thinks, real, line, act, earns, change])
    table(d, ["#", "Current title", "Thumbnail", "Viewer already thinks",
              "THAT'S IT realization", "7-day memory line", "Observable action",
              "Earns it?", "Minimal change needed"],
          rows, widths=[0.3, 0.85, 0.6, 0.95, 1.15, 0.85, 1.0, 0.35, 0.65])

    page_break(d)
    h(d, "Why nothing was changed")
    para(d, S.WHY_NO_CHANGE)
    caption(d, "In nine of the eleven the memory line is already spoken twice: "
               "once where it lands and again at the story-loop payoff. That "
               "is the structure this pass was asking for, and it was already "
               "there.")

    h(d, "What the audit did surface")
    para(d, "Three memory lines or constructions are shared across videos. "
            "None of them is a defect in any single video, and in every case "
            "the collision is between a NEW V1 to V3 re-record and a LOCKED "
            "V4 to V14 video, so none can be resolved without a decision.")
    for line, where, what, rec in S.COLLISIONS:
        sub(d, line)
        kv(d, "Shared by", where)
        para(d, what)
        para(d, rec)

    h(d, "The one optional change, if you want it")
    o = S.OPTIONAL
    kv(d, "Video", o["video"])
    kv(d, "Status", o["status"])
    kv(d, "Where", o["where"])
    kv(d, "Sentence to add", o["add"])
    para(d, o["why"])
    kv(d, "Cost", o["cost"])
    callout(d, "This is offered, not applied. V9 passes the four-item test as "
               "it stands, and the follow-up says to preserve a script that "
               "already delivers all four.")

    page_break(d)
    h(d, "What was read")
    table(d, ["#", "Source", "Checksum", "Spoken words"],
          [["V%d" % n, S.SOURCES[n][0], S.SOURCES[n][1],
            "{:,}".format(S.SOURCES[n][2])] for n in sorted(S.SOURCES)],
          widths=[0.4, 3.4, 1.5, 1.4])
    para(d, S.SOURCE_NOTE)

    h(d, "Not done, and why")
    for name, why in S.NOT_DONE:
        sub(d, name)
        para(d, why)
    footer_note(d, "Eleven videos read. Eleven LOCKED AS-IS. One optional "
                   "one-sentence change specified and not applied.")
    d.save(path)

def normalize(path):
    with zipfile.ZipFile(path) as z:
        items = [(i, z.read(i.filename)) for i in z.infolist()]
    out = []
    for info, data in items:
        if info.filename == "docProps/core.xml":
            t = data.decode("utf-8")
            t = re.sub(r"(<dcterms:(?:created|modified)[^>]*>)[^<]*(</dcterms:)",
                       r"\g<1>2026-09-23T00:00:00Z\g<2>", t)
            data = t.encode("utf-8")
        out.append((info.filename, info.compress_type, data))
    tmp = path + ".tmp"
    with zipfile.ZipFile(tmp, "w") as z:
        for nm, ct, dt in out:
            zi = zipfile.ZipInfo(nm, date_time=(2026, 9, 23, 0, 0, 0))
            zi.compress_type = ct
            zi.external_attr = 0o644 << 16
            z.writestr(zi, dt)
    os.replace(tmp, path)

if __name__ == "__main__":
    p = os.path.join(OUT, NAME)
    build(p)
    normalize(p)
    print(p)
    print(hashlib.sha256(open(p, "rb").read()).hexdigest())

def verify():
    """Every memory line in the table must be present verbatim in that video's
    own master. This caught two transcription slips in the first draft of the
    table: V7's payoff says "the bigger role", not "a bigger role", and V11's
    line sits lowercase inside a longer sentence."""
    import io
    SRC = "/tmp/claude-0/-home-user-temidayoafonja-site/f121668d-e262-5eb8-9b22-0eaa1006a361/scratchpad/v414/"
    bad = []
    for n in sorted(S.ROWS):
        try:
            body = io.open(SRC + "V%d.txt" % n, encoding="utf-8").read()
        except IOError:
            return ["master extract not available to re-verify"]
        body = " ".join(l.split("| ", 1)[1] for l in body.splitlines()
                        if "| " in l).lower()
        core = S.ROWS[n][4].rstrip(".?").split(". ")[-1].lower()
        if core not in body:
            bad.append("V%d memory line not in its master" % n)
    return bad
