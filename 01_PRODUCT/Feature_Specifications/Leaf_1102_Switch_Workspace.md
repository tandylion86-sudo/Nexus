# NX-FEAT-1102 — Switch Between Workspaces

| Field | Value |
|-------|-------|
| **Document ID** | NX-FEAT-1102 |
| **Title** | Switch Between Workspaces |
| **Area** | NX-FEAT-A0002 — Workspaces |
| **Owner** | Frontend AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P0 |
| **Horizon target** | H1 |
| **Estimated effort** | M |

---

## 1. Purpose
A user navigates from one Workspace to another. Switching is fast, preserves state, and is reachable from any screen.

## 2. User stories
- As any user, I want to switch Workspaces in under 1 second.
- As Devin, I want keyboard shortcuts for fast switching.

## 3. Functional requirements
### FR-1: Switcher UI
- Triggered by ⌘Tab / Ctrl+Tab or sidebar click.
- Lists recently-active + all Workspaces.
- Search filters.

**Acceptance:**
- [ ] Modal opens <100ms.
- [ ] Search filters live (<100ms).
- [ ] Switch happens in <200ms perceived.

### FR-2: Keyboard shortcuts
- ⌘Tab / Ctrl+Tab opens switcher.
- ⌘1..9 / Ctrl+1..9 jumps to Nth recent.
- ⌘K opens command palette (alternate path).

**Acceptance:**
- [ ] All shortcuts work without conflict.
- [ ] Shortcuts configurable in Settings.

## 4. Non-functional requirements
- Perceived latency: <200ms.
- Animation: 160ms (per NX-DS-5006).

## 5. UI surfaces
- NX-UI-6002 (Switcher), top-bar Workspace chip.

## 6. Permissions
- Switch: any user with access.

## 7. Telemetry
- `workspace.switched`
- `workspace_switcher.opened`

## 8. Failure modes
- Sync conflict: last-write-wins with toast.
- Workspace deleted while open: redirect to home.

## 9. Dependencies
- NX-FEAT-1109 (search)
- NX-FEAT-2005 (sync)

## 10. Out of scope
- Drag-and-drop reorder of Workspaces (P3).

## 11. Acceptance criteria summary
- [ ] Switch within 1 second.
- [ ] Keyboard nav full.

## 12. Open questions
- Q: Should ⌘Tab cycle or always open switcher?

## 13. Change log
| Date | Change | Author |
|------|--------|--------|
| 2026-06-30 | Initial spec | Frontend AI |

---

*End NX-FEAT-1102.*