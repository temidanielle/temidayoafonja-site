# -*- coding: utf-8 -*-
"""Rebuild SHA256SUMS.txt and the master ZIP from the files now on disk.

Used after restoring byte-identical files so that only the two documents whose
CONTENT actually changed carry new hashes. Same explicit 13-file allowlist as
build.py.
"""
import os, hashlib, zipfile

ROOT = "Video_7_HIT_FINAL"
ZIPNAME = "Video_7_HIT_FINAL_Recording_and_Shorts_Package.zip"
MANIFEST = [
 "LONG_FORM/Video7TeleprompterScriptwithslidemarkers_HIT_v2.0.docx",
 "LONG_FORM/Video7TeleprompterScriptwithslidemarkers_HIT_v2.0.txt",
 "LONG_FORM/Video7ReadingScriptnomarkers_HIT_v2.0.docx",
 "LONG_FORM/Video7ReadingScriptnomarkers_HIT_v2.0.txt",
 "LONG_FORM/Video_7_EDITOR_ONLY_HIT_Brief_v2.0.docx",
 "LONG_FORM/Video_7_Publishing_Package_HIT_v2.0.docx",
 "SHORTS/Video_7_Short_1_Work_Became_Invisible.docx",
 "SHORTS/Video_7_Short_2_Built_From_Scratch_Not_Alone.docx",
 "SHORTS/Video_7_Short_3_Building_While_Operating.docx",
 "SHORTS/Video_7_Short_4_Reconstruct_The_Before.docx",
 "SHORTS/Video_7_Shorts_EDITOR_ONLY_HIT_Brief.docx",
 "README_FINAL.txt",
]
SUMS = "SHA256SUMS.txt"

def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for b in iter(lambda: fh.read(1 << 20), b""): h.update(b)
    return h.hexdigest()

for m in MANIFEST:
    assert os.path.isfile(os.path.join(ROOT, m)), "missing: " + m
on_disk = set()
for dp, dn, fn in os.walk(ROOT):
    dn[:] = [x for x in dn if x != "__pycache__"]
    for f in fn:
        if f.endswith(".pyc"): continue
        on_disk.add(os.path.relpath(os.path.join(dp, f), ROOT).replace(os.sep, "/"))
unexpected = sorted(on_disk - set(MANIFEST) - {SUMS})
assert not unexpected, "unexpected files: %r" % unexpected

L = ["# VIDEO 7 - H.I.T. FINAL RECORDING PACKAGE",
     "# SHA-256 of the 12 user-facing files in this package.",
     "# SHA256SUMS.txt cannot hash itself. The master ZIP cannot contain its own",
     "# checksum either; it is published in the sibling file",
     "# " + ZIPNAME + ".sha256",
     "# Video_7_YouTube_Description_HIT.docx sits outside this package; its",
     "# SHA-256 is reported in the delivery summary.", ""]
for m in MANIFEST:
    L.append("%s  %s" % (sha256(os.path.join(ROOT, m)), m))
open(os.path.join(ROOT, SUMS), "w").write("\n".join(L) + "\n")

if os.path.exists(ZIPNAME): os.remove(ZIPNAME)
with zipfile.ZipFile(ZIPNAME, "w", zipfile.ZIP_DEFLATED) as z:
    for m in MANIFEST + [SUMS]:
        z.write(os.path.join(ROOT, m), "Video_7_HIT_FINAL/" + m)
zsha = sha256(ZIPNAME)
open(ZIPNAME + ".sha256", "w").write("%s  %s\n" % (zsha, ZIPNAME))
print("ZIP sha256:", zsha)
print("description-only doc sha256:", sha256("Video_7_YouTube_Description_HIT.docx"))
