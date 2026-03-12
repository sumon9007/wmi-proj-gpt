# Requirement Mapping

## Overview

This page summarizes how the tender requirements for `GT/GPT/009/2026` map to the proposed solution, delivery model, and proposal structure. It is intended to preserve traceability and highlight the highest-attention items without reproducing every internal proposal note.

## Mapping Scope

- Tender: GT/GPT/009/2026
- Opportunity: Development of Biometric Authentication System Including Support and Maintenance for a Period of 3 Years
- Coverage status: full mapping completed in the internal proposal workspace

## Requirement Families

### Administrative Compliance

- mandatory signed bid forms and submission documentation
- POPIA consent and integrity-related forms
- tax, registration, and supplier-status evidence
- preference-point support documentation

These are elimination-sensitive and should be treated as bid-pack controls rather than narrative-only items.

### Business And Functional Requirements

- web-based biometric authentication platform
- shared use across multiple departments and municipalities
- support for recruitment, payroll, supplier, forensic, and beneficiary-related verification use cases
- real-time and bulk verification capability
- reporting, audit trails, workflow, and exception handling

### Technical And Integration Requirements

- DHA integration
- credit bureau integration and service model
- banking-validation support
- payroll or Persal-related integration support
- ESB or controlled orchestration layer
- SITA-managed Windows hosting

### Security, Compliance, And Governance Requirements

- POPIA alignment
- GPT-led access control and governance
- encryption at rest and in transit
- RBAC and MFA
- audit logging and monitoring
- disaster recovery and uptime commitments
- GPT ownership of data, source code, configuration, and project-generated IP

### Delivery And Support Requirements

- implementation in the first 12 months
- support and maintenance through month 36
- training and first-line support enablement for GPT IT
- full documentation and handover set
- prototype readiness for demonstration scoring

## High-Attention Items

The most important mapped items from a delivery and bid-risk perspective are:

- DHA connectivity through GPT-approved IP arrangements
- SITA-managed Windows hosting as a hard architecture constraint
- no third-party platform license cost for system use
- GPT-exclusive ownership of code, data, configuration, and artefacts
- DR targets of RTO 4 hours and RPO 15 minutes
- 99.5 percent uptime and 24/7 monitoring expectations
- administrative compliance completeness
- prototype and demonstration readiness

## Internal Source

The full internal traceability matrix is maintained in:

- `/05-deliverables/proposals/2026-GAUTENGTREASURY-BIOMETRIC-AUTHENTICATION/requirement-mapping.md`

That document remains the detailed working version. This portal page is the condensed, browse-friendly version for the published knowledge base.
