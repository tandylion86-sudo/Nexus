# NX-UI-6002 — Workspace Switcher

| Field | Value |
|-------|-------|
| **Document ID** | NX-UI-6002 |
| **Screen** | Workspace Switcher |
| **Owner** | Frontend AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P0 |
| **Touches journeys** | J-07, J-13 |
| **Touches features** | NX-FEAT-1101-1110, NX-FEAT-1109 |

---

## 1. Purpose

The Workspace Switcher lets users navigate between Workspaces, see what's running, and create new ones. It is reachable from any screen via ⌘/Ctrl+Tab and is the second-most-frequent action after the home prompt.

## 2. When shown

- Triggered by ⌘+Tab / Ctrl+Tab (configurable).
- Triggered by clicking the Workspace chip in the top bar.
- Triggered by typing `/ws` in the command palette.

## 3. Layout

```
┌──────────────────────────────────────────────────────────────┐
│  Switch workspace                                              │
│  ┌──────────────────────────────────────────────────────┐    │
│  │ 🔍  Search workspaces...                              │    │
│  └──────────────────────────────────────────────────────┘    │
│                                                                  │
│  Recently active                                                │
│  ●  Acme Corp research                           Maya · 2h     │
│  ●  Q4 Market Map                                Maya · 1d     │
│  ●  Coding: Feature X                            Maya · 3d     │
│                                                                  │
│  All workspaces                                                 │
│  ◐  Daily Briefing                              Solo · 5d ago   │
│  ○  Personal: Reading                            Solo · 1w ago  │
│  ○  Marketing: Q4 Campaign                       Solo · 2w ago  │
│                                                                  │
│  + Create new workspace                                          │
└──────────────────────────────────────────────────────────────┘
```

A 480px-wide modal centered horizontally, anchored to top bar.

## 4. Component anatomy

### Search input
- 44px tall, autofocus on open.
- Filters workspaces by name, goal, or notes.
- Live results.

### Section: Recently active (max 4)
- Bullet indicator (`●`) for active.
- Empty dot (`○`) for inactive.
- Name (semibold), member (Solo / Team / shared with…), last activity relative.

### Section: All workspaces
- Same row pattern.
- Sorted by last activity, descending.
- Virtualized for >100 workspaces.

### Footer: Create new workspace
- Full-width button row.
- "+ Create new workspace" → opens inline creation flow.

## 5. Interactions

| Trigger | Action |
|---------|--------|
| Click row | Switch to workspace, close modal |
| Click "+ Create new" | Inline creation form appears |
| Type in search | Live filter |
| ↑ / ↓ | Move selection |
| Enter | Open selected workspace |
| Esc | Close modal |
| Tab | Move to next section |
| ⌘N | Create new workspace (from inside switcher) |

## 6. States

### Default
- Recently active populated.
- Search empty.

### Loading
- Skeleton rows (5 rows × 44px).

### Search results
- Sections replaced with filtered list.
- Empty result: "No workspaces match '[query]'. Try a different search."

### Inline creation
- Form replaces the list temporarily.
- Fields: name, goal sentence, template picker.
- "Create" button creates and switches.

### Empty (no workspaces)
- Replace list with illustration + "Create your first workspace."

## 7. Animation

- Modal: scale-in 160ms, scrim fades 160ms.
- Row hover: subtle background 80ms.
- Section transition: fade 160ms.
- Filtered list updates: items cross-fade 80ms.
- Reduced-motion: no scale, instant fade.

## 8. Accessibility

- `role="dialog"` with `aria-label="Switch workspace"`.
- Search input has label.
- List rows have `aria-selected` state.
- Active workspace announced.
- Keyboard navigation full.
- Focus trap inside modal.
- Esc closes and returns focus to opener.

## 9. Telemetry

- `workspace_switcher.opened`
- `workspace_switcher.searched`
- `workspace_switcher.switched`
- `workspace_switcher.created`

Activity Log captures the switch action.

## 10. Out of scope

- Workspace settings (handled in NX-UI-6009).
- Sharing (handled in NX-UI-6002 sub-screen).

## 11. Acceptance criteria

- [ ] Modal opens within 100ms of ⌘Tab.
- [ ] Search filters live (<100ms).
- [ ] Up to 100 workspaces render smoothly.
- [ ] Inline creation completes in ≤10 seconds.
- [ ] Esc returns focus to opener.

## 12. Reading list

- **Workspace Anchor** — NX-FEAT-1100
- **Home Screen** — NX-UI-6001

---

*End NX-UI-6002.*