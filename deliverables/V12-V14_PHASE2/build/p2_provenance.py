# -*- coding: utf-8 -*-
"""Source hierarchy, checksums and posting provenance for V12-V14."""

SOURCES = {
12: [
 dict(role="PRIMARY EDITORIAL SOURCE",
      name="Video_23_FINAL_Story_Led_Recording_Script.docx",
      where="Uploaded by Temidayo with the V22-V38 Locked Roadmap Extension during the Phase 1 audit. Not committed to the repository.",
      sha="d21872db2294794c72a4c835df81353f55690b8a094d874d4996c0a122bb2dbd",
      size="39,597 bytes",
      note="Old roadmap V23, 895 spoken words. Supplied the four questions, the depot example, and the change-the-emphasis boundary. Rewritten for voice, restructured around a visible before and after, and extended with the artifact reaction and the proof-is-not-an-offer boundary."),
 dict(role="SUPPORTING EVIDENCE",
      name="what-really-transfers-research.md",
      where="deliverables/VIDEOS_14-21_FINAL_PRODUCTION/_source/",
      sha="a7eac1a71e2245e34e61267be9e19d8c5e3750a66236da40e78f9715ad3e6421",
      size="69,275 bytes",
      note="Used for exactly one spoken claim: that moving people who do not report to you was one of the most common asks in the senior postings read for this series. Section 6, item 2 of that record names it the most uniformly worded capability in the sample."),
 dict(role="VOICE BENCHMARK",
      name="NEW_V11 Reconciled_Recording_Master.docx",
      where="deliverables/V4-V11_SYNC/PACKAGES/NEW_V11_Synchronized_Production_Package/01_RECORDING/",
      sha="not re-hashed; read for cadence only",
      size="1,289 spoken words",
      note="Read to match section architecture and spoken cadence. No wording was copied."),
],
13: [
 dict(role="PRIMARY EVIDENCE SOURCE",
      name="what-really-transfers-research.md",
      where="deliverables/VIDEOS_14-21_FINAL_PRODUCTION/_source/",
      sha="a7eac1a71e2245e34e61267be9e19d8c5e3750a66236da40e78f9715ad3e6421",
      size="69,275 bytes, 13 sections",
      note="Every count, every posting quotation and every limitation in V13 comes from this record. Sections used: 2 (opening), 3 (sample), 5 (exclusion log), 6 (real overlap), 7 (failed overlap), 8 (what does not travel), 9 (hard vs preferred), 10 (readable / observable / gated), 11 (second-pass check), 12 (limitations)."),
 dict(role="PRIMARY EDITORIAL SOURCE",
      name="Approved_Recording_Master_Reference.docx (old V14)",
      where="deliverables/VIDEOS_14-21_FINAL_PRODUCTION/VIDEO_14_FINAL_PRODUCTION_PACKAGE/01_Recording_Master/",
      sha="aa452c9746eeb8f8a224a1934ad0d3d127fdad5ed84bd3a1846bb0dc7c752b9b",
      size="42,422 bytes",
      note="Supplied the same-words-different-work spine and the what-not-to-claim discipline. Its four named buckets were deliberately NOT carried across as a framework; the same distinctions now run through the analysis without labels."),
],
14: [
 dict(role="PRIMARY EDITORIAL SOURCE",
      name="Video_31_FINAL_Story_Led_Recording_Script.docx",
      where="Uploaded by Temidayo with the V22-V38 Locked Roadmap Extension during the Phase 1 audit. Not committed to the repository.",
      sha="b054de52ebe53785f07cb014598817a57e217a2d4aebf764baf6214d2664c0de",
      size="39,217 bytes",
      note="Old roadmap V31, 694 spoken words. Substantially rebuilt. What survived: the four kinds of similar, and the idea that posting wording carries clues. What was cut: every assertion about what employers or hiring managers believe. The episode is now a read of two specific postings rather than a set of claims about readers."),
 dict(role="PRIMARY EVIDENCE SOURCE",
      name="what-really-transfers-research.md",
      where="deliverables/VIDEOS_14-21_FINAL_PRODUCTION/_source/",
      sha="a7eac1a71e2245e34e61267be9e19d8c5e3750a66236da40e78f9715ad3e6421",
      size="69,275 bytes",
      note="Rows H10 and F5 supply both postings. Section 11 of that record independently names this the best single contrast pair in the sample."),
],
}

# Posting rows quoted on camera, with everything needed to re-verify them.
POSTINGS = {
"H10": dict(
  code="H10", employer="Humana",
  title="Senior Project Manager (Risk Adjustment Strategy & Business Support)",
  url="https://jobs.peoria.org/companies/humana/jobs/64551181-senior-project-manager",
  collected="September 10, 2026", posted="Posted January 6, 2026; deadline 01-09-2026",
  location="Remote", capture="Mirror (Getro / Peoria board), full text",
  hard="5+ years of project management — HARD. Bachelor's degree — HARD.",
  preferred="PMP or CAPM — PREFERRED. Lean / Six Sigma — PREFERRED. Risk Adjustment domain knowledge — PREFERRED.",
  quote="“comfortable working on new projects with limited knowledge/expertise of the content and be able to learn quickly”",
  used_in="V13 (first of the three risk clauses) and V14 (posting one)",
  coder="The single clearest posting in the sample disclaiming domain knowledge as a prerequisite."),
"F1": dict(
  code="F1", employer="Wells Fargo",
  title="Senior Lead Project Manager (Wealth & Investment Management Technology)",
  url="https://www.themuse.com/jobs/wellsfargo/senior-lead-project-manager-f39c76 (R-478720)",
  collected="September 10, 2026", posted="Posted 2025-08-13; posting end 15 Aug 2025",
  location="Not restated on camera", capture="Mirror (The Muse), full text",
  hard="5+ years financial industry experience — HARD. 7+ years project management — HARD. 5+ years project financials — HARD. SAFe/Agile full lifecycle 3+ years — HARD.",
  preferred="PMBOK / Agile / Waterfall proficiency — PREFERRED.",
  quote="“execution of all applicable risk programs (Credit, Market, Financial Crimes, Operational, Regulatory Compliance)”",
  used_in="V13 (second of the three risk clauses)",
  coder="The standing enterprise-risk-program accountability is the key apparent-overlap trap for “manage risk.”"),
"H8": dict(
  code="H8", employer="Mass General Brigham",
  title="Senior Project Manager, Center for Disaster Medicine",
  url="https://builtin.com/job/senior-project-manager/7365786 (Workday RQ4038180)",
  collected="September 10, 2026", posted="Built In shows removal December 3, 2025; reposted per index",
  location="Boston, MA (hybrid)", capture="Mirror (Built In), full text",
  hard="ICS/NIMS 100, 200, 700, 800 before or upon hire — HARD. 5–7 years experience — HARD.",
  preferred="Emergency management background — desired, not an industry gate.",
  quote="Regional Disaster Health Response System Duty Officer; patient movement and special-pathogens work during infectious disease surge events",
  used_in="V13 (third of the three risk clauses)",
  coder="Incident-command coursework is readable. Serving as Duty Officer during a real surge is access-gated, supervised practice."),
"F5": dict(
  code="F5", employer="JPMorganChase — J.P. Morgan Wealth Management",
  title="Vice President, CWM Business Project Manager",
  url="https://www.themuse.com/jobs/jpmorganchase/jp-morgan-wealth-management-vice-president-cwm-business-project-manager (JPMorgan-210667842)",
  collected="September 10, 2026", posted="Posted 2025-09-17",
  location="New York", capture="Mirror (The Muse), full text",
  hard="7+ years of experience in the financial services industry — HARD. PowerPoint and Excel — HARD.",
  preferred="Wealth management / Chase business-model knowledge — PREFERRED. Project management background — PREFERRED.",
  quote="“7+ years of experience in the financial services industry”",
  used_in="V14 (posting two)",
  coder="The mirror image of H10. Here the industry is the gate and project management skill is the preference. Best single contrast pair in the sample."),
}

SAMPLE = [
 ("Postings surfaced by search", "~55"),
 ("Postings fetched and evaluated in full", "40"),
 ("Retained", "28"),
 ("Exclusion log entries", "18"),
 ("Retained — healthcare", "10"),
 ("Retained — financial services", "10"),
 ("Retained — technology", "8"),
 ("Collection date (all postings)", "September 10, 2026"),
]

SAMPLE_NOTE = (
 "The four sample numbers are carried exactly as the research record states them. They are not "
 "presented on camera as an arithmetic chain, and they should not be: 40 read in full minus 28 "
 "retained is 12, while the exclusion log carries 18 entries. The difference is in the record "
 "itself. Some log entries bundle several listings from one source (E17 groups three contract "
 "listings; E18 groups non-US health systems) and some rows were excluded at screening rather "
 "than after a full fetch. V13 therefore says “eighteen entries” rather than “eighteen "
 "postings,” which is true of the log as written and avoids asserting a subtraction the record "
 "does not support.")

LIMITS = [
 "It cannot show that any two of these roles are interchangeable, or that a person could move between them.",
 "It cannot show that a hiring manager would waive a stated requirement, or that an adjacent-experience candidate would be interviewed.",
 "It cannot show that the written posting reflects the actual job. Several carried copy-and-paste blocks.",
 "It cannot show that someone would succeed after moving industries.",
 "It says nothing about compensation trajectories or promotion outcomes.",
 "It is not representative of any industry or of the US labor market. 28 postings chosen for accessibility and codability are a convenience sample.",
 "Every count is a count within these 28 postings, not an estimate of any population rate.",
 "Several postings are dated 2025 or early 2026, or were captured from applicant-tracking mirrors rather than live employer pages.",
]
