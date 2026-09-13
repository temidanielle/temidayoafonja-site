# -*- coding: utf-8 -*-
"""Generate the story-led frame set from the pre-story-led one.

The visuals are not rebuilt because the scripts were reworded. Each existing
asset is carried across with its drawing unchanged and re-anchored to the
sentence the story-led script actually says, and every carry is labeled with
what the evidence supports:

  REUSE         the trigger sentence still exists word for word
  COPY UPDATE   the same sentence, reworded. The card is unchanged; its cue
                moved
  REBUILD       the moment survives but is materially rewritten
  NEW           written for this pass
  REMOVE        the moment is gone, or a graphic would interrupt a scene that
                should stay camera-led

Videos 4 and 5 were rewritten hardest and are mapped by hand in handmap_sl.
"""
import os, sys, textwrap
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                "VIDEOS_4-21_CORRECTED_RUNTIME/build")
sys.path.append("/home/user/temidayoafonja-site/deliverables/riverside-build")
import masters_sl as M
import trigaudit_sl as T
from frames421 import SETS as OLD
from handmap_sl import HAND, DROP, MODES

STATE_TO_STATUS = {"ALIVE": "REUSE", "RETRIGGER": "COPY UPDATE",
                   "MOMENT MOVED": "REBUILD"}

WHY = {
 "REUSE": ("The card is unchanged and its trigger sentence still exists word "
           "for word in the story-led script."),
 "COPY UPDATE": ("The card is unchanged. The story-led script rewords the "
                 "sentence it lands on, so only the cue moved."),
 "REBUILD": ("The teaching moment survives but the story-led script "
             "rewrites it materially, so the cue is re-anchored and the "
             "card copy checked against the new wording."),
}


def lit(text, indent):
    lines = textwrap.wrap(text, 70 - len(indent))
    out = []
    for i, l in enumerate(lines):
        q = l.replace("\\", "\\\\").replace('"', '\\"')
        out.append("%s\"%s%s\"" % ("" if i == 0 else indent, q,
                                   "" if i == len(lines) - 1 else " "))
    return "\n".join(out)


def build():
    rows = []
    for n in M.VIDEOS:
        audit = {r["key"]: r for r in T.audit(n)}
        seq = []
        for f in OLD[n]:
            key = f["key"]
            if key in DROP:
                continue
            if key in HAND:
                h = HAND[key]
                seq.append(dict(src=key, trigger=h["trigger"],
                                status=h["status"], why=h["why"],
                                mode=MODES.get(key, f.get("mode", "")),
                                old=f))
                continue
            a = audit[key]
            if a["state"] == "GONE":
                raise SystemExit("%s has no trigger and no hand mapping" % key)
            seq.append(dict(src=key, trigger=a["new_trigger"],
                            status=STATE_TO_STATUS[a["state"]],
                            why=WHY[STATE_TO_STATUS[a["state"]]],
                            mode=MODES.get(key, f.get("mode", "")),
                            old=f))
        rows.append((n, seq))
    return rows


if __name__ == "__main__":
    from collections import Counter
    rows = build()
    t = Counter()
    for n, seq in rows:
        t.update(s["status"] for s in seq)
        bad = [s for s in seq if not M.trigger_ok(n, s["trigger"])]
        print("V%-3d %2d frames  %s" % (n, len(seq),
              "all triggers verify" if not bad else
              "TRIGGER MISS: %s" % [b["src"] for b in bad]))
    print()
    print(dict(t), " dropped:", len(DROP))
