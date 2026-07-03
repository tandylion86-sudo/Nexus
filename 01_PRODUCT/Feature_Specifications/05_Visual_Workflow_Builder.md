# NX-FEAT-1800 — Visual Workflow Builder (Anchor Spec)

| Field | Value |
|-------|-------|
| **Document ID** | NX-FEAT-1800 |
| **Title** | Visual Workflow Builder (Anchor Spec) |
| **Area** | NX-FEAT-A0009 — Visual Workflow Builder |
| **Owner** | Frontend AI + Backend AI |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-06-30 |
| **Priority (H1)** | P1 |
| **Horizon target** | H1 |
| **Estimated effort** | XL (decomposed into NX-FEAT-1801-1812) |

---

## 1. Purpose

The **Visual Workflow Builder** lets users compose automations by connecting blocks on a canvas. Each block performs an action (browser, HTTP, model, condition, loop). Users drag from a palette, configure each block, connect them, and run.

For power users who prefer code, the same workflows can be edited as JavaScript or Python via inline editor.

This document is the anchor spec; leaf features (NX-FEAT-1801 through 1812) inherit from it.

## 2. Why a visual workflow builder

Without it:
- Power users build automations in scripts.
- Non-technical users can't automate.
- There's no shared format for automations.

With it:
- Non-technical users can build meaningful automations.
- Power users can compose faster.
- Workflows become shareable and monetizable (marketplace).
- NEXUS becomes a platform for automation, not just a browser.

## 3. User stories

- As **Maya**, I want to drag blocks together to "send a Slack message when a new competitor price is detected."
- As **Marcus**, I want to schedule a workflow that runs every Monday at 9am.
- As **Devin**, I want to edit the generated JavaScript for advanced logic.
- As **Riya**, I want to step through a workflow in debug mode to see where it failed.
- As **Thea**, I want my team to share workflow templates.

## 4. Functional requirements

### FR-1: Block-based editor (drag-drop canvas)
**Description:** A canvas where users drag blocks from a palette and connect them.
**Acceptance:**
- [ ] Palette shows block categories.
- [ ] Drag-and-drop creates block on canvas.
- [ ] Connections drawn by dragging from output port to input port.
- [ ] Pan, zoom, fit-to-screen.
- [ ] Undo/redo with full history.

### FR-2: Core blocks
**Description:** A library of core block types.
**Acceptance:**

Core blocks at launch:

| Block | Description | Inputs | Outputs |
|-------|-------------|--------|---------|
| HTTP Request | Make HTTP call | URL, method, headers, body | Response |
| Open URL (Cloud Browser) | Open URL in Cloud Browser | URL | Page, DOM |
| Click | Click selector | Selector, optional text | Confirmation |
| Extract | Extract data from page | Selector, attribute | Extracted value |
| Type | Type into field | Selector, text | Confirmation |
| Wait | Wait for condition | Selector or duration | Continuation |
| Transform | JS expression to transform value | Expression | Transformed value |
| Condition | Branch on predicate | Predicate | True/False paths |
| Loop | Iterate over array | Array | Per-item path |
| LLM Call | Call a model | Prompt, model | Response |
| Send Email | Send email | To, subject, body | Confirmation |
| Slack message | Send Slack message | Channel, text | Confirmation |
| Schedule trigger | Cron-style trigger | Schedule | – |
| Webhook trigger | Webhook trigger | URL | – |
| Webhook response | Send webhook response | Status, body | – |
| Note | Sticky note | – | – |
| Code | Run inline JS or Python | Code | Value |

Each block has a typed input/output schema; type errors are flagged.

### FR-3: Block configuration panel
**Description:** Each block has a configuration panel.
**Acceptance:**
- [ ] Click block → panel opens on right.
- [ ] Panel shows all block parameters.
- [ ] Parameters are typed (string, number, enum, secret, expression).
- [ ] Live validation; errors shown inline.
- [ ] "Test this block" runs it standalone with sample input.

### FR-4: Workflow execution engine
**Description:** A runtime that executes workflows.
**Acceptance:**
- [ ] Executes blocks in order, respecting branching and loops.
- [ ] Handles errors per block policy (fail, retry, continue).
- [ ] Streams execution progress to UI.
- [ ] Supports parallel branches.
- [ ] Logs all intermediate values for debugging.

### FR-5: Workflow versioning
**Description:** Workflows are versioned; users can view history and revert.
**Acceptance:**
- [ ] Every save creates a version.
- [ ] Version history is browsable.
- [ ] Diff between versions is shown.
- [ ] Revert is one click.

### FR-6: Workflow templates
**Description:** Pre-built workflow templates for common tasks.
**Acceptance:**
- [ ] 10+ templates at launch.
- [ ] Each template is annotated with: purpose, required integrations, expected runtime.
- [ ] Templates are configurable copies (do not auto-link).
- [ ] User can save any workflow as a template.

### FR-7: Workflow marketplace publishing
**Description:** Users can publish workflows to marketplace (H2 feature).
**Acceptance:**
- [ ] Publishing requires verified creator.
- [ ] Workflow is validated for safety.
- [ ] Pricing models: free, one-time, subscription.
- [ ] Revenue share per NX-FEAT-1509.

### FR-8: Inline code editing
**Description:** Power users can edit the generated code directly.
**Acceptance:**
- [ ] "View as code" toggles between visual and code.
- [ ] Code changes sync back to visual.
- [ ] Syntax highlighting, autocomplete.
- [ ] Errors in code are highlighted.
- [ ] Linting per language.

### FR-9: Debug mode (step-through)
**Description:** Users can step through a workflow one block at a time.
**Acceptance:**
- [ ] "Debug" mode shows current step highlighted.
- [ ] Each step's input/output is visible.
- [ ] User can pause, resume, skip.
- [ ] Breakpoints can be set on blocks.
- [ ] Conditional breakpoints supported (e.g., when value equals X).

### FR-10: Error visualization
**Description:** Failed blocks are highlighted with reasons.
**Acceptance:**
- [ ] Failed block turns red.
- [ ] Hover shows error message.
- [ ] User can click "Retry this block" or "Continue past failure."
- [ ] Error log is exportable.

### FR-11: Schedule trigger
**Description:** Workflows can run on a schedule.
**Acceptance:**
- [ ] Cron-style: every N units; specific times.
- [ ] Timezone support (per user).
- [ ] Schedule can be paused/resumed.
- [ ] Schedule conflicts (overlapping runs) are flagged.

### FR-12: Event trigger (webhook, message)
**Description:** Workflows can run on external events.
**Acceptance:**
- [ ] Webhook trigger exposes a stable URL with auth token.
- [ ] Slack / Discord message trigger (H2).
- [ ] Email trigger (H2).
- [ ] Trigger config is editable from canvas.

## 5. Non-functional requirements

### NFR-1: Performance
- Canvas load: <500ms for 50-block workflow.
- Block execution latency: depends on block; UI updates within 100ms.
- Schedule accuracy: within 1 minute.
- Code editor: handles 1000-line workflows.

### NFR-2: Reliability
- Execution durability: workflow can be re-driven from any step.
- Failures: retried per policy.
- Scheduled runs: history preserved.

### NFR-3: Security
- Workflow code runs in sandbox (NX-FEAT-1902).
- Secrets (API keys, tokens) encrypted at rest.
- Webhook endpoints auth-protected.
- No outbound network access without permission.

### NFR-4: Cost
- Execution: free for first-party blocks; metered for premium (LLM, Cloud Browser).
- Storage: $0.02/GB/month for workflow definitions.

## 6. UI surfaces

| Surface | Reference |
|---------|-----------|
| Workflow canvas | NX-UI-6501 |
| Block palette | NX-UI-6502 |
| Block configuration panel | NX-UI-6503 |
| Workflow run history | NX-UI-6504 |
| Workflow version history | NX-UI-6505 |
| Code editor | NX-UI-6506 |
| Debug mode | NX-UI-6507 |
| Schedule manager | NX-UI-6508 |
| Template gallery | NX-UI-6509 |

## 7. Permissions

Workflows require:

- Create: any user.
- Run: creator + workspace members (with permissions).
- Edit: creator + editor.
- Delete: creator + admin.
- Publish to marketplace: verified creator.

## 8. Telemetry

Workflow-specific telemetry (opt-in):

- `workflow.created`
- `workflow.executed`
- `workflow.scheduled`
- `workflow.failed`
- `workflow.template_used`
- `workflow.published`

Activity Log captures per-execution events regardless.

## 9. Failure modes

| Failure | Behavior |
|---------|----------|
| Block timeout | Retry per policy; then fail |
| Workflow infinite loop | Detected after N iterations; abort; notify |
| External API down | Retry with backoff; then fail |
| Schedule missed (workflow too long) | Skip next run; notify |
| Sandbox violation | Workflow killed; alert; creator notified |
| Storage full | Pause new workflows; notify |

## 10. Dependencies

- Agent Orchestrator (NX-FEAT-A0005).
- Plugin SDK (NX-FEAT-A0010).
- Cloud Browser Fleet (NX-FEAT-A0007).
- Memory Engine (NX-FEAT-A0008).
- Permission system (NX-FEAT-A0012).

## 11. Out of scope

- Visual debugging with breakpoints in production runs (H2).
- Workflow versioning with branching/merging (H2).
- Workflow marketplace transactions (H2).
- Multi-user collaborative editing (H2).

## 12. Acceptance criteria summary

Visual Workflow Builder is done when:

- [ ] User can build a 10-block workflow without code.
- [ ] Workflow runs reliably and durably.
- [ ] Debug mode surfaces failures clearly.
- [ ] Schedule triggers fire within 1 minute of target.
- [ ] Inline code editing syncs with visual.
- [ ] 10+ templates available.
- [ ] Failed blocks are visually highlighted with reasons.

## 13. Sub-features (leaf specs)

| ID | Name |
|----|------|
| NX-FEAT-1801 | Block-based editor |
| NX-FEAT-1802 | Core blocks |
| NX-FEAT-1803 | Block configuration panel |
| NX-FEAT-1804 | Workflow execution engine |
| NX-FEAT-1805 | Workflow versioning |
| NX-FEAT-1806 | Workflow templates |
| NX-FEAT-1807 | Workflow marketplace publishing |
| NX-FEAT-1808 | Inline code editing |
| NX-FEAT-1809 | Debug mode |
| NX-FEAT-1810 | Error visualization |
| NX-FEAT-1811 | Schedule trigger |
| NX-FEAT-1812 | Event trigger |

## 14. Open questions

- Q: How do we balance visual simplicity vs. expressiveness — what's the right block count ceiling?
- Q: Should workflows be exportable as standalone scripts (n8n-style)?
- Q: How do we handle workflows that call other workflows (composition)?
- Q: Should we ship a marketplace from day one or wait for organic templates to emerge?

## 15. Change log

| Date | Change | Author |
|------|--------|--------|
| 2026-06-30 | Initial anchor spec | Frontend AI |

---

*End NX-FEAT-1800.*