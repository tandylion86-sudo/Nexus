# NX-PRD-0003 — User Journeys

| Field | Value |
|-------|-------|
| **Document ID** | NX-PRD-0003 |
| **Title** | User Journeys |
| **Phase** | 2 — Complete PRD |
| **Owner** | Product |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-06-30 |
| **Depends on** | NX-DOC-0007 (Audiences), NX-FEAT-0001 (Feature Inventory), NX-PRD-0002 (Persona Matrix) |

---

## 1. Purpose

A user journey is a **narrative trace of how a specific persona achieves a specific outcome** using NEXUS. Journeys are how we discover edge cases, identify friction, and ensure cross-feature composition works.

This document defines the **20 canonical H1 journeys**. Every feature should serve at least one journey; ideally several. A feature that serves no journey is removed.

## 2. Journey template

Each journey follows the same template:

```markdown
### J-NN: <Journey name>
**Persona:** <code>
**Outcome:** <one-sentence goal>
**Trigger:** <what starts the journey>
**Pre-conditions:** <what must be true>
**Steps:**
1. <User action / system response>
2. ...
**Success criteria:** <how we know it worked>
**Failure modes:** <what can go wrong>
**Metrics:** <what we measure for this journey>
**Features used:** <NX-FEAT-#### list>
```

## 3. The 20 canonical H1 journeys

### J-01: Maya generates a week of social content

**Persona:** P-MAYA (Solo Operator)
**Outcome:** 7 days of social media posts ready for review.
**Trigger:** Empty Workspace, user types "Generate a week of social posts about [topic]."
**Pre-conditions:** Account created, at least one Workspace.

**Steps:**
1. User opens NEXUS, lands on home screen.
2. Types intent: "Generate a week of social posts about [topic]."
3. Planner proposes a 7-day content calendar with platform splits.
4. User reviews plan, clicks "Approve."
5. Researcher agent gathers trends and prior posts (RAG over uploaded docs).
6. Writer agent drafts 7 posts in user's style.
7. Reviewer agent checks tone, brand fit, length.
8. Posts are saved to a new Workspace "Social: Week of [date]."
9. User reviews in chat, asks for 2 revisions.
10. Final posts are exported to Notion.

**Success criteria:** ≤3 minutes from intent to draft-ready. User edits ≤20% of words.
**Failure modes:** Model rate limit (fall back to local); user style memory is sparse (ask 1 question).
**Metrics:** Time-to-first-draft, edit ratio, exports completed.
**Features used:** NX-FEAT-1201, 1202, 1203, 1208, 1401, 1402, 1404, 1406, 1412, 1704, 2305 (Notion).

---

### J-02: Devin triages GitHub issues with an agent

**Persona:** P-DEVIN (Developer)
**Outcome:** A prioritized list of issues with proposed responses.
**Trigger:** User opens "DevOps" Workspace, types "Triage today's issues."
**Pre-conditions:** GitHub integration connected; Cloud Browser session live.

**Steps:**
1. User invokes the Triage agent from the marketplace (one-click install).
2. Agent fetches today's issues via GitHub API.
3. Agent runs sub-agents in parallel: Classifier, Prioritizer, Drafter.
4. Classifier sorts by type (bug, feature, question).
5. Prioritizer scores by impact, mentions, recency.
6. Drafter proposes a response for each.
7. Plan displays in chat with grouped issues.
8. User reviews, accepts/regenerates responses.
9. Approved responses are posted as comments.
10. Summary saved to memory: "Daily triage — Aug 2026."

**Success criteria:** 50 issues triaged in <5 minutes. 80% of drafts accepted.
**Failure modes:** GitHub rate limit (queue + retry); repo permissions insufficient (graceful fail).
**Metrics:** Issues processed per minute, draft acceptance rate.
**Features used:** NX-FEAT-1401, 1404, 1410, 1411, 1501, 1503, 1702, 2205, 2304.

---

### J-03: Sara researches a company over three days

**Persona:** P-SARA (Researcher)
**Outcome:** A 30-page dossier on a target company, cited, organized.
**Trigger:** Sara opens "Investigation: Acme Corp" Workspace.
**Pre-conditions:** Memory engine active; cloud model access; ample bandwidth.

**Steps:**
1. Sara sets Workspace goal: "Build a dossier on Acme Corp."
2. Day 1: Sara types "Research Acme's leadership and recent news."
3. Researcher agent runs multi-source web searches, saving sources to memory.
4. Sara reviews sources, marks 5 as canonical.
5. Day 2: Sara asks "Compare Acme to two competitors."
6. Agent pulls competitor info, builds comparison table (inline artifact).
7. Day 3: Sara asks "Draft executive summary."
8. Agent synthesizes from memory, citing every claim.
9. Sara edits; agent updates memory with corrections.
10. Dossier exported as Markdown + sources JSON.

**Success criteria:** Every claim is sourced. Dossier builds incrementally across days.
**Failure modes:** Source unavailable (mark as unverified); model drifts (regenerate from memory).
**Metrics:** Source coverage, days-to-dossier, citation accuracy.
**Features used:** NX-FEAT-1106, 1201, 1203, 1301, 1303, 1701-1714, 1713 (KG), 1714 (RAG).

---

### J-04: Marcus monitors competitor prices hourly

**Persona:** P-MARCUS (Operator)
**Outcome:** Hourly price check, alert on >5% changes.
**Trigger:** User installs "Price Monitor" workflow template.
**Pre-conditions:** Workspace created; scheduled tasks enabled; notifications on.

**Steps:**
1. Marcus opens Workflow Builder, selects "Price Monitor" template.
2. Configures: URLs (10 product pages), threshold (5%), notification channel (email).
3. Workflow saves; first run is immediate.
4. Cloud Browser opens each URL, extracts price, compares to last value.
5. Changed prices (>5%) are recorded; email alert is sent.
6. Marcus reviews daily digest, sees 2 alerts.
7. Clicks alert, opens Cloud Browser snapshot to investigate.

**Success criteria:** Workflow runs every hour without intervention. Alerts are accurate.
**Failure modes:** Site structure changes (alert user); site blocks scraper (use proxy); product out of stock (mark N/A).
**Metrics:** Run success rate, false-positive rate, time-to-alert.
**Features used:** NX-FEAT-1601, 1608, 1801-1812, 2301 (email), 2201, 2203.

---

### J-05: Riya builds a personal daily briefing

**Persona:** P-RIYA (Power User)
**Outcome:** Every morning at 7am, a personalized briefing lands in Workspace.
**Trigger:** Scheduled workflow she built herself.
**Pre-conditions:** Local AI preferred; integrations set up.

**Steps:**
1. Riya creates Workflow: trigger = schedule (07:00 weekdays).
2. Step 1: Read calendar for today's events.
3. Step 2: Read inbox for unread important messages.
4. Step 3: Read Hacker News top stories.
5. Step 4: Synthesize into 200-word briefing.
6. Step 5: Save to "Daily Briefing" Workspace and notify.

**Success criteria:** Briefing arrives at 07:00 ±1 minute. Riya reads it.
**Failure modes:** Calendar API down (skip step, note in briefing); local model slow (fall back to cloud).
**Metrics:** On-time rate, open rate.
**Features used:** NX-FEAT-1801-1812, 2301, 2302, 2203, 2601-2603.

---

### J-06: Thea shares a research dossier with her team

**Persona:** P-THEA (Team Lead)
**Outcome:** Team members see and contribute to a shared dossier.
**Trigger:** Thea clicks "Share" on Workspace.
**Pre-conditions:** Team plan active; team members invited.

**Steps:**
1. Thea opens "Q4 Market Map" Workspace.
2. Clicks "Share" → selects "Team Research."
3. Sets permissions: members can edit, comment, but not delete.
4. Members receive notification, open shared Workspace.
5. Each member adds sources via intent: "Add this article about [topic]."
6. Agent deduplicates and re-sorts.
7. Thea reviews daily, sees activity stream.
8. Members can ask "What's new?" — agent summarizes.

**Success criteria:** All 5 team members contribute ≥1 source within a week.
**Failure modes:** Permission mismatch (request upgrade); member outside team (invite flow).
**Metrics:** Member activation rate, sources per member.
**Features used:** NX-FEAT-1110, 1401, 1702, 2205, 2209, 2901 (SSO).

---

### J-07: First-run onboarding for any persona

**Persona:** any
**Outcome:** User completes first successful task in <15 minutes.
**Trigger:** Account just created.
**Pre-conditions:** NEXUS installed; account created.

**Steps:**
1. Welcome screen (3 panels: intent, AI, workspace).
2. User picks a sample Workspace based on persona inference (or "Let me pick").
3. Sample agents pre-installed.
4. First-run intent shown: "Try: Generate this week's content."
5. Agent executes; result shown in chat with citations.
6. User prompted to customize (tone, format, language).
7. Memory captures preferences.
8. Tooltip tour of key UI surfaces.
9. Onboarding complete; user lands on home screen.

**Success criteria:** ≥70% of new users complete activation task.
**Failure modes:** User dismisses onboarding (offer replay); model fails (fallback content).
**Metrics:** Activation rate, time-to-first-task, onboarding completion.
**Features used:** NX-FEAT-2801-2810, 1101, 1201, 1506, 1701.

---

### J-08: User installs a marketplace agent

**Persona:** any
**Outcome:** Agent installed and used successfully.
**Trigger:** User browses Marketplace.
**Pre-conditions:** Account, internet.

**Steps:**
1. User clicks Marketplace icon.
2. Browses by category or searches.
3. Selects "LinkedIn Outreach" agent.
4. Detail page shows: description, permissions required (read inbox, send message), ratings, creator.
5. User clicks Install.
6. Permission prompt: "LinkedIn Outreach needs: read email, send messages. Approve?"
7. User approves; agent installed to default Workspace.
8. User invokes agent: "Reach out to 20 prospects from [CSV]."
9. Plan displays; agent executes.
10. Activity log records all actions.

**Success criteria:** Install in ≤3 clicks. Permissions clearly explained.
**Failure modes:** Permissions rejected (agent still installs but disabled); paid agent requires payment.
**Metrics:** Install-to-use conversion, time-to-first-use, uninstall rate.
**Features used:** NX-FEAT-1501-1505, 1511, 2101-2103, 2205, 2702.

---

### J-09: User audits what an agent did

**Persona:** any (especially P-MARCUS, P-THEA)
**Outcome:** User can see, understand, and reverse agent actions.
**Trigger:** User opens Activity Log.
**Pre-conditions:** At least one agent action has occurred.

**Steps:**
1. User clicks Activity Log icon.
2. Sees chronological list of agent actions with: timestamp, agent name, action type, target, result.
3. Filters: by agent, by action type, by Workspace, by date.
4. Clicks a specific action; sees input, reasoning, output.
5. For reversible actions, "Undo" button appears.
6. User undoes an action; system confirms reversion.
7. Audit log export to CSV.

**Success criteria:** Find any past action in ≤3 clicks. Undo reversible actions in ≤2 clicks.
**Failure modes:** Action not reversible (explain why); log too large (paginate).
**Metrics:** Audit log usage rate, undo success rate.
**Features used:** NX-FEAT-2104, 2205-2207.

---

### J-10: User revokes agent permission mid-task

**Persona:** any
**Outcome:** Agent stops immediately when permission is revoked.
**Trigger:** User opens agent's permission panel.
**Pre-conditions:** Agent currently has permission.

**Steps:**
1. User opens "Permissions" panel for active agent.
2. Sees scope: read inbox, send messages.
3. Clicks "Revoke send messages."
4. Confirmation: "Agent will stop sending. Continue?"
5. User confirms.
6. If agent is mid-task: task pauses at next send; user is informed.
7. Permission scope updated; activity log records revocation.

**Success criteria:** Revocation takes effect within 500ms. No partial messages sent.
**Failure modes:** Action already in flight (note it); multiple agents (revoke all or per-agent).
**Metrics:** Revocation response time, partial-action rate.
**Features used:** NX-FEAT-2101, 2103, 2107, 2205.

---

### J-11: User creates a recurring workflow

**Persona:** P-MARCUS (primary), P-MAYA, P-THEA
**Outcome:** Workflow runs automatically on schedule.
**Trigger:** User saves workflow with schedule trigger.
**Pre-conditions:** Workflow Builder available; Cloud Browser or API access.

**Steps:**
1. User opens Workflow Builder; drops blocks: HTTP request, transform, condition, email.
2. Configures blocks with parameters.
3. Adds trigger: schedule (every Monday 09:00).
4. Tests workflow with "Run once now."
5. Reviews result; adjusts.
6. Saves workflow.
7. Workflow appears in "Scheduled" list.
8. On Monday 09:00, workflow runs; user receives email digest.
9. User can pause, edit, or delete.

**Success criteria:** Schedule fires within 1 minute of target. Failure alert on error.
**Failure modes:** External API down (retry with backoff); quota exceeded (alert).
**Metrics:** Schedule accuracy, failure rate.
**Features used:** NX-FEAT-1801-1812, 1811, 2201, 2203.

---

### J-12: Devin builds and ships a feature using Cloud Browsers

**Persona:** P-DEVIN
**Outcome:** Code change tested in 3 browser environments and shipped.
**Trigger:** Devin opens "Coding: Feature X" Workspace.
**Pre-conditions:** GitHub connected, Cloud Browser Fleet provisioned.

**Steps:**
1. Devin: "Open a PR for Feature X and test it in Chrome, Firefox, Safari emulators."
2. Planner proposes: open PR, spawn 3 Cloud Browsers, run tests, report.
3. Devin approves.
4. Coder agent opens PR via GitHub API.
5. Test agent spawns 3 Cloud Browsers with different fingerprints.
6. Each runs smoke tests; results collected.
7. Reviewer agent compares to baseline; flags regressions.
8. Devin reviews report; approves merge.

**Success criteria:** Multi-browser test in ≤10 minutes. 100% pass rate required for merge.
**Failure modes:** Browser fingerprint detected (use proxy); test flake (rerun).
**Metrics:** Cross-browser coverage, time-to-test.
**Features used:** NX-FEAT-1601, 1605, 1606, 1808 (code), 2304 (GitHub), 1401-1414.

---

### J-13: Sara refines a draft over multiple iterations

**Persona:** P-SARA (and most personas)
**Outcome:** Draft improves through iteration, with version history.
**Trigger:** User clicks "Refine" or asks "Make it more concise."
**Pre-conditions:** Workspace has a draft artifact.

**Steps:**
1. Sara opens existing draft.
2. Types: "Make the executive summary more concise."
3. Agent revises; shows diff.
4. Sara: "Add 2 more competitor citations."
5. Agent revises; adds sources.
6. After 5 iterations, Sara clicks "Show history."
7. Sees version list with diffs; can restore any version.

**Success criteria:** Iterations complete in <10s each. Version history is intact.
**Failure modes:** Model rate limit (queue); user changes mind (restore).
**Metrics:** Iterations per session, restore usage.
**Features used:** NX-FEAT-1301, 1304, 1305, 1306, 1704, 2205.

---

### J-14: Marcus exports data to spreadsheet

**Persona:** P-MARCUS
**Outcome:** Data extracted from website and saved as CSV.
**Trigger:** User invokes "Extract & Export" workflow.
**Pre-conditions:** Workflow Builder, file storage integration.

**Steps:**
1. User opens Workflow Builder.
2. Drops blocks: Open URL → Wait for selector → Extract table → Save CSV.
3. Configures URL and selectors.
4. Runs once; reviews CSV in preview.
5. Saves workflow; runs on demand or schedule.

**Success criteria:** CSV is well-formed; columns match extraction.
**Failure modes:** Selector breaks (alert); site rate-limits (slow down).
**Metrics:** Extraction accuracy, schedule reliability.
**Features used:** NX-FEAT-1801-1812, 2303 (storage).

---

### J-15: User customizes a theme

**Persona:** P-RIYA (primary)
**Outcome:** Personal theme saved and applied.
**Trigger:** User opens Themes settings.
**Pre-conditions:** None.

**Steps:**
1. User opens Settings → Appearance → Theme.
2. Picks base theme (Light, Dark, Sepia, etc.).
3. Adjusts accent color, typography scale, motion level.
4. Preview updates in real time.
5. Saves as "My Theme."
6. Theme applies across all Workspaces.

**Success criteria:** Preview is instant. Theme persists across sessions/devices.
**Failure modes:** High-contrast override (apply if accessibility needs); theme conflicts (reset).
**Metrics:** Custom-theme usage, retention correlation.
**Features used:** NX-FEAT-2401, 2402.

---

### J-16: First-time AI-native extension install by Devin

**Persona:** P-DEVIN
**Outcome:** Extension installed, dev environment set up, agent can call it.
**Trigger:** Devin browses Plugin marketplace.
**Pre-conditions:** Developer mode enabled.

**Steps:**
1. Devin opens Plugin marketplace.
2. Finds "JIRA Connector" plugin.
3. Reads manifest: tools exposed, permissions, schema.
4. Installs plugin; sandboxed.
5. Runs `nexus plugin dev` to test locally.
6. Plugin registers a tool with the agent runtime.
7. Devin types: "Create a JIRA ticket from this bug report."
8. Agent invokes the plugin tool; JIRA ticket created.

**Success criteria:** Plugin tool is callable by agent in ≤2 minutes from install.
**Failure modes:** Plugin declares unsafe permissions (warn); schema invalid (reject).
**Metrics:** Plugin install-to-use time, tool-call success rate.
**Features used:** NX-FEAT-1901-1909, 1403.

---

### J-17: User deletes account and exports data first

**Persona:** any (especially P-SARA, P-MARCUS)
**Outcome:** Full data export received; account deleted.
**Trigger:** User opens Settings → Account → Delete account.
**Pre-conditions:** None.

**Steps:**
1. User opens account settings.
2. Sees "Export all data" option with size estimate.
3. Clicks Export; receives email when ready (typically <1 hour).
4. Downloads ZIP: workspaces, agents, workflows, memory, history.
5. Confirms receipt; clicks "Delete account."
6. Re-authenticates; confirms deletion.
7. Account and data are wiped within 30 days (logs purged immediately).
8. Confirmation email sent.

**Success criteria:** Export is complete; deletion is irreversible but well-explained.
**Failure modes:** Active subscriptions (cancel first); team owner (transfer first).
**Metrics:** Export success rate, time-to-delete.
**Features used:** NX-FEAT-2008, 2009, 2207, 2705.

---

### J-18: User works offline

**Persona:** any
**Outcome:** Most functions work without network.
**Trigger:** Network drops.
**Pre-conditions:** Local AI installed.

**Steps:**
1. Network drops; NEXUS detects.
2. UI shows "Offline" badge.
3. Cloud Browser actions queue locally.
4. Local AI continues responding to intents.
5. Memory continues working.
6. When network returns, queued actions sync; user is notified.

**Success criteria:** Core functions (chat, command bar, memory, local browsers) work offline.
**Failure modes:** Required cloud model (queue + alert); marketplace inaccessible (show offline message).
**Metrics:** Offline success rate, sync conflict count.
**Features used:** NX-FEAT-2601-2604, 2006.

---

### J-19: User invites teammate (Thea)

**Persona:** P-THEA (also P-MAYA occasionally)
**Outcome:** Teammate joins the team plan and sees shared Workspaces.
**Trigger:** Thea clicks "Invite teammate" from team dashboard.
**Pre-conditions:** Team plan active.

**Steps:**
1. Thea enters teammate's email.
2. Invitation sent; teammate receives email.
3. Teammate clicks link; creates account or signs in.
4. Teammate lands in team Workspace.
5. Shared Workspaces visible based on permissions.

**Success criteria:** Teammate activates within 24 hours of invite.
**Failure modes:** Email bounces; seat limit reached.
**Metrics:** Invite-to-activation rate, team size growth.
**Features used:** NX-FEAT-2001, 2005, 2709, 2905 (admin console).

---

### J-20: User encounters an error and recovers

**Persona:** any
**Outcome:** User understands error, recovers, optionally reports.
**Trigger:** System encounters an unrecoverable error.
**Pre-conditions:** None.

**Steps:**
1. Error occurs; toast appears with summary.
2. Toast has: "What happened," "What you can do," "Send feedback."
3. User clicks "What happened"; sees plain-language explanation.
4. User clicks "Send feedback"; pre-filled diagnostic info attached.
5. User retries or undoes; system succeeds or fails clearly.

**Success criteria:** Errors are plain-language. Recovery path is one click away.
**Failure modes:** Silent failure (rejected at QA gate); cryptic error (rewrite).
**Metrics:** Error rate, recovery rate, feedback rate.
**Features used:** NX-FEAT-2201, 2202, 2506, 2205.

---

## 4. Cross-journey metrics

A single set of metrics applies across all journeys:

| Metric | Target |
|--------|--------|
| Time-to-first-success | < 15 minutes (any persona) |
| Task completion rate | ≥ 80% |
| Iteration cycles to satisfaction | < 5 |
| Recovery from error | < 2 clicks |
| Memory retention across sessions | 100% of explicit preferences |

## 5. Journey-to-feature cross-check

This matrix verifies feature coverage:

| Journey | Most distinctive features |
|---------|---------------------------|
| J-01 (Maya content) | AI Command Bar, Memory (style), Marketplace |
| J-02 (Devin triage) | Agent Orchestrator, GitHub, Marketplace |
| J-03 (Sara dossier) | Memory, KG, Citations |
| J-04 (Marcus monitor) | Cloud Browser, Workflows, Scheduled |
| J-05 (Riya briefing) | Local AI, Workflows, Integrations |
| J-06 (Thea share) | Workspace sharing, Audit, SSO |
| J-07 (Onboarding) | Sample workspaces, Onboarding, Memory |
| J-08 (Marketplace install) | Marketplace, Permissions |
| J-09 (Audit) | Activity Log, Audit log |
| J-10 (Revoke) | Permissions, Activity Log |
| J-11 (Schedule) | Workflow Builder, Schedule trigger |
| J-12 (Devin test) | Cloud Browser, GitHub, Code blocks |
| J-13 (Iterate) | Chat, Memory, Versions |
| J-14 (Export CSV) | Workflows, File storage |
| J-15 (Theme) | Theming |
| J-16 (Plugin) | Plugin SDK |
| J-17 (Delete account) | Export, Delete |
| J-18 (Offline) | Local AI, Sync |
| J-19 (Invite) | Team, Sync |
| J-20 (Error recovery) | Notifications, Diagnostics |

Every feature in NX-FEAT-0001 should appear in at least one journey above. If not, the feature is suspect.

## 6. Reading list

- **Audiences** — NX-DOC-0007
- **Master PRD** — NX-PRD-0001
- **Feature Inventory** — NX-FEAT-0001
- **Persona × Feature Matrix** — NX-PRD-0002
- **Onboarding** — NX-PRD-0004

---

*End NX-PRD-0003.*