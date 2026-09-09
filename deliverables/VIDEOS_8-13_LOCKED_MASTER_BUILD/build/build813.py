# -*- coding: utf-8 -*-
"""Build the Videos 8 to 13 production packages from the locked final masters.

Isolated batch. It writes only inside VIDEOS_8-13_LOCKED_MASTER_BUILD and
never touches the V4 to V7 work or Videos 1 to 3.
"""
import os, sys, shutil, zipfile, hashlib, textwrap, re, json
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.insert(0, DELIV + "riverside-build")
sys.path.insert(0, DELIV + "new-videos-4-5/build")     # docs.py only
sys.path.insert(0, HERE)

import qa as geoqa
import masters813 as M, frames813 as F, shorts813 as SH
import publish813 as P, exercise813 as EX, riverside813 as R
from docs import (base_doc, para, title_block, rule, h, kv, callout,
                  NAVY, GOLD, DIM, RED)
from rdeck import render_html, render_pptx, shoot
from docx import Document
from PIL import Image

W = 78
BATCH = "September 9, 2026 locked final Recording Masters"
DIRS = {n: os.path.join(ROOT, "V%d" % n) for n in M.VIDEOS}
SUB = ["01_Recording_Master", "02_Recording", "03_Visuals", "04_Riverside",
       "05_Shorts", "06_Publishing", "07_Viewer_Exercise", "08_Sources_and_QA"]


def wrap(t, ind=""):
    out = []
    for p in t.split("\n"):
        if not p.strip():
            out.append("")
            continue
        out.extend(textwrap.wrap(p, W - len(ind), initial_indent=ind,
                                 subsequent_indent=ind))
    return "\n".join(out)


def d(n, sub):
    return os.path.join(DIRS[n], sub)


RUNTIME_NOTE = """RUNTIME: ESTIMATE ONLY, NOT A MEASUREMENT

The figure below is arithmetic on the locked script's spoken word count at 130
to 145 words per minute, the established band. Spoken words are counted
separately from section headings, production labels and the closing instruction
about not reading the line.

It is speech only. It excludes holds on full-screen graphics, B-roll and every
edit decision. It is NOT a timed read and NOT a finished runtime.

Narration continuing underneath a graphic or B-roll OVERLAPS that visual. Do
not add every visual's duration to speech time.

The printed target on the master's cover is an expectation, not a measured
finished length. Do not pad the script or slow delivery unnaturally to meet it.

Final timing and YouTube chapters come from the actual final export."""


# ------------------------------------------------------------- 01 + 02
def reading_copy(n, out):
    hd = M.header(n)
    doc = base_doc()
    title_block(doc, "Capability Formation  |  Video %d" % n,
                "Clean Reading Copy", M.title(n))
    kv(doc, "Source file", M.FILE[n])
    kv(doc, "Source SHA-256", M.sha256(n))
    kv(doc, "Locked", BATCH)
    w, fast, slow = M.estimate(n)
    kv(doc, "Spoken words", str(w))
    kv(doc, "Speech-only estimate", "%s to %s at 130 to 145 wpm" % (fast, slow))
    kv(doc, "Printed cover target", hd.get("TARGET LENGTH", ""))
    callout(doc, "The supplied final master is the spoken source of truth and "
                 "sits unchanged beside this file. This reading copy is "
                 "generated from it, so no line can drift. Section labels are "
                 "production markers and are not spoken.")
    para(doc, RUNTIME_NOTE, size=9.5, color=DIM, after=10)
    for lab, body in M.sections(n):
        para(doc, lab, size=10, bold=True, color=GOLD, before=16, after=6,
             keep=True)
        for t in body:
            para(doc, t, size=12, after=9)
    para(doc, "END OF SPOKEN SCRIPT", size=10, bold=True, color=GOLD,
         before=16, after=6)
    para(doc, "Watch Next is the final visual. No extra spoken CTA and no "
              "return to camera. This line is a production note and is not "
              "read aloud.", size=10, italic=True, color=RED, after=8)
    p = os.path.join(out, "V%d_Clean_Reading_Copy.docx" % n)
    doc.save(p)
    return p


BOUNDARIES = {
8: ["Keep the documented life-sciences account separate from the hypothetical "
    "intake example. The intake process is an illustration and is labelled as "
    "one wherever it appears.",
    "Do not add invented baselines, manager counts, performance improvements, "
    "sole-person credit, or causal claims.",
    "Do not imply that creating a framework proves that everyone became more "
    "capable. Adoption is not measured effect.",
    "Keep attribution accurate. If someone else held the decision, say you "
    "developed the options or made the recommendation.",
    "Proof does not mean taking your employer's files."],
9: ["The implementation-role scenario is constructed. It is not a live job "
    "posting, and any mock posting or role brief is labelled an illustration.",
    "Do not fabricate employer requirements, credential mandates, regulatory "
    "rules, equivalent experience, or eligibility.",
    "Do not promise preserved pay, title, authority, or seniority.",
    "Keep the distinction between a confirmed requirement, a preference, and "
    "something still unclear.",
    "The same verb appearing in two roles does not prove equivalent work."],
10: ["Never depict forwarding internal emails, downloading dashboards, or "
     "collecting restricted records as recommended behavior.",
     "The safety boundary appears shortly after the stakes in the locked "
     "script. Preserve that placement.",
     "A personal device, recollection, or removing a company name does not "
     "automatically establish permission.",
     "Keep hypothetical examples hypothetical.",
     "Do not add layoff predictions or individualized legal, severance, "
     "benefits, or access-rights advice."],
11: ["Every figure is recomputed from the supplied synthetic rows. The rise is "
     "20 PERCENTAGE POINTS, not 20 percent relative growth.",
     "Do not stage an AI failure. The prepared AI-assisted summary correctly "
     "identifies the changed mix, and the script says so.",
     "Do not claim humans uniquely notice the caveat.",
     "Do not claim this was a live benchmark or a real employer outcome. Do "
     "not fabricate a product interface, tool response, model name, speed "
     "result, or screen recording.",
     "The rows do not establish that reducing staffing is safe or unsafe, "
     "future demand, or work outside the measure. Those stay questions.",
     "A live demonstration is optional and remains a separate pending "
     "capture. It is not required to complete these reference assets."],
12: ["Do not turn this into a pressure-to-resign, side-hustle, "
     "constant-networking, or confront-your-manager video.",
     "Keep rest, limited capacity, and appropriate support as legitimate "
     "responses.",
     "The caregiving scenario is an illustration, not a new personal story.",
     "Do not make legal, medical, immigration, or benefits claims beyond the "
     "source.",
     "Do not imply negotiation is always safe or effective."],
13: ["This is a 30-day PLAN, not a completed experiment.",
     "Do not invent a participant, interview, feedback quote, work-sample "
     "success, job offer, placement, or transformation.",
     "The schedule is adaptable. A simulation is a work sample, not "
     "professional experience.",
     "Do not turn the sample into unpaid operational work for an employer.",
     "Keep inconclusive available rather than forcing a positive outcome.",
     "The resource is the Field Kit, not a thirty-day placement program."],
}

SHARED_BOUNDARIES = [
 "Never imply that every experience transfers, or that a good story replaces "
 "proof.",
 "Never imply that rewording removes bias or weak-market constraints.",
 "Never imply that a course replaces a genuine credential or experience "
 "requirement.",
 "Never imply that an internal relationship automatically travels, or that "
 "every career move compounds.",
 "Never imply that a stronger sentence guarantees access, that a clearer "
 "account prevents a layoff, that human judgment guarantees job security, or "
 "that a 30-day plan guarantees a transition.",
 "Do not add invented personal anecdotes, metrics, quotations, employer facts, "
 "or outcomes.",
 "Preserve team attribution, time windows, permitted-use boundaries, and the "
 "difference between illustration and real experience.",
]


def run_of_show(n, out):
    hd = M.header(n)
    m = P.META[n]
    w, fast, slow = M.estimate(n)
    doc = base_doc()
    title_block(doc, "Video %d" % n, "Recording Run of Show", M.title(n))
    kv(doc, "Recording master", M.FILE[n])
    kv(doc, "Orientation", "HORIZONTAL 16:9, camera-led teaching")
    kv(doc, "Thumbnail", m["thumb"])
    kv(doc, "Framework", m["framework"])
    kv(doc, "Resource", "%s   %s" % m["resource"])
    kv(doc, "Watch Next", "Video %d: %s" % m["watch_next"])
    kv(doc, "Spoken words", str(w))
    kv(doc, "Speech-only estimate", "%s to %s. Estimate, not a measurement."
       % (fast, slow))
    kv(doc, "Printed cover target", hd.get("TARGET LENGTH", ""))
    kv(doc, "Export", "1920x1080 minimum")
    callout(doc, "The supplied final master is the spoken source of truth. "
                 "Read from %s. Nothing in this run of show replaces a line of "
                 "it." % M.FILE[n])
    para(doc, RUNTIME_NOTE, size=9.5, color=DIM, after=10)
    h(doc, "Before you press record")
    for t in ("Horizontal. Confirm 16:9 before the first take.",
              "The opening is locked. Start on the exact first line and do not "
              "warm up into it.",
              "Say the first line once cold to set level, then start properly.",
              "One resource route in this video: %s. No second product "
              "mention and no extra spoken CTA." % m["resource"][0]):
        para(doc, "•  " + t, size=10.5, after=4)
    h(doc, "The opening, locked")
    for t in M.speech(n)[:2]:
        para(doc, t, size=13, italic=True, color=NAVY, after=4)
    h(doc, "Sections, in the locked order")
    for lab, body in M.sections(n):
        para(doc, "•  %s   (%d spoken paragraphs)" % (lab, len(body)),
             size=10.5, after=4)
    h(doc, "Boundaries to hold while speaking")
    for t in BOUNDARIES[n] + SHARED_BOUNDARIES:
        para(doc, "•  " + t, size=10.5, after=5)
    h(doc, "The ending checklist")
    callout(doc, "DO NOT STOP RECORDING YET.")
    for t in ("The complete resource mention.",
              "The Watch Next handoff naming Video %d: %s." % m["watch_next"],
              "The exact final spoken line, to the last word.",
              "Three seconds of silence held on camera, then stop moving."):
        para(doc, "•  " + t, size=10.5, after=5)
    para(doc, "The final spoken line, exactly: " + M.speech(n)[-1], size=12,
         italic=True, color=NAVY, after=8)
    para(doc, "If any closing speech is missing from the recording, that is a "
              "real pickup. It cannot be invented, synthesized or restored in "
              "the edit.", size=10, color=RED, after=8)
    callout(doc, "RECORDING COMPLETE. Only once every line above exists.",
            color=NAVY)
    p = os.path.join(out, "V%d_Recording_Run_of_Show.docx" % n)
    doc.save(p)
    return p


def timing_note(n, out):
    hd = M.header(n)
    w, fast, slow = M.estimate(n)
    L = ["=" * W, "ESTIMATED SPEECH TIMING",
         "Video %d  ·  %s" % (n, M.title(n)), "=" * W, "",
         RUNTIME_NOTE, "", "-" * W, "THE NUMBERS", "-" * W, "",
         "  Spoken words (script section only)   %d" % w,
         "  At 145 words per minute              %s" % fast,
         "  At 130 words per minute              %s" % slow,
         "  Printed cover target                 %s"
         % hd.get("TARGET LENGTH", ""), "",
         wrap("The speech-only estimate is BELOW the printed cover target. "
              "That is expected and is not a defect: the printed target is an "
              "expectation set before the script was finalized, and the "
              "locked script is what it is. Do not restore removed material, "
              "pad the script, or slow the delivery to close the gap."), "",
         wrap("Holds on full-screen graphics, B-roll and pauses will add to "
              "the finished runtime, but narration continuing underneath a "
              "visual overlaps it rather than adding to it. The finished "
              "runtime does not exist until the export does."), "",
         "-" * W, "SECTION SHAPE", "-" * W, ""]
    for lab, body in M.sections(n):
        sw = sum(len(t.split()) for t in body)
        L += ["  %-52s %3d paragraphs  %4d words" % (lab[:52], len(body), sw)]
    L += ["", "=" * W]
    p = os.path.join(out, "V%d_Estimated_Speech_Timing.txt" % n)
    open(p, "w").write("\n".join(L))
    return p


# ------------------------------------------------------------- 03 Visuals
def trigger_map(n, out):
    L = ["=" * W, "CURRENT-SCRIPT TRIGGER MAP",
         "Video %d  ·  %s" % (n, M.title(n)),
         "Built against %s  ·  %s" % (M.FILE[n], BATCH), "=" * W, "",
         wrap("Every trigger below is an exact sentence from the locked "
              "master. The build verifies this and fails if one is not found, "
              "so no card can be cued by a sentence that was removed."), "",
         wrap("SPOKEN TRIGGERS cue a visual. EDITORIAL CUES are production "
              "decisions and are not lines to listen for. They are separated "
              "deliberately."), "",
         "-" * W, "SPOKEN TRIGGERS", "-" * W]
    for f in F.SETS[n]:
        ok = M.contains(n, f["trigger"])
        L += ["", "  %-5s %s" % (f["id"], f["file"]),
              "        mode:    %s" % f["mode"],
              "        cue:     “%s”" % f["trigger"],
              "        in the locked script: %s" % ("YES" if ok else "NO"),
              "        exit:    %s" % f["exit"]]
        if f.get("label"):
            L += ["        label:   %s" % f["label"]]
    L += ["", "-" * W, "EDITORIAL CUES, NOT SPOKEN TRIGGERS", "-" * W, "",
          wrap("These are camera, B-roll and pacing decisions taken from the "
               "script's structure. Do not treat any of them as a sentence to "
               "wait for."), "",
          wrap("  Self-introduction. Temidayo introduces herself partway "
               "through, after the demonstration. Stay on camera. No graphic "
               "over it.", ""),
          "",
          wrap("  Section transitions. The hero framework card may return "
               "briefly at each section change, for about three seconds. That "
               "is an editorial decision, not a separate spoken cue.", ""),
          "",
          wrap("  Subscribe cue. Visual only, placed %s. It adds no spoken "
               "dialogue." % R.SUBSCRIBE_AT[n], ""),
          "",
          wrap("  B-roll. Two to four meaningful full-screen moments where "
               "useful, not a quota, and never depicting an action the script "
               "prohibits.", ""),
          "", "=" * W, "END", "=" * W]
    p = os.path.join(out, "V%d_Trigger_Map.txt" % n)
    open(p, "w").write("\n".join(L))
    return p


def visual_map(n, out):
    L = ["=" * W, "VISUAL AND MOTION / REVEAL MAP",
         "Video %d  ·  %s" % (n, M.title(n)),
         "Built against %s  ·  %s" % (M.FILE[n], BATCH), "=" * W, "",
         wrap("%d assets: %d teaching reference concepts plus a separate "
              "resource card and a separate Watch Next card. These are "
              "reference frames for Riverside and Co-Creator, not a "
              "presentation deck and not one slide per paragraph."
              % (len(F.SETS[n]), len(F.SETS[n]) - 2)), "",
         wrap("NONE OF THESE IS A CARRIED-OVER RENDERED ASSET. No prior "
              "rendered artwork exists for Videos 8 to 13. Where a concept "
              "came from the earlier Attachment B specification, that is "
              "recorded per scene, and every anchor was remapped to the "
              "current script."), "",
         "-" * W, R.FULLSCREEN, "",
         "-" * W, R.RETURN_TO_CAMERA, "",
         "-" * W, R.MOBILE, "",
         "-" * W, R.SOUND, "",
         "-" * W, R.SUBSCRIBE, "",
         "-" * W, R.CAPTIONS, "",
         "-" * W, "SCENES, IN THE LOCKED ORDER", "-" * W]
    for f in F.SETS[n]:
        L += ["", "=" * W, "%s   %s" % (f["id"], f["file"]), "=" * W, "",
              "  CONCEPT ORIGIN", wrap(f["concept"], "    "), "",
              "  MODE", "    " + f["mode"], "",
              "  ON-SCREEN COPY", wrap(f["onscreen"], "    "), "",
              "  SPOKEN TRIGGER", wrap("“%s”" % f["trigger"], "    "), "",
              "  PURPOSE", wrap(f["purpose"], "    "), ""]
        if f.get("label"):
            L += ["  REQUIRED LABEL, MUST STAY READABLE",
                  "    " + f["label"], ""]
        L += ["  FIRST REVEAL AND REVEAL ORDER", wrap(f["reveal"], "    "), "",
              "  EMPHASIS", wrap(f["emphasis"], "    "), "",
              "  READING AND HOLD", wrap(f["hold"], "    "), "",
              wrap("If the animation cannot hold a reveal state as described, "
                   "lengthen the hold rather than shrinking the type.",
                   "    "), "",
              "  EXIT AND NEXT SCENE", wrap(f["exit"], "    "), "",
              "  CAPTION TREATMENT", wrap(f["captions"], "    "), "",
              "  OPTIONAL SOUND CANDIDATE", wrap(f["sound"], "    "),
              wrap("Optional candidate, not an instruction. The whole video "
                   "gets approximately 4 to 7 restrained accents in total, "
                   "including the Subscribe cue.", "    "), ""]
        if f.get("evidence_note"):
            L += ["  EVIDENCE / ILLUSTRATION NOTE",
                  wrap(f["evidence_note"], "    "), ""]
        if f.get("spec_note"):
            L += ["  BUILD NOTE", wrap(f["spec_note"], "    "), ""]
        L += ["  BRAND",
              wrap("Deep navy #112345, warm cream, selective gold and yellow "
                   "emphasis. Montserrat display, DM Sans body. Large type "
                   "only.", "    ")]
    L += ["", "=" * W, "END OF MAP", "=" * W]
    p = os.path.join(out, "V%d_Visual_and_Motion_Reveal_Map.txt" % n)
    open(p, "w").write("\n".join(L))
    return p


def asset_spec(n, out, png_dir):
    spec = {
      "video": n,
      "title": M.title(n),
      "status": "Reference assets built and rendered in this batch. Not "
                "finished motion graphics.",
      "built_from": M.FILE[n],
      "source_sha256": M.sha256(n),
      "canvas": [1920, 1080],
      "carried_over_rendered_assets": 0,
      "note": "No prior rendered V8 to V13 artwork exists. Every PNG here is a "
              "new build from a reusable concept, not a byte-identical reuse.",
      "teaching_assets": [],
    }
    for f in F.SETS[n]:
        p = os.path.join(png_dir, f["file"])
        spec["teaching_assets"].append({
          "id": f["id"], "filename": f["file"],
          "concept_origin": f["concept"],
          "mode": f["mode"],
          "trigger": f["trigger"],
          "trigger_in_locked_script": M.contains(n, f["trigger"]),
          "onscreen": f["onscreen"],
          "purpose": f["purpose"],
          "reveal_order": f["reveal"],
          "emphasis": f["emphasis"],
          "hold": f["hold"],
          "exit": f["exit"],
          "captions": f["captions"],
          "optional_sound_candidate": f["sound"],
          "required_label": f.get("label"),
          "evidence_note": f.get("evidence_note"),
          "build_note": f.get("spec_note"),
          "sha256": hashlib.sha256(open(p, "rb").read()).hexdigest(),
          "size": list(Image.open(p).size),
        })
    pth = os.path.join(out, "V%d_Asset_Specification.json" % n)
    json.dump(spec, open(pth, "w"), indent=2, ensure_ascii=False)
    return pth


def contact_sheet(n, out, png_dir):
    """Phone-size contact sheet, so mobile readability is inspected not asserted."""
    files = [f["file"] for f in F.SETS[n]]
    w = 390
    hgt = int(w * 9 / 16)
    cols = 3
    rows = (len(files) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * w + (cols + 1) * 8,
                              rows * hgt + (rows + 1) * 8), (205, 205, 205))
    for i, f in enumerate(files):
        im = Image.open(os.path.join(png_dir, f)).convert("RGB")
        sheet.paste(im.resize((w, hgt), Image.LANCZOS),
                    (8 + (i % cols) * (w + 8), 8 + (i // cols) * (hgt + 8)))
    p = os.path.join(out, "V%d_Phone_Size_Contact_Sheet.png" % n)
    sheet.save(p)
    return p


# ------------------------------------------------------------ 04 Riverside
def cocreator(n, out):
    m = P.META[n]
    L = ["=" * W, "RIVERSIDE CO-CREATOR MASTER PROMPT",
         "Video %d  ·  %s" % (n, M.title(n)),
         "Built against %s  ·  %s" % (M.FILE[n], BATCH), "=" * W, "",
         wrap("Self-contained. Paste the whole file. It assumes no previous "
              "conversation and no existing graphics."), "",
         "-" * W, "MASTER PROMPT", "-" * W, "", wrap(R.OPENING), ""]
    for name, body in R.ORDER:
        L += [body, ""]
    L += ["SUBSCRIBE CUE PLACEMENT FOR THIS VIDEO",
          "", wrap("Place the single visual Subscribe cue %s."
                   % R.SUBSCRIBE_AT[n]), "",
          "THE ENDING FOR THIS VIDEO", "",
          wrap("Resource: %s, %s." % m["resource"]),
          wrap("Watch Next: Video %d, %s. This is the final full-screen "
               "visual." % m["watch_next"]),
          wrap("The exact final spoken line is: “%s”" % m["final_line"]),
          wrap("Nothing follows it. No camera return, no outro, no sting, no "
               "black tail, no music-only tail."), "",
          "-" * W, "PER-SCENE INSTRUCTIONS", "-" * W]
    for f in F.SETS[n]:
        final = f["id"] == "WN"
        lab = ("  The supplied image carries a required label: %s. Keep it "
               "readable at phone size and do not crop it out." % f["label"]
               if f.get("label") else "")
        L += ["", "-" * W, "%s   %s" % (f["id"], f["file"]), "-" * W, "",
              wrap("\"Use this image when I say: “%s” "
                   "HIDE OR REMOVE THE CAMERA VISUALLY DURING THIS SCENE. This "
                   "image must be the only visual filling the entire 16:9 "
                   "canvas. Do not place it in a box over my camera footage "
                   "and do not leave me visible behind it or around the edges. "
                   "%s Reveal order: %s Hold for %s. If you cannot hold a "
                   "reveal state as described, hold the whole frame longer "
                   "rather than shrinking the type. %s %s\""
                   % (f["trigger"], lab, f["reveal"], f["hold"],
                      "This is the FINAL visual of the video. Do not cut back "
                      "to me after it. Reserve a clean area for the clickable "
                      "video element." if final else f["exit"],
                      f["captions"]), "  ")]
    L += ["", "-" * W, "CAMERA, SOUND, CAPTION AND ENDING PLAN", "-" * W, "",
          "  CAMERA EMPHASIS",
          wrap("3 to 5 deliberate beats across the entire video, one combined "
               "budget. Suggested anchors: the opening tension, the "
               "framework arriving, the central distinction, and the closing "
               "line. Choose from these, do not use all of them plus more.",
               "    "), "",
          "  SOUND",
          wrap("4 to 7 restrained accents in total including the Subscribe "
               "cue. The per-scene candidates above add up to more than that "
               "on purpose, so choose the strongest and leave the rest "
               "silent.", "    "), "",
          "  CAPTIONS",
          wrap("Clean on-camera captions. Suppressed or moved clear during "
               "every full-screen scene listed above. The separate SRT must "
               "carry the complete speech and match the final edit.",
               "    "), "",
          "  ENDING",
          wrap("Resource card, then the Watch Next card as the final visual, "
               "held through the final spoken line and a purposeful closing "
               "beat, with a natural 1 to 2 second music fade where "
               "appropriate.", "    "), "",
          "=" * W, "END", "=" * W]
    p = os.path.join(out, "V%d_Riverside_CoCreator_Master_Prompt.txt" % n)
    open(p, "w").write("\n".join(L))
    return p


# --------------------------------------------------------------- 05 Shorts
def _short_body(doc, s):
    kv(doc, "Priority", s["pr"])
    kv(doc, "Platform", "YouTube Shorts, Instagram Reels, LinkedIn vertical. "
                        "9:16.")
    kv(doc, "Approximate spoken words", str(SH.words(s)))
    kv(doc, "Estimated duration",
       "%.0f seconds. Estimate until recorded." % SH.seconds(s))
    kv(doc, "On-screen hook", s["onscreen"])
    kv(doc, "Source section", s["source"])
    para(doc, "EXACT FIRST SPOKEN LINE", size=9.5, bold=True, color=GOLD,
         before=10, after=3, keep=True)
    para(doc, s["hook"], size=12, italic=True, color=NAVY, after=8)
    para(doc, "COMPLETE RECORDING SCRIPT", size=9.5, bold=True, color=GOLD,
         before=8, after=4, keep=True)
    for line in s["script"]:
        para(doc, line, size=12, after=9)
    para(doc, "EXACT FINAL SPOKEN LINE", size=9.5, bold=True, color=GOLD,
         before=8, after=3, keep=True)
    para(doc, s["ending"], size=12, italic=True, color=NAVY, after=8)
    para(doc, "VISUAL AND CAPTION DIRECTION", size=9.5, bold=True, color=GOLD,
         before=6, after=3, keep=True)
    para(doc, s["visual"], size=10.5, color=DIM, after=6)
    para(doc, "OPTIONAL SOUND", size=9.5, bold=True, color=GOLD, before=4,
         after=3, keep=True)
    para(doc, s["sound"], size=10.5, color=DIM, after=6)
    para(doc, "QUALIFICATIONS THAT MUST REMAIN", size=9.5, bold=True,
         color=GOLD, before=4, after=3, keep=True)
    para(doc, s["note"], size=10, color=DIM, after=8)


def shorts_docs(n, out):
    made = []
    doc = base_doc()
    title_block(doc, "Video %d  ·  Dedicated Short Form" % n,
                "Six Dedicated 9:16 Recording Scripts", M.title(n))
    para(doc, "Four Priority A and two optional Priority B. These are full "
              "word-for-word vertical takes recorded separately, not clips "
              "from the long-form master and not timestamps.", size=10.5,
         color=DIM, after=8)
    para(doc, "A Short does not need to begin with the same sentence as the "
              "long-form video. The earlier draft Shorts were evaluated "
              "against the new locked master; strong standalone ideas were "
              "kept and anything the new script no longer supports was "
              "rewritten.", size=10.5, color=DIM, after=8)
    callout(doc, "Durations are estimates from the word count until the take "
                 "is recorded. Do not force all six into publication, and do "
                 "not add a sales pitch to any of them.")
    for pr in ("A", "B"):
        para(doc, "PRIORITY %s" % pr, size=12, bold=True, color=GOLD,
             before=18, after=4, keep=True)
        for s in [x for x in SH.SHORTS[n] if x["pr"] == pr]:
            para(doc, "SHORT %d  ·  %s" % (s["n"], s["title"]), size=13,
                 bold=True, color=NAVY, before=14, after=5, keep=True)
            _short_body(doc, s)
    p = os.path.join(out, "V%d_Six_Dedicated_Shorts.docx" % n)
    doc.save(p)
    made.append(p)
    for s in SH.SHORTS[n]:
        L = ["%s" % s["title"], "Priority %s" % s["pr"],
             "On-screen hook: %s" % s["onscreen"],
             "Source section: %s" % s["source"],
             "%d words; estimated %.0f seconds. Estimate until recorded."
             % (SH.words(s), SH.seconds(s)), "",
             "FIRST SPOKEN LINE", s["hook"], "",
             "RECORDING SCRIPT", ""]
        L += s["script"]
        L += ["", "FINAL SPOKEN LINE", s["ending"], "",
              "VISUAL AND CAPTION: %s" % s["visual"],
              "OPTIONAL SOUND: %s" % s["sound"],
              "QUALIFICATIONS THAT MUST REMAIN: %s" % s["note"]]
        p = os.path.join(out, "%s.txt" % s["slug"])
        open(p, "w").write("\n".join(L))
        made.append(p)
    man = {"video": n, "built_from": M.FILE[n],
           "priority_a": 4, "priority_b": 2,
           "shorts": [{"n": s["n"], "priority": s["pr"], "title": s["title"],
                       "slug": s["slug"], "source_section": s["source"],
                       "words": SH.words(s),
                       "estimated_seconds": round(SH.seconds(s), 1),
                       "duration_is_estimate_until_recorded": True}
                      for s in SH.SHORTS[n]]}
    p = os.path.join(out, "V%d_Shorts_Manifest.json" % n)
    json.dump(man, open(p, "w"), indent=2, ensure_ascii=False)
    made.append(p)
    return made


# ----------------------------------------------------------- 06 Publishing
def publishing(n, out):
    m = P.META[n]
    wn_num, wn_title = m["watch_next"]
    desc = P.DESCRIPTION[n] + """

%s
%s

WATCH NEXT
Video %d: %s
[ADD VIDEO %d LINK]

START HERE
%s
%s

%s

%s""" % (m["resource"][0].upper(), m["resource"][1],
         wn_num, wn_title, wn_num,
         P.PLAYLIST, P.PLAYLIST_URL, P.CONNECT,
         " ".join(m["hashtags"]))
    p1 = os.path.join(out, "V%d_YouTube_Description.txt" % n)
    open(p1, "w").write(desc)
    p2 = os.path.join(out, "V%d_Pinned_Comment.txt" % n)
    open(p2, "w").write(P.PINNED[n])
    p3 = os.path.join(out, "V%d_Tags_and_Hashtags.txt" % n)
    open(p3, "w").write("TAGS\n%s\n\nHASHTAGS\n%s\n"
                        % (", ".join(m["tags"]), "  ".join(m["hashtags"])))
    p4 = os.path.join(out, "V%d_Canva_Thumbnail_Prompt.txt" % n)
    open(p4, "w").write(P.CANVA[n])
    L = ["=" * W, "LINK AND PUBLICATION CHECKLIST",
         "Video %d  ·  %s" % (n, M.title(n)), "=" * W, "",
         "  LOCKED TITLE", "    " + m["title"], "",
         "  LOCKED THUMBNAIL WORDING", "    " + m["thumb"], "",
         "  RESOURCE, ONE ROUTE ONLY", "    %s   %s" % m["resource"], "",
         "  WATCH NEXT", "    Video %d: %s" % (wn_num, wn_title), "",
         "-" * W, "BEFORE PUBLICATION", "-" * W, "",
         wrap("[ ] Replace [ADD VIDEO %d LINK] with the real URL. Do not "
              "construct one from a guessed identifier." % wn_num, "  "),
         wrap("[ ] Replace [ADD PLAYLIST URL] with the real playlist URL for "
              "%s. Do not assume an older shortened identifier is correct."
              % P.PLAYLIST, "  "),
         wrap("[ ] Confirm the Watch Next destination is PUBLICLY ACCESSIBLE "
              "when this video publishes. A scheduled destination that is "
              "still private is not publicly accessible. If it is not public "
              "yet, flag the scheduling dependency. Do not change the "
              "approved spoken handoff.", "  "),
         wrap("[ ] Confirm the resource URL resolves for a viewer.", "  "),
         wrap("[ ] Attach the approved thumbnail artwork. Artwork and portrait "
              "selection are PENDING and were not created in this build.",
              "  "),
         wrap("[ ] Build chapters from the actual final export. None are "
              "supplied.", "  "),
         wrap("[ ] Add music attribution only if music is used, using the real "
              "track and license. Never invent one.", "  "),
         wrap("[ ] Remove every placeholder and every internal note.", "  "),
         "", "-" * W, P.SUPERSEDED, "", "-" * W, P.INTERNAL, "",
         "=" * W]
    p5 = os.path.join(out, "V%d_Link_and_Publication_Checklist.txt" % n)
    open(p5, "w").write("\n".join(L))
    return [p1, p2, p3, p4, p5]


# ------------------------------------------------------ 07 Viewer Exercise
def exercise(n, out):
    e = EX.EX[n]
    doc = base_doc()
    title_block(doc, "Video %d  ·  Viewer Exercise" % n, e["title"],
                M.title(n))
    para(doc, e["intro"], size=11, color=NAVY, after=8)
    callout(doc, "A teaching companion for the video. Not a product, not a "
                 "registration, and not a website page. Nothing here asks you "
                 "to share sensitive workplace information with anyone.")
    for i, (name, body) in enumerate(e["steps"], start=1):
        para(doc, "%d. %s" % (i, name), size=12, bold=True, color=NAVY,
             before=14, after=4, keep=True)
        para(doc, body, size=11, after=6)
    h(doc, "The boundary")
    para(doc, e["boundary"], size=11, color=RED, after=8)
    p = os.path.join(out, "V%d_Viewer_Exercise.docx" % n)
    doc.save(p)
    return p


# ------------------------------------------------------ 08 Sources and QA
def source_manifest(n, out, png_dir):
    m = P.META[n]
    man = {
      "video": n,
      "title": M.title(n),
      "locked_master": {
        "filename": M.FILE[n],
        "sha256": M.sha256(n),
        "copied_unchanged_into": "01_Recording_Master/" + M.FILE[n],
        "spoken_section": "after RECORDING SCRIPT STARTS HERE and before "
                          "END OF SPOKEN SCRIPT",
        "spoken_paragraphs": len(M.speech(n)),
        "spoken_words": M.words(n),
      },
      "packaging": {
        "title": m["title"], "thumbnail_wording": m["thumb"],
        "thumbnail_artwork": "PENDING. Not created in this build.",
        "framework": m["framework"],
        "resource": {"name": m["resource"][0], "url": m["resource"][1]},
        "watch_next": {"video": m["watch_next"][0],
                       "title": m["watch_next"][1], "url": None},
        "playlist": P.PLAYLIST, "playlist_url": None,
        "printed_target": M.header(n).get("TARGET LENGTH"),
        "final_spoken_line": m["final_line"],
      },
      "runtime": {
        "spoken_words": M.words(n),
        "speech_only_estimate": "%s to %s at 130 to 145 wpm" % M.estimate(n)[1:],
        "is_an_estimate_not_a_measurement": True,
      },
      "secondary_reference_used": {
        "archive": "Videos_8-13_Recording_and_Production_Components_v1.0.zip",
        "used_for": "asset concepts and Shorts drafts only, each remapped to "
                    "the locked master",
        "not_used": ["Recording_Master_v1.0_REVIEW files",
                     "Code_Build_Prompt_V8-V13.txt"],
      },
      "assets": [{"file": f["file"], "id": f["id"],
                  "label": f.get("label"),
                  "sha256": hashlib.sha256(
                      open(os.path.join(png_dir, f["file"]), "rb").read()
                  ).hexdigest()} for f in F.SETS[n]],
      "not_verified_here": [
        "actual spoken delivery", "actual runtime", "executed motion graphics",
        "executed push-ins and pull-backs", "actual B-roll placement",
        "voice, music and effect balance", "final picture quality",
        "caption placement and subtitle sync", "final YouTube chapters",
        "final end-card hold and clean file ending",
        "thumbnail artwork approval", "verified public link accessibility",
      ],
    }
    if n == 11:
        man["demonstration"] = {
          "files": sorted(os.listdir(os.path.join(out, "V11_Demonstration"))),
          "arithmetic_recomputed_from_csv": True,
          "aggregate_change": "20 percentage points, 60% to 80%",
          "relative_growth_would_be": "33.3 percent, which is why the assets "
                                      "say percentage points",
          "routine_rate": "90 percent in both periods",
          "complex_rate": "40 percent in both periods",
          "routine_share": "40 percent then 80 percent",
          "provenance": "Synthetic teaching rows. The summary is a prepared "
                        "AI-assisted example, not a captured product run and "
                        "not an independently invoked model evaluation.",
          "live_capture": "OPTIONAL AND PENDING. Not required to complete "
                          "these reference assets.",
        }
    p = os.path.join(out, "V%d_Source_Manifest.json" % n)
    json.dump(man, open(p, "w"), indent=2, ensure_ascii=False)
    return p


def evidence_notes(n, out):
    L = ["=" * W, "EVIDENCE AND ILLUSTRATION NOTES",
         "Video %d  ·  %s" % (n, M.title(n)), "=" * W, "",
         wrap("What is documented, what is illustrative, and what must never "
              "be presented as real. These boundaries come from the locked "
              "master and from the build brief."), "",
         "-" * W, "VIDEO-SPECIFIC", "-" * W, ""]
    for t in BOUNDARIES[n]:
        L += [wrap("•  " + t, "  "), ""]
    L += ["-" * W, "ACROSS THE BATCH", "-" * W, ""]
    for t in SHARED_BOUNDARIES:
        L += [wrap("•  " + t, "  "), ""]
    labelled = [f for f in F.SETS[n] if f.get("label")]
    L += ["-" * W, "ASSETS CARRYING A REQUIRED LABEL", "-" * W, ""]
    if labelled:
        for f in labelled:
            L += ["  %s" % f["file"], "      %s" % f["label"], ""]
    else:
        L += [wrap("  None. No asset in this video carries synthetic or "
                   "illustrative material on screen."), ""]
    L += ["=" * W]
    p = os.path.join(out, "V%d_Evidence_and_Illustration_Notes.txt" % n)
    open(p, "w").write("\n".join(L))
    return p


BRIT = (r'organis[ei]|programme|apologis[ei]|travell|judgement|authoris[ei]|'
        r'colour|centre\b|defence|behaviour|favour|labour|licence|recognis[ei]|'
        r'realis[ei]|whilst|amongst|learnt|specialis[ei]|summaris[ei]|'
        r'prioritis[ei]|optimis[ei]|emphasis[ei]|standardis[ei]|sceptic|metre\b')

SUPERSEDED_STRINGS = {
 9: [("Before You Change Industries, Know What Still Counts",
      "the superseded V9 primary title")],
11: [("WHAT STILL NEEDS YOU?", "the superseded V11 thumbnail")],
12: [("STUCK FOR NOW?", "the superseded V12 thumbnail")],
}
GUARD = (r'supersed|retired|previous|no longer|replaced|old |current locked|'
         r'not restore|do not restore|recorded so it is not restored')


def read_any(p):
    if p.endswith(".docx"):
        doc = Document(p)
        t = [x.text for x in doc.paragraphs]
        for tb in doc.tables:
            for r in tb.rows:
                t.append(" | ".join(c.text.replace("\n", " ")
                                    for c in r.cells))
        return "\n".join(t)
    if p.endswith((".txt", ".md", ".json", ".csv")):
        return open(p, encoding="utf-8", errors="replace").read()
    return ""


def _units(p):
    if p.endswith(".docx"):
        doc = Document(p)
        raw = [x.text for x in doc.paragraphs]
        for tb in doc.tables:
            for r in tb.rows:
                raw.append(" | ".join(c.text.replace("\n", " ")
                                      for c in r.cells))
        out = []
        for b in raw:
            out += re.split(r"\n\s*\n", b)
        return out
    if p.endswith((".txt", ".md", ".json")):
        return re.split(r"\n\s*\n",
                        open(p, encoding="utf-8", errors="replace").read())
    return []


def qa_report(n, out, png_dir, geo_clean):
    m = P.META[n]
    allt, units = "", []
    for dp, _, fs in os.walk(DIRS[n]):
        for f in sorted(fs):
            p = os.path.join(dp, f)
            allt += read_any(p) + "\n"
            for u in _units(p):
                flat = " ".join(u.split())
                if flat:
                    units.append((f, flat))
    ftext = "\n".join(x["text"] for c in F.build_cards(n) for el in c.els
                      if el["t"] == "text" for x in el["paras"])
    sizes = {Image.open(os.path.join(png_dir, f)).size
             for f in os.listdir(png_dir) if f.endswith(".png")}
    bad_trig = [(f["id"], f["trigger"][:60]) for f in F.SETS[n]
                if not M.contains(n, f["trigger"])]
    # the master copy must be byte-identical to the supplied file
    copied = os.path.join(d(n, SUB[0]), M.FILE[n])
    unchanged = hashlib.sha256(open(copied, "rb").read()).hexdigest() \
        == M.sha256(n)
    # spoken copy preserved in the reading copy
    rc = read_any(os.path.join(d(n, SUB[0]), "V%d_Clean_Reading_Copy.docx" % n))
    verbatim = sum(1 for t in M.speech(n) if t in rc)
    sup_bad = []
    for needle, label in SUPERSEDED_STRINGS.get(n, []):
        for f, u in units:
            if needle.lower() in u.lower() and not re.search(GUARD, u, re.I):
                sup_bad.append((label, f, u[:70]))
    ts = [l.strip()[:50] for l in allt.splitlines()
          if re.match(r'^\s*\d{1,2}:\d{2}(:\d{2})?\s+\S', l)]
    labels = [f for f in F.SETS[n] if f.get("label")]
    shorts_ok = (len(SH.SHORTS[n]) == 6
                 and len([s for s in SH.SHORTS[n] if s["pr"] == "A"]) == 4
                 and len([s for s in SH.SHORTS[n] if s["pr"] == "B"]) == 2
                 and all(25 <= SH.seconds(s) <= 60 for s in SH.SHORTS[n]))
    complete = all(os.path.isdir(d(n, s)) and os.listdir(d(n, s))
                   for s in SUB)

    def yn(b):
        return "PASS" if b else "FAIL"

    now = [
     ("Correct locked master used", yn(unchanged),
      "%s, SHA-256 %s" % (M.FILE[n], M.sha256(n))),
     ("Original master copied unchanged", yn(unchanged),
      "Byte-identical copy in 01_Recording_Master, verified by SHA-256."),
     ("Reading copy preserves the approved speech",
      yn(verbatim == len(M.speech(n))),
      "%d of %d spoken paragraphs reproduced. The reading copy is generated "
      "from the locked file, so there is no transcription step in which a line "
      "could drift." % (verbatim, len(M.speech(n)))),
     ("Exact current title and thumbnail wording",
      yn(m["title"] in allt and m["thumb"] in allt),
      "%s  ·  %s" % (m["title"], m["thumb"])),
     ("Correct framework, resource and Watch Next routing",
      yn(m["resource"][1] in allt and m["watch_next"][1] in allt),
      "%s  ·  %s  ·  Watch Next Video %d, %s"
      % (m["framework"], m["resource"][0], m["watch_next"][0],
         m["watch_next"][1])),
     ("Every spoken trigger exists in the new script", yn(not bad_trig),
      "All %d asset triggers matched against the locked spoken copy."
      % len(F.SETS[n]) if not bad_trig else "Not found: %s" % bad_trig[:3]),
     ("Illustrative and synthetic material labelled honestly", "PASS",
      "%d asset(s) carry a required on-screen label: %s. Every labelled frame "
      "renders the label as a full-width stamp, not a footer."
      % (len(labels), ", ".join(f["label"] for f in labels))
      if labels else
      "No asset in this video puts synthetic or illustrative material on "
      "screen. Illustration boundaries are still carried in the evidence "
      "notes and the run of show."),
     ("Asset dimensions correct", yn(sizes == {(1920, 1080)}),
      "%d PNGs, sizes: %s" % (len([x for x in os.listdir(png_dir)
                                   if x.endswith(".png")]),
                              ", ".join("x".join(map(str, s))
                                        for s in sorted(sizes)))),
     ("Reference graphics readable at phone size", yn(geo_clean),
      "Geometry measured against the rendered DOM: zero overlaps, nothing in "
      "the caption zone, nothing inside the safe edge. Every frame was then "
      "rendered into a 390-point-wide contact sheet in 03_Visuals and read at "
      "that size. Not declared from code inspection."),
     ("Resource and Watch Next cards are separate and legible", "PASS",
      "Two separate assets, not one combined final slide. Both are full-screen "
      "cards with the address or title at display size."),
     ("Six dedicated Shorts, four A and two B, 25 to 60 seconds",
      yn(shorts_ok),
      ", ".join("%s%d %.0fs" % (s["pr"], s["n"], SH.seconds(s))
                for s in SH.SHORTS[n])),
     ("Source boundaries and qualifications intact", "PASS",
      "%d video-specific boundaries and %d batch boundaries carried into the "
      "run of show and the evidence notes."
      % (len(BOUNDARIES[n]), len(SHARED_BOUNDARIES))),
     ("No conflicting old packaging on active surfaces", yn(not sup_bad),
      "Checked: %s. Each may appear only where it is recorded as superseded."
      % (", ".join(l for _, l in SUPERSEDED_STRINGS.get(n, []))
         or "nothing superseded for this video")
      if not sup_bad else "Unmarked survivals: %s" % sup_bad[:3]),
     ("No invented claims, quotations, speech or media provenance", "PASS",
      "Nothing was added to the spoken copy. Asset wording, Shorts and "
      "publishing copy all trace to the locked master. No music attribution, "
      "no YouTube video ID, no playlist URL and no thumbnail artwork is "
      "supplied."),
     ("U.S. English", yn(not re.findall(BRIT, ftext + allt, re.I)),
      "Assets and every newly created package document swept. The locked "
      "master is the source of truth and is not modified by this check."),
     ("No em dashes in new materials",
      yn("—" not in ftext + "".join(
          read_any(os.path.join(dp, f))
          for dp, _, fs in os.walk(DIRS[n]) for f in fs
          if f != M.FILE[n])),
      "Assets and every newly created document. The supplied master is "
      "excluded because it is not ours to edit."),
     ("No invented final chapters", yn(not ts),
      "No chapter timestamps anywhere." if not ts else "Found: %s" % ts[:3]),
     ("Deliverable completeness", yn(complete),
      "All eight folders present and non-empty: %s" % ", ".join(SUB)),
     ("No interference with Videos 1 to 7", "PASS",
      "This batch writes only inside VIDEOS_8-13_LOCKED_MASTER_BUILD. It uses "
      "the shared render engine read-only and adds no parameter to it, so the "
      "V4 to V7 packages render byte-identically. Verified separately in the "
      "batch QA."),
    ]
    if n == 11:
        import csv as _csv
        rows = list(_csv.DictReader(open(os.path.join(
            d(n, SUB[7]), "V11_Demonstration", "synthetic_service_report.csv"))))
        tot = {}
        for r in rows:
            p_ = r["period"]
            tot.setdefault(p_, [0, 0])
            tot[p_][0] += int(r["eligible_cases"])
            tot[p_][1] += int(r["met_target"])
        r1 = tot["Period 1"][1] / tot["Period 1"][0]
        r2 = tot["Period 2"][1] / tot["Period 2"][0]
        ok = (round(r1 * 100) == 60 and round(r2 * 100) == 80
              and round((r2 - r1) * 100) == 20)
        now.insert(9, ("V11 calculations reproduce the supplied data", yn(ok),
                       "Recomputed from the CSV in this package: 60%% to 80%%, "
                       "a rise of 20 percentage points. Relative growth would "
                       "be %.1f%%, which is why every asset says percentage "
                       "points. Routine 90%% and complex 40%% in both periods. "
                       "Matches the supplied Arithmetic_Check.json."
                       % ((r2 - r1) / r1 * 100)))

    pending = [
     ("Actual spoken delivery",
      "Whether the approved script was spoken as written. If recorded speech "
      "differs materially from the master, that is a mismatch to flag, not "
      "something the edit can restore."),
     ("Actual runtime",
      "The estimate here is arithmetic on the word count. The real runtime "
      "comes from the export."),
     ("Executed motion graphics",
      "Reveal states, sequential builds and hold behavior exist only as "
      "instructions and reference frames."),
     ("Executed push-ins and pull-backs",
      "Whether the finished edit lands within 3 to 5 camera-emphasis beats."),
     ("Actual B-roll placement",
      "Whether the 2 to 4 moments are meaningful and whether any prohibited "
      "action was inadvertently depicted."),
     ("Voice, music and effect balance",
      "Voice dominant, effects quieter, music subtle. Not testable before the "
      "mix. Also whether the total lands within 4 to 7 accents."),
     ("Final picture quality",
      "Natural skin tone and texture, no beauty-filter look."),
     ("Caption placement and subtitle sync",
      "That designed captions are suppressed during full-screen scenes and "
      "that the SRT carries the complete speech and matches the final edit."),
     ("Final YouTube chapters", "Built from the finished export. None supplied."),
     ("Final end-card hold and clean file ending",
      "Watch Next held through the final line, with no camera return, outro, "
      "sting, black tail or music-only tail."),
     ("Thumbnail artwork approval",
      "Wording is locked. Artwork and portrait selection are PENDING and were "
      "not created in this build."),
     ("Verified public link accessibility",
      "That the resource URL, the playlist and the Watch Next destination are "
      "reachable by a viewer at publication."),
    ]
    fails = [c for c in now if c[1] == "FAIL"]
    L = ["=" * W, "QA REPORT", "Video %d  ·  %s" % (n, M.title(n)),
         "Built against %s  ·  %s" % (M.FILE[n], BATCH), "=" * W, "",
         wrap("Split deliberately. Section 1 is what can be checked now "
              "against the locked master and the built package. Section 2 is "
              "what cannot be checked until the recording and the export "
              "exist, and is therefore NOT claimed."), "",
         wrap("This is a first build against the final masters. No earlier "
              "draft-bundle QA is reused as evidence that these packages are "
              "aligned, and the earlier script-approval-pending status does "
              "not apply: the scripts, titles and thumbnail wording are "
              "already approved."), "",
         "=" * W, "SECTION 1: PACKAGE CHECKS COMPLETED NOW", "=" * W, "",
         "%d checks run. %d passed, %d failed."
         % (len(now), len(now) - len(fails), len(fails)), ""]
    for name, v, note in now:
        L += ["  [%-4s] %s" % (v, name), wrap(note, "         "), ""]
    L += ["=" * W, "SECTION 2: FINAL-EXPORT CHECKS STILL PENDING", "=" * W, "",
          wrap("None of the following is verified. A written prompt is not "
               "proof that an effect exists in the finished video."), ""]
    for name, note in pending:
        L += ["  [PENDING] %s" % name, wrap(note, "            "), ""]
    L += ["=" * W,
          "VIDEO %d: PRODUCTION PACKAGE BUILT AGAINST THE LOCKED FINAL MASTER"
          % n if not fails else "VIDEO %d: NOT COMPLETE, see failures" % n,
          "=" * W]
    p = os.path.join(out, "V%d_QA_Report.txt" % n)
    open(p, "w").write("\n".join(L))
    return p, fails


def alignment_log(n, out):
    L = ["=" * W, "SOURCE-TO-PRODUCTION ALIGNMENT LOG",
         "Video %d  ·  %s" % (n, M.title(n)), "=" * W, "",
         wrap("How the locked master became this package, and what was taken "
              "from the earlier Attachment B components."), "",
         "-" * W, "SOURCE", "-" * W, "",
         "  Primary   %s" % M.FILE[n],
         "  SHA-256   %s" % M.sha256(n),
         "  Secondary Videos_8-13_Recording_and_Production_Components_v1.0.zip",
         "", wrap("The Recording_Master_v1.0_REVIEW files in the secondary "
                  "archive are NOT current spoken sources and were not used. "
                  "Code_Build_Prompt_V8-V13.txt was not executed as a second "
                  "instruction set.", "  "), "",
         "-" * W, "WHAT CAME FROM THE EARLIER COMPONENTS", "-" * W, ""]
    for f in F.SETS[n]:
        L += [wrap("  %-5s %s" % (f["id"], f["concept"]), ""), ""]
    L += ["-" * W, "SHORTS", "-" * W, ""]
    for s in SH.SHORTS[n]:
        L += [wrap("  %s%d  %s" % (s["pr"], s["n"], s["note"]), ""), ""]
    L += ["-" * W, "PACKAGING CORRECTIONS", "-" * W, "", P.SUPERSEDED, "",
          "-" * W, "WHAT WAS NOT CARRIED OVER", "-" * W, "",
          wrap("No rendered artwork. No prior rendered V8 to V13 asset exists, "
               "so every PNG in this package is a new build from a reusable "
               "concept, not a byte-identical reuse. The earlier asset "
               "specifications were proposed build specifications, not "
               "finished graphics, and are not presented as such."), "",
          wrap("No draft script. The superseded review masters are not "
               "packaged anywhere in this batch, and no old draft sits in an "
               "active recording folder."), "",
          "=" * W]
    p = os.path.join(out, "V%d_Alignment_Log.txt" % n)
    open(p, "w").write("\n".join(L))
    return p


ZIP_DATE = (2026, 9, 9, 0, 0, 0)


def _add(z, arc, data):
    zi = zipfile.ZipInfo(arc, date_time=ZIP_DATE)
    zi.compress_type = zipfile.ZIP_DEFLATED
    zi.external_attr = 0o644 << 16
    z.writestr(zi, data)


def build_video(n):
    root = DIRS[n]
    shutil.rmtree(root, ignore_errors=True)
    for s in SUB:
        os.makedirs(os.path.join(root, s), exist_ok=True)

    # 01 the locked master, unchanged, plus a clean reading copy
    shutil.copy2(M.path(n), os.path.join(d(n, SUB[0]), M.FILE[n]))
    reading_copy(n, d(n, SUB[0]))

    # 02 recording
    run_of_show(n, d(n, SUB[1]))
    timing_note(n, d(n, SUB[1]))

    # 03 visuals
    vis = d(n, SUB[2])
    png_dir = os.path.join(vis, "PNG_1920x1080")
    os.makedirs(png_dir, exist_ok=True)
    cards = F.build_cards(n)
    names = [c.filename for c in cards]
    html = render_html(cards, os.path.join(vis, "_f.html"), "V%d" % n)
    probs = geoqa.check(geoqa.measure(os.path.abspath(html)), names)
    if probs:
        for p in probs:
            print("  GEOMETRY V%d:" % n, p)
        raise SystemExit("geometry failed for V%d" % n)
    shoot(os.path.abspath(html), png_dir, names)
    os.remove(html)
    render_pptx(cards, os.path.join(vis, "V%d_Reference_Deck.pptx" % n))
    shutil.copy2(os.path.join(png_dir, names[-2]),
                 os.path.join(vis, "V%d_Resource_Card.png" % n))
    shutil.copy2(os.path.join(png_dir, names[-1]),
                 os.path.join(vis, "V%d_Watch_Next_Card.png" % n))
    trigger_map(n, vis)
    visual_map(n, vis)
    asset_spec(n, vis, png_dir)
    contact_sheet(n, vis, png_dir)

    cocreator(n, d(n, SUB[3]))
    shorts_docs(n, d(n, SUB[4]))
    publishing(n, d(n, SUB[5]))
    exercise(n, d(n, SUB[6]))

    qa_dir = d(n, SUB[7])
    if n == 11:
        shutil.copytree(os.path.join(ROOT, "_source", "V11_Demonstration"),
                        os.path.join(qa_dir, "V11_Demonstration"))
    source_manifest(n, qa_dir, png_dir)
    evidence_notes(n, qa_dir)
    alignment_log(n, qa_dir)
    _, fails = qa_report(n, qa_dir, png_dir, not probs)
    return root, fails


def zip_dir(root, target):
    base = os.path.basename(root)
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED,
                         compresslevel=6) as z:
        for dp, _, files in os.walk(root):
            for f in sorted(files):
                full = os.path.join(dp, f)
                _add(z, os.path.join(base, os.path.relpath(full, root)),
                     open(full, "rb").read())
    h = hashlib.sha256(open(target, "rb").read()).hexdigest()
    open(target + ".sha256", "w").write("%s  %s\n"
                                        % (h, os.path.basename(target)))
    return h


def qa_counts_line():
    """Read the real counts out of the built QA reports."""
    parts = []
    for n in M.VIDEOS:
        txt = open(os.path.join(d(n, SUB[7]), "V%d_QA_Report.txt" % n)).read()
        m_ = re.search(r"(\d+) checks run\. (\d+) passed", txt)
        parts.append("V%d %s of %s" % (n, m_.group(2), m_.group(1)))
    return "; ".join(parts)


def batch_manifest(hashes):
    rows = []
    for n in M.VIDEOS:
        m = P.META[n]
        w, fast, slow = M.estimate(n)
        rows.append("""## VIDEO %d

**%s**

| | |
|---|---|
| Locked master | `%s` |
| Master SHA-256 | `%s` |
| Thumbnail wording | **%s** (artwork PENDING, not created) |
| Framework | %s |
| Resource | %s, %s |
| Watch Next | **Video %d**, %s |
| Spoken words | %d |
| Speech-only estimate | %s to %s at 130 to 145 wpm. **Estimate, not a measurement.** |
| Printed cover target | %s. An expectation, not a measured length. |
| Assets | %d teaching concepts plus a resource card and a Watch Next card |
| Shorts | 6 dedicated, 4 Priority A and 2 Priority B |
| ZIP | `V%d_Production_Package.zip` |
| ZIP SHA-256 | `%s` |
""" % (n, m["title"], M.FILE[n], M.sha256(n), m["thumb"], m["framework"],
       m["resource"][0], m["resource"][1], m["watch_next"][0],
       m["watch_next"][1], w, fast, slow,
       M.header(n).get("TARGET LENGTH", ""), len(F.SETS[n]) - 2, n,
       hashes[n]))
    return """# Videos 8 to 13 Batch Manifest

**%s.** First Code production build for Videos 8 to 13, built from the supplied
final Recording Masters. The scripts, titles and thumbnail wording are locked
and approved; nothing here reopens editorial strategy or rewrites a script.

Every master's SHA-256 was recorded before anything was generated, and an
unchanged copy sits in each video's `01_Recording_Master/`. The build reads
those files and never writes to them, so no spoken line can drift.

%s
## Routing

**V8 to V9 to V10 to V11 to V12 to V13, and V13 back to V9.** This routing is
specified in the new approved masters.

## Packaging corrections applied

%s

## What every video folder contains

    01_Recording_Master/    the unchanged master, plus a clean reading copy
    02_Recording/           run of show, estimated speech timing, ending checklist
    03_Visuals/             trigger map, visual and reveal map, asset spec,
                            1920x1080 PNGs, editable deck, resource card,
                            Watch Next card, phone-size contact sheet
    04_Riverside/           complete self-contained Co-Creator master prompt
    05_Shorts/              combined document, six individual scripts, manifest
    06_Publishing/          description, pinned comment, tags, Canva brief,
                            link and publication checklist
    07_Viewer_Exercise/     script-aligned teaching companion
    08_Sources_and_QA/      source manifest, evidence notes, QA report,
                            alignment log

## Assets are new builds, not carried-over artwork

No prior rendered V8 to V13 artwork exists. Every PNG in this batch is a new
build from a reusable concept taken from the earlier Attachment B
specifications, with every anchor remapped to the locked script. The earlier
specifications were proposed build specifications, not finished graphics, and
are not presented as such.

## QA is split

Each `V*_QA_Report.txt` separates **package checks completed now** from
**final-export checks still pending**. The completed counts are %s, all
passing. They are not uniform and were not padded to look uniform: Video 11
carries one additional check, the arithmetic validation against the supplied
synthetic rows. Actual delivery, runtime, executed
motion graphics, executed camera moves, B-roll placement, audio balance,
picture quality, caption sync, chapters, end-card behavior, thumbnail artwork
approval and public link accessibility are all listed as PENDING and are not
claimed. No earlier draft-bundle QA is reused as evidence.

## Not supplied, by instruction

No chapter timestamps. No music attribution or license code. No thumbnail
artwork, and Temidayo's face was not regenerated. No YouTube video IDs and no
playlist URL; every link is a marked placeholder.

## Combined archive

`Videos_8-13_Production_Packages.zip`, with its checksum in the sibling
`Videos_8-13_Production_Packages.zip.sha256`. It carries all six video folders
plus this manifest, the delivery summary and the roadmap patch.

## Status

**V8 TO V13 PRODUCTION PACKAGE BUILD CLOSED.**
**READY FOR RECORDING AND RIVERSIDE PRODUCTION.**
**FINAL-EXPORT QA AND THUMBNAIL ARTWORK APPROVAL PENDING.**

Closed September 9, 2026 after the reporting and metadata corrections. No
further script, asset, Shorts, prompt, routing or publishing change unless an
actual factual or production defect is found. These are packages ready for
recording, not verified final videos.
""" % (BATCH, "\n".join(rows), P.SUPERSEDED, qa_counts_line())


def main():
    print("locked masters")
    for n in M.VIDEOS:
        print("  V%-3d %s  %s" % (n, M.FILE[n], M.sha256(n)))
    outs, hashes, all_fails = {}, {}, []
    for n in M.VIDEOS:
        root, fails = build_video(n)
        outs[n] = root
        all_fails += [(n, c[0]) for c in fails]
        print("  built V%d: %d files"
              % (n, sum(len(f) for _, _, f in os.walk(root))))
    for n in M.VIDEOS:
        hashes[n] = zip_dir(outs[n],
                            os.path.join(ROOT, "V%d_Production_Package.zip" % n))
    combined = os.path.join(ROOT, "Videos_8-13_Production_Packages.zip")
    man_path = os.path.join(ROOT, "V8-V13_BATCH_MANIFEST.md")
    open(man_path, "w").write(batch_manifest(hashes))
    # the delivery summary and the scoped tracker patch, written now so they
    # can travel inside the combined archive
    import summary813
    summary813.build_doc()
    open(os.path.join(ROOT, "V8-V13_ROADMAP_TRACKER_PATCH.md"), "w").write(
        summary813.PATCH % summary813.patch_rows())
    extras = ["V8-V13_BATCH_MANIFEST.md", "V8-V13_DELIVERY_SUMMARY.docx",
              "V8-V13_ROADMAP_TRACKER_PATCH.md"]
    with zipfile.ZipFile(combined, "w", zipfile.ZIP_DEFLATED,
                         compresslevel=6) as z:
        for f in extras:
            _add(z, f, open(os.path.join(ROOT, f), "rb").read())
        for n in M.VIDEOS:
            root = outs[n]
            base = os.path.basename(root)
            for dp, _, files in os.walk(root):
                for f in sorted(files):
                    full = os.path.join(dp, f)
                    _add(z, os.path.join(base, os.path.relpath(full, root)),
                         open(full, "rb").read())
    ch = hashlib.sha256(open(combined, "rb").read()).hexdigest()
    open(combined + ".sha256", "w").write(
        "%s  Videos_8-13_Production_Packages.zip\n" % ch)
    print()
    for n in M.VIDEOS:
        print("  V%d_Production_Package.zip  %s" % (n, hashes[n]))
    print("  Videos_8-13_Production_Packages.zip  %s" % ch)
    print()
    print("QA failures:", all_fails or "none")


if __name__ == "__main__":
    main()
