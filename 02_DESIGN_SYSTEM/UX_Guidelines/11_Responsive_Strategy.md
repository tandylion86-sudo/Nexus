# NX-DS-5011 — Responsive Strategy

| Field | Value |
|-------|-------|
| **Document ID** | NX-DS-5011 |
| **Title** | Responsive Strategy |
| **Phase** | 3 — UX Bible |
| **Owner** | Design AI |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-06-30 |
| **Depends on** | NX-DS-5004 (Spacing & Layout), NX-DS-5009 (Accessibility) |

---

## 1. Purpose

NEXUS is desktop-first (H1) and expands to tablet and mobile in later horizons. This document defines the **breakpoints**, **layout adaptations**, and **density rules** for each form factor.

## 2. Form factors

| Form factor | Target | Min width | Max width | H1 |
|-------------|--------|-----------|-----------|----|
| Mobile | iOS, Android | 320 | 639 | H3 read-only; H4 full |
| Tablet portrait | iPad, Android | 640 | 767 | H3 (limited) |
| Tablet landscape | iPad, Android | 768 | 1023 | H3 |
| Laptop | macOS, Windows, Linux | 1024 | 1279 | H1 ✅ |
| Desktop | macOS, Windows, Linux | 1280 | 1535 | H1 ✅ |
| Wide desktop | macOS, Windows, Linux | 1536+ | – | H1 ✅ |

The H1 design system targets **laptop and above**. Below laptop is a separate effort (mobile companion in H3+).

## 3. Layout adaptations

### 3.1 Sidebar

| Form factor | Default | Behavior |
|-------------|---------|----------|
| Wide desktop | Expanded (240px) | Toggle |
| Desktop | Expanded (240px) | Toggle |
| Laptop | Collapsed (56px) | Hover-expand |
| Tablet landscape | Hidden | Hamburger |
| Tablet portrait | Hidden | Hamburger |
| Mobile | Hidden | Hamburger |

### 3.2 Tri-pane layouts

Tri-pane layouts (e.g., Visual Workflow Builder) collapse on smaller screens:

| Form factor | Tri-pane behavior |
|-------------|-------------------|
| Wide desktop | All three panes visible |
| Desktop | All three visible, panes resizable |
| Laptop | Middle + right only; left hidden |
| Below laptop | Single pane + tabs |

### 3.3 Tables

| Form factor | Table behavior |
|-------------|----------------|
| Wide desktop | Full table |
| Desktop | Full table with horizontal scroll if needed |
| Laptop | Compact density + horizontal scroll |
| Tablet | Card list view instead |
| Mobile | Card list view |

### 3.4 Dialogs

| Form factor | Dialog width |
|-------------|--------------|
| Wide desktop | Up to 1024px |
| Desktop | Up to 768px |
| Laptop | Up to 512px |
| Tablet | 90% of viewport |
| Mobile | Full-screen sheet |

### 3.5 Touch vs. pointer

| Form factor | Interaction model |
|-------------|-------------------|
| Desktop / Wide | Pointer (mouse, trackpad) + keyboard |
| Laptop | Pointer + keyboard |
| Tablet | Touch + keyboard (if available) |
| Mobile | Touch |

Touch-specific adjustments:
- Touch targets ≥44×44 px.
- Hover states replaced with active states.
- Drag handles enlarged.
- Long-press for context menu.

## 4. Density

Two density modes:

| Mode | Row height | Compact button | Default for |
|------|------------|----------------|-------------|
| Comfortable | 40px | 36px | Most users, mobile/tablet |
| Compact | 32px | 28px | Power users, desktop |

Density is per-Workspace, persisted across sessions.

## 5. Font scaling

Users can override base font size (default 16px, range 14–20px). All sizes scale proportionally.

## 6. Zoom support

Browser zoom (Cmd+/Cmd-) is supported up to 200%. Layouts reflow without horizontal scroll at 200% zoom on a 1280px viewport.

## 7. Orientation

Tablet supports portrait and landscape; layouts adapt:

| Surface | Portrait | Landscape |
|---------|----------|-----------|
| Workflow Builder | Stack panes | Tri-pane |
| Chat | Full | Tri-pane |
| Workspace | Full | Tri-pane |
| Home | Centered hero | Centered hero |

## 8. High-DPI displays

All vector assets are SVG. Raster assets ship at 2x and 3x. Icons render at 1x, 2x, 3x via vector.

## 9. Acceptance criteria

- [ ] All breakpoints have at least one tested layout.
- [ ] Sidebar collapses correctly at laptop width.
- [ ] Touch targets are ≥44px on touch form factors.
- [ ] Density switch is preserved across sessions and devices.
- [ ] 200% zoom does not cause horizontal scroll at 1280px.
- [ ] Tablet portrait and landscape are both tested.

## 10. Reading list

- **Overview** — NX-DS-5001
- **Spacing & Layout** — NX-DS-5004
- **Component Library** — NX-DS-5008
- **Accessibility Foundations** — NX-DS-5009

---

*End NX-DS-5011.*