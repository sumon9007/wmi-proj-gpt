# Reference Template Notes

This Word reference template is intended for draft and submission-stage proposal exports for Gauteng Provincial Treasury.

## Design Intent

- Present Waymark Infotech as a credible, enterprise-ready systems integrator.
- Give the proposal a public-sector look: formal, controlled, and polished rather than flashy.
- Improve readability for evaluators through justified body text, stronger heading hierarchy, and a cleaner cover layout.

## Visual Direction

- Primary heading color: deep navy for a formal government and enterprise tone.
- Accent line color: muted gold for subtle emphasis on major section breaks.
- Heading font: Cambria to create a more proposal-like document tone.
- Body font: Aptos for clean screen and print readability.
- Cover page: side-by-side bidder and customer logos, centered title, concise metadata block.

## Key Formatting Rules

- Body paragraphs are justified.
- Section headings use stronger spacing and a clearer typographic hierarchy.
- The export script suppresses the markdown placeholder cover content and generates a cleaner Word cover page.
- The template is optimized for Pandoc DOCX export, not manual Word authoring.

## Saved Templates

- `attachments/reference-template.docx`
- `attachments/submission-template.docx`

## Regeneration Notes

- The template can be regenerated with:
  - `python3 09-automation/create-reference-template.py <source.docx> <output.docx>`
- The draft DOCX export uses this template automatically when the file exists.
- The DOCX export is then post-processed to add:
  - a more polished cover-page treatment
  - first-page-only header and footer behavior for the cover
  - improved table styling
  - branded running headers with embedded bidder and customer logos
  - separate draft and final visual variants
  - page numbering
