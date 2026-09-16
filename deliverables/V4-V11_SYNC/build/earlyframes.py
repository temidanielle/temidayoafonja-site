# -*- coding: utf-8 -*-
"""The early-edit cards the briefs call for and the delivered sets lacked.

The independent review found that the Riverside prompts specify early
long-form cutaways that no camera map, asset index or state ever realized:
V11's two document cards on the second spoken sentence, V8's illustrative
login on "You cannot.", V4's early task-learning card. That made the
packages describe a cutaway and then leave the editor without a file.

Four of those gaps are closed by moving a card that already exists to the
place its own copy belongs. Six needed a state, and those are built here.

Nothing here teaches anything new. Every word on these cards is a sentence
from that video's own reconciled master or the display copy already
approved in its early-edit brief, drawn with the house layouts so the new
cards are indistinguishable in design from the ones beside them. The
archived sprint and V10/V11 builds are never edited: these families are
appended to the frame set in memory at render time, exactly as the five
copy updates are applied.
"""


def build(L, batch):
    """Return {video: [family, ...]} for this batch's layout module."""

    def fam(key, n, trigger, purpose, layout, states, hold, sound,
            treatment="STATEMENT"):
        return dict(key=key, video=n, former=None, trigger=trigger,
                    para=None, mode="FULL SCREEN", purpose=purpose,
                    layout=layout, states=states, svg=False, cls="NEW",
                    build="SINGLE" if len(states) == 1 else "BUILD",
                    hold=hold, sound=sound, source=None,
                    treatment=treatment, early=True)

    def st(name, reveal, draw):
        return dict(name=name, reveal=reveal, draw=draw)

    out = {}

    if batch == "sprint":
        # V7 | the two capable people, and the moment one name comes up.
        # The selection is carried by the spoken line and one quiet accent.
        # Nothing on the card marks a winner: both sides stay identical.
        def _v7(foot):
            return lambda c: L.compare(
                c, "the hook", "Two people can both be good at their jobs.",
                ("person one", "Good at the job",
                 [("dependable", "Yes"), ("experienced", "Yes"),
                  ("working hard", "Yes")]),
                ("person two", "Good at the job",
                 [("dependable", "Yes"), ("experienced", "Yes"),
                  ("working hard", "Yes")]),
                divider="", foot=foot)

        out[7] = [fam(
            "NEW_V7_FS_00_TWO_CAPABLE_PEOPLE", 7,
            "Two people can both be good at their jobs.",
            "Show the equivalence the hook asserts before the outcome "
            "differs, so the viewer is not told one person was better.",
            "Two identical cards, then the outcome line beneath them.",
            [st("NEW_V7_FS_00_TWO_CAPABLE_PEOPLE",
                "Establish on the first sentence.", _v7(None)),
             st("NEW_V7_FS_00B_ONE_NAME_COMES_UP",
                "Add the outcome line only when it is spoken.",
                _v7("one person’s name comes up. the other "
                    "person’s does not."))],
            "Cut in under the first sentence and hold through 'The other "
            "person’s does not.' Return to camera before 'I have seen "
            "versions of that happen inside organizations.'",
            "One quiet accent on the second state only. No second effect "
            "for the first card.", treatment="COMPARE")]

        # V8 | the illustrative login the Riverside prompt already asks for.
        out[8] = [fam(
            "NEW_V8_FS_00_ACCESS_UNAVAILABLE", 8, "You cannot.",
            "Realize the hook's imagined login so the cutaway the brief "
            "specifies has a file, and reuse it for the payoff callback.",
            "One illustrative claim card.",
            [st("NEW_V8_FS_00_ACCESS_UNAVAILABLE", "Single state.",
                lambda c: L.claim_card(
                    c, "illustration", "ACCESS UNAVAILABLE",
                    "Email gone. Dashboard gone. Project folders gone.",
                    foot="illustration. not an employer interface, file, "
                         "logo or customer data.", dark=True, size=58))],
            "Cut on 'You cannot.' and hold through the three losses. "
            "Return to camera for the interviewer's question.",
            "One muted lock or click on 'You cannot.' Nothing on the "
            "callback.", treatment="STATEMENT")]

        # V9 | the may-travel contrast the brief asks for on the third
        # paragraph of the hook. "may" stays visible on both sides.
        out[9] = [fam(
            "NEW_V9_FS_00_MAY_TRAVEL", 9, "Your judgment may travel.",
            "Hold the qualified contrast the hook makes, so the early "
            "promise is not read as a rule about all experience.",
            "Two sides revealed with the sentences that name them.",
            [st("NEW_V9_FS_00_MAY_TRAVEL", "Single state.",
                lambda c: L.compare(
                    c, "the hook", "",
                    ("may travel", "Judgment",
                     [("and", "Problem solving")]),
                    ("may not", "Relationships",
                     [("and", "Knowledge of that company’s systems")]),
                    divider="", foot="some of it absolutely can. not all "
                                     "of it."))],
            "Reveal each side with the sentence that names it. Return to "
            "camera before the regulation and credential boundary.",
            "One quiet paper-switch. No accent on the second side.",
            treatment="COMPARE")]

    else:
        # V10 | the early pressure question, then the two incomplete
        # defaults, one active at a time.
        out[10] = [fam(
            "NEW_V10_FS_00_THE_PRESSURE", 10,
            "And now you feel this pressure to prove they made the right "
            "decision.",
            "Give the early full-screen question the brief asks for on the "
            "sentence that creates the pressure.",
            "One claim card.",
            [st("NEW_V10_FS_00_THE_PRESSURE", "Single state.",
                lambda c: L.claim_card(
                    c, "the hook", "THE PRESSURE",
                    "And now you feel this pressure to prove they made the "
                    "right decision.", dark=True, size=56))],
            "Cut on the sentence and return to camera quickly, so the "
            "pressure stays personal.",
            "One subtle click.", treatment="STATEMENT"),

            fam("NEW_V10_FS_00B_TWO_DEFAULTS", 10,
                "You start trying to fix things before you understand why "
                "they work this way.",
                "Show the two incomplete defaults as two defaults, one "
                "active at a time, rather than an instruction to stop "
                "contributing.",
                "Comparison with one side active at a time.",
                [st("NEW_V10_FS_00B_FIX_TOO_SOON",
                    "Activate the first default when it is spoken.",
                    lambda c: L.compare(
                        c, "the hook", "",
                        ("one direction", "Fix it too soon",
                         [("the move", "Trying to fix things before you "
                                       "understand why they work this "
                                       "way")]),
                        ("the other direction", "Stay too quiet",
                         [("the move", "Staying quiet because you are "
                                       "afraid of getting something "
                                       "wrong")]),
                        divider="", active="left",
                        foot="neither one is the job of your first 90 "
                             "days.")),
                 st("NEW_V10_FS_00C_STAY_TOO_QUIET",
                    "Activate the second default when it is spoken.",
                    lambda c: L.compare(
                        c, "the hook", "",
                        ("one direction", "Fix it too soon",
                         [("the move", "Trying to fix things before you "
                                       "understand why they work this "
                                       "way")]),
                        ("the other direction", "Stay too quiet",
                         [("the move", "Staying quiet because you are "
                                       "afraid of getting something "
                                       "wrong")]),
                        divider="", active="right",
                        foot="neither one is the job of your first 90 "
                             "days."))],
                "Reveal the first side with its sentence and the second "
                "with the next. Return to camera for the correction.",
                "No accent. The first card already carried one.",
                treatment="COMPARE")]

        # V11 | the two document cards the Riverside prompt asks for during
        # the second spoken sentence of the hook.
        out[11] = [fam(
            "NEW_V11_FS_00_ACCEPTED_AND_DOING", 11,
            "Then you started doing another.",
            "Realize the opening pair of documents, so the hook cutaway "
            "the brief specifies has a file and the takeaway callback has "
            "something to bring back.",
            "Two plain document cards, identical on the facts the script "
            "says are identical.",
            [st("NEW_V11_FS_00_ACCEPTED_AND_DOING", "Single state.",
                lambda c: L.compare(
                    c, "the hook", "",
                    ("the job I accepted", "One job",
                     [("title", "The same"), ("salary", "The same")]),
                    ("the job I started doing", "Another",
                     [("title", "The same"), ("salary", "The same")]),
                    divider="", foot="illustration. not an employer "
                                     "contract, offer or email."))],
            "Cut in during the second sentence and clear before 'But three "
            "or six weeks in.' Bring the same card back at TAKEAWAY VALUE.",
            "One small click on the difference.", treatment="COMPARE")]

    return out


def apply(SETS, L, batch):
    """Append the new early families and report what was added."""
    made = build(L, batch)
    added = []
    for n, fams in made.items():
        if n not in SETS:
            continue
        have = {f["key"] for f in SETS[n]}
        for f in fams:
            if f["key"] in have:
                continue
            SETS[n].insert(0, f)
            added.append((n, f["key"], [s["name"] for s in f["states"]]))
    return added
