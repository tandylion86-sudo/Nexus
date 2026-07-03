# NX-FEAT-1105 — Workspace Files

| Field | Value |
|-------|-------|
| **Document ID** | NX-FEAT-1105 |
| **Title** | Workspace Files |
| **Area** | NX-FEAT-A0002 — Workspaces |
| **Owner** | Frontend AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P1 |
| **Horizon target** | H1 |
| **Estimated effort** | M |

---

## 1. Purpose
Each Workspace has file storage for uploads, generated outputs, and references. Files are auto-organized and indexed.

## 2. User stories
- As Marcus, I want to upload CSVs and have NEXUS analyze them.
- As Maya, I want agent outputs (PDFs, spreadsheets) saved to the Workspace.

## 3. Functional requirements
### FR-1: Upload and storage
- Drag-drop, paste, file picker.
- Per Workspace storage quota.
- Supported: PDF, images, CSV, JSON, Markdown, text, code.

**Acceptance:**
- [ ] Up to 100MB per file.
- [ ] Bulk upload (multi-select).

### FR-2: Auto-organization
- Files tagged by type, source, date.
- Searchable by content (OCR for images, full-text for docs).

### FR-3: Preview
- In-Workspace preview for images, PDFs, CSVs, code.
- "Open in viewer" for full-screen.

### FR-4: RAG indexing
- Indexed for retrieval by Memory Engine (NX-FEAT-1714).

## 4. Non-functional requirements
- Upload speed: parallel chunks.
- Storage: encrypted at rest.

## 5. UI surfaces
- Workspace Files panel.

## 6. Permissions
- Read/write: editor+.
- Read: viewer.

## 7. Telemetry
- `workspace_files.uploaded`
- `workspace_files.deleted`
- `workspace_files.previewed`

## 8. Failure modes
- Quota exceeded: clear error.
- Upload fails: retry with backoff.
- Unsupported format: convert or reject with explanation.

## 9. Dependencies
- S3-compatible storage.
- OCR service (Tesseract or cloud).

## 10. Out of scope
- Video files (H2).
- Real-time collaborative editing (H2).

## 11. Acceptance criteria summary
- [ ] Drag-drop upload works.
- [ ] Preview for supported formats.
- [ ] Search across files works.

## 12. Open questions
- Q: Should there be a per-Workspace storage cap independent of plan storage?

## 13. Change log
| Date | Change | Author |
|------|--------|--------|
| 2026-06-30 | Initial spec | Frontend AI |

---

*End NX-FEAT-1105.*