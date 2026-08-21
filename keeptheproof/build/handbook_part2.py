# -*- coding: utf-8 -*-
"""Second half of the Keep the Proof handbook: tools, translation, examples,
routines, retrieval, AI prompt, ledger pages, summary, boundary, about, close."""
from reportlab.platypus import (Paragraph, Spacer, NextPageTemplate, PageBreak,
    Table, TableStyle, KeepTogether)
from reportlab.lib.styles import ParagraphStyle
from ktp import (NAVY, CREAM, PAPER, GOLD, RUST, BLUE, INK, MUTE, HAIR, CREAMSOFT,
    HexColor, RustTab, HRule, styles as _st,
    quick_capture_fields, full_entry_pages, two_up_fields, Bookmark,
    IconMark, chip_mark, ic_clock_pencil, ic_form_card, ic_translate_arrow,
    ic_prooflines, ic_clock60, ic_calendar_arrow, ic_record_search)

def story(S, P, LEAD, H2, H3, EY, KI, NOTE, SP, bullets, CO, TBL, RULE,
          section_divider, workflow_strip, field_row, Field, CONTENT_W):
    st = []
    NT = lambda t: NextPageTemplate(t)
    PB = PageBreak
    GAP = lambda h=24: SP(h)  # soft section break when flowing sections on one page

    def example_card(name_role, tag_line, blocks):
        """blocks: list of (label, text). Rendered as a bordered card."""
        rows = [[Paragraph(name_role, ParagraphStyle("ex_n", fontName="DM-Bold", fontSize=10, textColor=CREAM, leading=13)),
                 Paragraph(tag_line, ParagraphStyle("ex_t", fontName="DM", fontSize=8.4, textColor=GOLD, leading=11))]]
        head = Table([[rows[0][0], rows[0][1]]], colWidths=[CONTENT_W*0.52-14, CONTENT_W*0.48-14])
        head.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),NAVY),("VALIGN",(0,0),(-1,-1),"MIDDLE"),
            ("LEFTPADDING",(0,0),(-1,-1),14),("RIGHTPADDING",(0,0),(-1,-1),14),
            ("TOPPADDING",(0,0),(-1,-1),8),("BOTTOMPADDING",(0,0),(-1,-1),8),("ALIGN",(1,0),(1,0),"RIGHT")]))
        body = []
        for label, text in blocks:
            body.append(Paragraph(label.upper(), ParagraphStyle("ex_l", fontName="DM-Bold", fontSize=7.8, textColor=RUST, leading=11, spaceBefore=5, spaceAfter=1)))
            body.append(Paragraph(text, ParagraphStyle("ex_b", fontName="DM", fontSize=9.2, textColor=INK, leading=13)))
        card = Table([[body]], colWidths=[CONTENT_W-28])
        card.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),HexColor("#FFFFFF")),
            ("LEFTPADDING",(0,0),(-1,-1),14),("RIGHTPADDING",(0,0),(-1,-1),14),
            ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),12),
            ("LINEBELOW",(0,0),(-1,-1),1,GOLD),("LINEBEFORE",(0,0),(0,-1),1,GOLD),("LINEAFTER",(0,0),(-1,-1),1,GOLD)]))
        return KeepTogether([head, card, SP(10)])

    # =================================================================
    # PART THREE DIVIDER
    # =================================================================
    st += [NT("divider"), PB(), Bookmark("Part Three: The tools", 0)]
    st += section_divider("Three", "The tools",
        "Capture, translate, and build the record",
        "Two levels of capture, a translation system, and the Proof Line. Every tool arrives with a finished example, not an empty box.")
    st += [NT("content"), PB()]

    # 14. TWO-MINUTE QUICK CAPTURE
    st += [Bookmark("The Two-Minute Quick Capture", 1), IconMark(chip_mark(ic_clock_pencil)), SP(6), EY("Tool one"),
        H2("The Two-Minute Quick Capture"),
        RULE(),
        P("The quick capture exists for one reason: to catch the work before it fades, in the two minutes after it happens. It is deliberately small. Five short prompts, no perfect wording required. You are not writing the final version. You are making sure the final version is still possible later."),
        H3("The five prompts"),
    ]
    st += bullets([
        "<b>What happened?</b> The event or piece of work, in a line.",
        "<b>What was my specific contribution or judgment?</b> Your part, not the team&#8217;s.",
        "<b>What changed, improved, became possible, or was prevented?</b> The consequence.",
        "<b>Verifier role or permitted public reference.</b> A role or a public source that could confirm it. Do not store a colleague&#8217;s personal details.",
        "<b>Confidential detail to keep out.</b> Name it, so you remember to leave it out.",
    ])
    st += [SP(5),
        example_card("Completed Quick Capture  ·  Devin A., distribution center supervisor",
            "Operations  ·  captured the same afternoon",
            [("What happened", "Recurring mispicks on the night shift were driving returns. I changed the pick-verification step and the error rate dropped."),
             ("My specific contribution", "I noticed the errors clustered on one workflow, proposed a second scan at pack-out, and ran the two-week trial that proved it out."),
             ("What changed", "Shipping errors on that line fell sharply and stayed down after the change was made permanent."),
             ("Permitted verification", "My operations manager, who approved the rollout. The improvement was later cited in a team update."),
             ("Must stay out", "The internal error dashboards, customer order data, and the returns figures themselves. I keep my own account, not the reports.")]),
        NOTE("Notice what the capture does and does not hold. It holds Devin&#8217;s account and a person who could confirm it. It does not hold a single employer file. That is the pattern for every capture you make."),
    ]
    st += [PB()]

    # 15. FULL CAREER EVIDENCE LEDGER (2 pages)
    st += [Bookmark("The Full Career Evidence Entry", 1), IconMark(chip_mark(ic_form_card)), SP(6), EY("Tool two"),
        H2("The Full Career Evidence Entry"),
        RULE(),
        P("When a piece of work matters enough to keep properly, you expand a quick capture into a full entry. The ledger below has room for everything that makes a contribution legible later. You will not fill every field every time, and you should not try. A strong entry with six good fields beats a padded one with sixteen."),
        H3("The twenty fields, in order"),
        TBL([["Field", "What it captures"],
             ["Date or period", "When the work happened, even approximately"],
             ["Project or work event", "The initiative, responsibility, or moment"],
             ["Situation or need", "The problem or condition you were responding to"],
             ["Why it mattered", "What was at stake if it went unaddressed"],
             ["Formal responsibility", "What you were assigned on paper"],
             ["Actual ownership", "What you truly drove, which is often different"],
             ["Decision or judgment exercised", "The call you made, and the options you weighed"],
             ["Actions taken", "What you actually did"],
             ["People and functions involved", "Who you worked with or influenced, by role"],
             ["Scope and constraint", "Scale, complexity, or the limits you worked within"],
             ["Outcome or observable change", "What was observably different afterward"],
             ["Problem prevented", "The cost, delay, or risk that did not land"],
             ["Quantitative evidence, accurate and permitted", "Numbers, only when accurate and permitted"],
             ["Qualitative evidence or validation", "Feedback, recognition, or credible validation"],
             ["Team result vs. your honest part", "The shared outcome, and your honest share of it"],
             ["Internal wording, before translation", "How it is said inside the company"],
             ["Portable-language version", "How you would say it to an outsider"],
             ["Permitted evidence reference", "Name the permitted source or location. Do not paste the artifact or confidential content here."],
             ["Confidentiality and permission check", "Confirmed nothing restricted is being kept"],
             ["Retrieval tags", "Review, promotion, compensation, resume, interview, biography, transition"]],
            [CONTENT_W*0.34, CONTENT_W*0.66], pad=3.4),
    ]
    st += [PB()]
    # completed full entry example (the People/HR one, start of full sequence)
    st += [SP(6), EY("Tool two, completed"),
        H2("A completed full entry"),
        RULE(),
        P("Here is the same tool, filled in. This is the first half of a full worked sequence that continues on the next pages: quick capture, to full entry, to a portable Proof Line, to a retrieval tag."),
        example_card("Full Career Evidence Entry  ·  Maya O., onboarding program lead",
            "People and HR  ·  measurable and qualitative",
            [("Period", "Second and third quarters of last year."),
             ("Project or work event", "Redesign of the new-hire onboarding program for a growing operations team."),
             ("Situation or need", "New hires were taking a long time to become productive, and early attrition was high. The existing program was a slide deck and a checklist."),
             ("Formal responsibility vs. actual ownership", "On paper I coordinated onboarding logistics. In practice I redesigned the program end to end: the sequence, the first-week plan, the manager&#8217;s role, and the thirty-day check-in."),
             ("Decision or judgment", "I chose to move the program from information delivery to a structured first month with clear milestones, over the easier option of simply updating the deck."),
             ("Outcome or change", "New hires reached full productivity noticeably sooner, and early departures dropped. Managers began asking to use the model for their own teams."),
             ("Quantitative and qualitative evidence", "Time to full productivity improved by a figure I recorded accurately at the time. Two department heads asked to adopt the approach, which I noted as it happened."),
             ("Confidentiality check", "I keep my own account and the fact of the improvement. I do not keep the HR system data, the employee records, or the internal reports the numbers came from."),
             ("Retrieval tags", "Promotion, performance review, resume, biography.")]),
    ]
    st += [PB()]

    # 16. RESPONSIBILITY / JUDGMENT / SCOPE / OUTCOME
    st += [SP(6), EY("Capturing well"),
        H2("Responsibility, judgment, scope, and outcome"),
        RULE(),
        P("Four things separate a memorable entry from a forgettable one. Most records capture the first and skip the rest."),
        H3("Assigned responsibility is where you start, not where you stop"),
        P("Your job description tells a reader what you were supposed to do. It rarely tells them what you actually did. The gap between the two is where most of your real contribution lives. Record the assignment, then record what you drove beyond it."),
        H3("Judgment is the part with no artifact"),
        P("Anyone can list actions. Fewer people can name the decision underneath the actions: the option they chose and the ones they set aside. That choice is often the most valuable thing you did, and it leaves no trace unless you write it down. Capture the call, not only the task."),
        H3("Scope makes size legible"),
        P("A title hides scale. &#8220;Managed the rollout&#8221; could mean two people or two hundred, one region or twelve. Without inventing precision you do not have, note the scope you worked within: how many, how large, how complex, under what constraint. Scope is what lets an outsider size the work correctly."),
        H3("Push past the action to the observable change"),
        P("The weakest entries end with what you did. The strongest end with what became different because you did it. Push every entry one step past the action to the observable change, even when the change is modest. When recording the work, include the effort where it adds useful context and describe the outcome or observable change."),
    ]
    st += [PB()]

    # 17. NO CLEAN METRIC
    st += [SP(6), EY("The hard cases"),
        H2("Capturing work with no clean metric"),
        RULE(),
        P("A great deal of valuable work produces no tidy number. Coordination, judgment, care, and prevention rarely come with a percentage attached. This does not make the work unrecordable. It means you describe the change in credible, concrete terms instead of forcing a figure that is not real."),
        H3("Describe the before and the after"),
        P("When there is no metric, there is almost always a contrast. What was true before your work, and what was true after? &#8220;The handoff between the two teams kept failing; after I redesigned it, work stopped falling through the gap&#8221; is credible evidence with no number in it, because a reader can picture both states."),
        H3("Name the specific consequence"),
        P("Vague improvement is not evidence. Specific improvement is. Not &#8220;made things better,&#8221; but &#8220;the weekly report that used to take two people a full day now takes one person an hour.&#8221; A concrete, honest particular is more persuasive than a round number you cannot defend."),
        SP(2),
        CO("Never invent the number",
            "If you do not have an accurate figure, do not manufacture one. An invented metric is the fastest way to lose a reader&#8217;s trust, because the first careful question exposes it. A well-described qualitative result is stronger than a fabricated quantitative one. Accuracy is the entire value of this record.",
            bg="navy"),
    ]
    st += [PB()]

    # 18. PROBLEMS PREVENTED / INVISIBLE
    st += [SP(6), EY("The invisible work"),
        H2("Problems prevented and invisible contributions"),
        RULE(),
        P("The most undervalued work in any organization is the problem that never happened. Prevention leaves no artifact by definition. The outage you caught before it spread, the error you flagged before it reached a customer, the misunderstanding you resolved before it became a conflict: none of these produce a result you can point to, because the point is that there was no result."),
        H3("Record the risk, the catch, and the likely path"),
        P("To capture prevention honestly, name three things: the risk that was forming, what you noticed or did, and the outcome that was on its way if no one had acted. &#8220;A misconfiguration would have exposed internal access; I caught it in review and it was corrected before anything was affected&#8221; is complete evidence of judgment, with nothing invented and nothing exposed."),
        H3("Stay honest about certainty"),
        P("Prevention invites overstatement, so hold the line. You do not know for certain what would have happened. Say &#8220;would likely have&#8221; rather than &#8220;definitely would have.&#8221; The honest version is still strong, and it is the version that survives a follow-up question."),
        SP(2),
        example_card("Prevention, captured honestly  ·  Theo R., security analyst",
            "Technology and cybersecurity  ·  no clean metric, problem prevented",
            [("The risk forming", "During a routine review I found that a group of accounts had been granted more access than their roles required."),
             ("What I did", "I traced how the access had been assigned, flagged it, and worked with the owning team to correct it and to close the gap that had allowed it."),
             ("The path avoided", "Left in place, the excess access would likely have become a real exposure. It was corrected before it was used."),
             ("Kept vs. left out", "I keep my account of the judgment and the fix. I keep no logs, no account names, no security configuration, and no internal tooling detail.")]),
    ]
    st += [PB()]

    # 19. TEAM VS INDIVIDUAL
    st += [SP(6), EY("Honest credit"),
        H2("Separating a team result from your part"),
        RULE(),
        P("Most meaningful work is shared, and shared work creates a recording problem. Claim the whole result and you are exaggerating. Claim nothing and you disappear from your own record. The skill is to state the team&#8217;s outcome honestly and then name your specific part within it, without inflating and without vanishing."),
        H3("Two sentences, always in this order"),
        P("First, the shared result: what the group achieved. Second, your contribution: the particular thing you drove inside it. &#8220;The team delivered the platform migration on schedule. My part was owning the data-integrity plan and making the call to phase the cutover, which kept us from a rushed switch.&#8221; Both sentences are true. Neither one steals from the other."),
        SP(3),
        example_card("A manager separating the two  ·  Grace W., engineering manager",
            "Management  ·  team outcome and honest individual contribution",
            [("The team result", "My team of nine shipped a long-delayed platform migration, on time, with no major incidents."),
             ("My actual contribution", "I did not write the migration. My part was sequencing the work, protecting the team from mid-project scope changes, and deciding to run a phased cutover instead of a single switch."),
             ("The judgment inside it", "The phased approach was mine to argue for and mine to own. It is the reason a risky switch did not become a bad weekend."),
             ("Portable version", "Led a nine-person team through a complex platform migration, delivered on schedule with no major incidents, and set the phased rollout approach that protected reliability during the transition.")]),
    ]
    st += [PB()]

    # =================================================================
    # 20. TRANSLATION SYSTEM
    # =================================================================
    st += [Bookmark("From internal language to portable language", 1), IconMark(chip_mark(ic_translate_arrow)), SP(6), EY("Translate"),
        H2("From internal language to portable language"),
        RULE(),
        P("A record only your current employer can read is a record that expires when you leave. Translation is the skill of saying the same true thing in words an outsider can follow. It is not embellishment and it is not lying. It is the difference between a private shorthand and a description that travels."),
        H3("Eight translation moves, plus one protection rule"),
        P("Most entries need one of the eight translation moves below. The final line is different: it is a protection rule for sensitive information."),
        TBL([["Move", "Turn this", "Into this"],
             ["Name to function", "&#8220;Ran Project Northwind&#8221;", "&#8220;Led the customer-data migration&#8221;"],
             ["Assignment to contribution", "&#8220;Responsible for reporting&#8221;", "&#8220;Rebuilt the reporting so leaders could act on it&#8221;"],
             ["Activity to consequence", "&#8220;Held weekly reviews&#8221;", "&#8220;Caught risks early enough to prevent slippage&#8221;"],
             ["Team to your part", "&#8220;We launched it&#8221;", "&#8220;I owned the rollout plan for the launch&#8221;"],
             ["Acronym to meaning", "&#8220;Cleared the KYC backlog&#8221;", "&#8220;Cleared a backlog of customer identity checks&#8221;"],
             ["&#8220;Helped with&#8221; to real role", "&#8220;Helped with the audit&#8221;", "&#8220;Prepared the evidence and answered the auditors directly&#8221;"],
             ["No number to credible detail", "&#8220;Improved the process&#8221;", "&#8220;Cut a two-day task to a few hours&#8221;"],
             ["Number to scale", "&#8220;Handled 40 accounts&#8221;", "&#8220;Managed 40 enterprise accounts across three regions&#8221;"],
             ["Sensitive to permitted", "&#8220;Fixed the breach in system X&#8221;", "&#8220;Resolved a security issue and closed the gap behind it&#8221;"]],
            [CONTENT_W*0.24, CONTENT_W*0.38, CONTENT_W*0.38]),
        SP(4),
        CO("Why the last line is different",
           "The first eight moves make your work clearer. The last one keeps you safe. Turning sensitive detail into a permitted, high-level description is never a way to smuggle restricted information out in disguise. If the only accurate version would expose something you may not keep, the correct move is to omit it, not to reword it.",
           bg="navy"),
    ]
    st += [PB()]

    # 21. PROOF LINE BUILDER
    st += [Bookmark("The Proof Line", 1), IconMark(chip_mark(ic_prooflines)), SP(6), EY("Build"),
        H2("The Proof Line"),
        RULE(),
        P("A Proof Line is a single, plain-language sentence that carries the most useful parts of an entry in a form you can drop into a review, a resume, or a conversation. It is the portable end product of everything the record holds. You build it by combining, in whatever order reads well, up to five ingredients."),
        H3("The five ingredients"),
    ]
    st += bullets([
        "<b>The condition.</b> The problem or situation you were responding to.",
        "<b>Your part.</b> The contribution, decision, or judgment that was yours.",
        "<b>The scope or constraint.</b> The size or the limits you worked within.",
        "<b>The outcome.</b> What changed, or what was prevented.",
        "<b>The support.</b> The permitted evidence or validation, when you have it.",
    ])
    st += [SP(4), H3("Built in front of you"),
        TBL([["Ingredient", "Maya&#8217;s onboarding work"],
             ["Condition", "New hires were slow to become productive and left early"],
             ["Your part", "Redesigned the onboarding program end to end"],
             ["Scope", "For a growing operations team, across the full first month"],
             ["Outcome", "Faster time to productivity and lower early attrition"],
             ["Support", "Adopted by two other department heads"]],
            [CONTENT_W*0.24, CONTENT_W*0.76]),
        SP(5),
        CO("Maya&#8217;s Proof Line",
           "&#8220;Redesigned new-hire onboarding for a growing operations team, cutting time to full productivity and reducing early attrition, with the model later adopted by two other departments.&#8221;",
           bg="sand", bar=GOLD),
        SP(4),
        NOTE("A Proof Line does not need a number to be strong, and it must never contain an invented one. It also never claims sole credit for a shared result. If a line would only sound impressive by overstating your ownership, it is not finished. It is wrong."),
    ]
    st += [PB()]

    # 22. BEFORE-AND-AFTER TRANSLATION EXAMPLES
    st += [SP(6), EY("See it work"),
        H2("Before and after"),
        RULE(),
        P("Translation is easiest to learn by watching it happen. Each pair below keeps the same underlying truth. The weaker version is internal, vague, or overclaimed. The stronger version is portable, specific, and honest."),
        TBL([["Weaker (internal, vague, or overclaimed)", "Stronger (portable, specific, honest)"],
             ["&#8220;Owned the Q3 OKR for the CS org&#8221;", "&#8220;Set and delivered the quarter&#8217;s top goal for the customer support team&#8221;"],
             ["&#8220;Helped migrate to the new platform&#8221;", "&#8220;Owned the data-integrity plan for a platform migration and phased the cutover to protect reliability&#8221;"],
             ["&#8220;Improved team efficiency&#8221;", "&#8220;Redesigned a weekly reporting task from two days to a few hours&#8221;"],
             ["&#8220;Single-handedly saved the launch&#8221;", "&#8220;Made the call to delay one day to fix a data issue, which kept the launch from shipping broken&#8221;"],
             ["&#8220;Handled a security thing&#8221;", "&#8220;Found and corrected an access gap in review before it could be exploited&#8221;"],
             ["&#8220;Did a lot of cross-functional work&#8221;", "&#8220;Coordinated three teams to resolve a recurring handoff failure between them&#8221;"]],
            [CONTENT_W*0.5, CONTENT_W*0.5]),
        SP(4),
        P("Read the right-hand column again and notice what none of them do. None invents a number. None claims a whole team&#8217;s work. None exposes a name, a system, or a file. They are simply the true thing, said well enough to travel."),
    ]
    st += [PB()]

    # =================================================================
    # 23. SIX COMPLETED EXAMPLES (already 3 shown: Devin, Maya, Theo, Grace)
    # add Priya (finance/audit, sensitive omission) and Sam (IC judgment),
    # and the second full sequence for Theo.
    # =================================================================
    st += [NT("divider"), PB(), Bookmark("Part Four: Worked examples", 0)]
    st += section_divider("Four", "Worked examples",
        "The record, filled in across real work",
        "Different functions, different levels, one discipline. Two examples run the full sequence from capture to retrieval tag.")
    st += [NT("content"), PB()]

    st += [SP(6), EY("Examples"),
        H2("Two more completed examples"),
        RULE(),
        P("You have already seen four people&#8217;s records take shape: Devin in operations, Maya in people and HR, Theo in security, and Grace in engineering management. Two more complete the set, chosen to show the hardest cases: work where the right choice is to leave detail out, and work whose whole value is judgment rather than output."),
        example_card("Priya N., senior internal auditor",
            "Finance, audit, and risk  ·  a sensitive context, handled by omission",
            [("The work", "I led an internal audit of a financial process and identified a control weakness that had gone unnoticed for some time."),
             ("The judgment", "I decided which findings were material enough to escalate and how to frame them so they would be acted on rather than argued with."),
             ("Why this one is delicate", "The subject matter is sensitive and specific to my employer. The correct record is my own high-level account, not the findings, the figures, or the systems involved."),
             ("Portable version", "Led an internal audit that surfaced a significant control weakness, and framed the findings so leadership acted on them. No confidential detail retained."),
             ("Kept vs. left out", "Kept: my role, my judgment, the fact of the outcome. Left out: the specific process, the numbers, the named systems, and every working paper.")]),
        example_card("Sam B., clinical research coordinator",
            "Healthcare and research  ·  value from coordination and influence, not output",
            [("The work", "A study was stalling because three groups (clinical staff, data management, and an external partner) were working from different assumptions."),
             ("My actual contribution", "I had no formal authority over any of the three. My part was seeing why they were stuck, building a shared plan, and keeping it moving without a title that required them to listen."),
             ("The outcome", "The study got back on schedule. My name appears on no deliverable, because the contribution was the coordination itself."),
             ("Portable version", "Coordinated three functions with no formal authority to unblock a stalled research study and return it to schedule, working through influence rather than mandate.")]),
    ]
    st += [PB()]

    # Second full sequence: Theo
    st += [SP(6), EY("Full sequence, end to end"),
        H2("One item, all the way through"),
        RULE(),
        P("Here is a single piece of work carried through the entire system: quick capture, to full entry, to Proof Line, to retrieval tag. This is the second full sequence, using Theo&#8217;s prevention work from earlier."),
        example_card("1 · Quick Capture  ·  Theo R., security analyst",
            "Two minutes, the same day",
            [("What happened", "Found over-broad access on a set of accounts during a routine review."),
             ("My contribution", "Traced how it happened, flagged it, and drove the fix and the process gap behind it."),
             ("Changed / prevented", "A likely exposure was prevented before the excess access could be used."),
             ("Verification", "The owning team&#8217;s lead, who made the correction with me."),
             ("Stays out", "All logs, account names, tooling, and configuration.")]),
        example_card("2 · Full Entry  ·  the fields that matter here",
            "Expanded when the item proved worth keeping",
            [("Formal vs. actual", "Assigned to routine access reviews; actually drove a correction and a process change."),
             ("Judgment", "Chose to treat a quiet finding as urgent and to fix the cause, not just the instance."),
             ("Outcome", "The excess access was removed, and the process gap that allowed it was closed."),
             ("Evidence", "No clean metric. Credible qualitative outcome, confirmed by the owning team.")]),
        example_card("3 · Proof Line  →  4 · Retrieval Tag",
            "The portable end product, tagged for later",
            [("Proof Line", "&#8220;During a routine access review, I found and corrected over-broad account access and closed the process gap behind it, preventing a likely exposure before the excess access could be used.&#8221;"),
             ("Retrieval tags", "Performance review, promotion, resume, interview (judgment and prevention).")]),
    ]
    st += [PB()]

    # =================================================================
    # PART FIVE DIVIDER: routines & use
    # =================================================================
    st += [NT("divider"), PB(), Bookmark("Part Five: The routines and the use", 0)]
    st += section_divider("Five", "The routines and the use",
        "Keep it current, and use it when it counts",
        "An hour to set up, a few minutes a month, a review each quarter. Then the record earns its keep at the moments that decide careers.")
    st += [NT("content"), PB()]

    # 24. 60-MINUTE SETUP
    st += [Bookmark("The complete 60-minute setup", 1), IconMark(chip_mark(ic_clock60)), SP(6), EY("Start here"),
        H2("The complete 60-minute setup"),
        RULE(),
        P("This is the first hour. Follow it in order and you will finish with a working system and your first real entries. It is not a promise that you can reconstruct a whole career in sixty minutes. It is a promise that you can leave the hour with the system running and something true already in it."),
        TBL([["Time", "What you do"],
             ["0&#8211;10 min", "Read the permission rule and the three tiers again. Choose a private home you control and turn on a password and multifactor authentication. Storage comes after permission, not before."],
             ["10&#8211;20 min", "Sweep your own memory and permitted sources for the last few months. No employer files. Just what you can recall and what is already public: projects, decisions, moments that mattered."],
             ["20&#8211;40 min", "Write at least three Quick Captures from that sweep. Rough is fine. Speed beats polish."],
             ["40&#8211;50 min", "Expand your strongest capture into a Full Entry. Fill only the fields that apply."],
             ["50&#8211;57 min", "Translate that entry into one portable Proof Line."],
             ["57&#8211;60 min", "Schedule the next Monthly Proof Sweep and the next Quarterly Proof Review. Put both on a calendar you control."]],
            [CONTENT_W*0.16, CONTENT_W*0.84]),
        SP(4),
        CO("What you have at minute sixty",
           "A private system you control, three or more captured items, one full entry, one portable Proof Line, and two recurring dates. That is a working record. Everything after this is maintenance.",
           bg="navy"),
    ]
    st += [PB()]

    # 25 & 26. ROUTINES
    st += [IconMark(chip_mark(ic_calendar_arrow)), SP(6), EY("Keep it current"),
        H2("The monthly and quarterly routines"),
        RULE(),
        P("A record is only useful if it stays current, and it only stays current if maintaining it is nearly effortless. Two routines do this. The monthly sweep is short and additive. The quarterly review is longer and corrective. Neither one asks you to diagnose your career. They only keep the evidence honest."),
        H3("The Monthly Proof Sweep  ·  about 10 to 15 minutes"),
    ]
    st += bullets([
        "Look back over the month&#8217;s projects, decisions, feedback, changes, and problems you helped prevent.",
        "Add Quick Captures for anything worth keeping. Rough notes, quickly.",
        "Expand the single most significant item into a Full Entry.",
        "Run the confidentiality check: is everything here permitted?",
        "Tag each item for how you might retrieve it later.",
    ])
    st += [SP(4), H3("The Quarterly Proof Review  ·  about 30 minutes")]
    st += bullets([
        "Read the quarter&#8217;s entries in one sitting.",
        "Remove duplicates and anything too vague to be useful.",
        "Correct overstatement and add missing context while you still remember it.",
        "Translate the strongest entries into portable Proof Lines.",
        "Note where evidence is thin, without drawing any conclusion about your career from the gap.",
        "Write a short quarterly index of your best entries, and set the date for the next review.",
    ])
    st += [SP(4),
        CO("What this is not",
           "The quarterly review is housekeeping, not a verdict. Noticing that you have little evidence of a certain kind of work is a prompt to capture more of it, nothing more. This record organizes and translates what happened. It does not tell you what your career means. That is a different tool, and a later page points to it quietly.",
           bg="sand", bar=GOLD),
    ]
    st += [PB()]

    # 27. RETRIEVAL
    st += [IconMark(chip_mark(ic_record_search)), SP(6), EY("Use it"),
        H2("Retrieving the right evidence"),
        RULE(),
        P("The whole point of tagging is this moment: something is about to happen, and you need the right entries fast. This section tells you which kinds of entries to pull for each occasion. It is a guide to retrieval, not a course in how to interview, negotiate, or write a resume. It gets you the raw material. What you do with it is yours."),
        TBL([["When this arrives", "Pull entries that show"],
             ["Performance review", "Outcomes and prevented problems from the review period, with honest scope"],
             ["Promotion case", "Judgment, ownership beyond your title, and work at the next level"],
             ["Compensation discussion", "Scope, results, and contributions others have recognized"],
             ["Internal application", "Work relevant to the new team, translated out of your current group&#8217;s language"],
             ["Resume preparation", "Your strongest Proof Lines across roles, each one honest and portable"],
             ["Interview preparation", "Entries with a clear situation, your decision, and the result, ready to tell aloud"],
             ["Biography or introduction", "A few durable, senior-sounding contributions stated plainly"],
             ["Proposal or portfolio", "Permitted outcomes that show the kind of work you deliver"],
             ["Unexpected transition", "Everything, quickly, because the record is now the only copy you have"]],
            [CONTENT_W*0.30, CONTENT_W*0.70]),
    ]
    st += [GAP()]

    # 28. IF ACCESS ALREADY DISAPPEARED
    st += [SP(6), EY("Starting late"),
        H2("If your access has already disappeared"),
        RULE(),
        P("Perhaps you are reading this after a change, not before one. The record you wish you had does not exist, and the systems that held the details are closed. This is recoverable. It is not as complete as capturing in real time, but a great deal can be reconstructed honestly from what is still yours."),
        H3("Work only from what you are permitted to use"),
        P("Your own memory is yours. Publicly disclosed outcomes are usable. Anything a former employer expressly permitted you to keep is usable. What is not usable is a copy of anything you took, or access you were not meant to retain. The rule does not relax because the timing is inconvenient."),
    ]
    st += bullets([
        "Reconstruct by period. Take each role or year in turn and recall its major projects and decisions.",
        "Anchor to moments you remember clearly: a hard call, a launch, a problem you caught, a piece of feedback.",
        "Write Quick Captures from memory, then expand the strongest into full entries.",
        "Mark anything uncertain as uncertain. An honest approximate record is worth far more than a confident wrong one.",
        "Then start capturing in real time, so you never have to reconstruct again.",
    ])
    st += [SP(4),
        NOTE("Reconstruction has a ceiling, and it is worth naming: you will not recover everything, and you should not pretend to. Capture what you can defend, note what you cannot, and let the going-forward habit do the rest."),
    ]
    st += [PB()]

    # 29. OPTIONAL AI PROMPT (own page). The prompt sits in a table-based box so
    # its height is exact; heading, box, and closing note occupy separate,
    # non-overlapping vertical regions. (The old bordered-Paragraph box drew
    # taller than its measured height and overlapped its neighbours.)
    _prompt_para = Paragraph(
        "&#8220;You are helping me describe my own work accurately for my private career record. I will give you only non-confidential information about what I did. "
        "Work only with what I provide. If context is missing, ask me for it rather than inventing anything. "
        "Never invent numbers, percentages, or results. "
        "Preserve my actual level of ownership, and keep any team result separate from my individual contribution. "
        "Translate internal language into plain, portable language an outsider could understand. "
        "Give me a few accurate versions for different uses: a short resume line, a spoken interview version, and a one-line summary. "
        "Flag anything that sounds inflated, vague, or unsupported so I can correct it.&#8221;",
        ParagraphStyle("prompt", fontName="DM", fontSize=9.6, textColor=INK, leading=15))
    _prompt_box = Table([[_prompt_para]], colWidths=[CONTENT_W])
    _prompt_box.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),HexColor("#FBF3E2")), ("BOX",(0,0),(-1,-1),1,GOLD),
        ("LEFTPADDING",(0,0),(-1,-1),14),("RIGHTPADDING",(0,0),(-1,-1),14),
        ("TOPPADDING",(0,0),(-1,-1),12),("BOTTOMPADDING",(0,0),(-1,-1),12)]))
    st += [SP(6), EY("Optional"),
        H2("An optional, privacy-conscious AI prompt"),
        RULE(),
        P("Everything in this guide works without any AI. This tool is optional, and it is for one narrow job: helping you translate an entry you have already written into portable language. Before the prompt, the rule that governs it."),
        CO("Before you use it",
           "Never paste employer names, customer names, colleague names, proprietary detail, employee information, sensitive metrics, code, security information, or any confidential material into an AI system. Give it only your own non-confidential account, already stripped of anything you may not keep. The permission rules in this guide apply to AI tools exactly as they apply to everything else.",
           bg="navy"),
        SP(6),
        KeepTogether([H3("The prompt"), SP(3), _prompt_box]),
        SP(10),
        NOTE("The AI does not decide what is true. You do. Treat every version it returns as a draft to check against your own memory and this guide&#8217;s rules, never as a finished record."),
    ]
    st += [PB()]

    # 30. REUSABLE LEDGER PAGES (fillable, in handbook)
    st += [SP(6), EY("Fill it in"),
        H2("Reusable ledger pages"),
        RULE(),
        P("Use the fillable pages that follow to begin now. The standalone Career Evidence Ledger, included with your purchase, repeats these same forms so you can reuse them indefinitely without reprinting the handbook. Every response field is fillable on screen and prints cleanly if you would rather write by hand."),
        SP(6),
        Paragraph("Two-Minute Quick Capture", ParagraphStyle("lgh", fontName="CG-Semi", fontSize=15, textColor=NAVY, leading=18, spaceAfter=2)),
        Paragraph("One capture per page. Print or copy this page whenever you need another.", S["fieldhint"]),
        SP(8),
    ]
    st += quick_capture_fields(S, "hb_qc")
    st += [PB()]
    # Full Career Evidence Entry — three pages, twenty taught fields, identical to the ledger
    p1, p2, p3 = full_entry_pages(S, "hb_fe")
    st += [SP(6), EY("Fill it in"),
        H2("Full Career Evidence Entry"), RULE(),
        Paragraph("Page one of three. Expand a Quick Capture into a complete entry, and fill only the fields that apply.", S["fieldhint"]), SP(8)]
    st += p1
    st += [PB()]
    st += [SP(6), EY("Fill it in, continued"),
        H2("Full Career Evidence Entry"), RULE(),
        Paragraph("Page two of three.", S["fieldhint"]), SP(8)]
    st += p2
    st += [PB()]
    st += [SP(6), EY("Fill it in, continued"),
        H2("Full Career Evidence Entry"), RULE(),
        Paragraph("Page three of three.", S["fieldhint"]), SP(8)]
    st += p3
    st += [PB()]

    # 31. OPERATING SUMMARY
    st += [Bookmark("The Keep the Proof operating summary", 1), SP(6), EY("One page"),  # (no tool chip: not in the RC3 icon set)
        H2("The Keep the Proof operating summary"), RULE(),
        P("Everything in this guide, on a single page you can return to."),
        SP(2),
        H3("The rule"),
        P("Keep your own account and what you are permitted to retain. Never copy or reconstruct what your employer owns. When unsure, leave it out."),
        H3("The workflow"),
        P("<b>Capture</b> it fresh. <b>Clarify</b> your part from the team&#8217;s. <b>Translate</b> it into portable words. <b>Protect</b> by keeping only what is permitted. <b>Retrieve</b> it by tagging for later."),
        H3("The tools"),
        P("A two-minute Quick Capture for speed. A Full Entry for what matters. A translation into portable language. A Proof Line as the portable end product."),
        H3("The rhythm"),
        P("An hour to set up. Ten to fifteen minutes each month to add. Thirty minutes each quarter to correct and index."),
        H3("The use"),
        P("Pull the right entries for reviews, promotions, compensation, internal moves, resumes, interviews, biographies, proposals, and sudden change."),
        SP(4),
        CO("If you remember only one line",
           "A secure personal device does not make information yours to retain. Permission comes first. Everything else is craft.",
           bg="navy"),
    ]
    st += [PB()]

    # 32. WHERE IT ENDS (boundary + quiet Field Kit route)
    st += [Bookmark("Where Keep the Proof ends", 1), SP(6), EY("The edge of the tool"),
        H2("Where Keep the Proof ends"), RULE(),
        P("This guide has a deliberate boundary, and naming it is part of using it well. Keep the Proof organizes and translates the record of your work. It does not interpret what that record means for your position, your direction, or your next move. Those are real and important questions. They are simply not this tool&#8217;s questions."),
        H3("What this guide answers"),
    ]
    st += bullets([
        "What happened, and what was my contribution?",
        "What decision or judgment did I exercise?",
        "What changed, and what evidence supports it?",
        "How do I describe it truthfully in portable language?",
        "Where and how should I keep a permitted record of it?",
    ])
    st += [SP(3), H3("What it deliberately does not answer")]
    st += bullets([
        "Whether my career is stalled, or what state it is in.",
        "Whether this role is still building me, or whether I should stay or leave.",
        "What move I should make, or what my next strategy should be.",
    ])
    st += [SP(4),
        CO("A quiet pointer, not a sales pitch",
           "Keep the Proof organizes and translates the record. If you later want to interpret what your current work is actually building toward, a separate tool from The Density Group, the Capability Formation Field Kit, is designed for exactly that reading. It is a different job for a different day. This guide&#8217;s work is done when your record is honest, portable, and safe to keep.",
           bg="sand", bar=GOLD),
    ]
    st += [PB()]

    # 33 & 34. ABOUT + CLOSING
    st += [Bookmark("About Temidayo Afonja", 0), SP(6), EY("About the author"),
        H2("About Temidayo Afonja"), RULE(),
        P("Temidayo Afonja is the Founder and Principal of The Density Group. For eighteen years, Temidayo has worked across Big Four consulting, life sciences, and technology, close to where talent decisions get made, at the intersection of workforce strategy, organizational design, and how careers actually form."),
        P("That path into this work began in IT audit and federal governance, and moved through cybersecurity workforce strategy before that field had its current name. That background is the reason the confidentiality and information-risk standard in this guide is treated with the seriousness it deserves, and the reason it is careful never to overstate what any guide can settle for you. Keep the Proof is educational, not legal advice, and it cannot interpret your specific agreements or your employer&#8217;s policies."),
        P("Keep the Proof grew out of a pattern that repeats in room after room: capable people who had done the work and could no longer prove it, reaching for details that had already gone. This guide is the discipline more of them needed."),
        SP(8), HRule(CONTENT_W, color=HAIR, thick=0.8, space=10),
        Paragraph("Keep the record while the facts are still yours to keep.", ParagraphStyle("close", fontName="CG-Semi", fontSize=17, textColor=NAVY, leading=22, spaceAfter=6)),
        Paragraph("Temidayo Afonja  ·  " + "temidayoafonja.com", ParagraphStyle("closeurl", fontName="DM-Med", fontSize=10, textColor=RUST, leading=14)),
    ]
    return st
