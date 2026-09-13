# -*- coding: utf-8 -*-
"""Publishing copy, audited against the story-led scripts.

Descriptions and pinned comments are updated only where the story-led script
materially changed the hook framing, the viewer problem, the CTA wording, the
Watch Next wording or the resource language. Metadata is not rewritten for
the sake of change, so most of the locked copy stands unaltered.

Titles come from the story-led script header. Where a header differs from the
previously locked package, the header wins.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                "VIDEOS_4-21_CORRECTED_RUNTIME/build")
import masters_sl as M
import packaging_sl as PK
from content421 import (ROUTES, PLAYLIST, DESC as _D, PINNED as _P,
                        TAGS, HASH, PSO, EX)

DESC = dict(_D)
PINNED = dict(_P)

# --------------------------------------------------------------- updates
# Video 5. The story-led script replaced the "read like a beginner" opening
# with the car analogy, so the description's first paragraph described a
# hook the video no longer has. The framework and the boundary are unchanged
# and are left exactly as locked.
DESC[5] = (
  "Changing career tracks does not automatically mean starting over. But it "
  "also does not mean everything from your old work comes with you.\n\n"
  "Think of it like taking the same car onto a different road. Some parts "
  "still work. Some need adjusting for the new road. Some may need "
  "replacing. And before you keep driving, you need to know what is "
  "actually working.\n\n"
  "This video separates four things: what you can carry, what you have to "
  "translate, what you genuinely need to relearn, and what you can prove.\n\n"
  "You will leave with a four-line move case for one move you are "
  "considering.\n\n"
  "It is honest in both directions. You do not have to erase your past, and "
  "you do not have to pretend your past gives you everything.")

PINNED[5] = (
  "Four lines for one move you are considering.\n"
  "Carry: what from your old work still matters here.\n"
  "Translate: how you would explain it in language this field understands.\n"
  "Relearn: what you honestly need to learn or rebuild.\n"
  "Prove: the evidence that shows you can work at the level you are asking "
  "for.\n\n"
  "You do not have to erase your past. You also do not have to pretend it "
  "gives you everything.")

# Video 15. The script now states the boundary as "this is not a diagnostic,
# there is no score, no level, no type". The pinned comment called it a
# reflection tool, which is no longer the script's own wording.
PINNED[15] = (
  "Name one gap and the step that matches it.\n"
  "LEARN, PRACTICE or PROVE. One word, one sentence.\n\n"
  "This is not a diagnostic. There is no score at the end of it, no level "
  "and no type. Some of these gaps are shaped by the organization rather "
  "than by you.")

CHANGED = {5: "description and pinned comment", 15: "pinned comment"}

# Thumbnail wording of record comes from the locked V4 to V21 roadmap, not
# from the story-led script header. Nothing changed: THUMB_CHANGED is empty
# and the two divergences are carried as metadata exceptions instead.
THUMB_CHANGED = {}

SPOKEN_NAME = {
 "Capability Formation Field Kit": ("field kit",),
 "Field Kit": ("field kit",),
 "Keep the Proof": ("keep the proof",),
 "Career Decision Evidence Check": ("career decision evidence check",
                                    "decision evidence check"),
 "Career Evidence Starter": ("career evidence starter",),
}


def route(n):
    """The resource this video speaks, or "" when it names none."""
    script = M.spoken_text(n).lower()
    hits = sorted({name for name, keys in SPOKEN_NAME.items()
                   if any(k in script for k in keys)}, key=len, reverse=True)
    if not hits:
        return ""
    if len({ROUTES[h] for h in hits}) > 1:
        raise SystemExit("V%d speaks more than one route: %s" % (n, hits))
    return hits[0]


def watch_next(n):
    """(destination number, title, where it came from)."""
    m = re.search(r'Watch\s+[“"]([^”"]+)[”"]\s+next', M.spoken_text(n))
    if m:
        for k in M.VIDEOS:
            if M.title(k) == m.group(1):
                return k, M.title(k), "spoken in the story-led script"
    import wncheck_sl
    return wncheck_sl.destination(n)


def audit(n):
    """What changed in this video's publishing copy, and what did not."""
    return dict(
        title=M.title(n), title_changed=False,
        thumbnail=PK.thumbnail(n),
        thumbnail_changed=n in THUMB_CHANGED,
        thumbnail_was=THUMB_CHANGED.get(n),
        thumbnail_source="locked V4 to V21 roadmap",
        script_header_thumbnail=PK.script_header_thumbnail(n),
        thumbnail_metadata_exception=PK.is_exception(n),
        copy_changed=CHANGED.get(n),
        route=route(n))
