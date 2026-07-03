# NX-FEAT-1206 — Quick Actions (Suggested Next)

| Field | Value |
|-------|-------|
| **Document ID** | NX-FEAT-1206 |
| **Title** | Quick Actions (Suggested Next) |
| **Area** | NX-FEAT-A0003 — AI Command Bar |
| **Owner** | AI Platform AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P1 |
| **Horizon target** | H1 |
| **Estimated effort** | M |

---

## 1. Purpose
NEXUS proactively suggests the next likely action based on context, recency, and user patterns.

## 2. User stories
- As Maya, I want NEXUS to suggest the next step.
- As Devin, I want one-click resume of recurring work.

## 3. Functional requirements
### FR-1: Suggestion engine
- Considers: current Workspace, recent actions, time of day, day of week.
- Top 3 suggestions surfaced.

### FR-2: Surface points
- Home screen.
- Command bar empty state.
- Workspace header.

**Acceptance:**
- [ ] Suggestions adapt to context.
- [ ] User can dismiss permanently.

## 4. Non-functional requirements
- Performance: <200ms.

## 5. UI surfaces
- NX-UI-6001 (Home), command bar.

## 6. Permissions
- View: any user.
- Disable: per-type opt-out.

## 7. Telemetry
- `suggestion.shown`
- `suggestion.clicked`
- `suggestion.dismissed`

## 8. Failure modes
- Poor suggestion: not clicked → ranking adjusts.

## 9. Dependencies
- Memory Engine.
- Activity Log.

## 10. Out of scope
- AI-generated suggestions beyond pre-computed (H2).

## 11. Acceptance criteria summary
- [ ] <200ms.
- [ ] Per-type opt-out.

## 12. Open questions
- Q: Should suggestions be A/B tested?

## 13. Change log
| Date | Change | Author |
|------|--------|--------|
| 2026-06-30 | Initial spec | AI Platform AI |

---

*End NX-FEAT-1206.*