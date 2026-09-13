# -*- coding: utf-8 -*-
"""Write a card's elements as an editable SVG.

The PNG is what the editor drops on the timeline; the SVG is what a designer
opens when a line has to be re-timed or re-colored. Both come from the same
element list, and the text is wrapped with the same metrics the geometry
check measured, so the two files agree.
"""
import os, sys
sys.path.append("/home/user/temidayoafonja-site/deliverables/riverside-build")
from rdeck import W, H, hexc, wrap_lines, FONT_DIR

FALLBACK = {"Montserrat": "Montserrat, 'Helvetica Neue', Arial, sans-serif",
            "DM Sans": "'DM Sans', 'Helvetica Neue', Arial, sans-serif"}

# The four faces the cards actually use, embedded so the SVG renders the same
# on a machine that does not have the brand fonts installed and still opens as
# live, editable text.
EMBED = (("Montserrat", 400, "Montserrat-400-normal-latin-49e242.woff2"),
         ("Montserrat", 700, "Montserrat-700-normal-latin-49e242.woff2"),
         ("DM Sans", 400, "DMSans-400-normal-latin-1c49a6.woff2"),
         ("DM Sans", 700, "DMSans-600-normal-latin-1c49a6.woff2"))
_FACE_CSS = None


def face_css():
    global _FACE_CSS
    if _FACE_CSS is None:
        import base64
        out = []
        for fam, wt, fn in EMBED:
            with open(os.path.join(FONT_DIR, fn), "rb") as f:
                b64 = base64.b64encode(f.read()).decode("ascii")
            out.append("@font-face{font-family:'%s';font-weight:%d;"
                       "font-style:normal;src:url(data:font/woff2;base64,%s) "
                       "format('woff2');}" % (fam, wt, b64))
        _FACE_CSS = "\n".join(out)
    return _FACE_CSS


def _esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;"))


def _text(el):
    out = []
    y = el["y"]
    for sp in el["paras"]:
        size, sp_h = sp["size"], sp["size"] * sp["spacing"]
        lines = wrap_lines(sp["text"], el["w"], sp["font"], size, sp["bold"],
                           sp["tracking"])
        anchor = {"l": "start", "c": "middle", "r": "end"}[sp["align"]]
        ax = {"l": el["x"], "c": el["x"] + el["w"] / 2.0,
              "r": el["x"] + el["w"]}[sp["align"]]
        y += sp["space_before"]
        for line in lines:
            # SVG y is the baseline. The browser puts the baseline about
            # 0.8 of the font size below the top of the line box, after the
            # half-leading above it.
            base = y + (sp_h - size) / 2.0 + size * 0.8
            style = ["font-family:%s" % FALLBACK.get(sp["font"], sp["font"]),
                     "font-size:%gpx" % size,
                     "font-weight:%d" % (700 if sp["bold"] else 400),
                     "fill:%s" % hexc(sp["color"])]
            if sp["tracking"]:
                style.append("letter-spacing:%gpx" % sp["tracking"])
            if sp["italic"]:
                style.append("font-style:italic")
            if sp.get("strike"):
                style.append("text-decoration:line-through")
            out.append('<text x="%g" y="%g" text-anchor="%s" style="%s">%s'
                       "</text>" % (ax, base, anchor, ";".join(style),
                                    _esc(line)))
            y += sp_h
        y += sp["space_after"]
    return out


def _rect(el):
    attrs = ['x="%g"' % el["x"], 'y="%g"' % el["y"],
             'width="%g"' % el["w"], 'height="%g"' % el["h"]]
    if el["shape"] == "oval":
        return ('<ellipse cx="%g" cy="%g" rx="%g" ry="%g" fill="%s" %s/>'
                % (el["x"] + el["w"] / 2.0, el["y"] + el["h"] / 2.0,
                   el["w"] / 2.0, el["h"] / 2.0,
                   hexc(el["fill"]) if el["fill"] is not None else "none",
                   ('stroke="%s" stroke-width="%g"'
                    % (hexc(el["line"]), el["lw"]))
                   if el["line"] is not None else ""))
    fill = hexc(el["fill"]) if el["fill"] is not None else "none"
    stroke = (' stroke="%s" stroke-width="%g"' % (hexc(el["line"]), el["lw"])
              if el["line"] is not None else "")
    return "<rect %s fill=\"%s\"%s/>" % (" ".join(attrs), fill, stroke)


def write(card, path, title=""):
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
             'viewBox="0 0 %d %d">' % (W, H, W, H)]
    if title:
        parts.append("<title>%s</title>" % _esc(title))
    parts.append("<!-- Capability Formation. Editable source for %s. Text is "
                 "live and the brand faces are embedded. -->"
                 % os.path.basename(path))
    parts.append("<defs><style type=\"text/css\"><![CDATA[\n%s\n]]></style>"
                 "</defs>" % face_css())
    for el in card.els:
        if el["t"] == "rect":
            parts.append(_rect(el))
        else:
            parts.extend(_text(el))
    parts.append("</svg>")
    with open(path, "w") as f:
        f.write("\n".join(parts))
    return path
