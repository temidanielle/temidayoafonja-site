"""Derivatives and placement simulations. Video 1, both composition options.

Every simulation is a local mock of YouTube surface geometry. Where a real
surface would show a view count, an upload date or a duration, the literal
placeholders "views", "date" and "--:--" appear, because no real figures exist
for an unpublished video.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FD   = os.path.expanduser("~/.fonts/")
TITLE = "How to Change Jobs Without Starting Your Career Over"
CHAN  = "Temidayo Afonja"
ITEMS = [("a","VIDEO_1_THUMBNAIL_OPTION_A_3840x2160.png","Option A"),
         ("b","VIDEO_1_THUMBNAIL_OPTION_B_3840x2160.png","Option B")]

def f(sz,w="Regular"): return ImageFont.truetype(FD+"MontserratTB-%s.ttf"%w, sz)
def tw(d,t,fo): return d.textbbox((0,0),t,font=fo)[2]-d.textbbox((0,0),t,font=fo)[0]

def wrap(d,text,fo,width,maxlines=2):
    words,lines,cur = text.split(),[],""
    for w_ in words:
        t=(cur+" "+w_).strip()
        if tw(d,t,fo)<=width: cur=t
        else:
            lines.append(cur); cur=w_
            if len(lines)==maxlines: break
    if cur and len(lines)<maxlines: lines.append(cur)
    if len(lines)==maxlines and tw(d,lines[-1],fo)>width-40:
        while lines[-1] and tw(d,lines[-1]+"...",fo)>width: lines[-1]=lines[-1][:-1]
        lines[-1]+="..."
    return lines

manifest=[]
def note(fn,what):
    manifest.append((fn, os.path.getsize(os.path.join(HERE,fn)), what))

M={}
for key,fn,label in ITEMS:
    M[key]=Image.open(os.path.join(HERE,fn))
    note(fn,"%s master, lossless PNG, 3840 x 2160"%label)

# ---------------------------------------------------------- derivatives
for key,fn,label in ITEMS:
    im=M[key]; stem=fn.replace("_3840x2160.png","")
    hq=stem+"_3840x2160_q95.jpg"
    im.save(os.path.join(HERE,hq),"JPEG",quality=95,subsampling=0,optimize=True)
    note(hq,"%s high quality JPG, 4:4:4 chroma, quality 95"%label)

    up=stem+"_UPLOAD_1280x720.jpg"
    small=im.resize((1280,720),Image.LANCZOS); q=95
    while q>=60:
        small.save(os.path.join(HERE,up),"JPEG",quality=q,subsampling=0,
                   optimize=True,progressive=True)
        if os.path.getsize(os.path.join(HERE,up))<=2*1024*1024: break
        q-=3
    note(up,"%s YouTube upload file, 1280 x 720, quality %d, %.0f KB, under 2 MB"
         %(label,q,os.path.getsize(os.path.join(HERE,up))/1024))

    for px in (640,360,200):
        pf="preview-%s-%dpx.png"%(key,px)
        im.resize((px,round(px*9/16)),Image.LANCZOS).save(os.path.join(HERE,pf))
        note(pf,"%s legibility preview at %d px wide"%(label,px))

# ------------------------------------------------------------ surfaces
def theme(dark):
    return dict(bg=(15,15,15) if dark else (255,255,255),
                fg=(241,241,241) if dark else (15,15,15),
                mut=(170,170,170) if dark else (96,96,96),
                line=(48,48,48) if dark else (229,229,229))
def thumb(im,w): return im.resize((w,round(w*9/16)),Image.LANCZOS)

def mobile_feed(im,dark):
    T=theme(dark); PW=1080
    c=Image.new("RGB",(PW,980),T["bg"]); d=ImageDraw.Draw(c)
    d.text((40,46),"Home",font=f(38,"Bold"),fill=T["fg"])
    d.line([(0,120),(PW,120)],fill=T["line"])
    t=thumb(im,PW); c.paste(t,(0,150)); y=150+t.height
    d.rounded_rectangle([PW-152,y-56,PW-24,y-16],8,fill=(0,0,0))
    d.text((PW-140,y-50),"--:--",font=f(24,"Bold"),fill=(255,255,255))
    d.ellipse([32,y+34,128,y+130],fill=(200,178,140))
    fo=f(34,"Bold")
    for i,l in enumerate(wrap(d,TITLE,fo,PW-230)): d.text((156,y+34+i*46),l,font=fo,fill=T["fg"])
    d.text((156,y+140),CHAN+"  ·  views  ·  date",font=f(28),fill=T["mut"])
    return c

def search_row(im,dark):
    T=theme(dark); PW=1080
    c=Image.new("RGB",(PW,620),T["bg"]); d=ImageDraw.Draw(c)
    d.rounded_rectangle([32,34,PW-32,124],45,outline=T["line"],width=3)
    d.text((80,62),"changing careers without starting over",font=f(32),fill=T["mut"])
    t=thumb(im,470); c.paste(t,(32,180))
    d.rounded_rectangle([424,180+t.height-52,494,180+t.height-14],6,fill=(0,0,0))
    d.text((432,180+t.height-48),"--:--",font=f(20,"Bold"),fill=(255,255,255))
    fo=f(32,"Bold")
    for i,l in enumerate(wrap(d,TITLE,fo,PW-560)): d.text((530,186+i*44),l,font=fo,fill=T["fg"])
    d.text((530,290),CHAN,font=f(26),fill=T["mut"])
    d.text((530,332),"views  ·  date",font=f(26),fill=T["mut"])
    return c

def right_column(im,dark):
    T=theme(dark); PW=820
    c=Image.new("RGB",(PW,730),T["bg"]); d=ImageDraw.Draw(c)
    d.text((28,26),"Up next",font=f(30,"Bold"),fill=T["fg"])
    for r in range(3):
        y=90+r*160; t=thumb(im,336)
        if r!=1: t=t.point(lambda v:int(v*0.45+128*0.55))
        c.paste(t,(28,y))
        fo=f(26,"Bold")
        for i,l in enumerate(wrap(d,TITLE,fo,PW-420)):
            d.text((392,y+4+i*36),l,font=fo,fill=T["fg"] if r==1 else T["mut"])
        d.text((392,y+92),CHAN,font=f(23),fill=T["mut"])
    d.text((28,668),"middle row is this thumbnail; rows above and below are dimmed placeholders",
           font=f(19),fill=T["mut"])
    return c

NAVY=(15,35,70); DIMC=(120,132,150); GOLDC=(201,168,76)
for key,fn,label in ITEMS:
    im=M[key]
    for dark in (False,True):
        tag="dark" if dark else "light"
        panels=[("Mobile home feed",mobile_feed(im,dark)),
                ("Mobile search results",search_row(im,dark)),
                ("Desktop right column",right_column(im,dark))]
        gap,pad=60,70
        SW=pad*2+sum(p.width for _,p in panels)+gap*(len(panels)-1)
        SH=pad+150+max(p.height for _,p in panels)+90
        T=theme(dark)
        s=Image.new("RGB",(SW,SH),(24,24,24) if dark else (250,247,241)); d=ImageDraw.Draw(s)
        head=(245,240,232) if dark else NAVY
        d.text((pad,50),"%s — PLACEMENT SIMULATIONS — %s MODE"%(label.upper(),tag.upper()),
               font=f(46,"Bold"),fill=head)
        d.rectangle([pad,120,SW-pad,124],fill=GOLDC)
        x=pad
        for lb,p in panels:
            s.paste(p,(x,190)); d.rectangle([x,190,x+p.width,190+p.height],outline=T["line"],width=2)
            d.text((x,150),lb,font=f(30,"Bold"),fill=head); x+=p.width+gap
        d.text((pad,SH-60),'Surface geometry is mocked locally. "views", "date" and "--:--" are '
               'placeholders; no real figures exist for an unpublished video.',
               font=f(24),fill=(150,150,150) if dark else DIMC)
        pf="placement-%s-%s.png"%(key,tag)
        s.save(os.path.join(HERE,pf))
        note(pf,"%s on mobile feed, mobile search and desktop right column, %s mode"%(label,tag))

for fn,sz,what in manifest:
    print("%-56s %8.1f KB  %s"%(fn,sz/1024,what))
