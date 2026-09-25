# -*- coding: utf-8 -*-
"""The approach document for the editorial advisor, covering V4 to V14."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.insert(0, HERE)
sys.path.append(DELIV + "VIDEOS_22-23/build")
sys.path.append(DELIV + "V4-V14_COMPLETE_PACKAGES/build")
from docs23 import (base_doc, title_block, h, kv, para, callout, sub, caption,
                    table, bullets, footer_note, page_break)
import ap_src as A, ap_meta as M

STAMP = "Thursday, September 25, 2026"
EYEBROW = "capability formation youtube | for the editorial advisor"
NAME = "V04-V14_PRODUCTION_APPROACH_FOR_EDITORIAL_ADVISOR.docx"

def build(path):
    d = base_doc()
    title_block(d, EYEBROW, "How Videos 4 to 14 Were Built",
                "The production approach, the rules it followed, and what is "
                "still open")
    kv(d, "Prepared", STAMP)
    kv(d, "Covers", "Videos 4 to 14 of the Capability Formation YouTube "
                    "series")
    kv(d, "Why now", "V4 to V11 have been reopened for the limited editorial "
                     "refresh described in the September 24 audit. This "
                     "document explains what already exists, so the refresh "
                     "changes the script and not the production system around "
                     "it.")
    callout(d, "This is a description of method, not a request for approval "
               "of the scripts. The scripts themselves are the audit's "
               "subject. What follows is how the eleven production packages "
               "were assembled, what was reused rather than made, what the "
               "build refused to do, and the seven questions that are open "
               "and need an editorial decision.")

    # ---------------------------------------------------------------- 1
    h(d, "1. What exists today")
    para(d, "Each of the eleven videos has a complete production package: one "
            "folder, seven sub-folders, thirty-one required artifacts. The "
            "same architecture was piloted on V1 to V3, approved, and then "
            "replicated across V4 to V14. Every required artifact is present "
            "for every video; none is missing and none was silently omitted.")
    table(d, ["Folder", "What it holds"], [
        ["01 Recording", "The locked recording master, the thought blocks, "
                         "the run of show, and an estimated speech timing."],
        ["02 Visuals", "The slide PNGs at 1920 x 1080, the editable source, "
                       "a reference deck, a contact sheet, the asset "
                       "specification, the trigger map, the reveal map, and "
                       "the resource and watch-next cards."],
        ["03 Editor", "Editor master notes, the Riverside prompt, the camera "
                      "emphasis map, B-roll guidance and sound guidance."],
        ["04 Shorts", "Three candidate Shorts and a manifest."],
        ["05 Publishing", "The description, a pinned comment, a publication "
                          "checklist, a thumbnail build prompt and metadata."],
        ["06 Viewer application", "The viewer exercise and the Sticky "
                                  "Realization record."],
        ["07 Evidence and QA", "The source manifest, evidence and "
                               "illustration notes, an alignment log and the "
                               "final QA report."],
    ], widths=[1.5, 5.2])

    # ---------------------------------------------------------------- 2
    h(d, "2. The rule the build followed")
    para(d, "Before any asset was created, the approved material was checked "
            "first. If an approved version existed, it was carried in "
            "unchanged. Only where an operational layer was missing "
            "altogether was anything new made, and then only the operational "
            "layer.")
    bullets(d, [
        "V4 to V11 carry their approved synchronized artwork exactly as "
        "delivered. Nothing was redesigned and nothing was re-rendered.",
        "V12 to V14 had an approved card specification but no delivered "
        "image set. The specification was rendered as written. That is an "
        "operational layer built around approved creative work, not a "
        "redesign of it.",
        "Where a package already held an approved file that the new standard "
        "also generates, both ship. The approved one keeps an _approved_ "
        "prefix so the original is never lost behind the new one.",
    ])
    para(d, "The principle behind this is worth stating plainly for the "
            "refresh: operational incompleteness was never solved by "
            "redesigning approved creative work.")

    # ---------------------------------------------------------------- 3
    h(d, "3. How the spoken word was protected")
    para(d, "The recording master is the source of truth for what is said. "
            "The build reads it and never writes to it. All twenty-two "
            "recording documents, eleven masters and eleven thought-block "
            "copies, ship byte for byte identical to the locked archive. "
            "That was verified by checksum, not assumed.")
    para(d, "Thought-block parity is mandatory and was measured rather than "
            "asserted. The spoken word count of each master matches its "
            "thought-block copy exactly:")
    rows = []
    for n in A.VIDEOS:
        rows.append(["V%d" % n, M.TITLES[n][0][:52],
                     "{:,}".format(A.words(n)), "PASS"])
    table(d, ["Video", "Title", "Spoken words", "Parity"], rows,
          widths=[0.6, 4.0, 1.0, 0.8])

    page_break(d)
    # ---------------------------------------------------------------- 4
    h(d, "4. Visual triggers are exact, never approximate")
    para(d, "Every substantive visual family carries an exact spoken trigger: "
            "the literal sentence, drawn from that video's own master, at "
            "which the visual enters. No cue reads “continues here” "
            "or “around this section.” Across the eleven videos "
            "there are 150 visual families and 150 exact triggers. Each one "
            "was verified as a literal string inside its own recording "
            "master; a trigger that did not appear in the master failed the "
            "build.")
    para(d, "This matters for the refresh. If a spoken sentence changes, any "
            "trigger quoting that sentence has to change with it. The trigger "
            "map in each package names the sentence, so the dependency is "
            "visible rather than buried.")

    # ---------------------------------------------------------------- 5
    h(d, "5. Timing is an estimate and is labelled as one")
    para(d, "No footage exists, so no figure in any package is a runtime. "
            "Every duration is arithmetic on the spoken word count at 130 to "
            "145 words per minute, and every file that carries one says "
            "ESTIMATE. Two titles promise ten minutes and both were checked "
            "specifically.")
    rows = []
    for n in A.VIDEOS:
        note = ""
        if n == 6:
            note = "Title promises 10 minutes. Defensible."
        elif n == 12:
            note = "Title promises 10 minutes. Defensible."
        rows.append(["V%d" % n, "{:,}".format(A.words(n)),
                     A.runtime(n, 145), A.runtime(n, 130), note])
    table(d, ["Video", "Words", "At 145 wpm", "At 130 wpm", "Note"], rows,
          widths=[0.6, 0.8, 1.0, 1.0, 3.0])
    para(d, "The guidance attached to both ten-minute videos is the same: do "
            "not pad the script and do not slow the delivery to reach ten "
            "minutes. If a finished export runs long, the edit is where to "
            "look.")

    # ---------------------------------------------------------------- 6
    h(d, "6. Evidence, employers and boundaries")
    para(d, "No employer name appears in any public-facing artifact. A sweep "
            "across 334 readable files in the eleven packages returned zero "
            "hits against the employer list, and the sweep was proved to fire "
            "by testing it against an injected name.")
    bullets(d, [
        "V13 ships under the approved public employer anonymization patch. "
        "The 28-posting research provenance is preserved in its evidence "
        "notes, where every count in the video is stated as a count within "
        "those 28 postings.",
        "V14 ships anonymized. No employer name was restored at any point.",
        "Real posting evidence is preserved internally with requisition IDs, "
        "source pages and capture dates, and is never displayed.",
    ])

    # ---------------------------------------------------------------- 7
    h(d, "7. Publishing copy is never silently promoted")
    para(d, "Every description in the eleven packages came from an approved "
            "synchronized source and says so, naming the file it came from. "
            "Nothing was reworded, regenerated or upgraded from draft to "
            "final by the packaging pass. Copy constructed during packaging, "
            "such as pinned comments, is marked DRAFT and stays draft until "
            "reviewed for that specific video.")

    # ---------------------------------------------------------------- 8
    h(d, "8. Deliberate departures from the older production standard")
    bullets(d, [
        "Three candidate Shorts per video, not six. Six was the old "
        "requirement and was not carried forward.",
        "No hashtag strategy. Hashtags were not treated as a requirement and "
        "none is specified.",
        "Every timing figure labelled as an estimate rather than presented "
        "as a runtime.",
    ])

    page_break(d)
    # ---------------------------------------------------------------- 9
    h(d, "9. What the September 24 audit changes")
    para(d, "The audit reopens V4 to V11 for a limited editorial refresh and "
            "leaves V12 to V14 alone. The production architecture above does "
            "not change. What changes is the spoken script, and then anything "
            "downstream of a sentence that moved.")
    table(d, ["Layer", "Effect of the refresh"], [
        ["Recording master", "Rewritten within the audit's scope. The "
                             "previous locked master stays as the base "
                             "source and is not discarded."],
        ["Thought blocks", "Rebuilt from the revised master. Parity is "
                           "re-measured, not assumed."],
        ["Trigger map", "Any trigger quoting a changed sentence has to be "
                        "repointed. The map names the sentence, so the "
                        "affected triggers are findable."],
        ["Visuals", "Unchanged unless a slide's own words were part of the "
                    "revision. Approved artwork is not redrawn to suit a new "
                    "line."],
        ["Estimated timing", "Recomputed from the new word count."],
        ["Shorts", "Re-cut only where their source lines moved."],
        ["Publishing", "Description and chapters follow the new wording. "
                       "Nothing is promoted to final by the rebuild."],
        ["Evidence and QA", "Re-run. A claim that survives a rewrite still "
                            "has to survive its source check."],
    ], widths=[1.5, 5.2])

    # ---------------------------------------------------------------- 10
    h(d, "10. Seven things that are open and need a decision")
    para(d, "These came out of the checks run before any rewriting began. "
            "None is a defect in the packages. Each is something the build "
            "could not settle on its own and refused to guess at.")

    sub(d, "A. Two figures in V6 cannot be verified at source")
    para(d, "V6 quotes a research corpus of 15 postings from 11 employers. "
            "The internal source capture packet documents eight postings "
            "across six employers, which are the ones used on camera. The "
            "other seven postings and five employers are asserted but never "
            "recorded anywhere in the workspace.")
    table(d, ["Figure in V6", "Verdict", "Source"], [
        ["$61,500 pay floor", "VERIFIED",
         "Requisition R0055598, published range $61,500 to $136,100, captured "
         "12 September 2026"],
        ["Just under $248,000", "VERIFIED",
         "Requisition R0054759, published range $133,400 to $247,700"],
        ["$180,000 to $440,000", "VERIFIED, with a qualifier",
         "The source records this as a base range. The script says "
         "“published pay range,” dropping the word base."],
        ["Three hours' overlap with East Africa Time", "VERIFIED",
         "Stated in the posting as captured"],
        ["15 postings", "NOT VERIFIABLE",
         "The packet records 8"],
        ["11 employers", "NOT VERIFIABLE",
         "The packet records 6"],
    ], widths=[1.5, 1.5, 3.7])
    para(d, "The audit already asks for the duplicate research line to be "
            "removed. Removing it leaves one instance of an unverifiable "
            "claim rather than none. The options are to drop both instances, "
            "soften the framing, or supply the missing capture records.")

    sub(d, "B. Most of the resources the audit routes are not live")
    para(d, "The audit assigns a resource to each video. Checked against the "
            "site as it stands:")
    table(d, ["Resource", "Status on the site"], [
        ["Field Kit, $150", "LIVE. On the professionals page and the book "
                            "page, and /fieldkit redirects to the store."],
        ["Career Move Review, $500", "PRICE AND TIER MATCH, NAME DOES NOT. "
                                     "The site sells a Private Capability "
                                     "Position Read at $500."],
        ["Career Evidence Starter", "NOT CURRENT. No page and no redirect "
                                    "exists for it."],
        ["Keep the Proof, $49", "NOT FOUND anywhere on the site."],
        ["Workshop", "NOT A LIVE OFFER. Only an interest-capture form tag "
                     "exists."],
    ], widths=[2.0, 4.7])
    para(d, "The audit routes the Career Evidence Starter into V6, V7 and V9, "
            "and the workshop into V5 and V11. Neither is currently "
            "purchasable. Only the Field Kit and the $500 read are. This "
            "needs an editorial decision before any resource line is written, "
            "because writing a call to action for an offer that does not "
            "exist is worse than writing none.")

    sub(d, "C. No video's publication status can be established")
    para(d, "There is no publication record anywhere in the workspace: no "
            "upload dates, no video URLs, no live flags. Every watch-next "
            "destination is therefore UNKNOWN as to whether it will be live. "
            "What can be established is whether the destination exists as an "
            "asset at all.")
    table(d, ["Video", "Current watch next", "Exists as"], [
        ["V4", "How to Prove Your Value When AI Does More of the Task",
         "V15, built"],
        ["V5", "It Took Me Years to Stop Mistaking More Work for Career "
               "Growth", "Nothing. No asset exists."],
        ["V6", "Turn One Accomplishment Into Proof in 10 Minutes",
         "V12, locked. The spoken title omits “How to.”"],
        ["V7", "What to Do When Your Work Is Valued but You Are Overlooked",
         "V16, built"],
        ["V8", "Before a Layoff, Know What You Can Still Prove",
         "V17, built. The audit flags this as a third pass at the same "
         "angle."],
        ["V9", "Which Parts of Your Experience Actually Transfer to Another "
               "Industry?", "V13, locked. Exact match."],
        ["V10", "What to Do When Your New Job Isn’t the Job You "
                "Accepted", "V11, internal"],
        ["V11", "If Your Company Needs You but Won’t Grow You",
         "V5, internal"],
    ], widths=[0.6, 3.3, 2.8])
    para(d, "Six of the eight point at real assets. V5 is the exception: its "
            "destination does not exist in any form and has to be repointed.")

    sub(d, "D. None of the proposed personal warrants can be verified")
    para(d, "The audit suggests a personal-experience warrant for V4, V7, V9, "
            "V10 and V11, and correctly hedges each one. None could be "
            "confirmed from approved source material in the workspace.")
    table(d, ["Video", "Proposed warrant", "What the workspace holds"], [
        ["V4", "Early audit years", "Not found."],
        ["V7", "What gets asked in rooms where names come up", "Not found."],
        ["V9", "Accounting and audit crossing into cybersecurity",
         "Not found. The word appears only in a slide-audit filename, never "
         "as biography."],
        ["V10", "First in role three times, including two named employers",
         "One of the two employers appears nowhere in the workspace. The "
         "other appears once, inside a section headed EXCLUDED METRICS. "
         "Neither job title is stated in any approved source."],
        ["V11", "A role that became the first of its kind", "Not found."],
    ], widths=[0.6, 2.4, 3.7])
    para(d, "These are flagged rather than written. Confirming them is a "
            "matter for Temidayo, not for inference.")

    sub(d, "E. A wording conflict on career span")
    para(d, "The claims ledger retired “18 years” in favour of "
            "“nearly two decades” for public-facing material. V1’s "
            "locked master says “more than 18 years.” V1 is locked "
            "and was not touched. Whichever wording is preferred should be "
            "settled before the V4 to V11 introductions are rewritten.")

    sub(d, "F. Four overlaps the refresh has to resolve, not just trim")
    para(d, "The audit identifies these and they are structural rather than "
            "cosmetic. V8 against V3 and V9 against V1 are repositionings, "
            "which means the packages downstream of them change more than a "
            "light edit would suggest.")

    sub(d, "G. What a rewrite costs downstream")
    para(d, "Worth stating so the scope is understood before it is approved. "
            "A changed sentence can invalidate a trigger, a Short, a caption "
            "card, a chapter title and a description line at the same time. "
            "The packages make every one of those dependencies visible, so "
            "the cost is knowable in advance rather than discovered during "
            "the rebuild.")

    page_break(d)
    # ---------------------------------------------------------------- 11
    h(d, "11. How the work is checked")
    para(d, "Every claim in the packages is produced by a check that was "
            "itself tested. When a check fails, the first question is "
            "whether the package is wrong or the check is wrong, and the "
            "answer is reported either way rather than resolved by loosening "
            "the check.")
    bullets(d, [
        "192 checks across the eleven videos, all passing.",
        "341 required-artifact slots, all present.",
        "Each check was proved to fire by running it against a deliberately "
        "broken copy. A check that cannot fail is not evidence.",
        "The build is deterministic: run twice, the archives are byte "
        "identical, so a change in output always means a change in input.",
    ])
    para(d, "Two examples of that discipline, both real. A check reported "
            "that the recording masters had changed; investigation showed the "
            "packaging step was rewriting their timestamps, and the packaging "
            "step was fixed so the masters ship untouched. A different check "
            "reported that chapter titles did not match the spoken roadmap; "
            "investigation showed the check was demanding word-identical "
            "matching where the source deliberately uses "
            "“deciding” in speech and “Decide” in a "
            "heading, so the check was corrected. One was a real defect, one "
            "was a false alarm, and they were reported as what they were.")

    # ---------------------------------------------------------------- 12
    h(d, "12. What is being asked of the advisor")
    para(d, "The scripts are the audit's business. These seven are the "
            "production questions that sit alongside them and cannot be "
            "answered from the workspace:")
    bullets(d, [
        "The two unverifiable V6 research figures: drop, soften, or supply "
        "the records.",
        "The resource for each video, given that three of the five named "
        "offers are not currently live.",
        "Which watch-next destinations will be published by the time these "
        "videos go out, and where V5 should point instead.",
        "Whether each proposed personal warrant is true and comfortable to "
        "say, in Temidayo’s own words.",
        "The career-span wording.",
        "Confirmation of the two repositionings, V8 as the monthly habit and "
        "V9 as the gap conversation.",
        "Whether the scope of the rewrite is accepted now that the "
        "downstream cost is visible.",
    ])
    footer_note(d, "Videos 4 to 14 only. V1 to V3 and V15 and above were not "
                   "modified. No script in this series was rewritten to "
                   "produce this document.")
    d.save(path)
    return path

if __name__ == "__main__":
    p = build(os.path.join(OUT, NAME))
    print(p, os.path.getsize(p))
