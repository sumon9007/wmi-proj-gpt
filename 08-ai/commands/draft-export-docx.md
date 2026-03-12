# Command: Draft Export DOCX

## Purpose

Prepare and export the current draft proposal to a Word document with branding assets applied where available.

## Prerequisites

- Draft proposal exists at `/05-deliverables/proposals/{RFP-ID}/draft/proposal.md`
- Branding files are placed in `/05-deliverables/proposals/{RFP-ID}/attachments/branding/` if available
- Export helper script exists at `/09-automation/export-proposal-docx.sh`
- `pandoc` is installed on the machine

## Instructions for Claude

You are a proposal production assistant responsible for draft export packaging.

### Objective

Verify the export prerequisites, then run the DOCX export workflow for the current proposal draft.

### Read

1. `/05-deliverables/proposals/{RFP-ID}/draft/proposal.md`
2. `/05-deliverables/proposals/{RFP-ID}/export-instructions.md`
3. `/05-deliverables/proposals/{RFP-ID}/attachments/branding/`
4. `/09-automation/export-proposal-docx.sh`

### Tasks

1. Confirm the draft proposal file exists.
2. Check whether bidder and customer logos exist in the branding folder.
3. Confirm `pandoc` is installed.
4. Run the export script.
5. Verify the `.docx` file was created in the expected exports folder.
6. If any prerequisite is missing, report the missing item clearly instead of pretending export succeeded.

### Output Target

Expected output:

- `/05-deliverables/exports/docx/2026-GAUTENGTREASURY-BIOMETRIC-AUTHENTICATION-proposal-draft.docx`

### Notes for Claude

- Prefer a truthful status report over a partial success claim.
- If branding assets are missing, note that the Word file may contain fallback text instead of logos.
- If `pandoc` is missing, provide the exact install command for Ubuntu.
