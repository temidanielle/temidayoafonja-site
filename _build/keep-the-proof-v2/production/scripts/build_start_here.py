#!/usr/bin/env python3
"""Build 01_START_HERE.pdf: the orientation piece and bundle map."""
import subprocess, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import icons as I
ROOT="/home/user/temidayoafonja-site"
FONTS=f"file://{ROOT}/fonts"
OUT_HTML=f"{ROOT}/_build/keep-the-proof-v2/production/renders/start_here.html"
OUT_PDF=f"{ROOT}/_build/keep-the-proof-v2/production/bundle/01_START_HERE.pdf"
NAVY="#112345"; CREAM="#F5F1E8"; GOLD="#C9A84C"; INK="#1c2333"; GREY="#5f636e"

FILES=[
 ("READ THIS FIRST","Start Here","This file. A two-minute orientation to the system and how the pieces fit together."),
 ("LEARN &amp; BUILD","Keep the Proof: Guided Handbook","The 55-page teaching guide. It opens with Before You Rebuild Anything, teaches you how to capture your work, clarify what was yours, and carry it forward in language anyone can follow, and closes with Put Your Record to Work. A completed example sits beside every tool."),
 ("KEEP USING","Your Professional Record","Your long-term working document, in an editable, copyable format you keep and control (Word, Google Docs, or Pages). Make one personal copy, keep it in a personally controlled account, and add to it over time. This is where the record lives for years."),
 ("PREFER PRINT OR A FORM?","Printable &amp; Fillable Tools","Eleven form pages holding the same fields as your Professional Record, for anyone who would rather write by hand or type into a form. Use whichever you will keep up. You do not need to complete both."),
]

cards="".join(f'''<div class="fcard"><div class="fk">{k}</div><div class="ft">{t}</div><div class="fb">{b}</div></div>''' for k,t,b in FILES)

html=f'''<!doctype html><html><head><meta charset="utf-8"><title>Start Here</title><style>
@font-face{{font-family:'Cormorant';src:url('{FONTS}/CormorantGaramond-600-normal-latin-abcaa8.woff2') format('woff2');font-weight:600;}}
@font-face{{font-family:'Cormorant';src:url('{FONTS}/CormorantGaramond-400-italic-latin-4db21d.woff2') format('woff2');font-weight:400;font-style:italic;}}
@font-face{{font-family:'DM Sans';src:url('{FONTS}/DMSans-400-normal-latin-1c49a6.woff2') format('woff2');font-weight:400;}}
@font-face{{font-family:'DM Sans';src:url('{FONTS}/DMSans-500-normal-latin-1c49a6.woff2') format('woff2');font-weight:500;}}
@font-face{{font-family:'DM Sans';src:url('{FONTS}/DMSans-600-normal-latin-1c49a6.woff2') format('woff2');font-weight:600;}}
@page{{size:8.5in 11in;margin:0;}}
*{{box-sizing:border-box;margin:0;padding:0;}}
html,body{{background:#fff;}}
body{{font-family:'DM Sans',sans-serif;color:{INK};font-size:10.4pt;line-height:1.32;}}
.hero{{background:{NAVY};color:{CREAM};padding:0.32in 0.85in 0.26in;}}
.mark{{font-family:'DM Sans';font-weight:500;letter-spacing:.34em;font-size:8pt;color:{GOLD};}}
.htitle{{font-family:'Cormorant',serif;font-weight:600;font-size:33pt;line-height:1;margin:.28em 0 .1em;color:{CREAM};}}
.hsub{{font-family:'Cormorant',serif;font-style:italic;font-size:15pt;color:#dcd4c3;}}
.wrap{{padding:0.2in 0.85in 0.26in;}}
.lead{{font-size:10.4pt;line-height:1.4;margin-bottom:.3em;}}
.rule-box{{background:{CREAM};border-left:3px solid {GOLD};border-radius:6px;padding:.44em .9em;margin:.38em 0 .48em;}}
.rule-box .rk{{font-family:'DM Sans';font-weight:600;font-size:8.5pt;letter-spacing:.08em;text-transform:uppercase;color:{GOLD};margin-bottom:.2em;}}
.rule-box .rt{{font-size:10.2pt;line-height:1.4;}}
.sh{{font-family:'Cormorant',serif;font-weight:600;font-size:14.5pt;color:{NAVY};margin:.1em 0 .04em;}}
.sh::after{{content:"";display:block;width:2em;height:2.5px;background:{GOLD};margin:.18em 0 .36em;}}
.fcard{{border:1px solid #e4dccb;border-top:3px solid {GOLD};border-radius:8px;padding:.36em .9em .42em;margin-bottom:.26em;page-break-inside:avoid;}}
.fk{{font-family:'DM Sans';font-weight:600;font-size:8pt;letter-spacing:.09em;color:{GOLD};margin-bottom:.12em;}}
.ft{{font-family:'Cormorant',serif;font-weight:600;font-size:14pt;color:{NAVY};line-height:1.05;margin-bottom:.2em;}}
.fb{{font-size:9.4pt;line-height:1.4;color:{INK};}}
.begin{{margin-top:.3em;}}
.foot{{font-size:7.9pt;color:{GREY};line-height:1.36;margin-top:.35em;border-top:1px solid #e4dccb;padding-top:.35em;}}
.ib{{white-space:nowrap;}}
.ib-ico{{vertical-align:-0.12em;margin-right:.12em;}}
</style></head><body>
<div class="hero">
  <div class="mark">KEEP THE PROOF</div>
  <div class="htitle">Start Here</div>
  <div class="hsub">Welcome to Keep the Proof.</div>
</div>
<div class="wrap">
  <p class="lead">You did excellent work. This system helps you hold on to the truth of it. It keeps the judgment, the decisions, and what changed, in language a stranger can follow and in a way that respects the people you work for. It builds an honest, portable record of what you did.</p>
  <div class="rule-box"><div class="rk">The one rule that never bends</div><div class="rt">You record your own recollection and information you are permitted to retain. You never copy, forward, photograph, download, screenshot, or reconstruct material your employer owns. If permission is unclear, you leave it out and ask someone qualified. Everything in this system sits underneath that rule.</div></div>
  <div class="sh">What is in your bundle</div>
  {cards}
  <div class="begin"><div class="sh">How to begin</div>
  <p>Open the <strong>Guided Handbook</strong> and start with <strong>Your First 60 Minutes</strong>. In one focused session you will <span class="ib">{I.svg("capture", px=13, cls="ib-ico", label=True)}</span>capture a few pieces of work, <span class="ib">{I.svg("clarify", px=13, cls="ib-ico", label=True)}</span>clarify one in depth, and <span class="ib">{I.svg("proofline", px=13, cls="ib-ico", label=True)}</span>write your first portable sentence. It takes about an hour of focused time. Sixty minutes is a guide. Take it in one sitting or several, stopping after any step and picking up where you left off. If your access to past work has already closed, <span class="ib">{I.svg("reconstruct", px=13, cls="ib-ico", label=True)}</span>use the reconstruct version of that session in Part Seven. You start differently, and you are not behind. Then set up <strong>Your Professional Record</strong> as the place the record lives from here on.</p></div>
  <div class="foot">Keep the Proof is an educational guide to keeping a private, permitted record of your own work. It is not legal advice, and it cannot interpret your specific employment agreement, your confidentiality obligations, your employer&rsquo;s policies, or the laws that apply where you work. Where permission is unclear, leave the information out and ask someone qualified.<br>Copyright &copy; 2026 Temidayo Afonja &middot; The Density Group &middot; temidayoafonja.com &middot; Licensed for the personal use of the individual purchaser.</div>
</div>
</body></html>'''

os.makedirs(os.path.dirname(OUT_HTML),exist_ok=True)
os.makedirs(os.path.dirname(OUT_PDF),exist_ok=True)
open(OUT_HTML,"w",encoding="utf-8").write(html)
CHROME="/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
r=subprocess.run([CHROME,"--headless=new","--disable-gpu","--no-sandbox","--no-pdf-header-footer",
    f"--print-to-pdf={OUT_PDF}",f"file://{OUT_HTML}"],capture_output=True,text=True)
print("rc",r.returncode)
import pypdfium2 as pdfium
print("PDF",OUT_PDF,os.path.getsize(OUT_PDF),"pages",len(pdfium.PdfDocument(OUT_PDF)))
