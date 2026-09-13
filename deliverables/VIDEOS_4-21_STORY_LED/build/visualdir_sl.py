# -*- coding: utf-8 -*-
"""The story-led visual direction, and which treatment each card takes.

The treatment is not assigned by taste. It is read from the layout each card
already uses, because that is what the card structurally is: a two-sided
comparison is a comparison, a numbered ladder is a sequence, a single
statement is a statement. That keeps the direction honest and keeps it from
forcing one template over eighteen videos.

The five treatments, adapted to the channel rather than copied from any
product:

  COMPARISON        two large sides, one revealed then the other
  SEQUENCE          the whole structure established, then one component
                    activated at a time, then the whole again
  ARTIFACT          a large artifact with a short explainer panel, walked
                    through with numbered markers revealed one at a time
  STATEMENT         one idea, held still long enough to land
  CTA / WATCH NEXT  simpler than teaching graphics, by design

Palette, stated once so every prompt can refer to it:
  deep navy #112345 carries authority and is the usual ground
  warm cream is breathing room and the light ground where legibility needs it
  muted gold marks the ACTIVE idea only: the selected item, the number, the
  underline, the key distinction. Never decoration.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                "VIDEOS_4-21_CORRECTED_RUNTIME/build")
import masters_sl as M
from frames_sl import SETS

NAVY, CREAM, GOLD = "#112345", "warm cream", "muted gold"

SRC = [
  "/home/user/temidayoafonja-site/deliverables/VIDEOS_4-21_CORRECTED_RUNTIME/"
  "build/frames421.py",
  "/home/user/temidayoafonja-site/deliverables/VIDEOS_14-21_FINAL_PRODUCTION/"
  "build/frames1421.py",
]

LAYOUT_TREATMENT = {
  "duo": "COMPARISON", "word_vs_work": "COMPARISON",
  "struck": "COMPARISON", "shared_then_split": "COMPARISON",
  "two_questions": "COMPARISON",
  "trio": "SEQUENCE", "quad": "SEQUENCE", "numbered": "SEQUENCE",
  "ladder": "SEQUENCE", "four_bucket": "SEQUENCE",
  "labeled_rows": "SEQUENCE", "three_lines": "SEQUENCE",
  "readings": "ARTIFACT", "statfacts": "ARTIFACT",
  "statement": "STATEMENT",
  "cta": "CTA", "cta_action": "CTA",
  "watch_next": "WATCH NEXT",
}

_layout = None


def layouts():
    """{frame key: layout function name}, read from the frame sources."""
    global _layout
    if _layout is not None:
        return _layout
    out = {}
    pat = re.compile(r'F\(key="([^"]+)",\s*draw=lambda c: X\.(\w+)\(')
    for p in SRC:
        if not os.path.exists(p):
            continue
        for m in pat.finditer(open(p, encoding="utf-8").read()):
            out.setdefault(m.group(1), m.group(2))
    _layout = out
    return out


def treatment(key):
    lay = layouts().get(key)
    return LAYOUT_TREATMENT.get(lay, "STATEMENT"), lay


# How each treatment is directed on screen. Written for an editor or for
# Co-Creator to follow without guessing.
DIRECTION = {
 "COMPARISON": [
   "Two large sides, full screen. Short label on each side, then the short "
   "content under it.",
   "Reveal the left side first and let it sit. Reveal the right side only "
   "when Temidayo reaches it. Do not present both at once.",
   "Gold marks the distinction that matters, on one side only. Everything "
   "else stays navy on cream or cream on navy.",
   "No camera behind the graphic. This is a true full-screen frame.",
 ],
 "SEQUENCE": [
   "Establish the complete structure first, all items visible but even in "
   "weight, so the viewer sees the shape.",
   "Then activate ONE item at a time as Temidayo explains it: that item "
   "comes up in gold, the others sit back in a dimmer neutral. Do not "
   "emphasize all of them at once.",
   "Return to the complete structure, evenly weighted, only after the last "
   "item.",
   "One sound accent at most across the whole sequence, not one per item.",
 ],
 "ARTIFACT": [
   "The artifact is the frame. Give it roughly two thirds of the screen at "
   "a size that reads on a phone, with a short explainer panel beside it.",
   "Place numbered markers on the artifact, all visible but subdued to "
   "begin with, so the viewer can see how many there are.",
   "Then walk them: highlight marker one in gold, neutralize the rest, and "
   "show only that marker's line in the panel. Advance as Temidayo reaches "
   "each one.",
   "Never show every explanatory line at once. The panel holds one idea.",
   "If the real artifact is too dense to read on a phone, simplify the "
   "artifact. Do not shrink the type.",
 ],
 "STATEMENT": [
   "One idea, full screen, large. Headline first, then the support line if "
   "there is one.",
   "Hold it still. Stillness is correct here: the viewer is reading or "
   "thinking.",
   "No motion beyond the entrance. No sound unless this is one of the few "
   "beats that earns it.",
 ],
 "CTA": [
   "Full screen, and simpler than the teaching graphics. The action is the "
   "only thing competing for attention.",
   "Resource name and route appear only where the script speaks them.",
 ],
 "WATCH NEXT": [
   "Full screen and final. Label, rule, destination title, video number.",
   "Keep the copy to the left so an end screen can sit on the right.",
   "Never return to camera after this frame. Nothing follows it.",
 ],
}

STANDING = [
 "Camera-led teaching governs. Recognition, personal story, tension and the "
 "moments that bring an idea back to the viewer stay on Temidayo.",
 "A graphic earns the screen when seeing the idea is easier than hearing it "
 "alone. It is not a decoration for a spoken point.",
 "Substantive teaching is TRUE full screen. Never a moving Temidayo behind "
 "or beside a framework. Never the teaching graphic shrunk into a corner.",
 "Editorial, not corporate training. Generous whitespace, strong hierarchy, "
 "clean cards, short labels, obvious reading order. No fake interactivity, "
 "no progress bars, no decorative icons, no quiz styling.",
 "Mobile legibility is not negotiable. Large type, few words, high "
 "contrast, generous margins. Simplify the graphic rather than shrink the "
 "type.",
 "Restraint holds: about 3 to 5 camera-emphasis beats, about 2 to 4 "
 "meaningful B-roll moments, about 4 to 7 restrained sound accents for the "
 "whole video. A framework sequence is one visual event, not one event per "
 "frame.",
 "A graphic may clarify, organize, compare, visualize, sequence or "
 "reinforce. It may never introduce a framework, a claim, a figure or a "
 "lesson the September 13 script does not already teach.",
]


def counts():
    from collections import Counter
    return Counter(treatment(f["key"])[0]
                   for n in M.VIDEOS for f in SETS[n])


if __name__ == "__main__":
    print(dict(counts()))
    missing = [f["key"] for n in M.VIDEOS for f in SETS[n]
               if f["key"] not in layouts()]
    print("frames whose layout could not be read:", missing or "none")
