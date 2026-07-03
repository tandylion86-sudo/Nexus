# NX-PRD-0002 — Persona × Feature Traceability Matrix

| Field | Value |
|-------|-------|
| **Document ID** | NX-PRD-0002 |
| **Title** | Persona × Feature Traceability Matrix |
| **Phase** | 2 — Complete PRD |
| **Owner** | Product |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-06-30 |
| **Depends on** | NX-DOC-0007 (Audiences), NX-FEAT-0001 (Feature Inventory) |

---

## 1. Purpose

This document maps every primary persona from NX-DOC-0007 to every feature that **directly serves that persona**. It is the contract that ensures no persona is ignored and no feature ships without a clear user.

A feature that serves no persona is rejected. A persona that no feature serves is a product gap.

## 2. Personas (from NX-DOC-0007)

| Code | Persona | One-line description |
|------|---------|----------------------|
| **P-MAYA** | Maya the Solo Operator | Runs a one-person business |
| **P-DEVIN** | Devin the Developer | Professional software engineer |
| **P-SARA** | Sara the Researcher | Academic / journalist / analyst |
| **P-MARCUS** | Marcus the Operator | Operations at SMB |
| **P-RIYA** | Riya the Power User | Productivity enthusiast |
| **P-THEA** | Thea the Team Lead | Manages 3–20 person team |

## 3. Feature-to-persona primary matrix

Legend: ● = critical to persona, ◐ = nice-to-have for persona, ○ = available but not distinctive, · = not relevant.

| Feature Area / Anchor Feature | P-MAYA | P-DEVIN | P-SARA | P-MARCUS | P-RIYA | P-THEA |
|-------------------------------|:------:|:-------:|:------:|:--------:|:------:|:------:|
| **Browser Core** | | | | | | |
| Tab management | ◐ | ◐ | ◐ | ◐ | ● | ◐ |
| Address bar w/ intent mode | ● | ● | ● | ● | ● | ● |
| Bookmarks w/ AI tagging | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ |
| History search | ◐ | ◐ | ● | ◐ | ◐ | ◐ |
| Site permissions | ◐ | ● | ◐ | ◐ | ◐ | ● |
| Cookie controls | ◐ | ● | · | ◐ | ● | ● |
| Password manager | ● | ● | ● | ● | ● | ● |
| **Workspaces** | | | | | | |
| Workspace goal sentence | ● | ● | ● | ● | ● | ● |
| Workspace notes | ● | ● | ● | ● | ● | ● |
| Workspace files | ● | ● | ● | ● | ● | ● |
| Workspace memory | ● | ● | ● | ● | ● | ● |
| Workspace templates | ● | ◐ | ● | ● | ● | ● |
| Workspace search | ◐ | ◐ | ● | ● | ◐ | ● |
| Workspace sharing (team) | · | · | ◐ | ● | · | ● |
| **AI Command Bar** | | | | | | |
| Command bar invocation | ● | ● | ● | ● | ● | ● |
| Intent parser | ● | ● | ● | ● | ● | ● |
| Plan display | ● | ● | ● | ● | ● | ● |
| Slash commands | ● | ● | ● | ● | ● | ● |
| Streaming acknowledgment | ● | ● | ● | ● | ● | ● |
| **AI Chat** | | | | | | |
| Conversational panel | ● | ● | ● | ● | ● | ● |
| Message references / citations | ◐ | ◐ | ● | ◐ | ◐ | ◐ |
| Regenerate response | ● | ● | ● | ● | ● | ● |
| Inline artifacts | ● | ● | ● | ● | ● | ● |
| Branch conversation | · | ● | ◐ | · | ◐ | ◐ |
| **Agent Orchestrator** | | | | | | |
| Planner agent | ● | ● | ● | ● | ● | ● |
| Plan execution | ● | ● | ● | ● | ● | ● |
| Tool dispatcher | ● | ● | ● | ● | ● | ● |
| Sub-agent spawning | ● | ● | ● | ● | ● | ● |
| Approval gates | ● | ● | ● | ● | ● | ● |
| Parallel execution | ● | ● | ● | ● | ● | ● |
| Structured disagreement | · | ● | ● | ◐ | · | ● |
| **Agent Marketplace** | | | | | | |
| Marketplace browse | ● | ● | ● | ● | ● | ● |
| One-click install | ● | ● | ● | ● | ● | ● |
| Third-party publishing | · | ● | · | ◐ | ◐ | ◐ |
| Paid agents | ◐ | ● | · | ● | ◐ | ◐ |
| Verified agents | ● | ● | ● | ● | ● | ● |
| **Cloud Browser Fleet** | | | | | | |
| Create Cloud Browser | ● | ● | ● | ● | ◐ | ● |
| Session resume | ● | ● | ● | ● | ◐ | ● |
| Per-browser cookies | ● | ● | ● | ● | ◐ | ● |
| Per-browser proxy | ◐ | ● | ◐ | ● | · | ◐ |
| Scheduled tasks | ● | ● | ◐ | ● | ● | ● |
| Live remote view | ◐ | ● | ◐ | ● | · | ◐ |
| **Memory Engine** | | | | | | |
| Preference memory | ● | ● | ● | ● | ● | ● |
| Project state memory | ● | ● | ● | ● | ● | ● |
| Conversation memory | ● | ● | ● | ● | ● | ● |
| Memory inspector | ● | ● | ● | ● | ● | ● |
| Memory export | ● | ● | ● | ● | ● | ● |
| RAG over documents | ◐ | ● | ● | ● | ◐ | ◐ |
| Knowledge graph | · | ◐ | ● | ◐ | · | ◐ |
| **Visual Workflow Builder** | | | | | | |
| Block editor | ● | ● | ◐ | ● | ● | ● |
| Schedule trigger | ● | ● | ◐ | ● | ● | ● |
| Event trigger | ◐ | ● | · | ● | ◐ | ● |
| Debug mode | · | ● | · | ● | ◐ | ◐ |
| **Plugin SDK** | | | | | | |
| Plugin manifest | · | ● | · | ◐ | ◐ | ◐ |
| Plugin runtime | · | ● | · | ◐ | ◐ | ◐ |
| Plugin CLI | · | ● | · | ◐ | · | ◐ |
| **Sync & Profiles** | | | | | | |
| Profile separation | ● | ● | ◐ | ● | ● | ● |
| Cloud sync | ● | ● | ● | ● | ● | ● |
| Local-only mode | ● | ● | ● | ◐ | ● | · |
| Export account data | ● | ● | ● | ● | ● | ● |
| **Permissions & Privacy** | | | | | | |
| Permission prompts | ● | ● | ● | ● | ● | ● |
| Audit log | ● | ● | ● | ● | ● | ● |
| Encrypted credential vault | ● | ● | ● | ● | ● | ● |
| Privacy mode | ● | ◐ | ● | ● | ● | ◐ |
| **Notifications & Activity** | | | | | | |
| Notification center | ● | ● | ● | ● | ● | ● |
| Activity Log | ● | ● | ● | ● | ● | ● |
| Activity search | ◐ | ◐ | ● | ● | ◐ | ● |
| **Integrations** | | | | | | |
| Email integration | ● | ◐ | ◐ | ● | ◐ | ● |
| Calendar integration | ● | · | ◐ | ● | ◐ | ● |
| File storage | ● | ● | ● | ● | ● | ● |
| GitHub | · | ● | · | ◐ | ◐ | ◐ |
| Slack / team chat | ◐ | · | · | ◐ | · | ● |
| **Theming & Accessibility** | | | | | | |
| Light/dark theme | ● | ● | ● | ● | ● | ● |
| Custom theme | · | · | · | · | ● | · |
| WCAG 2.2 AA | ● | ● | ● | ● | ● | ● |
| Keyboard nav | ● | ● | ● | ● | ● | ● |
| **Local AI** | | | | | | |
| Local model execution | ● | ● | ● | ● | ● | ● |
| Local-only mode | ● | ● | ● | ◐ | ● | · |
| GPU acceleration | ◐ | ● | · | ◐ | ● | · |
| **Subscription & Billing** | | | | | | |
| Tier selection | ● | ● | ● | ● | ● | ● |
| Plan management | ● | ● | ● | ● | ● | ● |
| Cloud Browser overage | ● | ● | ● | ● | ◐ | ● |
| **Onboarding** | | | | | | |
| First-run welcome | ● | ● | ● | ● | ● | ● |
| Intent onboarding | ● | ● | ● | ● | ● | ● |
| Sample workspaces | ● | ● | ● | ● | ● | ● |

## 4. Persona-to-feature priority ranking

For each persona, the **top 5 distinguishing features** are:

### P-MAYA (Solo Operator)
1. AI Command Bar (NX-FEAT-1201-1209) — primary interface
2. Cloud Browser Fleet (NX-FEAT-1601-1614) — parallel execution
3. Agent Marketplace (NX-FEAT-1501-1514) — out-of-the-box capability
4. Workspace templates (NX-FEAT-1107) — quick setup
5. Visual Workflow Builder (NX-FEAT-1801-1812) — automation without engineering

### P-DEVIN (Developer)
1. Agent Orchestrator (NX-FEAT-1401-1414) — agent-as-coworker
2. Plugin SDK (NX-FEAT-1901-1909) — extensibility
3. Cloud Browser Fleet with proxy (NX-FEAT-1605) — testing
4. GitHub integration (NX-FEAT-2304) — workflow continuity
5. Code execution in workflows (NX-FEAT-1808) — scripting

### P-SARA (Researcher)
1. Memory Engine with RAG (NX-FEAT-1701-1714) — long-running investigations
2. Citation references in chat (NX-FEAT-1303) — source provenance
3. Workspace memory (NX-FEAT-1106) — per-investigation context
4. Activity Log (NX-FEAT-2205) — reproducibility
5. Knowledge graph (NX-FEAT-1713) — entity tracking

### P-MARCUS (Operator)
1. Visual Workflow Builder (NX-FEAT-1801-1812) — automation
2. Scheduled tasks (NX-FEAT-1608) — recurring operations
3. Integrations (NX-FEAT-2301-2311) — existing stack
4. Audit log (NX-FEAT-2204) — accountability
5. Per-browser proxies (NX-FEAT-1605) — multi-account

### P-RIYA (Power User)
1. Custom themes (NX-FEAT-2402) — personalization
2. Memory inspector (NX-FEAT-1705) — fine control
3. Local-only mode (NX-FEAT-2603) — privacy
4. Slash commands (NX-FEAT-1205) — speed
5. Profile separation (NX-FEAT-2004) — multi-life organization

### P-THEA (Team Lead)
1. Workspace sharing (NX-FEAT-1110) — collaboration
2. Team billing (NX-FEAT-2709) — seat management
3. Audit log (NX-FEAT-2204) — oversight
4. SSO (NX-FEAT-2901, H2) — enterprise-grade
5. Marketplace verified agents (NX-FEAT-1512) — safe deployment

## 5. Activation features per persona

The "first task completed" path for each persona:

| Persona | First successful task enabled by |
|---------|----------------------------------|
| P-MAYA | Sample Workspace: "Generate a week's social content" |
| P-DEVIN | Sample Workflow: "Run GitHub issue triage" |
| P-SARA | Sample Workspace: "Research dossier on a company" |
| P-MARCUS | Sample Workflow: "Monitor competitor prices hourly" |
| P-RIYA | Sample Workspace: "Personal daily briefing" |
| P-THEA | Sample Team Workspace: "Shared research dossier" |

These activation paths are owned by NX-PRD-0004 (Onboarding).

## 6. Coverage gaps and risks

After mapping, we observe:

| Gap | Risk | Mitigation |
|-----|------|------------|
| P-DEVIN lacks first-class code execution in browser | Developer activation is harder | Phase 5 adds code-execution block; H2 code panel |
| P-SARA knowledge graph is P2 | Research activation may underperform | Re-prioritize to P1 if research is leading acquisition |
| P-MARCUS event triggers are P2 | Operations automation is limited | Re-prioritize if ops is target H2 segment |
| P-THEA SSO is H2 | Enterprise teams cannot adopt | Ship limited WorkOS-based SSO in H1 GA |
| P-RIYA theme marketplace is P3 | Power users may churn for lack of personalization | Re-prioritize to P2 if NPS dips |

## 7. Cross-check vs. design system

Every feature marked ● or ◐ for a persona MUST have:
- A UI surface in Phase 3 (UX Bible)
- An owner agent identified here
- A P0/P1/P2 priority assigned in NX-FEAT-0001

If any of these are missing, the matrix entry is incomplete and the feature spec is gated.

## 8. Reading list

- **Audiences** — NX-DOC-0007
- **Master PRD** — NX-PRD-0001
- **Feature Inventory** — NX-FEAT-0001
- **Onboarding** — NX-PRD-0004
- **Roadmap** — NX-PRD-0006

---

*End NX-PRD-0002.*