# -*- coding: utf-8 -*-
"""Source, provenance and evidence boundaries for V1, V2 and V3."""

SOURCES = {
1: dict(master="V1_FINAL_Sticky_Realization_Recording_Master.docx",
        master_sha="3d2fae1d7a79d145d959cb33bf9c553241f95b770ac600622a9b9cc98fa186b6",
        master_size="39,521 bytes",
        blocks="V1_FINAL_Sticky_Realization_Thought_Blocks.docx",
        blocks_sha="f5499eb9df8317a3d39c080927b1c840e4839055118f32cf0460ea38f59379be",
        blocks_size="39,820 bytes"),
2: dict(master="V2_FINAL_Sticky_Realization_Recording_Master.docx",
        master_sha="3fc351e9d481e6eb20d1a78ebdbde16c034a7d10daf1f94b99edd53834d353f7",
        master_size="39,495 bytes",
        blocks="V2_FINAL_Sticky_Realization_Thought_Blocks.docx",
        blocks_sha="34d6ee0956be2ca37a4f35407aed1702a308c2c0eaeb989fbaa86665461a46e2",
        blocks_size="39,773 bytes"),
3: dict(master="V3_FINAL_Sticky_Realization_Recording_Master.docx",
        master_sha="4500a3a0ab7a005abf8595cf7c76bf9faa25e9901a1f021fb96fcf528f46f139",
        master_size="39,490 bytes",
        blocks="V3_FINAL_Sticky_Realization_Thought_Blocks.docx",
        blocks_sha="8ff72c32e738ef71d18d224cb6a6d949e9d9ca601cdb6927094b1c8fd3e1d00e",
        blocks_size="39,781 bytes"),
}

SOURCE_NOTE = ("Uploaded by Temidayo on September 23, 2026 and named as the new "
               "spoken source of truth, superseding the earlier refreshed "
               "V1-V3 masters and their thought blocks. The spoken wording in "
               "this pack is read out of these documents at build time and is "
               "never retyped, so a diff against the upload is a byte "
               "comparison rather than a proofread.")

# The one place the source documents needed a mechanical repair.
FUSED_LABELS = [
 (2, "READ THE LAST 90 DAYS",
  "Then look at the last 90 days of your actual work.",
  "In both the master and the thought-block file, this section label runs "
  "straight into the first spoken sentence with no paragraph break. The label "
  "is not spoken, so it is separated here. No spoken word was changed, added "
  "or removed. The word count moves from 892 to 888 only because five label "
  "tokens stop being counted as speech."),
 (3, "KEEP THE PROOF, NOT THE PROPERTY",
  "So here is the rule: keep the proof, not the property.",
  "The same fusion, in both V3 documents. Separated the same way. The word "
  "count moves from 928 to 923 for the same reason."),
]

# V1's artifact. Anonymized in public, and the private fields are still empty.
ROLES = [
 ("ROLE A / CURRENT", "Senior Manager, Program Management",
  "NOT SUPPLIED", "NOT SUPPLIED"),
 ("ROLE B / DESTINATION", "Director, Enterprise Transformation",
  "NOT SUPPLIED", "NOT SUPPLIED"),
]

ROLES_NOTE = ("Anonymized role types based on two real U.S. postings used in "
              "the flagship research. Company names stay private and do not "
              "appear in any public asset in this pack. The employer names and "
              "source URLs are still NOT IN THIS WORKSPACE: they were not "
              "supplied with any prompt and they appear in no master, no "
              "thought-block file and no earlier package. They were not "
              "invented. Before publishing, both roles need an employer, the "
              "exact advertised title, and a source URL with a collection date "
              "and capture route. Until then the on-slide line “two real "
              "U.S. job postings” rests on the brief's own statement and "
              "not on a record anyone can re-check.")

# Constructed teaching examples. Every one carries a label on the card.
CONSTRUCTED = [
 (2, "V2_02_THE_SENTENCE", "A resume sentence: I own the QBR process for this "
     "business unit.",
     "Written for this video. It is not anyone's real resume and not an "
     "employer's words. The master introduces it with “Imagine this "
     "sentence on a resume”, so it is named as an example on camera."),
 (2, "V2_04_UNDERNEATH", "The same claim with the company nouns removed.",
     "A teaching example from the script, not an employer claim. The master "
     "hedges it out loud with “Maybe the real work is”."),
 (3, "V3_06_THE_LINE", "A line as most people write it: I reduced the time an "
     "internal process took.",
     "Written for this video. The master introduces it with “Suppose you "
     "write”."),
 (3, "V3_07_THE_WORK", "The same example reconstructed.",
     "A teaching example. The master hedges it out loud with “Maybe the "
     "real work was”."),
]

BOUNDARIES = {
1: ["Adjacent experience is never turned into direct experience. The four-column "
    "read keeps a separate column for what may need to be learned or built, and "
    "the word MAY is preserved on the card and in the spoken line.",
    "The destination-context items are never called hard requirements. They are "
    "described as what the destination role is built around.",
    "No claim that the viewer is qualified, and no claim that an employer will "
    "recognize the experience. The boundary section says out loud that a posting "
    "cannot tell anyone how a hiring manager will weigh adjacent experience.",
    "No employer name and no source URL appears in any public asset."],
2: ["No implication that value inside a company is fake. The master calls it real "
    "value in the first thirty seconds and the description repeats that.",
    "No implication that marketability decides whether somebody should leave. Pay, "
    "caregiving, health, timing, immigration, location and the market are named in "
    "the spoken master as real constraints.",
    "The pattern card is four described situations. It is not a score, nothing is "
    "ranked, no quadrant is tinted as the good one, and the card says so in its own "
    "footer.",
    "No implication that translation alone fixes a real gap. The master says "
    "explicitly that translation alone is not enough either."],
3: ["Keep the proof, not the property. Confidential information, customer or "
    "employee data, proprietary documents and employer-owned material are named "
    "on camera as staying with the employer.",
    "The safety boundary is spoken early and concisely: if health or safety is at "
    "risk, or there is harassment, discrimination or another urgent threat, this "
    "video is not a reason to delay leaving.",
    "Preservation is never presented as legal advice, and perfect documentation is "
    "never presented as a requirement before leaving.",
    "The capability claim is kept narrow on camera. The master refuses the jump "
    "from one project to “I can transform any organization”."],
}

DESCRIPTIONS_NOT_SUPPLIED = (
 "The refresh brief says to use the supplied refreshed descriptions as the "
 "publishing base. No description document was supplied, with either prompt or "
 "with the Sticky Realization upload. The descriptions in this pack were "
 "therefore written from the FINAL masters: every claim in them is something "
 "the video says out loud, the resource is the one the master names, and the "
 "Watch Next is the one the master routes to. They are marked CONSTRUCTED FROM "
 "THE RECORDING MASTER on the page itself and need approval before publishing.")

SCRIPTURE = ("NLT WORDING REQUIRES VERIFICATION. No authorized New Living "
             "Translation text exists anywhere in this workspace, so the three "
             "verses in the description pack could not be checked against one. "
             "They are recorded as intended references. This does not block the "
             "build; it blocks publishing until each verse is confirmed.")

URLS = ("Three URLs appear: career-evidence-starter (V1 and V2) and "
        "career-decisions (V3). Both are carried forward from the shipped "
        "packages and were NOT re-fetched in this pass. No URL was invented, "
        "and no URL is spoken on camera in any of the three videos.")

LIMITS = [
 "No new research was conducted. Nothing in this pack rests on anything outside "
 "the supplied masters, the supplied thought blocks, the two prompt documents "
 "and the approved flagship visual package already in the workspace.",
 "Runtime is arithmetic on the word count at a stated words-per-minute rate. "
 "Nothing was measured, because no footage exists.",
 "The employer names and source URLs behind V1's two roles are still missing "
 "and are recorded as missing rather than filled in.",
]
