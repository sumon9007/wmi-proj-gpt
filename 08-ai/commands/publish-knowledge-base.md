# Command: Publish Knowledge Base

## Purpose

Convert the current project, solution, delivery, and proposal material into a concise internal knowledge portal for reuse, onboarding, and project continuity.

## Prerequisites

- `/PROJECT_CONTEXT.md`
- `/CUSTOMER_PROFILE.md`
- `/BIDDER_PROFILE.md`
- `/02-analysis/`
- `/03-solution/`
- `/04-delivery/`
- `/05-deliverables/proposals/{RFP-ID}/draft/proposal.md` if available
- `/05-deliverables/proposals/{RFP-ID}/requirement-mapping.md` if available

Use the latest populated tender folder under `/05-deliverables/proposals/` when `{RFP-ID}` is not explicitly supplied.

## Instructions for Claude

You are a technical documentation lead creating a clean, reusable knowledge portal from active bid and solution material.

### Objective

Publish a small set of well-structured markdown pages that explain the engagement clearly for internal teams without copying raw proposal text, internal review comments, or procurement clutter.

### Read

1. `/PROJECT_CONTEXT.md`
2. `/CUSTOMER_PROFILE.md`
3. `/BIDDER_PROFILE.md`
4. `/02-analysis/rfp-analysis/`
5. `/02-analysis/customer-analysis/`
6. `/02-analysis/delivery-analysis/`
7. `/03-solution/architecture/`
8. `/03-solution/executive/`
9. `/03-solution/implementation-design/`
10. `/03-solution/standards/`
11. `/04-delivery/project-management/`
12. `/04-delivery/implementation/`
13. `/04-delivery/trackers/`
14. `/05-deliverables/proposals/{RFP-ID}/draft/proposal.md` if present
15. `/05-deliverables/proposals/{RFP-ID}/requirement-mapping.md` if present

Do not treat review checklists, comments, draft-only placeholders, or commercial pricing working files as source material for portal narrative unless they reveal important project risks or next steps.

### Output

Update these files in `/06-knowledge-portal/docs/`:

- `index.md`
- `project-overview.md`
- `architecture.md`
- `implementation.md`
- `operations.md`
- `decisions.md`
- `faq.md`

### Page Intent

1. **index.md**
   - Short landing page
   - What this knowledge portal covers
   - Links / pointers to the six core pages
   - Current project name and customer

2. **project-overview.md**
   - Business context
   - Customer problem summary
   - Scope at a glance
   - Key stakeholders
   - Delivery timeline and engagement model

3. **architecture.md**
   - Solution summary
   - Logical architecture
   - Physical / hosting model
   - Integration overview
   - Security architecture summary
   - Mention available diagram specs if diagrams are not yet rendered

4. **implementation.md**
   - Delivery phases
   - Major milestones
   - Workstreams
   - Dependencies and assumptions that affect implementation
   - What must happen in the first 90 days

5. **operations.md**
   - Support and maintenance model
   - Environment / hosting responsibilities
   - SLA / DR expectations
   - Security, monitoring, and operational control responsibilities
   - Handover and transition considerations

6. **decisions.md**
   - Important architectural and delivery decisions already implied by the tender and proposal
   - Constraints treated as design decisions
   - Open decisions or items requiring confirmation
   - Keep this page crisp and high-signal

7. **faq.md**
   - Answer practical internal questions a new team member or manager would ask
   - Example topics: hosting, DHA dependency, licensing rule, IP ownership, support term, prototype requirement, customer controls, bidder role

### Writing Rules

- Write for internal reuse, onboarding, and project continuity.
- Keep pages concise, navigable, and markdown-friendly.
- Prefer synthesis over copying.
- Remove tender noise, repetitive legal wording, and raw scoring language unless it changes delivery behavior.
- Use clear headings and short sections.
- Preserve critical public-sector constraints:
  - SITA-hosted environment
  - GPT governance and data ownership
  - no third-party license cost rule
  - GPT-exclusive IP ownership
  - POPIA / security controls
  - DHA and other external integration dependencies
  - 12-month implementation and 24-month support

### Exclusions

Do not include:

- raw review comments
- bid-readiness checklists
- internal editorial notes
- pricing detail unless needed to explain a structural commercial constraint
- placeholder evidence lists except where they affect readiness or risk

### Quality Checks

- [ ] All seven portal pages exist and are internally consistent
- [ ] Content reflects the current project artifacts, not generic boilerplate
- [ ] Public-sector constraints are visible where they matter
- [ ] Pages are concise enough for quick reuse
- [ ] No copied review-only or submission-only clutter
- [ ] Architecture, implementation, and operations views align with each other

### Notes for Claude

- Treat this as knowledge publication, not proposal drafting.
- The portal should help a teammate understand the engagement in minutes.
- If source material is incomplete, state assumptions briefly rather than padding the page.
- Reuse the latest proposal draft only as a secondary synthesis source after the primary analysis and solution files.
