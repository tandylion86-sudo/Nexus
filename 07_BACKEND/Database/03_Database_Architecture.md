# NX-ARCH-0203 — Database Architecture

| Field | Value |
|-------|-------|
| **Document ID** | NX-ARCH-0203 |
| **Title** | Database Architecture |
| **Phase** | 7 — AI Infrastructure |
| **Owner** | Backend AI (NX-AGENT-7055) |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-07-02 |
| **Depends on** | NX-ARCH-0002, NX-ARCH-0207 (Storage), NX-EM-9603 (Backend AI) |

---

## 1. Mission

Define the data layer for NEXUS — the databases, schemas, migration discipline, and access patterns — so data is durable, consistent, queryable for both humans and agents, and safe across multi-tenant boundaries.

## 2. Database inventory

Per NX-DOC-0011 §5, the data layer uses:

| Database | Purpose | H1 role | H2+ role |
|----------|---------|---------|----------|
| **PostgreSQL 16+** | Primary OLTP, transactional data | Production | Production |
| **pgvector** | Embedding storage, semantic search | Production (small/medium scale) | Supplement; replaced at scale |
| **Qdrant** | Vector search at scale | Evaluated | Production |
| **Redis** | Cache, sessions, ephemeral state, pub/sub | Production | Production |
| **ClickHouse** (H2+) | Analytics, audit log, event store | Not in H1 | Production |
| **S3-compatible** (NX-ARCH-0207) | Files, blobs, snapshots | Production | Production |

H1 ships with Postgres + pgvector + Redis. Qdrant migration path is documented; ClickHouse is H2.

## 3. PostgreSQL — the system of record

PostgreSQL is the source of truth for all transactional data. Schemas are versioned with `nx-migrate` (a thin wrapper around `node-pg-migrate`); every migration is reversible, in both directions.

### 3.1 Schema layout

```
db/
├── migrations/                   # forward + reverse migrations, ordered
│   ├── 0001_init.up.sql
│   ├── 0001_init.down.sql
│   ├── 0002_workspaces.up.sql
│   └── ...
├── schemas/                      # canonical schema definitions
│   ├── users.sql
│   ├── workspaces.sql
│   ├── agents.sql
│   ├── cloud_browsers.sql
│   ├── memory.sql
│   ├── workflows.sql
│   └── ...
└── seeds/                        # development seeds (never in production)
```

### 3.2 Core entities

| Entity | Purpose | Key relationships |
|--------|---------|-------------------|
| `users` | User accounts | has many workspaces, devices, agents |
| `workspaces` | Goal-oriented workspaces (NX-FEAT-A0002) | belongs to user; has many members (RBAC) |
| `profiles` | Browser profiles (NX-ARCH-0103) | belongs to user; has many sessions |
| `devices` | Enrolled devices | belongs to user |
| `agents` | Installed agents (instance) | references NX-AGENT-#### (the contract) |
| `cloud_browsers` | Cloud Browser instances | belongs to user/workspace |
| `memory_items` | Memory Engine items (NX-AGENT-7010) | belongs to user; has embedding (pgvector) |
| `workflows` | Workflow definitions and runs | belongs to user/workspace |
| `subscriptions` | Billing state | belongs to user/workspace |
| `audit_events` | Append-only audit log | references user, agent, resource |
| `webhooks` | Webhook subscriptions | belongs to user/workspace |
| `api_keys` | Partner API credentials | belongs to user/workspace |

### 3.3 Multi-tenancy

Two strategies coexist, picked per resource:

- **Shared schema with `workspace_id` column** (default): every row has a `workspace_id`; queries always filter by it; the API layer enforces. Cheaper, simpler, scales to tens of thousands of workspaces per database.
- **Schema-per-tenant** (Enterprise only, opt-in): the workspace gets its own PostgreSQL schema. More isolation, higher cost. Used by customers with strict data residency requirements (H2+).

Row-level security (RLS) is enabled on all shared-schema tables as defense in depth. The application sets `app.workspace_id` at the start of every transaction; RLS policies reject any query that doesn't filter by it.

### 3.4 Migrations

Per NX-DOC-0011 P9 (idempotency) and P13 (backwards compatibility):

- **Every migration has an up and a down.** The down is tested in staging before each release.
- **Destructive changes are split.** Adding a column: separate migration. Backfilling data: separate migration. Dropping the column: separate migration, gated on a release flag.
- **Long migrations run in the background.** Tables with > 1M rows get migrated with `pg_repack` or batched jobs; never with a single `ALTER TABLE` on prod.
- **Migration locks are short.** Anything taking > 30s under lock is restructured.

## 4. pgvector — semantic search

`pgvector` stores embeddings alongside the source data. H1 use cases:

- **Memory items** (NX-AGENT-7010): every memory item gets a vector embedding; semantic search is "find items similar to this query".
- **Marketplace listings**: agents have embeddings for "find agents similar to this description".
- **Knowledge graph nodes** (H2+): embeddings help with fuzzy lookup.

### 4.1 Schema

```sql
CREATE TABLE memory_items (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id),
    workspace_id UUID NOT NULL REFERENCES workspaces(id),
    content TEXT NOT NULL,
    embedding vector(1536),  -- OpenAI ada-002 / equivalent
    metadata JSONB NOT NULL DEFAULT '{}',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX memory_items_embedding_idx ON memory_items 
    USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);
```

### 4.2 Migration to Qdrant (H2+)

When pgvector's recall/speed degrades (typically > 10M items per database), NEXUS migrates to Qdrant. The migration:

- Qdrant receives a copy of vectors; pgvector remains the source of truth for metadata.
- Queries go to Qdrant for vector search; metadata fetch from Postgres.
- Eventually, the source of truth can move to Qdrant with a periodic Postgres mirror, if needed.

The decision to migrate is data-driven (latency, recall) — never a date.

## 5. Redis — cache, sessions, ephemeral state

Redis is used for:

- **API cache** (per endpoint, per params, short TTL).
- **Session metadata** (active sessions, last-seen).
- **Rate-limit counters** (per token, per resource).
- **Token deny list** (revoked JWT `jti`).
- **Pub/sub** for cross-service messaging (lightweight; the Event System — NX-ARCH-0204 — is the heavy path).
- **Distributed locks** (workflow coordination; per NX-ARCH-0206).

Redis is **not** a system of record. Anything in Redis is regenerable from Postgres.

## 6. ClickHouse (H2+)

ClickHouse is the analytics database. It receives:

- The audit log (denormalized).
- Aggregated usage metrics.
- Telemetry (per NX-AGENT-7016).
- Business metrics (MRR, churn, activation).

H1 ships without ClickHouse; analytics live in Postgres with materialized views. Migration to ClickHouse is H2 when query latency or data volume justifies it.

## 7. Data access patterns

### 7.1 Read paths

- **Direct DB** (Fastify → Postgres): the default for API reads. Connection-pooled via PgBouncer.
- **Read replicas** (H1: 1 replica; H2+: multiple): for read-heavy endpoints; the API routes by endpoint config.
- **Vector search** (Fastify → pgvector or Qdrant): for semantic search.
- **Cache** (Fastify → Redis → Postgres): for hot data; 30s-5min TTLs.

### 7.2 Write paths

- **Direct DB** (Fastify → Postgres): for synchronous writes.
- **Workflow** (Fastify → Temporal → DB): for long-running or retry-heavy writes (NX-ARCH-0206).
- **Outbox pattern**: a service writes to its DB and an outbox row in the same transaction; a separate process publishes to the event bus. Guarantees no lost events.

### 7.3 Query patterns

- **Indexed reads** — every hot query path has an index; verified via `EXPLAIN ANALYZE` in CI.
- **No N+1** — the application uses `JOIN`s, dataloader, or batch endpoints.
- **Cursor pagination** — never `OFFSET` (per NX-ARCH-0201).
- **Materialized views** — for known aggregate queries (e.g., "agent runs in last 7 days per workspace").
- **Read-only views** — for partner access; granted at the DB level.

## 8. Backup and recovery

- **Continuous backup** (PITR — point-in-time recovery): every 5 minutes, retained 30 days.
- **Daily snapshot**: full DB snapshot, retained 90 days; stored encrypted in S3.
- **Quarterly DR drill**: restore from snapshot in a fresh region, verify data integrity.
- **Per-tenant backup** (Enterprise, H2+): separate backup stream, longer retention, customer-controlled.

RPO (recovery point objective): 5 minutes.
RTO (recovery time objective): 1 hour.

## 9. Schema evolution

- **Additive changes** are safe and unannounced.
- **Breaking changes** (column removal, type change) require a deprecation cycle of 6 months minimum, with both old and new columns populated during the transition.
- **Schema documentation** is auto-generated from the live schema and published to the developer docs.

## 10. Performance budgets

- **OLTP read p95:** < 50ms (Postgres direct).
- **OLTP write p95:** < 100ms.
- **Vector search p95:** < 300ms (1M items in pgvector); < 100ms (Qdrant at scale).
- **Cache hit p95:** < 5ms.
- **Cross-region replication lag:** < 5s.

## 11. Security considerations

- **TLS** for all DB connections (enforced at the connection string).
- **Encryption at rest** via cloud-provider-managed keys; customer-managed keys (CMK) for Enterprise.
- **No direct DB access from the application edge.** All access via parameterized queries (no SQL injection vector).
- **Row-level security** (per §3.3) as defense in depth.
- **PII tagging** — every column is tagged (`pii:email`, `pii:phone`, `pii:none`, etc.); tags drive export and deletion logic.
- **Audit logging** — every write is logged to `audit_events` with the actor and before/after values for sensitive tables.
- **No DB credentials in code** — all credentials via secrets manager (Vault, AWS Secrets Manager).
- **No raw query logs to disk** — slow query log is structured, redacted, and shipped to observability.

## 12. Open questions

- Q: When do we introduce per-region sharding for Postgres? (H2+, when single-region write QPS exceeds capacity.)
- Q: Do we adopt a managed Postgres (RDS, Cloud SQL) or self-host? (Managed for H1; revisit at scale.)
- Q: Should we ship a NEXUS-native OLAP for agent analytics, or rely on ClickHouse + a thin layer? (ClickHouse + thin layer; H2+.)
- Q: How do we handle cross-region consistency for collaborative workspaces? (Active-active for non-conflicting, last-writer-wins for conflicting; H2+.)

## 13. Reading list

- **Overview** — NX-ARCH-0002
- **API Surface** — NX-ARCH-0201
- **Storage** — NX-ARCH-0207
- **Event System** — NX-ARCH-0204
- **Queues & Workflows** — NX-ARCH-0206
- **Memory Schema** — NX-AGENT-7010
- **Backend AI Manifest** — NX-EM-9603
- **Technical Principles** — NX-DOC-0011 (P4, P9, P13)

---

*End NX-ARCH-0203.*
