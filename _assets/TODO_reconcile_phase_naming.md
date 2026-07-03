# TODO — Reconcile PROGRESS Phase 6–10 with directory structure

✅ DONE.

## What was wrong

PROGRESS.md's Phase 6–10 table used compact names ("Browser / AI Infrastructure / Marketplace / Enterprise / Future") with no indication of which directories each phase covered. The actual repo has 8 directories (`04_BROWSER_ENGINE`, `07_BACKEND`, `08_SECURITY`, `09_MARKETPLACE`, `10_DEPLOYMENT`, `11_BUSINESS`, `12_DEVELOPER_GUIDE`, `99_MASTER_PROMPTS`) that need to be assigned to phases.

The 00_EXECUTIVE docs (Cover, Technical Principles, Master PRD) already use the thematic phase labels ("Phase 6 = Browser Architecture", "Phase 7 = AI Infrastructure", "Phase 8 = Marketplace", "Phase 9 = Enterprise", "Phase 10 = Future") and tie ID ranges to them (e.g., NX-API = Phase 7). So phase numbers are **load-bearing** — they can't be changed.

## What was done

1. **Updated PROGRESS.md Phase 6–10 table** to add a "Directories" column showing which dirs each phase spans, plus a "Subdirs" and "Docs" count for honest progress tracking.
2. **Added a "Directories NOT yet assigned" subsection** that documents the empty placeholder dirs (`02_DESIGN_SYSTEM/Mobile`, `05_AI_PLATFORM/{topic subdirs}`, etc.) and notes they belong to earlier phases as supplements, not separate phases.
3. **Added an "Open question" note** acknowledging the 1:many phase-to-directory relationship and the option to tighten it later.
4. **Updated MASTER_INDEX.md** to replace "To be indexed as they are produced" with a real Phase 6–10 table that points back to PROGRESS.md for detail.
5. **Added 2 decisions to the log** (thematic phase clarification, dir reconciliation).

## The mapping (final)

| Phase | Title | Directories |
|---|---|---|
| 6 | Browser Architecture | `04_BROWSER_ENGINE/` |
| 7 | AI Infrastructure | `07_BACKEND/` + `05_AI_PLATFORM/` substrate |
| 8 | Marketplace | `09_MARKETPLACE/` + `08_SECURITY/` |
| 9 | Enterprise Platform | `11_BUSINESS/` |
| 10 | Future Expansion | `10_DEPLOYMENT/` + `12_DEVELOPER_GUIDE/` + `99_MASTER_PROMPTS/` |

## Open question for the user

Phases 7–10 each span multiple directories. Two options going forward:

(a) Tighten scope: each phase = one directory. This would mean the "Phase 7 = AI Infrastructure" name is wrong; `07_BACKEND` is just backend, not all of AI infra. The label would need renaming.

(b) Keep themes: multiple directories per phase. The current choice. Requires explicit mapping tables (which we now have).

If the user has a preference, we should record it. Default: keep (b).
