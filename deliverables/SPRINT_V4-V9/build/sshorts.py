# -*- coding: utf-8 -*-
"""The three supplied candidate Shorts per video.

Three means three. These are the selection bank the script supplies; none is
added, none is expanded to six, and nothing is invented to strengthen a hook.
Each Short's evidence boundary is inherited from its parent video.
"""
import sprint as S
from sdocs import (base_doc, title_block, h, kv, para, callout, sub, caption,
                   table, bullets, footer_note, page_break, spoken, mono, hr,
                   head, _wrap, EYEBROW)

WPM = 165

# The boundary each video's Shorts must carry, in the parent video's terms.
BOUNDARY = {
 4: "Not an anti-AI claim. The video does not say AI always removes "
    "learning, always damages capability, or eliminates developmental "
    "experience. A Short may not tighten that into a prediction.",
 5: "Being needed is not treated as bad, and no employer owes an automatic "
    "promotion. A Short may not turn the tension into a grievance.",
 6: "Fifteen postings from eleven employers. No labor-market "
    "generalization, and the highest published ceiling is bounded to the "
    "sample. No local meeting time is stated or implied.",
 7: "Advancement is not reduced to merit. Bias, politics, sponsorship, "
    "access, timing and manager behavior stay visible in any Short drawn "
    "from this video.",
 8: "Keep the proof, not the property. No Short may suggest retaining "
    "confidential documents, proprietary files, customer data, screenshots "
    "of restricted systems, source code or internal financials.",
 9: "Not anti-transferability. A Short may not leave NOT EVERYTHING TRAVELS "
    "standing alone without the rest of the audit.",
}

EDITOR = {
 4: "Reuse the long-form cards reframed to 9:16 where one exists. No AI "
    "stock imagery.",
 5: "Reuse the dependence-and-development contrast where it fits. Nothing "
    "implying a specific employer.",
 6: "Reuse the posting artifact cards. Any figure keeps its sample "
    "boundary on screen.",
 7: "Reuse the four-things card. If only one of the four appears, the "
    "not-merit line still has to travel with it.",
 8: "Never depict a file, a screenshot or a download. Handwriting and "
    "plain cards only.",
 9: "If a Short uses only one audit question, the other three must appear "
    "at least once before the ask.",
}


def rows(n):
    out = []
    for s in S.shorts(n):
        words = len(s["body"].split())
        out.append(dict(num=s["num"], hook=s["hook"], body=s["body"],
                        ask=s["ask"], words=words,
                        secs=int(round(words / float(WPM) * 60))))
    return out


def bank(n, path, stamp):
    d = base_doc()
    title_block(d, EYEBROW, S.title(n),
                "Three candidate Shorts, as supplied with the script")
    kv(d, "New public number", "V%d" % n)
    kv(d, "Former roadmap number", "V%d" % S.NUMBERS[n])
    kv(d, "Count", "Three. This is the current selection bank and was not "
                   "expanded.")
    kv(d, "Generated", stamp)
    callout(d, "These three Shorts are supplied inside the FINAL sprint "
               "script and are reproduced here word for word. Three means "
               "three: the bank was not expanded to six, and not all three "
               "have to be published. Each must stand alone without the "
               "long-form video.")
    table(d, ["#", "Stop scroll", "Words", "At 165 wpm"],
          [["%d" % r["num"], r["hook"], format(r["words"], ","),
            "0:%02d" % r["secs"]] for r in rows(n)],
          widths=[0.35, 3.6, 0.8, 1.0], size=8.5)
    caption(d, "Lengths are arithmetic, not measured.")
    for r in rows(n):
        page_break(d)
        _one(d, n, r)
    d.save(path)
    return path


def _one(d, n, r):
    h(d, "Short %d  |  %s" % (r["num"], r["hook"]))
    kv(d, "Length", "%d words, about 0:%02d at 165 words per minute"
       % (r["words"], r["secs"]))
    sub(d, "Spoken, as supplied")
    spoken(d, r["body"])
    sub(d, "One ask")
    para(d, r["ask"], size=11, bold=True)
    sub(d, "Evidence boundary inherited from the long-form video")
    para(d, BOUNDARY[n], size=10.5)
    sub(d, "Editor note")
    para(d, EDITOR[n], size=10.5)
    sub(d, "Stands alone")
    para(d, "This Short is understandable without watching the long-form "
            "video. It is not a trailer, and the ask is the only ask.",
        size=10.5)


def single(n, r, path, stamp):
    d = base_doc()
    title_block(d, EYEBROW, "Short %d" % r["num"],
                "Candidate Short from NEW V%d (former roadmap V%d)"
                % (n, S.NUMBERS[n]))
    kv(d, "Parent video", S.title(n))
    kv(d, "Generated", stamp)
    _one(d, n, r)
    footer_note(d, "Vertical. Shorts captions are set at upload.")
    d.save(path)
    return path


def editor_notes(n, path):
    L = head("NEW V%d  (FORMER ROADMAP V%d)  |  SHORTS VISUAL AND EDITOR "
             "NOTES" % (n, S.NUMBERS[n]))
    L += [S.title(n), "",
          "Three candidates, as supplied. The bank was not expanded.",
          "Not all three have to be published.",
          "", hr(), "", "SHARED RULES", "",
          "  9:16. The same navy, cream and warm gold system as the video.",
          "  Large type. One idea per card. Generous margins.",
          "  Reuse the long-form card where one exists, reframed to 9:16,",
          "  rather than building a different-looking version of it.",
          "  Each Short stands alone. It is not a trailer and it does not",
          "  require the long-form video to make sense.",
          "  One ask at the end. Never two.",
          "  No claim is added to strengthen a hook.",
          "", hr(), "", "EVIDENCE BOUNDARY FOR EVERY SHORT FROM THIS VIDEO",
          ""]
    L += ["  %s" % x for x in _wrap(BOUNDARY[n], 68)]
    L += ["", hr(), ""]
    for r in rows(n):
        L += ["SHORT %d  |  %s" % (r["num"], r["hook"]),
              "    LENGTH:   %d words, about 0:%02d at 165 wpm"
              % (r["words"], r["secs"]),
              "    ONE ASK:  %s" % r["ask"],
              "    EDITOR:"]
        L += ["        %s" % x for x in _wrap(EDITOR[n], 62)]
        L.append("")
    return mono(path, L)


def boundary_notes(n, path, stamp):
    d = base_doc()
    title_block(d, EYEBROW, S.title(n),
                "Shorts evidence-boundary notes")
    kv(d, "New public number", "V%d" % n)
    kv(d, "Former roadmap number", "V%d" % S.NUMBERS[n])
    kv(d, "Generated", stamp)
    para(d, "Every Short inherits the research and evidence boundaries of "
            "its parent video. A Short is often where a boundary gets "
            "dropped for pace. It may not be dropped here.", size=11)
    h(d, "The boundary")
    callout(d, BOUNDARY[n])
    h(d, "Per Short")
    table(d, ["#", "Stop scroll", "The boundary it must carry"],
          [["%d" % r["num"], r["hook"], BOUNDARY[n]] for r in rows(n)],
          widths=[0.35, 2.6, 3.75], size=8)
    footer_note(d, "No Short adds a claim to strengthen a hook, and none "
                   "introduces research the long-form video does not make.")
    d.save(path)
    return path
