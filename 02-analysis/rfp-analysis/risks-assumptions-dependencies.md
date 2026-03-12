# Risks, Assumptions, and Dependencies

## Assumptions

- GPT will provide approved IP addresses and access coordination required for DHA integration.
- GPT will provide or enable access to the target SITA-managed hosting environment.
- GPT and partner departments will supply required policy inputs for access control, credential governance, and operating procedures.
- Customer-side agreements or approvals needed for DHA, credit bureau, banking, and Persal-related integrations can be established in time.
- Delivery can be performed through a mix of on-site and VPN-enabled remote work.

## Dependencies

- DHA connectivity through GPT-approved IP and test / production access paths
- SITA-managed infrastructure availability
- Department of e-Government support for hosting, governance, and security alignment
- Credit bureau service access and commercial model
- Banking validation interface availability
- Persal or payroll-related integration access and data interface definition
- Availability of GPT stakeholders for requirements confirmation, testing, and sign-off

## Constraints

- First 12 months must cover development, deployment, and training.
- Remaining 24 months must cover support, maintenance, and updates.
- No third-party platform license charges are allowed.
- Hosting must be in a SITA-managed cloud environment on Windows OS.
- Data must remain under GPT ownership and control.
- System access must be centrally controlled by GPT.
- Security controls must include encryption, RBAC, MFA, audit logging, backup, and DR.
- DR targets are fixed at RTO 4 hours and RPO 15 minutes.
- Service availability target is 99.5%.

## Ambiguities / Clarification Points

- The tender describes banking validation requirements, but does not fully define the integration method, data source, or ownership boundaries.
- Persal integration is required functionally, but interface scope and technical constraints are not fully described.
- The exact division of responsibilities between bidder, GPT, Department of e-Government, and SITA during operations may need clarification.
- The tender requires mobile capability and facial recognition, but does not fully specify target usage scenarios, device models, or rollout priority.
- The prototype must connect to DHA in the GPT test environment, but environment readiness and test data details are not defined in the tender.

## Bid Risks

- Missing or incomplete administrative submission items will lead to elimination.
- A weak or incomplete prototype can prevent progress beyond technical evaluation.
- Any pricing model that implies third-party license charges may render the response invalid.
- Failure to accept GPT-exclusive IP ownership and reuse rights may make the bid non-compliant.
- Weak evidence for team qualifications, references, or standards alignment will reduce competitiveness.

## Delivery Risks

- Third-party integration dependency risk with DHA, credit bureau, banking, and payroll-related systems
- Schedule compression risk due to 12-month implementation deadline
- Environment-readiness risk in SITA / customer-controlled hosting and access setup
- Security and compliance burden is high for a system processing biometric and demographic data
- Cross-department stakeholder coordination may slow requirements validation and rollout
- DR and uptime targets may require more operational maturity than a minimal implementation approach would support

## Recommended Mitigations

- Treat administrative compliance as a gated workstream with explicit sign-off.
- Start prototype planning and dependency confirmation early, not after proposal submission.
- Make hosting, IP, and licensing assumptions explicit in the commercial and solution response.
- Build the implementation plan around dependency management and staged integration readiness.
- Use the proposal to clearly show how security, resilience, and operational control are designed in from day one.
