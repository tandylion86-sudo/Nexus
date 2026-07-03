# NX-FEAT-1101 — Create Workspace

| Field | Value |
|-------|-------|
| **Document ID** | NX-FEAT-1101 |
| **Title** | Create Workspace |
| **Area** | NX-FEAT-A0002 — Workspaces |
| **Category** | Workspace lifecycle |
| **Owner** | Frontend AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P0 |
| **Horizon target** | H1 |
| **Estimated effort** | M |

---

## 1. Purpose
A user creates a new Workspace. The act is fast, low-friction, and immediately usable.

## 2. User stories
- As any user, I want to create a Workspace in under 10 seconds.
- As Maya, I want NEXUS to suggest a name based on my goal.

## 3. Functional requirements
### FR-1: Inline creation
- Triggered from home screen, Workspace switcher, or "+" button.
- Form: name (auto-suggested), goal sentence, color, icon, optional template.
- Single screen, ≤3 fields visible.
- Submit creates and switches.

**Acceptance:**
- [ ] Form auto-fills name from goal.
- [ ] Goal is required.
- [ ] Creation completes in <1 second.
- [ ] Workspace is immediately active.

### FR-2: Template picker
- User can pick from 10+ first-party templates.
- Each template pre-fills agents, default tabs, and notes structure.
- Templates include: Research, Coding, Marketing, Operations, Personal, etc.

**Acceptance:**
- [ ] Template preview shows contents.
- [ ] User can save any Workspace as a custom template.

## 4. Non-functional requirements
- Performance: <1s creation.
- Reliability: durable; no orphan Workspaces.

## 5. UI surfaces
- NX-UI-6001 (Home), NX-UI-6002 (Switcher), inline modal.

## 6. Permissions
- Create: any signed-in user.
- Limit: ≤100 Workspaces per user (free); 500 (Pro); unlimited (Business+).

## 7. Telemetry
- `workspace.created`
- `workspace.template_used`

## 8. Failure modes
- Limit reached: "You've hit the [N] workspace limit. Upgrade or archive some."
- Network error: creation queued locally; retry.

## 9. Dependencies
- NX-FEAT-1103 (goal sentence)
- NX-FEAT-1107 (templates)

## 10. Out of scope
- Workspace sharing (separate leaf NX-FEAT-1110).

## 11. Acceptance criteria summary
- [ ] Creation flow under 10 seconds.
- [ ] Form validates goal sentence.
- [ ] Templates apply correctly.

## 12. Open questions
- Q: Should we allow "blank" templates (no agents, no notes)?
- Q: Should templates be copy-on-use or share state?

## 13. Change log
| Date | Change | Author |
|------|--------|--------|
| 2026-06-30 | Initial spec | Frontend AI |

---

*End NX-FEAT-1101.*