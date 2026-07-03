# NX-AGENT-7006 — Reviewer Agent Specification

| Field | Value |
|-------|-------|
| **Document ID** | NX-AGENT-7006 |
| **Title** | Reviewer Agent |
| **Phase** | 4 — AI Brain |
| **Owner** | AI Platform AI |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-06-30 |
| **Depends on** | NX-AGENT-7001, NX-AGENT-7002 |

---

## 1. Mission

The Reviewer **critiques** the output of other agents. It exists to surface what other agents miss and to enforce quality.

## 2. Responsibilities

1. **Evaluate against criteria.** Check for correctness, completeness, style, security, accessibility.
2. **Surface weaknesses.** What could be better?
3. **Suggest improvements.** Concrete, actionable.
4. **Approve or block.** Decision is binary.
5. **Document reasoning.** Future reviewers can see why.

## 3. Tools

| Tool | Purpose |
|------|---------|
| `output.read` | Read the work product |
| `criteria.check` | Run criteria checks |
| `model.critique` | Generate critique |
| `memory.read` | Pull prior reviews for consistency |
| `comment.add` | Add inline comments |
| `decision.record` | Approve / block |

## 4. Permissions

```yaml
permissions:
  scopes:
    - workspace.read
    - workspace.write         # can comment
    - memory.read
    - memory.write            # review notes
  secrets: []
```

Reviewer is read-only with respect to the work product (e.g., it doesn't change code); it comments and decides.

## 5. Memory

```yaml
memory:
  read:
    - workspace:active
    - user:preferences        # style preferences
    - global:conventions      # project conventions
  write:
    - workspace:active        # review notes
```

## 6. Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Work product | ✅ | The output to review |
| Criteria | ✅ | What to check |
| Source context | – | Original request, prior iterations |

## 7. Outputs

```typescript
interface Review {
  id: string;
  work_id: string;
  decision: 'approve' | 'request_revisions' | 'block';
  summary: string;
  criteria_results: CriterionResult[];
  inline_comments: Comment[];
  suggestions: Suggestion[];
  confidence: number;
  reviewed_at: timestamp;
}

interface CriterionResult {
  criterion: string;
  status: 'pass' | 'fail' | 'warn' | 'na';
  evidence: string;
}

interface Comment {
  location: string;           // file:line or section
  body: string;
  severity: 'info' | 'warn' | 'error';
}

interface Suggestion {
  description: string;
  priority: 'low' | 'medium' | 'high';
  effort: 'small' | 'medium' | 'large';
}
```

## 8. Behavior

### 8.1 Review criteria (default)

Every review checks:

1. **Correctness.** Does it do what was asked?
2. **Completeness.** Are all requirements addressed?
3. **Style.** Does it match conventions?
4. **Security.** Any vulnerabilities?
5. **Accessibility.** WCAG compliance where applicable.
6. **Performance.** Any obvious perf issues?
7. **Tests.** Adequate coverage?
8. **Documentation.** Clear enough?

### 8.2 Decision logic

| Decision | When |
|----------|------|
| `approve` | All criteria pass; no blocking issues |
| `request_revisions` | Non-blocking issues; can be addressed |
| `block` | Critical issues; safety, security, correctness |

### 8.3 Constructive tone

Reviews surface issues with:

- Specific evidence ("L7 has `eval()` on user input — see XSS reference").
- Concrete suggestion ("Replace with `JSON.parse` after validation").
- Priority ("Critical" vs. "Nice-to-have").

No vague "could be better" without specifics.

### 8.4 Multi-pass

For complex work, the Reviewer may run multiple passes:

1. **Correctness pass.** Find bugs.
2. **Style pass.** Find inconsistencies.
3. **Security pass.** Find vulnerabilities.
4. **Accessibility pass.** Find a11y issues.

Each pass produces its own output; results are aggregated.

## 9. Streaming

The Reviewer streams:

- Initial verdict (≤5s).
- Per-criterion status.
- Inline comments as found.
- Final decision.

## 10. Failure modes

| Failure | Behavior |
|---------|----------|
| Insufficient criteria | Use defaults |
| Work is too large | Focus on critical paths |
| Disagreement with prior reviewer | Note as "differs from prior" |
| Cannot evaluate | Mark `na` and explain |

## 11. Performance

- Review latency: ≤10s for typical work.
- Concurrent reviews: 5 per Workspace.

## 12. Evaluation

| Metric | Target |
|--------|--------|
| Decision accuracy (vs human) | ≥85% |
| Critical issue catch rate | ≥95% |
| False positive rate | <15% |

Benchmarks: `reviewer.critical-catch-v1`, `reviewer.calibration-v1`.

## 13. Acceptance criteria

- [ ] Default criteria cover all eight categories.
- [ ] Decisions are well-reasoned and specific.
- [ ] Inline comments link to specific locations.
- [ ] Multi-pass works on large outputs.

## 14. Open questions

- Q: Should Reviewer be allowed to skip criteria explicitly?
- Q: Should we ship domain-specific Reviewer variants (Code Reviewer, Doc Reviewer)?

## 15. Reading list

- **Agent Contract** — NX-AGENT-7001
- **Coder** — NX-AGENT-7005
- **Tester** — NX-AGENT-7007
- **Reflection & Self-Evaluation** — NX-AGENT-7012

---

*End NX-AGENT-7006.*