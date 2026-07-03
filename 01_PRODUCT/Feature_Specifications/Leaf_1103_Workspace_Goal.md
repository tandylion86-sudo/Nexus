# NX-FEAT-1103 — Workspace Goal Sentence

| Field | Value |
|-------|-------|
| **Document ID** | NX-FEAT-1103 |
| **Title** | Workspace Goal Sentence |
| **Area** | NX-FEAT-A0002 — Workspaces |
| **Owner** | Frontend AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P0 |
| **Horizon target** | H1 |
| **Estimated effort** | S |

---

## 1. Purpose
Every Workspace has a single goal sentence. It captures intent, drives suggestions, and is the primary search anchor.

## 2. User stories
- As Maya, I want a goal sentence to remind me why this Workspace exists.
- As Sara, I want my goal sentence to drive research direction.

## 3. Functional requirements
### FR-1: Required at creation
- Goal is required.
- Min 5 chars, max 140.

### FR-2: Inline editable
- Editable from Workspace header.
- Click → input; blur saves.

**Acceptance:**
- [ ] Edit saves in <200ms.
- [ ] Change is searchable.

### FR-3: Drives suggestions
- Goal sentence is sent to agents in plan generation.
- Goal sentence appears in Workspace switcher tooltip.

## 4. Non-functional requirements
- Persists across sessions and devices.

## 5. UI surfaces
- NX-UI-6001 (Home — in resume cards), NX-UI-6002 (Switcher), Workspace header.

## 6. Permissions
- Edit: workspace owner / editor.

## 7. Telemetry
- `workspace.goal_updated`

## 8. Failure modes
- Empty: not allowed.

## 9. Dependencies
- Memory Engine for context.

## 10. Out of scope
- Multi-sentence goals (use notes instead).

## 11. Acceptance criteria summary
- [ ] Required at creation.
- [ ] Editable inline.
- [ ] Searchable.

## 12. Open questions
- Q: Should goal be visible to team members only, or also to Marketplace agents?

## 13. Change log
| Date | Change | Author |
|------|--------|--------|
| 2026-06-30 | Initial spec | Frontend AI |

---

*End NX-FEAT-1103.*