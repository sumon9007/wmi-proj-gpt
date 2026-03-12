# Proposal Approval Workflow

This document defines the stages, sign-offs, and roles required to move a proposal from draft to submission.

## Overview

Proposals move through this lifecycle:

```
DRAFT → INTERNAL REVIEW → READY FOR SUBMISSION → SUBMITTED → WON/LOST
```

Each stage requires specific approvals before proceeding to the next.

## Proposal Lifecycle Stages

### Stage 1: DRAFT (Days 1-3)

**Status:** In active development; not for review

**Responsibility:** Pre-Sales Engineer / Solution Architect

**Activities:**
- Write initial draft using content modules and response library
- Internal team reviews for completeness and accuracy
- Resolve major gaps

**Approval Required:** None yet

**Exit Criteria:**
- All RFP requirements addressed in proposal
- No placeholder text or {{VARIABLES}} remaining
- Internal team (arch, presales) confident in content

### Stage 2: INTERNAL REVIEW (Days 3-5)

**Status:** Proposal is under formal review

**Responsibility:** Multiple reviewers, owned by Proposal Manager

**Review Roles & Approval Authority:**

| Role | Focus Area | Approval Level | Sign-off Timing | Authority |
|---|---|---|---|---|
| **Solution Architect** | Technical accuracy, architecture credibility, feasibility | Required | Within 24 hours | Can request major changes |
| **Pre-Sales Leader** | Customer-facing language, completeness, messaging, RFP alignment | Required | Within 24 hours | Can request revisions |
| **Delivery PM** | Timeline realism, resource commitments, delivery feasibility | Required | Within 48 hours | Can flag risks, request timeline changes |
| **Pricing/Finance** | Cost estimates, margins, commercial terms | Required (if included) | Within 48 hours | Can request cost/scope changes |
| **Legal** | Terms & conditions, liability, compliance statements | Required (if included) | Within 48 hours | Can request legal language changes |
| **Sales Leadership** | Strategic alignment, competitive positioning, win confidence | Recommended | By sign-off | Can escalate if concerns |

**Review Process:**

1. **Proposal Manager** creates review checklist and distributes draft to all reviewers
2. Each **Reviewer** provides written feedback:
   - Issues/corrections in Markdown comments (suggested edits)
   - Approval status: ✅ Approved | ⚠️ Approved with conditions | ❌ Revision required
   - Rationale for conditions/required changes
3. **Proposal Manager** consolidates feedback, creates revision list
4. **Lead Author** addresses feedback, revises proposal
5. **Proposal Manager** obtains final sign-offs

**Sign-Off Tracking:**

Mark each approval in `/05-deliverables/proposals/{RFP-ID}/metadata.yml`:

```yaml
solution_architect_approved: yes | Date: 2026-03-13 | Name: [Name]
presales_engineer_approved: yes | Date: 2026-03-13 | Name: [Name]
delivery_pm_approved: yes with conditions | Date: 2026-03-13 | Name: [Name] | Condition: Timeline assumes resource availability
legal_approved: not-required | Date: N/A
sales_leadership_approved: yes | Date: 2026-03-13 | Name: [Name]
```

**Exit Criteria:**
- ✅ Solution Architect signed off (technical credibility)
- ✅ Pre-Sales Engineer signed off (customer readiness)
- ✅ Delivery PM signed off (delivery feasibility)
- ✅ Legal signed off (if applicable)
- ✅ Sales Leadership signed off (strategic alignment)
- Proposal Manager confirms all sign-offs in metadata.yml

### Stage 3: READY FOR SUBMISSION (Days 5-6)

**Status:** Proposal approved for submission

**Responsibility:** Proposal Manager + Sales Lead

**Activities:**
- Final formatting and branding applied
- PDF/Word exports created
- Submission checklist completed
- Cover letter / transmittal prepared

**Approval Required:** None (already approved in Stage 2)

**Exit Criteria:**
- All exports (PDF, Word, PowerPoint if required) generated
- Submission package reviewed for formatting/completeness
- Delivery method confirmed with customer
- Submission timeline confirmed with sales lead

### Stage 4: SUBMITTED (Day 6-7)

**Status:** Proposal has been submitted to customer

**Responsibility:** Sales Lead (actual submission)

**Activities:**
- Submission via [[email/portal/courier]] per RFP requirements
- Submission confirmation documented
- Customer advised of submission
- Steering committee notified

**Update Metadata:**

```yaml
submission_date: 2026-03-13
submission_method: email
submission_confirmation: RE: Proposal Submission - ACMECORP-CLOUD
submission_notes: Submitted to [Customer Contact] at [Email] per RFP requirements
```

**Exit Criteria:**
- Customer acknowledges receipt
- Submission confirmation documented

### Stage 5: WON / LOST

**Status:** Customer decision made

**Responsibility:** Sales Lead (decision communication) → Knowledge Manager (catalogue)

**For WON Proposals:**
- Celebrate! 🎉
- Schedule post-mortem win analysis
- Extract key winning differentiators
- Index winning responses to `/11-response-library/`
- Update metadata with win analysis

**For LOST Proposals:**
- Conduct loss analysis (why did we lose?)
- Document loss root cause in metadata
- File in `/10-archive/` with loss analysis
- Extract any best practices that worked despite loss

---

## Approval Checklist by Role

### Solution Architect Checklist (Technical Review)

Before approving, verify:

- [ ] Architecture is technically sound and feasible
- [ ] All technical RFP requirements are addressed
- [ ] Proposed technology stack is supported internally
- [ ] Design decisions are explained with rationale
- [ ] No architectural gaps or inconsistencies
- [ ] Diagrams are accurate and professional
- [ ] Risk mitigations are credible
- [ ] Scalability and performance claims are justified
- [ ] Security architecture meets requirements

**Common Issues to Raise:**
- "Architecture uses technology we don't support internally"
- "Timeline assumes 4-week infrastructure build, not realistic"
- "Scaling approach doesn't address stated 100K user requirement"
- "Security section misses customer's specific compliance requirement"

### Pre-Sales Engineer Checklist (Customer Readiness)

Before approving, verify:

- [ ] Executive summary is compelling and business-focused
- [ ] Customer's pain points are clearly articulated
- [ ] Solution addresses stated customer challenges
- [ ] Proposal language is professional and customer-centric
- [ ] No jargon without explanation
- [ ] All RFP requirements explicitly referenced/answered
- [ ] Messaging aligns with their stated priorities
- [ ] Examples are relevant to their industry
- [ ] Tone matches customer's sophistication level
- [ ] Proposal answers "Why you?" (differentiation)

**Common Issues to Raise:**
- "Executive summary is too technical; decision-makers won't read this"
- "We don't reference their stated need for 99.99% uptime"
- "Using banking examples for a healthcare customer"
- "Implementation section doesn't explain how customer's data will be migrated"

### Delivery PM Checklist (Feasibility Review)

Before approving, verify:

- [ ] Timeline is realistic given project complexity
- [ ] Resource allocations are achievable (no double-booking)
- [ ] Critical path items are identified
- [ ] Dependencies on customer are reasonable
- [ ] Risk mitigations are achievable within timeline
- [ ] Post-go-live support commitment is sustainable
- [ ] Team availability matches proposal commitment
- [ ] No major gaps between proposed and feasible approach

**Common Issues to Raise:**
- "We promised 16-week implementation but don't have capacity until week 8"
- "Timeline assumes 3 customer stakeholders available full-time; they said 20% availability"
- "Post-go-live support requires 2 people for 6 weeks; we can't commit to this"

---

## Conditions & Required Changes

If a reviewer approves "with conditions," the condition must be addressed:

**Examples:**

```
Pre-Sales Engineer: Approved with conditions
Condition: "Security section must reference HIPAA specifically, not just generically"
Resolution: Add HIPAA-specific controls before final submission

Delivery PM: Approved with conditions  
Condition: "Timeline assumes project starts March 15; if delayed past April 1, must revise"
Resolution: Confirm start date with customer before submission

Sales Leadership: Approved with conditions
Condition: "Competitive positioning section could be stronger; highlight our AWS certification"
Resolution: Enhance competitive comparison in solution section
```

If a reviewer requires revision (does NOT approve), the proposal cannot move to next stage until revised and re-approved.

---

## Sign-Off Authority

**Who can approve moving to next stage?**

- **Proposal Manager** owns the sign-off checklist; cannot approve on behalf of reviewers
- **Each Reviewer role** must affirmatively approve their area
- **Sales Lead** has final authority to submit (can override concerns with Risk Acknowledgement)

**Risk Acknowledgement Process:**

If a reviewer has concerns but Sales Lead wants to proceed anyway:

1. **Sales Lead** documents the risk in metadata:
   ```yaml
   known_risks:
     - "Delivery PM concerned about timeline feasibility; sales confident customer will flex"
     - "Legal flagged IP ownership language; customer agreed to standard terms"
   ```

2. **Sales Lead** signs off on risk acknowledgement with date and name
3. Proposal proceeds to submission with documented risk
4. Post-win, these risks are reviewed (were we right to take them?)

---

## Timing Requirements

Different RFP deadlines require different workflows:

### Rush Proposals (< 48 hours to deadline)

**Compressed workflow:**
- Draft + Internal Review happen simultaneously (1 day)
- Minimum reviewers: Solution Architect + Pre-Sales Engineer
- Delivery PM reviews async if possible; flag any deal-breaker issues only
- Sales Lead decides: proceed or decline bid

**Fast-track sign-off:**
```yaml
archived_timeline: "Rush - compressed review due to {{DAYS}} day deadline"
reviewers_included: [Solution Architect, Pre-Sales Engineer, Sales Lead]
approval_timeline: Same day
```

### Standard Proposals (3-7 days to deadline)

**Normal workflow as described above**
- 2-3 days for draft creation
- 2-3 days for internal review with full reviewer participation
- 1 day for final submission prep

### Strategic Proposals (> 7 days to deadline)

**Enhanced workflow:**
- Multiple internal review cycles
- Customer-facing messaging review with product/marketing
- Competitive positioning deep-dive
- Practice pitch with full team before submission

---

## Escalation Path

If reviewers disagree on approval:

**Level 1:** Proposal Manager facilitates discussion between reviewers

**Level 2:** Escalate to Sales Lead + Architecture Lead
- They make final decision on disputed items
- Decision is documented in metadata

**Level 3:** If still unresolved, Delivery Leadership decides whether to bid or decline

---

## Document Control

**Proposal Version Tracking:**

Save versions at key milestones:
```
proposal-v1-draft.md          # Initial draft
proposal-v2-after-review.md   # After internal feedback
proposal-v3-final.md          # Approved, ready for submission
```

Keep `metadata.yml` updated with version status at each stage.

---

## Post-Submission Learnings

After submission (or after outcome), conduct brief retrospective:

**Winning Proposals:**
- What were the top 3 things that made this proposal compelling?
- What unique differentiators did we highlight?
- Which content modules were most effective?
- Extract into `/11-response-library/` for future reuse

**Lost Proposals:**
- Why did we lose (if feedback available)?
- What would we write differently?
- What response library patterns didn't work here?

---

## Summary: Role Owners & Timing

| Stage | Owner | Approvals Needed | Timeline | Exit Criteria |
|---|---|---|---|---|
| **DRAFT** | Pre-Sales Eng / Architect | None | Days 1-3 | All RFP requirements addressed, no placeholders |
| **INTERNAL REVIEW** | Proposal Manager | Architect, Presales, PM, (Legal), Leadership | Days 3-5 | All roles signed off in metadata.yml |
| **READY FOR SUBMISSION** | Proposal Manager + Sales | None | Days 5-6 | Exports created, submissionplan confirmed |
| **SUBMITTED** | Sales Lead | None (confirmation only) | Day 6-7 | Customer acknowledgment of receipt |
| **POST-OUTCOME** | Knowledge Manager | None | After decision | Response catalogued or archived |
