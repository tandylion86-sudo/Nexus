# NX-ARCH-0401 — Coding Standards & Style Guide

| Field | Value |
|-------|-------|
| **Document ID** | NX-ARCH-0401 |
| **Title** | Coding Standards & Style Guide |
| **Phase** | 10 — Future Expansion |
| **Owner** | Frontend AI (NX-AGENT-7054) + Backend AI (NX-AGENT-7055) + Docs AI (NX-AGENT-7061) |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-07-03 |
| **Depends on** | NX-ARCH-0003, NX-DOC-0011 (Tech Principles), NX-WF-9003 (Quality Gates) |

---

## 1. Mission

Define the engineering style and standards for the NEXUS codebase — language, types, tests, structure, and review — so every contribution is consistent, readable, and meets the same bar regardless of who wrote it (human or AI agent).

## 2. Languages and tooling

NEXUS has two primary languages per NX-DOC-0011 §5.

| Language | Use | Tooling |
|----------|-----|---------|
| **TypeScript** | Frontend, backend API, workers, SDK, scripts | `tsc` (strict), `eslint`, `prettier`, `vitest` |
| **Rust** | Browser engine integration, performance-critical paths (e.g., event loop bridge, model tokenization) | `cargo`, `clippy`, `rustfmt`, `cargo test` |

A small amount of **Python** is used for ML training and evaluation (per Phase 4). Python is *not* used for application code; it's only in `services/ml/` and the eval harness.

## 3. TypeScript standards

### 3.1 tsconfig

Every TS package uses a strict config:

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "strict": true,
    "noImplicitAny": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedIndexedAccess": true,
    "noPropertyAccessFromIndexSignature": true,
    "exactOptionalPropertyTypes": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "isolatedModules": true
  }
}
```

These are non-negotiable. A PR that loosens any of these is rejected.

### 3.2 No `any`

`any` is forbidden except in three well-justified cases:

1. **Bridging untyped JS libraries.** With a `// eslint-disable-next-line` comment and a TODO to type it properly.
2. **Test fixtures** where the alternative is verbose and the test is clear.
3. **Generic escape hatches** in the SDK (`unknown` is preferred; `any` requires an explicit `// any: reason` comment).

Use `unknown` for values whose type is genuinely not known yet; narrow with type guards. The `unknown` is preferred to `any` everywhere.

### 3.3 Naming

- **Variables, functions, methods:** `camelCase`
- **Types, classes, interfaces, enums:** `PascalCase`
- **Constants (module-level immutable):** `SCREAMING_SNAKE_CASE`
- **File names:** `kebab-case.ts`
- **React components:** `PascalCase.tsx` (file matches the default export)
- **Test files:** `*.test.ts` co-located with the source

### 3.4 Imports

- **Path aliases** (`@/services/...`) over deep relative imports.
- **No default exports** for modules that export more than one thing; preferred even for one-thing modules in shared code.
- **Sort imports** by ESLint (`import/order`): external, internal `@nexus/*`, relative. Blank line between groups.

### 3.5 Async

- **Always `async`/`await`** over raw `.then()` chains. Exception: `Promise.all([...])`.
- **No floating promises.** Every promise is awaited, returned, or `.catch()`-ed. ESLint rule `@typescript-eslint/no-floating-promises` is on.
- **No fire-and-forget** in production code paths; the only fire-and-forget is in well-isolated telemetry emitters.

### 3.6 Errors

- **Throw `Error` subclasses**, not strings or plain objects. A `NexusError` base class is the standard.
- **Every thrown error has a code** (`error.code`) and a `userMessage` (safe to show to users).
- **No silent catches.** `catch (e) {}` is forbidden. Catch, log, and either rethrow or handle explicitly.

## 4. Rust standards

- **`cargo fmt --check`** in CI.
- **`cargo clippy -- -D warnings`** in CI.
- **No `unwrap()`** in non-test code. `expect()` with a message is allowed when the invariant is documented.
- **No `panic!`** in library code. In binaries, panics in startup paths are OK if documented.
- **Error handling** via `thiserror` for libraries, `anyhow` for binaries.
- **Async** uses `tokio`; no mixing with `async-std`.
- **Public APIs** are documented with `///` doc comments; CI fails if a public item lacks docs.

## 5. File and module structure

```typescript
// Every TS file follows this order:
// 1. License/copyright (if applicable)
// 2. Imports (external, internal, relative)
// 3. Type definitions local to the file
// 4. Constants
// 5. Helper functions (private to the file)
// 6. Main exported functions/classes
// 7. Default export (if any)
```

The structure is enforced by `eslint-plugin-import/order` and reviewed by the AI agents (the Frontend/Backend AI agents have these conventions in their training prompts).

## 6. Tests

### 6.1 The pyramid

| Layer | Tool | What it tests | Speed |
|-------|------|---------------|-------|
| **Unit** | Vitest | Pure functions, classes, branches | < 1 ms each |
| **Integration** | Vitest + testcontainers | DB queries, API endpoints, event handling | < 1 s each |
| **E2E** | Playwright | Full user flows, browser automation | < 30 s each |
| **Load** | k6 | Throughput, latency, saturation | Minutes |
| **Contract** | Pact | API compatibility between services | < 5 s each |

### 6.2 Coverage

- **Lines: 80%.**
- **Branches: 70%.**
- **Functions: 85%.**

Coverage is measured per package. A PR that drops a package's coverage below its baseline fails the build.

### 6.3 Test naming

```typescript
// Pattern: 'should <expected> when <condition>'
test('should return 404 when workspace is not found', ...);
test('should retry with exponential backoff when upstream is unavailable', ...);
test('should redact PII when logging user input', ...);
```

The condition is explicit; the assertion is clear. No "test 1", "test 2".

### 6.4 No skipped tests

`it.skip`, `xit`, `xdescribe` are forbidden in CI. A skipped test is a deleted test; if it's not worth running, it's not worth having. The only exception is `@skip` with a linked issue and an expiry date (the test must be un-skipped or removed within 30 days).

## 7. Linting and formatting

- **ESLint** with `@typescript-eslint`, `eslint-plugin-import`, `eslint-plugin-security`, `eslint-plugin-no-relative-import-paths`. The config is in `eslint.config.js` at the repo root.
- **Prettier** for formatting. No debates about formatting — Prettier decides.
- **Husky** + **lint-staged** runs ESLint and Prettier on staged files before commit.
- **CI** re-runs the lint on the full PR; if local pre-commit was bypassed, CI catches it.

The same applies to Rust: `rustfmt` and `clippy` run on staged files pre-commit, and full on CI.

## 8. Documentation in code

- **Every public function** has a JSDoc comment with `@param`, `@returns`, `@throws`, and an example.
- **Every module** has a top-of-file comment explaining its purpose, when to use it, and what it does *not* do.
- **Complex algorithms** have inline comments explaining *why*, not *what*.
- **No commented-out code.** Delete it; Git remembers. The only exception is a `// TODO: <issue link>` with a real issue.

## 9. Git conventions

### 9.1 Branch names

`<type>/<short-kebab-description>` — e.g., `fix/login-redirect-loop`, `feat/agent-streaming-cancel`, `chore/upgrade-fastify-v5`.

Types: `feat`, `fix`, `chore`, `refactor`, `docs`, `test`, `perf`, `ci`.

### 9.2 Commit messages

[Conventional Commits](https://www.conventionalcommits.org/):

```
feat(agents): add cancellation to streaming runs

Allow users to cancel an in-flight streaming agent run.
The cancellation propagates to in-flight tool calls.

Closes #1234
```

Breaking changes get a `!` and a `BREAKING CHANGE:` footer.

### 9.3 PRs

- **Title** = the commit message subject.
- **Description** = what, why, how to test. Screenshots for UI.
- **Linked issues** via `Closes #N` or `Refs #N`.
- **Reviewers:** at least one human for code that touches auth, billing, or the agent runtime; the AI agents self-review for everything else.
- **CI must be green** before merge.

## 10. Code review

For code review expectations, see `NX-WF-9003` (Quality Gates). Highlights:

- **At least one approver** from the relevant AI agent (Frontend, Backend, Browser, AI Platform, Security, DevOps) or a human.
- **Security review** required for changes to auth, billing, agent runtime, or any cross-tenant boundary.
- **Performance review** required for changes to hot paths (token streaming, Cloud Browser navigation, Memory index).
- **Doc review** required for changes to public API or SDK.

The AI agents review like humans: they look for correctness, security, perf, testability, readability. The prompts that drive this review are in `99_MASTER_PROMPTS/Workflows/`.

## 11. Architecture decisions

Non-trivial decisions are recorded as **ADRs** (Architecture Decision Records) in `docs/adr/`. The format:

```markdown
# ADR-NNNN: <title>

## Status
Accepted / Proposed / Deprecated / Superseded by ADR-XXXX

## Context
What is the situation? What forces are at play?

## Decision
What did we choose?

## Consequences
What becomes easier? What becomes harder?

## Alternatives considered
What else did we look at, and why didn't we pick it?
```

ADRs are immutable once accepted. A new ADR supersedes an old one; the old one is updated with "Superseded by ADR-XXXX".

## 12. Failure modes

| Failure | Behavior |
|---------|----------|
| Lint fails in CI | PR blocked; fix locally or `pnpm lint --fix` |
| Typecheck fails | PR blocked; run `pnpm typecheck` |
| Test fails | PR blocked; investigate; do not skip |
| Coverage drops | PR blocked; add tests or get an exception from QA AI |
| Pre-commit hook bypassed | CI catches it; the commit author is educated |

## 13. Open questions

- Q: Should NEXUS publish its coding standards as a standalone doc, or keep them in the codebase (as `CONTRIBUTING.md`)? (Decision: both — this doc is canonical; the `CONTRIBUTING.md` is a short pointer.)
- Q: Stricter linting (deny all warnings, even style)? (Decision: H2 — once the codebase stabilizes.)

## 14. Reading list

- **Overview** — NX-ARCH-0003
- **Technical Principles** — NX-DOC-0011
- **Quality Gates** — NX-WF-9003
- **API Documentation Standards** — NX-ARCH-0402
- **SDK Design** — NX-ARCH-0403
- **Contribution Guide** — NX-ARCH-0405
- **Frontend AI Manifest** — NX-EM-9608
- **Backend AI Manifest** — NX-EM-9603
- **Documentation AI Manifest** — NX-EM-9606

---

*End NX-ARCH-0401.*
