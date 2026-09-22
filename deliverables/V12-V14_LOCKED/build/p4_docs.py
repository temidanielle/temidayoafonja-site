# -*- coding: utf-8 -*-
"""Documents for the V12-V14 Phase 2 production pack.

Every number in these documents is read from the build modules, never typed.
House helpers are imported from the earlier batches and are not edited.
"""
import os, sys, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.append("/home/user/temidayoafonja-site/deliverables/VIDEOS_22-23/build")
# Every module in this pack is prefixed p4_ because the house document helpers
# insert their own build directories at the front of sys.path, which shadows bare
# names like build, shorts and packaging.

import importlib
from docs23 import (base_doc, title_block, h, kv, para, callout, sub, caption,
                    table, bullets, footer_note, page_break, spoken, marker,
                    cue, section_label, notspoken, numbered, field, rule)

import p4_blocks as B
import p4_shorts as S
import p4_production as PR
import p4_descriptions as D
import p4_provenance as PV
import p4_packaging as PK
import p4_checks_script as CH

EYEBROW = "capability formation | final locked"
STAMP = "Tuesday, September 22, 2026"

META = {
12: dict(number="V12", title="How to Turn One Accomplishment Into Proof in 10 Minutes",
         thumb="CAN YOU PROVE IT?", status=None,
         audit="What can you prove?",
         artifact="One accomplishment as it is currently written. Synthetic, labelled on screen, "
                  "seen before it is improved."),
13: dict(number="V13", title="Which Parts of Your Experience Actually Transfer to Another Industry?",
         thumb="SAME WORDS. DIFFERENT WORK.", status=None,
         audit="What travels? What does not?",
         artifact="Three real postings that all use the words “manage risk.”"),
14: dict(number="V14", title="I Read Two Similar Jobs. They Wanted Different Proof",
         thumb="SAME WORK. DIFFERENT REQUIREMENTS.",
         status=None,
         audit="What does not travel? What can you prove?",
         artifact="Two real postings, side by side."),
}

def words(n):
    return sum(len(p.split()) for _, p in CH.spoken(n))

def runtime(n, rate):
    w = words(n)
    return "%d:%02d" % (int(w / rate), round((w / rate % 1) * 60))

def _header(d, n, kind):
    m = META[n]
    title_block(d, EYEBROW, m["title"], kind)
    if m["status"]:
        callout(d, m["status"] + ". The title and thumbnail are a working assumption only, and no "
                                 "spoken line names either of them. See V14_FINAL_PACKAGING_DECISION.")
    kv(d, "Number", m["number"])
    kv(d, "Thumbnail", m["thumb"] + (("  [working]") if m["status"] else ""))
    kv(d, "Primary audit question", m["audit"])
    kv(d, "Spoken words", "{:,}".format(words(n)))
    kv(d, "Speech-only estimate", "%s at 145 wpm to %s at 130 wpm. Arithmetic on the words, "
                                  "not a measurement." % (runtime(n, 145), runtime(n, 130)))
    kv(d, "Generated", STAMP)

# ---------------------------------------------------------------- recording master
def recording_master(path, n):
    m = importlib.import_module(B.MODS[n])
    d = base_doc()
    _header(d, n, "Recording master")
    callout(d, "Section labels are production scaffolding and are NOT SPOKEN. The spoken stream is "
               "every paragraph below, in order. Word count is whitespace-delimited tokens of the "
               "spoken stream only.")
    cam = {t: why for t, why in PR.CAMERA[n]}
    br = {t: why for t, why in PR.BROLL[n]}
    snd = {t: why for t, why in PR.SOUND[n]}
    for sec, paras in m.SECTIONS:
        section_label(d, sec)
        notspoken(d, "[NOT SPOKEN]")
        for p in paras:
            spoken(d, p)
            for trig, why in PR.CAMERA[n]:
                if trig == p or trig in p:
                    cue(d, "camera", "CAMERA", why)
            for trig, why in PR.BROLL[n]:
                if trig == p or trig in p:
                    cue(d, "artifact", "FULL SCREEN / B-ROLL", why)
            for trig, why in PR.SOUND[n]:
                if trig == p or trig in p:
                    cue(d, "sound", "ACCENT", why)
    footer_note(d, "Spoken words: %d. Counted from this file's spoken paragraphs at build time."
                % words(n))
    d.save(path)

# ---------------------------------------------------------------- thought blocks
def thought_blocks(path, n):
    w, nb, bad = B.verify(n)
    d = base_doc()
    _header(d, n, "Thought-block recording copy")
    kv(d, "Blocks", "%d" % nb)
    callout(d, "Read one block silently. Look toward the lens. Deliver naturally. Stop. Reset "
               "posture and hands. Advance. Every spoken word from the recording master appears "
               "here exactly once, in the same order. Labels are not spoken.")
    i = 0
    for sec, bs in B.build(n):
        section_label(d, sec)
        notspoken(d, "[NOT SPOKEN]")
        for b in bs:
            i += 1
            marker(d, "BLOCK %02d" % i, "")
            spoken(d, b)
    footer_note(d, "%d blocks, %d spoken words, every block between 2 and 5 sentences. Verified "
                   "against the recording master at build time." % (nb, w))
    d.save(path)

# ---------------------------------------------------------------- production package
def production_package(path, n):
    d = base_doc()
    _header(d, n, "Production package")
    kv(d, "Artifact", META[n]["artifact"])

    h(d, "Full-screen cards")
    caption(d, "Card copy is written here so it can be set without reopening the script. "
               "Any line in a disclosure row stays on screen for the whole hold.")
    rows = []
    for cid, headline, lines, label in PR.FULLSCREEN[n]:
        rows.append([cid, headline, "\n".join(lines), label or ""])
    table(d, ["Card", "Headline", "Copy", "On-card label"], rows,
          widths=[1.55, 1.25, 2.85, 1.05])

    h(d, "Camera beats")
    caption(d, "%d beats. Each one names the sentence it starts on." % len(PR.CAMERA[n]))
    table(d, ["Starts on", "What the camera is doing"],
          [[t, why] for t, why in PR.CAMERA[n]], widths=[3.1, 3.6])

    h(d, "Artifact and B-roll moments")
    caption(d, "%d moments." % len(PR.BROLL[n]))
    table(d, ["Starts on", "Moment"],
          [[t, why] for t, why in PR.BROLL[n]], widths=[3.1, 3.6])

    h(d, "Sound accents")
    caption(d, "%d accents. A guide for the edit, not a quota." % len(PR.SOUND[n]))
    table(d, ["Starts on", "Accent"],
          [[t, why] for t, why in PR.SOUND[n]], widths=[3.1, 3.6])

    page_break(d)
    h(d, "Run of show")
    ros = []
    m = importlib.import_module(B.MODS[n])
    for idx, (sec, paras_) in enumerate(m.SECTIONS, 1):
        first = ""
        for p in paras_:
            hit = None
            for trig, _ in PR.BROLL[n]:
                if trig == p or trig in p:
                    hit = "FULL SCREEN"; break
            if hit is None:
                for trig, _ in PR.CAMERA[n]:
                    if trig == p or trig in p:
                        hit = "CAMERA"; break
            if hit:
                first = hit; break
        body = " ".join(paras_)
        carries = []
        if any(t in body for t, _ in PR.BROLL[n]): carries.append("artifact")
        if any(t in body for t, _ in PR.CAMERA[n]): carries.append("camera")
        if any(t in body for t, _ in PR.SOUND[n]): carries.append("accent")
        ros.append(["%02d" % idx, sec, "%d words" % sum(len(p.split()) for p in paras_),
                    first or "continues", ", ".join(carries)])
    table(d, ["#", "Section", "Length", "First cue", "Carries"], ros,
          widths=[0.45, 2.7, 0.95, 1.1, 1.5])
    caption(d, "First cue is the first camera or full-screen cue inside the section, taken in "
               "paragraph order. A section marked continues has no cue of its own and stays in "
               "whatever mode the previous cue set. Sound accents are listed separately above and "
               "do not change the frame.")

    h(d, "Watch next")
    wn = [c for c in PR.FULLSCREEN[n] if c[0].endswith("WATCH_NEXT")][0]
    para(d, "%s is a full-screen card and is the final frame of the video. Copy: %s"
          % (wn[0], wn[2][0]))
    if n == 13:
        callout(d, "V14's packaging is locked, so V13's Watch Next now names it on camera and on "
                   "the card. V13 still pays off its own promise in full before this line.")
    footer_note(d, "%d full-screen cards, %d camera beats, %d artifact moments, %d sound accents."
                % (len(PR.FULLSCREEN[n]), len(PR.CAMERA[n]), len(PR.BROLL[n]), len(PR.SOUND[n])))
    d.save(path)

# ---------------------------------------------------------------- shorts
def shorts_doc(path, n):
    d = base_doc()
    _header(d, n, "Three candidate Shorts")
    kv(d, "Count", "Three. A selection bank, not three mandatory uploads.")
    callout(d, "Every line below is a run of consecutive whole sentences lifted verbatim from this "
               "video's recording master, checked run by run against it at build time. Nothing was "
               "invented and no two non-adjacent sentences were pushed together into a claim the "
               "master does not make. Each Short carries one complete idea and one ask.")
    caption(d, "Lengths are arithmetic on the words, not measured. Final captions and timecodes "
               "follow the final Short export.")
    for num in (1, 2, 3):
        k = (n, num)
        s = S.SHORTS[k]
        h(d, "SHORT %d  |  %s" % (num, s["label"]))
        kv(d, "Length", "%d words. %.0f seconds at 165 wpm, %.0f seconds at 150 wpm."
           % (S.words(k), S.seconds(k, 165), S.seconds(k, 150)))
        sub(d, "STOP SCROLL")
        for x in s["stop"]:
            spoken(d, x)
        sub(d, "HOLD ATTENTION")
        for x in s["hold"]:
            spoken(d, x)
        sub(d, "ONE ASK")
        for x in s["ask"]:
            spoken(d, x)
        sub(d, "OPENING, SPECIFIC TO THIS SHORT")
        para(d, s["opening"])
        sub(d, "CUT TO")
        para(d, s["cut"])
        sub(d, "PAYOFF FRAME")
        para(d, "%s, held on the ask. It is the last frame." % s["card"])
        sub(d, "STANDS ALONE")
        para(d, "Understandable without the long-form video. It is not a trailer, and the ask is "
                "the only ask. The card named above is specified in this video's production package.")
    over = [(k, S.seconds(k, 150)) for k in sorted(S.SHORTS)
            if k[0] == n and S.seconds(k, 150) > S.CEILING_SECONDS]
    if over:
        callout(d, "At the 150 wpm planning rate, %s crosses 55 seconds (%s). Every Short here is "
                   "inside 55 seconds at the 165 wpm ceiling. If the read comes in slow, these are "
                   "the ones to trim in the edit."
                % (" and ".join("Short %d" % k[1] for k, _ in over),
                   " and ".join("%.0fs" % v for _, v in over)))
    d.save(path)

# ---------------------------------------------------------------- description
def description_doc(path, n):
    d = base_doc()
    _header(d, n, "Description and metadata")
    h(d, "Copy-ready YouTube description")
    for p in D.BODY[n]:
        spoken(d, p)
    emoji, name, blurb, url = D.RESOURCE[n]
    sub(d, emoji)
    para(d, name, bold=True)
    para(d, blurb)
    para(d, url)
    caption(d, "One resource. There is no second link and no second ask in this description.")
    wn, note = D.WATCH_NEXT[n]
    sub(d, "\U0001F3A5 Watch next")
    para(d, wn)
    if note:
        para(d, note, bold=True)
    para(d, "[PASTE VIDEO URL AFTER UPLOAD]")
    sub(d, "\U0001F4FA Playlist")
    para(d, D.PLAYLIST)
    para(d, "[PASTE PLAYLIST URL AFTER UPLOAD]")
    verse, ref, reflection = D.FAITH[n]
    sub(d, "\U0001F64F A faith anchor")
    callout(d, D.SCRIPTURE_STATUS)
    para(d, verse)
    para(d, ref + "   [NLT WORDING REQUIRES VERIFICATION]")
    para(d, reflection)
    caption(d, "The faith anchor is not spoken on camera, is kept clearly separate from the "
               "resource, and is not a second call to action.")
    para(d, D.COPYRIGHT, size=9)
    page_break(d)
    h(d, "Metadata")
    kv(d, "Title", META[n]["title"] + ("  [working]" if META[n]["status"] else ""))
    kv(d, "Thumbnail", META[n]["thumb"] + ("  [working]" if META[n]["status"] else ""))
    kv(d, "Playlist", D.PLAYLIST)
    sub(d, "Tags")
    para(d, ", ".join(D.TAGS[n]))
    sub(d, "Pinned comment")
    para(d, D.PINNED[n])
    d.save(path)

# ---------------------------------------------------------------- provenance
def provenance_doc(path, n):
    d = base_doc()
    _header(d, n, "Source and provenance")
    h(d, "Source hierarchy")
    for s in PV.SOURCES[n]:
        sub(d, s["role"])
        kv(d, "File", s["name"])
        kv(d, "Where", s["where"])
        kv(d, "SHA-256", s["sha"])
        kv(d, "Size", s["size"])
        para(d, s["note"])
    used = [c for c, p in PV.POSTINGS.items() if META[n]["number"] in p["used_in"]]
    if used:
        h(d, "Postings quoted on camera")
        caption(d, "Employers are named at the level of what the posting says. No claim is made "
                   "about how any employer evaluates people.")
        for c in used:
            p = PV.POSTINGS[c]
            sub(d, "%s  ·  %s" % (p["code"], p["employer"]))
            kv(d, "Role title", p["title"])
            kv(d, "URL", p["url"])
            kv(d, "Collected", p["collected"])
            kv(d, "Posting dates", p["posted"])
            kv(d, "Capture", p["capture"])
            kv(d, "Hard", p["hard"])
            kv(d, "Preferred", p["preferred"])
            kv(d, "Quoted", p["quote"])
            para(d, p["coder"])
    if n in (13, 14):
        h(d, "The sample")
        table(d, ["Metric", "Count"], [[a, b] for a, b in PV.SAMPLE], widths=[4.4, 2.3])
        para(d, PV.SAMPLE_NOTE)
        h(d, "What this evidence cannot establish")
        bullets(d, PV.LIMITS)
    if n == 12:
        h(d, "The synthetic artifact")
        para(d, "The accomplishment shown and rebuilt in V12 was written for the video. It is not "
                "anyone's resume and it is not drawn from a client, a case study, or any record "
                "held by Temidayo. The disclosure is spoken in the first thirty seconds, printed "
                "on both cards that carry the example, and repeated in the pinned comment.")
        para(d, "The rebuilt version is read in the first person because that is how the person "
                "would write it. The spoken line before it says so explicitly, so the “I” "
                "cannot be mistaken for Temidayo's own experience.")
    d.save(path)
