# NX-FEAT-1109 — Workspace Search

| Field | Value |
|-------|-------|
| **Document ID** | NX-FEAT-1109 |
| **Title** | Workspace Search |
| **Area** | NX-FEAT-A0002 — Workspaces |
| **Owner** | Frontend AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P1 |
| **Horizon target** | H1 |
| **Estimated effort** | M |

---

## 1. Purpose
Users search across all Workspaces by name, goal, notes, and files. Search is the primary discovery mechanism.

## 2. User stories
- As Sara, I want to find a Workspace from 6 months ago.
- As Devin, I want to search across notes.

## 3. Functional requirements
### FR-1: Cross-Workspace search
- Triggers via ⌘K / Ctrl+K.
- Searches: name, goal, notes, files, memory.

**Acceptance:**
- [ ] <500ms for 100 Workspaces.
- [ ] Live filtering.

### FR-2: Filters
- Date range.
- Has agent, has integration.
- Workspace status (active / archived).

### FR-3: Result ranking
- Recency + match relevance.
- Snippet preview.

## 4. Non-functional requirements
- Search latency: <500ms p95.

## 5. UI surfaces
- ⌘K command palette; in-switcher search.

## 6. Permissions
- Search own Workspaces; team Workspaces if member.

## 7. Telemetry
- `workspace_search.queried`
- `workspace_search.result_clicked`

## 8. Failure modes
- Index unavailable: keyword search fallback.
- Empty results: clear message.

## 9. Dependencies
- Search index (per Phase 7).

## 10. Out of scope
- Semantic search (RAG) — handled in Memory Engine (NX-FEAT-1714).

## 11. Acceptance criteria summary
- [ ] <500ms p95.
- [ ] Multi-source search.
- [ ] Filters work.

## 12. Open questions
- Q: Should we support regular expressions in search?

## 13. Change log
| Date | Change | Author |
|------|--------|--------|
| 2026-06-30 | Initial spec | Frontend AI |

---

*End NX-FEAT-1109.*