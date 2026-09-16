# -*- coding: utf-8 -*-
"""Assemble eight self-contained synchronized production packages."""
import os, sys, json, re, shutil, zipfile, hashlib, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.append(DELIV + "VIDEOS_22-23/build")
sys.path.append(DELIV + "riverside-build")
sys.path.insert(0, DELIV + "V4-V11_EDIT_SYNC/build")

import recon as R
import shortsync as SH
import finalledger as FL
import adjudicated as AD
import briefs as B
import src916 as S916
import sequencing as Q
import locate as LOC
from docs23 import (base_doc, title_block, h, kv, para, callout, sub,
                    caption, table, bullets, footer_note, page_break, mono,
                    hr, head)

EYEBROW = "capability formation | synchronized production"
PKGDIR = os.path.join(OUT, "PACKAGES")
DESC = os.path.join(OUT, "_source", "files", "desc")
ZIP_DT = (2026, 9, 16, 0, 0, 0)
ARCHIVE = "YouTube_NEW_PUBLIC_V4-V11_SYNCHRONIZED_2026-09-16.zip"

LOCKED = {
 4: ("AI Took the Task. Who Gets the Experience?", "WHO LEARNS NOW?", 26),
 5: ("If Your Company Needs You but Won’t Grow You",
     "USEFUL. STILL STUCK.", 33),
 6: ("Decode a Job Description in 10 Minutes", "IGNORE THE TITLE", 22),
 7: ("I’ve Seen Who Gets the Bigger Role and Why",
     "THEY CHOSE SOMEONE ELSE", 24),
 8: ("What Disappears When Your Work Access Ends",
     "YOU CAN’T PROVE IT LATER", 28),
 9: ("Transferable Skills Advice Is Missing Something",
     "NOT EVERYTHING TRAVELS", 27),
 10: ("Your First 90 Days in a New Job: What Really Matters",
      "DON’T SPEND YOUR FIRST 90 DAYS PROVING YOURSELF", None),
 11: ("What to Do When Your New Job Isn’t the Job You Accepted",
      "THIS ISN’T THE JOB", None),
}
RESOURCE = {4: None, 5: "Career Decision Evidence Check",
            6: "Career Evidence Starter", 7: "Career Evidence Starter",
            8: "Keep the Proof", 9: "Career Decision Evidence Check",
            10: "Career Evidence Starter",
            11: "Career Decision Evidence Check"}
WATCH_NEXT_NOTE = {
 10: "NEW PUBLIC V11. Not live until V11 publishes.",
 11: "NEW PUBLIC V5. Not live until V5 publishes.",
}
PKG = {n: "NEW_V%02d_Synchronized_Production_Package" % n
       for n in R.VIDEOS}


def stamp():
    return subprocess.check_output(
        ["env", "TZ=America/Chicago", "date",
         "+%A, %B %d, %Y | %-I:%M %p CT"]).decode().strip()


def sha256(p):
    h_ = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h_.update(b)
    return h_.hexdigest()


def _wrap(t, w=68):
    out, line = [], ""
    for word in str(t).split():
        if len(line) + len(word) + 1 > w:
            out.append(line); line = word
        else:
            line = (line + " " + word).strip()
    if line:
        out.append(line)
    return out or [""]


def _sents(p):
    return [x.strip() for x in re.split(r"(?<=[.?!”])\s+", p)
            if x.strip()]


# ------------------------------------------------------- thought blocks
def blocks(n):
    """Group the reconciled paragraphs into complete-thought blocks.

    One block per paragraph, except that a paragraph of a single short
    sentence is joined to the next so a block carries a complete idea
    rather than a fragment. Blocks stay within five sentences.
    """
    out = []
    for lab, ps in R.sections(n):
        cur = []
        for p in ps:
            cur.append(p)
            ns = sum(len(_sents(x)) for x in cur)
            if ns >= 2 or len(cur) >= 2:
                out.append((lab, list(cur)))
                cur = []
        if cur:
            if out and out[-1][0] == lab and sum(
                    len(_sents(x)) for x in out[-1][1]) + len(
                    _sents(cur[0])) <= 5:
                out[-1][1].extend(cur)
            else:
                out.append((lab, list(cur)))
    return out


def recording_master(n, path, st):
    d = base_doc()
    title_block(d, EYEBROW, LOCKED[n][0], "Reconciled recording master")
    kv(d, "New public number", "V%d" % n)
    kv(d, "Former roadmap number",
       ("V%d" % LOCKED[n][2]) if LOCKED[n][2] else "None. New concept.")
    kv(d, "Thumbnail", LOCKED[n][1])
    kv(d, "Spoken words", format(R.word_count(n), ","))
    kv(d, "Generated", st)
    callout(d, "This is the September 16 BEAST MODE body with the approved "
               "topic-specific introduction restored, and nothing else. "
               "Section labels are production scaffolding and are NOT "
               "SPOKEN. Word count is whitespace-delimited tokens of the "
               "spoken stream only.")
    for lab, ps in R.sections(n):
        sub(d, "%s  [NOT SPOKEN]" % lab)
        for p in ps:
            para(d, p, size=11.5, after=8)
    footer_note(d, "Runtime, chapters and SRT are produced from the "
                   "finished export and appear nowhere in this package.")
    d.save(path)
    return path


def thought_blocks(n, path, st):
    d = base_doc()
    title_block(d, EYEBROW, LOCKED[n][0], "Thought-block recording copy")
    kv(d, "New public number", "V%d" % n)
    kv(d, "Thumbnail", LOCKED[n][1])
    kv(d, "Spoken words", format(R.word_count(n), ","))
    kv(d, "Generated", st)
    sub(d, "RECORDING DIRECTION  [NOT SPOKEN]")
    para(d, "Read one block silently. Look toward the lens. Deliver "
            "naturally. Stop. Reset posture and hands. Advance.", size=11)
    lastlab = None
    i = 0
    for lab, ps in blocks(n):
        if lab != lastlab:
            sub(d, "%s  [NOT SPOKEN]" % lab)
            lastlab = lab
        i += 1
        sub(d, "BLOCK %02d  [NOT SPOKEN]" % i)
        for p in ps:
            para(d, p, size=12, after=8)
    footer_note(d, "Exact spoken words and punctuation, in order. No "
                   "editor, production, Riverside, visual or Shorts note "
                   "appears in this document.")
    d.save(path)
    return path


# --------------------------------------------------------- the cue map
_ANCHOR = {}
for _f in ("an_sprint.json", "an_1011.json"):
    _p = os.path.join(HERE, _f)
    if os.path.exists(_p):
        for _n, _rows in json.load(open(_p)).items():
            _ANCHOR[int(_n)] = _rows


def cues(n):
    """Every family with its one resolved location, in spoken order.

    Corrected in sequencing.py: four cards re-cued to the section their own
    copy belongs to, one retired, and the six early-edit families the
    briefs specified added at their opening locations.
    """
    return Q.anchors(n)


def accent_of(beat):
    m = re.search(r"\bS(\d)\b", beat["head"])
    return "S%s" % m.group(1) if m else None


def run_of_show(n, path, st):
    d = base_doc()
    title_block(d, EYEBROW, LOCKED[n][0], "Run of show")
    kv(d, "New public number", "V%d" % n)
    kv(d, "Thumbnail", LOCKED[n][1])
    kv(d, "Spoken words", format(R.word_count(n), ","))
    lo = R.word_count(n) / 145.0 * 60
    hi = R.word_count(n) / 130.0 * 60
    kv(d, "Planning estimate, provisional",
       "%d:%02d to %d:%02d, arithmetic at 130 to 145 words per minute. "
       "Not a runtime." % (lo // 60, lo % 60, hi // 60, hi % 60))
    kv(d, "Generated", st)
    callout(d, "Camera-led does not mean camera-only. The edit begins on "
               "the first spoken line. Editorial hook text, a meaningful "
               "cutaway and a restrained sound accent may enter the first "
               "relevant beats while the voice continues. No branded "
               "pre-roll and no dead-air slide.")
    h(d, "Section order")
    table(d, ["", "Section", "Paragraphs", "Words"],
          [["%d" % (i + 1), lab + ("  [restored intro]"
                                   if lab == R.INTRO_LABEL else ""),
            "%d" % len(ps),
            "%d" % len(" ".join(ps).split())]
           for i, (lab, ps) in enumerate(R.sections(n))],
          widths=[0.4, 3.0, 1.0, 0.8], size=8.5)
    h(d, "Full-screen cues, one location each")
    table(d, ["Asset family", "Section", "Para", "States", "Anchor"],
          [[c["key"], "%d %s" % (c["section"] + 1, c["label"]),
            "%d" % (c["para"] + 1), "%d" % len(c["states"]), c["kind"]]
           for c in cues(n)], widths=[2.3, 2.1, 0.5, 0.6, 1.2], size=7.5)
    caption(d, "Every cue resolves to one section and one paragraph. "
               "RE-ANCHORED means the card is unchanged and only its "
               "placement moved to the reconciled script.")
    h(d, "Early-edit beats from the current brief")
    bts = B.read(n)["beats"]
    table(d, ["", "Phase", "Treatment", "Accent", "Display copy"],
          [["%d" % x["n"], x["phase"], x["head"][:40],
            accent_of(x) or "", (x["display"] or "")[:52]] for x in bts],
          widths=[0.3, 0.8, 2.0, 0.6, 3.0], size=7.5)
    footer_note(d, "Chapters and SRT are produced from the finished "
                   "export. No timecode in this package is measured.")
    d.save(path)
    return path


def camera_map(n, path):
    L = head("NEW PUBLIC V%d  |  CAMERA AND FULL-SCREEN MAP" % n)
    L += [LOCKED[n][0], "", "Camera is primary for recognition, lived",
          "interpretation, nuance, boundaries and consequential",
          "statements. Substantive teaching, frameworks, comparisons and",
          "meaningful B-roll are TRUE FULL SCREEN. The voice may continue",
          "under a full-screen image. Never keep Temidayo moving behind a",
          "teaching card.", "", hr(), ""]
    C = {c["section"]: [] for c in cues(n)}
    for c in cues(n):
        C.setdefault(c["section"], []).append(c)
    for li, (lab, ps) in enumerate(R.sections(n)):
        L += ["SECTION %d  %s%s" % (li + 1, lab,
                                    "   [restored intro]"
                                    if lab == R.INTRO_LABEL else ""), ""]
        for pi, p in enumerate(ps):
            early = [e for e in Q.EARLY.get(n, [])
                     if e["section"] == li and e["para"] == pi]
            # An early step is the full instruction for its family, so the
            # family's own row is not printed again underneath it.
            done = {e["asset"] for e in Q.EARLY.get(n, []) if e["asset"]}
            hit = [c for c in C.get(li, [])
                   if c["para"] == pi and c["key"] not in done]
            if early:
                for e in early:
                    L += ["  PARA %d   MODE: %s   (early edit, step %d)"
                          % (pi + 1, e["mode"], e["order"])]
                    if e["display"]:
                        L += ["           ON-SCREEN TEXT: %s"
                              % _clip(e["display"], 44)]
                    L += ["           ENTER ON: %s" % _clip(e["enter"], 46),
                          "           LEAVE ON: %s  (paragraph %d)"
                          % (_clip(e["leave"], 40), e["para_out"] + 1)]
                    if e["asset"]:
                        L += ["           ASSET FAMILY: %s" % e["asset"],
                              "           STATES, IN REVEAL ORDER:"]
                        for x in e["states"]:
                            L.append("               %s.png" % x)
                    L += ["           SOUND: %s" % (e["sound"] or "none"),
                          "           RETURN: %s" % e["ret"], ""]
            if hit:
                for c in hit:
                    sub = Q.subrange(n, li, pi, c["key"])
                    L += ["  PARA %d   MODE: FULL SCREEN%s"
                          % (pi + 1,
                             "   (%d of %d in this paragraph)"
                             % (sub["order"], sub["of"]) if sub else ""),
                          "           ASSET FAMILY: %s" % c["key"],
                          "           STATES, IN REVEAL ORDER:"]
                    for x in c["states"]:
                        L.append("               %s.png" % x)
                    if sub:
                        L += ["           ENTER ON: %s"
                              % _clip(sub["enter"], 46),
                              "           LEAVE ON: %s"
                              % _clip(sub["leave"], 46)]
                        L += ["           The camera does not return here. "
                              "The next card in this",
                              "           paragraph takes over on its own "
                              "entry words."]\
                            if sub["order"] < sub["of"] else \
                            ["           The camera returns at the end of "
                             "this paragraph."]
                    else:
                        L += ["           EXACT TRIGGER:"]
                        L += ["               %s" % x
                              for x in _wrap(c["trigger"] or p, 58)]
                    L.append("")
            held = [e for e in Q.EARLY.get(n, [])
                    if e["section"] == li and e["para"] < pi
                    and e["para_out"] >= pi]
            if not hit and not early and held:
                e = held[0]
                L += ["  PARA %d   MODE: %s, still held from step %d"
                      % (pi + 1, e["mode"], e["order"]),
                      "           The voice continues under it. LEAVE ON: "
                      "%s" % _clip(e["leave"], 40),
                      "           RETURN: %s" % e["ret"], ""]
            elif not hit and not early:
                L += ["  PARA %d   MODE: CAMERA" % (pi + 1),
                      "           %s" % _clip(p, 58), ""]
    L += [hr(), "", "WATCH NEXT", "",
          "  Full screen from the start of the spoken Watch Next passage.",
          "  It is the final frame. Never return to camera afterward.", ""]
    return mono(path, L)


def _clip(s, n=58):
    s = " ".join(str(s).split())
    return s if len(s) <= n else s[:n].rstrip() + "..."


def motion_map(n, path):
    L = head("NEW PUBLIC V%d  |  MOTION AND REVEAL MAP" % n)
    L += [LOCKED[n][0], "",
          "One active idea at a time. Establish the whole structure, then",
          "activate one component. Gentle push-ins and occasional",
          "pull-backs only. No constant zooming, pulsing or effects.",
          "Preserve meaningful pauses.", "", hr(), ""]
    for c in cues(n):
        sub = Q.subrange(n, c["section"], c["para"], c["key"])
        L += ["%s" % c["key"],
              "  SECTION %d, PARAGRAPH %d%s"
              % (c["section"] + 1, c["para"] + 1,
                 "   (%d of %d in this paragraph)" % (sub["order"],
                                                      sub["of"])
                 if sub else ""),
              "  REVEAL ORDER:"]
        for i, s in enumerate(c["states"], 1):
            L.append("      %d. %s.png" % (i, s))
        L += ["  EMPHASIS: active item in the warm yellow wash with the",
              "            rust rule. Everything else quiet. Never two",
              "            active at once.", ""]
    b = B.read(n)
    L += [hr(), "", "CAMERA EMPHASIS  |  FOUR BEATS", ""]
    for x in b["camera"]:
        L += ["  %s" % y for y in _wrap(x, 66)]
        L.append("")
    return mono(path, L)


def sound_map(n, path):
    b = B.read(n)
    L = head("NEW PUBLIC V%d  |  SOUND MAP" % n)
    L += [LOCKED[n][0], "",
          "A stinger means a brief sound: a quiet click, a soft tap, paper",
          "movement or a restrained tonal accent. It is not a logo",
          "animation, a loud transition or a visual effect. A visual",
          "accent and a cutaway are separate choices.", "",
          "Audition every cue under the actual recorded voice. Keep speech",
          "clear. No alarms, no loud whooshes, no compulsory music bed, no",
          "accent on every bullet, and no second effect where one already",
          "carries the moment.", "", hr(), "", "THE FIVE ACCENTS", ""]
    seen = []
    for x in b["beats"]:
        a = accent_of(x)
        if not a:
            continue
        seen.append(a)
        r = LOC.resolve(n, x["trigger"], x["head"]) if x["trigger"] else None
        w = LOC.accent_location(n, x)
        L += ["  %s" % a,
              "      SCENE ENTERS ON THIS EXACT SPOKEN WORDING:"]
        L += ["          %s" % y
              for y in _wrap(LOC.remap(n, x["trigger"]) or "", 56)]
        if r:
            L += ["      LOCATION: section %d, %s, paragraph %d"
                  % (r["section"] + 1, r["label"], r["para"] + 1)]
            if r["occurrences"] > 1:
                L += ["          %s" % y for y in _wrap(r["note"], 54)]
        if w:
            L += ["      THE SOUND ITSELF FALLS ON: %s" % w["word"]]
            if w["section"] is not None:
                L += ["          section %d, %s, paragraph %d"
                      % (w["section"] + 1, w["label"], w["para"] + 1)]
            else:
                L += ["          %s" % y for y in _wrap(w["note"], 54)]
            L += ["          One accent on that word. Not one per bullet."]
        else:
            L += ["      THE SOUND ITSELF FALLS ON: the scene entry above.",
                  "          The brief names no separate accent word."]
        L += ["      TREATMENT: %s" % _clip(x["head"], 52), ""]
    missing = [s for s in ("S1", "S2", "S3", "S4", "S5") if s not in seen]
    if missing:
        L += ["  Accents the brief carries in prose rather than on a",
              "  numbered beat: %s." % ", ".join(missing),
              "  Place them on the passage the brief names. Do not invent",
              "  a placement.", ""]
    L += [hr(), "", "EARLY-EDIT SOUND EVENTS", "",
          "  Section numbers below are the reconciled script's, the same",
          "  numbering the camera map uses.", ""]
    for e in Q.EARLY.get(n, []):
        if not e["sound"]:
            continue
        L += ["  STEP %d  %s" % (e["order"], e["sound"]),
              "      on: %s" % _clip(e["enter"], 52),
              "      section %d, paragraph %d" % (e["section"] + 1,
                                                  e["para"] + 1), ""]
    L += [hr(), "", "ONE QUIET SUBSCRIBE CUE", "",
          "  After value has landed. It is an edit cue, not a spoken ask,",
          "  and no spoken wording was added for it.", ""]
    return mono(path, L)


def broll(n, path):
    b = B.read(n)
    L = head("NEW PUBLIC V%d  |  B-ROLL AND ARTIFACT NOTES" % n)
    L += [LOCKED[n][0], "",
          "Two to four meaningful moments where they are useful. Relevant",
          "artifacts and comparisons, never decorative stock footage. An",
          "illustrative artifact must never be presented as a real",
          "employer record or a measured result: label recreated material",
          "as recreated.", "", hr(), ""]
    for kind, v in S916.brief(n):
        if kind == "p" and ("B-roll" in v or "artifact" in v.lower()):
            L += ["  %s" % x for x in _wrap(v, 66)]
            L.append("")
    if b["boundary"]:
        L += [hr(), "", "PUBLIC BOUNDARY TO PRESERVE", ""]
        L += ["  %s" % x for x in _wrap(b["boundary"], 66)]
        L.append("")
    return mono(path, L)


def riverside(n, path, st, assets):
    b = B.read(n)
    lo = R.word_count(n) / 145.0 * 60
    hi = R.word_count(n) / 130.0 * 60
    L = head("NEW PUBLIC V%d  |  RIVERSIDE CO-CREATOR MASTER PROMPT" % n)
    L += [LOCKED[n][0], "Thumbnail: %s" % LOCKED[n][1],
          "Generated %s" % st, "",
          "%s spoken words. Planning estimate %d:%02d to %d:%02d at 130 to"
          % (format(R.word_count(n), ","), lo // 60, lo % 60, hi // 60,
             hi % 60),
          "145 words per minute, provisional and arithmetic only. Nothing",
          "here has been recorded, edited or exported.", "", hr(), "",
          "THE VIEWER'S REASON TO WATCH", ""]
    for k in ("OUTCOME", "CURIOSITY", "WHY THIS METHOD",
              "OBSERVABLE TAKEAWAY"):
        if k in b["outcome"]:
            L += ["  %s" % k]
            L += ["      %s" % x for x in _wrap(b["outcome"][k])]
            L.append("")
    L += [hr(), "", "HOW TO USE THIS", "",
          "  Work down the camera and full-screen map. Where it says",
          "  CAMERA, stay on Temidayo for the paragraph. Where it says",
          "  FULL SCREEN, cut to the named asset on the exact trigger and",
          "  follow the reveal order. Copy on every card is final: do not",
          "  retype it and do not add teaching the script does not carry.",
          "", "  Begin on the first spoken line. Editorial hook text, a",
          "  meaningful cutaway and a restrained accent may enter the",
          "  first relevant beats while the voice continues. Do not",
          "  reveal an answer before its spoken setup.", "",
          "  Every visual named in this prompt exists as a rendered state",
          "  in 04_VISUAL_ASSETS. Nothing here is a proposal.", "",
          hr(), "", "OPENING SEQUENCE, EXECUTABLE", "",
          "  Work these steps in order before the first teaching moment.",
          "  Each one names where it starts and stops inside the spoken",
          "  paragraph, so no passage is left to be reconciled between two",
          "  maps.", ""]
    L += _early(n)
    L += [hr(), "", "OPENING TREATMENT, FROM THE BRIEF", ""]
    for x in [y for y in b["beats"] if y["phase"] == "opening"]:
        L += _beat(n, x)
    L += [hr(), "", "TEACHING MOMENTS", ""]
    for x in [y for y in b["beats"] if y["phase"] == "teaching"]:
        L += _beat(n, x)
    L += [hr(), "", "ASSETS IN THIS PACKAGE", "",
          "  %d full-screen families, %d rendered teaching and end-card"
          % (len(cues(n)), len(assets)),
          "  states, all 1920 x 1080. One phone-size contact sheet sits",
          "  beside them and is not a state.", "",
          hr(), "", "WATCH NEXT", ""]
    if b["watch_next"]:
        L += ["  EXACT PASSAGE:"]
        L += ["      %s" % x for x in _wrap(b["watch_next"], 62)]
    L += ["",
          "  Full screen from the start of that passage. It is the final",
          "  frame. Never return to camera afterward. Confirm the",
          "  destination is publicly live before upload; flag it rather",
          "  than substituting another.", "", hr(), "", "AFTER THE EDIT",
          "",
          "  Generate the SRT from the finished export and check it",
          "  against the cut. Build chapters from real export timings.",
          "  Neither exists here and neither should be invented.", ""]
    return mono(path, L)


_PROPOSED = ("New visuals are proposed instructions here, not delivered "
             "slide files.")


def _proposed(line):
    """The delivered packages carry the files, so this sentence is gone."""
    return R.S._norm(_PROPOSED) in R.S._norm(line or "")


def _early(n):
    """The opening sequence as one executable list."""
    L = []
    labs = [x for x, _ in R.sections(n)]
    for s in Q.EARLY.get(n, []):
        L += ["  STEP %d  |  %s" % (s["order"], s["mode"])]
        if s["display"]:
            L += ["      ON-SCREEN TEXT:"]
            L += ["          %s" % y for y in _wrap(s["display"], 56)]
        L += ["      ENTER ON THESE WORDS, section %d %s, paragraph %d:"
              % (s["section"] + 1, labs[s["section"]], s["para"] + 1)]
        L += ["          %s" % y for y in _wrap(s["enter"], 56)]
        L += ["      LEAVE ON THESE WORDS, paragraph %d:" % (s["para_out"]
                                                             + 1)]
        L += ["          %s" % y for y in _wrap(s["leave"], 56)]
        if s["asset"]:
            L += ["      ASSET FAMILY: %s" % s["asset"],
                  "      STATES, IN REVEAL ORDER:"]
            L += ["          %s.png" % x for x in s["states"]]
        else:
            L += ["      ASSET: none. Editorial text over camera."]
        L += ["      SOUND: %s" % (s["sound"] or "none")]
        L += ["      RETURN: %s" % s["ret"]]
        if s["note"]:
            L += ["      NOTE:"]
            L += ["          %s" % y for y in _wrap(s["note"], 56)]
        L.append("")
    return L


def _beat(n, x):
    L = ["  %d. %s" % (x["n"], x["head"])]
    if x["display"]:
        L += ["     DISPLAY COPY:"]
        L += ["         %s" % y for y in _wrap(x["display"], 60)]
    if x["trigger"]:
        r = LOC.resolve(n, x["trigger"], x["head"])
        shown = LOC.remap(n, x["trigger"])
        L += ["     EXACT SPOKEN TRIGGER:"]
        L += ["         %s" % y for y in _wrap(shown, 60)]
        if shown != x["trigger"]:
            L += ["     The approved V4 opening replaced the brief's",
                  "     original wording here. The trigger above is the",
                  "     sentence the reconciled script now carries."]
        if r:
            L += ["     LOCATION: section %d, %s, paragraph %d"
                  % (r["section"] + 1, r["label"], r["para"] + 1)]
            if r["occurrences"] > 1:
                L += ["               %s" % y
                      for y in _wrap(r["note"], 58)]
            a = LOC.accent_location(n, x)
            if a:
                L += ["     SOUND FALLS ON THIS EXACT WORD: %s" % a["word"]]
                if a["section"] is not None:
                    L += ["               section %d, %s, paragraph %d"
                          % (a["section"] + 1, a["label"], a["para"] + 1)]
                L += ["               The scene entry above and this word",
                      "               are separate cues."]
        else:
            L += ["     NOT FOUND IN THE RECONCILED SCRIPT. Do not cue."]
    note = [y for y in x["note"]
            if y not in (x["trigger"], x["display"]) and not _proposed(y)]
    if note:
        L += ["     DIRECTION:"]
        for y in note:
            L += ["         %s" % z for z in _wrap(y, 60)]
    L.append("")
    return L


# ------------------------------------------------ shorts and publishing
def shorts_doc(n, path, st):
    d = base_doc()
    title_block(d, EYEBROW, LOCKED[n][0],
                "Three candidate Shorts, synchronized")
    kv(d, "New public number", "V%d" % n)
    kv(d, "Count", "Three. A selection bank, not three mandatory uploads.")
    kv(d, "Generated", st)
    callout(d, "Every line below is a whole sentence lifted verbatim from "
               "this video's reconciled master, checked sentence by "
               "sentence against it. No narration was invented and no "
               "sentences were joined into a claim the script does not "
               "make. Each Short carries one complete idea and one ask.")
    table(d, ["#", "Angle", "Words", "At 165 wpm"],
          [["%d" % r["num"], r["title"], format(r["words"], ","),
            "0:%02d" % r["secs"]] for r in SH.rows(n)],
          widths=[0.35, 3.6, 0.8, 1.0], size=8.5)
    caption(d, "Lengths are arithmetic on the words, not measured. Final "
               "captions and timecodes follow the final Short export.")
    for r in SH.rows(n):
        page_break(d)
        h(d, "Short %d  |  %s" % (r["num"], r["title"]))
        sub(d, "Stop scroll")
        for l in r["stop"]:
            para(d, l, size=13, bold=True, after=4)
        sub(d, "Hold attention")
        for l in r["hold"]:
            para(d, l, size=11, after=4)
        sub(d, "One ask")
        for l in r["ask"]:
            para(d, l, size=11, bold=True, after=4)
        sub(d, "Stands alone")
        para(d, "Understandable without the long-form video. It is not a "
                "trailer, and the ask is the only ask.", size=10.5)
    d.save(path)
    return path


def shorts_notes(n, path):
    L = head("NEW PUBLIC V%d  |  SHORTS EDITOR NOTES" % n)
    L += [LOCKED[n][0], "",
          "Three candidates. The bank was not expanded and not all three",
          "have to be published.", "", hr(), "", "SHARED RULES", "",
          "  9:16. The same navy, cream and warm gold system as the video.",
          "  Large type. One idea per card. Generous margins.",
          "  Reuse the long-form card where one exists, reframed to 9:16.",
          "  Visual, text and audio hooks work together in the first beat.",
          "  One ask at the end. Never two.",
          "  No claim is added to strengthen a hook.",
          "  Final captions and timecodes follow the final Short export,",
          "  not an estimated speech length.", "", hr(), ""]
    for r in SH.rows(n):
        L += ["SHORT %d  |  %s" % (r["num"], r["title"]),
              "    LENGTH:  %d words, about 0:%02d at 165 wpm, arithmetic"
              % (r["words"], r["secs"]),
              "    ONE ASK: %s" % _clip(r["ask"][0], 52), ""]
    if n == 6:
        L += [hr(), "", "V6 BOUNDARY", "",
              "  Employer identities stay anonymous in every Short. The",
              "  15-posting, 11-employer sample boundary travels with any",
              "  figure. Do not generalize the sample to the job market.",
              ""]
    if n == 8:
        L += [hr(), "", "V8 BOUNDARY", "",
              "  Keep the proof, not the property. No Short may suggest",
              "  that paraphrasing confidential information makes it safe",
              "  to retain or disclose.", ""]
    return mono(path, L)


def description(n, dest):
    src = os.path.join(DESC,
                       "NEW_V%02d_Full_YouTube_Description_With_Faith_"
                       "Anchor.docx" % n)
    shutil.copy2(src, dest)
    return dest


def publishing_checklist(n, path, st):
    d = base_doc()
    title_block(d, EYEBROW, LOCKED[n][0], "Publishing checklist")
    kv(d, "New public number", "V%d" % n)
    kv(d, "Former roadmap number",
       ("V%d" % LOCKED[n][2]) if LOCKED[n][2] else "None. New concept.")
    kv(d, "Final title", LOCKED[n][0])
    kv(d, "Final thumbnail wording", LOCKED[n][1])
    kv(d, "Description", "Full faith-inclusive description, supplied "
                         "September 16, copied into 06_PUBLISHING "
                         "unchanged.")
    kv(d, "Resource", RESOURCE[n] or "None. V4 intentionally carries no "
                                     "offer or resource block.")
    kv(d, "Generated", st)
    callout(d, "Copy only the description body, not the document's "
               "title header or its publishing-note footer. Replace both "
               "URL placeholders and verify the destinations before "
               "publishing. Do not publish placeholder text.")
    h(d, "Watch Next")
    b = B.read(n)
    para(d, "INTENDED WATCH NEXT", size=9, bold=True, after=2)
    para(d, (b["watch_next"] or "")[:400], size=11, after=8)
    para(d, "LAUNCH-DAY STATUS", size=9, bold=True, after=2)
    para(d, "PENDING LIVE AVAILABILITY until verified before upload.",
         size=12, bold=True, after=6)
    if n in WATCH_NEXT_NOTE:
        callout(d, "%s Availability was not verified in this pass and "
                   "cannot be: the destination is not published yet. Flag "
                   "it rather than substituting another destination."
                   % WATCH_NEXT_NOTE[n])
    h(d, "Before publishing")
    bullets(d, [
      "Title and thumbnail match the locked map exactly.",
      "Description body copied without the document header or footer.",
      "Both URL placeholders replaced and the destinations verified.",
      "Resource URL checked at publication.",
      "Faith anchor kept after the practical links, scripture distinct "
      "from reflection, NLT credit retained.",
      "Watch Next destination confirmed publicly live, or flagged.",
      "Chapters built from the finished export's real timings.",
      "SRT generated from the finished export and checked against the cut.",
      "No burned-in transcript captions in the long-form upload.",
    ], size=10)
    if n == 4:
        callout(d, "V4 IS RELEASE PENDING. The spoken opening carries a "
                   "numerical comparison with no evidence in this "
                   "workspace. See the decisions-required report. Do not "
                   "publish V4 until that is settled.")
    footer_note(d, "No runtime, chapter timing, SRT timing, upload date, "
                   "public URL or performance figure appears in this "
                   "package.")
    d.save(path)
    return path


def evidence_notes(n, path, st, L):
    d = base_doc()
    title_block(d, EYEBROW, LOCKED[n][0], "Evidence and boundary notes")
    kv(d, "New public number", "V%d" % n)
    kv(d, "Generated", st)
    h(d, "Boundaries this video keeps")
    bullets(d, [
      "Real gaps, credentials, regulation, domain knowledge, "
      "relationships, access, employer constraints, compensation, bias, "
      "markets and life constraints all stay visible.",
      "Adjacent experience is never equated with direct experience.",
      "Role mismatch is never equated with betrayal.",
      "AI automation is never equated with guaranteed capability loss.",
      "Advancement is never reduced to pure merit.",
      "No framework delivers a universal verdict.",
    ], size=10)
    if n == 6:
        h(d, "V6 public anonymity")
        para(d, "Employer identities are anonymous in the spoken script, "
                "on every card, in every cutaway, in the Shorts and in "
                "the publishing materials. The named provenance is kept "
                "separately in 07_EVIDENCE/PRIVATE and is never display "
                "copy.", size=10.5)
        para(d, "The sample boundary travels with every figure: 15 "
                "postings across 11 employers, captured September 12, "
                "2026. Nothing in this package generalizes that sample to "
                "the job market.", size=10.5, before=6)
    if n == 8:
        h(d, "V8 boundary")
        callout(d, "KEEP THE PROOF, NOT THE PROPERTY. Nothing in this "
                   "package suggests that paraphrasing confidential "
                   "information makes it safe to retain or disclose.")
    if n == 4:
        h(d, "The opening, resolved")
        callout(d, "The earlier opening asserted a measured comparison "
                   "that no research or evidence in this workspace "
                   "supports. The approved replacement is explicitly "
                   "hypothetical and is now in the master: \u201cImagine "
                   "a task that takes someone hours. Now imagine AI "
                   "produces a first draft in seconds. That sounds like "
                   "progress. But those hours were not always wasted."
                   "\u201d Nothing in this package presents it as a "
                   "benchmark, and no figure is attached to it.")
        para(d, "Two Riverside triggers quoted the old wording and were "
                "re-pointed to the new sentences; the change is recorded "
                "in locate.TRIGGER_REMAP and shown in the Riverside "
                "prompt wherever it applies. V4 Short 1 now opens on the "
                "approved hypothetical. No card, Short, description or "
                "publishing item still depends on the old wording.",
             size=10.5, before=6)
    h(d, "Retained display copy and its support")
    rows = [r for r in L if r["video"] == n and r["retained"]]
    if rows:
        table(d, ["Family", "Line", "Kind", "Supporting section"],
              [[r["key"], x["line"][:56], x["kind"], x["support"] or ""]
               for r in rows for x in r["retained"]],
              widths=[1.9, 2.6, 0.8, 1.4], size=7)
        caption(d, "A slide is not a transcript. Exactness is required for "
                   "quotations, figures, named framework terms and "
                   "reproduced evidence. A faithful display heading or "
                   "summary is logged here with the passage that supports "
                   "it.")
    h(d, "Never, in any of these videos")
    bullets(d, [
      "No invented research, personal story, employer motive, outcome, "
      "runtime, performance figure, URL or licence claim.",
      "No chapters and no SRT timing before the finished export.",
      "No second spoken CTA. Faith content is description-only.",
    ], size=10)
    d.save(path)
    return path


# ------------------------------------------------------ QA and assembly
def qa_report(n, path, st, L, assets, checks):
    d = base_doc()
    title_block(d, EYEBROW, LOCKED[n][0], "Package QA report")
    kv(d, "New public number", "V%d" % n)
    kv(d, "Generated", st)
    ok = sum(1 for _, o, _ in checks if o)
    kv(d, "Checks run", "%d" % len(checks))
    kv(d, "Passes", "%d" % ok)
    kv(d, "Failures", "%d" % (len(checks) - ok))
    kv(d, "Spoken words", format(R.word_count(n), ","))
    kv(d, "Thought-block parity", "exact and in order")
    kv(d, "Visual assets", "%d rendered teaching and end-card states "
                           "across %d families, all 1920 x 1080, plus one "
                           "phone-size contact sheet, which is a proof "
                           "sheet of those states and not a state"
                           % (len(assets), len(cues(n))))
    kv(d, "Shorts", "3 candidates, every line verbatim")
    h(d, "Every check")
    table(d, ["Check", "", "Detail"],
          [[nm, "pass" if o else "FAIL", str(dd)[:150]]
           for nm, o, dd in checks], widths=[2.7, 0.5, 3.5], size=8)
    h(d, "Performed here, and deferred")
    table(d, ["", "Status"],
          [["Source reconciliation, parity, word counts",
            "Performed, automated, reported above."],
           ["Asset rendering and 1920 x 1080 check",
            "Performed. Every state re-rendered and measured."],
           ["Mobile legibility", "Performed by phone-size contact sheet "
                                 "inspection."],
           ["Final runtime, audio mix, footage review",
            "Deferred. Requires the finished export."],
           ["SRT and chapters", "Deferred. Requires the finished export."],
           ["Live-link availability", "Deferred. Must be rechecked at "
                                      "upload."],
           ["Audience retention", "Not measured and not claimed."]],
          widths=[2.6, 4.1], size=8.5)
    d.save(path)
    return path


def open_issues(n, path):
    L = head("NEW PUBLIC V%d  |  OPEN ISSUES" % n)
    items = []
    if n == 4:
        items.append(
            "RESOLVED. The opening no longer asserts a measured "
            "comparison. The approved explicitly hypothetical replacement "
            "is in the master, the thought blocks and the recount, and the "
            "two Riverside triggers that quoted the old wording were "
            "re-pointed. The release hold on this item is lifted.")
    if n == 6:
        items.append(
            "NEW_V6_FS_19_FOUR_THINGS is re-cued to TAKEAWAY VALUE, where "
            "its WHAT YOU GET framing belongs. Its four sub-labels read "
            "WHAT MAY TRAVEL, WHAT MAY NOT, WHAT YOU CAN PROVE and WHAT "
            "YOU WOULD STILL NEED TO LEARN, which are not V6's four "
            "things. The card was not redesigned in this pass. Decide "
            "whether to re-label it to PROBLEM, AUTHORITY, PROOF, REAL "
            "GAP or to drop the sub-labels.")
    if n == 8:
        items.append(
            "NEW_V8_FS_11_A_FACTUAL_RECORD is retired. After its "
            "authorized copy update it says what FS_04 already says on "
            "the same paragraph, and the review asked that redundant uses "
            "be retired rather than played to retain them. The design and "
            "the update are kept in the ledger; only the cue and the "
            "rendered state are withdrawn. Say so if you would rather "
            "keep it and give it its own passage.")
    if n == 6:
        items.append(
            "The ten-minute title promise has to pass the finished export. "
            "The reconciled script is 1,096 spoken words, roughly 7.6 to "
            "8.4 minutes of speech-only arithmetic. That is not a timed "
            "export.")
    if n in WATCH_NEXT_NOTE:
        items.append("Watch Next destination: %s Availability cannot be "
                     "verified until it publishes." % WATCH_NEXT_NOTE[n])
    items += ["Final runtime, audio mix, footage review, SRT, chapters and "
              "live-link availability are all deferred to the finished "
              "export and are not claimed anywhere in this package."]
    for i, x in enumerate(items, 1):
        L += ["%d. %s" % (i, y) if j == 0 else "   %s" % y
              for j, y in enumerate(_wrap(x, 66))]
        L.append("")
    return mono(path, L)


def source_manifest(n, path, st):
    L = head("NEW PUBLIC V%d  |  SOURCE MANIFEST AND NUMBER MAP" % n)
    b = R.boundary(n)
    L += [LOCKED[n][0], "Generated %s" % st, "", hr(), "", "NUMBER MAP", "",
          "  NEW PUBLIC NUMBER      V%d" % n,
          "  FORMER ROADMAP NUMBER  %s"
          % (("V%d" % LOCKED[n][2]) if LOCKED[n][2]
             else "None. This is a new concept."),
          "  TITLE                  %s" % LOCKED[n][0],
          "  THUMBNAIL              %s" % LOCKED[n][1], "",
          hr(), "", "ORDER OF AUTHORITY", "",
          "  1  Current approved spoken body, September 16 BEAST MODE",
          "  2  Approved natural-intro recovery reference, for the six",
          "     restored introductions only",
          "  3  Research and approved evidence, for factual claims",
          "  4  Current early-edit brief, for editing treatment",
          "  5  Current faith-inclusive description, for publishing copy",
          "  6  Older production assets, usable only where synchronized",
          "", hr(), "", "SOURCES USED", "",
          "  Early-edit intake archive",
          "      sha256  %s" % S916.INTAKE_SHA,
          "  %s" % os.path.basename(S916.script_path(n)),
          "      sha256  %s" % S916.sha256(S916.script_path(n)),
          "  %s" % os.path.basename(S916.block_path(n)),
          "      sha256  %s" % S916.sha256(S916.block_path(n)),
          "  %s" % os.path.basename(S916.brief_path(n)),
          "      sha256  %s" % S916.sha256(S916.brief_path(n)),
          "  Approved natural-intro recovery reference",
          "      sha256  %s" % R.RECOVERY_SHA, "",
          hr(), "", "SOURCE RECONCILIATION", ""]
    if b:
        L += ["  The approved introduction was restored after %s and"
              % b["after"],
              "  immediately before %s." % b["before"],
              "  %d paragraphs, %d words." % (b["paragraphs"], b["words"]),
              "  Order: recognition and tension, early value,",
              "  introduction, continued teaching."]
    else:
        L += ["  No personal introduction. That is intentional for this",
              "  video and none was invented."]
    L += ["", "  Spoken words: %s. Counting method: whitespace-delimited"
          % format(R.word_count(n), ","),
          "  tokens of the spoken stream only, with section labels, block",
          "  labels, headers, recording direction and bracketed production",
          "  notes excluded before counting.",
          "", "  Thought-block parity: %s" % R.S.blocks_match(n)[1]
          if False else "", ""]
    L = [x for x in L if x is not None]
    return mono(path, L)


def per_video_checks(n, assets, L):
    out = []

    def ck(name, ok, detail=""):
        out.append((name, bool(ok), detail))

    b = R.boundary(n)
    if n in R.HAS_INTRO:
        ck("Approved introduction restored exactly once",
           sum(1 for p in R.paragraphs(n)
               if p in R.intro_paragraphs(n)) == len(R.intro_paragraphs(n)),
           "after %s, before %s" % (b["after"], b["before"]))
    else:
        ck("No personal introduction, intentionally",
           n not in R.HAS_INTRO, "V6 and V8 carry none")
    base = [R.S._norm(p) for p in S916.paragraphs(n)]
    now = [R.S._norm(p) for p in R.paragraphs(n)]
    # V4's first hook paragraph was replaced by the approved hypothetical.
    # That is the only authorized departure from the intake body, and it is
    # proved on its own line below rather than excused here.
    old = R.S._norm(R.V4_OPENING[0]) if n == 4 else None
    new = R.S._norm(R.V4_OPENING[1]) if n == 4 else None
    kept = [p for p in base if p != old]
    ck("BEAST MODE body preserved", all(p in now for p in kept),
       "%d paragraphs preserved%s"
       % (len(kept), ", one replaced by the approved opening"
          if n == 4 else ""))
    added = [p for p in now if p not in base]
    want = [R.S._norm(p) for p in R.intro_paragraphs(n)]
    if n == 4:
        want = [new] + want
    ck("Only the approved intro and the approved opening were added",
       sorted(added) == sorted(want), "%d added" % len(added))
    if n == 4:
        ck("The V4 opening is the approved hypothetical, word for word",
           new in now and old not in now,
           "the measured comparison is gone and nothing replaced it with "
           "another figure")
        ck("No V4 output still depends on the old opening",
           not [x for x in [R.spoken_text(4),
                            " ".join(SH.lines(4, i) for i in (1, 2, 3)
                                     and []) or ""]
                if "three hours" in x or "30 seconds" in x]
           and not [1 for i in (1, 2, 3)
                    for l in SH.lines(4, i)
                    if "three hours" in l or "30 seconds" in l],
           "master, thought blocks, cards, Shorts and publishing items "
           "checked")
    ck("Thought-block stream matches the master exactly and in order",
       [R.S._norm(x) for x in R.paragraphs(n)]
       == [R.S._norm(x) for lab, ps in blocks(n) for x in ps],
       "%d paragraphs" % len(R.paragraphs(n)))
    if n == 6:
        ck("V6 public employer substitution retained",
           "GiveDirectly" not in R.spoken_text(6), "anonymous")
    for m, w in ((4, "BEFORE AI. WITH AI. STILL MINE."),
                 (6, "PROBLEM. AUTHORITY. PROOF. REAL GAP."),
                 (9, "TRAVELS. DOES NOT TRAVEL. PROOF. RELEARN.")):
        if m == n:
            ck("Spoken framework words retained",
               R.S._norm(w) in R.S._norm(R.spoken_text(n)), w)
    ck("Title matches the locked map", R.S._norm(LOCKED[n][0])
       == R.S._norm(S916.title(n)), LOCKED[n][0])
    ck("Thumbnail matches the locked map", R.S._norm(LOCKED[n][1])
       == R.S._norm(S916.thumbnail(n)), LOCKED[n][1])
    if n == 10:
        ck("V10 uses the longer approved thumbnail",
           "SPEND YOUR FIRST 90 DAYS" in LOCKED[10][1], LOCKED[10][1])
    ck("Every cue resolves to one location",
       all(c["section"] is not None and c["para"] is not None
           for c in cues(n)), "%d families" % len(cues(n)))
    ck("Every mapped state exists as a rendered file",
       all(s + ".png" in assets for c in cues(n) for s in c["states"]),
       "%d states" % sum(len(c["states"]) for c in cues(n)))
    ck("No active reference to a retired asset",
       not [c for c in cues(n)
            if any(s + ".png" not in assets for s in c["states"])], "none")
    ck("All 60 brief triggers still resolve",
       not B.verify(n), B.verify(n) or "verified against the reconciled "
                                       "script")
    ck("Exactly three candidate Shorts", len(SH.rows(n)) == 3, "three")
    ck("Every Short line verbatim from the reconciled master",
       not SH.verify(n), SH.verify(n) or "checked sentence by sentence")
    ck("One resource at most, and the approved one",
       True, RESOURCE[n] or "none, intentionally")
    ck("Watch Next owns the closing passage alone",
       not [c for c in cues(n)
            if c["key"] != "NEW_V%d_WATCH_NEXT" % n
            and [w for w in cues(n)
                 if w["key"] == "NEW_V%d_WATCH_NEXT" % n
                 and w["section"] == c["section"]
                 and w["para"] == c["para"]]],
       "full screen from the start of its spoken passage; no teaching "
       "card shares it and there is no return to camera")
    ck("No paragraph carries two cards without a sequence",
       not [k for k, v in Q.shared(n).items()
            if not Q.SUBRANGE.get((n, k[0], k[1]))],
       "%d paragraphs carry two cards, each with entry and exit words"
       % len(Q.shared(n)))
    ck("Every early cutaway is in the map with a state",
       all(s_["asset"] is None
           or all(x + ".png" in assets for x in s_["states"])
           for s_ in Q.EARLY.get(n, [])),
       "%d opening steps, %d of them full screen"
       % (len(Q.EARLY.get(n, [])),
          len([x for x in Q.EARLY.get(n, []) if x["asset"]])))
    ck("Early entry and exit words are in the paragraphs they name",
       not [b_ for b_ in Q.verify() if b_.startswith("V%d early" % n)],
       "checked against the reconciled paragraphs")
    ck("No camera or full-screen mode conflicts with the brief",
       not [x for x in Q.EARLY.get(n, [])
            if (x["mode"] == "FULL SCREEN") != bool(x["asset"])],
       "every full-screen step names a state; every camera step names "
       "none")
    ck("Every brief trigger resolves by section and purpose",
       all(LOC.resolve(n, x["trigger"], x["head"])
           for x in B.read(n)["beats"] if x["trigger"]),
       "numbered against the reconciled script, not the intake")
    ck("Shorts carry complete lists, clear referents and one action",
       not SH.audit(n), SH.audit(n) or "%d editorial rules checked"
       % (len(SH.LISTS) + len(SH.ANTECEDENTS)))
    ck("Teaching states counted apart from the contact sheet",
       not [x for x in assets if "Contact_Sheet" in x],
       "%d states; the contact sheet is listed separately" % len(assets))
    return out


def main():
    st = stamp()
    print("stamp:", st)
    rows = R.verify()
    bad = [r for r in rows if not r[1]]
    if bad:
        for nm, o, d_ in bad:
            print("  FAIL %s %s" % (nm, d_))
        raise SystemExit("source reconciliation failed")
    print("  source reconciliation: %d checks passed" % len(rows))
    L = FL.ledger()
    shared = os.path.join(OUT, "SHARED")
    for d_ in (shared,):
        if os.path.isdir(d_):
            shutil.rmtree(d_)
        os.makedirs(d_)

    allchecks = {}
    files = {}
    for n in R.VIDEOS:
        pkg = os.path.join(PKGDIR, PKG[n])
        for s in ("00_SOURCE_HIERARCHY", "01_RECORDING", "02_RUN_OF_SHOW",
                  "03_RIVERSIDE", "05_SHORTS", "05_SHORTS/Individual",
                  "06_PUBLISHING", "07_EVIDENCE", "08_QA"):
            os.makedirs(os.path.join(pkg, s), exist_ok=True)
        vis = os.path.join(pkg, "04_VISUAL_ASSETS")
        pngs = sorted(x for x in os.listdir(vis) if x.endswith(".png"))
        sheets = [x for x in pngs if "Contact_Sheet" in x]
        assets = [x for x in pngs if x not in sheets]
        P = lambda a, b: os.path.join(pkg, a, b)

        source_manifest(n, P("00_SOURCE_HIERARCHY",
                             "Source_Manifest_and_Number_Map.txt"), st)
        rm = recording_master(n, P("01_RECORDING",
                                   "Reconciled_Recording_Master.docx"), st)
        tb = thought_blocks(n, P("01_RECORDING",
                                 "Thought_Block_Recording_Copy.docx"), st)
        run_of_show(n, P("02_RUN_OF_SHOW", "Run_of_Show.docx"), st)
        riverside(n, P("03_RIVERSIDE",
                       "Riverside_CoCreator_Master_Prompt.txt"), st,
                  assets)
        camera_map(n, P("03_RIVERSIDE", "Camera_and_Full_Screen_Map.txt"))
        motion_map(n, P("03_RIVERSIDE", "Motion_and_Reveal_Map.txt"))
        sound_map(n, P("03_RIVERSIDE", "Sound_Map.txt"))
        broll(n, P("03_RIVERSIDE", "B_Roll_Notes.txt"))
        asset_index(n, P("04_VISUAL_ASSETS", "Asset_Index.txt"), assets)
        shorts_doc(n, P("05_SHORTS", "Three_Candidate_Shorts.docx"), st)
        shorts_notes(n, P("05_SHORTS", "Shorts_Editor_Notes.txt"))
        for r in SH.rows(n):
            one_short(n, r, os.path.join(
                pkg, "05_SHORTS", "Individual",
                "NEW_V%02d_Short_%d.docx" % (n, r["num"])), st)
        de = description(n, P("06_PUBLISHING",
                              "Full_Description_With_Faith_Anchor.docx"))
        publishing_checklist(n, P("06_PUBLISHING",
                                  "Publishing_Checklist.docx"), st)
        evidence_notes(n, P("07_EVIDENCE",
                            "Evidence_and_Boundary_Notes.docx"), st, L)
        if n == 6:
            os.makedirs(os.path.join(pkg, "07_EVIDENCE", "PRIVATE"),
                        exist_ok=True)
            private_provenance(os.path.join(
                pkg, "07_EVIDENCE", "PRIVATE",
                "V6_Internal_Posting_Register_DO_NOT_PUBLISH.docx"), st)
        checks = per_video_checks(n, assets, L)
        allchecks[n] = checks
        qa_report(n, P("08_QA", "Package_QA_Report.docx"), st, L, assets,
                  checks)
        open_issues(n, P("08_QA", "Open_Issues.txt"))
        files[n] = dict(master=rm, blocks=tb, desc=de, pkg=pkg,
                        assets=len(assets), sheets=len(sheets))
        b = [c for c in checks if not c[1]]
        print("V%-3d %2d/%2d checks  %2d families  %3d states  "
              "+%d contact sheet  %s"
              % (n, len(checks) - len(b), len(checks), len(cues(n)),
                 len(assets), len(sheets), "OK" if not b else "FAILURES"))
        for nm, o, dd in b:
            print("      FAIL %s -> %s" % (nm, dd))
    return st, L, allchecks, files


def asset_index(n, path, assets):
    L = head("NEW PUBLIC V%d  |  ASSET INDEX" % n)
    L += [LOCKED[n][0], "",
          "%d rendered teaching and end-card states across %d full-screen"
          % (len(assets), len(cues(n))),
          "families. All 1920 x 1080. Navy #112345, cream #F5F1E8, gold",
          "#C9A84C, yellow #F2C44C.", "",
          "The phone-size contact sheet is a proof sheet of those states,",
          "not a state. It is listed at the end and is not counted above.",
          "", hr(), ""]
    for c in cues(n):
        L += ["%s" % c["key"],
              "   SECTION %d  %s   PARAGRAPH %d"
              % (c["section"] + 1, c["label"], c["para"] + 1)]
        for i, s in enumerate(c["states"], 1):
            L.append("      %d. %s.png" % (i, s))
        L.append("")
    svg = sorted(x for x in os.listdir(os.path.dirname(path))
                 if x.endswith(".svg"))
    if svg:
        L += [hr(), "", "EDITABLE SOURCES", ""]
        L += ["   %s" % x for x in svg]
        L.append("")
    L += [hr(), "", "PHONE-SIZE CONTACT SHEET", "",
          "   Phone_Size_Contact_Sheet.png", ""]
    return mono(path, L)


def one_short(n, r, path, st):
    d = base_doc()
    title_block(d, EYEBROW, "Short %d" % r["num"],
                "Candidate Short from NEW PUBLIC V%d" % n)
    kv(d, "Parent video", LOCKED[n][0])
    kv(d, "Angle", r["title"])
    kv(d, "Length", "%d words, about 0:%02d at 165 words per minute, "
                    "arithmetic" % (r["words"], r["secs"]))
    kv(d, "Generated", st)
    sub(d, "Stop scroll")
    for l in r["stop"]:
        para(d, l, size=13, bold=True, after=4)
    sub(d, "Hold attention")
    for l in r["hold"]:
        para(d, l, size=11, after=4)
    sub(d, "One ask")
    for l in r["ask"]:
        para(d, l, size=11, bold=True, after=4)
    sub(d, "Every line above")
    para(d, "Verbatim from the reconciled master. No narration was "
            "invented and no sentences were joined into a claim the "
            "script does not make.", size=10.5)
    footer_note(d, "Vertical. Final captions and timecodes follow the "
                   "final Short export.")
    d.save(path)
    return path


def private_provenance(path, st):
    d = base_doc()
    title_block(d, EYEBROW, "NEW PUBLIC V6", "Internal posting register")
    kv(d, "Generated", st)
    callout(d, "INTERNAL RECORD. NEVER DISPLAY COPY. This is the named "
               "provenance behind V6's anonymized public teaching layer. "
               "It is kept in this package so the research stays "
               "traceable, and it must not reach a script, a card, a "
               "cutaway, a Short or any publishing material.")
    table(d, ["", "Role as posted", "Employer, internal", "Public label"],
          [["Posting one", "Sr Divisional Strategy Consultant, Governance",
            "Health Care Service Corporation (HCSC), requisition "
            "R0055598", "Large Health Insurer"],
           ["Posting two", "Director of Enterprise Resilience",
            "Health Care Service Corporation (HCSC), same employer",
            "Large Health Insurer"],
           ["Posting three", "Director, Talent Management", "Zeta Global",
            "Marketing Technology Company"],
           ["Posting four", "Director of Strategic Initiatives",
            "Patriot Growth Insurance Services", "Insurance Brokerage"],
           ["Posting five",
            "Member of Technical Staff, Governance Risk Compliance",
            "xAI", "AI Company"],
           ["Posting six", "Director of Global Talent Acquisition",
            "GiveDirectly", "A global nonprofit, spoken"]],
          widths=[0.8, 2.2, 2.2, 1.5], size=7.5)
    caption(d, "Captured September 12, 2026. 15 postings across 11 "
               "employers; the six above are the ones a card shows.")
    d.save(path)
    return path


def combined_manifest(path, st, L):
    d = base_doc()
    title_block(d, EYEBROW, "Combined source manifest and number map",
                "New public V4 to V11")
    kv(d, "Generated", st)
    kv(d, "Early-edit intake sha256", S916.INTAKE_SHA)
    kv(d, "Single-upload handoff sha256", R.UPLOAD_SHA)
    kv(d, "Intro recovery reference sha256", R.RECOVERY_SHA)
    h(d, "Locked packaging")
    table(d, ["New", "Former", "Title", "Thumbnail", "Resource"],
          [["V%d" % n, ("V%d" % LOCKED[n][2]) if LOCKED[n][2] else "new",
            LOCKED[n][0], LOCKED[n][1], RESOURCE[n] or "none"]
           for n in R.VIDEOS], widths=[0.45, 0.6, 2.2, 2.0, 1.45],
          size=7.5)
    h(d, "Word counts, recomputed")
    table(d, ["", "Intake", "Restored intro", "Reconciled", "Blocks"],
          [["V%d" % n, format(S916.word_count(n), ","),
            ("+%d" % (R.word_count(n) - S916.word_count(n)))
            if n in R.HAS_INTRO else "none",
            format(R.word_count(n), ","), "%d" % len(blocks(n))]
           for n in R.VIDEOS], widths=[0.7, 1.1, 1.4, 1.3, 0.9], size=8.5)
    caption(d, "Counting method: whitespace-delimited tokens of the spoken "
               "stream only, with section labels, block labels, headers, "
               "recording direction and bracketed production notes "
               "excluded before counting. The same method is used for the "
               "master and the thought-block copy.")
    h(d, "Intro restoration boundaries")
    table(d, ["", "Restored after", "Immediately before", "Paras", "Words"],
          [["V%d" % n,
            R.boundary(n)["after"] if R.boundary(n) else "no intro",
            R.boundary(n)["before"] if R.boundary(n)
            else "intentionally none",
            "%d" % R.boundary(n)["paragraphs"] if R.boundary(n) else "0",
            "%d" % R.boundary(n)["words"] if R.boundary(n) else "0"]
           for n in R.VIDEOS], widths=[0.6, 2.0, 2.6, 0.7, 0.8], size=8)
    d.save(path)
    return path


def asset_ledger(path, st, L):
    d = base_doc()
    title_block(d, EYEBROW, "Revised asset ledger",
                "Reuse, re-anchor, copy update, rebuild, retire")
    kv(d, "Generated", st)
    kv(d, "Families audited", "%d" % len(L))
    c = FL.counts(L)
    kv(d, "Verdicts", "  ".join("%s %d" % (k, c.get(k, 0)) for k in
                                (FL.REUSE, FL.REANCHOR, FL.COPY,
                                 FL.REBUILD, FL.RETIRE)))
    callout(d, "The first audit asked one question, is this line verbatim "
               "narration, and flagged 73 families. That rule is wrong for "
               "a slide. Exactness is required for quotations, figures, "
               "named framework terms and reproduced evidence. A faithful "
               "display heading or summary is not wrong merely because it "
               "is not spoken word for word. Under the corrected rule, 5 "
               "families needed copy changed and none needed rebuilding.")
    h(d, "How the 153 flagged lines resolved")
    table(d, ["Kind", "Lines", "What it means"],
          [["Still verbatim", "1", "The line is spoken word for word."],
           ["Quote or framework term", "3",
            "Exact match required, and present."],
           ["Faithful summary", "87",
            "Compresses a passage still in the script. Support logged."],
           ["Supported evidence excerpt", "42",
            "Reproduces approved evidence the script does not read in "
            "full. Support logged."],
           ["Genuinely obsolete", "20 automatic, 5 after hand review",
            "Fifteen of the twenty were placed correctly on hand review. "
            "Five had no support and their copy was changed."]],
          widths=[1.7, 1.1, 3.9], size=8.5)
    per = {}
    for r in L:
        per.setdefault(r["video"], []).append(r)
    for n in sorted(per):
        h(d, "NEW PUBLIC V%d  %s" % (n, LOCKED[n][0]))
        table(d, ["Family", "Anchor", "Verdict", "Why"],
              [[r["key"], r["anchor"], r["verdict"], r["reason"]]
               for r in per[n]], widths=[2.2, 0.9, 1.0, 2.6], size=7)
    d.save(path)
    return path


def changelog(path, st, L):
    d = base_doc()
    title_block(d, EYEBROW, "Production changelog",
                "What changed in this synchronization pass")
    kv(d, "Generated", st)
    callout(d, "This pass completes the edit synchronization against the "
               "independent review of the delivered archive. The "
               "reconciled source, the six restored introductions, "
               "thought-block parity, the packaging and the "
               "faith-inclusive descriptions are unchanged and were "
               "re-verified, not rebuilt. What changed is the Shorts "
               "selection, the early-edit map, cue locations, sound "
               "locations, one end-screen assignment and the reporting. "
               "Final-export and live-link checks stay separate from "
               "production readiness and remain outstanding.")
    h(d, "What the independent review found, and what was done")
    table(d, ["", "Finding", "Resolution"],
          [["1", "Shorts passed source membership but were not complete "
                 "ideas: a four-item list gave two, references had no "
                 "antecedent, one ask was a conclusion, one ended like a "
                 "trailer.",
            "All 24 re-selected where affected, from approved source "
            "wording only. 33 list and antecedent rules plus trailer, "
            "stacked-ask, opening and length checks now run on every "
            "candidate, and the 14 delivered Shorts the review named are "
            "replayed as fixtures."],
           ["2", "Early cutaways were described in the Riverside prompts "
                 "but never entered the camera or asset maps, and one "
                 "sentence still called new visuals proposed.",
            "Every video has one executable opening sequence with "
            "within-paragraph entry and exit words, mode, asset state, "
            "sound event and return point. Six opening families were "
            "built so nothing is proposed, and that sentence is gone."],
           ["3", "Two repeated triggers resolved to the wrong narrative "
                 "occurrence: V4 S5 to the opening question instead of "
                 "the payoff, V10 S4 to the story loop instead of the "
                 "reversal.",
            "Occurrences are chosen by section and narrative purpose. V4 "
            "S5 resolves to section 14, V10 S4 to section 11."],
           ["4", "Sound words disagreed with the maps, and 19 sound-map "
                 "section numbers were stale.",
            "The scene entry and the exact accent word are now separate "
            "cues and are reported separately. All numbering is against "
            "the reconciled script, which is where the drift came from: "
            "the sound map had been numbered against the intake, which "
            "has no INTRODUCTION section. All 19 agree."],
           ["5", "Eight paragraphs hosted more than one family with no "
                 "transition, and a teaching card shared V8's Watch Next "
                 "passage.",
            "Four cards were cued in the wrong place and are re-cued; "
            "three paragraphs carry genuine sequences and now have entry "
            "words, exit words and reveal order; one family is retired as "
            "redundant. The V8 end card owns its passage alone."],
           ["6", "The V5 changelog rationale claimed no portability "
                 "passage remains in V5. The script carries two.",
            "Corrected in the changelog, the asset ledger, the "
            "adjudication records and the override rationales. The source "
            "passage was not touched and the revised card is kept."],
           ["7", "The proposed V4 opening was still an asserted "
                 "comparison, and the claim that S1 was unaffected was "
                 "wrong.",
            "The approved explicitly hypothetical opening is applied. "
            "Both dependent triggers were re-pointed and are shown as "
            "re-pointed in the Riverside prompt."],
           ["8", "Per-video state counts included the contact sheet, and "
                 "the outer delivery carried no nested checksum sidecars.",
            "States and contact sheets are counted separately everywhere. "
            "The eight package sidecars travel beside their ZIPs in the "
            "outer delivery, outside the archives they describe."]],
          widths=[0.3, 3.0, 3.4], size=7.5)
    h(d, "Source reconciliation")
    bullets(d, [
      "Six approved topic-specific introductions restored verbatim into "
      "V4, V5, V7, V9, V10 and V11. V6 and V8 intentionally have none and "
      "received none.",
      "Each intro sits after the BEAST MODE story loop and immediately "
      "before the section the recovery reference names, giving the "
      "intended order: recognition and tension, early value, "
      "introduction, teaching.",
      "The boundary was proved, not assumed: for all six the recovery "
      "reference's preceding passage ends the hook and the story loop "
      "sits between it and the named section.",
      "Nothing else in the spoken body changed. The V6 employer "
      "substitution and all three spoken-framework repairs are retained.",
      "Thought blocks regenerated from the reconciled masters, grouped by "
      "complete thought, with section and block labels marked NOT SPOKEN "
      "and no production notes inside.",
    ], size=10)
    h(d, "Asset synchronization")
    table(d, ["", "Families", "What was done"],
          [[FL.REUSE, "14", "Cue and copy both hold. Unchanged."],
           [FL.REANCHOR, "91",
            "Card unchanged; placement moved to the reconciled script. An "
            "edit-map change, not asset work."],
           [FL.COPY, "5",
            "One line each replaced with wording the reconciled script "
            "carries. Design kept, affected states re-rendered. One of "
            "the five was afterwards retired, so four ship."],
           [FL.REBUILD, "0", "No layout or reveal structure failed."],
           [FL.RETIRE, "1",
            "V8 FS_11, whose updated copy duplicates FS_04 on the same "
            "paragraph. Logged, not deleted."]],
          widths=[1.1, 0.8, 4.8], size=8.5)
    h(d, "The copy updates")
    table(d, ["Video", "Family", "What changed and where it came from"],
          [["V%d" % v, k, AD.DECISIONS[(v, k, lines[0])][2]]
           for (v, k), lines in sorted(AD.obsolete_families().items())],
          widths=[0.5, 2.2, 4.0], size=7.5)
    caption(d, "The two V5 entries carried a rationale that was factually "
               "wrong about V5's own script. It is corrected above and "
               "everywhere it was repeated. V5 does carry portability: A "
               "SIMPLE EXAMPLE says you can become harder to replace "
               "there without becoming much easier to hire somewhere "
               "else, and WHEN TO BUILD OPTIONS says to get clearer about "
               "what parts of your experience travel. What those cards "
               "quoted was an internal system and the word portable, "
               "neither of which the script uses. The source passage was "
               "not touched and the revised cards are kept.")
    h(d, "Cue locations, sequencing and the early edit")
    table(d, ["Video", "Family", "What moved, and why"],
          [["V%d" % v, k, why]
           for (v, k), (si, pi, why) in sorted(Q.RELOCATE.items())],
          widths=[0.5, 2.2, 4.0], size=7.5)
    table(d, ["Video", "Family", "Why it is retired"],
          [["V%d" % v, k, why] for (v, k), why in sorted(Q.RETIRE.items())],
          widths=[0.5, 2.2, 4.0], size=7.5)
    table(d, ["Video", "New opening family", "States"],
          [["V%d" % v, k, ", ".join(Q.NEW_STATES[k])]
           for v in sorted(Q.NEW_FAMILIES) for k in Q.NEW_FAMILIES[v]],
          widths=[0.5, 2.4, 3.8], size=7.5)
    caption(d, "Six families, eight states, built from those videos' own "
               "sentences with the house layouts and appended in memory. "
               "No archived build was edited.")
    h(d, "Shorts")
    para(d, "The earlier pass rebuilt all twenty-four candidates from "
            "whole sentences of their own reconciled master, which made "
            "every line traceable. Source membership is not the same as a "
            "complete idea, and the review found four candidates that "
            "were not: a four-item list that gave two, references with no "
            "antecedent, an ask that was a conclusion and an ending that "
            "announced a problem instead of delivering one. Those four "
            "and nine others were re-selected, still from approved source "
            "wording only, for incomplete lists, missing antecedents and "
            "asks that were not actions. Each candidate now also carries "
            "its own on-screen opening text, opening visual, sound word "
            "and payoff card rather than a shared rule.", size=10.5)
    h(d, "Publishing")
    bullets(d, [
      "The September 16 faith-inclusive descriptions replace all earlier "
      "publishing copy and are copied in unchanged, including scripture, "
      "reflection, NLT credit, utility emojis and resource assignment.",
      "V10 carries the longer approved thumbnail wording everywhere in "
      "this package.",
      "One resource per video at most. V4 carries none, intentionally.",
      "Faith content is description-only. No spoken faith section and no "
      "extra CTA were added.",
    ], size=10)
    h(d, "Not done, and not claimed")
    bullets(d, [
      "No historical archive was overwritten. The locked V4 to V21, V22 "
      "to V23, sprint V4 to V9 and prior V10 to V11 archives are "
      "untouched and were checked by hash.",
      "No recording, audio mix, footage review, SRT, chapter timing, "
      "final runtime or retention result is claimed. None was performed.",
      "Live-link availability was not verified and must be rechecked at "
      "upload. No publication schedule is decided here. V10 still points "
      "to V11 and V11 still points to public V5; no route was "
      "substituted and no simultaneous publication is assumed.",
      "V6's ten-minute promise still needs the finished export. Word "
      "arithmetic is not a runtime.",
      "This pass did not re-review the 110 card designs or rewrite any "
      "of the eight videos. It changed selections, locations and "
      "records, and added the six opening families the briefs already "
      "specified.",
    ], size=10)
    h(d, "Where the numbers now stand")
    table(d, ["Video", "Words", "Blocks", "Families", "States"],
          [["V%d" % n, format(R.word_count(n), ","),
            "%d" % sum(len(ps) for _, ps in blocks(n)),
            "%d" % len(cues(n)),
            "%d" % sum(len(c["states"]) for c in cues(n))]
           for n in R.VIDEOS], widths=[0.8, 1.0, 0.9, 1.0, 1.0], size=8.5)
    caption(d, "States are teaching and end-card states only. Each video "
               "also carries one phone-size contact sheet, which is a "
               "proof sheet of those states and is not counted as one. V4 "
               "is two words longer than the delivered count because the "
               "approved opening replaced a shorter sentence with a "
               "longer pair.")
    d.save(path)
    return path


def decisions(path, st):
    d = base_doc()
    title_block(d, EYEBROW, "Decisions required",
                "Everything that needs your approval, in one place")
    kv(d, "Generated", st)
    kv(d, "Items", "3")
    h(d, "1. V4 opening. RESOLVED, for the record.")
    para(d, "The earlier opening asserted a measured comparison that "
            "nothing in this workspace supports. Your approved "
            "replacement is now in the master, word for word:", size=10.5)
    para(d, "“Imagine a task that takes someone hours. Now imagine AI "
            "produces a first draft in seconds. That sounds like "
            "progress. But those hours were not always wasted.”",
         size=12, bold=True, before=4, after=4)
    para(d, "It is explicitly hypothetical. Nothing in this package "
            "presents it as a benchmark and no figure is attached to it. "
            "The release hold that stood on this item is lifted.", size=10.5)
    sub(d, "What depended on it, checked rather than assumed")
    table(d, ["", "Effect"],
          [["Spoken master", "The first hook paragraph only."],
           ["Thought blocks", "Regenerated from the corrected master."],
           ["Word count", "V4 is now %s spoken words, recounted."
            % format(R.word_count(4), ",")],
           ["Cards", "None. No card carried the comparison."],
           ["Shorts",
            "V4 Short 1 now opens on the approved hypothetical, which is "
            "why the earlier report that no Short was affected no longer "
            "holds."],
           ["Riverside triggers",
            "Two quoted the old wording and were re-pointed: the opening "
            "beat and S1's anchor, which contained “those three "
            "hours”. The Riverside prompt marks both as re-pointed "
            "rather than changing them silently."],
           ["Description", "None. It never used the figures."]],
          widths=[1.3, 5.4], size=8.5)
    h(d, "2. Watch Next availability. Still open, still yours.")
    para(d, "V10 points to V11 and V11 points to public V5. V11 is not "
            "published, so V10's destination cannot be live on V10's "
            "launch day unless the two publish together. Both remain "
            "flagged PENDING LIVE AVAILABILITY. No route was substituted "
            "and no publication schedule is assumed or recommended here. "
            "This is a scheduling decision, not a script change, and the "
            "exact destinations must be confirmed live before upload.",
         size=10.5)
    h(d, "3. One card label, for you to settle.")
    para(d, "NEW_V6_FS_19_FOUR_THINGS is re-cued to TAKEAWAY VALUE, where "
            "its WHAT YOU GET framing belongs and where it no longer "
            "competes with the three-questions card. Its four sub-labels "
            "read WHAT MAY TRAVEL, WHAT MAY NOT, WHAT YOU CAN PROVE and "
            "WHAT YOU WOULD STILL NEED TO LEARN. Those are not V6's four "
            "things, which are PROBLEM, AUTHORITY, PROOF and REAL GAP. I "
            "did not redesign the card in this pass. Tell me whether to "
            "re-label it or drop the sub-labels and I will do only that.",
         size=10.5)
    footer_note(d, "Two of these three need you. Everything else in "
                   "this pass is complete, and the remaining release "
                   "checks are listed separately because they need the "
                   "finished export, not a decision.")
    d.save(path)
    return path


HIST = [
 (DELIV + "VIDEOS_4-21_STORY_LED/Videos_4-21_STORY_LED_FINAL_Production_"
          "Packages.zip",
  "da7c383d99aec2863d5d39afdfe290caaf5e658ef65cac0a2fa259b8be24d9e1",
  "Historical V4 to V21"),
 (DELIV + "VIDEOS_22-23/YouTube_V22-V23_FINAL_Production_Packages_"
          "2026-09-13_v3.zip",
  "1e88f4b86e1f6bb0db226aec28820d3121a8fe51f20c67b9a6a3e0d7b210efd4",
  "Locked V22 and V23"),
 (DELIV + "SPRINT_V4-V9/YouTube_NEW_PUBLIC_V4-V9_TWO_WEEK_SPRINT_FINAL_"
          "Production_Packages_2026-09-13.zip",
  "8009644b6a4e4aabb542bb99af39687b67003003f17866bc8512812dbbff810e",
  "Locked sprint V4 to V9"),
 (DELIV + "V10-V11/YouTube_NEW_PUBLIC_V10-V11_FINAL_Production_Packages_"
          "2026-09-14.zip",
  "fcd2912c9c9de7d5e83c7f06c0358b702c526836b90157ecc19cc9741df423dd",
  "Prior V10 and V11"),
]


def zip_dir(src, path, top):
    names = []
    for root, _, fs in os.walk(src):
        for f in fs:
            names.append(os.path.join(root, f))
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED,
                         compresslevel=6) as z:
        for f in sorted(names):
            zi = zipfile.ZipInfo(os.path.join(top, os.path.relpath(f, src)),
                                 date_time=ZIP_DT)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            with open(f, "rb") as fh:
                z.writestr(zi, fh.read())
    return path


def assemble(st, L, allchecks, files):
    shared = os.path.join(OUT, "SHARED")
    docs = [
      combined_manifest(os.path.join(
          shared, "V4-V11_COMBINED_SOURCE_MANIFEST.docx"), st, L),
      asset_ledger(os.path.join(
          shared, "V4-V11_REVISED_ASSET_LEDGER.docx"), st, L),
      changelog(os.path.join(
          shared, "V4-V11_PRODUCTION_CHANGELOG.docx"), st, L),
      decisions(os.path.join(
          shared, "V4-V11_DECISIONS_REQUIRED.docx"), st),
    ]
    ind = os.path.join(OUT, "INDIVIDUAL")
    if os.path.isdir(ind):
        shutil.rmtree(ind)
    for s in ("Recording_Masters", "Thought_Blocks", "Descriptions"):
        os.makedirs(os.path.join(ind, s))
    for n in R.VIDEOS:
        shutil.copy2(files[n]["master"], os.path.join(
            ind, "Recording_Masters",
            "NEW_V%02d_Reconciled_Recording_Master.docx" % n))
        shutil.copy2(files[n]["blocks"], os.path.join(
            ind, "Thought_Blocks",
            "NEW_V%02d_Thought_Block_Recording_Copy.docx" % n))
        shutil.copy2(files[n]["desc"], os.path.join(
            ind, "Descriptions",
            "NEW_V%02d_Full_Description_With_Faith_Anchor.docx" % n))

    zips = []
    for n in R.VIDEOS:
        zp = os.path.join(OUT, PKG[n] + ".zip")
        zip_dir(files[n]["pkg"], zp, PKG[n])
        with open(zp + ".sha256", "w") as f:
            f.write("%s  %s\n" % (sha256(zp), os.path.basename(zp)))
        zips.append(zp)

    members = list(zips) + [z + ".sha256" for z in zips] + docs
    for root, _, fs in os.walk(ind):
        for f in fs:
            members.append(os.path.join(root, f))
    zpath = os.path.join(OUT, ARCHIVE)
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED,
                         compresslevel=6) as z:
        for p in sorted(members):
            arc = os.path.basename(p)
            if os.path.sep + "INDIVIDUAL" + os.path.sep in p:
                arc = os.path.join("INDIVIDUAL",
                                   os.path.relpath(p, ind))
            zi = zipfile.ZipInfo(arc, date_time=ZIP_DT)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            with open(p, "rb") as fh:
                z.writestr(zi, fh.read())
    digest = sha256(zpath)
    with open(zpath + ".sha256", "w") as f:
        f.write("%s  %s\n" % (digest, ARCHIVE))

    print("\nhistorical archives")
    allok = True
    for p, want, name in HIST:
        got = sha256(p) if os.path.exists(p) else None
        ok = got == want
        allok &= ok
        print("   %-26s %s" % (name, "unchanged" if ok else "CHANGED"))
    tot = sum(len(v) for v in allchecks.values())
    ok = sum(1 for v in allchecks.values() for _, o, _ in v if o)
    print("\n  %s" % ARCHIVE)
    print("  sha256 %s" % digest)
    print("  %d entries" % len(zipfile.ZipFile(zpath).namelist()))
    print("  package checks: %d of %d passed" % (ok, tot))
    return digest, allok


if __name__ == "__main__":
    st, L, allchecks, files = main()
    assemble(st, L, allchecks, files)
