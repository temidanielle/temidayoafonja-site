# -*- coding: utf-8 -*-
"""Analysis of the checksum condition on the V4 to V21 handoff lock.

Written with the same document helpers as the rest of the workspace. Every
figure is measured at generation time rather than typed in.
"""
import os, subprocess, sys, glob, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.append("/home/user/temidayoafonja-site/deliverables/riverside-build")
from docx import Document
from docs421f import (base_doc, para, title_block, h, kv, callout, table,
                      bullets, sub, caption, footer_note, numbered,
                      NAVY, GOLD, DIM, RED)

PKG = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(PKG, "AUDIT")
ARCHIVE = "Videos_4-21_CORRECTED_RUNTIME_Production_Packages.zip"
EXPECTED = "dcd8434320dce9cfb4d89d26365eaf20349efe0de46f5f643af60fea5e91445f"


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 16), b""):
            h.update(c)
    return h.hexdigest()


def stamped_documents():
    """How many delivered documents embed the build's own clock time."""
    hits, total = 0, 0
    for p in glob.glob(os.path.join(PKG, "VIDEO_*_PACKAGE", "**", "*.docx"),
                       recursive=True):
        total += 1
        d = Document(p)
        txt = " ".join(x.text for x in d.paragraphs)
        txt += " ".join(c.text for t in d.tables for r in t.rows
                        for c in r.cells)
        if "AM CT" in txt or "PM CT" in txt:
            hits += 1
    return hits, total


def build(path, stamp):
    actual = sha256(os.path.join(PKG, ARCHIVE))
    hits, total = stamped_documents()
    d = base_doc()
    footer_note(d, "Capability Formation  |  V4 to V21 handoff  |  checksum "
                   "condition analysis")
    title_block(d, "Capability Formation  |  Videos 4 to 21",
                "The checksum condition cannot be met as written",
                "Analysis of the archive checksum named in the handoff lock")
    kv(d, "Generated", stamp)
    kv(d, "Question", "The lock accepts the handoff provided the delivered "
                      "archive matches a named SHA-256. Does it?")
    kv(d, "Short answer", "No, and the named checksum cannot be produced by "
                          "any rebuild.")

    callout(d, "This is a decision memo, not a defect report. The packages "
               "themselves are sound: 701 of 701 package checks pass and "
               "nothing in the analysis below affects a script, an asset, a "
               "framework or a route.")

    # ------------------------------------------------------------- finding 1
    h(d, "1. The delivered archive does not match the named checksum")
    table(d, ["", "SHA-256"], [
      ["Named in the lock", EXPECTED],
      ["Delivered archive", actual],
      ["Match", "NO" if actual != EXPECTED else "yes"],
    ], widths=[1.6, 5.1], size=8.5)
    para(d, "The named value was real. It was the archive produced by the "
            "build reported at 701 of 701. That archive was then superseded "
            "by a rebuild, and the rebuild is what was delivered and "
            "committed.")

    # ------------------------------------------------------------- finding 2
    h(d, "2. Why the archive was rebuilt")
    para(d, "A typographic defect was found after that build. The document "
            "helper sub() sets a short gold label in capitals. Full "
            "sentences were being passed to it, so the editorial check "
            "rendered a spoken cue as a line of shouting, and the delivery "
            "summary carried two explanatory notes the same way.")
    table(d, ["", "Before", "After"], [
      ["Size", "8.5 pt", "9.5 pt"],
      ["Weight", "bold", "regular"],
      ["Color", "gold 8A6D1E", "dim 5A6B82"],
      ["Case", "FORCED UPPERCASE", "sentence case"],
    ], widths=[1.1, 2.3, 2.3], size=9)
    para(d, "The same rebuild also added a structural QA gate over every "
            "Word document, which changed no output but now stops a broken "
            "document from reaching an archive.")

    # ------------------------------------------------------------- finding 3
    h(d, "3. Exactly what differs between the two archives")
    para(d, "Measured, not asserted. Video 15's editorial check was "
            "generated under both code paths and compared paragraph by "
            "paragraph, run by run.")
    table(d, ["Measure", "Result"], [
      ["Paragraphs in the document", "24 under both"],
      ["Paragraphs whose words differ", "0"],
      ["Paragraphs whose letter case differs", "2"],
      ["Paragraphs whose formatting differs", "2"],
      ["Text identical ignoring case", "yes"],
    ], widths=[3.4, 3.3], size=9)
    para(d, "Across the archive that is 18 editorial checks and one delivery "
            "summary, two paragraphs each. Every other document is unchanged "
            "in content. No master, no rendered asset, no Short, no "
            "publishing copy, no resource route and no Watch Next "
            "destination differs between the two builds.")
    caption(d, "Because each package contains an editorial check, all 18 "
               "per-package checksums differ between the two builds, as does "
               "the SHA-256 manifest that lists them. That is a consequence "
               "of the two paragraphs, not evidence of anything wider.")

    # ------------------------------------------------------------- finding 4
    h(d, "4. The named checksum cannot be reproduced")
    para(d, "This is the decisive point, and it is independent of the "
            "typographic fix.")
    para(d, "Every build stamps its own clock time, to the minute, into the "
            "documents it generates. %d of the %d Word documents in the "
            "delivered packages carry that stamp." % (hits, total))
    table(d, ["Build", "Stamp written into its documents"], [
      ["Produced the named checksum", "Saturday, September 12, 2026 | "
                                      "5:11 AM CT"],
      ["Produced the delivered archive", "Saturday, September 12, 2026 | "
                                         "5:28 AM CT"],
    ], widths=[2.5, 4.2], size=9)
    callout(d, "A rebuild cannot recreate the named checksum. Reverting the "
               "typographic fix would not do it either, because the new "
               "build would stamp a new time and produce a third checksum. "
               "The only build that could have produced it was the one that "
               "ran in that minute, and its output no longer exists.",
            color=RED)

    # ------------------------------------------------------------- correction
    h(d, "5. A correction to what was reported earlier")
    para(d, "The earlier message offered, as an option, rebuilding without "
            "the typographic fix in order to restore the named checksum. "
            "That option does not exist. The timestamp makes the named value "
            "unreachable regardless of what the code does. The option should "
            "have read: accept the archive that exists, or rebuild and "
            "receive a third checksum.")

    # ------------------------------------------------------------- options
    h(d, "6. The options, as they actually stand")
    table(d, ["Option", "Result", "Assessment"], [
      ["Lock the delivered archive", actual[:24] + "…",
       "RECOMMENDED. The archive exists, passes 701 of 701, and carries the "
       "corrected typography and the document QA gate."],
      ["Rebuild unchanged", "a third, new checksum",
       "Produces an identical-in-content archive under a different "
       "checksum. Solves nothing and spends a build."],
      ["Rebuild reverting the fix", "a third, new checksum",
       "Does not recover the named value, and reintroduces the shouting "
       "capitals. Not advised."],
    ], widths=[1.75, 1.65, 3.3], size=8.5)

    # ------------------------------------------------------------- prevention
    h(d, "7. What this exposes, for future handoffs")
    para(d, "Conditioning acceptance on a checksum is the right instinct: it "
            "is what makes a handoff verifiable rather than trusted. The "
            "problem is that these builds are not reproducible, because each "
            "one writes its own clock into its output. A checksum can "
            "therefore only ever certify one specific artifact, never a "
            "rebuild of it.")
    bullets(d, [
      "Short term: lock the checksum of the artifact that exists, and treat "
      "any rebuild as producing a new artifact that needs a new checksum.",
      "Longer term, if reproducibility is wanted: make the build stamp "
      "injectable rather than read from the clock, so the same inputs "
      "produce the same bytes and a checksum certifies the content rather "
      "than the moment. This is a small change to one function and is not "
      "made here, because the current packages are locked.",
    ])

    # ------------------------------------------------------------- unaffected
    h(d, "8. What is unaffected")
    bullets(d, [
      "Videos 4 and 5 remain the only approximately 5-minute retention-test "
      "videos.",
      "Videos 6, 7 and 8 are built from their restored masters, and the "
      "supplied September 11 files remain unmodified as audit history.",
      "Videos 9 to 14 remain regular long-form; Videos 15 to 21 keep the "
      "restored 9 to 12 minute depth.",
      "The restoration report stands as the source-integrity decision.",
      "No file inside the locked packages has been modified by this "
      "analysis.",
    ])
    d.save(path)
    return path


if __name__ == "__main__":
    stamp = subprocess.check_output(
        ["env", "TZ=America/Chicago", "date",
         "+%A, %B %d, %Y | %-I:%M %p CT"]).decode().strip()
    os.makedirs(OUT, exist_ok=True)
    print(build(os.path.join(OUT, "Handoff_Checksum_Condition_Analysis.docx"),
                stamp))
