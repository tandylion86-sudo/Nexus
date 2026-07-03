# TODO — Phase 7: AI Infrastructure (`07_BACKEND/`)

## Goal
Write the backend / AI infrastructure architecture documentation. Phase 7 spans `07_BACKEND/` per the Phase 6–10 reconciliation; per `11_Technical_Principles` and the Cover doc, this is where `NX-API-####` IDs (range 8000–8999) live.

## Result: ✅ DONE

## What was written

8 architecture docs, ~12,603 words total:

| ID | File | Words |
|----|------|------:|
| NX-ARCH-0002 | `00_Overview.md` | 879 |
| NX-ARCH-0201 | `APIs/01_API_Surface.md` | 1,232 |
| NX-ARCH-0202 | `Authentication/02_Authentication.md` | 1,410 |
| NX-ARCH-0203 | `Database/03_Database_Architecture.md` | 1,617 |
| NX-ARCH-0204 | `Event_System/04_Event_System.md` | 1,317 |
| NX-ARCH-0205 | `Infrastructure/05_Infrastructure.md` | 1,966 |
| NX-ARCH-0206 | `Queues/06_Queues_and_Workflows.md` | 1,958 |
| NX-ARCH-0207 | `Storage/07_Storage.md` | 2,224 |

## What was created/changed

- **All 7 subdirs of `07_BACKEND/`** now have a doc.
- **Zero empty subdirs in `07_BACKEND/`.**
- **PROGRESS.md** updated: Phase 7 status moved to 🟢 Complete, with per-doc word counts and totals.
- **MASTER_INDEX.md** updated: added Phase 7 section with overview + 7 leaf docs, plus phase status table updated.
- **DOCUMENT_REGISTRY.md** updated: added Phase 7 section with 8 doc rows.
- **README.md** updated: Phase 7 status line added, total word/page count updated.

## Design choices made

- **Doc IDs** follow Phase 6's pattern: `NX-ARCH-0002` (overview) and `NX-ARCH-0201..0207` (one per subdir). Leaves room for Phase 8 to use `NX-ARCH-0301..0399`.
- **Each leaf doc follows the same 14-section template** as Phase 6, plus "Open questions" — consistent style across the architecture phases.
- **Overview doc sets the layered architecture** (Mermaid diagram) that the leaf docs elaborate, plus articulates the "two workloads" doctrine (user + agent).
- **Every leaf doc cross-references the overview** (NX-ARCH-0002) at least twice.
- **Every leaf doc references NX-DOC-0011 (Technical Principles)** in its reading list with the specific principle number relevant to the topic.
- **Tech stack is fully consistent with NX-DOC-0011 §5**: TypeScript/Node.js + Rust, Fastify, REST + WebSocket + OpenAPI, Postgres 16+ with pgvector → Qdrant, Redis, S3-compatible storage, Temporal, OpenTelemetry.
- **NX-API-#### ID allocation** is centralized in NX-ARCH-0201 (range 8000–8999) — leaves room for the actual endpoint/event/error registry to be populated later.

## Key architectural decisions captured

1. **Modular monolith for H1, not microservices** (per NX-DOC-0011 anti-pattern: "microservices for everything").
2. **Durable workflows on Temporal; short jobs on BullMQ** — the "workflows vs. jobs" doctrine.
3. **Redis Streams for H1 event bus; NATS or Kafka for H2+** — boring where possible, novel where necessary.
4. **Outbox pattern** for at-least-once event delivery.
5. **Per-user encryption** for Cloud Browser profile state — answers NX-FEAT-1600 NFR-3.
6. **S3-compatible storage only** (no cloud-specific services) — answers NX-DOC-0011 P14 (open formats).
7. **H1 single region; H2+ active-active multi-region** with explicit RPO/RTO targets.
8. **Distroless container images + Cosign signing** for supply chain security.
9. **Idempotency at every layer** (workflows, jobs, activities) per NX-DOC-0011 P9.

## Verification

- [x] All 7 leaf architecture documents (NX-ARCH-0201..0207) complete.
- [x] Every leaf doc cross-references NX-ARCH-0002.
- [x] Tech stack matches NX-DOC-0011 §5.
- [x] API surface doc includes NX-API-#### ID allocation strategy.
- [x] No empty subdirs in `07_BACKEND/`.
- [x] PROGRESS.md, MASTER_INDEX.md, DOCUMENT_REGISTRY.md, README.md all updated.

## What's NOT in Phase 7

This phase is **architecture-level**, like Phase 6. Specific things deferred to implementation repos (not the blueprint):

- Actual OpenAPI specs for every endpoint (lives in `services/api/openapi.yaml` in the implementation repo).
- Actual Postgres DDL (lives in `services/api/db/migrations/`).
- Helm charts / Terraform modules (lives in `infra/`).
- Specific Temporal workflow implementations (lives in `services/workflows/`).
- Per-endpoint rate limit values (H1 ops decision; documented in Phase 10 deployment).
- Disaster recovery runbooks (lives in `infra/runbooks/`).

## Repo totals after this work

- 309 docs / ~144,600 words / ~577 pages
- Phases 1–7 complete
- 0 empty subdirs in `07_BACKEND/`
- 0 empty subdirs in `04_BROWSER_ENGINE/`
- Architecture phases 6 + 7 fully documented

## Next phase candidates

- **Phase 8** (Marketplace): `09_MARKETPLACE/` + security aspect of marketplace in `08_SECURITY/`. Per Phase 6–10 reconciliation, this is the marketplace mechanics (billing flows, plugin SDK surface, agent store UX).
- **Phase 9** (Enterprise Platform): `11_BUSINESS/` — pricing, financials, GTM, investors.
- **Phase 10** (Future Expansion): `10_DEPLOYMENT/` + `12_DEVELOPER_GUIDE/` + `99_MASTER_PROMPTS/`.
