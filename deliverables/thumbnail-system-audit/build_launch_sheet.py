"""Three-video launch contact sheet and dark-mode feed simulation.

Shows only the selected launch thumbnails. No alternates, no archived tests.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE=os.path.dirname(os.path.abspath(__file__)); R=os.path.join(HERE,"..")
FD=os.path.expanduser("~/.fonts/")
CREAM=(250,247,241); NAVY=(15,35,70); GOLD=(201,168,76); DIM=(120,132,150)

def f(sz,w="Regular"): return ImageFont.truetype(FD+"MontserratTB-%s.ttf"%w,sz)
def tw(d,t,fo): b=d.textbbox((0,0),t,font=fo); return b[2]-b[0]
def wrap(d,t,fo,width,maxlines=2):
    words,lines,cur=t.split(),[],""
    for w_ in words:
        s=(cur+" "+w_).strip()
        if tw(d,s,fo)<=width: cur=s
        else:
            lines.append(cur); cur=w_
            if len(lines)==maxlines: break
    if cur and len(lines)<maxlines: lines.append(cur)
    return lines

V=[("VIDEO 1","DON'T START FROM ZERO","How to Change Jobs Without Starting Your Career Over",
    os.path.join(R,"video-1-slides/thumbnail/VIDEO_1_THUMBNAIL_OPTION_A_3840x2160.png")),
   ("VIDEO 2","YOUR SKILLS ARE STALLING","Is Your Job Making You Less Marketable?",
    os.path.join(R,"video-2-slides/thumbnail/VIDEO_2_THUMBNAIL_FINAL_3840x2160.png")),
   ("VIDEO 3","WAIT BEFORE YOU QUIT","3 Things to Do Before Quitting Your Job",
    os.path.join(R,"video-3-slides/thumbnail/VIDEO_3_THUMBNAIL_FINAL_A_3840x2160.png"))]
IM=[Image.open(p).convert("RGB") for *_,p in V]

# ------------------------------------------------- main launch contact sheet
SW,SH=3560,2400
s=Image.new("RGB",(SW,SH),CREAM); d=ImageDraw.Draw(s)
d.text((90,64),"THREE-VIDEO LAUNCH THUMBNAILS",font=f(62,"Bold"),fill=NAVY)
d.text((90,152),"The selected launch thumbnail for each video. No alternates, no archived tests. "
                "Every photograph is a verified original.",font=f(32),fill=DIM)
d.rectangle([90,232,SW-90,236],fill=GOLD)

# A — full size side by side
y=300
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

# B, C, D — stepped down
for label,px in (("B.  640 PX",640),("C.  360 PX",360),("D.  200 PX  (recommendation column)",200)):
    d.text((90,y),label,font=f(42,"Bold"),fill=NAVY); y+=70
    x=90
    for i in range(3):
        t=IM[i].resize((px,round(px*9/16)),Image.LANCZOS)
        s.paste(t,(x,y)); d.rectangle([x,y,x+px,y+t.height],outline=(214,204,186),width=2)
        x+=px+70
    y+=round(px*9/16)+80

d.text((90,SH-120),"Photographs: Video 1 uses photo-headshot-cream.png. Videos 2 and 3 use the "
       "verified caramel studio portrait. Nothing was generated, substituted or altered.",
       font=f(28),fill=DIM)
s.save(os.path.join(HERE,"LAUNCH_CONTACT_SHEET_three-video.png"))
print("contact sheet", s.size)

# ------------------------------------------------- E — dark mode feed
PW=1180
rows=[]
for i,(vn,words,title,_) in enumerate(V):
    t=IM[i].resize((PW-80,round((PW-80)*9/16)),Image.LANCZOS)
    rows.append((t,title))
FH=150+sum(t.height+230 for t,_ in rows)
c=Image.new("RGB",(PW,FH),(15,15,15)); d=ImageDraw.Draw(c)
d.text((40,52),"Home",font=f(40,"Bold"),fill=(241,241,241))
d.line([(0,124),(PW,124)],fill=(48,48,48))
y=160
for t,title in rows:
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

SW2=PW+180; SH2=FH+330
s2=Image.new("RGB",(SW2,SH2),(24,24,24)); d2=ImageDraw.Draw(s2)
d2.text((90,56),"E.  YOUTUBE DARK-MODE FEED",font=f(52,"Bold"),fill=(245,240,232))
d2.text((90,126),"All three launch thumbnails as they would sit together in one feed.",
        font=f(28),fill=(170,170,170))
d2.rectangle([90,186,SW2-90,190],fill=GOLD)
s2.paste(c,(90,225)); d2.rectangle([90,225,90+PW,225+FH],outline=(48,48,48),width=2)
d2.text((90,SH2-64),'"views", "date" and "--:--" are placeholders; no real figures exist yet.',
        font=f(24),fill=(150,150,150))
s2.save(os.path.join(HERE,"LAUNCH_DARK_MODE_FEED.png"))
print("dark feed", s2.size)

# ------------------------------------------------- 200 px comparison
c3=Image.new("RGB",(2200,760),CREAM); d3=ImageDraw.Draw(c3)
d3.text((70,54),"200 PX COMPARISON",font=f(52,"Bold"),fill=NAVY)
d3.text((70,122),"Native 200 px on top, the same pixels enlarged four times below.",
        font=f(28),fill=DIM)
d3.rectangle([70,180,2130,184],fill=GOLD)
for i,(vn,words,_,_) in enumerate(V):
    x=70+i*700; y=240
    sm=IM[i].resize((200,113),Image.LANCZOS)
    c3.paste(sm,(x,y)); d3.rectangle([x,y,x+200,y+113],outline=(214,204,186),width=2)
    c3.paste(sm.resize((640,362),Image.NEAREST),(x,y+150))
    d3.rectangle([x,y+150,x+640,y+512],outline=(214,204,186),width=2)
    d3.text((x,y+532),vn,font=f(32,"Bold"),fill=GOLD)
    d3.text((x,y+576),words,font=f(30,"Bold"),fill=NAVY)
c3.save(os.path.join(HERE,"LAUNCH_COMPARISON_200px.png"))
print("200px comparison", c3.size)
