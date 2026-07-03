# NX-UI-6001 — Home Screen

| Field | Value |
|-------|-------|
| **Document ID** | NX-UI-6001 |
| **Screen** | Home Screen |
| **Owner** | Frontend AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P0 |
| **Touches journeys** | J-07 (Onboarding), J-08 (Marketplace), J-11 (Schedule) |
| **Touches features** | NX-FEAT-1101, NX-FEAT-1201, NX-FEAT-1202, NX-FEAT-1501, NX-FEAT-2205, NX-FEAT-2801 |

---

## 1. Purpose

The Home Screen is the **first thing a user sees** when opening NEXUS. It exists to convert intent into action. There is no navigation menu, no logo on top, no search bar. The single primary element is the prompt: **"What do you want accomplished?"**

This screen is the embodiment of the mission.

## 2. When shown

- Default screen on app open (after onboarding).
- Triggered by ⌘+H (macOS) / Ctrl+H (Windows/Linux).
- Shown on `nexus://home`.

## 3. Layout

```
┌────────────────────────────────────────────────────────────────┐
│  [user avatar]                              [⌘K] [⚙] [🌙]      │  ← 56px top bar, sparse
├────────────────────────────────────────────────────────────────┤
│                                                                  │
│                                                                  │
│                                                                  │
│            Good evening, Maya                                     │
│                                                                  │
│   ┌────────────────────────────────────────────────────────┐   │
│   │  What do you want accomplished?                         │   │
│   │  [                                              ] [→]    │   │
│   └────────────────────────────────────────────────────────┘   │
│                                                                  │
│                                                                  │
│   Resume                                                         │
│   ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐     │
│   │ Acme     │  │ Q4 Market│  │ Coding:  │  │ Daily    │     │
│   │ research │  │ Map      │  │ Feature X│  │ Briefing │     │
│   └──────────┘  └──────────┘  └──────────┘  └──────────┘     │
│                                                                  │
│   Try one of these                                                │
│   • Generate this week's content calendar                        │
│   • Monitor my competitors' prices hourly                        │
│   • Build a dossier on Acme Corp                                  │
│                                                                  │
│                                                                  │
└────────────────────────────────────────────────────────────────┘
```

## 4. Component anatomy

### 4.1 Top bar (56px)

- **User avatar** (32px) on far left → opens profile switcher.
- **Command palette icon** (⌘K) center-right → opens NX-UI-6003.
- **Settings** (⚙) → opens NX-UI-6009.
- **Theme toggle** (🌙/☀️) → switches theme.
- Background: `--nx-bg-canvas` with bottom border `--nx-border-subtle`.

### 4.2 Greeting

- "Good evening, Maya" — uses user's first name from account.
- Time-of-day aware: morning/afternoon/evening.
- Hidden if user disables (Settings → Privacy).
- Type: `text-3xl`, weight semibold.

### 4.3 Intent prompt (the centerpiece)

- Width: 720px max, 80% of viewport min.
- Height: 72px.
- Padding: 24px horizontal.
- Border: 2px solid `--nx-border-default`.
- Background: `--nx-bg-elevated`.
- Shadow: `--nx-elev-1`; on focus `--nx-elev-3`.
- Placeholder: "What do you want accomplished?" (when empty).
- Trailing: arrow icon button "→" (only when input has text).
- Focus state: border `--nx-border-focus`, ring `--nx-focus-ring`.

**Interactions:**
- Click focuses; caret appears.
- Type shows streaming acknowledgment placeholder.
- Submit (Enter or arrow) opens NX-UI-6003 with the typed intent.
- Empty state shows suggestions on focus.

### 4.4 Resume row

- Header: "Resume" (text-sm, secondary text).
- Cards: 4 most-recently-active Workspaces.
- Each card: 220×120px, `--nx-bg-canvas`, elev-1, hover elev-2.
- Card content:
  - Workspace name (text-base, semibold).
  - Last activity ("2h ago", "yesterday").
  - 1-line goal sentence.
  - Color stripe on left (workspace color).
- Click → opens Workspace.

### 4.5 Suggestion list

- Header: "Try one of these" (text-sm, secondary).
- 3 sample intents, each a row with leading icon + text.
- Click → fills prompt and submits.
- Suggestions rotate based on:
  - Recent activity
  - Persona inference
  - Time of day
  - Day of week

## 5. Interactions

| Trigger | Action |
|---------|--------|
| Click prompt | Focus input |
| Type | Streaming acknowledgment appears |
| Enter / click → | Submits intent; opens NX-UI-6003 |
| ⌘K / Ctrl+K | Open command palette |
| Click Resume card | Open Workspace |
| Click suggestion | Fill prompt and submit |
| Tab | Move to next suggestion |
| Esc (with focused prompt) | Clear prompt |

## 6. States

### Default
- Prompt empty; suggestions visible.
- Resume row populated with up to 4 recent Workspaces.

### Loading (cold start)
- Skeleton for top bar (avatar, icons).
- Skeleton for prompt (full width).
- Skeleton for Resume row (4 cards).
- Skeleton for suggestions (3 rows).
- Total skeleton load: <300ms.

### Empty (no Workspaces)
- Resume row replaced with illustration + "Create your first workspace" CTA.
- Suggestions remain.

### Focused
- Prompt border becomes accent; ring visible.
- Suggestions stay visible but slightly dimmed.

### Typing
- Prompt grows with content (up to 4 lines).
- Submit arrow appears.
- Below prompt: "I'll think through this. Approve when ready?" skeleton (40ms).

### Submitted
- Prompt transitions to "Working on it…" state.
- Background dims; PlanViewer (NX-UI-6003 variant) slides in from bottom.

### Error
- If intent can't be parsed: "I'm not sure what you mean. Try one of these or rephrase."
- Suggestions remain visible.

### Offline
- Prompt disabled; banner above: "You're offline. Some commands are unavailable."

## 7. Animation

- Page enter: 240ms ease-out, prompt scales from 0.96 to 1.
- Resume cards: stagger 40ms each.
- Suggestions: stagger 20ms each.
- Submit: prompt collapses to top bar; plan viewer slides up (240ms).
- Reduced-motion: instant state changes, no transforms.

## 8. Accessibility

- Prompt has `aria-label="What do you want accomplished?"`.
- Resume row is a `role="region"` with `aria-label="Resume recent work"`.
- Each card is a button (`role="button"`) with descriptive label.
- Suggestions are buttons with full intent text in `aria-label`.
- Color contrast: prompt border passes 3:1.
- Keyboard: Tab cycles prompt → suggestions → resume cards.
- Screen reader announces greeting and Resume contents on focus.

## 9. Telemetry

Events emitted (opt-in):

- `home.viewed`
- `home.prompt.focused`
- `home.prompt.typed`
- `home.prompt.submitted`
- `home.suggestion.clicked`
- `home.resume.clicked`
- `home.command_palette.opened`

Activity Log captures all submitted intents.

## 10. Out of scope

- Workspace creation UI (handled in NX-UI-6002).
- Settings (NX-UI-6009).
- Notifications (NX-UI-6010).
- Mobile layout (H3).

## 11. Open questions

- Q: Should greeting use first name or "you"? (Currently first name; option to disable.)
- Q: Should Resume show >4 cards in a carousel, or paginate?
- Q: How do suggestions adapt when the user is on a free vs. paid plan?

## 12. Acceptance criteria

- [ ] First-paint <300ms on reference hardware.
- [ ] Intent prompt receives focus on load (configurable; default off).
- [ ] All keyboard interactions work without pointer.
- [ ] Suggestions adapt to user persona and recency.
- [ ] Resume row updates within 1s of Workspace activity.
- [ ] Submit transitions to plan viewer in <300ms.

## 13. Reading list

- **Product Philosophy** — NX-DOC-0005
- **Onboarding** — NX-PRD-0004
- **Workspace Anchor** — NX-FEAT-1100
- **AI Command Bar** — NX-UI-6003

---

*End NX-UI-6001.*