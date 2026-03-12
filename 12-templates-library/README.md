# Templates Library

Pre-built proposal templates organized by engagement type, industry, and solution domain. These templates provide:

- Recommended section flow and ordering
- Placeholder structure for rapid drafting
- Industry-specific considerations
- Engagement-type-specific sections
- Best practice language patterns

## Purpose

Templates accelerate proposal development by providing:

1. **Structural guidance** — What sections to include and in what order
2. **Content placeholders** — Questions to answer for each section
3. **Format consistency** — Standardized styles and conventions across proposals
4. **Best practices** — Proven approaches from past successful proposals

## Organization

Templates are organized three ways:

### By Engagement Type
- **implementation-proposal.md** — Major system builds, migrations, modernizations
- **managed-service-proposal.md** — 24/7 operations, support, SLAs
- **consulting-engagement.md** — Strategy, design, advisory, assessment
- **support-contract.md** — Maintenance, break-fix, technical support

### By Industry
- **financial-services.md** — Additional sections for regulatory compliance, risk, controls
- **healthcare.md** — HIPAA/privacy considerations, patient data handling
- **manufacturing.md** — Supply chain, equipment, industry-specific compliance
- **retail.md** — Omnichannel, POS, inventory, ecommerce specifics
- **government.md** — Security clearances, procurement compliance, budget cycles
- **technology.md** — Cloud-native, agile, DevOps, startup considerations

### By Solution Domain
- **cloud-migration.md** — RTO/RPO, cutover, legacy integration, phased migration
- **digital-transformation.md** — Change management, organizational impact, upskilling
- **platform-modernization.md** — Microservices, APIs, cloud-native architecture
- **security-hardening.md** — Controls, threat models, incident response, compliance

## How to Use a Template

1. **Identify your proposal type** — engagement type + industry + solution domain
2. **Read the relevant templates** in this order:
   - Start with by-engagement-type/[type].md
   - Add by-industry/[industry].md sections if applicable
   - Add by-solution-domain/[domain].md details if relevant
3. **Adapt the template** for your RFP:
   - Answer all placeholder questions
   - Copy sections from your response library (11-response-library/)
   - Customize with customer-specific details
   - Reference your requirement-mapping.md to ensure RFP coverage

## Template Structure

Each template follows this format:

```markdown
# Proposal Title

## About This Template
- Engagement Type: [type]
- Best For: [industries/scenarios]
- Typical Length: [page count]
- Customization Time: [hours]

## Section Checklist
- [ ] Executive Summary (1 page)
- [ ] Customer Challenges (1-2 pages)
- ...

## Full Template Content

### [Section Name]
**Purpose**: Why this section matters
**Placeholder Questions**:
- What is the customer's specific challenge here?
- What data/evidence supports this?
- How does our solution address this?

**Template Text**:
[Generic template that can be adapted]

---
```

## Template Versions

Some templates come in variations:

- **Standard** — 15-20 page comprehensive proposal
- **Executive** — 5-8 page condensed summary for decision makers
- **Technical** — 25-30 pages with deep architecture and design details
- **Financial** — Focused on cost models, ROI, pricing, financial justification

Choose based on the RFP's stated requirements or customer's preference.

## Combining Templates

For complex proposals, you may combine multiple templates:

Example: Technology company pursuing cloud migration implementation
```
Start with: by-engagement-type/implementation-proposal.md
Add sections from: by-industry/technology.md
Add sections from: by-solution-domain/cloud-migration.md
Result: Customized implementation proposal with tech and cloud details
```

## Maintaining Templates

- **Quarterly review** — Update templates based on recent wins
- **Tagging consistency** — Ensure engagement types and industries match naming-conventions.md
- **Variant notes** — Mark which industry/domain combinations work well together

## Examples

Each template includes 2-3 examples from past proposals showing:
- How the section was structured in a real proposal
- Actual customer language used
- Architecture diagrams or tables that worked

Find examples in each template file under **"Example from Real Proposal"** section.

## Related Resources

- [Response Library](../11-response-library/) — Actual past responses to copy language from
- [Content Modules](../08-ai/content-modules/) — Generic section templates
- Naming Conventions (00-admin/naming-conventions.md) — Consistent tagging
