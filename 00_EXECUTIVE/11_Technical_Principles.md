# NX-DOC-0011 — Technical Principles

| Field | Value |
|-------|-------|
| **Document ID** | NX-DOC-0011 |
| **Title** | Technical Principles |
| **Phase** | 1 — Master Blueprint |
| **Owner** | Engineering |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-06-30 |
| **Related** | NX-DOC-0004 (Core Principles), NX-DOC-0006 (AI-First Design Philosophy), Phase 6 (Browser Architecture), Phase 7 (AI Infrastructure) |

---

## 1. Purpose

This document defines the engineering principles that govern **how NEXUS builds software**. Every architectural decision, technology choice, and code review should be consistent with these principles. Where the principles conflict with a specific situation, the precedence order at the end applies.

## 2. The 14 principles

### Principle 1 — Boring where possible, novel where necessary

A browser is hard. An agent runtime is hard. We do not also need a novel database, a custom network stack, or a home-grown LLM. **Use proven, mainstream tools** for everything except the parts that are uniquely NEXUS's value: the agent runtime, the Memory Engine, the workflow engine, and the AI-native UX.

*Implication:* PostgreSQL, not a new database. Kubernetes, not a custom orchestrator. Standard OAuth, not a home-grown auth scheme.

### Principle 2 — Modularity through stable contracts

Every major component has a stable interface contract. Components are replaceable. We can swap the model provider, the database, the automation engine, even the browser engine, without rewriting the product.

*Implication:* Adapter interfaces (`ModelGateway`, `MemoryStore`, `AutomationEngine`) are first-class. We document them and version them.

### Principle 3 — Local-first, cloud-optional

Where feasible, work happens on the user's device. Cloud is opt-in. A "local-only mode" exists from day one. Network failures do not break the product; they degrade it.

*Implication:* Caching is the default. Telemetry is opt-in. Sync is opt-in. Cloud Browser Fleet is opt-in.

### Principle 4 — Type everything that crosses a boundary

Every interface, every API, every agent tool, every event has a typed schema. Generated from the schema. Validated at runtime. Errors are typed.

*Implication:* TypeScript for all UI. Strict types. OpenAPI / JSON Schema for APIs. Protobuf or JSON Schema for events. No `any` in shipped code without an exception.

### Principle 5 — Tests are part of the definition of done

A feature is not shipped without:
- Unit tests for business logic
- Integration tests for cross-component flows
- Browser automation tests for UI
- Acceptance tests mapped to PRD criteria
- Documentation updated

*Implication:* A PR that lacks tests fails CI. A feature without acceptance criteria does not enter the PRD.

### Principle 6 — Observability is not optional

Every component emits structured logs, metrics, and traces. Distributed tracing connects a user action from intent → plan → tool → result. We can answer "why did this take 4 seconds?" in minutes.

*Implication:* OpenTelemetry is the default. Dashboards are tied to alerts. On-call engineers have runbooks.

### Principle 7 — Security at the boundary, defense in depth

Every input is untrusted. Every output is checked. Permissions are enforced at the system level, not the application level. The browser engine, agent runtime, and storage each have independent security boundaries.

*Implication:* Sandboxing is real, not aspirational. Encryption-at-rest is mandatory. Secrets never appear in logs. Threat models are reviewed quarterly.

### Principle 8 — Performance is a feature

A 200ms response is delightful. A 2-second response is broken. We measure perceived latency, not just server time. We optimize for the felt experience.

*Implication:* Perceived-latency budgets are part of design specs. Streaming is the default for AI outputs. Caching is aggressive. Cold starts are budgeted.

### Principle 9 — Idempotency everywhere

Every state-mutating operation is idempotent or guarded by a unique operation ID. Retries are safe. Agents can be re-run.

*Implication:* Workflow engine tracks execution IDs. API mutations accept idempotency keys. Cloud Browser tasks can be re-driven.

### Principle 10 — Document the decision, not just the code

Every non-trivial design choice has a written rationale: the alternatives considered, the tradeoffs, the rejected options. ADRs (Architecture Decision Records) are the format.

*Implication:* An ADR template lives in `12_DEVELOPER_GUIDE/`. Major decisions are linked from the relevant phase documents.

### Principle 11 — Progressive enhancement for AI

When AI is uncertain, fall back to non-AI paths. The product must remain useful without the model gateway. The product must remain useful without cloud connectivity.

*Implication:* Every AI feature has a non-AI baseline. Local models can substitute for cloud models. Manual override exists for every automation.

### Principle 12 — Cost-aware architecture

Cloud Browser Fleet, model inference, and storage are not free. Architecture decisions account for cost-per-user at scale. A feature that costs $5/user/month must justify that in revenue or strategic value.

*Implication:* Cost dashboards are part of operational tooling. Cloud usage is metered and rate-limited per user.

### Principle 13 — Backwards compatibility is a contract

Public APIs (the Plugin SDK, the agent marketplace contract, the workflow schema, the export format) are versioned with deprecation windows. Breaking changes require a major version bump and a migration guide.

*Implication:* Semantic versioning for public interfaces. Deprecation warnings before removal. Migration tooling for breaking changes.

### Principle 14 — Open by default

Where possible, formats are open (Markdown, JSON, CSV, OpenAPI). The Plugin SDK is public. The agent contract is public. The Memory export format is documented.

*Implication:* Closed formats require a written exception. The default is open.

## 3. Precedence order

When principles conflict, the order below is authoritative:

1. **Security at the boundary** (P7) — never traded for any other principle.
2. **Local-first, cloud-optional** (P3) — privacy is structural.
3. **Tests are part of done** (P5) — quality is non-negotiable.
4. **Backwards compatibility** (P13) — public contracts are sacred.
5. **Modularity through stable contracts** (P2) — replaceability is sacred.
6. **Type everything** (P4) — boundaries are typed.
7. **Performance is a feature** (P8) — felt experience matters.
8. **Observability is not optional** (P6) — we must see what is happening.
9. **Idempotency everywhere** (P9) — retries are safe.
10. **Cost-aware architecture** (P12) — no unbounded spend.
11. **Progressive enhancement for AI** (P11) — fallbacks exist.
12. **Document the decision** (P10) — reasoning is preserved.
13. **Boring where possible** (P1) — proven tech wins unless unique value demands novelty.
14. **Open by default** (P14) — closed formats require justification.

Note: P1 and P14 are foundational defaults; they govern choices when no higher principle applies. P7, P3, and P5 are absolutes — they override any other principle without exception.

## 4. Engineering organization structure

NEXUS's engineering organization follows the company structure (see NX-DOC-0005 and Phase 5):

- **CTO AI** — owns overall architecture and cross-cutting concerns.
- **Frontend AI** — owns UI framework, design system, screen implementations.
- **Backend AI** — owns APIs, database, event system, queues.
- **Browser AI** — owns Chromium integration, tab management, sync, extensions.
- **AI Platform AI** — owns agent runtime, model gateway, memory engine.
- **Security AI** — owns threat model, encryption, permissioning, audit.
- **QA AI** — owns test framework, acceptance criteria, regression coverage.
- **DevOps AI** — owns CI/CD, deployment, monitoring, scaling.
- **Documentation AI** — owns all internal and external docs.

Each AI agent has a defined Mission, Tools, Memory access, and Escalation rules (see Phase 5).

## 5. Technology stack (canonical)

### Frontend
- React 18+, Next.js, TypeScript (strict), Tailwind CSS for layout primitives.
- State: Zustand for UI state; TanStack Query for server state.
- Streaming: SSE and WebSockets for AI token streaming.

### Desktop
- Tauri preferred (smaller, more secure by default); Electron permitted when specific Chromium APIs require it.
- Native messaging via Rust + WebView.

### Browser engine
- Chromium (latest stable LTS, with periodic upgrades).
- Playwright for browser automation.

### Backend
- Language: TypeScript on Node.js + Rust for performance-critical paths.
- Framework: Fastify (or tRPC for type-safe RPC).
- API: REST + WebSocket; OpenAPI for documentation.

### Database
- Primary: PostgreSQL 16+.
- Vector: pgvector (H1) → Qdrant (H2+ for scale).
- Cache: Redis.

### Storage
- S3-compatible object storage (Cloudflare R2 or AWS S3) for files.

### Auth
- OAuth 2.0 + OIDC for federated identity.
- WebAuthn passkeys for primary auth.
- Hardware-backed key storage where available.

### AI infrastructure
- Model Gateway: abstraction over multiple providers (OpenAI, Anthropic, Google, local).
- Local models: Ollama + llama.cpp; support for open weights.
- Orchestration: LangGraph or custom workflow engine.
- Queue: Temporal for durable workflows.

### Observability
- OpenTelemetry for traces/metrics/logs.
- Grafana + Prometheus (or compatible vendor).
- Sentry for error tracking.

### Deployment
- Docker, Kubernetes (H2+), Fly.io or AWS for H1.

### CI/CD
- GitHub Actions or equivalent.

## 6. Anti-patterns in engineering we reject

| Anti-pattern | Reason |
|--------------|--------|
| Microservices for everything | Premature distribution |
| "Move fast, no docs" | Violates P10 |
| Direct DB access from the UI | Violates P4, P7 |
| Long-lived feature branches | Merges become impossible |
| Skipping tests "to ship faster" | Violates P5 |
| Magic strings and configs | Violates P4 |
| Custom auth implementations | Violates P7 |
| Hardcoded secrets | Violates P7 |
| Single-region single-cloud | Vendor lock-in |
| Optimizing for benchmarks over felt UX | Violates P8 |

## 7. Decision checklist

Every architectural decision must answer "yes" to:

- [ ] Is the chosen technology boring or novel only where required? (P1)
- [ ] Are the contracts stable and replaceable? (P2)
- [ ] Does this work local-first? (P3)
- [ ] Are boundaries typed? (P4)
- [ ] Are tests written? (P5)
- [ ] Is it observable? (P6)
- [ ] Is it secure by default? (P7)
- [ ] Is the perceived latency within budget? (P8)
- [ ] Is it idempotent or guarded? (P9)
- [ ] Is the decision documented? (P10)
- [ ] Does it degrade gracefully without AI? (P11)
- [ ] Is cost understood at scale? (P12)
- [ ] Is backwards compatibility preserved? (P13)
- [ ] Is the format open? (P14)

## 8. Reading list

- **Core Principles** — NX-DOC-0004
- **AI-First Design Philosophy** — NX-DOC-0006
- **Phase 6 — Browser Architecture**
- **Phase 7 — AI Infrastructure**

---

*End NX-DOC-0011.*