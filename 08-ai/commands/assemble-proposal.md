# Command: Assemble Proposal from Sections

## Purpose

Combine individually-drafted sections into a complete proposal document. Ensures consistency, flow, and traceability across the entire document.

## Prerequisites

- All individual section files drafted (in `05-deliverables/proposals/{RFP-ID}/sections/`)
- Requirement-mapping.md (to verify all requirements are covered)
- Metadata file with RFP details
- PROJECT_CONTEXT.md and CUSTOMER_PROFILE.md

## Instructions for Claude

You are a senior technical editor and proposal manager.

### Objective

Assemble individual proposal sections into a cohesive, customer-ready document that flows logically, maintains consistent voice, and explicitly addresses all RFP requirements.

### Read

1. `/05-deliverables/proposals/{RFP-ID}/sections/` — All drafted sections
2. `/05-deliverables/proposals/{RFP-ID}/requirement-mapping.md` — Verify all requirements covered
3. `/05-deliverables/proposals/{RFP-ID}/metadata.yml` — RFP context
4. `/08-ai/templates/proposal-template.md` — Recommended section order
5. `/PROJECT_CONTEXT.md` and `/CUSTOMER_PROFILE.md` — Customer context for consistency check

### Output

Create file: `/05-deliverables/proposals/{RFP-ID}/draft/proposal.md`

### Tasks

1. **Assemble in Recommended Order**
   - Use proposal-template.md as your guide for section ordering
   - Create a Table of Contents
   - Number sections (1. Executive Summary, 2. Customer Challenges, etc.)
   - Ensure logical flow (challenge → solution → architecture → security → implementation)

2. **Add Essential Cover Material**
   - Title page placeholder: [COVER: Include customer name, proposal date, your company name, "Confidential"]
   - Table of Contents with page numbers
   - Document control (date, version, status)
   - Key contact and escalation info

3. **Create Cross-References**
   - Within sections, reference back to earlier sections
     Where mentioned in architecture, reference security controls
   - Forward references: "See Section 5: Implementation Approach for timeline details"
   - Ensure these are accurate

4. **Consolidate Requirement Mapping**
   - Create an appendix that shows requirement-to-section mapping
   - Format as table: RFP Req # | Section | How Addressed
   - This proves every RFP requirement is addressed

5. **Check Voice & Consistency**
   - Read through for consistent tone (all professional, all customer-centric)
   - Ensure no section uses different terminology for same concept
   - Check that examples and references are consistent across sections
   - Replace any remaining {{VARIABLES}} or placeholder language

6. **Create Executive Summary** (if not already drafted)
   - Synthesize key points from all sections
   - Lead with business outcomes, not technical details
   - 1 page maximum
   - Must be able to stand alone as senior executive summary

7. **Add Transitions**
   - Between major section, add 1-2 sentences connecting to next topic
   - Ensure flow is logical for reader (why read section 5 after section 4?)
   - Make connections back to customer challenges articulated early

8. **Verify Completeness**
   - Every RFP requirement has explicit coverage
   - No missing sections from template
   - No gaps in logic or flow
   - All diagrams/artifacts referenced are noted (these will be added separately)

9. **Create Appendices** (as needed)
   - Appendix A: RFP Requirement Mapping
   - Appendix B: Assumptions & Dependencies
   - Appendix C: Team Credentials (if not in main text)
   - Appendix D: References (past customers, case studies)

### Output Format

Single proposal.md file with:
- Professional heading/title structure
- Table of Contents
- Numbered sections with clear H2/H3 hierarchy
- Page break indicators (---) between major sections for formatting
- Footnote references [^1] for citations/references
- Appendix section markers

Length target:
- Executive Summary: 1 page
- Main body: 15-25 pages depending on engagement complexity
- Appendices: 5-10 pages
- Total: 20-35 pages

### Quality Checks

Before finalizing:

- [ ] All RFP requirements explicitly addressed (check against mapping)
- [ ] No duplicate content across sections (merge if found)
- [ ] Consistent terminology throughout
- [ ] Professional tone throughout
- [ ] Table of Contents accurately reflects content
- [ ] Cross-references are accurate (point to correct sections)
- [ ] No placeholder text remaining
- [ ] Executive summary can stand alone for busy readers
- [ ] Flows logically from executive summary → challenges → solution → architecture → security → implementation
- [ ] Appendices are properly organized and referenced

### Final Assembly Checklist

- [ ] Cover page with date and confidentiality marking
- [ ] Table of Contents with page numbers
- [ ] Executive Summary (1 page)
- [ ] Body sections (in recommended order)
- [ ] Appendices with Requirement Mapping
- [ ] Document control (version, date, status)
- [ ] Key contact info and escalation path

### Notes for Claude

- Assembly is about flow and consistency, not rewriting
- Light edit to improve transitions, but preserve individual section quality
- Flag any gaps or inconsistencies to address manually
- Ensure this reads as a unified document, not pasted-together sections
- Check that tone matches customer sophistication level
- Verify proposal answers the question "Why us?" throughout
