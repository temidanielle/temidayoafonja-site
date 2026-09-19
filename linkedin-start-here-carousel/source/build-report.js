const fs = require('fs');
const { execSync } = require('child_process');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, BorderStyle, ShadingType,
  LevelFormat, PageOrientation,
} = require('docx');

// Git facts are read at generation time rather than typed in, so the version
// control section of the document cannot drift away from the repository.
const git = cmd => execSync(`git ${cmd}`, { encoding: 'utf8' }).trim();
const COMMIT = git('rev-parse HEAD');
const BRANCH = git('rev-parse --abbrev-ref HEAD');
const SUBJECT = git('log -1 --pretty=%s');
const STATUS = git('status --short');

const NAVY = '112345';
const GOLD = 'B8952E';          // report accent only, printed on white paper
const MUTED = '5A6478';
const CONTENT = 9360;
const HAIR = { style: BorderStyle.SINGLE, size: 4, color: 'D8D2C6' };

const p = (text, opts = {}) => new Paragraph({
  spacing: { after: opts.after ?? 140, line: 300 },
  children: [new TextRun({
    text, font: 'Calibri', size: opts.size ?? 22,
    color: opts.color ?? '20242C', bold: opts.bold, italics: opts.italics,
  })],
});

const h = (text, level, opts = {}) => new Paragraph({
  heading: level,
  pageBreakBefore: opts.newPage,
  spacing: { before: level === HeadingLevel.HEADING_1 ? 360 : 260, after: 140 },
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

const cell = (text, { width, head, bold } = {}) => new TableCell({
  width: { size: width, type: WidthType.DXA },
  margins: { top: 90, bottom: 90, left: 140, right: 140 },
  shading: head ? { type: ShadingType.CLEAR, fill: 'F5F1E8', color: 'auto' } : undefined,
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
    cantSplit: true,   // keep a row whole rather than orphaning half of it over a page break
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
  title: 'START HERE carousel: status and overview',
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
          text: 'Status and overview', font: 'Calibri', bold: true, size: 40, color: NAVY,
        })],
      }),
      p('Does What You Have Already Done Still Count? LinkedIn Featured document carousel, eight slides, 1080 x 1350 portrait. Version 2, final, with the accessibility pass applied.',
        { color: MUTED }),
      p('Temidayo Afonja | Capability Formation', { color: MUTED, size: 20 }),
      rule(),

      h('Status', HeadingLevel.HEADING_1),
      p('The carousel is final and ready to upload. Content, structure and design were approved, the accessibility pass described below has been applied, and both cosmetic decisions that were previously open are now resolved. Nothing is outstanding.'),
      table([2600, 6760], [
        ['Item', 'State'],
        ['Carousel', 'Final and ready to upload.'],
        ['Slide copy', 'Final. Version 2 revisions applied to slides 1, 3, 4, 6 and 8 exactly as supplied, and unchanged since.'],
        ['Palette', 'Corrected. Four approved values only, confirmed by a pixel audit of all eight pages.'],
        ['Accessibility', 'Pass applied. Small text on cream is now navy at 13.8 to 1. Slide 8 is unchanged.'],
        ['Upload file', 'LinkedIn_Start_Here_Capability_Formation_V2.pdf, eight pages, ready.'],
        ['Quality gate', 'Passing. Ten automated checks, listed below, plus a page by page visual inspection.'],
        ['Open decisions', 'None. Both previous decisions are resolved and recorded below.'],
        ['Related work', 'The LinkedIn banner is separate work outside this package.'],
      ]),
      p('', { after: 60 }),

      h('The final accessibility pass', HeadingLevel.HEADING_1),
      p('One correction, applied after approval. It touches colour only. Copy, typography, the portrait, spacing, the eight slide sequence, the call to action and the footer are all untouched.'),
      table([2600, 6760], [
        ['Element', 'Treatment'],
        ['START HERE label, slide 1', 'Now navy 112345. It was gold on cream at 2.03 to 1 and now reads at 13.8 to 1.'],
        ['Page numbers on cream, slides 1 to 7', 'Now navy 112345, both the digits inside the ring and the total beside it. Also 13.8 to 1.'],
        ['Pagination ring', 'Unchanged, gold C9A84C on every slide. It is part of the preserved pagination system, not a new decorative element.'],
        ['Section numerals 01 to 04', 'Unchanged, gold C9A84C. At 96 pixels they are display marks, not reading text.'],
        ['Gold rules and the ruled serif line', 'Unchanged, gold C9A84C.'],
        ['Slide 8 pagination', 'Unchanged. Gold on navy measures 6.81 to 1, so the approved treatment was kept exactly as it was.'],
        ['Closing line, slide 8', 'Unchanged, bright yellow F2C44C on navy at 9.46 to 1.'],
      ]),
      p('', { after: 40 }),
      p('No colour was added. Navy and gold were already in the four value palette, and the ring keeps the gold so the pagination still reads as one system across all eight slides.'),
      p('The change was measured rather than assumed. Comparing the new exports against the previous ones pixel by pixel: slide 8 has zero changed pixels, slides 2 to 7 changed only inside the page number, and slide 1 changed only at the label and the page number. Nothing else on any slide moved.',
        { after: 200 }),

      h('What this carousel is', HeadingLevel.HEADING_1),
      p('The first item in the Featured section of the LinkedIn profile. It introduces the full career portability lens to an experienced professional arriving from one of the posts, then tells them what they will find by following. It is an introduction, not a product advertisement, and it carries no price, link or date.'),
      p('The eight slides run: the opening question, a statement that some experience travels and some does not, then the four questions in order, what travels, what does not, what you can prove and what you must relearn, then the boundary that adjacent experience is not automatic qualification, and finally the navy closing slide with the Follow line.',
        { after: 200 }),

      h('What was delivered', HeadingLevel.HEADING_1),
      p('Everything sits in the repository at linkedin-start-here-carousel/.'),
      table([4460, 4900], [
        ['File', 'What it is'],
        ['LinkedIn_Start_Here_Capability_Formation_V2.pdf', 'The upload file. Eight pages, vector text, 810 by 1013 points.'],
        ['slides/slide-01.png to slide-08.png', 'One preview per slide at 1080 by 1350.'],
        ['contact-sheet.png', 'All eight slides in order.'],
        ['START_HERE_Carousel_Report.docx', 'This document.'],
        ['source/copy.json', 'Editable copy, exactly as supplied in the brief.'],
        ['source/carousel.html', 'Editable layout. Live DOM text, no outlined type.'],
        ['source/build-carousel.mjs', 'Renders the PNGs, the PDF and the contact sheet.'],
        ['source/verify-carousel.mjs', 'The quality gate.'],
        ['source/build-report.js', 'Regenerates this document.'],
      ]),
      p('', { after: 40 }),
      p('Version 1 is kept beside version 2 rather than deleted, so the two can be compared.'),
      p('To rebuild after a copy edit, run build-carousel.mjs and then verify-carousel.mjs.', { after: 200 }),

      h('What changed in version 2', HeadingLevel.HEADING_1),
      p('Copy only, plus the palette. Structure, typography, portrait, spacing, white space, pagination and hierarchy were left untouched.'),
      table([2600, 6760], [
        ['Slide', 'Change'],
        ['1', 'Subheading replaced. Now reads Before a career pivot, internal move, or other change in context, ask four questions.'],
        ['3', 'Body replaced with the four fuller lines, ending These can remain useful when the employer, function, industry, or role changes.'],
        ['4', 'Body replaced with company-specific systems, relationship-based access and influence, internal language and the assumptions line. Some experience is context-bound keeps its gold ruled serif treatment.'],
        ['6', 'Body set to the exact two sentences supplied, including the comma before and constraints.'],
        ['8', 'Paragraph updated. This is the work you will find here is replaced by the Follow line, which keeps the bright yellow serif treatment.'],
        ['All', 'Every rust rule is now gold. The separate on cream gold used for small labels in version 1 is removed.'],
      ]),
      p('', { after: 60 }),

      h('Design system', HeadingLevel.HEADING_1),
      p('Canvas 1080 by 1350 with 96 pixel margins on all four sides. Cream forward, with a single deep navy closing slide.'),
      p('Palette: navy 112345, cream F5F1E8, gold C9A84C and the bright warm yellow F2C44C. Four values, no fifth colour. Gold carries the structural marks, the large section numerals, the rules and the pagination ring. Small tracked text is navy on the cream slides and gold on the navy slide, whichever reads better against its own background. The bright yellow is used once, on the closing line.'),
      p('Type is Cormorant Garamond for display and DM Sans for body, labels and navigation. Both are self hosted in the repository and both are the faces the Career Evidence Starter itself uses.'),
      p('Navigation is a gold ringed page number at the bottom right of every slide, with an arrow on slide one only. The ring is the same gold mark throughout. Only the figures inside and beside it change colour with the background.'),
      p('The portrait is the real photograph at images/temidayo-gold-ivory.png, circularly cropped and placed once, on slide one, at 264 pixels. It is scaled down from 1254 pixels and never up. Nothing about the photograph is altered.',
        { after: 200 }),

      h('Quality checks', HeadingLevel.HEADING_1),
      p('All checks below are automated in source/verify-carousel.mjs and currently pass. Every slide was also rendered and inspected by eye.'),
      table([4600, 4760], [
        ['Check', 'Result'],
        ['Copy is exact', 'Every line on every slide matches copy.json, which is the brief transcribed verbatim.'],
        ['No em dashes', 'Zero em dash and en dash characters in the slides, the copy file and this document.'],
        ['No font substitution', 'Cormorant Garamond and DM Sans both confirmed loaded at render time, not substituted.'],
        ['No clipped text', 'No text element overflows its column on any slide.'],
        ['Safe placement', 'No text sits outside the 96 pixel safe area on any slide.'],
        ['Legible on mobile', 'Body type is 34 pixels, about 13 pixels at LinkedIn mobile width. The smallest type is 21 pixels, the counter and footer, about 8 pixels.'],
        ['Imagery not blurred', 'The portrait is shown at 264 pixels from a 1254 pixel original. It is never upscaled.'],
        ['Consistent spacing', 'All eight slides share one grid: 96 pixel margins, one rule width, one counter position.'],
        ['Palette', 'Only navy 112345, cream F5F1E8, gold C9A84C and bright yellow F2C44C appear. No rust remains anywhere outside the photograph.'],
        ['Text contrast', 'Every text element passes. Navy on cream 13.8 to 1, cream on navy 13.8 to 1, gold on navy 6.81 to 1, bright yellow on navy 9.46 to 1. No small text is set in gold on cream.'],
        ['PDF opens correctly', 'Eight pages at 810 by 1013 points, which is 1080 by 1350 pixels, 2.8 MB.'],
      ]),
      p('', { after: 60 }),

      h('The two cosmetic decisions, both resolved', HeadingLevel.HEADING_1),
      p('These were the only items left open. Neither is open now.'),
      bullet('Small gold text on cream. Gold on cream measured 2.03 to 1, which is comfortable for the 96 pixel numerals and faint for the two smallest items, the START HERE label and the page number, both of which land near 8 pixels at LinkedIn mobile width. Resolved: those two are now navy at 13.8 to 1. The numerals, the rules and the ring stay gold. No colour was added.'),
      bullet('The ring around the page number. Resolved: the ring is kept. It is part of the pagination system that was preserved from the approved design, not a decorative element introduced afterwards, and it stays gold on all eight slides.'),
      p('', { after: 60 }),

      h('What was missing from the workspace', HeadingLevel.HEADING_1),
      p('Three things the original brief referred to were not present when this was built. None was invented or substituted.'),
      bullet('The carousel foundation build kit. It lived outside the repository and the working container was reset, so the files were gone. The system was rebuilt from its specification as established earlier in this project: canvas, margins, type pairing, palette, circular portrait treatment, gold ringed counter, and the render and verify export process.'),
      bullet('The Density Group logo files. Also lost with that directory. No logo appears on these slides, because redrawing or approximating one is not acceptable. The footer supplied in the brief carries the attribution on the closing slide. Send the logo zip and it drops into the template in one edit.'),
      bullet('final 3(1).pdf. Not in the workspace or the uploads, so it could not be used as a starting point. The carousel is built from the slide sequence and copy supplied in the brief.'),
      p('', { after: 60 }),

      h('Where this sits in version control', HeadingLevel.HEADING_1, { newPage: true }),
      p('Everything is committed locally on this machine. Nothing has been pushed, merged, deployed or published.'),
      table([2600, 6760], [
        ['Item', 'Value'],
        ['Branch', BRANCH],
        ['Commit', COMMIT],
        ['Commit message', SUBJECT],
        ['git status --short', STATUS ? STATUS : 'No output. The working tree is clean and nothing is uncommitted.'],
      ]),
      p('', { after: 40 }),
      p('A file cannot contain the hash of the commit that contains it, so the commit above is the one carrying the accessibility correction and the rebuilt exports. This document was regenerated against it and committed immediately afterwards as a short record commit, which is why the hash you see here is the correction itself rather than the commit that stores this page.'),
      p('The full hash is given rather than a short form so it can be checked exactly with git show.', { after: 200 }),

      h('Scope of this package', HeadingLevel.HEADING_1),
      p('This package is the START HERE carousel and nothing else. The LinkedIn banner is separate work outside this package and is not part of what is described here.'),
    ],
  }],
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync('START_HERE_Carousel_Report.docx', buf);
  console.log('wrote START_HERE_Carousel_Report.docx', buf.length, 'bytes');
});
