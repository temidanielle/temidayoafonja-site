#!/usr/bin/env python3
"""Build the Keep the Proof V2 Guided Handbook: markdown -> designed HTML -> PDF.
Applies the Keep the Proof / Capability Formation visual identity."""
import re, html, subprocess, sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
import record_model as M
import icons as I

ROOT = "/home/user/temidayoafonja-site"
# Table of contents entries: (display label, heading search string, indent).
# computetoc locates each entry by its actual section HEADING (not a body phrase),
# scanning pages in document order from a cursor that starts after the Contents
# page. Because entries are in document order, the ordered scan skips the Contents
# page (where the labels are printed) and any earlier body reference to the same
# words, landing on the page where the heading itself is rendered.
TOC_ENTRIES = [
    ("Before You Rebuild Anything", "Before You Rebuild Anything", False),
    ("Part One: Understand the Record", "PART ONE", False),
    ("What It Costs When the Proof Is Gone", "What It Costs When the Proof Is Gone", True),
    ("Your First 60 Minutes", "YOUR FIRST 60 MINUTES", False),
    ("Part Two: Capture", "PART TWO", False),
    ("Part Three: Permission and Protection", "PART THREE", False),
    ("Part Four: Clarify", "PART FOUR", False),
    ("Part Five: Carry", "PART FIVE", False),
    ("Part Six: Worked Examples", "PART SIX", False),
    ("Part Seven: Reconstruct", "PART SEVEN", False),
    ("Part Eight: Keep It Current, and Use It", "PART EIGHT", False),
    ("Match Your Proof to a Role", "Match Your Proof to a Role", True),
    ("Put Your Record to Work", "Put Your Record to Work", True),
    ("Part Nine: The Record You Own", "PART NINE", False),
    ("Closing", "CLOSING", False),
]
_TOC_JSON = os.path.join(os.path.dirname(__file__), "toc_pages.json")
try:
    TOC_PAGES = json.load(open(_TOC_JSON)) if os.path.exists(_TOC_JSON) else {}
except Exception:
    TOC_PAGES = {}
SRC = f"{ROOT}/_build/keep-the-proof-v2/production/FINAL_MANUSCRIPT.md"
OUT_HTML = f"{ROOT}/_build/keep-the-proof-v2/production/renders/handbook.html"
OUT_PDF = f"{ROOT}/_build/keep-the-proof-v2/production/bundle/02_KEEP_THE_PROOF_GUIDED_HANDBOOK.pdf"
FONTS = f"file://{ROOT}/fonts"

# Two-pass TOC: after a first build, this mode scans the rendered PDF for each
# entry's page and writes toc_pages.json; the next build bakes those numbers in.
if len(sys.argv) > 1 and sys.argv[1] == "computetoc":
    import pypdfium2 as pdfium
    _d = pdfium.PdfDocument(OUT_PDF)
    _nows = re.compile(r"\s+")
    # de-space page text so letter-spaced divider kickers still match
    _per = [_nows.sub("", _d[i].get_textpage().get_text_range()) for i in range(len(_d))]
    # Locate the Contents page so the scan can begin after it: its printed labels
    # would otherwise match every entry on page 3. Fall back to index 2 (page 3).
    _contents_idx = next((i for i in range(len(_d))
                          if "Contents" in _d[i].get_textpage().get_text_range()[:40]), 2)
    _pages = {}
    _cursor = _contents_idx + 1  # first page after Contents
    for _label, _key, _indent in TOC_ENTRIES:
        _k = _nows.sub("", _key)
        for _i in range(_cursor, len(_per)):
            if _k in _per[_i]:
                _pages[_key] = _i + 1
                _cursor = _i  # next entry may share this page; do not advance past it
                break
    json.dump(_pages, open(_TOC_JSON, "w"))
    print("toc pages:", _pages)
    sys.exit(0)

NAVY = "#112345"
CREAM = "#F5F1E8"
GOLD = "#C9A84C"
YELLOW = "#F2C44C"
PAGEBG = "#FFFFFF"
INK = "#1c2333"
HAIR = "#D9CBB2"
RUST = "#C1440E"

# ---------- read + split into blocks ----------
raw = open(SRC, encoding="utf-8").read()
# normalize
lines = raw.split("\n")

# Extract cover lines (between "## Cover" and "## The record and the fine print")
def between(start_pat, end_pat):
    out=[]; cap=False
    for ln in lines:
        if re.match(start_pat, ln): cap=True; continue
        if cap and re.match(end_pat, ln): break
        if cap: out.append(ln)
    return [l for l in out if l.strip()]

cover_lines = between(r'^## Cover\s*$', r'^## ')

# Build blocks: everything after front-matter cover handled generically.
# We'll parse the whole doc into (kind, payload) blocks, skipping the Cover section body.
blocks = []
i = 0
n = len(lines)
skip_cover = False
while i < n:
    ln = lines[i]
    if re.match(r'^# ', ln):
        blocks.append(("h1", ln[2:].strip())); i+=1; continue
    if re.match(r'^### ', ln):
        blocks.append(("h3", ln[4:].strip())); i+=1; continue
    if re.match(r'^## ', ln):
        title = ln[3:].strip()
        if title == "Cover":
            # skip until next H2
            i+=1
            while i < n and not re.match(r'^## ', lines[i]) and not re.match(r'^# ', lines[i]):
                i+=1
            continue
        blocks.append(("h2", title)); i+=1; continue
    if re.match(r'^---\s*$', ln):
        i+=1; continue
    if re.match(r'^\s*- ', ln):
        items=[]
        while i < n and re.match(r'^\s*- ', lines[i]):
            items.append(lines[i].strip()[2:].strip()); i+=1
        blocks.append(("ul", items)); continue
    if ln.strip()=="":
        i+=1; continue
    # paragraph: gather until blank
    para=[ln.strip()]; i+=1
    while i < n and lines[i].strip()!="" and not re.match(r'^#{1,3} ', lines[i]) and not re.match(r'^---\s*$', lines[i]) and not re.match(r'^\s*- ', lines[i]):
        para.append(lines[i].strip()); i+=1
    blocks.append(("p", " ".join(para)))

# ---------- helpers ----------
def esc(t):
    t = html.escape(t)
    # inline emphasis: **bold**, *italic*, `code`
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'`(.+?)`', r'<code>\1</code>', t)
    return t

CARD_LABELS = ["What happened:", "Portable version:", "Kept versus left out:", "The work:",
    "The team result:", "The risk forming:", "Must stay out:", "The judgment:",
    "Quick Capture:", "Confidentiality check:", "Who could corroborate:", "Who could confirm this:",
    "My specific contribution:", "What changed:", "Full Entry", "Proof Line:", "My actual contribution:",
    "My contribution:", "Actual ownership:", "The situation:", "The path avoided:", "Why this one is delicate:",
    "Retrieval tags:", "The outcome:", "Kept versus left"]

def is_card(text):
    hits = sum(1 for lab in CARD_LABELS if lab in text)
    return hits >= 2

def leadbold(html_text):
    # Bold a short run-in label ("Label:") at the very start of a paragraph or list item.
    # Kept tight (<= 3 words, <= 28 chars) so sentence lead-ins are not bolded.
    m = re.match(r"^([A-Z][A-Za-z0-9][A-Za-z0-9 ,/&-]{0,32}?:)\s", html_text)
    if m:
        label = m.group(1)
        if len(label) <= 28 and len(label.rstrip(':').split()) <= 3:
            return '<strong>' + label + '</strong>' + html_text[m.end(1):]
    return html_text

def bold_labels(text):
    # bold the "Label:" run-in headers inside cards
    def repl(m):
        return f'<strong class="lab">{m.group(1)}:</strong>'
    # match capitalized short label followed by colon
    return re.sub(r'(?<![\w])([A-Z][A-Za-z][A-Za-z ’\'/,-]{1,42}?):', repl, text)

# Section-title -> intro subtitle (the paragraph right after a PART h1)
PART_SET = {"PART ONE — UNDERSTAND THE RECORD","PART TWO — CAPTURE","PART THREE — PERMISSION AND PROTECTION",
    "PART FOUR — CLARIFY","PART FIVE — CARRY","PART SIX — WORKED EXAMPLES","PART SEVEN — RECONSTRUCT",
    "PART EIGHT — KEEP IT CURRENT, AND USE IT","PART NINE — THE RECORD YOU OWN"}
SPECIAL_H1 = {"FRONT MATTER","YOUR FIRST 60 MINUTES","CLOSING"}

# ---------- marquee device injectors ----------
def spine_device():
    ic_cap = I.svg("capture", px=26, cls="spine-ico", label=True)
    ic_cla = I.svg("clarify", px=26, cls="spine-ico", label=True, stroke=CREAM)
    ic_car = I.svg("carry", px=26, cls="spine-ico", label=True)
    return f'''
<div class="spine">
  <div class="spine-step"><div class="spine-ico-wrap">{ic_cap}</div><div class="spine-n">01</div><div class="spine-t">CAPTURE</div><div class="spine-q">What happened?</div></div>
  <div class="spine-arrow">&rarr;</div>
  <div class="spine-step focus"><div class="spine-ico-wrap">{ic_cla}</div><div class="spine-n">02</div><div class="spine-t">CLARIFY</div><div class="spine-q">What was yours?</div><div class="spine-tag">the heart of the system</div></div>
  <div class="spine-arrow">&rarr;</div>
  <div class="spine-step"><div class="spine-ico-wrap">{ic_car}</div><div class="spine-n">03</div><div class="spine-t">CARRY</div><div class="spine-q">What can you responsibly take forward?</div></div>
</div>'''

def kcn_device():
    ic_keep = I.svg("keep", px=22, cls="kcn-ico", label=True, stroke=CREAM)
    ic_care = I.svg("care", px=22, cls="kcn-ico", label=True)
    ic_never = I.svg("never", px=22, cls="kcn-ico", label=True)
    return f'''
<div class="kcn">
  <div class="kcn-tier keep"><div class="kcn-ico-wrap">{ic_keep}</div><div class="kcn-h">KEEP</div><div class="kcn-b">Your own high-level recollection: what you did, decisions you made, problems you helped prevent, publicly disclosed outcomes, and anything your employer has expressly permitted you to retain.</div></div>
  <div class="kcn-tier care"><div class="kcn-ico-wrap">{ic_care}</div><div class="kcn-h">CARE</div><div class="kcn-b">Numbers, client or project detail, and internal context that may be sensitive. Seek permission, use only what is already public, or leave it out. When unsure, treat it as the next tier.</div></div>
  <div class="kcn-tier never"><div class="kcn-ico-wrap">{ic_never}</div><div class="kcn-h">NEVER</div><div class="kcn-b">Source code, credentials, security settings, customer or employee data, unreleased product detail, internal financials, privileged or legal material, trade secrets, and any file your employer owns. Never copy, forward, screenshot, download, or reconstruct these anywhere.</div></div>
  <div class="kcn-rule">Default downward. Between Keep and Care, treat as Care. Between Care and Never, treat as Never.</div>
</div>'''

def doors_device():
    ic_now = I.svg("capture", px=22, cls="door-ico", label=True)
    ic_lost = I.svg("reconstruct", px=22, cls="door-ico", label="Reconstruct")
    return f'''
<div class="doors">
  <div class="door"><div class="door-ico-wrap">{ic_now}</div><div class="door-k">Capturing now?</div><div class="door-t">Start here</div><div class="door-b">You still have your access, your systems, and your memory of recent work. You are in the best possible position, because you can capture the record while the facts are fresh. Begin with Your First 60 Minutes, then let the habit carry it forward.</div></div>
  <div class="door"><div class="door-ico-wrap">{ic_lost}</div><div class="door-k">Already lost access?</div><div class="door-t">Start here</div><div class="door-b">The change has already happened, and the record you wish you had does not exist yet. You have not failed, and you did not buy the wrong guide. You simply start differently, by rebuilding from what is still yours. Turn to Part Seven, Reconstruct.</div></div>
</div>'''

def match_device():
    return f'''
<p class="match-instr"><span class="inl-ico">{I.svg("match", px=16, label=True)}</span>Pick three requirements from one posting. Match each to a Proof Line you have already written. If none fits, write the gap in the third column instead of stretching a line to cover it. A named gap is more credible than a stretched claim.</p>
<table class="match">
  <thead><tr><th>What the role asks for</th><th>My Proof Line that shows it</th><th>The gap I will name</th></tr></thead>
  <tbody>
    <tr class="ex"><td><strong>Example.</strong> Design and run onboarding for a growing team (in the posting&#8217;s own words).</td><td>Redesigned new-hire onboarding for a growing operations team, cutting time to full productivity and reducing early attrition, with the model later adopted by two other departments.</td><td>The posting asks for direct management of trainers. I coordinated them without that title, so I will name the scope I carried and not imply the title.</td></tr>
    <tr><td></td><td></td><td></td></tr>
    <tr><td></td><td></td><td></td></tr>
    <tr><td></td><td></td><td></td></tr>
  </tbody>
</table>'''

def rebuild_subtitle_device():
    return '<p class="chapter-sub">See what you already built</p>'

def cost_device():
    rows = [
        ("Performance review", "You describe a hard year in general words, and the review settles for them.", "You name the decisions, what changed, and who saw it."),
        ("Promotion conversation", "Your name comes up, and no one can say exactly what you handled.", "Someone has specific sentences to repeat about your work."),
        ("Interview", "Ten years become a few vague stories, and the offer comes in a level down.", "Each answer rests on a Proof Line you can stand behind."),
        ("Reorganization or layoff", "Your access can end the same day, and the details go with it.", "Your own account of the work is already somewhere you control."),
        ("Internal move", "People know you for your old job, and the new team cannot see your range.", "You can show the judgment that fits the new role."),
        ("Returning after leave or time away", "Your best recent work feels far away and hard to name.", "Your record reminds you, and others, what you built."),
    ]
    body = "".join(
        f'<tr><td class="cost-m">{esc(m)}</td><td>{esc(a)}</td><td class="cost-with">{esc(b)}</td></tr>'
        for m, a, b in rows)
    return f'''
<p class="chapter-sub">Six moments where your record matters most</p>
<table class="cost">
  <thead><tr><th>The moment</th><th>Without a record</th><th>With a record</th></tr></thead>
  <tbody>{body}</tbody>
</table>
<p class="cost-close">The work was real either way. The record decides how much of it someone else can see.</p>'''

def fades_diagram_device():
    # vector line chart, no numbers; navy = record holds, gold = memory fades
    W, H = 520, 250
    ox, oy = 46, 24           # plot origin offsets (left, top)
    pw, ph = W - ox - 20, H - oy - 46
    x0, y0 = ox, oy
    xr, yb = ox + pw, oy + ph
    # memory: high then fast decay to low flat (gold)
    mem = []
    import math
    for i in range(41):
        t = i / 40
        val = math.exp(-5.5 * t)
        mem.append((x0 + t * pw, yb - (0.12 + 0.82 * val) * ph))
    mem_pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in mem)
    # record: rising staircase then hold (navy)
    steps = [0.10, 0.10, 0.34, 0.34, 0.55, 0.55, 0.72, 0.72, 0.84, 0.84, 0.84, 0.84]
    n = len(steps)
    rec = [(x0 + (i / (n - 1)) * pw, yb - (0.06 + s * 0.84) * ph) for i, s in enumerate(steps)]
    rec_pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in rec)
    return f'''
<div class="fades">
<p class="fades-title">What Fades and What Holds</p>
<svg viewBox="0 0 {W} {H}" class="fades-svg" role="img" aria-label="An illustration: what you remember fades quickly after the work ends, while what your record holds steps up with each entry and then holds level.">
  <line x1="{x0}" y1="{y0}" x2="{x0}" y2="{yb}" class="axis"/>
  <line x1="{x0}" y1="{yb}" x2="{xr}" y2="{yb}" class="axis"/>
  <polyline points="{mem_pts}" class="line-mem"/>
  <polyline points="{rec_pts}" class="line-rec"/>
  <text x="{x0-6}" y="{y0+4}" class="axis-lbl axis-y" transform="rotate(-90 {x0-6} {y0+4})" text-anchor="end">Detail you can use</text>
  <text x="{xr}" y="{yb+18}" class="axis-lbl" text-anchor="end">Time since the work &rarr;</text>
  <text x="{rec[-1][0]-4:.0f}" y="{rec[-1][1]-8:.0f}" class="key key-rec" text-anchor="end">What your record holds</text>
  <text x="{mem[12][0]+6:.0f}" y="{mem[12][1]-6:.0f}" class="key key-mem">What you remember</text>
  <text x="{xr}" y="{y0+6}" class="note" text-anchor="end">An illustration of the idea, not data from a study.</text>
</svg>
<p class="fades-cap">The details another person needs are often the first to fade. A short entry made while the work is fresh keeps them.</p>
</div>'''

def toc_device():
    rows = ""
    for label, key, indent in TOC_ENTRIES:
        num = TOC_PAGES.get(key, "")
        cls = "toc-row toc-sub" if indent else "toc-row"
        rows += (f'<div class="{cls}"><span class="toc-label">{esc(label)}</span>'
                 f'<span class="toc-dots"></span><span class="toc-num">{num}</span></div>')
    return f'<section class="toc-page"><h1 class="toc-title">Contents</h1><div class="toc-list">{rows}</div></section>'

def words_panel_device():
    lines = "".join(f'<div class="wline">{html.escape(w)}</div>' for w in M.WORDS_AFFIRMATIONS)
    fill = f'<div class="wline wfill">{html.escape(M.WORDS_FILLIN)} <span class="wblank"></span></div>'
    ico = I.svg("words", px=20, cls="words-ico", label=True)
    return f'''
<div class="words">
  <div class="words-ico-wrap">{ico}</div>
  {lines}
  {fill}
</div>'''

# Prose paragraphs made redundant by an injected device — dropped so the
# device is not shadowed by a near-verbatim restatement.
SKIP_PREFIXES = [
    "Capturing now? Start here.",
    "Already lost access? Start here.",
    "You still have your access, your systems, your memory of recent work. You are in the best possible position",
    "The change has already happened. The systems are closed and the record you wish you had does not exist yet.",
    "Keep. Your own high-level recollection of what you did",
    "Care. Numbers, client or project detail, and internal context",
    "Never. Source code, credentials, security settings",
]
def is_skipped(text):
    t = text.strip()
    return any(t.startswith(p) for p in SKIP_PREFIXES)

INJECT_AFTER_H2 = {
    "The spine: Capture, Clarify, Carry": spine_device,
    "Keep, Care, Never": kcn_device,
    "Two ways in": doors_device,
    "Match Your Proof to a Role": match_device,
    "Before You Rebuild Anything": rebuild_subtitle_device,
    "What It Costs When the Proof Is Gone": cost_device,
    "The Two-Minute Quick Capture": fades_diagram_device,
}

# Chapter-level h2 headings that must begin on a fresh page.
PAGE_BREAK_H2 = {"Before You Rebuild Anything"}

# Icons rendered inline before a matching heading (h2 or h3).
ICON_FOR_HEADING = {
    "Build: the Proof Line": "proofline",
    "A resume line": "resume",
    "A LinkedIn About sentence": "about",
    "An interview answer, in three parts": "interview",
    "A promotion or self-review note": "promotion",
}

# ---------- render body ----------
body = []
part_counter = 0
prev_was_h1_part = False
pending_caption = None  # short p that should ride above a following card

def flush_caption_as_para():
    global pending_caption
    if pending_caption is not None:
        body.append(f'<p>{esc(pending_caption)}</p>')
        pending_caption = None

for idx,(kind,payload) in enumerate(blocks):
    if kind=="h1":
        flush_caption_as_para()
        if payload in PART_SET:
            part_counter += 1
            # look ahead for the immediately following paragraph (subtitle)
            sub = ""
            if idx+1 < len(blocks) and blocks[idx+1][0]=="p":
                sub = blocks[idx+1][1]
            roman = payload.split("—")[0].strip()  # "PART ONE"
            title = payload.split("—",1)[1].strip() if "—" in payload else payload
            body.append(f'''<section class="part-divider"><div class="pd-inner">
              <div class="pd-kicker">{esc(roman)}</div>
              <h1 class="pd-title">{esc(title)}</h1>
              <div class="pd-rule"></div>
              <div class="pd-sub">{esc(sub)}</div>
            </div></section>''')
            # mark that next paragraph (the subtitle) should be skipped
            blocks[idx+1] = ("_skip","") if idx+1 < len(blocks) and blocks[idx+1][0]=="p" else blocks[idx+1] if idx+1<len(blocks) else None
        else:
            # special section headers (FRONT MATTER, YOUR FIRST 60 MINUTES, CLOSING)
            if payload == "FRONT MATTER":
                # emit cover page then continue
                cov_title = cover_lines[0] if cover_lines else "KEEP THE PROOF"
                cov_desc = cover_lines[1] if len(cover_lines)>1 else ""
                cov_for = cover_lines[2] if len(cover_lines)>2 else ""
                cov_by = cover_lines[3] if len(cover_lines)>3 else ""
                body.append(f'''<section class="cover"><div class="cv-inner">
                  <h1 class="cv-title">{esc(cov_title)}</h1>
                  <div class="cv-rule"></div>
                  <div class="cv-desc">{esc(cov_desc)}</div>
                  <div class="cv-for">{esc(cov_for)}</div>
                  <div class="cv-by">{esc(cov_by)}</div>
                </div></section>''')
            else:
                body.append(f'<section class="band-divider"><h1 class="bd-title">{esc(payload)}</h1></section>')
        prev_was_h1_part = payload in PART_SET
        continue
    if kind=="_skip":
        continue
    if kind=="h2":
        flush_caption_as_para()
        if payload == "Contents":
            body.append(toc_device()); continue
        ic = ICON_FOR_HEADING.get(payload)
        pre = f'<span class="h-ico">{I.svg(ic, px=19, label=True)}</span>' if ic else ''
        hcls = ' class="chapter-start"' if payload in PAGE_BREAK_H2 else ''
        body.append(f'<h2{hcls}>{pre}{esc(payload)}</h2>')
        if payload in INJECT_AFTER_H2:
            body.append(INJECT_AFTER_H2[payload]())
        continue
    if kind=="h3":
        flush_caption_as_para()
        ic = ICON_FOR_HEADING.get(payload)
        pre = f'<span class="h-ico h-ico-sm">{I.svg(ic, px=17, label=True)}</span>' if ic else ''
        body.append(f'<h3>{pre}{esc(payload)}</h3>')
        continue
    if kind=="ul":
        flush_caption_as_para()
        items_html = []
        for it in payload:
            raw = it
            has_pause = raw.rstrip().endswith("{{pause}}")
            if has_pause:
                raw = raw.rstrip()[:-len("{{pause}}")].rstrip()
            lead_ico = ""
            if raw.startswith("A monthly sweep"):
                lead_ico = f'<span class="li-ico">{I.svg("monthly", px=15, label=True)}</span>'
            elif raw.startswith("A quarterly review"):
                lead_ico = f'<span class="li-ico">{I.svg("quarterly", px=15, label=True)}</span>'
            cell = lead_ico + leadbold(esc(raw))
            if has_pause:
                cell += f' <span class="pause">{I.svg("pause", px=12, cls="pause-ico", label=True)}Good place to pause</span>'
            items_html.append(f'<li>{cell}</li>')
        body.append(f'<ul>{"".join(items_html)}</ul>')
        continue
    if kind=="p":
        text = payload
        if text.strip() == "{{words-panel}}":
            flush_caption_as_para()
            body.append(words_panel_device())
            continue
        if is_skipped(text):
            continue
        if is_card(text):
            cap = ""
            if pending_caption is not None:
                cap = f'<div class="card-cap">{esc(pending_caption)}</div>'
                pending_caption = None
            body.append(f'<div class="card">{cap}<p>{bold_labels(esc(text))}</p></div>')
        else:
            # is this a short caption preceding a card? peek next
            nxt = blocks[idx+1] if idx+1 < len(blocks) else ("","")
            if len(text) < 150 and nxt[0]=="p" and is_card(nxt[1]):
                pending_caption = text
            else:
                flush_caption_as_para()
                # pull-quote for the emphatic one-rule lines
                body.append(f'<p>{leadbold(esc(text))}</p>')
        continue

flush_caption_as_para()
body_html = "\n".join(b for b in body if b)

# ---------- CSS ----------
css = f'''
@font-face{{font-family:'Cormorant';src:url('{FONTS}/CormorantGaramond-400-normal-latin-abcaa8.woff2') format('woff2');font-weight:400;font-style:normal;}}
@font-face{{font-family:'Cormorant';src:url('{FONTS}/CormorantGaramond-400-italic-latin-4db21d.woff2') format('woff2');font-weight:400;font-style:italic;}}
@font-face{{font-family:'Cormorant';src:url('{FONTS}/CormorantGaramond-500-normal-latin-abcaa8.woff2') format('woff2');font-weight:500;font-style:normal;}}
@font-face{{font-family:'Cormorant';src:url('{FONTS}/CormorantGaramond-600-normal-latin-abcaa8.woff2') format('woff2');font-weight:600;font-style:normal;}}
@font-face{{font-family:'DM Sans';src:url('{FONTS}/DMSans-300-normal-latin-1c49a6.woff2') format('woff2');font-weight:300;font-style:normal;}}
@font-face{{font-family:'DM Sans';src:url('{FONTS}/DMSans-400-normal-latin-1c49a6.woff2') format('woff2');font-weight:400;font-style:normal;}}
@font-face{{font-family:'DM Sans';src:url('{FONTS}/DMSans-500-normal-latin-1c49a6.woff2') format('woff2');font-weight:500;font-style:normal;}}
@font-face{{font-family:'DM Sans';src:url('{FONTS}/DMSans-600-normal-latin-1c49a6.woff2') format('woff2');font-weight:600;font-style:normal;}}

@page{{size:8.5in 11in;margin:0.95in 1.05in 0.9in 1.05in;
  @bottom-center{{content:counter(page);font-family:'DM Sans',sans-serif;font-size:8pt;color:#9096a1;}}}}
@page bleed{{size:8.5in 11in;margin:0;@bottom-center{{content:"";}}}}
*{{box-sizing:border-box;}}
html,body{{margin:0;padding:0;background:{PAGEBG};}}
body{{font-family:'DM Sans',sans-serif;font-weight:400;font-size:10.8pt;line-height:1.62;color:{INK};background:{PAGEBG};-webkit-print-color-adjust:exact;print-color-adjust:exact;}}

h2{{font-family:'Cormorant',serif;font-weight:600;font-size:20pt;line-height:1.12;color:{NAVY};margin:1.5em 0 0.15em;padding-top:0.2em;}}
h2::after{{content:"";display:block;width:2.2em;height:2.5px;background:{GOLD};margin-top:.32em;}}
p{{margin:0 0 0.72em;orphans:2;widows:2;}}
h2{{break-after:avoid;page-break-after:avoid;break-inside:avoid;}}
h2.chapter-start{{break-before:page;page-break-before:always;margin-top:0;}}
strong{{font-weight:600;color:{NAVY};}}
code{{font-family:'DM Sans',sans-serif;background:{CREAM};padding:0 .25em;border-radius:3px;font-size:.92em;}}
ul{{margin:0 0 0.9em;padding-left:1.15em;}}
li{{margin:0 0 .34em;padding-left:.15em;}}
li::marker{{color:{GOLD};}}

/* Cover */
.cover{{page:bleed;page-break-after:always;width:8.5in;height:11in;background:{NAVY};color:{CREAM};display:flex;align-items:center;justify-content:center;margin:0;padding:0;}}
.cv-inner{{text-align:center;padding:0 0.9in;}}
.cv-mark{{font-family:'DM Sans';font-weight:500;letter-spacing:.42em;font-size:8.5pt;color:{GOLD};margin-bottom:2.4em;}}
.cv-title{{font-family:'Cormorant',serif;font-weight:600;font-size:52pt;line-height:1;margin:0;color:{CREAM};letter-spacing:.01em;}}
.cv-rule{{width:64px;height:3px;background:{GOLD};margin:1.1em auto 1.2em;}}
.cv-desc{{font-family:'Cormorant',serif;font-style:italic;font-weight:400;font-size:18pt;color:#e8e0cf;margin-bottom:2.6em;}}
.cv-for{{font-family:'DM Sans';font-weight:300;font-size:10.5pt;letter-spacing:.02em;color:#c9d0dd;max-width:22em;margin:0 auto 3.2em;line-height:1.55;}}
.cv-by{{font-family:'DM Sans';font-weight:400;font-size:9.5pt;letter-spacing:.12em;color:{GOLD};}}

/* Part divider */
.part-divider{{page:bleed;page-break-before:always;page-break-after:always;width:8.5in;height:11in;background:{NAVY};color:{CREAM};display:flex;align-items:center;margin:0;padding:0 1.15in;}}
.pd-inner{{width:100%;}}
.pd-kicker{{font-family:'DM Sans';font-weight:500;letter-spacing:.34em;font-size:10pt;color:{GOLD};margin-bottom:.9em;}}
.pd-title{{font-family:'Cormorant',serif;font-weight:600;font-size:40pt;line-height:1.04;margin:0;color:{CREAM};}}
.pd-rule{{width:56px;height:3px;background:{GOLD};margin:1.1em 0 1.2em;}}
.pd-sub{{font-family:'Cormorant',serif;font-style:italic;font-size:15pt;line-height:1.4;color:#dcd4c3;max-width:26em;}}

/* Band divider (Front matter / First 60 / Closing) */
.band-divider{{page-break-before:always;margin:0 0 1.2em;padding:1.6em 0 0;}}
.bd-title{{font-family:'Cormorant',serif;font-weight:600;font-size:30pt;color:{NAVY};margin:0;padding-bottom:.28em;border-bottom:2.5px solid {GOLD};}}

/* Cards (completed examples) */
.card{{background:{CREAM};border-left:3px solid {GOLD};border-radius:6px;padding:.85em 1.05em .55em;margin:.6em 0 1.1em;page-break-inside:avoid;}}
.card .card-cap{{font-family:'DM Sans';font-weight:600;font-size:9pt;letter-spacing:.05em;text-transform:uppercase;color:{GOLD};margin-bottom:.4em;}}
.card p{{margin:0;font-size:10.2pt;line-height:1.56;}}
.card .lab{{color:{NAVY};font-weight:600;}}

/* Spine device */
.spine{{display:flex;align-items:stretch;gap:.5em;margin:1em 0 1.3em;page-break-inside:avoid;}}
.spine-step{{flex:1;background:{CREAM};border-radius:8px;padding:.95em .8em 1em;text-align:center;border-top:3px solid {NAVY};}}
.spine-step.focus{{background:{NAVY};border-top:3px solid {GOLD};color:{CREAM};position:relative;}}
.spine-n{{font-family:'Cormorant',serif;font-size:15pt;color:{GOLD};font-weight:600;}}
.spine-t{{font-family:'DM Sans';font-weight:600;letter-spacing:.16em;font-size:11pt;color:{NAVY};margin:.15em 0 .4em;}}
.spine-step.focus .spine-t{{color:{CREAM};}}
.spine-q{{font-family:'Cormorant',serif;font-style:italic;font-size:12pt;line-height:1.3;color:{INK};}}
.spine-step.focus .spine-q{{color:#e8e0cf;}}
.spine-tag{{margin-top:.5em;font-family:'DM Sans';font-weight:500;font-size:7.5pt;letter-spacing:.1em;text-transform:uppercase;color:{GOLD};}}
.spine-arrow{{align-self:center;color:{GOLD};font-size:16pt;font-weight:700;}}

/* Keep Care Never */
.kcn{{margin:1em 0 1.3em;page-break-inside:avoid;}}
.kcn-tier{{border-radius:7px;padding:.7em .95em;margin-bottom:.5em;display:flex;gap:1em;align-items:baseline;}}
.kcn-tier.keep{{background:{NAVY};color:{CREAM};}}
.kcn-tier.care{{background:{CREAM};color:{INK};border:1px solid {GOLD};}}
.kcn-tier.never{{background:#f3ede2;color:{INK};border:1px solid #b9432f;}}
.kcn-h{{font-family:'DM Sans';font-weight:600;letter-spacing:.14em;font-size:10.5pt;min-width:4.4em;flex-shrink:0;}}
.kcn-tier.keep .kcn-h{{color:{GOLD};}}
.kcn-tier.care .kcn-h{{color:{GOLD};}}
.kcn-tier.never .kcn-h{{color:#b9432f;}}
.kcn-b{{font-size:9.8pt;line-height:1.5;}}
.kcn-rule{{font-family:'Cormorant',serif;font-style:italic;font-size:12.5pt;color:{NAVY};text-align:center;margin-top:.55em;}}

/* Two doors */
.doors{{display:flex;gap:1em;margin:1em 0 1.3em;page-break-inside:avoid;}}
.door{{flex:1;background:{CREAM};border:1px solid #e0d7c4;border-top:3px solid {GOLD};border-radius:8px;padding:1em 1.05em 1.1em;}}
.door-k{{font-family:'DM Sans';font-weight:600;font-size:9pt;letter-spacing:.05em;text-transform:uppercase;color:{GOLD};margin-bottom:.15em;}}
.door-t{{font-family:'Cormorant',serif;font-weight:600;font-size:18pt;color:{NAVY};margin-bottom:.4em;}}
.door-b{{font-size:9.8pt;line-height:1.5;}}

/* Match your proof to a role */
.match-instr{{font-size:10.4pt;line-height:1.55;margin:0 0 .7em;}}
table.match{{width:100%;border-collapse:collapse;margin:.2em 0 1em;page-break-inside:avoid;font-family:'DM Sans',sans-serif;}}
table.match th{{background:{NAVY};color:{CREAM};font-weight:600;font-size:8.5pt;letter-spacing:.04em;text-align:left;padding:.5em .6em;vertical-align:top;}}
table.match td{{border:0.75px solid {HAIR};padding:.5em .6em;font-size:9.4pt;line-height:1.42;color:{INK};vertical-align:top;height:60px;}}
table.match tr.ex td{{background:#FBF3E2;}}
.pause{{display:inline-block;margin-left:.4em;font-family:'DM Sans';font-weight:600;font-size:7.5pt;letter-spacing:.06em;text-transform:uppercase;color:{RUST};white-space:nowrap;}}

/* Sub-headings (h3) */
h3{{font-family:'DM Sans',sans-serif;font-weight:600;font-size:11.5pt;letter-spacing:.01em;color:{NAVY};margin:1.15em 0 .3em;break-after:avoid;page-break-after:avoid;break-inside:avoid;}}

/* Chapter subtitle (under an opening-chapter h2) */
.chapter-sub{{font-family:'Cormorant',serif;font-style:italic;font-size:15pt;line-height:1.3;color:{GOLD};margin:-.1em 0 .8em;}}

/* Words to Stand On panel */
.words{{background:{CREAM};border:1px solid #e0d7c4;border-left:3px solid {GOLD};border-radius:8px;padding:1.05em 1.25em 1.15em;margin:1em 0 1.3em;page-break-inside:avoid;}}
.words-h{{font-family:'DM Sans';font-weight:600;font-size:9pt;letter-spacing:.14em;text-transform:uppercase;color:{GOLD};margin-bottom:.75em;}}
.wline{{font-family:'Cormorant',serif;font-size:14.5pt;line-height:1.35;color:{NAVY};padding:.34em 0;border-bottom:1px solid #ece3d2;}}
.wline:last-child{{border-bottom:0;}}
.wfill{{margin-top:.15em;}}
.wblank{{display:inline-block;min-width:9em;border-bottom:1px solid {GOLD};}}

/* Icons */
.h-ico{{display:inline-block;vertical-align:-0.16em;margin-right:.4em;}}
.h-ico svg{{display:inline-block;}}
.inl-ico{{display:inline-block;vertical-align:-0.18em;margin-right:.35em;}}
.li-ico{{display:inline-block;vertical-align:-0.14em;margin-right:.4em;}}
.pause-ico{{display:inline-block;vertical-align:-0.12em;margin-right:.25em;}}
.spine-ico-wrap{{margin-bottom:.35em;}}
.spine-step.focus .spine-ico path,.spine-step.focus .spine-ico line,.spine-step.focus .spine-ico polyline,.spine-step.focus .spine-ico circle{{}}
.kcn-ico-wrap{{flex-shrink:0;display:flex;align-items:center;}}
.door-ico-wrap{{margin-bottom:.5em;}}
.words-ico-wrap{{margin-bottom:.55em;}}

/* Cost table */
table.cost{{width:100%;border-collapse:collapse;margin:.4em 0 1em;page-break-inside:avoid;font-family:'DM Sans',sans-serif;}}
table.cost th{{background:{NAVY};color:{CREAM};font-weight:600;font-size:8.6pt;letter-spacing:.04em;text-align:left;padding:.55em .7em;vertical-align:top;}}
table.cost td{{border:0.75px solid {HAIR};padding:.55em .7em;font-size:9.5pt;line-height:1.42;color:{INK};vertical-align:top;}}
table.cost td.cost-m{{font-weight:600;color:{NAVY};width:22%;}}
table.cost td.cost-with{{background:#FBF3E2;}}
.cost-close{{font-family:'Cormorant',serif;font-style:italic;font-size:13.5pt;line-height:1.4;color:{NAVY};margin:.2em 0 .6em;}}

/* Fades diagram */
.fades{{margin:.6em 0 1.2em;page-break-inside:avoid;}}
.fades-title{{font-family:'Cormorant',serif;font-weight:600;font-size:14pt;color:{NAVY};margin:0 0 .35em;}}
.fades-svg{{width:100%;height:auto;}}
.fades-svg .axis{{stroke:{INK};stroke-width:1;opacity:.5;}}
.fades-svg .line-mem{{fill:none;stroke:{GOLD};stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round;}}
.fades-svg .line-rec{{fill:none;stroke:{NAVY};stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round;}}
.fades-svg .axis-lbl{{font-family:'DM Sans',sans-serif;font-size:9px;fill:{INK};opacity:.7;}}
.fades-svg .key{{font-family:'DM Sans',sans-serif;font-size:10px;font-weight:600;}}
.fades-svg .key-rec{{fill:{NAVY};}}
.fades-svg .key-mem{{fill:#9a7d2e;}}
.fades-svg .note{{font-family:'DM Sans',sans-serif;font-style:italic;font-size:8px;fill:{INK};opacity:.55;}}
.fades-cap{{font-size:9.8pt;line-height:1.5;color:{INK};margin:.1em 0 0;}}

/* Contents (table of contents) */
.toc-page{{page-break-before:always;page-break-after:always;padding-top:.3in;}}
.toc-title{{font-family:'Cormorant',serif;font-weight:600;font-size:30pt;color:{NAVY};margin:0 0 .5em;padding-bottom:.2em;border-bottom:2.5px solid {GOLD};}}
.toc-list{{margin-top:1.1em;}}
.toc-row{{display:flex;align-items:baseline;margin:0 0 .82em;font-family:'DM Sans',sans-serif;}}
.toc-label{{font-size:11.5pt;color:{NAVY};font-weight:500;white-space:nowrap;}}
.toc-dots{{flex:1;margin:0 .5em;border-bottom:1px dotted #b9bec8;transform:translateY(-0.2em);}}
.toc-num{{font-size:11pt;color:{INK};font-variant-numeric:tabular-nums;}}
.toc-row.toc-sub{{margin:-.22em 0 .82em 1.5em;}}
.toc-row.toc-sub .toc-label{{font-size:10pt;color:{INK};font-weight:400;}}
.toc-row.toc-sub .toc-num{{font-size:10pt;}}
'''

htmldoc = f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>Keep the Proof: Guided Handbook</title><style>{css}</style></head>
<body>{body_html}</body></html>'''

os.makedirs(os.path.dirname(OUT_HTML), exist_ok=True)
os.makedirs(os.path.dirname(OUT_PDF), exist_ok=True)
open(OUT_HTML,"w",encoding="utf-8").write(htmldoc)
print("HTML written:", OUT_HTML, len(htmldoc), "bytes")

# ---------- render PDF ----------
CHROME="/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
cmd=[CHROME,"--headless=new","--disable-gpu","--no-sandbox","--no-pdf-header-footer",
     f"--print-to-pdf={OUT_PDF}", f"file://{OUT_HTML}"]
r=subprocess.run(cmd,capture_output=True,text=True)
print("chrome rc",r.returncode)
if r.returncode!=0:
    print(r.stderr[-1500:])
print("PDF:", OUT_PDF, os.path.getsize(OUT_PDF) if os.path.exists(OUT_PDF) else "MISSING")
