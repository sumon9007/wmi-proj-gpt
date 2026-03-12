# Command: Analyze RFP Requirements & Create Mapping

## Purpose

Extract all RFP requirements and map them to proposed proposal sections. This creates the traceability matrix that ensures all RFP requirements are answered in your proposal.

## Prerequisites

- RFP document (located in `01-input/rfp/original/`)
- Proposal template understanding (see `08-ai/templates/proposal-template.md`)
- Completed `PROJECT_CONTEXT.md` and `CUSTOMER_PROFILE.md`

## Instructions for Claude

You are a solutions analyst specializing in RFP response strategy.

### Objective

Extract all RFP requirements and create a complete requirement-to-proposal mapping. This ensures every RFP requirement is explicitly answered.

### Read

1. `/01-input/rfp/original/` — The complete RFP document
2. `/08-ai/templates/requirement-mapping-template.md` — The mapping template structure
3. `/08-ai/templates/proposal-template.md` — Standard proposal sections
4. `/PROJECT_CONTEXT.md` — Project context
5. `/02-analysis/rfp-analysis/` — Any existing RFP analysis

### Output

Create file: `/05-deliverables/proposals/{RFP-ID}/requirement-mapping.md`

### Tasks

1. **Extract Requirements**
   - Read the RFP systematically, section by section
   - Identify EVERY stated requirement (marked as "must," "should," "required," "compliance," etc.)
   - List requirements at section-level and detail-level
   - Don't assume intent; extract what's literally stated

2. **Classify Requirements**
   - Mark each as Functional (what the system does) vs. Non-Functional (performance, security, compliance)
   - Identify Critical vs. Nice-to-have
   - Flag any ambiguous or contradictory requirements

3. **Map to Proposal Sections**
   - For each requirement, identify which proposal section should answer it
   - Use standard proposal sections: Executive Summary, Customer Challenges, Solution Overview, Architecture, Security, Implementation, Assumptions
   - Assign 1-2 sections maximum per requirement (if more, requirement is too broad)

4. **Create Traceability Table**
   - Use the structure from `requirement-mapping-template.md`
   - Complete all columns: RFP Section | RFP Requirement # | Requirement Text | Our Approach | Proposal Section | Status

5. **Completeness Check**
   - Every RFP requirement should appear in the table
   - Every requirement should map to at least one proposal section
   - Flag any unmapped requirements (document why in "Notes")

### Output Format

Use the template at `/08-ai/templates/requirement-mapping-template.md`

### Quality Checks

- [ ] All RFP pages referenced at least once
- [ ] No requirement is repeated (consolidated if similar)
- [ ] No requirement is left unmapped (or explicitly justified as out of scope)
- [ ] Mapping logic is clear ("Why does this requirement map to this section?")
- [ ] Total requirement count matches when cross-checked

### Notes for Claude

- Be thorough but concise
- Error on the side of inclusion (overmap requirements rather than miss them)
- Document any ambiguous requirements in the Notes column
- Calculate and include the "Requirements Mapped / Total" percentage summary
