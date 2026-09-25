# -*- coding: utf-8 -*-
"""The Word deliverables: script, Riverside sheet, editor notes, upload sheet,
Shorts cut sheet."""
import os, sys
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pl_data as D, pl_slides as SL

NAVY_RGB = RGBColor(0x0F, 0x23, 0x47)
GOLD_RGB = RGBColor(0xA8, 0x88, 0x30)   # gold darkened for paper legibility
GREY_RGB = RGBColor(0x55, 0x5F, 0x6D)

def doc(margin=0.85):
    d = Document()
    st = d.styles["Normal"]
    st.font.name = "DM Sans"
    st.font.size = Pt(10.5)
    st.paragraph_format.space_after = Pt(6)
    st.paragraph_format.line_spacing = 1.18
    for s in d.sections:
        s.top_margin = s.bottom_margin = Inches(margin)
        s.left_margin = s.right_margin = Inches(margin)
    return d

def _p(d, text="", size=10.5, bold=False, color=None, before=0, after=6,
       italic=False, align=None, indent=0):
    p = d.add_paragraph()
    p.paragraph_format.space_before = Pt(before)
    p.paragraph_format.space_after = Pt(after)
    if indent:
        p.paragraph_format.left_indent = Inches(indent)
    if align:
        p.alignment = align
    r = p.add_run(text)
    r.font.size = Pt(size)
    r.bold = bold
    r.italic = italic
    if color is not None:
        r.font.color.rgb = color
    return p

def title(d, eyebrow, head, sub=None):
    _p(d, eyebrow.upper(), 8.5, True, GOLD_RGB, 0, 3)
    _p(d, head, 20, True, NAVY_RGB, 0, 2)
    if sub:
        _p(d, sub, 11, False, GREY_RGB, 0, 10)

def h(d, text, before=14):
    _p(d, text.upper(), 11.5, True, NAVY_RGB, before, 5)

def kv(d, k, v):
    p = d.add_paragraph()
    p.paragraph_format.space_after = Pt(3)
    r = p.add_run(k + "  ")
    r.bold = True; r.font.size = Pt(10); r.font.color.rgb = NAVY_RGB
    r2 = p.add_run(v); r2.font.size = Pt(10)

def bullet(d, text, indent=0.18):
    p = d.add_paragraph()
    p.paragraph_format.left_indent = Inches(indent + 0.18)
    p.paragraph_format.first_line_indent = Inches(-0.18)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run("·   " + text); r.font.size = Pt(10.5)
    return p

def table(d, headers, rows, widths):
    t = d.add_table(rows=1, cols=len(headers))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.LEFT
    for i, htxt in enumerate(headers):
        c = t.rows[0].cells[i]
        c.text = ""
        r = c.paragraphs[0].add_run(htxt.upper())
        r.bold = True; r.font.size = Pt(8.5); r.font.color.rgb = NAVY_RGB
    for row in rows:
        cells = t.add_row().cells
        for i, val in enumerate(row):
            cells[i].text = ""
            for j, line in enumerate(str(val).split("\n")):
                p = cells[i].paragraphs[0] if j == 0 else cells[i].add_paragraph()
                p.paragraph_format.space_after = Pt(2)
                p.add_run(line).font.size = Pt(9)
    for row in t.rows:
        for i, w in enumerate(widths):
            row.cells[i].width = Inches(w)
    return t

FOOT = ("Built from the September 24, 2026 playlist document and production "
        "brief. Nothing here was invented: every story, name and figure comes "
        "from those two files.")

def footer(d, extra=None):
    _p(d, "", 6, after=2)
    _p(d, extra or FOOT, 8, False, GREY_RGB, 10, 0, italic=True)

# ===================================================================== 1
def script_doc(v, path):
    d = doc()
    title(d, "%s · video %d of 3" % (D.PLAYLIST_TITLE, v["n"]),
          v["title"],
          "%s  ·  %s  ·  Publishes %s"
          % (v["length"], v["alt_title"], v["publish"]))

    _p(d, "HOW TO USE THIS SCRIPT", 9, True, GOLD_RGB, 12, 4)
    bullet(d, "The hook, the roadmap and the close are word for word. Those "
              "three go on the teleprompter and nowhere else.")
    bullet(d, "Everything between them is talking points. Say them in your "
              "own words. The order matters, the phrasing does not.")
    bullet(d, "SAY THIS lines are the caption cards. Say them close to "
              "verbatim so the burned-in text matches your mouth.")
    bullet(d, "STORY marks a story from your own history. Only the stories in "
              "this script are approved for use.")
    bullet(d, "[ON SCREEN] marks where a slide or caption card appears. The "
              "editor has the same cues with timings.")

    slides = {s["at"]: s for s in SL.SLIDES[v["n"]]}

    h(d, "hook · 0:00 · say word for word")
    s1 = SL.SLIDES[v["n"]][0]
    _p(d, "[ON SCREEN] Slide 1, %s: %s" % (s1["label"], s1["when"]),
       9, True, GOLD_RGB, 0, 5)
    for line in v["hook"]:
        _p(d, line, 12, False, None, 0, 8)

    h(d, "roadmap · say word for word, right after the hook")
    s2 = SL.SLIDES[v["n"]][1]
    _p(d, "[ON SCREEN] Slide 2, %s: %s" % (s2["label"], s2["when"]),
       9, True, GOLD_RGB, 0, 5)
    for line in v["roadmap"]:
        _p(d, line, 12, False, None, 0, 8)
    _p(d, "These lines and the chapter titles name the same steps in the "
          "same order. If you change one, change the other.",
       9, False, GREY_RGB, 2, 6, italic=True)

    for at, head, beats in v["middle"]:
        kinds = {k for k, _t in beats}
        # A section whose beats are all on-screen copy is read, not talked
        # through. Labelling Video 2's script section "talking points"
        # contradicted its own heading.
        mode = ("on screen, then read" if kinds <= {"screen"}
                else "talking points")
        hl = head.lower()
        h(d, "%s · %s" % (at, hl) if mode in hl
          else "%s · %s · %s" % (at, hl, mode))
        if at in slides and slides[at]["no"] > 2:
            s = slides[at]
            _p(d, "[ON SCREEN] Slide %d, %s, at %s"
               % (s["no"], s["label"], s["when"]), 9, True, GOLD_RGB, 0, 5)
        for kind, text in beats:
            if kind == "point":
                bullet(d, text)
            elif kind == "screen":
                _p(d, "[ON SCREEN] " + text, 10, False, GOLD_RGB, 2, 5)
            elif kind == "say":
                p = d.add_paragraph()
                p.paragraph_format.left_indent = Inches(0.22)
                p.paragraph_format.space_before = Pt(4)
                p.paragraph_format.space_after = Pt(6)
                r = p.add_run("SAY THIS   "); r.bold = True
                r.font.size = Pt(9); r.font.color.rgb = GOLD_RGB
                r2 = p.add_run("“%s”" % text)
                r2.font.size = Pt(11.5); r2.bold = True
                r2.font.color.rgb = NAVY_RGB
            elif kind in ("story", "story_opt"):
                p = d.add_paragraph()
                p.paragraph_format.left_indent = Inches(0.22)
                p.paragraph_format.space_before = Pt(4)
                p.paragraph_format.space_after = Pt(6)
                lab = "STORY   " if kind == "story" else "STORY, OPTIONAL   "
                r = p.add_run(lab); r.bold = True
                r.font.size = Pt(9); r.font.color.rgb = GOLD_RGB
                r2 = p.add_run(text); r2.font.size = Pt(10.5); r2.italic = True

    last = SL.SLIDES[v["n"]][-1]
    h(d, "close · say word for word")
    _p(d, "[ON SCREEN] Slide %d, %s: %s"
       % (last["no"], last["label"], last["when"]), 9, True, GOLD_RGB, 0, 5)
    for line in v["close"]:
        _p(d, line, 12, False, None, 0, 8)

    h(d, "every on-screen cue in this script")
    rows = [[str(s["no"]), s["label"], s["when"], s["name"] + ".png"]
            for s in SL.SLIDES[v["n"]]]
    table(d, ["#", "Slide", "When", "PNG"], rows, [0.35, 1.9, 2.1, 2.7])
    footer(d)
    d.save(path)
    return path

# ===================================================================== 3
def riverside_doc(v, path):
    """One page. The brief says one page, so everything here is measured
    against the printable height and trimmed to fit rather than allowed to
    spill onto a second sheet the presenter would have to shuffle on camera."""
    d = Document()
    st = d.styles["Normal"]
    st.font.name = "DM Sans"; st.font.size = Pt(8.5)
    st.paragraph_format.space_after = Pt(2)
    st.paragraph_format.line_spacing = 1.08
    for sec in d.sections:
        sec.top_margin = sec.bottom_margin = Inches(0.42)
        sec.left_margin = sec.right_margin = Inches(0.5)

    def hh(t, before=7):
        _p(d, t.upper(), 9, True, NAVY_RGB, before, 2)
    def line(t, size=8.5, bold=False, color=None, ind=0, before=0, after=1.5,
             italic=False):
        pp = d.add_paragraph()
        pp.paragraph_format.space_before = Pt(before)
        pp.paragraph_format.space_after = Pt(after)
        pp.paragraph_format.line_spacing = 1.08
        if ind: pp.paragraph_format.left_indent = Inches(ind)
        r = pp.add_run(t); r.font.size = Pt(size); r.bold = bold
        r.italic = italic
        if color is not None: r.font.color.rgb = color
        return pp

    _p(d, "RIVERSIDE RECORDING SHEET \u00b7 VIDEO %d OF 3" % v["n"],
       7.5, True, GOLD_RGB, 0, 1)
    _p(d, v["title"], 13, True, NAVY_RGB, 0, 1)
    line("%s  \u00b7  publishes %s  \u00b7  one page, keep it beside the camera"
         % (v["length"], v["publish"]), 8, color=GREY_RGB, after=3)

    hh("setup", 4)
    line("16:9 at 1080p or 4K, separate audio and video tracks. Same outfit, "
         "background and framing as the other two videos. Chest-up, eyes on "
         "the top third, soft light from the front. Record 10 seconds of room "
         "tone first.")

    hh("teleprompter: these lines only, nothing else")
    for lab, key in (("Hook", "hook"), ("Roadmap", "roadmap"),
                     ("Close", "close")):
        line(lab, 8, True, GOLD_RGB, before=3, after=1)
        for t in v[key]:
            line(t, 8.5, ind=0.16)
    line("The middle stays on talking points so the delivery sounds like you.",
         7.5, color=GREY_RGB, before=2, italic=True)

    hh("segments \u00b7 record each one separately, in this order")
    rows = [["1", "Hook", "0:00", "Prompter. 3 takes."],
            ["2", "Roadmap", "after hook", "Prompter. 1 take, +1 if needed."]]
    i = 3
    for at, head, _b in v["middle"]:
        rows.append([str(i), head.title(), at, "Talking points. 1 take."])
        i += 1
    rows.append([str(i), "Close", v["chapters"][-1][0], "Prompter. 3 takes."])
    t = d.add_table(rows=0, cols=4); t.style = "Table Grid"
    for r0 in rows:
        cells = t.add_row().cells
        for j, val in enumerate(r0):
            cells[j].text = ""
            pp = cells[j].paragraphs[0]
            pp.paragraph_format.space_after = Pt(0)
            pp.paragraph_format.line_spacing = 1.0
            rr = pp.add_run(val); rr.font.size = Pt(7.8)
            if j == 1: rr.bold = True
    for r0 in t.rows:
        for j, w in enumerate([0.26, 2.75, 0.72, 3.7]):
            r0.cells[j].width = Inches(w)
    line("Pause three seconds in silence between segments. If one goes wrong, "
         "pause, then restart the sentence. Do not stop recording.",
         8, before=3)

    hh("pickups \u00b7 record after the main pass, for Shorts and punch-ins")
    says = [t2 for _a, _h, beats in v["middle"] for k, t2 in beats if k == "say"]
    if not says:
        says = [v["close"][0]]
    for s2 in says:
        line("\u00b7  \u201c%s\u201d" % s2, 8.5, ind=0.1)

    hh("b-roll")
    line("  ".join("\u00b7  " + b.rstrip(".") + "." for b in SL.BROLL), 8.2)

    hh("session")
    line("Video 1, short break, Video 2, short break, Video 3. About 2.5 to 3 "
         "hours including setup.", 8.5)
    _p(d, FOOT, 7, False, GREY_RGB, 5, 0, italic=True)
    d.save(path)
    return path

# ===================================================================== 4
def editor_doc(v, path):
    d = doc()
    title(d, "editor notes", "Video %d · %s" % (v["n"], v["title"]),
          "%s  ·  publishes %s" % (v["length"], v["publish"]))

    h(d, "cut list by chapter", 10)
    slides = {s["at"]: s for s in SL.SLIDES[v["n"]]}
    rows = []
    for i, (t, ch) in enumerate(v["chapters"]):
        s = slides.get(t)
        sl = ("Slide %d, %s\n%s.png" % (s["no"], s["label"], s["name"])
              if s else "No slide")
        if i == 0:
            note = ("Tight cuts. Remove every pause over half a second and "
                    "all filler. Lower third at 0:08.")
        elif i == 1:
            note = ("Roadmap slide holds while she lists the steps. After "
                    "this chapter, allow natural pauses on key lines.")
        else:
            note = ("Slide full-screen 3 to 5 seconds when first named, then "
                    "picture-in-picture while she talks it through.")
        rows.append([t, ch, sl, note])
    table(d, ["Time", "Chapter", "Slide", "Cut note"], rows,
          [0.6, 2.0, 1.6, 2.7])

    h(d, "caption cards · every SAY THIS line")
    cc = [(at, t) for at, _h, beats in v["middle"] for k, t in beats
          if k == "say"]
    if cc:
        table(d, ["Around", "Caption card text", "Treatment"],
              [[at, "“%s”" % t,
                "Sand on navy, centered, 2 to 3 seconds"] for at, t in cc],
              [0.75, 3.85, 2.3])
    else:
        _p(d, "This script carries no SAY THIS line. The script slide at "
              "8:15 is the card for this video.", 10.5)

    h(d, "slide timings")
    table(d, ["#", "Slide", "First appears", "File"],
          [[str(s["no"]), s["label"], s["when"], s["name"] + ".png"]
           for s in SL.SLIDES[v["n"]]], [0.35, 1.9, 2.1, 2.6])

    h(d, "lower third")
    _p(d, "At about 0:08: “%s”. Sand %s text on a navy %s band. DM "
          "Sans or Montserrat. Hold 4 to 5 seconds, then fade."
       % (D.LOWER_THIRD, D.SAND, D.NAVY), 10.5)

    h(d, "pacing")
    bullet(d, "First 60 seconds: tight. Every pause over half a second and "
              "all filler comes out.")
    bullet(d, "After the roadmap: allow natural pauses on key lines.")
    bullet(d, "Jump cuts or slight punch-ins about every 8 to 12 seconds "
              "during talking sections.")

    h(d, "captions")
    _p(d, "Upload a corrected SRT. Check these terms before you deliver:",
       10.5, after=4)
    _p(d, "   " + "   ·   ".join(D.CAPTION_TERMS), 10.5, True, NAVY_RGB)

    h(d, "music")
    _p(d, "Optional, low, under the hook and the end card only. No music "
          "under the teaching sections.", 10.5)

    h(d, "style limits")
    _p(d, "No emojis, arrows, sound effects, zoom whooshes or stock footage. "
          "Brand colors only: navy %s, sand %s, gold %s."
       % (D.NAVY, D.SAND, D.GOLD), 10.5)

    h(d, "end screen and cards")
    _p(d, "Last 20 seconds: %s" % v["end_screen"], 10.5, after=4)
    for at, what in v["cards"]:
        bullet(d, "Card at %s pointing to %s." % (at, what))

    h(d, "exports")
    bullet(d, "16:9 master at the recorded resolution, H.264, high bitrate.")
    bullet(d, "Shorts: 9:16, 1080 x 1920, under 60 seconds, burned-in "
              "captions. See the Shorts cut sheet.")
    footer(d)
    d.save(path)
    return path

# ===================================================================== 6
def upload_doc(v, path):
    d = doc()
    title(d, "upload sheet", "Video %d · %s" % (v["n"], v["title"]),
          "Everything that goes into the YouTube upload form.")

    h(d, "title and scheduling", 10)
    kv(d, "Title", v["title"])
    kv(d, "Alternate title", v["alt_title"])
    kv(d, "Publish date", v["publish"])
    kv(d, "Publish time", v["publish_time"])
    kv(d, "Length", v["length"])
    kv(d, "Visibility", "Scheduled. Do not publish manually before the date.")
    kv(d, "Playlist", D.PLAYLIST_TITLE)
    kv(d, "Position in playlist", "%d of 3" % v["n"])
    if v["n"] == 1:
        _p(d, "Create the playlist before January 4 so Video 1 launches "
              "inside it.", 9.5, True, GOLD_RGB, 4, 6)

    h(d, "description · copy ready")
    for para in v["description"]:
        _p(d, para, 10.5, after=7)
    _p(d, "Then paste the chapters below, starting on their own line.",
       9.5, False, GREY_RGB, 2, 6, italic=True)

    h(d, "chapters · paste under the description")
    _p(d, "The first chapter has to start at 0:00 or YouTube will not build "
          "the chapter list.", 9, False, GREY_RGB, 0, 6, italic=True)
    for t, ch in v["chapters"]:
        p = d.add_paragraph()
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(t + " "); r.bold = True; r.font.size = Pt(10.5)
        r.font.color.rgb = NAVY_RGB
        p.add_run(ch).font.size = Pt(10.5)

    h(d, "tags")
    _p(d, ", ".join(v["tags"]), 10.5)

    h(d, "pinned comment")
    _p(d, v["pinned"], 10.5)

    h(d, "end screen and cards")
    kv(d, "End screen", v["end_screen"])
    for at, what in v["cards"]:
        kv(d, "Card at " + at, what)

    h(d, "thumbnail")
    kv(d, "File", "%s_THUMBNAIL_1280x720.png" % v["slug"])
    kv(d, "Text", "  ".join(v["thumb_text"]))
    kv(d, "Alternate", "%s_THUMBNAIL_1280x720_contrast.png" % v["slug"])

    h(d, "before you hit schedule")
    for c in ["Captions: corrected SRT uploaded, not auto-generated.",
              "Chapter wording matches the roadmap you spoke.",
              "Playlist set, and the video sits in position %d." % v["n"],
              "End screen points where this sheet says it points.",
              "Thumbnail checked at 160 pixels wide.",
              "Links in the description open the right pages."]:
        bullet(d, c)
    footer(d)
    d.save(path)
    return path

# ===================================================================== 7
def shorts_doc(v, path):
    d = doc()
    n = v["n"]
    clips = SL.SHORTS[n]
    title(d, "shorts cut sheet",
          "Video %d · %s" % (n, v["title"]),
          "%d clip%s. 9:16, 1080 x 1920, under 60 seconds, burned-in "
          "captions." % (len(clips), "" if len(clips) == 1 else "s"))

    h(d, "specification", 10)
    bullet(d, "9:16, 1080 x 1920. Under 60 seconds, no exceptions.")
    bullet(d, "Reframe from the 16:9 master. Keep her eyes on the top third.")
    bullet(d, "Captions burned in: sand %s on navy %s, centered, heavy sans."
              % (D.SAND, D.NAVY))
    bullet(d, "No emojis, arrows, sound effects or stock footage.")
    bullet(d, "Use the pickup take where one exists. It is a cleaner read "
              "than the take inside the long-form cut.")

    for c in clips:
        h(d, "clip %d · %s" % (c["no"], c["name"]))
        kv(d, "Source", c["source"])
        kv(d, "Pull from", c["pull"])
        kv(d, "Target length", c["target"])
        kv(d, "File", c["name"] + ".mp4")
        _p(d, "Spoken", 9.5, True, GOLD_RGB, 6, 2)
        _p(d, c["spoken"], 10.5, indent=0.2)
        _p(d, "Caption text, in order", 9.5, True, GOLD_RGB, 6, 2)
        table(d, ["#", "On-screen caption"],
              [[str(i), t] for i, t in enumerate(c["captions"], 1)],
              [0.35, 6.1])
    footer(d)
    d.save(path)
    return path
