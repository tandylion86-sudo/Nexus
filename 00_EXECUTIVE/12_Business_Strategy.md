# NX-DOC-0012 — Business Strategy

| Field | Value |
|-------|-------|
| **Document ID** | NX-DOC-0012 |
| **Title** | Business Strategy |
| **Phase** | 1 — Master Blueprint |
| **Owner** | Founder + Business |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-06-30 |
| **Related** | NX-DOC-0002 (Vision), NX-DOC-0009 (Roadmap), NX-DOC-0010 (Goals & Metrics), NX-DOC-0008 (Competitive Landscape) |

---

## 1. Purpose

This document defines how NEXUS makes money, how it distributes, and how it survives long enough to deliver on the 10-year vision. It is a high-level strategy; detailed pricing lives in `11_BUSINESS/Pricing.md`, detailed GTM in `11_BUSINESS/GTM_Strategy.md`.

## 2. The business model in one sentence

> **NEXUS is a subscription-based AI-native browser with a two-sided marketplace, sold to individuals and teams who want intent-driven work.**

## 3. Revenue streams

NEXUS has **five revenue streams**, ordered by expected H1 contribution:

| Stream | Description | H1 contribution | H2 contribution |
|--------|-------------|------------------|------------------|
| 1. Subscriptions | Individual and team plans | 85% | 60% |
| 2. Marketplace commission | % of agent/template transactions | 5% | 15% |
| 3. Cloud Browser overages | Usage above plan limits | 5% | 10% |
| 4. Enterprise contracts | SSO, audit, compliance | 5% | 12% |
| 5. Premium model credits | Add-on usage of frontier cloud models | 0% | 3% |

The mix shifts toward marketplace and enterprise as the platform matures.

## 4. Pricing tiers (H1 target)

| Tier | Price | Includes |
|------|-------|----------|
| **Free** | $0 | 1 Cloud Browser, 50 hours/month, 5 marketplace agents, local-only mode available, standard models |
| **Pro** | $20/month | 5 Cloud Browsers, 300 hours/month, unlimited marketplace installs, premium models up to N credits/month, priority support |
| **Team** | $15/seat/month (5+ seats) | Everything in Pro + shared Workspaces, team templates, basic SSO, audit log |
| **Business** | $40/seat/month | Everything in Team + SSO/SAML, audit log export, role-based permissions, security review |
| **Enterprise** | Custom | Volume pricing, dedicated CSM, custom SLAs, on-prem options, compliance (SOC2, HIPAA, FedRAMP roadmap) |

Cloud Browser overages are billed at usage rates published in the dashboard. Model credits beyond plan limits are billed at provider cost + 20%.

Pricing is **subject to change** with 30-day notice; existing subscribers are grandfathered for 12 months.

## 5. Distribution strategy

NEXUS's distribution has three vectors, in priority order:

### Vector 1 — Prosumer word-of-mouth and creator economy
- Position NEXUS as the **creator's browser** — for YouTubers, indie founders, writers, developers.
- Sponsor 100 micro-creators in H1.
- Provide exclusive creator themes, agent packs, and revenue share.
- Goal: 30% of new signups from organic/creator channels by end of H1.

### Vector 2 — Developer ecosystem
- Open Plugin SDK + AI-native extensions.
- Build with Hacker News, dev.to, and Reddit presence.
- Publish engineering blog and architecture deep-dives.
- Goal: 10,000 developer-published agents/workflows by H2.

### Vector 3 — Enterprise sales motion (H2+)
- Hire 1 enterprise AE in H2; scale to 5 by H3.
- Target: design agencies, research firms, e-commerce ops, small SaaS companies.
- Goal: $5M enterprise ARR by end of H2.

## 6. Customer acquisition cost (CAC) and lifetime value (LTV)

| Metric | Target H1 | Target H2 |
|--------|-----------|-----------|
| Blended CAC | < $40 | < $60 |
| Pro LTV (24-month gross) | $480 | $600 |
| Team LTV (24-month gross, per seat) | $360 | $480 |
| LTV/CAC ratio | > 3.5x | > 4.0x |
| Payback period | < 12 months | < 9 months |

If CAC payback exceeds 12 months at any horizon boundary, the team re-evaluates distribution channels.

## 7. The moat

The moat is defined in detail in NX-DOC-0008. Summarized:

1. **Agent runtime** — production-grade, deeply integrated.
2. **Marketplace network effect** — more agents → more users → more creators → more agents.
3. **Cloud Browser Fleet** — infrastructure depth hard to replicate.
4. **Memory Engine** — personalized, hard to switch from.
5. **Local-only mode** — privacy moat for sensitive users.
6. **Plugin + SDK depth** — developer mindshare.

## 8. Funding strategy

NEXUS is capital-efficient by design: a small human team coordinates a large AI team. Funding milestones:

| Stage | Timing | Capital | Use |
|-------|--------|---------|-----|
| Bootstrap | 2026 | Personal funds | Phase 1, Phase 2, architecture prototype |
| Pre-seed | Q4 2026 | $1–2M | Phase 3 (UX Bible), first hires, alpha |
| Seed | Q2 2027 | $5–10M | Beta launch, marketplace v1, first Cloud Browser region |
| Series A | Q2 2028 | $20–40M | Public launch, multi-region Cloud, marketplace scale |
| Series B+ | H2 if needed | $50–100M | Mobile, voice, enterprise scale |

We will not raise more than is needed at each stage. The runway target is 18 months at each round.

## 9. Use of funds (illustrative)

For a $10M seed round:
- 50% — Engineering hires (humans)
- 20% — Cloud infrastructure (Cloud Browser Fleet, model inference, storage)
- 15% — Product, design, research
- 10% — Marketing, community, content
- 5% — Operations, legal, finance

For an enterprise-focused raise, the mix shifts toward sales and compliance.

## 10. Unit economics (Pro tier, illustrative)

| Line item | Per-user per-month |
|-----------|-------------------|
| Subscription revenue | $20.00 |
| Cost of cloud model inference | ($4.00) |
| Cost of Cloud Browser (amortized) | ($2.00) |
| Cost of storage | ($0.50) |
| Cost of support (amortized) | ($1.00) |
| **Gross margin** | **$12.50 (62.5%)** |

Target gross margin: 60%+ across all tiers. The Team and Business tiers have higher gross margins due to shared Cloud Browser pools.

## 11. Partnership strategy

We partner where NEXUS extends capability without distracting from core build:

| Partner type | Examples | Why |
|--------------|----------|-----|
| Model providers | OpenAI, Anthropic, Google, Mistral | Multi-model routing, preferential pricing |
| Cloud infrastructure | AWS, Cloudflare, Fly.io | Cost, geographic coverage |
| Identity | Auth0, WorkOS | Enterprise SSO, faster compliance |
| Productivity | Notion, Linear, GitHub, Slack | Deep integrations |
| Distribution | Product Hunt, Hacker News, dev communities | Reach |
| Hardware | Apple, Qualcomm (H3+) | Mobile, edge AI |

We do not partner where the partner's incentives conflict with our principles (P4, P9, P11).

## 12. Risks (commercial)

| Risk | Mitigation |
|------|------------|
| Frontier model company builds a browser | Compete on depth of agent platform and marketplace |
| Cloud cost outruns revenue | Aggressive metering; pricing aligned with cost; usage caps |
| Marketplace fails to launch | Seed with first-party agents; quality bar over quantity |
| Enterprise sales too slow | Stay prosumer-led; revisit enterprise in H2 |
| Open-source competitor undercuts us | Compete on integration, not features |
| Regulatory action on AI | Invest in safety, transparency, auditability from day one |
| Acquisition offer too early | Founder/board evaluates against 10-year plan |

## 13. The non-acquisition posture

NEXUS is built for a 10-year journey. We are not optimizing for an early acquisition. If an offer arrives, it is evaluated against the question: **"Does this accelerate or constrain the 10-year vision?"** A constrained exit is a failed exit.

We are not "for sale." We are building a company.

## 14. Reading list

- **Vision** — NX-DOC-0002
- **Audiences** — NX-DOC-0007
- **Competitive Landscape** — NX-DOC-0008
- **Roadmap** — NX-DOC-0009
- **Goals & Metrics** — NX-DOC-0010

---

*End NX-DOC-0012.*