# -*- coding: utf-8 -*-
"""Source hierarchy, evidence notes and claim-boundary notes.

Neither video cites external research, and none is invented for either. Both
are practitioner teaching: what Temidayo has seen, stated as her own read,
with the limits of that read kept on screen rather than trimmed for pace.
"""
import v1011 as S
import frames1011 as F
import shorts1011 as SH
from docs1011 import (base_doc, title_block, h, kv, para, callout, sub,
                      caption, table, bullets, footer_note, mono, hr, head,
                      _wrap, EYEBROW)

# The editorial boundary each video must keep, from the handoff and from the
# script itself. Nothing here is invented: each is stated or protected in
# the spoken script.
BOUNDARIES = {
 10: [("No theatrical quick win",
       "I do not think everybody needs a giant visible win by day 90.",
       "The script names the reasons: some work has a long learning curve, "
       "some is regulated, some senior roles require context before "
       "intervention, some problems should not be solved quickly. The "
       "PROVE card asks what you can prove, not what you can win."),
      ("No universal manager claim",
       "The script never says what every manager evaluates.",
       "The manager questions are questions to ask, not a claim about what "
       "managers do. No card generalizes them into a rule."),
      ("Experience is not context",
       "You can be experienced and still be new to the context.",
       "That sentence is a full-screen card. The video never treats "
       "experience as worthless, and never treats it as sufficient."),
      ("The reversal is not an exit instruction",
       "That does not automatically mean leave.",
       "The script protects legitimate change in the same breath: roles "
       "change, priorities change, organizations have real constraints. "
       "That protection is a card of its own and is not cut."),
      ("READ does not mean silence",
       "READ does not mean sit quietly for 30 days and contribute nothing.",
       "The script says to raise a risk, contribute what is useful, and "
       "use the expertise you were hired for. The point is not to make "
       "yourself small.")],
 11: [("The employer is not the villain",
       "A job can change for legitimate reasons.",
       "Roles change, priorities move, managers inherit new problems, "
       "organizations reorganize. Those lines open the video and are on "
       "the boundary card. No card, no Short and no Riverside instruction "
       "frames the organization as having lied."),
      ("Bait-and-switch is not a label",
       "Before you call it a bait-and-switch, I want you to slow the read "
       "down.",
       "The phrase appears once, as the reading the viewer is asked to "
       "slow down. It is never used as a verdict and never appears on a "
       "card."),
      ("Drift is not always downward",
       "Sometimes the actual role is better than the one you expected.",
       "The EXPECTED against ACTUAL comparison shows both directions. The "
       "better reading is on the card, not only the narrower one."),
      ("The framework is not a verdict",
       "This framework does not tell you whether to leave.",
       "Stay, stay for now, or plan an exit are all kept open on the "
       "boundary card, in the script's own words."),
      ("Constraints are real",
       "Compensation, health, caregiving, immigration, geography, timing, "
       "the market, and financial runway can all shape what is possible.",
       "Named on a card of their own, so the video is not advice for "
       "people with no constraints.")],
}

EVIDENCE_NOTE = {
 10: "This video cites no external research and none is invented for it. "
     "It is practitioner teaching: a read Temidayo offers in her own "
     "voice, phrased throughout as what she would do rather than as a "
     "finding. The phrasing matters and is preserved: I do not think, I "
     "would use a different question, I would have a very simple "
     "conversation. No study, statistic, employer behavior or outcome is "
     "claimed anywhere in the package.",
 11: "This video cites no external research and none is invented for it. "
     "It is practitioner teaching, phrased as a read rather than a "
     "finding: I use four questions for that, I would look at four costs, "
     "I would avoid two extremes. No study, statistic, employer intent or "
     "outcome is claimed anywhere in the package, and no claim is made "
     "about how often role drift happens.",
}

NEVER = [
 "No invented research, employer behavior, personal experience or "
 "outcome.",
 "No invented runtime, public URL, upload date, thumbnail result, "
 "retention figure or music license.",
 "No chapters and no SRT timing before the final edit.",
 "No former-roadmap number: both videos are new concepts and no lineage "
 "number exists to cite.",
 "No second spoken CTA, and no product named in the spoken script or on "
 "any card.",
]


def source_hierarchy(n, path, stamp, sources):
    L = head("NEW PUBLIC V%d  |  SOURCE MANIFEST AND NUMBER MAP" % n)
    L += [S.title(n), "Generated %s" % stamp, "", hr(), "",
          "NUMBER MAP", "",
          "  NEW PUBLIC NUMBER      V%d" % n,
          "  FORMER ROADMAP NUMBER  None. This is a new concept.",
          "",
          "  Neither V10 nor V11 came from the earlier roadmap, so there is",
          "  no lineage number to carry and none was invented. V10 follows",
          "  NEW PUBLIC V9 and V11 follows NEW PUBLIC V10.",
          "", hr(), "", "ORDER OF AUTHORITY", "",
          "  1  FINAL story-led recording script",
          "        Spoken wording, title, thumbnail, framework, section",
          "        order, CTA and Watch Next wording, and the claim",
          "        boundaries the script itself carries.",
          "",
          "  2  Thought-Block Recording Copy",
          "        A recording-format derivative of the script above. It",
          "        carries the same spoken wording exactly and in order.",
          "        Where the two disagree the script wins; QA reports",
          "        rather than repairs, and no discrepancy was found.",
          "",
          "  3  Advisor and Code Handoff",
          "        Production architecture, visual language, resource",
          "        mapping, Shorts strategy and boundaries. It does not",
          "        control spoken wording.",
          "", hr(), "", "SOURCE FILES", ""]
    for nm, sha in sources:
        L += ["  %s" % nm, "      sha256  %s" % sha, ""]
    lo, hi = S.estimate(n)
    L += [hr(), "", "SPOKEN SCRIPT", "",
          "  %d sections, %d spoken paragraphs, %s spoken words."
          % (len(S.sections(n)), len(S.paragraphs(n)),
             format(S.word_count(n), ",")),
          "  Arithmetic estimate %s to %s at 130 to 145 words per minute."
          % (lo, hi),
          "  That is arithmetic on the script. It is not a runtime, a",
          "  chapter, a Riverside time or an SRT time.", "",
          "  Thought-block match: %s" % S.blocks_match(n)[1], "",
          hr(), "", "LOCKED PACKAGING", "",
          "  TITLE      %s" % S.title(n),
          "  THUMBNAIL  %s" % S.thumbnail(n),
          "  WATCH NEXT %s" % S.watch_next(n), "",
          hr(), "", "THREE CANDIDATE SHORTS", ""]
    for r in SH.rows(n):
        L += ["  SHORT %d  %s" % (r["num"], r["title"]),
              "      %d words. Every line is a whole sentence lifted" % r["words"],
              "      verbatim from this video's spoken script. No Short",
              "      wording was invented, and the bank is three, not six.",
              ""]
    return mono(path, L)


def claim_notes(n, path, stamp):
    d = base_doc()
    title_block(d, EYEBROW, S.title(n), "Claim-boundary notes")
    kv(d, "New public number", "V%d" % n)
    kv(d, "Former roadmap number", "None. This is a new concept.")
    kv(d, "Generated", stamp)
    para(d, "Each row is a boundary the video keeps and where the package "
            "keeps it. A boundary is not a disclaimer to be cut for pace: "
            "in both of these videos it is part of the teaching.", size=11)
    table(d, ["The boundary", "What the script says",
              "Where the package keeps it"],
          [[a, b, c] for a, b, c in BOUNDARIES[n]],
          widths=[1.4, 2.3, 3.0], size=8)
    h(d, "Research and evidence in this video")
    para(d, EVIDENCE_NOTE[n], size=10.5)
    h(d, "Never, in either video")
    bullets(d, NEVER)
    footer_note(d, "Both videos are new concepts. No former-roadmap number "
                   "exists for either and none was invented.")
    d.save(path)
    return path
