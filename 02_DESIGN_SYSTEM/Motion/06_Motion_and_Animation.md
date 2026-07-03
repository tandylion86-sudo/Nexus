# NX-DS-5006 — Motion & Animation

| Field | Value |
|-------|-------|
| **Document ID** | NX-DS-5006 |
| **Title** | Motion & Animation |
| **Phase** | 3 — UX Bible |
| **Owner** | Design AI |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-06-30 |
| **Depends on** | NX-DS-5001 (Overview) |

---

## 1. Purpose

Motion in NEXUS is **purposeful, never decorative**. It serves three roles: signal state change, direct attention, and maintain spatial continuity. This document defines durations, easing curves, choreography, and reduced-motion handling.

## 2. Principles

1. **Motion is a signal.** It must communicate something the user would otherwise miss.
2. **Motion is fast.** Default animations are 120–200ms. Anything longer feels broken.
3. **Motion is interruptible.** A user action cancels any in-flight motion.
4. **Motion is honest.** Skeletons are skeletons; loading bars show real progress.
5. **Motion respects preference.** `prefers-reduced-motion` users see no transforms.

## 3. Duration scale

| Token | Duration | Usage |
|-------|----------|-------|
| `--nx-duration-instant` | 0ms | State toggles |
| `--nx-duration-fast` | 80ms | Micro-interactions (hover) |
| `--nx-duration-normal` | 160ms | Default (button, input) |
| `--nx-duration-slow` | 240ms | Component entry (cards, panels) |
| `--nx-duration-slower` | 360ms | Page-level transitions |
| `--nx-duration-slowest` | 600ms | Hero / onboarding animations |

## 4. Easing curves

| Token | Curve | Usage |
|-------|-------|-------|
| `--nx-ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` | Entries, hovers (fast out) |
| `--nx-ease-in` | `cubic-bezier(0.7, 0, 0.84, 0)` | Exits (fast in) |
| `--nx-ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | Position changes |
| `--nx-ease-spring` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | Playful overshoot (used sparingly) |
| `--nx-ease-linear` | `linear` | Progress bars, scroll |

The default for almost everything is `--nx-ease-out`.

## 5. Animation patterns

### 5.1 Fade in (entry)

```css
.nx-fade-in {
  animation: nx-fade-in var(--nx-duration-normal) var(--nx-ease-out) both;
}
@keyframes nx-fade-in {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}
```

Used for cards, list items, panels entering.

### 5.2 Fade out (exit)

```css
.nx-fade-out {
  animation: nx-fade-out var(--nx-duration-fast) var(--nx-ease-in) both;
}
@keyframes nx-fade-out {
  from { opacity: 1; }
  to { opacity: 0; }
}
```

### 5.3 Scale in (modals, popovers)

```css
.nx-scale-in {
  animation: nx-scale-in var(--nx-duration-normal) var(--nx-ease-out) both;
  transform-origin: var(--nx-scale-origin, center);
}
@keyframes nx-scale-in {
  from { opacity: 0; transform: scale(0.96); }
  to { opacity: 1; transform: scale(1); }
}
```

### 5.4 Slide in (drawers)

```css
.nx-slide-in-right {
  animation: nx-slide-in-right var(--nx-duration-slow) var(--nx-ease-out) both;
}
@keyframes nx-slide-in-right {
  from { transform: translateX(100%); }
  to { transform: translateX(0); }
}
```

## 6. Skeleton loaders

When content is loading, a **skeleton** is shown. Skeletons are:

- Same dimensions as the final content.
- Animated with a soft shimmer (1.5s linear infinite).
- Replaced by content the moment it's available.

```css
.nx-skeleton {
  background: linear-gradient(
    90deg,
    var(--nx-bg-muted) 0%,
    var(--nx-bg-hover) 50%,
    var(--nx-bg-muted) 100%
  );
  background-size: 200% 100%;
  animation: nx-shimmer 1.5s linear infinite;
  border-radius: var(--nx-radius-sm);
}
@keyframes nx-shimmer {
  to { background-position: -200% 0; }
}
```

## 7. Streaming AI content

When AI tokens stream in, the experience is:

1. **<500ms**: Empty container with shimmer.
2. **<500ms**: First token appears.
3. **Stream**: Tokens append at model rate.
4. **Complete**: A subtle "done" tick (60ms fade).

No jumpy reflows. Code blocks render with monospace from token 1.

## 8. State transitions

| Change | Animation |
|--------|-----------|
| Button hover | 80ms ease-out (background, transform) |
| Button press | 80ms scale(0.98) |
| Input focus | 160ms ease-out (border + ring) |
| Switch toggle | 160ms ease-in-out |
| Tab change | 160ms cross-fade |
| Modal open | 160ms scale-in + scrim fade |
| Modal close | 120ms scale-out + scrim fade |
| Toast enter | 240ms slide-down + fade |
| Toast exit | 160ms fade |

## 9. Choreography

When multiple elements animate together, they stagger:

| Distance | Stagger |
|----------|---------|
| Single component | 0ms |
| List of 5 items | 40ms each |
| List of 20+ items | 20ms each (cap at 400ms) |
| Page sections | 80ms |

Stagger uses `--nx-ease-out` and respects `prefers-reduced-motion`.

## 10. Reduced motion

When `prefers-reduced-motion: reduce` is set:

- All transform animations are replaced with opacity-only fades.
- All durations are capped at 80ms.
- Skeleton shimmer is removed (static gray block).
- Hover lifts are removed.
- Page transitions become instant.

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 80ms !important;
    transition-duration: 80ms !important;
    scroll-behavior: auto !important;
  }
  /* Disable transforms */
  .nx-card:hover { transform: none; }
}
```

## 11. Performance budget

- Animation frame budget: 16ms per frame.
- Use `transform` and `opacity` only for animations (avoid layout/paint).
- Use `will-change` sparingly and remove after animation.
- Heavy animations (e.g., canvas) off main thread when possible.

## 12. Acceptance criteria

- [ ] All animations use tokens; no raw ms values.
- [ ] Reduced-motion users see no transforms.
- [ ] Skeletons match final content dimensions.
- [ ] Streaming AI content streams without reflows.
- [ ] Hover/press/focus transitions are 80–160ms.
- [ ] Modals open/close within 160ms total.
- [ ] No animation runs longer than 600ms.

## 13. Reading list

- **Overview** — NX-DS-5001
- **Accessibility Foundations** — NX-DS-5009
- **Empty / Loading / Error States** — NX-DS-5012

---

*End NX-DS-5006.*