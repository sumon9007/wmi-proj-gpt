Export the current proposal draft to a Word document.

Use:
- `/05-deliverables/proposals/2026-GAUTENGTREASURY-BIOMETRIC-AUTHENTICATION/draft/proposal.md`
- `/05-deliverables/proposals/2026-GAUTENGTREASURY-BIOMETRIC-AUTHENTICATION/export-instructions.md`
- `/09-automation/export-proposal-docx.sh`

Before exporting:
- confirm `pandoc` is installed
- confirm whether the bidder and customer logos exist in `attachments/branding/`
- confirm the draft markdown file exists

Then:
- run the export helper script
- verify that the `.docx` file exists in `/05-deliverables/exports/docx/`

If anything is missing, report the exact blocker and the next command or action needed.
