#!/usr/bin/env python3
import os, re
import pypdfium2 as pdfium
from docx import Document

ROOT="/home/user/temidayoafonja-site"
BUN=f"{ROOT}/_build/keep-the-proof-v2/production/bundle"
SRC=f"{ROOT}/_build/keep-the-proof-v2/production"

ARTIFACT=re.compile(r'(?i)(legal review required|> ?visual:|stage 2|wording withheld|pending counsel|by counsel|counsel confirms|not reader-facing|build stage|end of manuscript|end of professional record)')
STALE=re.compile(r'(?i)(60[- ]?minute career evidence|career evidence ledger|career evidence system|reusable ledger)')
OWNER=re.compile(r'(?i)(\blawful\b|yours to keep|not yours\b|account is yours|belongs only to you|belongs to you|format you own|you own and control)')
BRACKET=re.compile(r'\[[^\]]{3,}\]')
# copy-proof
DOUBLE_PUNCT=re.compile(r'([?!]\.|\?\?|!!|,,|;;|::|\.\,|\,\.| \.| \,)')
DUP_WORD=re.compile(r'\b(\w+)\s+\1\b', re.IGNORECASE)
MOJIBAKE=re.compile(r'(Ã|Â|â€|�| Â)')
DOUBLE_SPACE=re.compile(r'\S  +\S')

def pdf_text(p):
    return "\n".join((pg.get_textpage().get_text_range() or "") for pg in pdfium.PdfDocument(p))

DUP_OK={'that','had','the','a','is','s','out','do','go','no','so','to','on','in'}  # allow legit repeats like "had had"? none expected
def proof(name, text):
    issues={}
    for label,pat in [("ARTIFACT",ARTIFACT),("STALE",STALE),("OWNERSHIP",OWNER),("BRACKET",BRACKET),("MOJIBAKE",MOJIBAKE)]:
        hits=set(m.group(0) for m in pat.finditer(text))
        if label=="BRACKET": hits={h for h in hits if not re.match(r'\[(x| |\d+)\]',h)}
        if hits: issues[label]=hits
    # double punctuation - show context
    dp=[]
    for m in DOUBLE_PUNCT.finditer(text):
        ctx=text[max(0,m.start()-25):m.end()+15].replace("\n"," ")
        dp.append(ctx)
    if dp: issues["DOUBLE_PUNCT"]=dp[:8]
    # duplicated words - filter false positives
    dups=[]
    for m in DUP_WORD.finditer(text):
        w=m.group(1).lower()
        ctx=text[max(0,m.start()-20):m.end()+20].replace("\n"," ")
        # skip numerals and known-ok
        if w.isdigit(): continue
        dups.append(ctx)
    if dups: issues["DUP_WORD"]=dups[:8]
    status="PASS" if not issues else "FLAG"
    print(f"[{status}] {name}")
    for k,v in issues.items():
        print(f"    {k}: {list(v)[:8]}")
    return not issues

print("="*60); print("CUSTOMER FILES — FULL PROOF"); print("="*60)
ok=True
for f in ["01_START_HERE.pdf","02_KEEP_THE_PROOF_GUIDED_HANDBOOK.pdf","04_PRINTABLE_FILLABLE_TOOLS.pdf"]:
    ok &= proof(f, pdf_text(f"{BUN}/{f}"))
d=Document(f"{BUN}/03_YOUR_PROFESSIONAL_RECORD.docx")
docx_text="\n".join(p.text for p in d.paragraphs)+"\n"+"\n".join(c.text for t in d.tables for r in t.rows for c in r.cells)
ok &= proof("03_YOUR_PROFESSIONAL_RECORD.docx", docx_text)

print()
print("="*60); print("SOURCE MANUSCRIPT (for record)"); print("="*60)
ok &= proof("FINAL_MANUSCRIPT.md", open(f"{SRC}/FINAL_MANUSCRIPT.md").read())
ok &= proof("source/03_...RECORD.md (internal)", open(f"{SRC}/source/03_YOUR_PROFESSIONAL_RECORD.md").read())

print()
print("="*60); print("BUNDLE STRUCTURE"); print("="*60)
files=sorted(os.listdir(BUN))
print("  bundle files:", files)
print("  exactly 4 files:", len(files)==4)
print("  no .md in bundle:", not any(x.endswith('.md') for x in files))
print("  .md internal present:", os.path.exists(f"{SRC}/source/03_YOUR_PROFESSIONAL_RECORD.md"))

print()
print("="*60); print("WEBSITE"); print("="*60)
ktp=open(f"{ROOT}/keep-the-proof.html").read()
print("  stale descriptors:", "NONE" if not STALE.search(ktp) else STALE.findall(ktp))
print("  ownership phrases:", "NONE" if not OWNER.search(ktp) else set(OWNER.findall(ktp)))
print("  .md/plain-text mention:", "NONE" if not re.search(r'(?i)\.md|plain-text|plain text', ktp) else "FOUND")
print("  gumroad CTAs:", ktp.count("temidayoafonja.gumroad.com/l/keep-the-proof"))
print("  $75 present:", "$75" in ktp, "| stale $49:", "$49" in ktp)

print()
print("OVERALL:", "ALL PASS" if ok else "FLAGS PRESENT")
