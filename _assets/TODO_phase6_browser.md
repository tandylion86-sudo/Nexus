# TODO — Phase 6: Browser Architecture (`04_BROWSER_ENGINE/`)

## Goal
Write the browser architecture documentation grounded in the existing Phase 1 (Vision/Tech Principles) and Phase 2 (Cloud Browser Fleet anchor NX-FEAT-1600) docs.

## Result: ✅ DONE

## What was written

9 architecture docs, 10,145 words total:

| ID | File | Words |
|----|------|------:|
| NX-ARCH-0001 | `00_Overview.md` | 837 |
| NX-ARCH-0101 | `Chromium_Layer/01_Chromium_Integration.md` | 1,034 |
| NX-ARCH-0102 | `Rendering/02_Rendering_Pipeline.md` | 976 |
| NX-ARCH-0103 | `Profiles/03_Profile_System.md` | 1,212 |
| NX-ARCH-0104 | `History/04_History_Engine.md` | 1,107 |
| NX-ARCH-0105 | `Sync/05_Sync_Protocol.md` | 1,411 |
| NX-ARCH-0106 | `Downloads/06_Download_Manager.md` | 1,076 |
| NX-ARCH-0107 | `Extension_API/07_Extension_Runtime.md` | 1,285 |
| NX-ARCH-0108 | `Performance/08_Performance_Architecture.md` | 1,207 |

## What was created/changed

- **New doc ID prefix `NX-ARCH-####`** added to `00_EXECUTIVE/01_Cover_and_Document_Control.md` (range 0001–0999, assigned starting in Phase 6).
- **New file `_assets/DOCUMENT_REGISTRY.md`** tracks every issued doc ID. Lists all 12 Phase 1 docs and all 9 Phase 6 docs.
- **PROGRESS.md** updated: Phase 6 status moved to 🟡 In progress, with per-doc word counts and totals.
- **MASTER_INDEX.md** updated: added Phase 6 section with overview + 8 leaf docs.

## Design choices made

- **Doc IDs** follow `NX-ARCH-0001` (overview) and `NX-ARCH-0101..0108` (one per subdir). Leaves room for Phase 7 to use `NX-ARCH-0201..0299`.
- **Each leaf doc has the same 10-section structure** as Phase 5 manifests, but adapted: identity table, mission, architecture/design, key decisions, interfaces, performance/limits, security, open questions, reading list.
- **Overview doc sets the layered architecture** (Mermaid diagram) that the leaf docs elaborate.
- **Each leaf doc cross-references the overview and the Browser AI manifest** (NX-EM-9611) in its reading list.
- **Performance budget doctrine** (NX-ARCH-0108) is the doc that other phases will reference for any performance claim.

## Verification

- All 8 subdirs of `04_BROWSER_ENGINE/` now have a doc.
- Zero empty subdirs in `04_BROWSER_ENGINE/`.
- All 8 leaf docs reference the overview (NX-ARCH-0001) at least twice.
- All 8 leaf docs reference the Browser AI manifest (NX-EM-9611) in their reading list.
- The Cloud Browser Fleet anchor (NX-FEAT-1600) is referenced where appropriate (Profile, Sync, History, Downloads, Performance).
- The Technical Principles (NX-DOC-0011) are explicitly cited in every doc.

## What's NOT in Phase 6

This phase is **architecture-level**. The leaf docs describe *how* the browser is built, not *what* features users have. The user-facing features (per NX-FEAT-1601..1614) are the consumer of this architecture.

Future work in this phase (if continued):
- Cloud Browser container orchestration specifics (per `_assets/chromium_lts.md` was referenced; file doesn't exist yet — would be a follow-up).
- Sub-area specs within each subdir (e.g., specific CDP integrations, specific extension patterns).
- ADR-format decision records for non-trivial choices.

## Repo totals after this work

- 301 docs / ~132,000 words / ~527 pages
- Phases 1–5 complete, Phase 6 in progress
- 0 empty subdirs in Phase 6
- New ID prefix and registry in place
