# -*- coding: utf-8 -*-
"""Build the eight Videos 14 to 21 final production packages.

  python3 build1421.py
"""
import os, sys, json, shutil, zipfile, hashlib, datetime, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import masters1421 as M
import research14, recdocs, prodocs, riverside1421, shortsdocs
import publish1421, exercise1421, qafinal, shootall
from frames1421 import SETS
from shorts1421 import SHORTS
from docs1421f import mono, hr, head

SUB = ["01_Recording_Master", "02_Recording", "03_Visuals", "04_Riverside",
       "05_Shorts", "06_Publishing", "07_Viewer_Exercise",
       "08_Sources_and_QA"]

ZIP_DT = (2026, 9, 10, 0, 0, 0)


def stamp():
    try:
        import zoneinfo
        now = datetime.datetime.now(zoneinfo.ZoneInfo("America/Chicago"))
    except Exception:
        o = subprocess.check_output(["env", "TZ=America/Chicago", "date",
                                     "+%Y-%m-%d %H:%M:%S %z"])
        now = datetime.datetime.strptime(o.decode().strip(),
                                         "%Y-%m-%d %H:%M:%S %z")
    off = now.strftime("%z")
    return "%s | %d:%02d %s CT (America/Chicago, UTC%s:%s)" % (
        now.strftime("%A, %B %d, %Y"), (now.hour % 12) or 12, now.minute,
        now.strftime("%p"), off[:3], off[3:])


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 16), b""):
            h.update(c)
    return h.hexdigest()


def pkg_dir(n):
    return os.path.join(OUT, "VIDEO_%d_FINAL_PRODUCTION_PACKAGE" % n)


def zip_dir(src, zpath):
    if os.path.exists(zpath):
        os.remove(zpath)
    files = []
    for root, _, names in os.walk(src):
        for nm in names:
            p = os.path.join(root, nm)
            files.append((os.path.relpath(p, os.path.dirname(src)), p))
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED,
                         compresslevel=6) as z:
        for rel, p in sorted(files):
            info = zipfile.ZipInfo(rel, date_time=ZIP_DT)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            with open(p, "rb") as f:
                z.writestr(info, f.read())
    with open(zpath + ".sha256", "w") as f:
        f.write("%s  %s\n" % (sha256(zpath), os.path.basename(zpath)))
    return zpath, len(files)


def source_manifest(n, pkg, stamp_):
    m = M.read(n)
    data = {
      "video": n,
      "title": M.title(n),
      "generated": stamp_,
      "spoken_source_of_truth": {
        "file": m["file"], "sha256": m["sha"],
        "note": "Copied unchanged into 01_Recording_Master. Never written "
                "to. This file overrides every earlier script."},
      "superseded": {
        "package": "Videos_14-21_SCRIPT_DEVELOPMENT_REVIEW.zip",
        "sha256": "80d9d54cf5049f77496c4546b624241a744a6cdeee27a6df7555866f0"
                  "c64ea47",
        "status": "SUPERSEDED. Development history only. Its scripts are not "
                  "current speech and are not preserved as alternates."},
      "secondary_context": [
        {"file": "Videos_1421_Roadmap_Addendum.docx",
         "sha256": "3f68bd6cf1c463551fe305b6c6d3ade6e6b030b5e58f5aa4b8f3df73"
                   "1f3a60ea"},
        {"file": "Videos_1421_Development_Briefs.docx",
         "sha256": "16e574b06772648a3cd4b197a37e75ff9061710174f55d8a5f09e61d"
                   "2f17f736"}],
      "packaging": {
        "thumbnail": M.thumbnail(n),
        "framework": M.framework(n),
        "primary_cta": M.cta(n),
        "resource": M.resource(n) or None,
        "watch_next": M.watch_next(n)},
      "script": {
        "sections": len(m["sections"]),
        "thought_blocks": len(M.blocks(n)),
        "spoken_words": M.word_count(n),
        "speech_only_estimate": "%s to %s at 130 to 145 words per minute"
                                % M.estimate(n)[1:],
        "estimate_note": "Arithmetic on the script. Excludes pauses and "
                         "visual holds. Not a timed read and not a runtime."},
      "assets": [{"file": f["key"] + ".png", "status": f["status"],
                  "why": f["why"], "mode": f["mode"],
                  "trigger": f["trigger"].replace("\n", " ")}
                 for f in SETS[n]],
      "shorts": [{"slug": s["slug"], "priority": s["priority"],
                  "title": s["title"], "source": s["source"]}
                 for s in SHORTS[n]],
      "not_verified": [
        "Nothing in this package has been recorded, edited or exported.",
        "Runtime figures are arithmetic, not measured.",
        "No thumbnail artwork exists or is approved.",
        "No chapters, SRT or music attribution exists.",
        "No public link has been checked."],
    }
    if n == 14:
        rows, ok = research14.verify()
        data["research"] = {
          "file": "what-really-transfers-research.md",
          "sha256": M.research_hash(),
          "retained_postings": 28,
          "by_industry": {"healthcare": 10, "financial_services": 10,
                          "technology": 8},
          "collection_date": "2026-09-10",
          "target_was": 30,
          "claims_verified": sum(1 for _, g, _ in rows if g),
          "claims_total": len(rows),
          "all_supported": ok,
          "limits": [
            "A convenience sample of 28 postings. Not representative of any "
            "industry or of the labor market.",
            "Cannot show two roles are interchangeable.",
            "Cannot show that an adjacent-experience candidate would be "
            "hired or that a requirement would be waived.",
            "Every count is a count within these 28 postings.",
            "Several postings were mirrored, older or closed. Not every "
            "source is a currently live employer posting."]}
    p = os.path.join(pkg, "08_Sources_and_QA", "Source_Manifest_V%d.json" % n)
    with open(p, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return p


def qa_report(n, pkg, rows, out_path):
    passed = sum(1 for _, ok, _ in rows if ok)
    L = head("VIDEO %d  |  QA REPORT" % n)
    L += [M.title(n), "",
          "%d package checks completed now. %d passed." % (len(rows), passed),
          "Every check ran against the built package on disk, not against the",
          "build data, so a check cannot pass because of something that was",
          "true only in a source module.", "", hr(), "",
          "PACKAGE CHECKS COMPLETED NOW", ""]
    for name, ok, detail in rows:
        L += ["  [%s] %s" % ("PASS" if ok else "FAIL", name)]
        d = detail if isinstance(detail, str) else "; ".join(map(str, detail))
        L += ["         %s" % d]
    L += ["", hr(), "", "FINAL-EXPORT CHECKS, STILL PENDING", "",
          "  These are NOT complete and are not claimed. A written prompt does",
          "  not prove an effect exists in the finished video.", ""]
    for item in qafinal.FINAL_EXPORT_PENDING:
        L += ["  [ PENDING ] %s" % item]
    L += ["", hr(), "",
          "  Nothing in this list can be checked until the video has been",
          "  recorded, edited and exported.", ""]
    return mono(out_path, L)


def change_log(n, pkg, out_path, stamp_):
    m = M.read(n)
    from collections import Counter
    cnt = Counter(f["status"] for f in SETS[n])
    L = head("VIDEO %d  |  CHANGE LOG" % n)
    L += [M.title(n), "", "Generated: %s" % stamp_, "", hr(), "",
          "SOURCE HIERARCHY CHANGE", "",
          "  The locked final Recording Master is now the definitive spoken",
          "  source of truth for this video:", "",
          "    %s" % m["file"],
          "    SHA-256 %s" % m["sha"], "",
          "  It OVERRIDES the script this workspace drafted earlier in",
          "  Videos_14-21_SCRIPT_DEVELOPMENT_REVIEW.zip. The two script sets",
          "  were not merged. The earlier draft was not used to reword the",
          "  master, and it is not retained as an alternate recording script.",
          "  It is development history.", "", hr(), "",
          "WHAT WAS AUDITED AND REUSED", "",
          "  Every production concept from the earlier package was checked",
          "  against this master and classified:", ""]
    for k in ("REUSE", "REORDER", "COPY UPDATE", "REBUILD", "REMOVE", "NEW"):
        L += ["    %-12s %d" % (k, cnt.get(k, 0))]
    L += ["",
          "  No frame is described as byte-identical reuse. The earlier",
          "  package held written concepts only. No rendered production asset",
          "  existed for any video in this range, so REUSE here means the",
          "  concept survived the final master unchanged, not that a file was",
          "  carried across.", "", hr(), "",
          "WHAT WAS NOT CHANGED", "",
          "  The master was copied byte for byte and never written to.",
          "  No spoken text was tightened, expanded, restructured or",
          "  reworded. The hook, the examples, the qualifications, the CTA,",
          "  the resource, the Watch Next and the final line are the",
          "  master's.",
          "  No statistic, example, employer, person or outcome was added.",
          "  No spoken Subscribe request was added.", "", hr(), ""]
    if n == 14:
        L += ["VIDEO 14 SPECIFICALLY", "",
              "  The research is complete. This video is no longer script",
              "  blocked.",
              "  The retained sample is 28 postings, not 30. 10 healthcare,",
              "  10 financial services, 8 technology, all collected",
              "  September 10, 2026. 30 was the target and was not reached.",
              "  The numerical past-tense title is NOT restored as active",
              "  packaging. The approved question title is used.",
              "  The mixed finding is preserved. The package does not say",
              "  that experience transfers, and it does not say that it does",
              "  not.", "", hr(), ""]
    L += ["WHAT IS NOT SUPPLIED BY INSTRUCTION", "",
          "  Final chapters, an SRT, music attribution, thumbnail artwork and",
          "  any public URL. These come from the finished export and the",
          "  separate artwork approval.", ""]
    return mono(out_path, L)


def evidence_notes(n, pkg, out_path):
    L = head("VIDEO %d  |  FACTUAL AND EVIDENCE NOTES" % n)
    L += [M.title(n), ""]
    tail = [t for t in M.read(n)["tail"]]
    if tail:
        L += ["CARRIED FROM THE MASTER, NOT SPOKEN", ""]
        for t in tail:
            L += ["  %s" % t]
        L += [""]
    L += [hr(), "", "PACKAGE-LEVEL BOUNDARIES", "",
          "  Nothing in this package adds a claim, an outcome or a certainty",
          "  that the master does not carry.",
          "  Constructed examples are labeled on the frame and are said aloud",
          "  as constructed in the master.",
          "  Runtime figures are arithmetic on the script, not measured.",
          "  No employer, colleague, client or outcome is invented anywhere.",
          ""]
    if n == 14:
        rows, ok = research14.verify()
        L += [hr(), "", "VIDEO 14 RESEARCH REFERENCE MAP", "",
              "  Archive: what-really-transfers-research.md",
              "  SHA-256 %s" % M.research_hash(), "",
              "  Every claim in this package was verified against that file",
              "  at build time. %d of %d verified." % (
                  sum(1 for _, g, _ in rows if g), len(rows)), ""]
        for claim, good, miss in rows:
            L += ["  [%s] %s" % ("OK" if good else "MISS", claim)]
        L += ["", "  Employer material. The master's notes permit Humana,",
              "  Wells Fargo, Mass General Brigham and JPMorgan to be named",
              "  on screen only with the preserved source wording. No",
              "  rendered frame in this package names an employer: the",
              "  employer-disagreement frame describes them by type. If the",
              "  editor names one, the source capture must travel with the",
              "  production archive.", "",
              "  Several source postings were mirrored, older or closed. Do",
              "  not present every source as a currently live employer",
              "  posting.", ""]
    return mono(out_path, L)


def build_one(n, stamp_):
    pkg = pkg_dir(n)
    if os.path.exists(pkg):
        shutil.rmtree(pkg)
    for s in SUB:
        os.makedirs(os.path.join(pkg, s))
    d = lambda s: os.path.join(pkg, s)

    # 01 Recording master
    recdocs.copy_master(n, d(SUB[0]))
    recdocs.reading_reference(
        n, os.path.join(d(SUB[0]),
                        "Approved_Recording_Master_Reference.docx"), stamp_)
    recdocs.script_only(
        n, os.path.join(d(SUB[0]),
                        "Video_%d_Script_Only_Recording_Copy.docx" % n))

    # 02 Recording
    prodocs.run_of_show(n, os.path.join(d(SUB[1]),
                                        "Recording_Run_of_Show.docx"), stamp_)

    # 03 Visuals
    prodocs.trigger_map(n, os.path.join(d(SUB[2]), "Sentence_Trigger_Map.txt"))
    prodocs.visual_build_map(
        n, os.path.join(d(SUB[2]), "Visual_Build_and_Motion_Reveal_Map.txt"))
    shootall.build(n, d(SUB[2]), "/tmp/v1421_geo")
    png = os.path.join(d(SUB[2]), "Support_Reference_PNG")
    for f in SETS[n]:
        if f["key"].endswith("_cta"):
            shutil.copy2(os.path.join(png, f["key"] + ".png"),
                         os.path.join(d(SUB[2]), "Resource_Card.png"))
        if f["key"].endswith("_watch_next"):
            shutil.copy2(os.path.join(png, f["key"] + ".png"),
                         os.path.join(d(SUB[2]), "Watch_Next_Card.png"))

    # 04 Riverside
    riverside1421.build(n, os.path.join(d(SUB[3]),
                                        "Riverside_CoCreator_Master_Prompt.txt"))

    # 05 Shorts
    shortsdocs.combined(
        n, os.path.join(d(SUB[4]),
                        "Video_%d_Six_Short_Form_Scripts.docx" % n), stamp_)
    ind = os.path.join(d(SUB[4]), "Individual")
    os.makedirs(ind, exist_ok=True)
    for s in SHORTS[n]:
        shortsdocs.individual(n, s, os.path.join(ind, s["slug"] + ".docx"))
    shortsdocs.manifest(n, os.path.join(d(SUB[4]),
                                        "Shorts_Priority_and_Source_Manifest.txt"))

    # 06 Publishing
    publish1421.build(n, os.path.join(d(SUB[5]),
                                      "Publishing_Materials.docx"), stamp_)

    # 07 Viewer exercise
    exercise1421.build(n, os.path.join(d(SUB[6]),
                                       "Viewer_Exercise.docx"), stamp_)

    # 08 Sources and QA
    source_manifest(n, pkg, stamp_)
    evidence_notes(n, pkg, os.path.join(d(SUB[7]),
                                        "Factual_and_Evidence_Notes.txt"))
    change_log(n, pkg, os.path.join(d(SUB[7]), "Change_Log.txt"), stamp_)
    with open(os.path.join(d(SUB[7]), "Source_Hashes.txt"), "w") as f:
        f.write("%s  %s\n" % (M.read(n)["sha"], M.FILES[n]))
        if n == 14:
            f.write("%s  what-really-transfers-research.md\n"
                    % M.research_hash())
    if n == 14:
        shutil.copy2(os.path.join(M.SRC, M.RESEARCH),
                     os.path.join(d(SUB[7]), M.RESEARCH))

    rows = qafinal.run(n, pkg)
    qa_report(n, pkg, rows, os.path.join(d(SUB[7]), "QA_Report.txt"))
    return pkg, rows


def main():
    s = stamp()
    print("stamp:", s)
    M.verify_all()
    print("all eight masters matched their extraction checksums")

    results = {}
    for n in M.VIDEOS:
        pkg, rows = build_one(n, s)
        # The QA report is written inside the package, so re-run once the
        # package is complete and rewrite it with the final result.
        rows = qafinal.run(n, pkg)
        qa_report(n, pkg, rows,
                  os.path.join(pkg, SUB[7], "QA_Report.txt"))
        rows2 = qafinal.run(n, pkg)
        if [(a, b) for a, b, _ in rows] != [(a, b) for a, b, _ in rows2]:
            raise SystemExit("V%d QA is not at a fixed point" % n)
        z, cnt = zip_dir(pkg, os.path.join(
            OUT, "Video_%d_Final_Production_Package.zip" % n))
        passed = sum(1 for _, ok, _ in rows if ok)
        results[n] = dict(pkg=pkg, zip=z, files=cnt, rows=rows,
                          passed=passed, total=len(rows), sha=sha256(z))
        print("V%-3d %2d/%2d checks  %3d files  %s"
              % (n, passed, len(rows), cnt, os.path.basename(z)))
        for name, ok, detail in rows:
            if not ok:
                print("        FAIL %s :: %s" % (name, detail))

    # Batch-level deliverables.
    import summary1421
    combined = "Videos_14-21_FINAL_Production_Packages.zip"
    batch = summary1421.batch_manifest(
        os.path.join(OUT, "Videos_14-21_Batch_Manifest.json"), s, results)
    log = summary1421.change_log(
        os.path.join(OUT, "SOURCE_HIERARCHY_CHANGE_LOG.txt"), s)
    summ = summary1421.delivery_summary(
        os.path.join(OUT, "Videos_14-21_Delivery_Summary.docx"), s, results,
        combined)

    # The combined archive holds the eight package archives, their checksum
    # files, and the three batch documents. Its own checksum is calculated
    # afterwards and written beside it, never inside it.
    zpath = os.path.join(OUT, combined)
    if os.path.exists(zpath):
        os.remove(zpath)
    members = []
    for n in M.VIDEOS:
        members.append(results[n]["zip"])
        members.append(results[n]["zip"] + ".sha256")
    members += [batch, log, summ]
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED,
                         compresslevel=6) as z:
        for p_ in sorted(members):
            info = zipfile.ZipInfo(os.path.basename(p_), date_time=ZIP_DT)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            with open(p_, "rb") as f:
                z.writestr(info, f.read())
    with open(zpath + ".sha256", "w") as f:
        f.write("%s  %s\n" % (sha256(zpath), combined))

    total = sum(r["total"] for r in results.values())
    passed_all = sum(r["passed"] for r in results.values())
    print()
    print("  %-46s %d entries" % (combined, len(members)))
    print("  sha256 %s" % sha256(zpath))
    print("  package checks: %d of %d passed" % (passed_all, total))
    return s, results


if __name__ == "__main__":
    main()
