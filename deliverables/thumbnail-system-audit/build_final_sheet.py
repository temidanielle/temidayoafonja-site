"""Final three-video launch contact sheet. Sections A to E on one sheet.

Shows only the current launch candidates. Nothing is redesigned or overwritten.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE=os.path.dirname(os.path.abspath(__file__)); R=os.path.join(HERE,"..")
FD=os.path.expanduser("~/.fonts/")
CREAM=(250,247,241); NAVY=(15,35,70); GOLD=(201,168,76); DIM=(120,132,150)
def f(s,w="Regular"): return ImageFont.truetype(FD+"MontserratTB-%s.ttf"%w,s)
def tw(d,t,fo): b=d.textbbox((0,0),t,font=fo); return b[2]-b[0]
def wrap(d,t,fo,width,ml=2):
    words,lines,cur=t.split(),[],""
    for w_ in words:
        s=(cur+" "+w_).strip()
        if tw(d,s,fo)<=width: cur=s
        else:
            lines.append(cur); cur=w_
            if len(lines)==ml: break
    if cur and len(lines)<ml: lines.append(cur)
    return lines

V=[("VIDEO 1","DON'T START FROM ZERO","How to Change Jobs Without Starting Your Career Over",
    R+"/video-1-slides/thumbnail/VIDEO_1_THUMBNAIL_OPTION_A_3840x2160.png"),
   ("VIDEO 2","YOUR SKILLS ARE STALLING","Is Your Job Making You Less Marketable?",
    R+"/video-2-slides/thumbnail/VIDEO_2_THUMBNAIL_FINAL_3840x2160.png"),
   ("VIDEO 3","WAIT BEFORE YOU QUIT","3 Things to Do Before Quitting Your Job",
    R+"/video-3-slides/thumbnail/VIDEO_3_THUMBNAIL_FINAL_A_3840x2160.png")]
IM=[Image.open(p).convert("RGB") for *_,p in V]

# ---- E panel: dark mode feed, built first so we know its height
PW=1180
c=Image.new("RGB",(PW,150+sum(round((PW-80)*9/16)+230 for _ in V)),(15,15,15))
d=ImageDraw.Draw(c)
d.text((40,52),"Home",font=f(40,"Bold"),fill=(241,241,241))
d.line([(0,124),(PW,124)],fill=(48,48,48))
y=160
for i,(vn,words,title,_) in enumerate(V):
    t=IM[i].resize((PW-80,round((PW-80)*9/16)),Image.LANCZOS)
    c.paste(t,(40,y))
    d.rounded_rectangle([PW-190,y+t.height-58,PW-58,y+t.height-16],8,fill=(0,0,0))
    d.text((PW-178,y+t.height-52),"--:--",font=f(25,"Bold"),fill=(255,255,255))
    yy=y+t.height+30
    d.ellipse([40,yy+6,136,yy+102],fill=(200,178,140))
    fo=f(33,"Bold")
    for j,l in enumerate(wrap(d,title,fo,PW-230)):
        d.text((164,yy+6+j*44),l,font=fo,fill=(241,241,241))
    d.text((164,yy+104),"Temidayo Afonja  ·  views  ·  date",font=f(27),fill=(170,170,170))
    y+=t.height+230
FEED=c

SW=3560
SH=300+596+240+ (360+90) + (round(360*9/16)+90) + (round(200*9/16)+120) + FEED.height+470
s=Image.new("RGB",(SW,SH),CREAM); d=ImageDraw.Draw(s)
d.text((90,64),"THREE-VIDEO LAUNCH THUMBNAILS — FINAL COHERENCE CHECK",font=f(58,"Bold"),fill=NAVY)
d.text((90,150),"Current launch candidates only. No alternates, no archived tests, nothing redesigned.",
       font=f(32),fill=DIM)
d.rectangle([90,228,SW-90,232],fill=GOLD)

y=296
d.text((90,y),"A.  FULL SIZE",font=f(42,"Bold"),fill=NAVY); y+=76
tw_,th_=1060,596
for i,(vn,words,title,_) in enumerate(V):
    x=90+i*(tw_+110)
    s.paste(IM[i].resize((tw_,th_),Image.LANCZOS),(x,y))
    d.rectangle([x,y,x+tw_,y+th_],outline=(214,204,186),width=3)
    d.text((x,y+th_+22),vn,font=f(34,"Bold"),fill=GOLD)
    d.text((x,y+th_+68),words,font=f(36,"Bold"),fill=NAVY)
    for j,l in enumerate(wrap(d,title,f(26),tw_)):
        d.text((x,y+th_+120+j*36),l,font=f(26),fill=DIM)
y+=th_+210

for label,px in (("B.  640 PX",640),("C.  360 PX",360),
                 ("D.  200 PX   — recommendation column, the one that matters most",200)):
    d.text((90,y),label,font=f(42,"Bold"),fill=NAVY); y+=70
    x=90
    for i in range(3):
        t=IM[i].resize((px,round(px*9/16)),Image.LANCZOS)
        s.paste(t,(x,y)); d.rectangle([x,y,x+px,y+t.height],outline=(214,204,186),width=2)
        x+=px+70
    y+=round(px*9/16)+ (110 if px==200 else 80)

d.text((90,y),"E.  YOUTUBE DARK-MODE HOME FEED",font=f(42,"Bold"),fill=NAVY); y+=76
s.paste(FEED,(90,y)); d.rectangle([90,y,90+FEED.width,y+FEED.height],outline=(200,190,175),width=3)
d.text((90+FEED.width+70,y+20),'All three in one feed. "views", "date" and "--:--"',font=f(28),fill=DIM)
d.text((90+FEED.width+70,y+62),'are placeholders; no real figures exist yet.',font=f(28),fill=DIM)
d.text((90+FEED.width+70,y+140),'Note the alternation:',font=f(30,"Bold"),fill=NAVY)
for j,t in enumerate(["Video 1  navy left, portrait right",
                      "Video 2  portrait left, navy right",
                      "Video 3  cream left, portrait right"]):
    d.text((90+FEED.width+70,y+190+j*46),t,font=f(27),fill=DIM)
y+=FEED.height+70

d.text((90,SH-90),"Photographs: Video 1 uses photo-headshot-cream.png. Videos 2 and 3 both use the "
       "verified caramel studio portrait. Nothing generated, substituted or altered.",
       font=f(28),fill=DIM)
s.save(os.path.join(HERE,"FINAL_LAUNCH_CONTACT_SHEET.png"))
print("final sheet",s.size)
FEED_SHEET=Image.new("RGB",(FEED.width+180,FEED.height+250),(24,24,24))
dd=ImageDraw.Draw(FEED_SHEET)
dd.text((90,56),"YOUTUBE DARK-MODE FEED",font=f(52,"Bold"),fill=(245,240,232))
dd.rectangle([90,140,FEED.width+90,144],fill=GOLD)
FEED_SHEET.paste(FEED,(90,180))
dd.text((90,FEED.height+205),'"views", "date" and "--:--" are placeholders.',font=f(24),fill=(150,150,150))
FEED_SHEET.save(os.path.join(HERE,"FINAL_DARK_MODE_FEED.png"))
print("dark feed",FEED_SHEET.size)
