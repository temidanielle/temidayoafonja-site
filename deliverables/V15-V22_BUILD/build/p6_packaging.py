# -*- coding: utf-8 -*-
"""V20 thumbnail decision. Three candidates, one recommendation, pending approval.

The V20 TITLE is locked and is not reopened here. Only the thumbnail line is open.
"""

V20_TITLE = "What Happens When the Next Step in Your Career Disappears?"
STATUS = ("PENDING TEMIDAYO APPROVAL. p6_script20.THUMB currently holds the literal string "
          "PENDING TEMIDAYO APPROVAL and will keep holding it until one of the three lines "
          "below is chosen. The production pack ships with that placeholder on purpose, so "
          "that an unapproved thumbnail line cannot reach a card or a render by accident.")

RULED_OUT = [
 ("THERE'S NO NEXT ROLE",
  "Too close to V22's locked THE NEXT RUNG IS GONE. Two consecutive-ish episodes in the "
  "same playlist would read as the same video twice in a feed, and V22 is the one that "
  "earns that line, because V22 is the structural diagnosis and V20 is not."),
 ("MIDDLE MANAGEMENT IS DYING",
  "The source of record explicitly says this overstates the case, and V20 spends a "
  "paragraph refusing it. A thumbnail must not assert what the script corrects."),
]

CANDIDATES = [
 dict(rank=1,
      line="THE BOX ABOVE YOU",
      why="It is the episode's own image. The script says a box above you that people "
          "moved into, then it was not. It states the subject without making a claim the "
          "script then has to walk back, it does not collide with V22, and it reads at "
          "thumbnail size in three short words.",
      risk="It is quieter than the rest of the set. Somebody scrolling fast may not "
           "register what the box is."),
 dict(rank=2,
      line="NOT PROMISED. BUT THERE.",
      why="Lifted verbatim from the cold open. It carries the specific feeling of the "
          "episode, which is not anger but the removal of something nobody ever actually "
          "committed to. Two short beats match the house punctuation style used in V16.",
      risk="It needs the title to make sense. Alone it is ambiguous, so it depends on the "
           "title being read, which on mobile is not guaranteed."),
 dict(rank=3,
      line="WHAT WAS IT FOR?",
      why="It points at the useful part of the episode, which is taking the promotion "
          "apart into what it was going to supply. It is a question, matching V19 and "
          "V21 in the set.",
      risk="Three of eight thumbnails in this run would then be questions. It also reads "
           "more existential than the episode is; V20 is practical."),
]

RECOMMENDATION = ("Recommend candidate 1, THE BOX ABOVE YOU. It is the only one of the "
                  "three that is self-contained at thumbnail size, does not compete with "
                  "V22, and does not assert anything the script corrects. If Temidayo "
                  "wants more energy in the set, candidate 2 is the alternative and it is "
                  "verbatim from the master, which candidate 1 is not.")

NOT_REOPENED = ("The V20 title is locked and was not reconsidered. No other title, "
                "thumbnail, description, Short or Watch Next in V15 to V22 is open in this "
                "document, and nothing in V4 to V14 is touched by it.")
