# NX-UI-6007 — Visual Workflow Builder

| Field | Value |
|-------|-------|
| **Document ID** | NX-UI-6007 |
| **Screen** | Visual Workflow Builder |
| **Owner** | Frontend AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P1 |
| **Touches journeys** | J-04, J-11, J-12, J-14 |
| **Touches features** | NX-FEAT-1801-1812 |

---

## 1. Purpose

The Visual Workflow Builder is the **drag-and-drop canvas** for composing automations. Users drag blocks from a palette, connect them, configure parameters, and run.

## 2. When shown

- Triggered by Workflow Builder icon in sidebar.
- Triggered by opening a workflow file.
- Triggered by "Create workflow" CTA in Workflows panel.

## 3. Layout

```
┌────────────────────────────────────────────────────────────────────────┐
│ Price Monitor v3                              [Test] [Save] [Run ▶] [⋯]│
├──────────────┬─────────────────────────────────────────┬──────────────┤
│  Blocks      │  ┌────────┐                              │ Config        │
│              │  │ Schedule│                              │               │
│  ▸ Triggers  │  │ every   │                              │ Selected:    │
│  ▸ Browser   │  │  1h     │                              │  HTTP GET    │
│  ▸ HTTP      │  └────┬───┘                              │               │
│  ▸ Transform │       │                                   │ URL          │
│  ▸ Logic     │       ▼                                   │ [https://...]│
│  ▸ AI        │  ┌────────┐                              │               │
│  ▸ Messaging │  │ HTTP   │                              │ Method        │
│              │  │ GET    │                              │ [GET ▾]       │
│              │  └────┬───┘                              │               │
│              │       │                                   │ Headers       │
│              │       ▼                                   │ [+ Add]       │
│              │  ┌────────┐                              │               │
│              │  │Extract │                              │ Body          │
│              │  │ price  │                              │ [            ]│
│              │  └────┬───┘                              │               │
│              │       │                                   │ Body type     │
│              │       ▼                                   │ [JSON ▾]      │
│              │  ┌────────┐                              │               │
│              │  │Condition│                             │ Retry policy  │
│              │  │>5%?    │                              │ [3 retries]   │
│              │  └─┬────┬─┘                              │               │
│              │  T│    F│                                 │               │
│              │    ▼    ▼                                 │               │
│              │  [Send] [Skip]                           │               │
│              │  email                                   │               │
│              │                                           │               │
└──────────────┴─────────────────────────────────────────┴──────────────┘
```

## 4. Component anatomy

### Toolbar (top, 56px)
- Workflow name (editable inline).
- Status badge (Draft / Saved / Running / Failed).
- Test button (runs once).
- Save button.
- Run button.
- Menu (⋯): Version history, Export, Publish, Duplicate.

### Block palette (left, 240px)
- Categories: Triggers, Browser, HTTP, Transform, Logic, AI, Messaging.
- Each block is a draggable chip.

### Canvas (center, flex)
- Pan / zoom.
- Grid background.
- Nodes placed by drag-drop.
- Connections drawn between output ports and input ports.
- Connection lines color-coded by data type (string, number, boolean, object, array).

### Config panel (right, 320px)
- Shows the selected node's parameters.
- Form-based UI for each parameter.
- "Test this block" button runs only this node.
- Errors shown inline.

### Mini-map (bottom right, optional)
- Small overview of the canvas.
- Drag to navigate.

### Status bar (bottom)
- Cursor position.
- Zoom level.
- Last saved time.
- Run status when running.

## 5. Interactions

| Trigger | Action |
|---------|--------|
| Drag from palette | Create node on canvas |
| Drag from output port | Start connection |
| Drop on input port | Complete connection |
| Click node | Select; show in config panel |
| Double-click node | Open detail view |
| Delete key | Delete selected node / connection |
| ⌘Z / ⌘⇧Z | Undo / Redo |
| ⌘S | Save |
| ⌘R | Run |
| Scroll | Pan |
| ⌘+/⌘- | Zoom |
| Right-click | Context menu |
| Drag connection to empty space | Create new node from connection |

## 6. States

### Draft (unsaved)
- "Unsaved changes" indicator in toolbar.
- Auto-save every 30s.

### Saved
- No indicator; clean state.

### Running
- Active node pulses (aurora-500).
- Connection lines animate.
- Toolbar shows "Stop" instead of "Run."
- Status bar shows progress.

### Failed
- Failed node turns red.
- Error message in status bar.
- Hover shows details.

### Debug mode
- Step button visible.
- Each step pauses for review.
- Variables panel shows current values.

### Empty canvas
- "Drag a trigger here to start" hint.

## 7. Animation

- Node enter: scale-in 160ms.
- Connection draw: 200ms line draw.
- Running pulse: 1.5s ease-in-out infinite.
- Selection ring: 80ms fade.
- Reduced-motion: instant.

## 8. Accessibility

- Canvas is focusable; arrow keys move between nodes.
- Each node has `role="button"` with descriptive label.
- Connections are announced.
- Config panel is keyboard navigable.
- Screen reader announces selection, run state, errors.

## 9. Telemetry

- `workflow.opened`
- `workflow.node_added`
- `workflow.connection_made`
- `workflow.saved`
- `workflow.tested`
- `workflow.ran`
- `workflow.failed`

## 10. Out of scope

- Code view (separate screen, but accessible via toggle).
- Marketplace publishing (separate flow).

## 11. Acceptance criteria

- [ ] Canvas loads in <500ms for 50 nodes.
- [ ] Drag-drop creates node within 80ms.
- [ ] Connections validate type compatibility.
- [ ] Run begins within 500ms.
- [ ] Errors visible within 1s of failure.

## 12. Reading list

- **Visual Workflow Builder Anchor** — NX-FEAT-1800
- **Cloud Browser Fleet Anchor** — NX-FEAT-1600

---

*End NX-UI-6007.*