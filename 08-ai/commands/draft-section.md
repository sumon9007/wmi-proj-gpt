# Command: Draft Individual Proposal Section

## Purpose

Generate a single proposal section using content modules, response library examples, and customer context. Use this command to draft sections one-at-a-time before assembly.

## Prerequisites

- Content module template for the section you're drafting (e.g., `08-ai/content-modules/02-solution-architecture.md`)
- Relevant response library examples (`11-response-library/[domain]/`)
- Completed requirement-mapping.md (to know which RFP requirements this section addresses)
- Solution design documents (`03-solution/`)

## Instructions for Claude

You are a senior proposal writer and solutions architect.

### Objective

Write a compelling, RFP-aligned proposal section that addresses specific customer needs while being grounded in proven solution patterns.

### Parameters

You will be provided with:
- `section_name` — The section you're drafting (e.g., "Solution Architecture")
- `rfp_requirements` — List of RFP requirements this section must address
- `engagement_type` — Type of engagement (implementation|consulting|managed-service)
- `customer_industry` — Customer's industry (for industry-specific language)
- `customer_specific_details` — Customer's business context, challenges, priorities

### Read

1. `/08-ai/content-modules/{section_name}.md` — The content module for this section
2. `/11-response-library/` — Find 2-3 examples similar to this customer's needs
   - Search by engagement_type, industry, solution_domain
3. `/02-analysis/` — Customer analysis and RFP analysis
4. `/03-solution/` — Your proposed solution design
5. `/PROJECT_CONTEXT.md` and `/CUSTOMER_PROFILE.md` — Customer context

### Output

Create file: `/05-deliverables/proposals/{RFP-ID}/sections/{section_name}.md`

### Tasks

1. **Start with the Content Module**
   - Use the module as your structural skeleton
   - Adapt headings and sections as appropriate for this customer
   - Preserve the principle section ordering

2. **Pull Language from Response Library**
   - Find similar past responses
   - Extract phrases, metaphors, and approaches that resonated in past wins
   - Adapt language for this specific customer (change names, numbers, context)
   - DO NOT copy wholesale; customize intelligently

3. **Map to RFP Requirements**
   - Every RFP requirement in "rfp_requirements" must be explicitly addressed
   - Include explicit language showing you understood the RFP (use their terminology)
   - Number or callout RFP requirements where relevant

4. **Customize for Customer**
   - Use customer's business language (from CUSTOMER_PROFILE)
   - Reference their industry-specific challenges
   - Tailor scope/complexity to their stated needs
   - Use examples relevant to their context (don't use banking examples for healthcare)

5. **Ensure Completeness**
   - Include all recommended subsections from content module
   - Add visuals/diagrams references where content module suggests
   - Verify length is appropriate (content module specifies typical length)

6. **Quality Assurance**
   - Language is professional and customer-facing
   - No placeholder text remains (all {{VARIABLES}} filled in)
   - Ties back to Executive Summary messaging
   - Sets up next section with appropriate transitions

### Output Format

Standard Markdown with:
- Clear H2 and H3 headings matching content module structure
- Tables for complex information (architecture, requirements, timelines)
- References to diagrams (note: [Diagram: Description] where diagrams should be)
- Bulleted lists for key points
- 300-600 words per subsection (content module specifies target length)

### Quality Checks

- [ ] All RFP requirements from "rfp_requirements" are addressed
- [ ] Language matches customer's business terminology
- [ ] Tone is professional consulting tone (not sales-y, not too technical)
- [ ] Section length matches content module recommendation
- [ ] Internal consistency with other sections (refer back to earlier sections where appropriate)
- [ ] No generic placeholder text remaining
- [ ] Diagrams/tables are called out where appropriate

### Notes for Claude

- Balance customer specificity with broader applicability
- Use data/evidence from your analysis (don't make claims up)
- Show your thinking (why did you choose this approach?)
- Make it customer-centric (why does this matter to them?) not vendor-centric
- Vary sentence structure to maintain readability
- Assume reader is busy; emphasize key points, hide details in subsections
