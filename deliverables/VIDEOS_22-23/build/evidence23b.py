# -*- coding: utf-8 -*-
"""Source and evidence notes, and claim-boundary notes, for the new scripts.

Provenance still comes from the Internal Source Capture Packet, which remains
the authority for how a source is presented, anonymized and bounded. What
changed is which sources the current spoken script uses: the V23 same-company
comparison is gone from the video, so it is recorded here as archived
evidence rather than as an active production source.
"""
import masters23b as M
from docs23 import (base_doc, title_block, h, kv, para, callout, sub, caption,
                    table, bullets, footer_note, mono, hr, head)

ACTIVE = {
 22: [
  ("A1", "Health Care Service Corporation",
   "Sr Divisional Strategy Consultant, Governance",
   "$61,500 to $136,100",
   "Named on camera. Highlight order: the published floor, then the ability "
   "to accept direction and feedback, then the verb supporting."),
  ("A2", "Health Care Service Corporation",
   "Director of Enterprise Resilience", "$133,400 to $247,700",
   "Named on camera, and the viewer must hear it is the same employer as A1. "
   "The posting establishes predefined decisions. It does not establish who "
   "created them, and nothing on camera or on screen may say otherwise."),
  ("A3", "Zeta Global", "Director, Talent Management",
   "$135,000 to $145,000",
   "Named on camera. Paired with A4 in one comparison. No compensation "
   "comparison is drawn: the new script does not make one."),
  ("A4", "Patriot Growth Insurance Services",
   "Director of Strategic Initiatives", "$200,000 to $250,000",
   "Named on camera. Paired with A3. The two are compared on scope, "
   "reporting relationship and authority, not on pay."),
  ("A5", "xAI", "Member of Technical Staff, Governance Risk Compliance",
   "$180,000 to $440,000 base",
   "Named on camera. The acronym density is shown as captured, unedited, so "
   "it registers before the reversal. The range is revealed after the four "
   "postures, and the ceiling claim stays bounded to the sample."),
  ("A6", "GiveDirectly", "Director, Global Talent Acquisition (Remote)",
   "Fixed United States base of $128,000",
   "Named on camera, in the past tense. Two constraints are shown: the "
   "geographic boundary and the overlap requirement. The posting states the "
   "overlap; no local meeting time is stated or implied on screen."),
 ],
 23: [],
}

ARCHIVED = {
 23: [("B1", "Mercury", "Senior Product Manager, Cards Experience",
       "$173,600 to $204,200"),
      ("B2", "Mercury", "Senior Product Manager, Personal Banking",
       "$203,100 to $238,900")],
}

BOUNDARIES = {
 22: [
  ("The sample", "15 postings from 11 employers, read for this research.",
   "Never: representative of the labor market, how all employers write "
   "roles, that titles are meaningless, or that titles never matter."),
  ("The ceiling claim", "Highest published ceiling in the sample.",
   "Never: highest in the market. The words in the sample stay on screen "
   "with the figure."),
  ("The two Director roles", "Two different industries, roughly the same "
   "experience minimums, different work and authority.",
   "No compensation comparison is drawn and none may be added. The new "
   "script does not make one."),
  ("Bounded decisions", "A Director role describing decisions made against "
   "predefined decisions.",
   "The script describes a serious role under pressure and the video must "
   "too. Nothing visually mocks the role, and nothing claims another person "
   "wrote the predefined decisions."),
  ("The real gap", "A real gap is not always a skill gap.",
   "The geographic boundary and the three-hour overlap are both stated in "
   "one posting. No local meeting time is stated or implied, on screen or "
   "in any Short."),
  ("What the method does", "It gives you a cleaner read.",
   "The script says reading better does not guarantee a better outcome. "
   "That sentence is not cut, softened or moved."),
 ],
 23: [
  ("The example", "Three depots, 71 percent, 89 percent, seven months, 18 "
   "percent.",
   "Synthetic. Not Temidayo's experience, not a client case, not an employer "
   "example, and not one of the researched postings. The label SYNTHETIC "
   "EXAMPLE is on screen wherever a synthetic figure is, including in any "
   "Short or clip."),
  ("The research", "In the job postings I reviewed, employers often asked "
   "for more than outcomes.",
   "Stated exactly as the script states it. No denominator claim is made: "
   "the nine-of-fifteen figure is not in the new script and does not appear "
   "in any active production material."),
  ("Authority", "Several senior roles in the postings clearly described "
   "support or execution postures.",
   "Nothing may imply that formal authority equals value or that execution "
   "means no judgment. The card states the boundary explicitly."),
  ("The catch", "Another employer may still require domain knowledge, a "
   "credential, regulated experience, or direct exposure.",
   "Better proof does not remove a real requirement. Change the emphasis, "
   "not the truth. The closing line is not cut."),
  ("The archived comparison", "The same-company posting pair.",
   "Retired from the active edit. The new script does not use it. No "
   "employer-derived comparison appears in the video or in any Short, and "
   "the employer stays unnamed wherever the evidence is referenced."),
 ],
}


def source_notes(n, path, stamp):
    d = base_doc()
    title_block(d, "capability formation | v%d" % n, M.title(n),
                "Source and evidence notes")
    kv(d, "Capture date", M.CAPTURE_DATE)
    kv(d, "Authority", "Internal Source Capture Packet")
    kv(d, "Generated", stamp)
    callout(d, "The URL is not the asset. Every production visual is built "
               "from the preserved text in the capture packet, never from a "
               "page reopened on shoot day. Where a URL appears in frame, "
               "the visual carries CAPTURED %s." % M.CAPTURE_DATE.upper())
    if ACTIVE[n]:
        h(d, "Sources used on camera")
        table(d, ["Ref", "Employer", "Exact title", "Published compensation"],
              [[a, b, c, dd] for a, b, c, dd, _ in ACTIVE[n]],
              widths=[0.5, 1.9, 2.5, 1.8], size=8.5)
        h(d, "Presentation rules, per source")
        for ref, emp, ttl, comp, note in ACTIVE[n]:
            sub(d, "%s  %s" % (ref, ttl))
            para(d, note, size=10.5)
    else:
        h(d, "Sources used on camera")
        para(d, "None. The new script cites the research in bounded prose "
                "and shows no employer posting on screen.", size=10.5)
    if ARCHIVED.get(n):
        h(d, "Archived evidence, not used in this video")
        para(d, "The previous script compared two postings from one "
                "employer. The new script does not, so this evidence is "
                "retired from the active production layer and preserved here "
                "for traceability only. The anonymization rule still "
                "applies: the employer is not named, shown or styled "
                "anywhere a viewer could see it.", size=10.5)
        table(d, ["Ref", "Employer (internal only)", "Exact title",
                  "Published compensation"],
              [[a, b, c, dd] for a, b, c, dd in ARCHIVED[n]],
              widths=[0.5, 1.9, 2.5, 1.8], size=8.5)
    h(d, "Where the packet and the script differ")
    para(d, "The capture packet quotes lines from an earlier draft under "
            "'exact lines used in the script'. The September 13 FINAL "
            "story-led script is the wording of record and differs from "
            "those quotations throughout. The evidence itself is unchanged: "
            "the employers, titles, compensation, preserved text and "
            "presentation rules all still govern. This is recorded rather "
            "than resolved, because resolving it would mean editing one of "
            "the two sources.", size=10.5)
    footer_note(d, "If current-source wording later differs from the "
                   "captured packet, flag it. Do not silently update the "
                   "research or rewrite the video.")
    d.save(path)
    return path


def claim_notes(n, path, stamp):
    d = base_doc()
    title_block(d, "capability formation | v%d" % n, M.title(n),
                "Claim-boundary notes")
    kv(d, "Generated", stamp)
    para(d, "Each row is a claim the video makes and the limit that travels "
            "with it. A boundary is not a disclaimer to be cut for pace: in "
            "both videos it is part of the teaching.", size=11)
    table(d, ["What is claimed", "Exactly", "The limit"],
          [[a, b, c] for a, b, c in BOUNDARIES[n]],
          widths=[1.5, 2.2, 3.0], size=8.5)
    h(d, "Never, in either video")
    bullets(d, [
      "That better wording can talk someone around a real requirement.",
      "That all prior experience transfers.",
      "That credentials, regulation, domain knowledge, geography, time-zone "
      "requirements, employer constraints, market conditions, compensation "
      "realities, relationships or bias can be reframed away.",
      "No invented employer intent, market conclusion or personal "
      "experience.",
      "No invented outcome, measured runtime or public URL.",
      "No chapters and no SRT timing before the final edit. No thumbnail "
      "artwork in this package.",
      "No music license is chosen and no performance result is claimed.",
    ])
    d.save(path)
    return path


def hierarchy(path, stamp, prior_sha):
    L = head("V22 AND V23  |  SOURCE HIERARCHY AND MANIFEST")
    L += ["Generated %s" % stamp, "", hr(), "",
          "ORDER OF AUTHORITY", "",
          "  1  Video_22_FINAL_Story_Led_Recording_Script.docx",
          "  2  Video_23_FINAL_Story_Led_Recording_Script.docx",
          "        Title, thumbnail, spoken wording and editorial sequence.",
          "        These supersede the 50CHAR advisor-review scripts the",
          "        previous package was built from.",
          "",
          "  3  V22-V38_Roadmap_Extension_Overview_and_Editorial_Map.docx",
          "        Locked packaging and the runtime map. It does not",
          "        override exact spoken wording.",
          "",
          "  4  Internal Source Capture Packet",
          "        Provenance, employer and posting evidence, research",
          "        boundaries, source presentation, anonymization and the",
          "        synthetic-example rules. Unchanged by this pass.",
          "", hr(), "", "SUPERSEDED. NOT USED AS CURRENT SOURCE.", ""]
    for t in M.SUPERSEDED_TITLES:
        L += ["  Title:     %s" % t]
    for t in M.SUPERSEDED_THUMBNAILS:
        L += ["  Thumbnail: %s" % t]
    L += ["", "  The 50CHAR advisor-review scripts are no longer current",
          "  spoken source. None of the above appears in any active",
          "  production document this build writes, which QA checks rather",
          "  than assumes.",
          "", hr(), "", "PRIOR PACKAGE, PRESERVED", "",
          "  YouTube_V22-V23_FINAL_Production_Packages_2026-09-13.zip",
          "  sha256 %s" % prior_sha,
          "",
          "  Not modified and not overwritten. It is no longer the active",
          "  production handoff.",
          "", hr(), "", "SOURCE FILES, AS SUPPLIED", ""]
    for rel, sha, size in M.manifest():
        L += ["  %s" % rel, "      sha256  %s" % sha,
              "      bytes   %s" % format(size, ","), ""]
    L += [hr(), "", "LOCKED PACKAGING", ""]
    for n in M.VIDEOS:
        L += ["  V%d" % n,
              "      TITLE      %s" % M.title(n),
              "      THUMBNAIL  %s" % M.script_header_thumbnail(n),
              "      WORDS      %s spoken" % format(M.word_count(n), ","), ""]
    L += [hr(), "", "WORD COUNT, AND WHY TWO FIGURES EXIST", "",
          "  The supplied figures are V22 982 and V23 895.",
          "  Whitespace tokenization of the spoken text gives V22 978 and",
          "  V23 895.",
          "",
          "  The V22 difference is fully explained and nothing was changed.",
          "  The script contains exactly four currency figures: $61,500,",
          "  $248,000, $180,000 and $440,000. A counter that separates the",
          "  currency symbol from the numeral counts each as two tokens,",
          "  which is 978 plus 4, or 982. V23 contains no currency figure,",
          "  which is why the two methods agree there exactly.",
          "",
          "  Both figures describe the same unchanged script. No wording was",
          "  altered to make either number work.", ""]
    return mono(path, L)
