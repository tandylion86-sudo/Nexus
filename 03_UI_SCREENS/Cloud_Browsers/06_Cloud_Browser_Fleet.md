# NX-UI-6006 — Cloud Browser Fleet Dashboard

| Field | Value |
|-------|-------|
| **Document ID** | NX-UI-6006 |
| **Screen** | Cloud Browser Fleet Dashboard |
| **Owner** | Frontend AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P0 |
| **Touches journeys** | J-04, J-12 |
| **Touches features** | NX-FEAT-1601-1614 |

---

## 1. Purpose

The Cloud Browser Fleet Dashboard is the **management surface** for all of a user's Cloud Browsers. Users create, monitor, configure, schedule, snapshot, and delete browsers from here.

## 2. When shown

- Triggered by Cloud Browsers icon in sidebar.
- Triggered by ⌘⇧B / Ctrl+Shift+B.
- Triggered by typing `/cloud` in command palette.

## 3. Layout

```
┌────────────────────────────────────────────────────────────────┐
│  Cloud Browsers                                       [+ New]    │
├────────────────────────────────────────────────────────────────┤
│  🔍 Search browsers...                       Status ▾  Region ▾ │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ 🟢 LinkedIn Outreach                                     │   │
│  │ Solo · US-East · Proxy: residential-pool · 32h active    │   │
│  │ Last task: Sent 12 messages · 5m ago                      │   │
│  │ [Open]  [Schedule]  [Snapshot]  [⋯]                       │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ 🟡 Price Monitor                                         │   │
│  │ Solo · US-East · Proxy: none · 8h active                 │   │
│  │ Scheduled: every 1h · Next run: in 47m                   │   │
│  │ [Open]  [Schedule]  [Snapshot]  [⋯]                       │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ ⚪ GitHub Test #1                                        │   │
│  │ Solo · EU-West · Proxy: residential-2 · Idle 3d          │   │
│  │ Cookies: 12 sites · Storage: 240MB                       │   │
│  │ [Open]  [Schedule]  [Snapshot]  [⋯]                       │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  Total usage this month: 84 / 300 hours     [View analytics]    │
└────────────────────────────────────────────────────────────────┘
```

## 4. Component anatomy

### Header
- Title + "New" button.

### Search + filters
- Search bar.
- Status filter (Active / Idle / Suspended / All).
- Region filter (US-East / US-West / EU / APAC / All).

### Browser row
- Status indicator (colored dot).
- Name (semibold).
- Metadata line: workspace, region, proxy, activity.
- Last task or next scheduled.
- Actions: Open / Schedule / Snapshot / menu (⋯).

### Usage footer
- Current period usage.
- "View analytics" link.

## 5. Interactions

| Trigger | Action |
|---------|--------|
| Click "+ New" | Create dialog |
| Click "Open" | Live view (sub-screen) |
| Click "Schedule" | Schedule editor |
| Click "Snapshot" | Snapshot dialog |
| Click ⋯ | Menu: Rename, Change proxy, Edit fingerprint, Delete, etc. |
| Click row (anywhere not on action) | Detail panel |

## 6. States

### Default
- All browsers listed.

### Loading
- Skeleton rows (5 × 88px).

### Empty
- "No Cloud Browsers yet." CTA: "Create your first Cloud Browser."

### Search active
- Live filter.

### Browser suspended
- Greyed row with "Suspended" badge.
- "Resume" replaces "Open."

### Error
- Red status; "Browser unhealthy" badge.
- Action: "Diagnose."

## 7. Animation

- Row enter: stagger 30ms.
- Status changes: dot color cross-fades 240ms.
- Reduced-motion: instant.

## 8. Accessibility

- Each row has accessible label: "LinkedIn Outreach, active, US-East, 32 hours this month."
- Status announced.
- Keyboard nav full.

## 9. Telemetry

- `cloud_browser_fleet.viewed`
- `cloud_browser.created`
- `cloud_browser.opened`
- `cloud_browser.scheduled`
- `cloud_browser.snapshotted`
- `cloud_browser.deleted`

## 10. Out of scope

- Live remote view (sub-screen — separate spec).
- Analytics dashboard (separate spec).

## 11. Acceptance criteria

- [ ] List loads in <500ms for 100 browsers.
- [ ] Filters update <100ms.
- [ ] Create dialog completes in <30s.
- [ ] All actions keyboard-accessible.

## 12. Reading list

- **Cloud Browser Fleet Anchor** — NX-FEAT-1600
- **Subscription Model** — NX-PRD-0005

---

*End NX-UI-6006.*