const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, BorderStyle, ShadingType,
  LevelFormat, PageOrientation,
} = require('docx');

const NAVY = '0F2347';
const GOLD = 'B8952E';
const MUTED = '5A6478';
const CONTENT = 9360;          // 12240 letter width less two 1440 margins
const HAIR = { style: BorderStyle.SINGLE, size: 4, color: 'D8D2C6' };

const p = (text, opts = {}) => new Paragraph({
  spacing: { after: opts.after ?? 140, line: 300 },
  alignment: opts.align,
  children: [new TextRun({
    text, font: 'Calibri', size: opts.size ?? 22,
    color: opts.color ?? '20242C', bold: opts.bold, italics: opts.italics,
  })],
});

const h = (text, level) => new Paragraph({
  heading: level,
  spacing: { before: level === HeadingLevel.HEADING_1 ? 360 : 280, after: 140 },
  children: [new TextRun({
    text, font: 'Calibri', bold: true, color: NAVY,
    size: level === HeadingLevel.HEADING_1 ? 30 : 25,
  })],
});

const bullet = text => new Paragraph({
  numbering: { reference: 'dots', level: 0 },
  spacing: { after: 100, line: 300 },
  children: [new TextRun({ text, font: 'Calibri', size: 22, color: '20242C' })],
});

const cell = (text, { bold, width, head } = {}) => new TableCell({
  width: { size: width, type: WidthType.DXA },
  margins: { top: 90, bottom: 90, left: 140, right: 140 },
  shading: head ? { type: ShadingType.CLEAR, fill: 'F5F0E8', color: 'auto' } : undefined,
  borders: { top: HAIR, bottom: HAIR, left: HAIR, right: HAIR },
  children: [new Paragraph({
    spacing: { after: 0, line: 280 },
    children: [new TextRun({
      text, font: 'Calibri', size: 21,
      bold: bold || head, color: head ? NAVY : '20242C',
    })],
  })],
});

const table = (cols, rows) => new Table({
  columnWidths: cols,
  width: { size: CONTENT, type: WidthType.DXA },
  rows: rows.map((r, i) => new TableRow({
    tableHeader: i === 0,
    children: r.map((t, k) => cell(t, { width: cols[k], head: i === 0, bold: i > 0 && k === 0 })),
  })),
});

const rule = () => new Paragraph({
  spacing: { before: 60, after: 240 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: GOLD } },
  children: [],
});

const doc = new Document({
  creator: 'Temidayo Afonja',
  title: 'START HERE carousel: delivery and QA report',
  numbering: {
    config: [{
      reference: 'dots',
      levels: [{
        level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 360, hanging: 240 } } },
      }],
    }],
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840, orientation: PageOrientation.PORTRAIT },
        margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 },
      },
    },
    children: [
      new Paragraph({
        spacing: { after: 60 },
        children: [new TextRun({
          text: 'START HERE CAROUSEL', font: 'Calibri', bold: true,
          size: 18, color: GOLD, characterSpacing: 60,
        })],
      }),
      new Paragraph({
        spacing: { after: 100 },
        children: [new TextRun({
          text: 'Delivery and QA report', font: 'Calibri', bold: true, size: 40, color: NAVY,
        })],
      }),
      p('Does What You Have Already Done Still Count? LinkedIn Featured document carousel, eight slides, 1080 x 1350 portrait.',
        { color: MUTED }),
      p('Temidayo Afonja | Capability Formation', { color: MUTED, size: 20 }),
      rule(),

      h('What was delivered', HeadingLevel.HEADING_1),
      p('Everything sits in the repository at linkedin-start-here-carousel/.'),
      table([4060, 5300], [
        ['File', 'What it is'],
        ['LinkedIn_Start_Here_Capability_Formation.pdf', 'The upload file. Eight pages, vector text, 810 by 1013 points.'],
        ['slides/slide-01.png to slide-08.png', 'One preview per slide at 1080 by 1350.'],
        ['contact-sheet.png', 'All eight slides in order.'],
        ['source/copy.json', 'Editable copy, exactly as supplied in the brief.'],
        ['source/carousel.html', 'Editable layout. Live DOM text, no outlined type.'],
        ['source/build-carousel.mjs', 'Renders the PNGs, the PDF and the contact sheet.'],
        ['source/verify-carousel.mjs', 'The quality gate.'],
      ]),
      p('To rebuild after a copy edit, run build-carousel.mjs and then verify-carousel.mjs.',
        { after: 200 }),

      h('Design system', HeadingLevel.HEADING_1),
      p('Canvas 1080 by 1350 with 96 pixel margins on all four sides. Cream forward, with a single deep navy closing slide.'),
      p('Palette: navy 0F2347, cream F5F0E8, gold C9A84C on navy and B8952E on cream, rust C1440E for the short rules, and the bright warm yellow F2C44C used once, on the closing slide.'),
      p('Type is Cormorant Garamond for display and DM Sans for body, labels and navigation. Both are self hosted in the repository and both are the faces the Career Evidence Starter itself uses.'),
      p('Navigation is a gold ringed page number at the bottom right of every slide, with an arrow on slide one only.'),
      p('The portrait is the real photograph at images/temidayo-gold-ivory.png, circularly cropped and placed once, on slide one, at 264 pixels. It is scaled down from 1254 pixels and never up. Nothing about the photograph is altered.',
        { after: 200 }),

      h('What was missing from the workspace', HeadingLevel.HEADING_1),
      p('Three things the brief refers to were not present. None was invented or substituted.'),
      bullet('The carousel foundation build kit. It lived outside the repository and this container was reset, so the files were gone. The system was rebuilt from its specification as established earlier in this project: canvas, margins, type pairing, palette, circular portrait treatment, gold ringed counter, and the render and verify export process. The original was not overwritten, because there was nothing left to overwrite.'),
      bullet('The Density Group logo files. Also lost with that directory. No logo appears on these slides, because redrawing or approximating one is not acceptable. The footer supplied in the brief carries the attribution on the closing slide. Send the logo zip and it drops into the template in one edit.'),
      bullet('final 3(1).pdf. Not in the workspace or the uploads, so it could not be used as a starting point. The carousel is built from the slide sequence and copy supplied in the brief.'),
      p('', { after: 60 }),

      h('One palette decision', HeadingLevel.HEADING_1),
      p('The brief names navy 112345 and cream F5F1E8. The real Capability Formation artifacts, including the Career Evidence Starter, are drawn in 0F2347 and F5F0E8, which is what these slides use, so the carousel sits beside the existing assets without a visible shade mismatch. The two cream values differ by one unit in the green channel and are indistinguishable.'),
      p('Gold is C9A84C exactly as specified wherever it sits on navy. On cream it drops to B8952E, the brand value for gold on a light field, because C9A84C measures about 2 to 1 against cream and is too weak for small labels.'),
      p('Both are one word away from being re-rendered on the values in the brief.', { after: 200 }),

      h('QA results', HeadingLevel.HEADING_1),
      p('All checks below are automated in source/verify-carousel.mjs and currently pass. Every slide was also rendered and inspected.'),
      table([4600, 4760], [
        ['Check', 'Result'],
        ['Copy is exact', 'Every line on every slide matches copy.json, which is the brief transcribed verbatim.'],
        ['No em dashes', 'Zero em dash and en dash characters in the slides, the copy file and this package.'],
        ['No font substitution', 'Cormorant Garamond and DM Sans both confirmed loaded at render time, not substituted.'],
        ['No clipped text', 'No text element overflows its column on any slide.'],
        ['Safe placement', 'No text sits outside the 96 pixel safe area on any slide.'],
        ['Legible on mobile', 'Body type is 34 pixels, about 13 pixels at LinkedIn mobile width. The smallest type is 21 pixels, the counter and footer, about 8 pixels.'],
        ['Imagery not blurred', 'The portrait is shown at 264 pixels from a 1254 pixel original. It is never upscaled.'],
        ['Consistent spacing', 'All eight slides share one grid: 96 pixel margins, one rule width, one counter position.'],
        ['PDF opens correctly', 'Eight pages at 810 by 1013 points, which is 1080 by 1350 pixels.'],
        ['Exports', 'Eight slide PNGs between 52 and 140 KB. The PDF is 2.8 MB, carrying the portrait at full resolution.'],
      ]),
      p('', { after: 60 }),

      h('Open items', HeadingLevel.HEADING_1),
      bullet('Send the Density Group logo zip if you want the mark on the slides.'),
      bullet('Confirm the palette decision above, or ask for a re-render on 112345 and F5F1E8.'),
      bullet('Send final 3(1).pdf if it holds anything that should be carried into this carousel.'),
    ],
  }],
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync('START_HERE_Carousel_Report.docx', buf);
  console.log('wrote START_HERE_Carousel_Report.docx', buf.length, 'bytes');
});
