# NX-UI-6009 — Settings

| Field | Value |
|-------|-------|
| **Document ID** | NX-UI-6009 |
| **Screen** | Settings |
| **Owner** | Frontend AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P0 |
| **Touches journeys** | J-15, J-17 |
| **Touches features** | NX-FEAT-2401-2402, NX-FEAT-2701-2711, NX-FEAT-2008, NX-FEAT-2009 |

---

## 1. Purpose

Settings is the **central configuration surface**. Users manage account, subscription, appearance, integrations, privacy, security, AI behavior, and danger zone (delete account).

## 2. When shown

- Triggered by Settings (⚙) icon in top bar.
- Triggered by ⌘, (Cmd+comma) / Ctrl+,.

## 3. Layout

```
┌────────────────────────────────────────────────────────────────┐
│  Settings                                                        │
├──────────────┬─────────────────────────────────────────────────┤
│              │  Account                                         │
│  Account     │  ─────────────────────────────────────────────   │
│  Appearance  │  Maya Patel                                       │
│  AI Behavior │  maya@example.com                                 │
│  Privacy     │  Joined: Jan 2027                                 │
│  Security    │                                                   │
│  Subscription│  Display name    [Maya Patel              ]      │
│  Integrations│  Email           [maya@example.com        ]      │
│  Workspaces  │  Timezone        [America/Los_Angeles  ▾]          │
│  Plugins     │  Language        [English                  ▾]      │
│  Developers  │                                                   │
│  Help        │  Plan                                             │
│  Danger zone │  ─────────────────────────────────────────────   │
│              │  Pro · $20/month · Renews Sep 14, 2027           │
│              │  [Manage subscription]   [View invoices]           │
│              │                                                   │
│              │  Profile                                          │
│              │  ─────────────────────────────────────────────   │
│              │  Passkey:  ✓ Set up                               │
│              │  [Manage passkeys]                                │
└──────────────┴─────────────────────────────────────────────────┘
```

## 4. Component anatomy

### Sidebar (240px)
- Sections: Account, Appearance, AI Behavior, Privacy, Security, Subscription, Integrations, Workspaces, Plugins, Developers, Help, Danger zone.

### Main panel (flex)
- Each section's content.
- Section header + description.
- Form rows with label + control + description.
- Save is implicit (autosave) for most settings.

### Sections

**Account** — display name, email, timezone, language, passkeys.

**Appearance** — theme, accent color, typography size, motion level, density.

**AI Behavior** — tone preference, output length, model preferences, auto-memory toggle.

**Privacy** — telemetry opt-in, browsing history, conversation memory, data export, account deletion.

**Security** — passkeys, password, active sessions, audit log access.

**Subscription** — current plan, usage, billing history, payment method, change plan, cancel.

**Integrations** — connected services (Gmail, Calendar, GitHub, etc.); add/remove.

**Workspaces** — defaults, sharing permissions, archive policy.

**Plugins** — installed AI-native extensions; marketplace link.

**Developers** — API tokens, plugin dev mode, debug tools.

**Help** — onboarding replay, keyboard shortcuts, docs, contact support, status.

**Danger zone** — delete account.

## 5. Interactions

| Trigger | Action |
|---------|--------|
| Click sidebar item | Switch section |
| Edit field | Autosave on blur |
| Click "Manage subscription" | Open NX-UI-6009 sub-screen (billing portal) |
| Click "Delete account" | Confirmation flow |
| Click "Export data" | Triggers data export |

## 6. States

### Default
- Active section visible; sidebar highlighted.

### Loading
- Skeleton for active section.

### Editing
- Field has focus state.
- "Saving…" indicator.
- "Saved ✓" on success.

### Error
- Inline error on field.
- Toast on persistent failure.

### Confirming dangerous action
- Modal: re-authenticate + type confirmation phrase.

### Section not available (H2 feature)
- Greyed; "Coming soon" badge.

## 7. Animation

- Section transition: 200ms cross-fade.
- Field focus: 80ms border.
- Toast: slide-in 240ms.
- Reduced-motion: instant.

## 8. Accessibility

- Sidebar items are buttons with `aria-current="page"`.
- Each field has label.
- Errors announced.
- Tabs (for sub-sections) use `role="tab"`.

## 9. Telemetry

- `settings.opened`
- `settings.section_viewed`
- `settings.changed`
- `settings.exported`
- `settings.account_deleted`

Activity Log captures all settings changes.

## 10. Out of scope

- Per-Workspace settings (handled in Workspace settings).
- Admin console (NX-UI-6009 enterprise variant, H2).

## 11. Acceptance criteria

- [ ] Settings load <300ms.
- [ ] Autosave <500ms.
- [ ] All sections keyboard-accessible.
- [ ] Dangerous actions require confirmation.
- [ ] Export produces a valid archive.

## 12. Reading list

- **Subscription Model** — NX-PRD-0005
- **Sync & Profiles** — NX-FEAT-2001-2009
- **Privacy** — NX-DOC-0004 P4

---

*End NX-UI-6009.*