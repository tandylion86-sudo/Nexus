# NX-FEAT-1403 — Tool Dispatcher

| Field | Value |
|-------|-------|
| **Document ID** | NX-FEAT-1403 |
| **Title** | Tool Dispatcher |
| **Area** | NX-FEAT-A0005 — Agent Orchestrator |
| **Owner** | Backend AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P0 |
| **Estimated effort** | L |

---

## 1. Purpose
Routes tool calls from agents to the right implementation (browser, file, API, model).

## 2. Functional requirements
- Tool registry.
- Permission check before invocation.
- Result typing.
- Error normalization.

**Acceptance:**
- [ ] All agent tools registered.
- [ ] Permission denials returned cleanly.

## 3. Acceptance criteria summary
- [ ] Tool dispatch works.

## 4. Change log
| Date | Change | Author |
|------|--------|--------|
| 2026-06-30 | Initial spec | Backend AI |

---

*End NX-FEAT-1403.*