# NEXUS Blueprint — AI Role Manifests (Phase 5)

Seven role manifest documents for the engineering org's AI agents. Each is a short, specific operational document for one of the empty subdirs under `06_ENGINEERING_TEAM/`.

| Subdir | Manifest file | Role | Reports to | Primary agent ID |
|---|---|---|---|---|
| `CEO_AI/` | `01_CEO_AI_Manifest.md` | CEO Agent | Founder | NX-AGENT-7050 |
| `CTO_AI/` | `02_CTO_AI_Manifest.md` | CTO Agent | CEO | NX-AGENT-7051 |
| `Backend_AI/` | `03_Backend_AI_Manifest.md` | Backend Agent | CTO | NX-AGENT-7055 |
| `QA_AI/` | `04_QA_AI_Manifest.md` | QA Agent | CPO | NX-AGENT-7059 |
| `Security_AI/` | `05_Security_AI_Manifest.md` | Security Agent | CTO | NX-AGENT-7058 |
| `Documentation_AI/` | `06_Documentation_AI_Manifest.md` | Documentation Agent | CPO | NX-AGENT-7061 |
| `Marketing_AI/` | `07_Marketing_AI_Manifest.md` | Marketing Agent | CEO | NX-AGENT-7062 |

**Why these seven?** The org chart in NX-WF-9001 names exactly these 7 roles as direct owner-roles referenced by the existing Phase 5 docs (Quality Gates is "Owner: QA AI", Escalation Paths is "Owner: CEO AI", etc.). Frontend, Browser, AI Platform, DevOps, Research, and Finance agents are also referenced but the dir structure only contains these 7.

**Format.** Each manifest is a ~500–900 word document with the same structure:

1. Identity (agent ID, version, status, dependencies)
2. Mission (one sentence)
3. Authority & decision rights (what they can decide alone, what requires escalation)
4. Owned workflows (which of the 12 SOPs they own or co-own)
5. Owned quality gates (which of the 9 gates they enforce)
6. Day-to-day responsibilities (concrete activities)
7. Inputs / outputs (what they consume, what they produce)
8. Escalation rights (when they go up, when they're escalated to)
9. Anti-patterns (what this role should NOT do)
10. Reading list

**Doc IDs.** Continue the `NX-AT-####` or create a new range. The `NX-WF-####` range is used for workflows (9001–9004) and `NX-AT-9501` for the test suite. These are manifests — I'll use `NX-AT-####` style with new IDs `NX-AT-9601` through `NX-AT-9607` to keep them grouped as "auxiliary engineering docs" near the acceptance test suite.

Actually, looking again: NX-WF-9001–9004 are workflow docs, NX-AT-9501 is acceptance tests. The cleanest grouping is to start a new range. I'll use `NX-EM-####` (Engineering Manifest) starting at 9601. This keeps the convention readable.

**Writing order.** Will write all 7 in one batched operation since each is independent.

**After writing:** update PROGRESS.md to note these are done, and update MASTER_INDEX.md to reference them.
