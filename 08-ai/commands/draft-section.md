# Command: Draft Individual Proposal Section

## Purpose

Draft a single proposal section that is aligned to the RFP, consistent with the overall proposal, and ready to be assembled into the full response.

## Prerequisites

- Relevant content module in `/08-ai/content-modules/` if one exists for the section
- `/05-deliverables/proposals/{RFP-ID}/requirement-mapping.md`
- `/PROJECT_CONTEXT.md`
- `/CUSTOMER_PROFILE.md`
- `/BIDDER_PROFILE.md`
- Relevant analysis in `/02-analysis/`
- Relevant solution documents in `/03-solution/` if available
- Existing proposal draft in `/05-deliverables/proposals/{RFP-ID}/draft/proposal.md` if available

The response library is optional. Use it only if suitable examples actually exist.

## Instructions for Claude

You are a senior proposal writer and solution architect.

### Objective

Write one proposal section that is customer-ready, requirement-aware, and consistent with the rest of the proposal package.

### Parameters

You may be provided with:

- `section_name` — for example `Executive Summary`, `Solution Architecture`, or `Implementation Approach`
- `rfp_requirements` — relevant requirement IDs or requirement statements for that section
- `engagement_type`
- `customer_industry`
- `customer_specific_details`

If some parameters are missing, derive them from the existing project files instead of stopping.

### Read

1. `/05-deliverables/proposals/{RFP-ID}/requirement-mapping.md`
2. `/PROJECT_CONTEXT.md`
3. `/CUSTOMER_PROFILE.md`
4. `/BIDDER_PROFILE.md`
5. `/02-analysis/`
6. `/03-solution/`
7. `/05-deliverables/proposals/{RFP-ID}/draft/proposal.md` if present
8. `/08-ai/content-modules/{section_name}.md` if a matching module exists
9. `/11-response-library/` only if a clearly relevant example exists

### Output

Create:

- `/05-deliverables/proposals/{RFP-ID}/sections/{NN-section-name}.md`

Use numbered section filenames that match the proposal flow where possible, for example:

- `01-executive-summary.md`
- `02-customer-challenges.md`
- `03-proposed-solution.md`
- `04-solution-architecture.md`
- `05-security-and-compliance.md`
- `06-implementation-approach.md`
- `07-assumptions-and-dependencies.md`
- `08-benefits-and-outcomes.md`
- `09-next-steps.md`

### Tasks

1. **Determine the Right Scope for the Section**
   - Use the requirement mapping to identify what the section must cover.
   - Keep ownership clear: the section should fully address its assigned requirements without absorbing unrelated content.

2. **Use the Best Available Source Structure**
   - Start from the matching content module if it exists and is useful.
   - If no module exists, derive structure from the proposal template and requirement mapping.

3. **Draft from Real Project Context**
   - Use the customer context, RFP analysis, solution pack, and delivery plan.
   - Use the bidder profile when the section should reflect company capability, experience, delivery approach, or qualifications.
   - Use customer terminology from the tender and existing project documents.
   - Avoid invented claims, invented metrics, and generic filler.

4. **Reuse Existing Proposal Content Carefully**
   - If the full proposal draft already contains a strong version of the section, improve and normalize it rather than rewriting from scratch.
   - Keep terminology, tone, and assumptions consistent with the assembled draft.

5. **Use the Response Library Only When Helpful**
   - If no relevant example exists, do not force it.
   - Never copy long passages directly.
   - Adapt patterns, not wording.

6. **Call Out Supporting Visuals Where Useful**
   - Add simple placeholders such as `[Diagram: Logical Architecture]` only when they genuinely help.
   - Prefer references to the actual diagram spec documents when available.

7. **Check Section Quality**
   - Ensure the section reads well on its own.
   - Ensure it supports the overall proposal narrative.
   - Ensure it addresses the relevant tender requirements explicitly or obviously.

### Output Format

- Standard markdown
- Clear heading hierarchy
- Tables only where they improve clarity
- Diagram callouts only where useful
- No unresolved placeholders unless explicitly marked as draft notes

### Quality Checks

- [ ] Relevant RFP requirements are addressed
- [ ] Language matches customer and tender terminology
- [ ] Section is consistent with proposal draft, solution pack, and delivery plan
- [ ] No unsupported claims or invented facts
- [ ] Tone is professional, clear, and public-sector appropriate
- [ ] File naming matches proposal section order

### Notes for Claude

- Draft sections so they can be assembled with minimal cleanup.
- Prefer concrete, traceable statements over persuasive fluff.
- If the section depends on open assumptions, state them cleanly rather than hiding them.
- Keep the section scoped; do not let one section become the entire proposal.
