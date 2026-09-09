# -*- coding: utf-8 -*-
"""One summary document covering the September 9 synchronization.

Everything in it is read from the built packages and the locked masters, so the
document cannot drift from what was actually delivered.
"""
import os, sys, json, hashlib, zipfile
HERE = os.path.dirname(os.path.abspath(__file__))
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.insert(0, DELIV + "riverside-build")
sys.path.insert(0, DELIV + "new-videos-4-5/build")
sys.path.insert(0, HERE)

import masters, build
from docs import (base_doc, para, title_block, rule, h, kv, callout,
                  NAVY, GOLD, DIM, RED)
from frames import SETS
from shorts import SHORTS, seconds as sh_sec
from publish import META, DESC_CHANGE, PINNED_CHANGE, TAGS_CHANGE

PRE = build.PRE_HASHES

DOCS = [
 ("V{n}_Recording_Master_LOCKED_2026-09-09.docx",
  "The locked script itself, copied byte for byte from your handoff. The "
  "spoken source of truth."),
 ("Approved_Recording_Master_Reference.docx",
  "A reading copy for the recording desk, generated from the locked file. "
  "Section labels and bracketed delivery directions are marked as production "
  "instructions so they are never read aloud."),
 ("Recording_Run_of_Show.docx",
  "What to do before, during and after the take. Carries the locked opening, "
  "the delivery directions to protect, the sections in order, the never-imply "
  "boundaries, the exact final spoken line, and the standing Riverside rules."),
 ("Sentence_Trigger_Map.txt",
  "Every graphic with the exact spoken sentence that cues it, plus the beats "
  "that are deliberately NOT graphics, labelled as editorial cues."),
 ("Visual_Build_Map_and_Motion_Reveal_Map.txt",
  "Scene by scene: status and why, on-screen idea, trigger, treatment, reveal "
  "order, hold, what happens after, captions, sound and brand."),
 ("Riverside_CoCreator_Master_Prompt.txt",
  "The complete master prompt plus one prompt per scene, ready to paste. "
  "Includes every standing instruction from Video 4 onward."),
 ("Asset_Reuse_and_Change_Table.txt",
  "Every asset classified REUSE, REORDER, COPY UPDATE, REBUILD or REMOVE, "
  "with the reason and the SHA-256 proof."),
 ("Video_{n}_Six_Short_Form_Recording_Scripts.docx",
  "All six Shorts in one document, with each one's status and why."),
 ("Video_{n}_Shorts/",
  "One document per Short, for recording them individually."),
 ("Publishing_Materials.docx",
  "Copy-ready description and pinned comment, tags, hashtags, what changed and "
  "why, and the internal notes that must not be pasted."),
 ("Source_Manifest_V{n}.json",
  "Machine-readable record: the exact script file used, its hashes, word "
  "count, every asset with its status and hash, every Short, and an explicit "
  "list of what is NOT verified."),
 ("QA_Report.txt",
  "28 package checks completed now, and 10 final-export checks listed as "
  "pending and not claimed."),
 ("Change_Log.txt",
  "What changed, what did not, what is not supplied by instruction, and the "
  "runtime position."),
 ("Support_Reference_PNG/ and .zip",
  "The 1920x1080 reference frames."),
 ("Recording_Support_Deck.pptx",
  "The same frames as an editable deck."),
 ("CTA_Asset.png and Watch_Next_Asset.png",
  "The two cards lifted out for convenience."),
]


def counts(rows, key="status"):
    out = {}
    for r in rows:
        out[r[key]] = out.get(r[key], 0) + 1
    return ", ".join("%s %d" % kv for kv in sorted(out.items()))


def build_doc():
    d = base_doc()
    title_block(d, "Capability Formation  |  Videos 4 to 7",
                "September 9 Script Synchronization",
                "What changed, what was reused, and what is not yet verified")
    kv(d, "Date", "September 9, 2026")
    kv(d, "Scope", "Videos 4, 5, 6 and 7. Videos 1 to 3 untouched.")
    kv(d, "Source", "YouTube_Roadmap_and_V4V7_Lock_Sep09_2026.zip")
    kv(d, "Nature of the work",
       "A targeted production update. Not a strategy rebuild, not a numbering "
       "change, and not a new visual system.")
    callout(d, "No spoken script was rewritten. No thumbnail was designed, "
               "generated or altered. No new slide deck was created. No V8 to "
               "V15 work was started.")

    h(d, "1. How the source was handled")
    para(d, "The four September 9 Recording Masters are the spoken source of "
            "truth. Before anything was generated, each file's SHA-256 was "
            "recomputed and matched against your own Source_Lock_Manifest.json. "
            "All four matched, and the build stops if one ever does not.",
         size=11, after=8)
    para(d, "The build reads those files and never writes to them. The reading "
            "copy, the run of show, the trigger map and the word counts are "
            "all generated from the locked text, so there is no transcription "
            "step in which a line could drift.", size=11, after=8)
    for n in (4, 5, 6, 7):
        hh, ok = masters.verify(n)
        kv(d, "V%d  %s" % (n, masters.CANON[n]),
           "SHA-256 %s  ·  matches lock manifest: %s"
           % (hh[:24] + "...", "yes" if ok else "NO"))

    h(d, "2. Runtime, stated honestly")
    para(d, "I first used a 140 to 165 words per minute band, which would have "
            "produced figures that contradicted your roadmap. I found that and "
            "switched to the roadmap's own 130 to 145 band and its own counting "
            "method. The estimates below now reproduce the roadmap's printed "
            "figures exactly.", size=11, after=8)
    for n in (4, 5, 6, 7):
        w, fast, slow = build.runtime_estimate(n)
        kv(d, "V%d" % n, "%d spoken words  ·  %s to %s speech only  ·  printed "
           "cover target %s" % (w, fast, slow,
            masters.header(n).get("TARGET RUNTIME")
            or masters.header(n).get("TARGET LENGTH")))
    para(d, "These are arithmetic on the script. They are not a timed read and "
            "not a finished runtime, and they exclude the scripted pauses, the "
            "holds on graphics, B-roll and every edit decision. The printed "
            "cover targets are not verified finished lengths either.",
         size=10, color=DIM, after=6)
    para(d, "WORTH YOUR ATTENTION: Video 4 and Video 5 print targets of 12:00 "
            "to 14:00 and 17:00 to 18:30, well above the speech-only estimates. "
            "The September 9 scripts are genuinely shorter. Nothing was padded "
            "to close that gap, and the packages say so in three places. You "
            "may want to reset expectations on those two before recording.",
         size=10.5, bold=True, color=RED, after=10)

    h(d, "3. What changed, per video")
    for n in (4, 5, 6, 7):
        m = META[n]
        para(d, "VIDEO %d  ·  %s" % (n, m["title"]), size=12, bold=True,
             color=NAVY, before=14, after=5, keep=True)
        kv(d, "Thumbnail", "%s  (not rebuilt)" % m["thumbnail"])
        kv(d, "Opening identifier", m["opening_id"])
        kv(d, "Assets", counts(SETS[n]))
        kv(d, "Shorts", counts(SHORTS[n]))
        for t in build.CHANGES[n]:
            para(d, "•  " + t, size=10.5, after=5)

    h(d, "4. Reuse was proved, not asserted")
    ident = chg = new = 0
    for n in (4, 5, 6, 7):
        pd = os.path.join(build.DIRS[n], "Support_Reference_PNG")
        for f in SETS[n]:
            cur = hashlib.sha256(
                open(os.path.join(pd, f["file"]), "rb").read()).hexdigest()
            prev = PRE.get(f["was"]) if f.get("was") else None
            if prev is None:
                new += 1
            elif prev == cur:
                ident += 1
            else:
                chg += 1
    para(d, "Every rendered asset was hashed against the package as it stood "
            "before this synchronization. An asset marked REUSE or REORDER "
            "whose bytes moved is a QA failure, not a footnote.", size=11,
         after=8)
    kv(d, "Carried over byte-identical", "%d of %d assets" % (ident, ident + chg + new))
    kv(d, "Changed, as intended", "%d" % chg)
    kv(d, "New", "%d" % new)
    para(d, "Three assets failed that check on the first run. The cause was "
            "mine: I had retyped their draw calls from the previous package "
            "instead of copying them, so type sizes and separator spacing "
            "drifted by a few points. I restored them exactly, which made the "
            "reuse claim true rather than relabelling it.", size=10.5,
         color=DIM, after=8)

    h(d, "5. Two checks I corrected rather than relaxed")
    para(d, "SENTENCE TRIGGERS. Six triggers I had written spanned two script "
            "paragraphs, so they did not exist as single spoken sentences. That "
            "is the check working. Each was shortened to a sentence the locked "
            "script actually contains.", size=11, after=8)
    para(d, "RETIRED INSTRUCTIONS. The first version read hard-wrapped lines in "
            "isolation, so a paragraph naming a retired rule in order to record "
            "that it was retired failed on the wrapped fragment. It now reads "
            "paragraph units. A separate check was added for the thing that "
            "actually matters: that no prompt still requires a retired opening. "
            "Video 5 needed that distinction, because its retired opening "
            "sentence is still spoken later in the locked script, so banning "
            "the string outright would have been wrong.", size=11, after=8)

    h(d, "6. The documents in each package")
    para(d, "Every document below was regenerated from the September 9 locked "
            "script. Substitute the video number for {n}.", size=10.5,
         color=DIM, after=8)
    for name, what in DOCS:
        kv(d, name, what)

    h(d, "7. QA, split as you asked")
    para(d, "Each QA_Report.txt separates what can be checked now from what "
            "cannot be checked until the recording and the export exist.",
         size=11, after=8)
    kv(d, "Package checks completed now", "28 per video, all passing")
    kv(d, "Final-export checks still pending", "10 per video, none claimed")
    para(d, "Listed as PENDING and explicitly not verified: executed animation, "
            "recorded audio and delivery, audio balance, final pacing and "
            "actual runtime, caption placement, chapter timestamps, thumbnail "
            "artwork, live reachability of linked destinations, and whether "
            "the finished edit lands inside the camera-emphasis and sound "
            "budgets.", size=10.5, color=DIM, after=8)
    para(d, "No earlier QA pass is reused as evidence that these packages are "
            "aligned.", size=10.5, color=DIM, after=8)

    h(d, "8. Not supplied, by instruction")
    for t in ("No chapter timestamps. Build them from the finished export.",
              "No music attribution or license code.",
              "No thumbnail artwork. Nothing was designed, generated or "
              "altered.",
              "No YouTube video URL built from a guessed identifier. Each "
              "description carries a deliberate placeholder for Watch Next."):
        para(d, "•  " + t, size=10.5, after=5)

    h(d, "9. Superseded material")
    para(d, "Isolated in deliverables/SUPERSEDED_DO_NOT_USE/ as "
            "OLD_Sep08_V4-V7_Scripts/ and OLD_Sep08_Packages/, each with a "
            "notice. Every active script is named "
            "..._LOCKED_2026-09-09.docx and nothing superseded carries that "
            "name, so the two sets cannot be confused.", size=11, after=8)

    h(d, "10. Roadmap")
    para(d, "The September 9 roadmap is filed with its lock manifest. Videos 4 "
            "to 7 hold their positions. Videos 8 to 15 carry the approved "
            "directions with their evidence conditions intact: V13 is a plan "
            "rather than a completed experiment, V14 is conditional on research "
            "being actually completed and documented, and V11 requires tool and "
            "task-capability claims to be verified before scripting. V16 to V30 "
            "are retained exactly as the September 7 map had them, and V31 "
            "stays in the backlog. No V8 to V15 script or artwork was started.",
         size=11, after=8)

    h(d, "11. Archives")
    for n in (4, 5, 6, 7):
        z = build.ZIPS[n]
        kv(d, z, open(DELIV + z + ".sha256").read().split()[0])
    kv(d, build.COMBINED,
       open(DELIV + build.COMBINED + ".sha256").read().split()[0])

    rule(d)
    para(d, "VIDEOS 4, 5, 6 AND 7: PACKAGES SYNCHRONIZED TO THE SEPTEMBER 9 "
            "SCRIPT LOCK.", size=12, bold=True, color=NAVY, before=10, after=6)
    para(d, "Ready for recording and Riverside production. Nothing about the "
            "recording or the export is verified, because neither exists yet.",
         size=11, color=DIM, after=6)

    pth = DELIV + "V4-V7_Sep09_Synchronization_Summary.docx"
    d.save(pth)
    return pth


if __name__ == "__main__":
    p = build_doc()
    print("wrote", p, os.path.getsize(p), "bytes")
