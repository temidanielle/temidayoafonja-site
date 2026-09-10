# -*- coding: utf-8 -*-
"""Build every V14 to V21 editorial development deliverable.

Rebuildable from two read-only sources: the locked September 9 roadmap and the
uploaded refinement document. Run:  python3 buildv1421.py
"""
import os, sys, zipfile, hashlib, datetime, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import baseline, addendum, briefsdoc, changelog, briefs

ADDENDUM = "Videos_14-21_Roadmap_Addendum.docx"
BRIEFSDOC = "Videos_14-21_Development_Briefs.docx"
CHANGELOG = "CHANGE_LOG.md"
PATCH = "ROADMAP_TRACKER_PATCH.md"
ZIPNAME = "Videos_14-21_Editorial_Development.zip"

# Fixed entry timestamp so the archive is byte-stable across rebuilds.
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
    # The archive's own checksum lives beside it, never inside it.
    with open(zpath + ".sha256", "w") as f:
        f.write("%s  %s\n" % (sha256(zpath), ZIPNAME))
    return zpath


def verify_labels():
    """Every brief title must match its source character for character.

    The eight slot labels come from the refinement's own proposal table, and
    the reserved brief's title from its approved working angle. Checking it
    here means a hand-typed apostrophe or a dropped word cannot reach the
    documents unnoticed.
    """
    rf = baseline.refinement_slots()
    bad = []
    for b in briefs.BRIEFS:
        if b["num"].startswith("V"):
            n = int(b["num"][1:])
            if b["label"] != rf[n][0]:
                bad.append((b["num"], b["label"], rf[n][0]))
        elif not baseline.refinement_says(b["label"]):
            bad.append((b["num"], b["label"], "not found in refinement"))
    if bad:
        for x in bad:
            print("  LABEL MISMATCH %s\n    got %r\n    src %r" % x)
        raise SystemExit("brief labels do not match their sources")
    print("brief labels matched to source: %d of %d"
          % (len(briefs.BRIEFS), len(briefs.BRIEFS)))


def main():
    s = stamp()
    print("stamp:", s)
    print("roadmap checksum matched:", baseline.verify_roadmap())
    verify_labels()

    addendum.build(os.path.join(OUT, ADDENDUM), s)
    briefsdoc.build(os.path.join(OUT, BRIEFSDOC), s)
    with open(os.path.join(OUT, CHANGELOG), "w") as f:
        f.write(changelog.change_log(s))
    with open(os.path.join(OUT, PATCH), "w") as f:
        f.write(changelog.patch(s))

    files = [ADDENDUM, BRIEFSDOC, CHANGELOG, PATCH]
    files += [os.path.join("build", n) for n in sorted(os.listdir(HERE))
              if n.endswith(".py")]
    z = make_zip(files)

    print()
    for rel in files:
        p = os.path.join(OUT, rel)
        print("  %-46s %7d bytes" % (rel, os.path.getsize(p)))
    print()
    print("  %-46s %7d bytes  %d entries" % (
        ZIPNAME, os.path.getsize(z), len(files)))
    print("  sha256 %s" % sha256(z))


if __name__ == "__main__":
    main()
