# Delivery Implications

## Delivery Model Implications

- The project should be planned as a two-phase engagement:
  - Phase 1: design, build, integrate, test, train, and deploy within 12 months
  - Phase 2: support, maintenance, updates, and operational stabilization for 24 months
- Delivery must include a formal first-line support enablement and handover workstream for GPT IT Services.
- Governance must be strong from the beginning because customer-controlled approvals will affect access, integration, security, and acceptance.

## Architecture Implications

- The architecture must assume SITA-managed Windows hosting as a hard constraint.
- An integration-centric design is required because the platform must work across DHA, credit bureau, banking, payroll-related systems, and department-specific usage patterns.
- The ESB / integration layer is not optional; it is a named requirement and should be explicit in the architecture.
- The design should separate capture, verification, decisioning, reporting, and audit functions to make controls and traceability clear.

## Security and Hosting Implications

- Security cannot be handled as a generic section; it must explicitly address POPIA, ISO alignment, encryption, MFA, audit logging, backups, DR, and incident response.
- Operational resilience must be designed, not implied, because uptime, RTO, and RPO targets are stated in the tender.
- Government ownership and control of data and artefacts must be reflected both technically and contractually.
- Hosting assumptions must align with GPT, SITA, and Department of e-Government roles.

## Integration Implications

- DHA access through GPT-approved IP is a key gating dependency for both prototype and production.
- Credit bureau delivery is part of the bidder scope, so integration and commercial design are tightly linked.
- Banking and payroll-related integrations may need discovery and staged onboarding because the tender does not fully define technical interfaces.
- The proposal should show an integration roadmap rather than implying all interfaces are equally ready on day one.

## Support and Training Implications

- Training is not just end-user onboarding; GPT IT must be prepared for first-line support, troubleshooting, case handling, and escalation.
- Operational documentation should be treated as a contractual deliverable, not optional collateral.
- SLA, monitoring, and incident handling must be explained in practical terms to show support readiness.

## Proposal Authoring Implications by Section

- Executive Summary
  - Emphasize fraud reduction, control, audit improvement, and government ownership.
- Customer Challenges
  - Tie the problem statement to fragmented verification, poor data quality, and public-sector risk exposure.
- Proposed Solution
  - Show end-to-end verification flows, multi-department use cases, and credit bureau service inclusion.
- Solution Architecture
  - Make SITA hosting, ESB integration, DHA access, device support, and resilience architecture explicit.
- Security and Compliance Considerations
  - Address POPIA, ISO standards, MFA, RBAC, audit logging, backups, DR, and secure biometric handling directly.
- Implementation Approach
  - Show a 12-month implementation plan, named workstreams, dependency management, support transition, and prototype readiness.
- Assumptions and Dependencies
  - Clearly state customer-controlled dependencies including IP approvals, environment access, and third-party connectivity.

## Most Important Internal Delivery Priorities

- De-risk administrative compliance before submission.
- Treat the prototype as a core delivery stream early in the bid lifecycle.
- Confirm hosting, integration, and commercial assumptions that could create non-compliance.
- Keep architecture, security, and implementation narratives tightly aligned with the requirement mapping.
