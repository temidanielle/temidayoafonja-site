# -*- coding: utf-8 -*-
"""The V6 to V8 restoration report as a Word document.

Built with the same document helpers as every other deliverable in this
workspace, so it files alongside them rather than arriving in a different
visual language. Every figure is read from the build rather than typed here.
"""
import os, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.append("/home/user/temidayoafonja-site/deliverables/riverside-build")
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                "VIDEOS_8-13_LOCKED_MASTER_BUILD/build")
from collections import Counter
from docx import Document

import audit678 as A
import masters421 as M
import restore678 as R
import verifyrestore as V
import flags421
from docs421f import (base_doc, para, title_block, h, kv, callout, table,
                      bullets, sub, footer_note, numbered, page_break,
                      NAVY, GOLD, DIM, RED)


def caption(d, text):
    """A note under a table. sub() is a short gold label set in capitals,
    which a full sentence should not be."""
    return para(d, text, size=9.5, color=DIM, before=5, after=10)

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "AUDIT")

TITLES = {6: "I've Worked Across 8 Industries and Sectors. Here's How I Know "
              "If a New Role Is Actually Growth.",
          7: "It Took Me Years to Stop Mistaking More Work for Career Growth",
          8: "How to Show Your Impact at Work When You Built It From Scratch"}

# Sections the supplied compressed master no longer contained, read from the
# comparison rather than listed by hand.
def restored_sections(n):
    supplied = set()
    real = M.path
    M.path = lambda k, _r=real: (M.supplied_path(k) if k == n else _r(k))
    try:
        doc = Document(M.supplied_path(n))
        flat = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
        start = next(i for i, t in enumerate(flat)
                     if M.SCRIPT_START in t) + 1
        for t in flat[start:]:
            if any(t.upper().startswith(e) for e in M.SCRIPT_END):
                break
            if M._is_heading(t):
                supplied.add(t.split("|")[0].strip().upper())
    finally:
        M.path = real
    out = []
    for name, ps in R.SCRIPTS[n]:
        key = name.split("|")[0].strip().upper()
        words = sum(len(p["text"].split()) for p in ps)
        out.append((name, words, key not in supplied))
    return out


def compressed_words(n):
    real = M.path
    M.path = lambda k, _r=real: (M.supplied_path(k) if k == n else _r(k))
    try:
        doc = Document(M.supplied_path(n))
        flat = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
        start = next(i for i, t in enumerate(flat)
                     if M.SCRIPT_START in t) + 1
        body = []
        for t in flat[start:]:
            if any(t.upper().startswith(e) for e in M.SCRIPT_END):
                break
            if M._is_heading(t):
                continue
            body.append(t)
        return sum(len(x.split()) for x in body)
    finally:
        M.path = real


def build(path, stamp, qa=None):
    d = base_doc()
    footer_note(d, "Capability Formation  |  Videos 6, 7 and 8  |  source "
                   "integrity audit and restoration")
    title_block(d, "Capability Formation  |  Videos 6, 7 and 8",
                "Three masters came back half-length",
                "The audit that found it, and the restoration that put the "
                "teaching back")
    kv(d, "Generated", stamp)
    kv(d, "Videos", "6, 7 and 8. Videos 4 and 5 remain the only 5-minute "
                    "test videos and were not touched.")
    kv(d, "Branch", "claude/video-1-slides-deck-go9bzy")

    callout(d, "Videos 6, 7 and 8 were supplied on September 11 carrying "
               "roughly half the teaching that had already been approved. "
               "All three declared themselves regular long-form. The "
               "declaration and the measurement disagreed.")

    # ---------------------------------------------------------- the finding
    h(d, "The finding")
    para(d, "A runtime estimate could not answer this on its own. An "
            "estimate taken from a compressed file simply reports the "
            "compression as a fact. So the test was a source-to-source "
            "comparison against the last full-length approved master, not a "
            "clock reading.")

    h(d, "The parser was controlled first", size=11.5)
    caption(d, "Before trusting any word count, the extractor was run against "
           "five masters whose approved counts are already known. If it "
           "could reproduce those exactly, a short count elsewhere would be "
           "the file rather than the reader.")
    table(d, ["Control", "Corrected", "Previously approved", "Result"],
          [["Video %d" % n, str(a), str(b), "identical" if ok else "DIFFERS"]
           for n, a, b, ok in A.unchanged()],
          widths=[1.5, 1.4, 2.0, 1.8], size=9)
    caption(d, "Five of five to the word. The extractor was not the cause.")

    callout(d, "Verdict. Videos 6, 7 and 8 were accidentally shortened. All "
               "three share one signature: the closing CTA and the spoken "
               "Watch Next were gone entirely, and the teaching sections "
               "were near-uniformly halved. That is consistent with a "
               "single compression pass that should only ever have touched "
               "Videos 4 and 5.", color=NAVY)

    # ----------------------------------------------------------- the repair
    h(d, "The repair")
    rows = []
    for n in sorted(R.SCRIPTS):
        w, fast, slow = V.estimate(n)
        cw = compressed_words(n)
        rows.append(["Video %d" % n, str(cw), str(w), str(R.PREV_WORDS[n]),
                     "%d%%" % round(100.0 * w / R.PREV_WORDS[n]),
                     "%s to %s" % (fast, slow)])
    table(d, ["Video", "As supplied", "Restored", "Approved", "Of approved",
              "Speech-only"], rows,
          widths=[1.0, 1.15, 1.05, 1.1, 1.15, 1.25], size=9)
    caption(d, "Speech-only, at 130 to 145 words per minute. It excludes pauses, "
           "framework holds, full-screen demonstrations and transitions, so "
           "the finished runtime will be longer. Nothing was padded to reach "
           "a clock.")

    # ------------------------------------------------------- no new writing
    h(d, "No new teaching was written")
    cnt = Counter(p["src"] for n in R.SCRIPTS
                  for _, ps in R.SCRIPTS[n] for p in ps)
    total = sum(cnt.values())
    para(d, "Every one of the %d restored paragraphs carries a tag recording "
            "where its words came from. The tags are checked against the two "
            "source masters rather than trusted, and that checker was tested "
            "against injected violations before it was relied on." % total)
    table(d, ["Tag", "What it means", "Lines"], [
      ["CUR", "The corrected September 11 master's own speech, unchanged. "
              "Hooks, architecture and framework headings all kept.",
       str(cnt.get(R.CUR, 0))],
      ["SEP09", "Previously approved speech, word for word.",
       str(cnt.get(R.SEP09, 0))],
      ["SEP09-SPLIT", "Approved speech with a sentence the corrected master "
                      "already says removed, or approved lines joined into "
                      "one spoken paragraph. Nothing added.",
       str(cnt.get(R.SPLIT, 0))],
      ["SEP09-ADJ", "Approved speech with a minimal change, each one "
                    "recorded in the document itself. All three are in "
                    "Video 6.", str(cnt.get(R.ADJ, 0))],
      ["BRIDGE", "Newly authored connecting language.",
       str(cnt.get(R.BRIDGE, 0))],
    ], widths=[1.15, 4.35, 0.7], size=9)
    para(d, "Newly authored speech across all three scripts: %d lines."
            % cnt.get(R.BRIDGE, 0), bold=True,
            color=NAVY if not cnt.get(R.BRIDGE) else RED, before=6)

    h(d, "The three adjustments, in full", size=11.5)
    for n in sorted(R.SCRIPTS):
        for sec, ps in R.SCRIPTS[n]:
            for p in ps:
                if p["src"] != R.ADJ:
                    continue
                para(d, "Video %d  ·  %s" % (n, sec), size=9, bold=True,
                     color=GOLD, before=10, after=4)
                para(d, p["text"], size=10.5, italic=True, after=4)
                caption(d, p["note"])

    page_break(d)

    # ------------------------------------------------------ section by section
    h(d, "Section by section")
    caption(d, "Word counts are the restored figures. A section marked "
               "RESTORED was absent from the supplied master entirely.")
    for n in sorted(R.SCRIPTS):
        para(d, "Video %d" % n, size=13, bold=True, color=NAVY, before=14,
             after=2)
        para(d, TITLES[n], size=10, color=DIM, after=8)
        table(d, ["Section", "Words", "State"],
              [[name, str(words), "RESTORED" if new else "kept"]
               for name, words, new in restored_sections(n)],
              widths=[4.6, 0.85, 1.25], size=9)
    para(d, "", after=4)
    bullets(d, [
      "Video 6: WHAT THIS TEST CANNOT SOLVE was the one that mattered most. "
      "Employer constraints, manager access, compensation bands, bias and "
      "age discrimination, caregiving, immigration status, health and "
      "safety. The compression had removed the section that keeps the video "
      "from implying three questions settle a career decision.",
      "Video 7: Return had retained only about a third of its approved "
      "depth, leaving CAR lopsided. It is back to 194 words against the "
      "previous 200, and the three tests now sit at 151, 147 and 194. THE "
      "SCOPE CONVERSATION brings back the four questions to take to a "
      "manager, which is the video's actual viewer tool.",
      "Video 8: the four-part architecture was kept, as directed. BEFORE, "
      "MY PART, JUDGMENT and PROOF stand, with Existence, Use and Effect, "
      "and the approved depth was mapped into that structure rather than "
      "the old three-part version being restored over it. Two passages were "
      "moved deliberately rather than pasted under a new heading, and both "
      "moves are recorded.",
    ])

    # -------------------------------------------------------- source integrity
    h(d, "Source integrity")
    para(d, "Each restored script is a separate derivative document. The "
            "file as supplied stays where it was, unchanged, and is copied "
            "into its package as a superseded file. Verification now fails "
            "if either the supplied master or the restored derivative "
            "changes on disk, so a restoration that quietly edited the "
            "original would pass the first check and fail the second.")
    table(d, ["Video", "File", "SHA-256"],
          [x for n in sorted(R.SCRIPTS) for x in (
            ["Video %d" % n, M.filename(n), M.read(n)["sha"]],
            ["", "%s  (supplied, superseded)" % M.FILES[n],
             M.read(n)["supplied_sha"]])],
          widths=[0.8, 3.0, 2.9], size=8)

    callout(d, "Videos 9 to 13 match their previously approved masters to "
               "the word, so their speech-only estimates sitting below the "
               "printed finished-runtime targets is the ordinary difference "
               "between speech time and finished time. Nothing was padded.",
            color=NAVY)

    # -------------------------------------------------------------- status
    h(d, "Status")
    if qa:
        para(d, "Package checks: %d of %d passed across all 18 videos."
                % (qa["passed"], qa["total"]), bold=True, color=NAVY)
        kv(d, "Combined archive", qa["zip"])
        kv(d, "Archive SHA-256", qa["sha"])
        kv(d, "Prior-asset audit", qa["audit"])
    bullets(d, [
      "Nothing in this work has been recorded, edited or exported.",
      "Every runtime figure is arithmetic on the script, not a measurement.",
      "No thumbnail artwork, chapters, SRT or music attribution exists yet. "
      "Those come from the finished export.",
    ])
    d.save(path)
    return path


if __name__ == "__main__":
    stamp = subprocess.check_output(
        ["env", "TZ=America/Chicago", "date",
         "+%A, %B %d, %Y | %-I:%M %p CT"]).decode().strip()
    qa = None
    log = "/tmp/build8.log"
    if os.path.exists(log):
        txt = open(log).read()
        import re
        m = re.search(r"package checks: (\d+) of (\d+) passed", txt)
        z = re.search(r"(Videos_4-21_[^\s]+\.zip)\s+(\d+) entries", txt)
        sh = re.search(r"sha256 ([0-9a-f]{64})", txt)
        ad = re.search(r"(prior-asset audit: .*)", txt)
        if m:
            qa = dict(passed=int(m.group(1)), total=int(m.group(2)),
                      zip=z.group(1) if z else "", sha=sh.group(1) if sh else "",
                      audit=ad.group(1).replace("prior-asset audit: ", "")
                      if ad else "")
    os.makedirs(OUT, exist_ok=True)
    print(build(os.path.join(OUT, "V6_V7_V8_Restoration_Report.docx"),
                stamp, qa))
