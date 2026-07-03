# NX-FEAT-1104 — Workspace Notes

| Field | Value |
|-------|-------|
| **Document ID** | NX-FEAT-1104 |
| **Title** | Workspace Notes |
| **Area** | NX-FEAT-A0002 — Workspaces |
| **Owner** | Frontend AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P1 |
| **Horizon target** | H1 |
| **Estimated effort** | M |

---

## 1. Purpose
Each Workspace has a rich-text notes surface for capturing thoughts, decisions, references, and ongoing context.

## 2. User stories
- As Sara, I want to take notes during research that stay with the project.
- As Devin, I want notes linked to code blocks.

## 3. Functional requirements
### FR-1: Rich text editor
- Markdown-based; renders as formatted text.
- Headings, lists, bold, italic, code, links, blockquotes.
- Inline AI: "Continue writing," "Summarize," "Expand."

**Acceptance:**
- [ ] Edits autosave every 5 seconds.
- [ ] Markdown round-trips losslessly.

### FR-2: Notes structure
- Hierarchical pages (multiple notes per Workspace).
- Tags and backlinks.

### FR-3: Search within notes
- Full-text search.
- <500ms for 1MB of notes.

## 4. Non-functional requirements
- Performance: 60fps typing.
- Reliability: durable.

## 5. UI surfaces
- Workspace content panel; dedicated Notes tab.

## 6. Permissions
- Read/write: editor+.
- Read: viewer.

## 7. Telemetry
- `workspace_notes.edited`
- `workspace_notes.searched`

## 8. Failure modes
- Sync conflict: 3-way merge; flag unresolved.

## 9. Dependencies
- Markdown parser.
- Sync engine.

## 10. Out of scope
- Real-time co-editing (H2).
- Inline database / kanban (H2).

## 11. Acceptance criteria summary
- [ ] Markdown round-trip lossless.
- [ ] Autosave within 5 seconds.
- [ ] Search <500ms.

## 12. Open questions
- Q: Should notes be plain Markdown files for export, or proprietary format?

## 13. Change log
| Date | Change | Author |
|------|--------|--------|
| 2026-06-30 | Initial spec | Frontend AI |

---

*End NX-FEAT-1104.*