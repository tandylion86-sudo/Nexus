# NX-UI-6004 — AI Chat

| Field | Value |
|-------|-------|
| **Document ID** | NX-UI-6004 |
| **Screen** | AI Chat |
| **Owner** | Frontend AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P0 |
| **Touches journeys** | J-01, J-02, J-03, J-13 |
| **Touches features** | NX-FEAT-1301-1309, NX-FEAT-1406, NX-FEAT-1704 |

---

## 1. Purpose

AI Chat is the **persistent conversational surface** for the active Workspace. It is where agents deliver results, where the user iterates, and where longer interactions live. Distinct from the Command Bar: Chat is for **iteration**, not **initiation**.

## 2. When shown

- Default surface inside every Workspace (right pane).
- Can be expanded to full width.
- Can be collapsed (icon-only rail).

## 3. Layout

```
┌────────────────────────────────────────────────────────────────┐
│  Acme Corp research                              [⌘⇧C] [⚙]   │  ← Workspace header
├────────────────────────────────────────────────────────────────┤
│                                                                  │
│                                                                  │
│  ┌────────────────────────────────────────────────────┐        │
│  │ Maya · 2:14 PM                                      │        │
│  │ Summarize the latest 5 articles about Acme's       │        │
│  │ pricing changes.                                    │        │
│  └────────────────────────────────────────────────────┘        │
│                                                                  │
│  ┌────────────────────────────────────────────────────┐        │
│  │ 🟣 Planner  ·  2:14 PM                              │        │
│  │ I'll plan this. One moment.                         │        │
│  └────────────────────────────────────────────────────┘        │
│                                                                  │
│  ┌────────────────────────────────────────────────────┐        │
│  │ 🔵 Researcher  ·  2:15 PM                           │        │
│  │ I found 5 articles. Key pricing changes:            │        │
│  │                                                     │        │
│  │ • Mar 3: Acme raised list price 12%                 │        │
│  │ • Mar 17: Acme introduced a "team" tier             │        │
│  │ • Apr 2: Acme matched competitor discounts          │        │
│  │ ...                                                  │        │
│  │ Sources: [1] [2] [3] [4] [5]                         │        │
│  └────────────────────────────────────────────────────┘        │
│                                                                  │
│                                                                  │
├────────────────────────────────────────────────────────────────┤
│  [Ask a follow-up or give feedback...            ] [↗]            │
└────────────────────────────────────────────────────────────────┘
```

## 4. Component anatomy

### Workspace header
- Workspace name + goal sentence (small).
- Toggle: Chat expanded / collapsed (⌘⇧C).
- Settings (⚙) → Workspace settings.

### Message bubbles
- **User messages**: right-aligned, slate-100 background.
- **Agent messages**: left-aligned, agent color stripe (5px left border).
- **System messages**: centered, italic, muted.
- Each message:
  - Author badge (avatar + agent name).
  - Timestamp (relative).
  - Body (Markdown).
  - Actions on hover: copy, regenerate, edit.

### Streaming
- Tokens appear as generated.
- Container does not reflow.
- Code blocks render with monospace from token 1.

### Inline artifacts
- Tables, charts, images rendered in place.
- "Open in viewer" expands to full size.
- "Copy" / "Save to file" actions.

### Citations
- Numbered references like `[1]`.
- Hover shows tooltip with title + URL.
- Click opens source.

### Composer (bottom)
- Multi-line input (resizes 1–4 lines).
- Submit (Enter or ↗).
- Shift+Enter for newline.
- Voice input icon (when supported).
- File attach icon (when relevant).

## 5. Interactions

| Trigger | Action |
|---------|--------|
| Click composer | Focus + cursor |
| Enter | Submit |
| Shift+Enter | Newline |
| Hover message | Show actions |
| Click "Copy" | Copy markdown to clipboard |
| Click "Regenerate" | Re-run last assistant message |
| Click "Edit" | Edit user message; resubmit |
| Click citation | Open source |
| ⌘⇧C | Toggle collapse |
| ⌘↑ / ⌘↓ | Navigate messages |
| Esc | Cancel streaming |

## 6. States

### Default
- Workspace's conversation visible.
- Composer ready.

### Empty (first open)
- Welcome message from system.
- "Try asking: …" suggestions (3 contextual).

### Loading (initial)
- Skeleton for first assistant message.

### Streaming
- Active message shows streaming indicator.
- Composer disabled.
- "Stop" button replaces submit.

### Regenerating
- "Regenerate" replaces message in place.
- "Stop" button visible.

### Editing user message
- Message becomes editable.
- Resubmit cancels future messages; starts new branch.

### Error
- Inline error message in place of response.
- "Retry" button.

### Workspace changed
- Conversation clears (or loads previous if available).
- Brief loading state.

## 7. Animation

- New message: fade + slide up 160ms.
- Streaming: tokens appear instantly (no flicker).
- Hover actions: 80ms fade.
- Toggle collapse: 240ms width animation.
- Reduced-motion: instant; no transforms.

## 8. Accessibility

- Each message has `role="article"`.
- Author and timestamp announced.
- Streaming changes announced via `aria-live="polite"`.
- Citations are focusable buttons.
- Composer has label.
- Full keyboard nav.

## 9. Telemetry

- `chat.opened`
- `chat.message_sent`
- `chat.regenerated`
- `chat.citation_clicked`
- `chat.stream_completed`

Activity Log captures all messages.

## 10. Out of scope

- Voice conversation (H2).
- Branching visual tree (H2; current edit-and-resubmit is simpler).
- Voice input (H2).

## 11. Acceptance criteria

- [ ] First message visible in <500ms of Workspace open.
- [ ] Streaming starts in <500ms of submit.
- [ ] Citations are keyboard-focusable.
- [ ] Copy / Regenerate / Edit work without errors.
- [ ] Toggle collapse persists.

## 12. Reading list

- **AI Chat leaves** — NX-FEAT-1301-1309
- **Workspace Anchor** — NX-FEAT-1100
- **AI Command Bar** — NX-UI-6003

---

*End NX-UI-6004.*