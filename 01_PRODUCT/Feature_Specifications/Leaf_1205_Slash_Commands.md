# NX-FEAT-1205 — Slash Commands

| Field | Value |
|-------|-------|
| **Document ID** | NX-FEAT-1205 |
| **Title** | Slash Commands |
| **Area** | NX-FEAT-A0003 — AI Command Bar |
| **Owner** | Frontend AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P1 |
| **Horizon target** | H1 |
| **Estimated effort** | S |

---

## 1. Purpose
Slash commands provide quick access to common actions without typing full intents.

## 2. User stories
- As Devin, I want `/summarize` to summarize the active tab.
- As Marcus, I want `/schedule` to open the schedule editor.

## 3. Functional requirements
### FR-1: Slash command set
- First-party: `/summarize`, `/research`, `/translate`, `/schedule`, `/workflow`, `/memory`, `/agents`, `/workspace`, `/cloud`, `/settings`, `/help`.
- User-defined slash commands (from saved workflows).

### FR-2: Discovery
- Type `/` → show list with descriptions.
- Tab to complete.

**Acceptance:**
- [ ] Slash command list <200ms.
- [ ] Tab completion works.

## 4. Non-functional requirements
- Consistent keyboard shortcuts.

## 5. UI surfaces
- Command bar suggestions.

## 6. Permissions
- Use: any user.

## 7. Telemetry
- `slash_command.used`

## 8. Failure modes
- Unknown slash: "No command matches. Try /help."

## 9. Dependencies
- None.

## 10. Out of scope
- Plugin-defined slash commands (H2).

## 11. Acceptance criteria summary
- [ ] 11+ first-party commands.
- [ ] User-defined from workflows.

## 12. Open questions
- Q: Should we ship a `/cheatsheet` modal?

## 13. Change log
| Date | Change | Author |
|------|--------|--------|
| 2026-06-30 | Initial spec | Frontend AI |

---

*End NX-FEAT-1205.*