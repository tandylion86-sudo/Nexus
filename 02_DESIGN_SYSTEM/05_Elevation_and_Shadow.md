# NX-DS-5005 — Elevation & Shadow

| Field | Value |
|-------|-------|
| **Document ID** | NX-DS-5005 |
| **Title** | Elevation & Shadow |
| **Phase** | 3 — UX Bible |
| **Owner** | Design AI |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-06-30 |
| **Depends on** | NX-DS-5001 (Overview), NX-DS-5002 (Colors) |

---

## 1. Purpose

Elevation establishes the **visual depth hierarchy** of NEXUS. Higher-elevation surfaces feel closer to the user; lower-elevation surfaces feel like background. This document defines five elevation levels and the shadows that produce them.

## 2. The 5 elevation levels

| Token | Elevation | Shadow | Usage |
|-------|-----------|--------|-------|
| `--nx-elev-0` | 0 | none | Flat surfaces, page background |
| `--nx-elev-1` | 1 | `0 1px 2px rgba(0,0,0,0.04), 0 1px 3px rgba(0,0,0,0.06)` | Cards, list items |
| `--nx-elev-2` | 2 | `0 4px 6px rgba(0,0,0,0.05), 0 2px 4px rgba(0,0,0,0.06)` | Hover state, sticky bars |
| `--nx-elev-3` | 3 | `0 10px 15px rgba(0,0,0,0.07), 0 4px 6px rgba(0,0,0,0.05)` | Popovers, dropdowns |
| `--nx-elev-4` | 4 | `0 20px 25px rgba(0,0,0,0.10), 0 10px 10px rgba(0,0,0,0.04)` | Modals, dialogs |
| `--nx-elev-5` | 5 | `0 25px 50px rgba(0,0,0,0.15)` | Hero, full-screen takeovers |

## 3. Shadow color rules

| Theme | Base shadow |
|-------|------------|
| Light | `rgba(15, 23, 42, 0.X)` (slate-900 alpha) |
| Dark | `rgba(0, 0, 0, 0.X)` (pure black alpha, heavier) |
| Sepia | `rgba(61, 47, 31, 0.X)` (sepia-base alpha) |

Dark mode shadows are deeper because dark surfaces don't shadow as visibly with subtle blacks.

## 4. Elevation by component

| Component | Default | Hover/Active |
|-----------|---------|--------------|
| Page background | elev-0 | – |
| Card (rest) | elev-1 | elev-2 |
| Card (selected) | elev-2 | elev-2 |
| List item | elev-0 | elev-1 |
| Dropdown menu | elev-3 | – |
| Tooltip | elev-3 | – |
| Modal | elev-4 | – |
| Toast | elev-4 | – |
| Popover | elev-3 | – |
| Command bar | elev-3 | elev-4 (when expanded) |
| Sticky header | elev-2 | – |

## 5. Borders vs. shadows

Two ways to define elevation: shadows and borders. NEXUS prefers **shadows for elevation**, borders for delineation.

- **Shadow** = surface above background.
- **Border** = part of the same surface (e.g., input field, divider).

A card that needs to look "above" uses a shadow. A card that needs to look "outlined" uses a 1px border. The two are not combined unless for high-contrast or specific accessibility needs.

## 6. Focus rings

Focus rings are NOT part of the elevation scale; they are accessibility indicators.

| Token | Value |
|-------|-------|
| `--nx-focus-ring` | `0 0 0 3px rgba(99,102,241, 0.4)` |
| `--nx-focus-ring-inset` | `inset 0 0 0 2px var(--nx-border-focus)` |

The focus ring is **always visible** for keyboard users and is preserved across themes.

## 7. Hover lift

Some surfaces lift on hover:

```css
.nx-card {
  box-shadow: var(--nx-elev-1);
  transition: box-shadow 120ms ease-out, transform 120ms ease-out;
}
.nx-card:hover {
  box-shadow: var(--nx-elev-2);
  transform: translateY(-1px);
}
```

The lift is subtle (1px) and quick (120ms). Reduced-motion users do not see the lift.

## 8. Dark mode adjustments

Dark mode increases shadow contrast:

| Level | Light alpha | Dark alpha |
|-------|-------------|------------|
| 1 | 0.04 / 0.06 | 0.20 / 0.30 |
| 2 | 0.05 / 0.06 | 0.25 / 0.35 |
| 3 | 0.07 / 0.05 | 0.30 / 0.40 |
| 4 | 0.10 / 0.04 | 0.40 / 0.45 |
| 5 | 0.15 | 0.50 |

In dark mode, elevation also benefits from a subtle border (`1px solid rgba(255,255,255,0.06)`) to delineate cards from background.

## 9. Acceptance criteria

- [ ] Every interactive surface has an explicit elevation token.
- [ ] Hover states are visually distinct from rest.
- [ ] Modal layering is unambiguous (elev-4 sits above elev-3).
- [ ] Focus rings are visible at all elevations.
- [ ] Reduced-motion users see no lift animation.
- [ ] Dark mode shadows pass visual review.

## 10. Reading list

- **Overview** — NX-DS-5001
- **Color Tokens** — NX-DS-5002
- **Motion & Animation** — NX-DS-5006
- **Accessibility Foundations** — NX-DS-5009

---

*End NX-DS-5005.*