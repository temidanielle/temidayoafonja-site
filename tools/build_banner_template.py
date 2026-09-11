import numpy as np, os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W,H = 2560,1440
CX,CY = W/2, H/2
SL,SR,ST,SB = 507.0, 2053.0, 508.5, 931.5
PAD = 50
SS  = 2                                   # supersample for vector art

CREAM      = (250,243,233)
CREAM_WARM = (245,232,217)
TAN_1      = (238,216,196)
TAN_2      = (228,198,173)
TAN_3      = (214,175,145)
LEAF_A     = (201,150,114)
LEAF_B     = (216,173,141)
INK        = (28,28,32)
BROWN      = (138,90,58)
TERRA      = (176,111,71)

PORTRAIT = os.environ.get('PORTRAIT_SRC','images/temidayo-terracotta.jpg')
CROPBOX  = tuple(int(v) for v in os.environ.get('PORTRAIT_CROP','454,180,1154,880').split(','))

def font(n,s): return ImageFont.truetype('ttf/'+n, s)
SCRIPT='DancingScript-700.ttf'; SERIF='CormorantGaramond-500.ttf'; SERIF6='CormorantGaramond-600.ttf'

# ───────────────── background washes ─────────────────
ys,xs = np.mgrid[0:H,0:W].astype(np.float32)
bg = np.broadcast_to(np.array(CREAM,float),(H,W,3)).astype(np.float32).copy()
def wash(cx,cy,rx,ry,amp,f,ph,soft):
    dx,dy=(xs-cx)/rx,(ys-cy)/ry
    r=np.sqrt(dx*dx+dy*dy)*(1+amp*np.sin(f*np.arctan2(dy,dx)+ph))
    return np.clip((1-r)/soft,0,1)[...,None]
bg += (np.array(CREAM_WARM,float)-bg)*wash(-60,1010,820,980,0.15,3,0.7,0.34)
bg += (np.array(TAN_1,float)     -bg)*wash(-190,1210,700,780,0.20,2,1.9,0.30)
bg += (np.array(TAN_2,float)     -bg)*wash(-300,1330,560,600,0.18,2,0.5,0.28)*0.9
bg += (np.array(CREAM_WARM,float)-bg)*wash(2640,380,840,960,0.17,3,2.4,0.34)
bg += (np.array(TAN_1,float)     -bg)*wash(2720,220,700,740,0.21,2,0.4,0.30)
bg += (np.array(TAN_2,float)     -bg)*wash(2700,1300,640,600,0.19,3,1.1,0.30)*0.9
bg += (np.array(TAN_1,float)     -bg)*wash(-140,120,600,520,0.18,3,2.8,0.32)*0.8
g=((np.random.default_rng(5).normal(0,1,(H,W))*40)+128).clip(0,255).astype(np.uint8)
g=np.asarray(Image.fromarray(g).filter(ImageFilter.GaussianBlur(0.7))).astype(np.float32)[...,None]
bg += (g-128)/128.0*1.5
img = Image.fromarray(np.clip(bg,0,255).astype(np.uint8),'RGB')

# ───────────────── botanical sprigs (drawn, kept outside the safe area) ─────────────────
art = Image.new('RGBA',(W*SS,H*SS),(0,0,0,0)); A = ImageDraw.Draw(art)
def bez(p0,p1,p2,n=60):
    return [((1-t)**2*p0[0]+2*(1-t)*t*p1[0]+t*t*p2[0],
             (1-t)**2*p0[1]+2*(1-t)*t*p1[1]+t*t*p2[1]) for t in (i/n for i in range(n+1))]

def leaf(cx,cy,L,Wd,ang,fill=None,outline=None,wid=3):
    """pointed oval leaf, tip along ang"""
    ca,sa = math.cos(ang), math.sin(ang)
    pts=[]
    for side in (1,-1):
        for i in range(21):
            t=i/20; u=t*L
            # half-width profile: 0 at base, max at 45%, 0 at tip
            hw = Wd*math.sin(math.pi*t)**0.85*side
            pts.append((cx+ (u*ca - hw*sa), cy+ (u*sa + hw*ca)))
        L,Wd = L,Wd
        pts = pts if side==1 else pts
    half=len(pts)//2
    poly = pts[:half] + pts[half:][::-1]
    poly=[(x*SS,y*SS) for x,y in poly]
    if fill:    A.polygon(poly, fill=fill)
    if outline: A.line(poly+[poly[0]], fill=outline, width=wid*SS, joint='curve')
    if fill or outline:   # centre vein
        A.line([(cx*SS,cy*SS),((cx+L*ca)*SS,(cy+L*sa)*SS)],
               fill=(outline or (255,255,255,90)), width=max(1,wid//2)*SS)

def sprig(p0,p1,p2,n,L0,W0,ang_off,fill,outline,taper=0.55,stem=4,flip=True):
    pts=bez(p0,p1,p2,80)
    A.line([(x*SS,y*SS) for x,y in pts], fill=(fill or outline), width=stem*SS, joint='curve')
    for i in range(n):
        t=0.10+0.82*i/max(1,n-1); k=int(t*80)
        x,y = pts[k]; x2,y2 = pts[min(80,k+2)]
        base = math.atan2(y2-y, x2-x)
        sc = 1-taper*t
        for s in ((1,-1) if flip else (1,)):
            leaf(x,y, L0*sc, W0*sc, base + s*ang_off, fill=fill, outline=outline)

# top-left sprig group
sprig((30,300),(210,180),(370,70), 7, 130, 30, 0.85, LEAF_A+(190,), None)
sprig((-30,230),(140,150),(300,20), 6, 105, 24, 0.95, LEAF_B+(165,), None)
sprig((60,360),(180,300),(330,250), 5,  85, 20, 1.05, LEAF_B+(140,), None)
for p in [(300,160),(330,205),(275,120),(355,255),(240,95)]:
    A.ellipse([(p[0]-5)*SS,(p[1]-5)*SS,(p[0]+5)*SS,(p[1]+5)*SS], fill=LEAF_A+(150,))
# right-hand sprig group (outlined, like the reference)
sprig((2555,760),(2330,900),(2230,1180), 8, 165, 38, 0.80, None, LEAF_A+(185,))
sprig((2560,980),(2380,1100),(2300,1370), 7, 140, 32, 0.90, None, LEAF_B+(165,))
sprig((2480,1440),(2400,1230),(2300,1060), 6, 120, 28, 1.00, LEAF_B+(120,), None)
sprig((2420,540),(2500,700),(2560,880), 5, 110, 26, 0.95, None, LEAF_B+(150,))
for p in [(2270,1000),(2310,1060),(2245,930),(2350,1150),(2220,1120)]:
    A.ellipse([(p[0]-5)*SS,(p[1]-5)*SS,(p[0]+5)*SS,(p[1]+5)*SS], fill=LEAF_A+(150,))

art = art.resize((W,H), Image.LANCZOS)
img = Image.alpha_composite(img.convert('RGBA'), art).convert('RGB')

# ───────────────── portrait disc ─────────────────
from collections import deque
D = 300; DISC_X, DISC_Y = 562+D/2, (ST+SB)/2
photo = Image.open(PORTRAIT).convert('RGB').crop(CROPBOX)
pa = np.asarray(photo).astype(np.float32)
pR,pG,pB = pa[...,0],pa[...,1],pa[...,2]
pL = 0.299*pR+0.587*pG+0.114*pB

# isolate the studio wall: bright, warm, and connected to the crop border
wall = (pL>132) & ((pR-pB)<120) & (pG>pB+18)
hh,ww = wall.shape; seen = np.zeros_like(wall); dq = deque()
for x in range(ww):
    for y in (0,hh-1):
        if wall[y,x] and not seen[y,x]: seen[y,x]=True; dq.append((y,x))
for y in range(hh):
    for x in (0,ww-1):
        if wall[y,x] and not seen[y,x]: seen[y,x]=True; dq.append((y,x))
while dq:
    y,x = dq.popleft()
    for ny,nx in ((y-1,x),(y+1,x),(y,x-1),(y,x+1)):
        if 0<=ny<hh and 0<=nx<ww and wall[ny,nx] and not seen[ny,nx]:
            seen[ny,nx]=True; dq.append((ny,nx))
wm = (np.asarray(Image.fromarray((seen*255).astype(np.uint8))
        .filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(2.5)))
        .astype(np.float32)/255.)[...,None]

# grade the wall to the reference terracotta, then flatten it
vgrad = np.linspace(0,1,hh,dtype=np.float32)[:,None,None]
terra = np.array([182,118,78],float) + (np.array([150,92,58],float)-np.array([182,118,78],float))*vgrad
graded = np.clip(pa*(1-wm) + (pa*0.22 + terra*0.78)*wm, 0, 255)
inner = (np.asarray(Image.fromarray((seen*255).astype(np.uint8))
          .filter(ImageFilter.MinFilter(9)).filter(ImageFilter.GaussianBlur(6)))
          .astype(np.float32)/255.)[...,None]
blur = np.asarray(Image.fromarray(graded.astype(np.uint8)).filter(ImageFilter.GaussianBlur(26))).astype(np.float32)
graded = graded*(1-inner) + blur*inner

disc = Image.fromarray(graded.astype(np.uint8)).resize((D*4,D*4), Image.LANCZOS)
m = Image.new('L',(D*4,D*4),0); ImageDraw.Draw(m).ellipse((0,0,D*4-1,D*4-1),fill=255)
img.paste(disc.resize((D,D),Image.LANCZOS),(int(DISC_X-D/2),int(DISC_Y-D/2)), m.resize((D,D),Image.LANCZOS))
ring = Image.new('RGBA',(W*SS,H*SS),(0,0,0,0))
ImageDraw.Draw(ring).ellipse([(DISC_X-D/2-8)*SS,(DISC_Y-D/2-8)*SS,(DISC_X+D/2+8)*SS,(DISC_Y+D/2+8)*SS],
                             outline=TERRA+(150,), width=3*SS)
img = Image.alpha_composite(img.convert('RGBA'), ring.resize((W,H), Image.LANCZOS)).convert('RGB')

# ───────────────── type ─────────────────
d = ImageDraw.Draw(img)
def met(t,f,ls=0.0):
    x=0.0;L,T,R,B=1e9,1e9,-1e9,-1e9
    for c in t:
        bb=f.getbbox(c)
        if bb[3]>bb[1]: L=min(L,x+bb[0]);R=max(R,x+bb[2]);T=min(T,bb[1]);B=max(B,bb[3])
        x+=f.getlength(c)+ls
    return L,T,R,B
def put(t,f,col,axis,y,ls=0.0):
    L,T,R,B=met(t,f,ls); x=axis-(L+R)/2
    for c in t:
        d.text((x,y),c,font=f,fill=col); x+=f.getlength(c)+ls
    return (axis-(R-L)/2, y+T, axis+(R-L)/2, y+B)
def fit(t,name,cap,maxw,ls=0.0,lo=12):
    s=cap
    while s>lo:
        f=font(name,s); L,_,R,_=met(t,f,ls)
        if R-L<=maxw: return f
        s-=1
    return font(name,lo)

TXT_L, TXT_R = DISC_X+D/2+86, SR-PAD
AXIS, COLW = (TXT_L+TXT_R)/2, TXT_R-TXT_L

NAME="Temidayo Afonja"; TAG="Make your next move without starting over"
CATS=["CAREER","TRANSITIONS","PRACTICAL STRATEGIES","REAL CONVERSATIONS"]; URL="www.temidayoafonja.com"
f_name = fit(NAME, SCRIPT, 170, min(COLW,860))
f_tag  = fit(TAG,  SERIF,   50, min(COLW,800))
f_cat  = fit("   ".join(CATS), SERIF6, 27, min(COLW,900), 3.2)
f_url  = fit(URL,  SERIF,   32, min(COLW,520), 1.0)

mn,mt,mg,mu = met(NAME,f_name), met(TAG,f_tag), met(CATS[0],f_cat,3.2), met(URL,f_url,1.0)
G1,G2,G3 = 6, 30, 26
y0=0.0; y1=y0+mn[3]+G1-mt[1]; y2=y1+mt[3]+G2-mg[1]; y3=y2+mg[3]+G3-mu[1]
top,bot = y0+mn[1], y3+mu[3]
dy = (ST+SB)/2-(top+bot)/2

r1=put(NAME,f_name,INK,  AXIS,y0+dy)
r2=put(TAG, f_tag, INK,  AXIS,y1+dy)
# category strip with thin dividers
seg=[(c, sum(f_cat.getlength(ch)+3.2 for ch in c)-3.2) for c in CATS]
SPC=46.0
total=sum(w for _,w in seg)+SPC*(len(seg)-1)
x=AXIS-total/2; cat_l=x
for i,(c,w) in enumerate(seg):
    xx=x
    for ch in c:
        d.text((xx,y2+dy),ch,font=f_cat,fill=BROWN); xx+=f_cat.getlength(ch)+3.2
    x+=w
    if i<len(seg)-1:
        mx=x+SPC/2
        d.line([(mx,y2+dy+mg[1]-3),(mx,y2+dy+mg[3]+3)], fill=(198,166,138), width=2)
        x+=SPC
r3=(cat_l, y2+dy+mg[1], x, y2+dy+mg[3])
r4=put(URL,f_url,INK, AXIS,y3+dy,1.0)

OUT='/home/user/temidayoafonja-site/temidayo_afonja_youtube_banner_template.png'
img.save(OUT, optimize=True)
for lbl,r in (("name",r1),("tagline",r2),("cats",r3),("url",r4)):
    print(f"  {lbl:8s} x {r[0]:7.1f}..{r[2]:7.1f}  y {r[1]:6.1f}..{r[3]:6.1f}")
print(f"  disc     x {DISC_X-D/2:7.1f}..{DISC_X+D/2:7.1f}  y {DISC_Y-D/2:6.1f}..{DISC_Y+D/2:6.1f}")

gi=img.copy(); gd=ImageDraw.Draw(gi,'RGBA')
gd.rectangle([SL,ST,SR,SB],outline=(200,60,60,255),width=4)
gd.rectangle([SL+PAD,ST+PAD,SR-PAD,SB-PAD],outline=(60,120,200,170),width=2)
gd.text((SL+8,ST-40),"ALL-DEVICES SAFE AREA 1546 x 423",font=font('DMSans-400.ttf',26),fill=(200,60,60,255))
gi.save('/home/user/temidayoafonja-site/temidayo_afonja_youtube_banner_template_SAFEAREA_GUIDE.png',optimize=True)
P='/home/user/temidayoafonja-site/banner-previews/'; os.makedirs(P,exist_ok=True)
img.crop((int(CX-773),int(CY-211),int(CX+773),int(CY+212))).save(P+'template_mobile_1546x423.png')
img.crop((int(CX-773),int(CY-211),int(CX+773),int(CY+212))).resize((960,262)).save('t_m.png')
img.resize((1100,619)).save('t_f.png')
