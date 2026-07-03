# NX-DOC-0007 — Target Audiences & Personas

| Field | Value |
|-------|-------|
| **Document ID** | NX-DOC-0007 |
| **Title** | Target Audiences & Personas |
| **Phase** | 1 — Master Blueprint |
| **Owner** | Product |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-06-30 |
| **Related** | NX-DOC-0008 (Competitive Landscape), NX-DOC-0010 (Goals & Metrics), NX-DOC-0012 (Business Strategy) |

---

## 1. Purpose

This document defines **who NEXUS is for**. Every product decision must answer: "Does this serve one of these audiences?" If not, the decision is rejected.

## 2. Audience segmentation philosophy

We do not segment by industry, geography, or company size in the first pass. We segment by **relationship with AI execution**: how much autonomy a user is comfortable delegating, and how much orchestration work they want to do themselves.

The result is six primary personas plus three emerging personas, listed below in priority order for v1.

## 3. Primary personas (v1)

### Persona 1 — "Maya the Solo Operator" ⭐ priority
- **Demographics:** 28–45, runs a one-person business (creator, freelancer, indie founder, e-commerce).
- **Relationship with AI:** Trusts AI for execution, reviews the work, owns the outcome.
- **Today:** Switches between 8–15 SaaS tools daily.
- **Pain:** Context switching kills productivity. AI tools are too generic for their niche.
- **Jobs to be done:**
  - "Run my business without hiring."
  - "Automate the boring parts."
  - "Produce content, research, outreach."
- **Workspace shape:** Business, Content, Research, Finance.
- **Willingness to pay:** $30–100/month.

### Persona 2 — "Devin the Developer"
- **Demographics:** 24–40, professional software engineer or solo developer.
- **Relationship with AI:** Heavy power user; builds on top of AI tools; demands extensibility.
- **Today:** Uses VS Code/Cursor, ChatGPT, GitHub, custom scripts.
- **Pain:** AI tools are siloed. No shared memory across tools. No way to compose automations that touch the web.
- **Jobs to be done:**
  - "Build software with a team of AI agents."
  - "Automate web interactions in my dev workflow."
  - "Replace Zapier + n8n + custom scripts with one platform."
- **Workspace shape:** Code, DevOps, Research, Side Projects.
- **Willingness to pay:** $20–80/month; will pay for marketplace agents.

### Persona 3 — "Sara the Researcher"
- **Demographics:** 30–55, academic, journalist, analyst, competitive intelligence professional.
- **Relationship with AI:** Uses AI to accelerate but verifies every output.
- **Today:** Browsers + bookmarks + Zotero + spreadsheets + long reports.
- **Pain:** Research is scattered. AI summaries are unreliable. Re-doing work because context was lost.
- **Jobs to be done:**
  - "Investigate a topic across hundreds of sources."
  - "Maintain a living dossier on a person, company, or field."
  - "Produce a report I can defend in front of an editor."
- **Workspace shape:** Investigation, Source Library, Drafts.
- **Willingness to pay:** $30–100/month; team plans at $200–500/month.

### Persona 4 — "Marcus the Operator"
- **Demographics:** 35–55, runs operations at a small-to-mid business (marketing ops, RevOps, e-commerce ops).
- **Relationship with AI:** Pragmatic. Will automate anything that saves headcount.
- **Today:** Live in spreadsheets, Zapier, Notion, HubSpot, Slack.
- **Pain:** Tools don't talk. Workflows break. No audit trail for "what did the AI actually do?"
- **Jobs to be done:**
  - "Monitor competitor prices hourly."
  - "Generate daily reports."
  - "Run outreach campaigns without paying for 5 tools."
- **Workspace shape:** Operations, Reporting, Outreach.
- **Willingness to pay:** $50–300/month per seat; team plans at $1,000+/month.

### Persona 5 — "Riya the Power User"
- **Demographics:** 22–40, productivity enthusiast, "life hacker," uses Alfred/Notion/Arc/Reflect.
- **Relationship with AI:** Curious, wants control, willing to tinker.
- **Today:** Builds personal systems with Notion databases, Obsidian vaults, custom dashboards.
- **Pain:** AI tools feel generic. Wants the product to learn them.
- **Jobs to be done:**
  - "Make this browser feel like mine."
  - "Automate my daily routine."
  - "Get recommendations tailored to me."
- **Workspace shape:** Personal, Reading, Learning, Hobby Projects.
- **Willingness to pay:** $15–30/month.

### Persona 6 — "Thea the Team Lead"
- **Demographics:** 30–50, manages a team of 3–20; small agency, design studio, research team.
- **Relationship with AI:** Wants to deploy AI across the team without losing control.
- **Today:** Mix of Asana, Slack, Notion, shared docs.
- **Pain:** Team members use AI inconsistently. No shared AI workflows. Compliance concerns.
- **Jobs to be done:**
  - "Standardize how my team uses AI."
  - "Share agents and workflows across the team."
  - "Audit what AI did, with attribution."
- **Workspace shape:** Team-shared Workspaces per project/client.
- **Willingness to pay:** $20–80/month per seat; $500–5,000/month team plans.

## 4. Emerging personas (v2+)

These audiences are tracked but not v1 priorities. They become primary in Horizon 2.

### Persona 7 — "Henry the Hobbyist Investor"
- Trades crypto/stocks part-time. Wants monitoring, alerts, research. Pain: lives in 6 apps.
- **Activation cost:** Low. **Retention risk:** High if markets are quiet.
- **v2 status:** Tracked; not actively designed for in v1.

### Persona 8 — "Aisha the Educator"
- Teacher or course creator. Wants to produce materials, automate grading feedback, monitor student questions.
- **Activation cost:** Medium (privacy considerations for student data).
- **v2 status:** Requires separate compliance review.

### Persona 9 — "Enterprise Buyer"
- 100+ person company. Wants SOC2, SSO, audit logs, on-prem options.
- **v2 status:** Will not be a focus until Horizon 2. Early conversations only.

## 5. Personas we are NOT designing for in v1

| Out of scope | Why |
|--------------|-----|
| Children under 13 | COPPA / GDPR-K compliance is heavy; not v1 |
| High-frequency traders | Latency requirements exceed browser architecture |
| Professional gamers | Wrong product category |
| Ad-supported users | Violates P4 |
| Users requiring air-gapped deployment | Architecture supports it; productization is v3+ |

## 6. Persona-to-feature traceability

| Persona | Anchor features in v1 |
|---------|----------------------|
| Maya (Solo Operator) | Business Workspace, AI Studio, Marketplace agents |
| Devin (Developer) | Plugin SDK, AI-native extensions, Cloud Browsers |
| Sara (Researcher) | Long-Term Memory, Knowledge Graph, source citations |
| Marcus (Operator) | Workflow Builder, scheduled tasks, audit log |
| Riya (Power User) | Custom Workspaces, themes, shortcuts, memory editor |
| Thea (Team Lead) | Team plans, shared Workspaces, permissioning |

## 7. Activation by persona

A user is "activated" when they have completed one meaningful end-to-end task with an AI agent. Targets:

| Persona | Target activation time | Activation task |
|---------|------------------------|-----------------|
| Maya | < 10 minutes | Generate a week's content calendar |
| Devin | < 15 minutes | Run an automation that hits an API and persists data |
| Sara | < 20 minutes | Produce a research dossier on a topic |
| Marcus | < 20 minutes | Schedule a recurring data extraction |
| Riya | < 5 minutes | Set up a personal Workspace |
| Thea | < 30 minutes | Invite a teammate and share a Workflow |

These targets drive product and onboarding design.

## 8. Retention model by persona

| Persona | Retention driver |
|---------|------------------|
| Maya | Recurring workflows + business automations |
| Devin | Plugin ecosystem + agent marketplace |
| Sara | Memory depth over time |
| Marcus | Reliability of scheduled automations |
| Riya | Personalization and theme system |
| Thea | Team-wide agent deployment |

## 9. Persona risk: who we might lose

| Persona | Risk of losing them | Mitigation |
|---------|---------------------|------------|
| Maya | To a more specialized tool (e.g., a CRM-only AI) | Cross-cutting integrations; default agents in marketplace |
| Devin | To VS Code + Cursor | SDK + plugin story; Cloud Browsers |
| Sara | To a research-specific tool | Citation quality, source verification, knowledge graph |
| Marcus | To Zapier + ChatGPT | Reliability + auditability + cross-tool depth |
| Riya | To Arc or a future competitor | Personalization, memory, themes |
| Thea | To Notion AI or Slack AI | Shared Workspaces + permissioning depth |

## 10. Reading list

- **Product Philosophy** — NX-DOC-0005
- **Competitive Landscape** — NX-DOC-0008
- **Long-Term Roadmap** — NX-DOC-0009
- **Goals & Metrics** — NX-DOC-0010

---

*End NX-DOC-0007.*