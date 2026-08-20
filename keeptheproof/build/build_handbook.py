#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Keep the Proof handbook (customer PDF). Original content, brand
system, fillable where appropriate. Run: python3 build_handbook.py <out.pdf> <buildtime>
"""
import sys
from ktp import *
from reportlab.platypus import (Paragraph, Spacer, NextPageTemplate, PageBreak,
    Table, TableStyle, KeepTogether, Flowable)
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.units import inch

OUT = sys.argv[1] if len(sys.argv) > 1 else "handbook.pdf"
BUILDTIME = sys.argv[2] if len(sys.argv) > 2 else "Monday, August 17, 2026 at 1:05 PM"
VERSION = "Version 1.0.1"
REVLINE = f"{VERSION}  ·  Revised {BUILDTIME} CT"
URL = "temidayoafonja.com"

register_fonts()
S = styles()
Field._seen = set()

# ---- content shortcuts ----
def P(t, j=False): return Paragraph(t, S["body_j"] if j else S["body"])
def LEAD(t): return Paragraph(t, S["lead"])
def H2(t): return Paragraph(t, S["h2"])
def H3(t): return Paragraph(t, S["h3"])
def EY(t): return Paragraph(t.upper(), S["eyebrow"])
def KI(t): return Paragraph(t.upper(), S["kicker"])
def NOTE(t): return Paragraph(t, S["note"])
def SP(h=6): return Spacer(1, h)
def bullets(items, style=None):
    st = style or S["bullet"]
    return [Paragraph(f"<font color='#C1440E'>•</font>&nbsp;&nbsp;{it}", st) for it in items]
def CO(title, body, bg="navy", bar=RUST): return KeepTogether([build_callout(title, body, S, bg=bg, bar=bar)])
def GAP(h=24): return Spacer(1, h)  # soft section break when flowing sections on one page
def TBL(rows, cw, **kw): return build_table(rows, S, cw, **kw)
def RULE(w=CONTENT_W, c=HAIR, t=0.8): return HRule(w, color=c, thick=t, space=8)

def section_divider(num, part, title, blurb):
    """Navy full-bleed divider (rendered on divider template)."""
    fls = [SP(150),
           Paragraph(f"PART {num}", ParagraphStyle("dv_e", fontName="DM-Bold", fontSize=11,
                     textColor=GOLD, leading=15)),
           Paragraph(part, ParagraphStyle("dv_p", fontName="CG-Semi", fontSize=15,
                     textColor=CREAMSOFT, leading=19, spaceAfter=18)),
           Paragraph(title, ParagraphStyle("dv_t", fontName="CG-Semi", fontSize=34,
                     textColor=CREAM, leading=38)),
           RustTab(64), SP(10),
           Paragraph(blurb, ParagraphStyle("dv_b", fontName="DM", fontSize=11.5,
                     textColor=CREAMSOFT, leading=17))]
    return fls

def workflow_strip():
    steps = [("1","Capture","Record it while the facts are fresh."),
             ("2","Clarify","Separate the team result from your part."),
             ("3","Translate","Put it in words an outsider understands."),
             ("4","Protect","Keep only what you are permitted to hold."),
             ("5","Retrieve","Tag it so you can find it when it matters.")]
    cells = []
    for n, name, desc in steps:
        inner = [Paragraph(n, ParagraphStyle("wf_n", fontName="CG-Semi", fontSize=22, textColor=GOLD, leading=24)),
                 Paragraph(name, ParagraphStyle("wf_h", fontName="DM-Bold", fontSize=10, textColor=CREAM, leading=13, spaceBefore=2, spaceAfter=3)),
                 Paragraph(desc, ParagraphStyle("wf_d", fontName="DM", fontSize=8.2, textColor=CREAMSOFT, leading=10.8))]
        cells.append(inner)
    w = CONTENT_W/5
    t = Table([cells], colWidths=[w]*5)
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),NAVY),("VALIGN",(0,0),(-1,-1),"TOP"),
        ("LEFTPADDING",(0,0),(-1,-1),12),("RIGHTPADDING",(0,0),(-1,-1),10),
        ("TOPPADDING",(0,0),(-1,-1),13),("BOTTOMPADDING",(0,0),(-1,-1),13),
        ("LINEAFTER",(0,0),(-2,-1),0.7,HexColor("#2C3B54"))]))
    return t

def tier_block():
    rows = [
        [Paragraph("KEEP", S["tbl_h"]), Paragraph("Your own high-level recollection of what you did, decisions you made, problems you helped prevent, publicly disclosed outcomes, and anything your employer has expressly permitted you to retain.", S["tbl"])],
        [Paragraph("CARE", S["tbl_h"]), Paragraph("Numbers, client or project detail, and internal context that may be sensitive. Seek permission, use only what is already public, or leave it out. When you are unsure, treat it as the next tier.", S["tbl"])],
        [Paragraph("NEVER", S["tbl_h"]), Paragraph("Source code, credentials, security settings, customer or employee data, unreleased product detail, internal financials, privileged or legal material, trade secrets, and any document or file owned by your employer. Never copy, forward, screenshot, download, or reconstruct these anywhere.", S["tbl"])],
    ]
    t = Table(rows, colWidths=[86, CONTENT_W-86])
    t.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("BACKGROUND",(0,0),(0,0),BLUE),("BACKGROUND",(0,1),(0,1),GOLD),("BACKGROUND",(0,2),(0,2),RUST),
        ("TEXTCOLOR",(0,0),(0,-1),CREAM),
        ("BACKGROUND",(1,0),(1,0),HexColor("#EEF3F8")),("BACKGROUND",(1,1),(1,1),HexColor("#FBF3E2")),("BACKGROUND",(1,2),(1,2),HexColor("#FBEBE3")),
        ("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),
        ("TOPPADDING",(0,0),(-1,-1),9),("BOTTOMPADDING",(0,0),(-1,-1),9),
        ("LINEBELOW",(0,0),(-1,-1),3,PAPER),("LINEBEFORE",(1,0),(1,0),0,BLUE),
    ]))
    # relabel header cells as tier names in cream bold
    return t

story = []

# =====================================================================
# 1. COVER
# =====================================================================
class Cover(Flowable):
    def __init__(self): super().__init__(); self.width=PAGE_W; self.height=PAGE_H
    def wrap(self,aw,ah): return (0,0)
    def drawOn(self, canvas, x, y, _sW=0):
        # The cover paints at absolute page coordinates. The base Flowable.drawOn
        # would translate the canvas to the frame cursor (top of a full-page
        # frame), pushing every string a full page height off the top and
        # leaving a blank navy page. Draw directly on the untranslated canvas.
        self.canv = canvas
        self.draw()
    def draw(self):
        c=self.canv
        # motif top-left
        record_motif(c, MARGIN, PAGE_H-120, w=52)
        c.setFont("DM-Bold", 11); c.setFillColor(GOLD)
        c.drawString(MARGIN, PAGE_H-190, "A  6 0 - M I N U T E   C A R E E R   E V I D E N C E   S Y S T E M")
        # title
        c.setFont("CG-Semi", 74); c.setFillColor(CREAM)
        c.drawString(MARGIN-2, PAGE_H-320, "Keep the")
        c.drawString(MARGIN-2, PAGE_H-392, "Proof")
        # rust rule
        c.setFillColor(RUST); c.rect(MARGIN, PAGE_H-430, 88, 5, fill=1, stroke=0)
        # subtitle
        c.setFont("CG", 21); c.setFillColor(HexColor("#D8D2C4"))
        c.drawString(MARGIN, PAGE_H-476, "How to Track Your Work Accomplishments")
        c.drawString(MARGIN, PAGE_H-504, "Before You Need a Resume")
        # bottom promise
        c.setFont("DM", 11); c.setFillColor(CREAMSOFT)
        c.drawString(MARGIN, 150, "Build a private, usable record of your work before a review,")
        c.drawString(MARGIN, 133, "promotion, job search, or unexpected change forces you to")
        c.drawString(MARGIN, 116, "reconstruct it from memory.")
        c.setFont("DM-Bold", 10.5); c.setFillColor(GOLD)
        c.drawString(MARGIN, 74, "Temidayo Afonja")
        c.setFont("DM", 9.5); c.setFillColor(CREAMSOFT)
        c.drawRightString(PAGE_W-MARGIN, 74, URL)
        uw = c.stringWidth(URL, "DM", 9.5)
        c.linkURL(f"https://{URL}", (PAGE_W-MARGIN-uw, 71, PAGE_W-MARGIN, 85), relative=0, thickness=0)

story += [Bookmark("Cover", 0), Cover(), NextPageTemplate("content"), PageBreak()]

# =====================================================================
# 2. COPYRIGHT / DISCLAIMER / VERSION
# =====================================================================
story += [SP(6), EY("Keep the Proof"),
    Paragraph("The record and the fine print", S["h2"]), RULE(),
    H3("Copyright"),
    P(f"Keep the Proof: How to Track Your Work Accomplishments Before You Need a Resume. {VERSION}. Copyright &#169; 2026 Temidayo Afonja. All rights reserved. This document is licensed for the personal use of the individual purchaser. Please do not resell, redistribute, or republish it."),
    H3("What this guide is, and what it is not"),
    P("This is an educational guide to keeping a private, permitted record of your own work. It is not legal advice. It cannot interpret your specific employment agreement, your non-disclosure obligations, your employer&#8217;s policies, or the laws that apply where you work. Where a question of permission is genuinely unclear, treat that as a signal to leave the information out and to ask someone qualified, such as your manager, your human resources team, or an attorney."),
    H3("A note on confidentiality before you begin"),
    P("Everything in this system is built on one rule: you record only your own recollection of your work and information you are permitted to keep. You will be asked, repeatedly, not to copy, forward, photograph, download, screenshot, or reconstruct anything your employer owns. That rule holds on any device, at any hour, in any format. It is the first thing this guide teaches and the last thing it will let you forget."),
    SP(10), RULE(),
    Paragraph(REVLINE, ParagraphStyle("rev", fontName="DM-Med", fontSize=9, textColor=RUST, leading=13)),
    Paragraph("Written and designed by Temidayo Afonja, Founder and Principal, The Density Group.  " + URL, S["note"]),
]
story += [PageBreak()]

# =====================================================================
# 3. WELCOME FROM TEMIDAYO
# =====================================================================
story += [Bookmark("Welcome", 0), SP(6), EY("Welcome"),
    Paragraph("A short word before you start", S["h2"]), RULE(),
    LEAD("Most people do excellent work and remember almost none of it clearly."),
    P("Not because the work was small. Because the work was constant. You solved the problem, absorbed the lesson, and moved to the next thing before the last one had a name. Months later a review, a promotion case, or a sudden change asks you to account for a year, and you find yourself reaching for details that have already gone soft."),
    P("I have spent eighteen years working close to where talent decisions get made: performance calibrations, promotion panels, restructurings, and the quiet conversations that precede all of them. The people who fared well in those rooms were rarely the ones who had done the most. They were the ones who could describe what they had done, accurately, without inflating it and without shrinking it. That skill is learnable. It is mostly a matter of keeping a record while the facts are still available to you."),
    P("Keep the Proof is that record and the discipline around it. It will not tell you what your career means or what move to make. It will help you hold on to the truth of your own work, in language a stranger can understand, kept in a way that respects the people you work for. That is a smaller promise than most career products make. It is also one you can actually keep."),
    SP(4),
    Paragraph("Temidayo Afonja", ParagraphStyle("sig", fontName="CG-Semi", fontSize=15, textColor=NAVY, leading=18)),
    Paragraph("Founder and Principal, The Density Group", S["note"]),
]
story += [PageBreak()]

# =====================================================================
# 4. WHAT IS INSIDE / HOW TO USE
# =====================================================================
story += [Bookmark("Orientation", 0), SP(6), EY("Orientation"),
    Paragraph("What is inside, and how to use it", S["h2"]), RULE(),
    P("This guide has three jobs. It teaches you what career evidence is and what is not worth keeping. It gives you tools to capture and translate your work. And it builds those tools into short routines so the record maintains itself instead of becoming another thing you fall behind on."),
    H3("The four things you will build"),
]
story += bullets([
    "<b>A permitted private system.</b> A place you own and control, holding only what you are allowed to keep.",
    "<b>A capture habit.</b> A two-minute method for catching work the moment it happens, and a fuller entry for the work that matters most.",
    "<b>A translation skill.</b> A repeatable way to turn internal labels and half-finished notes into accurate, portable language.",
    "<b>Two light routines.</b> A monthly sweep and a quarterly review that keep the record honest and current.",
])
story += [SP(4), H3("How to read it"),
    P("You can read straight through in about an hour, or jump to the tool you need. If you want to start immediately, turn to the sixty-minute setup and follow it in order. Wherever a tool appears, a completed example appears with it, so you are never looking at an empty box wondering what belongs there."),
    SP(4),
    CO("The one rule that never bends",
       "You record your own recollection and information you are permitted to retain. You never copy, forward, or reconstruct material your employer owns. If permission is unclear, you leave it out. Everything else in this guide sits underneath that rule.",
       bg="navy"),
]
story += [PageBreak()]

# =====================================================================
# PART ONE DIVIDER + 5,6,7,8,9
# =====================================================================
story += [NextPageTemplate("content")]
story += [NextPageTemplate("divider"), PageBreak(), Bookmark("Part One: Understand the record", 0)]
story += section_divider("One", "Understand the record",
    "What career evidence is, and why it goes missing",
    "Before the tools, a clear idea of what you are keeping and what you are not. Most career records fail here, not in the formatting.")
story += [NextPageTemplate("content"), PageBreak()]

# 5. OPENING SCENARIO
story += [SP(6), KI("The opening question"),
    Paragraph("If your access disappeared this afternoon", S["h2"]), RULE(),
    LEAD("If your work access disappeared this afternoon, how much of your career evidence would disappear with it?"),
    P("Picture the ordinary version of a bad day. Not a scandal, just a change. A reorganization removes your login by five o&#8217;clock. A role is eliminated with two weeks&#8217; notice. A system migration wipes three years of your sent mail. You are fine, professionally and otherwise. But the record of what you did now lives in systems you can no longer open."),
    P("What would you still have? For most capable people the honest answer is: a current title, a rough sense of their projects, and a handful of numbers they are not quite sure of. The specific decisions, the problems they caught before anyone noticed, the exact shape of the thing they built, all of it sat inside the work, and the work is behind a door that just closed."),
    P("This guide is built for the stretch of time between two sentences. The first is <i>I am doing the work.</i> The second is <i>I suddenly need to explain what the work amounted to.</i> That gap is usually months or years long, and almost nobody uses it. Keep the Proof is how you use it."),
]
story += [GAP()]

# 6. WHY EVIDENCE DISAPPEARS
story += [SP(6), EY("The problem"),
    Paragraph("Why career evidence disappears", S["h2"]), RULE(),
    P("It is tempting to blame memory. Memory is part of it, but it is not the main cause. Career evidence disappears for reasons that are structural, and once you see them you can design around them."),
    H3("It lives in systems you do not own"),
    P("Your accomplishments are recorded, but not by you and not for you. They sit in a ticketing system, a shared drive, a customer platform, an email account, a chat history. Every one of those belongs to your employer. Access to them is a condition of your role, and it ends when the role does."),
    H3("It is written in a private language"),
    P("Inside a company, work is described in shorthand: project code names, internal acronyms, team rituals. That shorthand is efficient at work and meaningless everywhere else. A record written only in internal language is a record only your current employer can read."),
    H3("The best parts are the least visible"),
    P("The work that most deserves to be remembered often leaves the faintest trace. A judgment call that prevented a bad outcome produces no artifact, because the bad outcome never happened. Coordination across three teams shows up in no single person&#8217;s numbers. The quieter and more valuable the contribution, the more likely it is to vanish without a deliberate record."),
    H3("It decays quietly"),
    P("Details do not leave all at once. They fade. The figure you were sure of becomes approximate. The reason behind a decision blurs into the decision itself. Six months on, you can still tell the story, but you can no longer defend the specifics, and specifics are what a review or a resume runs on."),
]
story += [GAP()]

# 7. WHAT EVIDENCE IS / IS NOT
story += [SP(6), EY("The category"),
    Paragraph("What career evidence is, and is not", S["h2"]), RULE(),
    P("Career evidence is a truthful, private, retrievable record of what you contributed, what judgment you exercised, what changed because of your work, and what permitted information supports the account. That is the whole definition, and each word in it is doing work."),
    TBL([["Career evidence is", "Career evidence is not"],
         ["A record of your contribution and judgment", "A list of everything you were assigned"],
         ["Written in language an outsider can follow", "A wall of internal names and acronyms"],
         ["Honest about your part in a shared result", "A claim of sole credit for team work"],
         ["Built only from what you may keep", "A copy of files that belong to your employer"],
         ["Useful before many career moments", "A document you touch only when job hunting"]],
        [CONTENT_W*0.5, CONTENT_W*0.5]),
    SP(6),
    P("It is disciplined recordkeeping, not self-promotion. The point is not to make your work sound impressive. The point is to make it accurate and findable, so that when a moment arrives that depends on the details, the details are there and you can trust them. Done well, an accurate record is more persuasive than an inflated one, because it holds up when someone asks a second question."),
    SP(2),
    NOTE("Some people call this a brag document. The name is understandable, and it is the last time this guide will use it. What you are building is evidence rather than bragging, and the difference is practical. Evidence holds up when it gives someone else something concrete to examine."),
]
story += [GAP()]

# 8. WHAT IS WORTH CAPTURING
story += [SP(6), EY("The filter"),
    Paragraph("What is worth capturing", S["h2"]), RULE(),
    P("You cannot record everything, and you should not try. Activity is not contribution. Answering forty emails is activity. Deciding which of the forty actually needed a decision, and getting that one right, is contribution. The filter below keeps the record small and worth keeping."),
    H3("Capture it if one of these is true"),
]
story += bullets([
    "You exercised judgment, made a decision, or chose between real options.",
    "Something changed, improved, or became possible because of what you did.",
    "You prevented a problem, a cost, a delay, or a risk that would otherwise have landed.",
    "You handled scope, scale, or complexity that a description of your title would not reveal.",
    "You coordinated, influenced, or unblocked work across people or functions.",
    "You received specific feedback, recognition, or a result you can honestly point to.",
])
story += [SP(4), H3("Let it go if it is only this"),
]
story += bullets([
    "Routine execution of your basic duties with nothing distinctive about how you did it.",
    "Attendance, hours, or effort with no observable change attached.",
    "A task you were assigned but did not meaningfully shape.",
])
story += [SP(4),
    CO("A simple test",
       "Before you record something, ask: if I described this to a thoughtful stranger, would they understand what I actually contributed and why it mattered? If the honest answer is no, either find the contribution underneath the activity, or leave it out.",
       bg="sand", bar=GOLD),
]
story += [PageBreak()]

# 9. EVIDENCE VS EMPLOYER ARTIFACTS
story += [SP(6), EY("The boundary"),
    Paragraph("Evidence versus employer-owned artifacts", S["h2"]), RULE(),
    P("This is the distinction the whole system depends on, so it is worth stating plainly. Your career evidence is your own account of your work. An employer-owned artifact is the material itself: the deck, the model, the code, the client file, the report. The account is yours to keep. The artifact is not."),
    TBL([["Yours to keep (your account)", "Not yours (the artifact itself)"],
         ["&#8220;I rebuilt the onboarding process and cut new-hire ramp time.&#8221;", "The onboarding deck, the HR system export, the employee list"],
         ["&#8220;I found and closed a gap in how we granted system access.&#8221;", "The access logs, the security configuration, the audit tooling"],
         ["&#8220;I led the vendor selection and negotiated better terms.&#8221;", "The signed contract, the pricing sheet, the internal cost model"]],
        [CONTENT_W*0.5, CONTENT_W*0.5]),
    SP(6),
    P("Notice what the left column has in common. Each entry is a sentence you could say out loud in a hallway without exposing anything your employer owns. It describes your contribution and the change, at a level of detail that is yours to carry. The right column is the underlying material, and none of it belongs in a personal record, no matter how convenient it would be to keep."),
    CO("The line you will learn to hear",
       "If the thing you want to save is a file, a screenshot, an export, or a copy of anything produced at work, it is an artifact, and it stays behind. If it is your own sentence about what you did, it is evidence, and it comes with you.",
       bg="navy"),
]
story += [PageBreak()]

# =====================================================================
# 10. FIVE-PART WORKFLOW
# =====================================================================
story += [SP(6), EY("The method"),
    Paragraph("The Keep the Proof workflow", S["h2"]), RULE(),
    P("Every entry you make, from a two-minute note to a full record, moves through the same five steps. You will not think about them consciously for long. They become the shape of how you handle a piece of work worth keeping."),
    SP(4), workflow_strip(), SP(10),
    H3("Read the five steps once, slowly"),
    P("<b>Capture</b> is speed. The goal is to catch the work before the details soften, even if the note is rough. <b>Clarify</b> is honesty. You separate what the team achieved from what you actually did, and you name the judgment inside the task. <b>Translate</b> is reach. You convert internal shorthand into language someone outside your company could follow. <b>Protect</b> is permission. You confirm that everything you are keeping is yours to keep, and you leave out anything that is not. <b>Retrieve</b> is usefulness. You tag the entry so that when a review or a resume or a hard week arrives, you can find exactly what you need."),
    SP(2),
    NOTE("The order matters more than the names. Capture before you clarify, because a rough note beats a perfect memory you never wrote down. Protect before you retrieve, because a record you were not permitted to keep is worse than no record at all."),
]
story += [PageBreak()]

# =====================================================================
# PART TWO DIVIDER + 11,12,13
# =====================================================================
story += [NextPageTemplate("divider"), PageBreak(), Bookmark("Part Two: Permission and protection", 0)]
story += section_divider("Two", "Permission and protection",
    "The standard that keeps this safe",
    "The most valuable thing this guide does is tell you what not to keep. Permission comes before protection, and it comes before everything else.")
story += [NextPageTemplate("content"), PageBreak()]

# 11. PERMISSION BEFORE PROTECTION
story += [SP(6), KI("The central rule"),
    Paragraph("Permission comes before protection", S["h2"]), RULE(),
    LEAD("A secure personal device does not make information yours to retain."),
    P("This is the sentence to remember above all others. People reach for the wrong test constantly. They ask whether the information is stored safely, whether they used their own laptop, whether it happened after hours. None of those questions is the right one. The right question is whether you are permitted to keep the information at all. Security is what you do <i>after</i> you have established permission. It is never a substitute for it."),
    H3("What does not create permission"),
]
story += bullets([
    "Using a personal device, a personal account, or your own phone. Ownership of the hardware does not transfer ownership of the information.",
    "Working outside office hours. Confidentiality obligations do not clock out at six.",
    "Generalizing, rounding, anonymizing, or otherwise &#8220;sanitizing&#8221; something. Softening the wording does not make restricted information yours.",
    "Believing the information is harmless, or that no one would mind. Permission is a fact about your agreements, not a guess about intentions.",
])
story += [SP(4),
    CO("The permission test",
       "Before anything enters your record, ask one question: am I permitted to retain this outside my employer&#8217;s systems? If yes, keep your own high-level account of it. If no, or if you are not sure, leave it out and, where it matters, ask someone qualified. Uncertainty is not a yellow light. For this record, it is a red one.",
       bg="navy"),
]
story += [GAP()]

# 12. CONFIDENTIALITY GUIDE (2 pages)
story += [SP(6), EY("Information risk"),
    Paragraph("The confidentiality and information-risk guide", S["h2"]), RULE(),
    P("This section is the one to read slowly, because it is the one most people get wrong in ways that are hard to undo. The guiding idea is simple. Your record is built from your own memory of your own work and from information you are clearly permitted to hold. It is never built by extracting, copying, or reconstructing what your employer owns."),
    H3("Three tiers, one habit"),
    P("Sort everything you might record into three tiers. With practice this becomes instant."),
    SP(3), tier_block(), SP(8),
    P("Generalizing information does not create permission. Use generalized wording only after you have confirmed that you are permitted to retain the underlying information. Softening the words changes how something reads, not whether it is yours to keep."),
    P("The habit is to default downward. When something sits between Keep and Care, treat it as Care. When it sits between Care and Never, treat it as Never. You will lose a little detail this way. You will never lose your standing."),
]
story += [GAP()]
story += [SP(6), EY("Information risk, continued"),
    Paragraph("Lines that do not move", S["h2"]), RULE(),
    P("Some actions are outside the system entirely. They are not judgment calls and they are not softened by good intentions or careful storage."),
]
story += bullets([
    "Do not forward, download, photograph, screenshot, print, upload, or copy employer-owned material into any personal system.",
    "Do not circumvent security controls, data-loss tools, access restrictions, monitoring, or retention rules to obtain something for your record.",
    "Do not retain source code, credentials, security configurations, customer or employee data, personal information, internal financials, privileged communications, unreleased product detail, trade secrets, confidential research, proprietary models, internal decks, or client materials.",
    "Do not paste confidential or employer-owned work information into an AI system of any kind.",
    "When permission is uncertain, omit the information and seek qualified advice. That is the whole procedure.",
])
story += [SP(4),
    CO("What the record actually runs on",
       "Your own high-level recollection of what you did. Information that has been publicly disclosed. And anything your employer has expressly permitted you to retain. That is the entire supply. It is narrower than people expect, and it is enough.",
       bg="sand", bar=GOLD),
    SP(4),
    NOTE("This guide is educational and is not legal advice. It cannot read your employment agreement or your employer&#8217;s policies. Where a question of permission genuinely matters, ask your manager, your human resources team, or an attorney before you keep anything."),
]
story += [GAP()]

# 13. CHOOSING & SECURING A SYSTEM
story += [SP(6), EY("Setup"),
    Paragraph("Choosing and securing a private system", S["h2"]), RULE(),
    P("Your record needs a home. The requirements are modest, and they come in a strict order: the content must be permitted first, and only then does the storage matter. Securing a record you were not allowed to keep does not fix the problem. It hides it."),
    H3("Choose a home you actually control"),
]
story += bullets([
    "Use a private account that belongs to you, not an employer-owned account, drive, or device.",
    "A plain document, a personal notebook, or a simple notes app is enough. The tools in this guide work in any of them.",
    "Keep it in one place. A record scattered across four apps is a record you will not maintain.",
])
story += [SP(3), H3("Then secure it, in this order")]
story += bullets([
    "Protect it with a unique password and turn on multifactor authentication.",
    "Prefer storage that is encrypted and access-controlled.",
    "Keep a backup only where the underlying content is permitted to live.",
    "Never store the record on a device or in an account your employer owns or can reclaim.",
])
story += [SP(4),
    CO("Order of operations",
       "Permission, then storage. Every time. A locked box is only as safe as your right to hold what is inside it. Establish that you may keep something before you decide where to keep it.",
       bg="navy"),
]
story += [PageBreak()]

print("PART1_2 sections queued")

# The remaining parts (tools, examples, routines, retrieval, close) are appended
# by build_handbook_2 for readability; import and extend.
import handbook_part2 as hp2
story += hp2.story(S, P, LEAD, H2, H3, EY, KI, NOTE, SP, bullets, CO, TBL, RULE,
                   section_divider, workflow_strip, field_row, Field, CONTENT_W)

# =====================================================================
# BUILD
# =====================================================================
# Collapse the double page break that precedes each PART divider: a section's
# trailing PageBreak followed immediately by the divider's NextPageTemplate +
# PageBreak would emit a stray blank page. Drop any PageBreak that is directly
# followed by a NextPageTemplate.
def _collapse_breaks(items):
    out = []
    for i, it in enumerate(items):
        if isinstance(it, PageBreak):
            nxt = items[i+1] if i+1 < len(items) else None
            if isinstance(nxt, NextPageTemplate):
                continue
        out.append(it)
    return out
story = _collapse_breaks(story)

doc = KTPDoc(OUT, footer_title="Keep the Proof", url=URL)
doc.title = "Keep the Proof: A 60-Minute Career Evidence System"
doc.author = "Temidayo Afonja"
doc.subject = "A career evidence system: capture, translate, protect, and retrieve a private record of your work."
doc.keywords = "career evidence, work accomplishments, portable language, confidentiality, Temidayo Afonja, Keep the Proof v1.0.1"
doc.build(story)
print("wrote", OUT)
