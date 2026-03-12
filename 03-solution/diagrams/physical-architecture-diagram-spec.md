# Physical Architecture Diagram Spec

## Purpose

Provide a diagram-ready specification for the deployment view of the solution.

## Diagram Title

Physical / Deployment Architecture: SITA-Managed Hosting Model

## Diagram Type

Environment and deployment diagram

## Diagram Zones

### Zone 1: User Access

- Departmental user workstations
- Mobile user devices
- GPT administrative access

### Zone 2: Application Access Tier

- Web access tier
- Mobile access gateway or access services

### Zone 3: Application Services Tier

- Core application services
- Workflow and decisioning services
- Reporting services

### Zone 4: Integration Tier

- ESB / integration services
- Secure external interface connectors

### Zone 5: Data Tier

- Verification data store
- Audit log store
- Reporting / analytics data structures

### Zone 6: Operations and Resilience Tier

- Monitoring and alerting services
- Backup services
- DR / recovery services

### Zone 7: External Systems

- DHA
- Credit bureau
- Banking validation services
- Payroll / Persal-related systems

## Environment Views to Label

- Development
- Test / integration
- Production

## Required Notes

- All core deployment is aligned to a SITA-managed Windows environment.
- Exact topology and network segmentation remain subject to customer confirmation.
- DHA connectivity is dependent on GPT-approved IP and external access controls.
- Backup, monitoring, and DR are required operational capabilities, not optional add-ons.
