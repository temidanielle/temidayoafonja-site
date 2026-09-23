# -*- coding: utf-8 -*-
"""Editor cue map for V1, V2 and V3, synchronized to the newest spoken masters.

Every cue is anchored to an exact sentence, or an exact consecutive run of
sentences, from the video's FINAL Sticky Realization recording master. Nothing
is anchored to a paraphrase, so anchors_ok() below is a real check and not a
formality.

Guide ranges from the refresh brief: 3 to 5 camera-emphasis beats, 2 to 4
artifact or B-roll moments, 4 to 7 restrained sound accents, one quiet
Subscribe cue placed after value has been delivered.
"""
import st_parse as P
import st_frames as F

# (anchor sentence or run, direction)
CAMERA = {
1: [("So the question is not only, “Can I change careers?” It is: “What from everything I have built actually comes with me?”",
     "Camera, close. The two questions are the promise of the video. Let the second one land before the cut."),
    ("Matching words are not enough.",
     "Come off the comparison to camera for one line. This is the re-hook and it is the sentence the card repeats."),
    ("A higher title does not just mean more of the same work.",
     "Camera, level, after a beat of silence. The distinction the whole middle of the video is built on."),
    ("If you have not worked in those contexts, better resume language does not create experience you have not had.",
     "Camera, blunt, no softening afterwards. This is the line that keeps the video honest."),
    ("You can be experienced and new at the same time.",
     "Camera, close, warm. Hold. The emotional payoff of the episode.")],
2: [("You can be doing very well at work and quietly becoming harder to hire somewhere else.",
     "Camera, close. The title sentence, said once, plainly, in the first thirty seconds."),
    ("Those things are valuable. But they do not all leave with you.",
     "Camera. The realization. Do not decorate it."),
    ("Now I can hear the judgment.",
     "Come off the artifact to camera on this line. The turn from reading to hearing."),
    ("Speed matters. Efficiency matters. But proficiency is not always the same as expansion.",
     "Camera. The correction most viewers need, delivered without a lecture."),
    ("The question is: if this context disappeared, could another person see and use what I know how to do?",
     "Camera, close. Hold through the last two sentences.")],
3: [("Your experience did not disappear. But some of your ability to reconstruct it did.",
     "Camera, quiet, no card. The whole cold open is one person talking."),
    ("One important boundary first. If your health or safety is at risk, or you are dealing with harassment, discrimination or another urgent threat, this is not a reason to delay leaving. Act on that first.",
     "Camera, direct, unhurried. No card, no music. This is the most important forty seconds in the video for tone."),
    ("That is why I say: keep the proof, not the property.",
     "Camera, close. The memory line, said for the first time."),
    ("Keep the claim narrow.",
     "Camera. Short, firm, then a half-second of nothing."),
    ("Future-you should not have to rebuild the whole story from memory.",
     "Camera, warm. Hold into the close.")],
}

BROLL = {
1: [("Role one is Senior Manager, Program Management. Role two is Director, Enterprise Transformation.",
     "V1_01_THE_MOVE. Both roles on screen before any conclusion. The source line stays up for the whole hold."),
    ("Complex programs. Governance. Risk and dependencies. Budgets. Executive communication. Cross-functional influence.",
     "V1_02A through V1_02D. Build the repeating language one side at a time, mark the overlap, then bring in the banner."),
    ("What travels? Cross-functional influence, program governance, risk and dependency management, executive communication, complex delivery.",
     "V1_07A through V1_07D. One column per question, in the spoken order. V1_07D_COMPLETE is the frame people photograph.")],
2: [("“I own the QBR process for this business unit.”",
     "V2_02_THE_SENTENCE. Hold long enough to be read twice. The constructed-example label stays on the card."),
    ("Maybe the real work is: “I combine incomplete operating data, surface the decision leaders are avoiding, and create a shared view of what needs to happen next.”",
     "V2_04_UNDERNEATH. Same card shape as the sentence before it, so the swap is the whole argument."),
    ("If your judgment is growing and it remains useful across contexts, your work may be expanding your options.",
     "V2_07A through V2_07D. Build one situation at a time. Four reads, no score, nothing added up.")],
3: [("You can check when something happened. You can confirm your responsibility. You may be able to look at your own permitted review or recognition history. You can remember who was involved and why the decision mattered.",
     "V3_02A through V3_02C. Build as each is named, then hold on the line about the project name and the judgment."),
    ("Confidential information, customer or employee data, proprietary documents and employer-owned material stay with the employer.",
     "V3_03B_STAYS_WITH_EMPLOYER. Held, not flashed. This card should feel more deliberate than anything else in the video."),
    ("What was true before?",
     "V3_05A through V3_05D. One line at a time. The four-line card is the frame people pause and photograph."),
    ("Maybe the real work was that you found where the process kept getting stuck, brought together people who owned different parts of it, redesigned the handoff, and made the change without creating another control problem.",
     "V3_06 then V3_07. The thin version, then the same example rebuilt in the same card shape.")],
}

SOUND = {
1: [("You have something to lose.", "Hard stop. Cut everything under these five words."),
    ("Your experience does not move as one big block.", "One low accent under the whole sentence. Nothing else in the episode gets this."),
    ("Matching words are not enough.", "Silence under it."),
    ("That is a much more useful answer than “your skills transfer.”", "Bed lifts slightly as the fourth column completes."),
    ("My experience does not move as one block.", "The memory line. One accent, low, and let it ring."),
    ("You can be experienced and new at the same time.", "Resolve and hold under the close.")],
2: [("But here is the uncomfortable question: how much of that value still makes sense when the company name disappears?",
     "Cold open accent on the question."),
    ("Those things are valuable. But they do not all leave with you.", "One low accent under the realization."),
    ("Now I can hear the judgment.", "Small lift. The only place the music moves in the middle of the video."),
    ("Not because one bad quarter means leave. Because patterns matter.", "Accent on the last clause."),
    ("What part of this is me, and what part is my access to this environment?", "The memory question. One accent, low."),
    ("That is a harder question. It is also a much more useful one.", "Resolve and hold.")],
3: [("And the system where all of that lived? You cannot get into it anymore.", "Cold open accent, very low. This episode should sound quieter than the other two."),
    ("Your evidence has an access problem.", "One accent under the realization."),
    ("The project name stays. The judgment disappears.", "Hard stop. Cut everything for the pause."),
    ("So here is the rule: keep the proof, not the property.", "Silence under the rule. Nothing competes with it."),
    ("Keep the proof, not the property.", "The memory line, second time. One accent, low."),
    ("That is a much stronger place to leave from than, “I know I did a lot there.”", "Resolve and hold into the CTA.")],
}

# One quiet Subscribe cue per video, placed after value has been delivered and
# never on top of a boundary, a payoff or the CTA.
SUBSCRIBE = {
1: ("That is a much more useful answer than “your skills transfer.”",
    "Small lower-third, four seconds, no sound, no voiceover. It sits after the "
    "four-column read has paid off and before the boundary, so it never lands "
    "on top of a limitation."),
2: ("You are looking for evidence that the usefulness was not completely trapped inside one environment.",
    "Small lower-third, four seconds, no sound. After the outside-context test "
    "has given the viewer something usable and before the 90-day section."),
3: ("You need enough context that future-you can reconstruct the story accurately.",
    "Small lower-third, four seconds, no sound. After the four-line record has "
    "been taught and well clear of the safety and property boundaries."),
}

CTA_CARD = {1: "V1_10_CTA", 2: "V2_11_CTA", 3: "V3_12_CTA"}
WATCH_CARD = {1: "V1_11_WATCH_NEXT", 2: "V2_12_WATCH_NEXT", 3: "V3_13_WATCH_NEXT"}

def anchors_ok():
    bad = []
    for n in (1, 2, 3):
        ms = P.master_sentences(n)
        joined = " ".join(ms)
        groups = [(CAMERA[n], "camera"), (BROLL[n], "artifact"),
                  (SOUND[n], "sound"), ([SUBSCRIBE[n]], "subscribe")]
        for group, label in groups:
            for trig, _why in group:
                if trig not in ms and trig not in joined:
                    bad.append((n, label, trig[:70]))
    return bad

def _resolve(ref, names, fams):
    """A cue direction may name a card by a unique prefix.

    Directions describe a build as a range, "V1_02A through V1_02D", which is
    what an editor scrubbing the asset folder actually types. The first version
    of this check demanded the full card name and reported all twelve of those
    as missing cards, which was a checker-scope error rather than a broken
    reference. A prefix resolves only when it matches exactly one card, so an
    ambiguous or invented reference is still caught.
    """
    if ref in names or ref in fams:
        return True
    hits = [x for x in names if x.startswith(ref)]
    return len(hits) == 1

def cards_ok():
    """Every card named in a cue direction has to resolve to exactly one card."""
    import re
    bad = []
    for n in (1, 2, 3):
        names = {name for _f, name, _d, _no in F.states(n)}
        fams = {fam for fam, _n, _d, _no in F.states(n)}
        for _trig, why in BROLL[n]:
            for m in re.findall(r"V[123]_[0-9A-Z_]+", why):
                if not _resolve(m, names, fams):
                    bad.append((n, m))
        for m in (CTA_CARD[n], WATCH_CARD[n]):
            if m not in names:
                bad.append((n, m))
    return bad

def cards_regression():
    """A reference to a card that does not exist must still be rejected, and an
    ambiguous prefix must not silently pass."""
    names = {"V1_02A_ROLE_A", "V1_02B_ROLE_B", "V1_07D_COMPLETE"}
    return (_resolve("V1_02A", names, set())
            and not _resolve("V1_99_NOT_A_CARD", names, set())
            and not _resolve("V1_02", names, set()))

if __name__ == "__main__":
    for n in (1, 2, 3):
        print("V%d  %d camera  %d artifact  %d sound  1 subscribe"
              % (n, len(CAMERA[n]), len(BROLL[n]), len(SOUND[n])))
        assert 3 <= len(CAMERA[n]) <= 5, "camera out of guide range"
        assert 2 <= len(BROLL[n]) <= 4, "artifact out of guide range"
        assert 4 <= len(SOUND[n]) <= 7, "sound out of guide range"
    bad = anchors_ok()
    print("unanchored cues:", len(bad))
    for b in bad:
        print("   ", b)
    cb = cards_ok()
    print("cue directions naming a card that does not resolve:", len(cb), cb)
    print("card check still rejects a bad name and an ambiguous prefix:",
          cards_regression())
