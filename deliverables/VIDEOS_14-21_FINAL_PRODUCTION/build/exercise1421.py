# -*- coding: utf-8 -*-
"""07_Viewer_Exercise. One script-aligned exercise per video.

Each exercise is the artifact the master's own CTA asks for. Nothing is added
beyond what the script already teaches.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import masters1421 as M
from docs1421f import (base_doc, para, title_block, rule, h, kv, callout,
                       table, bullets, sub, footer_note, numbered,
                       NAVY, GOLD, DIM, RED)

EX = {
 14: ("Audit one destination role",
      ["Choose ONE role you are actually considering. Not an industry.",
       "List every requirement in the posting that looks familiar.",
       "For each one, answer two questions. What would I actually have to "
       "decide? What happens if I decide badly?",
       "Sort each answer into one of four buckets: TRAVELS, LOOKS SIMILAR, "
       "MUST BE LEARNED, MUST BE EXPERIENCED.",
       "Look at the TRAVELS column and write the evidence you already have "
       "for each item.",
       "Look at the MUST BE LEARNED column and pick the one item you would "
       "start this month.",
       "Look at the MUST BE EXPERIENCED column and write honestly what access "
       "or practice it would require."],
      ["A posting is a recruiting document, not a description of the work.",
       "Similar wording does not make two roles interchangeable.",
       "This exercise cannot tell you whether you would be hired."]),
 15: ("Name one gap and the step that matches",
      ["Write down one recent moment when the work got harder. A question you "
       "could not answer well, a decision you were not ready to own, or a "
       "capability you could not demonstrate.",
       "Ask: do I need to learn this?",
       "Ask: have I ever genuinely practiced this, as the person who had to "
       "decide?",
       "Ask: can I prove that I already have?",
       "Choose the ONE answer that fits and write the matching next step. "
       "Learn, practice, or prove.",
       "Write one sentence describing what you will do in the next two "
       "weeks."],
      ["This is a reflection tool, not a diagnostic. It assigns no score, "
       "level or type.",
       "You may have none of these gaps, or more than one.",
       "Some gaps require access or authority you cannot award yourself."]),
 16: ("Build a contribution record",
      ["Choose three pieces of consequential work from the last year.",
       "For each, write four lines. What was true before. What you decided. "
       "What changed. What evidence supports the account.",
       "Read each one back and ask whether a person outside your team could "
       "understand it without you explaining.",
       "Pick the conversations where scope actually gets allocated and decide "
       "where each line belongs.",
       "Then answer the harder question in writing: does the decision-maker "
       "not know, or do they know and not act?"],
      ["A clearer record does not override bias, create a role, or move a "
       "budget you do not control.",
       "It removes the obstacle that is yours, so what remains is easier to "
       "see."]),
 17: ("Four lines for one piece of AI-assisted work",
      ["Choose one piece of work from this week where a tool did most of the "
       "visible production.",
       "Line one: what were you actually asked to get right, not what were "
       "you asked to produce.",
       "Line two: what did you check, and why did you check that. Write the "
       "reason, not just the check.",
       "Line three: what did you conclude that the initial output did not "
       "establish.",
       "Line four: what were you accountable for if the result was wrong.",
       "Put the record where your work already gets discussed, not in a file "
       "you will not open again."],
      ["This does not make a job safe. Roles are redesigned and removed for "
       "reasons unrelated to any individual's contribution.",
       "It is also not a claim about what these tools can or cannot do."]),
 18: ("A decision record for the offer",
      ["Write what work you want more of, using last month as evidence rather "
       "than a general sense of yourself.",
       "Ask two managers at the level you are considering what their last "
       "ordinary week actually contained.",
       "Ask what senior individual work looks like here, and ask for names.",
       "List what you could decide without asking, then list what you would "
       "be answerable for. Compare the lengths.",
       "Find out whether anyone has moved into management here and back out "
       "without penalty.",
       "Write the one thing you still do not know, and who could answer it "
       "this week."],
      ["Some organizations genuinely cap individual contributors.",
       "Neither path is the braver choice."]),
 19: ("One service, written as a proposal",
      ["Name the problem in the buyer's words, not yours.",
       "Name the buyer specifically enough that you could list three real "
       "organizations.",
       "Write the deliverable as something a person receives, with a "
       "beginning and an end.",
       "Write the scope, including what is not included.",
       "Write the conditions that would have to be true before this is "
       "viable.",
       "Read your employment agreement before any outreach, and get "
       "qualified advice on anything unclear."],
      ["This is not legal or tax advice.",
       "Nothing here promises revenue, clients or a timeline."]),
 20: ("The two-part return record",
      ["Sort what you carry into three buckets: still current, needs "
       "updating, needs rebuilding.",
       "Inside those, mark what stayed current, what decayed, what changed in "
       "the field, what changed in your circumstances, what is unproven "
       "rather than absent, and what genuinely has to be rebuilt.",
       "For every item in still current, write the evidence a person could "
       "actually inspect.",
       "For every unproven item, write one way you could create a current "
       "instance.",
       "Choose ONE thing you are rebuilding and put a start date and a "
       "target date on it.",
       "Write the short, honest sentence about the break. Once. Then stop "
       "working on it."],
      ["Bias against career breaks exists and framing does not remove it.",
       "A different title, scope or compensation on return is a tradeoff to "
       "evaluate, not a measurement of your worth."]),
 21: ("A five-layer relearning inventory",
      ["Choose ONE destination role. Not an entire industry.",
       "Make five headings: domain knowledge, regulation and credentials, "
       "systems and tooling, relationships and internal history, and how "
       "decisions get made here.",
       "Under each, write what you actually need to understand here, and how "
       "you could realistically learn it.",
       "Mark each item as something you can read, or something that needs "
       "exposure and practice.",
       "Confirm the binding requirements from the body or employer that "
       "actually sets them.",
       "Reorder the whole list by one question: what stops me contributing "
       "usefully first?",
       "Start the top item this week. The item, not the plan for it."],
      ["A licensing requirement is not a mindset issue.",
       "Some layers only develop through practice in the environment, and "
       "that is normal rather than evidence of a wrong move."]),
}


def build(n, out_path, stamp):
    name, steps, limits = EX[n]
    d = base_doc()
    footer_note(d, "Video %d viewer exercise  |  aligned to the locked final "
                   "master" % n)
    title_block(d, "Capability Formation  |  Video %d" % n, name,
                M.title(n))
    kv(d, "Generated", stamp)
    kv(d, "The video's own CTA", M.cta(n))
    kv(d, "Resource", M.resource(n) or
       "None. This video names no resource and none is added.")
    callout(d, "This exercise is the artifact the script already asks for. It "
               "adds no new claim, no new framework and no new offer.")
    h(d, "Do this")
    numbered(d, steps)
    h(d, "What this exercise cannot do")
    bullets(d, limits)
    h(d, "Where it goes")
    para(d, "Keep it somewhere you will reread it. The value is in having "
            "written it down, not in the format.")
    d.save(out_path)
    return out_path
