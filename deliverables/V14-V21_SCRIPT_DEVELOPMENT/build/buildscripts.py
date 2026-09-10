# -*- coding: utf-8 -*-
"""Build every V14 to V21 script-development deliverable.

  python3 buildscripts.py
"""
import os, sys, zipfile, hashlib, datetime, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import s15_16, s17_18, s19_21
import masterdoc, scriptcopy, v14doc, reviewdoc, qa1421

VIDEOS = [s15_16.V15, s15_16.V16, s17_18.V17, s17_18.V18,
          s19_21.V19, s19_21.V20, s19_21.V21]

ZIPNAME = "Videos_14-21_SCRIPT_DEVELOPMENT_REVIEW.zip"
ZIP_DT = (2026, 9, 10, 0, 0, 0)


def stamp():
    try:
        import zoneinfo
        now = datetime.datetime.now(zoneinfo.ZoneInfo("America/Chicago"))
    except Exception:
        out = subprocess.check_output(
            ["env", "TZ=America/Chicago", "date", "+%Y-%m-%d %H:%M:%S %z"])
        now = datetime.datetime.strptime(out.decode().strip(),
                                         "%Y-%m-%d %H:%M:%S %z")
    off = now.strftime("%z")
    return "%s | %d:%02d %s CT (America/Chicago, UTC%s:%s)" % (
        now.strftime("%A, %B %d, %Y"),
        (now.hour % 12) or 12, now.minute, now.strftime("%p"),
        off[:3], off[3:])


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for c in iter(lambda: f.read(1 << 16), b""):
            h.update(c)
    return h.hexdigest()


def make_zip(files):
    zpath = os.path.join(OUT, ZIPNAME)
    if os.path.exists(zpath):
        os.remove(zpath)
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED,
                         compresslevel=6) as z:
        for rel in sorted(files):
            info = zipfile.ZipInfo(rel, date_time=ZIP_DT)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            with open(os.path.join(OUT, rel), "rb") as f:
                z.writestr(info, f.read())
    # The archive's checksum lives beside it, never inside it.
    with open(zpath + ".sha256", "w") as f:
        f.write("%s  %s\n" % (sha256(zpath), ZIPNAME))
    return zpath


def main():
    s = stamp()
    print("stamp:", s)

    made = []

    # A. Video 14 research design package. No script, by design.
    made.append(v14doc.build_design(
        os.path.join(OUT, "V14_Research_Design.docx"), s))
    made += v14doc.build_csvs(OUT)
    made.append(v14doc.build_status(
        os.path.join(OUT, "V14_Research_Status.txt"), s))

    # B and C. Recording masters and the recording copies.
    for v in VIDEOS:
        made.append(masterdoc.build(
            v, os.path.join(OUT, "Video_%d_Recording_Master_DRAFT.docx"
                            % v["num"]), s))
        made.append(scriptcopy.build(
            v, os.path.join(OUT, "Video_%d_Script_Only_Recording_Copy.docx"
                            % v["num"])))

    # D. The review summary carries the QA table, so QA runs first and its
    # real results go into the document rather than a claim about them.
    summary = os.path.join(OUT, "V14-V21_Editorial_Review_Summary.docx")

    # Three checks read the summary, and the summary reports the checks. Build
    # it once so those three have something to read, run QA against the
    # complete set, then rebuild the summary with those results. The rebuild
    # touches only the QA table, which none of the three reads, so the second
    # pass is stable. The third pass below proves it.
    rows, passed = qa1421.run()
    reviewdoc.build(summary, s, VIDEOS, rows, passed)
    rows, passed = qa1421.run()
    reviewdoc.build(summary, s, VIDEOS, rows, passed)
    rows2, passed2 = qa1421.run()
    if [(n, ok) for n, ok, _ in rows] != [(n, ok) for n, ok, _ in rows2]:
        raise SystemExit("QA results moved on rebuild; the summary and the "
                         "checks are not at a fixed point")
    made.append(summary)

    for name, ok, detail in rows:
        if not ok:
            print("  QA FAIL: %s" % name)
            for d_ in detail[:4]:
                print("           %s" % d_)
    print("QA: %d of %d checks passed" % (passed, len(rows)))

    # E. The combined archive.
    rels = sorted(os.path.relpath(p, OUT) for p in made)
    rels += [os.path.join("build", n) for n in sorted(os.listdir(HERE))
             if n.endswith(".py")]
    z = make_zip(rels)

    print()
    for rel in rels:
        print("  %-52s %7d bytes"
              % (rel, os.path.getsize(os.path.join(OUT, rel))))
    print()
    print("  %-52s %7d bytes  %d entries"
          % (ZIPNAME, os.path.getsize(z), len(rels)))
    print("  sha256 %s" % sha256(z))
    return 0 if passed == len(rows) else 1


if __name__ == "__main__":
    sys.exit(main())
