# NX-FEAT-1203 — Plan Display

| Field | Value |
|-------|-------|
| **Document ID** | NX-FEAT-1203 |
| **Title** | Plan Display |
| **Area** | NX-FEAT-A0003 — AI Command Bar |
| **Owner** | Frontend AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P0 |
| **Horizon target** | H1 |
| **Estimated effort** | M |

---

## 1. Purpose
Plans generated from intents are shown before execution, with approval gating and live status updates.

## 2. User stories
- As Marcus, I want to see what an agent will do before it does it.
- As Riya, I want to cancel a plan mid-execution.

## 3. Functional requirements
### FR-1: Plan visualization
- Numbered steps with descriptions.
- Agent badges.
- Status icons (pending / running / done / error).
- Streaming updates.

### FR-2: Approval
- Each step lists required permissions.
- User can approve / deny each.
- Default: approve all (with revoke later).

### FR-3: Edit plan
- User can edit step descriptions inline.
- Re-plan button regenerates.

**Acceptance:**
- [ ] Plan visible within 3s of intent.
- [ ] Edit saves within 200ms.
- [ ] Re-plan regenerates in <3s.

## 4. Non-functional requirements
- Update latency: <100ms per state change.

## 5. UI surfaces
- NX-UI-6003 (Command Bar).

## 6. Permissions
- Edit: user.
- Approve: user.

## 7. Telemetry
- `plan.displayed`
- `plan.approved`
- `plan.edited`
- `plan.replanned`

## 8. Failure modes
- Step failure: error inline.
- Permission denied: re-prompt.

## 9. Dependencies
- NX-FEAT-1202 (parser).

## 10. Out of scope
- Branching plans (H2).

## 11. Acceptance criteria summary
- [ ] Live updates.
- [ ] Edit / re-plan works.

## 12. Open questions
- Q: Should the plan show estimated time?

## 13. Change log
| Date | Change | Author |
|------|--------|--------|
| 2026-06-30 | Initial spec | Frontend AI |

---

*End NX-FEAT-1203.*