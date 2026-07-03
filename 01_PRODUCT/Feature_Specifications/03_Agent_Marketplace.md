# NX-FEAT-1500 — Agent Marketplace (Anchor Spec)

| Field | Value |
|-------|-------|
| **Document ID** | NX-FEAT-1500 |
| **Title** | Agent Marketplace (Anchor Spec) |
| **Area** | NX-FEAT-A0006 — Agent Marketplace |
| **Owner** | Backend AI + Product AI |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-06-30 |
| **Priority (H1)** | P1 |
| **Horizon target** | H1 |
| **Estimated effort** | XL (decomposed into NX-FEAT-1501-1514) |

---

## 1. Purpose

The **Agent Marketplace** is a curated catalog of agents that users can install to extend NEXUS's capabilities. It enables a network effect: more agents → more users → more creators → more agents.

This document is the anchor spec; leaf features (NX-FEAT-1501 through 1514) inherit from it.

## 2. Why a marketplace

Without a marketplace:

- Every user builds their own agents from scratch.
- Domain expertise is locked inside individuals.
- NEXUS is just a tool, not an ecosystem.

With a marketplace:

- A marketer publishes "Email Drip Campaign" agent. Thousands of users install it.
- A researcher publishes "Literature Review" agent. Academics find it via search.
- A creator earns revenue; they make more agents.
- Network effects compound.

## 3. User stories

- As **Maya**, I want to find a "Real Estate Listing Monitor" agent that does what I need, instead of building one.
- As **Devin**, I want to publish my "JIRA Sync" agent and earn from it.
- As **Marcus**, I want to install a "Price Monitoring" agent from a verified creator.
- As **Thea**, I want a private marketplace for my team's internal agents.
- As any user, I want to know what an agent does before installing it.

## 4. Functional requirements

### FR-1: Marketplace browse
**Description:** Users browse the marketplace by category, search, featured collections, and trending.
**Acceptance:**
- [ ] 10+ categories (Business, Developer, Research, Security, etc.).
- [ ] Search supports name, description, tags.
- [ ] Trending algorithm updates daily.
- [ ] Featured collections surface manually curated sets.
- [ ] Sort by: relevance, rating, downloads, recency.

### FR-2: Agent detail page
**Description:** Each agent has a detail page showing description, screenshots, permissions, ratings, creator info, version history.
**Acceptance:**
- [ ] Description (Markdown), at least 200 words for quality agents.
- [ ] Permissions listed in plain language.
- [ ] Required integrations listed.
- [ ] Screenshots or video.
- [ ] Creator info (name, link, other agents).
- [ ] Version history with changelog.
- [ ] Compatibility (NEXUS version, OS).

### FR-3: One-click install
**Description:** Install an agent with one click.
**Acceptance:**
- [ ] Install completes in <10 seconds.
- [ ] Permission prompt is shown before install.
- [ ] Agent is immediately usable.
- [ ] Install can be undone (uninstall).

### FR-4: Agent update
**Description:** Installed agents update when the creator publishes a new version.
**Acceptance:**
- [ ] Auto-update by default; user can opt out per agent.
- [ ] Update notification in product.
- [ ] Major version updates require user consent (breaking changes).
- [ ] Update preserves user data scoped to agent.

### FR-5: Agent uninstall
**Description:** Users can uninstall an agent and clean up its data.
**Acceptance:**
- [ ] Uninstall completes in <5 seconds.
- [ ] User is warned about what will be deleted.
- [ ] Option to keep data (orphan it) or delete.
- [ ] Activity log records uninstall.

### FR-6: First-party agents (curated set)
**Description:** NEXUS publishes a curated set of high-quality first-party agents.
**Acceptance:**
- [ ] At least 20 first-party agents at GA.
- [ ] Each agent maintained to a quality bar.
- [ ] First-party agents are clearly labeled.
- [ ] First-party agents install without payment.

### FR-7: Third-party publishing flow
**Description:** Verified creators can publish agents.
**Acceptance:**
- [ ] Publishing requires creator account (KYC, Stripe Connect).
- [ ] Submission includes: manifest, description, screenshots, test plan.
- [ ] Review process takes ≤5 business days.
- [ ] Rejection includes reason and remediation guidance.
- [ ] Re-submission allowed.

### FR-8: Ratings and reviews
**Description:** Users rate and review agents.
**Acceptance:**
- [ ] 5-star rating + written review.
- [ ] Only verified installers can review.
- [ ] Reviews are public; creator can respond.
- [ ] Reviews cannot be deleted by creator (only by NEXUS).
- [ ] Spam filtering on reviews.

### FR-9: Revenue share (creator monetization)
**Description:** Paid agents share revenue between creator and NEXUS.
**Acceptance:**
- [ ] Pricing: one-time, subscription, or usage-based.
- [ ] Revenue share: 70/30 (≤$10), 75/25 ($10–$100), 80/100+ ($>100).
- [ ] Subscription: 75/25 monthly.
- [ ] Creator payouts monthly via Stripe Connect.
- [ ] Earnings dashboard for creators.

### FR-10: Paid agents
**Description:** Creators can publish paid agents with pricing models.
**Acceptance:**
- [ ] One-time purchase (lifetime use).
- [ ] Subscription (monthly/yearly).
- [ ] Usage-based (per task).
- [ ] Free trials (creator-configurable duration).
- [ ] Refunds per NX-FEAT-2706 policy.

### FR-11: Agent permissions display
**Description:** All agent permissions are clearly displayed before install.
**Acceptance:**
- [ ] Permissions shown in plain language (e.g., "Read your email" not "Inbox:read").
- [ ] Permissions categorized (data, money, identity, communication).
- [ ] User can see exactly which permissions a paid agent will use.
- [ ] Permissions cannot change without user re-consent.

### FR-12: Verified agents
**Description:** NEXUS verifies certain agents as safe, high-quality, and well-maintained.
**Acceptance:**
- [ ] Verification process: code review, security review, performance test.
- [ ] Verified badge shown on detail page.
- [ ] Verified agents may be featured.
- [ ] Verification can be revoked.

### FR-13: Featured collections
**Description:** NEXUS curates themed collections (e.g., "Agents for Researchers").
**Acceptance:**
- [ ] 5+ collections at launch.
- [ ] Each collection has a curator.
- [ ] Collections updated quarterly.
- [ ] Submit-an-agent-to-collection flow for creators.

### FR-14: Developer publishing dashboard
**Description:** Creators have a dashboard showing installs, ratings, earnings, reviews.
**Acceptance:**
- [ ] Real-time install count.
- [ ] Daily/weekly/monthly charts.
- [ ] Earnings statement with payout schedule.
- [ ] Review feed with reply capability.
- [ ] Version publishing UI.

## 5. Non-functional requirements

### NFR-1: Performance
- Marketplace load: <1 second.
- Install: <10 seconds.
- Search: <500ms for 10K agents.

### NFR-2: Reliability
- Marketplace uptime: 99.9%.
- Payout reliability: 99.99%.

### NFR-3: Security
- All agent code reviewed for vulnerabilities before publication.
- Sandboxed execution (NX-FEAT-1902).
- Permission enforcement at runtime.
- No network access without permission.

### NFR-4: Trust
- Verified agents badge backed by real review.
- Reviews cannot be purchased.
- Creator identity verified.

## 6. UI surfaces

| Surface | Reference |
|---------|-----------|
| Marketplace home | NX-UI-6201 |
| Agent detail | NX-UI-6202 |
| Install dialog | NX-UI-6203 |
| My agents | NX-UI-6204 |
| Publishing flow | NX-UI-6205 |
| Creator dashboard | NX-UI-6206 |
| Review submission | NX-UI-6207 |

## 7. Permissions

Marketplace requires:

- Browse: any user.
- Install: any user (with payment if paid).
- Publish: verified creator.
- Review: verified installer.
- Curator actions: NEXUS staff.

## 8. Telemetry

Events emitted (opt-in):

- `marketplace.browsed`
- `marketplace.searched`
- `agent.viewed`
- `agent.installed`
- `agent.uninstalled`
- `agent.updated`
- `agent.reviewed`
- `agent.purchased`

Activity Log captures install/uninstall events regardless.

## 9. Failure modes

| Failure | Behavior |
|---------|----------|
| Marketplace API down | Show offline message; allow installed agents to work |
| Install fails | Roll back cleanly; error message |
| Update breaks user workflow | Auto-rollback to last working version |
| Creator account compromised | Suspend account; freeze payouts |
| Payment processing fails | Refund flow; support escalation |

## 10. Dependencies

- Plugin SDK (NX-FEAT-A0010).
- Permission system (NX-FEAT-A0012).
- Activity Log (NX-FEAT-A0013).
- Billing (NX-FEAT-A0018).
- Stripe Connect for payouts.

## 11. Out of scope

- Agent-to-agent marketplace (H2).
- Agent auctions / bidding (H3+).
- Cross-marketplace federation (H3+).
- Agent subscriptions with usage tiers beyond what's listed.

## 12. Acceptance criteria summary

The Marketplace is done when:

- [ ] 100+ agents published (first + third party).
- [ ] ≥5 paid agents generating revenue.
- [ ] At least 1 creator earning >$1,000.
- [ ] Verified program produces 10+ verified agents.
- [ ] Install-to-use time ≤10 seconds.
- [ ] Sandbox prevents all known privilege-escalation patterns.
- [ ] Marketplace uptime ≥99.9%.

## 13. Sub-features (leaf specs)

| ID | Name |
|----|------|
| NX-FEAT-1501 | Marketplace browse |
| NX-FEAT-1502 | Agent detail page |
| NX-FEAT-1503 | One-click install |
| NX-FEAT-1504 | Agent update |
| NX-FEAT-1505 | Agent uninstall |
| NX-FEAT-1506 | First-party agents |
| NX-FEAT-1507 | Third-party publishing flow |
| NX-FEAT-1508 | Ratings and reviews |
| NX-FEAT-1509 | Revenue share |
| NX-FEAT-1510 | Paid agents |
| NX-FEAT-1511 | Agent permissions display |
| NX-FEAT-1512 | Verified agents |
| NX-FEAT-1513 | Featured collections |
| NX-FEAT-1514 | Developer publishing dashboard |

## 14. Open questions

- Q: Should agents be allowed to call other agents? (Composition)
- Q: How do we handle agents that depend on specific Cloud Browsers or models?
- Q: Should private marketplaces (for teams) be a feature, or just shared Workspaces with private agents?
- Q: How do we ensure fairness in the trending algorithm?

## 15. Change log

| Date | Change | Author |
|------|--------|--------|
| 2026-06-30 | Initial anchor spec | Backend AI |

---

*End NX-FEAT-1500.*