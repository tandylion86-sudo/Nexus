# NX-ARCH-0403 — SDK Design & Usage

| Field | Value |
|-------|-------|
| **Document ID** | NX-ARCH-0403 |
| **Title** | SDK Design & Usage |
| **Phase** | 10 — Future Expansion |
| **Owner** | Backend AI (NX-AGENT-7055) + Frontend AI (NX-AGENT-7054) + Docs AI (NX-AGENT-7061) |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-07-03 |
| **Depends on** | NX-ARCH-0003, NX-ARCH-0201 (API Surface), NX-ARCH-0402 (API Docs) |

---

## 1. Mission

Define the NEXUS SDK — the official client libraries that wrap the REST/GraphQL/WebSocket APIs — so third-party developers integrate NEXUS in minutes, the SDK is the recommended path (not raw HTTP), and the SDK is the long-term stable interface (not the REST API, which may evolve).

## 2. SDK inventory

NEXUS ships first-party SDKs for the languages that matter most to its target audience (per NX-DOC-0007, Personas).

| Language | Package | Status (H1) | Repo |
|----------|---------|-------------|------|
| **TypeScript / Node** | `@nexus/sdk` | ✅ v1.0 | `github.com/nexus/sdk-ts` |
| **Python** | `nexus-sdk` | ✅ v1.0 | `github.com/nexus/sdk-python` |
| **Go** | `nexus-sdk-go` | H2 | — |
| **Rust** | `nexus-sdk-rust` | H2 | — |
| **Java / Kotlin** | `nexus-sdk-java` | H2 (after enterprise tier) | — |
| **Swift** | `nexus-sdk-swift` | H2 (iOS app) | — |
| **C# / .NET** | `nexus-sdk-dotnet` | H3 | — |

H1 ships TypeScript and Python. The others follow as the platform grows.

## 3. Design principles

Per NX-DOC-0011 P2 (stable contracts), P4 (typed boundaries), and P11 (graceful degradation), the SDK:

1. **Is the recommended path.** Third parties should never need to write raw HTTP.
2. **Is type-safe end to end.** Generated from the OpenAPI spec; the user gets full IDE autocompletion.
3. **Mirrors the resource hierarchy.** `nx.agents.run(...)`, `nx.cloudBrowsers.create(...)` — discoverable, predictable.
4. **Hides transport details.** The user doesn't choose REST vs. WebSocket; the SDK picks per operation.
5. **Surfaces errors clearly.** NEXUS error codes become typed exceptions with a `userMessage`.
6. **Is fully async-native.** Sync wrappers are provided, but the core is `async`/`await` (TS) and `asyncio` (Python).
7. **Is dependency-light.** The TS SDK has 1 runtime dep (the HTTP client); Python has 2 (httpx, pydantic).

## 4. The client shape

```typescript
import { Nexus } from '@nexus/sdk';

const nx = new Nexus({
  apiKey: process.env.NEXUS_API_KEY,
  // optional:
  baseUrl: 'https://api.nexus.ai/v1',  // default
  timeout: 30_000,                      // default 30s
  maxRetries: 3,                        // default 3
});

// Resources are namespaces:
const run = await nx.agents.run({
  agent: 'NX-AGENT-7003',
  input: { task: 'Research quantum computing' },
});
console.log(run.output);

// Streaming:
const stream = nx.agents.runStream({
  agent: 'NX-AGENT-7003',
  input: { task: '...' },
});
for await (const event of stream) {
  if (event.type === 'token') process.stdout.write(event.text);
  if (event.type === 'tool_call') console.log('tool:', event.name);
}

// Errors are typed:
try {
  await nx.workspaces.get('ws_404');
} catch (e) {
  if (e instanceof Nexus.NotFoundError) {
    console.log('Workspace not found');
  } else if (e instanceof Nexus.RateLimitError) {
    console.log(`Rate limited; retry after ${e.retryAfter}s`);
  } else {
    throw e;
  }
}
```

## 5. Resource namespaces

The SDK exposes resources as namespaces, one per OpenAPI tag. As of H1:

- `nx.agents` — run agents, list runs, cancel
- `nx.workspaces` — CRUD, members, settings
- `nx.cloudBrowsers` — create, resume, snapshot, list
- `nx.memory` — search, write, list
- `nx.workflows` — list schedules, run, pause, resume
- `nx.marketplace` — search agents, install, rate
- `nx.billing` — usage, invoices, payment methods
- `nx.audit` — activity log, security events

Each namespace has the same shape: methods that map to OpenAPI operations. Method names follow the API verb (`get`, `list`, `create`, `update`, `delete`, `run`, `cancel`).

## 6. Streaming

Some operations are long-running and emit partial results. The SDK provides:

- **`runStream`** — returns an async iterable of events.
- **`run`** — returns a promise that resolves to the final result (suitable for short runs).
- **Polling helpers** — `runAndPoll` for workflows that emit checkpoint events.

The TS SDK uses `AsyncIterable<T>`; the Python SDK uses `AsyncIterator[T]`. Both are backpressured; neither is firehose.

## 7. Error model

The SDK maps every HTTP error to a typed class. The hierarchy:

```
NexusError
├── NexusRequestError        (network, timeout, 5xx)
│   └── NexusRateLimitError  (429, includes retryAfter)
├── NexusResponseError       (4xx, has code + message)
│   ├── NexusAuthError       (401, 403)
│   ├── NexusNotFoundError   (404)
│   ├── NexusValidationError (400, 422)
│   ├── NexusConflictError   (409)
│   └── NexusServerError     (5xx)
└── NexusProtocolError       (response shape unexpected)
```

Every error has:

- `message` — human-readable; safe to show.
- `code` — the NEXUS error code (e.g., `NX-ERR-1004`).
- `requestId` — for support.
- `status` — the HTTP status.
- `cause` — the underlying error (for wrapping).

The Python SDK uses the same hierarchy as Python exception types.

## 8. Pagination

The SDK supports two pagination styles, picked per endpoint:

- **Cursor-based** (the default for most list endpoints): `for await (const item of nx.agents.list({ workspace: 'w_1' }))`.
- **Page-based** (for a few stable endpoints): `nx.agents.listPage({ page: 2, perPage: 50 })`.

Cursor pagination is preferred (NX-DOC-0011 P13) because it's stable across inserts.

## 9. Configuration

The client takes a config object:

```typescript
interface NexusConfig {
  apiKey: string;              // required
  baseUrl?: string;            // default https://api.nexus.ai/v1
  timeout?: number;            // default 30_000 ms
  maxRetries?: number;         // default 3
  retryOn?: number[];          // default [408, 429, 500, 502, 503, 504]
  idempotencyKey?: (op: string) => string;  // custom key generator
  userAgent?: string;          // default 'nexus-sdk/1.0.0'
  fetch?: typeof fetch;        // for custom fetch (Node, edge)
}
```

Env vars are also supported: `NEXUS_API_KEY`, `NEXUS_BASE_URL`, `NEXUS_TIMEOUT`.

## 10. Retries and idempotency

- **Retries are automatic** for retryable statuses (per `retryOn`).
- **Backoff is exponential** with jitter: 500ms, 1s, 2s, 4s, capped at 30s.
- **Idempotency keys** are auto-generated for write operations, derived from the request body hash. Users can override with `idempotencyKey: 'my-key'`.
- **The SDK never retries a non-idempotent request** (e.g., `POST` without an idempotency key) on 5xx — it surfaces the error.

## 11. Authentication

Three auth modes:

| Mode | Use | Example |
|------|-----|---------|
| **API key** | Server-to-server | `apiKey: 'nxk_...'` |
| **OAuth bearer** | User-context (e.g., a partner app acting on behalf of a user) | `bearerToken: 'eyJ...'` |
| **Agent token** | Agent identity (per NX-AGENT-70##) | `agentToken: 'nxa_...'` |

API keys are prefixed `nxk_`, agent tokens `nxa_`, OAuth tokens are opaque JWTs.

## 12. Versioning and stability

- **Semver.** Breaking changes get a major version. The current `1.x` is the H1 API.
- **LTS.** Every major version is supported for 12 months after the next major ships.
- **Deprecation warnings.** When an API is deprecated, the SDK logs a warning to `console.warn` (TS) / `warnings.warn` (Python) with the migration path.
- **Codemod.** A `nexus-codemod` CLI auto-migrates common patterns.

## 13. Testing and CI

The SDK has its own test suite, separate from the API:

- **Unit tests** for the client (mocked transport).
- **Integration tests** against a sandbox API (testcontainers).
- **Type tests** (`tsd` for TS, `mypy` for Python) — the public types are tested for shape and assignability.
- **Schema compatibility** — the SDK is rebuilt against every API spec change; if the change is breaking, the SDK major version bumps.

The SDK's CI matrix: Node 18, 20, 22; Python 3.10, 3.11, 3.12.

## 14. Distribution

| Language | Registry | Install |
|----------|----------|---------|
| TypeScript | npm | `npm install @nexus/sdk` |
| Python | PyPI | `pip install nexus-sdk` |
| Go | pkg.go.dev | `go get github.com/nexus/sdk-go` |
| Rust | crates.io | `cargo add nexus-sdk` |
| Java | Maven Central | TBD |
| Swift | Swift Package Index | TBD |
| C# | NuGet | TBD |

Each package is signed; signatures are verified in CI.

## 15. Failure modes

| Failure | Behavior |
|---------|----------|
| Network error | Retry; then NexusRequestError |
| 429 | Retry after `Retry-After`; then NexusRateLimitError |
| 5xx | Retry on retryable; then NexusServerError |
| 4xx (not 429) | No retry; typed error raised |
| Stream interrupted | Resume from last event ID; SDK provides `stream.from(eventId)` |
| Auth expired | Auto-refresh OAuth tokens; re-throw if refresh fails |
| Schema mismatch | Logged + alert; SDK may not understand a new field (forward-compat) |

## 16. Open questions

- Q: Should the SDK support browser builds (smaller, no Node deps)? (Decision: yes, H1; the TS SDK has a separate entry point.)
- Q: Generated vs. hand-written SDK? (Decision: generated scaffold + hand-written "ergonomic" wrapper layer. Pure generated is too thin.)
- Q: Should we publish a CLI that wraps the SDK? (Decision: yes, H2; the `nexus` CLI uses the SDK internally.)

## 17. Reading list

- **Overview** — NX-ARCH-0003
- **API Surface** — NX-ARCH-0201
- **API Documentation** — NX-ARCH-0402
- **Coding Standards** — NX-ARCH-0401
- **Plugin Development** — NX-ARCH-0404
- **Contribution Guide** — NX-ARCH-0405
- **Backend AI Manifest** — NX-EM-9603
- **Frontend AI Manifest** — NX-EM-9608
- **Documentation AI Manifest** — NX-EM-9606
- **Technical Principles** — NX-DOC-0011 (P2, P4, P11, P13)

---

*End NX-ARCH-0403.*
