# -*- coding: utf-8 -*-
"""Source hierarchy, evidence notes and claim-boundary notes."""
import sprint as S
import frames as F
from sdocs import (base_doc, title_block, h, kv, para, callout, sub, caption,
                   table, bullets, footer_note, mono, hr, head, _wrap,
                   EYEBROW)

# The editorial boundary each video must keep, from the build brief and the
# script itself. Nothing here is invented: each is stated or protected in the
# spoken script.
BOUNDARIES = {
 4: [("Not anti-AI", "The video does not claim AI always removes learning, "
      "always damages capability, or automatically eliminates developmental "
      "experience.",
      "The script says some work should disappear, some automation gives "
      "people time for better work, and some tools can teach faster. Those "
      "lines are not cut."),
     ("No single outcome", "Different jobs answer this differently.",
      "In some work AI may increase learning. In regulated or high-risk "
      "work human review may remain essential. In others the task may truly "
      "disappear. The script refuses one outcome and so does the package."),
     ("Not a job-loss prediction",
      "AI taking the task is not the same as AI taking the job.",
      "That sentence is on a card. No card or Short turns the video into a "
      "prediction about employment.")],
 5: [("Being needed is not bad", "Usefulness can be real security.",
      "The script says sometimes it is. Nothing implies that being relied "
      "on is inherently a problem."),
     ("No employer obligation", "Employers do not owe a custom career path.",
      "The script says so directly. Nothing implies an automatic promotion "
      "is owed."),
     ("The manager is not the villain",
      "That does not mean they are plotting against you.",
      "The line is on a card, not only on camera."),
     ("The answer may be no", "Budget, openings, bias and company shape.",
      "The boundary card lists them and calls the answer information.")],
 6: [("The sample", "15 postings from 11 employers, read for this research.",
      "Never representative of the labor market, never a claim that titles "
      "are meaningless or never matter."),
     ("The ceiling claim", "Highest published ceiling in the sample.",
      "Never highest in the market. The words stay on screen with the "
      "figure."),
     ("Bounded decisions", "A senior role described in bounded-decision "
      "language.",
      "The posting establishes predefined decisions. It does not establish "
      "who created them, and nothing says otherwise. The defense of the "
      "role stays in."),
     ("The real gap", "A real gap is not always a skill gap.",
      "The geographic boundary and the three-hour overlap are both stated "
      "in one posting. No local meeting time is stated or implied."),
     ("What the method does", "It gives you a cleaner read.",
      "Reading better does not guarantee a better outcome. That sentence "
      "is not cut, softened or moved."),
     ("The ten-minute promise", "The promise stays real.",
      "No spoken material was added, the script was not expanded, no "
      "editor narration was introduced, and there is no second spoken "
      "CTA.")],
 7: [("Not merit alone", "Careers do not happen in a vacuum.",
      "Bias, relationships, manager support and access to developmental "
      "work are named on a card, and the script's refusal to reduce this "
      "to merit is on the same card."),
     ("Not a formula", "Four things tend to matter.",
      "The card carries 'not a guaranteed formula, a way to read what may "
      "be happening' from the first frame."),
     ("The organization may say no",
      "Politics, bias, favoritism, timing, budget, headcount, a manager "
      "who does not advocate.",
      "All six are on a card. The video does not promise the opportunity."),
     ("Temidayo is warrant, not destination",
      "Her experience is why she can read the room.",
      "No card says why she succeeded. The viewer stays the subject.")],
 8: [("Keep the proof, not the property", "The ethical rule of the video.",
      "No card depicts a file, a screenshot, a download, an internal "
      "system, or any circumvention of access control."),
     ("Lawful record only",
      "Do not forward confidential documents, copy customer data, or take "
      "proprietary reports, source code or internal financials.",
      "The script lists these and the package never illustrates them."),
     ("Reconstructed examples", "In your own words.",
      "The capture examples are the script's own placeholder sentences. No "
      "real or fabricated employer record appears anywhere."),
     ("Evidence is not a guarantee",
      "Good evidence will not remove every hiring problem.",
      "A future employer can still discount the experience or require a "
      "credential. That card is in the set.")],
 9: [("Not anti-transferability", "The question is incomplete, not wrong.",
      "The card says 'not wrong, incomplete' and the video gives "
      "transferable-skills advice its due before complicating it."),
     ("The full audit", "All four questions.",
      "The establish card shows all four together before any one is "
      "activated, and the closing card shows all four again."),
     ("Real gates stay real",
      "Regulation, credentials, domain knowledge, customer knowledge, "
      "technical depth, local relationships.",
      "Named on a card, with the script's line that they are not insults "
      "to the viewer's experience."),
     ("What does not disappear",
      "Employer preference for direct experience, a non-negotiable "
      "credential, bias, compensation reset, a crowded market.",
      "All five are on the boundary card.")],
}

EVIDENCE_NOTE = {
 4: "No employer, posting or research corpus is cited. The junior-analyst "
    "passage is an illustrative scenario the script introduces with "
    "'Think about', not a real person or client.",
 5: "No employer, posting or research corpus is cited. The end-to-end "
    "process passage is an illustrative scenario the script introduces "
    "with 'Imagine', not a real employer.",
 6: "This video carries the researched posting corpus: 15 postings from 11 "
    "employers, captured September 12, 2026, preserved in the Internal "
    "Source Capture Packet. Employers are named on camera as the packet "
    "requires. Every posting card is built from preserved text, never from "
    "a page reopened later.",
 7: "No employer or posting is cited. The video draws on Temidayo's own "
    "experience of seeing larger assignments allocated, which is warrant "
    "for the reading, not a claim about any specific organization.",
 8: "No employer, posting or research corpus is cited. The capture "
    "examples use placeholders the script speaks. The recalled numbers in "
    "the story section are the script's own illustration of forgetting, "
    "not a claim about a real project.",
 9: "No employer, posting or research corpus is cited. The sorting image "
    "and the interview answer are the script's own constructions.",
}


# The internal posting register. Anonymizing the public teaching layer must
# not cost the research its traceability, so every posting shown on a card
# is recorded here against the employer it actually came from. This is the
# named layer, and it stays named.
POSTING_REGISTER = (
 ("Posting one", "Sr Divisional Strategy Consultant, Governance",
  "Health Care Service Corporation (HCSC), requisition R0055598",
  "Large Health Insurer"),
 ("Posting two", "Director of Enterprise Resilience",
  "Health Care Service Corporation (HCSC), same employer as posting one",
  "Large Health Insurer"),
 ("Posting three", "Director, Talent Management", "Zeta Global",
  "Marketing Technology Company"),
 ("Posting four", "Director of Strategic Initiatives",
  "Patriot Growth Insurance Services", "Insurance Brokerage"),
 ("Posting five", "Member of Technical Staff, Governance Risk Compliance",
  "xAI", "AI Company"),
 ("Posting six", "Director of Global Talent Acquisition", "GiveDirectly",
  "A global nonprofit, spoken"),
)


def source_hierarchy(n, path, stamp, zips):
    L = head("NEW V%d  (FORMER ROADMAP V%d)  |  SOURCE MANIFEST AND NUMBER "
             "MAP" % (n, S.NUMBERS[n]))
    L += [S.title(n), "Generated %s" % stamp, "", hr(), "",
          "NUMBER MAP", "",
          "  NEW PUBLIC NUMBER      V%d" % n,
          "  FORMER ROADMAP NUMBER  V%d" % S.NUMBERS[n],
          "",
          "  The former number is retained for traceability and source",
          "  lineage only. It does not control the public publishing order,",
          "  and the historical locked V4 to V21 production archive is a",
          "  separate layer that this sprint does not touch.",
          "", hr(), "", "ORDER OF AUTHORITY", "",
          "  1  FINAL sprint script",
          "        Spoken wording, new and former number, title, thumbnail,",
          "        section order, long-form CTA, spoken Watch Next wording,",
          "        three candidate Shorts, and the claim boundaries the",
          "        script itself carries.",
          "",
          "  2  Thought-Block Recording Copy",
          "        A recording-format derivative of the script above. It",
          "        carries the same spoken wording exactly. Where the two",
          "        disagree the script wins; QA reports rather than",
          "        repairs, and no discrepancy was found.",
          "", hr(), "", "SOURCE FILES", ""]
    for nm, sha in zips:
        L += ["  %s" % nm, "      sha256  %s" % sha, ""]
    L += ["  %s" % S.read(n)["file"],
          "      sha256  %s" % S.read(n)["sha"], "",
          "  %s" % S.block_path(n).split("/")[-1],
          "      sha256  %s" % S.sha256(S.block_path(n)), "",
          hr(), "", "SPOKEN SCRIPT", "",
          "  %d sections, %d spoken paragraphs, %s spoken words."
          % (len(S.sections(n)), len(S.paragraphs(n)),
             format(S.word_count(n), ",")),
          "  Arithmetic estimate %s to %s at 130 to 145 words per minute."
          % S.estimate(n),
          "  That is arithmetic on the script. It is not a runtime, a",
          "  chapter, a Riverside time or an SRT time.", "",
          "  Thought-block match: %s" % S.blocks_match(n)[1], "",
          hr(), "", "LOCKED PACKAGING", "",
          "  TITLE      %s" % S.title(n),
          "  THUMBNAIL  %s" % S.thumbnail(n),
          "  WATCH NEXT %s" % S.watch_next(n), "",
          hr(), "", "THREE CANDIDATE SHORTS", ""]
    for sh in S.shorts(n):
        L += ["  SHORT %d  %s" % (sh["num"], sh["hook"]),
              "      %d words. Supplied inside the FINAL sprint script and"
              % len(sh["body"].split()),
              "      reproduced word for word. Not part of the spoken",
              "      long-form script.", ""]
    return mono(path, L)


def claim_notes(n, path, stamp):
    d = base_doc()
    title_block(d, EYEBROW, S.title(n), "Claim-boundary notes")
    kv(d, "New public number", "V%d" % n)
    kv(d, "Former roadmap number", "V%d" % S.NUMBERS[n])
    kv(d, "Generated", stamp)
    para(d, "Each row is a boundary the video keeps and where the package "
            "keeps it. A boundary is not a disclaimer to be cut for pace: "
            "in every one of these videos it is part of the teaching.",
         size=11)
    table(d, ["The boundary", "What the script says", "Where the package "
                                                      "keeps it"],
          [[a, b, c] for a, b, c in BOUNDARIES[n]],
          widths=[1.4, 2.3, 3.0], size=8)
    h(d, "Research and evidence in this video")
    para(d, EVIDENCE_NOTE[n], size=10.5)
    if n == 6:
        h(d, "Internal posting register")
        para(d, "The public teaching layer carries a generic label instead "
                "of an employer name. The research stays fully traceable "
                "here. These are real captured postings, not synthetic "
                "examples, and this register records exactly which "
                "employer each one came from.", size=10.5)
        table(d, ["", "Role as posted", "Employer, internal",
                  "Public label"],
              [[a, b, c, e] for a, b, c, e in POSTING_REGISTER],
              widths=[0.8, 2.2, 2.2, 1.5], size=7.5)
        caption(d, "Internal record. Never display copy. Captured "
                   "September 12, 2026. 15 postings across 11 employers; "
                   "the six above are the ones a card shows.")
    h(d, "Never, in any sprint video")
    bullets(d, [
      "No invented research, employer behavior, personal experience or "
      "outcome.",
      "No invented runtime, public URL, upload date, thumbnail result, "
      "retention figure or music license.",
      "No chapters and no SRT timing before the final edit.",
      "No recruiter tips, resume hacks, workplace outrage, generic career "
      "advice, AI-tool tutorial or job-loss prediction.",
    ])
    footer_note(d, "The public promise: help experienced professionals make "
                   "career pivots and internal moves without starting over.")
    d.save(path)
    return path
