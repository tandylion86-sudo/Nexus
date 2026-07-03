# NX-DS-5007 — Iconography

| Field | Value |
|-------|-------|
| **Document ID** | NX-DS-5007 |
| **Title** | Iconography |
| **Phase** | 3 — UX Bible |
| **Owner** | Design AI |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-06-30 |
| **Depends on** | NX-DS-5001 (Overview) |

---

## 1. Purpose

NEXUS icons are **geometric, restrained, and legible**. They use a single-stroke style with consistent corner radius. This document defines the icon family, sizing, naming, and usage rules.

## 2. Icon family

NEXUS uses **Phosphor Icons (Regular weight)** as the primary family. License: MIT.

| Source | License | Usage |
|--------|---------|-------|
| Phosphor (Regular) | MIT | Default |
| Phosphor (Bold) | MIT | Active state emphasis |
| Lucide (fallback) | ISC | When Phosphor lacks a glyph |
| Custom | NEXUS | Branded icons (logo, agent avatars) |

A custom layer (Phosphor-aligned stroke) can be created for unique concepts.

## 3. Sizes

| Token | px | Usage |
|-------|----|-------|
| `--nx-icon-xs` | 12 | Inline with caption text |
| `--nx-icon-sm` | 16 | Default UI (buttons, list rows) |
| `--nx-icon-md` | 20 | Section headers |
| `--nx-icon-lg` | 24 | Empty state heroes |
| `--nx-icon-xl` | 32 | Page heroes |
| `--nx-icon-2xl` | 48 | Onboarding |

Icons align to the type baseline: 16px icon centers on 20px line-height (text-sm).

## 4. Stroke and geometry

- **Stroke width:** 1.5px (Regular) / 2px (Bold) at 24px size; scales proportionally.
- **Corner radius:** 1px on internal corners; 2px on outer corners.
- **Grid:** 24x24px optical grid; icons have 1px padding inside.
- **Stroke caps:** Round.
- **Stroke joins:** Round.

## 5. Naming convention

`<category>-<name>-<variant>`

| Example | Meaning |
|---------|---------|
| `agent-planner` | Agent category, planner name |
| `nav-workspace` | Navigation category, workspace name |
| `action-search` | Action category, search name |
| `status-success` | Status category, success variant |

Custom NEXUS icons use the `nx-` prefix: `nx-cloud-browser`, `nx-memory`, `nx-workflow`.

## 6. Iconography by category

### Navigation

- `nav-home`, `nav-workspace`, `nav-marketplace`, `nav-cloud-browser`, `nav-memory`, `nav-workflow`, `nav-settings`, `nav-notifications`, `nav-activity`, `nav-help`

### Actions

- `action-search`, `action-add`, `action-remove`, `action-edit`, `action-delete`, `action-share`, `action-download`, `action-upload`, `action-copy`, `action-filter`, `action-sort`, `action-refresh`

### Agents

- `agent-planner`, `agent-researcher`, `agent-coder`, `agent-reviewer`, `agent-tester`, `agent-publisher`, `agent-default`

### Status

- `status-success`, `status-warning`, `status-danger`, `status-info`, `status-loading`

### Memory

- `memory-fact`, `memory-preference`, `memory-style`, `memory-document`, `memory-graph`

### Custom NEXUS

- `nx-cloud-browser`, `nx-memory`, `nx-workflow`, `nx-workspace`, `nx-command-bar`, `nx-agent`, `nx-marketplace`, `nx-activity`

## 7. Usage rules

1. **Single-color.** Icons use `currentColor`. No multi-color icons.
2. **No text inside icons.** Words belong in labels.
3. **No decorative-only icons.** Every icon must have a meaning.
4. **Pair icons with labels** unless space is critical (≤24px).
5. **Don't redraw.** Always use the library; no bespoke SVG unless approved.

## 8. State changes

| State | Variant |
|-------|---------|
| Default | Regular |
| Hover | Regular (slight scale 1.05) |
| Active | Bold |
| Selected | Bold + accent color |
| Disabled | Regular + 40% opacity |

## 9. Accessibility

- All interactive icons must have a `aria-label`.
- Decorative icons get `aria-hidden="true"`.
- Color is never the only signal — pair with text or shape variation.

## 10. Animation

- Icons can rotate (loading), pulse (notification), or flip (toggle).
- Animations respect reduced-motion (no spin for `prefers-reduced-motion`).
- Icon swap (e.g., bookmark filled vs. outline) uses cross-fade, not swap.

## 11. Custom NEXUS icons

The following are custom (not in Phosphor):

| Icon | Description |
|------|-------------|
| `nx-cloud-browser` | Browser window with cloud overlay |
| `nx-memory` | Brain glyph with circuit detail |
| `nx-workflow` | Three connected nodes |
| `nx-workspace` | Folder with goal indicator |
| `nx-command-bar` | Terminal-prompt-style bar |
| `nx-agent` | Hexagon with center dot |
| `nx-marketplace` | Storefront awning |
| `nx-activity` | Pulse-line waveform |

## 12. Acceptance criteria

- [ ] Every UI icon comes from the defined library.
- [ ] Icons are single-color and use `currentColor`.
- [ ] Custom NEXUS icons are documented in this spec.
- [ ] Interactive icons have `aria-label`s.
- [ ] Icon swaps cross-fade, not pop.
- [ ] All sizes align to text baselines.

## 13. Reading list

- **Overview** — NX-DS-5001
- **Typography** — NX-DS-5003
- **Component Library** — NX-DS-5008
- **Accessibility Foundations** — NX-DS-5009

---

*End NX-DS-5007.*