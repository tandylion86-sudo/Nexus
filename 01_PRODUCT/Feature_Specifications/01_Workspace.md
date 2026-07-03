# NX-FEAT-1100 — Workspaces (Anchor Spec)

| Field | Value |
|-------|-------|
| **Document ID** | NX-FEAT-1100 |
| **Title** | Workspaces (Anchor Spec) |
| **Area** | NX-FEAT-A0002 — Workspaces |
| **Owner** | Frontend AI |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-06-30 |
| **Priority (H1)** | P0 |
| **Horizon target** | H1 |
| **Estimated effort** | XL (decomposed into NX-FEAT-1101-1110) |

---

## 1. Purpose

A **Workspace** is the primary unit of organization in NEXUS. It replaces the browser tab as the user's mental model for "what I'm working on." A Workspace bundles a goal, the relevant tabs, notes, files, agents, and memory into one persistent, shareable, goal-oriented container.

This document is the **anchor spec** for the Workspace feature area. It establishes the philosophy, the data model, and the cross-cutting concerns. Leaf features (NX-FEAT-1101 through 1110) inherit from this document.

## 2. Why Workspaces, not Tabs

Tabs are a low-level abstraction designed for static document viewing. They:

- Don't persist a goal — just a URL.
- Don't carry context — close a tab, lose your place.
- Don't scale beyond ~20 — beyond that, they're noise.
- Don't support collaboration natively.
- Don't have memory.

NEXUS is for goal-oriented work. The unit of organization must be **goal-oriented**, not URL-oriented.

## 3. User stories

- As **Maya**, I want to open NEXUS and immediately see "this week's content project" with everything I need, so I can resume without searching for tabs.
- As **Devin**, I want a "Coding: Feature X" Workspace that pulls together my PR, my test environments, my notes, and a research agent, so I don't context-switch.
- As **Sara**, I want a Workspace per investigation, with its own memory and source library, so each project has isolated context.
- As **Marcus**, I want to share a Workspace with my team so we work on the same dashboard.
- As **Riya**, I want to customize a Workspace per life-area (work, hobbies, learning) so they stay separate.
- As **Thea**, I want shared Workspaces with permissions so my team has appropriate access.

## 4. Functional requirements

### FR-1: Workspace creation
**Description:** A user creates a new Workspace by typing a goal sentence. The system proposes a name, optional icon, color, and template based on the goal.
**Acceptance:**
- [ ] User can create a Workspace from the home screen in ≤10 seconds.
- [ ] System proposes a name derived from the goal (e.g., "Research Acme Corp").
- [ ] User can override name, icon, color, template.
- [ ] Workspace is created and visible in the Workspace switcher within 1 second.

### FR-2: Workspace goal sentence
**Description:** Every Workspace has a single goal sentence that captures intent. The sentence is displayed prominently and editable.
**Acceptance:**
- [ ] Goal sentence is required at creation.
- [ ] Goal sentence is editable inline.
- [ ] Goal sentence is searchable (full-text).
- [ ] Goal sentence is shown in the Workspace switcher tooltip.

### FR-3: Workspace persistence
**Description:** A Workspace persists across sessions, devices, and restarts.
**Acceptance:**
- [ ] Closing NEXUS preserves all Workspace state.
- [ ] Crash recovery restores last-known state.
- [ ] Sync (if enabled) propagates Workspace state to other devices within 5 seconds.

### FR-4: Workspace memory isolation
**Description:** Each Workspace has its own memory scope. Memory from one Workspace is not automatically available to another (but can be explicitly granted).
**Acceptance:**
- [ ] Memory items have a `workspace_id` field.
- [ ] Agent memory queries default to the active Workspace's scope.
- [ ] User can mark a memory item as "cross-Workspace."
- [ ] Cross-Workspace memory can be filtered out.

### FR-5: Workspace notes and files
**Description:** Each Workspace has notes (rich text) and files (auto-organized).
**Acceptance:**
- [ ] Notes support Markdown with rich editing.
- [ ] Files dropped into a Workspace are stored and indexed.
- [ ] Notes and files are searchable across the Workspace.
- [ ] Files support text/image/PDF/CSV preview.

### FR-6: Workspace tabs (subordinate)
**Description:** Workspaces contain tabs, but tabs are subordinate. Closing a tab does not lose Workspace state.
**Acceptance:**
- [ ] Tabs exist within Workspaces.
- [ ] Closing all tabs does not remove the Workspace.
- [ ] Tab state is restored on next Workspace open.

### FR-7: Workspace templates
**Description:** Users can create Workspaces from templates (e.g., "Research," "Coding," "Marketing Campaign").
**Acceptance:**
- [ ] 10+ first-party templates ship at GA.
- [ ] Templates bundle: agents, default tabs, notes structure, memory schema.
- [ ] User can save any Workspace as a custom template.
- [ ] Marketplace allows template publishing (H2).

### FR-8: Workspace archive / delete
**Description:** Workspaces can be archived (hidden, recoverable) or deleted (irreversible).
**Acceptance:**
- [ ] Archive removes from switcher but preserves all data.
- [ ] Archive auto-deletes after 90 days (configurable).
- [ ] Delete requires confirmation and shows what will be lost.
- [ ] Delete is reversible for 30 days (soft delete).

### FR-9: Workspace search
**Description:** Users can search across all Workspaces (name, goal, notes, files).
**Acceptance:**
- [ ] Search bar opens with ⌘K / Ctrl-K.
- [ ] Results show Workspace name, snippet, last modified.
- [ ] Search is <500ms for users with ≤100 Workspaces.
- [ ] Filters: date range, has agent, has integration, archived.

### FR-10: Workspace sharing (team plans)
**Description:** Workspaces can be shared with team members with configurable permissions.
**Acceptance:**
- [ ] Owner can invite by email.
- [ ] Permissions: viewer / commenter / editor / admin.
- [ ] Shared Workspace appears in member's switcher.
- [ ] Activity log shows who changed what.

## 5. Non-functional requirements

### NFR-1: Performance
- Workspace switch: <200ms perceived.
- Search: <500ms for 100 Workspaces.
- Sync propagation: <5 seconds.
- Cold start with 50 Workspaces: <2 seconds added.

### NFR-2: Reliability
- Crash recovery: no Workspace data loss.
- Sync conflict resolution: deterministic, user-visible.
- 99.9% sync uptime.

### NFR-3: Security
- Workspace data encrypted at rest with user-specific key.
- Per-Workspace encryption option for sensitive Workspaces (e.g., financial).
- Sharing requires explicit permission; no implicit inheritance.

### NFR-4: Privacy
- A Workspace's memory is private by default.
- Memory export includes/excludes per-Workspace.
- Local-only mode: Workspaces are not synced.

### NFR-5: Accessibility
- Keyboard navigation across Workspace switcher.
- Screen reader labels for goal sentence, name, status.
- High-contrast theme support.

## 6. UI surfaces

| Surface | Reference |
|---------|-----------|
| Workspace switcher | NX-UI-6101 |
| Workspace create flow | NX-UI-6102 |
| Workspace detail view | NX-UI-6103 |
| Workspace settings | NX-UI-6104 |
| Workspace search | NX-UI-6105 |
| Workspace share dialog | NX-UI-6106 |
| Workspace archive/delete | NX-UI-6107 |

## 7. Permissions

Workspace features require:

- Read access to user's Workspace list.
- Write access to create / modify / delete a Workspace.
- For sharing: invite permission (workspace owner or admin).
- For cross-Workspace memory: explicit grant.

## 8. Telemetry

Events emitted (opt-in):

- `workspace.created`
- `workspace.opened`
- `workspace.switched`
- `workspace.shared`
- `workspace.archived`
- `workspace.deleted`
- `workspace.template.used`

Activity Log captures per-action details regardless of telemetry opt-in.

## 9. Failure modes

| Failure | Behavior |
|---------|----------|
| Sync conflict | Show conflict resolution UI; default to last-write-wins |
| Disk full | Warn user; auto-archive inactive Workspaces |
| Service unavailable | Workspace works locally; sync resumes later |
| Sharing recipient not found | Email bounce notification to inviter |
| Corrupt Workspace data | Recoverable from backup; user warned |

## 10. Dependencies

- Memory Engine (NX-FEAT-A0008) for per-Workspace memory.
- Sync engine (NX-FEAT-2005) for multi-device.
- Permission system (NX-FEAT-A0012) for sharing.
- Activity Log (NX-FEAT-A0013) for audit.

## 11. Out of scope

- Real-time collaborative editing (H2).
- Workspace-as-deployment-unit (H2 — for "NEXUS Apps").
- Nested Workspaces (deferred indefinitely).
- Workspace-level subscriptions (H2).

## 12. Acceptance criteria summary

The Workspace feature is done when:

- [ ] A new user can create and use 3 Workspaces within 5 minutes.
- [ ] Workspace state survives a crash.
- [ ] Memory is isolated per Workspace by default.
- [ ] Search across 100 Workspaces returns in <500ms.
- [ ] Sync propagates a Workspace to a second device within 5 seconds.
- [ ] Sharing works for at least 3 permission levels.
- [ ] WCAG 2.2 AA compliance for all Workspace UIs.

## 13. Sub-features (leaf specs)

| ID | Name |
|----|------|
| NX-FEAT-1101 | Create Workspace |
| NX-FEAT-1102 | Switch between Workspaces |
| NX-FEAT-1103 | Workspace goal sentence |
| NX-FEAT-1104 | Workspace notes |
| NX-FEAT-1105 | Workspace files |
| NX-FEAT-1106 | Workspace memory |
| NX-FEAT-1107 | Workspace templates |
| NX-FEAT-1108 | Archive / delete Workspace |
| NX-FEAT-1109 | Workspace search |
| NX-FEAT-1110 | Workspace sharing |

Each leaf feature inherits from this anchor spec and adds leaf-specific detail.

## 14. Open questions

- Q: Should cross-Workspace memory be opt-in per item, or opt-out per Workspace?
- Q: Should Workspaces support guest access (no account required)?
- Q: Should we allow nested Workspaces for power users?
- Q: How aggressive should auto-archiving be for inactive Workspaces?

## 15. Change log

| Date | Change | Author |
|------|--------|--------|
| 2026-06-30 | Initial anchor spec | Frontend AI |

---

*End NX-FEAT-1100.*