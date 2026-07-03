# NX-FEAT-1209 — Command Cancellation

| Field | Value |
|-------|-------|
| **Document ID** | NX-FEAT-1209 |
| **Title** | Command Cancellation |
| **Area** | NX-FEAT-A0003 — AI Command Bar |
| **Owner** | Frontend AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P0 |
| **Horizon target** | H1 |
| **Estimated effort** | S |

---

## 1. Purpose
Users can cancel an in-flight command at any time.

## 2. User stories
- As Marcus, I want to stop a workflow that is doing the wrong thing.

## 3. Functional requirements
### FR-1: Cancel button
- Visible during execution.
- Click stops all pending steps.

### FR-2: Confirmation
- For partial-execution: confirm "Cancel? Steps already done will remain."

**Acceptance:**
- [ ] Cancel halts within 1s.
- [ ] Completed steps preserved.
- [ ] Activity Log records cancellation.

## 4. Non-functional requirements
- Latency: <1s to halt.

## 5. UI surfaces
- Command bar.

## 6. Permissions
- Cancel: user who initiated.

## 7. Telemetry
- `command.cancelled`

## 8. Failure modes
- Step cannot be cancelled: continues, then reports.

## 9. Dependencies
- Orchestrator cancel API.

## 10. Out of scope
- None.

## 11. Acceptance criteria summary
- [ ] <1s halt.
- [ ] Completed preserved.

## 12. Open questions
- Q: Should we offer "rollback" for some completed steps?

## 13. Change log
| Date | Change | Author |
|------|--------|--------|
| 2026-06-30 | Initial spec | Frontend AI |

---

*End NX-FEAT-1209.*