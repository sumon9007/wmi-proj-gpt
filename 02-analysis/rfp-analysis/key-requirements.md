# Key Requirements

## Functional Requirements

- Build a web-based biometric authentication system for GPT/GPG.
- Integrate with Department of Home Affairs systems for identity verification.
- Integrate with credit bureau services for demographic, employment, address, and business-interest checks.
- Support fingerprint capture, facial recognition, and identity-number-based processing.
- Support bulk verification using identity numbers.
- Validate banking details, addresses, and mortality status.
- Integrate with Persal-related payroll workflows.
- Provide decisioning, reporting, dashboards, audit trails, and exception reporting.
- Support desktop web and mobile operation on Android and iOS.
- Support one-to-many searches from the GPG database.

## Non-Functional Requirements

- Real-time query, transport, receipt, and storage of verification results.
- Compatibility with Microsoft-aligned operating environment and latest Microsoft browser.
- Support Lumidigm V302-20 series or recent equivalent / DHA-approved devices.
- 99.5% minimum uptime, excluding scheduled maintenance.
- 24/7 monitoring and automated incident alerting.
- DR requirements:
  - RTO: 4 hours
  - RPO: 15 minutes
  - Semi-annual DR testing

## Security and Compliance Requirements

- POPIA compliance and consent capture before personal-information verification.
- Data encryption in transit and at rest.
- Role-based access control, MFA, and comprehensive audit logging.
- Secure storage and management of biometric data.
- Alignment with GPT and Department of e-Government security and governance policies.
- SITA-managed Windows-based hosting environment.
- Standards alignment expected in the technical response:
  - ISO/IEC 27001:2022
  - ISO/IEC 27701:2019
  - ISO/IEC 30107-3:2017
  - ISO/IEC 25010:2011

## Commercial and Contractual Requirements

- Contract term is 3 years.
- Development, deployment, and training must complete within the first 12 months.
- Years 2 and 3 are for support, maintenance, and updates.
- Bidder must provide credit bureau service for the contract duration.
- No third-party license costs may be charged for system use.
- Annual maintenance and support fees are allowed.
- All data is owned and controlled by GPT.
- All IP, source code, documentation, schemas, and related artefacts vest exclusively in GPT.
- GPT may reuse and deploy the solution across broader government entities without additional royalty or licensing fees.

## Evaluation, Demo, and Submission Requirements

- Mandatory administrative forms and supporting documents must be complete and signed.
- Technical response must include:
  - risk assessment
  - architecture design diagram
  - deliverables and timelines
  - project purpose and objectives
  - standards-based security plan
  - project plan with scope, schedule, resources, stakeholder engagement, issue management, and post-implementation support
- Team submission must include CVs, qualifications, and evidence of relevant experience.
- References must include signed client letters and letters of award.
- Prototype must demonstrate:
  - user creation and authentication
  - user utilization reporting
  - SA ID validity checks and blocking invalid input
  - consent capture with date/time
  - ID and ten-fingerprint capture
  - DHA submission and response handling
  - returned name / initials, surname, photo, and matched fingerprint results
  - error handling for invalid IDs
  - report display and Excel export

## Highest-Proposal-Priority Items

- Administrative compliance pack, because failure causes elimination.
- Prototype readiness, because Stage 1C has a minimum threshold and requires working capability.
- SITA hosting and GPT-controlled governance, because they shape the entire architecture.
- No-license-cost rule and full GPT IP ownership, because they directly affect pricing and commercial acceptability.
- DR, uptime, monitoring, and auditability, because they are explicit and high-impact non-functional requirements.
