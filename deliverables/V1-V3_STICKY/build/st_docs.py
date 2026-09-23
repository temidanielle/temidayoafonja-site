# -*- coding: utf-8 -*-
"""Documents for the V1-V3 sticky-realization production packages.

Every number in these documents is read from the build modules at generation
time, never typed.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.append("/home/user/temidayoafonja-site/deliverables/VIDEOS_22-23/build")

from docs23 import (base_doc, title_block, h, kv, para, callout, sub, caption,
                    table, bullets, footer_note, page_break, spoken, marker,
                    cue, section_label, notspoken, rule)

import st_parse as P, st_frames as F, st_production as PR
import st_shorts as S, st_desc as D, st_prov as V

EYEBROW = "capability formation | h.i.t. refresh"
STAMP = "Tuesday, September 23, 2026"

META = {
1: dict(number="V1", title="How to Change Careers After 10+ Years Without Starting Over",
        thumb="WHAT ACTUALLY TRANSFERS?",
        question="I have spent 10, 15 or 20 years building this career. If I "
                 "change direction, what actually comes with me?",
        artifact="Two anonymized role types, side by side: Senior Manager, "
                 "Program Management and Director, Enterprise Transformation."),
2: dict(number="V2", title="Is Your Job Making You Harder to Hire?",
        thumb="HARDER TO HIRE?",
        question="How much of what makes me valuable here would still make "
                 "sense somewhere else?",
        artifact="One resume sentence, then the same claim with the company "
                 "nouns removed. Both labelled as constructed examples."),
3: dict(number="V3", title="Before You Quit Your Job, Save This First",
        thumb="YOU CAN’T PROVE IT LATER",
        question="What can I still prove, lawfully, once my access is gone?",
        artifact="A thin one-line claim, then the same example rebuilt. Both "
                 "labelled as constructed examples."),
}

MEMORY = {
1: ("MY EXPERIENCE DOES NOT MOVE AS ONE BLOCK.",
    "Put your current work beside the destination and separate what travels, "
    "what does not, what can be proved, and what may need relearning."),
2: ("WHAT PART OF THIS IS ME, AND WHAT PART IS MY ACCESS TO THIS ENVIRONMENT?",
    "Take one thing people rely on you for, remove the company language, "
    "explain the judgment underneath it, then look for evidence it works "
    "elsewhere."),
3: ("KEEP THE PROOF, NOT THE PROPERTY.",
    "Before access ends, capture one permitted example: the problem, what was "
    "yours, what changed, and what permitted evidence supports it."),
}

def words(n):
    return P.words(n)

def runtime(n, rate):
    w = words(n)
    return "%d:%02d" % (int(w / rate), round((w / rate % 1) * 60))

def _header(d, n, kind):
    m = META[n]
    title_block(d, EYEBROW, m["title"], kind)
    kv(d, "Number", m["number"])
    kv(d, "Thumbnail", m["thumb"])
    kv(d, "Core viewer question", m["question"])
    kv(d, "Spoken words", "{:,}".format(words(n)))
    kv(d, "Speech-only estimate",
       "%s at 145 wpm to %s at 130 wpm. Arithmetic on the words, not a "
       "measurement." % (runtime(n, 145), runtime(n, 130)))
    kv(d, "Generated", STAMP)

# ---------------------------------------------------------------- master
def recording_master(path, n):
    d = base_doc()
    _header(d, n, "Recording master")
    callout(d, "This is the FINAL Sticky Realization master, read out of the "
               "supplied .docx at build time and not retyped. Section labels "
               "are production scaffolding and are NOT SPOKEN. The spoken "
               "stream is every paragraph below, in order.")
    for sec, paras in P.master(n)[1]:
        section_label(d, sec)
        notspoken(d, "[NOT SPOKEN]")
        for p in paras:
            spoken(d, p)
            for trig, why in PR.CAMERA[n]:
                if trig == p or trig in p or p in trig:
                    cue(d, "camera", "CAMERA", why)
            for trig, why in PR.BROLL[n]:
                if trig == p or trig in p or p in trig:
                    cue(d, "artifact", "FULL SCREEN / B-ROLL", why)
            for trig, why in PR.SOUND[n]:
                if trig == p or trig in p or p in trig:
                    cue(d, "sound", "ACCENT", why)
            if PR.SUBSCRIBE[n][0] == p or PR.SUBSCRIBE[n][0] in p:
                cue(d, "camera", "SUBSCRIBE", PR.SUBSCRIBE[n][1])
    footer_note(d, "Spoken words: %d. Counted from this file's spoken "
                   "paragraphs at build time." % words(n))
    d.save(path)

# ---------------------------------------------------------------- blocks
def thought_blocks(path, n):
    d = base_doc()
    _header(d, n, "Thought-block recording copy")
    wa, wb, ok, _f = P.verify(n)
    kv(d, "Blocks", "%d" % sum(len(b) for _s, b in P.blocks(n)))
    kv(d, "Parity with the master", "exact, %d words" % wa if ok else "MISMATCH")
    callout(d, "These are the SUPPLIED thought blocks, used exactly. Nothing "
               "was rewritten during conversion. Read one block silently. Look "
               "toward the lens. Deliver naturally. Stop. Reset posture and "
               "hands. Advance. Labels are not spoken.")
    i = 0
    for sec, bs in P.blocks(n):
        section_label(d, sec)
        notspoken(d, "[NOT SPOKEN]")
        for b in bs:
            i += 1
            marker(d, "BLOCK %02d" % i, "")
            spoken(d, b)
    footer_note(d, "%d blocks, %d spoken words, verified word for word against "
                   "the recording master at build time." % (i, wa))
    d.save(path)

# ---------------------------------------------------------------- production
def production_package(path, n):
    d = base_doc()
    _header(d, n, "Production package and editor cue map")
    kv(d, "Teaching artifact", META[n]["artifact"])
    kv(d, "Seven-day memory line", MEMORY[n][0])

    h(d, "Full-screen slides and reveal states")
    caption(d, "Card copy is written here so it can be set without reopening "
               "the script. A constructed-example label stays on screen for "
               "the whole hold of the card that carries it.")
    rows = []
    for fam, name, draw, note in F.states(n):
        rows.append([name, note])
    table(d, ["State", "What it is doing, and when"], rows, widths=[2.1, 4.6])

    h(d, "Camera-emphasis beats")
    caption(d, "%d beats. Each one names the sentence it starts on."
            % len(PR.CAMERA[n]))
    table(d, ["Starts on", "What the camera is doing"],
          [[t, w] for t, w in PR.CAMERA[n]], widths=[3.1, 3.6])

    h(d, "Artifact and B-roll moments")
    caption(d, "%d moments." % len(PR.BROLL[n]))
    table(d, ["Starts on", "Moment"],
          [[t, w] for t, w in PR.BROLL[n]], widths=[3.1, 3.6])

    h(d, "Sound accents")
    caption(d, "%d accents. A guide for the edit, not a quota."
            % len(PR.SOUND[n]))
    table(d, ["Starts on", "Accent"],
          [[t, w] for t, w in PR.SOUND[n]], widths=[3.1, 3.6])

    h(d, "Subscribe cue")
    sub(d, "Starts on")
    para(d, PR.SUBSCRIBE[n][0])
    para(d, PR.SUBSCRIBE[n][1])
    caption(d, "One cue, quiet, placed after value has been delivered and "
               "never on top of a boundary, a payoff or the CTA.")

    page_break(d)
    h(d, "Run of show")
    ros = []
    for idx, (sec, paras_) in enumerate(P.master(n)[1], 1):
        body = " ".join(paras_)
        carries = []
        if any(t in body or body in t for t, _ in PR.BROLL[n]): carries.append("artifact")
        if any(t in body or body in t for t, _ in PR.CAMERA[n]): carries.append("camera")
        if any(t in body or body in t for t, _ in PR.SOUND[n]): carries.append("accent")
        ros.append(["%02d" % idx, sec, "%d words" % sum(len(p.split()) for p in paras_),
                    ", ".join(carries) or "continues"])
    table(d, ["#", "Section", "Length", "Carries"], ros,
          widths=[0.45, 3.0, 1.0, 2.25])

    h(d, "CTA and Watch Next")
    para(d, "%s is the full-screen call to action. %s is a full-screen card and "
            "is the FINAL frame of the video."
          % (PR.CTA_CARD[n], PR.WATCH_CARD[n]))
    para(d, "Watch next: %s" % D.WATCH_NEXT[n])
    footer_note(d, "%d full-screen states, %d camera beats, %d artifact "
                   "moments, %d sound accents, one Subscribe cue."
                % (sum(1 for _ in F.states(n)), len(PR.CAMERA[n]),
                   len(PR.BROLL[n]), len(PR.SOUND[n])))
    d.save(path)

# ---------------------------------------------------------------- shorts
def shorts_doc(path, n):
    d = base_doc()
    _header(d, n, "Three candidate Shorts")
    kv(d, "Count", "Three. A candidate bank, not three mandatory uploads.")
    callout(d, "Every line below is a run of consecutive whole sentences "
               "lifted verbatim from this video's recording master, checked "
               "word for word against it at build time. Nothing was invented "
               "and no two non-adjacent passages were pushed together into a "
               "claim the master does not make. Each Short carries one "
               "complete idea and one ask.")
    caption(d, "Lengths are arithmetic on the words, not measured. Captions "
               "must be set from these lines exactly.")
    for num in (1, 2, 3):
        k = (n, num)
        s = S.SHORTS[k]
        h(d, "SHORT %d  |  %s" % (num, s["label"]))
        kv(d, "Territory", s["territory"])
        kv(d, "Length", "%d words. %.0f seconds at 165 wpm, %.0f seconds at "
                        "150 wpm." % (S.words(k), S.seconds(k, 165),
                                      S.seconds(k, 150)))
        sub(d, "STOP SCROLL")
        for x in s["stop"]:
            spoken(d, x)
        sub(d, "HOLD")
        for x in s["hold"]:
            spoken(d, x)
        sub(d, "ONE ASK")
        for x in s["ask"]:
            spoken(d, x)
        sub(d, "OPENING")
        para(d, s["opening"])
        sub(d, "CUT TO")
        para(d, s["cut"])
        sub(d, "PAYOFF FRAME")
        para(d, "%s, held on the ask. It is the last frame." % s["card"])
    d.save(path)

# ---------------------------------------------------------------- description
def description_doc(path, n):
    d = base_doc()
    _header(d, n, "Description and publishing metadata")
    callout(d, D.STATUS)
    h(d, "Copy-ready YouTube description")
    for p in D.BODY[n]:
        spoken(d, p)
    emoji, name, blurb, url = D.RESOURCE[n]
    sub(d, emoji)
    para(d, name, bold=True)
    para(d, blurb)
    para(d, url)
    caption(d, "One resource. There is no second link and no second ask in "
               "this description, and the video names this resource out loud.")
    sub(d, "\U0001F3A5 Watch next")
    para(d, D.WATCH_NEXT[n])
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
    caption(d, "The faith anchor follows the practical link, is not spoken on "
               "camera, and is not a second call to action.")
    para(d, D.COPYRIGHT, size=9)
    page_break(d)
    h(d, "Metadata")
    kv(d, "Title", META[n]["title"])
    kv(d, "Thumbnail", META[n]["thumb"])
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
    callout(d, "PRIVATE. NOT FOR PUBLICATION.")

    h(d, "Spoken source of truth")
    s = V.SOURCES[n]
    kv(d, "Recording master", s["master"])
    kv(d, "SHA-256", s["master_sha"])
    kv(d, "Size", s["master_size"])
    kv(d, "Thought blocks", s["blocks"])
    kv(d, "SHA-256", s["blocks_sha"])
    kv(d, "Size", s["blocks_size"])
    para(d, V.SOURCE_NOTE)
    wa, wb, ok, _f = P.verify(n)
    kv(d, "Parity", "Blocks reproduce the master exactly: %d words." % wa
       if ok else "MISMATCH")

    fused = [x for x in V.FUSED_LABELS if x[0] == n]
    if fused:
        h(d, "Source repair")
        for _n, lab, first, why in fused:
            sub(d, lab)
            kv(d, "Ran into", first)
            para(d, why)

    if n == 1:
        h(d, "The teaching artifact")
        table(d, ["Public identifier", "Role title", "Employer", "Source URL"],
              [[a, b, c, e] for a, b, c, e in V.ROLES], widths=[1.6, 2.2, 1.4, 1.5])
        para(d, V.ROLES_NOTE)

    con = [x for x in V.CONSTRUCTED if x[0] == n]
    if con:
        h(d, "Constructed examples")
        for _n, cid, what, why in con:
            sub(d, cid)
            kv(d, "What it shows", what)
            kv(d, "On-card label", "SYNTHETIC EXAMPLE")
            para(d, why)

    h(d, "Boundaries held")
    bullets(d, V.BOUNDARIES[n])

    h(d, "Descriptions")
    para(d, V.DESCRIPTIONS_NOT_SUPPLIED)

    h(d, "Scripture verification status")
    callout(d, V.SCRIPTURE)

    h(d, "URLs")
    para(d, V.URLS)

    h(d, "What this pack cannot establish")
    bullets(d, V.LIMITS)
    d.save(path)

# ---------------------------------------------------------------- asset index
def asset_index(path, n, pngs, svgs, sheet):
    d = base_doc()
    _header(d, n, "Asset index")
    kv(d, "Full-screen states", "%d" % len(pngs))
    kv(d, "Editable vector source", "%d SVG" % len(svgs))
    kv(d, "Phone-size contact sheet", os.path.basename(sheet))
    callout(d, "Every PNG is 1920x1080. SVG is written for the frames an "
               "editor is most likely to re-time or re-colour: each memory "
               "card, each CTA, each Watch Next, and the frame that is this "
               "video's visual payoff.")
    rows = []
    svgset = {os.path.basename(x)[:-4] for x in svgs}
    for fam, name, draw, note in F.states(n):
        rows.append([name, "PNG + SVG" if name in svgset else "PNG", note])
    table(d, ["Asset", "Formats", "Purpose"], rows, widths=[2.0, 0.9, 3.8])
    footer_note(d, "%d PNG, %d SVG, one contact sheet."
                % (len(pngs), len(svgs)))
    d.save(path)
