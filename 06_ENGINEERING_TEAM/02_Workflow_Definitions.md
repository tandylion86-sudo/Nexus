# NX-WF-9002 — Workflow Definitions

| Field | Value |
|-------|-------|
| **Document ID** | NX-WF-9002 |
| **Title** | Workflow Definitions |
| **Phase** | 5 — Autonomous Engineering Company |
| **Owner** | CEO AI |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-06-30 |
| **Depends on** | NX-WF-9001 (Org Overview), NX-AGENT-7014 (Multi-Agent Composition) |

---

## 1. Mission

This document defines the **standard operating procedures (SOPs)** for the engineering organization. Every repeatable task has a defined workflow. Workflows are versioned and updated.

## 2. The 12 standard workflows

```mermaid
graph LR
    W1[Idea → Ship] --> W2[Feature Dev]
    W2 --> W3[Architecture Review]
    W3 --> W4[Research]
    W4 --> W5[Design]
    W5 --> W6[Build]
    W6 --> W7[Test]
    W7 --> W8[Review]
    W8 --> W9[Release]
    W9 --> W10[Monitor]
    W10 --> W11[Iterate]
```

| # | Workflow | Purpose |
|---|----------|---------|
| 1 | Idea → Ship | From user idea to released feature |
| 2 | Bug Triage | From report to fix |
| 3 | Architecture Review | From proposal to decision |
| 4 | Security Review | From request to approval |
| 5 | Documentation Update | From change to published docs |
| 6 | Release | From green CI to public release |
| 7 | Incident Response | From alert to resolution |
| 8 | Customer Escalation | From complaint to resolution |
| 9 | Roadmap Update | From market signal to plan |
| 10 | Pricing Change | From hypothesis to published |
| 11 | Onboarding Update | From feedback to flow update |
| 12 | Quarterly Review | From data to decisions |

## 3. Workflow: Idea → Ship

**Trigger:** User feedback, market signal, internal proposal.

```mermaid
graph TD
    A[Idea] --> B{CEO triage}
    B -->|reject| R1[Reject with reason]
    B -->|accept| C[Research: validate]
    C --> D{Validates?}
    D -->|no| R1
    D -->|yes| E[Architect: spec architecture]
    E --> F[Security: threat model]
    F --> G[Product: PRD]
    G --> H[Design: UX]
    H --> I[Engineer: build]
    I --> J[QA: test]
    J --> K{Tests pass?}
    K -->|no| I
    K -->|yes| L[Release]
    L --> M[Monitor]
    M --> N{Working?}
    N -->|no| O[Iterate]
    O --> I
    N -->|yes| P[Done]
```

**SLA:** 4 weeks for typical feature; 12 weeks for major.

**Roles:** Research, Architect, Security, Product, Design, Engineer, QA.

**Quality gates:** PRD approved; Architecture reviewed; Security approved; Tests pass; Docs updated.

## 4. Workflow: Bug Triage

**Trigger:** Bug report.

```mermaid
graph TD
    A[Report] --> B[QA: reproduce]
    B --> C{Reproducible?}
    C -->|no| D[Request more info]
    D --> A
    C -->|yes| E[Severity assessment]
    E -->|P0| F[Immediate hotfix]
    E -->|P1| G[Current sprint]
    E -->|P2| H[Backlog]
    E -->|P3| I[Won't fix / defer]
    F --> J[Engineer: fix]
    G --> J
    J --> K[QA: verify]
    K --> L{Resolved?}
    L -->|no| J
    L -->|yes| M[Release]
```

**SLA:** P0 = 4 hours; P1 = 1 week; P2 = next sprint; P3 = backlog.

## 5. Workflow: Architecture Review

**Trigger:** Major architectural decision needed.

```mermaid
graph TD
    A[Proposal] --> B[CTO: draft ADR]
    B --> C[Architect: critique]
    C --> D{Reviewer approval?}
    D -->|no| B
    D -->|yes| E[Security: threat review]
    E --> F{Security concerns?}
    F -->|yes| B
    F -->|no| G[CEO: cost / scope check]
    G --> H{Approved?}
    H -->|no| B
    H -->|yes| I[Document ADR]
    I --> J[Communicate]
```

**Output:** Architecture Decision Record (ADR) in `12_DEVELOPER_GUIDE/ADRs/`.

## 6. Workflow: Security Review

**Trigger:** New feature with security implications; major dependency change.

```mermaid
graph TD
    A[Request] --> B[Security: threat model]
    B --> C[Risk classification]
    C -->|low| D[Approved]
    C -->|medium| E[Mitigations required]
    E --> F[Implementer: apply]
    F --> G[Verify]
    G --> D
    C -->|high| H[Founder: approve]
    H -->|approve| E
    H -->|reject| I[Block]
```

**Output:** Security review record + mitigations tracked.

## 7. Workflow: Documentation Update

**Trigger:** Any code change.

```mermaid
graph TD
    A[Code change] --> B{User-facing?}
    B -->|yes| C[Docs: update user docs]
    B -->|no| D{API change?}
    D -->|yes| E[Docs: update API ref]
    D -->|no| F[Skip]
    C --> G[Review]
    E --> G
    G --> H[Publish]
```

**Rule:** PR without docs does not merge.

## 8. Workflow: Release

**Trigger:** Sprint end with approved changes.

```mermaid
graph TD
    A[CI green] --> B[DevOps: build artifacts]
    B --> C[QA: smoke test]
    C --> D{Pass?}
    D -->|no| E[Block]
    D -->|yes| F[Staging deploy]
    F --> G[Internal dogfood]
    G --> H{Issues?}
    H -->|yes| I[Fix + restart]
    I --> G
    H -->|no| J[Production deploy]
    J --> K[Monitor]
    K --> L{Healthy?}
    L -->|no| M[Rollback]
    L -->|yes| N[Release notes]
    N --> O[Done]
```

## 9. Workflow: Incident Response

**Trigger:** P0 alert.

```mermaid
graph TD
    A[Alert] --> B[On-call: investigate]
    B --> C{Confirmed?}
    C -->|no| D[Close]
    C -->|yes| E[Severity]
    E --> F[Page team]
    F --> G[Mitigate]
    G --> H[Restore service]
    H --> I[Postmortem]
    I --> J[Action items]
```

**SLA:** Mitigation within 1 hour; full resolution within 24 hours; postmortem within 5 days.

## 10. Workflow: Customer Escalation

**Trigger:** Customer complaint.

```mermaid
graph TD
    A[Complaint] --> B[Support: categorize]
    B --> C[Product: investigate]
    C --> D[Action: fix / explain / refund]
    D --> E[Communicate]
    E --> F[Follow up]
    F --> G{Resolved?}
    G -->|no| C
    G -->|yes| H[Close + log]
```

## 11. Workflow: Roadmap Update

**Trigger:** Quarterly, or major market signal.

```mermaid
graph TD
    A[Market signal] --> B[Research: synthesize]
    B --> C[Product: re-evaluate]
    C --> D[CEO: propose update]
    D --> E[Founder: approve]
    E --> F[Update roadmap]
    F --> G[Communicate]
```

## 12. Workflow: Pricing Change

**Trigger:** Cost pressure, market shift, A/B test results.

```mermaid
graph TD
    A[Hypothesis] --> B[Finance: model]
    B --> C[Product: validate UX]
    C --> D[Marketing: communicate]
    D --> E[Founder: approve]
    E --> F[A/B test (optional)]
    F --> G[Roll out]
    G --> H[Monitor]
```

## 13. Workflow: Onboarding Update

**Trigger:** Activation metric regression or qualitative feedback.

```mermaid
graph TD
    A[Feedback / data] --> B[Product: analyze]
    B --> C[Design: propose]
    C --> D[Founder: approve]
    D --> E[Implement]
    E --> F[A/B test]
    F --> G[Roll out]
```

## 14. Workflow: Quarterly Review

**Trigger:** Every 90 days.

```mermaid
graph TD
    A[Quarter close] --> B[Gather metrics]
    B --> C[Each dept: report]
    C --> D[CEO: synthesize]
    D --> E[Founder: review]
    E --> F[Decisions]
    F --> G[Update plans]
```

## 15. Workflow inputs and outputs

Every workflow has:

- **Trigger.** What starts it.
- **Inputs.** Required context.
- **Steps.** Ordered activities.
- **Quality gates.** Pass / fail criteria.
- **Outputs.** Artifacts produced.
- **SLA.** Time and quality expectations.
- **Owners.** Which roles.

## 16. Acceptance criteria

- [ ] All 12 workflows documented.
- [ ] Each has trigger / inputs / steps / outputs / SLA.
- [ ] Quality gates identified.
- [ ] Owners identified.

## 17. Open questions

- Q: Should workflows themselves be agent-managed (suggested improvements)?
- Q: How do we handle cross-workflow dependencies?

## 18. Reading list

- **Org Overview** — NX-WF-9001
- **Quality Gates** — NX-WF-9003
- **Escalation Paths** — NX-WF-9004

---

*End NX-WF-9002.*