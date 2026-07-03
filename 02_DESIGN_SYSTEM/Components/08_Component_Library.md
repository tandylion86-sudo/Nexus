# NX-DS-5008 — Component Library

| Field | Value |
|-------|-------|
| **Document ID** | NX-DS-5008 |
| **Title** | Component Library |
| **Phase** | 3 — UX Bible |
| **Owner** | Design AI + Frontend AI |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-06-30 |
| **Depends on** | NX-DS-5002 (Colors), NX-DS-5003 (Typography), NX-DS-5004 (Spacing), NX-DS-5005 (Elevation), NX-DS-5006 (Motion), NX-DS-5007 (Icons) |

---

## 1. Purpose

This document catalogs every **primitive component** in the NEXUS design system. Each component has a fixed API, fixed states, fixed accessibility behavior, and fixed visual treatment. Screens compose from these primitives; they never invent their own.

## 2. Component principles

1. **One component, one purpose.** Variants handle differences.
2. **Tokens over values.** No raw px, hex, or ms.
3. **Accessibility built in.** ARIA, keyboard, focus rings are part of the contract.
4. **Composable.** Components stack and slot into each other predictably.
5. **Deterministic.** Output is the same given the same inputs.

## 3. Surfaces

### Surface

The base container for elevated content.

| Prop | Type | Default |
|------|------|---------|
| `elevation` | 0–5 | 1 |
| `padding` | none / sm / md / lg | md |
| `radius` | none / sm / md / lg / xl | lg |
| `bordered` | boolean | false |

**States:** default, hover (elev +1), selected (elev +1, accent border).

### Panel

A larger surface that contains sections.

| Prop | Type | Default |
|------|------|---------|
| `title` | string | – |
| `collapsible` | boolean | false |
| `sticky` | boolean | false |

## 4. Buttons

### Button

| Variant | Use |
|---------|-----|
| `primary` | Default call-to-action |
| `secondary` | Less prominent |
| `tertiary` | Tertiary (no border) |
| `danger` | Destructive |
| `ghost` | Borderless |

| Size | Height | Padding | Font |
|------|--------|---------|------|
| `sm` | 28 | 8/12 | text-sm |
| `md` | 36 | 10/16 | text-sm |
| `lg` | 44 | 12/20 | text-base |

**States:** default, hover, active (scale 0.98), focus, loading (spinner replaces label), disabled.

**Icons:** leading and trailing icon slots (16px).

### IconButton

Same as Button but icon-only. Requires `aria-label`.

### ButtonGroup

Horizontal grouping of buttons with shared borders (radius on outer buttons only).

## 5. Inputs

### TextField

| Prop | Type | Default |
|------|------|---------|
| `placeholder` | string | – |
| `value` | string | – |
| `type` | text / email / password / url / search | text |
| `error` | string | – |
| `disabled` | boolean | false |
| `leadingIcon` / `trailingIcon` | icon | – |
| `size` | sm / md / lg | md |

**States:** default, focus, error (red border + helper text), disabled.

### TextArea

Same props as TextField plus `rows`, `resize`.

### Select

Dropdown select with search, multi-select, and clear.

### Checkbox

Standard checkbox with label and helper.

### Radio

Radio button group with horizontal/vertical layout.

### Toggle

Switch-style toggle. `on`/`off` states. Animated.

### Slider

Range slider with optional value labels.

## 6. Feedback

### Toast

| Variant | Color |
|---------|-------|
| `info` | info |
| `success` | success |
| `warning` | warning |
| `danger` | danger |

Position: bottom-right. Auto-dismiss: 5s default. Manual dismiss via ×.

### Tooltip

Trigger: hover/focus. Delay: 200ms in, 0ms out. Position: top by default.

### Banner

Inline alert banner at top of a surface. Variants: info, success, warning, danger.

### ProgressBar

Linear progress with optional label.

### Spinner

Indeterminate spinner. Sizes: 16, 20, 24.

### Skeleton

Per NX-DS-5006 §6. Variants: text, block, circle.

## 7. Data display

### List / ListItem

A vertical list with optional sections.

| Prop (Item) | Type |
|------|------|
| `leading` | icon / avatar / checkbox |
| `title` | string |
| `description` | string |
| `trailing` | metadata / chevron / action |
| `selected` | boolean |
| `disabled` | boolean |

### Card

A flexible content container with slots: media, header, body, actions.

### Table

Column-based data display with sort, filter, pagination. Density-aware.

### Badge

Small status indicator. Variants: success, warning, danger, info, neutral.

### Avatar

| Size | px |
|------|----|
| xs | 16 |
| sm | 24 |
| md | 32 |
| lg | 40 |
| xl | 56 |

Supports image, initials (with auto color), and icon fallback.

### Tabs

Horizontal tabs with optional close button per tab. Animated underline.

### Accordion

Vertical collapsible sections.

## 8. Navigation

### TopBar

App-wide top bar (56px) with logo, search, and trailing actions.

### Sidebar

Left navigation. Collapsible to icon-only (56px) or full (240px).

### Breadcrumbs

Path display with clickable ancestors.

### Pagination

Numeric + prev/next. Compact mode for tight spaces.

### CommandPalette

Cmd-K palette. Search + actions. (See NX-UI-6003.)

## 9. Overlays

### Modal

| Size | Width |
|------|-------|
| `sm` | 384 |
| `md` | 512 |
| `lg` | 768 |
| `xl` | 1024 |

Centered. Scrim dims background. Trap focus inside. ESC closes.

### Drawer

Side-anchored overlay. Slide-in animation. Width: 320/480/640.

### Popover

Floating content anchored to a trigger. Used for menus, color pickers, etc.

### ContextMenu

Right-click menu. Positioned at cursor.

## 10. Specialized

### AgentBadge

A badge showing an agent's name and role color. Per NX-DS-5002 §2.4.

### MemoryItem

A row displaying a memory fact with type, source, recency, and edit affordances.

### WorkflowNode

A node on the Visual Workflow Builder canvas. Inputs/outputs are typed ports.

### CloudBrowserTile

A card showing a Cloud Browser's status, name, and quick actions.

### IntentPrompt

The signature large input field for the home screen and command bar.

## 11. Component API conventions

- All components forward `className` and `style`.
- All components accept `data-testid`.
- Components expose ref via `React.forwardRef`.
- Asynchronous state changes (e.g., loading) emit data-state attributes.

## 12. Acceptance criteria

- [ ] Every primitive has an entry in this document.
- [ ] Every primitive has Storybook stories (storybook.js.org).
- [ ] Every primitive passes axe-core a11y checks.
- [ ] Every primitive has keyboard interactions defined.
- [ ] No screen ships a bespoke component not in this library.

## 13. Reading list

- **All NX-DS-5001 to NX-DS-5007** (foundations)
- **Accessibility Foundations** — NX-DS-5009
- **UX Guidelines** — NX-DS-5010
- **Empty / Loading / Error States** — NX-DS-5012

---

*End NX-DS-5008.*