# NX-DOC-0004 — Core Principles

| Field | Value |
|-------|-------|
| **Document ID** | NX-DOC-0004 |
| **Title** | Core Principles |
| **Phase** | 1 — Master Blueprint |
| **Owner** | Founder |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-06-30 |
| **Related** | NX-DOC-0005 (Product Philosophy), NX-DOC-0011 (Technical Principles), NX-DOC-0006 (AI-First Design Philosophy) |

---

## 1. Purpose

These are the **non-negotiable principles** that govern every decision at NEXUS. They outlast any feature, any employee, any model, and any market condition. When two principles conflict in a specific decision, this document also describes the precedence order.

## 2. The 12 principles

### Principle 1 — Intent over navigation
**The user describes outcomes, not paths.**

The browser's job is to translate intent into execution. URLs are an implementation detail, not the interface. Every surface — home screen, command bar, settings, marketplace — is evaluated by how well it serves intent.

*Implication:* The home screen is a prompt, not a search engine. Settings are goals, not toggles. The address bar is an escape hatch, not the primary input.

### Principle 2 — Human authority is preserved
**The user is always in control of high-impact actions.**

AI agents operate within boundaries. Money, identity, credentials, legal commitments, communications sent in the user's name, and irreversible actions require explicit human approval. Agents can propose; only humans can dispose.

*Implication:* Every agent has a permission scope. Every high-impact action shows a confirmation that names the agent, the action, and the consequence.

### Principle 3 — Transparency by default
**Every agent action is visible, explainable, and reversible when possible.**

NEXUS does not hide what its agents are doing. Activity streams show every action with reasoning. Users can pause, redirect, or reverse at any time.

*Implication:* No silent background behavior on important state. The Activity Log is a first-class UI surface, not buried in settings.

### Principle 4 — Privacy is a structural property
**User data is encrypted, isolated, and never sold.**

Encryption is end-to-end where feasible. Vaults are per-user. Telemetry is opt-in, never opt-out, for any feature that touches content. The default is the most private configuration.

*Implication:* Architectural decisions that would force telemetry-on for correctness are rejected. A "local-only mode" exists from day one.

### Principle 5 — Reliability earns trust
**A browser that breaks is unusable. We treat stability as a feature.**

Every release must clear a reliability bar: cold-start under 1.5 seconds on reference hardware, zero-crash session for 99.9% of users per week, recovery from crash without data loss. When reliability and a new feature conflict, reliability wins.

*Implication:* Performance and stability are tracked at the executive level. A release-blocking bug prevents ship.

### Principle 6 — Progressive disclosure
**Beginners see a clean surface. Advanced controls appear when needed.**

The default UI is approachable. Complexity is layered. A user never sees a feature they have not earned the right to use. Power-user controls exist, but are not the front door.

*Implication:* Onboarding reveals the next layer only after the previous one is mastered. Settings are organized by goal, not by technical taxonomy.

### Principle 7 — Modularity over monolith
**Every major capability is replaceable.**

Models, databases, automation engines, storage backends, even the browser engine can be swapped without rewriting the product. NEXUS is a composition of components with stable contracts.

*Implication:* Adapter interfaces are mandatory. Every third-party SDK has a defined abstraction layer. We can move from one model provider to another in under a week.

### Principle 8 — Quality at the source
**Defects are cheaper to prevent than to repair.**

Every phase — research, design, code, test, ship — has a quality gate. We do not "throw it over the wall." Reviews happen before merge, not after. Documentation is a release blocker.

*Implication:* Code without tests is incomplete. Features without documentation are not "done." Specifications without acceptance criteria are not approved.

### Principle 9 — User data is portable
**A user can export everything: history, memory, agents, workflows, integrations.**

We do not lock in users by holding their data hostage. Portability is a feature and a guarantee. If a user leaves NEXUS, their work continues to function.

*Implication:* Export is a first-class operation, not a support ticket. Open formats (Markdown, JSON, CSV) are required for core data types.

### Principle 10 — Speed of execution
**A small team shipping rapidly beats a large team shipping slowly.**

NEXUS is built by a small number of humans coordinating a much larger AI team. Decisions are made fast. Iteration cycles are measured in days, not quarters. When in doubt, ship the simpler version and improve it.

*Implication:* Quarterly OKRs exist but do not gate weekly decisions. The bias is to act, then correct.

### Principle 11 — Honest disclosure
**NEXUS discloses when an action is performed by an agent.**

We do not pretend agents are humans, or humans are agents. Every UI element makes its origin visible. Generated content is marked. Recommendations are distinct from autonomous actions.

*Implication:* Avatar, badge, or label conventions are part of the design system. Lying-by-omission is treated as a brand-damaging offense.

### Principle 12 — Build for the long term
**Decisions are evaluated over 10 years, not 10 weeks.**

We avoid architectural choices that create short-term velocity at long-term cost. We avoid business models that require lock-in to survive. We avoid product patterns that optimize for hype cycles.

*Implication:* "It's easier right now" is a weak argument. "It will still be right in 2031" is a strong one.

## 3. Precedence order

When principles conflict, the order below is authoritative. Higher-numbered principles do not override lower-numbered ones in this list.

1. **Privacy is structural** (P4) — never compromised for any other principle.
2. **Human authority preserved** (P2) — never bypassed for convenience or speed.
3. **Reliability earns trust** (P5) — never traded for new features in production.
4. **Transparency by default** (P3) — required wherever it conflicts with elegance.
5. **User data is portable** (P9) — never withheld to improve retention metrics.
6. **Honest disclosure** (P11) — non-negotiable in user-facing surfaces.
7. **Quality at the source** (P8) — never waived to ship faster.
8. **Intent over navigation** (P1) — guides product design.
9. **Progressive disclosure** (P6) — guides information architecture.
10. **Modularity over monolith** (P7) — guides architecture.
11. **Speed of execution** (P10) — guides process.
12. **Build for the long term** (P12) — guards against short-termism.

Note: a higher-numbered principle is **not** more important. The numbering indicates the order in which conflicts are resolved when no other rule applies. P4 > P11 in absolute priority; P10 governs only when P1–P9 do not apply.

## 4. Anti-patterns we reject

These are decisions we have seen other companies make that NEXUS will not:

| Anti-pattern | Why we reject it |
|--------------|------------------|
| Engagement-optimized feeds | Engagement is not the user's goal |
| Dark-pattern permission flows | Erodes trust permanently |
| Forced account creation | Reduces accessibility |
| Telemetry-on by default | Violates P4 |
| Vendor lock-in for growth | Violates P9 |
| Single-model architecture | Violates P7 |
| Premature scaling | Wastes runway and attention |
| "Move fast and break things" in a browser | Violates P5 |
| AI agents that act without logging | Violates P3 |
| Marketing claims that exceed capability | Violates P11 |
| Acqui-hiring instead of building | Dilutes mission clarity |

## 5. Decision checklist

Every material decision (product, engineering, hiring, partnership) must answer "yes" to all of:

- [ ] Does this serve intent over navigation? (P1)
- [ ] Does this preserve human authority over high-impact actions? (P2)
- [ ] Is the action visible, explainable, reversible? (P3)
- [ ] Does this respect privacy structurally? (P4)
- [ ] Is this reliable? (P5)
- [ ] Is the complexity appropriate to the user? (P6)
- [ ] Are the components replaceable? (P7)
- [ ] Is quality built in? (P8)
- [ ] Can the user take their data with them? (P9)
- [ ] Are we moving fast without sacrificing principles 1–9? (P10)
- [ ] Are we being honest about what this is? (P11)
- [ ] Will we still be glad we made this decision in 2031? (P12)

If any answer is "no" or "uncertain," the decision is paused until it can be made consistent with the principles.

## 6. How principles evolve

Principles are not laws of physics. They are inherited from the founder's judgment and may be amended — but only deliberately:

1. A proposed amendment is written as a Markdown document with rationale.
2. It is reviewed by all executive agents and the human founder.
3. It is either accepted (with version bump) or rejected (with written reasoning).
4. Amendments are rare; the existence of an amendment is itself a signal.

The current version of the principles has not been amended since v0.1.0.

## 7. Reading list

- **Vision** — NX-DOC-0002
- **Mission** — NX-DOC-0003
- **Product Philosophy** — NX-DOC-0005
- **Technical Principles** — NX-DOC-0011
- **AI-First Design Philosophy** — NX-DOC-0006

---

*End NX-DOC-0004.*