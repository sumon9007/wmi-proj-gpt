# Architecture

## Solution Summary

The proposed solution is a centrally governed biometric authentication platform for Gauteng Provincial Treasury. It is intended to support multiple government departments while keeping access control, data ownership, and operational governance under GPT.

The design is built around five principles:

- central governance
- secure integration
- government ownership
- resilience by design
- practical extensibility across departments and use cases

## Logical Architecture

The logical design separates the platform into clear control layers:

- user interaction layer for desktop and mobile-capable access
- verification and workflow layer for consent capture, biometric orchestration, and rules-based decisioning
- integration and orchestration layer for DHA, credit bureau, banking, and payroll-related interfaces
- data and reporting layer for records, audit data, and reporting outputs
- security and operations layer for RBAC, MFA, encryption, monitoring, backup, and DR

This layered design supports traceability, phased onboarding of interfaces, and stronger operational control than a single monolithic application.

## Physical And Hosting Model

The deployment model assumes a SITA-managed Windows-based environment as a hard constraint. The physical architecture should therefore be treated as a controlled deployment model rather than a vendor-hosted topology.

Core physical components include:

- web application tier
- application services tier
- ESB or integration tier
- data storage tier
- monitoring and security services
- backup and disaster-recovery services

## Integration Overview

The integration layer is central to the solution:

- DHA is the most critical external dependency and requires GPT-approved IP and access arrangements
- credit bureau capability is both a service component and an integration workstream
- banking validation is in scope but needs interface clarification
- payroll and Persal-related interfaces are functionally required but should be staged based on confirmed customer-side definitions

An ESB-led approach is preferred to avoid point-to-point sprawl and to preserve monitoring, routing, transformation, and auditability.

## Security Architecture Summary

The security design is built around public-sector governance requirements:

- GPT-controlled role-based access
- MFA for system and data access
- encryption at rest and in transit
- consent capture within business workflows
- comprehensive audit logging
- monitoring and alerting
- backup and DR aligned to RTO 4 hours and RPO 15 minutes
- POPIA and ISO-aligned control posture

## Related Artifacts

Detailed architecture and diagram-spec source files are available in:

- `/03-solution/architecture/`
- `/03-solution/diagrams/`

Diagram specs exist for logical, physical, security, and integration views if rendered visuals are needed later.
