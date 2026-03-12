# Compliance Mapping

## Purpose

Map key tender requirements to standards, controls, and governance expectations that the solution design must address.

## Standards and Governance Summary

| Requirement Area | Standard / Governance Reference | Design Response |
|---|---|---|
| Personal information protection | POPIA | Consent capture, controlled access, purpose-limited processing, secure handling of biometric and demographic data |
| Information security management | ISO/IEC 27001:2022 | Security controls, governance alignment, logging, access control, resilience, operational security |
| Privacy information management | ISO/IEC 27701:2019 | Privacy-oriented data handling, consent, access governance, controlled processing |
| Biometric integrity | ISO/IEC 30107-3:2017 | Biometric handling controls and integrity considerations in the verification model |
| Software quality expectations | ISO/IEC 25010:2011 | Quality-oriented design approach, maintainability, security, reliability, and usability considerations |
| GPT and Department of e-Government directives | Customer governance requirements | Centralized control, hosting alignment, operational policy compliance, auditability |
| SITA-managed hosting requirement | Hosting / operating constraint | Physical deployment model aligned to mandated environment |

## Tender Control Mapping

| Tender Requirement | Control / Design Implication |
|---|---|
| Data owned and controlled by GPT | Data storage, access, and operating model must remain GPT-governed |
| All IP vests in GPT | Solution delivery and handover must support full transfer of artefacts |
| Encryption in transit and at rest | Security architecture must include encryption controls across storage and integrations |
| RBAC, MFA, and audit logging | Identity and access model must be explicit and enforceable |
| RTO 4 hours / RPO 15 minutes | Backup and DR design must support the required recovery posture |
| 99.5% uptime and 24/7 monitoring | Operational architecture must support monitoring, alerting, and service continuity controls |
| SITA-managed Windows hosting | Physical architecture must align to customer-managed deployment constraints |
| No third-party license costs for system use | Solution approach must avoid licensing-dependent deployment models that violate the tender |

## Compliance Notes

- Standards alignment in the tender is both a design expectation and an evaluation consideration.
- POPIA is not a peripheral requirement; it directly affects workflow, consent, data handling, and operating controls.
- GPT governance requirements must be treated as design controls, not just contractual statements.
- Compliance in this context is as much about traceable operational control as it is about named standards.

## Open Points

- Final internal policy references from GPT and Department of e-Government have not yet been supplied in detail.
- Specific retention, logging, and operational evidence expectations may need refinement during discovery.
- Exact control implementation patterns will depend partly on the confirmed SITA target environment.
