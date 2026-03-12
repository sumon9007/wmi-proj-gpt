# Naming Conventions

## General Rules

- Use lowercase for all filenames
- Use hyphen-separated words (not underscores or spaces)
- Include dates for time-sensitive documents (YYYY-MM-DD format)
- Include lifecycle state when relevant: `draft`, `review`, `final`
- Be descriptive enough to search later (file names should be self-explanatory)

## RFP & Proposal Naming

### RFP Identifier Format

**Format:** `{YEAR}-{CUSTOMER-SHORT}-{PROJECT-TYPE}`

**Examples:**
- `2026-ACMECORP-CLOUD-MIGRATION` — Cloud migration for Acme Corp, 2026 RFP
- `2026-TECHCO-SECURITY-HARDENING` — Security engagement for TechCo, 2026
- `2025-HEALTHPLUS-DATA-WAREHOUSE` — Data warehouse for HealthPlus, 2025

**Rules:**
- YEAR = 4-digit year (2026, 2025, etc.)
- CUSTOMER-SHORT = 4-8 character customer identifier (derived from legal name or common name)
- PROJECT-TYPE = Hyphenated project type (cloud-migration, security-hardening, modernization, etc.)

### Proposal Folder Structure

**Location:** `05-deliverables/proposals/{RFP-ID}/`

**Example:** `05-deliverables/proposals/2026-ACMECORP-CLOUD-MIGRATION/`

**Contents:**
```
2026-ACMECORP-CLOUD-MIGRATION/
├── metadata.yml                        # RFP tracking and metadata
├── requirement-mapping.md              # RFP requirement to proposal mapping
├── draft/
│   └── proposal.md                     # Initial draft (may iterate: v1, v2, etc.)
├── review/
│   └── comments-and-feedback.md        # Internal review notes
├── final/
│   └── proposal.md                     # Final approved version for submission
├── sections/
│   ├── 01-executive-summary.md
│   ├── 02-customer-challenges.md
│   ├── 03-solution-overview.md
│   └── [other sections as drafted]
└── attachments/                        # Diagrams, charts, supporting docs
    ├── architecture-diagram.png
    └── compliance-matrix.xlsx
```

### Individual Proposal Sections

**File naming:** `{NUMBER}-{SECTION-NAME}.md` (in `/sections/` folder)

**Examples:**
- `01-executive-summary.md`
- `02-customer-challenges.md`
- `03-solution-overview.md`
- `04-solution-architecture.md`
- `05-security-compliance.md`
- `06-implementation-approach.md`
- `07-assumptions-dependencies.md`

**Numbering:** Sequential (01, 02, 03...) to match recommended proposal flow

### Proposal Export Files

**Location:** `05-deliverables/exports/{FILE-TYPE}/`

**Format:** `{RFP-ID}-proposal-final.{EXTENSION}` 

**Examples:**
- `05-deliverables/exports/pdf/2026-ACMECORP-CLOUD-MIGRATION-proposal-final.pdf`
- `05-deliverables/exports/docx/2026-ACMECORP-CLOUD-MIGRATION-proposal-final.docx`
- `05-deliverables/exports/pptx/2026-ACMECORP-CLOUD-MIGRATION-presentation-final.pptx`

---

## Response Library Naming

### Response File Naming

**Format:** `{DOMAIN}-{SOLUTION-PATTERN}-{YEAR}.md`

**Examples:**
- `11-response-library/cloud-architecture/cloud-aws-multi-region-2026.md`
- `11-response-library/security-compliance/pci-dss-banking-sector-2026.md`
- `11-response-library/infrastructure/kubernetes-enterprise-2025.md`
- `11-response-library/integration/api-platform-ecommerce-2026.md`

**Rules:**
- DOMAIN = Subfolder name (cloud-architecture, security-compliance, infrastructure, etc.)
- SOLUTION-PATTERN = Descriptive pattern name (aws-multi-region, pci-dss-banking, kubernetes-enterprise)
- YEAR = 4-digit year when response was created/sourced

### Response ID (for metadata)

**Format:** `{DOMAIN}-{PATTERN}-{YEAR}` (matches filename without extension)

**Used in:** YAML frontmatter `response_id` field

**Example:**
```yaml
response_id: cloud-aws-multi-region-2026
```

### Subfolder Organization

**Primary domains:**
- `cloud-architecture/` — Cloud migrations, multi-region, hybrid
- `security-compliance/` — Regulatory frameworks, controls, certifications
- `infrastructure/` — On-premise, virtualization, modernization, containers
- `integration/` — API strategies, middleware, data integration
- `deployment-models/` — SaaS, managed services, operations

**Sub-categorization (optional):**
- `cloud-architecture/aws/` — AWS-specific patterns
- `cloud-architecture/azure/` — Azure-specific patterns
- `security-compliance/financial-services/` — Compliance for banking
- `security-compliance/healthcare/` — HIPAA-specific approaches

---

## Metadata Tagging Standards

### Engagement Type Tags
Use EXACTLY one of these:
- `implementation`
- `managed-service`
- `consulting`
- `support`
- `training`

### Industry Tags
Use one or more of these (comma-separated):
- `financial-services`
- `healthcare`
- `manufacturing`
- `retail`
- `government`
- `education`
- `technology`
- `other`

### Solution Domain Tags
Use one or more of these:
- `cloud-migration`
- `security`
- `infrastructure`
- `integration`
- `transformation`
- `deployment-models`

### Customer Size Tags
Use EXACTLY one of these:
- `startup` — < 100 employees, < $10M revenue
- `mid-market` — 100-1000 employees, $10M-$100M revenue
- `enterprise` — > 1000 employees, > $100M revenue

### Complexity Levels
Use EXACTLY one of these:
- `basic` — Single system, straightforward requirements, < 3 months
- `intermediate` — Multiple systems, moderate integration, 3-6 months
- `advanced` — Complex architecture, significant custom work, > 6 months

### Outcome Tags
Use EXACTLY one of these (for archival/learning):
- `won` — Won the deal
- `lost` — Lost the deal (conduct loss analysis)
- `in-progress` — Actively being worked on
- `no-award` — Customer chose not to award to anyone

---

## Template & Module Naming

### Content Module Files

**Location:** `08-ai/content-modules/`

**Format:** `{NUMBER}-{MODULE-NAME}.md`

**Examples:**
- `01-executive-summary.md`
- `02-solution-architecture.md`
- `03-security-compliance.md`
- `04-implementation-approach.md`
- `05-assumptions-dependencies.md`

**Numbering:** Sequential (01, 02, 03...) in recommended section order

### AI Command Files

**Location:** `08-ai/commands/`

**Format:** `{VERB}-{NOUN}.md`

**Examples:**
- `analyze-requirements.md` — Extract RFP requirements
- `draft-section.md` — Write individual proposal section
- `assemble-proposal.md` — Combine sections into final proposal
- `index-winning-response.md` — Catalog response into library

### Template Files

**Location:** `08-ai/templates/`

**Format:** `{PURPOSE}-template.md` (or `.yml` for YAML templates)

**Examples:**
- `proposal-template.md` — Standard proposal structure
- `metadata-template.yml` — RFP metadata tracking
- `requirement-mapping-template.md` — RFP-to-proposal mapping

---

## General Examples

### Meeting Notes
```
2026-03-12-kickoff-meeting.md
2026-03-15-architecture-review.md
2026-03-20-customer-update.md
```

### Status Documents
```
weekly-status-2026-03-15.md
monthly-status-march-2026.md
delivery-status-final.md
```

### Analysis Documents
```
rfp-requirements-analysis.md
customer-data-assessment.md
competitive-analysis.md
```

### Working Drafts
```
solution-architecture-draft-v1.md
solution-architecture-draft-v2.md
solution-architecture-final.md
```

---

## Searching & Discovery

**Proper naming enables searching:**

The naming conventions above enable these searches:

- **Find all RFP responses:** Search for `05-deliverables/proposals/202[0-9]-`
- **Find AWS responses:** Search for `11-response-library/cloud-architecture/aws-*`
- **Find security responses:** Filter by `solution_domain: security` in metadata
- **Find healthcare proposals:** Filter by `industry: healthcare` in all RFP folders
- **Find recent responses:** Sort by YYYY-MM-DD in filename or `created_date` in metadata

---

## Consistent Tagging Across Workspace

**Critical:** Use the EXACT tags defined above to ensure searchability.

**Example of consistent tagging:**
```yaml
engagement_type: implementation  # EXACT match from list
industry: [financial-services]    # EXACT match from list
solution_domain: [cloud-migration, security]  # EXACT matches
customer_size: enterprise         # EXACT match from list
complexity: advanced              # EXACT match from list
```

**NOT correct:**
```yaml
engagement_type: "systems implementation" # TOO SPECIFIC
industry: "banking"               # USE: financial-services
solution_domain: "aws and security"  # USE: cloud-migration, security
customer_size: "large company"    # USE: enterprise
complexity: "very hard"           # USE: advanced
```
