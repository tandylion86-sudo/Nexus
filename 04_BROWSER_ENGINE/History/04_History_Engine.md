# NX-ARCH-0104 — History Engine

| Field | Value |
|-------|-------|
| **Document ID** | NX-ARCH-0104 |
| **Title** | History Engine |
| **Phase** | 6 — Browser Architecture |
| **Owner** | Browser AI (NX-AGENT-7056) |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-07-02 |
| **Depends on** | NX-ARCH-0001, NX-ARCH-0103 (Profile System), NX-ARCH-0105 (Sync) |

---

## 1. Mission

Capture, index, and surface the user's browsing history — across profiles, across local and cloud, for the user and for agents — while preserving per-profile isolation and giving the user control over retention.

## 2. What is captured

A **history entry** is created when the user (or an authorized agent on the user's behalf) navigates a page. Captured:

- URL (canonicalized).
- Title.
- Visit timestamp.
- Referrer URL.
- Transition type (typed, link, redirect, form submission, etc.).
- Active profile at the time.
- Active tab ID (for session reconstruction).
- Page-load duration (for performance telemetry).
- Optional: page summary (H2, see §10).

**Not captured** by default:

- Form field values.
- POST bodies.
- Pages visited in Incognito profile (see §7).
- Pages where the user has explicitly opted out (per §6).

## 3. Storage

Local history is per-profile (`history.sqlite` under the profile root per NX-ARCH-0103 §4). Cloud history is per-account in PostgreSQL, partitioned by profile.

The local store is a SQLite database with three tables:

```
visits (id, url_id, profile_id, timestamp, transition, referrer_url_id, tab_id, load_ms)
urls (id, canonical_url, title, last_visit, visit_count)
favicons (url_id, icon_blob, last_updated)
```

Indexes on `urls.canonical_url`, `visits.timestamp`, `visits.profile_id`.

Cloud store follows the same schema, replicated via NX-ARCH-0105 (Sync Protocol). Cloud adds:

- A search index (per NX-FEAT-2808 Onboarding Progress, similar — Postgres full-text in H1, dedicated search service H2+).
- Aggregate analytics tables (per NX-FEAT-1614).

## 4. Retention

| Mode | Default retention | Configurable | Hard cap |
|------|------------------:|--------------|---------:|
| Standard profile | Forever | Yes (30 days / 1 year / forever) | 10 years |
| Incognito profile | None (no history written) | n/a | n/a |
| Agent profile (H2) | Configurable per agent | Yes | 1 year default |
| Cloud profile | Per sync rules | Yes | 10 years |

User can:

- Delete individual entries.
- Delete by time range.
- Delete by URL pattern.
- Delete by domain.
- Wipe a profile's history.
- Wipe all history (across all profiles, single action — rare, audited).

All deletions are logged in the account activity log.

## 5. Search and surfacing

History is searchable:

- **URL substring match** (instant, client-side).
- **Title substring match** (instant, client-side).
- **Full-text search** (cloud side, returns ranked results).
- **Time range filter.**
- **Profile filter.**
- **Visit count filter** ("show me pages I've visited more than 5 times").

Surfaced to:

- The NEXUS address bar (in-line suggestions).
- The History panel in the browser.
- The Memory Engine (NX-AGENT-7010) — agents can query "what was the URL I visited last Tuesday about X?"
- The Command Bar (NX-UI-6003) — natural-language queries.

## 6. Privacy controls

- **Per-URL opt-out.** Pages can be excluded from history via a "don't record history for this site" toggle.
- **Per-domain opt-out.** Toggle applies to all subdomains.
- **Sensitive-domain detection.** NEXUS maintains a default list of sensitive domains (banking, health) that are excluded from cloud sync by default; user must explicitly opt in. (This list is local; not phoned home.)
- **History pause.** A global toggle that stops new history entries from being written.
- **Incognito-equivalent profile.** A profile marked "private" writes no history at all (NX-ARCH-0103 §7 — Incognito is a profile-level flag, not a separate mode).
- **Cloud sync opt-in.** History syncs to cloud only if the user has history sync enabled (default: on for standard profiles).

## 7. Incognito semantics

NEXUS does not have a "private window" mode like other browsers. Instead, **a private profile** is a profile that:

- Does not write history.
- Does not write to caches beyond the session.
- Does not store cookies beyond the session.
- Is automatically suspended on close (cookies wiped; disk state encrypted and held for crash recovery, then wiped).

This is a stronger privacy guarantee than "incognito window inside a non-private profile" because there's no risk of leakage via the containing profile.

The agent bridge does not have access to private profiles unless explicitly authorized by the user, and that authorization is profile-scoped and audit-logged.

## 8. Agent access to history

Agents can access history *for the profile they are scoped to* (per NX-ARCH-0103 §7), with the same restrictions as the user:

- Read access by default (with audit).
- Search access by default.
- Write/delete access is rare and always user-approved.

Agent access to history is a powerful feature for research and research agents. It's also a privacy risk; the audit log (NX-AGENT-7015) captures every read.

## 9. Cross-profile history

By default, history is per-profile and not searchable across profiles. The user can:

- **Enable cross-profile search** (per-account setting) — searches return results tagged with profile.
- **Create a "merged" view** — for users who want a unified history across all standard profiles.

The cross-profile feature is opt-in because it can reveal patterns the user may not want to surface to themselves (e.g., "you have a work calendar and a dating-app profile that overlap on Tuesday evenings").

## 10. Page summaries (H2)

In H2, history entries gain a page summary (LLM-generated, 1–2 sentences) and a topic tag. This is opt-in and computed server-side. The agent can use summaries instead of fetching the page again.

H1 does not generate summaries; it stores the URL, title, and metadata only.

## 11. Performance

- **Local search** of 100K entries < 50ms (indexed SQLite).
- **Cloud search** of 10M entries < 500ms (Postgres + GIN index).
- **Insert throughput** 1000 entries/second sustained per profile (rare workload; history is usually sparse).
- **Memory footprint** of in-process cache < 50MB.

## 12. Open questions

- Q: How do we handle history of pages that have since been deleted from the web? (We have the title and timestamp; should we offer an "archive this" feature?)
- Q: Should NEXUS ship a "reading list" feature separate from history? (Probably yes; H2.)
- Q: Do we support history export (per user requests for backup)?
- Q: What's the right default retention for agent profiles (H2)?

## 13. Reading list

- **Overview** — NX-ARCH-0001
- **Profile System** — NX-ARCH-0103
- **Sync Protocol** — NX-ARCH-0105
- **Memory Schema** — NX-AGENT-7010
- **Cloud Browser Fleet** — NX-FEAT-1600
- **Usage analytics** — NX-FEAT-1614
- **Guardrails & Safety** — NX-AGENT-7015

---

*End NX-ARCH-0104.*
