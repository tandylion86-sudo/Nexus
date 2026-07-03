# NX-FEAT-1110 — Workspace Sharing

| Field | Value |
|-------|-------|
| **Document ID** | NX-FEAT-1110 |
| **Title** | Workspace Sharing |
| **Area** | NX-FEAT-A0002 — Workspaces |
| **Owner** | Backend AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P2 |
| **Horizon target** | H1 |
| **Estimated effort** | L |

---

## 1. Purpose
Team plan users can share Workspaces with team members with configurable permissions.

## 2. User stories
- As Thea, I want to share an investigation with my team.
- As Maya, I want team members to have edit access on a campaign Workspace.

## 3. Functional requirements
### FR-1: Invite by email
- Workspace owner invites by email.
- Invitation includes role and message.

### FR-2: Permission levels
- Viewer: read-only.
- Commenter: read + comment.
- Editor: full edit (except settings).
- Admin: full edit including settings and member management.

### FR-3: Activity attribution
- Each action attributed to a member.

### FR-4: Removal
- Owner / admin can remove members.
- Removed members lose access within 5 seconds.

## 4. Non-functional requirements
- Sync propagation <5s.
- Permissions enforced server-side.

## 5. UI surfaces
- Workspace settings → Members.
- NX-UI-6002 sub-screen for invitations.

## 6. Permissions
- Invite: owner / admin.
- Permission change: owner / admin.
- Remove: owner / admin.

## 7. Telemetry
- `workspace.member_invited`
- `workspace.member_joined`
- `workspace.member_removed`
- `workspace.permission_changed`

## 8. Failure modes
- Email not deliverable: notify inviter.
- Recipient already team member: skip.
- Plan downgrade: warn; downgrade permissions if seat removed.

## 9. Dependencies
- Team plans (NX-FEAT-2709).
- Auth (NX-FEAT-2001).

## 10. Out of scope
- Cross-team sharing (H2 enterprise).
- Public Workspaces (deferred).

## 11. Acceptance criteria summary
- [ ] 4 permission levels.
- [ ] Invite by email.
- [ ] Removal instant.
- [ ] Activity attribution.

## 12. Open questions
- Q: Should invites auto-expire? (Suggested: 14 days.)

## 13. Change log
| Date | Change | Author |
|------|--------|--------|
| 2026-06-30 | Initial spec | Backend AI |

---

*End NX-FEAT-1110.*