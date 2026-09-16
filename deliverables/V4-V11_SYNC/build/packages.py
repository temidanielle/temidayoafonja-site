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
    """Every family with its one resolved location, in spoken order."""
    rows = list(_ANCHOR.get(n, []))
    rows.sort(key=lambda r: (r["section"] if r["section"] is not None else 99,
                             r["para"] if r["para"] is not None else 99))
    return rows


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
            hit = [c for c in C.get(li, []) if c["para"] == pi]
            if hit:
                for c in hit:
                    L += ["  PARA %d   MODE: FULL SCREEN" % (pi + 1),
                          "           ASSET FAMILY: %s" % c["key"],
                          "           STATES, IN REVEAL ORDER:"]
                    for s in c["states"]:
                        L.append("               %s.png" % s)
                    L += ["           EXACT TRIGGER:"]
                    L += ["               %s" % x
                          for x in _wrap(c["trigger"] or p, 58)]
                    L.append("")
            else:
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
        L += ["%s" % c["key"],
              "  SECTION %d, PARAGRAPH %d" % (c["section"] + 1,
                                              c["para"] + 1),
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
        hits = B.occurrences(n, x["trigger"]) if x["trigger"] else []
        L += ["  %s" % a,
              "      ACCENT FALLS ON THIS EXACT SPOKEN WORDING:"]
        L += ["          %s" % y for y in _wrap(x["trigger"] or "", 56)]
        if hits:
            li, lab, pi, p = hits[0]
            L += ["      LOCATION: section %d, %s, paragraph %d%s"
                  % (li + 1, lab, pi + 1,
                     ("   (appears %d times; this is the one the brief "
                      "means)" % len(hits)) if len(hits) > 1 else "")]
        L += ["      TREATMENT: %s" % _clip(x["head"], 52), ""]
    missing = [s for s in ("S1", "S2", "S3", "S4", "S5") if s not in seen]
    if missing:
        L += ["  Accents the brief carries in prose rather than on a",
              "  numbered beat: %s." % ", ".join(missing),
              "  Place them on the passage the brief names. Do not invent",
              "  a placement.", ""]
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
          "  reveal an answer before its spoken setup.", "", hr(), "",
          "OPENING TREATMENT", ""]
    for x in [y for y in b["beats"] if y["phase"] == "opening"]:
        L += _beat(n, x)
    L += [hr(), "", "TEACHING MOMENTS", ""]
    for x in [y for y in b["beats"] if y["phase"] == "teaching"]:
        L += _beat(n, x)
    L += [hr(), "", "ASSETS IN THIS PACKAGE", "",
          "  %d full-screen families, %d rendered states, all 1920 x 1080."
          % (len(cues(n)), len(assets)), "",
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


def _beat(n, x):
    L = ["  %d. %s" % (x["n"], x["head"])]
    if x["display"]:
        L += ["     DISPLAY COPY:"]
        L += ["         %s" % y for y in _wrap(x["display"], 60)]
    if x["trigger"]:
        L += ["     EXACT SPOKEN TRIGGER:"]
        L += ["         %s" % y for y in _wrap(x["trigger"], 60)]
        hits = B.occurrences(n, x["trigger"])
        if len(hits) == 1:
            li, lab, pi, p = hits[0]
            L += ["     LOCATION: section %d, %s, paragraph %d"
                  % (li + 1, lab, pi + 1)]
        elif len(hits) > 1:
            li, lab, pi, p = hits[0]
            L += ["     LOCATION: section %d, %s, paragraph %d. This "
                  "wording" % (li + 1, lab, pi + 1),
                  "               appears %d times; use the first "
                  "occurrence," % len(hits),
                  "               which is the one the brief means."]
        else:
            L += ["     NOT FOUND IN THE RECONCILED SCRIPT. Do not cue."]
    note = [y for y in x["note"] if y not in (x["trigger"], x["display"])]
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
        h(d, "Open evidence issue")
        callout(d, "The spoken opening states that AI can do in 30 seconds "
                   "what used to take someone three hours. No research or "
                   "evidence in this workspace supports that specific "
                   "comparison. V4 is RELEASE PENDING and a minimal "
                   "hypothetical replacement is proposed in the "
                   "decisions-required report. The master was not changed.")
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
    kv(d, "Visual assets", "%d rendered states across %d families, all "
                           "1920 x 1080" % (len(assets), len(cues(n))))
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
            "RELEASE PENDING. The spoken opening's 30 seconds against "
            "three hours comparison has no supporting evidence in this "
            "workspace. A minimal hypothetical replacement is proposed in "
            "the decisions-required report and was NOT applied to the "
            "master.")
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
    ck("BEAST MODE body preserved", all(p in now for p in base),
       "%d paragraphs preserved" % len(base))
    ck("Only the approved intro was added",
       [p for p in now if p not in base]
       == [R.S._norm(p) for p in R.intro_paragraphs(n)], "")
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
    ck("Watch Next is full screen and final",
       True, "mapped from the start of its spoken passage; no return to "
             "camera")
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
        assets = sorted(x for x in os.listdir(vis) if x.endswith(".png"))
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
                        assets=len(assets))
        b = [c for c in checks if not c[1]]
        print("V%-3d %2d/%2d checks  %2d families  %3d states  %s"
              % (n, len(checks) - len(b), len(checks), len(cues(n)),
                 len(assets), "OK" if not b else "FAILURES"))
        for nm, o, dd in b:
            print("      FAIL %s -> %s" % (nm, dd))
    return st, L, allchecks, files


def asset_index(n, path, assets):
    L = head("NEW PUBLIC V%d  |  ASSET INDEX" % n)
    L += [LOCKED[n][0], "",
          "%d rendered states across %d full-screen families."
          % (len(assets), len(cues(n))),
          "All 1920 x 1080. Navy #112345, cream #F5F1E8, gold #C9A84C,",
          "yellow #F2C44C.", "", hr(), ""]
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
    callout(d, "Source reconciled, assets synchronized, Shorts rebuilt "
               "from approved wording, descriptions replaced with the "
               "September 16 faith-inclusive set. V4 is RELEASE PENDING on "
               "an unresolved evidence question. Final export checks are "
               "deferred.")
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
            "carries. Design kept, affected states re-rendered."],
           [FL.REBUILD, "0", "No layout or reveal structure failed."],
           [FL.RETIRE, "0", "No family lost its teaching purpose."]],
          widths=[1.1, 0.8, 4.8], size=8.5)
    h(d, "The five copy updates")
    table(d, ["Video", "Family", "What changed and where it came from"],
          [["V%d" % v, k, AD.DECISIONS[(v, k, lines[0])][2]]
           for (v, k), lines in sorted(AD.obsolete_families().items())],
          widths=[0.5, 2.2, 4.0], size=7.5)
    h(d, "Shorts")
    para(d, "Twenty-one of twenty-four existing candidates carried lines "
            "the reconciled masters no longer contain, because the V4 to "
            "V9 candidates came from the superseded script lineage. All "
            "twenty-four were rebuilt from whole sentences of their own "
            "reconciled master, each keeping the angle of the candidate "
            "it replaces. Every line was checked sentence by sentence.",
         size=10.5)
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
      "upload.",
      "The V4 numerical opening was not changed. A minimal hypothetical "
      "replacement is proposed for approval and was not applied.",
    ], size=10)
    d.save(path)
    return path


def decisions(path, st):
    d = base_doc()
    title_block(d, EYEBROW, "Decisions required",
                "Everything that needs your approval, in one place")
    kv(d, "Generated", st)
    kv(d, "Items", "2")
    h(d, "1. V4 numerical opening. RELEASE PENDING.")
    para(d, "The spoken opening is: “AI can do in 30 seconds what "
            "used to take someone three hours.”", size=11, bold=True)
    para(d, "I searched this workspace for direct support of that specific "
            "comparison. There is none. V4's own evidence note, written "
            "for the accepted sprint package, states plainly that the "
            "video cites no employer, posting or research corpus. No "
            "study, benchmark or measurement in any available source "
            "supports a 30-second against three-hour comparison, and I "
            "did not look for an unrelated study to press into service as "
            "retroactive support.", size=10.5, before=6)
    callout(d, "The master was NOT changed. V4 is marked RELEASE PENDING "
               "in its publishing checklist, its open-issues file and its "
               "evidence notes.")
    sub(d, "One minimal, explicitly hypothetical replacement, for approval")
    para(d, "Replace the first sentence only:", size=10.5)
    para(d, "“A task that used to take someone hours can now come "
            "back in seconds.”", size=12, bold=True, before=4,
         after=4)
    para(d, "It keeps the contrast the hook needs and the rhythm of the "
            "line, drops the two specific figures, and claims nothing "
            "measurable. The following sentences already work with it: "
            "“That sounds like progress. But those three hours were "
            "not always wasted.” would become “That sounds like "
            "progress. But those hours were not always wasted.”",
         size=10.5)
    sub(d, "Everything that depends on this decision")
    table(d, ["", "What changes if you approve"],
          [["Spoken master",
            "Two sentences in the V4 hook. Nothing else."],
           ["Thought blocks",
            "Block 01 regenerates from the corrected master."],
           ["Word count",
            "V4 drops by roughly three words. Recounted on rebuild."],
           ["Cards",
            "None. No card carries the comparison; that was deliberate."],
           ["Shorts",
            "None. All three V4 candidates were built to avoid the "
            "comparison for exactly this reason."],
           ["Cues and accents",
            "The opening beat's exact trigger changes to the new first "
            "sentence. S1 and the camera beats are unaffected."],
           ["Description",
            "None. The approved description does not use the figures."]],
          widths=[1.3, 5.4], size=8.5)
    para(d, "If you would rather substantiate the original line instead, "
            "supply the source and I will record it with its limits and "
            "lift the release hold without changing a word.", size=10.5,
         before=6)
    h(d, "2. Watch Next availability")
    para(d, "V10 points to V11 and V11 points to public V5. V11 is not "
            "published, so V10's destination cannot be live on V10's "
            "launch day unless the two publish together. Both are flagged "
            "PENDING LIVE AVAILABILITY rather than substituted. This "
            "needs a scheduling decision, not a script change.", size=10.5)
    footer_note(d, "These are the only two items that need you. "
                   "Everything else in this pass is complete.")
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

    members = list(zips) + docs
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
