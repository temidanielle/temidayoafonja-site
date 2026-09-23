# -*- coding: utf-8 -*-
"""Evidence source of record, evidence classes and per-video provenance for V15 to V22.

The Second-Reader Audit report is the evidence source of record for every structural
claim in this pack. Its own evidence labels are preserved exactly as it wrote them.
Nothing here upgrades one class into another: an Interpretation is not reported as a
Quantitative finding, a Hypothesis is not reported as an Interpretation, and an Unknown
is never filled in.
"""

EVIDENCE_OF_RECORD = dict(
    name="second-reader-market-audit.docx",
    where="Uploaded by Temidayo to this session, September 23, 2026, with the final "
          "roadmap lock instruction. Not committed to the repository.",
    sha="e0584a81853f6dcc456a858fb574cca0ba5e3c519f0c7d1348c852fbd900eeef",
    size="57,556 bytes",
    shape="147 paragraphs, 18 tables. Read in full.",
    note="This is the report the previous roadmap reconciliation recorded as BLOCKING "
         "because it was named as the primary source for V20 to V23 and was not in the "
         "workspace. It is now in the workspace with a checksum, which is what unblocked "
         "the V20 and V22 evidence sections. It is a second-reader audit of a book "
         "market, not a study, and it says so about itself.",
)

# ---- the report's own definitions, quoted from its paragraph 2. These are not my labels.
CLASS_DEFINITIONS = [
 ("Observed", "directly supported by a cited source"),
 ("Quantitative", "a measured figure from a named dataset"),
 ("Qualitative", "language or cases, useful for meaning but silent on prevalence"),
 ("Interpretation", "my reasoning connecting evidence"),
 ("Hypothesis", "a proposition needing a test"),
 ("Unknown", "I could not establish it, and I say “insufficient evidence” rather "
              "than filling the gap"),
]

CLASS_NOTE = ("Those six definitions are the report's, written in its own voice. They are "
              "reproduced here unchanged so that the class attached to each claim below "
              "can be checked against the source rather than against my summary of it.")

# ---- every claim this pack takes from the report, with the class the REPORT gave it.
# spoken: the video that says it out loud. None means recorded but not spoken anywhere.
CLAIMS = [
 dict(id="C1",
      claim="Middle managers made up 29% of layoffs in 2024 against a 2018-2022 average "
            "of 22%, and openings for middle-management roles fell by more than 40% "
            "after 2022.",
      source="Korn Ferry, citing Live Data Technologies and Revelio Labs.",
      report_class="Quantitative",
      spoken=[20, 22],
      carried="Spoken in V20 as twenty-nine percent, twenty-two percent and more than "
              "forty percent, and in V22 in the same terms. The attribution is on the "
              "card for the whole hold in both videos."),
 dict(id="C2",
      claim="Gallup reports global manager engagement fell to 22% in 2025, nine points "
            "below 2022, and finds engagement declines as spans of control grow.",
      source="Gallup.",
      report_class="Quantitative",
      spoken=[20, 22],
      carried="V20 says manager engagement has fallen, including as the number of people "
              "reporting to each manager goes up. V22 says the managers who remain are "
              "carrying wider spans, with engagement falling as those spans grow. Neither "
              "video speaks the 22% or the nine-point figure, because two engagement "
              "numbers on top of three layoff numbers is more arithmetic than a viewer "
              "can hold. The direction is spoken; the figures are recorded here."),
 dict(id="C3",
      claim="“Middle management is dying” still overstates the case. “The "
            "next rung is disappearing for many experienced managers” is supported.",
      source="The report's own conclusion on its own data, same paragraph as C1.",
      report_class="Interpretation",
      spoken=[20, 22],
      carried="This is the boundary both videos are built on. V20: it is also not middle "
              "management dying, those roles still exist, people still get them. V22: I "
              "am not going to tell you middle management is dead, the evidence does not "
              "support that. It is spoken as a limit on the numbers, not as a finding of "
              "its own."),
 dict(id="C4",
      claim="Boris Groysberg's study of more than 1,000 star Wall Street analysts found "
            "that stars who changed firms suffered an immediate and lasting performance "
            "decline, because much of their prior excellence depended on the old firm's "
            "resources, colleagues and systems.",
      source="Groysberg, Princeton University Press, as cited by the report.",
      report_class="Quantitative",
      spoken=[18],
      carried="Spoken in V18 as star analysts who moved firms and a performance drop, "
              "with the reason attributed to the old firm's people, systems and support. "
              "The on-card label reads STAR ANALYSTS WHO CHANGED FIRMS. ONE STUDY, ONE "
              "PROFESSION, because that is what it is."),
 dict(id="C5",
      claim="Experience is valued in place and discounted in transit.",
      source="The report's own compression of C4 plus the displacement findings. It "
             "labels this sentence a simpler, stronger statement and marks it "
             "interpretation.",
      report_class="Interpretation",
      spoken=[18],
      carried="V18 speaks it as: experience holds its value in place and loses some of "
              "it in transit. It is spoken as a way of reading the study, immediately "
              "after the study is described, and never as a separate finding."),
 dict(id="C6",
      claim="Workers displaced in mass layoffs lose, in present-value terms, about 1.4 "
            "years of prior earnings when unemployment is low and about 2.8 years when "
            "it exceeds 8%.",
      source="Davis and von Wachter, Brookings 2011, as cited by the report.",
      report_class="Quantitative",
      spoken=[],
      carried="NOT SPOKEN ANYWHERE IN THIS PACK. It was considered for V17 and left out. "
              "V17 is addressed to somebody who has just been laid off or is about to be, "
              "and a present-value earnings penalty is true, old, and of no use to them "
              "in that week. Recorded here so the decision is visible."),
 dict(id="C7",
      claim="Since generative AI's spread, employment of 22-to-25-year-olds in AI-exposed "
            "occupations has fallen to 19% below trend, while experienced workers show no "
            "comparable gap, and the decline runs mainly through reduced hiring of the "
            "young.",
      source="Brynjolfsson, Chandar and Chen, August 2026 payroll study, as cited by the "
             "report.",
      report_class="Quantitative",
      spoken=[15],
      carried="V15 speaks the direction without the figure: in the work that is most "
              "exposed to these tools, it is early-career employment that has softened, "
              "while experienced people have held steadier. The 19% is not spoken, "
              "because V15 uses this only to refuse a claim (that AI is taking your "
              "value), and a refusal does not need a decimal."),
 dict(id="C8",
      claim="Skills-based hiring, as a lever, is contradicted by implementation data: the "
            "practice changed fewer than 1 in 700 hires in 2023, and 45% of firms that "
            "removed degree requirements changed nothing.",
      source="Burning Glass Institute and Harvard Business School, as cited by the report.",
      report_class="Quantitative",
      spoken=[],
      carried="NOT SPOKEN ANYWHERE IN THIS PACK. No video in V15 to V22 makes a "
              "skills-based-hiring claim, so nothing needed this correction. Recorded "
              "because it is the reason none of these eight videos tells a viewer that "
              "dropping a degree requirement opens a door."),
 dict(id="C9",
      claim="Across the three books readable in depth, the most repeated review complaint "
            "is that the book assumes a privileged, mobile, early-career or elite reader "
            "and ignores money, family obligations, location and age.",
      source="Goodreads and Amazon review reading, three titles.",
      report_class="Qualitative",
      spoken=[19, 20, 21, 22],
      carried="This is not spoken as a finding. It is the reason four of the eight videos "
              "carry an explicit constraint paragraph: V19 on authority you cannot award "
              "yourself, V20 on caregiving, health, immigration status and household "
              "risk, V21 on compensation, V22 on timing and life. Qualitative evidence is "
              "used here to decide what to include, never to assert prevalence."),
 dict(id="C10",
      claim="Manager-to-individual-contributor moves, wider spans and megamanager roles "
            "appear in forums and trade press.",
      source="Forum and trade-press observation.",
      report_class="Qualitative, with volume and trajectory recorded as Unknown",
      spoken=[22],
      carried="V22's constructed chart shows two former senior managers now individual "
              "contributors with large scopes. It is labelled a constructed example on "
              "screen and in the script, precisely because this class of evidence cannot "
              "support a claim about how common the pattern is."),
 dict(id="C11",
      claim="Accumulated experience becomes simultaneously valuable and harder to move, "
            "explain, prove or have recognized when context changes.",
      source="The report's Section 8, stated as the hypothesis under test.",
      report_class="Hypothesis",
      spoken=[],
      carried="NOT SPOKEN AS A CLAIM ANYWHERE. The report tests it and reports that the "
              "broad version does not survive. No video in this pack asserts that "
              "experience is losing value; V15 explicitly refuses that framing. Recorded "
              "so that a hypothesis is not later mistaken for a finding of the report."),
]

# ---- what the report could not establish. None of this is filled in anywhere.
UNKNOWNS = [
 ("Verified quantitative search demand",
  "Insufficient evidence for every phrase. The only figures are secondhand, from a "
  "Searchbloom analysis reported by Inc., and the year of that data is not stated."),
 ("Google Trends",
  "Not accessible in that pass. No trajectory for any phrase, 2024 to 2026."),
 ("YouTube demand",
  "Insufficient evidence. No autocomplete, query or view data obtained. Whether "
  "experienced-professional questions have YouTube demand separate from early-career "
  "demand is not established."),
 ("Prevalence behind the forum language",
  "Blind and Reddit over-represent technology workers and active job seekers."),
 ("Unit sales for any mid-career title",
  "No BookScan access. Amazon ranks and Goodreads counts are not sales."),
 ("Whether the pattern continues",
  "The report makes no forecast. Neither does any video in this pack."),
]

UNKNOWN_RULE = ("No title, thumbnail, description, tag or spoken line in V15 to V22 makes "
                "a claim about search demand, search volume, trend direction, YouTube "
                "demand or audience size. Every one of those is an Unknown in the source "
                "of record, and an Unknown stays unfilled. Titles in this pack were chosen "
                "for plainness and for match to the spoken teaching, not from keyword data, "
                "because there is no keyword data to choose from.")

# ---- constructed artifacts. Every one carries an on-screen label.
CONSTRUCTED = [
 (15, "V15_FS_02_THE_SUMMARY", "A four-page quarterly business summary.",
      "CONSTRUCTED EXAMPLE. WRITTEN FOR THIS VIDEO.",
      "Written for this video. Not anyone's real work, and no employer is described. "
      "The script says so out loud before the artifact appears."),
 (15, "V15_FS_05_TIMING_AND_ONE_CUSTOMER", "The two things the reviewer checked against "
      "that summary: a timing effect, and one large customer carrying a broad-looking "
      "trend.",
      "CONSTRUCTED EXAMPLE.",
      "Second state of the same constructed artifact. Carries its own label because it "
      "holds on screen separately from the summary card."),
 (19, "V19_FS_02_HESITATION", "An analyst with six years of trusted work who is asked "
      "which of two options the business should take.",
      "CONSTRUCTED EXAMPLE.",
      "Written for this video. Not a client, not a composite of anyone in particular. "
      "The script says this is made up before she is described."),
 (22, "V22_FS_05_OLD_CHART", "A four-level org chart: manager, senior manager, director, "
      "vice president.",
      "CONSTRUCTED EXAMPLE. NOT A REAL EMPLOYER'S ORG CHART.",
      "Made up to show the shape. The script says here is a constructed example, not a "
      "real employer's chart, I made this one up to show the shape."),
 (22, "V22_FS_06_NEW_CHART", "The same chart with the senior manager layer gone and two "
      "former senior managers now individual contributors.",
      "CONSTRUCTED EXAMPLE. NOT A REAL EMPLOYER'S ORG CHART.",
      "Same constructed chart, second state. Carries the same label for its full hold."),
]

CONSTRUCTED_NOTE = ("Five cards across the eight videos are constructed, covering three constructed examples. Every one is "
                    "labelled on the card for the whole hold and named as constructed in "
                    "the spoken master, not only in the description. No artifact in this "
                    "pack is a real document from a real employer, so no anonymization was "
                    "required for any of them.")

# ---- no employer is named publicly anywhere in this pack.
EMPLOYERS = ("No employer is named in any public asset in V15 to V22: not in a script, a "
             "card, a description, a tag, a pinned comment or a Short. No job posting is "
             "read in any of these eight videos, so the situation that produced the V13 "
             "and V14 anonymization patch does not arise here. The only named "
             "organizations anywhere in the pack are the sources of published research, "
             "which are cited on purpose: Korn Ferry, Live Data Technologies, Revelio "
             "Labs, and Gallup, all in V20 and V22, all on the card and in the "
             "description.")

# ---- editorial sources per video.
SOURCES = {
15: [("ROADMAP SOURCE", "V15-V21 x Missing Rung final roadmap reconciliation",
      "deliverables/FINAL_ROADMAP_RECONCILIATION/. Fixed the sequence position, the "
      "Career Evidence Starter CTA and the Watch Next to locked V12."),
     ("EVIDENCE", "second-reader-market-audit.docx",
      "Claim C7 only, used to refuse the AI-is-taking-your-value framing."),
     ("BOUNDARY", "Locked V12",
      "V15 stops at the point where V12 begins. It does not rebuild an accomplishment "
      "on camera; it says which part of one stopped being visible, then routes to V12.")],
16: [("ROADMAP SOURCE", "V15-V21 x Missing Rung final roadmap reconciliation",
      "Fixed the hinge structure, the no-CTA decision, and the Watch Next to V17."),
     ("BOUNDARY", "Locked V5",
      "V16 does not re-teach making work visible. It uses that as one of two branches "
      "and points at it.")],
17: [("ROADMAP SOURCE", "V15-V21 x Missing Rung final roadmap reconciliation",
      "Fixed the Keep the Proof CTA and the Watch Next to locked V13."),
     ("BOUNDARY", "Locked V8",
      "V8 teaches the habit of keeping a record with access. V17 is explicitly the other "
      "situation: no time to build a habit because the window is closing or has closed. "
      "The script names V8 and points to it rather than repeating it.")],
18: [("ROADMAP SOURCE", "V15-V21 x Missing Rung final roadmap reconciliation",
      "Fixed the Field Kit CTA and the Watch Next to V19."),
     ("EVIDENCE", "second-reader-market-audit.docx",
      "Claims C4 and C5. The one-study label on the card comes from the report's own "
      "description of the study's scope."),
     ("BOUNDARY", "Locked V13",
      "V13 answers which parts of experience transfer. V18 does not re-teach that; it "
      "starts after the move has happened and sorts what still has to be rebuilt.")],
19: [("ROADMAP SOURCE", "V15-V21 x Missing Rung final roadmap reconciliation",
      "Fixed the no-CTA decision and the Watch Next to V20."),
     ("BOUNDARY", "Locked V8 and the Learn/Practice/Prove language",
      "The three gaps are never named as a framework, never numbered on a card and "
      "never boxed as a set. The third gap routes to the existing evidence video "
      "instead of re-teaching it.")],
20: [("ROADMAP SOURCE", "V15-V21 x Missing Rung final roadmap reconciliation",
      "Recorded that MR5 is the stronger version of the old V20 and that the old V20 is "
      "absorbed into a future V23. This V20 is the roadmap's V20, not MR5."),
     ("EVIDENCE", "second-reader-market-audit.docx",
      "Claims C1, C2, C3 and C9. The numbers card carries the attribution for its full "
      "hold."),
     ("BOUNDARY", "V22",
      "V20 does not run V22's structural diagnosis. It does not draw an org chart, does "
      "not count the roles above you and does not ask whether the problem is readiness "
      "or structure. It takes the loss apart into what the next role was going to "
      "supply, and stops.")],
21: [("ROADMAP SOURCE", "V15-V21 x Missing Rung final roadmap reconciliation",
      "Fixed the Field Kit CTA and the Watch Next to V22."),
     ("BOUNDARY", "Promotion, title and compensation stay real",
      "The script refuses the titles-are-meaningless move twice, keeps compensation in "
      "the ask, and names the pattern where harder work arrives as a development "
      "opportunity with no money attached.")],
22: [("ROADMAP SOURCE", "V15-V21 x Missing Rung final roadmap reconciliation",
      "Fixed V22 as the structural diagnosis and recorded that it must not route to an "
      "unbuilt V23."),
     ("EVIDENCE", "second-reader-market-audit.docx",
      "Claims C1, C2, C3 and C10."),
     ("BOUNDARY", "Two limits spoken on camera",
      "That this is your organization and not the economy, and that nobody can say "
      "whether the direction continues. Both are spoken, not only written in the "
      "description.")],
}

VIEWER_FACING_SCOPE = (
 "A distinction worth stating, because a reader sweeping this pack for the string V23 will "
 "find it. The rule is that no VIEWER-FACING asset may name or route to an unbuilt video: "
 "that means the recording masters, thought blocks, production packages, Shorts and "
 "descriptions, and the QA item that enforces it checks exactly those five. Provenance "
 "documents are internal records and must be free to name their own sources, so they cite "
 "the roadmap reconciliation by its real title and quote its history, including the "
 "sentence about V20 to V23 that recorded this evidence report as BLOCKING before it "
 "arrived. The same applies to the phrase Missing Rung: it is the roadmap document's name "
 "and appears in provenance as a citation, never as a structure a viewer is shown or told "
 "about.")

SCRIPTURE = ("NLT WORDING REQUIRES VERIFICATION. No authorized New Living Translation text "
             "exists anywhere in this workspace, so the eight verses in the description "
             "pack could not be checked against one. They are recorded as intended "
             "references, not as verified NLT wording. This does not block the build; it "
             "blocks publishing until each verse is confirmed against an NLT edition.")

URLS = ("Three URLs are used: career-evidence-starter (V15), keep-the-proof (V17) and "
        "fieldkit (V18 and V21). All three are carried forward from the locked V12 to V14 "
        "pack and were NOT re-verified against a live site in this pass, because this "
        "session has no reason to fetch them and they are Temidayo's own pages. A fourth, "
        "career-decisions, is recorded in the descriptions module as carried but unused: "
        "no video in V15 to V22 earns it out loud. Career Move Review still has no page "
        "and no URL anywhere in the workspace and is therefore not referenced.")

LIMITS = [
 "The source of record is a second-reader audit of a book market. It is not a labor "
 "study, and its author says so. Its strongest material for this pack is the layoff and "
 "openings data it cites from Korn Ferry, and that data is itself cited, not collected.",
 "Every figure spoken in V20 and V22 is a figure the report quotes from somebody else. "
 "The primary datasets were not opened in this pass. What was verified is that the "
 "report says what this pack says it says, against a checksummed copy.",
 "No new research was conducted for this pack. Nothing in V15 to V22 rests on anything "
 "outside the workspace, the supplied Missing Rung masters and this report.",
 "The Gallup engagement figures are spoken as a direction and not as numbers. That is a "
 "deliberate reduction and it is recorded as one, not presented as the report's own "
 "framing.",
 "Four claims in the report are recorded above as considered and not spoken. They are "
 "listed so that a later pass can see they were read and set aside, rather than missed.",
]
