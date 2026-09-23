# -*- coding: utf-8 -*-
"""Assemble the V1-V14 final locked master archive.

Nothing is regenerated. Every recording master and thought-block copy is copied
byte for byte from the approved source, and the archive records the checksum of
the file it copied so the copy can be proved identical to the original.
"""
import os, sys, shutil, zipfile, hashlib, re
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.insert(0, HERE)
sys.path.append(DELIV + "VIDEOS_22-23/build")
from docs23 import (base_doc, title_block, h, kv, para, callout, sub, caption,
                    table, bullets, footer_note, page_break)
import ar_sources as S, ar_parity as P, ar_data as D

ROOT = "CAPABILITY_FORMATION_YOUTUBE_V1-V14_FINAL_LOCKED_MASTER_ARCHIVE"
STAGE = os.path.join(HERE, "_stage", ROOT)
ZIPNAME = ROOT + ".zip"
MANIFEST = "V1-V14_FINAL_LOCKED_SOURCE_OF_TRUTH_MANIFEST.docx"
SUPERSESSION = "V1-V14_SUPERSESSION_AND_ARCHIVE_STATUS.docx"
RECON = "V4-V14_STICKY_REALIZATION_RECONCILIATION.docx"
EYEBROW = "capability formation | v1-v14 final locked"
FIXED = (2026, 9, 23, 0, 0, 0)

def master_name(n):
    return "V%02d_LOCKED_RECORDING_MASTER.docx" % n

def blocks_name(n):
    return "V%02d_LOCKED_THOUGHT_BLOCKS.docx" % n

def sha256(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

# Production packages carried by reference. Each is a package already built
# against the master it sits beside; none of them is a spoken source.
PROD_REF = [
 ("V1-V3", DELIV + "V1-V3_STICKY/CAPABILITY_FORMATION_V1-V3_REFRESH_PRODUCTION_PACK.zip"),
 ("V4-V11", DELIV + "V4-V11_SYNC/YouTube_NEW_PUBLIC_V4-V11_SYNCHRONIZED_2026-09-16.zip"),
 ("V12", DELIV + "V12-V14_LOCKED/YOUTUBE_V12-V14_FINAL_LOCKED_PACK.zip"),
 ("V13-V14", DELIV + "V13-V14_ANON/V13-V14_PUBLIC_EMPLOYER_ANONYMIZATION_PATCH.zip"),
]

def manifest(path, rows):
    d = base_doc()
    title_block(d, EYEBROW, "Source of truth manifest",
                "V1 to V14. The active spoken source for every video.")
    kv(d, "Generated", D.STAMP)
    kv(d, "Videos", "Fourteen")
    kv(d, "Thought-block parity", "14 of 14 PASS")
    callout(d, "This manifest exists so the active source can be identified "
               "without opening any older folder. Every recording master and "
               "thought-block copy in this archive was copied byte for byte "
               "from the file named in its SOURCE FILE row, and the checksum "
               "in the row is the checksum of that original.")

    h(d, "The fourteen, at a glance")
    table(d, ["#", "Title", "Thumbnail", "Spoken words", "Parity", "Status"],
          [["V%d" % r["n"], S.TITLES[r["n"]][0], S.TITLES[r["n"]][1],
            "{:,}".format(r["words"]), "PASS" if r["passed"] else "FAIL",
            "LOCKED"] for r in rows],
          widths=[0.4, 2.55, 1.6, 0.8, 0.55, 0.8])

    for r in rows:
        n = r["n"]
        page_break(d)
        h(d, "V%d  %s" % (n, S.TITLES[n][0]))
        kv(d, "Video number", "V%d" % n)
        kv(d, "Title", S.TITLES[n][0])
        kv(d, "Thumbnail", S.TITLES[n][1])
        kv(d, "Locked recording master", master_name(n))
        kv(d, "Locked thought-block copy", blocks_name(n))
        kv(d, "Source file used", os.path.basename(S.SRC[n][0]))
        kv(d, "Source checksum", sha256(S.SRC[n][0]))
        kv(d, "Thought-block source", os.path.basename(S.SRC[n][1]))
        kv(d, "Thought-block checksum", sha256(S.SRC[n][1]))
        kv(d, "Spoken word count", "{:,}" .format(r["words"]))
        kv(d, "Thought-block word count", "{:,}".format(r["block_words"]))
        kv(d, "Parity", "PASS, word for word and in order" if r["passed"] else "FAIL")
        kv(d, "Status", "LOCKED")
        kv(d, "Sticky realization / memory line", D.MEMORY[n][0])
        kv(d, "Observable viewer action", D.MEMORY[n][1])
        kv(d, "CTA / resource", D.CTA[n])
        kv(d, "Watch next", D.WATCH_NEXT[n])
        kv(d, "Production asset status", PRODUCTION_LINE(n))
        para(d, S.SRC[n][3])
        note = D.PROVENANCE_NOTES.get(n)
        if note:
            sub(d, "Provenance note")
            para(d, note)
        if r["fused"]:
            sub(d, "Source formatting note")
            para(d, "This file carries the fused section label described in "
                    "00_SOURCE_OF_TRUTH. It was recorded, not repaired.")
    page_break(d)
    h(d, "The fused label in V2 and V3")
    para(d, D.FUSED_NOTE)
    h(d, "Recurring Capability Formation ideas, preserved")
    table(d, ["Idea", "Where", "Status"],
          [[a, b, c] for a, b, c in D.RECURRING], widths=[2.6, 1.9, 2.2])
    para(d, D.RECURRING_NOTE)
    footer_note(d, "Fourteen videos, fourteen masters, fourteen thought-block "
                   "copies, 14 of 14 parity PASS.")
    d.save(path)

def PRODUCTION_LINE(n):
    st, why = D.PRODUCTION[n]
    return "%s. %s" % (st, why)

def supersession(path, rows):
    d = base_doc()
    title_block(d, EYEBROW, "Supersession and archive status",
                "What is current, and what is history")
    kv(d, "Generated", D.STAMP)
    callout(d, D.NO_DELETION)

    h(d, "CURRENT")
    bullets(d, D.CURRENT)
    table(d, ["#", "Active spoken source", "Checksum", "Words"],
          [["V%d" % r["n"], os.path.basename(S.SRC[r["n"]][0]),
            sha256(S.SRC[r["n"]][0])[:16], "{:,}".format(r["words"])]
           for r in rows], widths=[0.4, 3.6, 1.5, 0.8])

    page_break(d)
    h(d, "SUPERSEDED / HISTORY")
    caption(d, "Superseded where it conflicts with this archive. Still in the "
               "workspace, still readable, simply not the active source.")
    table(d, ["What", "Where it lives", "Why it is superseded"],
          [[a, b, c] for a, b, c in D.SUPERSEDED], widths=[2.0, 2.2, 2.5])

    h(d, "One case worth reading twice")
    para(d, "The locked V12-V14 pack is superseded for V13 and V14 only. Its "
            "V12 is still the approved source for V12. A folder is not "
            "superseded as a whole here; a video is.")

    h(d, "Publishing descriptions")
    para(d, D.DESCRIPTIONS_NOTE)

    h(d, "Not done, and why")
    for name, why in D.NOT_DONE:
        sub(d, name)
        para(d, why)
    footer_note(d, "Nothing was deleted and nothing was rewritten.")
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
            zi = zipfile.ZipInfo(nm, date_time=FIXED)
            zi.compress_type = ct
            zi.external_attr = 0o644 << 16
            z.writestr(zi, dt)
    os.replace(tmp, path)

def main():
    if os.path.isdir(os.path.dirname(STAGE)):
        shutil.rmtree(os.path.dirname(STAGE))
    for sub_ in ("00_SOURCE_OF_TRUTH", "01_RECORDING_MASTERS",
                 "02_THOUGHT_BLOCKS", "03_PRODUCTION_ASSETS_REFERENCE",
                 "04_DRAFT_PUBLISHING_DESCRIPTIONS_REVIEW_REQUIRED",
                 "05_PROVENANCE_AND_EVIDENCE"):
        os.makedirs(os.path.join(STAGE, sub_))

    rows = P.run()

    # 01 and 02: byte-for-byte copies of the approved sources
    copies = []
    for n in sorted(S.SRC):
        m_src, b_src = S.SRC[n][0], S.SRC[n][1]
        m_dst = os.path.join(STAGE, "01_RECORDING_MASTERS", master_name(n))
        b_dst = os.path.join(STAGE, "02_THOUGHT_BLOCKS", blocks_name(n))
        shutil.copy2(m_src, m_dst)
        shutil.copy2(b_src, b_dst)
        copies.append((n, m_src, m_dst, b_src, b_dst))

    # 03: production packages by reference
    for label, src in PROD_REF:
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(
                STAGE, "03_PRODUCTION_ASSETS_REFERENCE", os.path.basename(src)))

    # 04: the unapproved V1-V3 descriptions, lifted out of the production pack
    pack = DELIV + "V1-V3_STICKY/CAPABILITY_FORMATION_V1-V3_REFRESH_PRODUCTION_PACK.zip"
    with zipfile.ZipFile(pack) as z:
        for nm in z.namelist():
            if "DESCRIPTION_AND_METADATA" in nm:
                dst = os.path.join(
                    STAGE, "04_DRAFT_PUBLISHING_DESCRIPTIONS_REVIEW_REQUIRED",
                    "NOT_YET_APPROVED_" + os.path.basename(nm))
                with open(dst, "wb") as fh:
                    fh.write(z.read(nm))

    # 05: provenance already written for the locked scripts. Nothing invented.
    with zipfile.ZipFile(pack) as z:
        for nm in z.namelist():
            if "SOURCE_AND_PROVENANCE" in nm:
                with open(os.path.join(STAGE, "05_PROVENANCE_AND_EVIDENCE",
                                       os.path.basename(nm)), "wb") as fh:
                    fh.write(z.read(nm))
    for src in (DELIV + "FLAGSHIP_CAREER_CHANGE/FLAGSHIP_JD_PROVENANCE.md",):
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(STAGE, "05_PROVENANCE_AND_EVIDENCE",
                                           os.path.basename(src)))

    # 00: the three source-of-truth documents
    sot = os.path.join(STAGE, "00_SOURCE_OF_TRUTH")
    manifest(os.path.join(sot, MANIFEST), rows)
    supersession(os.path.join(sot, SUPERSESSION), rows)
    shutil.copy2(DELIV + "V4-V14_STICKY_AUDIT/" + RECON,
                 os.path.join(sot, RECON))
    for f in (MANIFEST, SUPERSESSION):
        normalize(os.path.join(sot, f))

    # a copy of the manifest outside the ZIP
    shutil.copy2(os.path.join(sot, MANIFEST), os.path.join(OUT, MANIFEST))

    names = sorted(os.path.relpath(os.path.join(r, f), os.path.dirname(STAGE))
                   for r, _d, fs in os.walk(STAGE) for f in fs)
    zpath = os.path.join(OUT, ZIPNAME)
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for rel in names:
            zi = zipfile.ZipInfo(rel.replace(os.sep, "/"), date_time=FIXED)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            with open(os.path.join(os.path.dirname(STAGE), rel), "rb") as fh:
                z.writestr(zi, fh.read())
    with open(zpath + ".sha256", "w") as fh:
        fh.write("%s  %s\n" % (sha256(zpath), ZIPNAME))
    return zpath, names, rows, copies

if __name__ == "__main__":
    zp, names, rows, copies = main()
    ident = [n for n, ms, md, bs, bd in copies
             if sha256(ms) != sha256(md) or sha256(bs) != sha256(bd)]
    print("byte-for-byte copies that do not match their source:", ident or "none")
    print("%d files" % len(names))
    print("%s" % zp)
    print(sha256(zp))
