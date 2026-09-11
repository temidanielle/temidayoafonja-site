# -*- coding: utf-8 -*-
"""06_Publishing materials, and the 07 viewer exercise.

Titles and thumbnail wording come from the locked masters and are never
restyled here. Nothing is invented: no URL, no chapter, no music credit, no
performance claim. Placeholders are marked.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import masters421 as M
import wncheck421 as WN
from docs421f import (base_doc, para, title_block, rule, h, kv, callout,
                       table, bullets, sub, field, page_break, footer_note,
                       numbered, mono, hr, head, NAVY, GOLD, DIM, RED)

from content421 import ROUTES, PLAYLIST, DESC, PINNED, TAGS, HASH as HASHTAGS


def thumb_brief(n):
    return [
      "Headline text, exactly as locked: %s" % M.thumbnail(n),
      "Set the headline flush left in short stacked lines, Montserrat "
      "ExtraBold, cap height 240 to 300 px on a 3840 by 2160 master.",
      "Deep navy #112345 field. Warm cream and white for the headline. Bright "
      "warm yellow as selective emphasis only, well under about 4 percent of "
      "the canvas.",
      "Large real portrait of Temidayo on the right, about 44 to 47 percent "
      "of the canvas. Natural skin tone. Use an approved real photograph.",
      "Do NOT generate, reconstruct, beautify or alter the face. Permitted on "
      "the source photograph: crop, mask, restrained exposure adjustment, "
      "color balance, background removal.",
      "No clutter, no tiny text, no fake icons, no AI-looking people, no "
      "numbers and no implied statistic.",
      "Keep the portrait layer and the text layer editable and separate.",
      "Must be legible at 200 px wide, which is the recommendation-column "
      "size.",
      "Export a 3840 by 2160 PNG master and a 1280 by 720 JPG for upload, "
      "quality 95, under 2 MB.",
      "Artwork is approved separately. This brief does not authorize a "
      "finished thumbnail.",
    ]


def primary_cta(n):
    """The one primary action, as the CTA card states it.

    Only Video 14's master carries a CTA metadata row. For the rest the ask
    lives in the speech, and the CTA card is the copy built from it, so the
    card is read rather than the row invented.
    """
    from frames421 import SETS
    import rdeck
    for i, f in enumerate(SETS[n], 1):
        if f["key"].endswith("_cta"):
            c = rdeck.Card(i, f["key"] + ".png")
            f["draw"](c)
            lines = [pa["text"] for el in c.els if el.get("t") == "text"
                     for pa in el["paras"] if pa.get("text")]
            res = route(n)
            drop = {res} | ({"temidayoafonja.com"} if res else set())
            body = [x for x in lines
                    if "temidayoafonja.com" not in x and x != res]
            # lines[0] is the eyebrow label, which is a card device, not copy.
            return " ".join(body[1:]).strip(), f["trigger"]
    return M.cta(n), ""


def watch_next(n):
    """The Watch Next destination, as a destination number and a title.

    V6 to V14 name it in a metadata row. V4, V5 and V15 to V21 do not, and
    their masters require a Watch Next card without naming its destination.
    For those, the destination is the one built into the production deck, and
    wncheck421 has already verified that the card carries the destination
    master's exact title. Reading it from the same place keeps the
    description and the final frame from ever disagreeing.
    """
    for src, dest, shown in WN.cards():
        if src == n:
            return dest, shown, ("the master's Watch Next row"
                                 if M.watch_next(n) else
                                 "the Watch Next card in the production deck")
    return None, "", "not set"


SPOKEN_NAME = {
 "Capability Formation Field Kit": ("field kit",),
 "Field Kit": ("field kit",),
 "Keep the Proof": ("keep the proof",),
 "Career Decision Evidence Check": ("career decision evidence check",
                                    "decision evidence check"),
 "Career Evidence Starter": ("career evidence starter",),
}


def route(n):
    """The video's resource route, or "" when it has none.

    Two shapes of master exist. V6 to V13 carry a Resource route row, and
    where the route is not spoken the row appends a note in parentheses
    saying so. That note is instruction, not part of the name.

    V15 to V21 carry no such row. Their route is named in the speech instead,
    so the script is read for it. Nothing is inferred: a route is returned
    only when the script says its name, and only when it says exactly one.
    """
    r = M.resource(n)
    if r:
        return r.split("(")[0].strip()
    script = M.spoken_text(n).lower()
    hits = sorted({name for name, keys in SPOKEN_NAME.items()
                   if any(k in script for k in keys)},
                  key=len, reverse=True)
    if not hits:
        return ""
    # "Field Kit" and "Capability Formation Field Kit" are the same route.
    urls = {ROUTES[h] for h in hits}
    if len(urls) > 1:
        raise SystemExit("V%d speaks more than one resource route: %s"
                         % (n, hits))
    return hits[0]


def spoken_route(n):
    """True when the corrected script actually says the resource out loud."""
    r = route(n)
    if not r:
        return False
    script = M.spoken_text(n).lower()
    return any(x in script for x in SPOKEN_NAME.get(r, (r.lower(),)))


def build(n, out_path, stamp):
    res = route(n)
    d = base_doc()
    footer_note(d, "Video %d publishing materials  |  copy taken from the "
                   "locked final master" % n)
    title_block(d, "Capability Formation  |  Video %d" % n,
                "Publishing Materials", M.title(n))
    kv(d, "Generated", stamp)
    kv(d, "Source", "%s  ·  SHA-256 %s" % (M.FILES[n], M.read(n)["sha"]))

    callout(d, "The title and the thumbnail wording are taken from the locked "
               "master and are not restyled here. No URL, chapter timestamp, "
               "music credit or performance claim is invented anywhere in "
               "this document.")

    h(d, "YouTube title")
    para(d, M.title(n), size=13, bold=True, color=NAVY)

    h(d, "Thumbnail text")
    para(d, M.thumbnail(n), size=13, bold=True, color=NAVY)

    h(d, "Description")
    for block_ in DESC[n].split("\n\n"):
        para(d, block_)
    para(d, "RESOURCE LINE, paste as the last block:", size=9, bold=True,
         color=GOLD, before=10, after=4)
    if res:
        para(d, "%s: https://%s" % (res, ROUTES[res]), size=11, bold=True)
    else:
        para(d, "This video names no resource. Do not add one.", size=11,
             bold=True, color=RED)
    wn_num, wn_title, wn_src = watch_next(n)
    para(d, "WATCH NEXT LINE: Video %s: %s" % (wn_num, wn_title), size=10,
         color=DIM)
    para(d, "[PLACEHOLDER] Insert the Watch Next video URL after that video "
            "is published. Do not invent a URL.", size=10, color=RED)

    h(d, "Pinned comment")
    for block_ in PINNED[n].split("\n\n"):
        para(d, block_)
    if res and not spoken_route(n):
        para(d, "ROUTE LINE, paste as the last block of the pinned comment:",
             size=9, bold=True, color=GOLD, before=10, after=4)
        para(d, "%s: https://%s" % (res, ROUTES[res]), size=11, bold=True)
        para(d, "This master routes the resource to the description and the "
                "pinned comment and states it is not a second spoken CTA, so "
                "it is written here and is not on any card.", size=9,
             color=DIM)

    h(d, "Tags")
    para(d, ", ".join(TAGS[n]))

    h(d, "Hashtags")
    para(d, "  ".join(HASHTAGS[n]), size=12, bold=True)

    h(d, "Resource route")
    if res:
        table(d, ["Resource", "Where it lives", "How it is used"],
              [[res, ROUTES[res],
                "Named once in the script, after the teaching. One primary "
                "CTA. No second offer is added."]],
              widths=[1.9, 2.1, 2.7], size=9)
    else:
        para(d, "None. This master names no resource route, so none appears "
                "in the script, the description, the pinned comment or on any "
                "card.", color=RED, bold=True)

    h(d, "Watch Next and playlist")
    table(d, ["Field", "Value"], [
      ["Watch Next", "Video %s: %s" % (wn_num, wn_title)],
      ["Where that comes from", wn_src],
      ["Playlist", PLAYLIST],
      ["End screen", "Watch Next is the final full-screen visual. The card "
                     "keeps its copy on the left so a YouTube end screen can "
                     "sit on the right. No return to camera afterward."],
    ], widths=[1.35, 5.35], size=9)

    h(d, "Canva thumbnail brief")
    bullets(d, thumb_brief(n))

    h(d, "Publication and link checklist")
    numbered(d, [
      "Thumbnail artwork approved separately, and checked at 200 px wide.",
      "Title and thumbnail wording match the locked master exactly.",
      "Description resource link tested while signed out." if res else
      "No resource link appears anywhere, because the master names none.",
      "Watch Next URL inserted once that video is published. Not before.",
      "Captions: no burned-in subtitles on the export. SRT uploaded, "
      "generated from the final edited timeline.",
      "Chapters written from the actual final export. None exist yet.",
      "Music attribution completed from the actual track used. None is "
      "recorded here.",
      "End screen configured so it does not cover the Watch Next copy.",
    ])
    d.save(out_path)
    return out_path
