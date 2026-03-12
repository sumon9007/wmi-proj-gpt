# Logical Architecture Diagram Spec

## Purpose

Provide a diagram-ready specification for the logical architecture of the biometric authentication platform.

## Diagram Title

Logical Architecture: Gauteng Provincial Treasury Biometric Authentication Platform

## Diagram Type

Layered architecture diagram

## Diagram Sections

### Section 1: User Interaction Layer

Components:

- Departmental users
- GPT administrators
- Desktop web interface
- Mobile-capable interface

### Section 2: Verification and Workflow Layer

Components:

- Authentication and session management
- Consent capture
- ID / passport pre-validation
- Biometric capture orchestration
- Verification workflow engine
- Rules-based decision engine

### Section 3: Integration and Orchestration Layer

Components:

- ESB / orchestration layer
- Request transformation
- Routing and interface control
- Error handling and retry management

### Section 4: External Information Holders

Components:

- Department of Home Affairs
- Credit bureau services
- Banking validation services

### Section 5: Data and Reporting Layer

Components:

- Verification results store
- Audit log repository
- Reporting and dashboard services
- Exception reporting

### Section 6: Security and Operations Layer

Components:

- RBAC
- MFA
- Encryption services
- Monitoring and alerting
- Backup and DR controls

## Key Flows to Show

1. User logs in through desktop or mobile interface.
2. User captures consent and identity details.
3. Biometric and identity data flow into the verification layer.
4. Verification layer sends request to the ESB.
5. ESB routes requests to DHA, credit bureau, and banking services as applicable.
6. Responses return through the ESB to the application layer.
7. Results are stored in GPT-controlled repositories.
8. Reporting and audit services consume stored result and event data.

## Annotations to Include

- GPT centrally controls access and governance.
- Data remains government-owned.
- Hosting and deployment occur in a SITA-managed environment.
- External connectivity is subject to GPT-approved IP and access controls.
