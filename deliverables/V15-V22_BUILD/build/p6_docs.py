# -*- coding: utf-8 -*-
"""Documents for the V15-V22 final production pack.

Every number in these documents is read from the build modules, never typed.
House helpers are imported from the earlier batches and are not edited.
"""
import os, sys, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.append("/home/user/temidayoafonja-site/deliverables/VIDEOS_22-23/build")
# Every module in this pack is prefixed p6_ because the house document helpers
# insert their own build directories at the front of sys.path, which shadows bare
# names like build, shorts and packaging.

import importlib
from docs23 import (base_doc, title_block, h, kv, para, callout, sub, caption,
                    table, bullets, footer_note, page_break, spoken, marker,
                    cue, section_label, notspoken, numbered, field, rule)

import p6_blocks as B
import p6_shorts as S
import p6_production as PR
import p6_descriptions as D
import p6_provenance as PV
import p6_packaging as PK
import p6_checks_script as CH

EYEBROW = "capability formation | final production"
STAMP = "Wednesday, September 23, 2026"

META = {
15: dict(number="V15", title="How to Prove Your Value When AI Does More of the Task",
         thumb="SO WHAT DID YOU DO?", status=None,
         audit="What can you prove?",
         artifact="A four-page quarterly summary a tool drafted in forty minutes. "
                  "Constructed, labelled on the card and named as constructed on camera."),
16: dict(number="V16", title="What to Do When Your Work Is Valued but You Are Overlooked",
         thumb="RELIED ON. STILL SKIPPED.", status=None,
         audit="Is this an information problem, or is it not?",
         artifact="No constructed artifact. The cards are the pattern, the hinge, and the "
                  "two branches that follow from it."),
17: dict(number="V17", title="Before a Layoff, Know What You Can Still Prove",
         thumb="KEEP THE EVIDENCE", status=None,
         audit="What can you still prove, lawfully, from where you are standing?",
         artifact="No constructed artifact. The boundary card is the one that has to hold "
                  "longest on screen."),
18: dict(number="V18", title="What You Must Relearn When You Change Industries",
         thumb="EXPERIENCED AND NEW", status=None,
         audit="What does not travel?",
         artifact="One evidence card carrying the star-analyst study, labelled ONE STUDY, "
                  "ONE PROFESSION for its full hold."),
19: dict(number="V19", title="The Career Gaps You Don't See Until the Work Gets Harder",
         thumb="WHAT DO YOU RECOMMEND?", status=None,
         audit="Which gap is this actually?",
         artifact="A constructed analyst, labelled on the card. No real person and no "
                  "composite of one."),
20: dict(number="V20", title="What Happens When the Next Step in Your Career Disappears?",
         thumb="PENDING TEMIDAYO APPROVAL",
         status="THUMBNAIL PENDING APPROVAL",
         audit="What was the next role actually going to give you?",
         artifact="A numbers card carrying the attribution for its full hold. Three "
                  "figures, no chart."),
21: dict(number="V21", title="How Do You Grow When There Are Fewer Roles Above You?",
         thumb="WHAT DOES \u201cUP\u201d MEAN NOW?", status=None,
         audit="Did anything actually move this year?",
         artifact="Two people at the same level, side by side. The longest hold in the "
                  "video."),
22: dict(number="V22", title="The Career Ladder Doesn't Work the Same Way Anymore",
         thumb="THE NEXT RUNG IS GONE", status=None,
         audit="Readiness, or structure?",
         artifact="Two org charts, before and after. Both constructed, both labelled NOT "
                  "A REAL EMPLOYER'S ORG CHART for their full hold."),
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
        callout(d, m["status"] + ". The title is LOCKED and is not reopened. Only the thumbnail "
                                 "line is open, the script names neither, and the placeholder "
                                 "above ships on purpose so an unapproved line cannot reach a "
                                 "render. Three candidates and one recommendation are in "
                                 "00_V20_THUMBNAIL_DECISION.")
    kv(d, "Number", m["number"])
    kv(d, "Thumbnail", m["thumb"])
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
    if n == 22:
        callout(d, "V22 routes to the locked V13. It deliberately does not point at the episode "
                   "that would naturally follow it, because that episode has not been built. "
                   "Nothing in this pack sends a viewer to a video that does not exist.")
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
    if n in D.RESOURCE:
        emoji, name, blurb, url = D.RESOURCE[n]
        sub(d, emoji)
        para(d, name, bold=True)
        para(d, blurb)
        para(d, url)
        caption(d, "One resource. There is no second link and no second ask in this description. "
                   "It is here because the recording master earns it out loud.")
    else:
        caption(d, "NO RESOURCE. This video ships with no commercial link and no ask beyond "
                   "Watch next. The recording master does not mention a resource, and adding "
                   "one in the description would be an ask the video did not earn.")
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

    h(d, "Editorial sources for this video")
    for role, name, note in PV.SOURCES[n]:
        sub(d, role)
        kv(d, "Source", name)
        para(d, note)

    cited = [c for c in PV.CLAIMS if n in c["spoken"]]
    if cited:
        h(d, "Evidence spoken in this video")
        caption(d, "The class beside each claim is the class the SOURCE REPORT gave it, not a "
                   "class assigned here. An Interpretation is not reported as a Quantitative "
                   "finding and a Hypothesis is not reported as an Interpretation.")
        for c in cited:
            sub(d, "%s  \u00b7  %s" % (c["id"], c["report_class"]))
            para(d, c["claim"])
            kv(d, "Cited by the report as", c["source"])
            para(d, c["carried"])

    art = [c for c in PV.CONSTRUCTED if c[0] == n]
    if art:
        h(d, "Constructed artifacts in this video")
        for _, cid, desc, label, note in art:
            sub(d, cid)
            kv(d, "What it shows", desc)
            kv(d, "On-card label", label)
            para(d, note)

    h(d, "Employers")
    para(d, PV.EMPLOYERS)
    caption(d, PV.VIEWER_FACING_SCOPE)

    h(d, "Evidence source of record")
    kv(d, "File", PV.EVIDENCE_OF_RECORD["name"])
    kv(d, "Where", PV.EVIDENCE_OF_RECORD["where"])
    kv(d, "SHA-256", PV.EVIDENCE_OF_RECORD["sha"])
    kv(d, "Size", PV.EVIDENCE_OF_RECORD["size"])
    kv(d, "Shape", PV.EVIDENCE_OF_RECORD["shape"])
    para(d, PV.EVIDENCE_OF_RECORD["note"])
    caption(d, "The full evidence-class table, every claim considered and set aside, and "
               "everything the report could not establish are in "
               "00_MISSING_RUNG_EVIDENCE_BOUNDARIES.")
    d.save(path)
