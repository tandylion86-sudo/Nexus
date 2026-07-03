# NX-FEAT-1204 — Command History

| Field | Value |
|-------|-------|
| **Document ID** | NX-FEAT-1204 |
| **Title** | Command History |
| **Area** | NX-FEAT-A0003 — AI Command Bar |
| **Owner** | Frontend AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P1 |
| **Horizon target** | H1 |
| **Estimated effort** | S |

---

## 1. Purpose
Users can search and re-run past commands. History is searchable, filterable, and persists across devices.

## 2. User stories
- As Maya, I want to find yesterday's command.
- As Devin, I want to re-run a workflow that worked.

## 3. Functional requirements
### FR-1: History list
- All commands (intent, plan, agents used, status).
- Sortable by recency.
- Searchable by intent text.

### FR-2: Re-run
- Click command → opens in command bar with same intent.
- Or "Run again" button.

**Acceptance:**
- [ ] History loads <500ms for 1,000 commands.
- [ ] Search filters live.

## 4. Non-functional requirements
- Stored: per-user, encrypted.

## 5. UI surfaces
- Command bar suggestions; dedicated history panel.

## 6. Permissions
- View: own history.

## 7. Telemetry
- `command_history.viewed`
- `command_history.rerun`

## 8. Failure modes
- Storage full: oldest pruned (configurable).

## 9. Dependencies
- Backend storage.

## 10. Out of scope
- Cross-user history (H2).

## 11. Acceptance criteria summary
- [ ] Search <500ms.
- [ ] Re-run works.

## 12. Open questions
- Q: Should re-run include the original Workspace context?

## 13. Change log
| Date | Change | Author |
|------|--------|--------|
| 2026-06-30 | Initial spec | Frontend AI |

---

*End NX-FEAT-1204.*