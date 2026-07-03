# NX-UI-6011 — Onboarding

| Field | Value |
|-------|-------|
| **Document ID** | NX-UI-6011 |
| **Screen** | Onboarding |
| **Owner** | Frontend AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P0 |
| **Touches journeys** | J-07 |
| **Touches features** | NX-FEAT-2801-2810 |

---

## 1. Purpose

Onboarding is the **first-run experience** that turns a fresh install into an activated user. It is the most important UX in the product — every percentage point of activation rate compounds.

## 2. When shown

- First install only (state flag in account).
- Re-playable from Settings → Help → "Replay onboarding."

## 3. Layout — Phase 1: Welcome

```
┌────────────────────────────────────────────────────────────────┐
│                                                                  │
│                                                                  │
│                          NEXUS                                    │
│                                                                  │
│                                                                  │
│              What do you want accomplished?                      │
│                                                                  │
│      NEXUS is built around what you want to do,                  │
│         not where you want to go.                                 │
│                                                                  │
│                                                                  │
│                          [Get started]                           │
│                                                                  │
│                                                                  │
│   ●────○────○                                                    │
│   Welcome  Profile  First Intent                                  │
└────────────────────────────────────────────────────────────────┘
```

A full-screen centered hero.

## 4. Component anatomy — Welcome (3 panels)

3 swipeable panels, each with:

- Icon (96px).
- Headline (text-3xl).
- Body (1–2 sentences, text-lg).
- Dot pagination.

Panel 1: "What do you want accomplished?"
Panel 2: "Your AI team"
Panel 3: "Your workspaces"

Footer: "Get started" button (default focus).

## 5. Layout — Phase 2: Profile Setup

```
┌────────────────────────────────────────────────────────────────┐
│                                                                  │
│   Tell us about you                                              │
│                                                                  │
│   Role                                                           │
│   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│   │  Founder     │  │  Developer   │  │  Researcher  │         │
│   └──────────────┘  └──────────────┘  └──────────────┘         │
│   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│   │  Operator    │  │  Marketer    │  │  Designer    │         │
│   └──────────────┘  └──────────────┘  └──────────────┘         │
│   ┌──────────────┐                                                 │
│   │  Other       │                                                 │
│   └──────────────┘                                                 │
│                                                                  │
│   What do you most want NEXUS to do for you?                     │
│   ┌──────────────────────────────────────────────────────┐      │
│   │ Help me run my business without hiring.              │      │
│   └──────────────────────────────────────────────────────┘      │
│                                                                  │
│   Email                                                          │
│   ┌──────────────────────────────────────────────────────┐      │
│   │ you@example.com                                      │      │
│   └──────────────────────────────────────────────────────┘      │
│                                                                  │
│   ☐ Continue with Google                                         │
│   ☐ Continue with GitHub                                         │
│   ☐ Continue with Apple                                          │
│                                                                  │
│                                          [Continue]              │
│                                                                  │
│   ●────●────○                                                    │
└────────────────────────────────────────────────────────────────┘
```

## 6. Component anatomy — Profile Setup

- Role chips (selectable, single).
- Goal textarea (140 char max).
- Email input.
- OAuth buttons.
- "Continue" button (primary, disabled until email + role set).

## 7. Layout — Phase 3: First Intent

```
┌────────────────────────────────────────────────────────────────┐
│                                                                  │
│   Try your first command                                         │
│                                                                  │
│   We picked one for you based on your role. Change it if you    │
│   want, or write your own.                                       │
│                                                                  │
│   ┌──────────────────────────────────────────────────────┐      │
│   │ Generate a week's content calendar for my product    │      │
│   └──────────────────────────────────────────────────────┘      │
│                                                                  │
│   Or try one of these:                                           │
│   • Summarize today's top 5 articles on AI startups             │
│   • Find 10 SaaS ideas I could build this weekend               │
│   • Monitor a website for changes                               │
│                                                                  │
│                                                                  │
│                                              [Run]               │
│                                                                  │
│   ●────●────●                                                    │
└────────────────────────────────────────────────────────────────┘
```

After Run:
```
┌────────────────────────────────────────────────────────────────┐
│                                                                  │
│   Generating your content calendar...                            │
│                                                                  │
│   ┌─ Plan ──────────────────────────────────────────────┐       │
│   │ 1.  Identify topics in your product space   ✓        │       │
│   │ 2.  Draft 7 posts                            ⟳        │       │
│   │ 3.  Format for 3 platforms                  ◯        │       │
│   └──────────────────────────────────────────────────────┘       │
│                                                                  │
└────────────────────────────────────────────────────────────────┘
```

Then success:
```
┌────────────────────────────────────────────────────────────────┐
│                                                                  │
│                       ✓ Done                                     │
│                                                                  │
│      You just completed your first task.                         │
│                                                                  │
│   ┌──────────────────────────────────────────────────────┐      │
│   │  Preview of your week 1 content calendar...           │      │
│   │  [expand]                                             │      │
│   └──────────────────────────────────────────────────────┘      │
│                                                                  │
│                                              [Continue]          │
└────────────────────────────────────────────────────────────────┘
```

## 8. Component anatomy — First Intent

- Pre-filled suggestion (editable).
- 3 alternative suggestions.
- Run button.
- Plan viewer (per NX-UI-6003).
- Success state with task preview.
- Continue button.

## 9. Layout — Phase 4: Personalize

(Skipped for brevity — settings panel per NX-UI-6009 subset.)

## 10. Interactions

### Welcome

| Trigger | Action |
|---------|--------|
| Click "Get started" | Move to Profile |
| Click pagination dot | Jump to panel |
| Arrow keys | Navigate panels |
| Esc | Skip (advanced) |

### Profile

| Trigger | Action |
|---------|--------|
| Click role chip | Select role |
| Type in goal | Update goal |
| Type in email | Update email |
| Click OAuth button | Begin OAuth |
| Click Continue | Move to First Intent |

### First Intent

| Trigger | Action |
|---------|--------|
| Click Run | Execute |
| Click suggestion | Fill prompt |
| Edit prompt | Override suggestion |
| After success → Continue | Land on home screen |

## 11. States

Each phase has standard states (loading, error, success) per NX-DS-5012.

The **First Intent phase has the strictest error handling** — failures must not block activation. On failure:

- Show "Something didn't work. Try a different one?"
- Display 2 simpler alternatives.
- Offer "Skip for now — I'll explore."

## 12. Animation

- Panel transitions: 240ms cross-fade.
- Role chip selection: 80ms scale 0.95 → 1.
- Plan streaming: per NX-DS-5006.
- Success: ✓ fade-in 60ms.
- Reduced-motion: instant.

## 13. Accessibility

- All phases keyboard navigable.
- Form fields properly labeled.
- Plan steps announced.
- Skip option available.
- Screen reader announces phase progress.

## 14. Telemetry

- `onboarding.started`
- `onboarding.welcome_completed`
- `onboarding.profile_completed`
- `onboarding.first_intent_started`
- `onboarding.first_intent_succeeded`
- `onboarding.first_intent_failed`
- `onboarding.completed`
- `onboarding.skipped`

## 15. Out of scope

- Voice onboarding (H2).
- Multi-user onboarding (H2).
- Custom onboarding flows (H2 enterprise).

## 16. Acceptance criteria

- [ ] Welcome <2s to first panel.
- [ ] Profile setup <2 minutes for 90% of users.
- [ ] First Intent succeeds for ≥70% of users.
- [ ] Failure recovery: skip path always available.
- [ ] All locales render correctly.

## 17. Reading list

- **Onboarding Specification** — NX-PRD-0004
- **Home Screen** — NX-UI-6001
- **AI Command Bar** — NX-UI-6003

---

*End NX-UI-6011.*