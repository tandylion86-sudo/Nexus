# NX-FEAT-1107 — Workspace Templates

| Field | Value |
|-------|-------|
| **Document ID** | NX-FEAT-1107 |
| **Title** | Workspace Templates |
| **Area** | NX-FEAT-A0002 — Workspaces |
| **Owner** | Product AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P1 |
| **Horizon target** | H1 |
| **Estimated effort** | M |

---

## 1. Purpose
Users create Workspaces from pre-built templates or save custom templates for reuse.

## 2. User stories
- As Maya, I want to start from a "Marketing Campaign" template instead of building one.
- As Riya, I want to share a template with my team.

## 3. Functional requirements
### FR-1: First-party templates
- 10+ templates ship at GA.
- Categories: Research, Coding, Marketing, Operations, Personal, Security, etc.

### FR-2: Template contents
- Pre-installed agents.
- Default tabs (URLs).
- Notes structure.
- Memory schema.

### FR-3: Custom templates
- Save any Workspace as a template.
- Templates are copies; do not auto-link.

### FR-4: Template sharing
- Team plans: shared templates (H2).

## 4. Non-functional requirements
- Templates load <500ms.
- Apply template <2 seconds.

## 5. UI surfaces
- NX-UI-6002 (Switcher); Workspace creation modal.

## 6. Permissions
- Create from first-party: any user.
- Custom templates: workspace owner.
- Share template: workspace owner + plan-eligible.

## 7. Telemetry
- `template.used`
- `template.saved`

## 8. Failure modes
- Template references missing agent: install prompt.

## 9. Dependencies
- NX-FEAT-1501 (Marketplace) for template distribution.

## 10. Out of scope
- Marketplace-published templates (H2).

## 11. Acceptance criteria summary
- [ ] 10+ first-party templates.
- [ ] Custom template save/load.
- [ ] Apply template in <2 seconds.

## 12. Open questions
- Q: Should templates include scheduled workflows?

## 13. Change log
| Date | Change | Author |
|------|--------|--------|
| 2026-06-30 | Initial spec | Product AI |

---

*End NX-FEAT-1107.*