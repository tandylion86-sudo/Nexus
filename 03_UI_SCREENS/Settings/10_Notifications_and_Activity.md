# NX-UI-6010 — Notifications & Activity Log

| Field | Value |
|-------|-------|
| **Document ID** | NX-UI-6010 |
| **Screen** | Notifications & Activity Log |
| **Owner** | Frontend AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P0 |
| **Touches journeys** | J-09, J-10, J-20 |
| **Touches features** | NX-FEAT-2201-2209 |

---

## 1. Purpose

Notifications surfaces real-time system events; Activity Log provides the **full audit trail** of agent actions. Both are critical for trust (per NX-DOC-0004 P3 — Transparency by default).

## 2. When shown

- **Notifications panel**: bell icon in top bar (⌘⇧. / Ctrl+Shift+.).
- **Activity Log**: clock icon in top bar (⌘⇧A / Ctrl+Shift+A) or via Settings → Security.

## 3. Layout — Notifications

```
┌──────────────────────────────────────┐
│  Notifications           [Mark all]   │
├──────────────────────────────────────┤
│  ●  Workflow "Price Monitor" ran       │
│     2m ago · Cloud Browser #2          │
│                                        │
│  ●  LinkedIn agent sent 12 messages    │
│     1h ago                             │
│                                        │
│  ○  GitHub PR #234 review ready        │
│     3h ago                             │
│                                        │
│  ⚠  Action required: Permission       │
│     request from Research agent        │
│     5h ago                             │
└──────────────────────────────────────┘
```

A 360px-wide panel anchored to the bell icon.

## 4. Component anatomy (Notifications)

- Header: title + "Mark all read."
- Notification rows:
  - Unread indicator (filled dot).
  - Title.
  - Source (workspace / agent).
  - Timestamp (relative).
  - Status (action required vs. info).
- Footer: "View all activity" link → Activity Log.

## 5. Layout — Activity Log

```
┌────────────────────────────────────────────────────────────────┐
│  Activity Log                          [Filter ▾]  [Export]    │
├────────────────────────────────────────────────────────────────┤
│  Today                                                          │
│  ● 14:23 · Researcher · Read article "Acme pricing"            │
│         Target: example.com/pricing                            │
│         ✓ Completed in 4.2s                                     │
│  ● 14:23 · LinkedIn agent · Sent message                       │
│         Target: jane@example.com                                │
│         ✓ Completed in 1.8s                                     │
│  ● 14:20 · Planner · Generated plan                           │
│         Workspace: Acme Corp research                           │
│                                                                  │
│  Yesterday                                                      │
│  ● 09:15 · Cloud Browser #2 · Resumed                          │
│  ● 09:14 · User · Opened workspace "Q4 Market Map"             │
└────────────────────────────────────────────────────────────────┘
```

## 6. Component anatomy (Activity Log)

### Filter bar
- Date range.
- Agent.
- Action type.
- Workspace.
- Status (success / failure / pending).

### Search
- Live search across action descriptions, targets.

### Timeline
- Day-grouped.
- Each row:
  - Timestamp (HH:MM).
  - Actor (agent or user).
  - Action verb.
  - Target (truncated; expand for full).
  - Duration or result.

### Row expand
- Click → full details: input, reasoning, output, links to source artifacts.

## 7. Interactions

### Notifications

| Trigger | Action |
|---------|--------|
| Click row | Navigate to source |
| Click "Mark all read" | Clear unread |
| Click "View all" | Open Activity Log |

### Activity Log

| Trigger | Action |
|---------|--------|
| Click row | Expand details |
| Click filter | Apply filter |
| Click "Export" | Download CSV / JSON |
| Click "Clear" | Confirm and clear older entries (per retention) |

## 8. States

### Notifications

- **Default**: unread + read mixed, sorted by recency.
- **Empty**: "All caught up." (passive, no CTA).
- **Action required**: badge on bell icon.

### Activity Log

- **Default**: today's entries visible.
- **Loading**: skeleton rows.
- **Empty**: "No activity yet. As agents work, you'll see their actions here."
- **Filtered**: filter chips shown; "Clear filters" button.
- **Search active**: filtered list.
- **Error**: "Couldn't load activity. [Retry]."

## 9. Animation

- New notification: bell badge pulses once (240ms).
- Notification enter: 200ms slide-down.
- Activity row expand: 160ms.
- Reduced-motion: instant.

## 10. Accessibility

- Notifications list has `role="log"` with `aria-live="polite"`.
- Each notification has full label.
- Activity Log rows have labels with timestamps.
- Filter buttons have toggle state announced.

## 11. Telemetry

- `notifications.opened`
- `notifications.read`
- `activity_log.opened`
- `activity_log.filtered`
- `activity_log.exported`

## 12. Out of scope

- Cross-user activity (team plans, H2).
- SIEM export (H2 enterprise).

## 13. Acceptance criteria

- [ ] Notifications load <200ms.
- [ ] Activity Log loads <500ms for 10,000 entries.
- [ ] Filter applies <100ms.
- [ ] Export completes <10s.
- [ ] All actions keyboard-accessible.

## 14. Reading list

- **Activity Log leaves** — NX-FEAT-2205-2209
- **Permission system** — NX-FEAT-2101-2110
- **Transparency principle** — NX-DOC-0004 P3

---

*End NX-UI-6010.*