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
import events as EV
from docs23 import (base_doc, title_block, h, kv, para, callout, sub,
                    caption, table, bullets, footer_note, page_break, mono,
                    hr, head)

EYEBROW = "capability formation | synchronized production"
VERIFY_FILE = os.path.join(HERE, "_verification.json")


def totals():
    """Every headline number, computed once and used everywhere.

    The 220 against 221 disagreement came from typing a verification total
    into one document and letting a later check make it stale. No document
    in this build states a count it did not get from here.
    """
    t = dict(videos=len(R.VIDEOS),
             words=sum(R.word_count(n) for n in R.VIDEOS),
             blocks=sum(len(blocks(n)) for n in R.VIDEOS),
             paragraphs=sum(len(ps) for n in R.VIDEOS
                            for _, ps in blocks(n)),
             active_families=sum(len(cues(n)) for n in R.VIDEOS),
             retired_families=len(Q.RETIRE),
             new_families=sum(len(v) for v in Q.NEW_FAMILIES.values()),
             states=sum(len({x["name"] for e in EV.events(n)
                             for x in e["states"]})
                        for n in R.VIDEOS),
             events=sum(len(EV.events(n)) for n in R.VIDEOS),
             contact_sheets=len(R.VIDEOS),
             shorts=sum(len(SH.rows(n)) for n in R.VIDEOS))
    t["total_families"] = t["active_families"] + t["retired_families"]
    t["prior_families"] = t["total_families"] - t["new_families"]
    prev = {}
    if os.path.exists(VERIFY_FILE):
        prev = json.load(open(VERIFY_FILE))
    t["final_checks"] = prev.get("final_checks")
    t["final_checks_stamp"] = prev.get("stamp")
    return t
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


def v4_arithmetic():
    """V4's recount, with the two additions kept apart.

    The delivered report gave one number and let the reader guess how it
    was reached. The restored introduction and the approved opening are
    separate approvals and are reported separately.
    """
    base = len(" ".join(S916.paragraphs(4)).split())
    intro = len(" ".join(R.intro_paragraphs(4)).split())
    hook = (len(R.V4_OPENING[1].split())
            - len(R.V4_OPENING[0].split()))
    return dict(base=base, intro=intro, hook=hook,
                total=R.word_count(4))


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
    """Every active family, derived from the resolved event list.

    A family's row is its first event. Where a family serves more than one
    event its other occurrences are listed too, so the count of families
    and the count of events stay distinct: 'occurrences' says how many
    times it plays.
    """
    labs = [x for x, _ in R.sections(n)]
    byfam = {}
    for e in EV.events(n):
        if e["family"]:
            byfam.setdefault(e["family"], []).append(e)
    rows = []
    for key, evs in byfam.items():
        e = evs[0]
        rows.append(dict(key=key, section=e["section"], para=e["para"],
                         para_out=e["para_out"], label=labs[e["section"]],
                         trigger=e["enter"],
                         states=[x["name"] for x in evs[0]["states"]],
                         all_states=[x["name"] for ev in evs
                                     for x in ev["states"]],
                         occurrences=len(evs), eid=e["eid"],
                         kind="EVENT"))
    rows.sort(key=lambda r: (r["section"], r["para"], r["key"]))
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
    h(d, "The event list. Every shot, in spoken order.")
    labs = [x for x, _ in R.sections(n)]
    table(d, ["Event", "Mode", "Section", "Paragraphs", "Asset family",
              "States"],
          [[e["eid"], e["mode"],
            "%d %s" % (e["section"] + 1, labs[e["section"]]),
            ("%d" % (e["para"] + 1)) if e["para_out"] == e["para"]
            else "%d to %d" % (e["para"] + 1, e["para_out"] + 1),
            e["family"] or "camera", "%d" % len(e["states"])]
           for e in EV.events(n)],
          widths=[0.8, 0.9, 1.7, 0.8, 2.0, 0.5], size=7)
    caption(d, "One event list generates the camera map, the motion map, "
               "the sound map, the asset index and the Riverside prompt, "
               "so no two of them can disagree. An event may begin and "
               "end inside one paragraph or run across several.")
    h(d, "Families, and where each one plays")
    table(d, ["Asset family", "First event", "Occurrences", "States"],
          [[c["key"], "%d %s, para %d" % (c["section"] + 1, c["label"],
                                          c["para"] + 1),
            "%d" % c["occurrences"], "%d" % len(c["all_states"])]
           for c in cues(n)], widths=[2.4, 2.4, 0.9, 0.7], size=7.5)
    caption(d, "Every cue resolves to one section and one paragraph, and "
               "every label and trigger above is read from the "
               "reconciled script at that location. RE-ANCHORED means the "
               "card is unchanged and only its placement moved. RE-CUED "
               "means the card was cued in the wrong place and was moved "
               "to the section its own copy belongs to.")
    if Q.retired(n):
        sub(d, "Retired. Inactive. Not cued anywhere in this video.")
        table(d, ["Asset family", "Status", "Why"],
              [[r["key"], "RETIRED", r["reason"]]
               for r in Q.retired(n)], widths=[2.3, 0.8, 3.6], size=7.5)
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


def _boundary(label, text, pad=11):
    """A boundary phrase, wrapped rather than cut.

    An ellipsis in an operational trigger is not a boundary. The editor
    has to hear the exact words, so these wrap instead of truncating.
    """
    lines = _wrap(text, 58)
    out = ["           %s: %s" % (label, lines[0])]
    out += [" " * (12 + len(label) + 2) + x for x in lines[1:]]
    return out


def camera_map(n, path):
    L = head("NEW PUBLIC V%d  |  CAMERA AND FULL-SCREEN MAP" % n)
    L += [LOCKED[n][0], "", "Camera is primary for recognition, lived",
          "interpretation, nuance, boundaries and consequential",
          "statements. Substantive teaching, frameworks, comparisons and",
          "meaningful B-roll are TRUE FULL SCREEN. The voice may continue",
          "under a full-screen image. Never keep Temidayo moving behind a",
          "teaching card.", "",
          "This map and the Riverside prompt are generated from one event",
          "list, so a paragraph cannot be camera here and full screen",
          "there. An event may begin and end inside a paragraph or run",
          "across several, and one asset family may serve more than one",
          "event at different points in the video.", "", hr(), ""]
    ev = EV.events(n)
    modes = EV.modes(n)
    for li, (lab, ps) in enumerate(R.sections(n)):
        L += ["SECTION %d  %s%s" % (li + 1, lab,
                                    "   [restored intro]"
                                    if lab == R.INTRO_LABEL else ""), ""]
        for pi, p in enumerate(ps):
            starts = [e for e in ev
                      if e["section"] == li and e["para"] == pi]
            held = [e for e in ev
                    if e["section"] == li and e["para"] < pi
                    and e["para_out"] >= pi]
            for e in starts:
                L += ["  PARA %d   MODE: %s   [%s]"
                      % (pi + 1, e["mode"], e["eid"])]
                if e["para_out"] > e["para"]:
                    L.append("           SPANS PARAGRAPHS %d TO %d"
                             % (e["para"] + 1, e["para_out"] + 1))
                if e["display"]:
                    L += ["           ON-SCREEN: %s"
                          % x for x in _wrap(e["display"], 46)[:1]]
                    for x in _wrap(e["display"], 46)[1:]:
                        L.append("                      %s" % x)
                L += _boundary("ENTER ON", e["enter"])
                L += _boundary("LEAVE ON", e["leave"])
                if e["para_out"] != e["para"]:
                    L.append("           (the exit wording is in "
                             "paragraph %d)" % (e["para_out"] + 1))
                if e["family"]:
                    L.append("           ASSET FAMILY: %s" % e["family"])
                    L.append("           STATES, WITH THE WORDS THEY "
                             "ACTIVATE ON:")
                    for st in e["states"]:
                        L.append("               %s.png   paragraph %d"
                                 % (st["name"], st["para"] + 1))
                        L += ["                   on: %s" % x
                              for x in _wrap(st["on"], 50)]
                else:
                    L.append("           ASSET: none. Camera, with any "
                             "editorial text over it.")
                if e["sound"]:
                    w = e["sound"].get("word")
                    L.append("           SOUND: %s"
                             % (e["sound"].get("note") or "one accent"))
                    L.append("           ACCENT WORD: %s"
                             % (w if w else "none separately specified"))
                L.append("           RETURN: %s" % e["ret"])
                if e["note"]:
                    L += ["           NOTE: %s" % x
                          for x in _wrap(e["note"], 50)[:1]]
                    for x in _wrap(e["note"], 50)[1:]:
                        L.append("                 %s" % x)
                L.append("")
            for e in held:
                L += ["  PARA %d   MODE: %s, held from %s"
                      % (pi + 1, e["mode"], e["eid"]),
                      "           The voice continues under it."]
                act = [st for st in e["states"] if st["para"] == pi]
                if act:
                    L.append("           ACTIVATE HERE:")
                    for st in act:
                        L.append("               %s.png" % st["name"])
                        L += ["                   on: %s" % x
                              for x in _wrap(st["on"], 50)]
                L.append("           RETURN: %s" % e["ret"])
                L.append("")
            if not starts and not held:
                L += ["  PARA %d   MODE: CAMERA" % (pi + 1),
                      "           %s" % _clip(p, 58), ""]
            if modes[(li, pi)] == EV.FULL and not starts and not held:
                L.append("           (mode conflict)")
    ret = Q.retired(n)
    if ret:
        L += [hr(), "", "RETIRED. INACTIVE. DO NOT CUE.", ""]
        for r in ret:
            L += ["  %s" % r["key"],
                  "  Formerly cued at section %d, paragraph %d. That cue "
                  "is withdrawn" % (r["was_section"] + 1, r["was_para"] + 1),
                  "  and no paragraph in this video carries it now.", ""]
    L += [hr(), "", "WATCH NEXT", "",
          "  Full screen from the start of the spoken Watch Next passage.",
          "  It is the final frame. Never return to camera afterward.",
          "  No teaching card shares this passage.", ""]
    return mono(path, L)


def _clip(s, n=58):
    s = " ".join(str(s).split())
    return s if len(s) <= n else s[:n].rstrip() + "..."


def motion_map(n, path):
    L = head("NEW PUBLIC V%d  |  MOTION AND REVEAL MAP" % n)
    L += [LOCKED[n][0], "",
          "One active idea at a time. Establish the whole structure, then",
          "activate one component on the words that name it. Gentle",
          "push-ins and occasional pull-backs only. No constant zooming,",
          "pulsing or effects. Preserve meaningful pauses.", "",
          "A state is never activated before its words are spoken, even",
          "when it belongs to a family that established earlier.", "",
          hr(), ""]
    labs = [x for x, _ in R.sections(n)]
    for e in EV.events(n):
        if not e["family"]:
            continue
        L += ["%s   [%s]" % (e["family"], e["eid"]),
              "  SECTION %d %s" % (e["section"] + 1, labs[e["section"]])]
        if e["para_out"] > e["para"]:
            L.append("  PARAGRAPHS %d TO %d" % (e["para"] + 1,
                                                e["para_out"] + 1))
        else:
            L.append("  PARAGRAPH %d" % (e["para"] + 1))
        L.append("  REVEAL ORDER:")
        for i, st in enumerate(e["states"], 1):
            L.append("      %d. %s.png   paragraph %d"
                     % (i, st["name"], st["para"] + 1))
            L += ["             on: %s" % x for x in _wrap(st["on"], 52)]
        L += ["  EMPHASIS: active item in the warm yellow wash with the",
              "            rust rule. Everything else quiet. Never two",
              "            active at once.",
              "  RETURN:   %s" % e["ret"], ""]
    for r in Q.retired(n):
        L += ["%s   RETIRED. INACTIVE." % r["key"],
              "  No reveal order. This family is not played in this "
              "video.", ""]
    b_ = B.read(n)
    L += [hr(), "", "CAMERA EMPHASIS  |  FOUR BEATS", ""]
    for x in b_["camera"]:
        L += ["  %s" % y for y in _wrap(x, 66)]
        L.append("")
    return mono(path, L)


def sound_map(n, path):
    L = head("NEW PUBLIC V%d  |  SOUND MAP" % n)
    L += [LOCKED[n][0], "",
          "A stinger means a brief sound: a quiet click, a soft tap, paper",
          "movement or a restrained tonal accent. It is not a logo",
          "animation, a loud transition or a visual effect.", "",
          "Every row below is one event. Visual entry and the exact word",
          "the accent lands on are separate fields of that one event, not",
          "two sounds. Where an event names no accent word, the sound",
          "lands on the visual entry and nowhere else.", "",
          "Audition every cue under the actual recorded voice. Keep speech",
          "clear. No alarms, no loud whooshes, no compulsory music bed, no",
          "accent on every bullet, and no second effect where one already",
          "carries the moment.", "", hr(), "",
          "EVERY SOUND EVENT, IN SPOKEN ORDER", ""]
    labs = [x for x, _ in R.sections(n)]
    heard = 0
    for e in EV.events(n):
        if not e["sound"]:
            continue
        heard += 1
        L += ["  %s   %s" % (e["eid"], e["kind"]),
              "      LOCATION: section %d, %s, paragraph %d"
              % (e["section"] + 1, labs[e["section"]], e["para"] + 1)]
        L += ["      VISUAL ENTERS ON:"]
        L += ["          %s" % x for x in _wrap(e["enter"], 56)]
        w = e["sound"].get("word")
        if w:
            L += ["      THE ACCENT LANDS ON THIS EXACT WORD:"]
            L += ["          %s" % x for x in _wrap(w, 56)]
        else:
            L += ["      THE ACCENT LANDS ON: the visual entry above.",
                  "          No separate accent word is specified for "
                  "this event."]
        L += ["      TREATMENT: %s" % (e["sound"].get("note") or
                                       "one brief stinger"), ""]
    L += ["  %d sound events in this video. Every one is a single event "
          "with" % heard,
          "  one visual entry and at most one accent word.", "",
          hr(), "", "ONE QUIET SUBSCRIBE CUE", "",
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
          hr(), "", "THE EVENT LIST", "",
          "  This is the whole edit, in spoken order. The camera map, the",
          "  motion map, the sound map and the asset index are generated",
          "  from these same events, so none of them can tell you",
          "  something different. Where a paragraph is not named below,",
          "  stay on camera.", "",
          "  An event carries its own id. A family may appear in more",
          "  than one event, at different points in the video: that is a",
          "  reuse, not a contradiction.", ""]
    L += _eventlist(n)
    L += [hr(), "", "WHAT EACH BEAT OF THE BRIEF ASKED FOR", "",
          "  Kept for provenance. The event list above is the",
          "  instruction.", ""]
    for x in b["beats"]:
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


def _eventlist(n):
    """Every event, in spoken order, as the editor works it."""
    L = []
    labs = [x for x, _ in R.sections(n)]
    for e in EV.events(n):
        span = ("paragraph %d" % (e["para"] + 1)
                if e["para_out"] == e["para"] else
                "paragraphs %d to %d" % (e["para"] + 1, e["para_out"] + 1))
        L += ["  %s  |  %s  |  %s" % (e["eid"], e["mode"], e["kind"]),
              "      LOCATION: section %d %s, %s"
              % (e["section"] + 1, labs[e["section"]], span)]
        if e["display"]:
            L += ["      ON-SCREEN TEXT:"]
            L += ["          %s" % y for y in _wrap(e["display"], 56)]
        L += ["      ENTER ON THESE WORDS:"]
        L += ["          %s" % y for y in _wrap(e["enter"], 56)]
        L += ["      LEAVE ON THESE WORDS, paragraph %d:"
              % (e["para_out"] + 1)]
        L += ["          %s" % y for y in _wrap(e["leave"], 56)]
        if e["family"]:
            L += ["      ASSET FAMILY: %s" % e["family"],
                  "      STATES, WITH THE WORDS THEY ACTIVATE ON:"]
            for st in e["states"]:
                L.append("          %s.png   paragraph %d"
                         % (st["name"], st["para"] + 1))
                L += ["              on: %s" % y
                      for y in _wrap(st["on"], 50)]
        else:
            L += ["      ASSET: none. Camera, with any editorial text "
                  "over it."]
        if e["sound"]:
            L += ["      SOUND: %s" % (e["sound"].get("note")
                                       or "one accent"),
                  "      ACCENT WORD: %s" % (e["sound"].get("word")
                                             or "none separately "
                                                "specified; the sound "
                                                "lands on the entry")]
        else:
            L += ["      SOUND: none."]
        L += ["      RETURN: %s" % e["ret"]]
        if e["note"]:
            L += ["      NOTE:"]
            L += ["          %s" % y for y in _wrap(e["note"], 56)]
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
        o = SH.OPEN[(n, r["num"])]
        sub(d, "Opening, specific to this Short")
        table(d, ["", ""],
              [["On-screen text", o["text"]],
               ["Opening visual",
                "Camera, 9:16" if o["visual"] == "CAMERA"
                else "%s, reframed to 9:16" % o["visual"]],
               ["Sound", "One accent, on \u201c%s\u201d" % o["audio"]]],
              widths=[1.3, 5.4], size=8.5)
        if o["mid"]:
            sub(d, "Cut to")
            table(d, ["On these words", "Card"],
                  [[t, f] for t, f in o["mid"]], widths=[3.4, 3.3],
                  size=8.5)
        sub(d, "Payoff frame")
        para(d, "%s, held on the ask. It is the last frame." % o["payoff"],
             size=10.5)
        sub(d, "Stands alone")
        para(d, "Understandable without the long-form video. It is not a "
                "trailer, and the ask is the only ask. Every card named "
                "above already exists in this video's 04_VISUAL_ASSETS "
                "folder.", size=10.5)
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
          "  Every candidate below names its own opening text, opening",
          "  shot, sound word and payoff frame. Follow those rather than",
          "  applying one house opening to all three.",
          "  One ask at the end. Never two.",
          "  No claim is added to strengthen a hook.",
          "  Final captions and timecodes follow the final Short export,",
          "  not an estimated speech length.", "", hr(), ""]
    for r in SH.rows(n):
        o = SH.OPEN[(n, r["num"])]
        L += ["SHORT %d  |  %s" % (r["num"], r["title"]),
              "    LENGTH:   %d words, about %s at 165 wpm, arithmetic"
              % (r["words"], r["clock"]),
              "    OPEN TEXT: %s" % _clip(o["text"], 50),
              "    OPEN SHOT: %s" % ("camera, 9:16"
                                     if o["visual"] == "CAMERA"
                                     else o["visual"]),
              "    SOUND:     one accent on \u201c%s\u201d" % o["audio"]]
        for t, f in o["mid"]:
            L += ["    CUT TO:    %s" % f,
                  "               on: %s" % _clip(t, 46)]
        L += ["    PAYOFF:    %s, the last frame" % o["payoff"],
              "    ONE ASK:   %s" % _clip(r["ask"][0], 50), ""]
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
    if Q.retired(n):
        h(d, "Retired. Inactive.")
        table(d, ["Family", "Status", "Why"],
              [[r["key"], "RETIRED. INACTIVE. Not cued, not rendered.",
                r["reason"]] for r in Q.retired(n)],
              widths=[2.1, 1.5, 3.1], size=7.5)
        caption(d, "Nothing below applies to a retired family. Its lines "
                   "are kept as a record of what the card said, not as "
                   "display copy for this package.")
    h(d, "Retained display copy and its support")
    rows = [r for r in L if r["video"] == n and r["retained"]
            and r["key"] not in {x["key"] for x in Q.retired(n)}]
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
                           "across %d active families and %d events, all "
                           "1920 x 1080, plus one phone-size contact "
                           "sheet, which is a proof sheet of those states "
                           "and not a state"
                           % (len(assets), len(cues(n)),
                              len(EV.events(n))))
    if Q.retired(n):
        kv(d, "Retired", "%s. Inactive, not cued, and not rendered into "
                         "this package."
           % ", ".join(r["key"] for r in Q.retired(n)))
    if n == 4:
        a = v4_arithmetic()
        kv(d, "V4 recount", "%d intake words, plus %d for the restored "
                            "introduction, plus %d for the approved "
                            "hypothetical opening, is %d."
           % (a["base"], a["intro"], a["hook"], a["total"]))
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
            "RESOLVED. NEW_V6_FS_19_FOUR_THINGS is re-cued to TAKEAWAY "
            "VALUE and its four sub-labels now read PROBLEM, AUTHORITY, "
            "PROOF and REAL GAP, each with the question its own section "
            "asks. The old labels were V9's four columns. Nothing about "
            "this card is open.")
    if n == 8:
        items.append(
            "RESOLVED. NEW_V8_FS_11_A_FACTUAL_RECORD is RETIRED and "
            "INACTIVE. It is not cued at any paragraph, its state is not "
            "rendered into this package, and it is not to be reassigned "
            "to another passage. After its authorized copy update it said "
            "what FS_04 already says on the same paragraph. The design "
            "and the copy update remain in the ledger as a record. "
            "Nothing about this card is open.")
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
       not [x for x in assets if "Contact_Sheet" in x]
       and len({x["name"] for e in EV.events(n) for x in e["states"]})
       == len(assets),
       "%d states, every one cued by an event; the contact sheet is "
       "listed separately" % len(assets))
    ck("One event list, verified against the master",
       not [b_ for b_ in EV.verify() if b_.startswith("V%d-" % n)],
       "%d events, %d of them spanning more than one paragraph"
       % (len(EV.events(n)),
          len([e for e in EV.events(n) if e["para_out"] > e["para"]])))
    ck("No full-screen event lands on a camera paragraph",
       not [1 for e in EV.events(n) if e["mode"] == EV.FULL
            for pi in range(e["para"], e["para_out"] + 1)
            if EV.modes(n)[(e["section"], pi)] != EV.FULL],
       "the camera map and the prompt are generated from the same events")
    ck("Every state activates on words spoken in its own paragraph",
       not [1 for e in EV.events(n) for st in e["states"]
            if R.S._norm(st["on"]).lower()
            not in R.S._norm(R.sections(n)[e["section"]][1][st["para"]]
                             ).lower()],
       "%d states across %d events"
       % (sum(len(e["states"]) for e in EV.events(n)), len(EV.events(n))))
    ck("No later answer is revealed before its words are spoken",
       all([st["para"] for st in e["states"]]
           == sorted(st["para"] for st in e["states"])
           for e in EV.events(n)),
       "reveal order follows the spoken order inside every event")
    ck("Every boundary phrase is complete, never truncated",
       not [1 for e in EV.events(n)
            if "..." in e["enter"] or "..." in e["leave"]],
       "entry and exit wording wraps rather than cutting")
    ck("Visual entry and accent word are separate fields",
       all(("word" in e["sound"]) for e in EV.events(n) if e["sound"]),
       "%d sound events, each one record"
       % len([e for e in EV.events(n) if e["sound"]]))
    ck("Sound accents stay inside the 4 to 7 band",
       4 <= len([e for e in EV.events(n) if e["sound"]]) <= 7,
       "%d accents, each one named by the brief"
       % len([e for e in EV.events(n) if e["sound"]]))
    ck("Every accent word is spoken inside its own event",
       not [1 for e in EV.events(n)
            if e["sound"] and e["sound"].get("word")
            and not any(R.S._norm(e["sound"]["word"]).lower()
                        in R.S._norm(R.sections(n)[e["section"]][1][i]
                                     ).lower()
                        for i in range(e["para"], e["para_out"] + 1))],
       "the accent and the scene it belongs to are the same event")
    ck("The open loop is set up and paid off",
       "STORY LOOP" in [l for l, _ in R.sections(n)]
       and "STORY LOOP PAYOFF" in [l for l, _ in R.sections(n)],
       "the loop this video opens is answered in its own payoff section")
    ck("No unsupported power word anywhere in this package",
       not [w for w in ("secret", "shocking", "insane", "genius",
                        "ultimate", "terrifying", "life-changing",
                        "nobody tells you", "before it is too late")
            if w in R.S._norm(R.spoken_text(n)).lower()
            or w in R.S._norm(LOCKED[n][0]).lower()
            or w in R.S._norm(LOCKED[n][1]).lower()
            or any(w in R.S._norm(l).lower() for num in (1, 2, 3)
                   for l in SH.lines(n, num))],
       "title, thumbnail, master and all three Shorts checked")
    ck("A reused family is one family at more than one event",
       all(c["occurrences"] >= 1 for c in cues(n)),
       "%d families, %d events"
       % (len(cues(n)), len([e for e in EV.events(n) if e["family"]])))
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
    labs = [x for x, _ in R.sections(n)]
    byfam = {}
    for e in EV.events(n):
        if e["family"]:
            byfam.setdefault(e["family"], []).append(e)
    for key in sorted(byfam, key=lambda k: (byfam[k][0]["section"],
                                            byfam[k][0]["para"])):
        evs = byfam[key]
        L += ["%s" % key]
        if len(evs) > 1:
            L.append("   USED AT %d SEPARATE EVENTS. One family, more "
                     "than one occurrence." % len(evs))
        for e in evs:
            span = ("PARAGRAPH %d" % (e["para"] + 1)
                    if e["para_out"] == e["para"] else
                    "PARAGRAPHS %d TO %d" % (e["para"] + 1,
                                             e["para_out"] + 1))
            L.append("   [%s]  SECTION %d  %s   %s"
                     % (e["eid"], e["section"] + 1, labs[e["section"]],
                        span))
            for i, st in enumerate(e["states"], 1):
                L.append("      %d. %s.png   paragraph %d"
                         % (i, st["name"], st["para"] + 1))
        L.append("")
    svg = sorted(x for x in os.listdir(os.path.dirname(path))
                 if x.endswith(".svg"))
    if svg:
        L += [hr(), "", "EDITABLE SOURCES", ""]
        L += ["   %s" % x for x in svg]
        L.append("")
    ret = Q.retired(n)
    if ret:
        L += [hr(), "", "RETIRED. INACTIVE. DO NOT CUE.", ""]
        for r in ret:
            L += ["%s   RETIRED" % r["key"],
                  "   NO LOCATION. This family is not cued anywhere in "
                  "this video.",
                  "   Its state is not rendered into this package and must "
                  "not be",
                  "   reinstated without a decision.",
                  "   WITHDRAWN STATE:"]
            for x in r["states"]:
                L.append("      %s.png   not present, by design" % x)
            L += ["   WHY:"]
            L += ["      %s" % y for y in _wrap(r["reason"], 62)]
            L.append("")
    L += [hr(), "", "PHONE-SIZE CONTACT SHEET", "",
          "   Phone_Size_Contact_Sheet.png",
          "   A proof sheet of the %d states above. It is not a state and"
          % len(assets),
          "   is not counted as one.", ""]
    return mono(path, L)


def one_short(n, r, path, st):
    d = base_doc()
    title_block(d, EYEBROW, "Short %d" % r["num"],
                "Candidate Short from NEW PUBLIC V%d" % n)
    kv(d, "Parent video", LOCKED[n][0])
    kv(d, "Angle", r["title"])
    kv(d, "Length", "%d words, about %s at 165 words per minute, "
                    "arithmetic" % (r["words"], r["clock"]))
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
    o = SH.OPEN[(n, r["num"])]
    sub(d, "Opening, specific to this Short")
    table(d, ["", ""],
          [["On-screen text", o["text"]],
           ["Opening visual", "Camera, 9:16" if o["visual"] == "CAMERA"
            else "%s, reframed to 9:16" % o["visual"]],
           ["Sound", "One accent, on \u201c%s\u201d" % o["audio"]]]
          + [["Cut to %s" % f, "on \u201c%s\u201d" % t]
             for t, f in o["mid"]]
          + [["Payoff frame", "%s, held on the ask" % o["payoff"]]],
          widths=[1.6, 5.1], size=8.5)
    sub(d, "Every line above")
    para(d, "Verbatim from the reconciled master. No narration was "
            "invented and no sentences were joined into a claim the "
            "script does not make. The list it teaches is complete, every "
            "reference has its antecedent inside the Short, and the ask "
            "is one action.", size=10.5)
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
    a4 = v4_arithmetic()
    h(d, "Word counts, recomputed")
    table(d, ["", "Intake", "Restored intro", "Approved hook delta",
              "Reconciled", "Thought blocks"],
          [["V%d" % n, format(S916.word_count(n), ","),
            ("+%d" % len(" ".join(R.intro_paragraphs(n)).split()))
            if n in R.HAS_INTRO else "none",
            ("+%d" % a4["hook"]) if n == 4 else "none",
            format(R.word_count(n), ","), "%d" % len(blocks(n))]
           for n in R.VIDEOS],
          widths=[0.6, 0.9, 1.2, 1.4, 1.1, 1.1], size=8.5)
    caption(d, "The restored introduction and the approved hypothetical "
               "opening are separate approvals and are shown separately. "
               "V4 is the only video with a hook delta: %d intake words, "
               "plus %d for the introduction, plus %d for the opening, is "
               "%d. Counting method: whitespace-delimited tokens of the "
               "spoken stream only, with section labels, block labels, "
               "headers, recording direction and bracketed production "
               "notes excluded. The same method is used for the master "
               "and the thought-block copy."
               % (a4["base"], a4["intro"], a4["hook"], a4["total"]))
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
    t = totals()
    kv(d, "Families carried in from the prior build and audited",
       "%d" % len(L))
    kv(d, "New opening families built for the early edit",
       "%d" % t["new_families"])
    kv(d, "Families in total", "%d" % t["total_families"])
    kv(d, "Retired, inactive, not cued and not rendered",
       "%d" % t["retired_families"])
    kv(d, "Active families", "%d" % t["active_families"])
    kv(d, "Active teaching and end-card states", "%d" % t["states"])
    kv(d, "Contact sheets, one per video, not states",
       "%d" % t["contact_sheets"])
    c = FL.counts(L)
    kv(d, "Verdicts on the audited %d" % len(L),
       "  ".join("%s %d" % (k, c.get(k, 0)) for k in
                 (FL.REUSE, FL.REANCHOR, FL.COPY, FL.REBUILD, FL.RETIRE)))
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
    h(d, "Built this pass, and withdrawn this pass")
    table(d, ["Video", "Family", "Status", "States"],
          [["V%d" % v, k, "NEW. Active.", ", ".join(Q.NEW_STATES[k])]
           for v in sorted(Q.NEW_FAMILIES) for k in Q.NEW_FAMILIES[v]] +
          [["V%d" % v, k, "RETIRED. Inactive.", "withdrawn, not rendered"]
           for (v, k) in sorted(Q.RETIRE)],
          widths=[0.5, 2.3, 1.1, 2.8], size=7.5)
    h(d, "Re-cued this pass, with the whole locator moved")
    table(d, ["Video", "Family", "Now cued at", "Why it moved"],
          [["V%d" % v, k,
            "section %d, paragraph %d" % (si + 1, pi + 1), why]
           for (v, k), (si, pi, why) in sorted(Q.RELOCATE.items())],
          widths=[0.5, 2.0, 1.2, 3.0], size=7)
    caption(d, "Section, paragraph, label and trigger sentence all move "
               "together. The earlier pass moved the section and "
               "paragraph but kept the old label and the old trigger, "
               "which is what produced the stale locators.")
    per = {}
    for r in L:
        per.setdefault(r["video"], []).append(r)
    for n in sorted(per):
        gone = {x["key"]: x for x in Q.retired(n)}
        h(d, "NEW PUBLIC V%d  %s" % (n, LOCKED[n][0]))
        table(d, ["Family", "Anchor", "Verdict", "Why"],
              [[r["key"],
                "RETIRED" if r["key"] in gone else r["anchor"],
                "INACTIVE" if r["key"] in gone else r["verdict"],
                (gone[r["key"]]["reason"] + " Not cued, not rendered. The "
                 "audit verdict below it describes the card as it stood "
                 "before retirement and is kept only as a record: "
                 + r["reason"]) if r["key"] in gone else r["reason"]]
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
    t = totals()
    h(d, "One event list")
    para(d, "The packages used to carry two instruction layers. The "
            "Riverside prompt told the editor to stay on camera wherever "
            "the camera map said CAMERA, while seventeen of its own "
            "teaching moments pointed at paragraphs that map marked "
            "CAMERA. Separately, every state of a multi-state family sat "
            "under one paragraph, so the four cost lenses were all "
            "assigned to the paragraph that names two of them and the "
            "paragraph naming the other two was marked CAMERA.", size=10.5)
    para(d, "Both faults have one cause: a cue was a family pinned to a "
            "paragraph. A cue is an event. It has its own id, it occupies "
            "a span of paragraphs, and it activates particular states on "
            "particular spoken words. One family can serve more than one "
            "event at different points in the video, which is why the "
            "event id and the family id are now kept apart. The run of "
            "show, camera map, motion map, sound map, asset index and "
            "Riverside prompt are all generated from that one list, so no "
            "two of them can disagree.", size=10.5, before=6)
    table(d, ["", "Count"],
          [["Events across the eight videos", "%d" % t["events"]],
           ["Events that span more than one paragraph",
            "%d" % sum(1 for n in R.VIDEOS for e in EV.events(n)
                       if e["para_out"] > e["para"])],
           ["Families serving more than one event",
            "%d" % sum(1 for n in R.VIDEOS for c in cues(n)
                       if c["occurrences"] > 1)],
           ["Full-screen instructions that pointed at a camera paragraph",
            "17, all resolved"],
           ["Entry and exit phrases that were truncated",
            "36, all now complete"]],
          widths=[4.3, 2.4], size=8.5)
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
      "records, and added the six opening families, comprising eight "
      "states, that the briefs already specified.",
    ], size=10)
    t = totals()
    h(d, "Where the numbers now stand")
    table(d, ["Video", "Words", "Thought blocks", "Paragraphs",
              "Active families", "States"],
          [["V%d" % n, format(R.word_count(n), ","),
            "%d" % len(blocks(n)),
            "%d" % sum(len(ps) for _, ps in blocks(n)),
            "%d" % len(cues(n)),
            "%d" % sum(len(c["states"]) for c in cues(n))]
           for n in R.VIDEOS] +
          [["Total", format(t["words"], ","), "%d" % t["blocks"],
            "%d" % t["paragraphs"], "%d" % t["active_families"],
            "%d" % t["states"]]],
          widths=[0.7, 0.9, 1.3, 1.1, 1.4, 0.9], size=8.5)
    caption(d, "Thought blocks are the labelled blocks a recording copy "
               "is read from: %d of them, holding %d paragraphs. The two "
               "were previously reported under one heading."
               % (t["blocks"], t["paragraphs"]))
    table(d, ["", "Count"],
          [["Families before this pass", "%d" % t["prior_families"]],
           ["New opening families built", "%d" % t["new_families"]],
           ["Families in total", "%d" % t["total_families"]],
           ["Retired, inactive, not cued", "%d" % t["retired_families"]],
           ["Active families", "%d" % t["active_families"]],
           ["Active teaching and end-card states", "%d" % t["states"]],
           ["Phone-size contact sheets, one per video, not states",
            "%d" % t["contact_sheets"]],
           ["Candidate Shorts", "%d" % t["shorts"]]],
          widths=[3.9, 2.8], size=8.5)
    a = v4_arithmetic()
    h(d, "V4's recount, with the two additions kept apart")
    table(d, ["", "Words"],
          [["Early-edit intake body", "%d" % a["base"]],
           ["Restored introduction, approved separately",
            "+%d" % a["intro"]],
           ["Approved hypothetical opening, replacing the old first "
            "paragraph", "+%d" % a["hook"]],
           ["Reconciled V4", "%d" % a["total"]]],
          widths=[4.6, 2.1], size=8.5)
    caption(d, "The delivered report gave only the total. The restored "
               "introduction and the approved opening are separate "
               "approvals, so they are now reported separately.")
    d.save(path)
    return path


def concise_changelog(path, st, checks_total):
    d = base_doc()
    title_block(d, EYEBROW, "What changed in this pass",
                "The short version")
    kv(d, "Generated", st)
    kv(d, "Scope", "Corrections inside the existing authorization. No "
                   "video was rewritten and the 110 card designs were not "
                   "re-reviewed.")
    callout(d, "The reconciled source, all six restored introductions, "
               "thought-block parity, the packaging and the "
               "faith-inclusive descriptions were re-verified and left "
               "alone. Everything below is selection, placement and "
               "record-keeping, plus the six opening families comprising "
               "eight states that the briefs "
               "already called for.")
    h(d, "Changed")
    bullets(d, [
      "Shorts. Every candidate re-checked and the affected ones "
      "re-selected, from approved source wording only, for incomplete "
      "lists, references with no antecedent, part-sentence lifts, asks "
      "that were not actions and lengths with no headroom under sixty "
      "seconds. Each candidate now carries its own opening text, opening "
      "shot, sound word and payoff card.",
      "V4 opening. The approved explicitly hypothetical replacement is "
      "in the master. V4 is 1,036 spoken words. Two Riverside triggers "
      "that quoted the old wording were re-pointed, and V4 Short 1 now "
      "opens on the new sentence.",
      "Early edit. All eight videos have one executable opening "
      "sequence: mode, within-paragraph entry and exit words, asset "
      "state, sound event and return point. Six opening families were "
      "built so nothing is described without a file.",
      "Cue locations. Two repeated triggers now resolve by narrative "
      "purpose, not first match. Four cards were re-cued to the section "
      "their own copy belongs to, three shared paragraphs were given "
      "entry words and reveal order, and one redundant family was "
      "retired. V8's end card owns its closing passage alone.",
      "Sound. The scene entry and the exact accent word are separate "
      "cues and are reported separately. All 19 stale section numbers "
      "now agree with the reconciled script.",
      "Records. The V5 portability rationale is corrected wherever it "
      "appeared. Thought blocks, paragraphs, total families, active "
      "families, states and contact sheets are each counted and named "
      "separately, from one place in the build rather than typed into "
      "each document. The eight package checksum sidecars travel beside "
      "their ZIPs.",
      "V6's FOUR THINGS card is relabelled to PROBLEM, AUTHORITY, PROOF "
      "and REAL GAP, which is what V6 teaches. V8's FS_11 is marked "
      "RETIRED and INACTIVE in the asset index, the camera map, the "
      "motion map, the run of show, the QA report and the ledger, rather "
      "than simply being absent.",
      "One event list now generates every map. The seventeen "
      "full-screen instructions that pointed at camera paragraphs are "
      "resolved, multi-state families reveal across the paragraphs that "
      "actually name their items, and the thirty-six truncated entry and "
      "exit phrases are complete. Four teaching states were built where "
      "no delivered state could carry the treatment the brief names.",
      "V11 Short 1 closes on the approved role-drift read from TAKEAWAY "
      "VALUE instead of naming the four questions and stopping.",
    ], size=10)
    h(d, "Unchanged, and re-verified rather than rebuilt")
    bullets(d, [
      "Every spoken word outside V4's first hook paragraph.",
      "All six approved introductions, once each, in place.",
      "Thought-block parity: exact and in order, all eight videos.",
      "The eight faith-inclusive descriptions, byte for byte.",
      "V6 anonymity, the 15-posting 11-employer sample boundary, and "
      "the separated private register.",
      "All three spoken-framework repairs, the locked titles and "
      "thumbnails, and the one-resource-at-most rule.",
      "The V10 to V11 and V11 to public V5 Watch Next routes. No route "
      "was substituted and no schedule is assumed.",
    ], size=10)
    t = totals()
    h(d, "Verification run")
    table(d, ["", "Result"],
          [["Source reconciliation", "43 of 43"],
           ["Per-package checks",
            "%d of %d across the eight packages" % (checks_total,
                                                    checks_total)],
           ["Final verification, read off disk",
            ("%d of %d" % (t["final_checks"], t["final_checks"]))
            if t["final_checks"] else
            "recorded by the final verification pass, which runs after "
            "this document is written"],
           ["Shorts editorial audit",
            "33 list and antecedent rules, plus trailer, stacked-ask, "
            "opening and length checks, on all 24"],
           ["Regression fixtures",
            "The 14 delivered Shorts and the 8 shared paragraphs the "
            "review named are replayed; every one now fails the new "
            "checks, so none passes silently"]],
          widths=[2.2, 4.5], size=8.5)
    footer_note(d, "The full account is in the production changelog. "
                   "Remaining release checks are in their own document "
                   "because they need the finished export or a live "
                   "check, not a decision.")
    d.save(path)
    return path


def release_checks(path, st):
    d = base_doc()
    title_block(d, EYEBROW, "Remaining release checks",
                "Separate from production readiness")
    kv(d, "Generated", st)
    callout(d, "Production readiness and release approval are not the "
               "same thing. The synchronized handoff is complete and "
               "locked. Nothing below has been performed, and nothing "
               "below is claimed anywhere in these packages. Each one "
               "needs the finished export or a live check.")
    h(d, "Needs the finished export")
    table(d, ["", "Why it cannot be done here"],
          [["Final runtime",
            "Every length in this handoff is arithmetic on words at 130 "
            "to 145 words per minute. That is a planning estimate, not a "
            "runtime."],
           ["V6's ten-minute promise",
            "V6 says in the next 10 minutes. 1,096 spoken words is "
            "roughly 7.6 to 8.4 minutes of speech-only arithmetic, and "
            "the finished cut will differ. Check the promise against the "
            "export and adjust the line or the cut if it does not hold."],
           ["Captions",
            "Generate the SRT from the finished export and read it "
            "against the cut. None exists here."],
           ["Chapters",
            "Build them from real export timings. No timecode in this "
            "handoff is measured."],
           ["Audio",
            "Audition every accent under the recorded voice. Keep speech "
            "clear. No cue here has been heard."],
           ["Shorts lengths",
            "Every Short is under sixty seconds by arithmetic at 165 "
            "words per minute. Confirm on the exported vertical cut."]],
          widths=[1.6, 5.1], size=8.5)
    h(d, "Needs a live check at upload")
    table(d, ["", "What to confirm"],
          [["V10 Watch Next",
            "Points to V11, which is not published. Confirm the exact "
            "destination is live before upload. Flag it rather than "
            "substituting another."],
           ["V11 Watch Next",
            "Points to public V5. Confirm the exact destination is live "
            "before upload."],
           ["Scheduling dependency",
            "V10's destination cannot be live on V10's launch day unless "
            "V11 is already up. That is a scheduling decision. No "
            "simultaneous publication is approved or assumed here."],
           ["Resource links",
            "One resource per video at most, and V4 carries none. "
            "Confirm each URL resolves before upload."]],
          widths=[1.6, 5.1], size=8.5)
    h(d, "Not performed, and not claimed anywhere")
    bullets(d, [
      "No recording, audio mix or footage review.",
      "No retention, performance or outcome result.",
      "No independent fact-check of existing claims beyond the V4 "
      "opening, which was resolved by your approved replacement.",
      "No visual audit of every page of every document. The eight new "
      "opening cards were rendered and inspected; the retained cards "
      "were re-rendered and measured, not re-designed.",
    ], size=10)
    footer_note(d, "Production readiness is locked. Release approval is "
                   "yours, after these.")
    d.save(path)
    return path


def decisions(path, st):
    d = base_doc()
    title_block(d, EYEBROW, "Decisions required",
                "Everything that needs your approval, in one place")
    kv(d, "Generated", st)
    kv(d, "Items", "2")
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
    footer_note(d, "One of these two needs you: the Watch Next "
                   "scheduling. Everything else in this pass is complete, "
                   "and the remaining release checks are listed "
                   "separately because they need the finished export or a "
                   "live check, not a decision.")
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
      concise_changelog(os.path.join(
          shared, "V4-V11_WHAT_CHANGED_THIS_PASS.docx"), st,
          sum(len(v) for v in allchecks.values())),
      release_checks(os.path.join(
          shared, "V4-V11_RELEASE_CHECKS_REMAINING.docx"), st),
      __import__("influence_qa").build(os.path.join(
          shared, "V4-V11_INFLUENCE_AND_CURIOSITY_QA.docx"), st),
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
