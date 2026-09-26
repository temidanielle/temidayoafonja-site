# -*- coding: utf-8 -*-
"""Every piece of content for the playlist kit.

Source of truth, both uploaded September 24, 2026:
  PLAYLIST  YouTube_Playlist_New_Job_2027_Without_Starting_Over_2026-09-24.docx
            sha256 43a67cfd09d5b689... (re-uploaded September 26, 2026)
  BRIEF     YouTube_Production_Brief_for_Code_Playlist_2027_2026-09-24.docx
            sha256 b2f6c2ac8e14a7f1... (re-uploaded September 26, 2026)

Hook, roadmap and close are transcribed word for word from the playlist
document. Middle sections are the playlist document's own talking points, kept
as talking points. Nothing here is invented: every story, figure and name comes
from the scripts.

The release plan changed after those documents were written. Every reference to
2027, January, the new year and December recording is gone, and the lines that
leaned on the new year are rewritten to work at any time of year. Each of those
rewrites is marked RELEASE EDIT below.

Chapter titles and the spoken roadmap now match word for word. Where they
differed only by inflection, one side was moved to the other. Each is marked
ROADMAP MATCH.
"""

# ---------------------------------------------------------------- brand
NAVY = "#0F2347"
SAND = "#F5F0E8"
GOLD = "#C9A84C"

# RELEASE EDIT: the year is out of the playlist title.
PLAYLIST_TITLE = "How to Get a New Job Without Starting Over"
PLAYLIST_DESC = ("A three-part series for experienced professionals: the five "
                 "steps before your resume, how to answer “you "
                 "don’t have direct experience,” and how to get "
                 "referred when your network is thin.")

LOWER_THIRD = "Temidayo Afonja · Founder, The Density Group"
CAPTION_TERMS = ["Temidayo", "Deloitte", "CISSP", "NYU", "Proof Line",
                 "Career Evidence Starter"]

# ---------------------------------------------------------------- video 1
V1 = dict(
    n=1,
    slug="VIDEO_1_NEW_JOB",   # RELEASE EDIT: year out of the folder name
    publish="Monday, October 5, 2026",
    publish_time="7:00 a.m. Central",
    # RELEASE EDIT: the year is out of both titles.
    title="How to Get a New Job When You Have 10+ Years of Experience",
    alt_title="How to Change Jobs Without Starting Over",
    length="About 12 minutes",
    thumb_text=["10+ YEARS.", "STILL NO OFFER?"],
    thumb_direction=(
        "You at chest height, direct to camera, calm and knowing (a slight "
        "raised eyebrow, not shock). Bookshelf or clean home-office "
        "background, warm light. Text on the left in two stacked lines, heavy "
        "sans serif, sand on navy band or navy on sand. One small gold accent "
        "under “STILL NO OFFER?” Nothing else on the image."),
    # RELEASE EDIT: the year is out of the first two tags.
    tags=["new job", "job search", "career change",
          "experienced professionals", "mid-career job search",
          "how to get a job", "career pivot", "job search tips"],
    chapters=[
        ("0:00", "If the job search feels built for someone else"),
        ("0:45", "Why the usual advice fails experienced people"),
        ("2:00", "Step 1: Decide what kind of move you are making"),
        ("3:30", "Step 2: Build your evidence before your resume"),
        ("5:30", "Step 3: Translate what travels"),
        ("7:00", "Step 4: Become referable, even if your network is thin"),
        ("8:45", "Step 5: Name the gap before they do"),
        ("10:00", "Rapid-fire round"),
        ("11:30", "Where to start this week"),
    ],
    hook=[
        "If you have ten, fifteen, or twenty years of experience and the job "
        "search feels built for someone else, this video is for you.",
        "I am Temidayo Afonja. I have been hired by Deloitte three times, I "
        "have changed industries more than once, and I have had an offer "
        "rescinded before I could start. Here is how I would look for a new "
        "job right now if I were you.",   # RELEASE EDIT
    ],
    roadmap=[
        # ROADMAP MATCH: gerunds became imperatives so each clause is the
        # chapter title word for word, minus its "Step N: " prefix. The
        # imperative reads as naturally aloud and keeps Step numbering in the
        # chapter list.
        "In this video, I will walk you through five steps. First, decide "
        "what kind of move you are making. Second, build your evidence "
        "before your resume. Third, translate what travels. "
        "Fourth, become referable, even if your network is thin. And fifth, "
        "name the gap before they do.",
        "Then I will finish with a rapid-fire round of real questions people "
        "have asked me. The chapters are below if you want to jump to one.",
    ],
    close=[
        "You are not starting over. You are starting from what you built.",
        "If you want a first step, the free Career Evidence Starter is linked "
        "below. And watch the next video in this playlist, on how to answer "
        "“you don’t have direct experience.”",
    ],
    # (chapter time, section heading, [ (kind, text) ]) kind in:
    #   point, story, say, screen
    middle=[
        ("0:45", "WHY THE USUAL ADVICE FAILS YOU", [
            ("point", "Most job advice is written for someone early in their "
                      "career or someone who has already been laid off: update "
                      "the resume, apply more, network."),
            ("point", "For experienced people, that advice skips the hard "
                      "part. Your current employer has watched you use your "
                      "experience. The next one has not."),
            ("point", "The cost: capable people start applying a level down, "
                      "or start describing twenty years of work in the "
                      "language of the loss."),
            ("say", "Before the resume, there is work to do. Five "
                    "steps."),
        ]),
        ("2:00", "STEP 1: DECIDE WHAT KIND OF MOVE YOU ARE MAKING", [
            ("point", "Most career advice gives you two options: stay or "
                      "leave. There are at least seven."),
            ("screen", "Name a few on screen: remain and deepen, translate "
                       "what is built, widen exposure, test portability, "
                       "repair the conditions, prepare for exit, seek an "
                       "outside perspective."),
            ("point", "An internal move may be the fastest path in a slow "
                      "hiring market."),
            ("say", "Pick the move your evidence supports testing next. It "
                    "can change in ninety days."),
        ]),
        ("3:30", "STEP 2: BUILD YOUR EVIDENCE BEFORE YOUR RESUME", [
            ("story", "An offer I had accepted was rescinded before I "
                      "started. I drove for Uber while I worked out what came "
                      "next. Months later a recruiter found me on LinkedIn, "
                      "and I went back to Deloitte for the third time. My "
                      "circumstances had changed faster than my experience "
                      "had."),
            ("point", "The lesson: your history has to be readable by someone "
                      "who was not there."),
            ("screen", "Show a Proof Line on screen, built from five parts: "
                       "the situation, your part, the scope, what changed, and "
                       "the evidence you are allowed to keep."),
            ("say", "Your memory is not a record. Write one entry this week."),
        ]),
        ("5:30", "STEP 3: TRANSLATE WHAT TRAVELS", [
            ("screen", "Four questions on screen: What travels? What does "
                       "not? What can you prove? What must you relearn?"),
            ("story", "I failed the CISSP, a cybersecurity certification, "
                      "three times. My accounting and audit background came "
                      "with me. It did not remove what I still had to learn. "
                      "That result pushed me toward NYU’s master’s "
                      "in cybersecurity risk and strategy."),
            ("say", "Starting as a learner is not the same as starting from "
                    "zero."),
        ]),
        ("7:00", "STEP 4: BECOME REFERABLE, EVEN IF YOUR NETWORK IS THIN", [
            ("point", "Referrals matter, and access to them is uneven. Not "
                      "everyone grew up with a network, and many experienced "
                      "people spent their best years inside one company."),
            ("point", "You can still become referable: tell five people "
                      "exactly what you are good at, using a Proof Line "
                      "instead of your old title."),
            ("point", "Reconnect with former colleagues and managers. How you "
                      "left a place shapes who will vouch for you later."),
            ("point", "For leaders watching: if you only hire through "
                      "referrals, you are hiring your network. Open the door "
                      "wider."),
        ]),
        ("8:45", "STEP 5: NAME THE GAP BEFORE THEY DO", [
            ("point", "Every career move has a gap. The interviewer will find "
                      "it."),
            ("screen", "Sample answer on screen: “I have led this kind "
                       "of decision in a different industry. Here is what I "
                       "did and what changed. What I would still need to learn "
                       "here is your regulatory context, and here is how I "
                       "plan to learn it.”"),
            ("say", "Naming the gap early is how you keep their trust."),
        ]),
        ("10:00", "RAPID-FIRE ROUND (real questions people have asked me)", [
            ("point", "“My company may be sold. Stay or start "
                      "looking?” Start preparing either way: evidence, "
                      "relationships, and one option inside and one outside."),
            ("point", "“I survived two reorganizations. Now what?” "
                      "Surviving and being ready are different. Ask what the "
                      "work built in the last ninety days."),
            ("point", "“Should I take a lower title?” Look at what "
                      "the work will make you practice. A smaller title with "
                      "bigger practice can be the stronger move."),
            ("point", "“They said I need direct experience.” That "
                      "is the next video in this playlist."),
            ("point", "“My offer was rescinded.” Your capability "
                      "did not disappear. Start with evidence, then tell five "
                      "people."),
        ]),
    ],
    description=[
        # RELEASE EDIT
        "Looking for a new job with ten or more years of experience? "
        "Reorganizations, a company that might be sold, “direct "
        "experience required,” being passed over, or an offer that "
        "disappeared. Most job advice was not written for you.",
        "In this video: five steps I would take before touching my "
        "resume, and a rapid-fire round of real questions people "
        "have asked me.",
        "Free Career Evidence Starter: "
        "https://temidayoafonja.com/career-evidence-starter",
        "Keep the Proof, my career evidence system: "
        "https://temidayoafonja.gumroad.com/l/keep-the-proof",
        "Subscribe for more on changing careers without starting over.",
    ],
    pinned="Which step is hardest for you right now? Tell me in a sentence "
           "and I may answer it in a future video.",
    end_screen="Video 2 of this playlist, plus the playlist itself.",
    cards=[("8:45", "Video 2"), ("7:00", "Video 3")],
)

# ---------------------------------------------------------------- video 2
V2 = dict(
    n=2,
    slug="VIDEO_2_DIRECT_EXPERIENCE",
    publish="Wednesday, October 7, 2026",
    publish_time="7:00 a.m. Central",
    title="How to Answer “You Don’t Have Direct Experience” "
          "When You Have 10+ Years",
    alt_title="No Direct Experience? How Experienced Professionals Should "
              "Answer",
    length="About 9 minutes",
    thumb_text=["“DIRECT EXPERIENCE?”"],
    thumb_direction=(
        "You mid-thought, one hand raised slightly as if answering a "
        "question, a composed half smile. Same background and color treatment "
        "as Video 1 so the playlist reads as a set. Text in quotation marks, "
        "large, in one line if possible."),
    tags=["direct experience", "no direct experience", "transferable skills",
          "interview answers", "career change interview", "career pivot",
          "experienced professionals"],
    chapters=[
        ("0:00", "Years of experience and still “no direct "
                 "experience”"),
        ("0:40", "What the employer is deciding"),
        # ROADMAP MATCH: chapters now carry the roadmap's own wording.
        ("2:00", "Why listing transferable skills is not enough"),
        ("3:30", "The four questions I use"),
        ("5:30", "How to build one Proof Line"),
        ("7:00", "How to name the gap"),
        ("8:15", "A script you can use in your next interview"),
    ],
    hook=[
        # WORDING CHECK: the hook says "ten, fifteen, or twenty years".
        "You have ten, fifteen, or twenty years of experience. The posting "
        "still says no. “Direct experience required.” Here is how "
        "to answer that, in an application and in an interview.",
    ],
    roadmap=[
        "Here is what we will cover. What the employer is deciding. Why "
        "listing transferable skills is not enough. The four questions I use. "
        "How to build one Proof Line. How to name the gap. And a script you "
        "can use in your next interview.",
    ],
    close=[
        "Adjacent experience still has to be read. Your job is to make it "
        "readable.",
        "The Career Evidence Starter below walks you through your first Proof "
        "Line. And the last video in this playlist covers what to do when "
        "your network is thin.",
    ],
    middle=[
        ("0:40", "WHAT THE EMPLOYER IS DECIDING", [
            ("point", "The employer is deciding whether enough of your value "
                      "can be trusted here, in their context."),
            ("point", "The consequence if you answer badly: you either "
                      "overclaim and lose trust, or undersell and accept "
                      "less."),
        ]),
        ("2:00", "WHY “TRANSFERABLE SKILLS” IS NOT ENOUGH", [
            ("screen", "Show on screen: “Strategic thinking” could "
                       "mean you prepared the analysis, or you made the "
                       "trade-off and carried the consequence. Same label, "
                       "different experience."),
            ("say", "The word is not the evidence."),
        ]),
        ("3:30", "THE FOUR QUESTIONS", [
            ("point", "What travels? Judgment, patterns, ways of solving "
                      "problems you have shown more than once."),
            ("point", "What does not? Internal systems, relationships, "
                      "reputation, company language."),
            ("point", "What can you prove? A specific decision, what changed, "
                      "who saw it."),
            ("point", "What must you relearn? New regulation, vocabulary, "
                      "credibility."),
            ("story", "At 15 I arrived in Houston from Lagos. I had already "
                      "led a dance and drama group, and nobody could see it. "
                      "What I carried had to be made visible."),
        ]),
        ("5:30", "BUILD THE ANSWER: ONE PROOF LINE", [
            ("screen", "Walk through one example on screen, with the five "
                       "parts: situation, your part, scope, what changed, "
                       "evidence."),
            ("point", "Turn it into a single sentence the hiring manager can "
                      "repeat to someone else."),
        ]),
        ("7:00", "NAME THE GAP", [
            ("point", "Say what you would need to learn, and how you would "
                      "learn it, before they ask."),
            ("point", "This is how an experienced candidate stays credible."),
        ]),
        ("8:15", "YOUR SCRIPT (on screen, then read)", [
            ("screen", "“You’re right that I haven’t held this "
                       "exact title. Here’s what I have done that this "
                       "role asks for: [Proof Line]. The part I would still "
                       "need to learn is [gap], and here is how I would learn "
                       "it in the first ninety days.”"),
        ]),
    ],
    description=[
        "Ten or more years of experience and still hearing “we need "
        "someone with direct experience”? This video shows what the "
        "employer is deciding, why listing transferable skills rarely works, "
        "and a script for answering the question in an application or "
        "interview.",
        "Free Career Evidence Starter: "
        "https://temidayoafonja.com/career-evidence-starter",
        "Keep the Proof: https://temidayoafonja.gumroad.com/l/keep-the-proof",
    ],
    pinned="What exact phrase were you told when you did not get a role? "
           "Share it below. I read every one.",
    end_screen="Video 3 and the playlist.",
    cards=[("0:40", "Video 1, for anyone who starts here")],
)

# ---------------------------------------------------------------- video 3
V3 = dict(
    n=3,
    slug="VIDEO_3_REFERRED_THIN_NETWORK",
    publish="Friday, October 9, 2026",
    publish_time="7:00 a.m. Central",
    title="How to Get Referred When Your Network Is Thin",
    # RELEASE EDIT: the year is out of the alternate title.
    alt_title="No Network? How Experienced Professionals Get Referred",
    length="About 8 minutes",
    thumb_text=["NO NETWORK?", "START HERE"],
    thumb_direction=(
        "You looking slightly off camera, then toward the viewer, warm and "
        "steady. Same set design as Videos 1 and 2. Text in two lines: "
        "“NO NETWORK?” and “START HERE.”"),
    tags=["referrals", "how to get a referral", "networking",
          "job search without a network", "career change",
          "experienced professionals", "job referral tips"],
    chapters=[
        ("0:00", "Referrals matter, and access is uneven"),
        ("1:00", "What a referral really is"),
        ("2:15", "Step 1: Become easy to describe"),
        ("3:45", "Step 2: Tell five people"),
        # ROADMAP MATCH: "the people", and "who referrals leave out".
        ("5:00", "Step 3: Reconnect with the people who saw your work"),
        ("6:30", "For leaders: who referrals leave out"),
        ("7:30", "This week"),
    ],
    hook=[
        "Referrals are one of the fastest ways into a new job. And not "
        "everyone has a network that can refer them. If that is you, this "
        "video is for you.",
    ],
    roadmap=[
        "I will show you three steps. First, become easy to describe. Second, "
        "tell five people. Third, reconnect with the people who saw your "
        "work. Then a word for leaders about who referrals leave out.",
    ],
    close=[
        "You do not need a big network. You need a few people who can "
        "describe what you do well.",
        "Start with the Career Evidence Starter below, then send your Proof "
        "Line to one person today. That is the end of this playlist. If it "
        "helped, share it with someone who is looking right now.",
    ],
    middle=[
        ("0:00", "REFERRALS MATTER, AND ACCESS IS UNEVEN", [
            ("point", "Name the reality plainly: people who changed "
                      "industries, moved countries, took time away, or spent "
                      "years inside one company often have thinner networks "
                      "outside it."),
            ("point", "The consequence: good candidates wait for postings "
                      "while others walk in through a side door."),
        ]),
        ("1:00", "WHAT A REFERRAL REALLY IS", [
            ("point", "A referral is someone willing to put their name next "
                      "to yours. They need two things: to trust you, and to "
                      "be able to describe what you are good at."),
            ("point", "Most people only work on the first."),
        ]),
        ("2:15", "STEP 1: BECOME EASY TO DESCRIBE", [
            ("point", "Write one Proof Line someone else could repeat for "
                      "you."),
            ("point", "Drop the internal job title and company language. Use "
                      "the situation, your part, and what changed."),
        ]),
        ("3:45", "STEP 2: TELL FIVE PEOPLE", [
            ("point", "Five specific people, not a mass post. Say exactly "
                      "what you are good at and what kind of role or problem "
                      "you are looking for."),
            ("point", "Give them the sentence. Make it easy to pass along."),
        ]),
        ("5:00", "STEP 3: RECONNECT WITH PEOPLE WHO SAW YOUR WORK", [
            ("point", "Former managers, peers, clients, classmates, church or "
                      "community leaders who watched you lead."),
            ("story", "Deloitte hired me three times. How you leave a place "
                      "shapes who will vouch for you later."),
            ("story_opt", "At Texas Southern and through NABA, I kept asking "
                          "people with accounting backgrounds how they built "
                          "careers beside accounting. Those conversations "
                          "shaped my path."),
        ]),
        ("6:30", "FOR LEADERS: WHO YOUR REFERRALS LEAVE OUT", [
            ("point", "If most of your hires come through referrals, you are "
                      "hiring the networks you already have."),
            ("point", "Ask who never gets referred, and why. Build a second "
                      "door."),
        ]),
    ],
    description=[
        "Referrals can open doors fast, and not everyone has a network ready "
        "to refer them. If you changed industries, moved countries, took time "
        "away, or spent years inside one company, this video shows how to "
        "become referable anyway, and what leaders can do about who referrals "
        "leave out.",
        "Free Career Evidence Starter: "
        "https://temidayoafonja.com/career-evidence-starter",
        # RELEASE EDIT
        "Watch the full playlist: How to Get a New Job Without "
        "Starting Over",
    ],
    pinned="Who is one person who saw your best work up close and has not "
           "heard from you in a year? Send them a note this week.",
    end_screen="The full playlist and the channel subscribe.",
    cards=[("0:00", "Video 1")],
)

# Chapter indices the spoken roadmap enumerates. The others are the hook
# chapter, the setup chapter before step one, and the closing chapter, none of
# which the roadmap names.
ROADMAP_CHAPTERS = {1: range(2, 8), 2: range(1, 7), 3: range(2, 6)}

# Thumbnail words and photo direction only. Temidayo builds the thumbnails in
# Canva, so this kit produces no thumbnail image.
THUMB_DIRECTION = {
 1: "Calm and knowing. A slight raised eyebrow, not shock. Chest height, "
    "direct to camera.",
 2: "Mid-answer. One hand slightly raised, composed half smile.",
 3: "Warm and steady, looking toward the camera.",
}

VIDEOS = [V1, V2, V3]
BY_N = {v["n"]: v for v in VIDEOS}
