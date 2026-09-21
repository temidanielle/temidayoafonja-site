# -*- coding: utf-8 -*-
"""V14 packaging options. Five pairs, one recommendation, nothing chosen on
Temidayo's behalf. The working script is built on the recommendation only so that a
complete episode exists to look at."""

BANNED = ["The Experience Gap Hiring Managers Care About"]

OPTIONS = [
dict(n=1,
 title="What Your Experience Proves, and What It Only Suggests",
 thumb="PROVES / SUGGESTS",
 gap="Most of what is on your resume is a suggestion, and the posting itself tells you which of your lines is which.",
 fit=("The episode's whole method is splitting evidence from implication, one posting at a time, "
      "and this title says exactly that. It sits in the thumbnail territory the brief prefers, it "
      "promises a distinction rather than a verdict, which is how V13 is titled, and it contains no "
      "claim about what anybody thinks. It is also the most durable of the five: it will still be "
      "accurate in two years when both postings are long gone."),
 risk="Least dramatic of the five. It wins on truth and search, not on the first half second."),
dict(n=2,
 title="I Read Two Real Job Postings Line by Line",
 thumb="PROVES / SUGGESTS",
 gap="Two employers hiring what reads like the same job, and the thing one of them calls optional is the thing the other one gates on.",
 fit=("Truth in packaging: the episode is literally a read-along, and watch-me-read is a format "
      "promise viewers can verify in the first ten seconds. Pairs well with the preferred thumbnail "
      "because the title carries the format and the thumbnail carries the idea."),
 risk="Weaker evergreen search. It describes the format rather than the problem the viewer has."),
dict(n=3,
 title="Two Job Postings. Same Work. Opposite Requirements.",
 thumb="OPPOSITE LOCKS",
 gap="One posting says you do not need to know the subject matter. The other says seven years in the industry or nothing.",
 fit=("The contrast pair is the artifact the whole episode is built on, and this title puts the "
      "surprise in the title instead of holding it back. Fully honest: it describes the two documents "
      "and claims nothing about intent."),
 risk="Moves away from the PROVES / SUGGESTS thumbnail territory the brief prefers. The curiosity is "
      "about the postings rather than about the viewer, which historically pulls fewer of the people "
      "who most need the episode."),
dict(n=4,
 title="Required or Preferred? How to Tell What a Job Posting Is Really Gating On",
 thumb="REQUIRED / PREFERRED",
 gap="The same requirement is hard in one posting and optional in another, and the page tells you which if you read the right column.",
 fit=("Names the single most actionable mechanic in the episode. Strong search intent, and it sets a "
      "promise the video keeps literally, since the first pass of the closing exercise is marking "
      "required against preferred."),
 risk="Reads as a how-to rather than an observation, which makes the two-posting read feel like setup "
      "instead of the point. Also the narrowest of the five."),
dict(n=5,
 title="What One Job Posting Can and Cannot Tell You About Your Own Experience",
 thumb="PROVES / SUGGESTS",
 gap="A posting will tell you exactly what it is asking you to prove, and it will never tell you what anybody thinks of you.",
 fit=("Closest to the spoken rule of the episode, and the can-and-cannot shape matches the two-part "
      "verdict sentence used after each posting. Refuses mind reading in the title itself, which is "
      "unusual in this category and is a real differentiator."),
 risk="Long. Truncates badly on mobile, where the useful half sits after the cut."),
]

RECOMMENDED = 1
RECOMMENDED_LABEL = "RECOMMENDED, PENDING TEMIDAYO APPROVAL"
RUNNER_UP = 2

WHY = ("Option 1 is recommended because it is the only one of the five that is simultaneously in the "
       "preferred thumbnail territory, aligned to both audit questions the episode answers, free of any "
       "claim about what a reader thinks, and still true once these two specific postings are gone. "
       "Option 2 is the runner-up and is the better choice if the format itself should carry the "
       "promise. Nothing here is decided. The working script is built on Option 1 so that a complete "
       "episode exists to react to, and swapping in any other option changes the spoken hook, the "
       "on-screen title card, the description's first line and V13's Watch Next line. Those four "
       "places are listed in the working script so the swap is mechanical.")

SWAP_POINTS = [
 "V14 recording master, HOOK: no spoken line names the title, so the hook survives any of the five unchanged.",
 "V14 full-screen card V14_FS_04_PROVES_OR_SUGGESTS: the headline matches Options 1, 2 and 5. Options 3 and 4 need a new headline.",
 "V14 description, opening line and the title field in the metadata sheet.",
 "V13 description, Watch next line, currently carrying the working title with a bracketed confirm note.",
 "V13 recording master, WATCH NEXT: written to describe the episode rather than name it, so it needs no change under any of the five.",
]
