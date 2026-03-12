# Team Collaboration Guide

This document defines how multiple team members can work together on proposals without conflicts, and how decisions are made when perspectives differ.

## Collaboration Model

Proposal development is a **shared accountability** model where:

- **Pre-Sales Engineer** leads the overall proposal
- **Solution Architect** ensures technical credibility
- **Delivery PM** ensures delivery feasibility
- **Sales Lead** ensures strategic alignment and customer fit

Everyone can contribute, but clear ownership prevents duplication and conflicting guidance.

## Team Roles & Responsibilities

### Pre-Sales Engineer (Proposal Lead)

**Primary Owner:** Proposal assembly, customer-facing messaging, RFP mapping

**Responsibilities:**
- Leads proposal creation and owns final submission
- Ensures all RFP requirements are addressed
- Maintains traceability matrix (requirement-mapping.md)
- Coordinates reviews and manages feedback
- Makes final edits for consistency and flow
- Accountable for "do we answer the RFP?"

**Authority:**
- Can request changes from other reviewers "for customer readiness"
- Decides voice, tone, and messaging consistency
- If conflicts with Architect, escalates to Sales Lead

**Time Commitment:**
- Days 1-3: 60% effort (initial draft)
- Days 3-5: 80% effort (incorporating feedback, revisions)
- Days 5-6: 100% effort (final assembly, exports)

### Solution Architect

**Primary Owner:** Technical design, architecture section, solution credibility

**Responsibilities:**
- Proposes the technical solution approach
- Reviews architecture section for accuracy and feasibility
- Validates that proposed design matches RFP requirements
- Flags any architectural gaps or risks
- Suggests improvements to technical approach
- Signs off on technical credibility before submission

**Authority:**
- Can require changes to architecture section for technical accuracy
- Can escalate if they think solution is not feasible
- If presales wants to commit to something technically impossible, can veto (escalates to Sales Lead)

**Time Commitment:**
- Day 2-3: 20% effort (initial solution design)
- Day 4: 50% effort (architecture drafting)
- Day 5: 40% effort (review and sign-off)

### Delivery Project Manager

**Primary Owner:** Implementation approach, timeline feasibility, delivery risk

**Responsibilities:**
- Reviews implementation approach for realism
- Validates timeline assumptions
- Confirms resource availability for commitments made
- Escalates if timeline is not achievable
- Reviews risk mitigation for credibility
- Signs off on "we can deliver this"

**Authority:**
- Can require timeline changes if not feasible
- Can flag risks that were missed
- If delivery is impossible as proposed, can escalate (escalates to Sales Lead)

**Time Commitment:**
- Days 3-5: 40% effort (timeline and approach review)
- Day 5: 20% effort (final sign-off)

### Sales Lead

**Primary Owner:** Strategic alignment, competitive positioning, final approval to bid

**Responsibilities:**
- Ensures proposal answers "why us?" vs. competitors
- Assesses win probability and competitive positioning
- Makes final decision on whether to bid
- Resolves conflicts between other team members
- Accountable for "do we want to win this deal?"
- Ensures commercial terms are appropriate

**Authority:**
- Final authority to submit proposal (can override concerns with risk acknowledgement)
- Can request changes to emphasize competitive differentiation
- Resolves disputes between team members

**Time Commitment:**
- Day 3: 10% effort (bid decision)
- Days 5-6: 20% effort (final review and submission approval)

### Optional: Legal/Compliance

**If applicable:** Reviews terms & conditions, liability, regulatory compliance statements

**Changes:** Can require legal language changes, IP ownership clarity, compliance statement accuracy

**Time Commitment:**
- Day 5: 30% effort (one-time legal review)

---

## Decision-Making: When People Disagree

Proposals are collaborative, but conflicts happen. Here's how to resolve them:

### Type 1: Technical Disagreement

**Scenario:** Pre-sales wants to promote approach A. Architect thinks approach B is better.

**Resolution Process:**

1. **Pre-Sales + Architect discuss** (30 minutes)
   - Pre-Sales: "Why is B better? What's the trade-off?"
   - Architect: "A doesn't scale beyond 10K users; B costs 20% more but scales to 100K"

2. **Evaluate:**
   - Does RFP specify scale requirement?
   - What's customer's likely growth profile?
   - Which trade-off is better for win probability?

3. **Decide:**
   - If RFP specifies 100K users → Go with B
   - If RFP is silent and customer is likely 10K → Propose A (lower cost)
   - If unsure about customer preference → Propose A but position B as upgrade path

4. **If still disagreed:**
   - Escalate to **Delivery PM** (who has casting vote on feasibility)
   - If still stuck, **Sales Lead** makes final call

### Type 2: Messaging Disagreement

**Scenario:** Pre-Sales wants to emphasize "cost savings." Architect wants to emphasize "technical excellence."

**Resolution Process:**

1. **Review RFP** — What does customer prioritize? Cost or quality?

2. **Check CUSTOMER_PROFILE.md** — What are customer's stated priorities?

3. **Decide:**
   - If cost-conscious customer → Lead with savings, support with quality
   - If quality-focused → Lead with excellence, support with cost efficiency
   - If unsure → Lead with business outcome, let them choose path

4. **Typical solution:** Address both, but in order of customer priority

### Type 3: Timeline Disagreement

**Scenario:** Pre-Sales promised 4-month delivery. Delivery PM says needs 6 months.

**Resolution Process:**

1. **Delivery PM shows detail** — Activities, dependencies, what takes time

2. **Pre-Sales asks** — Which items are critical path? Can anything parallel?

3. **Architect suggests** — Any phased approach? Can we deliver value early?

4. **Options:**
   - Option A: Revise proposal timeline to 6 months (more realistic)
   - Option B: Deliver Phase 1 in 4 months, Phase 2 in months 5-6 (keeps their target)
   - Option C: 4-month timeline but phased or reduced scope

5. **Sales Lead decides** — What's the competitive position? Can we win with 6 months?

### Type 4: Strategic Disagreement

**Scenario:** Sales Lead wants to underbid to win. Delivery PM says margin is too low.

**Resolution Process:**

1. **Sales + Delivery discuss:**
   - Sales: "This customer is strategic; $50K margin on $500K engagement seems OK"
   - Delivery: "At 10% margin, we won't have budget for overruns; classic loss scenario"

2. **Options:**
   - Option A: Reduce scope to improve margin (tighter timeline, fewer features)
   - Option B: Increase price (but lower win probability)
   - Option C: Accept low margin with documented risk and commitment to operational discipline

3. **Sales Lead decides:** What's the strategic value of this customer? Is margin acceptable?

---

## Conflict Prevention

Most conflicts can be prevented by:

### 1. Clear Requirements Definition (Day 1)
Before anyone starts writing, everyone agrees:
- What are the top 3 customer priorities?
- What's our competitive position?
- What's our timeline constraint?
- What's the cost/margin target?

**Pre-Sales + Sales Lead + Architecture align on these before drafting starts.**

### 2. Weekly Standups (Days 2-5)
Brief 15-minute sync each day:
- "What did I draft/review today?"
- "Any blockers or concerns?"
- "Anyone see gaps I'm missing?"

This surfaces concerns early, before major rewrites needed.

### 3. Clear Ownership
- **Pre-Sales owns messaging**
- **Architect owns technical approach**
- **Delivery PM owns timeline**
- **Sales owns strategy**

No dual ownership → no conflicting guidance.

### 4. Assume Competence
If the Architect says "this won't scale," they're not wrong; find out why.
If Delivery PM says "timeline is tight," they're communicating risk; address it.

Assume everyone is trying to win; disagree on *how*, not *whether*.

---

## Asynchronous Collaboration

Not everyone can be in the same room. Async workflows:

### Async Drafting
- **Pre-Sales** posts initial draft to shared location
- **Architect** suggests architecture revisions (Markdown comments)
- **Delivery PM** comments on timeline feasibility
- **Pre-Sales** gathers feedback, revises, repost
- Each person responds within 24 hours

### Async Review
- Share draft with all reviewers
- Each person comments within 24 hours
- Pre-Sales consolidates into revision list
- Lead author revises
- Each reviewer confirms revised version is acceptable

### Tools
- Shared document (Google Docs, Markdown in Git)
- Comments with @ mentions ("@architect can you review section 4?")
- Slack threads for quick questions
- Synchronous meetings only for conflicts

---

## Escalation Process

If team can't agree:

**Level 1:** Try to resolve between the two people in conflict
- Direct conversation (30 min)
- Understand both perspectives
- Seek compromise

**Level 2:** Bring in **Third-Party Mediator** (Proposal Manager)
- Neutral perspective
- Helps frame options
- Facilitates decision

**Level 3:** Escalate to **Sales Lead** (final authority)
- Sales Lead makes the call
- Rationale is documented
- Everyone commits to decision and moves forward

---

## Contributing Without "Owning"

Not every team member needs to own something, but anyone can **contribute**:

- **You see a typo?** → Fix it or mention it
- **You see a gap?** → Point it out to owner
- **You have an idea?** → Share as suggestion, owner decides inclusion
- **You disagree?** → Raise concern with owner; respect their decision if legitimate

**Respect is key:** Owner makes final call; if you're not the owner, you've had your input.

---

## Communication Norms

### What to Communicate

Share asynchronously (Slack, email, docs):
- "I've drafted section [X]"
- "Architecture change needed: [rationale]"
- "Timeline concern: [specific issue]"
- "Customer question: how do we address [requirement]?"

### What NOT to Share

Don't take to team:
- Vague concerns ("This doesn't feel right")
- Complaints without solutions ("This is going to fail")
- Lack of engagement ("I don't have time to review this")

**Norm:** Come with specific, constructive input. Assume good faith from others.

### Response Times

- **Simple questions:** Answer within 4 hours
- **Review requests:** Complete within 24 hours
- **Major conflicts:** Schedule 30-minute call within 24 hours

---

## Remote Team Considerations

For fully remote teams:

**Synchronous meetings only when needed:**
- Kick-off alignment (Day 1 or 2)
- Conflict resolution (if can't resolve via Slack/comments)
- Final validation before submission

**Asynchronous preference:**
- Drafting via shared docs
- Feedback via comments with timestamps
- Async standups (Slack thread)

**Timezone considerations:**
- Use "morning" = 9am local, not absolute time
- Don't require attendance at 6am for someone else's morning
- Async updates so everyone can catch up regardless of timezone

---

## Post-Proposal Retrospective

After proposal submission (won or lost), team meets to discuss:

**What went well:**
- Which sections were most compelling?
- Whose arguments were most persuasive in conflicts?
- What collaboration approach worked?

**What to improve:**
- Any delayed decisions blocking progress?
- Unclear ownership causing duplication?
- Communication gaps?

**For next proposal:**
- Apply learnings to next RFP response

---

## Summary: Working Well Together

✅ **DO:**
- Own your area with confidence
- Contribute to others' work constructively
- Assume good faith from colleagues
- Escalate conflicts promptly
- Respect others' expertise

❌ **DON'T:**
- Make unilateral changes outside your ownership
- Assume worst about colleague's motives
- Let concerns fester unsaid
- Override colleague without escalation
- Disrespect expertise in others' domains

**Remember:** You're trying to win together. Conflicts about HOW to win are healthy. Conflicts about WHETHER to win are a problem.
