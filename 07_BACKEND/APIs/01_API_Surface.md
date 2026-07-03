# NX-ARCH-0201 — API Surface

| Field | Value |
|-------|-------|
| **Document ID** | NX-ARCH-0201 |
| **Title** | API Surface |
| **Phase** | 7 — AI Infrastructure |
| **Owner** | Backend AI (NX-AGENT-7055) |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-07-02 |
| **Depends on** | NX-ARCH-0002, NX-ARCH-0202 (Auth), NX-EM-9603 (Backend AI) |

---

## 1. Mission

Define NEXUS's public and partner-facing API surface — the contract that every NEXUS client (app, Cloud Browser, agent, integration) programs against — so the surface is stable, versioned, documented, and observable.

## 2. API styles

NEXUS exposes four API styles, each for a specific use case.

| Style | Use case | Transport | Format | Doc spec |
|-------|----------|-----------|--------|----------|
| **REST** | CRUD, configuration, traditional webhooks | HTTPS | JSON | OpenAPI 3.1 |
| **GraphQL** | Read-heavy, deeply nested data (Memory Engine, Marketplace listings) | HTTPS | JSON | GraphQL SDL |
| **WebSocket** | AI token streaming, live view, real-time events | WSS | JSON / MessagePack | Custom schema |
| **gRPC** | Internal service-to-service (H2+) | HTTP/2 | Protobuf | Protos in repo |

The **public API** is REST + GraphQL + WebSocket. gRPC is internal-only.

## 3. URL structure

```
https://api.nexus.ai/v1/<resource>
wss://stream.nexus.ai/v1/<channel>
https://api.nexus.ai/graphql
```

- `v1` is the current major version. Backwards-incompatible changes get a new major version (`v2`).
- All endpoints are namespaced by resource (e.g., `/v1/workspaces`, `/v1/agents`, `/v1/cloud-browsers`).
- WebSocket channels are namespaced similarly (`/v1/agents/<id>/stream`).

## 4. The NX-API-#### ID scheme

Per the Cover doc, **API identifiers** (endpoints, events, errors) get `NX-API-####` IDs from the 8000–8999 range. Allocation:

| Range | Purpose |
|-------|---------|
| 8000–8099 | Common (errors, pagination, rate limits) |
| 8100–8199 | Authentication & accounts |
| 8200–8299 | Workspaces |
| 8300–8399 | Agents & marketplace |
| 8400–8499 | Cloud Browsers |
| 8500–8599 | Memory & knowledge graph |
| 8600–8699 | Workflows & schedules |
| 8700–8799 | Billing & subscriptions |
| 8800–8899 | Telemetry, audit, observability |
| 8900–8999 | Reserved (future expansion) |

Every endpoint gets an ID. Every error code gets an ID. Every event type gets an ID. The IDs are stable across versions — they are part of the contract.

## 5. Versioning

Per NX-DOC-0011 P13 (backwards compatibility is a contract):

- **Major version** (`v1` → `v2`): breaking changes only. Old version supported for 12 months after new version GA.
- **Minor version** (in headers or path): additive changes. No breaking changes to existing fields.
- **Patch version**: bug fixes, no contract change.

Deprecation policy:

- Endpoint marked deprecated → 6 months notice + `Sunset` header.
- `Sunset` date is honored — endpoint stops working on that date.
- Deprecations are announced on the developer changelog and emailed to API consumers.

## 6. Authentication

Authentication uses bearer tokens (per NX-ARCH-0202):

```
Authorization: Bearer <access_token>
```

- **User tokens** (session-bound): short-lived (1 hour), refresh via refresh token.
- **Agent tokens** (long-lived): scoped per agent, revocable, with explicit capability grants.
- **Partner tokens** (OAuth client credentials): for integrations, scoped per integration.

WebSocket connections authenticate via a query parameter or subprotocol token at connection time.

## 7. Rate limits

Rate limits are per-token, per-resource, and per-tier. Default limits (per NX-PRD-0005):

| Tier | Requests / minute | Concurrent | Burst |
|------|------------------:|-----------:|------:|
| Free | 60 | 5 | 100 |
| Pro | 600 | 25 | 1,000 |
| Team | 600/seat | 25/seat | 1,000/seat |
| Business | 1,200/seat | 50/seat | 2,000/seat |
| Enterprise | Custom | Custom | Custom |

Rate limit responses include:

- `X-RateLimit-Limit`
- `X-RateLimit-Remaining`
- `X-RateLimit-Reset`
- `Retry-After` (on 429)

Agent-driven rate limits are tracked separately from user limits (per agent, not per user) so a runaway agent doesn't block the user.

## 8. Pagination

Cursor-based pagination for all list endpoints. No `offset` (encourages stable cursors; supports infinite scroll).

```json
{
  "data": [...],
  "page_info": {
    "has_next_page": true,
    "next_cursor": "eyJpZCI6MTIzfQ==",
    "total_count": 1234
  }
}
```

Default page size: 50. Max: 200. Configurable per call.

## 9. Errors

Standard error envelope:

```json
{
  "error": {
    "id": "NX-API-8001",
    "code": "rate_limit_exceeded",
    "message": "Rate limit exceeded. Try again in 30 seconds.",
    "details": {
      "retry_after_ms": 30000
    },
    "request_id": "req_abc123",
    "documentation_url": "https://docs.nexus.ai/errors/NX-API-8001"
  }
}
```

- `id` is the stable `NX-API-####` identifier.
- `code` is a snake_case machine-readable code.
- `message` is human-readable, safe to display to end users.
- `request_id` is the trace ID — used for support.
- `documentation_url` is always present; docs explain the error, what causes it, and how to fix it.

## 10. Webhooks

Webhooks let NEXUS push events to partner systems. The webhook contract:

- **Signed.** HMAC-SHA256 of the body using a per-subscription secret; signature in `X-Nexus-Signature`.
- **Retried.** Exponential backoff up to 24 hours, then dead-letter.
- **Ordered within a subscription.** No global ordering guarantee.
- **Replayable.** A replay endpoint re-fires a past event.
- **Documented per event.** Each event has an `NX-API-####` ID and a documented payload schema.

Event categories (illustrative):

- `agent.run.started`, `agent.run.completed`, `agent.run.failed` (NX-API-83xx)
- `cloud_browser.created`, `cloud_browser.idle`, `cloud_browser.deleted` (NX-API-84xx)
- `memory.item.created`, `memory.item.updated` (NX-API-85xx)
- `workflow.scheduled`, `workflow.executed` (NX-API-86xx)
- `subscription.created`, `subscription.cancelled` (NX-API-87xx)

## 11. Streaming and WebSocket

WebSocket channels (NX-ARCH-0202 for auth):

- `agent.<id>.stream` — AI token streaming for chat/command.
- `agent.<id>.events` — agent lifecycle events.
- `cloud_browser.<id>.live` — live view frame stream.
- `cloud_browser.<id>.events` — browser events (navigation, errors, etc.).
- `workspace.<id>.events` — workspace-level events for collaboration.
- `user.events` — user-level events (notifications, billing).

Each channel has a documented message schema, with `NX-API-####` IDs for each message type.

## 12. Observability

Every API request emits:

- Trace (OpenTelemetry): full request trace with span IDs.
- Metrics: `api.request.count`, `api.request.duration_ms`, `api.error.count` (per endpoint, per status, per client).
- Logs: structured, with `request_id`, `user_id`, `agent_id` (if applicable).

These are visible:

- **To the user:** in their Activity Log (their requests, their errors).
- **To the user (admin):** for Team/Business/Enterprise, in the workspace observability dashboard.
- **To NEXUS:** in the global observability stack (Grafana, Datadog, etc.).

## 13. Security considerations

- **TLS everywhere.** No plaintext HTTP. HSTS enabled.
- **CORS** is restrictive by default; partners are explicitly allowlisted.
- **CSRF** is mitigated by token-based auth + SameSite cookies.
- **Input validation** at the gateway; no endpoint trusts the client.
- **Output encoding** for all user-generated content rendered to other users.
- **SQL injection** impossible because we use parameterized queries (NX-ARCH-0203).
- **Secret leakage** mitigated by no echoing secrets in errors.

## 14. Performance budgets

- **Read p95:** < 100ms.
- **Write p95:** < 300ms (synchronous writes; async work goes to workflows).
- **GraphQL p95:** < 200ms.
- **WebSocket frame latency p95:** < 50ms.
- **Webhook delivery p95:** < 5s (excluding partner downtime).

## 15. Open questions

- Q: Do we ship a NEXUS SDK (TypeScript, Python) at H1 launch? (Probably yes; H2 candidates: Go, Rust, Swift.)
- Q: Should we expose agent-to-agent APIs (one agent invoking another's tools) directly, or only via the orchestrator? (Orchestrator-only for audit clarity; direct is H3+.)
- Q: GraphQL federation across subdomains, or single endpoint? (Single endpoint for H1; federation H2+.)

## 16. Reading list

- **Overview** — NX-ARCH-0002
- **Authentication** — NX-ARCH-0202
- **Database** — NX-ARCH-0203
- **Event System** — NX-ARCH-0204
- **Backend AI Manifest** — NX-EM-9603
- **Master PRD** — NX-PRD-0001
- **Subscription Model** — NX-PRD-0005
- **Technical Principles** — NX-DOC-0011 (P7, P9, P13)

---

*End NX-ARCH-0201.*
