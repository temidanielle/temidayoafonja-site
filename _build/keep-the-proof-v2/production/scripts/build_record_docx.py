#!/usr/bin/env python3
"""Build 03_YOUR_PROFESSIONAL_RECORD.docx (primary copyable working document)
and 03_YOUR_PROFESSIONAL_RECORD.md (portable plain-text mirror)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import record_model as M

from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

ROOT = "/home/user/temidayoafonja-site"
OUT_DOCX = f"{ROOT}/_build/keep-the-proof-v2/production/bundle/03_YOUR_PROFESSIONAL_RECORD.docx"
OUT_MD = f"{ROOT}/_build/keep-the-proof-v2/production/bundle/03_YOUR_PROFESSIONAL_RECORD.md"

NAVY = RGBColor(0x11, 0x23, 0x45)
GOLD = RGBColor(0xA8, 0x86, 0x2E)   # slightly deeper gold for text legibility on white
GREY = RGBColor(0x6b, 0x70, 0x7d)
INK = RGBColor(0x1c, 0x23, 0x33)

doc = Document()
# base style
normal = doc.styles["Normal"]
normal.font.name = "Calibri"
normal.font.size = Pt(10.5)
normal.font.color.rgb = INK
normal.paragraph_format.space_after = Pt(6)
normal.paragraph_format.line_spacing = 1.15

for s in doc.sections:
    s.top_margin = Inches(0.9); s.bottom_margin = Inches(0.9)
    s.left_margin = Inches(1.0); s.right_margin = Inches(1.0)

def para(text="", size=10.5, bold=False, italic=False, color=INK, after=6, before=0, align=None):
    p = doc.add_paragraph()
    if align is not None: p.alignment = align
    p.paragraph_format.space_after = Pt(after); p.paragraph_format.space_before = Pt(before)
    if text:
        r = p.add_run(text); r.font.size = Pt(size); r.bold = bold; r.italic = italic
        r.font.color.rgb = color
    return p

def h_section(num, title):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(16); p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(f"Section {num}.  "); r.bold = True; r.font.size = Pt(14); r.font.color.rgb = GOLD
    r2 = p.add_run(title); r2.bold = True; r2.font.size = Pt(14); r2.font.color.rgb = NAVY
    _bottom_border(p, "C9A84C", 8)

def h_block(title, color=NAVY, size=11.5):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(10); p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(title); r.bold = True; r.font.size = Pt(size); r.font.color.rgb = color
    return p

def _bottom_border(p, hexcolor="BBBBBB", sz=6):
    pPr = p._p.get_or_add_pPr()
    pbdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single'); bottom.set(qn('w:sz'), str(sz))
    bottom.set(qn('w:space'), '2'); bottom.set(qn('w:color'), hexcolor)
    pbdr.append(bottom); pPr.append(pbdr)

def field(label, hint, lines):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(label); r.bold = True; r.font.size = Pt(10); r.font.color.rgb = NAVY
    if hint:
        rh = p.add_run("  " + hint); rh.italic = True; rh.font.size = Pt(8.5); rh.font.color.rgb = GREY
    for i in range(lines):
        lp = doc.add_paragraph(); lp.paragraph_format.space_before = Pt(9); lp.paragraph_format.space_after = Pt(0)
        _bottom_border(lp, "C9C4B7", 4)

def checkbox_line(text):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(3)
    r = p.add_run("☐  "); r.font.size = Pt(11); r.font.color.rgb = GOLD
    r2 = p.add_run(text); r2.font.size = Pt(10)

def bullet(text_bold, text):
    p = doc.add_paragraph(style=None); p.paragraph_format.left_indent = Inches(0.25)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run("•  "); r.font.color.rgb = GOLD; r.bold = True
    if text_bold:
        rb = p.add_run(text_bold + " "); rb.bold = True; rb.font.size = Pt(10); rb.font.color.rgb = NAVY
    rt = p.add_run(text); rt.font.size = Pt(10)

def divider():
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(6)

# ---------- Title ----------
tp = para(M.TITLE, size=26, bold=True, color=NAVY, after=2, align=WD_ALIGN_PARAGRAPH.LEFT)
tp.runs[0].font.name = "Cambria"
sp = para(M.SUBTITLE, size=13, italic=True, color=GOLD, after=10)
sp.runs[0].font.name = "Cambria"

para(M.INTRO_LEAD, after=8)
for b, t in M.INTRO_BULLETS:
    bullet(b, t)
para(M.INTRO_SECTIONS, before=4, after=6)
para(M.FORMATS_NOTE, italic=True, color=GREY, after=4)

# ---------- Section 1 ----------
h_section(1, "Capture Log")
para("Catch work the moment it happens, in two minutes, before the details soften. Fill one block per event; expand only the strongest into Full Entries. Duplicate the block below for each new capture.", after=6)
for n in range(1, 4):
    h_block(f"Capture {n}", color=GOLD, size=10.5)
    for label, hint, lines in M.CAPTURE_FIELDS:
        field(label, hint, lines)
    divider()
para("To add more, copy any Capture block above and paste it here.", italic=True, color=GREY)

# ---------- Section 2 ----------
h_section(2, "Full Entries")
para("For work worth keeping in depth, expand a capture into a full entry. Fill only the fields that apply; a strong entry with six good fields beats a padded one with sixteen. Duplicate the whole entry template for each new entry.", after=6)
for n in range(1, 3):
    h_block(f"Full Entry {n}", color=GOLD, size=11)
    for cluster_title, fields in M.FULL_ENTRY_CLUSTERS:
        h_block(cluster_title, color=NAVY, size=10.5)
        for label, hint, lines in fields:
            field(label, hint, lines)
    para(M.RECON_MARKER, italic=True, color=GREY, before=4, after=4)
    divider()
para("To add more, copy a Full Entry template above and paste it here.", italic=True, color=GREY)

# ---------- Section 3 ----------
h_section(3, "Corroboration list")
para("Keep, in one place, who could confirm your work while they still remember it. This is corroboration readiness, not networking: it records that a witness exists and what they saw. It does not decide any employer's choice.", after=6)
for n in range(1, 5):
    h_block(f"Corroboration {n}", color=GOLD, size=10.5)
    for label, hint, lines in M.CORROB_FIELDS:
        field(label, hint, lines)
    divider()
para(M.CORROB_NOTE, italic=True, color=GREY)

# ---------- Section 4 ----------
h_section(4, "Translation and Proof Line workspace")
para("Turn internal language into portable language, and build the portable sentence you can reuse.", after=6)
h_block("Translation worksheet", color=NAVY, size=10.5)
para("Work down the eight moves and apply the ones that fit, then the protection rule.", after=4)
for m in M.TRANSLATION_MOVES:
    checkbox_line(m)
para(M.TRANSLATION_PROTECTION, italic=True, color=GREY, before=2, after=8)
h_block("Proof Line builder", color=NAVY, size=10.5)
para("Combine, in whatever order reads well, up to five ingredients into one portable sentence.", after=4)
for label, hint, lines in M.PROOFLINE_INGREDIENTS:
    field(label, hint, lines)
para("Your Proof Line", size=10, bold=True, color=NAVY, before=6, after=1)
for i in range(2):
    lp = doc.add_paragraph(); lp.paragraph_format.space_before = Pt(9); _bottom_border(lp, "C9C4B7", 4)
para(M.PROOFLINE_RULE, italic=True, color=GREY, before=2, after=8)
h_block("Proof Lines kept", color=NAVY, size=10.5)
para("A running list of your finished Proof Lines, ready to pull for a review, a resume, or a conversation.", after=4)
for i in range(6):
    lp = doc.add_paragraph(); lp.paragraph_format.space_before = Pt(9); _bottom_border(lp, "C9C4B7", 4)

# ---------- Section 5 ----------
h_section(5, "Your index")
para("A running list of what you have, so any entry is a search away. Add a line whenever you add or revise an entry, and read it when a moment arrives and you need the right material fast.", after=6)
table = doc.add_table(rows=1, cols=len(M.INDEX_COLUMNS)); table.style = "Table Grid"
hdr = table.rows[0].cells
for i, c in enumerate(M.INDEX_COLUMNS):
    hdr[i].text = ""
    rp = hdr[i].paragraphs[0].add_run(c); rp.bold = True; rp.font.size = Pt(9); rp.font.color.rgb = NAVY
for _ in range(8):
    table.add_row()

# ---------- Section 6 ----------
h_section(6, "Optional maintenance checklists")
para("Two ways to keep the record current: capture when something worth keeping happens, and a light periodic sweep that catches what you missed. Neither is required, and neither is better; use whichever you will sustain, or both.", after=6)
h_block("Monthly sweep, about ten to fifteen minutes", color=NAVY, size=10.5)
for m in M.MONTHLY:
    checkbox_line(m)
h_block("Quarterly review, about thirty minutes", color=NAVY, size=10.5)
for q in M.QUARTERLY:
    checkbox_line(q)
para(M.MAINT_NOTE, italic=True, color=GREY, before=6)

os.makedirs(os.path.dirname(OUT_DOCX), exist_ok=True)
doc.save(OUT_DOCX)
print("DOCX:", OUT_DOCX, os.path.getsize(OUT_DOCX), "bytes")

# ================= Markdown mirror =================
md = []
md.append(f"# {M.TITLE}")
md.append(f"*{M.SUBTITLE}*\n")
md.append(M.INTRO_LEAD + "\n")
for b, t in M.INTRO_BULLETS:
    md.append(f"- **{b}** {t}")
md.append("")
md.append(M.INTRO_SECTIONS + "\n")
md.append("*" + M.FORMATS_NOTE + "*\n")
md.append("---\n")

def md_field(label, hint, lines):
    h = f"  _{hint}_" if hint else ""
    md.append(f"**{label}.**{h}")
    md.append("`__________________________________________________________________`")
    if lines > 1:
        md.append("`__________________________________________________________________`")
    md.append("")

md.append("## Section 1. Capture Log\n")
md.append("Catch work the moment it happens, in two minutes. Fill one block per event; expand only the strongest into Full Entries. Copy the block below for each new capture.\n")
for n in range(1,4):
    md.append(f"### Capture {n}\n")
    for label,hint,lines in M.CAPTURE_FIELDS: md_field(label,hint,lines)
    md.append("---\n")

md.append("## Section 2. Full Entries\n")
md.append("For work worth keeping in depth. Fill only the fields that apply. Copy the whole template for each new entry.\n")
for n in range(1,3):
    md.append(f"### Full Entry {n}\n")
    for ct,fields in M.FULL_ENTRY_CLUSTERS:
        md.append(f"**{ct}**\n")
        for label,hint,lines in fields: md_field(label,hint,lines)
    md.append(f"_{M.RECON_MARKER}_\n")
    md.append("---\n")

md.append("## Section 3. Corroboration list\n")
md.append("Who could confirm your work while they still remember it. Corroboration readiness, not networking.\n")
for n in range(1,5):
    md.append(f"### Corroboration {n}\n")
    for label,hint,lines in M.CORROB_FIELDS: md_field(label,hint,lines)
md.append(f"_{M.CORROB_NOTE}_\n")
md.append("---\n")

md.append("## Section 4. Translation and Proof Line workspace\n")
md.append("**Translation worksheet.** Work down the eight moves and apply the ones that fit, then the protection rule.\n")
for m in M.TRANSLATION_MOVES: md.append(f"- [ ] {m}")
md.append("")
md.append(f"_{M.TRANSLATION_PROTECTION}_\n")
md.append("**Proof Line builder.** Combine up to five ingredients into one portable sentence.\n")
for label,hint,lines in M.PROOFLINE_INGREDIENTS: md_field(label,hint,lines)
md.append("**Your Proof Line.**")
md.append("`__________________________________________________________________`\n")
md.append(f"_{M.PROOFLINE_RULE}_\n")
md.append("**Proof Lines kept.** A running list of your finished Proof Lines.\n")
for i in range(6): md.append("`__________________________________________________________________`")
md.append("\n---\n")

md.append("## Section 5. Your index\n")
md.append("A running list of what you have, so any entry is a search away.\n")
md.append("| " + " | ".join(M.INDEX_COLUMNS) + " |")
md.append("| " + " | ".join(["---"]*len(M.INDEX_COLUMNS)) + " |")
for _ in range(8):
    md.append("| " + " | ".join([" "]*len(M.INDEX_COLUMNS)) + " |")
md.append("\n---\n")

md.append("## Section 6. Optional maintenance checklists\n")
md.append("**Monthly sweep, about ten to fifteen minutes.**\n")
for m in M.MONTHLY: md.append(f"- [ ] {m}")
md.append("")
md.append("**Quarterly review, about thirty minutes.**\n")
for q in M.QUARTERLY: md.append(f"- [ ] {q}")
md.append("")
md.append(f"_{M.MAINT_NOTE}_")

open(OUT_MD,"w",encoding="utf-8").write("\n".join(md))
print("MD:", OUT_MD, os.path.getsize(OUT_MD), "bytes")
