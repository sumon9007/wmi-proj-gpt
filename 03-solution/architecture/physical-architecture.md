# Physical Architecture

## Purpose

Describe the deployment-oriented architecture assumptions for the solution, aligned to the tender's requirement for hosting within a SITA-managed Windows environment.

## Deployment Assumptions

- The solution will be deployed into a SITA-managed environment operating on Windows-based infrastructure.
- GPT remains the data owner and governing authority for application and data access.
- Department of e-Government supports governance, security, and hosting alignment.
- Exact network zones, IP allocations, and infrastructure topology remain subject to customer-controlled environment confirmation.

## Environment View

### Development Environment

- Used for controlled build, configuration, and internal testing
- Subject to secure access controls and version management
- Supports documentation and build packaging activities

### Test / Integration Environment

- Used for functional testing, integration validation, and prototype alignment
- Supports DHA and related external interface testing where access is approved
- Used for security-control validation and readiness reviews

### Production Environment

- Operates within the customer-governed SITA-managed target environment
- Hosts the application, integration components, and required data stores
- Supports monitoring, backup, audit logging, and operational control

## Physical Component View

- Web application tier
- Mobile-capable access tier
- Application services tier
- Integration / ESB tier
- Data storage tier
- Logging / monitoring / security services tier
- Backup and recovery services

## Resilience and Operations Considerations

- Backup design must support recoverability in line with stated RTO and RPO requirements.
- Monitoring and alerting must support 24/7 service awareness.
- Patch and update operations must fit GPT security protocols.
- Audit logging must be retained in a way that supports operational review and governance evidence.

## Physical Architecture Constraints

- Hosting must remain within the SITA-managed model.
- No architecture should assume unrestricted vendor-managed external hosting.
- External connectivity, especially to DHA, depends on customer-approved network configuration.
- Final physical topology should only be finalized once the customer environment is confirmed.

## Architecture Position

The physical architecture should be treated as a controlled deployment model rather than a fixed topology at this stage. The key design decision is to align to the mandated hosting and governance environment early, so that no later design rework is caused by non-compliant infrastructure assumptions.
