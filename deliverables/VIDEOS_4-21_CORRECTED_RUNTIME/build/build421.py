# -*- coding: utf-8 -*-
"""Build the eight Videos 4 to 21 final production packages.

  python3 build1421.py
"""
import os, sys, json, shutil, zipfile, hashlib, datetime, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

# Appended, never inserted at the front: this batch's own modules must win
# over the September 10 batch's identically named ones.
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                "VIDEOS_14-21_FINAL_PRODUCTION/build")
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                "riverside-build")
# Several modules in the earlier batches put their own directory at the front
# of sys.path when they load, and this batch has files with the same names.
# Importing by name would then be a race decided by import order. These three
# are loaded from this directory by explicit path instead, and registered
# under their names before anything else can claim them.
import importlib.util


def _local(name):
    spec = importlib.util.spec_from_file_location(
        name, os.path.join(HERE, name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


for _n in ("docs421f", "masters421", "content421", "recdocs", "prodocs",
           "shortsdocs", "publish421"):
    _local(_n)

import masters421 as M
import recdocs, prodocs, shortsdocs
import editorial421, flags421, prior421, summary421
import assetclass421, priortext421, restore678, verifyrestore
import publish421, exercise421, qa421, shootall421, riverside421
import research14
from frames421 import SETS
from shorts421 import SHORTS
from docs421f import mono, hr, head

for _name in ("docs421f", "masters421", "content421", "recdocs", "prodocs",
              "shortsdocs", "publish421", "exercise421", "qa421",
              "riverside421", "shootall421"):
    if os.path.dirname(os.path.abspath(sys.modules[_name].__file__)) != HERE:
        raise SystemExit("%s resolved to %s, not to this batch"
                         % (_name, sys.modules[_name].__file__))

SUB = ["01_Recording_Master", "02_Recording", "03_Visuals", "04_Riverside",
       "05_Shorts", "06_Publishing", "07_Viewer_Exercise",
       "08_Sources_and_QA"]

ZIP_DT = (2026, 9, 11, 0, 0, 0)


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
    return os.path.join(OUT, "VIDEO_%d_CORRECTED_RUNTIME_PACKAGE" % n)


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
      "secondary_reference": [
        {"body": name, "description": desc,
         "status": "Secondary reference only. Superseded wherever it "
                   "differs from the corrected master."}
        for name, _roots, desc in prior421.BODIES],
      "runtime": {
        "mode": M.mode(n),
        "is_five_minute_test": n in M.FIVE_MIN,
        "restored_regular_depth": n in M.RESTORED_DEPTH,
        "target_stated_by_master": M.runtime_intent(n) or None,
        "note": "Videos 4 and 5 are the only 5-minute retention test. "
                "Videos 6 to 21 are regular long-form and were not "
                "shortened to meet a 5-minute target."},
      "packaging": {
        "thumbnail": M.thumbnail(n),
        "framework": M.framework(n) or None,
        "primary_cta": publish421.primary_cta(n)[0],
        "primary_cta_spoken_at": publish421.primary_cta(n)[1],
        "resource": publish421.route(n) or None,
        "resource_spoken": publish421.spoken_route(n),
        "watch_next": "Video %s: %s" % publish421.watch_next(n)[:2],
        "watch_next_source": publish421.watch_next(n)[2]},
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
    for item in qa421.FINAL_EXPORT_PENDING:
        L += ["  [ PENDING ] %s" % item]
    L += ["", hr(), "",
          "  Nothing in this list can be checked until the video has been",
          "  recorded, edited and exported.", ""]
    return mono(out_path, L)


def change_log(n, pkg, out_path, stamp_, prior_rows=None):
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
          "  It OVERRIDES every earlier script, package, brief and roadmap",
          "  for this video. The corrected September 11 recording master wins",
          "  in every conflict. The script sets were not merged, no earlier",
          "  wording was carried back into the master, and the master was not",
          "  rewritten, tightened, expanded or shortened.", "", hr(), "",
          "RUNTIME", "",
          "  Mode: %s" % M.mode(n), ""]
    if n in M.FIVE_MIN:
        L += ["  This is one of the two approximately 5-minute test videos.",
              "  V4 and V5 are the only two. The experiment does not extend",
              "  past V5."]
    else:
        L += ["  This is regular long-form. It is NOT part of the V4 and V5",
              "  5-minute experiment, and it was not shortened to meet a",
              "  5-minute target."]
        if n in M.RESTORED_DEPTH:
            L += ["  Its fuller original regular long-form depth is preserved,",
                  "  approximately 9 to 12 minutes, which was the approved",
                  "  target."]
    w, fast, slow = M.estimate(n)
    L += ["",
          "  %d spoken words. %s to %s at 130 to 145 words per minute."
          % (w, fast, slow),
          "  Target stated by the master: %s"
          % (M.runtime_intent(n) or "none stated"),
          "  The estimate is speech only. It excludes pauses and visual",
          "  holds, so the recorded runtime will be longer. It is not a",
          "  measured runtime.", ""]
    vf = [f for f in flags421.all_flags() if f[0] == n]
    if vf:
        L += ["  FLAGGED, NOT REPAIRED:", ""]
        for _n, kind, label, detail in vf:
            L += ["    [%s] %s" % (kind, label)]
            for line in summary421._wrap(detail, 68):
                L += ["          %s" % line]
        L += [""]
    L += [hr(), "",
          "WHAT WAS AUDITED AND REUSED", "",
          "  Every rendered asset in the earlier packages was checked against",
          "  this master and classified. A card is REUSE only when the newly",
          "  rendered file is byte-identical to the earlier one. Not when the",
          "  visual topic sounds similar.", ""]
    for k in ("REUSE", "COPY UPDATE", "REBUILD", "NEW",
              "REMOVE, replaced by NEW"):
        if cnt.get(k):
            L += ["    %-26s %d" % (k, cnt[k])]
    L += [""]
    if prior_rows is not None:
        mine = [r for r in prior_rows if r["video"] == n]
        ident = [r for r in mine if r["identical"]]
        L += ["  %d of %d newly rendered assets are byte-identical to a"
              % (len(ident), len(mine)),
              "  prior rendered asset:", ""]
        for r in ident:
            L += ["    %-34s matches %s/%s" % (r["key"], r["matched"][0],
                                               r["matched"][1])]
        if not ident:
            L += ["    none"]
        L += ["",
              "  Every other asset in this package changed. Where a card was",
              "  first written down as reuse and the rendered bytes did not",
              "  bear that out, the label was corrected and the card's own",
              "  note records both the measurement and what was originally",
              "  written.", ""]
    L += ["", hr(), "",
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
    shootall421.build(n, d(SUB[2]), "/tmp/v421_geo")
    png = os.path.join(d(SUB[2]), "Support_Reference_PNG")
    for f in SETS[n]:
        if f["key"].endswith("_cta"):
            shutil.copy2(os.path.join(png, f["key"] + ".png"),
                         os.path.join(d(SUB[2]), "Resource_Card.png"))
        if f["key"].endswith("_watch_next"):
            shutil.copy2(os.path.join(png, f["key"] + ".png"),
                         os.path.join(d(SUB[2]), "Watch_Next_Card.png"))

    # 04 Riverside
    riverside421.build(n, os.path.join(d(SUB[3]),
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
    publish421.build(n, os.path.join(d(SUB[5]),
                                      "Publishing_Materials.docx"), stamp_)

    # 07 Viewer exercise
    exercise421.build(n, os.path.join(d(SUB[6]),
                                       "Viewer_Exercise.docx"), stamp_)
    editorial421.build(n, os.path.join(d(SUB[6]),
                                       "Editorial_Check.docx"), stamp_)

    # 08 Sources and QA
    source_manifest(n, pkg, stamp_)
    evidence_notes(n, pkg, os.path.join(d(SUB[7]),
                                        "Factual_and_Evidence_Notes.txt"))
    change_log(n, pkg, os.path.join(d(SUB[7]), "Change_Log.txt"), stamp_)
    if n in M.RESTORED:
        mono(os.path.join(d(SUB[7]), "Restoration_Provenance.txt"),
             head("VIDEO %d  |  RESTORATION PROVENANCE" % n)
             + [M.title(n), "",
                "The September 11 master supplied for this video carried "
                "about half",
                "the approved teaching. This package is built from a "
                "restored",
                "derivative. The supplied file is unchanged in _source/ and "
                "still",
                "matches its original checksum:", "",
                "    %s" % M.FILES[n],
                "    SHA-256 %s" % M.read(n)["supplied_sha"], "",
                "    %s" % M.filename(n),
                "    SHA-256 %s" % M.read(n)["sha"], "", hr(), ""]
             + restore678.provenance_report(n))
    with open(os.path.join(d(SUB[7]), "Source_Hashes.txt"), "w") as f:
        f.write("%s  %s\n" % (M.read(n)["sha"], M.filename(n)))
        if n in M.RESTORED:
            f.write("%s  %s  (supplied, superseded)\n"
                    % (M.read(n)["supplied_sha"], M.FILES[n]))
        if n == 14:
            f.write("%s  what-really-transfers-research.md\n"
                    % M.research_hash())
    if n == 14:
        shutil.copy2(os.path.join(M.SRC, M.RESEARCH),
                     os.path.join(d(SUB[7]), M.RESEARCH))

    rows = qa421.run(n, pkg)
    qa_report(n, pkg, rows, os.path.join(d(SUB[7]), "QA_Report.txt"))
    return pkg, rows




def main():
    s = stamp()
    print("stamp:", s)
    M.verify_all()
    print("all 18 corrected masters matched their extraction checksums")

    # Editorial standard, before anything is built.
    ed = editorial421.failures()
    if ed:
        for n, label, note in ed:
            print("V%d EDITORIAL: %s :: %s" % (n, label, note))
        raise SystemExit("editorial check failed")
    print("editorial check: painful problem, solution, viewer outcome, "
          "18 videos, all pass")

    results, png_dirs = {}, {}
    for n in M.VIDEOS:
        pkg, rows = build_one(n, s)
        png_dirs[n] = os.path.join(pkg, SUB[2], "Support_Reference_PNG")
        results[n] = dict(pkg=pkg, rows=rows)

    # The prior-asset audit runs against the rendered PNGs, so it happens
    # after every package has been built and before anything is archived.
    prior_rows, prior_index = prior421.audit(png_dirs)
    identical = {r["key"] for r in prior_rows if r["identical"]}
    bad = assetclass421.disagreements(identical)
    if bad:
        for n, key, declared, measured, ev in bad:
            print("V%d ASSET %s: declared %s, measured %s :: %s"
                  % (n, key, declared, measured, ev))
        raise SystemExit("an asset classification is not supported by the "
                         "evidence")
    print("prior-asset audit: %d of %d newly rendered assets are "
          "byte-identical to an earlier rendered asset, and every REUSE "
          "label is backed by that identity"
          % (len(identical), len(prior_rows)))

    for n in M.VIDEOS:
        pkg = results[n]["pkg"]
        # Rewrite the change log now that the audit has run, then re-run QA
        # against the finished package and settle it at a fixed point.
        change_log(n, pkg, os.path.join(pkg, SUB[7], "Change_Log.txt"), s,
                   prior_rows)
        rows = qa421.run(n, pkg)
        qa_report(n, pkg, rows, os.path.join(pkg, SUB[7], "QA_Report.txt"))
        rows2 = qa421.run(n, pkg)
        if [(a, b) for a, b, _ in rows] != [(a, b) for a, b, _ in rows2]:
            raise SystemExit("V%d QA is not at a fixed point" % n)
        z, cnt = zip_dir(pkg, os.path.join(
            OUT, "Video_%d_Corrected_Runtime_Package.zip" % n))
        passed = sum(1 for _, ok, _ in rows if ok)
        results[n].update(zip=z, files=cnt, rows=rows, passed=passed,
                          total=len(rows), sha=sha256(z))
        print("V%-3d %2d/%2d checks  %3d files  %s"
              % (n, passed, len(rows), cnt, os.path.basename(z)))
        for name, ok, detail in rows:
            if not ok:
                print("        FAIL %s :: %s" % (name, detail))

    # Batch-level deliverables.
    combined = "Videos_4-21_CORRECTED_RUNTIME_Production_Packages.zip"
    batch = []
    batch.append(summary421.source_hierarchy(
        os.path.join(OUT, "Source_Hierarchy_Manifest.txt"), s))
    batch.append(summary421.runtime_log(
        os.path.join(OUT, "Runtime_Correction_and_Change_Log.txt"), s))
    batch.append(summary421.prior_asset_table(
        os.path.join(OUT, "Prior_Asset_Reuse_and_Change_Table.txt"), s,
        prior_rows, prior_index))
    batch.append(summary421.superseded_index(
        os.path.join(OUT, "Superseded_Materials_Index.txt"), s, prior_rows,
        prior_index))
    batch.append(summary421.sha_manifest(
        os.path.join(OUT, "SHA256_Manifest.txt"), s, results, OUT))
    batch.append(summary421.delivery_summary(
        os.path.join(OUT, "Videos_4-21_Delivery_Summary.docx"), s, results,
        combined, prior_rows))

    # The combined archive holds the 18 package archives, their checksum
    # files, and the batch documents. Its own checksum is calculated
    # afterwards and written beside it, never inside it, because an archive
    # cannot contain a checksum of itself.
    zpath = os.path.join(OUT, combined)
    if os.path.exists(zpath):
        os.remove(zpath)
    members = []
    for n in M.VIDEOS:
        members.append(results[n]["zip"])
        members.append(results[n]["zip"] + ".sha256")
    members += batch
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
    print("  %-58s %d entries" % (combined, len(members)))
    print("  sha256 %s  (written beside the archive, not inside it)"
          % sha256(zpath))
    print("  package checks: %d of %d passed" % (passed_all, total))
    for n, kind, label, detail in flags421.all_flags():
        print("  FLAGGED V%-3d [%s] %s" % (n, kind, label))
    return s, results


if __name__ == "__main__":
    main()
