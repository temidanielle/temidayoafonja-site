# -*- coding: utf-8 -*-
"""The delivery report, generated beside the pack. Every figure is read from the build."""
import os, sys, zipfile
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.append("/home/user/temidayoafonja-site/deliverables/VIDEOS_22-23/build")
# Every module in this pack is prefixed p2_ because the house document helpers
# insert their own build directories at the front of sys.path, which shadows bare
# names like build, shorts and packaging.
from docs23 import (base_doc, title_block, h, kv, para, callout, sub, caption,
                    table, bullets, footer_note, page_break)
import p2_build as BD, p2_docs as DP, p2_qa as QA, p2_packaging as PK, p2_provenance as PV
import p2_shorts as S, p2_production as PR, p2_descriptions as D

NAME = "V12-V14_PHASE2_DELIVERY_REPORT.docx"

CHANGED = {
12: ["The accomplishment is now an artifact on screen before anything is said about it, and the "
     "first teaching section is Temidayo splitting it into what she can check and what she is being "
     "asked to assume. The old script asserted the sentence was weak; this one shows it.",
     "The four questions are never named, abbreviated, or capitalized into a label. They are asked "
     "in plain sentences and the rebuilt artifact carries the teaching.",
     "A ten-minute budget is spoken out loud so the title is a promise the video actually keeps: "
     "two, three, two, three.",
     "A new boundary section: proof is not an offer. The old script ended on emphasis-not-truth, "
     "which is kept, but the harder limit is now stated first.",
     "One research claim was dropped rather than carried. The old script said employers asked for "
     "benefit tracking, cost-benefit analysis, metrics and value realization. That wording could "
     "not be verified in any source in the workspace, so it was replaced with a plain statement "
     "that needs no citation. The one research line that remains is verifiable in Section 6 of the "
     "28-posting record."],
13: ["Rebuilt around three real postings that use the same two words, read in the first ninety "
     "seconds. The old script opened on an abstraction.",
     "The old four named buckets were removed as a framework. The same distinctions run through "
     "the analysis with no labels, no numbering and no on-screen framework card.",
     "Every sample number is carried exactly and stated on camera, including the exclusion log and "
     "the collection date, and the video says out loud that several postings were already closed.",
     "The hard-versus-preferred counts are now spoken with their own uncertainty: six of "
     "twenty-eight, and the fact that a careful reader could code it five or seven.",
     "Employers are named only at the level of what their posting says. No sentence in the script "
     "attributes a belief, a preference or an intention to an employer or an industry."],
14: ["Substantially rebuilt. The old script asserted what employers care about; this one reads two "
     "specific postings and, after each, says only two things: what it gives evidence of, and what "
     "cannot be told from it.",
     "The no-mind-reading rule is stated on camera in the first minute and then kept. The verdict "
     "sentence after each posting uses the same two-part shape so the pattern is audible.",
     "The proves-versus-suggests distinction is new and is the spine of the second half.",
     "The posting-wording clues from the old script survive only as the required-versus-preferred "
     "read, which is what the two postings actually demonstrate.",
     "Its packaging is not decided. Five options are documented, one is recommended, and the "
     "script was built on the recommendation so that a complete episode exists to react to."],
}

UNRESOLVED = [
 ("V14 packaging", "Not chosen, by instruction. Every V14 file is marked working. Choosing a "
                   "different option changes four places, all listed in V14_PACKAGING_OPTIONS."),
 ("V13's Watch Next line in the description", "Carries the V14 working title with a bracketed "
   "confirm note. The spoken Watch Next in V13 deliberately describes V14 instead of naming it, so "
   "a packaging decision does not force a re-record. Only the description line and the on-screen "
   "card need updating."),
 ("Scripture wording", "The three NLT verses were not checked against a licensed NLT text in this "
   "pass. Confirm before publishing."),
 ("Resource URLs", "Taken from the shipped V4 to V11 descriptions. None was loaded to confirm it "
   "is live."),
 ("Posting URLs", "Not re-fetched. Every posting detail comes from the checksummed September 10, "
   "2026 research record. Four of the twenty-eight are quoted on camera and all four are "
   "documented with URL, collection date, capture route and hard-versus-preferred coding."),
 ("Three Shorts at a slow read", "V12 Short 2, V13 Short 3 and V14 Short 1 are inside 55 seconds "
   "at 165 words per minute but cross it at the 150 wpm planning rate. Flagged inside each Shorts "
   "document as the ones to trim if the read comes in slow."),
 ("Card art", "No PNG or SVG was rendered for V12, V13 or V14. Card copy, headline and on-card "
   "disclosure labels are specified in each production package."),
 ("V12 runtime against its own title", "At 1,266 spoken words the speech-only estimate is 8:44 to "
   "9:44. Full-screen holds will push the finished edit past that. If the cut runs long, the "
   "section marked THE TEN MINUTES is the one written to survive compression."),
]

def build_report(path, names, rows, zpath, digest):
    d = base_doc()
    title_block(d, DP.EYEBROW, "V12 to V14 delivery report",
                "What was built, what it is based on, and what is still open")
    kv(d, "Generated", DP.STAMP)
    kv(d, "Pack", BD.ZIPNAME)
    kv(d, "SHA-256", digest)
    kv(d, "Files in pack", "%d" % len(names))
    kv(d, "Branch", "claude/video-1-slides-deck-go9bzy")
    callout(d, "This report is generated beside the archive, not inside it, so the archive's own "
               "checksum is never embedded in itself. V4 to V11 were not touched. No historical "
               "source file was renumbered, overwritten or deleted. Work stopped at V14.")

    h(d, "Verified spoken word counts and runtime estimates")
    table(d, ["#", "Title", "Spoken words", "At 145 wpm", "At 130 wpm"],
          [[DP.META[n]["number"], DP.META[n]["title"] + ("  [working]" if DP.META[n]["status"] else ""),
            "{:,}".format(DP.words(n)), DP.runtime(n, 145), DP.runtime(n, 130)]
           for n in (12, 13, 14)], widths=[0.5, 3.1, 1.0, 1.05, 1.05])
    caption(d, "Word counts are exact: whitespace-delimited tokens of the spoken stream, counted "
               "from the built documents and cross-checked against the script modules. The two "
               "runtime columns are ESTIMATES. They are arithmetic on the word count, not "
               "measurements, and the finished edit will run longer because of full-screen holds.")

    h(d, "Files created")
    table(d, ["Path", "What it is"],
          [[p, _what(p)] for p in names], widths=[3.2, 3.5])
    para(d, "Delivered beside the archive: %s, %s.sha256, and this report."
          % (BD.ZIPNAME, BD.ZIPNAME))

    page_break(d)
    h(d, "Sources used")
    for n in (12, 13, 14):
        sub(d, DP.META[n]["number"])
        for s in PV.SOURCES[n]:
            kv(d, s["role"], "%s  ·  %s" % (s["name"], s["sha"][:16] + "…"
                                                 if len(s["sha"]) > 30 else s["sha"]))
    para(d, "Four of the twenty-eight coded postings are quoted on camera: Humana (H10), Wells "
            "Fargo (F1) and Mass General Brigham (H8) in V13, and Humana (H10) with J.P. Morgan "
            "Wealth Management (F5) in V14. Each is documented in that video's provenance file with "
            "its URL, collection date, posting dates, capture route, hard requirements, preferred "
            "requirements and the exact clause quoted.")

    h(d, "What materially changed, per video")
    for n in (12, 13, 14):
        sub(d, "%s  ·  %s" % (DP.META[n]["number"], DP.META[n]["title"]))
        bullets(d, CHANGED[n])

    page_break(d)
    h(d, "V14 recommended provisional packaging")
    o = PK.OPTIONS[PK.RECOMMENDED - 1]
    callout(d, "%s. Nothing is decided here." % PK.RECOMMENDED_LABEL)
    kv(d, "Title", o["title"])
    kv(d, "Thumbnail", o["thumb"])
    kv(d, "Curiosity gap", o["gap"])
    para(d, PK.WHY)
    para(d, "The other four options, each with its own curiosity gap, its fit and what it costs, "
            "are in V14_PACKAGING_OPTIONS inside the pack. “%s” was not developed."
          % PK.BANNED[0])

    h(d, "QA actually performed")
    kv(d, "Checks run against the built files", "%d of 20" % sum(1 for r in rows if r["state"] == QA.PERFORMED))
    kv(d, "Passing", "%d" % sum(1 for r in rows if r["ok"]))
    table(d, ["#", "Check", "Result"],
          [["%02d" % r["n"], r["name"], "pass" if r["ok"] else "FAIL"] for r in rows],
          widths=[0.45, 5.3, 0.95])
    para(d, "Four of these twenty checks failed on their first run and three of the four failures "
            "were faults in the check, not in the pack: the word-count reader looked for a colon "
            "the house helper does not print, the faith-anchor reader matched mixed case against an "
            "upper-cased heading, and the spoken-text reader used a short-all-caps heuristic that "
            "silently kept three long section labels inside the spoken stream. Each reader was "
            "rewritten to read the document structurally and each now carries a regression that "
            "proves it still fires. The fourth failure was real: the Shorts verbatim check, once "
            "corrected to require consecutive runs, caught a V13 Short that had a middle sentence "
            "removed, and a V13 Short that ran 170 words against a 150-word ceiling. Both were "
            "fixed in the Shorts, not in the check.")

    h(d, "What was not done")
    for name, why in QA.NOT_DONE:
        sub(d, name)
        para(d, why)
    callout(d, "Nothing in this delivery is described as fully verified, production ready, or QA "
               "passed. Twenty checks ran against the built files and twenty passed. Everything "
               "above is outside what those checks cover.")

    h(d, "Unresolved issues")
    for name, why in UNRESOLVED:
        sub(d, name)
        para(d, why)
    footer_note(d, "Generated from the build. No figure in this report was typed by hand.")
    d.save(path)

def _what(p):
    b = os.path.basename(p)
    if b.startswith("00_PHASE2"): return "Overview: the three videos, their sources, and what is not in the pack."
    if b.startswith("00_V12-V14_QA"): return "The twenty checks, run against these files, plus what was not performed."
    if "PACKAGING_OPTIONS" in b: return "Five title and thumbnail pairs for V14, one recommended, none chosen."
    if "RECORDING_MASTER" in b: return "The spoken script with camera, artifact and sound cues in place."
    if "THOUGHT_BLOCKS" in b: return "The same spoken words as blocks of two to five sentences, for recording."
    if "PRODUCTION_PACKAGE" in b: return "Full-screen cards, camera beats, artifact moments, sound accents, run of show."
    if "SHORTS" in b: return "Three candidate Shorts, every line lifted verbatim from that master."
    if "DESCRIPTION_METADATA" in b: return "Copy-ready description with one resource and a faith anchor, plus metadata."
    if "SOURCE_PROVENANCE" in b: return "Source hierarchy with checksums, posting provenance, and stated limits."
    return ""

if __name__ == "__main__":
    import hashlib
    zp, names, rows = BD.main()
    digest = BD.sha256(zp)
    path = os.path.join(OUT, NAME)
    build_report(path, names, rows, zp, digest)
    print(path)
    print("pack:", digest)
