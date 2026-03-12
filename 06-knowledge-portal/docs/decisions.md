# Decisions

## Current Design And Delivery Decisions

### 1. SITA-Managed Hosting Is A Hard Constraint

The solution is designed around a SITA-managed Windows environment. Vendor-hosted or unconstrained cloud assumptions are out of bounds.

### 2. GPT Owns Data And Project-Generated IP

Data, source code, configuration, and related project artefacts are treated as GPT-owned. This is both a contractual constraint and a design driver.

### 3. Integration Must Be Centrally Orchestrated

The architecture assumes an ESB or equivalent orchestration layer rather than point-to-point integrations. This supports control, monitoring, and phased onboarding.

### 4. Security Controls Are Core Architecture, Not Add-Ons

RBAC, MFA, encryption, audit logging, backup, DR, and monitoring are treated as mandatory design elements because they directly affect compliance and evaluation.

### 5. Delivery Is Split Into Implementation Then Support

The engagement is planned as 12 months of implementation followed by 24 months of support and maintenance. Planning, handover, and staffing should align to that model.

### 6. Prototype Readiness Is A Real Delivery Stream

The prototype is not a side activity. It is part of the bid-critical path and should reflect the intended production design as closely as practical.

## Open Decisions Or Confirmation Items

- exact network and environment topology within the SITA model
- confirmed DHA access mechanics and whitelisted IP arrangements
- detailed banking and payroll-related interface definitions
- named customer sign-off roles and governance cadence
- final operating split between GPT IT, Department of e-Government, SITA, and bidder support teams

## Constraints Being Treated As Decisions

- no third-party platform license cost for system use
- GPT control over access policies and data usage
- public-sector compliance-first operating posture
- phased integration onboarding where technical interface detail is incomplete
