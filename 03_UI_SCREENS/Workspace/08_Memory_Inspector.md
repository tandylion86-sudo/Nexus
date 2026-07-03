# NX-UI-6008 — Memory Inspector

| Field | Value |
|-------|-------|
| **Document ID** | NX-UI-6008 |
| **Screen** | Memory Inspector |
| **Owner** | Frontend AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P0 |
| **Touches journeys** | J-03, J-13 |
| **Touches features** | NX-FEAT-1701-1714 |

---

## 1. Purpose

The Memory Inspector is the **transparency surface** for the Memory Engine. Users see exactly what NEXUS remembers, edit, delete, and export memory items. Trust is built by visibility.

## 2. When shown

- Triggered by Memory icon in sidebar.
- Triggered by ⌘⇧M / Ctrl+Shift+M.
- Triggered by "What do you remember about me?" in command palette.

## 3. Layout

```
┌────────────────────────────────────────────────────────────────┐
│  Memory                                              [Export]   │
├──────────────┬─────────────────────────────────────────────────┤
│  Types       │  🔍 Search memory...                              │
│              │                                                   │
│  ▸ Preferenc.│  All memory (1,247 items)                         │
│  ▸ Project   │                                                   │
│  ▸ Conversat.│  ┌──────────────────────────────────────────┐   │
│  ▸ Style     │  │ 🟦 Preference · 2d ago                     │   │
│  ▸ Knowledge │  │ Tone: Casual                               │   │
│  ▸ Documents │  │ Source: Chat, Acme Corp research           │   │
│              │  │ Scope: Workspace                           │   │
│  Workspaces  │  │ [Edit]  [Delete]  [Make global]            │   │
│  ▸ Acme Corp │  └──────────────────────────────────────────┘   │
│  ▸ Q4 Market │                                                   │
│  ▸ Coding X  │  ┌──────────────────────────────────────────┐   │
│  ▸ Personal  │  │ 🟨 Project fact · 5d ago                   │   │
│              │  │ Acme Corp raised list price 12% on Mar 3    │   │
│  Date range  │  │ Source: Web research, citation [1]         │   │
│  ▸ Last 7d   │  │ Scope: Acme Corp research                 │   │
│  ▸ Last 30d  │  │ Confidence: high                           │   │
│  ▸ All time  │  │ [Edit]  [Delete]  [Show source]            │   │
│              │  └──────────────────────────────────────────┘   │
│              │                                                   │
│              │  ┌──────────────────────────────────────────┐   │
│              │  │ 🟪 Style · 1w ago                         │   │
│              │  │ Profile: prefers short paragraphs          │   │
│              │  │ Source: 5 sample analyses                 │   │
│              │  │ Scope: Global                             │   │
│              │  │ [Edit]  [Delete]                           │   │
│              │  └──────────────────────────────────────────┘   │
└──────────────┴─────────────────────────────────────────────────┘
```

## 4. Component anatomy

### Sidebar (240px)
- **Types**: Preference, Project fact, Conversation summary, Style, Knowledge graph, Document.
- **Workspaces**: list of Workspaces with memory counts.
- **Date range**: 7d / 30d / All.

### Search bar (top)
- Live search across all memory.

### Memory item card
- Type indicator (color dot + type label).
- Timestamp (relative).
- Content (2–3 line preview; expandable).
- Source (where the fact came from).
- Scope (Workspace / Global).
- Confidence (high / medium / low; for inferences).
- Actions: Edit, Delete, Make global (if scoped), Show source.

### Export button
- Triggers memory export (per NX-FEAT-1707).

## 5. Interactions

| Trigger | Action |
|---------|--------|
| Click type / workspace / range | Filter |
| Type in search | Live filter |
| Click "Edit" | Inline edit |
| Click "Delete" | Confirm then remove |
| Click "Make global" | Promote scope |
| Click "Show source" | Open source link / conversation |

## 6. States

### Default
- All memory listed, sorted by recency.

### Loading
- Skeleton cards (5 × 100px).

### Filtered
- Filter chips show active filters.
- "Clear filters" button.

### Empty results
- "No memory matches."

### Empty (zero memory)
- "NEXUS hasn't remembered anything yet. As you work, important facts will appear here."

### Editing
- Card becomes editable.
- Save / cancel buttons.

### Confirming delete
- Modal: "Delete this memory? This cannot be undone."

## 7. Animation

- Cards stagger 30ms on load.
- Edit transition: 160ms fade.
- Delete: fade-out 200ms then list collapses.
- Reduced-motion: instant.

## 8. Accessibility

- Each card has full accessible label: type, content preview, source, scope.
- Filters are buttons with toggle state.
- Edit / delete announced.
- Full keyboard nav.

## 9. Telemetry

- `memory_inspector.opened`
- `memory.filtered`
- `memory.edited`
- `memory.deleted`
- `memory.exported`

Activity Log captures all memory edits.

## 10. Out of scope

- Knowledge graph visualization (separate screen — H2).
- Bulk operations (H2).

## 11. Acceptance criteria

- [ ] List loads in <500ms for 1,000 items.
- [ ] Edit save within 200ms.
- [ ] Delete confirm prevents accidents.
- [ ] Export works for all memory types.

## 12. Reading list

- **Memory Engine Anchor** — NX-FEAT-1700
- **Privacy** — NX-DOC-0004 P4

---

*End NX-UI-6008.*