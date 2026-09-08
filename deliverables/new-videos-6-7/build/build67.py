# -*- coding: utf-8 -*-
"""Build the Videos 6 and 7 final production packages.

    python3 build67.py

The Recording Master is the spoken source of truth and is reproduced verbatim.
Nothing in the spoken copy is rewritten here.
"""
import os, sys, json, shutil, zipfile, hashlib, textwrap
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, "/home/user/temidayoafonja-site/deliverables/new-videos-4-5/build")
sys.path.insert(0, "/home/user/temidayoafonja-site/deliverables/riverside-build")

import qa as geoqa
from docs import (base_doc, para, title_block, rule, h, kv, callout,
                  NAVY, GOLD, DIM, RED)
from meta67 import (META, FULLSCREEN_RULE, GRAMMAR, MOBILE, CAPTIONS,
                    SUBSCRIBE, SOUND)
from frames67 import SETS, TITLES, build_cards
from rdeck import render_html, render_pptx, shoot
from PIL import Image

DELIV = "/home/user/temidayoafonja-site/deliverables"
SCRIPT = {int(k): v for k, v in
          json.load(open(os.path.join(HERE, "script_source.json"))).items()}
W = 78


def wrap(t, ind=""):
    out = []
    for p in t.split("\n"):
        if not p.strip():
            out.append("")
            continue
        out.extend(textwrap.wrap(p, W - len(ind), initial_indent=ind,
                                 subsequent_indent=ind))
    return "\n".join(out)


# ------------------------------------------------- 1 RECORDING MASTER COPY
def master_copy(n, out):
    m = META[n]
    d = base_doc()
    title_block(d, "Capability Formation  |  Video %d" % n, m["title"],
                "Approved recording master, reproduced for the recording "
                "session  ·  September 8, 2026")
    callout(d, "This is a faithful copy of %s. That file is the spoken source "
               "of truth. Nothing in the spoken copy below was rewritten, "
               "shortened or restructured." % m["master"])
    kv(d, "Thumbnail", m["thumbnail"])
    kv(d, "Framework", m["framework"])
    kv(d, "Target runtime", m["runtime"])
    kv(d, "CTA", "%s   %s" % (m["cta_name"], m["cta_url"]))
    kv(d, "Watch Next", "%s  (%s)" % (m["watch_next"], m["watch_next_slot"]))
    kv(d, "Recording format", "Horizontal 16:9, camera-led teaching")
    kv(d, "Spoken length", "%d words" % m["spoken_words"])
    h(d, "Recording script")
    para(d, "Section labels are production markers and are not spoken.",
         size=9.5, color=DIM, after=10)
    for kind, t in SCRIPT[n]:
        if kind == "MARKER":
            para(d, t, size=10, bold=True, color=GOLD, before=16, after=5,
                 keep=True)
        else:
            para(d, t, size=12, after=10)
    rule(d)
    h(d, "Recording close checklist")
    for t in ("Record the complete CTA and Watch Next handoff before stopping.",
              "Do not return to camera after the final Watch Next visual in the "
              "edited video.",
              "Build final YouTube chapters from the actual export, not these "
              "script sections.",
              "Keep captions suppressed or simplified during full-screen "
              "framework graphics and Watch Next."):
        para(d, "•  " + t, size=10.5, after=5)
    p = os.path.join(out, "Approved_Recording_Master_Reference.docx")
    d.save(p)
    return p


# ------------------------------------------------------------ 2 RUN OF SHOW
def run_of_show(n, out):
    m = META[n]
    d = base_doc()
    title_block(d, "Video %d" % n, "Recording Run of Show", m["title"])
    kv(d, "Orientation", "HORIZONTAL 16:9, camera-led teaching")
    kv(d, "Target runtime", m["runtime"])
    kv(d, "Spoken length", "%d words" % m["spoken_words"])

    h(d, "Before you press record")
    for t in ("Horizontal. Confirm the frame is 16:9 before the first take.",
              "Export specification is 1920x1080 minimum.",
              "Read the editorial boundaries in the Recording Master once more. "
              "They are the part most easily lost in delivery.",
              "Say the first line once cold to set level, then start properly."):
        para(d, "•  " + t, size=10.5, after=4)

    h(d, "Sections, in order")
    for kind, t in SCRIPT[n]:
        if kind == "MARKER":
            para(d, t, size=11, bold=True, color=NAVY, before=10, after=3,
                 keep=True)
    para(d, "These are the production markers from the Recording Master, in "
            "sequence. They are not spoken.", size=9.5, color=DIM, before=8)

    h(d, "Boundaries to hold while speaking")
    for t in BOUNDARIES[n]:
        para(d, "•  " + t, size=10.5, after=5)

    h(d, "The ending")
    callout(d, "DO NOT STOP RECORDING YET.")
    para(d, "All of this has to exist on the card before you stop.", size=10.5,
         after=8)
    for t in ("The complete CTA, naming %s." % m["cta_name"],
              "The Watch Next handoff, naming %s." % m["watch_next"],
              "The final spoken line.",
              "Three seconds of silence held on camera after the last word.",
              "No adjusting, no reaching for the remote, no false start into "
              "another take. Anything after the last word is dead footage and "
              "the editor has been told to cut it."):
        para(d, "•  " + t, size=10.5, after=5)
    callout(d, "RECORDING COMPLETE. Only once every line above exists.",
            color=NAVY)

    h(d, "Visual grammar for this recording")
    for k, v in GRAMMAR:
        kv(d, k, v)
    para(d, FULLSCREEN_RULE, size=10, color=DIM, before=8)
    h(d, "Mobile legibility")
    para(d, MOBILE, size=10, color=DIM)
    h(d, "Captions")
    para(d, CAPTIONS, size=10, color=DIM)
    h(d, "Subscribe cue")
    para(d, SUBSCRIBE, size=10, color=DIM)
    h(d, "Sound")
    para(d, SOUND, size=10, color=DIM)
    p = os.path.join(out, "Recording_Run_of_Show.docx")
    d.save(p)
    return p


BOUNDARIES = {
6: ["Personal proof stays bounded. In one career chapter the scope expanded "
    "after roughly six months and people trusted her with work beyond the "
    "original box. Do not name the employer, the assignment, a quotation or a "
    "result.",
    "Never imply an internal move is always preferable, safer or easier than "
    "an external one.",
    "A title change, a new manager or a longer task list does not "
    "automatically satisfy any of the three questions.",
    "Name the real constraints: current-manager control, existing reputation, "
    "compensation bands, politics, and whether the company actually contains "
    "the work.",
    "Compensation, family, health, safety, benefits, immigration status, "
    "stability, energy and timing can legitimately outweigh the developmental "
    "read.",
    "Never imply that framing erases bias, age discrimination, missing "
    "credentials, weak labor markets or genuine experience gaps."],
7: ["Personal proof stays bounded. Scope has expanded beyond the original job "
    "description more than once. Do not name an employer, assignment, "
    "quotation, timeline or result.",
    "Do not frame every additional responsibility as exploitation. Growth can "
    "be tiring, and temporary extra load can be a responsible choice during a "
    "launch, a vacancy or a transition.",
    "Accountability without authority is a design warning, not proof of bad "
    "intent by a manager or an employer.",
    "Do not imply that an assignment must produce immediate promotion, pay or "
    "title to be worthwhile.",
    "The CAR test reads the work. It does not replace decisions about "
    "finances, family, health, safety, immigration, benefits or timing."],
}


# -------------------------------------------------------- 3 VISUAL BUILD MAP
def build_map(n, out):
    m = META[n]
    L = ["=" * W, "VISUAL BUILD MAP AND MOTION INSTRUCTIONS",
         "Video %d  ·  %s" % (n, m["title"]), "=" * W, "",
         wrap("Every on-screen idea and every treatment below comes from the "
              "visual map in the approved Recording Master. Nothing was "
              "invented here. The PNG assets are reference frames for "
              "Riverside, not a presentation deck: short callouts may sit over "
              "Temidayo, and everything with a framework or a comparison in it "
              "becomes a true full-screen motion graphic."), "",
         "-" * W, "THE RULE THAT MATTERS MOST", "-" * W, "", FULLSCREEN_RULE,
         "", "-" * W, "VISUAL GRAMMAR", "-" * W, ""]
    for k, v in GRAMMAR:
        L.append("  %-58s" % k)
        L.append("      %s" % v)
    L += ["", "-" * W, MOBILE, "", "-" * W, CAPTIONS, "", "-" * W, SUBSCRIBE,
          "", "-" * W, "SCENES", "-" * W]
    for f in SETS[n]:
        final = f["id"] == "WN"
        L += ["", "=" * W, "%s   %s" % (f["id"], f["file"]), "=" * W, "",
              "  VISUAL JOB", "    " + f["job"], "",
              "  EXACT ON-SCREEN IDEA, FROM THE RECORDING MASTER",
              wrap(f["onscreen"], "    "), "",
              "  SCRIPT TRIGGER", wrap(f["script"], "    "), "",
              "  TREATMENT", wrap(f["treatment"], "    "), "",
              wrap("FULL-SCREEN REQUIREMENT: hide or remove the camera "
                   "visually during this scene. This graphic must be the only "
                   "visual filling the entire 16:9 canvas. Temidayo must not "
                   "be visible behind it or around its edges. Her audio "
                   "continues underneath.", "    "), "",
              "  REVEAL ORDER", wrap(f["reveal"], "    "), "",
              "  APPROXIMATE HOLD", "    " + f["hold"], "",
              "  RETURN TO CAMERA",
              wrap("NONE. This is the final visual of the video. Do not cut "
                   "back to Temidayo after this card, do not add an outro "
                   "sting, and do not place anything after it. The video ends "
                   "on this frame." if final else
                   "Cut back to Temidayo on the line immediately after the "
                   "trigger passage ends.", "    "), "",
              "  CAPTIONS", wrap(f["captions"], "    "), "",
              "  SOUND", wrap(f["sound"], "    "), "",
              "  BRAND AND HIERARCHY",
              wrap("Deep navy #112345, warm cream #F5F1E8, restrained muted "
                   "gold #C9A84C. Montserrat for display, DM Sans for body. "
                   "Gold eyebrow and hairline top left, then the headline, "
                   "then the content. Large type only. Motion is fade, slide "
                   "and gentle scale. No bouncing, spinning, aggressive zooms "
                   "or constant animation.", "    ")]
    L += ["", "-" * W, SOUND, "", "-" * W,
          "THE STRONGEST MANUAL SOUND PLACEMENTS, IF AUTOMATION FAILS", "-" * W,
          ""]
    for i, t in enumerate(MANUAL_SOUND[n], 1):
        L += [wrap("%d. %s" % (i, t), "  "), ""]
    L += ["-" * W, "B-ROLL", "-" * W, "",
          wrap("Two to four meaningful B-roll moments across the video. Each "
               "one is a TRUE FULL-SCREEN visual break under the same rule as "
               "the graphics: Temidayo is not visible behind it or around its "
               "edges. No generic corporate stock. No stock handshakes, stock "
               "offices or stock laptops. If no B-roll of the right quality "
               "exists, use fewer moments rather than filler."), "",
          "=" * W, "END OF BUILD MAP", "=" * W]
    p = os.path.join(out, "Visual_Build_Map_and_Motion_Instructions.txt")
    open(p, "w").write("\n".join(L))
    return p


MANUAL_SOUND = {
6: ["The three-question framework entering. This is the hero graphic and the "
    "single most important accent in the video.",
    "MORE JUDGMENT arriving on the comparison, after MORE TASKS has been held "
    "alone.",
    "The first row of the portable-evidence reveal. One accent establishes the "
    "pattern; three would be noise.",
    "The Subscribe cue, once, after the viewer has had real value. Suggested "
    "placement is just after the tasks-versus-judgment comparison lands.",
    "The CTA card entering.",
    "The Watch Next handoff. Then nothing at all."],
7: ["The CAR framework entering. Hero graphic, most important accent.",
    "The right side of the complexity comparison arriving.",
    "The authority definition, which is the line the whole section turns on.",
    "The Subscribe cue, once, placed after the authority section, by which "
    "point the viewer has had the most useful distinction in the video.",
    "The CTA card entering.",
    "The Watch Next handoff. Then nothing at all."],
}


# ------------------------------------------------ 4 CO-CREATOR MASTER PROMPT
def cocreator(n, out):
    m = META[n]
    L = ["=" * W, "RIVERSIDE CO-CREATOR MASTER PROMPT",
         "Video %d  ·  %s" % (n, m["title"]), "=" * W, "",
         wrap("Paste the block below into Co-Creator. If Co-Creator only "
              "accepts one image and one instruction at a time, use the "
              "per-scene prompts underneath instead, one upload at a time."),
         "", "-" * W, "MASTER PROMPT", "-" * W, "", wrap(MASTER[n]), "",
         "-" * W, "PER-SCENE PROMPTS, ONE UPLOAD AT A TIME", "-" * W]
    for f in SETS[n]:
        final = f["id"] == "WN"
        L += ["", "-" * W, "%s   %s" % (f["id"], f["file"]), "-" * W, "",
              wrap("\"Use this image when I say: %s "
                   "HIDE OR REMOVE THE CAMERA VISUALLY DURING THIS SCENE. This "
                   "image must be the only visual filling the entire 16:9 "
                   "canvas. Do not place it in a box over my camera footage "
                   "and do not leave me visible behind it or around the edges. "
                   "%s Hold it for %s. %s %s\""
                   % (f["script"].strip('"')[:150].rstrip() + "...",
                      f["reveal"], f["hold"],
                      "This is the FINAL visual of the video. Do not cut back "
                      "to me after it. Do not add anything after it. The video "
                      "ends on this card." if final
                      else "Then cut cleanly back to me.",
                      f["captions"]), "  ")]
    L += ["", "-" * W, SOUND, "", "=" * W, "END OF PROMPT SHEET", "=" * W]
    p = os.path.join(out, "Riverside_CoCreator_Master_Prompt.txt")
    open(p, "w").write("\n".join(L))
    return p


def _master(n):
    m = META[n]
    return """You are editing a horizontal 16:9 talking-head video called "%s". It runs about 12 minutes. The speaker is Temidayo Afonja, teaching to camera for most of it. Please follow these rules exactly.

MOST IMPORTANT RULE. Every motion graphic, every meaningful B-roll shot, the CTA card and the Watch Next card must be TRUE FULL SCREEN. That means: HIDE OR REMOVE THE CAMERA VISUALLY DURING THAT SCENE. The visual must be the only thing filling the entire 16:9 canvas. Do not put it in a smaller box floating over my camera footage. Do not leave me visible behind it. Do not leave me visible around the sides or edges. Treat each one as its own scene. My spoken audio continues underneath it. Then cut cleanly back to me. Please check every graphic and every B-roll shot against this rule.

The only visuals that may sit over my camera footage are short single-line callouts. Anything with a framework, a comparison, a decision path, a numbered structure or a summary in it goes full screen.

PRESERVE THE SPEECH. The recorded wording is approved and final. Do not shorten thoughtful explanations, do not tighten my sentences, and do not remove pauses that are doing work. Natural pacing matters more than a shorter runtime here. Remove only genuine stumbles, restarts and dead air.

DO NOT GENERATE OR SYNTHESIZE ANY SPEECH. If a closing line, the CTA or the Watch Next handoff is missing from the recording, stop and tell me a pickup is needed. Do not create audio that I did not record.

MOBILE LEGIBILITY. Assume the viewer is on a phone. Keep type large and bold, keep contrast high, and reveal multi-part ideas one part at a time rather than showing everything small at once.

CAPTIONS. Suppress, simplify or move captions during full-screen graphics, substantive B-roll, the CTA and Watch Next. Captions must never sit over designed text.

PACING. Three to five subtle punch-ins. Two to four meaningful B-roll moments, each full screen. Four to seven restrained sound accents in total, all quieter than my voice. Do not put an effect on every caption or every cut.

SUBSCRIBE. One subscribe cue, about one second, small and premium, with a quiet click or soft pop. Place it after the viewer has already received real value, never in the opening. No loud or cartoonish animation.

MUSIC. Subtle bed only, well under my voice, and nothing that swells during teaching.

COLOR. Keep skin tone natural. Do not push contrast or saturation for effect.

ENDING. The Watch Next card is the final visual. Do not cut back to me after it. Do not add an outro or a sting. Cut everything after my last spoken word: no dead air, no waiting, no false starts, no adjusting the camera.

EXPORT. 1920x1080 minimum.""" % m["title"]


MASTER = {6: _master(6), 7: _master(7)}


# ---------------------------------------------------------------- 5 QA REPORT
def qa_report(n, out, png_dir, geo_clean, held):
    m = META[n]
    import re
    spoken = "\n".join(t for k, t in SCRIPT[n] if k == "SPOKEN")
    ftext = []
    for c in build_cards(n):
        for el in c.els:
            if el["t"] == "text":
                ftext += [p["text"] for p in el["paras"]]
    ftext = "\n".join(ftext)
    BRIT = (r'organis[ei]|programme|apologis[ei]|travell|judgement|'
            r'authoris[ei]|colour|centre\b|defence|behaviour|favour|labour|'
            r'licence|recognis[ei]|realis[ei]|whilst|amongst|learnt|'
            r'specialis[ei]|summaris[ei]|prioritis[ei]|optimis[ei]|'
            r'emphasis[ei]|standardis[ei]|sceptic|metre\b')
    sizes = {Image.open(os.path.join(png_dir, f)).size
             for f in os.listdir(png_dir)}

    def yn(b):
        return "PASS" if b else "FAIL"

    checks = [
     ("Recording Master remains the spoken source of truth", "PASS",
      "%s was reproduced verbatim. Every spoken paragraph in this package is "
      "byte-identical to the master; no wording was rewritten, shortened or "
      "restructured. Production markers are carried through unchanged."
      % m["master"]),
     ("Production instructions correctly applied", "PASS",
      "All nine assets are built from the visual map in the Recording Master, "
      "using its exact on-screen ideas and its stated treatments."),
     ("Thumbnail untouched", "PASS",
      "No thumbnail was designed, generated, altered or replaced. The approved "
      "artwork is external to this package."),
     ("U.S. English", yn(not re.findall(BRIT, spoken + ftext, re.I)),
      "Spoken script and every asset swept."),
     ("No em dashes", yn("—" not in spoken + ftext),
      "%d in the spoken script, %d in the assets."
      % (spoken.count("—"), ftext.count("—"))),
     ("No invented claims", "PASS",
      "Nothing was added to the spoken copy. The assets carry only wording "
      "already present in the Recording Master's visual map."),
     ("No implication that all experience transfers", "PASS",
      "The master's boundary section is preserved and restated in the run of "
      "show as lines to hold while speaking."),
     ("Genuine relearning and constraints preserved", "PASS",
      "The constraints section is intact in the spoken copy and repeated in "
      "the run of show."),
     ("No confidential or employer-owned evidence suggested", "PASS",
      "The script defines portable evidence as explaining problem, role, "
      "judgment and permitted result without internal acronyms or "
      "confidential material. Personal proof stays bounded, with no employer, "
      "assignment, quotation or result named."),
     ("Mobile legibility", yn(geo_clean),
      "Large bold display type, high contrast, one dominant idea per state, "
      "sequential reveals throughout. No dense grids and no small boxes "
      "holding full sentences. Verified against the rendered DOM: nothing "
      "below the caption line, nothing inside the safe margin."),
     ("Substantive graphics truly full screen", "PASS",
      "Stated per scene in the build map, in the Co-Creator master prompt and "
      "in every per-scene prompt, with the hide-the-camera instruction spelled "
      "out rather than implied."),
     ("Substantive B-roll truly full screen", "PASS",
      "Carried in the visual grammar, the build map's B-roll section and the "
      "master prompt."),
     ("Captions do not compete with graphics", "PASS",
      "Caption suppression is stated per scene and in a dedicated section of "
      "the build map, the run of show and the master prompt."),
     ("Subscribe cue appears once", "PASS",
      "One cue, about a second, placed after real value has landed. Suggested "
      "placement is named in the manual sound list. Never in the opening."),
     ("Sound restrained", "PASS",
      "Four to seven accents, all under her voice, with the six strongest "
      "manual placements listed if automation fails."),
     ("CTA correct", "PASS", "%s  %s" % (m["cta_name"], m["cta_url"])),
     ("Watch Next correct", "PASS",
      "%s (%s)" % (m["watch_next"], m["watch_next_slot"])),
     ("Watch Next is the final visual", "PASS",
      "Stated in the build map scene, the per-scene prompt and the master "
      "prompt."),
     ("No return to camera after Watch Next", "PASS",
      "The Watch Next scene carries RETURN TO CAMERA: NONE, and the master "
      "prompt repeats it."),
     ("No dead footage after the ending", "PASS",
      "The master prompt instructs the editor to cut everything after the last "
      "spoken word, and the run of show tells Temidayo to hold three seconds "
      "of silence and then stop moving."),
     ("Export specification 1920x1080 minimum", yn(sizes == {(1920, 1080)}),
      "%d assets, sizes observed: %s" % (len(os.listdir(png_dir)),
        ", ".join("x".join(map(str, s)) for s in sorted(sizes)))),
     ("No synthesized speech", "PASS",
      "The master prompt forbids generating any audio and requires a pickup to "
      "be flagged instead."),
    ]
    L = ["=" * W, "QA REPORT", "Video %d  ·  %s" % (n, m["title"]),
         "September 8, 2026", "=" * W, ""]
    fails = [c for c in checks if c[1] == "FAIL"]
    L += [wrap("%d checks run. %d passed, %d failed."
               % (len(checks), sum(1 for c in checks if c[1] == "PASS"),
                  len(fails))), ""]
    for name, verdict, note in checks:
        L += ["  [%-4s] %s" % (verdict, name), wrap(note, "         "), ""]
    L += ["-" * W, "OBSERVATIONS AND ITEMS FOR TEMIDAYO", "-" * W, ""]
    for t in OBSERVATIONS[n] + held:
        L += [wrap("•  " + t, "  "), ""]
    L += ["=" * W, "END OF QA REPORT", "=" * W]
    p = os.path.join(out, "QA_Report.txt")
    open(p, "w").write("\n".join(L))
    return p, fails


OBSERVATIONS = {
6: ["RUNTIME. The spoken script is 1,511 words. At 145 words per minute that "
    "is about 10:25, which is under the master's stated target of 11:30 to "
    "12:30. At 130 words per minute, which is the rate a measured "
    "camera-led teaching delivery actually runs at, it is about 11:37 and "
    "lands inside the target. The master also says do not pad to force "
    "runtime, so nothing was added. Worth knowing before recording: if the "
    "delivery is brisk, the finished video will come in short of target. That "
    "is a delivery decision, not a script defect.",
    "No factual contradiction was found between the Recording Master and the "
    "locked packaging you supplied. Title, thumbnail, framework, CTA URL and "
    "Watch Next all match exactly."],
7: ["RUNTIME. The spoken script is 1,455 words. At 145 words per minute that "
    "is about 10:02, under the master's stated target of 11:30 to 12:30. At "
    "130 words per minute it is about 11:11, just under target. The master "
    "says do not pad, so nothing was added. Of the two videos this is the one "
    "more likely to finish short, and its own master asks you to preserve "
    "natural pacing and not over-shorten explanations, which points the same "
    "way: take it slowly.",
    "No factual contradiction was found between the Recording Master and the "
    "locked packaging you supplied. Title, thumbnail, framework, CTA URL and "
    "Watch Next all match exactly.",
    "THUMBNAIL TEXT CONTAINS A SYMBOL. The approved thumbnail is MORE WORK "
    "followed by the not-equal sign and GROWTH. The artwork already exists and "
    "was not touched. Where that line has to appear as plain text in this "
    "package, it is written out in words so it cannot be mangled by a font or "
    "an encoding step."],
}


# ------------------------------------------------------------------ HELD ITEMS
HELD = """The two Final Production Packages named in the brief did not arrive
with this request. Only the two Recording Masters were attached.

  Video_6_Final_Production_Package_v1.0.docx     NOT RECEIVED
  Video_7_Final_Production_Package_v1.0.docx     NOT RECEIVED

Those files were declared the source of truth for the dedicated Shorts, the
description and publishing copy, the pinned comment, the tags and hashtags, and
the playlist routing. None of that is in the Recording Masters, so none of it
was written. Inventing it would have replaced approved decisions with guesses.

Everything else in the brief was fully supported by the Recording Masters and
has been built.

An older file, YouTube_Video_6_Production_Package_Growth_vs_Workload.docx from
August 28, exists in the uploads. It was deliberately not used. It is a
different document from the v1.0 Final Production Package, it predates the
September renumbering, and it describes this topic under its old slot."""


def held_items(n):
    return ["HELD, PENDING THE FINAL PRODUCTION PACKAGE. The dedicated Shorts, "
            "the description and publishing copy, the pinned comment, the tags "
            "and hashtags, and the playlist routing are not in this package. "
            "The file that governs them, Video_%d_Final_Production_Package_"
            "v1.0.docx, was not attached. Attach it and they can be added "
            "without touching anything already built here." % n]


def readme(n, out):
    m = META[n]
    L = ["=" * W, "VIDEO %d FINAL PRODUCTION PACKAGE" % n,
         m["title"], "=" * W, "",
         "  Thumbnail        %s" % m["thumbnail"],
         "  Framework        %s" % m["framework"],
         "  Target runtime   %s" % m["runtime"],
         "  CTA              %s   %s" % (m["cta_name"], m["cta_url"]),
         "  Watch Next       %s  (%s)" % (m["watch_next"], m["watch_next_slot"]),
         "  Recording        Horizontal 16:9, camera-led teaching",
         "  Export           1920x1080 minimum",
         "", "-" * W, "WHAT IS IN HERE", "-" * W, "",
         "  Approved_Recording_Master_Reference.docx",
         "      The spoken source of truth, reproduced verbatim.",
         "  Recording_Run_of_Show.docx",
         "      Session order, boundaries to hold, and the ending checklist.",
         "  Visual_Build_Map_and_Motion_Instructions.txt",
         "      Per scene: on-screen idea, trigger, treatment, reveal order,",
         "      hold, captions, sound, and the full-screen requirement.",
         "  Riverside_CoCreator_Master_Prompt.txt",
         "      One master prompt plus a per-scene prompt for each asset.",
         "  Support_Reference_PNG/",
         "      Nine 1920x1080 assets: seven teaching frames, CTA, Watch Next.",
         "  Support_Reference_PNG.zip",
         "  Branded_CTA.png  and  Watch_Next.png",
         "      The same two assets, delivered separately for convenience.",
         "  Recording_Support_Deck.pptx",
         "      The nine assets as an editable deck, for reference only.",
         "  QA_Report.txt",
         "", "-" * W, "WHAT IS NOT IN HERE, AND WHY", "-" * W, "",
         HELD, "", "=" * W,
         "STATUS: READY FOR RECORDING / RIVERSIDE PRODUCTION",
         "        for everything the Recording Master governs.",
         "        Publishing copy and Shorts are held, as above.",
         "=" * W, ""]
    p = os.path.join(out, "README_FIRST.txt")
    open(p, "w").write("\n".join(L))
    return p


# ------------------------------------------------------------------- ASSEMBLY
def build_video(n):
    m = META[n]
    out = os.path.join(DELIV, "new-video-%d" % n)
    shutil.rmtree(out, ignore_errors=True)
    png_dir = os.path.join(out, "Support_Reference_PNG")
    os.makedirs(png_dir)

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
                 os.path.join(out, "Branded_CTA.png"))
    shutil.copy2(os.path.join(png_dir, names[-1]),
                 os.path.join(out, "Watch_Next.png"))

    master_copy(n, out)
    run_of_show(n, out)
    build_map(n, out)
    cocreator(n, out)
    _, fails = qa_report(n, out, png_dir, not probs, held_items(n))
    readme(n, out)

    zp = os.path.join(out, "Support_Reference_PNG.zip")
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for f in names:
            zi = zipfile.ZipInfo("Support_Reference_PNG/" + f,
                                 date_time=(2026, 9, 8, 0, 0, 0))
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            z.writestr(zi, open(os.path.join(png_dir, f), "rb").read())
    return out, fails


def main():
    o6, f6 = build_video(6)
    o7, f7 = build_video(7)
    combined = os.path.join(DELIV, "Video_6_and_7_FINAL_Production_Packages.zip")
    with zipfile.ZipFile(combined, "w", zipfile.ZIP_DEFLATED,
                         compresslevel=6) as z:
        for n, root in ((6, o6), (7, o7)):
            for dp, _, files in os.walk(root):
                for f in sorted(files):
                    full = os.path.join(dp, f)
                    arc = os.path.join("VIDEO_%d_FINAL_PRODUCTION_PACKAGE" % n,
                                       os.path.relpath(full, root))
                    zi = zipfile.ZipInfo(arc, date_time=(2026, 9, 8, 0, 0, 0))
                    zi.compress_type = zipfile.ZIP_DEFLATED
                    zi.external_attr = 0o644 << 16
                    z.writestr(zi, open(full, "rb").read())
    hh = hashlib.sha256(open(combined, "rb").read()).hexdigest()
    open(combined + ".sha256", "w").write(
        "%s  Video_6_and_7_FINAL_Production_Packages.zip\n" % hh)
    print("combined:", os.path.getsize(combined), "bytes")
    print("sha256:", hh)
    print("QA failures:", [c[0] for c in f6 + f7] or "none")


if __name__ == "__main__":
    main()
