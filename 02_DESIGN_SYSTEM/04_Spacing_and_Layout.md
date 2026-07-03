# NX-DS-5004 — Spacing & Layout

| Field | Value |
|-------|-------|
| **Document ID** | NX-DS-5004 |
| **Title** | Spacing & Layout |
| **Phase** | 3 — UX Bible |
| **Owner** | Design AI |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-06-30 |
| **Depends on** | NX-DS-5001 (Overview) |

---

## 1. Purpose

Spacing in NEXUS is built on a **4-point grid**. Every margin, padding, and gap is a multiple of 4px. This document defines the spacing tokens, container widths, and the responsive strategy.

## 2. Spacing scale

| Token | px | rem | Usage |
|-------|----|----|-------|
| `--nx-space-0` | 0 | 0 | Reset |
| `--nx-space-1` | 4 | 0.25 | Tightest (icon to text) |
| `--nx-space-2` | 8 | 0.5 | Compact (button gap) |
| `--nx-space-3` | 12 | 0.75 | Snug |
| `--nx-space-4` | 16 | 1 | Default (paragraph, padding) |
| `--nx-space-5` | 20 | 1.25 | Section inner |
| `--nx-space-6` | 24 | 1.5 | Card padding |
| `--nx-space-8` | 32 | 2 | Card-to-card |
| `--nx-space-10` | 40 | 2.5 | Section break |
| `--nx-space-12` | 48 | 3 | Major section |
| `--nx-space-16` | 64 | 4 | Page-level |
| `--nx-space-20` | 80 | 5 | Hero |
| `--nx-space-24` | 96 | 6 | Marketing |
| `--nx-space-32` | 128 | 8 | Marketing hero |

## 3. Spacing by component

| Component | Padding | Gap |
|-----------|---------|-----|
| Button | 8 / 16 | – |
| Input | 8 / 12 | – |
| Card | 16 / 24 | 16 |
| Modal | 24 | 16 |
| Page | 32 | 24 |
| Sidebar item | 8 / 12 | 2 |
| List item | 12 / 16 | 8 |
| Toast | 12 / 16 | 8 |

## 4. Layout primitives

### 4.1 The 12-column grid

NEXUS uses a 12-column grid with 16px gutters.

```
┌────────────────────────────────────────────────┐
│  Margin 24px                                     │
│  ┌────┬────┬────┬────┬────┬────┬────┬────┬────┐  │
│  │ c1 │ c2 │ c3 │ c4 │ c5 │ c6 │ c7 │ c8 │ c9 │  │
│  │    │    │    │    │    │    │    │    │    │  │
│  └────┴────┴────┴────┴────┴────┴────┴────┴────┘  │
│  16px gutters                                    │
└────────────────────────────────────────────────┘
```

### 4.2 Container widths

| Token | Max width | Usage |
|-------|-----------|-------|
| `--nx-container-sm` | 640 | Forms, narrow content |
| `--nx-container-md` | 768 | Article |
| `--nx-container-lg` | 1024 | Default |
| `--nx-container-xl` | 1280 | Wide tables |
| `--nx-container-2xl` | 1536 | Marketing |
| `--nx-container-prose` | 720 | Long-form reading |

## 5. Breakpoints

| Token | Min width | Target |
|-------|-----------|--------|
| `--nx-bp-sm` | 640 | Tablet portrait |
| `--nx-bp-md` | 768 | Tablet |
| `--nx-bp-lg` | 1024 | Laptop |
| `--nx-bp-xl` | 1280 | Desktop |
| `--nx-bp-2xl` | 1536 | Wide desktop |

Mobile-first; layouts grow from `--nx-bp-sm` upward.

## 6. Common layout patterns

### 6.1 App shell

```
┌──────────────────────────────────────────┐
│ Top bar (56px)                            │
├────┬─────────────────────────────────────┤
│ N  │                                       │
│ a  │                                       │
│ v  │  Content                              │
│    │                                       │
│ 56 │                                       │
└────┴─────────────────────────────────────┘
```

Sidebar: 56px collapsed, 240px expanded.

### 6.2 Two-column split

```
┌────────────────┬─────────────────────────┐
│ Sidebar (320)  │  Main (flex)              │
│                │                            │
└────────────────┴─────────────────────────┘
```

Used in: Workspace switcher, Settings, Memory Inspector.

### 6.3 Centered hero

```
┌──────────────────────────────────────────┐
│                                            │
│           ┌─────────────────┐              │
│           │   Max 720       │              │
│           │   Centered      │              │
│           └─────────────────┘              │
│                                            │
└──────────────────────────────────────────┘
```

Used in: Home screen, Onboarding.

### 6.4 Tri-pane

```
┌────┬─────────────┬─────────────────────┐
│ L  │  Middle     │  Right               │
│ 56 │  280        │  flex                │
└────┴─────────────┴─────────────────────┘
```

Used in: AI Chat, Visual Workflow Builder.

## 7. Density

Two density modes are supported:

| Mode | Row height | Use case |
|------|------------|----------|
| **Comfortable** | 40px | Default for most surfaces |
| **Compact** | 32px | Power users, data-dense tables |

Users can switch density per Workspace (per NX-DS-5011).

## 8. Border radius

| Token | px | Usage |
|-------|----|-------|
| `--nx-radius-none` | 0 | – |
| `--nx-radius-sm` | 4 | Tags, chips |
| `--nx-radius-md` | 8 | Inputs, buttons |
| `--nx-radius-lg` | 12 | Cards |
| `--nx-radius-xl` | 16 | Modals |
| `--nx-radius-2xl` | 24 | Hero surfaces |
| `--nx-radius-full` | 9999 | Pills, avatars |

## 9. Z-index scale

| Token | Value | Usage |
|-------|-------|-------|
| `--nx-z-base` | 0 | Default |
| `--nx-z-dropdown` | 1000 | Dropdowns |
| `--nx-z-sticky` | 1100 | Sticky bars |
| `--nx-z-overlay` | 1300 | Modal scrim |
| `--nx-z-modal` | 1400 | Modal dialog |
| `--nx-z-popover` | 1500 | Popovers |
| `--nx-z-toast` | 1700 | Toasts |
| `--nx-z-tooltip` | 1800 | Tooltips |

## 10. Acceptance criteria

- [ ] Every layout uses tokens; no raw px for spacing.
- [ ] All breakpoints have at least one tested layout.
- [ ] Density switch is preserved across sessions.
- [ ] Sidebar collapse/expand works at all breakpoints.
- [ ] Z-index scale prevents overlap bugs.

## 11. Reading list

- **Overview** — NX-DS-5001
- **Responsive Strategy** — NX-DS-5011
- **Component Library** — NX-DS-5008

---

*End NX-DS-5004.*