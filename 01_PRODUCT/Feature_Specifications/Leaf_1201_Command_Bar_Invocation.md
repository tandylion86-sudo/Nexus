# NX-FEAT-1201 — Command Bar Invocation

| Field | Value |
|-------|-------|
| **Document ID** | NX-FEAT-1201 |
| **Title** | Command Bar Invocation |
| **Area** | NX-FEAT-A0003 — AI Command Bar |
| **Owner** | Frontend AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P0 |
| **Horizon target** | H1 |
| **Estimated effort** | S |

---

## 1. Purpose
Global keyboard shortcut opens the AI Command Bar from any screen.

## 2. User stories
- As Devin, I want to invoke the command bar without leaving my keyboard.

## 3. Functional requirements
### FR-1: Global hotkey
- Default: ⌘K (macOS), Ctrl+K (Windows/Linux).
- Alternative: ⌘L / Ctrl+L.
- Configurable in Settings.

**Acceptance:**
- [ ] Hotkey works from any surface.
- [ ] Bar opens within 100ms.

### FR-2: Visual feedback
- Scrim dims background.
- Bar slides in (160ms).

## 4. Non-functional requirements
- Hotkey intercepts at the lowest level to avoid focus issues.

## 5. UI surfaces
- NX-UI-6003 (Command Bar).

## 6. Permissions
- Trigger: any user.

## 7. Telemetry
- `command_bar.invoked`

## 8. Failure modes
- Hotkey conflict with system: configurable.

## 9. Dependencies
- None.

## 10. Out of scope
- Custom per-user shortcuts (deferred).

## 11. Acceptance criteria summary
- [ ] Opens <100ms.
- [ ] Configurable.

## 12. Open questions
- Q: Should ⌘Space also be supported (Spotlight-like)?

## 13. Change log
| Date | Change | Author |
|------|--------|--------|
| 2026-06-30 | Initial spec | Frontend AI |

---

*End NX-FEAT-1201.*