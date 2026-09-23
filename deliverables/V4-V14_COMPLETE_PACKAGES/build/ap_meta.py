# -*- coding: utf-8 -*-
"""Editorial fields, carried from the V1-V14 Source-of-Truth Manifest.

Nothing here is re-derived. The realization, memory line and observable action
are the ones approved in the manifest and in the V4-V14 sticky-realization
reconciliation. No new slogan and no second exercise was invented.
"""
import sys
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.append(DELIV + "V1-V14_FINAL_ARCHIVE/build")
sys.path.append(DELIV + "V4-V14_STICKY_AUDIT/build")
import ar_sources as AR, ar_data as AD
import sa_data as SA

TITLES = {n: AR.TITLES[n] for n in range(4, 15)}

THINKING = {n: SA.ROWS[n][2] for n in range(4, 15)}
REALIZATION = {n: SA.ROWS[n][3] for n in range(4, 15)}
MEMORY = {n: AD.MEMORY[n][0] for n in range(4, 15)}
ACTION = {n: AD.MEMORY[n][1] for n in range(4, 15)}
CTA = {n: AD.CTA[n] for n in range(4, 15)}
WATCH = {n: AD.WATCH_NEXT[n] for n in range(4, 15)}

CTA_URL = {
12: "https://temidayoafonja.com/career-evidence-starter",
13: "https://temidayoafonja.com/fieldkit",
14: "https://temidayoafonja.com/fieldkit",
}

# "Next time the viewer ___, I want them to remember ___, and then ___."
NEXT_LINE = {
4: "Next time the viewer hands a task to a tool, I want them to remember to "
   "ask what the person is still getting better at, and then write three "
   "columns for one task: before AI, with AI, still mine.",
5: "Next time the viewer is asked to absorb more work, I want them to "
   "remember to ask whether this is more capacity or more capability, and "
   "then request one piece of work that builds a new decision and set a date "
   "to review it.",
6: "Next time the viewer reads a job title that impresses or scares them, I "
   "want them to remember that the title can start the search but cannot "
   "finish the read, and then write four lines on one real posting: problem, "
   "authority, proof, real gap.",
7: "Next time the viewer is passed over, I want them to remember to ask what "
   "someone could already point to, and then write down the last three times "
   "they were trusted with something bigger.",
8: "Next time the viewer finishes a piece of work that mattered, I want them "
   "to remember keep the proof, not the property, and then write five things "
   "about it in their own words while the detail is still fresh.",
9: "Next time the viewer is told their skills are transferable, I want them "
   "to remember that the capability may still be there but the shortcuts are "
   "not, and then sort one destination role into four columns.",
10: "Next time the viewer starts a new job, I want them to remember that the "
    "first 90 days are also their first real evidence about the job, and then "
    "write four lines at day 90: read, test, prove, role check.",
11: "Next time the viewer feels this is not the job they accepted, I want them "
    "to remember to name the difference before they normalize it, and then "
    "put expected and actual side by side and name one real cost.",
12: "Next time the viewer writes an accomplishment into one line, I want them "
    "to remember that they did the work and the sentence does not say so, and "
    "then spend ten minutes putting back what a stranger needs.",
13: "Next time the viewer sees their own words in a posting, I want them to "
    "remember that they can carry the method but not the instinct for what "
    "counts as wrong in a room they have never been in, and then check "
    "whether the decision underneath the words matches too.",
14: "Next time the viewer guesses at what an employer wants, I want them to "
    "remember that sometimes the employer wrote the important part down, and "
    "then read one posting twice and mark required against preferred in the "
    "posting's own words.",
}

# One page. Built from the already approved observable action, not a second
# exercise invented to fill the folder.
EXERCISE = {
4: ("Take one task AI now helps you do.",
    ["Write the task at the top. One task, not your whole job.",
     "BEFORE AI. What did you have to notice, decide or create yourself?",
     "WITH AI. What does the tool now do?",
     "STILL MINE. What judgment, checking or responsibility is still yours?",
     "If the third column is almost empty, ask where the learning comes from "
     "next."],
    "This is not an argument against the tool. It is a way of seeing what the "
    "task used to teach you."),
5: ("Ask for one piece of work that builds something new.",
    ["Write what you have absorbed in the last six months. Rescue work, "
     "cover, training others.",
     "Next to it, write what new decision, new problem or new proof any of it "
     "gave you.",
     "If that column is thin, name one piece of work that would change it.",
     "Ask for that specific thing, not for a promotion in general.",
     "Set a date to review what actually changed. Ninety days is enough."],
    "Being needed and being developed are not the same thing. The review date "
    "is what tells you which one you are getting."),
6: ("Read one real posting in ten minutes.",
    ["PROBLEM. What does this company need this person to solve?",
     "AUTHORITY. Circle the verbs. Decide, lead, negotiate, recommend, "
     "support, execute.",
     "PROOF. What would they need to see to believe you can do it?",
     "REAL GAP. What is specific and might genuinely matter here?",
     "Then ask: could I do this work, can I prove something close to it, do I "
     "meet the real requirements?"],
    "Those are three different questions. Answering them separately is the "
    "whole method."),
7: ("Read your own situation instead of working harder.",
    ["Write down the last three times you were trusted with something bigger "
     "than your normal role.",
     "For each one: what problem was I trusted with?",
     "What decision was mine?",
     "Who saw me handle it?",
     "What changed because of my work?",
     "Then look for what is missing. Strong proof nobody senior saw is a "
     "different problem from no proof at all."],
    "This gives you something more useful than I need to work harder."),
8: ("Write five things about one project, in your own words.",
    ["BASELINE. What was true before you started?",
     "SCOPE. How many people, teams, customers, locations or systems?",
     "THE DECISION. What was actually yours to choose?",
     "THE RESULT. What changed?",
     "THE METHOD. How do you know the result was real?",
     "Then ask what you are allowed to say outside the company."],
    "Keep the proof, not the property. Nothing here asks you to take "
    "confidential documents, customer data or anything you are not allowed to "
    "keep."),
9: ("Sort one destination role into four columns.",
    ["TRAVELS. What have you already shown you can do that this role can use?",
     "DOES NOT TRAVEL. What belonged to the old place? Relationships, "
     "systems, informal power.",
     "PROOF. Of the first column, what can another person actually see?",
     "RELEARN. Regulation, credentials, domain knowledge, local "
     "relationships.",
     "Do not force everything into the first column."],
    "A large relearn column does not mean no. It tells you the size of the "
    "move."),
10: ("Write four lines at day 90.",
     ["READ. What do I understand now that I did not understand on day one?",
      "TEST. What from my previous experience works here, what needs "
      "translating, what does not?",
      "PROVE. What can I now show that I have done successfully in this "
      "context?",
      "ROLE CHECK. What have these 90 days taught me about the job itself?",
      "Finish the sentences: I came in assuming X, I learned Y."],
     "The fourth line is the one people skip. The first 90 days are also your "
     "first real evidence about the job."),
11: ("Put expected and actual side by side.",
     ["EXPECTED. What did you reasonably believe you were accepting? Use the "
      "posting, the interviews and the offer, not the version you imagined.",
      "ACTUAL. What is the job asking of you now? Look for the recurring "
      "pattern, not one bad week.",
      "COST. What is the difference doing to your capability, your evidence, "
      "your compensation or your life?",
      "CHOICE. What can you clarify, negotiate, test for a defined period, or "
      "decide next?"],
     "Name the difference before you normalize it. A job can change for "
     "legitimate reasons and still cost you something worth naming."),
12: ("Rebuild one accomplishment in ten minutes.",
     ["Pick one you remember clearly. Not your best one.",
      "What was true before you stepped in? Two sentences is enough.",
      "What was mine to decide? Not the title. The decisions.",
      "What was not obvious? A call that could have gone the other way.",
      "What changed, and how do I know? The result, then the method.",
      "Then read it back and ask: could a stranger check any of this?"],
     "A rough version that puts the real parts back beats a polished version "
     "that leaves them out."),
13: ("Read one posting against your own experience.",
     ["Take one posting you are actually considering. One posting, not a "
      "category.",
      "Underline every place its language matches your experience.",
      "For each match, ask a second question: does the decision underneath "
      "match too?",
      "And what happens there when it goes wrong?",
      "Where the words match and the decision matches, that is real overlap."],
     "Where the words match and the decision does not, that is where to stop "
     "claiming direct transfer."),
14: ("Read one posting twice.",
     ["FIRST PASS. Mark every requirement as required or preferred, using the "
      "posting's own words and not your sense of what should matter.",
      "SECOND PASS. Write two short lines.",
      "What do these words actually support?",
      "What can I still not tell?",
      "Do it on three postings and you will stop guessing about what "
      "transfers."],
     "Nobody reading a posting knows what a hiring manager thinks. Reading "
     "what is written is a smaller claim and a much more honest one."),
}

# What the evidence layer must protect, per video. Drawn from the approved
# boundary language already in each master.
PROTECT = {
4: ["AI automation is never converted into guaranteed capability loss. The "
    "master says explicitly that this is not an anti-AI argument and that "
    "some tools may help people learn faster.",
    "Different jobs get different answers. The master refuses to say one "
    "outcome will happen everywhere.",
    "Regulated and high-risk work is named as a case where hands-on practice "
    "and human review may still be required."],
5: ["An organizational decision is never converted into pure merit or pure "
    "malice. Budget, headcount, an open role, manager need and bias are all "
    "named as real.",
    "More responsibility is never converted into growth. That distinction is "
    "the whole video.",
    "The employer is not said to owe the viewer a career path."],
6: ["Preferred is never converted into required. The method reads the "
    "posting's own words.",
    "The method is explicitly said not to predict who gets hired, whether "
    "paper authority is real authority, whether a manager will bend a "
    "requirement, or whether bias will affect the decision.",
    "A life constraint, the East Africa Time overlap, is named as a genuine "
    "reason a fit can fail that has nothing to do with capability."],
7: ["An organizational decision is never converted into pure merit. Access, "
    "sponsorship, politics, favoritism, timing, budget and bias are all named "
    "on camera.",
    "Adjacent is never converted into direct. Evidence for the current role "
    "is explicitly distinguished from evidence for the next one.",
    "The video states that building the right evidence may still not get the "
    "opportunity."],
8: ["Keep the proof, not the property. Confidential documents, customer data, "
    "private reports, screenshots, source code and internal financial "
    "information are named as things not to take.",
    "Evidence is never converted into an offer. Credentials, direct industry "
    "experience, unfamiliar context and bias are named as things a record "
    "does not remove.",
    "Illustration is never converted into evidence. The worked examples are "
    "phrased as the shape of a record, not as a sourced case."],
9: ["Adjacent is never converted into direct. The relearn column is the point "
    "of the video.",
    "Regulation, credentials, industry knowledge, customer knowledge, "
    "technical depth and local relationships are named as genuine gaps.",
    "Employer preference, pay, a crowded market and bias are named as real "
    "limits that do not disappear because the viewer can explain themselves "
    "well."],
10: ["Experience is never converted into context. The video's whole first "
     "movement is that they are not the same thing.",
     "A quick win is explicitly refused as a universal requirement. Long "
     "learning curves, regulation and senior roles needing context before "
     "intervention are named.",
     "A mismatch between the job on paper and the job in practice is "
     "explicitly said not to automatically mean leave."],
11: ["A mismatch is never converted into betrayal. Roles change for "
     "legitimate reasons and the video says so first.",
     "The framework explicitly does not tell the viewer whether to leave.",
     "Compensation, health, caregiving, immigration, geography, timing, the "
     "market and financial runway are all named as real constraints."],
12: ["The accomplishment is synthetic and is labelled on camera and on the "
     "card.",
     "Proof is never converted into an offer. The boundary says a strong "
     "reconstruction can still lose to domain knowledge, a credential or "
     "direct exposure.",
     "Judgment is defined as a call that could have gone the other way, which "
     "keeps execution from being inflated into decision authority."],
13: ["Employer names are removed by the approved anonymization patch and are "
     "not restored anywhere in this package.",
     "Every count is a count within the 28 postings. The video says twenty-"
     "eight postings is not the labor market.",
     "Preferred is never converted into required. The video reports what was "
     "hard in six, preferred in about nine and unmentioned in eleven, and "
     "says three of those could reasonably be read either way.",
     "Adjacent is never converted into direct. The video refuses the phrase "
     "directly transferable as a conclusion that belongs to the reader."],
14: ["Employer names are removed by the approved anonymization patch and are "
     "not restored. Both postings are described by industry only.",
     "Intent is never read. The stated rule of the video is that nobody "
     "reading a posting knows what a hiring manager thinks.",
     "Preferred is never converted into required. The whole video is the "
     "observation that two employers inverted each other on exactly that."],
}

if __name__ == "__main__":
    for n in range(4, 15):
        print("V%-3d %-52s %s" % (n, TITLES[n][0][:52], MEMORY[n][:44]))
    print("\nexercises:", len(EXERCISE), "next-lines:", len(NEXT_LINE),
          "protect:", len(PROTECT))
