# NX-AT-9501 — Acceptance Test Suite

| Field | Value |
|-------|-------|
| **Document ID** | NX-AT-9501 |
| **Title** | Acceptance Test Suite |
| **Phase** | 5 — Autonomous Engineering Company |
| **Owner** | QA AI |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-06-30 |
| **Depends on** | NX-PRD-0001 (Master PRD), NX-WF-9003 (Quality Gates) |

---

## 1. Purpose

This document defines the **acceptance tests** that verify the product meets its PRD specifications. Acceptance tests are derived from PRD criteria (NX-PRD-0001 §11). They run nightly and gate every release.

## 2. Acceptance test framework

Each acceptance test has:

```typescript
interface AcceptanceTest {
  id: string;                  // NX-AT-####-NN
  title: string;
  description: string;
  feature_refs: string[];       // NX-FEAT-####
  prd_refs: string[];           // NX-PRD-####
  category: ATCategory;
  priority: 'P0' | 'P1' | 'P2' | 'P3';
  steps: TestStep[];
  preconditions: string[];
  success_criteria: string[];
  expected_outcome: string;
  automated: boolean;
  last_run?: timestamp;
  last_status?: 'pass' | 'fail' | 'skip';
}

type ATCategory =
  | 'functional'
  | 'performance'
  | 'security'
  | 'accessibility'
  | 'usability'
  | 'compatibility'
  | 'reliability'
  | 'data_integrity';
```

## 3. Test categories

### 3.1 Functional

Verifies features behave per spec. Largest category.

Examples: "User can create Workspace in <10 seconds."

### 3.2 Performance

Verifies latency, throughput, scale.

Examples: "Cold start <1.5s on reference hardware."

### 3.3 Security

Verifies permissions, encryption, audit.

Examples: "Every agent action recorded in audit log."

### 3.4 Accessibility

Verifies WCAG 2.2 AA compliance.

Examples: "All interactive elements keyboard-navigable."

### 3.5 Usability

Verifies user-facing criteria.

Examples: "First task completed in <15 minutes."

### 3.6 Compatibility

Verifies cross-platform, cross-version.

Examples: "Works on macOS 13+ and Windows 11."

### 3.7 Reliability

Verifies recovery from failures.

Examples: "Crash recovery preserves Workspace state."

### 3.8 Data integrity

Verifies data correctness.

Examples: "Account export contains all memory items."

## 4. Test selection per release

| Release type | Tests required |
|--------------|---------------|
| **Patch** | Functional + data integrity (relevant) |
| **Minor** | + Performance + Security + Accessibility |
| **Major** | All categories |

## 5. Test execution

### 5.1 Schedule

| Frequency | What runs |
|-----------|-----------|
| Per PR | Smoke (subset of functional, fast) |
| Nightly | Full functional + performance |
| Weekly | + security, accessibility |
| Pre-release | All categories |

### 5.2 Environment

Tests run in:

- **CI:** ephemeral containers.
- **Staging:** persistent environment mirroring production.
- **Production canary:** 5% of users (for selected tests).

### 5.3 Reporting

Each run produces a report:

```typescript
interface ATReport {
  run_id: string;
  started_at: timestamp;
  completed_at: timestamp;
  results: ATResult[];
  summary: {
    pass: number;
    fail: number;
    skip: number;
    regressions: number[];
  };
}

interface ATResult {
  test_id: string;
  status: 'pass' | 'fail' | 'skip';
  duration_ms: number;
  evidence?: Evidence[];
  failure?: { message: string; stack?: string };
}
```

## 6. Acceptance criteria map

The full acceptance test catalog maps directly to PRD criteria. Selection:

| PRD ref | Test IDs |
|--------|----------|
| NX-PRD-0002 (Persona matrix) | NX-AT-9501-P01 to P06 (one per persona activation) |
| NX-PRD-0003 (User journeys) | NX-AT-9501-J01 to J20 |
| NX-PRD-0004 (Onboarding) | NX-AT-9501-O01 to O12 |
| NX-PRD-0005 (Subscription) | NX-AT-9501-S01 to S15 |
| NX-PRD-0006 (Roadmap) | NX-AT-9501-M01 to M08 (metrics) |
| NX-FEAT-1100 (Workspace) | NX-AT-9501-W01 to W20 |
| NX-FEAT-1500 (Marketplace) | NX-AT-9501-MP01 to MP15 |
| NX-FEAT-1600 (Cloud Browser) | NX-AT-9501-CB01 to CB20 |
| NX-FEAT-1700 (Memory) | NX-AT-9501-ME01 to ME18 |
| NX-FEAT-1800 (Workflows) | NX-AT-9501-WF01 to WF15 |

150+ acceptance tests at H1.

## 7. Sample acceptance tests

### NX-AT-9501-P01: Maya activates

```yaml
id: NX-AT-9501-P01
title: Solo Operator completes first task in <15 min
category: usability
priority: P0
feature_refs: [NX-FEAT-2801, NX-FEAT-2802]
preconditions:
  - Fresh install
  - Account created
  - Persona: P-MAYA
steps:
  - Complete welcome
  - Skip profile setup
  - Run suggested intent: "Generate a week's content calendar"
  - Approve plan
  - Wait for completion
success_criteria:
  - Task completes within 15 minutes
  - User can edit at least one post
expected_outcome: First task done
automated: true
```

### NX-AT-9501-W01: Cold start time

```yaml
id: NX-AT-9501-W01
title: Cold start time on reference hardware
category: performance
priority: P0
preconditions:
  - macOS reference hardware (M2 Pro)
  - Account with 50 Workspaces
  - Cold cache
steps:
  - Quit NEXUS
  - Launch NEXUS
  - Measure time-to-first-paint
success_criteria:
  - Time-to-first-paint <1.5s
expected_outcome: <1.5s
automated: true
```

### NX-AT-9501-S01: Cloud Browser creation

```yaml
id: NX-AT-9501-S01
title: Cloud Browser creation <30s
category: functional
priority: P0
feature_refs: [NX-FEAT-1601]
preconditions:
  - Pro account
  - <5 Cloud Browsers
steps:
  - Navigate to Fleet dashboard
  - Click "New Cloud Browser"
  - Confirm defaults
  - Wait for ready
success_criteria:
  - Browser ready in <30s
expected_outcome: Browser running
automated: true
```

### NX-AT-9501-ME01: Memory export completeness

```yaml
id: NX-AT-9501-ME01
title: Memory export contains all items
category: data_integrity
priority: P0
feature_refs: [NX-FEAT-1707]
preconditions:
  - Account with 100 memory items
steps:
  - Trigger export
  - Wait for download
  - Parse export
  - Count items
success_criteria:
  - Exported count = 100
  - All types represented
expected_outcome: Export complete and accurate
automated: true
```

## 8. Manual tests

Some criteria cannot be automated:

- Subjective usability.
- Visual design feel.
- Tone of voice in copy.

These run as **manual tests**:

- Scheduled weekly.
- Run by QA Agent + founder.
- Logged with rating 1–5.

## 9. Regression detection

A test is a regression if:

- It passed in the previous release and fails now.
- Or: a new test fails on existing code.

Regressions block release.

## 10. Acceptance criteria for the suite itself

- [ ] Every PRD criterion maps to at least one test.
- [ ] 80%+ tests automated.
- [ ] Full suite runs in <4 hours.
- [ ] Failures include diagnostic info.
- [ ] Suite integrated with CI.

## 11. Open questions

- Q: Should we ship a public status page (e.g., status.nexus.ai)?
- Q: How do we handle flaky tests (intermittent failures)?

## 12. Reading list

- **Master PRD** — NX-PRD-0001
- **Quality Gates** — NX-WF-9003
- **User Journeys** — NX-PRD-0003
- **Agent Evaluation** — NX-AGENT-7017

---

*End NX-AT-9501.*