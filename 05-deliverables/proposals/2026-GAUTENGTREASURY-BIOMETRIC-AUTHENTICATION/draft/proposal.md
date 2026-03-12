# Proposal for Gauteng Provincial Treasury

[Image: Bidder logo from `/home/suruz/claude-workspace/01-PROJECTS/wmi-proj-gpt/05-deliverables/proposals/2026-GAUTENGTREASURY-BIOMETRIC-AUTHENTICATION/attachments/branding/bidder-logo.svg` or `/home/suruz/claude-workspace/01-PROJECTS/wmi-proj-gpt/05-deliverables/proposals/2026-GAUTENGTREASURY-BIOMETRIC-AUTHENTICATION/attachments/branding/bidder-logo.png`]

[Image: Customer logo from `/home/suruz/claude-workspace/01-PROJECTS/wmi-proj-gpt/05-deliverables/proposals/2026-GAUTENGTREASURY-BIOMETRIC-AUTHENTICATION/attachments/branding/customer-logo.svg` or `/home/suruz/claude-workspace/01-PROJECTS/wmi-proj-gpt/05-deliverables/proposals/2026-GAUTENGTREASURY-BIOMETRIC-AUTHENTICATION/attachments/branding/customer-logo.png`]

**Tender:** GT/GPT/009/2026  
**Opportunity:** Development of Biometric Authentication System Including Support and Maintenance for Period of 3 Years  
**Customer:** Gauteng Provincial Treasury (GPT), on behalf of Gauteng Provincial Government (GPG)  
**Date:** 2026-03-13  
**Status:** Draft for internal review  
**Confidentiality:** Confidential

---

## Table of Contents

1. Executive Summary
2. Customer Challenges
3. Proposed Solution
4. Solution Architecture
5. Security and Compliance Considerations
6. Implementation Approach
7. Assumptions and Dependencies
8. Benefits and Outcomes
9. Company Profile and Relevant Experience
10. Next Steps
11. Appendices

---

## 1. Executive Summary

Gauteng Provincial Treasury is seeking a secure, government-controlled biometric authentication platform that can improve recruitment screening, payroll cleansing, supplier due diligence, beneficiary verification, and fraud prevention across Gauteng Provincial Government. The tender makes clear that this is not only a systems-development exercise. It is a public-sector control and modernization initiative that must balance operational usability with strong governance, privacy protection, resilience, and auditability.

Waymark Infotech brings more than two decades of systems-integration experience to this opportunity. Since 2003, we have delivered custom core business applications using an agile, collaboration-led approach that relies on early prototype validation to extract requirements, reduce delivery risk, and align business goals with technical outcomes. Our proposed response is an end-to-end biometric verification platform designed for the GPT operating environment and aligned to the tender's explicit requirements. The solution combines biometric capture, identity verification through the Department of Home Affairs, demographic and business-interest verification through credit bureau services, workflow-driven decision support, reporting, audit trails, and a centralized control model under GPT. It is structured to operate in a SITA-managed Windows environment, with security controls aligned to POPIA, GPT policy requirements, and the ISO-aligned standards referenced in the tender.

The delivery model is built around two clear phases. In the first 12 months, we would complete design, build, integration, testing, deployment, training, and handover. In the remaining 24 months, we would provide support, maintenance, updates, and operational stabilization. This approach aligns directly with the three-year contract structure and supports GPT's requirement for sustainable operations, first-line support readiness, and long-term control of the solution.

The proposal is also designed to support competitiveness in evaluation. It addresses the mandatory administrative compliance items, the technical scoring areas, the standards-based security expectations, the team and reference evidence requirements, and the prototype obligations that will be tested in the GPT environment. Just as importantly, it respects the non-negotiable commercial and governance constraints in the tender, including no third-party system license costs for use of the platform, exclusive GPT ownership of data and intellectual property, and GPT's right to extend the solution across broader government structures without additional royalty or license cost. Waymark Infotech's relevant delivery experience includes biometric enrolment and verification for SASSA using Department of Home Affairs APIs, grant-verification and vetting workflows for the National Lotteries Commission across multiple government and financial interfaces, voter enrolment and verification solutions across several African electoral commissions, and biometrics-driven registration for telecom regulatory compliance. These engagements strengthen the credibility of our proposed approach for the GPT requirement.

In short, this proposal positions the solution as a practical government platform: secure, interoperable, supportable, and built for operational control. It is intended to help GPT improve data quality, reduce fraud risk, strengthen internal controls, and provide faster, more reliable verification services across provincial departments and municipalities.

---

## 2. Customer Challenges

GPT's tender describes a public-sector environment where verification processes affect high-impact government functions, including recruitment, payroll administration, supply chain controls, forensic support, and beneficiary screening. In this context, verification gaps create both operational inefficiency and governance risk. Manual or fragmented processes make it harder to confirm identities, validate banking details, check current addresses, monitor mortality status, and identify undeclared business interests involving government employees.

The tender also highlights the need for stronger internal controls and better data quality. GPT is not simply looking for a front-end biometric tool. It is looking for a mechanism to improve the integrity of government records and support science-based decision-making. This includes more reliable employee vetting, cleaner payroll data, stronger fraud-prevention capability, and better beneficiary targeting for public programs.

Another core challenge is the complexity of the stakeholder environment. The solution must operate across multiple Gauteng departments and municipalities while integrating with external information holders such as the Department of Home Affairs, credit bureaus, and banking-sector services. GPT must retain central control of data access and governance even while the platform serves a broad operational footprint. That creates a strong requirement for controlled integration, role-based access, auditability, and a disciplined operating model.

The tender further makes clear that GPT is operating in a compliance-first context. The solution must align with POPIA, public-sector governance expectations, GPT and Department of e-Government security directives, and the operational standards implied by SITA-managed hosting. In practice, this means the customer will respond best to a proposal that demonstrates control, clarity, and implementation realism rather than generic innovation language.

These challenges shape the proposal that follows. The recommended approach is not to treat verification as a narrow point solution, but as a centrally governed verification platform that can support multiple departments, multiple use cases, and multiple external information sources while maintaining a clear compliance and accountability model.

---

## 3. Proposed Solution

We propose a web-based biometric authentication platform designed specifically for GPT's multi-department operating environment. The solution is structured to support both desktop and mobile use cases, with biometric and numeric input options, real-time verification workflows, reporting and dashboard capability, and strong administrative control. The platform is designed to help GPT move from fragmented verification activities to a more consistent, traceable, and policy-aligned service. This approach reflects Waymark Infotech's established delivery model: collaborative requirement discovery, early prototype validation, and pragmatic integration design in regulated environments.

At the core of the solution is an end-to-end verification workflow. Authorized users initiate a verification session, capture the subject's consent, enter identity information, and perform biometric capture using supported fingerprint devices or other approved biometric mechanisms. The system performs local validation, including South African ID format checks where relevant, and then routes requests through the controlled integration layer to the Department of Home Affairs and other approved information providers. Returned results are displayed in a usable business format, archived within the government-controlled environment, and made available for reporting, downstream workflow, and audit purposes.

The proposed platform includes the following functional capability areas:

- Identity verification against Department of Home Affairs services
- Demographic, address, employment, and business-interest verification through credit bureau services
- Banking verification support
- Mortality verification and recurring checking support
- Persal-related payroll integration support
- Rules-based decisioning and mismatch highlighting
- Generic, customized, ad hoc, and scheduled reporting
- Exception reporting for invalid, unmatched, or unverified cases
- Audit trails for user actions and verification outcomes
- Role-based workflow configuration and operational control under GPT

Because the tender describes multiple user groups and varied use cases, the solution is positioned as a shared service platform rather than a single-purpose application. Human Resources, supply chain services, forensic teams, beneficiary screening functions, and other line departments can all operate within the same governed environment, while GPT retains control over access, data, policy enforcement, and service oversight.

The proposal also includes the credit bureau service element explicitly required by the tender. This is important because the credit bureau capability is not merely an integration point; it is part of the service model. The proposed commercial structure therefore supports per-query or bulk consumption patterns in line with the tender's user-pay expectation for participating departments.

To support evaluation readiness, the proposed solution approach also anticipates the prototype stage. The demo path will mirror the production design as closely as practical: user authentication, consent capture, ID validation, ten-fingerprint capture, DHA submission, response display, result reporting, and exportable output. This ensures that the prototype is not treated as a disconnected showcase, but as an early expression of the same architectural and operational approach proposed for the full solution. It also aligns with Waymark Infotech's delivery practice of validating design and business fit early through working prototypes rather than deferring risk until late in the lifecycle.

---

## 4. Solution Architecture

The proposed architecture is designed around four principles that are strongly implied by the tender: central governance, secure integration, operational resilience, and government ownership. To reflect those principles, the architecture separates capture, integration, decisioning, data management, and reporting into controlled layers rather than embedding everything into a monolithic application.

### 4.1 Logical Architecture

The logical architecture consists of the following layers:

- Presentation layer
  - Desktop web interface for departmental users
  - Mobile-capable interface for Android and iOS use cases
  - User authentication and session management
- Verification and workflow layer
  - Consent capture
  - ID and passport pre-validation
  - Biometric capture and submission orchestration
  - Rules-based decisioning
  - Workflow and case progression
- Integration layer
  - ESB or equivalent secure service orchestration layer
  - DHA integration
  - Credit bureau integration
  - Banking validation interface support
  - Persal or payroll-related integration support
- Data and reporting layer
  - Government-controlled result storage
  - Audit trail repository
  - Reporting and dashboard capability
  - Exception and reconciliation reporting
- Security and operations layer
  - RBAC and MFA
  - Encryption services
  - Monitoring and alerting
  - Backup and DR controls
  - Logging and compliance evidence

### 4.2 Hosting and Deployment Model

The deployment model is aligned to the tender's hard constraints. The complete solution, including application components, configuration, source code, and related artefacts, is intended for hosting within a SITA-managed Windows-based environment, supported by the Department of e-Government. This requirement shapes infrastructure design decisions from the outset and avoids any architecture that depends on non-compliant hosting assumptions.

All data is assumed to remain within the GPT-controlled environment, with access governed centrally by GPT. This supports the tender's requirements for government ownership, controlled access, and protection of sensitive biometric and demographic data.

### 4.3 Integration Approach

The integration layer is a central architectural element because the platform must operate across several external and internal systems with different security, interface, and governance expectations. For that reason, the proposal includes an ESB or equivalent integration orchestration capability to handle movement, transformation, storage coordination, encryption, and controlled interface management.

Special attention is given to DHA connectivity, because the tender makes it clear that access will depend on GPT-approved IP standards and customer-controlled access arrangements. The architecture therefore assumes that external institution verification, especially DHA connectivity, will be mediated through approved customer-network parameters such as Site-ID, Workstation-ID, and whitelisted IP paths.

### 4.4 Device and Functional Compatibility

The platform design supports Lumidigm V302-20 series devices, recent equivalent devices, and other DHA-approved biometric capture devices, as required by the tender. It also supports both biometric input and numeric input, which is important for bulk verification and for workflows where biometric capture is not the only required entry mechanism.

The architecture further supports:

- one-to-many search against the GPG database
- bulk identity-number-based verification
- reporting and export
- exception handling
- auditability across user actions and system events

### 4.5 Architecture Outcome

The result is an architecture that is not only technically suitable, but also structurally aligned to GPT's operating needs. It supports central control, controlled integration, resilience, and future extension across departments without undermining the governance model defined in the tender.

---

## 5. Security and Compliance Considerations

Security and compliance are not supporting topics in this engagement; they are central evaluation and design requirements. The tender explicitly calls for POPIA-aligned operation, secure storage and management of biometric data, encryption, RBAC, MFA, audit logging, resilience controls, and alignment to named ISO standards in the technical response. The proposed security approach therefore combines governance, technical control, and operational discipline.

### 5.1 Data Protection and Privacy

The platform is designed to support consent-based verification flows, purpose-limited processing, controlled data access, and secure data handling in line with POPIA and GPT governance expectations. Consent capture is included directly in the business workflow, not treated as an external paper control. Personal data processing is scoped to government use, in line with the tender's requirement that data be used exclusively for GPG purposes.

### 5.2 Identity and Access Control

The solution will support centralized GPT control over user access policies. Role-based access control will be used to assign permissions by function and business role, while MFA will be used to strengthen access protection for system and data assets. Credential behavior, password controls, and administrative role allocation will be aligned to GPT policy, as required by the tender.

### 5.3 Encryption, Auditability, and Secure Operations

The security model includes encryption in transit and at rest, secure management of biometric and demographic data, and comprehensive audit logging for user activity, verification actions, administration events, and system-level security events. This is necessary not only for security protection, but also for traceability, accountability, and evidence in a public-sector audit context.

### 5.4 Standards Alignment

The technical response and security plan will align to the standards named in the tender:

- ISO/IEC 27001:2022 for information security management
- ISO/IEC 27701:2019 for privacy information management
- ISO/IEC 30107-3:2017 for biometric presentation attack detection considerations
- ISO/IEC 25010:2011 for software quality considerations

The proposal does not assume that standards references alone are sufficient. Instead, the intent is to map key tender requirements such as secure integration, privacy handling, role control, auditability, and resilience to a standards-aligned control narrative that GPT can evaluate credibly.

### 5.5 Backup, Resilience, and Incident Readiness

The tender includes explicit operational requirements for backup, disaster recovery, uptime, and incident response. The proposed model therefore includes:

- regular and incremental backup of application, configuration, and database assets
- DR planning aligned to an RTO of 4 hours and an RPO of 15 minutes
- semi-annual DR testing and evidence-sharing
- 24/7 monitoring and alerting for downtime or security events
- incident notification and recovery procedures aligned to GPT expectations

### 5.6 Governance Fit

Most importantly, the proposed security approach supports GPT's governance posture. Data remains government-owned, access remains centrally governed, hosting remains within the mandated environment, and operational controls are designed to be visible and auditable. This is the kind of security model that supports both compliance and practical service delivery.

---

## 6. Implementation Approach

The implementation approach is designed to meet the tender's time, control, and support expectations. It is structured around a 12-month implementation program followed by a 24-month support and maintenance period. This aligns directly to the contract term and creates a delivery model that can move from controlled build into stable operations without a handoff gap.

### 6.1 Phase 1: Design, Build, Integrate, and Deploy

Phase 1 covers the first 12 months and includes the following major workstreams:

- Mobilization and governance setup
  - kickoff, roles, governance cadence, risk and issue controls
- Discovery and requirements confirmation
  - workflow validation, stakeholder engagement, integration confirmation, environment assumptions
- Solution design
  - functional design, architecture definition, security plan, reporting model, data flows
- Build and configuration
  - core platform, access model, verification workflows, reporting, audit logging
- Integration delivery
  - DHA, credit bureau, banking, and payroll-related integration workstreams
- Testing and prototype readiness
  - functional testing, integration testing, customer demonstration readiness, environment validation
- Training and handover
  - GPT IT first-line support training, user guidance, operational documentation
- Go-live and stabilization
  - controlled rollout, issue management, transition into operational support

### 6.2 Phase 2: Support, Maintenance, and Continuous Improvement

Phase 2 covers the remaining 24 months and is focused on keeping the platform stable, secure, and aligned to GPT operating needs. Activities include:

- incident and service request support
- patching and maintenance updates
- monitoring, alerting, and operational review
- periodic DR testing and recovery validation
- controlled enhancement and update management
- documentation refresh where required

### 6.3 Delivery Governance

Because several key dependencies are customer-controlled or third-party-controlled, governance is essential. The implementation plan will therefore include:

- stakeholder engagement planning
- issue and risk management
- dependency tracking
- milestone-based acceptance
- evidence-backed readiness reviews for key integration and security checkpoints

This is especially important for DHA connectivity, SITA environment readiness, and any banking or payroll-related interfaces that require customer-side access coordination.

### 6.4 Team and Capability Alignment

The tender places scoring emphasis on named roles and evidence of qualifications and experience. The implementation approach therefore assumes a delivery team that includes:

- project management
- software development
- solutions architecture
- business analysis
- supporting security, integration, and testing capability as needed

Updated CVs, qualifications, and role-aligned evidence should be positioned not as generic credentials, but as proof that the team can deliver a comparable enterprise solution within the stated time and governance constraints. Waymark Infotech's prior work across public sector, telecoms, and financial services environments provides a strong base for this delivery model, particularly where biometric verification, government interfaces, and regulated operational controls intersect.

### 6.5 Prototype Readiness

The prototype should be treated as an early delivery workstream, not a late-stage bid accessory. The implementation plan will include explicit preparation for:

- user access creation and authentication
- utilization reporting
- ID validation logic
- consent capture
- ten-fingerprint capture
- DHA submission and response handling
- reporting and Excel export

This improves Stage 1C readiness and reduces the risk of disconnect between the proposal promise and the demonstrated solution path.

---

## 7. Assumptions and Dependencies

This proposal is based on several key assumptions derived from the tender and current project analysis.

### 7.1 Assumptions

- GPT will provide or enable the approved IP configuration needed for DHA connectivity.
- The target SITA-managed Windows environment will be made available in line with the delivery plan.
- GPT, Department of e-Government, and related stakeholders will support access-control, hosting, and governance alignment activities.
- Required third-party integration arrangements can be established for DHA, credit bureau, banking, and payroll-related interfaces.
- Delivery may be performed through a controlled mix of on-site and VPN-enabled remote work.

### 7.2 Dependencies

- DHA environment connectivity and access approvals
- SITA infrastructure readiness
- Credit bureau service access and commercial setup
- Banking validation interface definition
- Persal or payroll-related interface availability
- Availability of GPT stakeholders for design validation, testing, and sign-off

### 7.3 Constraints

- Development, deployment, and training must complete within 12 months.
- Support and maintenance must continue through month 36.
- No third-party license cost may be charged for use of the delivered platform.
- All data and all project-generated IP must vest exclusively in GPT.
- Hosting must remain within the mandated SITA-managed environment.

These items should be treated as explicit delivery and proposal controls, not background assumptions.

---

## 8. Benefits and Outcomes

The expected outcome of the proposed engagement is a more controlled, more reliable, and more scalable verification capability for GPT and GPG. The value is not limited to one system implementation. It includes measurable improvement in data integrity, process efficiency, governance control, and risk reduction across multiple public-sector functions.

Expected benefits include:

- improved employee vetting and payroll-data integrity
- stronger fraud prevention and due-diligence controls
- better verification of suppliers, beneficiaries, and sensitive public-service cases
- reduced manual verification effort and faster decision cycles
- stronger audit posture through better logging, traceability, and policy enforcement
- better cross-department operational consistency under GPT governance
- government retention of data, source code, and deployment rights for long-term value

These outcomes align directly to the tender's stated goals of improving internal controls, preventing adverse audit findings, supporting science-based decision-making, and modernizing service delivery through a secure verification platform.

In practical terms, Waymark Infotech's role is to bring proven systems-integration capability, biometric verification experience, and a prototype-led delivery model that reduces uncertainty early and improves the likelihood of a controlled, supportable deployment.

---

## 9. Company Profile and Relevant Experience

Waymark Infotech has delivered custom core business applications as a systems integrator since 2003. Our delivery model is built around collaboration, early requirement discovery, and prototype-led validation so that business goals, solution design, and implementation constraints are aligned as early as possible. This approach is especially relevant for engagements such as this one, where the project includes public-sector governance requirements, multiple external dependencies, and a high need for operational control, auditability, and risk reduction.

Our experience spans public sector, telecoms, and financial services environments, including regulated and verification-heavy implementations. This background is relevant to GPT's requirement because the tender is not only asking for application development. It is asking for a controlled verification platform that integrates with trusted external information holders, supports sensitive decision-making, and can be governed over time within a public-sector operating model.

Relevant Waymark Infotech engagements include:

- South African Social Security Agency (SASSA)
  - Biometric enrolment and verification of beneficiary identities using Department of Home Affairs APIs
  - Included development of a PKI-based digital signature and non-repudiation capability
- National Lotteries Commission
  - Online grant application submission, adjudication, verification, and vetting of organizations and their directors / members
  - Included integrations with CIPC, DSD, SARS, banking services, and South African Fraud Prevention interfaces
- Electoral commissions across the African continent
  - Biometric enrolment and verification of voters for Zambia, Tanzania, Guinea, and Liberia electoral programs
- Independent Electoral Commission of Lesotho
  - Enrolment and identity verification of voters using Ministry of Home Affairs API services
- Eswatini Mobile
  - Biometrics-based mobile subscriber registration and verification for regulatory compliance

These engagements demonstrate experience in biometric workflows, identity verification, public-sector and regulatory operating contexts, and interface-led solution delivery. They also support the credibility of Waymark Infotech's proposed implementation approach for GPT, particularly where prototype validation, controlled integration, and secure operational handover are required.

For this response, Waymark Infotech has structured its approach around four themes:

- business context and understanding of requirements
- proposed solution
- implementation approach and methodology
- maintenance and support of the solution

---

## 10. Next Steps

The following next steps are recommended to move from draft proposal to submission-ready response:

1. Finalize administrative compliance packaging, including all mandatory forms and supporting documents.
2. Attach team qualifications, updated CVs, and comparable-client references aligned to the technical scoring model.
3. Finalize the standards-based security plan and architecture evidence required for Stage 1B.
4. Confirm commercial treatment of credit bureau service and ensure pricing remains compliant with the no-license-cost rule.
5. Prepare and test the prototype against the Stage 1C scoring checklist, with particular focus on DHA connectivity assumptions.
6. Validate customer-controlled dependencies and reflect them consistently in the final submission.

---

## 11. Appendices

### Appendix A: Requirement Mapping Summary

The proposal structure aligns to the requirement mapping prepared for `GT/GPT/009/2026`. High-priority coverage areas are distributed as follows:

| Requirement Area | Primary Proposal Section |
|---|---|
| Business goals and multi-department use cases | Executive Summary, Customer Challenges, Proposed Solution |
| Web-based biometric platform capability | Proposed Solution |
| DHA, credit bureau, banking, and payroll-related integration | Proposed Solution, Solution Architecture |
| SITA hosting and GPT control model | Solution Architecture, Security and Compliance Considerations |
| POPIA, encryption, MFA, RBAC, audit logging, DR, uptime | Security and Compliance Considerations |
| 12-month implementation and 24-month support | Implementation Approach |
| Credit bureau service model and no-license-cost constraint | Proposed Solution, Assumptions and Dependencies |
| GPT-exclusive data and IP ownership | Security and Compliance Considerations, Assumptions and Dependencies |
| Prototype and evaluation readiness | Proposed Solution, Implementation Approach, Next Steps |
| Administrative submission compliance | Next Steps |

### Appendix B: Assumptions and Dependencies Summary

- GPT-approved IP and access arrangements are required for DHA connectivity.
- SITA-managed Windows hosting is a mandatory environmental constraint.
- Several external and customer-controlled interfaces require coordinated onboarding.
- Prototype success depends on environment readiness as well as solution functionality.

### Appendix C: Team and Delivery Evidence

To be inserted in the final submission:

- project manager CV and qualifications
- software developer CV and qualifications
- solutions architect CV and qualifications
- business analyst CV and qualifications
- supporting certificates and evidence of experience

### Appendix D: Reference Evidence

To be inserted in the final submission:

- signed client reference letters
- corresponding letters of award
- evidence of comparable enterprise or public-sector delivery

### Draft Notes

- This draft is assembled from the current project context, customer profile, RFP analysis, and requirement mapping.
- Detailed commercial pricing, named team evidence, reference documents, and any architecture diagrams still need to be attached or drafted separately.
