# -*- coding: utf-8 -*-
"""Camera beats, artifact/B-roll moments, sound accents and full-screen cards.

Every cue is anchored to an exact sentence from that video's recording master.
anchors_ok() proves each trigger sentence exists verbatim before anything is written.
"""
import importlib
import p3_blocks as B

def master_sentences(n):
    m = importlib.import_module(B.MODS[n])
    return [s for _, ps in m.SECTIONS for p in ps for s in B.sentences(p)]

FULLSCREEN = {
12: [
 ("V12_FS_01_THE_LINE", "ONE LINE",
  ["“Led a cross-functional transformation that improved on-time delivery by 18 percent.”"],
  "WRITTEN FOR THIS VIDEO. NOT A REAL RESUME."),
 ("V12_FS_02_TWO_PILES", "WHAT A STRANGER CAN DO WITH IT",
  ["CAN CHECK    one number", "MUST ASSUME    everything else"], None),
 ("V12_FS_03_MINE_TO_DECIDE", "WHAT WAS MINE TO DECIDE",
  ["What did you sequence?", "What did you escalate?", "What tradeoff did you hand to somebody else?"], None),
 ("V12_FS_04_NOT_OBVIOUS", "WHAT WAS NOT OBVIOUS",
  ["Two reasonable options.", "I picked one.", "Here is why."], None),
 ("V12_FS_05_HOW_YOU_KNOW", "RESULT, THEN METHOD",
  ["RESULT    89 percent", "HOW I KNOW    one definition, baseline recalculated"], None),
 ("V12_FS_06_THE_REWRITE", "THE SAME ACCOMPLISHMENT, PUT BACK TOGETHER",
  ["Before    three depots, 71 percent, three definitions of late",
   "Mine to decide    the definition, and the order",
   "Not obvious    worst depot last",
   "How I know    one definition, baseline recalculated"],
  "SAME SYNTHETIC EXAMPLE. WRITTEN FOR THIS VIDEO."),
 ("V12_FS_07_BEFORE_AND_AFTER", "BEFORE / AFTER",
  ["BEFORE    a number with nothing under it", "AFTER    something a stranger can question"], None),
 ("V12_FS_08_TEN_MINUTES", "HOW THE TEN MINUTES GO",
  ["2 min    what was true before", "3 min    what was mine to decide",
   "2 min    what was not obvious", "3 min    what changed, and how I know"], None),
 ("V12_FS_09_THE_BOUNDARY", "PROOF IS NOT AN OFFER",
  ["Proof makes you readable.", "It does not make you chosen."], None),
 ("V12_WATCH_NEXT", "WATCH NEXT",
  ["Which Parts of Your Experience Actually Transfer to Another Industry?"], None),
],
13: [
 ("V13_FS_01_THE_SAMPLE", "WHAT THIS IS",
  ["~55 surfaced", "40 read in full", "28 in the set", "10 healthcare  ·  10 financial services  ·  8 technology",
   "18 exclusions logged", "all collected September 10, 2026"],
  "28 POSTINGS. NOT THE LABOR MARKET."),
 ("V13_FS_02_THREE_RISKS", "MANAGE RISK",
  ["Humana    project risk register    a project slips",
   "Wells Fargo    all applicable risk programs    regulatory and financial exposure",
   "Mass General Brigham    duty officer, surge events    patient care"],
  "POSTING LANGUAGE ONLY. COLLECTED SEPTEMBER 10, 2026."),
 ("V13_FS_03_WHAT_TRAVELS", "WHAT SHOWED UP EVERYWHERE",
  ["Owning a plan end to end", "Moving people who do not report to you",
   "The reporting rhythm that keeps leaders deciding", "The mechanics of risk and issue management",
   "Delivery method itself"], None),
 ("V13_FS_04_WHERE_IT_BREAKS", "WHAT WRONG LOOKS LIKE",
  ["in the project    a dependency nobody sized",
   "in the bank    a control that fails an examiner",
   "in the hospital    a patient movement that cannot happen"], None),
 ("V13_FS_05_THREE_KINDS_OF_GAP", "WHICH KIND OF GAP IS IT",
  ["READ IT    methods, frameworks, common tools",
   "SEE IT    how the work actually operates",
   "BE GIVEN IT    access, authority, supervised practice"], None),
 ("V13_FS_06_HARD_OR_PREFERRED", "IN THESE 28 POSTINGS",
  ["same-industry experience hard in 6", "preferred in about 9", "not mentioned in 11",
   "PM certification hard in 4"],
  "COUNTS WITHIN THIS SAMPLE ONLY."),
 ("V13_FS_07_WHAT_NOT_TO_CLAIM", "WHAT NOT TO CLAIM",
  ["“directly transferable”", "“industry is just context”",
   "“I can learn the domain quickly”", "“I am not qualified”"], None),
 ("V13_FS_08_THE_SECOND_QUESTION", "THE SECOND QUESTION",
  ["The words match.", "Does the decision underneath match too?",
   "And what happens there when it goes wrong?"], None),
 ("V13_WATCH_NEXT", "WATCH NEXT",
  ["Two real postings, read side by side"], None),
],
14: [
 ("V14_FS_01_THE_RULE", "THE RULE FOR THIS VIDEO",
  ["Read what is written.", "Do not guess what anybody thinks."], None),
 ("V14_FS_02_POSTING_ONE", "POSTING ONE",
  ["Humana    Senior Project Manager", "HARD    5 years of project management, a degree",
   "PREFERRED    PMP, Lean or Six Sigma, the risk adjustment knowledge",
   "“comfortable working on new projects with limited knowledge”"],
  "COLLECTED SEPTEMBER 10, 2026. POSTED JANUARY 2026."),
 ("V14_FS_03_SIDE_BY_SIDE", "SIDE BY SIDE",
  ["HUMANA    project management required, subject matter preferred",
   "J.P. MORGAN WEALTH MANAGEMENT    industry years required, project management preferred"],
  "POSTING LANGUAGE ONLY. NEITHER POSTING WAS OPEN ON THE COLLECTION DATE."),
 ("V14_FS_04_WHAT_A_READER_CAN_CHECK", "WHAT A READER CAN CHECK",
  ["CAN BE CHECKED    a date, a scope, a number with a method under it, a decision that could have gone the other way",
   "HAS TO BE TAKEN ON TRUST    strategic, transformational, extensive experience, proven track record"], None),
 ("V14_FS_05_AFTER_EACH_POSTING", "AFTER EACH POSTING",
  ["What do these words actually support?", "What can I still not tell?"], None),
 ("V14_FS_06_WHAT_IM_NOT_SAYING", "WHAT I AM NOT SAYING",
  ["The posting is not the truth.", "Intent cannot be read off the page."], None),
 ("V14_FS_07_TWO_PASSES", "READ IT TWICE",
  ["FIRST PASS    required or preferred, in the posting's own words",
   "SECOND PASS    what these words support, what I still cannot tell"], None),
 ("V14_WATCH_NEXT", "WATCH NEXT",
  ["Turn One Accomplishment Into Proof in 10 Minutes"], None),
],
}

# (trigger sentence, what the camera is doing and why)
CAMERA = {
12: [
 ("And I still cannot tell what you did. I cannot see what was broken before you got there, what you were allowed to decide, what was hard about it, or where the 18 percent came from.",
  "Come off the card to camera. This is the turn from reading to reacting, and it should land as a person judging a sentence, not a narrator."),
 ("Try the harder version. What was mine to decide?",
  "Camera, close. The question is the hinge of the whole video and should be asked, not narrated."),
 ("Same made-up accomplishment. Here it is with all of that put back, read the way the person would write it, in their own voice.",
  "Camera, with the disclosure. Say this looking at the lens so the synthetic framing is unmistakable, then move to the card to read."),
 ("One thing I am not going to promise you. This does not get you hired. Proof and an offer are two different things.",
  "Camera, still and level. No card for the first two sentences. The boundary carries more if nothing is competing with it."),
 ("Put it back.", "Camera. Last three words of the body, held."),
],
13: [
 ("Same two words. Three different jobs.",
  "Cut from the three-column card to camera for the reaction. The card stays up underneath if a split is available."),
 ("I'm Temidayo. This one comes out of a research read I did for this series, and I want to be straight with you about what it is and what it is not.",
  "Camera. The whole provenance section should be delivered to the lens, not read off a card, because it is a promise about method."),
 ("What does not travel is knowing what wrong looks like before it happens.",
  "Camera. This is the sentence the episode exists to deliver."),
 ("And now the part I did not expect.",
  "Camera, a beat of real surprise. Do not smile through it. The finding is genuinely mixed and should sound like it."),
 ("Your experience is not worth less than you thought. It is more specific than you thought. Say the specific thing.",
  "Camera, close, warm. The only consoling line in the video and the one people will clip."),
],
14: [
 ("I am not going to tell you what a hiring manager thinks. I do not know. Nobody reading a posting knows.",
  "Camera, no card. State the rule plainly and let the silence sit for a beat afterward."),
 ("This tells me that project management experience is the hard requirement here. It does not tell me that the subject matter does not matter at all.",
  "Camera. The two-part verdict sentence is the shape of the whole video and should be delivered the same way both times."),
 ("Two employers. Work that reads nearly the same. Different things are required.",
  "Camera, with the two-column card still on screen behind or beside if a split is available."),
 ("Both kinds of lines are normal. The point is to know which of yours give somebody something concrete and which ones still need support, so you do not mistake a strong-sounding phrase for evidence.",
  "Camera, gentle. This is the sentence that keeps the episode from feeling like an accusation."),
 ("You do not have to guess at everything. Sometimes the employer wrote the important part down. Read it.",
  "Camera. Hold after “Read it.”"),
],
}

# (trigger sentence, artifact or B-roll moment)
BROLL = {
12: [
 ("“Led a cross-functional transformation that improved on-time delivery by 18 percent.”",
  "The artifact itself. Hold the single line on screen, alone, long enough to be read twice. Disclosure label stays on the card for the full hold."),
 ("Pile one is what I can check. There is a number. Eighteen percent. That is the whole pile.",
  "Highlight pass over the artifact: the number lights, everything else dims. No motion beyond the dim."),
 ("Before I got there, three depots each ran their own dispatch. On-time delivery sat at 71 percent, and the three of them counted lateness differently, so nobody could agree on the size of the problem.",
  "Build the rebuilt version line by line as each answer is spoken. The finished card is the before/after payoff."),
 ("Here is how the ten minutes actually go. Two on what was true before. Three on what was yours to decide, because you will want to argue with yourself. Two on the call that was not obvious. Three on what changed and how you know.",
  "The ten-minute budget card, built one row at a time on the numbers."),
],
13: [
 ("About fifty-five postings surfaced in the search. I read forty of them all the way through. Twenty-eight went into the set. Ten healthcare, ten financial services, eight technology. Everything I threw out is logged with a reason, eighteen entries, so you can check the work instead of trusting me.",
  "The sample card, built count by count. This is the credibility artifact and should not be rushed."),
 ("The first is a senior project manager job at Humana. Manage risk there means run the project risk register. Spot what could derail the project, log it, escalate it. When that goes wrong, a project slips.",
  "Three-column artifact. Each column fills as its posting is read, with the employer name and the failure mode. Posting language only, no logos, no employer branding."),
 ("In this set, direct same-industry experience was a hard requirement in six of the twenty-eight. Preferred in about nine. Not mentioned at all in eleven. A project management certification was hard in four.",
  "The counts card. Each number appears as it is spoken, and the sample-only label stays on screen the whole time."),
],
14: [
 ("Required: five years of project management, and a bachelor's degree. Preferred: the project management certification, the Lean or Six Sigma belt, and the risk adjustment knowledge itself.",
  "Posting one as an artifact: the requirement list, with required and preferred visually separated. Text only, no employer branding."),
 ("Then look at the requirements. Seven or more years of experience in the financial services industry. Hard. PowerPoint and Excel, hard. Wealth management and knowledge of the Chase business model, preferred. A project management background, preferred.",
  "Posting two as an artifact, laid out identically to posting one so the flip is visible without a word of narration."),
 ("Almost everything the first posting treats as preferred, the second one requires. What the second one treats as preferred, the first one requires.",
  "The side-by-side. Animate the swap once, slowly. This is the single most important frame in the video."),
 ("A line only hints at something when the reader has to supply most of the belief. Strategic. Transformational. Extensive experience. Proven track record. Those words may be true, but by themselves they do not give the reader much to check.",
  "Fill the second column word by word as each phrase is spoken."),
]
}

SOUND = {
12: [
 ("“Led a cross-functional transformation that improved on-time delivery by 18 percent.”", "Card set. Single low placement, no tail."),
 ("You did the work. I believe you. The sentence does not.", "Silence. Cut the bed entirely for these three sentences and bring it back on the next section."),
 ("Try the harder version. What was mine to decide?", "One soft accent under the question."),
 ("If nobody could have disagreed with you, it was a task.", "Accent on “task,” then a half-second of nothing."),
 ("Seven months later all three were at 89 percent, measured against one definition, with the baseline recalculated backward so the comparison was honest.", "Resolve. The rebuilt card completes on this line."),
 ("This does not get you hired.", "Bed out. Nothing under the boundary."),
 ("Put it back.", "Final accent, then hold silence into the CTA."),
],
13: [
 ("Three job postings. All three of them say manage risk.", "Cold open accent on the card."),
 ("Same two words. Three different jobs.", "Hard stop. Cut everything for a beat."),
 ("What does not travel is knowing what wrong looks like before it happens.", "One accent, low, under the whole sentence."),
 ("And now the part I did not expect.", "Bed lifts slightly. This is the only place in the video where the music moves."),
 ("The real question is not whether your experience transfers. It is whether it transfers to this posting.", "Accent on “this posting.”"),
 ("Your experience is not worth less than you thought. It is more specific than you thought. Say the specific thing.", "Resolve and hold under the close."),
],
14: [
 ("Same family of work. Very different requirements.", "Cold open accent as the second column lands."),
 ("I do not know.", "Silence. Nothing under the rule."),
 ("This tells me that project management experience is the hard requirement here. It does not tell me that the subject matter does not matter at all.", "One low accent, used identically after both postings so the pattern is audible."),
 ("This tells me that years inside financial services are the hard requirement here. It does not tell me that a strong outside candidate would never be considered.", "The same accent, same placement. The repetition is the point."),
 ("Two employers. Work that reads nearly the same. Different things are required.", "Accent on the swap animation."),
 ("Sometimes the employer wrote the important part down. Read it.", "Final accent on “Read it,” then out."),
],
}

def anchors_ok():
    bad = []
    for n in (12, 13, 14):
        ms = master_sentences(n)
        joined = " ".join(ms)
        for group, label in ((CAMERA[n], "camera"), (BROLL[n], "broll"), (SOUND[n], "sound")):
            for trig, _ in group:
                if trig not in ms and trig not in joined:
                    bad.append((n, label, trig[:70]))
    return bad

if __name__ == "__main__":
    bad = anchors_ok()
    for n in (12, 13, 14):
        print("V%d  %d full-screen cards  %d camera beats  %d artifact/B-roll  %d sound accents"
              % (n, len(FULLSCREEN[n]), len(CAMERA[n]), len(BROLL[n]), len(SOUND[n])))
    print("unanchored cues:", len(bad))
    for b in bad:
        print("   ", b)
