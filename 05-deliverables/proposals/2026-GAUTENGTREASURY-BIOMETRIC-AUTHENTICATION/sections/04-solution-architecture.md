## Solution Architecture

The proposed architecture is designed around four principles that are strongly implied by the tender: central governance, secure integration, operational resilience, and government ownership. To reflect those principles, the architecture separates capture, integration, decisioning, data management, and reporting into controlled layers rather than embedding everything into a monolithic application.

### Logical Architecture

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

### Hosting and Deployment Model

The deployment model is aligned to the tender's hard constraints. The complete solution, including application components, configuration, source code, and related artefacts, is intended for hosting within a SITA-managed Windows-based environment, supported by the Department of e-Government. This requirement shapes infrastructure design decisions from the outset and avoids any architecture that depends on non-compliant hosting assumptions.

All data is assumed to remain within the GPT-controlled environment, with access governed centrally by GPT. This supports the tender's requirements for government ownership, controlled access, and protection of sensitive biometric and demographic data.

### Integration Approach

The integration layer is a central architectural element because the platform must operate across several external and internal systems with different security, interface, and governance expectations. For that reason, the proposal includes an ESB or equivalent integration orchestration capability to handle movement, transformation, storage coordination, encryption, and controlled interface management.

Special attention is given to DHA connectivity, because the tender makes it clear that access will depend on GPT-approved IP standards and customer-controlled access arrangements. The architecture therefore assumes that external institution verification, especially DHA connectivity, will be mediated through approved customer-network parameters such as Site-ID, Workstation-ID, and whitelisted IP paths.

### Device and Functional Compatibility

The platform design supports Lumidigm V302-20 series devices, recent equivalent devices, and other DHA-approved biometric capture devices, as required by the tender. It also supports both biometric input and numeric input, which is important for bulk verification and for workflows where biometric capture is not the only required entry mechanism.

The architecture further supports:

- one-to-many search against the GPG database
- bulk identity-number-based verification
- reporting and export
- exception handling
- auditability across user actions and system events

### Architecture Outcome

The result is an architecture that is not only technically suitable, but also structurally aligned to GPT's operating needs. It supports central control, controlled integration, resilience, and future extension across departments without undermining the governance model defined in the tender.

[Diagram: Physical Architecture]
[Diagram: Integration Architecture]
