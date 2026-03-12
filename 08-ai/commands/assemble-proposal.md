# Command: Assemble Proposal from Sections

## Purpose

Combine drafted proposal sections into a single proposal document that is coherent, requirement-aligned, and ready for review.

## Prerequisites

- Drafted section files in `/05-deliverables/proposals/{RFP-ID}/sections/` if available
- `/05-deliverables/proposals/{RFP-ID}/requirement-mapping.md`
- `/PROJECT_CONTEXT.md`
- `/CUSTOMER_PROFILE.md`
- `/BIDDER_PROFILE.md`
- Relevant analysis outputs in `/02-analysis/`
- `/08-ai/templates/proposal-template.md`

`metadata.yml` is helpful if present, but not required. If it is missing, derive title, customer, and tender details from the existing project files.

## Instructions for Claude

You are a senior proposal manager and technical editor.

### Objective

Assemble the proposal into a single customer-ready markdown document that reads as one narrative, not a stack of disconnected sections.

### Read

1. `/05-deliverables/proposals/{RFP-ID}/sections/` — drafted section files
2. `/05-deliverables/proposals/{RFP-ID}/requirement-mapping.md`
3. `/02-analysis/rfp-analysis/`
4. `/02-analysis/customer-analysis/`
5. `/02-analysis/delivery-analysis/`
6. `/PROJECT_CONTEXT.md`
7. `/CUSTOMER_PROFILE.md`
8. `/BIDDER_PROFILE.md`
9. `/08-ai/templates/proposal-template.md`
10. `/05-deliverables/proposals/{RFP-ID}/metadata.yml` if present

### Output

Create:

- `/05-deliverables/proposals/{RFP-ID}/draft/proposal.md`

### Tasks

1. **Assemble in Template Order**
   - Use the proposal template as the default section order.
   - If section files already exist, preserve their strongest content.
   - If a section is missing, create a concise but complete draft using the analysis and requirement mapping.

2. **Create Front Matter**
   - Proposal title
   - Customer name
   - Tender / RFP number
   - Date
   - Confidentiality marker
   - Document status

3. **Create a Markdown Table of Contents**
   - Use section headings without pretending to know final page numbers.
   - Keep it clean and useful for review.

4. **Unify Voice and Terminology**
   - Standardize customer naming, solution naming, and requirement language.
   - Use bidder information consistently where company experience, implementation approach, or support capability is relevant.
   - Remove placeholder text and duplicated claims.
   - Keep tone professional, confident, and public-sector appropriate.

5. **Preserve Requirement Coverage**
   - Cross-check the assembled draft against `requirement-mapping.md`.
   - Ensure all critical requirements are covered somewhere in the proposal body or appendices.
   - Do not paste the full requirement matrix into the main body; summarize it and attach a focused appendix.

6. **Add Only Helpful Transitions**
   - Add short bridging text where needed.
   - Do light editing for flow, not heavy rewriting without reason.

7. **Build Practical Appendices**
   - Appendix A: Requirement Mapping Summary
   - Appendix B: Assumptions and Dependencies
   - Appendix C: Team and Delivery Evidence placeholders if the detailed content is not yet drafted
   - Appendix D: References placeholder if reference material is not yet drafted

8. **Flag Gaps Clearly**
   - If important sections are still missing source content, note this briefly in a `Draft Notes` section at the end.
   - Do not hide missing inputs behind generic filler.

### Output Structure

The assembled `proposal.md` should normally contain:

1. Title / front matter
2. Table of contents
3. Executive Summary
4. Customer Challenges
5. Proposed Solution
6. Solution Architecture
7. Security and Compliance Considerations
8. Implementation Approach
9. Assumptions and Dependencies
10. Benefits and Outcomes
11. Next Steps
12. Appendices

Use markdown headings and horizontal rules where helpful. Do not simulate pagination.

### Quality Checks

- [ ] Reads as a unified proposal, not pasted fragments
- [ ] Uses consistent customer and solution terminology
- [ ] Covers all high-priority RFP requirements
- [ ] Aligns with the requirement mapping
- [ ] No unresolved placeholders remain unless explicitly marked as draft placeholders
- [ ] Architecture, security, implementation, and commercial constraints are all addressed
- [ ] Appendix content is useful and not redundant

### Notes for Claude

- Assembly is a synthesis step, not a blind merge.
- Prefer clarity and flow over verbosity.
- If sections are missing, draft them from analysis rather than stopping.
- Be especially careful with public-sector constraints such as compliance, hosting, licensing, IP ownership, and mandatory submission items.
