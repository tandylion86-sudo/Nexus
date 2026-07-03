# NX-FEAT-1600 — Cloud Browser Fleet (Anchor Spec)

| Field | Value |
|-------|-------|
| **Document ID** | NX-FEAT-1600 |
| **Title** | Cloud Browser Fleet (Anchor Spec) |
| **Area** | NX-FEAT-A0007 — Cloud Browser Fleet |
| **Owner** | Backend AI + Browser AI |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-06-30 |
| **Priority (H1)** | P0 |
| **Horizon target** | H1 |
| **Estimated effort** | XL (decomposed into NX-FEAT-1601-1614) |

---

## 1. Purpose

A **Cloud Browser** is a persistent, isolated Chromium-based browser container running in NEXUS's cloud infrastructure. It maintains its own cookies, local storage, profiles, and proxy. It can be live-viewed, scheduled to run tasks, snapshotted, and restored.

The **Cloud Browser Fleet** is the user's pool of Cloud Browsers. The Fleet is what allows NEXUS to do parallel, persistent, scheduled, multi-account web automation.

This document is the anchor spec; leaf features (NX-FEAT-1601 through 1614) inherit from it.

## 2. Why Cloud Browsers

Some web tasks cannot happen in a local browser:

- The user has closed their laptop.
- The task needs to run on a schedule (every hour, every Monday).
- The task needs a different identity (proxy, fingerprint, cookies).
- The user wants to watch what an agent is doing without disrupting their own session.

Cloud Browsers solve these by providing a remote, persistent, isolated browser environment.

## 3. User stories

- As **Maya**, I want a Cloud Browser that runs my LinkedIn outreach agent while I sleep, so I wake up to a full report.
- As **Devin**, I want 3 Cloud Browsers with different fingerprints to test cross-browser behavior.
- As **Sara**, I want a Cloud Browser that scrapes a paywalled source on my behalf.
- As **Marcus**, I want a Cloud Browser that monitors competitor prices every hour and emails me on changes.
- As **Riya**, I want a Cloud Browser that runs my morning briefing workflow.
- As **Thea**, I want shared Cloud Browsers so my team can collaborate on investigations.

## 4. Functional requirements

### FR-1: Create Cloud Browser
**Description:** A user creates a new Cloud Browser from the Fleet dashboard or via API.
**Acceptance:**
- [ ] Creation completes in <30 seconds.
- [ ] Browser is assigned a unique ID and stored.
- [ ] User can name the browser (e.g., "LinkedIn outreach").
- [ ] User can assign a region (US, EU, APAC).
- [ ] Default fingerprint and proxy are assigned (configurable).

### FR-2: Idle persistence
**Description:** A Cloud Browser does not terminate when the user closes their local app. It remains in an idle state, ready to be resumed.
**Acceptance:**
- [ ] Cloud Browser remains running for at least 30 days of inactivity.
- [ ] Disk state (cookies, storage, downloads) persists.
- [ ] User can configure idle timeout (H2).
- [ ] Idle Browsers are billed at a reduced rate (50%).

### FR-3: Session resume
**Description:** A user resumes a Cloud Browser from any device; the session state is exactly as left.
**Acceptance:**
- [ ] Resume completes in <5 seconds.
- [ ] Open tabs are restored.
- [ ] Cookies and storage are preserved.
- [ ] Active downloads are paused and resumable.

### FR-4: Per-browser cookies & storage
**Description:** Each Cloud Browser has completely isolated cookies, local storage, IndexedDB, and service workers.
**Acceptance:**
- [ ] No state leaks between browsers.
- [ ] User can export cookies (e.g., to import into another browser).
- [ ] User can clear cookies/storage manually.

### FR-5: Per-browser proxy assignment
**Description:** Each Cloud Browser can be assigned a proxy. Proxies may be residential, datacenter, or custom.
**Acceptance:**
- [ ] Built-in proxy pool: 100+ IPs across 50 countries.
- [ ] User can bring their own proxy (string in settings).
- [ ] Proxy health is monitored; failed proxies are auto-replaced.
- [ ] Proxy assignment is logged in Activity Log.

### FR-6: Per-browser fingerprint profile
**Description:** Each Cloud Browser has a configurable fingerprint profile (UA, screen size, fonts, language, WebGL, etc.).
**Acceptance:**
- [ ] Default fingerprint is realistic and varied per browser.
- [ ] User can pick from preset profiles (Windows Chrome, macOS Safari, etc.).
- [ ] Custom fingerprint editing available (advanced).
- [ ] Fingerprint is consistent within a browser session.

### FR-7: Live remote view
**Description:** A user can see what a Cloud Browser is doing in real time via a streamed view.
**Acceptance:**
- [ ] View loads in <2 seconds.
- [ ] View updates at ≥10 fps.
- [ ] User can interact with the view (clicks, typing) as if local.
- [ ] View auto-pauses on inactivity to save bandwidth.

### FR-8: Scheduled tasks
**Description:** Cloud Browsers can run workflows on a schedule.
**Acceptance:**
- [ ] Cron-style schedule: every N minutes/hours/days; specific times.
- [ ] Schedule respects timezone.
- [ ] Failure retries per workflow policy.
- [ ] History of runs is accessible.

### FR-9: Multi-user collaboration
**Description:** Team members can share a Cloud Browser session (team plans).
**Acceptance:**
- [ ] Multiple users can live-view simultaneously.
- [ ] Only one user has "control" at a time.
- [ ] Activity log shows all participants.
- [ ] Permissions: viewer / controller.

### FR-10: Snapshot & restore
**Description:** A Cloud Browser state can be snapshotted and restored.
**Acceptance:**
- [ ] Snapshot captures: tabs, cookies, storage, downloads, agent state.
- [ ] Snapshots are stored in user storage.
- [ ] Restore creates a new browser from a snapshot.
- [ ] Snapshots can be scheduled (e.g., daily).

### FR-11: Bandwidth controls
**Description:** Users can cap Cloud Browser bandwidth.
**Acceptance:**
- [ ] Cap is per browser and per user.
- [ ] When cap is reached, browsers throttle.
- [ ] User is notified when cap is approached.

### FR-12: Resource limits
**Description:** Each Cloud Browser has CPU, RAM, and disk quotas.
**Acceptance:**
- [ ] Default: 1 CPU, 2 GB RAM, 10 GB disk.
- [ ] Limits are configurable per browser.
- [ ] When limit is reached, browser degrades gracefully.

### FR-13: Fleet dashboard
**Description:** A single UI shows all of a user's Cloud Browsers.
**Acceptance:**
- [ ] Shows: name, status, last active, scheduled tasks, current proxy.
- [ ] Filters: by status, by Workspace, by tag.
- [ ] Bulk actions: start, stop, snapshot, delete.
- [ ] Total usage (hours, bandwidth) shown.

### FR-14: Usage analytics
**Description:** Detailed analytics on Cloud Browser usage.
**Acceptance:**
- [ ] Hours per browser per day/week/month.
- [ ] Bandwidth per browser.
- [ ] Most-used sites per browser.
- [ ] Cost to date.

## 5. Non-functional requirements

### NFR-1: Performance
- Browser resume: <5 seconds.
- Live view latency: <500ms.
- Schedule accuracy: within 1 minute.
- Provisioning: <30 seconds for a new browser.

### NFR-2: Reliability
- Cloud Browser uptime: 99.5% (target), 99.9% (H2).
- State durability: 99.999% (no data loss).
- Region failover: optional in H2.

### NFR-3: Security
- All Cloud Browser traffic encrypted (TLS 1.3+).
- Per-user encryption of stored state.
- No cross-user data leakage.
- Session hijacking prevention (WebSocket auth + per-session tokens).
- Bot detection mitigation via fingerprinting and proxy rotation.

### NFR-4: Privacy
- NEXUS does not log Cloud Browser content (only metadata).
- User can disable all telemetry.
- Compliance: GDPR, CCPA.

### NFR-5: Cost
- Idle rate: $0.05/hour equivalent.
- Active rate: $0.10/hour equivalent.
- Storage: $0.02/GB/month.

## 6. UI surfaces

| Surface | Reference |
|---------|-----------|
| Fleet dashboard | NX-UI-6301 |
| Browser detail view | NX-UI-6302 |
| Create Cloud Browser | NX-UI-6303 |
| Live remote view | NX-UI-6304 |
| Schedule manager | NX-UI-6305 |
| Snapshot manager | NX-UI-6306 |
| Usage analytics | NX-UI-6307 |

## 7. Permissions

Cloud Browsers require:

- Create: any paid user (within plan limits).
- Run tasks: agent permission to invoke Cloud Browser action.
- View: workspace member.
- Configure: workspace owner/admin.
- Share: workspace owner/admin.

## 8. Telemetry

Events emitted (opt-in):

- `cloud_browser.created`
- `cloud_browser.resumed`
- `cloud_browser.idle`
- `cloud_browser.scheduled_task.ran`
- `cloud_browser.snapshot.created`
- `cloud_browser.deleted`

Activity Log captures per-task details regardless.

## 9. Failure modes

| Failure | Behavior |
|---------|----------|
| Region outage | Auto-failover (H2); show user notification |
| Disk full | Auto-cleanup of old downloads; notify user |
| Proxy failure | Auto-replace with healthy proxy |
| Browser crash | Auto-restart; state preserved; notify user |
| Live view lag | Auto-degrade to lower fps |
| Schedule overrun | Skip if previous run still active; notify |

## 10. Dependencies

- Chromium engine (Phase 6).
- Browser automation framework (Playwright).
- Container orchestration (Kubernetes).
- Storage (S3-compatible).
- Memory Engine for task state.
- Agent Orchestrator for executing scheduled workflows.

## 11. Out of scope

- Real browser fingerprint spoofing at hardware level (deferred).
- Voice-driven Cloud Browser control (H2).
- Cloud Browser rentals to other users (H3+).
- NEXUS-operated Cloud Browsers on customer cloud (H3+).

## 12. Acceptance criteria summary

The Cloud Browser Fleet is done when:

- [ ] User can create 5 Cloud Browsers in <2 minutes total.
- [ ] A Cloud Browser survives a 7-day idle period.
- [ ] Resume time <5 seconds.
- [ ] Live view streams at ≥10 fps.
- [ ] Scheduled task fires within 1 minute of target time.
- [ ] Per-browser cookies/storage are fully isolated.
- [ ] 99.5% uptime measured weekly.

## 13. Sub-features (leaf specs)

| ID | Name |
|----|------|
| NX-FEAT-1601 | Create Cloud Browser |
| NX-FEAT-1602 | Cloud Browser idle persistence |
| NX-FEAT-1603 | Cloud Browser session resume |
| NX-FEAT-1604 | Per-browser cookies & storage |
| NX-FEAT-1605 | Per-browser proxy |
| NX-FEAT-1606 | Per-browser fingerprint profile |
| NX-FEAT-1607 | Live remote view |
| NX-FEAT-1608 | Scheduled tasks |
| NX-FEAT-1609 | Multi-user collaboration |
| NX-FEAT-1610 | Snapshot & restore |
| NX-FEAT-1611 | Bandwidth controls |
| NX-FEAT-1612 | Resource limits |
| NX-FEAT-1613 | Fleet dashboard |
| NX-FEAT-1614 | Usage analytics |

## 14. Open questions

- Q: How aggressively should we rotate proxies for organic-feeling browsing?
- Q: Should scheduled tasks run in headless mode by default to save resources?
- Q: How do we handle websites that explicitly block known datacenter IPs?
- Q: Should we ship our own proxy network or partner with existing providers?

## 15. Change log

| Date | Change | Author |
|------|--------|--------|
| 2026-06-30 | Initial anchor spec | Backend AI |

---

*End NX-FEAT-1600.*