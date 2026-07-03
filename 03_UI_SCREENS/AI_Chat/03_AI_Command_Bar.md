# NX-UI-6003 — AI Command Bar

| Field | Value |
|-------|-------|
| **Document ID** | NX-UI-6003 |
| **Screen** | AI Command Bar |
| **Owner** | Frontend AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P0 |
| **Touches journeys** | J-01, J-02, J-03, J-04, J-08, J-11 |
| **Touches features** | NX-FEAT-1201-1209, NX-FEAT-1401, NX-FEAT-1406, NX-FEAT-1412 |

---

## 1. Purpose

The AI Command Bar is the **universal intent entry point** from anywhere in NEXUS. It accepts natural-language commands, suggests actions, dispatches to the agent orchestrator, and shows plan streaming.

## 2. When shown

- Triggered by ⌘+K / Ctrl+K from any screen.
- Triggered by ⌘+L / Ctrl+L (alternative).
- Triggered by submitting the Home prompt.
- Triggered by `/` in any text field (focus-stealing).

## 3. Layout

```
┌────────────────────────────────────────────────────────────────┐
│                                                                  │
│   ┌──────────────────────────────────────────────────────┐     │
│   │  📝  Summarize this article and add key points to...    │     │
│   │      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━      │     │
│   └──────────────────────────────────────────────────────┘     │
│                                                                  │
│   ┌─ Plan ───────────────────────────────────────────────┐     │
│   │  1.  Extract article text (browser)              ✓      │     │
│   │  2.  Generate summary (researcher)                ⟳      │     │
│   │  3.  Save key points to Workspace memory          ◯      │     │
│   │  4.  Notify you when ready                        ◯      │     │
│   └────────────────────────────────────────────────────────┘    │
│                                                                  │
│   ┌─ Approvals ──────────────────────────────────────────┐    │
│   │  ◯ Read current page                                  │    │
│   │  ◯ Save to memory                                     │    │
│   │  ◯ Notify you                                         │    │
│   └────────────────────────────────────────────────────────┘    │
│                                                                  │
│                                            [Edit plan] [Run]    │
└────────────────────────────────────────────────────────────────┘
```

## 4. Component anatomy

### Intent input
- 56px tall, autofocus.
- Leading icon (varies by mode: text = ✎, voice = 🎙, file = 📎).
- Placeholder: "Tell NEXUS what you want."
- Streaming acknowledgment: shimmer below caret when typing.

### Suggestions dropdown
- Appears when input is empty or query is short.
- Shows: recent commands, slash commands, suggested actions.

### Plan viewer
- Step list (1–N steps).
- Each step:
  - Number (1, 2, 3...).
  - Description.
  - Status icon: pending (◯), running (⟳ spinner), done (✓), error (✗).
  - Agent badge (color + name).
- Real-time updates (sub-100ms).

### Approvals panel
- Permissions required for the plan.
- Each is a checkbox the user toggles to grant/deny.
- Defaults to "ask each time" (more restrictive) or "remember for this session" (less restrictive).

### Footer actions
- "Edit plan" (text button) → opens inline editor.
- "Run" (primary) → executes plan.
- "Cancel" (during execution) → stops and reports what was done.

## 5. Interactions

| Trigger | Action |
|---------|--------|
| Click / ⌘K | Open bar |
| Type | Suggestion dropdown updates |
| Enter / submit | Generate plan |
| Tab | Move through approvals |
| Space | Toggle approval |
| ↑ / ↓ | Move through suggestions |
| Esc | Close (or cancel if running) |
| Click "Run" | Execute plan |

## 6. States

### Empty
- Suggestions shown.

### Typing
- Suggestions filter live.
- After 800ms of no typing: "Generating plan…" shimmer.

### Plan generated
- Plan visible.
- Approvals visible.
- "Run" button enabled.
- "Edit plan" button visible.

### Editing plan
- Inline text editor for each step.
- Add / remove / reorder steps.
- Save returns to plan view.

### Running
- "Run" replaced with "Cancel."
- Steps update live.
- Streaming output below plan.
- Approvals locked (cannot change mid-run).

### Partial result
- Some steps done, some pending.
- User can pause / resume.

### Done
- All steps ✓.
- Result displayed below.
- "Done" tick (60ms fade).
- "Run again" / "Save as workflow" actions.

### Error
- Step with error highlighted (red).
- Error message inline.
- "Retry this step" / "Skip" / "Cancel" actions.

### Cancelled
- "Plan cancelled." message.
- Steps that completed remain visible.

## 7. Animation

- Open: scale-in 160ms from top of viewport.
- Plan streaming: each step fades in as it starts.
- Approvals: slide down 200ms.
- Done: ✓ fades in 60ms.
- Reduced-motion: instant state changes.

## 8. Accessibility

- `role="dialog"`.
- Input has label.
- Plan steps are a `role="list"`; each step has descriptive label.
- Status changes announced via `aria-live="polite"`.
- Errors announced `aria-live="assertive"`.
- Full keyboard control.

## 9. Telemetry

- `command_bar.opened`
- `command_bar.typed`
- `command_bar.plan_generated`
- `command_bar.approved`
- `command_bar.run`
- `command_bar.cancelled`
- `command_bar.error`

Activity Log captures every plan execution.

## 10. Out of scope

- Multi-modal commands (voice, image upload — H2).
- Command history browser (handled in command palette).

## 11. Acceptance criteria

- [ ] Opens in <100ms globally.
- [ ] Plan generation ≤3s for typical intents.
- [ ] Step status updates within 100ms of state change.
- [ ] Streaming output visible within 500ms of run.
- [ ] Cancel halts execution within 1s.

## 12. Reading list

- **AI Command Bar leaves** — NX-FEAT-1201-1209
- **Agent Orchestrator** — NX-FEAT-1401-1414
- **Home Screen** — NX-UI-6001

---

*End NX-UI-6003.*