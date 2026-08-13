#!/usr/bin/env python3
"""Build the seven Capability Formation Field Kit Gumroad merchandising assets
as editable SVG masters, render to exact-dimension sRGB PNGs, and emit reduced
readability tests, the Image 01 1280x720 export, and a contact sheet.

Copy is taken verbatim from the four final copy locks + the Version 2.0 brief.
Reproduced product content comes only from real Field Kit page crops."""
import os, sys
from gumlib import *

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, ".."))
MASTERS = os.path.join(OUT, "masters"); PNG = os.path.join(OUT, "png")
RED = os.path.join(OUT, "reduced")
for d in (MASTERS, PNG, RED): os.makedirs(d, exist_ok=True)

def save_master(name, svg):
    p = os.path.join(MASTERS, name+".svg")
    with open(p, "w") as f: f.write(svg)
    return p

# =========================================================================
# THUMBNAIL 600x600
# =========================================================================
def build_thumb():
    W = H = 600; M = 72; cw = W-2*M
    b = []
    s = fit_size("IS YOUR JOB STILL", cw, CG, 600, start=66)
    lead = s*1.02
    # vertical composition: device / headline (dominant) / rule / category / id
    hl1_y = 262
    b.append(device(M, hl1_y - lead - 96, 62))
    b.append(text(M, hl1_y, "IS YOUR JOB STILL", s, CG, 600, CREAM))
    b.append(text(M, hl1_y+lead, "BUILDING YOU?", s, CG, 600, CREAM))
    ry = hl1_y+lead+34
    b.append(rect(M, ry, 74, 4, fill=RUST))
    b.append(text(M, ry+52, "CAREER POSITION ASSESSMENT", 16.5, DM, 700, GOLD, spacing=2.8))
    b.append(text(M, ry+92, "THE CAPABILITY FORMATION FIELD KIT", 13, DM, 500, CREAM_SOFT, spacing=1.6))
    svg = svg_doc(W, H, "\n".join(b), bg=NAVY)
    return save_master("fieldkit_gumroad_thumbnail_600x600", svg), W, H

# shared listing-image frame -------------------------------------------------
LW, LH, LM = 1600, 900, 96
def eyebrow_block(x, y, category, headline_lines, hl_size, hl_fill, sub=None,
                  sub_fill=None, cat_fill=GOLD, rule=True, hl_weight=600, lead=None):
    b = [text(x, y, category, 17, DM, 700, cat_fill, spacing=3.0)]
    hy = y + 62
    lead = lead or hl_size*0.98
    for i, ln in enumerate(headline_lines):
        b.append(text(x, hy + i*lead, ln, hl_size, CG, hl_weight, hl_fill))
    ry = hy + (len(headline_lines)-1)*lead + 34
    if rule:
        b.append(rect(x, ry, 66, 4, fill=RUST)); ry += 4
    if sub:
        sy = ry + 40
        for j, ln in enumerate(sub):
            b.append(text(x, sy + j*28, ln, 18, DM, 400, sub_fill or NAVY_SOFT))
        ry = sy + (len(sub)-1)*28
    return "\n".join(b), ry

# =========================================================================
# IMAGE 01 - Recognition cover (navy). Left text, right cover mockup.
# =========================================================================
def build_01():
    W, H = LW, LH; b = []
    b.append(rect(0,0,W,H,fill=NAVY))
    lx = LM; lw = int(W*0.58) - LM - 20
    b.append(device(lx, 150, 58))
    b.append(text(lx, 268, "AN EVIDENCE-LED CAREER POSITION ASSESSMENT", 16, DM, 700, GOLD, spacing=2.6))
    hl = ["Is Your Job Still", "Building You?"]
    s = fit_size("Is Your Job Still", lw, CG, 600, start=92)
    lead = s*0.96
    for i,ln in enumerate(hl):
        b.append(text(lx, 350 + i*lead, ln, s, CG, 600, CREAM))
    ry = 350 + lead + 40
    b.append(rect(lx, ry, 72, 5, fill=RUST))
    sub = wrap_words("Use evidence from the last 90 days to read what your work is building, what can travel, and where your position may be exposed.", lw, 21, DM, 400)
    for j,ln in enumerate(sub):
        b.append(text(lx, ry+52 + j*30, ln, 21, DM, 400, CREAM_SOFT))
    b.append(text(lx, H-96, "THE CAPABILITY FORMATION FIELD KIT", 15, DM, 700, GOLD, spacing=2.4))
    # right: restrained perspective mockup of the real cover with 2 interior edges
    coverw = 420; cx = int(W*0.60)+70; cy = 150
    iw, ih = img_size(os.path.join(CROPS,"cover.png")); chh = coverw*ih/iw
    uri = img_datauri(os.path.join(CROPS,"cover.png"))
    b.append(rect(cx+30, cy+30, coverw, chh, fill="#0A1830", opacity=0.55, rx=4))     # page edge 2
    b.append(rect(cx+16, cy+16, coverw, chh, fill="#16294a", opacity=0.9, rx=4))       # page edge 1
    b.append(f'<g filter="url(#lift)" transform="translate({cx},{cy})">'
             f'<g transform="skewY(-5)">'
             f'<image x="0" y="0" width="{coverw}" height="{chh:.1f}" href="{uri}"/>'
             f'<rect x="0" y="0" width="{coverw}" height="{chh:.1f}" fill="none" stroke="{GOLD}" stroke-width="1.4"/>'
             f'</g></g>')
    svg = svg_doc(W,H,"\n".join(b),bg=NAVY)
    return save_master("fieldkit_gumroad_01_recognition_1600x900", svg), W, H

# =========================================================================
# IMAGE 02 - Tangible outputs (sand). Left text+labels, right 3 real cards.
# =========================================================================
def build_02():
    W,H = LW,LH; b=[rect(0,0,W,H,fill=SAND)]
    lx=LM; lw=int(W*0.44)-LM
    b.append(device(lx,130,52,stroke=GOLD,fill=RUST))
    s=52; hl=wrap_words("Leave With a Dated Read of Where You Stand.", lw, s, CG,600)
    while any(measure(x, s, CG,600)>lw for x in hl) and s>34:
        s-=1; hl=wrap_words("Leave With a Dated Read of Where You Stand.", lw, s, CG,600)
    for i,ln in enumerate(hl):
        b.append(text(lx,262+i*s*1.0,ln,s,CG,600,NAVY))
    ry=262+(len(hl)-1)*s*1.0+30
    b.append(rect(lx,ry,66,4,fill=RUST))
    sub=wrap_words("Not just a score. A position you can save, revisit, and rescore.", lw,19,DM,400)
    for j,ln in enumerate(sub): b.append(text(lx,ry+44+j*26,ln,19,DM,400,NAVY_SOFT))
    labels=["TWO SCORES","STATE OR BOUNDARY","STANDING-STILL LINE","SELF-READ","POSITION CARD","NEXT RESCORE DATE"]
    ly=ry+44+len(sub)*26+40
    for k,lab in enumerate(labels):
        col=k%2; row=k//2
        xx=lx+col*(lw/2); yy=ly+row*46
        b.append(rect(xx,yy-13,5,18,fill=(GOLD if col==0 else RUST)))
        b.append(text(xx+16,yy,lab,15.5,DM,700,NAVY,spacing=1.2))
    # right proof zone ~56%
    rz_x=int(W*0.44)+24; rz_w=W-LM-rz_x
    # dominant Position Card
    pcw=int(rz_w*0.60)
    pc_svg,pch=page_card(rz_x+rz_w-pcw, 150, pcw, "p20_card.png", shadow="lift")
    # supporting: self-read + tracker (stacked left of position card)
    sw_=int(rz_w*0.40)-18
    sr_svg,srh=page_card(rz_x, 150, sw_, "p19_skel.png", shadow="soft")
    tr_svg,trh=page_card(rz_x, 150+srh+26, sw_, "p22_track.png", shadow="soft")
    b += [sr_svg,tr_svg,pc_svg]
    b.append(text(rz_x, 150+srh+26+ min(trh, 999) +0, "", 1))  # noop anchor
    svg=svg_doc(W,H,"\n".join(b),bg=SAND)
    return save_master("fieldkit_gumroad_02_outputs_1600x900",svg),W,H

# =========================================================================
# IMAGE 03 - Product proof (navy). Four real pages: score -> place -> record.
# =========================================================================
def build_03():
    W,H=LW,LH; b=[rect(0,0,W,H,fill=NAVY)]
    lx=LM
    b.append(device(lx,120,52))
    b.append(text(lx,238,"From Evidence to Position.",58,CG,600,CREAM))
    b.append(rect(lx,262,66,4,fill=RUST))
    b.append(text(lx,308,"Score the work you actually lived. Place the pattern. Record the position.",20,DM,400,CREAM_SOFT))
    # four panels aligned at top, Position Card ~18% larger (culmination)
    top=418; gap=34; base=300
    plan=[("p05_evid.png",base,"1","SCORE"),("p06_seq.png",base,None,None),
          ("p08_seq.png",base,"2","PLACE"),("p20_card.png",int(base*1.18),"3","RECORD")]
    xs=[]; x=lx
    widths=[p[1] for p in plan]
    total=sum(widths)+gap*3
    x=lx + (W-2*LM-total)/2
    centers=[]
    for crop,w,num,lab in plan:
        svg,h=page_card(x,top,w,crop,shadow="lift")
        b.append(svg); centers.append((x+w/2,top,w,h,num,lab)); xs.append((x,w))
        x+=w+gap
    # gold connector dots between panels (no arrows)
    for i in range(len(xs)-1):
        x0=xs[i][0]+xs[i][1]; x1=xs[i+1][0]
        cyc=top+ base*0.5
        b.append(f'<circle cx="{(x0+x1)/2:.1f}" cy="{cyc:.1f}" r="4" fill="{GOLD}"/>')
    # step labels above panels
    for cx,ty,w,h,num,lab in centers:
        if num:
            b.append(text(cx,top-40,num,26,CG,600,RUST,anchor="middle"))
            b.append(text(cx,top-18,lab,14,DM,700,CREAM,spacing=2.0,anchor="middle"))
    svg=svg_doc(W,H,"\n".join(b),bg=NAVY)
    return save_master("fieldkit_gumroad_03_product_proof_1600x900",svg),W,H

# =========================================================================
# IMAGE 04 - Evidence method (sand). Evidence crop + misreadings + principle.
# =========================================================================
def build_04():
    W,H=LW,LH; b=[rect(0,0,W,H,fill=SAND)]
    lx=LM
    b.append(device(lx,110,50))
    b.append(text(lx,214,"Do Not Just Score It. Support It.",54,CG,600,NAVY))
    b.append(rect(lx,238,66,4,fill=RUST))
    sub=wrap_words("Every answer is tied to evidence from the last 90 days. Then the scores are tested against three common misreadings.", W-2*LM,20,DM,400)
    for j,ln in enumerate(sub): b.append(text(lx,282+j*28,ln,20,DM,400,NAVY_SOFT))
    top=330
    # left column: evidence crop (protocol + statements + score boxes) over the principle callout
    lwd=648
    lsvg,lh=page_card(lx,top,lwd,"p05_evid_short.png",shadow="soft")
    b.append(lsvg)
    py=top+lh+26; pw=lwd; ph=H-py-64
    b.append(rect(lx,py,pw,ph,fill=NAVY,rx=5))
    b.append(rect(lx,py,6,ph,fill=RUST,rx=0))
    cl=wrap_words("A score without an evidence line is a guess with decimal points.", pw-72,26,CG,600)
    cy0=py+ph/2-(len(cl)-1)*17
    for j,ln in enumerate(cl):
        b.append(text(lx+32,cy0+j*34,ln,26,CG,600,CREAM))
    # right: misreadings page (near-full), centred in the right half
    rzone_x=lx+lwd+56; rzone_w=W-LM-rzone_x
    rh_target=H-64-top
    rwd=rh_target*2550/2788
    rx=rzone_x+(rzone_w-rwd)/2
    rsvg,rh=page_card(rx,top,rwd,"p11_full.png",shadow="soft")
    b.append(rsvg)
    svg=svg_doc(W,H,"\n".join(b),bg=SAND)
    return save_master("fieldkit_gumroad_04_evidence_method_1600x900",svg),W,H

def _copy_list(x,y,items,w,tick,txtcol,step=40,size=18):
    out=[]
    for i,it in enumerate(items):
        yy=y+i*step
        out.append(rect(x,yy-13,5,17,fill=tick))
        out.append(text(x+18,yy,it,size,DM,500,txtcol))
    return "\n".join(out)

# =========================================================================
# IMAGE 05 - Free vs $150 (sand ground; two equal columns).
# =========================================================================
def build_05():
    W,H=LW,LH; b=[rect(0,0,W,H,fill=SAND)]
    lx=LM
    # two-sentence stacked headline; second sentence carries greater weight
    b.append(text(lx,150,"The Free Check Helps You See the Pattern.",40,CG,500,NAVY_SOFT))
    b.append(text(lx,198,"The Field Kit Tests Your Position.",45,CG,700,NAVY))
    b.append(rect(lx,222,66,4,fill=RUST))
    # two equal columns
    top=278; colw=(W-2*LM-40)/2; colh=470
    fx=lx; kx=lx+colw+40
    # FREE column (light, dignified)
    b.append(rect(fx,top,colw,colh,fill=CREAM,rx=6,stroke="#E3DAC9",sw=1.5))
    b.append(text(fx+34,top+52,"FREE",22,CG,600,RUST))
    b.append(text(fx+34,top+84,"WHAT MIGHT BE HAPPENING?",14,DM,700,NAVY,spacing=1.6))
    b.append(_copy_list(fx+34,top+170,
        ["Recognition","Plain-language signs","An initial evidence-led career check","Language for what may have stopped moving"],
        colw-68,GOLD,NAVY,step=70,size=18.5))
    # $150 FIELD KIT column (navy, structured) + proof strip
    b.append(rect(kx,top,colw,colh,fill=NAVY,rx=6))
    b.append(text(kx+34,top+52,"$150 FIELD KIT",22,CG,600,GOLD))
    b.append(text(kx+34,top+84,"WHAT DOES MY EVIDENCE SAY?",14,DM,700,CREAM,spacing=1.4))
    b.append(_copy_list(kx+34,top+130,
        ["12 statements","Mandatory evidence lines","Density and Optionality scores","State or boundary","Self-Read and Position Card","Quarterly rescore"],
        colw-68,RUST,CREAM,step=34,size=16.5))
    # restrained proof strip (real crops p5, p8, p20)
    strip_y=top+colh-118; sx=kx+34; sw=120
    for crop in ("p05_evid.png","p08_matrix.png","p20_card.png"):
        s,hh=page_card(sx,strip_y,sw,crop,shadow="soft",bw=1.2)
        b.append(s); sx+=sw+14
    # footer
    b.append(text(lx,H-70,"Choose the Field Kit when you are ready to run the full private assessment.",20,CG,600,NAVY,italic=True))
    svg=svg_doc(W,H,"\n".join(b),bg=SAND)
    return save_master("fieldkit_gumroad_05_free_vs_fieldkit_1600x900",svg),W,H

# =========================================================================
# IMAGE 06 - $150 Field Kit vs $500 live Position Read (two connected panels)
# =========================================================================
def build_06():
    W,H=LW,LH; b=[rect(0,0,W,H,fill=SAND)]
    lx=LM
    hl=fit_size("Choose the Level of Support Your Decision Requires.",W-2*LM,CG,600,start=52)
    b.append(text(lx,160,"Choose the Level of Support Your Decision Requires.",hl,CG,600,NAVY))
    b.append(rect(lx,186,66,4,fill=RUST))
    top=232; colw=(W-2*LM-44)/2; colh=486
    ax=lx; bx=lx+colw+44
    # LEFT: $150 Field Kit (navy) with real Position Card crop
    b.append(rect(ax,top,colw,colh,fill=NAVY,rx=6))
    b.append(text(ax+34,top+56,"$150",34,CG,700,GOLD))
    b.append(text(ax+150,top+50,"FIELD KIT",18,DM,700,CREAM,spacing=1.6))
    b.append(text(ax+150,top+74,"PRIVATE SELF-ASSESSMENT",12.5,DM,700,CREAM_SOFT,spacing=1.8))
    b.append(_copy_list(ax+34,top+118,
        ["Complete on your own","Evidence-led scores","State or boundary","Standing-Still line","Self-Read and Position Card","Quarterly tracker"],
        colw*0.5,GOLD,CREAM,step=32,size=15.5))
    pc,pch=page_card(ax+colw-232, top+112, 200, "p20_card.png", shadow="lift", bw=1.2)
    b.append(pc)
    # RIGHT: $500 live Position Read (cream, gold-bordered) - text-led facilitator panel
    b.append(rect(bx,top,colw,colh,fill=CREAM,rx=6,stroke=GOLD,sw=2))
    b.append(text(bx+34,top+56,"$500",34,CG,700,RUST))
    b.append(text(bx+156,top+50,"LIVE POSITION READ",18,DM,700,NAVY,spacing=1.2))
    b.append(text(bx+156,top+74,"HUMAN CORRECTION + DECISION SUPPORT",11.5,DM,700,NAVY_SOFT,spacing=1.2))
    b.append(_copy_list(bx+34,top+118,
        ["Guided evidence correction","Interpreted state or boundary","Next-Move Decision","Live facilitation","30-day follow-up","Supported 90-day rescore"],
        colw-68,RUST,NAVY,step=34,size=16))
    # decision rule
    dr=wrap_words("Choose the Field Kit when you want a private self-read. Choose the live Position Read when a consequential decision requires another trained reader in the room.",W-2*LM,19,CG,600)
    for j,ln in enumerate(dr):
        b.append(text(lx,top+colh+50+j*28,ln,19,CG,600,NAVY,italic=True))
    svg=svg_doc(W,H,"\n".join(b),bg=SAND)
    return save_master("fieldkit_gumroad_06_fieldkit_vs_live_1600x900",svg),W,H

BUILDERS = {"thumb":build_thumb,"01":build_01,"02":build_02,"03":build_03,
            "04":build_04,"05":build_05,"06":build_06}

if __name__=="__main__":
    sel = sys.argv[1:] or list(BUILDERS)
    items=[]
    for k in sel:
        path,Wd,Hd=BUILDERS[k]()
        png=os.path.join(PNG, os.path.basename(path)[:-4]+".png")
        items.append((path,png,Wd,Hd)); print("built",k,"->",os.path.basename(path))
    render_svgs(items)
    for _,png,_,_ in items:
        sz=to_srgb_png(png); print("rendered",os.path.basename(png),sz)
