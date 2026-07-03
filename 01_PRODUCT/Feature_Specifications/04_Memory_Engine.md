# NX-FEAT-1700 — Memory Engine (Anchor Spec)

| Field | Value |
|-------|-------|
| **Document ID** | NX-FEAT-1700 |
| **Title** | Memory Engine (Anchor Spec) |
| **Area** | NX-FEAT-A0008 — Memory Engine |
| **Owner** | AI Platform AI |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-06-30 |
| **Priority (H1)** | P0 |
| **Horizon target** | H1 |
| **Estimated effort** | XL (decomposed into NX-FEAT-1701-1714) |

---

## 1. Purpose

The **Memory Engine** is NEXUS's long-term knowledge store about the user, their projects, and the system's own actions. It is what makes NEXUS feel personalized rather than generic.

Memory powers:
- Personalized defaults (writing style, tone, length).
- Context-aware responses (current project, recent tasks).
- Cross-session continuity (resume where you left off).
- Trust through transparency (user can see what NEXUS remembers).

This document is the anchor spec; leaf features (NX-FEAT-1701 through 1714) inherit from it.

## 2. Why memory matters

Without memory:
- Every conversation starts from zero.
- NEXUS asks the same questions repeatedly.
- The product feels generic.

With memory:
- NEXUS knows your style, your projects, your preferences.
- Recommendations are tailored.
- The product compounds in value over time.

Memory is the **switching cost** that protects NEXUS from being trivially replaced.

## 3. User stories

- As **Maya**, I want NEXUS to remember my brand voice so I don't restate it every content brief.
- As **Devin**, I want NEXUS to remember my project's stack so it can suggest correct code.
- As **Sara**, I want NEXUS to remember facts I've confirmed so I don't re-verify them.
- As **Marcus**, I want NEXUS to remember my team's SOPs so workflows are consistent.
- As **Riya**, I want full visibility and control over what NEXUS remembers.
- As **Thea**, I want team members to share project memory but keep personal memory private.

## 4. Functional requirements

### FR-1: Preference memory
**Description:** NEXUS remembers user-stated or inferred preferences.
**Acceptance:**
- [ ] Preferences: writing tone, length, format, language, theme, motion, etc.
- [ ] User can edit preferences explicitly via settings.
- [ ] NEXUS infers preferences from behavior; user can confirm/reject.
- [ ] Preferences are workspace-scoped or global, configurable.

### FR-2: Project state memory
**Description:** NEXUS remembers facts about each project (Workspace).
**Acceptance:**
- [ ] Facts include: entities (people, companies, products), decisions, files, sources.
- [ ] Facts are auto-extracted from conversations and actions.
- [ ] Facts are searchable per Workspace.
- [ ] Facts can be edited or deleted.

### FR-3: Conversation memory
**Description:** NEXUS remembers key facts from past conversations.
**Acceptance:**
- [ ] Each conversation is summarized into key facts.
- [ ] User can see and edit the summary.
- [ ] Summary is linked to source conversation (for verification).
- [ ] Summary is searchable across all conversations.

### FR-4: Style memory
**Description:** NEXUS learns the user's writing style from their outputs.
**Acceptance:**
- [ ] Style profile built from ≥5 samples.
- [ ] Style is applied to AI-generated content unless overridden.
- [ ] Style is editable.
- [ ] Style can be disabled per Workspace.

### FR-5: Memory inspector
**Description:** A UI for users to see all memory items.
**Acceptance:**
- [ ] List view: all memory items, sortable by recency, type, workspace.
- [ ] Detail view: source, date, confidence, related items.
- [ ] Filters: by type, by workspace, by source.
- [ ] Search across all memory.

### FR-6: Memory edit / delete
**Description:** Users can edit or delete any memory item.
**Acceptance:**
- [ ] Edit in place; changes propagate to all dependent responses.
- [ ] Delete is irreversible; confirm dialog.
- [ ] Bulk operations: delete by type, by workspace, by date.
- [ ] All edits are logged in Activity Log.

### FR-7: Memory export
**Description:** Users can export all memory in a portable format.
**Acceptance:**
- [ ] Export format: JSON-LD + Markdown.
- [ ] Export includes all memory items with metadata.
- [ ] Export is encrypted with user passphrase.
- [ ] Export is portable to other NEXUS instances (NX-FEAT-1708).

### FR-8: Memory import
**Description:** Users can import memory from another NEXUS instance or backup.
**Acceptance:**
- [ ] Import requires explicit user consent.
- [ ] Conflicts are surfaced for user resolution.
- [ ] Import can be partial (by type, by date, by workspace).

### FR-9: Cross-Workspace memory scope
**Description:** Memory can be Workspace-scoped or cross-Workspace.
**Acceptance:**
- [ ] Default: memory is Workspace-scoped.
- [ ] User can mark memory as cross-Workspace.
- [ ] Cross-Workspace memory is searchable across all Workspaces.
- [ ] Cross-Workspace memory is opt-out per item.

### FR-10: Memory relevance ranking
**Description:** Memory is ranked by relevance to current context.
**Acceptance:**
- [ ] Ranking considers: recency, type, workspace, current task.
- [ ] Top-K memory items are loaded into context.
- [ ] User can see "why this was included" attribution.

### FR-11: Memory auto-deletion (TTL)
**Description:** Memory can auto-delete after a configurable TTL.
**Acceptance:**
- [ ] TTL is configurable per type (default: never for preferences; 1 year for conversations).
- [ ] User can pin memory to prevent auto-deletion.
- [ ] User is warned before deletion.

### FR-12: Encrypted-at-rest storage
**Description:** Memory is encrypted at rest.
**Acceptance:**
- [ ] Encryption: AES-256-GCM or equivalent.
- [ ] Key derived from user passphrase or hardware-backed.
- [ ] Memory is unreadable without authentication.

### FR-13: Knowledge graph (entities, relations)
**Description:** Memory builds a knowledge graph of entities and relations.
**Acceptance:**
- [ ] Entities: people, companies, products, concepts.
- [ ] Relations: works-at, owns, related-to, etc.
- [ ] Graph is queryable (NX-FEAT-1713).
- [ ] Graph visualization in UI (basic).

### FR-14: RAG over user documents
**Description:** NEXUS can retrieve from user's uploaded documents.
**Acceptance:**
- [ ] Supported formats: PDF, Markdown, text, HTML, CSV.
- [ ] Index size up to 1M tokens per user (H1); 10M (H2).
- [ ] Retrieval is <500ms.
- [ ] Citations link to source passages.

## 5. Non-functional requirements

### NFR-1: Performance
- Memory read: <100ms.
- Memory write: <200ms.
- Memory search: <500ms for 10K items.
- RAG retrieval: <500ms.

### NFR-2: Reliability
- Memory durability: 99.999%.
- No silent memory loss.

### NFR-3: Security
- Memory encrypted at rest (NFR-12).
- Memory encrypted in transit (TLS 1.3).
- Memory export is encrypted.
- No cross-user memory leakage.

### NFR-4: Privacy
- Memory is private by default.
- User can disable any memory type.
- Memory is included in account deletion (30-day retention).
- Memory is included in account export.

### NFR-5: Cost
- Memory storage: ≤$0.05/user/month at H1 scale.
- Embedding generation: batched to minimize cost.

## 6. UI surfaces

| Surface | Reference |
|---------|-----------|
| Memory inspector | NX-UI-6401 |
| Memory item detail | NX-UI-6402 |
| Memory preferences | NX-UI-6403 |
| Memory export dialog | NX-UI-6404 |
| Memory import dialog | NX-UI-6405 |
| Knowledge graph view | NX-UI-6406 |
| Style profile editor | NX-UI-6407 |

## 7. Permissions

Memory requires:

- Read: agent (within scope).
- Write: agent (with permission to extract facts); user (manual).
- Delete: user only.
- Export: user only.
- Inspect: user only.

## 8. Telemetry

Memory-specific telemetry (opt-in):

- `memory.fact.added`
- `memory.fact.updated`
- `memory.fact.deleted`
- `memory.style.profile_updated`
- `memory.export.completed`
- `memory.import.completed`

Memory item count and storage size are surfaced to user (not telemetry).

## 9. Failure modes

| Failure | Behavior |
|---------|----------|
| Embedding service unavailable | Memory search degrades; keyword search works |
| Memory corruption | Recover from last snapshot; user warned |
| Storage full | Oldest unpinned items deleted; user warned |
| Import conflict | Surface conflict; user resolves |
| Cross-Workspace privacy violation | Detected in QA; blocked |

## 10. Dependencies

- Storage backend (PostgreSQL + pgvector in H1).
- Embedding service (configurable).
- Encryption library (libsodium or equivalent).
- Workspace system (for scoping).

## 11. Out of scope

- Memory sharing with other users (except via Workspace sharing).
- Memory-as-product (selling user memory) — explicitly forbidden by NX-DOC-0004 P4.
- Memory-based advertising — explicitly forbidden.
- Federated memory across organizations (H2+).

## 12. Acceptance criteria summary

Memory Engine is done when:

- [ ] User can inspect, edit, delete, and export all memory.
- [ ] Preferences persist across devices.
- [ ] Style memory improves response quality measurably.
- [ ] RAG over 10K documents returns relevant results in <500ms.
- [ ] No silent memory loss in 6-month soak test.
- [ ] All memory is encrypted at rest.
- [ ] Account deletion removes all memory within 30 days.

## 13. Sub-features (leaf specs)

| ID | Name |
|----|------|
| NX-FEAT-1701 | Preference memory |
| NX-FEAT-1702 | Project state memory |
| NX-FEAT-1703 | Conversation memory |
| NX-FEAT-1704 | Style memory |
| NX-FEAT-1705 | Memory inspector |
| NX-FEAT-1706 | Memory edit / delete |
| NX-FEAT-1707 | Memory export |
| NX-FEAT-1708 | Memory import |
| NX-FEAT-1709 | Cross-Workspace memory scope |
| NX-FEAT-1710 | Memory relevance ranking |
| NX-FEAT-1711 | Memory auto-deletion (TTL) |
| NX-FEAT-1712 | Encrypted-at-rest storage |
| NX-FEAT-1713 | Knowledge graph |
| NX-FEAT-1714 | RAG over user documents |

## 14. Open questions

- Q: How do we balance memory "stickiness" with privacy — when should memory expire by default?
- Q: Should we support memory sharing across user accounts (e.g., family members)?
- Q: How do we handle memory of sensitive content (medical, financial)?
- Q: Should memory be encrypted with user-controlled keys for extra privacy?

## 15. Change log

| Date | Change | Author |
|------|--------|--------|
| 2026-06-30 | Initial anchor spec | AI Platform AI |

---

*End NX-FEAT-1700.*