# -*- coding: utf-8 -*-
"""The Video 14 research design package: design document, coding framework
CSV files, and the research status file."""
import os, sys, csv
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import v14design as D
from docsx import (base_doc, para, title_block, rule, h, kv, callout, table,
                   bullets, sub, field, page_break, footer_note, numbered,
                   NAVY, GOLD, DIM, RED)

TITLE_PLANNING = "Which Parts of Your Experience Will Transfer to Another Industry?"
TITLE_CONDITIONAL = "I Compared 30 Job Descriptions Across 3 Industries"


def build_design(out_path, stamp):
    d = base_doc()
    footer_note(d, "Capability Formation  |  Video 14 research design  |  "
                   "RESEARCH DESIGN READY. No data collected. No finding "
                   "exists.")

    title_block(d, "Capability Formation  |  Video 14",
                "Research Design",
                "The design for the comparison. Not the comparison, and not "
                "its result.")
    kv(d, "Created", stamp)
    kv(d, "Status", "RESEARCH DESIGN READY. FINAL SCRIPT BLOCKED UNTIL "
                    "COMPARISON RESEARCH IS COMPLETED AND DOCUMENTED.")
    kv(d, "Planning title", TITLE_PLANNING)
    kv(d, "Conditional title", "%s. CONDITIONAL and not usable. See item 20."
       % TITLE_CONDITIONAL)
    kv(d, "Thumbnail direction", "WHAT REALLY TRANSFERS? Carried from the "
                                 "locked roadmap. The thumbnail line was "
                                 "never the part under the research gate.")

    callout(d, "No postings have been collected. Nothing has been coded. "
               "There is no findings section in this document and there is "
               "no finding. A research plan is not research, and this "
               "document does not become evidence by existing.")

    h(d, "The research question")
    para(d, D.QUESTION, size=11.5, bold=True, color=NAVY)
    para(d, "Sub-questions the coding is built to answer:", size=10,
         color=DIM, before=8, after=4)
    bullets(d, D.SUB_QUESTIONS)

    h(d, "The design")
    para(d, "Items marked FOR APPROVAL are Temidayo's decisions, not "
            "settled here. Collection does not begin until they are "
            "settled, because changing them afterward would invalidate the "
            "sample.", size=10, color=DIM)
    for headline, body in D.DESIGN:
        para(d, headline, size=11, bold=True, color=NAVY, before=12, after=3,
             keep=True)
        para(d, body)

    page_break(d)
    h(d, "Codebook")
    para(d, "%d fields. Every posting is coded on every field. Where a "
            "posting says nothing about a field, the value is NOT STATED, "
            "which is a finding rather than an absence."
            % len(D.CODEBOOK), size=10, color=DIM)
    table(d, ["Field", "Type", "Definition", "Allowed values or format"],
          [[a, b, c, e] for a, b, c, e in D.CODEBOOK],
          widths=[1.5, 0.72, 2.55, 1.93], size=8)

    h(d, "Exclusion log fields")
    para(d, "The exclusion log is part of the result. The count of what was "
            "rejected, and why, is what allows anybody to judge the sample.",
         size=10, color=DIM)
    table(d, ["Field", "Format"], [[a, b] for a, b in D.EXCLUSION_FIELDS],
          widths=[1.9, 4.8], size=8.5)

    page_break(d)
    h(d, "Research integrity rules")
    bullets(d, D.INTEGRITY)

    h(d, "Sequence")
    para(d, "In this order. Step 7 is the first point at which a title, a "
            "number, or a decision to make the video is available.",
         size=10, color=DIM)
    table(d, ["", "What happens"], [[a, b] for a, b in D.SEQUENCE],
          widths=[0.85, 5.85], size=9)

    h(d, "What the video may claim, and what it may not")
    table(d, ["Job descriptions CAN establish", "They CANNOT establish"],
          [[D.DESIGN[16][1],
            D.DESIGN[17][1].replace(" This list belongs in the video, not "
                                    "only in this document.", "")]],
          widths=[3.35, 3.35], size=8.5)
    para(d, "The second column belongs in the video itself, spoken, not only "
            "in this document.", size=9.5, color=DIM)

    h(d, "Files in this package")
    table(d, ["File", "What it is"], [
      ["V14_Research_Design.docx", "This document."],
      ["V14_Coding_Framework.csv",
       "The collection template. Header row only, one column per codebook "
       "field, zero data rows. Data rows appear only when real postings are "
       "coded."],
      ["V14_Coding_Codebook.csv",
       "The codebook as a file, so the definitions travel with the sheet."],
      ["V14_Exclusion_Log.csv",
       "The exclusion log template. Header row only."],
      ["V14_Research_Status.txt", "The gate, in one file."],
    ], widths=[2.1, 4.6], size=9)

    rule(d)
    para(d, "RESEARCH DESIGN READY. FINAL SCRIPT BLOCKED UNTIL COMPARISON "
            "RESEARCH IS COMPLETED AND DOCUMENTED.",
         size=10.5, bold=True, color=RED)
    d.save(out_path)
    return out_path


def build_csvs(outdir):
    made = []
    p = os.path.join(outdir, "V14_Coding_Framework.csv")
    with open(p, "w", newline="") as f:
        csv.writer(f).writerow([r[0] for r in D.CODEBOOK])
    made.append(p)

    p = os.path.join(outdir, "V14_Coding_Codebook.csv")
    with open(p, "w", newline="") as f:
        wcsv = csv.writer(f)
        wcsv.writerow(["field", "type", "definition",
                       "allowed_values_or_format"])
        for row in D.CODEBOOK:
            wcsv.writerow(list(row))
    made.append(p)

    p = os.path.join(outdir, "V14_Exclusion_Log.csv")
    with open(p, "w", newline="") as f:
        csv.writer(f).writerow([r[0] for r in D.EXCLUSION_FIELDS])
    made.append(p)
    return made


def build_status(out_path, stamp):
    L = [
     "VIDEO 14 RESEARCH STATUS",
     "=" * 60,
     "",
     "RESEARCH DESIGN READY.",
     "FINAL SCRIPT BLOCKED UNTIL COMPARISON RESEARCH IS COMPLETED AND",
     "DOCUMENTED.",
     "",
     "Recorded: %s" % stamp,
     "",
     "-" * 60,
     "WHAT EXISTS",
     "-" * 60,
     "",
     "  A research design.",
     "  A codebook of %d fields." % len(D.CODEBOOK),
     "  A collection template with a header row and no data rows.",
     "  An exclusion log template with a header row and no data rows.",
     "",
     "-" * 60,
     "WHAT DOES NOT EXIST",
     "-" * 60,
     "",
     "  No postings have been collected.",
     "  No postings have been coded.",
     "  No comparison has been run.",
     "  No finding, result, count or conclusion exists.",
     "  No script has been written for this video.",
     "",
     "-" * 60,
     "WHAT IS BLOCKED, AND UNTIL WHEN",
     "-" * 60,
     "",
     "  BLOCKED until the coded record exists:",
     "",
     "    The title \"%s\"." % TITLE_CONDITIONAL,
     "    Any number, in a title, thumbnail, description or spoken line.",
     "    Any past-tense claim about the comparison.",
     "    Any statement of what the comparison found.",
     "    The final recording script.",
     "",
     "  NOT blocked:",
     "",
     "    The topic, which is approved direction.",
     "    The planning title, \"%s\"." % TITLE_PLANNING,
     "    The thumbnail line WHAT REALLY TRANSFERS?, which was never the",
     "    part under the gate.",
     "",
     "-" * 60,
     "WHAT UNBLOCKS IT",
     "-" * 60,
     "",
     "  1. Temidayo approves the role family, the three industries and the",
     "     geographic scope. Nothing collects before this.",
     "  2. The pilot code runs on three postings and the codebook is",
     "     revised once.",
     "  3. Collection and coding reach at least the stated minimum of 24",
     "     postings, 8 per industry, with every exclusion logged.",
     "  4. The counts are produced from the coded record.",
     "  5. Only then: decide whether there is a video, what its title is,",
     "     and whether any number belongs in that title. The number is the",
     "     count of postings actually retained, whatever that number is.",
     "",
     "-" * 60,
     "IF THE RESULT IS WEAK",
     "-" * 60,
     "",
     "  A weak or mixed comparison is published as a weak or mixed",
     "  comparison, or the video is not made. It is not improved, rounded,",
     "  reframed, or supplemented with an example that was not in the",
     "  sample.",
     "",
    ]
    with open(out_path, "w") as f:
        f.write("\n".join(L) + "\n")
    return out_path
