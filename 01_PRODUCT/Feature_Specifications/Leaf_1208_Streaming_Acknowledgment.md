# NX-FEAT-1208 — Streaming Acknowledgment (<500ms)

| Field | Value |
|-------|-------|
| **Document ID** | NX-FEAT-1208 |
| **Title** | Streaming Acknowledgment |
| **Area** | NX-FEAT-A0003 — AI Command Bar |
| **Owner** | Frontend AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P0 |
| **Horizon target** | H1 |
| **Estimated effort** | S |

---

## 1. Purpose
Once the user submits an intent, NEXUS acknowledges within 500ms with a streaming indicator.

## 2. User stories
- As Maya, I want to know NEXUS is working immediately.

## 3. Functional requirements
### FR-1: Immediate acknowledgment
- ≤500ms after submit: show "Planning…"
- Streaming acknowledgment text: "I'll think through this."

### FR-2: Indicator
- Below prompt: shimmering bar or animated dots.
- Disappears when plan is ready.

**Acceptance:**
- [ ] First acknowledgment pixel <500ms.

## 4. Non-functional requirements
- Perceived latency budget: 500ms.

## 5. UI surfaces
- Command bar.

## 6. Permissions
- None.

## 7. Telemetry
- `intent.acknowledged`

## 8. Failure modes
- Slow network: still shows local acknowledgment.

## 9. Dependencies
- None.

## 10. Out of scope
- None.

## 11. Acceptance criteria summary
- [ ] <500ms acknowledgment.
- [ ] Streaming indicator visible.

## 12. Open questions
- Q: Should the acknowledgment be customizable?

## 13. Change log
| Date | Change | Author |
|------|--------|--------|
| 2026-06-30 | Initial spec | Frontend AI |

---

*End NX-FEAT-1208.*