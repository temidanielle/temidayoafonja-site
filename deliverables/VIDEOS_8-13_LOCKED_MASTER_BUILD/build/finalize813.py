# -*- coding: utf-8 -*-
"""Regenerate the batch-level documents and the combined archive only.

The six per-video packages are NOT rebuilt. Their contents did not change, so
their ZIPs and checksums must not move. Only the three root documents and the
combined archive are regenerated, and the combined checksum is computed after
the archive is final.
"""
import os, sys, hashlib, zipfile
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.insert(0, DELIV + "riverside-build")
sys.path.insert(0, DELIV + "new-videos-4-5/build")
sys.path.insert(0, HERE)
import masters813 as M, build813 as B, summary813 as S

EXTRAS = ["V8-V13_BATCH_MANIFEST.md", "V8-V13_DELIVERY_SUMMARY.docx",
          "V8-V13_ROADMAP_TRACKER_PATCH.md"]
COMBINED = os.path.join(ROOT, "Videos_8-13_Production_Packages.zip")


def main():
    before = {}
    for n in M.VIDEOS:
        z = os.path.join(ROOT, "V%d_Production_Package.zip" % n)
        before[n] = hashlib.sha256(open(z, "rb").read()).hexdigest()

    hashes = {n: open(os.path.join(
        ROOT, "V%d_Production_Package.zip.sha256" % n)).read().split()[0]
        for n in M.VIDEOS}

    open(os.path.join(ROOT, EXTRAS[0]), "w").write(B.batch_manifest(hashes))
    S.build_doc()
    open(os.path.join(ROOT, EXTRAS[2]), "w").write(S.patch_text())

    with zipfile.ZipFile(COMBINED, "w", zipfile.ZIP_DEFLATED,
                         compresslevel=6) as z:
        for f in EXTRAS:
            B._add(z, f, open(os.path.join(ROOT, f), "rb").read())
        for n in M.VIDEOS:
            root = B.DIRS[n]
            base = os.path.basename(root)
            for dp, _, files in os.walk(root):
                for f in sorted(files):
                    full = os.path.join(dp, f)
                    B._add(z, os.path.join(base, os.path.relpath(full, root)),
                           open(full, "rb").read())

    # computed only now that the archive is complete
    ch = hashlib.sha256(open(COMBINED, "rb").read()).hexdigest()
    open(COMBINED + ".sha256", "w").write(
        "%s  Videos_8-13_Production_Packages.zip\n" % ch)

    print("per-video packages, unchanged as required:")
    moved = 0
    for n in M.VIDEOS:
        z = os.path.join(ROOT, "V%d_Production_Package.zip" % n)
        now = hashlib.sha256(open(z, "rb").read()).hexdigest()
        ok = now == before[n] == hashes[n]
        moved += not ok
        print("  V%-3d %s  %s" % (n, "unchanged" if ok else "MOVED", now))
    print()
    print("combined archive rebuilt:")
    print("  entries  %d" % len(zipfile.ZipFile(COMBINED).namelist()))
    print("  bytes    %d" % os.path.getsize(COMBINED))
    print("  testzip  %s" % zipfile.ZipFile(COMBINED).testzip())
    print("  sha256   %s" % ch)
    print()
    print("per-video ZIPs that moved:", moved)


if __name__ == "__main__":
    main()
