# NX-FEAT-1202 — Natural Language Intent Parser

| Field | Value |
|-------|-------|
| **Document ID** | NX-FEAT-1202 |
| **Title** | Natural Language Intent Parser |
| **Area** | NX-FEAT-A0003 — AI Command Bar |
| **Owner** | AI Platform AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P0 |
| **Horizon target** | H1 |
| **Estimated effort** | L |

---

## 1. Purpose
The parser converts a natural-language intent into a structured plan that the orchestrator can dispatch.

## 2. User stories
- As Maya, I want to type "Apply to 12 jobs matching my profile" and have it understood.
- As Sara, I want "Build a dossier on Acme Corp" parsed into research steps.

## 3. Functional requirements
### FR-1: Intent classification
- Detect intent category (research, automation, content, communication, etc.).
- Detect target entity.
- Detect scope and constraints.

### FR-2: Plan generation
- Convert intent into ordered steps.
- Each step: action, agent, parameters.
- Streaming plan with confidence per step.

### FR-3: Fallback
- If confidence low: ask clarifying question.
- If no agent can fulfill: explain and suggest alternatives.

**Acceptance:**
- [ ] Plan generated <3s for typical intents.
- [ ] Confidence reported per step.

## 4. Non-functional requirements
- Performance: <3s p95.
- Cost: within model budget.

## 5. UI surfaces
- NX-UI-6003 (Command Bar — Plan viewer).

## 6. Permissions
- Trigger: any user.
- Plan execution: requires plan permissions.

## 7. Telemetry
- `intent.parsed`
- `plan.generated`
- `clarification.asked`

## 8. Failure modes
- Low confidence: clarification.
- Model failure: retry, then fall back to URL escape hatch.

## 9. Dependencies
- Model gateway.
- Agent registry.

## 10. Out of scope
- Voice intent (H2).
- Multi-modal intent (H2).

## 11. Acceptance criteria summary
- [ ] <3s plan generation.
- [ ] Confidence per step.

## 12. Open questions
- Q: How do we evaluate parser quality systematically?

## 13. Change log
| Date | Change | Author |
|------|--------|--------|
| 2026-06-30 | Initial spec | AI Platform AI |

---

*End NX-FEAT-1202.*