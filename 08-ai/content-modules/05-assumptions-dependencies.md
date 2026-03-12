# Content Module: Assumptions & Dependencies

## Purpose

This critical section explicitly lists the assumptions your proposal is based on and the dependencies outside your control. Customers often overlook this section, but it's your safety net — it clarifies what could cause your timeline or budget to slip.

**When to use:** Required for all proposals, especially implementation.

**Estimated customization time:** 30-45 minutes

**Complexity level:** Basic

## Metadata

```yaml
module_name: assumptions-dependencies
applicable_to: [implementation, consulting, managed-service]
estimated_time_to_customize: 30-45 min
common_industries: [all]
typical_length: 1-2 pages
optimal_position: Section 7 (after implementation approach)
estimated_impact: High (prevents scope creep disputes and unmet expectations)
requires_project_manager_input: true
```

## Key Principles

1. **Explicit** — Don't assume the reader will infer; state every assumption clearly
2. **Realistic** — Assumptions should be reasonable, not unreasonable barriers
3. **Mutually understood** — Customer should agree with these assumptions
4. **Qualified** — Show which assumptions are high-risk
5. **Gating** — Some assumptions are prerequisites (must be true or timeline/budget changes)

## Generic Template

---

### ASSUMPTIONS & DEPENDENCIES

This proposal is based on the following assumptions and depends on the following items from your organization. If any assumptions prove incorrect or dependencies aren't met, we will revisit timeline and cost.

#### Assumptions

**About Your Organization:**

- **Current State Assessment** — {{ASSUMPTION_ABOUT_CURRENT_SYSTEMS}}
  - Impact if wrong: {{TIMELINE_IMPACT}} delay, {{COST_IMPACT}} additional cost
  - Verification: {{HOW_VERIFIED}} (assessment, data sample review, stakeholder interview)
  - Risk Level: {{GREEN/AMBER/RED}}

- **Data Availability** — {{ASSUMPTION_ABOUT_DATA_READINESS}}
  - Impact if wrong: {{TIMELINE_IMPACT}} delay
  - Verification: {{HOW_VERIFIED}} (Phase 1 data assessment)
  - Risk Level: {{GREEN/AMBER/RED}}

- **Stakeholder Availability** — {{ASSUMPTION_ABOUT_KEY_PEOPLE_BEING_AVAILABLE}}
  - Impact if wrong: {{TIMELINE_IMPACT}} delay
  - Verification: {{HOW_VERIFIED}} (signed statement from sponsor)
  - Risk Level: {{GREEN/AMBER/RED}}

- **Legacy System Knowledge** — {{ASSUMPTION_ABOUT_DOCUMENTATION_AND_EXPERTISE}}
  - Impact if wrong: {{TIMELINE_IMPACT}} delay
  - Verification: {{HOW_VERIFIED}} (discovery phase validation)
  - Risk Level: {{GREEN/AMBER/RED}}

**About External Environment:**

- **Third-Party System Availability** — {{ASSUMPTION_ABOUT_VENDOR_SYSTEMS_BEING_OPERATIONAL}}
  - Examples: {{SYSTEMS_ASSUMED_AVAILABLE}}
  - Impact if wrong: {{TIMELINE_IMPACT}} delay
  - Risk Level: {{GREEN/AMBER/RED}}

- **Compliance Requirements Unchanged** — {{ASSUMPTION_ABOUT_REGULATORY_LANDSCAPE}}
  - Impact if wrong: {{TIMELINE_IMPACT}} delay, {{COST_IMPACT}} additional cost
  - Risk Level: {{GREEN/AMBER/RED}}

**About Our Engagement:**

- **Scope Definition Stability** — {{ASSUMPTION_ABOUT_RFP_SCOPE_BEING_FINAL}}
  - Impact if wrong: {{COST_IMPACT}} change management process
  - Risk Level: {{GREEN/AMBER/RED}}

- **Technology Stack Stability** — {{ASSUMPTION_ABOUT_PRODUCT_VERSIONS_AND_ROADMAP}}
  - Impact if wrong: {{TIMELINE_IMPACT}} delay, rework required
  - Risk Level: {{GREEN/AMBER/RED}}

#### Dependencies

**From Your Organization (Critical Path):**

| Dependency | Timing | Responsibility | Impact if Late |
|---|---|---|---|
| {{DEPENDENCY_1}} (e.g., "Existing data export") | By {{DATE}} | {{CUSTOMER_ROLE}} | Project delays {{DURATION}} |
| {{DEPENDENCY_2}} (e.g., "Stakeholder sign-off on design") | By {{DATE}} | {{CUSTOMER_ROLE}} | Cannot proceed to build phase |
| {{DEPENDENCY_3}} (e.g., "Test system access for integration testing") | By {{DATE}} | {{CUSTOMER_ROLE}} | Cannot validate integrations |

**From Third Parties:**

| Dependency | Timing | Owner | Impact if Unavailable |
|---|---|---|---|
| {{VENDOR_SERVICE}} availability | Throughout | {{VENDOR_NAME}} | Rollback to {{CONTINGENCY}} |
| {{INTEGRATION_AVAILABILITY}} API uptime | Testing & deployment | {{VENDOR_NAME}} | 1-2 week delay |

**From Our Organization:**

We commit to:
- {{RESOURCE_1}} — {{PERSON_NAME}} available {{HOURS_PER_WEEK}} throughout project
- {{RESOURCE_2}} — {{SPECIALIZED_EXPERTISE}} available on {{AVAILABILITY_SCHEDULE}}
- {{RESOURCE_3}} — {{SUPPORT_AVAILABILITY}} during go-live week

#### Exclusions

The following items are {{EXPLICITLY_NOT_INCLUDED}} in this proposal's scope:

- {{EXCLUSION_1}} — {{EXPLANATION_OF_WHY_NOT_INCLUDED}}
- {{EXCLUSION_2}} — {{EXPLANATION}}
- {{EXCLUSION_3}} — {{EXPLANATION}}

These may be addressed in a separate engagement if prioritized post-launch.

#### Gating Assumptions

The following assumptions, if violated, would require timeline/budget revision:

| Gate | Assumption | Mitigation | Alternative Timeline |
|---|---|---|---|
| **Before Phase 1 Starts** | Current systems not as documented | Reassess in Phase 1; renegotiate timeline | {{WEEKS}} additional weeks |
| **Before Phase 2 Starts** | Data not in exportable format | Develop custom export tools; delays Phase 2 | {{WEEKS}} additional weeks |
| **Before Phase 3 Starts** | Stakeholder availability inadequate | Rescope work; extend timeline | {{WEEKS}} additional weeks |

If any gating assumption fails, we will {{PROCESS}} (e.g., reconvene steering committee, reassess scope, provide revised timeline estimate).

#### Known Constraints

We're aware of the following constraints and have factored them into the plan:

| Constraint | Approach | Impact |
|---|---|---|
| {{CONSTRAINT_1}} (e.g., "No weekend maintenance windows available") | {{APPROACH}} (e.g., "All changes during business hours; staged rollout") | {{IMPACT}} (e.g., "Longer stabilization period") |
| {{CONSTRAINT_2}} (e.g., "Key stakeholder available only 10 hours/week") | {{APPROACH}} (e.g., "Async decision-making; written approvals") | {{IMPACT}} (e.g., "Slightly longer design phase") |

#### Change Management Process

If assumptions prove incorrect, here's how we'll address it:

1. **Notify immediately** — Within 24 hours of discovery, notify steering committee
2. **Quantify impact** — Provide revised timeline/budget estimate
3. **Options analysis** — Present options: additional time, additional budget, reduced scope
4. **Steering approval** — Get written approval of revised plan
5. **Proceed with revised plan** — Update project schedule and communicate to team

---

## Sections Explained

### About Your Organization
**Purpose:** State what you're assuming about THEIR readiness/capability

**Customization guidance:**
- These are areas where they could cause delays or cost overruns
- Be diplomatic but clear ("We assume data is documented" vs. "Your system is a mess")
- For each, estimate the impact if the assumption proves wrong

**Examples:**
- "Current system provides X data points; we assume they're accurate"
- "Documentation exists for current processes; we'll validate in Phase 1"
- "{{STAKEHOLDER_NAME}} will be available 50% of the time for decisions"
- "Current network infrastructure can handle the throughput requirements"

### About External Environment
**Purpose:** State what you're assuming about things outside both of your control

**Customization guidance:**
- Acknowledge you can't control everything
- Show you've thought about contingencies

**Examples:**
- "Third-party API remains stable and available (99.9% uptime)"
- "Regulatory environment doesn't change significantly during engagement"
- "Vendor roadmap includes features we're planning to use (confirm: {{VENDOR}})"

### About Our Engagement
**Purpose:** State what you're assuming about the engagement itself

**Customization guidance:**
- Show that you're committing to scope and timeline
- Also show that the RFP/requirements are final

**Examples:**
- "RFP scope is final; incremental requests will go through change management"
- "We can use [[database product]] current version; major version upgrade would be separate engagement"

### Dependencies
**Purpose:** List what the customer MUST DO for you to succeed

**Customization guidance:**
- Be specific about WHEN (by what date)
- Be specific about WHAT (provide data, approve designs, allocate people)
- Be specific about WHO (which role/person is responsible)
- Be honest about IMPACT (if they miss the deadline, what happens?)

**Examples:**
- "Customer must provide clean data export by {{DATE}} or Phase 2 testing slips {{WEEKS}}"
- "{{NUMBER}} customer team members must attend {{WORKSHOP}} on {{DATE}}"
- "Customer must sign off on design by {{DATE}} to maintain Go-Live on {{TARGET_DATE}}"

### Exclusions
**Purpose:** Clarify what's NOT included (prevents "but we thought you were doing that?" arguments)

**Customization guidance:**
- Be clear about what's out of scope
- Offer to include it (separately) if prioritized
- Link to potential follow-on engagements

**Examples:**
- "Advanced reporting/BI is not included in this phase (can be Phase 2 engagement)"
- "Training for all {{NUMBER}} users not included; we can provide instructor-led training for {{NUMBER}} core users"
- "Custom integrations with legacy systems X beyond basic API integration not included"

### Gating Assumptions
**Purpose:** Identify critical assumptions that, if wrong, force a renegotiation

**Customization guidance:**
- Limit to 3-5 truly critical assumptions
- These should be things you can't plan around; they must be verified before proceeding
- Show what happens if they fail

**Examples:**
- "Current system can export data in CSV format" — If not, we need custom export tools (add 2 weeks)
- "{{STAKEHOLDER_NAME}} availability 60% throughout project" — If less, decisions slow; add timeline
- "Network bandwidth adequate for {{THROUGHPUT}}" — If not, we need infrastructure upgrade first

### Known Constraints
**Purpose:** Show you understand their reality and have adapted

**Customization guidance:**
- This shows flexibility and customer understanding
- Show that you've factored constraints into the plan
- Don't complain; show you've adapted

**Examples:**
- "No off-hours maintenance windows available → All testing during business hours, staged rollout"
- "Budget constraints prevent buying new hardware → We'll use cloud services to bridge capacity gap"
- "Key developer on leave {{DATES}} → We've adjusted Phase 2 timeline to accommodate"

### Change Management Process
**Purpose:** Show how you'll handle it if assumptions change

**Customization guidance:**
- Be clear about the process
- Show it's fair to both parties
- Include a steering committee review (shows customer is in control)

---

## Variations by Project Size

### Small Projects (< $100K, < 2 months)
Keep assumptions section brief (1 page)
Focus on: data availability, stakeholder availability, scope stability

### Medium Projects ($100K-$500K, 2-6 months)
More detailed assumptions (1-2 pages)
Add: third-party dependencies, technology constraints, resource constraints

### Large Projects (> $500K, > 6 months)
Detailed section with gating assumptions (2+ pages)
Add: regulatory dependencies, vendor roadmap, organizational change assumptions

---

## Examples from Real Proposals

### Example 1: Cloud Migration (Large Project)
```
ASSUMPTIONS
- Current system can export 10GB of data in readable format (to be verified in Phase 1)
- 3 business stakeholders will be available for 10 hours/week throughout
- Network bandwidth supports 100 Mbps uploads during cutover
- Vendor {{SYSTEM_X}} APIs are stable during project timeline

DEPENDENCIES
- Customer provides data export by Phase 1 completion (if late, Phase 2 slips by {{WEEKS}} weeks)
- Customer signs off on architecture design by {{DATE}} (required for Phase 2 start)
- {{VENDOR_NAME}} API access provisioned by {{DATE}}

GATING ASSUMPTIONS
- If current system data quality is worse than assumed → We implement data cleansing (add {{WEEKS}})
- If network bandwidth insufficient → Customer must upgrade (add {{WEEKS}} for infrastructure work)

CHANGE MANAGEMENT
If any assumption proves wrong, we reconvene steering committee within 3 business days, 
revise estimate, and proceed with written approval.
```

### Example 2: Managed Service (Ongoing)
```
ASSUMPTIONS
- Current systems remain supported by vendors (no EOL announcements during engagement)
- Staffing levels remain stable (turnover expected is <20% annually)
- Compliance requirements remain stable (no new regulatory mandates)

DEPENDENCIES
- Customer provides access to all production systems on {{DATE}}
- Monthly steering meetings with customer leadership

EXCLUSIONS
- Hardware procurement/replacement (we manage; customer procures)
- Vendor license management (customer responsibility)

CONSTRAINTS
We're aware capacity is limited during {{PERIODS}}.
Our staffing plan includes buffer capacity; no accelerated delivery during high-demand periods.
```

---

## Common Mistakes to Avoid

| ❌ Mistake | ✅ Fix |
|---|---|
| No assumptions stated ("We've planned for everything") | Explicitly state 5-8 assumptions; shows realism |
| Assumptions are too detailed/academic | Simple, business language; focus on impact |
| Dependencies don't have dates | Every dependency should have a specific deadline |
| No impact if assumptions fail | Always explain "what happens if this goes wrong" |
| Assumes too much about customer ("They have perfect processes") | Realistic: "Data may need validation; we'll check in Phase 1" |
| Exclusions are vague | Be specific about what's out of scope and why |
| No gating assumptions for large projects | For projects > 3 months, identify 3-5 must-verify items |

---

## Customization Checklist

Before finalizing your assumptions section:

- [ ] 5-8 realistic assumptions about their organization
- [ ] 2-3 assumptions about external dependencies
- [ ] 2-3 assumptions about the engagement itself
- [ ] Each assumption includes impact estimate (time/cost if wrong)
- [ ] Every dependency includes a specific deadline
- [ ] Every dependency includes an ownership (who provides it)
- [ ] Every dependency includes impact if late (timeline/cost)
- [ ] Exclusions are specific (not vague "out of scope")
- [ ] Exclusions offer alternatives (can be done separately if prioritized)
- [ ] For large projects: 3-5 gating assumptions identified
- [ ] Gating assumptions include alternative timelines if violated
- [ ] Known constraints are listed with mitigation approach
- [ ] Change management process is clear and fair
- [ ] Uses customer-friendly language (not too technical)
- [ ] Tone is collaborative, not defensive

---

## Related Content

- **Implementation Approach:** [See 04-implementation-approach.md]
- **RFP Analysis:** [See 02-analysis/rfp-analysis/]
- **Risk Management:** [See risk section in 04-implementation-approach.md]
- **Project Plan:** [See 04-delivery/project-management/]
