# NX-UI-6012 — Plugin SDK / Developer

| Field | Value |
|-------|-------|
| **Document ID** | NX-UI-6012 |
| **Screen** | Plugin SDK / Developer |
| **Owner** | Frontend AI + Documentation AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P1 |
| **Touches journeys** | J-16 |
| **Touches features** | NX-FEAT-1901-1909 |

---

## 1. Purpose

The Developer surface gives plugin creators everything they need to **build, test, publish, and monetize** AI-native extensions for NEXUS. It includes documentation, a CLI, sandbox testing, and a publishing dashboard.

## 2. When shown

- Triggered by Developers section in Settings.
- Triggered by `nexus://dev` URL.
- Triggered by menu in Marketplace → "Become a creator."

## 3. Layout

```
┌────────────────────────────────────────────────────────────────┐
│  Developer Hub                                                   │
├──────────────┬─────────────────────────────────────────────────┤
│              │  Welcome, Maya                                    │
│  Getting     │                                                    │
│   started    │  Quick start                                       │
│  Tutorials   │  ─────────────────────────────────────────────   │
│  API         │                                                    │
│  Plugin SDK  │  Install the CLI:                                  │
│  Workflows   │  $ npm install -g @nexus/cli                       │
│  Marketplace │                                                    │
│  Publishing  │  Create a plugin:                                  │
│  Analytics   │  $ nexus plugin init my-plugin                     │
│  Community   │                                                    │
│              │  Run locally:                                      │
│              │  $ nexus plugin dev                                │
│              │                                                    │
│              │  Publish when ready:                               │
│              │  $ nexus plugin publish                            │
│              │                                                    │
│              │  [Full documentation]   [API reference]            │
└──────────────┴─────────────────────────────────────────────────┘
```

## 4. Component anatomy

### Sidebar (240px)
- Getting started
- Tutorials
- API
- Plugin SDK
- Workflows
- Marketplace
- Publishing (creator-only)
- Analytics (creator-only)
- Community

### Main panel
- Content varies by section.
- Code blocks with syntax highlighting + copy buttons.
- Inline runnable examples.

### Plugin SDK section
- Manifest schema reference.
- Runtime API.
- Permission API.
- Storage API.
- UI extension points.

### Publishing section (creators)
- Submission form.
- Status: Draft / In review / Approved / Rejected.
- Version history.

### Analytics (creators)
- Installs over time (chart).
- Active users.
- Ratings distribution.
- Earnings.

## 5. Interactions

| Trigger | Action |
|---------|--------|
| Click sidebar | Switch section |
| Click code block "Copy" | Copy to clipboard |
| Click "Run example" | Open sandbox |
| Click "Submit for review" | Begin publishing flow |
| Click "View source" | Open GitHub link |

## 6. States

### Default
- Documentation content rendered.

### Loading
- Skeleton for content.

### Sandbox running
- Code panel; output panel below.
- "Stop" button.

### Publishing
- Submission form with validation.
- Status updates after submit.

### Approved / Live
- Dashboard with metrics.
- "Update version" CTA.

### Rejected
- Reason displayed.
- "Resubmit" with fixes.

## 7. Animation

- Section transitions: 200ms cross-fade.
- Code copy: brief highlight 200ms.
- Reduced-motion: instant.

## 8. Accessibility

- Code blocks have `role="region"` and labels.
- Tabs have `role="tab"`.
- Copy buttons have aria-live announcements.
- Keyboard nav throughout.

## 9. Telemetry

- `dev_hub.opened`
- `dev_hub.section_viewed`
- `dev_hub.code_copied`
- `dev_hub.sandbox_run`
- `dev_hub.submitted`
- `dev_hub.published`

## 10. Out of scope

- In-browser IDE (H2).
- Plugin collaboration (H2).

## 11. Acceptance criteria

- [ ] Documentation loads <500ms.
- [ ] Code copy works in all browsers.
- [ ] Submission form validates correctly.
- [ ] Publishing flow <5 minutes.
- [ ] Analytics updates within 1 hour of activity.

## 12. Reading list

- **Plugin SDK leaves** — NX-FEAT-1901-1909
- **Agent Marketplace Anchor** — NX-FEAT-1500
- **Coding Standards** — 12_DEVELOPER_GUIDE (Phase 5+)

---

*End NX-UI-6012.*