# Command: Analyze RFP Requirements & Create Mapping

## Purpose

Extract the RFP's explicit requirements and map each one to the proposal section that will answer it. The goal is to create a traceable, reviewable requirement matrix that prevents gaps in the final response.

## Prerequisites

- Primary RFP source material available under `/01-input/rfp/`
- Completed `/PROJECT_CONTEXT.md`
- Completed `/CUSTOMER_PROFILE.md`
- Proposal section structure understood from `/08-ai/templates/proposal-template.md`
- Requirement mapping format available in `/08-ai/templates/requirement-mapping-template.md`

## Instructions for Claude

You are a senior solutions analyst specializing in public-sector RFP response management.

### Objective

Read the source material, extract every relevant requirement, classify it, and map it to the proposal section where it will be addressed.

### Read

1. `/PROJECT_CONTEXT.md`
2. `/CUSTOMER_PROFILE.md`
3. `/01-input/rfp/` — official tender / RFP source files
4. `/01-input/customer-documents/` — supporting customer material, if present
5. `/01-input/submitted-response/` — prior or draft response material, if present
6. `/02-analysis/rfp-analysis/` — existing analysis, if present
7. `/08-ai/templates/requirement-mapping-template.md`
8. `/08-ai/templates/proposal-template.md`

### Output

Create:

- `/05-deliverables/proposals/{RFP-ID}/requirement-mapping.md`

If `{RFP-ID}` is not yet established elsewhere in the repo, derive it from the RFP filename or tender number and use the same value consistently across the deliverables folder.

### Extraction Rules

Treat the following as candidate requirements when stated or clearly implied by the RFP:

- `must`, `shall`, `required`, `will`, `should`, `expected to`
- compliance, security, legal, governance, audit, hosting, support, DR, SLA, training, deliverable, and documentation statements
- evaluation criteria that imply mandatory response content
- customer-owned assumptions or operating constraints that the proposal must acknowledge

Do not invent requirements. Capture what the source material actually says, then normalize wording only enough to make the matrix usable.

### Tasks

1. **Extract Requirements Systematically**
   - Review the RFP section by section.
   - Capture each distinct requirement once.
   - Break broad paragraphs into atomic requirements where useful.
   - Record the source section and page reference where possible.

2. **Normalize and De-duplicate**
   - Merge duplicate requirements that appear in multiple places.
   - Preserve the strongest or most complete wording.
   - Note repeated references in the `Notes` column instead of duplicating rows.

3. **Classify Each Requirement**
   - Functional
   - Non-Functional
   - Compliance / Governance
   - Commercial / Contractual
   - Delivery / Resourcing
   - Documentation / Training

Also mark:

   - `Mandatory` when the RFP language is explicit
   - `Evaluation-Linked` when tied to scoring or bid responsiveness
   - `Ambiguous` when wording is open to interpretation

4. **Map to Proposal Sections**
   - Assign the best-fit proposal section from the proposal template.
   - Prefer 1 primary section and at most 1 supporting section.
   - If a requirement spans multiple sections, keep the main owner clear.

5. **Draft the Response Strategy**
   - Add a short `Our Proposed Approach` entry for each requirement.
   - Keep it specific enough to guide drafting, but not full proposal prose.
   - Flag dependencies, assumptions, or response risks in `Notes`.

6. **Validate Completeness**
   - Check that all major RFP sections have been reviewed.
   - Check that each requirement is mapped to a proposal section.
   - Identify unmapped, conflicting, or risky requirements explicitly.

### Output Structure

Use the structure in `/08-ai/templates/requirement-mapping-template.md`, but make sure the completed file includes:

- RFP name
- RFP ID / tender number
- Created date
- Summary statistics
- A complete requirement mapping table
- Unmapped requirements, if any
- Key risk notes

Where helpful, extend the table content by embedding detail inside existing columns instead of redesigning the template.

### Suggested Status Values

- `Complete` — clear proposal coverage identified
- `Partial` — only partially addressed or dependent on assumptions
- `Dependent` — requires customer clarification, third-party integration, or award-stage confirmation
- `Pending` — requirement identified but proposal coverage not yet assigned
- `Out of Scope` — explicitly outside response scope, with rationale documented

### Quality Checks

- [ ] All relevant RFP sections reviewed
- [ ] Each requirement has a clear source reference
- [ ] Each requirement appears only once in normalized form
- [ ] Each requirement maps to at least one proposal section
- [ ] Mandatory and evaluation-linked requirements are clearly identifiable
- [ ] Ambiguities, contradictions, and dependencies are called out in `Notes`
- [ ] Summary counts are internally consistent

### Notes for Claude

- Prefer inclusion over omission, especially in public-sector tenders.
- Write analysis, not marketing copy.
- Keep requirement text close to the source language.
- Use concise, practical proposal-section mapping names.
- Highlight disqualification risks, compliance obligations, and delivery constraints early.
- If the RFP includes explicit service levels, security controls, IP ownership, licensing, or hosting constraints, make those highly visible in the matrix.
