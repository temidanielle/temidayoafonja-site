"""Video 3 — more-presence variants. Approved Final A is NOT touched.

Every variant uses a real, unmodified photograph. No gesture, pose, hand or
expression was generated, and none was borrowed from another image.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE=os.path.dirname(os.path.abspath(__file__))
U="/root/.claude/uploads/f121668d-e262-5eb8-9b22-0eaa1006a361/"
STUDIO=U+"a55ff6e1-D85AD998016A47539E6889F2988BF6B5.png"
SELFIE=U+"7b293c91-78BFE8B3F16F408A8ACE6572F92B19F0.jpeg"

W,H=3840,2160
CREAM=(245,240,232); NAVY=(15,35,70); GOLD=(201,168,76); GOLDD=(168,134,40)
FD=os.path.expanduser("~/.fonts/")
def f(s,w="ExtraBold"): return ImageFont.truetype(FD+"MontserratTB-%s.ttf"%w,s)
def mw(d,t,fo):
    b=d.textbbox((0,0),t,font=fo); return b[2]-b[0]
def fit(d,t,tw,st=470):
    s=st
    while s>40:
        fo=f(s)
        if mw(d,t,fo)<=tw: return fo,s
        s-=2
    return f(40),40

def place(canvas,src,box,cx,y0,y1):
    x0,y0b,x1,y1b=box; tw,th=x1-x0,y1b-y0b
    ch=y1-y0; cw=int(round(ch*tw/th))
    sx=max(0,min(int(round(cx-cw/2)),src.width-cw))
    canvas.paste(src.crop((sx,y0,sx+cw,y1)).resize((tw,th),Image.LANCZOS),(x0,y0b))
    return cw,ch,tw/cw

def layout(canvas, lines, sizes_start=460):
    d=ImageDraw.Draw(canvas)
    d.rectangle([2040,0,2058,H],fill=GOLD)
    col=2040-200-150; y=470
    for t in lines:
        fo,s=fit(d,t,col,sizes_start)
        d.text((200,y),t,font=fo,fill=NAVY); y+=int(s*1.02)
    d.rectangle([206,y+70,206+760,y+104],fill=GOLD)
    return d

REP=[]
# ---------------------------------------------- C: tighter crop, same layout
c=Image.new("RGB",(W,H),CREAM)
S=Image.open(STUDIO).convert("RGB")
cw,ch,sc=place(c,S,(2040,0,W,H),712,300,1210); REP.append(("Variant C",cw,ch,sc))
layout(c,["WAIT","BEFORE","YOU QUIT"])
c.save(os.path.join(HERE,"VIDEO_3_VARIANT_C_tighter-crop_3840x2160.png"))

# ---------------------------------------------- D: the caramel selfie
dd=Image.new("RGB",(W,H),CREAM)
SF=Image.open(SELFIE).convert("RGB")
cw,ch,sc=place(dd,SF,(2040,0,W,H),830,0,1536); REP.append(("Variant D",cw,ch,sc))
layout(dd,["WAIT","BEFORE","YOU QUIT"])
dd.save(os.path.join(HERE,"VIDEO_3_VARIANT_D_selfie_3840x2160.png"))

# ---------------------------------------------- E: the word does the telling
e=Image.new("RGB",(W,H),CREAM)
cw,ch,sc=place(e,S,(2040,0,W,H),712,300,1210); REP.append(("Variant E",cw,ch,sc))
d=ImageDraw.Draw(e)
d.rectangle([2040,0,2058,H],fill=GOLD)
col=2040-200-150
fo,s=fit(d,"WAIT",col,760)
y=330
d.text((200,y),"WAIT",font=fo,fill=NAVY); y+=int(s*0.98)
d.rectangle([206,y+34,206+col,y+70],fill=GOLD); y+=126
for t in ["BEFORE","YOU QUIT"]:
    fo2,s2=fit(d,t,col,300)
    d.text((200,y),t,font=fo2,fill=NAVY); y+=int(s2*1.04)
e.save(os.path.join(HERE,"VIDEO_3_VARIANT_E_wait-dominant_3840x2160.png"))

for n,cw,ch,sc in REP: print("%s: source crop %dx%d  upscale %.3fx"%(n,cw,ch,sc))
