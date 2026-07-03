# NX-UI-6005 — Agent Marketplace

| Field | Value |
|-------|-------|
| **Document ID** | NX-UI-6005 |
| **Screen** | Agent Marketplace |
| **Owner** | Frontend AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P1 |
| **Touches journeys** | J-08 |
| **Touches features** | NX-FEAT-1501-1514 |

---

## 1. Purpose

The Agent Marketplace is the **browse, install, and review surface** for agents. Users discover agents by category, search, or featured collections; install with one click; and review their experience.

## 2. When shown

- Triggered by clicking Marketplace icon in sidebar.
- Triggered by ⌘⇧M / Ctrl+Shift+M.
- Reachable from any "Browse agents" link.

## 3. Layout

```
┌────────────────────────────────────────────────────────────────┐
│  Marketplace                                          [⌘⇧M]   │
├──────────────┬─────────────────────────────────────────────────┤
│  Categories  │  🔍 Search agents...                              │
│              │                                                   │
│  Business    │  Featured                                         │
│  Developer   │  ┌────────────┐ ┌────────────┐ ┌────────────┐ │
│  Research    │  │ LinkedIn   │ │ GitHub     │ │ Price      │ │
│  Security    │  │ Outreach   │ │ Triage     │ │ Monitor    │ │
│  Creative    │  │ ★ 4.8      │ │ ★ 4.6      │ │ ★ 4.9      │ │
│  Personal    │  │ Pro plan   │ │ Free       │ │ $5/mo      │ │
│              │  └────────────┘ └────────────┘ └────────────┘ │
│  Collections │                                                   │
│              │  Trending this week                              │
│  For Solo    │  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐│
│  For Teams   │  │      │ │      │ │      │ │      │ │      ││
│  Verified    │  └──────┘ └──────┘ └──────┘ └──────┘ └──────┘│
│              │                                                   │
│  Verified    │  All agents                                       │
│              │  ┌──────────────────────────────────────────┐   │
│              │  │ Listing row                                │   │
│              │  └──────────────────────────────────────────┘   │
│              │  ┌──────────────────────────────────────────┐   │
│              │  │ Listing row                                │   │
│              │  └──────────────────────────────────────────┘   │
└──────────────┴─────────────────────────────────────────────────┘
```

## 4. Component anatomy

### Sidebar (240px)
- Categories list with counts.
- Collections list.
- "Verified only" toggle.
- Filters: free / paid / first-party / third-party.

### Search bar (top)
- Live search across name, description, tags.
- Filters appear as chips below.

### Featured row
- 3 large cards (300×200).
- Auto-rotating.
- "Featured collection" link.

### Trending row
- 5 smaller cards (180×140).
- "Trending this week" header.
- Updates daily.

### All agents list
- Full-width rows.
- Each row: avatar, name, short description, rating, install count, price.
- Sort: relevance / rating / installs / recency.

### Agent card (mini)
- 180×140.
- Avatar (32px), name (semibold), short description (2 lines).
- Rating, install count, price.

### Agent card (large)
- 300×200.
- Larger avatar (48px).
- Description (3 lines).
- "Verified" badge if applicable.
- "Install" button.

## 5. Interactions

| Trigger | Action |
|---------|--------|
| Click category | Filter list |
| Type search | Live filter |
| Click featured card | Open detail (NX-UI-6005 sub-screen) |
| Click install | Begin install flow |
| Click sort | Change sort |
| Click filter | Apply filter |

## 6. States

### Default
- Featured row + Trending + All agents.

### Loading
- Skeleton rows (3 featured, 5 trending, 10 list).

### Empty results
- "No agents match. Try clearing filters."

### Search active
- Filtered list; counts update.
- "Clear filters" button.

### Installing
- Card shows progress.
- "Installing…" replaces "Install" button.

### Installed
- Card shows "Installed ✓"; can click "Open" or "Manage."

## 7. Animation

- Featured cards: stagger 60ms.
- Trending row: stagger 30ms.
- Filter change: cross-fade 160ms.
- Install progress: linear bar.
- Reduced-motion: instant.

## 8. Accessibility

- Each card is a button with full label.
- Search has label.
- Filters are toggleable; state announced.
- Keyboard nav across cards (arrow keys).

## 9. Telemetry

- `marketplace.viewed`
- `marketplace.searched`
- `marketplace.filtered`
- `marketplace.card_clicked`
- `marketplace.install_clicked`

## 10. Out of scope

- Publishing UI (separate screen, NX-UI-6012 sub-screen).
- Creator dashboard (NX-UI-6012).

## 11. Acceptance criteria

- [ ] Page loads in <1s.
- [ ] Search returns in <500ms.
- [ ] Install completes in <10s.
- [ ] Filters compose correctly.
- [ ] Keyboard nav reaches every card.

## 12. Reading list

- **Agent Marketplace Anchor** — NX-FEAT-1500
- **Onboarding** — NX-PRD-0004

---

*End NX-UI-6005.*