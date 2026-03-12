# Document Naming Conventions

## Purpose

This page captures the preferred naming approach for key proposal and project documents so outputs remain traceable and easy to identify across multiple tenders.

## Proposal Draft Naming

Use tender-specific filenames for assembled proposal drafts instead of generic names.

Preferred format:

- `/05-deliverables/proposals/{RFP-ID}/draft/{RFP-ID}-proposal-draft.md`

Example:

- `/05-deliverables/proposals/2026-GAUTENGTREASURY-BIOMETRIC-AUTHENTICATION/draft/GT-GPT-009-2026-proposal-draft.md`

## Why This Convention Is Better

- avoids ambiguity when multiple tenders exist in the repo
- improves export, review, and automation workflows
- makes generated files self-describing outside their folder context
- helps with archival, packaging, and handover

## Section And Supporting File Conventions

- proposal sections should stay numbered for reading order
- review files should describe their purpose directly
- export files should include both tender context and document state such as `draft` or `final`

## Practical Rule

If a document is likely to be exported, shared, archived, or referenced outside its immediate folder, prefer an explicit tender-aware filename over a generic one.
