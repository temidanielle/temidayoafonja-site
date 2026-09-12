# -*- coding: utf-8 -*-
"""Batch-level deliverables for the corrected Videos 4 to 21 build.

  * the source hierarchy manifest
  * the runtime correction and change log
  * the prior-asset reuse and change table
  * the superseded-materials index
  * the SHA-256 manifest
  * the delivery summary
"""
import os, sys, json
from collections import Counter
sys.path.append("/home/user/temidayoafonja-site/deliverables/riverside-build")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import masters421 as M
import flags421, prior421
import publish421 as PUB
from frames421 import SETS
from shorts421 import SHORTS
from docs421f import (base_doc, para, title_block, rule, h, kv, callout,
                      table, bullets, sub, caption, footer_note, numbered,
                      mono, hr,
                      head, NAVY, GOLD, DIM, RED)

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PRIMARY = ("YouTube_V4-V21_CORRECTED_RUNTIME_Recording_Masters, "
           "18 corrected September 11, 2026 recording masters. For Videos "
           "6, 7 and 8 the spoken source of truth is the restored "
           "derivative, because the supplied file for each was compressed "
           "to roughly half the approved teaching.")

SECONDARY = [
 ("Videos 4 to 7 handoff package, September 9, 2026",
  "Secondary reference. Superseded wherever it differs."),
 ("Videos 8 to 13 production packages, September 9, 2026",
  "Secondary reference. Superseded wherever it differs."),
 ("Videos 14 to 21 final production packages, September 10, 2026",
  "Secondary reference. Superseded wherever it differs."),
]


# ------------------------------------------------------- source hierarchy
def source_hierarchy(out_path, stamp):
    L = head("VIDEOS 4 TO 21  |  SOURCE HIERARCHY MANIFEST")
    L += ["Generated: %s" % stamp, "", hr(), "",
          "THE RULE", "",
          "  The corrected September 11, 2026 recording master wins in every",
          "  conflict. Where any earlier package, script, brief or roadmap",
          "  disagrees with it, the master is right and the earlier material",
          "  is wrong.", "",
          "  The script sets were not merged. No earlier wording was carried",
          "  back into a master, and no master was rewritten, tightened,",
          "  expanded or shortened.", "", hr(), "",
          "PRIMARY, AND DEFINITIVE", "", "  %s" % PRIMARY, ""]
    for n in M.VIDEOS:
        m = M.read(n)
        L += ["    V%-2d  %s" % (n, m["file"]),
              "         SHA-256 %s" % m["sha"]]
        if m["restored"]:
            L += ["         RESTORED DERIVATIVE. Supersedes the supplied "
                  "file below,",
                  "         which is retained unchanged and is not used for "
                  "recording:",
                  "         %s" % m["supplied_file"],
                  "         SHA-256 %s" % m["supplied_sha"]]
    L += ["", hr(), "", "SECONDARY REFERENCE ONLY", ""]
    for name, note in SECONDARY:
        L += ["  %s" % name, "      %s" % note]
    L += ["", hr(), "", "RESEARCH SOURCE OF TRUTH, VIDEO 14 ONLY", "",
          "  %s" % M.RESEARCH,
          "  SHA-256 %s" % M.research_hash(),
          "  28 retained postings. 10 healthcare, 10 financial services,",
          "  8 technology, collected September 10, 2026. 30 was the target",
          "  and was not reached, so 30 is never used as a count.", "",
          hr(), "", "WHAT EACH PACKAGE COPIES UNCHANGED", "",
          "  01_Recording_Master holds the master itself, copied byte for",
          "  byte and never written to. Every other document in the package",
          "  is derived from it and states the master's SHA-256.", ""]
    return mono(out_path, L)


# ------------------------------------------------- runtime correction log
def runtime_log(out_path, stamp):
    L = head("VIDEOS 4 TO 21  |  RUNTIME CORRECTION AND CHANGE LOG")
    L += ["Generated: %s" % stamp, "", hr(), "",
          "WHAT WAS CORRECTED", "",
          "  Videos 4 and 5 are approximately 5-minute test videos. They are",
          "  a deliberate retention experiment and they are the only two.", "",
          "  Videos 6 through 21 are regular long-form. The 5-minute",
          "  experiment is NOT a channel-wide runtime strategy and has not",
          "  been applied to them.", "",
          "  Videos 15 through 21 keep the fuller original regular long-form",
          "  depth, approximately 9 to 12 minutes where that was the approved",
          "  target. Nothing in that range was shortened to meet a 5-minute",
          "  target.", "", hr(), "",
          "EVERY VIDEO, AND WHERE IT SITS", ""]
    L += ["  %-4s %-11s %-7s %-15s %s"
          % ("V", "MODE", "WORDS", "SPEECH ONLY", "TARGET STATED BY MASTER"),
          "  " + "-" * 92]
    for n in M.VIDEOS:
        w, fast, slow = M.estimate(n)
        mode = "5-MIN TEST" if n in M.FIVE_MIN else "LONG-FORM"
        L += ["  %-4s %-11s %-7d %-15s %s"
              % ("V%d" % n, mode, w, "%s to %s" % (fast, slow),
                 M.runtime_intent(n) or "none stated")]
    L += ["",
          "  Every figure is arithmetic on the script at 130 to 145 words per",
          "  minute. It is speech only. It excludes pauses, visual holds and",
          "  delivery, so a recorded runtime will be longer than the range",
          "  shown. No figure here is a measured runtime.", "", hr(), "",
          "SUPERSEDED RUNTIME LANGUAGE", "",
          "  Any earlier document that describes a 5-minute target for a",
          "  video other than V4 or V5 is superseded by this log. Any earlier",
          "  document that describes the 5-minute experiment as the channel's",
          "  runtime direction is superseded by this log.", "", hr(), "",
          "FLAGGED, NOT REPAIRED", ""]
    fl = flags421.all_flags()
    if not fl:
        L += ["  Nothing flagged.", ""]
    for n, kind, label, detail in fl:
        L += ["  V%-3d [%s] %s" % (n, kind, label)]
        for line in _wrap(detail, 72):
            L += ["        %s" % line]
        L += [""]
    L += [hr(), "",
          "  None of the above was corrected in any package. Approved speech",
          "  is not edited, and a difference between two approved masters is",
          "  not resolved by rewriting one of them.", ""]
    return mono(out_path, L)


def _wrap(s, w):
    out, line = [], ""
    for word in s.split():
        if len(line) + len(word) + 1 > w:
            out.append(line)
            line = word
        else:
            line = (line + " " + word).strip()
    if line:
        out.append(line)
    return out


# ------------------------------------------------------ prior-asset table
def prior_asset_table(out_path, stamp, rows, prior):
    bad = prior421.contradictions(rows)
    cnt = Counter(r["declared"] for r in rows)
    ident = sum(1 for r in rows if r["identical"])
    L = head("VIDEOS 4 TO 21  |  PRIOR-ASSET REUSE AND CHANGE TABLE")
    L += ["Generated: %s" % stamp, "", hr(), "",
          "THE TEST", "",
          "  An asset is REUSE only when a prior rendered asset exists and",
          "  the newly rendered PNG is byte-identical to it. A similar visual",
          "  topic, a similar headline or a shared layout is not reuse.", "",
          "  %d of %d newly rendered assets are byte-identical to a prior"
          % (ident, len(rows)),
          "  rendered asset.", "", hr(), "",
          "DECLARED CLASSIFICATION", ""]
    for k, v in sorted(cnt.items(), key=lambda kv: -kv[1]):
        L += ["    %-24s %d" % (k, v)]
    L += ["", hr(), "", "CONTRADICTIONS BETWEEN THE LABEL AND THE BYTES", ""]
    if bad:
        for n, key, why in bad:
            L += ["  V%-3d %-34s %s" % (n, key, why)]
    else:
        L += ["  None. Every REUSE label is backed by a byte-identical prior",
              "  file, and nothing labeled NEW matches a prior file.", ""]
    L += ["", hr(), "", "EVERY ASSET", "",
          "  %-34s %-22s %-10s %s"
          % ("ASSET", "CLASSIFICATION", "IDENTICAL", "MATCHED PRIOR FILE"),
          "  " + "-" * 110]
    for r in rows:
        L += ["  %-34s %-22s %-10s %s"
              % (r["key"], r["declared"], "yes" if r["identical"] else "no",
                 ("%s/%s" % r["matched"]) if r["matched"] else "")]
    L += ["", hr(), "", "WHY EACH ASSET CARRIES ITS CLASSIFICATION", ""]
    for r in rows:
        L += ["  V%-3d %s" % (r["video"], r["key"])]
        for line in _wrap(r["why"], 70):
            L += ["        %s" % line]
        L += [""]
    return mono(out_path, L)


# ------------------------------------------------ superseded materials
def superseded_titles():
    """Every title an earlier package carried that a corrected master
    replaced. Read from the earlier packages themselves, not from a list
    typed here, so it cannot drift out of date."""
    import re
    old = {}
    # V4 to V7: the package directory names are the record.
    for n, d in zip(range(4, 8), prior421.V47):
        name = os.path.basename(d.rstrip("/"))
        t = name.split("_", 2)[2].rsplit("_FINAL", 1)[0].replace("_", " ")
        old[n] = t
    # V8 to V13 and V14 to V21: their build modules hold the titles.
    for path, mod, rng in (
        ("VIDEOS_8-13_LOCKED_MASTER_BUILD/build", "masters813", range(8, 14)),
        ("VIDEOS_14-21_FINAL_PRODUCTION/build", "masters1421", range(14, 22))):
        full = os.path.join(os.path.dirname(OUT), path)
        if not os.path.isdir(full):
            continue
        sys.path.insert(0, full)
        try:
            m = __import__(mod)
            for n in rng:
                old[n] = m.title(n)
        except Exception:
            pass

    def fold(x):
        return re.sub(r"[^a-z0-9]+", " ", x.lower()).strip()

    return [(n, old[n], M.title(n)) for n in sorted(old)
            if fold(old[n]) != fold(M.title(n))]



def superseded_index(out_path, stamp, rows, prior):
    sup = prior421.superseded(rows, prior)
    by_body = {}
    for body, rel, h_ in sup:
        by_body.setdefault(body, []).append((rel, h_))
    L = head("VIDEOS 4 TO 21  |  SUPERSEDED MATERIALS INDEX")
    L += ["Generated: %s" % stamp, "", hr(), "",
          "WHAT THIS LISTS", "",
          "  Every rendered asset in an earlier package that has NO",
          "  byte-identical successor in this corrected build. Each one is",
          "  superseded: it was built against an earlier script and must not",
          "  be used for recording, editing or publishing.", "",
          "  These files are not deleted. They remain where they are as",
          "  history. They are simply not current.", "", hr(), ""]
    for name, roots, desc in prior421.BODIES:
        items = by_body.get(name, [])
        L += ["%s" % desc,
              "  %d superseded rendered assets" % len(items), ""]
        for rel, h_ in sorted(items):
            L += ["    %s" % rel, "        SHA-256 %s" % h_]
        L += ["", hr(), ""]
    L += ["SUPERSEDED TITLES", "",
          "  Titles the earlier packages carried that no corrected master",
          "  carries. Any document still using one of these is out of date.",
          ""]
    for n, old, new in superseded_titles():
        L += ["    V%-3d was: %s" % (n, old),
              "         now: %s" % new]
    L += ["", hr(), "",
          "SUPERSEDED RECORDING MASTERS", "",
          "  The September 11 masters supplied for Videos 6, 7 and 8. Each",
          "  carried about half the approved teaching after a compression",
          "  pass that should only ever have applied to Videos 4 and 5. They",
          "  are retained unchanged, and they are not used for recording.",
          ""]
    for n in sorted(M.RESTORED):
        m = M.read(n)
        L += ["    %s" % m["supplied_file"],
              "        SHA-256 %s" % m["supplied_sha"]]
    L += ["", hr(), "",
          "SUPERSEDED WRITTEN MATERIAL", "",
          "  Videos_14-21_SCRIPT_DEVELOPMENT_REVIEW.zip. Development history.",
          "  Its scripts are not current speech and are not retained as",
          "  alternates.", "",
          "  Any earlier runtime statement that applies a 5-minute target to",
          "  a video other than V4 or V5.", "",
          "  Any earlier document using one of the superseded titles listed",
          "  above. The corrected masters are the authority on every title.",
          ""]
    return mono(out_path, L)


# ------------------------------------------------------- SHA-256 manifest
def sha_manifest(out_path, stamp, results, root):
    L = head("VIDEOS 4 TO 21  |  SHA-256 MANIFEST")
    L += ["Generated: %s" % stamp, "", hr(), "",
          "CORRECTED RECORDING MASTERS, THE SOURCE OF TRUTH", ""]
    for n in M.VIDEOS:
        L += ["  %s  %s" % (M.read(n)["sha"], M.FILES[n])]
    L += ["  %s  %s" % (M.research_hash(), M.RESEARCH), "", hr(), "",
          "PACKAGE ARCHIVES", ""]
    for n in M.VIDEOS:
        r = results[n]
        L += ["  %s  %s" % (r["sha"], os.path.basename(r["zip"]))]
    L += ["", hr(), "", "EVERY FILE IN EVERY PACKAGE", ""]
    for n in M.VIDEOS:
        pkg = results[n]["pkg"]
        L += ["  VIDEO %d" % n, ""]
        for dirpath, _, files in sorted(os.walk(pkg)):
            for fn in sorted(files):
                p = os.path.join(dirpath, fn)
                L += ["    %s  %s" % (prior421.sha(p),
                                      os.path.relpath(p, pkg))]
        L += [""]
    L += [hr(), "",
          "  The combined archive's own checksum is written beside it in a",
          "  separate .sha256 file. It is never embedded inside the archive,",
          "  because an archive cannot contain its own checksum.", ""]
    return mono(out_path, L)


# -------------------------------------------------------- delivery summary
def delivery_summary(out_path, stamp, results, combined, rows):
    ident = sum(1 for r in rows if r["identical"])
    total_checks = sum(r["total"] for r in results.values())
    passed = sum(r["passed"] for r in results.values())
    d = base_doc()
    footer_note(d, "Videos 4 to 21  |  corrected runtime and production "
                   "synchronization  |  September 11, 2026")
    title_block(d, "Capability Formation  |  Videos 4 to 21",
                "Corrected Runtime and Production Synchronization",
                "Eighteen packages rebuilt from the corrected September 11 "
                "recording masters")
    kv(d, "Generated", stamp)
    kv(d, "Combined archive", combined)

    callout(d, "Videos 4 and 5 are the only 5-minute test videos. Videos 6 "
               "through 21 are regular long-form, and Videos 15 through 21 "
               "keep the fuller 9 to 12 minute depth. The 5-minute "
               "experiment is not a channel-wide runtime strategy and has "
               "not been applied anywhere else.")

    h(d, "Runtime mode, every video")
    table(d, ["V", "Mode", "Words", "Speech-only estimate", "Target stated"],
          [[str(n), "5-minute test" if n in M.FIVE_MIN else "Regular "
            "long-form", str(M.estimate(n)[0]),
            "%s to %s" % M.estimate(n)[1:],
            M.runtime_intent(n) or "none stated"] for n in M.VIDEOS],
          widths=[0.35, 1.25, 0.6, 1.5, 2.9], size=8)
    caption(d, "Every figure is arithmetic on the script at 130 to 145 words "
               "per minute. It is speech only and excludes pauses and visual "
               "holds, so a recorded runtime will be longer. None of these "
               "is measured.")

    h(d, "What was built")
    table(d, ["V", "Title", "Assets", "Shorts", "Checks", "Files"],
          [[str(n), M.title(n), str(len(SETS[n])), str(len(SHORTS[n])),
            "%d/%d" % (results[n]["passed"], results[n]["total"]),
            str(results[n]["files"])] for n in M.VIDEOS],
          widths=[0.3, 3.5, 0.6, 0.6, 0.75, 0.55], size=8)

    h(d, "The source hierarchy")
    bullets(d, [
      "The corrected September 11, 2026 recording master wins in every "
      "conflict. Where any earlier package disagrees with it, the master is "
      "right.",
      "The script sets were not merged. No earlier wording was carried back "
      "into a master.",
      "No master was rewritten, tightened, expanded or shortened. Each was "
      "copied byte for byte into its package and never written to.",
      "The Videos 4 to 7 handoff and the Videos 8 to 13 packages are "
      "secondary reference only.",
    ])

    h(d, "Prior-asset audit")
    para(d, "%d of %d newly rendered assets are byte-identical to an asset "
            "in an earlier package. Everything else was rebuilt, had its "
            "copy updated, or is new. Nothing is described as reuse because "
            "its topic sounded similar." % (ident, len(rows)))
    cnt = Counter(r["declared"] for r in rows)
    table(d, ["Classification", "Assets"],
          [[k, str(v)] for k, v in sorted(cnt.items(), key=lambda kv: -kv[1])],
          widths=[3.0, 1.0], size=9)

    h(d, "Flagged, not repaired")
    fl = flags421.all_flags()
    if fl:
        table(d, ["V", "Kind", "Finding"],
              [["V%d" % n, k, "%s. %s" % (l, dt)] for n, k, l, dt in fl],
              widths=[0.4, 1.0, 5.3], size=8)
    else:
        para(d, "Nothing flagged.")
    caption(d, "None of these was corrected. Approved speech is not edited, "
               "and a difference between two approved masters is not "
               "resolved by rewriting one of them.")

    h(d, "Package checks")
    para(d, "%d of %d package checks passed. Every check ran against the "
            "built package on disk, not against the build data."
            % (passed, total_checks))

    h(d, "What is not verified and is not claimed")
    bullets(d, [
      "No video has been recorded, edited or exported.",
      "Every runtime figure is arithmetic, not measured.",
      "No thumbnail artwork exists or is approved.",
      "No chapters, SRT or music attribution exists. They come from the "
      "finished export.",
      "No public link has been checked.",
      "Nothing here claims that all experience transfers. Employer "
      "constraints, bias, markets, credentials, regulation, domain "
      "knowledge, relationships, compensation realities, genuine gaps and "
      "relearning all still apply.",
    ])
    d.save(out_path)
    return out_path
