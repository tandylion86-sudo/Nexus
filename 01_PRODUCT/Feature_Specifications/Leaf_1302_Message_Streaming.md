# NX-FEAT-1302 — Message Streaming (Token-by-Token)

| Field | Value |
|-------|-------|
| **Document ID** | NX-FEAT-1302 |
| **Title** | Message Streaming |
| **Area** | NX-FEAT-A0004 — AI Chat |
| **Owner** | Frontend AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P0 |
| **Estimated effort** | M |

---

## 1. Purpose
AI responses stream token-by-token for perceived speed.

## 2. Functional requirements
- First token within 500ms.
- No reflows mid-stream.
- Code blocks render monospace from token 1.

**Acceptance:**
- [ ] First token <500ms.
- [ ] No layout shift.

## 3. Out of scope
- Voice streaming (H2).

## 4. Acceptance criteria summary
- [ ] <500ms first token.

## 5. Change log
| Date | Change | Author |
|------|--------|--------|
| 2026-06-30 | Initial spec | Frontend AI |

---

*End NX-FEAT-1302.*