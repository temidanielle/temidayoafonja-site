# -*- coding: utf-8 -*-
"""Re-render the Video 5 slide-preview PDF from the same HTML source the deck
was built from, WITHOUT rewriting either PPTX, then compare it page by page
against the published PDF to prove the visual deck is unchanged."""
import os, sys, shutil
B="/home/user/temidayoafonja-site/deliverables/video-5-slides/build"
sys.path.insert(0,B)
from deck import W,H,Canvas,render_html
import slides as S
CHROME="/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
TMP="/tmp/v5v3/_preview"; os.makedirs(TMP,exist_ok=True)
N=12
cvs=[]
for n in range(1,N+1):
    cv=Canvas(n,S.STEPS[n]); S.BUILDERS[n](cv,S.STEPS[n]); cvs.append(cv)
html=render_html(cvs, os.path.join(TMP,"deck.html"),
                 "Should I Make an Internal Move? 3 Questions to Decide")
new=os.path.join(TMP,"Video_5_Slide_Preview.pdf")
from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    b=pw.chromium.launch(executable_path=CHROME,args=["--no-sandbox"])
    pg=b.new_page(viewport={"width":W,"height":H},device_scale_factor=1)
    pg.goto("file://"+os.path.abspath(html),wait_until="load")
    pg.wait_for_timeout(600)
    pg.pdf(path=new,width="13.333in",height="7.5in",print_background=True,
           scale=0.66665,margin={"top":"0","bottom":"0","left":"0","right":"0"})
    b.close()

import pymupdf, hashlib
old="/home/user/temidayoafonja-site/deliverables/video-5-slides/out/Video_5_Slide_Preview.pdf"
a=pymupdf.open(old); c=pymupdf.open(new)
print("pages old/new:",a.page_count,c.page_count)
same=True
for i in range(max(a.page_count,c.page_count)):
    pa=a[i].get_pixmap(dpi=100).tobytes("png")
    pc=c[i].get_pixmap(dpi=100).tobytes("png")
    eq=hashlib.sha256(pa).hexdigest()==hashlib.sha256(pc).hexdigest()
    same &= eq
    if not eq: print("  page",i+1,"DIFFERS")
print("preview PDF pixel-identical to published file:",same)
