# TODO — Phase 8: Marketplace

## Goal
Document the marketplace, plugin/agent distribution, billing, and the security substrate that the marketplace depends on.

## Directories
- `09_MARKETPLACE/` — Agent_Store, Billing, Plugin_SDK, Ratings, Revenue_Sharing
- `08_SECURITY/` — AI_Safety, Encryption, Permissions, Privacy, Threat_Model, Zero_Trust (security aspect of marketplace; the rest of security lives in `08_SECURITY/` as cross-cutting infrastructure documented here too)

## ID scheme
Continue `NX-ARCH-` prefix. Phase 8 uses 0600s for marketplace and 0700s for security, keeping the leaf-doc structure.

- `NX-ARCH-0004` — Phase 8 overview (Marketplace)
- `NX-ARCH-0601..0605` — Marketplace leaves (5)
- `NX-ARCH-0701..0706` — Security leaves (6)
- Total: 12 docs

## Subdir → doc mapping

### Marketplace (5)

| Subdir | Doc ID | Title |
|--------|--------|-------|
| (root) | NX-ARCH-0004 | Marketplace Architecture Overview |
| 09_MARKETPLACE/Agent_Store/ | NX-ARCH-0601 | Agent Store & Discovery |
| 09_MARKETPLACE/Plugin_SDK/ | NX-ARCH-0602 | Plugin SDK & API Contracts |
| 09_MARKETPLACE/Billing/ | NX-ARCH-0603 | Billing, Metering & Subscriptions |
| 09_MARKETPLACE/Ratings/ | NX-ARCH-0604 | Ratings, Reviews & Trust |
| 09_MARKETPLACE/Revenue_Sharing/ | NX-ARCH-0605 | Revenue Sharing & Payouts |

### Security (6)

| Subdir | Doc ID | Title |
|--------|--------|-------|
| 08_SECURITY/Threat_Model/ | NX-ARCH-0701 | Threat Model & Attack Surface |
| 08_SECURITY/AI_Safety/ | NX-ARCH-0702 | AI Safety & Prompt-Injection Defense |
| 08_SECURITY/Permissions/ | NX-ARCH-0703 | Permissions & Capability Model |
| 08_SECURITY/Privacy/ | NX-ARCH-0704 | Privacy, PII & Data Residency |
| 08_SECURITY/Encryption/ | NX-ARCH-0705 | Encryption (at rest & in transit) |
| 08_SECURITY/Zero_Trust/ | NX-ARCH-0706 | Zero-Trust Architecture |

## Steps

- [x] Plan doc IDs and subdir mapping
- [ ] Read upstream context (Phase 1 strategy, Phase 2 marketplace anchor, Phase 5 escalation, Phase 6/7 architecture)
- [ ] Write `00_Overview.md` (NX-ARCH-0004) — frames marketplace + security
- [ ] Write `09_MARKETPLACE/Agent_Store/01_Agent_Store_and_Discovery.md` (NX-ARCH-0601)
- [ ] Write `09_MARKETPLACE/Plugin_SDK/02_Plugin_SDK_and_API_Contracts.md` (NX-ARCH-0602)
- [ ] Write `09_MARKETPLACE/Billing/03_Billing_Metering_and_Subscriptions.md` (NX-ARCH-0603)
- [ ] Write `09_MARKETPLACE/Ratings/04_Ratings_Reviews_and_Trust.md` (NX-ARCH-0604)
- [ ] Write `09_MARKETPLACE/Revenue_Sharing/05_Revenue_Sharing_and_Payouts.md` (NX-ARCH-0605)
- [ ] Write `08_SECURITY/Threat_Model/01_Threat_Model_and_Attack_Surface.md` (NX-ARCH-0701)
- [ ] Write `08_SECURITY/AI_Safety/02_AI_Safety_and_Prompt_Injection_Defense.md` (NX-ARCH-0702)
- [ ] Write `08_SECURITY/Permissions/03_Permissions_and_Capability_Model.md` (NX-ARCH-0703)
- [ ] Write `08_SECURITY/Privacy/04_Privacy_PII_and_Data_Residency.md` (NX-ARCH-0704)
- [ ] Write `08_SECURITY/Encryption/05_Encryption_at_Rest_and_In_Transit.md` (NX-ARCH-0705)
- [ ] Write `08_SECURITY/Zero_Trust/06_Zero_Trust_Architecture.md` (NX-ARCH-0706)
- [ ] Update PROGRESS.md (Phase 8 table, cumulative totals, decisions log)
- [ ] Update MASTER_INDEX.md (Phase 8 section)
- [ ] Update README.md (status, totals)
- [ ] Update DOCUMENT_REGISTRY.md (12 new rows)
- [ ] Update cover doc changelog + last updated

## Risks
- **Length creep**: 12 docs at 1,000+ words = ~12k words. Mitigation: 800–1,200 words per leaf.
- **Overlap with Phase 7 (auth, storage)**: Security docs reference but don't duplicate auth (NX-ARCH-0202) and storage (NX-ARCH-0207).
- **Billing overlaps Phase 9 (Pricing)**: Marketplace billing is metering/invoicing. Pricing is list price and tiers — Phase 9.
- **Plugin SDK overlaps NX-ARCH-0404 (Plugin Development)**: NX-ARCH-0404 is the developer guide (how to build a plugin); NX-ARCH-0602 is the API contract + distribution side.
