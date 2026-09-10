# -*- coding: utf-8 -*-
"""06_Publishing materials, and the 07 viewer exercise.

Titles and thumbnail wording come from the locked masters and are never
restyled here. Nothing is invented: no URL, no chapter, no music credit, no
performance claim. Placeholders are marked.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import masters1421 as M
from docs1421f import (base_doc, para, title_block, rule, h, kv, callout,
                       table, bullets, sub, field, page_break, footer_note,
                       numbered, mono, hr, head, NAVY, GOLD, DIM, RED)

ROUTES = {
 "Career Evidence Starter": "temidayoafonja.com/career-evidence-starter",
 "Field Kit": "temidayoafonja.com/fieldkit",
 "Career Decision Evidence Check": "temidayoafonja.com/career-decisions",
 "Keep the Proof": "temidayoafonja.com/keep-the-proof",
}

PLAYLIST = "Capability Formation: career pivots and internal moves"

DESC = {
 14: ("Most transferable-skills advice stops at the words. This video "
      "compares what the words actually sit on top of.\n\n"
      "Working from a structured reading of 28 senior program and project "
      "delivery job descriptions across healthcare, financial services and "
      "technology, all collected on September 10, 2026, it separates the "
      "delivery work that genuinely recurs across industries from the "
      "requirements that only look portable until you examine the decision "
      "underneath.\n\n"
      "The test is two questions. What would this person actually have to "
      "decide? And what happens if they decide badly?\n\n"
      "You will leave with a four-bucket audit for one destination role: what "
      "travels, what only looks similar, what must be learned, and what must "
      "be experienced.\n\n"
      "A note on the evidence. 28 job descriptions are a convenience sample. "
      "They show what these employers chose to write down on one date. They "
      "do not represent the labor market, they do not prove two roles are "
      "interchangeable, and they cannot tell you who would be hired."),
 15: ("Three career gaps feel identical from the inside and need completely "
      "different responses.\n\n"
      "A learning gap, where there is something you genuinely do not know "
      "yet. A practice and authority gap, where you understand the decision "
      "but have never been allowed to own it. And an evidence gap, where you "
      "already know how and nobody can see enough proof.\n\n"
      "Learn. Practice. Prove. If you misread which one you have, you can "
      "spend a year fixing the wrong problem.\n\n"
      "This is a reflection tool, not a diagnostic. It does not assign you a "
      "type, and some of these gaps are shaped by the organization rather "
      "than by you."),
 16: ("There is a particular kind of stuck that is not the same as being "
      "invisible. Your work is relied on. Your name is not in the room where "
      "scope gets decided.\n\n"
      "The usual advice is to speak up more. That can help, but it treats "
      "several different problems as though they are one.\n\n"
      "This video separates four: is the work seen, is it attributed to you, "
      "are you trusted for delivery or considered for larger scope, and is "
      "the obstacle one you can actually remove.\n\n"
      "It is honest about the limit. A clearer record does not override bias, "
      "create a role that does not exist, or move a budget you do not "
      "control. What it does is remove the obstacle that is yours, so "
      "whatever remains becomes easier to see."),
 17: ("The report used to take two days. Now a tool produces most of it in "
      "forty minutes. The work is not worse, but the answer to what did you "
      "actually do has become harder to give.\n\n"
      "The problem is usually not that your value dropped. It is that the "
      "artifact used to be the evidence, and the artifact has stopped being "
      "scarce.\n\n"
      "This video gives four lines to keep for one piece of AI-assisted work: "
      "what you were asked to get right, what you checked and why, what you "
      "concluded that the output did not establish, and what you were "
      "accountable for.\n\n"
      "It does not claim that human judgment makes a job safe, and it does "
      "not claim that these tools cannot perform work that looks like "
      "judgment. The narrower point holds either way."),
 18: ("Management is often offered as a reward. It is not a reward. It is a "
      "different job.\n\n"
      "This video separates five things that get bundled together and do not "
      "reliably move together: scope, responsibility, compensation, "
      "authority, and people management.\n\n"
      "Then four questions to ask before you answer. What does the job "
      "consume? Does the other path really exist here? What authority comes "
      "with it? And can you come back?\n\n"
      "It stays two-sided. Some organizations genuinely cap individual "
      "contributors, and that is information you need rather than "
      "encouragement or discouragement."),
 19: ("Someone has told you that you should consult. It usually arrives right "
      "after you solve something difficult, which is why almost nobody "
      "examines it.\n\n"
      "Your experience tells you what you know. It does not automatically "
      "tell you what somebody will buy.\n\n"
      "This video separates four things people call consulting: expertise, an "
      "offer, a buyer, and repeatability. Then it works through the buyer "
      "question, turning expertise into a deliverable, and how to test the "
      "offer before you change anything.\n\n"
      "No income promises, no client promises, and no business-setup advice. "
      "Check your own employment agreement before side work or outreach. This "
      "video is not legal or tax advice."),
 20: ("Returning after a career break is not mainly about finding the perfect "
      "sentence to explain the gap. The explanation matters. It is not the "
      "whole return.\n\n"
      "This video sorts what you carry into three buckets: still current, "
      "needs updating, and needs rebuilding. And it holds on to one "
      "distinction that saves people a great deal of wasted effort. Unproven "
      "is not the same as absent.\n\n"
      "It is honest about the market. Bias against career breaks exists, and "
      "a better explanation does not make every employer fair. Some routes "
      "back may involve a different title, scope or compensation, which is a "
      "tradeoff to evaluate rather than a measurement of your worth."),
 21: ("You made the industry change, and you can still do the work. What "
      "keeps catching you are the things nobody thought to explain.\n\n"
      "This video sorts the relearning into five layers: domain knowledge, "
      "regulation and credentials, systems and tooling, relationships and "
      "internal history, and how decisions actually get made.\n\n"
      "It says the part a lot of career content avoids. A licensing "
      "requirement is not a mindset issue. If a role requires a "
      "qualification you do not hold, adjacent experience does not erase "
      "that.\n\n"
      "You will leave with an inventory for one destination role, ordered by "
      "one question: what stops me contributing usefully first?"),
}

PINNED = {
 14: ("The two questions from this video, for one role you are considering:\n"
      "What would I actually have to decide? What happens if I decide badly?\n"
      "Then sort what you find into TRAVELS, LOOKS SIMILAR, MUST BE LEARNED, "
      "MUST BE EXPERIENCED.\n\n"
      "On the evidence: 28 retained job descriptions, 10 healthcare, 10 "
      "financial services, 8 technology, all collected September 10, 2026. "
      "That is a convenience sample of what these employers wrote down. It "
      "does not represent the labor market and it cannot tell you who gets "
      "hired."),
 15: ("Name one gap and the step that matches it.\n"
      "LEARN, PRACTICE or PROVE. One word, one sentence.\n\n"
      "This is a reflection tool, not a diagnostic. It does not assign you a "
      "type, and some of these gaps are shaped by the organization rather "
      "than by you."),
 16: ("Write one decision you made and what it changed.\n\n"
      "Then the harder read: does your manager not know, or do they know and "
      "not act? Those are different situations, and you cannot tell which one "
      "you are in until the information problem is gone."),
 17: ("Take one piece of work from this week where a tool did most of the "
      "visible production, and write what you checked and why.\n\n"
      "That is the line people forget fastest, and it is the one that "
      "carries the contribution."),
 18: ("Before you answer the offer, ask four questions.\n"
      "What does the job consume? Does the other path really exist here? What "
      "authority comes with it? Can you come back?\n\n"
      "And ask for names. If nobody can name a person on the senior "
      "individual track, that path may exist on a slide and nowhere else."),
 19: ("One sentence: what would somebody receive from you, and by when?\n\n"
      "If that is hard to write, the offer is still a description of you "
      "rather than something a person can buy. Check your employment "
      "agreement before any outreach. This video is not legal or tax "
      "advice."),
 20: ("Two short lists.\n"
      "What is current now, with evidence for each item.\n"
      "What you are rebuilding now, with a date attached.\n\n"
      "The date is the part entirely within your control."),
 21: ("Build the five-layer inventory for one destination role, then reorder "
      "it by one question: what stops me contributing usefully first?\n\n"
      "And check the binding requirements from the body or employer that "
      "actually sets them. A licensing requirement is not a mindset issue."),
}

TAGS = {
 14: ["transferable skills", "career change", "changing industries",
      "job description analysis", "career pivot", "program manager",
      "project manager", "senior individual contributor", "career research",
      "experienced professionals", "industry transfer", "career strategy"],
 15: ["career gaps", "decision making at work", "career development",
      "experienced professionals", "career growth", "skills gap",
      "career reflection", "workplace judgment", "career evidence",
      "mid career", "professional development", "career strategy"],
 16: ["overlooked at work", "workplace recognition", "career visibility",
      "promotion", "contribution record", "career evidence",
      "experienced professionals", "workplace advice", "scope and promotion",
      "mid career", "career strategy", "being undervalued"],
 17: ["AI at work", "proving your value", "contribution record",
      "AI and careers", "career evidence", "knowledge work",
      "experienced professionals", "workplace AI", "professional value",
      "career strategy", "mid career", "future of work"],
 18: ["individual contributor", "should I become a manager",
      "management career", "career decision", "IC vs manager",
      "career path", "promotion decision", "experienced professionals",
      "senior individual contributor", "career strategy", "mid career",
      "people management"],
 19: ["consulting", "should I consult", "independent consulting",
      "career change", "consulting business", "career decision",
      "experienced professionals", "leaving employment", "consulting offer",
      "career strategy", "mid career", "professional services"],
 20: ["career break", "returning to work", "career gap", "return to work",
      "maternity leave return", "career restart", "returnship",
      "experienced professionals", "career reentry", "career strategy",
      "mid career", "employment gap"],
 21: ["changing industries", "industry change", "career pivot",
      "transferable skills", "new industry", "career transition",
      "relearning", "experienced professionals", "domain knowledge",
      "career strategy", "mid career", "starting over"],
}

HASHTAGS = {
 14: ["#CareerChange", "#TransferableSkills", "#CapabilityFormation"],
 15: ["#CareerGrowth", "#CareerDevelopment", "#CapabilityFormation"],
 16: ["#CareerAdvice", "#WorkplaceRecognition", "#CapabilityFormation"],
 17: ["#AIAtWork", "#CareerAdvice", "#CapabilityFormation"],
 18: ["#CareerDecisions", "#IndividualContributor", "#CapabilityFormation"],
 19: ["#Consulting", "#CareerDecisions", "#CapabilityFormation"],
 20: ["#CareerBreak", "#ReturnToWork", "#CapabilityFormation"],
 21: ["#CareerChange", "#ChangingIndustries", "#CapabilityFormation"],
}


def thumb_brief(n):
    return [
      "Headline text, exactly as locked: %s" % M.thumbnail(n),
      "Set the headline flush left in short stacked lines, Montserrat "
      "ExtraBold, cap height 240 to 300 px on a 3840 by 2160 master.",
      "Deep navy #112345 field. Warm cream and white for the headline. Bright "
      "warm yellow as selective emphasis only, well under about 4 percent of "
      "the canvas.",
      "Large real portrait of Temidayo on the right, about 44 to 47 percent "
      "of the canvas. Natural skin tone. Use an approved real photograph.",
      "Do NOT generate, reconstruct, beautify or alter the face. Permitted on "
      "the source photograph: crop, mask, restrained exposure adjustment, "
      "color balance, background removal.",
      "No clutter, no tiny text, no fake icons, no AI-looking people, no "
      "numbers and no implied statistic.",
      "Keep the portrait layer and the text layer editable and separate.",
      "Must be legible at 200 px wide, which is the recommendation-column "
      "size.",
      "Export a 3840 by 2160 PNG master and a 1280 by 720 JPG for upload, "
      "quality 95, under 2 MB.",
      "Artwork is approved separately. This brief does not authorize a "
      "finished thumbnail.",
    ]


def build(n, out_path, stamp):
    res = M.resource(n)
    d = base_doc()
    footer_note(d, "Video %d publishing materials  |  copy taken from the "
                   "locked final master" % n)
    title_block(d, "Capability Formation  |  Video %d" % n,
                "Publishing Materials", M.title(n))
    kv(d, "Generated", stamp)
    kv(d, "Source", "%s  ·  SHA-256 %s" % (M.FILES[n], M.read(n)["sha"]))

    callout(d, "The title and the thumbnail wording are taken from the locked "
               "master and are not restyled here. No URL, chapter timestamp, "
               "music credit or performance claim is invented anywhere in "
               "this document.")

    h(d, "YouTube title")
    para(d, M.title(n), size=13, bold=True, color=NAVY)

    h(d, "Thumbnail text")
    para(d, M.thumbnail(n), size=13, bold=True, color=NAVY)

    h(d, "Description")
    for block_ in DESC[n].split("\n\n"):
        para(d, block_)
    para(d, "RESOURCE LINE, paste as the last block:", size=9, bold=True,
         color=GOLD, before=10, after=4)
    if res:
        para(d, "%s: https://%s" % (res, ROUTES[res]), size=11, bold=True)
    else:
        para(d, "This video names no resource. Do not add one.", size=11,
             bold=True, color=RED)
    para(d, "WATCH NEXT LINE: %s" % M.watch_next(n), size=10, color=DIM)
    para(d, "[PLACEHOLDER] Insert the Watch Next video URL after that video "
            "is published. Do not invent a URL.", size=10, color=RED)

    h(d, "Pinned comment")
    for block_ in PINNED[n].split("\n\n"):
        para(d, block_)

    h(d, "Tags")
    para(d, ", ".join(TAGS[n]))

    h(d, "Hashtags")
    para(d, "  ".join(HASHTAGS[n]), size=12, bold=True)

    h(d, "Resource route")
    if res:
        table(d, ["Resource", "Where it lives", "How it is used"],
              [[res, ROUTES[res],
                "Named once in the script, after the teaching. One primary "
                "CTA. No second offer is added."]],
              widths=[1.9, 2.1, 2.7], size=9)
    else:
        para(d, "None. This master names no resource route, so none appears "
                "in the script, the description, the pinned comment or on any "
                "card.", color=RED, bold=True)

    h(d, "Watch Next and playlist")
    table(d, ["Field", "Value"], [
      ["Watch Next", M.watch_next(n)],
      ["Playlist", PLAYLIST],
      ["End screen", "Watch Next is the final full-screen visual. The card "
                     "keeps its copy on the left so a YouTube end screen can "
                     "sit on the right. No return to camera afterward."],
    ], widths=[1.35, 5.35], size=9)

    h(d, "Canva thumbnail brief")
    bullets(d, thumb_brief(n))

    h(d, "Publication and link checklist")
    numbered(d, [
      "Thumbnail artwork approved separately, and checked at 200 px wide.",
      "Title and thumbnail wording match the locked master exactly.",
      "Description resource link tested while signed out." if res else
      "No resource link appears anywhere, because the master names none.",
      "Watch Next URL inserted once that video is published. Not before.",
      "Captions: no burned-in subtitles on the export. SRT uploaded, "
      "generated from the final edited timeline.",
      "Chapters written from the actual final export. None exist yet.",
      "Music attribution completed from the actual track used. None is "
      "recorded here.",
      "End screen configured so it does not cover the Watch Next copy.",
    ])
    d.save(out_path)
    return out_path
