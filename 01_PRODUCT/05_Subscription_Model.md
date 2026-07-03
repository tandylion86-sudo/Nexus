# NX-PRD-0005 — Subscription Model

| Field | Value |
|-------|-------|
| **Document ID** | NX-PRD-0005 |
| **Title** | Subscription Model |
| **Phase** | 2 — Complete PRD |
| **Owner** | Business + Backend AI |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-06-30 |
| **Depends on** | NX-DOC-0012 (Business Strategy), NX-FEAT-2701-2711 |

---

## 1. Purpose

This document defines how NEXUS is priced, billed, upgraded, downgraded, refunded, and taxed. It is the source of truth for the Subscription & Billing feature area (NX-FEAT-A0018).

## 2. Pricing tiers

The H1 pricing matrix:

| Tier | Price | Cloud Browsers | Cloud hours/mo | Marketplace installs | Models | Support |
|------|-------|----------------|----------------|----------------------|--------|---------|
| **Free** | $0 | 1 | 50 | 5 (first-party only) | Local + Standard cloud (rate-limited) | Community |
| **Pro** | $20/mo or $192/yr | 5 | 300 | Unlimited first-party + paid | All cloud, $10 credit/mo premium | Email |
| **Team** | $15/seat/mo (5+ seats) | 5/seat (pool) | 300/seat | Unlimited | All cloud, $10/seat/mo credit | Email + Slack |
| **Business** | $40/seat/mo | 10/seat (pool) | 600/seat | Unlimited + verified | All cloud, $25/seat/mo credit | Priority + dedicated CSM |
| **Enterprise** | Custom | Custom | Custom | Unlimited + private marketplace | All + custom models | Custom SLA |

Annual billing: 20% discount vs. monthly. Customer commits to 12 months.

## 3. What each tier includes

### Free
- 1 Cloud Browser
- 50 hours/month of Cloud Browser usage
- 5 first-party agents from marketplace
- Local AI (after download)
- Standard cloud models with rate limits (50 requests/day)
- Community support
- Local-only mode available
- 5 GB cloud storage

### Pro
- Everything in Free, plus:
- 5 Cloud Browsers
- 300 hours/month
- Unlimited marketplace installs (first-party)
- All cloud models, $10 credit/month toward premium models
- Premium themes (curated)
- Email support (24h response)
- 100 GB cloud storage
- Priority queue for new model rollouts

### Team
- Everything in Pro, plus:
- Per-seat pricing (5+ seats required)
- Shared Workspaces (NX-FEAT-1110)
- Team templates
- Basic SSO (Google, Microsoft)
- Audit log access
- $10/seat/month premium model credit
- 200 GB/seat cloud storage
- Slack-based support

### Business
- Everything in Team, plus:
- SSO (SAML, OIDC) — NX-FEAT-2901 (P3 H1; P0 H2)
- Role-based access (lightweight RBAC)
- Audit log export
- $25/seat/month premium model credit
- 500 GB/seat cloud storage
- Priority support with dedicated CSM
- 99.9% uptime SLA

### Enterprise
- Everything in Business, plus:
- Volume pricing
- Custom Cloud Browser limits
- Private marketplace option
- Custom model deployment
- 99.95% uptime SLA
- Compliance: SOC2 Type II, HIPAA, FedRAMP roadmap
- Custom DPA / MSA
- Dedicated success manager

## 4. Overage billing

When a user exceeds plan limits:

| Resource | Overage rate (Pro) | Overage rate (Team/Business) |
|----------|--------------------|------------------------------|
| Cloud Browser hours | $0.10/hour | $0.08/hour |
| Cloud Browser count (above plan) | $5/browser/month | $4/browser/month |
| Premium model credits | Provider cost + 20% | Provider cost + 15% |
| Cloud storage | $0.02/GB/month | $0.015/GB/month |

A user can set **hard caps** to prevent overage charges. When a cap is reached, the system pauses usage and notifies the user.

## 5. Payment methods

H1 launch supports:

- **Credit / debit cards** (Visa, Mastercard, Amex, Discover)
- **Apple Pay** (macOS, iOS)
- **Google Pay** (Web, Android)
- **Bank debit (ACH)** — US only, Team plans+
- **Wire transfer** — Enterprise only

Crypto, PayPal, Alipay, and others are evaluated for H2.

## 6. Billing cycle

| Item | Detail |
|------|--------|
| Cycle | Monthly or annual (annual = 20% discount) |
| Anchor date | Day of initial purchase |
| Proration | On plan change, prorated to the day |
| Currency | USD, EUR, GBP, JPY, AUD, CAD (H1); more in H2 |
| Invoices | Emailed on each charge; downloadable from account settings |
| Auto-renew | Default ON; user can disable anytime |

## 7. Plan changes

### Upgrade
- Effective immediately.
- Charged prorated amount for remaining period.
- New limits apply right away.

### Downgrade
- Effective at end of current billing period.
- User retains current features until then.
- If usage already exceeds new plan limits, user is asked to reduce usage or accept overage.

### Cancellation
- Effective at end of current period.
- Account remains active until then.
- After period end: account downgrades to Free tier.
- Cloud Browsers and data follow Free tier limits (or are archived).

## 8. Refunds

| Scenario | Policy |
|----------|--------|
| Cancel within 14 days of first charge | Full refund |
| Cancel within 14 days of renewal | Full refund |
| Cancel mid-period (annual) | Prorated refund; admin review for amounts >$1,000 |
| Service outage >4 hours in a month | Service credit issued (1 day per 4 hours; max 7 days/month) |
| Accidental upgrade | Reversed within 24h, no questions |
| Chargeback dispute | Account flagged; resolution process |
| Refund method | Original payment method |

Refunds are self-serve for amounts ≤$100 via Support. Larger amounts require human review.

## 9. Taxes

- **US:** Sales tax applied based on customer state (Stripe Tax).
- **EU:** VAT applied based on customer country; reverse-charge for B2B with valid VAT ID.
- **UK:** VAT included in displayed price.
- **Canada:** GST/HST applied per province.
- **Japan:** 10% consumption tax.
- **Other regions:** Local tax rules applied automatically.

For tax-exempt organizations (nonprofits, governments, education), a Tax Exemption Certificate upload flow is available.

## 10. Coupons and promotions

Coupon types:

- **Percentage off** (e.g., 20% off first year)
- **Fixed amount off** (e.g., $50 off first charge)
- **Free trial extension** (e.g., +30 days)
- **Referral credit** (referrer + referee get $10 each)

Coupon usage is tracked; abuse (multiple accounts per user) results in voiding.

## 11. Team plan mechanics

- **Minimum seats:** 5 (annual), 3 (monthly).
- **Adding seats:** Prorated; immediate.
- **Removing seats:** Effective at period end (cannot reduce below already-billed seats in current period).
- **Member activity:** Seats with no activity for 60 days can be reclaimed by admin.
- **Billing owner:** One person is the billing owner; receives all invoices.

## 12. Enterprise contracts

For Enterprise (10+ seats typically):
- Custom MSA / DPA available.
- Annual contracts with NET-30 payment terms.
- Procurement-friendly terms (e.g., auto-renewal opt-in, security questionnaires).
- Volume discounts negotiated.

## 13. Marketplace revenue share

When a user purchases a paid agent or template:

| Agent price | NEXUS take rate | Creator share |
|-------------|-----------------|---------------|
| ≤ $10 | 30% | 70% |
| $10–$100 | 25% | 75% |
| > $100 | 20% | 80% |
| Subscription (any price) | 25% / month | 75% / month |

Creator payouts monthly via Stripe Connect (or PayPal in H2).

## 14. Failed payments

If a payment fails:

1. User is notified immediately (email + in-product).
2. Retry schedule: 1 day, 3 days, 7 days.
3. After 7 days, account downgrades to Free.
4. After 30 days, account is suspended; data archived.
5. After 90 days, data is deleted (with notice).

## 15. Account deletion and data

On account deletion:
- Active subscription is canceled.
- Refund issued per policy above.
- Cloud Browsers are destroyed.
- Data is wiped within 30 days (logs immediately).
- Export is available 30 days before deletion.

## 16. Pricing changes

- Pricing changes require 30 days' notice to existing subscribers.
- Existing subscribers are grandfathered for 12 months at the old price.
- Annual subscribers keep their rate until renewal.

## 17. Out of scope for H1

- Usage-based pricing for individuals.
- Crypto payments.
- Reseller / affiliate programs.
- Custom enterprise feature gating beyond what's listed.
- Group/enterprise onboarding fees.

## 18. Acceptance criteria summary

The Subscription Model is "done" when:

- [ ] User can select tier, pay, and be active within 60 seconds.
- [ ] Free tier provides clear upgrade prompts at limit boundaries.
- [ ] Overages are metered and visible to the user before charging.
- [ ] Plan changes are prorated correctly.
- [ ] Refunds self-serve for amounts ≤$100.
- [ ] Invoices are downloadable from account settings.
- [ ] Team admins can manage seats and billing owner.
- [ ] Tax is computed correctly for all H1 regions.
- [ ] Failed-payment retry works per the schedule above.

## 19. Reading list

- **Business Strategy** — NX-DOC-0012
- **Goals & Metrics** — NX-DOC-0010
- **Feature Inventory** — NX-FEAT-0001 (NX-FEAT-2701-2711)

---

*End NX-PRD-0005.*