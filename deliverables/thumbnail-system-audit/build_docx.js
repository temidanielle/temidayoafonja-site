const fs = require('fs');
const d = require('docx');
const {Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, ImageRun,
       Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle,
       PageBreak, LevelFormat} = d;

const NAVY="0F2346", GOLD="A88628", RED="B02A1E", GREEN="186E48", DIM="5A6478";
const W = 9360; // content width in DXA for Letter with 1.1" margins

const img = (f, w, h) => new Paragraph({
  alignment: AlignmentType.CENTER, spacing:{before:120, after:80},
  children:[new ImageRun({type:"png", data: fs.readFileSync("docimg/"+f),
                          transformation:{width:w, height:h}})]});

const cap = t => new Paragraph({alignment: AlignmentType.CENTER, spacing:{after:260},
  children:[new TextRun({text:t, size:17, italics:true, color:DIM})]});

const p = (t, o={}) => new Paragraph({spacing:{after:o.after??160}, ...o.pp,
  children:[new TextRun({text:t, size:21, color:o.color??"1A1A1A", bold:o.bold})]});

const rich = runs => new Paragraph({spacing:{after:160},
  children: runs.map(r => new TextRun({text:r[0], size:21, bold:r[1]==="b",
    color:r[2]??"1A1A1A"}))});

const h1 = t => new Paragraph({heading: HeadingLevel.HEADING_1, spacing:{before:340, after:150},
  children:[new TextRun({text:t, size:30, bold:true, color:NAVY})]});
const h2 = t => new Paragraph({heading: HeadingLevel.HEADING_2, spacing:{before:250, after:110},
  children:[new TextRun({text:t, size:24, bold:true, color:NAVY})]});

function callout(title, lines, colour, fill) {
  return new Table({ width:{size:W, type:WidthType.DXA}, columnWidths:[W],
    rows:[new TableRow({children:[new TableCell({
      width:{size:W, type:WidthType.DXA},
      shading:{type:ShadingType.CLEAR, fill:fill},
      margins:{top:170, bottom:170, left:200, right:200},
      borders:{ left:{style:BorderStyle.SINGLE, size:18, color:colour},
                top:{style:BorderStyle.SINGLE, size:4, color:colour},
                bottom:{style:BorderStyle.SINGLE, size:4, color:colour},
                right:{style:BorderStyle.SINGLE, size:4, color:colour}},
      children:[
        new Paragraph({spacing:{after:90}, children:[
          new TextRun({text:title, bold:true, size:22, color:colour})]}),
        ...lines.map(l => new Paragraph({spacing:{after:70}, children:[
          new TextRun({text:l, size:20, color:"1A1A1A"})]}))]
    })]})]});
}

function table(headers, rows, widths) {
  const mk = (t,bold,fill,w) => new TableCell({
    width:{size:w, type:WidthType.DXA},
    shading: fill?{type:ShadingType.CLEAR, fill:fill}:undefined,
    margins:{top:90, bottom:90, left:120, right:120},
    children:[new Paragraph({children:[new TextRun({
      text:t, size:18, bold:bold, color: bold&&fill===NAVY?"FFFFFF":"1A1A1A"})]})]});
  return new Table({ width:{size:W, type:WidthType.DXA}, columnWidths:widths,
    rows:[
      new TableRow({tableHeader:true, children: headers.map((t,i)=>mk(t,true,NAVY,widths[i]))}),
      ...rows.map((r,ri)=> new TableRow({children:
        r.map((t,i)=>mk(t,false, ri%2?"F7F5F0":undefined, widths[i]))}))]});
}

const doc = new Document({
  numbering:{config:[{reference:"b", levels:[{level:0, format:LevelFormat.BULLET,
    text:"•", alignment:AlignmentType.LEFT,
    style:{paragraph:{indent:{left:420, hanging:220}}}}]}]},
  styles:{default:{document:{run:{font:"Calibri", size:21}}}},
  sections:[{
    properties:{page:{size:{width:12240, height:15840}, margin:{top:1440,bottom:1440,left:1440,right:1440}}},
    children:[

// ---------------------------------------------------------------- title
new Paragraph({spacing:{after:60}, children:[new TextRun({
  text:"Three-Video Thumbnail System Audit", bold:true, size:44, color:NAVY})]}),
new Paragraph({spacing:{after:40}, border:{bottom:{style:BorderStyle.SINGLE, size:12, color:GOLD, space:8}},
  children:[new TextRun({text:"Capability Formation launch cluster — Videos 1, 2 and 3",
                         size:23, color:DIM})]}),
new Paragraph({spacing:{before:130, after:280}, children:[new TextRun({
  text:"Prepared 20 August 2026. Nothing was redesigned, created or altered to produce this audit.",
  size:19, italics:true, color:DIM})]}),

callout("FINDING: THE SUPPLIED VIDEO 1 AND VIDEO 2 CANDIDATES CONTAIN SYNTHETIC IMAGERY",
 ["They cannot be adopted as launch thumbnails without breaking the “real photographs only” rule.",
  "No approved thumbnail exists for Video 1 or Video 2.",
  "Video 3 Final A is unaffected, verified, and cleared to upload."], RED, "FDEEEC"),

h1("1.  Video 3 — approved and confirmed"),
p("Final A was checked against all three conditions you set. It passes each one."),
table(["Check","Result"],
 [["Dimensions","1280 × 720, exactly 16:9"],
  ["Under 2 MB","Yes — 200,945 bytes (196.2 KB), 9.6% of the ceiling"],
  ["Exact Final A from the approved contact sheet","Yes — proven by pixel comparison"]],
 [4200,5160]),
new Paragraph({spacing:{after:120}}),
p("The third condition was verified rather than assumed. The Final A panel embedded in the approved contact sheet is pixel-identical to the master at the same size: zero differing pixels once the 4-pixel frame drawn around it is excluded, and all 11,850 differing pixels sit on that frame, none inside the artwork. The upload JPG against the same master downscaled to 1280 × 720 differs by a mean of 0.75 out of 255, which is ordinary JPEG quantisation at quality 95 and nothing else. The approved image, the contact sheet panel and the upload file all trace to one master."),
img("v3_final_a.png", 470, 264),
cap("Video 3 Final A — approved, unchanged, cleared to upload"),

new Paragraph({children:[new PageBreak()]}),

h1("2.  File inventory"),
h2("Video 3 — exists, approved"),
table(["Attribute","Value"],
 [["Filename","VIDEO_3_THUMBNAIL_FINAL_A_UPLOAD_1280x720.jpg"],
  ["Path","deliverables/video-3-slides/thumbnail/"],
  ["Version","v1.2"],
  ["Dimensions","1280 × 720"],
  ["File size","200,945 bytes (196.2 KB)"],
  ["Marked","SELECTED / APPROVED, in VIDEO_3_THUMBNAIL_STATUS_v1.2.md"],
  ["Source portrait","a55ff6e1-D85AD998016A47539E6889F2988BF6B5.png, 1254 × 1254"]],
 [2700,6660]),
new Paragraph({spacing:{after:140}}),
p("Archived alternate: VIDEO_3_THUMBNAIL_FINAL_B_UPLOAD_1280x720.jpg, same folder, same version, 1280 × 720, 204,663 bytes, marked ALTERNATE and retained for future A/B testing."),

h2("Video 1 — no final exists"),
p("No thumbnail file. No thumbnail directory. Nothing marked FINAL, RECOMMENDED or SELECTED. I searched the working tree and every branch of git history. The words DON’T START FROM ZERO appear nowhere in the repository."),

h2("Video 2 — no final exists"),
p("The same. The words YOUR SKILLS ARE STALLING appear once, as deck metadata on line 9 of VIDEO_2_SLIDE_QA_v1.0.md. Recorded, never designed."),
p("Files named phone-thumbnail-check-*.png do exist for both videos. Despite the name, these are slide legibility checks at phone size, carried over from the original Video 1 brief. They are not YouTube thumbnails and cannot serve as one.", {color:DIM}),

h2("Candidates supplied in this round"),
p("None of these is in the repository. They are conversation attachments with no version number, no approval marker and no documentation identifying any of them as approved."),
table(["Ref","Words","Dimensions","File size","16:9?"],
 [["c1","WHAT STILL TRAVELS?","1672 × 941","3,013,462 B","No — 1.7768"],
  ["c2","DON’T START FROM ZERO","1672 × 941","3,711,486 B","No — 1.7768"],
  ["c3","YOUR EXPERIENCE COUNTS","1672 × 941","3,154,622 B","No — 1.7768"],
  ["c4","YOUR SKILLS ARE STALLING","1672 × 941","3,146,999 B","No — 1.7768"],
  ["sheet","contact sheet, panels 1A/1B/1C/2/3","1536 × 1024","2,242,910 B","n/a"]],
 [900,3360,1700,1800,1600]),
img("candidates.png", 460, 261),
cap("The four supplied candidates, as received"),

callout("COMPETING CANDIDATES — NOT CHOSEN SILENTLY",
 ["Video 1 has three competing sets of words across five files: DON’T START FROM ZERO (c2, sheet 1A),",
  "YOUR EXPERIENCE COUNTS (c3, sheet 1B), WHAT STILL TRAVELS? (c1, sheet 1C). Only the first matches your lock.",
  "Video 2 has two competing treatments: c4 (wine outfit, briefcase blocks) and sheet panel 2 (caramel, desk pose).",
  "No project documentation identifies any of them as approved, because none is documented at all. The supplied",
  "sheet’s own manifest describes a thumbs_v1.0/ folder that does not exist in this repository."],
 NAVY, "F2F5F9"),

new Paragraph({children:[new PageBreak()]}),

h1("3.  The blocking finding"),
h2("The only real photographs available"),
p("Four images in total: three in the repository, plus the approved Video 3 portrait."),
img("reals.png", 470, 120),
cap("photo-headshot-green.png  ·  photo-headshot-cream.png  ·  photo-portrait-wine.png  ·  a55ff6e1…B5.png"),
callout("NO PURPLE-OUTFIT PHOTOGRAPH AND NO GREEN-SHIRT PHOTOGRAPH EXISTS",
 ["“Green” in the asset name refers to the BACKDROP. In all three repository photographs she wears the same wine top.",
  "The expected visual story for Video 1 asks for a real earlier purple-outfit photograph and a real earlier",
  "green-shirt photograph. Those photographs do not exist, and something generated them to fill the gap."],
 GREEN, "EDF5F0"),

h2("Evidence A — a different person, presented as her career history"),
p("The middle polaroid in “YOUR EXPERIENCE COUNTS” shows a woman in a black business suit with different facial structure and different hair. It is not Temidayo."),
img("evid_A.png", 380, 270),

h2("Evidence B — a pose and setting that never existed"),
p("Contact-sheet panel 2 shows her in the caramel top, seated at a desk, index finger to her temple, with a full office behind her. The real caramel photograph is a plain studio headshot against a seamless backdrop with her hands out of frame. No such photograph was ever supplied."),
img("evid_B.png", 300, 275),

new Paragraph({children:[new PageBreak()]}),

h2("Evidence C — pseudo-text on the props"),
p("Magnified eight times from that same panel. The sticky notes carry letter-shaped marks that spell nothing in any language. This is a signature of generative image synthesis; real photographs of real sticky notes do not produce it."),
img("evid_C.png", 420, 303),

h2("Evidence D — garments with no photographic source"),
p("Panel 1A shows insets of a purple suit and a green shirt. Neither garment appears in any photograph supplied at any point in this project."),
img("evid_D.png", 260, 331),

callout("THE SUPPLIED CONTACT SHEET CARRIES A FALSE ASSURANCE",
 ["Its footer reads: “No part of Temidayo’s appearance was generated or altered. All thumbnails use",
  "original photographs only.”  Items A to D contradict that claim directly.",
  "This is flagged as a finding in its own right, because it is the part most likely to cause harm if trusted."],
 RED, "FDEEEC"),

new Paragraph({children:[new PageBreak()]}),

h1("4.  Consistency audit"),
p("Steps 2 to 4 of the brief asked for a three-video launch contact sheet and a full cohesion grading. Two of the three thumbnails do not exist in publishable form. Building that sheet would mean either inventing Video 1 and Video 2 thumbnails or presenting synthetic imagery as approved launch artwork. I did neither."),
p("Grading imagery that fails the threshold test — real photographs only — would lend it a legitimacy it has not earned. These are the rows that can be filled honestly."),
table(["Attribute","Video 1","Video 2","Video 3","Consistent?","Action needed"],
 [["Compliant thumbnail exists","No","No","Yes","NO","Videos 1 and 2 need original work"],
  ["Real photographs only","Fails (A, D)","Fails (B, C)","Passes","NO","Do not adopt the candidates"],
  ["Correct locked words","Three competing sets","Matches","Matches","NO","Confirm Video 1 wording"],
  ["Correct source portrait","Wine, per brief","Wine, brief says caramel","Caramel","NO","Resolve for Video 2"],
  ["Upload-ready geometry","1672×941, not 16:9","1672×941, not 16:9","1280×720","NO","Rebuild at 16:9"]],
 [2000,1620,1720,1200,1000,1820]),

h1("5.  Verdict"),
callout("D.  NOT A SYSTEM YET — VIDEOS 1 AND 2 NEED ORIGINAL, COMPLIANT THUMBNAILS",
 ["None of options A, B or C fits. This is not a cohesion problem to be micro-aligned.",
  "Two of the three thumbnails do not exist in a form that can be published under your own rules.",
  "Video 3 needs no change and is cleared to upload."], RED, "FDEEEC"),

h2("What is needed before Videos 1 and 2 can be built"),
new Paragraph({numbering:{reference:"b", level:0}, spacing:{after:130}, children:[new TextRun({
 text:"Photographs. Real ones. There is no purple-outfit or green-shirt photo. If earlier-career photographs exist, they need to land as files. If they do not, Video 1’s past-into-present story needs a device built from real material — the green-backdrop and cream-backdrop headshots can carry a then-and-now reading through backdrop and treatment rather than wardrobe.", size:21})]}),
new Paragraph({numbering:{reference:"b", level:0}, spacing:{after:130}, children:[new TextRun({
 text:"Video 2’s portrait. Your brief says caramel; candidate c4 uses wine. Confirm which, noting that the caramel portrait is the one Video 3 already uses — worth deciding whether the two videos should share a portrait.", size:21})]}),
new Paragraph({numbering:{reference:"b", level:0}, spacing:{after:240}, children:[new TextRun({
 text:"Video 1’s title and words. The title given here reads “How to Change Jobs Without Starting Your Career Over”; the deck, scripts and all v2.4 exports use “How I Changed Jobs Without Starting My Career Over”.", size:21})]}),

h1("6.  Confirmations"),
...["No existing thumbnail was overwritten.",
    "No source photograph was modified.",
    "No part of Temidayo’s appearance was generated or altered in this work.",
    "No website, video, slide, script or product file was changed.",
    "Video 3 Final A, Final B and all their derivatives are untouched."
   ].map(t => new Paragraph({numbering:{reference:"b", level:0}, spacing:{after:100},
     children:[new TextRun({text:t, size:21})]})),

new Paragraph({spacing:{before:300}, border:{top:{style:BorderStyle.SINGLE, size:8, color:GOLD, space:10}},
  children:[new TextRun({text:"Two items remain open from earlier and are unrelated to the thumbnails: the /career-decisions route does not exist on the site, and the Video 3 chapter timestamps are still to be set from the real export.", size:18, italics:true, color:DIM})]})
]}]});

Packer.toBuffer(doc).then(b => {
  fs.writeFileSync("Three-Video_Thumbnail_System_Audit.docx", b);
  console.log("written", b.length, "bytes");
});
