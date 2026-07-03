# NX-DS-5009 — Accessibility Foundations

| Field | Value |
|-------|-------|
| **Document ID** | NX-DS-5009 |
| **Title** | Accessibility Foundations |
| **Phase** | 3 — UX Bible |
| **Owner** | Design AI + Security AI |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-06-30 |
| **Depends on** | NX-DS-5002 (Colors), NX-DS-5003 (Typography), NX-DS-5006 (Motion) |

---

## 1. Purpose

NEXUS commits to **WCAG 2.2 AA** as the floor and pursues AAA where feasible. This document defines accessibility foundations: contrast, focus, keyboard navigation, screen reader support, motion, and the testing methodology.

Accessibility is not a feature added at the end. It is **structural** to every component.

## 2. Compliance targets

| Standard | Target |
|----------|--------|
| WCAG 2.2 AA | Required |
| WCAG 2.2 AAA | Aspirational (focus indicator, sign language, contrast) |
| EN 301 549 | Required (EU public sector) |
| Section 508 | Required (US federal) |
| ADA Title III | Required (US commerce) |

## 3. Perceivable

### 3.1 Color contrast

| Pair | Min ratio |
|------|-----------|
| Body text on background | 4.5:1 |
| Large text (≥18pt or 14pt bold) on background | 3:1 |
| UI components (icons, borders) on background | 3:1 |
| Focus indicator on background | 3:1 |
| Disabled text on background | 3:1 (for AAA; not required for AA) |

Color combinations in NX-DS-5002 are pre-validated. Component tests assert contrast at runtime.

### 3.2 Color independence

Color is never the only signal. Each color change is accompanied by:
- An icon
- A text label
- A shape change

Examples:
- Error: red border + ✕ icon + helper text "Invalid email."
- Success: green check + ✓ icon + "Saved."

### 3.3 Text alternatives

| Element | Alternative |
|---------|-------------|
| Decorative images | `alt=""` (empty alt) |
| Functional icons (button) | `aria-label` |
| Informative images | Descriptive `alt` |
| Charts | Long description in `aria-describedby` |
| Code blocks | Full code as text |

### 3.4 Resize and reflow

- Layout reflows at 320px width (1.4x zoom on a 1280px viewport).
- No horizontal scroll at 320px.
- Text scales to 200% without loss of content.

## 4. Operable

### 4.1 Keyboard navigation

Every interactive element is reachable by keyboard, in a logical order.

| Key | Action |
|-----|--------|
| Tab | Move focus forward |
| Shift+Tab | Move focus backward |
| Arrow keys | Within composite widgets (menus, lists) |
| Enter | Activate |
| Space | Toggle / activate |
| Escape | Cancel / close overlay |
| Cmd+K / Ctrl+K | Open command palette |

Focus order matches visual order unless an alternative is documented.

### 4.2 Focus indicator

The focus ring is **always visible** for keyboard users and **hidden** for pointer users.

```css
.nx-focus-ring:focus-visible {
  outline: 2px solid var(--nx-border-focus);
  outline-offset: 2px;
  border-radius: var(--nx-radius-md);
}
```

`focus-visible` (not `:focus`) ensures mouse clicks do not show rings.

### 4.3 Skip links

Long pages have skip links at the start:
- Skip to main content
- Skip to navigation
- Skip to search

### 4.4 Touch targets

Touch targets are at least **44×44 px** (WCAG 2.5.5 AAA) with at least 8px spacing between adjacent targets.

### 4.5 No motion-required controls

No essential function requires motion (e.g., drag). All drag interactions have keyboard equivalents.

## 5. Understandable

### 5.1 Language

- Page language is declared (`<html lang="en">`).
- Language changes within content are marked (`<span lang="ja">`).
- Locale follows user preference (per NX-DS-5011).

### 5.2 Consistent navigation

Navigation order, naming, and position are consistent across pages. Repeated components look and behave the same.

### 5.3 Input assistance

- Form fields have associated labels (`<label for>`).
- Required fields are marked both visually and with `aria-required`.
- Errors are announced to screen readers (`aria-describedby`).
- Suggestions are provided where possible (e.g., password strength).

## 6. Robust

### 6.1 Markup validity

HTML passes W3C validation. ARIA is used only when no native element exists.

### 6.2 Compatibility

Tested with:
- NVDA + Firefox
- JAWS + Chrome
- VoiceOver + Safari (macOS, iOS)
- TalkBack + Chrome (Android)
- Windows Narrator + Edge

### 6.3 Status announcements

Live regions announce state changes:

```html
<div aria-live="polite">Saved.</div>
<div aria-live="assertive">Error: unable to save.</div>
```

- `polite`: non-urgent (saved, loaded).
- `assertive`: urgent (error, alert).

## 7. Reduced motion

Per NX-DS-5006 §10, all motion is suppressed for `prefers-reduced-motion: reduce`. Equivalent visual cues (color, text) replace motion cues.

## 8. Cognitive accessibility

- Plain language in microcopy.
- Short sentences.
- Consistent terminology.
- No jargon in user-facing copy.
- Progressive disclosure of complexity.

## 9. Internationalization

- 7 launch locales: en, es, pt-BR, fr, de, ja, zh-CN.
- RTL planned: ar, he (H2).
- Strings externalized to i18n catalogs.
- Date/time/number formatting per locale.

## 10. Testing methodology

| Test | Tool | Frequency |
|------|------|-----------|
| Automated a11y | axe-core in CI | Every PR |
| Visual a11y | Storybook a11y addon | Every PR |
| Manual keyboard | QA AI | Weekly |
| Screen reader | Manual + NVDA/JAWS | Bi-weekly |
| Color contrast | Stark / Colour Contrast Analyser | Per release |
| User testing | 3rd-party audit annually | Annual |

A failure on axe-core blocks merge.

## 11. Acceptance criteria

- [ ] Every component passes axe-core.
- [ ] Every screen is fully keyboard navigable.
- [ ] Every screen is announced by NVDA + VoiceOver.
- [ ] Color contrast passes WCAG AA in all themes.
- [ ] Touch targets ≥44px.
- [ ] Focus indicator visible in all themes.
- [ ] Reduced-motion users see no transforms.
- [ ] 3rd-party audit passes annually.

## 12. Reading list

- **Overview** — NX-DS-5001
- **Color Tokens** — NX-DS-5002
- **Typography** — NX-DS-5003
- **Motion & Animation** — NX-DS-5006
- **Component Library** — NX-DS-5008
- **UX Guidelines** — NX-DS-5010

---

*End NX-DS-5009.*