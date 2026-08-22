const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, BorderStyle, ShadingType, PageBreak
} = require('docx');

const NAVY = "0F2347", GOLD = "9A7B2E", INK = "26313F", MUTE = "5A6B82", RULE = "D9CBB2", BG = "F5F0E8", GREEN="2F6B3A";

const H = (t) => new Paragraph({ heading: HeadingLevel.HEADING_1, keepNext: true, keepLines: true, spacing: { before: 260, after: 90 },
  children: [ new TextRun({ text: t, color: NAVY, font: "Calibri", bold: true, size: 26 }) ] });
const H2 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_2, spacing: { before: 180, after: 60 },
  children: [ new TextRun({ text: t, color: NAVY, font: "Calibri", bold: true, size: 22 }) ] });
const P = (runs, opts={}) => new Paragraph({ spacing: { after: 120, line: 276 }, ...opts,
  children: (Array.isArray(runs)?runs:[runs]).map(r => typeof r === "string"
    ? new TextRun({ text: r, font: "Calibri", size: 21, color: INK }) : r) });
const B = (t, color=INK) => new TextRun({ text: t, bold: true, font: "Calibri", size: 21, color });
const T = (t, color=INK) => new TextRun({ text: t, font: "Calibri", size: 21, color });
const bullet = (runs, opts={}) => new Paragraph({ bullet: { level: 0 }, spacing: { after: 70, line: 270 }, ...opts,
  children: (Array.isArray(runs)?runs:[runs]).map(r => typeof r==="string"?new TextRun({text:r,font:"Calibri",size:21,color:INK}):r) });

const cell = (runs, { w, shade, bold, color, align } = {}) => new TableCell({
  width: { size: w, type: WidthType.DXA },
  shading: shade ? { type: ShadingType.CLEAR, fill: shade, color: "auto" } : undefined,
  margins: { top: 60, bottom: 60, left: 110, right: 110 },
  children: [ new Paragraph({ alignment: align || AlignmentType.LEFT, spacing:{after:0,line:264},
    children: (Array.isArray(runs)?runs:[runs]).map(r => typeof r === "string"
      ? new TextRun({ text: r, font: "Calibri", size: 19, color: color||INK, bold: !!bold }) : r) }) ]
});
const headRow = (cells, widths) => new TableRow({ tableHeader: true,
  children: cells.map((c,i)=>cell(c,{w:widths[i],shade:NAVY,bold:true,color:"FFFFFF"})) });
const row = (cells, widths, shade) => new TableRow({
  children: cells.map((c,i)=>cell(Array.isArray(c)?c:[c],{w:widths[i],shade})) });
const table = (widths, rows) => new Table({
  width: { size: widths.reduce((a,b)=>a+b,0), type: WidthType.DXA },
  columnWidths: widths,
  borders: ["top","bottom","left","right","insideHorizontal","insideVertical"].reduce((o,k)=>
    (o[k]={style:BorderStyle.SINGLE,size:4,color:RULE},o),{}),
  rows
});

const rule = () => new Paragraph({ spacing:{after:120}, border:{ bottom:{ style:BorderStyle.SINGLE, size:6, color:GOLD } }, children:[] });

const W = [3300, 2600, 1500, 2000]; // gates table
const WP = [3400, 1400, 3800];       // poppler table
const WH = [6300, 3100];             // hashes table

const doc = new Document({
  creator: "The Density Group",
  title: "Keep the Proof v1.0.1 — Release Readiness & QA Sign-off",
  styles: { default: { document: { run: { font: "Calibri", size: 21, color: INK } } } },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1200, bottom: 1100, left: 1200, right: 1200 } } },
    children: [
      new Paragraph({ spacing:{after:20}, children:[ new TextRun({ text:"KEEP THE PROOF", color:GOLD, bold:true, font:"Calibri", size:20, characterSpacing: 40 }) ] }),
      new Paragraph({ spacing:{after:40}, children:[ new TextRun({ text:"Release Readiness & QA Sign-off", color:NAVY, bold:true, font:"Calibri", size:40 }) ] }),
      new Paragraph({ spacing:{after:60}, children:[ new TextRun({ text:"Internal build RC5  ·  Public version 1.0.1 (unpublished)  ·  Prepared 2026-08-21", color:MUTE, font:"Calibri", size:20 }) ] }),
      rule(),

      P([ B("Status: RELEASE-READY. ", GREEN), T("Both QA release gates are passed. No open release blocker remains on the QA side. Nothing has been published — final publication remains a deliberate owner action.") ]),

      H("Release gates"),
      table(W, [
        headRow(["Gate","Requirement","Status","Confirmed"], W),
        row([[B("1  Adobe acceptance")], "Interactive field-capacity acceptance in Adobe Acrobat Reader", [B("PASSED", GREEN)], "2026-08-21"], W),
        row([[B("2  Poppler 26.05+")], "Page 37 renders correctly on Poppler 26.05 or later", [B("PASSED", GREEN)], "2026-08-21"], W),
      ]),
      P([ T("Both product PDFs are unchanged throughout this QA cycle (byte-identical, hashes below). ") ], { spacing:{before:120, after:120} }),

      H("Gate 1 — Adobe Acrobat Reader field-capacity acceptance"),
      P("The product owner ran the manual acceptance test on both RC5 PDFs in Adobe Acrobat Reader and confirmed:"),
      bullet("Long multiline entries and short fields accept their intended input;"),
      bullet("Saving, closing, and reopening preserve the values exactly;"),
      bullet("Fields remain editable; and handbook page 37 renders correctly."),
      P([ T("This closes the interactive typeability question that earlier programmatic tests could not establish. Underlying correction: every fillable field previously inherited ReportLab's default "), B("/MaxLen 100"), T("; RC5 assigns a deliberate per-field capacity (full narrative / evidence ≥ 300, medium ≥ 180, verifier / confidentiality / support ≥ 140, short metadata sized per field), corrected at source. All 142 fields persist their full intended-length value after save and reopen with zero truncation.") ]),

      H("Gate 2 — Poppler 26.05+ page-37 rendering"),
      P([ T("The local build environment caps Poppler at 24.02, so the gate was exercised in CI: a GitHub Actions job in an Arch Linux container running "), B("Poppler 26.07.0"), T(" — at or beyond the reported failing version — rendered the shipped RC5 handbook page 37 in every mode and compared the content top edge and bounding box against the approved PyMuPDF reference (top = 156 px at 150 dpi).") ]),
      table(WP, [
        headRow(["Render mode (Poppler 26.07.0)","Top edge","Result"], WP),
        row(["Blank — whole document","155 px", [B("OK (within 1px)",GREEN)]], WP),
        row(["Blank — pdfseparate true isolation","155 px", [B("OK (within 1px)",GREEN)]], WP),
        row(["Blank — annotations hidden (control)","155 px", [B("OK (within 1px)",GREEN)]], WP),
        row(["Stress-filled — whole document","155 px", [B("OK (within 1px)",GREEN)]], WP),
        row(["Stress-filled — pdfseparate true isolation","155 px", [B("OK (within 1px)",GREEN)]], WP),
      ]),
      P([ B("VERDICT: PASS", GREEN), T(". The page-37 heading and top content sit at the reference position in every mode; bounding box within 1 px (antialiasing floor). No clipping, no shift — whole-document or isolated, blank or filled, annotations on or off. (CI run 32530971761; result recorded in KEEP_THE_PROOF_v1.0.1_POPPLER_26_PAGE37_RESULT.txt.)") ], { spacing:{before:120} }),

      H("Customer deliverables"),
      P([ B("Customer bundle: "), T("KEEP_THE_PROOF_CUSTOMER_BUNDLE_v1.0.1.zip — contains exactly three purchaser-facing files and nothing else:") ], { keepNext: true }),
      bullet("Keep_the_Proof_A_60_Minute_Career_Evidence_System_v1.0.1_FINAL.pdf  (handbook, 41 pages)", { keepNext: true }),
      bullet("Keep_the_Proof_Career_Evidence_Ledger_v1.0.1_FINAL.pdf  (ledger, 12 pages)", { keepNext: true }),
      bullet("KEEP_THE_PROOF_START_HERE_v1.0.1.pdf  (one-page orientation)", { keepNext: true }),
      P([ T("The plain-text README was replaced by the designed one-page "), B("Start Here"), T(" PDF (handbook visual language). No source, QA, or internal materials are in the bundle.") ]),

      H("SHA-256 — customer-facing files"),
      table(WH, [
        headRow(["File","SHA-256 (abbrev.)"], WH),
        row(["Handbook PDF", [new TextRun({text:"7ee951ce…bcf78c2a", font:"Consolas", size:17, color:INK})]], WH),
        row(["Career Evidence Ledger PDF", [new TextRun({text:"259315b0…f8717f81", font:"Consolas", size:17, color:INK})]], WH),
        row(["Start Here PDF", [new TextRun({text:"5cfc6f0f…c1f9f2fc", font:"Consolas", size:17, color:INK})]], WH),
        row(["Customer bundle ZIP", [new TextRun({text:"d2e4030d…d98cbc87", font:"Consolas", size:17, color:INK})]], WH),
      ]),
      P([ T("Both product PDF hashes are unchanged since RC5; the Start Here PDF and bundle are new.") ], { spacing:{before:100} }),

      H("Recommendation"),
      P([ B("RC5 v1.0.1 is release-ready. "), T("Both QA gates are passed and there is no open release blocker. Recommended next step is the owner's deliberate publication action (website download link and Gumroad delivery). Publication has intentionally not been performed.") ]),

      H("Notes"),
      bullet([ B("Scope of the Poppler test: "), T("the shipped RC5 build (which carries the appearance-clip mitigation) renders correctly on Poppler 26.07. The superseded pre-mitigation RC3 file was not separately rendered on 26.07, so whether that original would have clipped there is not established — moot for release, since the shipped build passes.") ]),
      bullet([ B("CI font note: "), T("Poppler logged “couldn't find a font for 'Helvetica'” while rasterizing form-field text, because the minimal CI container lacks a Helvetica substitute. Helvetica is a PDF base-14 standard font present in Adobe Reader and normal installs; it is a container note, not a product issue, and did not affect page-37 layout.") ]),
      bullet([ B("Version & distribution: "), T("public version remains 1.0.1, unpublished; no website, Gumroad, YouTube, email, or social change was made in this cycle.") ]),
    ]
  }]
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(process.argv[2], buf);
  console.log("wrote", process.argv[2], buf.length, "bytes");
});
