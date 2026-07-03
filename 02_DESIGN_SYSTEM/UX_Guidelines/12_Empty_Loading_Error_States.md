# NX-DS-5012 — Empty / Loading / Error States

| Field | Value |
|-------|-------|
| **Document ID** | NX-DS-5012 |
| **Title** | Empty / Loading / Error States |
| **Phase** | 3 — UX Bible |
| **Owner** | Design AI |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-06-30 |
| **Depends on** | NX-DS-5006 (Motion), NX-DS-5008 (Components), NX-DS-5010 (UX Guidelines) |

---

## 1. Purpose

Every screen in NEXUS has at least three states: **default, loading, empty, error**. This document defines each state with consistent patterns so screens feel cohesive across the product.

## 2. The state matrix

| State | Trigger | Duration budget | Visual |
|-------|---------|------------------|--------|
| **Default** | Data present | – | Content |
| **Loading** | Fetching | <2s default | Skeleton |
| **Long-loading** | Fetching | >2s | Skeleton + label + cancel |
| **Empty** | No data | – | Hero illustration + CTA |
| **Partial** | Some data | – | Existing + "load more" |
| **Error** | Failure | – | Icon + headline + recovery |
| **Offline** | No network | – | Banner + offline behavior |
| **Permission denied** | User denied | – | Explanation + request flow |

## 3. Loading state

### 3.1 Skeletons

Per NX-DS-5006 §6. Skeletons match the final content's dimensions exactly.

Skeleton variants:

| Variant | Usage |
|---------|-------|
| `text` | Single-line text |
| `block` | Multi-line text or paragraph |
| `circle` | Avatar, icon |
| `rect` | Image, media |
| `card` | Full card surface |
| `table-row` | Table row |

### 3.2 Spinners

Used for **determinate actions** (e.g., submitting a form), not for content loading.

| Size | Use |
|------|-----|
| 16 | Inline with text |
| 20 | Button replacement |
| 24 | Page-level action |
| 32 | Full-page load |

### 3.3 Progress bars

Used for **measurable progress** (uploads, downloads, long-running tasks).

- Linear by default.
- Optional label and percentage.
- Color: aurora-500; danger if progress halts.

### 3.4 Streaming

Per NX-DS-5006 §7. AI tokens stream into a stable container.

## 4. Empty state

### 4.1 Pattern

Per NX-DS-5010 §5.2:

```
┌──────────────────────────────────┐
│                                    │
│           [Illustration]           │
│                                    │
│         Headline (≤6 words)        │
│                                    │
│      Description (1–2 sentences)   │
│                                    │
│      [Primary CTA]   [Secondary]   │
│                                    │
└──────────────────────────────────┘
```

### 4.2 Per-surface empty states

| Surface | Headline | Primary CTA |
|---------|----------|-------------|
| Home (no workspaces) | "What do you want to accomplish?" | (input) |
| Workspace list (none) | "No workspaces yet" | "Create workspace" |
| Marketplace (none in category) | "No agents here yet" | "Suggest an agent" |
| Memory Inspector (none) | "Nothing remembered yet" | (auto-fills as you work) |
| Activity Log (none) | "No activity yet" | (passive) |
| Cloud Browser Fleet (none) | "No Cloud Browsers yet" | "Create Cloud Browser" |
| Workflow Builder (canvas empty) | "Build your first workflow" | (palette hint) |
| Notifications (none) | "All caught up" | (passive) |

### 4.3 Empty state illustrations

- Style: line-art, single accent color.
- Size: 96–144px square.
- Subject: representative of the surface's purpose.
- Tone: gentle, never scolding.

## 5. Error state

### 5.1 Pattern

```
┌──────────────────────────────────┐
│                                    │
│            [⚠ icon]                │
│                                    │
│       Headline (clear)             │
│                                    │
│   What happened (1 sentence)       │
│   What to do (1 sentence)          │
│                                    │
│   [Primary: retry]   [Get help]    │
│                                    │
└──────────────────────────────────┘
```

### 5.2 Error categories

| Category | Pattern |
|----------|---------|
| Network | "Couldn't reach the server. Check your connection." |
| Permission | "You don't have permission to do that." |
| Validation | Inline error on the offending field |
| Not found | "We couldn't find that. It may have been moved or deleted." |
| Server | "Something went wrong on our end. We're looking into it." |
| Conflict | "This changed since you opened it. [Reload latest]" |
| Quota | "You've hit the limit on this plan. [Upgrade]" |

### 5.3 Error announcement

Errors are announced to screen readers via `aria-live="assertive"`. Toast variants are non-modal; modal variants trap focus.

### 5.4 Recovery

Every error has a recovery action:
- Retry (most common)
- Refresh
- Contact support
- Upgrade
- Undo

The error never asks the user to "try again later" without offering an alternative.

## 6. Offline state

When the network drops:

- A persistent banner appears at the top: "You're offline. Changes will sync when you reconnect."
- Cloud-dependent features show a "Unavailable offline" placeholder.
- Local features continue working.
- Queue is shown in Activity Log.

The user can dismiss the banner; it reappears on next state change.

## 7. Permission denied state

When a user denies a permission:

- The denied action is greyed out or shows a "Why we need this" link.
- Re-requesting opens a clear explanation, not the same prompt.
- A persistent "Denied permissions" entry in Settings lists all denied.

## 8. Component state quick-reference

| Component | States |
|-----------|--------|
| Button | default, hover, active, focus, loading, disabled |
| Input | default, focus, filled, error, disabled, read-only |
| Toggle | off, on, hover, focus, disabled |
| Card | default, hover, selected, focused, disabled |
| List item | default, hover, selected, focused, disabled |
| Modal | closed, opening, open, closing |
| Toast | entering, visible, exiting |
| Tabs | inactive, hover, focus, active |

## 9. Acceptance criteria

- [ ] Every screen has a loading skeleton.
- [ ] Every list has an empty state with CTA.
- [ ] Every error has a recovery action.
- [ ] Offline banner appears within 5s of network drop.
- [ ] Skeleton dimensions match final content.
- [ ] Spinners used only for actions, not content loading.
- [ ] Streaming shows skeletons before tokens arrive.

## 10. Reading list

- **Overview** — NX-DS-5001
- **Motion & Animation** — NX-DS-5006
- **Component Library** — NX-DS-5008
- **UX Guidelines** — NX-DS-5010
- **Responsive Strategy** — NX-DS-5011

---

*End NX-DS-5012.*