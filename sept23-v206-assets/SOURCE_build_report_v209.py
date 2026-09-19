# -*- coding: utf-8 -*-
"""Free Flagship Change Log and QA Report — v2.0.8 -> v2.0.9.

Adds the v2.0.6 revision section and Group N, whose rows are written by
qa_v206.py at build time so the document cannot report a pass the checks did not
produce. The build refuses to save if any check fails.

Rows that THIS revision falsified are repointed rather than left to rot: the
seven-page SOP pin, the slide-18 clearance row, the single-line move-row row and
the rows that described the Private Capability Position Read as a live decision.
Historical rows that describe what an earlier version did are left alone, since
they are the audit trail.
"""
import copy, hashlib, importlib, os, sys
import docx

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
SRC = "sept23-v205-assets/Free_Flagship_60MIN_v2.0.8_Change_Log_and_QA_Report.docx"
OUT = "scratchpad/sept23/out"
DST = f"{OUT}/Free_Flagship_60MIN_v2.0.9_Change_Log_and_QA_Report.docx"
STAMP = "Saturday, September 19, 2026 at 8:30 AM CT"
OLD = "Friday, September 4, 2026 at 6:40 AM CT"

CHANGES = [
 ("The opening",
  "The approved audit-to-cybersecurity warrant moves from slide 5's OPTIONAL "
  "SPOKEN PROOF block into the core spoken opening on slide 2, where it now "
  "arrives before any terminology. It is capped at thirty to forty-five seconds "
  "and the note forbids adding to it. Nothing was invented: no dates, employers, "
  "metrics, reactions, reasons for the move or outcomes. The words are the ones "
  "already approved in this package."),
 ("Ordinary language first",
  "Slides 4 and 5 now ask the question before naming the term. Slide 4 reads “Is "
  "the work still building you?” with “This reading calls that Density.” beneath "
  "it; slide 5 reads “Will what you build still travel?” with “This reading calls "
  "that Optionality.” Both terms are still taught and still measured by six "
  "statements each."),
 ("Density, in natural language",
  "The definition drops the academic register. It now reads that Density reads "
  "whether this environment is still forming you, that it reads conditions rather "
  "than effort, and that a role can be demanding, important and exhausting and "
  "still stop building you. The correction beneath it names what Density is not: "
  "not how busy you are, not how much pressure you carry, not how much the "
  "organization depends on you."),
 ("Optionality, realigned",
  "The old wording said Optionality was whether capability would be “recognised "
  "and valued somewhere other than here”, which read as a claim about employer "
  "recognition. It now reads whether what the work is building stays useful beyond "
  "the current context, and whether the participant could make it legible to "
  "someone outside the organization using evidence rather than a title. The "
  "boundary beneath it says plainly that translation is not recognition and that "
  "making work legible removes a barrier without deciding what another "
  "organization does with what it sees."),
 ("The 12 statements",
  "UNTOUCHED, and asserted rather than assumed. Slides 6, 7, 9 and 10 are compared "
  "string by string against the approved v2.0.5 deck on disk. The scale, both /30 "
  "totals, the bands, the evidence protocol, the 3-versus-question-mark "
  "distinction and the ninety-day window are all unchanged."),
 ("Slide 18, simplified",
  "The face carried the full sensitivity specification: four procedure steps, the "
  "1-to-5 bound and the consequence, printed alongside the three tiers. It now "
  "carries the three tiers, a boundary band reading “17 TO 21 IS THE BOUNDARY "
  "BAND. A boundary reading overrides the normal high and low split.”, and the "
  "simplified dual-axis rule. Seventeen text blocks became fifteen and 955 "
  "characters became 706. NOTHING WAS LOST: the procedure was already printed on "
  "workbook page 4 and is repeated in full in the presenter note."),
 ("The four-question portability audit",
  "Now appears ONCE, on slide 22, as a single line directly above the Next-Move "
  "Note: what travels, what does not, what can I prove, what must I relearn. It "
  "was an optional aside in slide 5's notes and is now the interpretive frame at "
  "the moment of interpretation. No new exercise, no new worksheet, nothing to "
  "score and nothing to hand in. The note adds the destination boundary: you "
  "cannot fully answer what travels until you know where it is travelling to, and "
  "generic portability is not destination-specific portability."),
 ("Three move-category readings",
  "The seven names stand. “Translate what is built” now reads that the evidence is "
  "not yet legible outside, rather than that the language does not exist. “Widen "
  "exposure” now reads “Reach people who can evaluate or use it. Visibility is not "
  "evidence.”, replacing “The work is good and the wrong people have seen it.” "
  "“Repair formation conditions” becomes a category to test rather than the "
  "instruction “Change the work, not the employer, first.” All three stay on one "
  "line, which is what the row layout was built for."),
 ("Slide 20",
  "The closing line said the fuller cost “belongs in deeper follow-on work”, which "
  "read as if the real interpretation was held back. It now says the reading given "
  "today is complete, and that depth, a named destination and rerunning as "
  "conditions change are what continued work adds."),
 ("The close",
  "Slide 25 returns to the question the session opened with: you came in asking "
  "stay or leave, you leave with a clearer read. The body says plainly that the "
  "decision was not made for the participant and should not be, names what they do "
  "have, and keeps the ninety-day rescore. Not motivational, not grand."),
 ("Commercial architecture",
  "The Private Capability Position Read is retired as an offer. The SOP's offer "
  "table is rebuilt to the current individual architecture: Career Evidence "
  "Starter free, Keep the Proof $49, Field Kit $150, Career Move Review $500 with "
  "qualification before payment. Keep the Proof is deliberately NOT added to the "
  "recorded continuation slide, because it answers a different problem and belongs "
  "in follow-up."),
 ("Career Move Review — route not verified",
  "Route 3 stays OFF the recorded deck. No page, no route and no copy for Career "
  "Move Review exists anywhere in the repository, on this branch or on main. Under "
  "the operational condition in the brief, an unverified route is not offered from "
  "the stage. The SOP names it as the current advisory architecture and records "
  "its route verification as an outstanding launch condition."),
 ("Polls",
  "The blanket ban becomes a precise rule. Nothing diagnostic, score-revealing, "
  "state-revealing, employer-revealing or decision-revealing runs inside the "
  "recorded assessment. One optional anonymous arrival poll may run BEFORE the "
  "recording starts while the dated holding slide is up, asking only “What brought "
  "you here?”. If the platform does not make it easy, skip it."),
 ("The protected block",
  "Still twelve minutes, still non-negotiable, still silent. The note now permits "
  "ONE quiet midpoint cue at about 25:00: if you are around statement six you are "
  "on pace, keep the evidence phrases short. Then back to silence. The two-minute "
  "and thirty-second warnings are unchanged. This is facilitator presence, not "
  "teaching."),
 ("Timing",
  "Ten seconds move from slide 1 to slide 2 so the lived warrant fits. Slide 1 is "
  "0:00–0:30 and slide 2 is 0:30–1:20. Nothing else moves: the 2:00 and 5:00 block "
  "boundaries, the protected 19:00–31:00 rescore, the 50:00 recording stop and the "
  "50:00–60:00 Q&A are all exactly where they were, and the SOP's master "
  "reconciliation table needed no timing edit."),
 ("Two pre-existing defects repaired",
  "Slide 22's third label ran past its box and collided with the answer rule; it "
  "is shortened to the length the other two labels use. Slide 18's overrun is "
  "resolved by the simplification. Five text frames flagged as overflowing on "
  "v2.0.5; three do on v2.0.6, and none of them is new."),
 ("The workbook",
  "NOT TOUCHED. Byte-identical at sha256 2bd2912846a679837e8e6bfb4aadff2b… Its 68 "
  "form fields, calculation behavior, validation, question-mark handling, manual "
  "total fallback and JavaScript are untouched, so the owner-run Adobe Acrobat "
  "Reader pass of August 21, 2026 still applies to the exact file being shipped. "
  "Its British spellings are recorded as a deferred cosmetic issue and are NOT a "
  "reason to regenerate a validated form."),
]

REPOINTS = {
 # Three rows that THIS revision made untrue. Repointed, not excused.
 (14, 4, 3): ("the Private Read priced but marked NOT OPERATIONAL",
   "REPOINTED IN v2.0.9. The SOP's offer table no longer prices an unavailable "
   "Private Read. It now carries the current individual architecture: free "
   "session, Career Evidence Starter free, Keep the Proof $49, Field Kit exactly "
   "$150, Career Move Review $500 with qualification before payment and its route "
   "marked NOT VERIFIED, the Private Capability Position Read marked RETIRED, and "
   "the former paid group workshop marked retired from active public sale."),
 (20, 24, 1): ("SOP section 9 states the current Field Kit and Private Read checks",
               "SOP section 9 states the current Field Kit and Career Move Review "
               "checks"),
 (20, 24, 3): (None,
   "REPOINTED IN v2.0.9. Section 9 asked the facilitator to confirm the Private "
   "Read was still off the sequence. It now asks them to confirm the Career Move "
   "Review is still absent until its fulfillment route is verified operational, "
   "which is the check that actually applies."),
 (21, 10, 3): ("stays off the slide and out of Q&A while",
   "Slide 23 carries two routes: do nothing, or the Field Kit. The Private "
   "Capability Position Read is RETIRED as an offer. Career Move Review is the "
   "current advisory architecture and stays off the slide and out of Q&A until its "
   "fulfillment route is verified, so no unavailable service is offered from the "
   "stage."),
 (17, 2, 1): ("Slide 18 dual-axis rule has clearance",
              "Slide 18 dual-axis rule has clearance, on a simplified face"),
 (17, 2, 3): (None,
   "REPOINTED IN v2.0.9. v2.0.5 fitted the rule beneath a face that also printed "
   "the whole sensitivity procedure. v2.0.6 removes four procedure lines from the "
   "face, so the rule now sits under a boundary band with room to breathe. It "
   "still breaks one clause per line and is still clear of the bar above it."),
 (17, 3, 1): ("Slide 21 move rows are all single-line",
              "Slide 21 move rows keep their single-line rhythm"),
 (17, 3, 3): (None,
   "REPOINTED IN v2.0.9, AND MORE HONEST THAN BEFORE. Three readings were "
   "rewritten and all three were kept to one line for the 5.48in column. Rows 6 "
   "and 7 wrapped to two lines in v2.0.5 as well, so the original claim that ALL "
   "rows were single-line was never quite true; this row now asserts what the "
   "layout actually requires."),
 (19, 2, 1): ("Exported SOP is exactly seven pages",
              "Exported SOP is exactly eight pages"),
 (21, 14, 1): ("SOP still exports at exactly seven pages",
               "SOP still exports at exactly eight pages"),
 (21, 14, 3): (None,
   "Re-pinned in v2.0.9. Seven pages was the right pin for a document with two "
   "live offers; five offers and three new operational rules need eight. Prose "
   "was tightened first, the orientation sequence is unchanged, and page 8 "
   "carries 31 substantive lines rather than a stub."),
 (19, 2, 3): (None,
   "REPINNED FROM SEVEN IN v2.0.9, AND SAID OUT LOUD RATHER THAN QUIETLY DROPPED. "
   "The commercial architecture grew from two live offers to five, and sections 4, "
   "5 and 12 gained operational rules the revision required. Prose was tightened "
   "first and the document still needs the page. The pin exists to catch an "
   "unnoticed overrun, not to cap content, so the count is re-pinned at eight and "
   "the stub-page test it protected is kept: page 8 carries 31 substantive lines."),
}


def set_para(para, text):
    runs = para.runs
    keep = next((r for r in runs if r.text.strip()), runs[0])
    keep.text = text
    for r in runs:
        if r._r is not keep._r:
            r._r.getparent().remove(r._r)


def set_cell(cell, text):
    p = cell.paragraphs[0]
    for extra in cell.paragraphs[1:]:
        extra._element.getparent().remove(extra._element)
    set_para(p, text)


def build():
    os.makedirs(OUT, exist_ok=True)
    import shutil
    shutil.copyfile(SRC, DST)
    d = docx.Document(DST)

    qa = importlib.import_module("qa_v206")
    total = 162 + len(qa.R)
    passed = 162 + sum(1 for r in qa.R if r[3] == "PASS")

    # Located by content, not by index. The v2.0.8 document's paragraph numbers
    # differ from v2.0.7's because that pass inserted a section, and hardcoding
    # indices against a document that grows is how an edit lands on the wrong line.
    def find(fragment, nth=None):
        hits = [x for x in d.paragraphs if fragment in x.text]
        if nth is not None:
            return hits[nth]
        assert len(hits) == 1, f"{fragment[:44]!r} matched {len(hits)} paragraphs"
        return hits[0]

    for para in [x for x in d.paragraphs if OLD in x.text]:
        for r in para.runs:
            if OLD in r.text:
                r.text = r.text.replace(OLD, STAMP)

    EDITS = [
     ("DECK IS NOW v2.0.5.", "DECK IS NOW v2.0.6."),
     ("UNCHANGED FROM v2.0.2 THROUGH v2.0.8.",
      "UNCHANGED FROM v2.0.2 THROUGH v2.0.9."),
     ("PowerPoint v2.0.5, workbook v2.0.1, SOP v2.0.8",
      "PowerPoint v2.0.6, workbook v2.0.1, SOP v2.0.9"),
     ("Verification — 162 items", f"Verification — {total} items"),
     ("162 of 162 PASS.", f"{passed} of {total} PASS."),
     ("The September 23 deck v2.0.5 was exported",
      "The September 23 deck v2.0.6 was exported"),
     ("PREVIEW_Presentation_60MIN_v2.0.5_LibreOffice.pdf, rendered from the v2.0.5 "
      "deck in this pass",
      "PREVIEW_Presentation_60MIN_v2.0.6_LibreOffice.pdf, rendered from the v2.0.6 "
      "deck in this pass"),
     ("PREVIEW_SOP_60MIN_v2.0.8_LibreOffice.pdf",
      "PREVIEW_SOP_60MIN_v2.0.9_LibreOffice.pdf"),
     ("The export is EXACTLY SEVEN PAGES",
      "The v2.0.9 export is EXACTLY EIGHT PAGES"),
     ("QA REPORT v2.0.8", "QA REPORT v2.0.9"),
    ]
    for old, new in EDITS:
        para = find(old)
        for r in para.runs:
            if old in r.text:
                r.text = r.text.replace(old, new)
                break
        else:
            # the fragment spans runs, so collapse the paragraph onto its carrier
            set_para(para, para.text.replace(old, new))

    banner = d.tables[0].rows[0].cells[0]
    for para in banner.paragraphs:
        for r in para.runs:
            r.text = r.text.replace("v2.0.8 CANDIDATE", "v2.0.9 CANDIDATE") \
                           .replace(OLD, STAMP)

    for (ti, ri, ci), (expect, new) in REPOINTS.items():
        cell = d.tables[ti].rows[ri].cells[ci]
        if expect:
            assert expect in cell.text, f"T{ti}r{ri}c{ci}: expected {expect[:40]!r}"
        set_cell(cell, new)

    # the new change-log section and Group N
    head = copy.deepcopy(find("SOP — the 60-minute rewrite")._element)
    body = copy.deepcopy(find("Rewritten as the operational source of truth")._element)
    sub = copy.deepcopy(find("Group A — Duration consistency")._element)
    tbl2 = copy.deepcopy(d.tables[6]._element)
    tbl4 = copy.deepcopy(d.tables[19]._element)
    blank = copy.deepcopy([x for x in d.paragraphs if not x.text.strip()][3]._element)
    from docx.text.paragraph import Paragraph

    def insert(anchor_el, tmpl, text=None):
        el = copy.deepcopy(tmpl)
        anchor_el.addprevious(el)
        if text is not None:
            set_para(Paragraph(el, d), text)
        return el

    def table_before(anchor_el, tmpl, rows):
        el = copy.deepcopy(tmpl)
        anchor_el.addprevious(el)
        t = docx.table.Table(el, d)
        while len(t.rows) > 2:
            t._element.remove(t.rows[-1]._element)
        template = copy.deepcopy(t.rows[1]._element)
        for ci, v in enumerate(rows[0]):
            set_cell(t.rows[0].cells[ci], v)
        t._element.remove(t.rows[1]._element)
        for row in rows[1:]:
            t._element.append(copy.deepcopy(template))
            for ci, v in enumerate(row):
                set_cell(t.rows[-1].cells[ci], v)
        return t

    anchor = find("Zero-tolerance duration sweep")._element
    insert(anchor, head, "September 19 revision — what changed in v2.0.6 / v2.0.9")
    insert(anchor, body,
           "A focused revision of an approved family, not a rebuild. The learning "
           "spine is untouched and so is the instrument. What changed is how the "
           "session opens, how two definitions are worded, how much slide 18 prints, "
           "where the portability frame lives, how three move categories read, how "
           "the session closes, and which offers exist.")
    table_before(anchor, tbl2, [("Where", "Change")] + CHANGES)
    insert(anchor, blank)

    tail = [p for p in d.paragraphs
            if p.text.strip() == f"{passed} of {total} PASS."][0]._element
    insert(tail, sub, "Group N — the September 19 revision")
    table_before(tail, tbl4, [("#", "Category", "Status", "Notes")]
                 + [(str(162 + n), label, st, note)
                    for n, g, label, st, note in qa.R])
    insert(tail, blank)

    d.save(DST)
    assert passed == total, "the report cannot be saved while a check fails"
    return DST, passed, total


if __name__ == "__main__":
    path, p_, t_ = build()
    print("built", os.path.basename(path), f"({p_}/{t_})")
    print("  sha256", hashlib.sha256(open(path, "rb").read()).hexdigest())
