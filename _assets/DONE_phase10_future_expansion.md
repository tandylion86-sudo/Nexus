# TODO — Phase 10: Future Expansion

## Goal
Document the **operational & developer-facing** surface that doesn't fit cleanly into a "what NEXUS does for users" phase:

- **Deployment** (`10_DEPLOYMENT/`) — Docker, K8s, CI/CD, monitoring, scaling, DR
- **Developer Guide** (`12_DEVELOPER_GUIDE/`) — coding standards, API docs, SDK, plugins, contribution
- **Master Prompts** (`99_MASTER_PROMPTS/`) — diagrams and workflow templates used to drive AI-assisted authoring of the rest of the blueprint

This is the last phase. The plan is ~13 docs / ~15k words / ~60 pages.

## Scope (and what is NOT in this phase)

**In scope:**
- Operational runbooks (Docker, K8s, CI/CD, Monitoring, Scaling, DR) — the "how it gets to production" complement to the Phase 7 "what runs in production".
- The developer experience: how a third-party developer writes a NEXUS plugin/agent, contributes to the codebase, or uses the SDK/API.
- The master prompt library that future AI agents (and humans) use to generate new blueprint content consistently.

**NOT in scope:**
- Phase 6 (browser internals) and Phase 7 (backend architecture) — those describe *what's running*. This phase describes *how it gets there* and *how to build on it*.
- Per-cloud deployment specifics (Phase 7 §Infrastructure made the cloud-philosophy decision; this phase captures the concrete K8s manifests / CI pipelines / dashboards structure, but not the actual YAML — that lives in `infra/` in the implementation repo).
- Implementation-specific code (the SDK *interface* is documented; the actual `npm install @nexus/sdk` package lives in the implementation repo).

## ID scheme

Continue the `NX-ARCH-` prefix. Phase 10 uses the 0300 range (after Phase 7's 0200s).

- `NX-ARCH-0003` — Phase 10 overview ("Future Expansion Overview")
- `NX-ARCH-0301..0306` — Deployment leaves (6)
- `NX-ARCH-0401..0405` — Developer Guide leaves (5)
- `NX-ARCH-0501..0502` — Master Prompts leaves (2)

Total: 14 docs.

## Subdir → doc mapping

| Subdir | Doc ID | Title |
|--------|--------|-------|
| (root) | NX-ARCH-0003 | Future Expansion Overview |
| 10_DEPLOYMENT/Docker/ | NX-ARCH-0301 | Docker Image Strategy |
| 10_DEPLOYMENT/Kubernetes/ | NX-ARCH-0302 | Kubernetes Manifests & Helm Charts |
| 10_DEPLOYMENT/CI_CD/ | NX-ARCH-0303 | CI/CD Pipelines |
| 10_DEPLOYMENT/Monitoring/ | NX-ARCH-0304 | Monitoring & Observability Stack |
| 10_DEPLOYMENT/Scaling/ | NX-ARCH-0305 | Scaling & Capacity Planning |
| 10_DEPLOYMENT/Disaster_Recovery/ | NX-ARCH-0306 | Disaster Recovery & Business Continuity |
| 12_DEVELOPER_GUIDE/Coding_Standards/ | NX-ARCH-0401 | Coding Standards & Style Guide |
| 12_DEVELOPER_GUIDE/API_Docs/ | NX-ARCH-0402 | API Documentation Standards |
| 12_DEVELOPER_GUIDE/SDK/ | NX-ARCH-0403 | SDK Design & Usage |
| 12_DEVELOPER_GUIDE/Plugin_Development/ | NX-ARCH-0404 | Plugin Development Guide |
| 12_DEVELOPER_GUIDE/Contribution_Guide/ | NX-ARCH-0405 | Contribution Guide & Governance |
| 99_MASTER_PROMPTS/Workflows/ | NX-ARCH-0501 | Master Workflow Prompts |
| 99_MASTER_PROMPTS/Diagrams/ | NX-ARCH-0502 | Diagram Library & Conventions |

## Per-doc structure (template, same as Phases 6/7)

1. Mission
2. Core concepts / taxonomy
3. Architecture / process diagram (Mermaid)
4. Key decisions
5. Interfaces / contracts / interfaces with other systems
6. Performance / reliability budgets (where applicable)
7. Security considerations
8. Failure modes
9. Open questions
10. Reading list

Plus doc-ID header (identity table) consistent with Phases 6/7.

Target length: 800–1500 words per leaf.

## Steps

- [x] Plan doc IDs and subdir mapping
- [x] Read upstream context (Phase 7 done; need to skim 06_ENGINEERING_TEAM, 09_MARKETPLACE briefly for the SDK/plugin context, 10_DEPLOYMENT subdirs are empty)
- [ ] Write `00_Overview.md` (NX-ARCH-0003) — frames the three-bucket structure
- [ ] Write `10_DEPLOYMENT/Docker/01_Docker_Image_Strategy.md` (NX-ARCH-0301)
- [ ] Write `10_DEPLOYMENT/Kubernetes/02_Kubernetes_and_Helm.md` (NX-ARCH-0302)
- [ ] Write `10_DEPLOYMENT/CI_CD/03_CI_CD_Pipelines.md` (NX-ARCH-0303)
- [ ] Write `10_DEPLOYMENT/Monitoring/04_Monitoring_and_Observability.md` (NX-ARCH-0304)
- [ ] Write `10_DEPLOYMENT/Scaling/05_Scaling_and_Capacity.md` (NX-ARCH-0305)
- [ ] Write `10_DEPLOYMENT/Disaster_Recovery/06_Disaster_Recovery.md` (NX-ARCH-0306)
- [ ] Write `12_DEVELOPER_GUIDE/Coding_Standards/01_Coding_Standards.md` (NX-ARCH-0401)
- [ ] Write `12_DEVELOPER_GUIDE/API_Docs/02_API_Documentation.md` (NX-ARCH-0402)
- [ ] Write `12_DEVELOPER_GUIDE/SDK/03_SDK_Design.md` (NX-ARCH-0403)
- [ ] Write `12_DEVELOPER_GUIDE/Plugin_Development/04_Plugin_Development.md` (NX-ARCH-0404)
- [ ] Write `12_DEVELOPER_GUIDE/Contribution_Guide/05_Contribution_Guide.md` (NX-ARCH-0405)
- [ ] Write `99_MASTER_PROMPTS/Workflows/01_Master_Workflows.md` (NX-ARCH-0501)
- [ ] Write `99_MASTER_PROMPTS/Diagrams/02_Diagram_Library.md` (NX-ARCH-0502)
- [ ] Update PROGRESS.md
- [ ] Update MASTER_INDEX.md
- [ ] Update DOCUMENT_REGISTRY.md
- [ ] Update README.md
- [ ] Verify

## Risks

- **Length creep**: 14 docs at 1,000+ words = ~14k words. That's a lot for one phase. Mitigation: shorter docs (800 words) for the narrower topics (Coding Standards, Diagram Library).
- **Drift from implementation**: this phase is closest to "implementation" in the blueprint. Mitigation: stay at architecture/process level, defer specific YAML/SDK code to the implementation repo.
- **Master Prompts is meta**: it's the prompts that generate the rest of the blueprint, not user-facing. Mitigation: frame as "the operating manual for the AI agents that maintain this repository".
