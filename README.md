# NEXUS Blueprint

> The single source of truth for the NEXUS AI-native browser and autonomous engineering platform.

This repository is the architectural and product specification for NEXUS. It is **not** a codebase — it is the blueprints. A separate implementation repository will be created once Phase 1 and Phase 2 (PRD) reach a stable state.

## How to read this repository

1. Start at **`MASTER_INDEX.md`** — describes the canonical reading order.
2. Begin with **`00_EXECUTIVE/`** — Vision, Mission, Principles, Strategy.
3. Each document is self-contained but cross-references others using `NX-DOC-####` identifiers.
4. Diagrams use Mermaid (renders natively in GitHub, VS Code, and most Markdown viewers).
5. A complete progress log lives in **`_assets/PROGRESS.md`**.

## Repository structure

```
NEXUS-blueprint/
├── 00_EXECUTIVE/         Master Blueprint (Vision, Mission, Strategy)
├── 01_PRODUCT/           Complete Product Requirements (PRD)
├── 02_DESIGN_SYSTEM/     Design system, colors, typography, components
├── 03_UI_SCREENS/        Per-screen UI/UX specifications
├── 04_BROWSER_ENGINE/    Chromium integration and browser internals
├── 05_AI_PLATFORM/       Agent framework, memory, planning, model routing
├── 06_ENGINEERING_TEAM/  The AI engineering organization
├── 07_BACKEND/           APIs, database, queues, infrastructure
├── 08_SECURITY/          Threat model, encryption, permissions, AI safety
├── 09_MARKETPLACE/       Agent store, plugin SDK, billing
├── 10_DEPLOYMENT/        Docker, K8s, CI/CD, monitoring
├── 11_BUSINESS/          Pricing, financials, GTM, investors
├── 12_DEVELOPER_GUIDE/  Coding standards, API docs, SDK, contribution
├── 99_MASTER_PROMPTS/    Master prompts and workflow templates
└── _assets/              Progress tracker, diagrams, schemas
```

## Naming conventions

- **Product name:** NEXUS (working title; candidate names tracked in `11_BUSINESS/Naming_Brief.md` once Phase 1 is complete).
- **Document IDs:** `NX-DOC-####` assigned sequentially. Cross-references use this format: `(see NX-DOC-0002)`.
- **Feature IDs:** `NX-FEAT-####` assigned in Phase 2.
- **Agent IDs:** `NX-AGENT-####` assigned in Phase 4.
- **API IDs:** `NX-API-####` assigned in Phase 7.
- **Diagram files:** `_<kebab-case-name>.md` inside `_assets/diagrams/`.

## Document status legend

- ⚪ Not started
- 🟡 In progress
- 🟢 Complete
- 🔵 In review
- 🔴 Blocked / needs decision

## Status

- **Phase 1** (Master Blueprint): 🟢 Complete (2026-06-30) — 12 docs.
- **Phase 2** (Complete PRD): 🟢 Complete (2026-06-30) — 7 core + 5 anchors + 152 leaf specs.
- **Phase 3** (UX Bible): 🟢 Complete (2026-06-30) — 12 design system docs + 12 screen specs.
- **Phase 4** (AI Brain): 🟢 Complete (2026-06-30) — 18 agent specs (contract + 6 core roles + 11 supporting).
- **Phase 5** (Engineering Org): 🟢 Complete (2026-06-30) — 5 docs (org overview, workflows, gates, escalation, AT suite).
- **Phase 6** (Browser Architecture): 🟢 Complete (2026-07-02) — 9 docs / ~10,145 words.
- **Phase 7** (AI Infrastructure): 🟢 Complete (2026-07-03) — 8 docs / ~12,603 words.
- **Phase 8** (Marketplace): 🟢 Complete (2026-07-03) — 12 docs / ~27,309 words (5 marketplace + 6 security + 1 overview).
- **Phase 9** (Enterprise Platform): ⚪ Not started — `11_BUSINESS/`.
- **Phase 10** (Future Expansion): 🟢 Complete (2026-07-03) — 14 docs / ~22,912 words.

**Total written:** ~192,300 words across 335 Markdown files (~768 pages at 250 wpp).

---

© NEXUS Project. Confidential — do not distribute.