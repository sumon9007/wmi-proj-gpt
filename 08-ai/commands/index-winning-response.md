# Command: Index Winning Response for Library

## Purpose

After winning a major proposal, catalog key sections from the winning response into the response library for future reuse. This builds organizational knowledge and accelerates future proposal development.

## Prerequisites

- Completed proposal in final form (in `05-deliverables/proposals/{RFP-ID}/final/`)
- Metadata.yml for the RFP (with outcome: won)
- Requirement-mapping.md showing what you solved

## Instructions for Claude

You are a knowledge manager and proposal strategist.

### Objective

Extract high-value sections from winning proposals and catalog them in the response library with proper metadata, enabling future teams to find and reuse proven approaches.

### Read

1. `/05-deliverables/proposals/{RFP-ID}/final/proposal.md` — The winning proposal
2. `/05-deliverables/proposals/{RFP-ID}/metadata.yml` — RFP context and outcome
3. `/05-deliverables/proposals/{RFP-ID}/requirement-mapping.md` — What requirements it solved
4. `/11-response-library/README.md` — Metadata tagging standards
5. `/11-response-library/responses-index.md` — Existing catalog (to avoid duplication)

### Output

Create multiple files in `/11-response-library/`:

1. **Response Files** — Extract 2-5 key solution sections, one file each
   - Location: `/11-response-library/{DOMAIN}/{response-id}.md`
   - Where DOMAIN = cloud-architecture, security-compliance, infrastructure, integration, deployment-models, or other
   - Where response-id = [DOMAIN]-[PATTERN]-[YEAR] (e.g., cloud-aws-multi-region-2026)

2. **Index Entry** — Add entry to `/11-response-library/responses-index.md`

### Tasks

1. **Identify Key Sections to Extract**
   - Solution Architecture section (usually most reusable)
   - Security/Compliance approach (if addressed elaborate compliance requirements)
   - Implementation Methodology (if unique or proven approach)
   - Risk Mitigation strategy (if it solved a particular risk class)
   - Integration patterns (if it solved complex integration)
   - Do NOT extract: customer-specific details, pricing, timeline, team names

   Typically extract 2-5 sections maximum (quality over quantity)

2. **Sanitize Customer-Specific Details**
   - Remove customer name, replace with {{CUSTOMER_INDUSTRY}}
   - Remove specific metrics tied to their business, keep approach
   - Remove internal team names, keep role descriptions
   - Keep technical approach and decision reasoning

   Examples of what to remove:
   - "BigBank required PCI-DSS v4.0" → "Financial services custimer required PCI-DSS v4.0"
   - "Customer had 500 active users" → "{{NUMBER}} active users"
   - "Recommended by Lead Architect John Smith" → "Recommended by {{ARCHITECT_ROLE}}"

3. **Add Metadata Header**
   Each response file should start with YAML frontmatter:
   ```yaml
   ---
   response_id: [domain]-[pattern]-[year]
   engagement_type: [implementation|consulting|managed-service]
   industry: [financial-services|healthcare|manufacturing|retail|govt|tech|other]
   solution_domain: [cloud-architecture|security|infrastructure|integration|deployment-models]
   customer_size: [startup|mid-market|enterprise]
   complexity: [basic|intermediate|advanced]
   outcome: won
   original_rfp: [RFP ID from metadata]
   created_date: [Date extracted]
   source_proposal: [Path to original proposal]
   keywords: [comma, separated, search, terms]
   related_domains: [other solution domains this touches]
   ---
   ```

4. **Add Context Header**
   After metadata, add 2-3 paragraph summary:
   - What problem this approach solves
   - Why this approach was winning (what made it stand out)
   - Key decision points
   - Where this approach is strongest (industries, scenarios, team sizes)

5. **Include Key Artifacts**
   - Architecture diagrams referenced (indicate [Diagram: Description])
   - Tables showing requirements mapping or approach comparison
   - Timeline milestones if illustrative
   - Risk/mitigation tables if exemplary

6. **Create Search Index Entry**
   - Add one row to `/11-response-library/responses-index.md`
   - Fill in: response_id | title | industry | engagement_type | complexity | outcome | keywords

### Output File Example

```
# /11-response-library/cloud-architecture/cloud-aws-multi-region-2026.md

---
response_id: cloud-aws-multi-region-2026
engagement_type: implementation
industry: financial-services
solution_domain: cloud-architecture
customer_size: enterprise
complexity: advanced
outcome: won
original_rfp: 2026-ACMECORP-CLOUD
created_date: 2026-03-12
source_proposal: 05-deliverables/proposals/2026-ACMECORP-CLOUD/final/proposal.md
keywords: [aws, multi-region, failover, high-availability, pci-dss, active-active]
related_domains: [security-compliance]
---

## Context: Multi-Region AWS Architecture for Financial Services

This proposal won against 2 competitors by proposing active-active multi-region deployment 
(vs. standard active-passive). This approach provided {{CUSTOMER_INDUSTRY}} with:
- 99.99% uptime capability
- Sub-second regional failover
- Compliance with PCI-DSS multi-region requirements
- Cost optimization through unused capacity leveraging

The key differentiator was demonstrating that active-active was achievable with their 
existing {{TECHNOLOGY_STACK}} (vs. competitor proposals requiring expensive new platforms).

## Solution Architecture

[Full architecture section from proposal, sanitized of customer details]
```

7. **Verify Reusability**
   - Can someone in a similar industry/engagement type use this as a template?
   - Are all customer-specific details removed?
   - Are the principles and approach clear?
   - Are decision trade-offs explained?

### Quality Checks

For each response file created:
- [ ] Metadata is complete and accurate
- [ ] Customer-specific details removed (names, internal details)
- [ ] Core approach and customer-agnostic details preserved
- [ ] Problem statement is clear (what does this solve?)
- [ ] Keywords are searchable (industry, engagement, technical domain)
- [ ] Related sections cross-referenced
- [ ] Read-in-isolation is possible (doesn't reference full proposal)

For index entry:
- [ ] Response_id matches filename
- [ ] Industry, engagement_type, complexity match metadata
- [ ] Keywords are Google-searchable (not jargon-heavy)
- [ ] Entry actually appears in index table

### Frequency

Perform this command:
- **Immediately after win** — Create files while fresh
- **Quarterly review** — Catalog any major wins from past quarter
- **Before proposal season** — Ensure library is current

### Notes for Claude

- Err on side of inclusion (library is most valuable when comprehensive)
- Keep sections reasonably modular (2-4 page sections, not 20-page sections)
- Focus on approaches that are industry/pattern-specific (not generic)
- Highlight what made this winning (what beat competitors?)
- Make it usable (future proposers should find this, understand it, and adapt it)
