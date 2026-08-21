#!/usr/bin/env python3
"""Multi-engine page QA: render every page through PyMuPDF, Poppler (whole-doc
and isolated) and Ghostscript, and flag blank pages and renderer-dependent
divergence. Usage: qa_multiengine.py <pdf> <outdir>"""
import sys, os, subprocess, fitz
from PIL import Image
import numpy as np

PDF, OUTD = sys.argv[1], sys.argv[2]
os.makedirs(OUTD, exist_ok=True)
DPI = 110
d = fitz.open(PDF); N = d.page_count

for i in range(N):
    fitz.open(PDF)[i].get_pixmap(dpi=DPI).save(f"{OUTD}/pymupdf-{i+1:03d}.png")
subprocess.run(["pdftoppm","-r",str(DPI),"-png",PDF,f"{OUTD}/popwhole"], check=True, capture_output=True)
for i in range(N):
    subprocess.run(["pdftoppm","-r",str(DPI),"-png","-f",str(i+1),"-l",str(i+1),"-singlefile",
                    PDF,f"{OUTD}/popiso-{i+1:03d}"], check=True, capture_output=True)
subprocess.run(["gs","-q","-dNOPAUSE","-dBATCH","-sDEVICE=png16m",f"-r{DPI}",
                f"-sOutputFile={OUTD}/gs-%03d.png", PDF], check=True, capture_output=True)

def arr(f):
    return np.asarray(Image.open(f).convert("L")).astype(int)
def ink(a):  # % pixels differing from modal background
    bg = np.bincount(a.ravel()).argmax()
    return round(100*float((np.abs(a-bg)>25).mean()),2)

def norm(f, w, h):
    return np.asarray(Image.open(f).convert("L").resize((w,h))).astype(int)

print(f"== {PDF.split('/')[-1]} : {N} pages ==")
print("pg | ink% pymu/pop/gs | pop whole-vs-iso | pymu-vs-pop | pymu-vs-gs | flags")
blanks=[]; diverge=[]
for i in range(N):
    n=i+1
    fp=f"{OUTD}/pymupdf-{n:03d}.png"
    pw=f"{OUTD}/popwhole-{n:02d}.png" if os.path.exists(f"{OUTD}/popwhole-{n:02d}.png") else f"{OUTD}/popwhole-{n:03d}.png"
    pi=f"{OUTD}/popiso-{n:03d}.png"
    gf=f"{OUTD}/gs-{n:03d}.png"
    a_p=arr(fp); a_pw=arr(pw); a_pi=arr(pi); a_g=arr(gf)
    ink_p, ink_pw, ink_g = ink(a_p), ink(a_pw), ink(a_g)
    W=min(a_p.shape[1],a_pw.shape[1],a_pi.shape[1],a_g.shape[1])
    H=min(a_p.shape[0],a_pw.shape[0],a_pi.shape[0],a_g.shape[0])
    P=norm(fp,W,H); PW=norm(pw,W,H); PI=norm(pi,W,H); G=norm(gf,W,H)
    d_wi=round(float(np.abs(PW-PI).mean()),3)
    d_pp=round(float(np.abs(P-PW).mean()),2)
    d_pg=round(float(np.abs(P-G).mean()),2)
    flags=[]
    if min(ink_p,ink_pw,ink_g) < 0.4: flags.append("BLANK?"); blanks.append(n)
    if d_wi > 0.5: flags.append("WHOLE!=ISO"); diverge.append(n)
    if d_pp > 8 or d_pg > 8: flags.append("ENGINE-DIVERGE"); diverge.append(n)
    print(f"{n:3d} | {ink_p:5}/{ink_pw:5}/{ink_g:5} | {d_wi:6} | {d_pp:5} | {d_pg:5} | {' '.join(flags)}")
print(f"\nblank-suspect pages: {blanks or 'none'}")
print(f"divergent pages: {sorted(set(diverge)) or 'none'}")
sys.exit(1 if (blanks or diverge) else 0)
