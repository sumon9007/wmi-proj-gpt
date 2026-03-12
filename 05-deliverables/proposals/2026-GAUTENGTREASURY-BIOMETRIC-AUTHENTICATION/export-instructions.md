# Export Instructions

## Source Document

Use:

- `/home/suruz/claude-workspace/01-PROJECTS/wmi-proj-gpt/05-deliverables/proposals/2026-GAUTENGTREASURY-BIOMETRIC-AUTHENTICATION/draft/proposal.md`
- Export helper:
  - `/home/suruz/claude-workspace/01-PROJECTS/wmi-proj-gpt/09-automation/export-proposal-docx.sh`
  - `/home/suruz/claude-workspace/01-PROJECTS/wmi-proj-gpt/09-automation/export-proposal-pdf.sh`

## Branding Assets

Use these logo files if present:

- bidder logo:
  - `/home/suruz/claude-workspace/01-PROJECTS/wmi-proj-gpt/05-deliverables/proposals/2026-GAUTENGTREASURY-BIOMETRIC-AUTHENTICATION/attachments/branding/bidder-logo.svg`
  - or `/home/suruz/claude-workspace/01-PROJECTS/wmi-proj-gpt/05-deliverables/proposals/2026-GAUTENGTREASURY-BIOMETRIC-AUTHENTICATION/attachments/branding/bidder-logo.png`
- customer logo:
  - `/home/suruz/claude-workspace/01-PROJECTS/wmi-proj-gpt/05-deliverables/proposals/2026-GAUTENGTREASURY-BIOMETRIC-AUTHENTICATION/attachments/branding/customer-logo.svg`
  - or `/home/suruz/claude-workspace/01-PROJECTS/wmi-proj-gpt/05-deliverables/proposals/2026-GAUTENGTREASURY-BIOMETRIC-AUTHENTICATION/attachments/branding/customer-logo.png`

## Export Rules

- The export script replaces the logo placeholders at the top of `draft/proposal.md` with actual embedded images when logo files exist.
- Prefer `svg` logos over `png` if both exist.
- Keep proportions intact and do not stretch logos.
- Use a clean title page layout with both bidder and customer branding visible.
- Preserve markdown heading hierarchy and section numbering.
- Keep page breaks between major sections where helpful in Word formatting.

## Recommended Command

After installing `pandoc`, run:

```bash
./09-automation/export-proposal-docx.sh
```

For PDF export, run:

```bash
./09-automation/export-proposal-pdf.sh
```

## Output Targets

Create exports as:

- Word:
  - `/home/suruz/claude-workspace/01-PROJECTS/wmi-proj-gpt/05-deliverables/exports/docx/2026-GAUTENGTREASURY-BIOMETRIC-AUTHENTICATION-proposal-draft.docx`
- PDF:
  - `/home/suruz/claude-workspace/01-PROJECTS/wmi-proj-gpt/05-deliverables/exports/pdf/2026-GAUTENGTREASURY-BIOMETRIC-AUTHENTICATION-proposal-draft.pdf`

## Final Check Before Export

- Confirm both logo files exist
- Confirm no placeholder text remains that should be replaced
- Confirm diagrams and attachments are included or clearly marked as pending
- Confirm the latest draft file is being exported
