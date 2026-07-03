# NX-DOC-0001 — Cover & Document Control

| Field | Value |
|-------|-------|
| **Document ID** | NX-DOC-0001 |
| **Title** | Cover & Document Control |
| **Phase** | 1 — Master Blueprint |
| **Owner** | NEXUS Program Office |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-06-30 |
| **Last Updated** | 2026-07-03 (Phase 8 closeout) |
| **Classification** | Confidential — Internal |
| **Distribution** | Founders, executive AI, advisors |

---

## 1. Purpose

This document is the **administrative shell** for the NEXUS Blueprint repository. It does not describe the product. Its job is to keep every other document honest: who owns it, what version it is, what changed, and what to read next.

## 2. Repository identity

- **Working product name:** NEXUS
- **Project type:** AI-native browser and autonomous engineering platform
- **Specification type:** Living document — never "finished," always versioned
- **Primary artifacts:**
  - Markdown source (`.md`) — canonical
  - Mermaid diagrams — embedded inline or in `_assets/diagrams/`
  - JSON schemas — in `_assets/schemas/`
  - PDFs — generated on demand from Markdown via Pandoc

## 3. Document ID convention

All documents in this repository carry an identifier of the form:

```
NX-{TYPE}-{NUMBER}
```

| Type | Prefix | Range | Assigned in |
|------|--------|-------|-------------|
| Strategy / Executive | `NX-DOC-` | 0001–0099 | Phase 1 |
| Product Requirements | `NX-PRD-` | 0100–0999 | Phase 2 |
| Feature Specification | `NX-FEAT-` | 1000–4999 | Phase 2 |
| Design System | `NX-DS-` | 5000–5999 | Phase 3 |
| UI Screen | `NX-UI-` | 6000–6999 | Phase 3 |
| AI Agent | `NX-AGENT-` | 7000–7999 | Phase 4 |
| Architecture | `NX-ARCH-` | 0001–0999 | Phase 6+ |
| Engineering Manifest | `NX-EM-` | 9601–9699 | Phase 5 |
| API | `NX-API-` | 8000–8999 | Phase 7 |
| Workflow | `NX-WF-` | 9000–9499 | Phase 5 |
| Test / Acceptance | `NX-AT-` | 9500–9999 | Phase 5 |

**Note on `NX-ARCH-`:** introduced 2026-07-02 for Phase 6 (Browser Architecture). Doc IDs are grouped by phase: `0001` is the phase overview; `0101–0199` are leaf docs in the first phase that uses the range. Future phases may use `0201–0299`, `0301–0399`, etc.

When creating a new document, the next free number in the appropriate range MUST be assigned. The `_assets/DOCUMENT_REGISTRY.md` file tracks issued IDs.

## 4. Versioning

We use [Semantic Versioning](https://semver.org/) for documents:

- **Major (X.0.0):** Substantive change to meaning, scope, or intent. Requires re-approval.
- **Minor (0.X.0):** Additions, clarifications, new sections. Does not change prior conclusions.
- **Patch (0.0.X):** Typographical corrections, link fixes, Mermaid diagram syntax repairs.

Every document carries a version in its header table. Material changes are recorded in the change log below.

## 5. Change log

### Phase 1 — v0.1.0 — 2026-06-30

| ID | Document | Action | Summary |
|----|----------|--------|---------|
| NX-DOC-0001 | Cover & Document Control | Created | Initial scaffolding |
| NX-DOC-0002 | Vision | Created | 10-year vision statement |
| NX-DOC-0003 | Mission | Created | Mission and guiding question |
| NX-DOC-0004 | Core Principles | Created | 12 non-negotiable principles |
| NX-DOC-0005 | Product Philosophy | Created | 7 product beliefs |
| NX-DOC-0006 | AI-First Design Philosophy | Created | What AI-first means in practice |
| NX-DOC-0007 | Target Audiences & Personas | Created | 6 primary personas |
| NX-DOC-0008 | Competitive Landscape | Created | Market map and positioning |
| NX-DOC-0009 | Long-Term Roadmap | Created | 10-year horizon, 4 horizons |
| NX-DOC-0010 | Product Goals & North Star Metrics | Created | North Star + supporting metrics |
| NX-DOC-0011 | Technical Principles | Created | 14 engineering principles |
| NX-DOC-0012 | Business Strategy | Created | Revenue, distribution, moat |

### Phase 8 — v0.1.0 — 2026-07-03

| ID | Document | Action | Summary |
|----|----------|--------|---------|
| NX-ARCH-0004 | Marketplace Architecture Overview | Created | Frames marketplace + security |
| NX-ARCH-0601 | Agent Store & Discovery | Created | Catalog, search, install, update |
| NX-ARCH-0602 | Plugin SDK & API Contracts | Created | .nxpkg, manifest, signature, runtime |
| NX-ARCH-0603 | Billing, Metering & Subscriptions | Created | 5 meters, Stripe, tax, dunning |
| NX-ARCH-0604 | Ratings, Reviews & Trust | Created | Bayesian rating, badges, T&S, anti-abuse |
| NX-ARCH-0605 | Revenue Sharing & Payouts | Created | Commission, ledger, KYC, payouts |
| NX-ARCH-0701 | Threat Model & Attack Surface | Created | STRIDE, adversary model, asset model |
| NX-ARCH-0702 | AI Safety & Prompt-Injection Defense | Created | AI attack taxonomy, layered defense |
| NX-ARCH-0703 | Permissions & Capability Model | Created | Capabilities, grants, enforcement |
| NX-ARCH-0704 | Privacy, PII & Data Residency | Created | Classification, DSAR, residency, breach |
| NX-ARCH-0705 | Encryption (at Rest & in Transit) | Created | Algorithms, KMS/HSM, mTLS, post-quantum |
| NX-ARCH-0706 | Zero-Trust Architecture | Created | SPIFFE, mTLS, microseg, continuous verify |

## 6. Document registry

| ID | Title | Phase | Status | Version | Owner |
|----|-------|-------|--------|---------|-------|
| NX-DOC-0001 | Cover & Document Control | 1 | 🟢 | 0.1.0 | Program Office |
| NX-DOC-0002 | Vision | 1 | 🟢 | 0.1.0 | Founder |
| NX-DOC-0003 | Mission | 1 | 🟢 | 0.1.0 | Founder |
| NX-DOC-0004 | Core Principles | 1 | 🟢 | 0.1.0 | Founder |
| NX-DOC-0005 | Product Philosophy | 1 | 🟢 | 0.1.0 | Product |
| NX-DOC-0006 | AI-First Design Philosophy | 1 | 🟢 | 0.1.0 | Product + AI |
| NX-DOC-0007 | Target Audiences & Personas | 1 | 🟢 | 0.1.0 | Product |
| NX-DOC-0008 | Competitive Landscape | 1 | 🟢 | 0.1.0 | Strategy |
| NX-DOC-0009 | Long-Term Roadmap | 1 | 🟢 | 0.1.0 | Product + Engineering |
| NX-DOC-0010 | Product Goals & North Star Metrics | 1 | 🟢 | 0.1.0 | Product + Growth |
| NX-DOC-0011 | Technical Principles | 1 | 🟢 | 0.1.0 | Engineering |
| NX-DOC-0012 | Business Strategy | 1 | 🟢 | 0.1.0 | Founder + Business |

## 7. Approval & re-review schedule

| Phase | Documents | Review cadence |
|-------|-----------|----------------|
| 1 — Master Blueprint | NX-DOC-0001 to 0012 | Quarterly or on material event |
| 2 — PRD | NX-PRD-#### | Bi-weekly during build, then quarterly |
| 3 — UX Bible | NX-DS-####, NX-UI-#### | Per release |
| 4 — AI Brain | NX-AGENT-#### | On every agent schema change |
| 5 — Engineering Org | NX-WF-####, NX-AT-#### | Continuous |

## 8. How to use this repository

### For humans
1. Read `00_EXECUTIVE/` in order (NX-DOC-0002 → 0012).
2. Stop at NX-DOC-0011 (Technical Principles) before reading any PRD.
3. Use the `MASTER_INDEX.md` cross-reference graph to find related documents.

### For AI coding assistants
1. Always load `MASTER_INDEX.md` first.
2. Treat every `NX-` prefixed document as a binding specification.
3. Do not contradict Phase 1 documents when generating lower-phase documents.
4. When uncertain about scope, propose additions to this registry rather than untracked documents.

### For investors / reviewers
1. Start with `NX-DOC-0002` (Vision) and `NX-DOC-0012` (Business Strategy).
2. Then read `NX-DOC-0009` (Roadmap) and `NX-DOC-0010` (Metrics).
3. Phase 1 alone is sufficient for early evaluation; Phases 2+ represent depth, not weakness of Phase 1.

## 9. Glossary of terms

| Term | Definition |
|------|------------|
| **NEXUS** | The product — an AI-native browser. Working name. |
| **Workspace** | A goal-oriented collection of tabs, files, notes, and agent state. |
| **Cloud Browser** | A persistent, isolated browser container managed by NEXUS. |
| **Agent** | An autonomous AI worker with a defined role, tools, and permissions. |
| **Command** | A natural-language intent submitted to NEXUS. |
| **Memory** | NEXUS's persistent knowledge about the user, projects, and history. |
| **Plan** | A structured sequence of steps produced by the Planner agent. |
| **Tool** | A capability an agent can invoke (browser action, API call, code execution, etc.). |
| **Worktree** | An isolated filesystem + state scope for parallel work. |

## 10. Out of scope for this document

This document does NOT define:
- Product behavior (see NX-DOC-0005).
- Technical architecture (see NX-DOC-0011 and Phase 6).
- Pricing (see NX-DOC-0012 and `11_BUSINESS/Pricing.md`).
- Legal terms (see `_assets/legal/` once created).

---

*End NX-DOC-0001.*