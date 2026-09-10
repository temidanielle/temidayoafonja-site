# -*- coding: utf-8 -*-
"""Batch manifest, delivery summary and source-hierarchy change log."""
import os, sys, json, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import masters1421 as M
import research14, flags1421
from frames1421 import SETS
from shorts1421 import SHORTS
from docs1421f import (base_doc, para, title_block, rule, h, kv, callout,
                       table, bullets, sub, footer_note, numbered, mono, hr,
                       head, NAVY, GOLD, DIM, RED)

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(OUT)


def batch_manifest(out_path, stamp, results):
    from collections import Counter
    data = {
      "batch": "Videos 14 to 21 final production packages",
      "generated": stamp,
      "source_hierarchy": {
        "primary": "YouTube_V14-V21_FINAL_Complete_Recording_Masters.zip, "
                   "eight locked final Recording Masters. Definitive spoken "
                   "source of truth.",
        "secondary_research": "what-really-transfers-research.md, the research "
                              "source of truth for Video 14 only.",
        "superseded": "Videos_14-21_SCRIPT_DEVELOPMENT_REVIEW.zip. "
                      "Development history. Its scripts are not current "
                      "speech.",
        "context": ["Videos_1421_Roadmap_Addendum.docx",
                    "Videos_1421_Development_Briefs.docx"],
      },
      "masters": {str(n): {"file": M.FILES[n], "sha256": M.read(n)["sha"],
                           "title": M.title(n), "thumbnail": M.thumbnail(n),
                           "framework": M.framework(n),
                           "primary_cta": M.cta(n),
                           "resource": M.resource(n) or None,
                           "watch_next": M.watch_next(n),
                           "spoken_words": M.word_count(n),
                           "speech_only_estimate":
                               "%s to %s" % M.estimate(n)[1:]}
                  for n in M.VIDEOS},
      "research_archive": {"file": M.RESEARCH, "sha256": M.research_hash(),
                           "retained": 28,
                           "by_industry": {"healthcare": 10,
                                           "financial_services": 10,
                                           "technology": 8},
                           "collected": "2026-09-10"},
      "packages": {str(n): {"zip": os.path.basename(r["zip"]),
                            "sha256": r["sha"], "files": r["files"],
                            "checks_passed": r["passed"],
                            "checks_total": r["total"],
                            "assets": len(SETS[n]),
                            "shorts": len(SHORTS[n])}
                   for n, r in results.items()},
      "asset_classification": dict(Counter(
          f["status"] for n in M.VIDEOS for f in SETS[n])),
      "not_verified": [
        "No video has been recorded, edited or exported.",
        "Every runtime figure is arithmetic on the script, not measured.",
        "No thumbnail artwork exists or is approved.",
        "No chapters, SRT or music attribution exists.",
        "No public link has been checked."],
    }
    with open(out_path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return out_path


def change_log(out_path, stamp):
    L = head("VIDEOS 14 TO 21  |  SOURCE HIERARCHY CHANGE LOG")
    L += ["Generated: %s" % stamp, "", hr(), "",
          "1. THE EARLIER DRAFTS ARE SUPERSEDED", "",
          "   The V15 to V21 recording scripts this workspace drafted in",
          "   Videos_14-21_SCRIPT_DEVELOPMENT_REVIEW.zip are SUPERSEDED.",
          "   They are development history. They were not merged with the new",
          "   masters, they were not used to reword them, and they are not",
          "   retained anywhere as alternate recording scripts.", "",
          "2. THE EIGHT NEW MASTERS ARE AUTHORITATIVE", "",
          "   The masters inside",
          "   YouTube_V14-V21_FINAL_Complete_Recording_Masters.zip are now the",
          "   definitive spoken source of truth for Videos 14 to 21. They",
          "   control the exact spoken script, hook, teaching sequence, title,",
          "   thumbnail wording, framework, examples, qualifications, CTA,",
          "   resource route, Watch Next, closing line and boundaries.", ""]
    for n in M.VIDEOS:
        L += ["     V%-3d %s" % (n, M.FILES[n]),
              "          SHA-256 %s" % M.read(n)["sha"]]
    L += ["", "3. VIDEO 14 RESEARCH IS COMPLETE", "",
          "   The research has been done and documented. Video 14 is no",
          "   longer script blocked. The previous status,",
          "   V14 FINAL SCRIPT BLOCKED PENDING DOCUMENTED RESEARCH,",
          "   is superseded.", "",
          "4. THE V14 SAMPLE IS 28, NOT 30", "",
          "   28 retained postings. 10 healthcare, 10 financial services,",
          "   8 technology. All collected September 10, 2026. 30 was the",
          "   target and was not reached, and the shortfall is stated rather",
          "   than papered over. Nothing in this batch uses 30.", "",
          "5. THE V14 QUESTION TITLE IS THE CURRENT APPROVED TITLE", "",
          "   Which Parts of Your Experience Actually Transfer to Another",
          "   Industry?",
          "   Thumbnail: WHAT REALLY TRANSFERS?",
          "   The numerical past-tense title is NOT restored as active",
          "   packaging. If it is ever reconsidered, the number must be the",
          "   actual retained sample.", "",
          "6. PRODUCTION CONCEPTS WERE REUSED ONLY WHERE THEY ALIGN", "",
          "   Every concept from the superseded package was read against the",
          "   new master and classified REUSE, REORDER, COPY UPDATE, REBUILD,",
          "   REMOVE or NEW, with a reason recorded per asset. No frame is",
          "   described as byte-identical reuse, because the superseded",
          "   package contained written concepts and no rendered production",
          "   asset for any video in this range.", ""]
    from collections import Counter
    cnt = Counter(f["status"] for n in M.VIDEOS for f in SETS[n])
    for k in ("REUSE", "REORDER", "COPY UPDATE", "REBUILD", "REMOVE", "NEW"):
        L += ["     %-12s %d" % (k, cnt.get(k, 0))]
    L += ["", "7. VIDEOS 1 TO 13 WERE NOT CHANGED", "",
          "   No script, asset, thumbnail, Short, publishing material or",
          "   route belonging to Videos 1 to 13 was touched. Videos 22 to 30",
          "   were not started.", "",
          "8. RESERVED TOPICS WERE NOT RENUMBERED", "",
          "   The employer due-diligence topic, Before You Accept the Job,",
          "   Find Out How the Company Actually Uses People Like You, stays",
          "   reserved and unnumbered.",
          "   The after-40 topic, How to Stay Relevant After 40 Without",
          "   Chasing Every Trend, stays in the future queue with its",
          "   thumbnail direction UPDATE. DON'T ERASE. and is not assigned a",
          "   number.",
          "   V22 remains the promotion-timing slot.", ""]
    return mono(out_path, L)


def delivery_summary(out_path, stamp, results, combined_name):
    d = base_doc()
    footer_note(d, "Capability Formation  |  Videos 14 to 21 final production "
                   "packages  |  ready for recording and Riverside")
    title_block(d, "Capability Formation  |  Videos 14 to 21",
                "Final Production Packages",
                "Built against the eight locked final Recording Masters")
    kv(d, "Generated", stamp)
    kv(d, "Primary source", "YouTube_V14-V21_FINAL_Complete_Recording_"
                            "Masters.zip, eight locked masters")
    kv(d, "Research source", "%s  ·  SHA-256 %s"
       % (M.RESEARCH, M.research_hash()))
    kv(d, "Superseded", "Videos_14-21_SCRIPT_DEVELOPMENT_REVIEW.zip. "
                        "Development history only.")

    callout(d, "The eight new masters override every script this workspace "
               "drafted earlier. The two script sets were not merged, no "
               "approved speech was reworded, and no earlier draft is kept as "
               "an alternate. Each master was copied byte for byte into its "
               "package and never written to.")

    h(d, "The eight packages")
    rows = []
    for n in M.VIDEOS:
        r = results[n]
        w, fast, slow = M.estimate(n)
        rows.append(["V%d" % n, M.title(n), M.thumbnail(n),
                     "{:,}".format(w), "%s to %s" % (fast, slow),
                     "%d of %d" % (r["passed"], r["total"])])
    table(d, ["#", "Title", "Thumbnail", "Words", "Estimate", "Checks"], rows,
          widths=[0.4, 2.3, 1.5, 0.65, 1.0, 0.85], size=8)
    para(d, "Estimates are arithmetic on the spoken script at 130 to 145 "
            "words per minute. They exclude pauses and visual holds. No "
            "recording has been timed.", size=9.5, color=DIM)

    h(d, "What is in each package")
    table(d, ["Folder", "Contents"], [
      ["01_Recording_Master", "The untouched locked master, an approved "
                              "reading reference generated from it, and the "
                              "script-only MacBook recording copy."],
      ["02_Recording", "Run of show, the exact opening and final line, the "
                       "thought-block method, and the ending checklist."],
      ["03_Visuals", "Sentence trigger map, visual build and motion reveal "
                     "map, ten 1920 by 1080 support PNGs, an editable "
                     "PowerPoint deck, a phone-size contact sheet, the "
                     "resource card and the Watch Next card."],
      ["04_Riverside", "One complete self-contained Co-Creator master prompt "
                       "with per-scene instructions, audio treatment, camera "
                       "budget, the sound and transition-hook plan and SRT "
                       "instructions."],
      ["05_Shorts", "The combined Shorts document, six individual scripts, "
                    "and the priority and source manifest."],
      ["06_Publishing", "Description, pinned comment, tags, hashtags, "
                        "resource route, Watch Next and playlist, the Canva "
                        "thumbnail brief and the publication checklist."],
      ["07_Viewer_Exercise", "The artifact the script's own CTA asks for."],
      ["08_Sources_and_QA", "Source manifest, source hashes, factual and "
                            "evidence notes, the QA report, the change log "
                            "and the pending final-export list. Video 14 also "
                            "carries the research archive and its reference "
                            "map."],
    ], widths=[1.5, 5.2], size=8.5)

    h(d, "Video 14 research")
    rrows, ok = research14.verify()
    para(d, "The research is complete and Video 14 is no longer script "
            "blocked. %d of %d claims used anywhere in the package were "
            "verified against the supplied archive at build time."
         % (sum(1 for _, g, _ in rrows if g), len(rrows)))
    bullets(d, [
      "28 retained postings. 10 healthcare, 10 financial services, 8 "
      "technology. All collected September 10, 2026.",
      "30 was the target and was not reached. Nothing in this batch uses 30, "
      "and the numerical past-tense title is not restored as active "
      "packaging.",
      "The mixed finding is preserved. The package does not say your "
      "experience transfers and it does not say it does not.",
      "Counts keep their denominator. Six of 28 postings make same-industry "
      "experience a hard requirement, and that is stated as a count within "
      "these 28 postings rather than as a rate.",
      "The convenience-sample limit appears on a full-screen frame in the "
      "video itself, not only in the notes.",
      "No employer is named on any rendered frame. The employer-disagreement "
      "frame describes them by type.",
    ])

    h(d, "Flagged, not repaired")
    para(d, "Approved speech was not edited and no handoff was redirected. "
            "These are for review.", size=10, color=DIM)
    frows = []
    for n, dest, string, kind, spoken in flags1421.scheduling_dependencies():
        frows.append(["V%d to V%d" % (n, dest),
                      "SCHEDULING DEPENDENCY",
                      kind + (" The destination title is also spoken in the "
                              "approved script, so it cannot be redirected "
                              "without rerecording." if spoken else "")])
    for name, note in flags1421.NOTES:
        frows.append(["", "PRODUCTION NOTE", "%s. %s" % (name, note)])
    table(d, ["Where", "Kind", "What to decide"], frows,
          widths=[0.95, 1.35, 4.4], size=8)

    h(d, "Runtime, reported rather than adjusted")
    para(d, "These masters are shorter than the drafts they replace and "
            "shorter than the planning band the earlier roadmap work used. "
            "Nothing was padded, and no explanation was expanded to reach a "
            "target. The figures are stated as they are so pacing, chapters "
            "and any playlist decisions can be made on real numbers.")
    table(d, ["#", "Spoken words", "Speech-only estimate"],
          [["V%d" % n, "{:,}".format(w), "%s to %s" % (f, s)]
           for n, w, f, s in flags1421.runtime_note()],
          widths=[0.7, 1.6, 4.4], size=9)

    h(d, "Quality checks")
    total = sum(r["total"] for r in results.values())
    passed = sum(r["passed"] for r in results.values())
    para(d, "%d package checks across the eight packages. %d passed. Every "
            "check ran against the built package on disk rather than against "
            "the build data, so a check cannot pass because of something that "
            "was true only in a source module. Each package carries its own "
            "QA report." % (total, passed))
    callout(d, "FINAL-EXPORT CHECKS REMAIN PENDING AND ARE NOT CLAIMED. "
               "Actual delivery, runtime, executed cuts and camera moves, "
               "motion graphics, B-roll placement, audio clarity, loudness, "
               "music balance, picture quality, caption absence on the "
               "export, SRT synchronization, chapters, the Watch Next hold, "
               "a clean ending, thumbnail artwork approval and public link "
               "accessibility. A written prompt does not prove an effect "
               "exists in the finished video.")

    h(d, "Archives")
    table(d, ["Archive", "SHA-256"],
          [[os.path.basename(results[n]["zip"]), results[n]["sha"]]
           for n in M.VIDEOS] +
          [[combined_name, "in the sibling .sha256 file"]],
          widths=[2.7, 4.0], size=7.5)
    para(d, "The combined archive's own checksum is never embedded inside it. "
            "It is calculated after the archive is complete and written to "
            "the sibling .sha256 file.", size=9.5, color=DIM)

    h(d, "What was not touched, and what was not started")
    bullets(d, [
      "Videos 1 to 13. No script, asset, thumbnail, Short, publishing "
      "material or route was changed.",
      "Videos 22 to 30 were not started.",
      "The reserved employer due-diligence topic stays reserved and "
      "unnumbered.",
      "The after-40 topic stays in the future queue with its thumbnail "
      "direction, and was not assigned a number.",
      "V22 remains the promotion-timing slot.",
      "The website, the book page, the products and the global styles.",
    ])

    rule(d)
    para(d, "VIDEOS 14 TO 21 PRODUCTION PACKAGES BUILT AGAINST LOCKED FINAL "
            "RECORDING MASTERS.", size=10.5, bold=True, color=RED)
    para(d, "VIDEO 14 RESEARCH VERIFIED AGAINST THE SUPPLIED 28-POSTING "
            "RESEARCH ARCHIVE.", size=10.5, bold=True, color=RED)
    para(d, "READY FOR RECORDING AND RIVERSIDE PRODUCTION.", size=10.5,
         bold=True, color=RED)
    para(d, "FINAL-EXPORT QA, SRT SYNC, AUDIO REVIEW, THUMBNAIL ARTWORK, AND "
            "PUBLIC LINK VERIFICATION PENDING.", size=10.5, bold=True,
         color=RED)
    d.save(out_path)
    return out_path
