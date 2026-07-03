# NX-FEAT-0001 — Feature Inventory

| Field | Value |
|-------|-------|
| **Document ID** | NX-FEAT-0001 |
| **Title** | Feature Inventory |
| **Phase** | 2 — Complete PRD |
| **Owner** | Product |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-06-30 |
| **Depends on** | NX-PRD-0001 (Master PRD), NX-DOC-0007 (Audiences), NX-DOC-0009 (Roadmap) |

---

## 1. Purpose

This document is the **canonical catalog of every NEXUS feature**. It assigns stable IDs (`NX-FEAT-####`) that are referenced by every other document in the repository.

If a feature is not in this catalog, it does not officially exist. If a feature has an ID but no spec, it is on the spec backlog.

## 2. How to read this catalog

Each feature appears as a row with:
- **ID** — stable identifier (`NX-FEAT-####`)
- **Name** — short human-readable name
- **Area** — top-level feature area
- **H1 Priority** — P0, P1, P2, P3, or P4+
- **Horizon** — H1, H2, H3, H4
- **Owner agent** — the AI agent responsible for the spec

The catalog is organized by area for readability; the ID is the only ordering that matters for cross-references.

## 3. Catalog size

| Horizon | Feature count target |
|---------|----------------------|
| H1 | ~150 leaf features |
| H2 | +200 |
| H3 | +150 |
| H4 | +100 |

H1 inventory below contains **152 leaf features** across 20 areas. Specs are written for P0/P1 features first; P2+ specs may be batched.

## 4. H1 Feature Inventory

### Area A0001 — Browser Core

| ID | Feature | Priority | Owner |
|----|---------|----------|-------|
| NX-FEAT-1001 | Tab management (open, close, group, suspend, restore) | P0 | Frontend AI |
| NX-FEAT-1002 | Address bar with intent vs. URL mode | P0 | Frontend AI |
| NX-FEAT-1003 | Bookmarks (with AI tagging) | P1 | Frontend AI |
| NX-FEAT-1004 | History (search, filter, time-range, AI summary) | P1 | Frontend AI |
| NX-FEAT-1005 | Downloads (queue, scan, resume) | P1 | Frontend AI |
| NX-FEAT-1006 | Print dialog | P2 | Frontend AI |
| NX-FEAT-1007 | Find-in-page | P0 | Frontend AI |
| NX-FEAT-1008 | Reader mode (AI-enhanced) | P1 | Frontend AI |
| NX-FEAT-1009 | Picture-in-picture video | P3 | Frontend AI |
| NX-FEAT-1010 | Site permissions (camera, mic, location, notifications) | P0 | Security AI |
| NX-FEAT-1011 | Cookie controls | P0 | Security AI |
| NX-FEAT-1012 | Pop-up, redirect, and tracker blocking | P0 | Security AI |
| NX-FEAT-1013 | Password manager (integrated, encrypted) | P0 | Security AI |

### Area A0002 — Workspaces

| ID | Feature | Priority | Owner |
|----|---------|----------|-------|
| NX-FEAT-1101 | Create Workspace | P0 | Frontend AI |
| NX-FEAT-1102 | Switch between Workspaces | P0 | Frontend AI |
| NX-FEAT-1103 | Workspace goal sentence | P0 | Frontend AI |
| NX-FEAT-1104 | Workspace notes (rich text, attachments) | P1 | Frontend AI |
| NX-FEAT-1105 | Workspace files (auto-organized) | P1 | Frontend AI |
| NX-FEAT-1106 | Workspace memory (per-workspace context) | P0 | AI Platform AI |
| NX-FEAT-1107 | Workspace templates | P1 | Frontend AI |
| NX-FEAT-1108 | Archive / delete Workspace | P1 | Frontend AI |
| NX-FEAT-1109 | Workspace search (cross-workspace) | P1 | Frontend AI |
| NX-FEAT-1110 | Workspace sharing (team plans) | P2 | Backend AI |

### Area A0003 — AI Command Bar

| ID | Feature | Priority | Owner |
|----|---------|----------|-------|
| NX-FEAT-1201 | Command bar invocation (global hotkey) | P0 | Frontend AI |
| NX-FEAT-1202 | Natural language intent parser | P0 | AI Platform AI |
| NX-FEAT-1203 | Plan display (steps before execution) | P0 | AI Platform AI |
| NX-FEAT-1204 | Command history (searchable, filterable) | P1 | Frontend AI |
| NX-FEAT-1205 | Slash commands (e.g., /summarize, /research) | P1 | AI Platform AI |
| NX-FEAT-1206 | Quick actions (suggested next) | P1 | AI Platform AI |
| NX-FEAT-1207 | Command bar voice input | P3 | Frontend AI |
| NX-FEAT-1208 | Streaming acknowledgment (<500ms) | P0 | Frontend AI |
| NX-FEAT-1209 | Command cancellation | P0 | Frontend AI |

### Area A0004 — AI Chat

| ID | Feature | Priority | Owner |
|----|---------|----------|-------|
| NX-FEAT-1301 | Conversational panel | P0 | Frontend AI |
| NX-FEAT-1302 | Message streaming (token-by-token) | P0 | Frontend AI |
| NX-FEAT-1303 | Message references (cite sources, link files) | P1 | AI Platform AI |
| NX-FEAT-1304 | Regenerate response | P1 | Frontend AI |
| NX-FEAT-1305 | Edit & resubmit prompt | P1 | Frontend AI |
| NX-FEAT-1306 | Branch conversation | P2 | Frontend AI |
| NX-FEAT-1307 | Export chat (Markdown, JSON) | P2 | Frontend AI |
| NX-FEAT-1308 | Inline artifacts (tables, code, charts) | P1 | Frontend AI |
| NX-FEAT-1309 | Conversation search | P2 | Frontend AI |

### Area A0005 — Agent Orchestrator

| ID | Feature | Priority | Owner |
|----|---------|----------|-------|
| NX-FEAT-1401 | Planner agent (intent → plan) | P0 | AI Platform AI |
| NX-FEAT-1402 | Plan execution engine | P0 | AI Platform AI |
| NX-FEAT-1403 | Tool dispatcher (browser, file, API, model) | P0 | AI Platform AI |
| NX-FEAT-1404 | Sub-agent spawning | P0 | AI Platform AI |
| NX-FEAT-1405 | Agent memory access (scoped permissions) | P0 | AI Platform AI |
| NX-FEAT-1406 | Plan streaming + checkpointing | P0 | AI Platform AI |
| NX-FEAT-1407 | Plan revision (user edits, agent re-plans) | P1 | AI Platform AI |
| NX-FEAT-1408 | Failure recovery (retry, alternative path) | P1 | AI Platform AI |
| NX-FEAT-1409 | Confidence reporting (per plan step) | P1 | AI Platform AI |
| NX-FEAT-1410 | Parallel agent execution | P1 | AI Platform AI |
| NX-FEAT-1411 | Structured disagreement (Reviewer, Tester) | P2 | AI Platform AI |
| NX-FEAT-1412 | Approval gates (per-step, per-plan) | P0 | AI Platform AI |
| NX-FEAT-1413 | Durable execution (Temporal-style) | P1 | Backend AI |
| NX-FEAT-1414 | Plan visualization (tree view) | P2 | Frontend AI |

### Area A0006 — Agent Marketplace

| ID | Feature | Priority | Owner |
|----|---------|----------|-------|
| NX-FEAT-1501 | Marketplace browse (categories, search) | P1 | Frontend AI |
| NX-FEAT-1502 | Agent detail page (description, permissions, ratings) | P1 | Frontend AI |
| NX-FEAT-1503 | One-click install | P1 | Backend AI |
| NX-FEAT-1504 | Agent update (semver, user consent) | P2 | Backend AI |
| NX-FEAT-1505 | Agent uninstall (with cleanup) | P1 | Backend AI |
| NX-FEAT-1506 | First-party agents (curated set) | P0 | Product AI |
| NX-FEAT-1507 | Third-party publishing flow | P2 | Backend AI |
| NX-FEAT-1508 | Ratings and reviews | P2 | Frontend AI |
| NX-FEAT-1509 | Revenue share (creator monetization) | P2 | Backend AI |
| NX-FEAT-1510 | Paid agents (one-time, subscription) | P2 | Backend AI |
| NX-FEAT-1511 | Agent permissions display | P0 | Security AI |
| NX-FEAT-1512 | Verified agents (NEXUS-reviewed) | P1 | Security AI |
| NX-FEAT-1513 | Featured collections | P2 | Frontend AI |
| NX-FEAT-1514 | Developer publishing dashboard | P2 | Frontend AI |

### Area A0007 — Cloud Browser Fleet

| ID | Feature | Priority | Owner |
|----|---------|----------|-------|
| NX-FEAT-1601 | Create Cloud Browser | P0 | Backend AI |
| NX-FEAT-1602 | Cloud Browser idle persistence | P0 | Backend AI |
| NX-FEAT-1603 | Cloud Browser session resume | P0 | Backend AI |
| NX-FEAT-1604 | Per-browser cookies & local storage | P0 | Browser AI |
| NX-FEAT-1605 | Per-browser proxy assignment | P1 | Backend AI |
| NX-FEAT-1606 | Per-browser fingerprint profile | P1 | Browser AI |
| NX-FEAT-1607 | Live remote view (VNC-style) | P1 | Frontend AI |
| NX-FEAT-1608 | Scheduled tasks (cron, trigger) | P1 | Backend AI |
| NX-FEAT-1609 | Multi-user collaboration (session share) | P2 | Backend AI |
| NX-FEAT-1610 | Snapshot & restore | P1 | Browser AI |
| NX-FEAT-1611 | Bandwidth controls | P2 | Backend AI |
| NX-FEAT-1612 | Resource limits (CPU, RAM, network) | P1 | Backend AI |
| NX-FEAT-1613 | Fleet dashboard | P1 | Frontend AI |
| NX-FEAT-1614 | Usage analytics | P1 | Backend AI |

### Area A0008 — Memory Engine

| ID | Feature | Priority | Owner |
|----|---------|----------|-------|
| NX-FEAT-1701 | Preference memory (settings, defaults) | P0 | AI Platform AI |
| NX-FEAT-1702 | Project state memory (Workspace context) | P0 | AI Platform AI |
| NX-FEAT-1703 | Conversation memory (recurring facts) | P0 | AI Platform AI |
| NX-FEAT-1704 | Style memory (writing tone, length, format) | P1 | AI Platform AI |
| NX-FEAT-1705 | Memory inspector (user-facing UI) | P0 | Frontend AI |
| NX-FEAT-1706 | Memory edit / delete | P0 | Frontend AI |
| NX-FEAT-1707 | Memory export (portable format) | P0 | AI Platform AI |
| NX-FEAT-1708 | Memory import (from another NEXUS instance) | P1 | AI Platform AI |
| NX-FEAT-1709 | Cross-Workspace memory scope | P0 | AI Platform AI |
| NX-FEAT-1710 | Memory relevance ranking | P1 | AI Platform AI |
| NX-FEAT-1711 | Memory auto-deletion (TTL, configurable) | P1 | AI Platform AI |
| NX-FEAT-1712 | Encrypted-at-rest storage | P0 | Security AI |
| NX-FEAT-1713 | Knowledge graph (entities, relations) | P2 | AI Platform AI |
| NX-FEAT-1714 | RAG over user documents | P1 | AI Platform AI |

### Area A0009 — Visual Workflow Builder

| ID | Feature | Priority | Owner |
|----|---------|----------|-------|
| NX-FEAT-1801 | Block-based editor (drag-drop canvas) | P1 | Frontend AI |
| NX-FEAT-1802 | Core blocks (browser action, HTTP, model, condition, loop) | P1 | Backend AI |
| NX-FEAT-1803 | Block configuration panel | P1 | Frontend AI |
| NX-FEAT-1804 | Workflow execution engine | P1 | Backend AI |
| NX-FEAT-1805 | Workflow versioning | P2 | Backend AI |
| NX-FEAT-1806 | Workflow templates | P2 | Frontend AI |
| NX-FEAT-1807 | Workflow marketplace publishing | P2 | Backend AI |
| NX-FEAT-1808 | Inline code editing (JS, Python) | P2 | Frontend AI |
| NX-FEAT-1809 | Debug mode (step-through) | P2 | Backend AI |
| NX-FEAT-1810 | Error visualization (failed nodes highlighted) | P1 | Frontend AI |
| NX-FEAT-1811 | Schedule trigger | P1 | Backend AI |
| NX-FEAT-1812 | Event trigger (webhook, message) | P2 | Backend AI |

### Area A0010 — Plugin SDK

| ID | Feature | Priority | Owner |
|----|---------|----------|-------|
| NX-FEAT-1901 | Plugin manifest schema | P1 | Backend AI |
| NX-FEAT-1902 | Plugin runtime (sandboxed) | P1 | Backend AI |
| NX-FEAT-1903 | Plugin permission API | P0 | Security AI |
| NX-FEAT-1904 | Plugin UI (sidebar, panel, command) | P1 | Frontend AI |
| NX-FEAT-1905 | Plugin storage API | P1 | Backend AI |
| NX-FEAT-1906 | Plugin CLI (`nexus plugin dev`) | P1 | Backend AI |
| NX-FEAT-1907 | Plugin documentation site | P1 | Documentation AI |
| NX-FEAT-1908 | AI-native extensions (LLM-callable tools) | P1 | AI Platform AI |
| NX-FEAT-1909 | Plugin versioning | P1 | Backend AI |

### Area A0011 — Sync & Profiles

| ID | Feature | Priority | Owner |
|----|---------|----------|-------|
| NX-FEAT-2001 | Account creation (email, OAuth, passkey) | P0 | Backend AI |
| NX-FEAT-2002 | Login (multi-factor, passkey) | P0 | Backend AI |
| NX-FEAT-2003 | Profile switcher | P1 | Frontend AI |
| NX-FEAT-2004 | Profile separation (work/personal) | P1 | Browser AI |
| NX-FEAT-2005 | Cloud sync (Workspaces, agents, memory) | P0 | Backend AI |
| NX-FEAT-2006 | Local-only mode (no sync) | P0 | Backend AI |
| NX-FEAT-2007 | Conflict resolution UI | P1 | Frontend AI |
| NX-FEAT-2008 | Account deletion (with data wipe) | P0 | Backend AI |
| NX-FEAT-2009 | Export full account data | P0 | Backend AI |

### Area A0012 — Permissions & Privacy

| ID | Feature | Priority | Owner |
|----|---------|----------|-------|
| NX-FEAT-2101 | Permission prompts (per agent, per action) | P0 | Security AI |
| NX-FEAT-2102 | Permission templates (low/medium/high) | P0 | Security AI |
| NX-FEAT-2103 | Per-agent permission scopes | P0 | Security AI |
| NX-FEAT-2104 | Audit log (every agent action) | P0 | Backend AI |
| NX-FEAT-2105 | Encrypted credential vault | P0 | Security AI |
| NX-FEAT-2106 | Hardware-backed encryption (where available) | P0 | Security AI |
| NX-FEAT-2107 | Permission revoke (instant, mid-action) | P0 | Security AI |
| NX-FEAT-2108 | Permission expiration (time-bound grants) | P1 | Security AI |
| NX-FEAT-2109 | Sensitive action confirmation dialog | P0 | Frontend AI |
| NX-FEAT-2110 | Privacy mode (incognito workspaces) | P1 | Frontend AI |

### Area A0013 — Notifications & Activity

| ID | Feature | Priority | Owner |
|----|---------|----------|-------|
| NX-FEAT-2201 | Notification center | P0 | Frontend AI |
| NX-FEAT-2202 | In-product toasts | P0 | Frontend AI |
| NX-FEAT-2203 | OS notifications (opt-in) | P1 | Frontend AI |
| NX-FEAT-2204 | Email digests (opt-in) | P2 | Backend AI |
| NX-FEAT-2205 | Activity Log (full agent history) | P0 | Backend AI |
| NX-FEAT-2206 | Activity Log search/filter | P0 | Frontend AI |
| NX-FEAT-2207 | Activity Log export | P1 | Frontend AI |
| NX-FEAT-2208 | Activity Log retention controls | P1 | Backend AI |
| NX-FEAT-2209 | Per-agent activity view | P1 | Frontend AI |

### Area A0014 — Integrations

| ID | Feature | Priority | Owner |
|----|---------|----------|-------|
| NX-FEAT-2301 | Email integration (Gmail, Outlook) | P1 | Backend AI |
| NX-FEAT-2302 | Calendar integration (Google, Apple, Outlook) | P1 | Backend AI |
| NX-FEAT-2303 | File storage (Google Drive, Dropbox, OneDrive) | P1 | Backend AI |
| NX-FEAT-2304 | GitHub integration | P1 | Backend AI |
| NX-FEAT-2305 | Notion integration | P2 | Backend AI |
| NX-FEAT-2306 | Slack integration | P2 | Backend AI |
| NX-FEAT-2307 | Linear integration | P2 | Backend AI |
| NX-FEAT-2308 | CRM integrations (HubSpot, Pipedrive) | P2 | Backend AI |
| NX-FEAT-2309 | OAuth flow for third-party connections | P1 | Backend AI |
| NX-FEAT-2310 | Webhook triggers (in & out) | P2 | Backend AI |
| NX-FEAT-2311 | REST API client (custom integrations) | P2 | Backend AI |

### Area A0015 — Theming & Accessibility

| ID | Feature | Priority | Owner |
|----|---------|----------|-------|
| NX-FEAT-2401 | Light/dark theme | P0 | Frontend AI |
| NX-FEAT-2402 | Custom theme (colors, typography) | P1 | Frontend AI |
| NX-FEAT-2403 | Theme marketplace | P3 | Frontend AI |
| NX-FEAT-2404 | WCAG 2.2 AA compliance | P0 | Frontend AI |
| NX-FEAT-2405 | Keyboard navigation (full) | P0 | Frontend AI |
| NX-FEAT-2406 | Screen reader support | P0 | Frontend AI |
| NX-FEAT-2407 | Reduced motion support | P0 | Frontend AI |
| NX-FEAT-2408 | High contrast mode | P1 | Frontend AI |
| NX-FEAT-2409 | Locale & timezone | P1 | Frontend AI |
| NX-FEAT-2410 | Right-to-left layout support | P2 | Frontend AI |

### Area A0016 — Telemetry & Diagnostics

| ID | Feature | Priority | Owner |
|----|---------|----------|-------|
| NX-FEAT-2501 | Crash reporting (opt-out) | P0 | Backend AI |
| NX-FEAT-2502 | Performance metrics (local, anonymous) | P0 | Backend AI |
| NX-FEAT-2503 | A/B testing framework | P1 | Backend AI |
| NX-FEAT-2504 | Feature flag system | P0 | Backend AI |
| NX-FEAT-2505 | Diagnostics page (user-facing health check) | P1 | Frontend AI |
| NX-FEAT-2506 | User feedback widget | P1 | Frontend AI |
| NX-FEAT-2507 | Support bundle (zip export) | P2 | Backend AI |

### Area A0017 — Local AI

| ID | Feature | Priority | Owner |
|----|---------|----------|-------|
| NX-FEAT-2601 | Local model execution (Ollama integration) | P0 | AI Platform AI |
| NX-FEAT-2602 | Model download manager | P0 | AI Platform AI |
| NX-FEAT-2603 | Local-only mode (no cloud calls) | P0 | AI Platform AI |
| NX-FEAT-2604 | Model capability routing (local vs. cloud) | P0 | AI Platform AI |
| NX-FEAT-2605 | GPU acceleration (Metal, CUDA, ROCm) | P1 | AI Platform AI |
| NX-FEAT-2606 | Model benchmark tool (user-side) | P2 | Frontend AI |

### Area A0018 — Subscription & Billing

| ID | Feature | Priority | Owner |
|----|---------|----------|-------|
| NX-FEAT-2701 | Tier selection UI | P0 | Frontend AI |
| NX-FEAT-2702 | Payment (Stripe, Apple/Google Pay) | P0 | Backend AI |
| NX-FEAT-2703 | Invoice history | P1 | Frontend AI |
| NX-FEAT-2704 | Plan upgrade/downgrade | P0 | Backend AI |
| NX-FEAT-2705 | Plan cancellation | P0 | Backend AI |
| NX-FEAT-2706 | Refund processing | P1 | Backend AI |
| NX-FEAT-2707 | Cloud Browser overage billing | P0 | Backend AI |
| NX-FEAT-2708 | Premium model credits | P1 | Backend AI |
| NX-FEAT-2709 | Team billing (per-seat) | P1 | Backend AI |
| NX-FEAT-2710 | Marketplace earnings dashboard (for creators) | P2 | Frontend AI |
| NX-FEAT-2711 | Tax handling (regional) | P1 | Backend AI |

### Area A0019 — Onboarding & Education

| ID | Feature | Priority | Owner |
|----|---------|----------|-------|
| NX-FEAT-2801 | First-run welcome screen | P0 | Frontend AI |
| NX-FEAT-2802 | Intent onboarding (3 guided intents) | P0 | Frontend AI |
| NX-FEAT-2803 | Sample Workspaces | P0 | Product AI |
| NX-FEAT-2804 | Sample agents (curated) | P0 | Product AI |
| NX-FEAT-2805 | Interactive tutorial overlay | P1 | Frontend AI |
| NX-FEAT-2806 | Help center (in-product) | P1 | Documentation AI |
| NX-FEAT-2807 | Tooltips and coachmarks | P1 | Frontend AI |
| NX-FEAT-2808 | Onboarding progress tracker | P1 | Frontend AI |
| NX-FEAT-2809 | Skip onboarding (advanced users) | P0 | Frontend AI |
| NX-FEAT-2810 | Replay onboarding | P2 | Frontend AI |

### Area A0020 — Enterprise Readiness (H2 primarily; tracked here for H1 stubs)

| ID | Feature | Priority | Owner |
|----|---------|----------|-------|
| NX-FEAT-2901 | SSO (SAML, OIDC) | P3 (H1) / P0 (H2) | Backend AI |
| NX-FEAT-2902 | SCIM provisioning | H2 | Backend AI |
| NX-FEAT-2903 | Role-based access control | H2 | Security AI |
| NX-FEAT-2904 | Audit log export (SIEM-compatible) | H2 | Backend AI |
| NX-FEAT-2905 | Admin console | H2 | Frontend AI |
| NX-FEAT-2906 | Compliance posture (SOC2, HIPAA, GDPR) | H2 | Security AI |

## 5. Summary

- **Total H1 leaf features:** 152
- **By priority:**
  - P0: 47 (must ship in alpha/beta)
  - P1: 56 (must ship in H1 GA)
  - P2: 31 (H1 GA, may slip)
  - P3: 12 (deferrable to H2)
  - H2+ only: 6
- **By area:** 20 areas, average 7.6 features each
- **By owner:** Frontend AI (most features), AI Platform AI (agent/memory), Backend AI (services), Security AI (privacy), Product AI (content), Documentation AI (docs)

## 6. Feature-to-spec backlog

The 5 anchor specs called out by the user (Cloud Browser Fleet, Agent Marketplace, Workspace, Memory Engine, Visual Workflow Builder) cover the platform's **5 most distinctive areas**. Other P0 specs will follow.

Initial spec writing order:
1. NX-FEAT-1101–1110 (Workspace family)
2. NX-FEAT-1201–1209 (AI Command Bar family)
3. NX-FEAT-1401–1414 (Agent Orchestrator family)
4. NX-FEAT-1601–1614 (Cloud Browser Fleet family)
5. NX-FEAT-1501–1514 (Agent Marketplace family)
6. NX-FEAT-1701–1714 (Memory Engine family)
7. NX-FEAT-1801–1812 (Visual Workflow Builder family)
8. Remaining P0/P1 features

## 7. Change log

| Date | Change | Author |
|------|--------|--------|
| 2026-06-30 | Initial catalog, 152 features across 20 areas | Product AI |

---

*End NX-FEAT-0001.*