#!/usr/bin/env python3
"""Build the Keep the Proof V2 Guided Handbook: markdown -> designed HTML -> PDF.
Applies the Keep the Proof / Capability Formation visual identity."""
import re, html, subprocess, sys, os

ROOT = "/home/user/temidayoafonja-site"
SRC = f"{ROOT}/_build/keep-the-proof-v2/production/FINAL_MANUSCRIPT.md"
OUT_HTML = f"{ROOT}/_build/keep-the-proof-v2/production/renders/handbook.html"
OUT_PDF = f"{ROOT}/_build/keep-the-proof-v2/production/bundle/02_KEEP_THE_PROOF_GUIDED_HANDBOOK.pdf"
FONTS = f"file://{ROOT}/fonts"

NAVY = "#112345"
CREAM = "#F5F1E8"
GOLD = "#C9A84C"
YELLOW = "#F2C44C"
PAGEBG = "#FFFFFF"
INK = "#1c2333"

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
    return f'''
<div class="spine">
  <div class="spine-step"><div class="spine-n">01</div><div class="spine-t">CAPTURE</div><div class="spine-q">What actually happened?</div></div>
  <div class="spine-arrow">&rarr;</div>
  <div class="spine-step focus"><div class="spine-n">02</div><div class="spine-t">CLARIFY</div><div class="spine-q">What was actually yours?</div><div class="spine-tag">the heart of the system</div></div>
  <div class="spine-arrow">&rarr;</div>
  <div class="spine-step"><div class="spine-n">03</div><div class="spine-t">CARRY</div><div class="spine-q">What can you responsibly take forward?</div></div>
</div>'''

def kcn_device():
    return f'''
<div class="kcn">
  <div class="kcn-tier keep"><div class="kcn-h">KEEP</div><div class="kcn-b">Your own high-level recollection: what you did, decisions you made, problems you helped prevent, publicly disclosed outcomes, and anything your employer has expressly permitted you to retain.</div></div>
  <div class="kcn-tier care"><div class="kcn-h">CARE</div><div class="kcn-b">Numbers, client or project detail, and internal context that may be sensitive. Seek permission, use only what is already public, or leave it out. When unsure, treat it as the next tier.</div></div>
  <div class="kcn-tier never"><div class="kcn-h">NEVER</div><div class="kcn-b">Source code, credentials, security settings, customer or employee data, unreleased product detail, internal financials, privileged or legal material, trade secrets, and any file your employer owns. Never copy, forward, screenshot, download, or reconstruct these anywhere.</div></div>
  <div class="kcn-rule">Default downward. Between Keep and Care, treat as Care. Between Care and Never, treat as Never.</div>
</div>'''

def doors_device():
    return f'''
<div class="doors">
  <div class="door"><div class="door-k">Capturing now?</div><div class="door-t">Start here</div><div class="door-b">You still have your access, your systems, and your memory of recent work &mdash; the best possible position, because you can capture the record while the facts are fresh. Begin with Your First 60 Minutes, then let the habit carry it forward.</div></div>
  <div class="door"><div class="door-k">Already lost access?</div><div class="door-t">Start here</div><div class="door-b">The change has already happened, and the record you wish you had does not exist yet. You have not failed, and you did not buy the wrong guide. You simply start differently, by rebuilding from what is still yours. Turn to Part Seven, Reconstruct.</div></div>
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
        body.append(f'<h2>{esc(payload)}</h2>')
        if payload in INJECT_AFTER_H2:
            body.append(INJECT_AFTER_H2[payload]())
        continue
    if kind=="ul":
        flush_caption_as_para()
        lis = "".join(f'<li>{esc(it)}</li>' for it in payload)
        body.append(f'<ul>{lis}</ul>')
        continue
    if kind=="p":
        text = payload
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
                body.append(f'<p>{esc(text)}</p>')
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

@page{{size:8.5in 11in;margin:0.95in 1.05in 0.9in 1.05in;}}
@page bleed{{size:8.5in 11in;margin:0;}}
*{{box-sizing:border-box;}}
html,body{{margin:0;padding:0;background:{PAGEBG};}}
body{{font-family:'DM Sans',sans-serif;font-weight:400;font-size:10.8pt;line-height:1.62;color:{INK};background:{PAGEBG};-webkit-print-color-adjust:exact;print-color-adjust:exact;}}

h2{{font-family:'Cormorant',serif;font-weight:600;font-size:20pt;line-height:1.12;color:{NAVY};margin:1.5em 0 0.15em;padding-top:0.2em;}}
h2::after{{content:"";display:block;width:2.2em;height:2.5px;background:{GOLD};margin-top:.32em;}}
p{{margin:0 0 0.72em;orphans:2;widows:2;}}
h2{{break-after:avoid;}}
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
'''

htmldoc = f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>Keep the Proof — Guided Handbook</title><style>{css}</style></head>
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
