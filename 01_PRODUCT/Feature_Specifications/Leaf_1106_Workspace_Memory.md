# NX-FEAT-1106 — Workspace Memory

| Field | Value |
|-------|-------|
| **Document ID** | NX-FEAT-1106 |
| **Title** | Workspace Memory |
| **Area** | NX-FEAT-A0002 — Workspaces |
| **Owner** | AI Platform AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P0 |
| **Horizon target** | H1 |
| **Estimated effort** | M |

---

## 1. Purpose
Each Workspace has its own memory scope. Project facts, decisions, and conversation summaries live in Workspace memory.

## 2. User stories
- As Sara, I want each investigation to have isolated memory.
- As Marcus, I want project context to persist across sessions.

## 3. Functional requirements
### FR-1: Per-Workspace scope
- Memory items tagged with workspace_id.
- Default: agents query only active Workspace memory.
- Cross-Workspace items require explicit user action (per NX-FEAT-1709).

### FR-2: Auto-extraction
- Agents extract facts from conversations and actions.
- User can confirm/reject inferred facts.

### FR-3: Memory inheritance
- Workspace template may pre-seed memory items.

## 4. Non-functional requirements
- Performance: <100ms read; <200ms write.
- Reliability: durable.

## 5. UI surfaces
- Memory Inspector (NX-UI-6008).
- Workspace settings.

## 6. Permissions
- Read: agent within scope.
- Write: agent (with permission); user (manual).
- Delete: user only.

## 7. Telemetry
- `workspace_memory.fact_added`
- `workspace_memory.fact_queried`

## 8. Failure modes
- Scope violation: blocked; logged.
- Conflict (same fact from different sources): user resolves.

## 9. Dependencies
- Memory Engine (NX-FEAT-A0008).

## 10. Out of scope
- Cross-Workspace query (separate leaf NX-FEAT-1709).

## 11. Acceptance criteria summary
- [ ] Default scope is Workspace.
- [ ] Memory item CRUD works.
- [ ] Memory Inspector surfaces scoped items.

## 12. Open questions
- Q: Should there be a "global within team" scope?

## 13. Change log
| Date | Change | Author |
|------|--------|--------|
| 2026-06-30 | Initial spec | AI Platform AI |

---

*End NX-FEAT-1106.*