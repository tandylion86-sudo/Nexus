# NX-PRD-0007 — Target Audiences & Personas (Product Reference)

| Field | Value |
|-------|-------|
| **Document ID** | NX-PRD-0007 |
| **Title** | Target Audiences & Personas — Product Reference |
| **Phase** | 2 — Product Requirements (reference to Phase 1 source) |
| **Owner** | Product AI (`NX-EM-9609`) |
| **Status** | 🟢 Complete (redirect to canonical source) |
| **Version** | 0.1.0 |
| **Created** | 2026-07-03 |
| **Last Updated** | 2026-07-03 |
| **Classification** | Confidential — Internal |
| **Distribution** | Founders, executive AI, all engineering AI, Marketing AI, Research AI |
| **Canonical source** | [`00_EXECUTIVE/07_Target_Audiences_and_Personas.md`](../00_EXECUTIVE/07_Target_Audiences_and_Personas.md) — `NX-DOC-0007` |
| **Related** | `NX-DOC-0008` (Competitive Landscape), `NX-DOC-0010` (Goals & Metrics), `NX-DOC-0012` (Business Strategy), `NX-PRD-0002` (Persona × Feature Matrix), `NX-PRD-0003` (User Journeys) |

---

## 1. Purpose

This document exists to give **`NX-PRD-0007` a real, on-disk home**. Three engineering manifests (`Marketing_AI`, `Research_AI`, `Product_AI`) reference `NX-PRD-0007` in their reading lists and dependency tables, but the underlying content was authored as a Phase-1 executive document under `NX-DOC-0007` and lives in `00_EXECUTIVE/`.

There is exactly one canonical source for the personas: `00_EXECUTIVE/07_Target_Audiences_and_Personas.md`. **Do not duplicate the content here.** This document:

1. Records the `NX-PRD-0007` → `NX-DOC-0007` identity for the registry.
2. Adds the **Phase-2 product framing** — i.e. the rules that govern how personas are used in PRD authoring, feature design, and acceptance testing. The personas themselves are in the canonical source; the *usage contract* is here.
3. Provides the anchor link the manifests need to resolve `NX-PRD-0007` without re-typing the path.

## 2. Identity mapping

| Phase-2 reference | Phase-1 source | Status |
|-------------------|----------------|--------|
| `NX-PRD-0007` (Target Audiences & Personas) | `NX-DOC-0007` (`00_EXECUTIVE/07_Target_Audiences_and_Personas.md`) | 🟢 Identity established 2026-07-03; recorded in `_assets/DOCUMENT_REGISTRY.md` |

This mapping is **one-way and stable**: `NX-PRD-0007` is an alias for `NX-DOC-0007`. Future work that needs the personas must read the canonical source, not this file. If the personas ever diverge between Executive (`NX-DOC-0007`) and Product (`NX-PRD-0007`), the Executive version wins; the Product version is for cross-references and usage contract only.

## 3. Phase-2 usage contract

The personas defined in the canonical source (`NX-DOC-0007`) are the binding input to every Phase-2 deliverable. The rules below govern *how* they are used:

### 3.1 In the PRD (`01_PRODUCT/`)

- Every requirement in `01_PRODUCT/00_Master_PRD.md` and any sub-PRD **MUST** cite the persona(s) it serves. Acceptable citation forms: inline `(Persona: P3 — "AI-Augmented Developer")`, or a column in a requirements table.
- A requirement with no persona citation is **incomplete** and returns to the author for revision.
- A requirement serving a persona **not** present in `NX-DOC-0007` MUST be flagged as a candidate-new-persona; the owning manifest (Product AI) must either reject the requirement or escalate the persona proposal through the change process defined in `00_EXECUTIVE/01_Cover_and_Document_Control.md` §5.

### 3.2 In feature design (`01_PRODUCT/Feature_Specifications/`, `02_DESIGN_SYSTEM/`, `03_UI_SCREENS/`)

- Every Feature Specification **MUST** have a "Primary persona" row in its header table, citing the persona ID from the canonical source.
- Every Design System token or component **MUST** have an "Used by personas" row if its use is persona-conditional (e.g. only relevant to "AI-Augmented Developer" or only to "AI-Delegated Operator"). Otherwise, "All personas" is sufficient.
- Every UI Screen **MUST** declare its primary persona in the screen header.

### 3.3 In acceptance testing (`06_ENGINEERING_TEAM/05_Acceptance_Test_Suite.md`)

- Every acceptance test (`NX-AT-####`) **SHOULD** list the persona(s) it exercises. A test that does not name a persona is permitted only when its scope is cross-persona infrastructure (e.g. auth, billing, telemetry).
- The test count per persona is the primary coverage metric for the Phase-2 review. A persona with zero tests at the end of a phase is a gap that blocks the phase sign-off.

### 3.4 In user journeys (`01_PRODUCT/03_User_Journeys.md`)

- Every journey **MUST** start from a named persona in `NX-DOC-0007` §3.
- The persona at the start of a journey is the **anchor persona**; deviations from the anchor (e.g. "this journey also touches P5 mid-flow") must be explicit.

## 4. Cross-references (verified live)

The following documents in the blueprint reference `NX-PRD-0007`. Each must be resolvable via this document or, by extension, via the canonical source at `00_EXECUTIVE/07_Target_Audiences_and_Personas.md`.

| Referencing document | Reference type | Verification |
|----------------------|----------------|--------------|
| `06_ENGINEERING_TEAM/Marketing_AI/07_Marketing_AI_Manifest.md` | Reading list + dependency | Resolves via this file |
| `06_ENGINEERING_TEAM/Research_AI/10_Research_AI_Manifest.md` | Reading list + persona research | Resolves via this file |
| `06_ENGINEERING_TEAM/Product_AI/09_Product_AI_Manifest.md` | Reading list + persona definition | Resolves via this file |
| `01_PRODUCT/02_Persona_Feature_Matrix.md` | Source of all personas | Resolves via canonical source |
| `01_PRODUCT/01_Feature_Inventory.md` | Persona column | Resolves via canonical source |
| `01_PRODUCT/03_User_Journeys.md` | Journey anchors | Resolves via canonical source |
| `01_PRODUCT/04_Onboarding.md` | First-run personas | Resolves via canonical source |
| `01_PRODUCT/00_Master_PRD.md` | Methodology reference | Resolves via canonical source |

## 5. Maintenance rules

1. **Do not move the personas content.** The canonical source is `NX-DOC-0007`. Any change to the personas themselves goes through that document, not this one.
2. **Do not edit this file to add personas.** If a new persona is needed, propose it through the change process in `00_EXECUTIVE/01_Cover_and_Document_Control.md` §5 and reference the new persona by the ID it is given in the canonical source.
3. **This file's only mutable content is the usage contract (§3) and the cross-reference table (§4).** Both are owned by Product AI (`NX-EM-9609`).
4. **If `NX-DOC-0007` is ever deprecated or renumbered**, update the "Canonical source" field in the header table, update §2, and notify all three engineering manifests in the same change. This is the only edit that touches the identity mapping.

## 6. Change log

### v0.1.0 — 2026-07-03

| Action | Summary |
|--------|---------|
| Created | Identity-mapping document to give `NX-PRD-0007` an on-disk home. Records the `NX-PRD-0007` → `NX-DOC-0007` alias, codifies the Phase-2 usage contract, and lists every cross-reference so the registry can verify resolution. Resolves the 🟠 orphan row in `01_PRODUCT/07_Requirements_Traceability_Matrix.md` §7. |
