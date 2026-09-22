# -*- coding: utf-8 -*-
"""Locked packaging for V12, V13 and V14, and the construction rule behind it.

This is a record of decisions already made, not a set of options. No brainstorm was run
in this pass and none should be run from this file.
"""

LOCKED = [
 dict(n="V12", title="How to Turn One Accomplishment Into Proof in 10 Minutes",
      thumb="CAN YOU PROVE IT?",
      construction="Benefit-led how-to. Clear action, desirable result, real time promise.",
      jobs="The title states the transformation and the time. The thumbnail asks the question "
           "the video answers, so the two are not saying the same thing twice.",
      changed="Changed this pass. How to was added to the front of the Phase 2 title."),
 dict(n="V13", title="Which Parts of Your Experience Actually Transfer to Another Industry?",
      thumb="SAME WORDS. DIFFERENT WORK.",
      construction="Question. The promise is a distinction, not a verdict.",
      jobs="The title asks the viewer's own question. The thumbnail states the finding that "
           "makes the question worth watching.",
      changed="Unchanged. Another industry adds specificity and search intent, and the packaging "
              "document says keep it."),
 dict(n="V14", title="I Read Two Similar Jobs. They Wanted Different Proof",
      thumb="SAME WORK. DIFFERENT REQUIREMENTS.",
      construction="Artifact-led discovery, first person. Deliberately not the how-to "
                   "construction, so the slate does not turn one structure into a house formula.",
      jobs="The title carries the behavior, which is Temidayo reading two real documents. The "
           "thumbnail carries the finding. Neither claims to know what anybody thinks.",
      changed="Locked this pass. The previous working packaging, PROVES / SUGGESTS, is retired "
              "and appears nowhere in this pack."),
]

RULE = ("Learn from a successful title construction without turning it into a house formula. The "
        "channel should keep several curiosity mechanisms in rotation: benefit-led how-to, "
        "contradiction, insider authority, consequence, recognizable situation, question, and "
        "artifact-led discovery. Fast comprehension beats an arbitrary word count. A title may be "
        "longer when the promise is clearer, and thumbnail copy may run to a sentence when it is "
        "still readable on a phone. The title and the thumbnail should do different jobs, and "
        "every curiosity gap has to be paid off inside the video.")

BORROWED = ("The construction being borrowed is clear action or problem, plus desirable outcome or "
            "consequence, plus a curiosity gap. It is used on V12, where the script already earns "
            "the promise. It is deliberately not used on V13, whose question already works, or on "
            "V14, which is the slate's first artifact-led packaging.")

V4_V11 = ("The V4 to V14 packaging document also proposes alternative titles and thumbnails for V4 "
          "through V11. Those are NOT approved changes and nothing in this pack acts on them. V4 "
          "to V11 remain locked: no title, thumbnail, script, description, production package, "
          "metadata, Watch Next or Short was opened, read for edit, or modified. The document was "
          "used only to confirm V12, V13 and V14 packaging and to record the construction rule "
          "above for prospective use from V12 onward.")

RETIRED = ("PROVES / SUGGESTS was retired as packaging language. Proves is too absolute for career "
           "evidence: a checkable line supports a claim, it does not establish causation, "
           "readiness, or how any reader will take it. The reconciled V14 script no longer builds "
           "that binary, and no file in this pack carries the phrase.")

EXCLUDED = "The Experience Gap Hiring Managers Care About"

# Where a title or thumbnail is written down, so a future change is mechanical.
TOUCHPOINTS = [
 "The recording master header, and the WATCH NEXT card of whichever video points at it.",
 "The description's opening line and its metadata Title and Thumbnail fields.",
 "The spoken WATCH NEXT line of the video that routes to it. V12 names V13, V13 names V14, and "
 "V14 names V12, so a title change in any one of the three touches exactly one spoken line in "
 "another.",
 "The thumbnail artwork itself, which is specified here but not rendered in this pack.",
]
