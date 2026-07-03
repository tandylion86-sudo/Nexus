# NX-FEAT-1108 — Archive / Delete Workspace

| Field | Value |
|-------|-------|
| **Document ID** | NX-FEAT-1108 |
| **Title** | Archive / Delete Workspace |
| **Area** | NX-FEAT-A0002 — Workspaces |
| **Owner** | Frontend AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P1 |
| **Horizon target** | H1 |
| **Estimated effort** | S |

---

## 1. Purpose
Users archive Workspaces they no longer actively use, or delete them permanently. Both operations are reversible for a window.

## 2. User stories
- As Maya, I want to archive a completed campaign but keep the data.
- As Marcus, I want to delete a test Workspace.

## 3. Functional requirements
### FR-1: Archive
- Removes from switcher, search, and dashboard.
- Data preserved.
- 90-day auto-delete (configurable).

**Acceptance:**
- [ ] Archive is reversible from archived list.
- [ ] Search excludes archived by default.

### FR-2: Delete
- Soft delete: 30-day window.
- After 30 days, hard delete.

**Acceptance:**
- [ ] Confirm dialog names what will be lost.
- [ ] Restore available for 30 days.

## 4. Non-functional requirements
- Archive: <1s.
- Delete (soft): <2s.
- Hard delete (background): durable.

## 5. UI surfaces
- Workspace settings; archived list view.

## 6. Permissions
- Archive: owner / admin.
- Delete: owner only.

## 7. Telemetry
- `workspace.archived`
- `workspace.deleted`
- `workspace.restored`

## 8. Failure modes
- Active agents in Workspace: warn before delete.
- Shared Workspace: confirm with all members.

## 9. Dependencies
- Soft delete infrastructure.

## 10. Out of scope
- Bulk archive / delete (H2).

## 11. Acceptance criteria summary
- [ ] Archive reversible.
- [ ] Delete with 30-day restore window.

## 12. Open questions
- Q: Default auto-delete period (30 / 60 / 90 days)?

## 13. Change log
| Date | Change | Author |
|------|--------|--------|
| 2026-06-30 | Initial spec | Frontend AI |

---

*End NX-FEAT-1108.*