# -*- coding: utf-8 -*-
"""Source and evidence notes, and the claim-boundary notes.

Provenance comes from the Internal Source Capture Packet, which is the
authority for how a source is presented, anonymized and bounded. Where the
packet quotes the script, it quotes the pre-advisor draft; the wording of
record is the updated script, and that divergence is stated here rather than
resolved by rewriting anything.
"""
import masters23 as M
from docs23 import (base_doc, title_block, h, kv, para, callout, sub, caption,
                    table, bullets, footer_note, page_break, mono, hr, head)

POSTINGS = {
 22: [
  ("A1", "Health Care Service Corporation",
   "Sr Divisional Strategy Consultant, Governance",
   "$61,500 to $136,100", "R0055598",
   "Named on camera. Highlight order: the verb supporting, then the ability "
   "to accept direction and feedback, then the $61,500 floor."),
  ("A2", "Health Care Service Corporation",
   "Director of Enterprise Resilience", "$133,400 to $247,700", "R0054759",
   "Named on camera, and the viewer must hear it is the same company as A1. "
   "The posting establishes predefined decisions. It does not establish who "
   "created them, and nothing on camera or on screen may say otherwise."),
  ("A3", "Zeta Global", "Director, Talent Management",
   "$135,000 to $145,000", "6130327004",
   "Named on camera. Paired with A4 in one comparison. Compensation revealed "
   "last, both together."),
  ("A4", "Patriot Growth Insurance Services", "Director of Strategic "
   "Initiatives", "$200,000 to $250,000", "4363758009",
   "Named on camera. The limit on the $65,000 figure is mandatory and must "
   "follow the reveal immediately."),
  ("A5", "xAI", "Member of Technical Staff, Governance Risk Compliance",
   "$180,000 to $440,000 base", "5007261007",
   "Named on camera. The acronym density is shown as captured, unedited, so "
   "it registers before the reversal. Salary held to the end of the beat."),
  ("A6", "GiveDirectly", "Director, Global Talent Acquisition (Remote)",
   "Fixed United States base of $128,000", "4714132005",
   "Named on camera, in the past tense, so the line holds if the posting "
   "closes. The 7 or 8 a.m. figure is locality-dependent and carries the "
   "Central Time qualifier. The beat runs about 45 seconds."),
 ],
 23: [
  ("B1", "NOT NAMED ON CAMERA", "Senior Product Manager, Cards Experience",
   "$173,600 to $204,200", "employer-hosted board",
   "Anonymized. If posting text appears on screen, the employer name, logo "
   "and URL are cropped or masked. The teaching value is entirely in the "
   "language overlap and the requirement divergence."),
  ("B2", "NOT NAMED ON CAMERA", "Senior Product Manager, Personal Banking",
   "$203,100 to $238,900", "5384125004",
   "Anonymized, same treatment as B1. Presented beside B1 with all employer "
   "identifiers removed."),
 ],
}

BOUNDARIES = {
 22: [
  ("The sample", "Fifteen postings from eleven employers, read in September "
   "2026.",
   "Never: representative of the labor market, how all employers write "
   "roles, that titles are meaningless, or that titles never matter."),
  ("The ceiling claim", "Highest published ceiling in this sample.",
   "Never: highest in the market. The words in this sample stay on screen "
   "with the figure."),
  ("The Director pair", "About $65,000 between these two floors.",
   "Applies only to these two jobs from these two employers. It does not "
   "prove who is more senior, and the boundary card follows the reveal "
   "immediately."),
  ("Execution", "A quarter-million-dollar Director role described in "
   "execution language.",
   "The script defends the role and the video must too. Making the right "
   "call under pressure is hard. Nothing visually mocks the role, and "
   "nothing claims another person wrote the predefined decisions."),
  ("The real gap", "A gap is not always a credential.",
   "The geographic and time-zone constraints are stated in one posting. The "
   "7 or 8 a.m. implication is for someone on Central Time and is never "
   "universalized."),
  ("What the method does", "It improves your aim, not your odds.",
   "The script says reading the posting better does not improve your odds "
   "by itself. That sentence is not cut, softened or moved."),
 ],
 23: [
  ("The example", "Three depots, 71 percent, 89 percent, seven months, 18 "
   "percent.",
   "Synthetic. Not Temidayo's experience, not a client case, not an employer "
   "example, and not one of the researched postings. The label SYNTHETIC "
   "EXAMPLE is on screen wherever a synthetic figure is, including in any "
   "Short or clip."),
  ("The mechanism claim", "Nine of the fifteen job descriptions.",
   "Never: most employers, the market wants, or most jobs require. The "
   "denominator stays visible."),
  ("Authority", "The postings separate govern, negotiate, co-own, recommend, "
   "influence, support and execute.",
   "One role can contain more than one, and none of them is the valuable "
   "one. Nothing may imply that formal authority equals value or that "
   "execution means no judgment."),
  ("The same-company pair", "Same company, same level, near-identical "
   "language, different requirement.",
   "The employer stays anonymous by closed editorial decision. No name, no "
   "logo, no URL, no identifying styling, in the video or in any Short."),
  ("Real gaps", "Sometimes there is a real gap you still have to learn, "
   "earn, or experience.",
   "Better proof does not erase it. The closing line is not cut."),
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
               "the visual carries CAPTURED %s."
               % M.CAPTURE_DATE.upper())
    table(d, ["Ref", "Employer", "Exact title", "Published compensation"],
          [[a, b, c, dd] for a, b, c, dd, _, _ in POSTINGS[n]],
          widths=[0.5, 1.9, 2.5, 1.8], size=8.5)
    h(d, "Presentation rules, per source")
    for ref, emp, title, comp, jid, note in POSTINGS[n]:
        sub(d, "%s  %s" % (ref, title))
        para(d, note, size=10.5)
    h(d, "Where the packet and the script differ")
    para(d, "The capture packet quotes lines from the pre-advisor draft "
            "under the heading 'exact lines used in the script'. The updated "
            "50-character script is the wording of record and differs from "
            "those quotations in places. The evidence itself is unchanged: "
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


def hierarchy(path, stamp):
    L = head("V22 AND V23  |  SOURCE HIERARCHY AND MANIFEST")
    L += ["Generated %s" % stamp, "",
          "Input archive V22_V23_CODE_BUILD_INPUTS_2026-09-13.zip",
          "  sha256  %s" % M.INPUT_ZIP_SHA, "", hr(), "",
          "ORDER OF AUTHORITY", "",
          "  1  V22 UPDATED 50CHAR script document",
          "        V22 title, thumbnail, spoken wording, editorial",
          "        sequence and CTA wording.",
          "",
          "  2  V23 UPDATED 50CHAR script document",
          "        The same, for V23.",
          "",
          "  3  V22-V23 UPDATED Advisor Overview",
          "        Editorial rationale, the distinction between the two",
          "        videos, preserved boundaries and what changed in the",
          "        advisor pass. It does not override exact spoken wording.",
          "",
          "  4  Internal Source Capture Packet",
          "        Provenance, employer and posting evidence, research",
          "        boundaries, source presentation, anonymization and the",
          "        synthetic-example rules.",
          "",
          "  5  Visual reference screenshots",
          "        Information-design principles only. None of their",
          "        branding, color, interface, icons, layout or visual",
          "        identity is used.",
          "", hr(), "", "SUPERSEDED. NOT USED AS CURRENT SOURCE.", ""]
    for t in M.SUPERSEDED_TITLES:
        L += ["  Title:     %s" % t]
    L += ["  Thumbnail: %s" % M.SUPERSEDED_THUMBNAIL,
          "", "  Older Video A and Video B scripts are not current spoken",
          "  source. None of the above appears in any file this build",
          "  writes, which QA checks rather than assumes.",
          "", hr(), "", "INPUT FILES, AS SUPPLIED", ""]
    for rel, sha, size in M.manifest():
        L += ["  %s" % rel, "      sha256  %s" % sha,
              "      bytes   %s" % format(size, ","), ""]
    L += [hr(), "", "LOCKED PACKAGING", ""]
    for n in M.VIDEOS:
        L += ["  V%d" % n,
              "      TITLE      %s" % M.title(n),
              "      THUMBNAIL  %s" % M.thumbnail(n),
              "      WORDS      %s" % format(M.word_count(n), ","), ""]
    return mono(path, L)
