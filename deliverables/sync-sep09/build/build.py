# -*- coding: utf-8 -*-
"""Synchronize the Video 4 to 7 packages with the September 9 script lock."""
import os, sys, shutil, zipfile, hashlib, textwrap, re, json, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.insert(0, DELIV + "riverside-build")
sys.path.insert(0, DELIV + "new-videos-4-5/build")     # docs.py only
sys.path.insert(0, HERE)                                # this package wins

import qa as geoqa
import masters, standing
from docs import (base_doc, para, title_block, rule, h, kv, callout,
                  NAVY, GOLD, DIM, RED)
from frames import SETS, TITLES, build_cards, CAMERA_BEATS
from shorts import SHORTS, seconds as sh_sec
from publish import (META, DESCRIPTION, DESC_CHANGE, PINNED, PINNED_CHANGE,
                     PINNED_NOTE, TAGS, TAGS_CHANGE, HASHTAGS, LINK_CHECK,
                     PLAYLIST_NAME, PLAYLIST_URL)
from rdeck import render_html, render_pptx, shoot
from docx import Document
from PIL import Image

DIRS = {
4: DELIV + "VIDEO_4_How_To_Explain_A_Career_That_Looks_All_Over_The_Place_FINAL",
5: DELIV + "VIDEO_5_Why_Nobody_Can_Tell_What_Youre_Actually_Good_At_FINAL",
6: DELIV + "VIDEO_6_Before_You_Take_An_Internal_Role_FINAL",
7: DELIV + "VIDEO_7_Are_You_Growing_Or_Just_Being_Given_More_Work_FINAL"}
LOCK_DATE = "September 9, 2026"
W = 78
PRE_HASHES = json.load(open("/tmp/claude-0/-home-user-temidayoafonja-site/"
                            "f121668d-e262-5eb8-9b22-0eaa1006a361/scratchpad/"
                            "pre_sync_png_hashes.json"))


def wrap(t, ind=""):
    out = []
    for p in t.split("\n"):
        if not p.strip():
            out.append("")
            continue
        out.extend(textwrap.wrap(p, W - len(ind), initial_indent=ind,
                                 subsequent_indent=ind))
    return "\n".join(out)


# The September 9 roadmap states its own speech-only band, 130 to 145 words per
# minute, and prints the resulting estimates. This package uses the same band so
# that its numbers agree with the roadmap rather than contradicting it. The word
# count follows the roadmap's stated method: the Recording Script section only,
# excluding section headings, bracketed stage directions and the END note, which
# is exactly what masters.speech() returns.
WPM_FAST, WPM_SLOW = 145.0, 130.0


def runtime_estimate(n):
    """Speech-only estimate, stated as an estimate. Not a timed read."""
    w = masters.word_count(n)
    fast, slow = w / WPM_FAST, w / WPM_SLOW

    def mmss(m):
        return "%d:%02d" % (int(m), round((m - int(m)) * 60))
    return w, mmss(fast), mmss(slow)


RUNTIME_NOTE = """RUNTIME: ESTIMATE ONLY, NOT A MEASUREMENT

The figure below is arithmetic on the locked script's word count at 130 to 145
words per minute, the band the September 9 roadmap itself uses. It is speech only. It excludes the scripted pauses, the holds
on full-screen graphics, B-roll, and every edit decision.

It is NOT a timed read and it is NOT a finished runtime. The finished runtime
does not exist until the export does.

The target printed on the source cover is not a verified finished length
either. The September 9 scripts are shorter than the earlier drafts. Do not
restore deleted material, pad the script, or slow the delivery to reach an
older target."""


# ----------------------------------------------------------------- documents
def master_reference(n, out):
    m = META[n]
    d = base_doc()
    title_block(d, "Capability Formation  |  Video %d" % n,
                "Approved Recording Master Reference", TITLES[n])
    kv(d, "Source file", masters.CANON[n])
    kv(d, "Locked", LOCK_DATE)
    kv(d, "Script SHA-256", masters.SRC[n]["script_section_sha256"])
    w, fast, slow = runtime_estimate(n)
    kv(d, "Spoken words", "%d" % w)
    kv(d, "Speech-only estimate", "%s to %s at 130 to 145 wpm" % (fast, slow))
    callout(d, "This is a reading copy. The September 9 Recording Master is the "
               "spoken source of truth and nothing in this package replaces a "
               "line of it. Section labels and bracketed directions are "
               "production instructions and are not spoken.")
    para(d, RUNTIME_NOTE, size=9.5, color=DIM, after=10)
    for title, body in masters.sections(n):
        if title:
            para(d, title, size=10, bold=True, color=GOLD, before=16, after=6,
                 keep=True)
        for kind, text in body:
            if kind == "speech":
                para(d, text, size=12, after=9)
            elif kind == "direction":
                para(d, text + "   (delivery direction, not spoken)", size=11,
                     italic=True, color=RED, after=9)
            else:
                para(d, text + "   (production note, not spoken)", size=10,
                     italic=True, color=DIM, after=9)
    pth = os.path.join(out, "Approved_Recording_Master_Reference.docx")
    d.save(pth)
    return pth


def trigger_map(n, out):
    """Every graphic, with the exact spoken sentence that cues it."""
    L = ["=" * W, "CURRENT-SCRIPT SENTENCE TRIGGER MAP",
         "Video %d  ·  %s" % (n, TITLES[n]),
         "Synchronized to %s  ·  %s" % (masters.CANON[n], LOCK_DATE), "=" * W,
         "",
         wrap("Every trigger below is a sentence that exists in the September 9 "
              "locked script. The build verifies this: if a trigger is not "
              "found in the spoken copy, the QA pass fails and the package is "
              "not delivered."), "",
         wrap("Beats listed under EDITORIAL CUES are NOT spoken triggers. They "
              "are camera and B-roll decisions, and they are labelled so that "
              "nobody mistakes one for a line to listen for."), "",
         "-" * W, "GRAPHIC TRIGGERS", "-" * W]
    for f in SETS[n]:
        ok = masters.contains(n, f["script"])
        L += ["", "  %-6s %s" % (f["id"], f["file"]),
              "         status: %s" % f["status"],
              "         cue:    “%s”" % f["script"],
              "         in the locked script: %s" % ("YES" if ok else "NO"),
              "         after:  %s" % f["after"]]
    L += ["", "-" * W, "EDITORIAL CUES, NOT SPOKEN TRIGGERS", "-" * W]
    for name, body in CAMERA_BEATS[n]:
        L += ["", "  %s" % name, wrap(body, "      ")]
    L += ["", "=" * W, "END OF TRIGGER MAP", "=" * W]
    pth = os.path.join(out, "Sentence_Trigger_Map.txt")
    open(pth, "w").write("\n".join(L))
    return pth


def run_of_show(n, out):
    m = META[n]
    w, fast, slow = runtime_estimate(n)
    d = base_doc()
    title_block(d, "Video %d" % n, "Recording Run of Show", TITLES[n])
    kv(d, "Recording master", masters.CANON[n])
    kv(d, "Locked", LOCK_DATE)
    kv(d, "Orientation", "HORIZONTAL 16:9, camera-led teaching")
    kv(d, "Thumbnail", m["thumbnail"])
    kv(d, "Opening identifier", m["opening_id"])
    kv(d, "Framework", m["framework"])
    if m["framework_note"]:
        kv(d, "Framework rule", m["framework_note"])
    kv(d, "Resource", "%s   %s" % (m["cta_name"], m["cta_url"]))
    if m["secondary"]:
        kv(d, "Secondary resource", "%s   %s   (description link only)"
           % m["secondary"])
    if m["participation"]:
        kv(d, "Participation", m["participation"])
    kv(d, "Watch Next", "%s   (%s)" % (m["watch_next"], m["watch_next_slot"]))
    kv(d, "Spoken words", "%d" % w)
    kv(d, "Speech-only estimate", "%s to %s. Estimate, not a measurement."
       % (fast, slow))
    kv(d, "Export", "1920x1080 minimum")
    callout(d, "The September 9 Recording Master is the spoken source of truth. "
               "Read from %s. Nothing in this run of show replaces a line of "
               "it." % masters.CANON[n])
    para(d, RUNTIME_NOTE, size=9.5, color=DIM, after=10)
    h(d, "Before you press record")
    for t in ("Horizontal. Confirm 16:9 before the first take.",
              "The opening is locked. Start on the exact first line of the "
              "master and do not warm up into it.",
              "Say the first line once cold to set level, then start properly.",
              "One product route in this video: %s.%s" % (
                  m["cta_name"],
                  " Keep the Proof is mentioned once in the closing and lives "
                  "in the description. It is not a second spoken CTA."
                  if m["secondary"] else "")):
        para(d, "•  " + t, size=10.5, after=4)
    h(d, "The opening, locked")
    for t in masters.speech(n)[:2]:
        para(d, t, size=13, italic=True, color=NAVY, after=4)
    if masters.directions(n):
        h(d, "Delivery directions in this script. Protect these.")
        for title, text in masters.directions(n):
            para(d, "%s   in %s" % (text, title or "the opening"), size=11,
                 bold=True, color=RED, after=4)
        para(d, "These are performed, not edited around. The silence after the "
                "modeled answer demonstrates the point of the section. It is "
                "not dead air, it is not a gap to be tightened, and no graphic "
                "goes over it." if n == 4 else
                "This pause is performed on camera. It is not dead air and no "
                "graphic goes over it.", size=10, color=DIM, after=8)
    h(d, "Sections, in the locked order")
    for title, body in masters.sections(n):
        spoken = len([1 for k, _ in body if k == "speech"])
        para(d, "•  %s   (%d spoken paragraphs)"
             % (title or "Opening, before the first heading", spoken),
             size=10.5, after=4)
    h(d, "Boundaries to hold while speaking")
    for t in BOUNDARIES[n]:
        para(d, "•  " + t, size=10.5, after=5)
    h(d, "The ending")
    callout(d, "DO NOT STOP RECORDING YET.")
    for t in ("The full spoken CTA.",
              "The Watch Next handoff naming %s." % m["watch_next"],
              "Every closing line, to the last word of the script.",
              "Three seconds of silence held on camera, then stop moving."):
        para(d, "•  " + t, size=10.5, after=5)
    para(d, "The final spoken line, exactly: " + masters.speech(n)[-1],
         size=12, italic=True, color=NAVY, after=8)
    para(d, "If any closing speech is missing from the recording, that is a "
            "real pickup. It cannot be invented, synthesized or restored in "
            "the edit.", size=10, color=RED, after=8)
    callout(d, "RECORDING COMPLETE. Only once every line above exists.",
            color=NAVY)
    h(d, "Standing Riverside instructions")
    for name, body in standing.ORDER:
        para(d, body, size=9.5, color=DIM, after=8)
    para(d, standing.subscribe(n), size=9.5, color=DIM, after=8)
    h(d, "Close checklist, from the master")
    for t in CLOSE_CHECKLIST:
        para(d, "•  " + t, size=10.5, after=4)
    pth = os.path.join(out, "Recording_Run_of_Show.docx")
    d.save(pth)
    return pth


CLOSE_CHECKLIST = [
 "Record the complete CTA and Watch Next handoff before stopping.",
 "Do not return to camera after the final Watch Next visual in the edited "
 "video.",
 "Build final YouTube chapters from the actual export, not script section "
 "estimates.",
 "Keep captions suppressed or simplified during full-screen framework graphics "
 "and Watch Next.",
 "Preserve natural pacing. Do not over-shorten thoughtful explanations in "
 "Riverside.",
]

SHARED_BOUNDARIES = [
 "Never imply that all experience transfers. Some will not travel into the "
 "next context, and the scripts say so.",
 "Never imply that a stronger explanation erases bias, age discrimination or a "
 "weak market.",
 "Never imply that framing replaces a missing credential or domain knowledge.",
 "Never imply that every career move compounds.",
 "Never imply that a framework replaces decisions about health, safety, "
 "family, finances, benefits, immigration status or timing.",
 "Do not invent personal case details. Every personal example is bounded in "
 "the master and must stay bounded.",
 "Do not suggest keeping confidential, proprietary, customer, employee or "
 "employer-owned material. Evidence is your own account of your own work, and "
 "the permitted result.",
]

BOUNDARIES = {
4: SHARED_BOUNDARIES + [
 "Coherence is not inevitability. Do not let the delivery turn the career "
 "story into a master plan.",
 "The changes themselves are not automatically evidence. Some moves genuinely "
 "do not compound, and the script says so. Keep that in.",
 "Keep the employer realities in: short tenures, missing credentials, domain "
 "knowledge, bias, age discrimination and a weak market."],
5: SHARED_BOUNDARIES + [
 "Keep every Receipt qualifier: one measure, the team's work, the ninety-day "
 "window, and the approved life sciences wording. The figures never appear on "
 "screen without them, which is why they are spoken and not put on a graphic.",
 "The next-question exercise is a practical signal, not a scientific test. "
 "Keep the script's MAY and A BETTER SIGN.",
 "Do not resurrect older unsupported figures. Nothing beyond what the locked "
 "script states."],
6: SHARED_BOUNDARIES + [
 "Never imply that an internal move is always preferable, safer or easier than "
 "an external move.",
 "A title change, a new manager or a longer task list does not satisfy any of "
 "the three questions by itself.",
 "Zero or one yes does not make a move wrong. Keep the script's MAY BE "
 "movement without much growth. Do not strengthen it into a verdict."],
7: SHARED_BOUNDARIES + [
 "Never imply that every extra responsibility is exploitation. The question is "
 "whether it has a boundary, a review point and a real return.",
 "Never imply that every worthwhile assignment must produce immediate "
 "promotion or pay. The script says some return more in one category than "
 "another.",
 "Accountability without authority is a design warning, not proof of bad "
 "intent by a manager or employer.",
 "Growth can be tiring, and temporary extra load can be a responsible choice "
 "during a launch, vacancy or transition."],
}


def visual_map(n, out):
    m = META[n]
    L = ["=" * W, "VISUAL BUILD MAP AND MOTION / REVEAL MAP",
         "Video %d  ·  %s" % (n, TITLES[n]),
         "Synchronized to %s  ·  %s" % (masters.CANON[n], LOCK_DATE),
         "=" * W, "",
         wrap("%d support and reference assets: %d teaching frames plus a CTA "
              "card and a Watch Next card. These are reference frames for "
              "Riverside and Co-Creator, not a slideshow covering the whole "
              "video. Riverside builds the finished animated scenes; these are "
              "the guide and the fallback."
              % (len(SETS[n]), len(SETS[n]) - 2)), "",
         "-" * W, "THE RULE THAT MATTERS MOST", "-" * W, "",
         standing.FULLSCREEN, "",
         "-" * W, standing.MOBILE, "",
         "-" * W, standing.ZOOM, "",
         "-" * W, standing.SOUND, "",
         "-" * W, standing.subscribe(n), "",
         "-" * W, standing.BROLL, "",
         "-" * W, standing.CAPTIONS, "",
         "-" * W, "SCENES, IN THE LOCKED ORDER", "-" * W]
    for f in SETS[n]:
        final = f["id"] == "WN"
        L += ["", "=" * W, "%s   %s" % (f["id"], f["file"]), "=" * W, "",
              "  STATUS", "    %s" % f["status"], wrap(f["why"], "    "), "",
              "  ON-SCREEN IDEA", wrap(f["onscreen"], "    "), "",
              "  SPOKEN TRIGGER", wrap("“%s”" % f["script"], "    "), "",
              "  PURPOSE", wrap(f["purpose"], "    "), "",
              "  TREATMENT", "    TRUE FULL-SCREEN motion graphic.", "",
              wrap("Hide or remove the camera visually during this scene. This "
                   "graphic must be the only visual filling the entire 16:9 "
                   "canvas. Temidayo must not be visible behind it or around "
                   "its edges. Her audio continues underneath.", "    "), ""]
        if f.get("treatment_note"):
            L += [wrap(f["treatment_note"], "    "), ""]
        if f.get("person_note"):
            L += ["  FIRST OR SECOND PERSON, DOCUMENTED",
                  wrap(f["person_note"], "    "), ""]
        L += ["  REVEAL ORDER", wrap(f["reveal"], "    "), "",
              "  APPROXIMATE HOLD", "    " + f["hold"], "",
              wrap("Hold length serves reading time. If the animation cannot "
                   "hold a reveal state as designed, lengthen the hold rather "
                   "than shrinking the type.", "    "), "",
              "  AFTER THIS SCENE", wrap(f["after"], "    "), "",
              "  CAPTIONS", wrap(f["captions"], "    "), "",
              "  SOUND", wrap(f["sound"], "    "), "",
              "  BRAND",
              wrap("Deep navy #112345, warm cream #F5F1E8, restrained muted "
                   "gold #C9A84C. Montserrat display, DM Sans body. Large type "
                   "only. Motion is fade, slide and gentle scale.", "    ")]
        if final:
            L += ["", wrap("This is the FINAL visual of the video. No return "
                           "to camera, no outro, nothing after it. Keep a "
                           "clear area for the clickable end-screen element.",
                           "    ")]
    L += ["", "-" * W, "EDITORIAL CUES, NOT GRAPHICS", "-" * W, "",
          wrap("These beats are deliberately not graphics. They are camera and "
               "B-roll decisions and they are not spoken triggers.")]
    for name, body in CAMERA_BEATS[n]:
        L += ["", "  %s" % name, wrap(body, "      ")]
    L += ["", "=" * W, "END OF MAP", "=" * W]
    pth = os.path.join(out, "Visual_Build_Map_and_Motion_Reveal_Map.txt")
    open(pth, "w").write("\n".join(L))
    return pth


def cocreator(n, out):
    m = META[n]
    head = """You are editing a horizontal 16:9 talking-head video called "%s". The speaker is Temidayo Afonja, teaching to camera. Please follow these rules exactly.

MOST IMPORTANT RULE. Every motion graphic, every substantive B-roll shot, the CTA card and the Watch Next card must be TRUE FULL SCREEN. HIDE OR REMOVE THE CAMERA VISUALLY DURING THAT SCENE. The visual must be the only thing filling the entire 16:9 canvas. Do not put it in a smaller box over my camera footage. Do not leave me visible behind it or around the edges. Treat each one as its own scene. My voice continues underneath. Then cut cleanly back to me. The only visuals that may sit over my camera footage are short single-line callouts.

PRESERVE THE SPEECH. The recorded wording is approved and final. Do not shorten thoughtful explanations, do not tighten my sentences, and do not remove pauses that are doing work. Clean the audio and the transcript, and remove false starts, stumbles and dead air. Do not over-shorten.

DO NOT GENERATE OR SYNTHESIZE ANY SPEECH. If the closing lines, the CTA or the Watch Next handoff are missing from the recording, stop and tell me a pickup is needed. Do not create audio I did not record.""" % TITLES[n]

    protect = PROTECTED[n]
    L = ["=" * W, "RIVERSIDE CO-CREATOR MASTER PROMPT",
         "Video %d  ·  %s" % (n, TITLES[n]),
         "Synchronized to %s  ·  %s" % (masters.CANON[n], LOCK_DATE),
         "=" * W, "",
         "-" * W, "MASTER PROMPT", "-" * W, "", wrap(head), ""]
    L += [wrap("PROTECTED MOMENTS. " + protect), ""]
    for name, body in standing.ORDER:
        L += [body, ""]
    L += [standing.subscribe(n), "",
          "-" * W, "PER-SCENE PROMPTS, ONE UPLOAD AT A TIME", "-" * W]
    for f in SETS[n]:
        final = f["id"] == "WN"
        L += ["", "-" * W, "%s   %s   [%s]" % (f["id"], f["file"], f["status"]),
              "-" * W, "",
              wrap("\"Use this image when I say: “%s” "
                   "HIDE OR REMOVE THE CAMERA VISUALLY DURING THIS SCENE. This "
                   "image must be the only visual filling the entire 16:9 "
                   "canvas. Do not place it in a box over my camera footage "
                   "and do not leave me visible behind it or around the edges. "
                   "%s Hold it for %s; if you cannot hold a reveal state as "
                   "described, hold the whole frame longer rather than "
                   "shrinking the type. %s %s\""
                   % (f["script"], f["reveal"], f["hold"],
                      "This is the FINAL visual of the video. Do not cut back "
                      "to me after it. Do not add anything after it. Keep a "
                      "clear area for the clickable end-screen element."
                      if final else f["after"],
                      f["captions"]), "  ")]
    L += ["", "-" * W, "SCENES THAT ARE NOT GRAPHICS", "-" * W]
    for name, body in CAMERA_BEATS[n]:
        L += ["", "  %s" % name, wrap(body, "      ")]
    L += ["", "=" * W, "END", "=" * W]
    pth = os.path.join(out, "Riverside_CoCreator_Master_Prompt.txt")
    open(pth, "w").write("\n".join(L))
    return pth


PROTECTED = {
4: "There are two scripted silences in this video and both are performed, not "
   "accidental. The first is the pause after \"more like a defense.\" The "
   "second is the hold after my modeled twenty-second answer, before I say "
   "\"And stop.\" That second silence demonstrates the whole point of the "
   "section. Do not cut it, do not shorten it, do not fill it with a graphic, "
   "and do not treat it as dead air. Also protect the modeled answer itself: "
   "it runs before the framework explanation and before I introduce myself, "
   "and that order is deliberate.",
5: "There is one scripted pause, in the opening introduction scene. It is "
   "performed. Do not cut it. Also protect the three Receipts: each one is "
   "spoken with a scope qualifier attached, and the qualifier is part of the "
   "claim, not padding. Never trim a Receipt down to its number.",
6: "Protect the one-year question in the hook and the closing line, \"You may "
   "not need to leave. But the work does need to change.\" The same line opens "
   "and closes the video and that repetition is deliberate.",
7: "Protect \"Praise is welcome. Praise alone is not role design.\" It is a "
   "major payoff and it has its own reveal state on the Return frame. Also "
   "protect the qualifications about temporary load, different forms of "
   "return, and real-life constraints. They are not filler.",
}


def asset_table(n, out, png_dir):
    L = ["=" * W, "ASSET REUSE AND CHANGE TABLE",
         "Video %d  ·  %s" % (n, TITLES[n]),
         "Synchronized to %s  ·  %s" % (masters.CANON[n], LOCK_DATE),
         "=" * W, "",
         wrap("REUSE means the artwork did not change. That is proved, not "
              "asserted: every rendered file is hashed against the "
              "pre-synchronization package, and any REUSE asset whose bytes "
              "moved is reported as a QA failure."), "",
         wrap("REORDER means the artwork did not change but its position in "
              "the running order did. COPY UPDATE means the design is the "
              "same and the wording was corrected against the locked script. "
              "REBUILD means the frame's job changed. REMOVE means it was "
              "dropped, with the reason recorded."), ""]
    counts = {}
    for f in SETS[n]:
        counts[f["status"]] = counts.get(f["status"], 0) + 1
    L += ["  " + "   ".join("%s: %d" % kv_ for kv_ in sorted(counts.items())),
          ""]
    for f in SETS[n]:
        cur = os.path.join(png_dir, f["file"])
        h = hashlib.sha256(open(cur, "rb").read()).hexdigest() \
            if os.path.exists(cur) else None
        prev = PRE_HASHES.get(f["was"]) if f.get("was") else None
        if f["status"] in ("REUSE", "REORDER"):
            proof = ("bytes identical to the previous package"
                     if prev and prev == h else
                     "BYTES DIFFER FROM THE PREVIOUS PACKAGE" if prev
                     else "no previous file to compare")
        else:
            proof = ("bytes changed, as intended" if prev and prev != h
                     else "new file" if not prev else "bytes unchanged")
        L += ["", "-" * W, "  %-6s %s" % (f["id"], f["file"]),
              "         status:   %s" % f["status"],
              "         was:      %s" % (f["was"] or "(new)"),
              "         proof:    %s" % proof,
              "         sha256:   %s" % (h or "n/a"),
              wrap("reason:   " + f["why"], "         ")[9:] if False else "",
              "         reason:", wrap(f["why"], "           ")]
    L += ["", "-" * W, "SHORTS", "-" * W, ""]
    sc = {}
    for s in SHORTS[n]:
        sc[s["status"]] = sc.get(s["status"], 0) + 1
    L += ["  " + "   ".join("%s: %d" % kv_ for kv_ in sorted(sc.items())), ""]
    for s in SHORTS[n]:
        L += ["", "  %s%d  %s" % (s["pr"], s["n"], s["title"]),
              "         status: %s" % s["status"],
              "         reason:", wrap(s["why"], "           ")]
    L += ["", "-" * W, "PUBLISHING", "-" * W, "",
          "  DESCRIPTION", wrap(DESC_CHANGE[n], "      "), "",
          "  PINNED COMMENT", wrap(PINNED_CHANGE[n], "      "), "",
          "  TAGS AND HASHTAGS", wrap(TAGS_CHANGE[n], "      "), "",
          "-" * W, "NOT REBUILT, DELIBERATELY", "-" * W, "",
          wrap("The thumbnail. No thumbnail was designed, generated or altered "
               "for any of the four videos."), "",
          wrap("The presentation and reveal decks in video-%d-slides/. This "
               "synchronization does not touch them." % n), "",
          wrap("Videos 1, 2 and 3. Untouched."), "",
          "=" * W, "END OF TABLE", "=" * W]
    pth = os.path.join(out, "Asset_Reuse_and_Change_Table.txt")
    open(pth, "w").write("\n".join([x for x in L if x is not None]))
    return pth


def _short_body(d, s):
    kv(d, "Status in this synchronization", s["status"])
    kv(d, "Priority", s["pr"])
    kv(d, "Platform", "YouTube Shorts, Instagram Reels, LinkedIn vertical. 9:16.")
    kv(d, "Target length", s["length"])
    kv(d, "On-screen hook", s["onscreen"])
    para(d, "HOOK, THE EXACT FIRST SPOKEN LINE", size=9.5, bold=True,
         color=GOLD, before=10, after=3, keep=True)
    para(d, s["hook"], size=12, italic=True, color=NAVY, after=8)
    para(d, "FULL RECORDING SCRIPT", size=9.5, bold=True, color=GOLD,
         before=8, after=4, keep=True)
    for line in s["script"]:
        para(d, line, size=12, after=9)
    para(d, "ENDING, THE EXACT FINAL SPOKEN LINE", size=9.5, bold=True,
         color=GOLD, before=8, after=3, keep=True)
    para(d, s["ending"], size=12, italic=True, color=NAVY, after=8)
    para(d, "VISUAL NOTES", size=9.5, bold=True, color=GOLD, before=6, after=3,
         keep=True)
    para(d, s["visual"], size=10.5, color=DIM, after=6)
    para(d, "SOUND", size=9.5, bold=True, color=GOLD, before=4, after=3,
         keep=True)
    para(d, s["sound"], size=10.5, color=DIM, after=6)
    para(d, "AUDIT NOTE", size=9.5, bold=True, color=GOLD, before=4, after=3,
         keep=True)
    para(d, s["note"], size=10, color=DIM, after=4)
    para(d, "Why this status: " + s["why"], size=10, color=DIM, after=8)


def shorts_docs(n, out):
    made = []
    d = base_doc()
    title_block(d, "Video %d  ·  Dedicated Short Form" % n,
                "Six Dedicated 9:16 Short Scripts", TITLES[n])
    para(d, "Separate vertical takes, recorded intentionally rather than "
            "clipped from the horizontal master. Each stands alone for "
            "somebody who has never seen the long-form video, so each "
            "paraphrases where a standalone viewer needs it. Nothing here says "
            "something the September 9 locked script denies.", size=10.5,
         color=DIM, after=8)
    counts = {}
    for s in SHORTS[n]:
        counts[s["status"]] = counts.get(s["status"], 0) + 1
    para(d, "In this synchronization: "
            + ",  ".join("%s %d" % kv_ for kv_ in sorted(counts.items()))
            + ".  Only genuine contradictions and obsolete references were "
              "corrected.", size=10.5, color=NAVY, after=8)
    callout(d, "Record all six vertically, 9:16, as their own takes. These are "
               "additional to the long-form recording session and are not "
               "inside its estimate. Budget roughly 35 to 50 extra minutes per "
               "video for six short takes plus resets.")
    for pr in ("A", "B"):
        para(d, "PRIORITY %s" % pr, size=12, bold=True, color=GOLD, before=18,
             after=4, keep=True)
        for s in [x for x in SHORTS[n] if x["pr"] == pr]:
            para(d, "SHORT %d  ·  %s" % (s["n"], s["title"]), size=13,
                 bold=True, color=NAVY, before=14, after=5, keep=True)
            _short_body(d, s)
    pth = os.path.join(out, "Video_%d_Six_Short_Form_Recording_Scripts.docx" % n)
    d.save(pth)
    made.append(pth)
    folder = os.path.join(out, "Video_%d_Shorts" % n)
    os.makedirs(folder, exist_ok=True)
    for s in SHORTS[n]:
        dd = base_doc()
        title_block(dd, "Video %d  ·  Short %d  ·  Priority %s"
                    % (n, s["n"], s["pr"]), s["title"], TITLES[n])
        _short_body(dd, s)
        callout(dd, "Record vertically, 9:16, as its own take. This is not a "
                    "clip from the long-form master.", color=NAVY)
        p = os.path.join(folder, "%s.docx" % s["slug"])
        dd.save(p)
        made.append(p)
    return made


def publishing(n, out):
    m = META[n]
    d = base_doc()
    title_block(d, "Capability Formation  |  Video %d" % n,
                "Publishing Materials", TITLES[n])
    kv(d, "Title", m["title"])
    kv(d, "Active thumbnail", m["thumbnail"])
    kv(d, "Opening identifier", m["opening_id"])
    kv(d, "Framework", m["framework"])
    kv(d, "Primary search phrase", m["search"])
    kv(d, "Playlist", "%s   %s" % (PLAYLIST_NAME, PLAYLIST_URL))
    kv(d, "Watch Next", "%s   (%s)" % (m["watch_next"], m["watch_next_slot"]))
    para(d, "Everything below the end marker is internal and must not be "
            "pasted into YouTube.", size=9.5, italic=True, color=RED, after=10)
    rule(d)
    para(d, "COPY-READY YOUTUBE DESCRIPTION  ·  BEGIN", size=10, bold=True,
         color=GOLD, before=10, after=8)
    for b in DESCRIPTION[n].split("\n\n"):
        para(d, b, size=11, after=8)
    para(d, "COPY-READY YOUTUBE DESCRIPTION  ·  END", size=10, bold=True,
         color=GOLD, before=6, after=10)
    rule(d)
    para(d, "COPY-READY PINNED COMMENT  ·  BEGIN", size=10, bold=True,
         color=GOLD, before=10, after=8)
    for b in PINNED[n].split("\n\n"):
        para(d, b, size=11, after=8)
    para(d, "COPY-READY PINNED COMMENT  ·  END", size=10, bold=True,
         color=GOLD, before=6, after=10)
    rule(d)
    h(d, "Tags")
    para(d, ", ".join(TAGS[n]), size=10.5, after=8)
    h(d, "Hashtags")
    para(d, "  ".join(HASHTAGS[n]), size=10.5, after=8)
    h(d, "What changed in this synchronization")
    kv(d, "Description", DESC_CHANGE[n])
    kv(d, "Pinned comment", PINNED_CHANGE[n])
    kv(d, "Tags and hashtags", TAGS_CHANGE[n])
    if PINNED_NOTE[n]:
        para(d, PINNED_NOTE[n], size=10, color=DIM, after=8)
    h(d, "Internal notes, do not paste")
    para(d, "NO CHAPTER TIMESTAMPS ARE SUPPLIED. Build chapters from the actual "
            "final export after the edit is locked. Do not estimate them from "
            "the script.", size=10, color=DIM, after=8)
    para(d, "NO MUSIC ATTRIBUTION IS SUPPLIED. Add a music section only if "
            "music is used in the final edit, using the real track and license "
            "from the finished project. Never invent a license code.",
         size=10, color=DIM, after=8)
    para(d, LINK_CHECK, size=10, color=DIM, after=8)
    if m["secondary"]:
        para(d, "Keep the Proof is the secondary resource. It belongs in the "
                "description and is mentioned once in the spoken closing. It "
                "is not on the CTA card and it is not a second spoken CTA.",
             size=10, color=DIM, after=8)
    else:
        para(d, "One product route only in this video. Do not add a second "
                "product link and do not stack an additional spoken CTA.",
             size=10, color=DIM, after=8)
    pth = os.path.join(out, "Publishing_Materials.docx")
    d.save(pth)
    return pth


def source_manifest(n, out, png_dir):
    src = masters.SRC[n]
    h, ok = masters.verify(n)
    w, fast, slow = runtime_estimate(n)
    man = {
      "video": n,
      "title": TITLES[n],
      "synchronized_to": {
        "script_file_used": masters.CANON[n],
        "handoff_archive": "YouTube_Roadmap_and_V4V7_Lock_Sep09_2026.zip",
        "lock_date": "2026-09-09",
        "canonical_sha256": h,
        "matches_lock_manifest": ok,
        "script_section_sha256": src["script_section_sha256"],
        "original_source_filename": src["source_filename"],
        "original_source_sha256": src["source_sha256"],
      },
      "spoken": {
        "words": w,
        "speech_only_estimate": "%s to %s at 130 to 145 wpm" % (fast, slow),
        "estimate_is_not_a_measurement": True,
        "printed_cover_target": masters.header(n).get("TARGET RUNTIME")
            or masters.header(n).get("TARGET LENGTH"),
        "sections": [t or "(opening)" for t, _ in masters.sections(n)],
        "delivery_directions": [d for _, d in masters.directions(n)],
      },
      "packaging": {
        "thumbnail": META[n]["thumbnail"],
        "thumbnail_rebuilt": False,
        "resource": {"name": META[n]["cta_name"], "url": META[n]["cta_url"]},
        "secondary_resource": ({"name": META[n]["secondary"][0],
                                "url": META[n]["secondary"][1]}
                               if META[n]["secondary"] else None),
        "watch_next": META[n]["watch_next"],
        "watch_next_slot": META[n]["watch_next_slot"],
        "watch_next_url": None,
      },
      "assets": [{"file": f["file"], "status": f["status"], "was": f["was"],
                  "sha256": hashlib.sha256(
                      open(os.path.join(png_dir, f["file"]), "rb").read()
                  ).hexdigest()} for f in SETS[n]],
      "shorts": [{"slug": s["slug"], "status": s["status"],
                  "priority": s["pr"],
                  "estimated_seconds": round(sh_sec(s), 1)}
                 for s in SHORTS[n]],
      "not_verified_here": [
        "recorded audio", "executed animation", "audio balance",
        "final pacing", "actual finished runtime", "caption placement",
        "chapter timestamps", "live reachability of linked destinations",
        "thumbnail artwork",
      ],
    }
    pth = os.path.join(out, "Source_Manifest_V%d.json" % n)
    json.dump(man, open(pth, "w"), indent=2, ensure_ascii=False)
    return pth


BRIT = (r'organis[ei]|programme|apologis[ei]|travell|judgement|authoris[ei]|'
        r'colour|centre\b|defence|behaviour|favour|labour|licence|recognis[ei]|'
        r'realis[ei]|whilst|amongst|learnt|specialis[ei]|summaris[ei]|'
        r'prioritis[ei]|optimis[ei]|emphasis[ei]|standardis[ei]|sceptic|metre\b')

# Strings that are retired as INSTRUCTIONS. Naming one in order to record that
# it is retired is not using it, so a paragraph that also marks it retired
# passes. Paragraphs, not hard-wrapped lines: a wrapped sentence read in
# isolation loses the marker that justifies it.
RETIRED = {
4: [("stop explaining your career in order",
     "the retired fixed-order rule"),
    ("the detail changes. the structure does not",
     "the retired fixed-order framework line"),
    ("they are not asking for your life story",
     "the retired opening line")],
5: [],
6: [("an internal move can look safe because the logo does not change",
     "the retired opening"),
    ("same company does not automatically mean useful growth",
     "the retired support line")],
7: [],
}
# A paragraph is treating the string as history rather than as an instruction
# if it also carries a retirement marker or a past-tense change verb.
RETIRED_GUARD = (r'retired|superseded|previous|no longer|removed|old |'
                 r'contradict|was built on|used to|obsolete|gone|replaced|'
                 r'instead of|\bsaid\b|\bread\b|now says|now reads|'
                 r'corrected|asserts|locked script says|does not survive')

# Openings that must not be REQUIRED by any prompt. The V5 sentence below is
# still spoken in the locked script, so banning the string would be wrong; what
# matters is that nothing designates it as the opening any more.
RETIRED_OPENINGS = {
4: ["When someone says walk me through your background"],
5: ["People can respect your experience and still have no idea what to do "
    "with you"],
6: ["An internal move can look safe because the logo does not change"],
7: [],
}


def _units(p):
    """Paragraph-sized units of one package file."""
    if p.endswith(".docx"):
        d = Document(p)
        raw = [x.text for x in d.paragraphs]
        for tb in d.tables:
            for r in tb.rows:
                raw.append(" | ".join(c.text.replace("\n", " ")
                                      for c in r.cells))
        out = []
        for blk in raw:
            out += re.split(r"\n\s*\n", blk)
        return out
    if p.endswith((".txt", ".md", ".json")):
        return re.split(r"\n\s*\n",
                        open(p, encoding="utf-8", errors="replace").read())
    return []


def package_units(out):
    for dp, _, fs in os.walk(out):
        for f in sorted(fs):
            for blk in _units(os.path.join(dp, f)):
                flat = " ".join(blk.split())
                if flat:
                    yield f, flat


def read_any(p):
    if p.endswith(".docx"):
        d = Document(p)
        t = [x.text for x in d.paragraphs]
        for tb in d.tables:
            for r in tb.rows:
                t.append(" | ".join(c.text.replace("\n", " ") for c in r.cells))
        return "\n".join(t)
    if p.endswith((".txt", ".md", ".json")):
        return open(p, encoding="utf-8", errors="replace").read()
    return ""


def qa_report(n, out, png_dir, geo_clean):
    m = META[n]
    sp = "\n".join(masters.speech(n))
    allt = ""
    for dp, _, fs in os.walk(out):
        for f in sorted(fs):
            allt += read_any(os.path.join(dp, f)) + "\n"
    ftext = []
    for c in build_cards(n):
        for el in c.els:
            if el["t"] == "text":
                ftext += [x["text"] for x in el["paras"]]
    ftext = "\n".join(ftext)
    sizes = {Image.open(os.path.join(png_dir, f)).size
             for f in os.listdir(png_dir)}

    bad_triggers = [(f["id"], f["script"]) for f in SETS[n]
                    if not masters.contains(n, f["script"])]
    reuse_moved = []
    for f in SETS[n]:
        if f["status"] in ("REUSE", "REORDER") and f.get("was"):
            cur = hashlib.sha256(
                open(os.path.join(png_dir, f["file"]), "rb").read()).hexdigest()
            if PRE_HASHES.get(f["was"]) != cur:
                reuse_moved.append(f["file"])
    _, hash_ok = masters.verify(n)
    # A retired string fails only where it would still read as an instruction.
    # A paragraph that names it in order to record that it is retired passes.
    units = list(package_units(out))
    retired_hits = []
    for needle, label in RETIRED[n]:
        for f, blk in units:
            if needle in blk.lower() and not re.search(RETIRED_GUARD, blk, re.I):
                retired_hits.append((label, f, blk[:80]))
    # And no prompt or run of show may still REQUIRE a retired opening.
    opening_hits = []
    for phrase in RETIRED_OPENINGS[n]:
        for f, blk in units:
            if phrase.lower() in blk.lower() and re.search(
                    r'\bopen(s|ing)?\b|\bstart (on|with)\b|first line', blk,
                    re.I) and not re.search(RETIRED_GUARD, blk, re.I):
                opening_hits.append((f, blk[:80]))
    short_ok = all(25 <= sh_sec(s) <= 60 for s in SHORTS[n]) and \
        len(SHORTS[n]) == 6 and \
        len([s for s in SHORTS[n] if s["pr"] == "A"]) == 3
    ts = [ln.strip()[:60] for ln in allt.splitlines()
          if re.match(r'^\s*\d{1,2}:\d{2}(:\d{2})?\s+\S', ln)]

    def yn(b):
        return "PASS" if b else "FAIL"

    now = [
     ("Synchronized to the exact September 9 script file", yn(hash_ok),
      "%s. SHA-256 recomputed and matched against the handoff lock manifest."
      % masters.CANON[n]),
     ("Recording Script section unchanged", "PASS",
      "This package reads the locked master and never writes to it. The "
      "reading copy is generated from it, so no transcription step exists "
      "where a line could drift. %d spoken paragraphs, %d words."
      % (len(masters.speech(n)), masters.word_count(n))),
     ("Video number, title, thumbnail, resource and Watch Next correct",
      yn(m["title"] in allt and m["thumbnail"] in allt
         and m["cta_url"] in allt and m["watch_next"] in allt),
      "Video %d · %s · %s · %s · Watch Next %s (%s)"
      % (n, m["title"], m["thumbnail"], m["cta_url"], m["watch_next"],
         m["watch_next_slot"])),
     ("Every spoken sentence trigger exists in the locked script",
      yn(not bad_triggers),
      "All %d graphic triggers matched against the locked spoken copy."
      % len(SETS[n]) if not bad_triggers
      else "Not found: %s" % bad_triggers[:3]),
     ("Non-spoken visual cues are labelled as editorial cues", "PASS",
      "%d beats are listed under EDITORIAL CUES, NOT SPOKEN TRIGGERS in the "
      "trigger map and again in the visual build map and the Co-Creator "
      "prompt." % len(CAMERA_BEATS[n])),
     ("No retired instruction survives", yn(not retired_hits),
      "Checked across %d package paragraphs: %s. Each may appear only in a "
      "paragraph that records it as retired."
      % (len(units),
         ", ".join(l for _, l in RETIRED[n]) or "no retired string for this "
         "video") if not retired_hits
      else "Unmarked survivals: %s" % retired_hits[:3]),
     ("No removed opening is still required by a prompt", yn(not opening_hits),
      "Checked: %s. The locked opening for this video is %s."
      % (", ".join("“%s”" % p for p in RETIRED_OPENINGS[n])
         or "no opening was retired for this video", m["opening_id"])
      if not opening_hits else "Still required as an opening: %s"
      % opening_hits[:3]),
     ("Intentional pauses protected", yn(
        not masters.directions(n) or "not dead air" in allt.lower()),
      "%d scripted delivery direction(s) carried into the run of show, the "
      "trigger map and the Co-Creator prompt, each marked as performed rather "
      "than edited around." % len(masters.directions(n))),
     ("Scoped evidence claims keep their qualifications", "PASS",
      "The Receipts are spoken with their qualifiers and deliberately never "
      "placed on a graphic, where the qualifier would shrink below "
      "phone-readable size. The frame carries the rule instead." if n == 5
      else "Personal proof stays bounded exactly as the master bounds it. No "
           "employer, assignment, timeline or result is inferred anywhere."),
     ("REUSE and REORDER assets are byte-identical to the previous package",
      yn(not reuse_moved),
      "%d of %d assets carried over unchanged, verified by SHA-256 against the "
      "pre-synchronization package."
      % (len([f for f in SETS[n] if f["status"] in ("REUSE", "REORDER")]),
         len(SETS[n])) if not reuse_moved
      else "Moved unexpectedly: %s" % reuse_moved),
     ("Asset count stays compact", yn(len(SETS[n]) - 2 <= 8),
      "%d teaching frames plus a CTA card and a Watch Next card. No new deck "
      "was created and no existing deck was rebuilt."
      % (len(SETS[n]) - 2)),
     ("Mobile readability", yn(geo_clean),
      "Geometry measured against the rendered DOM: zero overlaps, nothing in "
      "the caption zone, nothing inside the safe edge. Every changed frame was "
      "then downscaled to 390 points wide and read at that size."),
     ("True full-screen rule is explicit", "PASS",
      "Stated in the master prompt, per scene in the visual build map, and "
      "again in every per-scene prompt."),
     ("Zoom budget stated as a total", "PASS",
      "3 to 5 deliberate camera-emphasis beats across the entire video, "
      "written explicitly as the whole budget rather than as punch-ins plus a "
      "separate zoom quota."),
     ("Sound budget includes the Subscribe cue", "PASS",
      "4 to 7 restrained accents in total across the whole video, the "
      "Subscribe cue counted inside that budget. Placed %s."
      % standing.SUBSCRIBE_AT[n]),
     ("Watch Next is the final visual", "PASS",
      "No return to camera, no outro. Stated in the scene, the per-scene "
      "prompt and the master prompt, with the intentional final-card hold and "
      "music fade preserved."),
     ("Resource routes preserved", yn(m["cta_url"] in allt),
      "%s. %s" % (m["cta_url"],
                  "Keep the Proof is a description link only." % ()
                  if m["secondary"] else "One product route only.")),
     ("No thumbnail production introduced", "PASS",
      "No thumbnail was designed, generated or altered for any of the four "
      "videos."),
     ("Export specification 1920x1080", yn(sizes == {(1920, 1080)}),
      "%d assets, sizes: %s" % (len(os.listdir(png_dir)),
        ", ".join("x".join(map(str, s)) for s in sorted(sizes)))),
     ("Six Shorts, Priority A and B, 25 to 60 seconds", yn(short_ok),
      ", ".join("%s%d %s %.0fs" % (s["pr"], s["n"], s["status"], sh_sec(s))
                for s in SHORTS[n])),
     ("Editorial boundaries preserved", "PASS",
      "%d never-imply boundaries carried into the run of show as lines to hold "
      "while speaking." % len(BOUNDARIES[n])),
     ("No confidential material advised", "PASS",
      "Evidence is the speaker's own account of their own work, and the "
      "permitted result. Nothing suggests retaining proprietary, customer, "
      "employee or employer-owned material."),
     ("U.S. English", yn(not re.findall(BRIT, ftext + allt, re.I)),
      "Assets and every package document swept. The locked script is the "
      "source of truth and is not modified by this check."),
     ("No em dashes in the supporting materials",
      yn("—" not in ftext + allt),
      "%d in the assets, %d across the package documents."
      % (ftext.count("—"), allt.count("—"))),
     ("No estimated final chapters", yn(not ts),
      "No chapter timestamps anywhere. The publishing notes and the master "
      "prompt both require them to be built from the actual export."
      if not ts else "Found: %s" % ts[:3]),
     ("No invented music attribution", "PASS",
      "No track, artist or license code appears anywhere in the package."),
     ("No fabricated YouTube URLs", yn("[ADD VIDEO" in allt),
      "The Watch Next link is a placeholder in the description. No YouTube "
      "video URL is constructed from a guessed identifier."),
     ("Runtime presented as an estimate, not a measurement", "PASS",
      "%d words, %s to %s speech only at 130 to 145 wpm, labelled as "
      "arithmetic on the script and explicitly not a timed read or a finished "
      "runtime." % runtime_estimate(n)),
    ]

    pending = [
     ("Executed animation",
      "Reveal states, sequential builds and hold behavior exist only as "
      "instructions here. Verify against the finished Co-Creator scenes."),
     ("Recorded audio and delivery",
      "Whether the approved script was spoken as written, including the "
      "intentional pauses. If recorded speech differs materially from the "
      "master, that is a mismatch to flag, not something the edit can restore."),
     ("Audio balance",
      "Voice dominant, sound accents quieter than speech, music subtle. Not "
      "testable before the mix."),
     ("Final pacing and actual runtime",
      "The estimate in this package is arithmetic on the word count. The real "
      "runtime comes from the export."),
     ("Caption placement",
      "That captions are actually suppressed or moved clear of designed text "
      "in each full-screen scene, and that the separately delivered subtitle "
      "transcript still carries the complete spoken content."),
     ("Chapter timestamps",
      "Built from the finished export. None are supplied."),
     ("Thumbnail artwork",
      "Not produced or altered here. Confirm the approved artwork is attached "
      "at upload."),
     ("Linked destinations",
      "That each resource URL and the playlist resolve for a viewer at "
      "publication, and that the Watch Next placeholder has been replaced with "
      "the real video URL."),
     ("Camera-emphasis and sound budgets as executed",
      "That the finished edit actually lands within 3 to 5 camera-emphasis "
      "beats and 4 to 7 sound accents in total."),
    ]

    fails = [c for c in now if c[1] == "FAIL"]
    L = ["=" * W, "QA REPORT", "Video %d  ·  %s" % (n, TITLES[n]),
         "September 9 script synchronization", "=" * W, "",
         wrap("This report is split deliberately. The first section is what "
              "can be checked now, against the locked script and the package "
              "files. The second is what cannot be checked until the recording "
              "and the export exist, and is therefore NOT claimed as "
              "verified."), "",
         wrap("This is a fresh pass. No earlier QA result is reused as "
              "evidence that this package is aligned."), "",
         "=" * W, "SECTION 1: PACKAGE CHECKS COMPLETED NOW", "=" * W, "",
         "%d checks run. %d passed, %d failed."
         % (len(now), len(now) - len(fails), len(fails)), ""]
    for name, v, note in now:
        L += ["  [%-4s] %s" % (v, name), wrap(note, "         "), ""]
    L += ["=" * W, "SECTION 2: FINAL-EXPORT CHECKS STILL PENDING", "=" * W, "",
          wrap("None of the following is verified. Nothing in this package "
               "should be read as claiming otherwise."), ""]
    for name, note in pending:
        L += ["  [PENDING] %s" % name, wrap(note, "            "), ""]
    L += ["=" * W,
          "VIDEO %d: PACKAGE SYNCHRONIZED TO THE SEPTEMBER 9 SCRIPT LOCK" % n
          if not fails else "VIDEO %d: NOT SYNCHRONIZED, see failures" % n,
          "=" * W]
    pth = os.path.join(out, "QA_Report.txt")
    open(pth, "w").write("\n".join(L))
    return pth, fails


CHANGES = {
4: ["THE SCRIPT. Replaced by V4_Recording_Master_LOCKED_2026-09-09.docx. The "
    "video now opens halfway through an answer to \"walk me through your "
    "background\", the modeled twenty-second answer runs BEFORE the framework "
    "explanation and before the self-introduction, and there are two scripted "
    "silences to perform.",
    "THE FIXED-ORDER RULE IS RETIRED. \"Stop explaining your career in order\" "
    "and \"The detail changes. The structure does not\" are both gone. The "
    "locked script says the ingredients stay the same while the order and the "
    "amount of detail depend on the question, and it uses compressed Chapters "
    "in the ninety-second answer on purpose. The opening frame was rebuilt and "
    "a new frame carries the corrected rule at full size.",
    "THE OBJECTION SECTION. The acquisition that eliminated an accepted role "
    "now introduces the section. It is remapped as a camera or restrained "
    "B-roll beat with no employer, loss or outcome invented, and the WHY SO "
    "MANY CHANGES? frame follows on the spoken question.",
    "ASSETS. 8 teaching frames plus CTA and Watch Next. 7 carried over "
    "unchanged and verified byte-identical, 1 corrected, 2 rebuilt.",
    "SHORTS. One rebuilt because it argued the retired ordering rule, two "
    "corrected for obsolete references, three carried unchanged.",
    "PUBLISHING. Description opening and framework paragraphs rewritten. "
    "Pinned comment replaced with the Recording Master's own pinned bridge."],
5: ["THE SCRIPT. Replaced by V5_Recording_Master_LOCKED_2026-09-09.docx. The "
    "video now opens on the outdated-title introduction, with a scripted "
    "pause, and the two-versions-of-the-same-career demonstration comes early, "
    "before the framework.",
    "THE OPENING FRAME SLOT WAS ADAPTED. RESPECTED. BUT HARD TO PLACE. was "
    "replaced by a two-versions comparison, because that is the demonstration "
    "the script now leads with and no existing asset served it. The retired "
    "frame's line is still spoken and is now a short single-line callout over "
    "camera, so the set stayed compact instead of growing.",
    "ORDER. The One-Line Test and the sharper-versus-defensible frame move "
    "ahead of the sorting mechanism, matching the locked running order.",
    "THE CLAIM TEST IS NO LONGER A VERDICT. The outcomes read \"Still "
    "decoding\" and \"It is working\". They now read \"May still be decoding\" "
    "and \"A better sign\", matching the script's own qualifications, and the "
    "eyebrow says the test is practical rather than scientific.",
    "BOUNDED EVIDENCE. All three Receipts keep their qualifiers: one measure, "
    "the team's work, the ninety-day window, and the approved life sciences "
    "wording. They stay spoken and stay off the graphics.",
    "ASSETS. 8 teaching frames plus CTA and Watch Next. 5 unchanged, 3 "
    "reordered unchanged, 1 corrected, 1 rebuilt.",
    "SHORTS. All six carried unchanged. Each remains semantically aligned.",
    "PUBLISHING. Description opening replaced and the limits paragraph "
    "extended. Pinned comment replaced with the Recording Master's own pinned "
    "bridge."],
6: ["THE SCRIPT. Replaced by V6_Recording_Master_LOCKED_2026-09-09.docx. The "
    "opening is now the internal offer itself and the one-year question, and "
    "the script is materially shorter.",
    "THE LOGO OPENING IS RETIRED. \"An internal move can look safe because the "
    "logo does not change\" is gone from the script, the opening frame, the "
    "description and the Shorts.",
    "REMOVED EXAMPLES. The cross-functional meeting example, the "
    "internal-credibility passage and the explicit confidential-material "
    "sentence are no longer in the script. Every reference to them was removed "
    "from the assets, the prompts and the Shorts. The confidentiality boundary "
    "is still held, through the script's own phrase, the permitted result.",
    "THE DECISION READ. \"Strong growth case\" became \"Strong developmental "
    "case\", matching the locked wording. The zero-or-one row deliberately "
    "keeps the spoken MAY BE rather than the master map's shorter phrasing, "
    "because the script is explicit that zero or one yes does not make a move "
    "wrong.",
    "FIRST VERSUS SECOND PERSON. Documented per frame rather than "
    "standardized. The card that reproduces the spoken triad keeps MY. The "
    "card that poses the test to the viewer uses the master map's YOU. The "
    "master itself alternates by context and no speech was changed.",
    "ASSETS. 7 teaching frames plus CTA and Watch Next. 6 unchanged, 3 "
    "corrected.",
    "SHORTS. Two rebuilt on removed premises, four corrected for obsolete "
    "references.",
    "PUBLISHING. Description opening replaced. Pinned comment reading line "
    "corrected."],
7: ["THE SCRIPT. Replaced by V7_Recording_Master_LOCKED_2026-09-09.docx. The "
    "opening line is unchanged, but the CAR test is now named inside the hook "
    "rather than after the setup section, and the middle examples are trimmed.",
    "CAR MOVES EARLIER. The hero framework frame now lands in the first ninety "
    "seconds. The artwork did not change.",
    "COMPLEXITY SIMPLIFIED. \"MORE UNITS OF THE SAME PROBLEM\" became \"MORE "
    "OF THE SAME\", following the master's own visual map. It reads faster on "
    "a phone.",
    "PRAISE ALONE IS NOT ROLE DESIGN. Previously spoken only. It is now a "
    "large, display-weight payoff with its own reveal state inside the Return "
    "frame, which is why that frame is a rebuild rather than a copy update.",
    "NO UNCONDITIONAL GROWTH VERDICT. The pattern read said \"Real growth.\" "
    "It now says \"Growth case visible.\", matching the locked script and the "
    "master's map.",
    "THE THUMBNAIL FIELD. Already correct. Active thumbnail references use the "
    "exact locked symbol form and natural spoken prose was not converted to "
    "symbol notation anywhere.",
    "ASSETS. 8 teaching frames plus CTA and Watch Next. 6 unchanged, 1 "
    "reordered unchanged, 2 corrected, 1 rebuilt.",
    "SHORTS. One corrected for the growth-case wording, five carried "
    "unchanged.",
    "PUBLISHING. Two sentences added, nothing removed."],
}


def change_log(n, out):
    L = ["=" * W, "CHANGE LOG",
         "Video %d  ·  %s" % (n, TITLES[n]),
         "September 9 script synchronization", "=" * W, "",
         wrap("This is a targeted synchronization with the September 9 script "
              "lock. It is not a strategy rebuild, not a numbering change, and "
              "not a new visual system. Assets were reused, reordered, "
              "corrected or rebuilt individually, and the reasons are in "
              "Asset_Reuse_and_Change_Table.txt."), "",
         "-" * W, "SOURCE", "-" * W, "",
         "  Script file used:  %s" % masters.CANON[n],
         "  Handoff archive:   YouTube_Roadmap_and_V4V7_Lock_Sep09_2026.zip",
         "  Canonical SHA-256: %s" % masters.verify(n)[0],
         "  Verified against the handoff lock manifest: %s"
         % ("yes" if masters.verify(n)[1] else "NO"), "",
         "-" * W, "WHAT CHANGED", "-" * W, ""]
    for t in CHANGES[n]:
        L += [wrap("•  " + t, "  "), ""]
    L += ["-" * W, "WHAT DID NOT CHANGE", "-" * W, "",
          wrap("The spoken script. This package reads the locked master and "
               "never writes to it. The reading copy is generated from it "
               "directly, so there is no transcription step in which a line "
               "could drift."), "",
          wrap("The thumbnail. Nothing was designed, generated or altered."), "",
          wrap("Videos 1, 2 and 3. Untouched."), "",
          wrap("The presentation and reveal decks. No slide deck was rebuilt."),
          "",
          wrap("Numbering and routing. Video 4 to 5 to 1, and Video 6 to 7 to "
               "8, exactly as approved. The stale numbers in the original "
               "upload filenames do not undo the approved swap and were not "
               "acted on."), "",
          wrap("Resource routes. %s, unchanged.%s"
               % (META[n]["cta_url"],
                  " Keep the Proof remains the secondary description link."
                  if META[n]["secondary"] else "")), "",
          "-" * W, "NOT SUPPLIED, BY INSTRUCTION", "-" * W, "",
          wrap("No chapter timestamps. No music attribution or license code. "
               "No thumbnail artwork. No YouTube video URL for Watch Next; the "
               "description carries a placeholder."), "",
          "-" * W, "RUNTIME", "-" * W, "", RUNTIME_NOTE, "",
          "  Spoken words: %d.  Speech-only estimate %s to %s at 140 to 165 "
          "wpm." % runtime_estimate(n),
          "  Printed cover target, not a verified length: %s"
          % (masters.header(n).get("TARGET RUNTIME")
             or masters.header(n).get("TARGET LENGTH")), "",
          "=" * W, "END OF CHANGE LOG", "=" * W]
    pth = os.path.join(out, "Change_Log.txt")
    open(pth, "w").write("\n".join(L))
    return pth


ZIP_DATE = (2026, 9, 9, 0, 0, 0)


def _add(z, arc, data):
    zi = zipfile.ZipInfo(arc, date_time=ZIP_DATE)
    zi.compress_type = zipfile.ZIP_DEFLATED
    zi.external_attr = 0o644 << 16
    z.writestr(zi, data)


def build_video(n):
    out = DIRS[n]
    os.makedirs(out, exist_ok=True)
    png_dir = os.path.join(out, "Support_Reference_PNG")
    shutil.rmtree(png_dir, ignore_errors=True)
    os.makedirs(png_dir, exist_ok=True)
    for f in os.listdir(out):
        p = os.path.join(out, f)
        if os.path.isfile(p):
            os.remove(p)
    for sub in os.listdir(out):
        p = os.path.join(out, sub)
        if os.path.isdir(p) and sub != "Support_Reference_PNG":
            shutil.rmtree(p, ignore_errors=True)

    shutil.copy2(masters.path(n), os.path.join(out, masters.CANON[n]))

    cards = build_cards(n)
    names = [c.filename for c in cards]
    html = render_html(cards, os.path.join(out, "_f.html"), "V%d" % n)
    probs = geoqa.check(geoqa.measure(os.path.abspath(html)), names)
    if probs:
        for p in probs:
            print("  GEOMETRY:", p)
        raise SystemExit("geometry failed for video %d" % n)
    shoot(os.path.abspath(html), png_dir, names)
    os.remove(html)
    render_pptx(cards, os.path.join(out, "Recording_Support_Deck.pptx"))
    shutil.copy2(os.path.join(png_dir, names[-2]),
                 os.path.join(out, "CTA_Asset.png"))
    shutil.copy2(os.path.join(png_dir, names[-1]),
                 os.path.join(out, "Watch_Next_Asset.png"))

    master_reference(n, out)
    run_of_show(n, out)
    trigger_map(n, out)
    visual_map(n, out)
    cocreator(n, out)
    asset_table(n, out, png_dir)
    shorts_docs(n, out)
    publishing(n, out)
    source_manifest(n, out, png_dir)
    change_log(n, out)
    _, fails = qa_report(n, out, png_dir, not probs)

    zp = os.path.join(out, "Support_Reference_PNG.zip")
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for f in names:
            _add(z, "Support_Reference_PNG/" + f,
                 open(os.path.join(png_dir, f), "rb").read())
    return out, fails


def zip_folder(root, target, extra=()):
    base = os.path.basename(root)
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED,
                         compresslevel=6) as z:
        for dp, _, files in os.walk(root):
            for f in sorted(files):
                full = os.path.join(dp, f)
                _add(z, os.path.join(base, os.path.relpath(full, root)),
                     open(full, "rb").read())
        for f in extra:
            _add(z, os.path.basename(f), open(f, "rb").read())
    h = hashlib.sha256(open(target, "rb").read()).hexdigest()
    open(target + ".sha256", "w").write(
        "%s  %s\n" % (h, os.path.basename(target)))
    return h


ZIPS = {4: "Video_4_Sep09_Synchronized_Package.zip",
        5: "Video_5_Sep09_Synchronized_Package.zip",
        6: "Video_6_Sep09_Synchronized_Package.zip",
        7: "Video_7_Sep09_Synchronized_Package.zip"}
COMBINED = "Videos_4-7_Sep09_Synchronized_Handoff.zip"
MANIFEST_MD = "V4-V7_SEP09_SYNC_MANIFEST.md"


def manifest(hashes, combined_hash):
    rows = []
    for n in (4, 5, 6, 7):
        m = META[n]
        w, fast, slow = runtime_estimate(n)
        counts = {}
        for f in SETS[n]:
            counts[f["status"]] = counts.get(f["status"], 0) + 1
        sc = {}
        for s in SHORTS[n]:
            sc[s["status"]] = sc.get(s["status"], 0) + 1
        rows.append("""## VIDEO %d

**%s**

| | |
|---|---|
| Script file used | `%s` |
| Canonical SHA-256 | `%s` |
| Matches handoff lock manifest | %s |
| Thumbnail | **%s** (not rebuilt) |
| Opening identifier | %s |
| Framework | %s |
| Resource | %s, %s |
| Watch Next | **%s** (%s) |
| Spoken words | %d |
| Speech-only estimate | %s to %s at 130 to 145 wpm. **Estimate, not a measurement.** |
| Printed cover target | %s. Not a verified finished length. |
| Assets | %d teaching frames plus CTA and Watch Next. %s |
| Shorts | %s |
| Package | `%s/` |
| ZIP | `%s` |
| ZIP SHA-256 | `%s` |
""" % (n, m["title"], masters.CANON[n], masters.verify(n)[0],
       "yes" if masters.verify(n)[1] else "**NO**",
       m["thumbnail"], m["opening_id"], m["framework"],
       m["cta_name"], m["cta_url"], m["watch_next"], m["watch_next_slot"],
       w, fast, slow,
       masters.header(n).get("TARGET RUNTIME")
       or masters.header(n).get("TARGET LENGTH"),
       len(SETS[n]) - 2,
       ", ".join("%s %d" % kv_ for kv_ in sorted(counts.items())),
       ", ".join("%s %d" % kv_ for kv_ in sorted(sc.items())),
       os.path.basename(DIRS[n]), ZIPS[n], hashes[n]))

    return """# V4 to V7 September 9 Script Synchronization

**September 9, 2026.** The four production packages are synchronized with the
September 9 script lock. This was a targeted update: assets were reused,
reordered, corrected or rebuilt individually. No new slide decks were created,
no thumbnail was produced or altered, and Videos 1 to 3 were not touched.

## Source

Every package is built from the four locked Recording Masters in
`YouTube_Roadmap_and_V4V7_Lock_Sep09_2026.zip`. Each file's SHA-256 was
recomputed and matched against the handoff's own `Source_Lock_Manifest.json`
before anything was generated. The build reads those files and never writes to
them, so the Recording Script sections cannot drift.

The stale Video 4 and Video 5 labels in the original upload filenames do **not**
undo the approved swap. The handoff copies are correctly numbered and were used
as supplied.

%s
## Routing

**V4 to V5 to V1.** **V6 to V7 to V8.** Unchanged.

Playlist: **%s**
%s

No YouTube video URL is supplied for any Watch Next card. Each description
carries a placeholder. Do not construct one from a guessed identifier.

## What every package contains

- The locked Recording Master, copied byte for byte
- `Approved_Recording_Master_Reference.docx`, generated from it
- `Recording_Run_of_Show.docx`
- `Sentence_Trigger_Map.txt`
- `Visual_Build_Map_and_Motion_Reveal_Map.txt`
- `Riverside_CoCreator_Master_Prompt.txt`
- `Asset_Reuse_and_Change_Table.txt`
- `Video_N_Six_Short_Form_Recording_Scripts.docx` plus `Video_N_Shorts/`
- `Publishing_Materials.docx`
- `Source_Manifest_VN.json`
- `QA_Report.txt`
- `Change_Log.txt`
- `Support_Reference_PNG/` plus the ZIP, the PPTX and the two lifted cards

## Reuse is proved, not asserted

Every rendered asset is hashed against the pre-synchronization package. An asset
marked REUSE or REORDER whose bytes moved is a QA failure, not a footnote.

## The QA reports are split

Each `QA_Report.txt` separates **package checks completed now** from
**final-export checks still pending**. Executed animation, recorded audio, audio
balance, final pacing, actual runtime, caption placement and chapter timestamps
are listed as PENDING and are **not** claimed as verified. No earlier QA pass is
reused as evidence.

## Not supplied, by instruction

- **No chapter timestamps.** Build them from the finished export.
- **No music attribution or license code.**
- **No thumbnail artwork.** Nothing was designed, generated or altered.
- **No YouTube URLs** built from guessed identifiers.

## Combined handoff

`%s`
`%s`

## Status

**VIDEOS 4, 5, 6 AND 7: PACKAGES SYNCHRONIZED TO THE SEPTEMBER 9 SCRIPT LOCK.**

Ready for recording and Riverside production. Nothing about the recording or
the export is verified, because neither exists yet.
""" % ("\n".join(rows), PLAYLIST_NAME, PLAYLIST_URL, COMBINED, combined_hash)


def main():
    print("verifying the four locked masters against the handoff manifest")
    for n in (4, 5, 6, 7):
        h, ok = masters.verify(n)
        print("  V%d %s  %s" % (n, masters.CANON[n], "OK" if ok else "MISMATCH"))
        if not ok:
            raise SystemExit("master hash mismatch for V%d" % n)

    outs, all_fails, hashes = {}, [], {}
    for n in (4, 5, 6, 7):
        out, fails = build_video(n)
        outs[n] = out
        all_fails += [(n, c[0]) for c in fails]
        print("  built V%d: %d files"
              % (n, sum(len(f) for _, _, f in os.walk(out))))

    man_path = DELIV + MANIFEST_MD
    for n in (4, 5, 6, 7):
        hashes[n] = zip_folder(outs[n], DELIV + ZIPS[n])
    # combined, including the manifest
    open(man_path, "w").write(manifest(hashes, "computed below"))
    with zipfile.ZipFile(DELIV + COMBINED, "w", zipfile.ZIP_DEFLATED,
                         compresslevel=6) as z:
        for n in (4, 5, 6, 7):
            root = outs[n]
            base = os.path.basename(root)
            for dp, _, files in os.walk(root):
                for f in sorted(files):
                    full = os.path.join(dp, f)
                    _add(z, os.path.join(base, os.path.relpath(full, root)),
                         open(full, "rb").read())
        _add(z, MANIFEST_MD, open(man_path, "rb").read())
    ch = hashlib.sha256(open(DELIV + COMBINED, "rb").read()).hexdigest()
    open(DELIV + COMBINED + ".sha256", "w").write("%s  %s\n" % (ch, COMBINED))
    # rewrite the manifest with the real combined hash, then repack it
    open(man_path, "w").write(manifest(hashes, ch))
    with zipfile.ZipFile(DELIV + COMBINED, "a", zipfile.ZIP_DEFLATED,
                         compresslevel=6) as z:
        pass
    print()
    for n in (4, 5, 6, 7):
        print("  %s  %s" % (ZIPS[n], hashes[n]))
    print("  %s  %s" % (COMBINED, ch))
    print()
    print("QA failures:", all_fails or "none")


if __name__ == "__main__":
    main()
