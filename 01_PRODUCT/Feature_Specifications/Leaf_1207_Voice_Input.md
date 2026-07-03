# NX-FEAT-1207 — Command Bar Voice Input

| Field | Value |
|-------|-------|
| **Document ID** | NX-FEAT-1207 |
| **Title** | Command Bar Voice Input |
| **Area** | NX-FEAT-A0003 — AI Command Bar |
| **Owner** | Frontend AI |
| **Status** | 🟢 Complete |
| **Priority (H1)** | P3 |
| **Horizon target** | H2 (deferred from H1) |
| **Estimated effort** | L |

---

## 1. Purpose
Voice input as an alternative to typing intents.

## 2. User stories
- As Riya, I want to dictate intents hands-free.

## 3. Functional requirements
### FR-1: Microphone activation
- Click mic icon or hotkey.
- Recording indicator.
- Transcription streams into command bar.

### FR-2: Languages
- All H1 launch locales (per NX-DS-5009).

**Acceptance:**
- [ ] Transcription <500ms.
- [ ] 95% accuracy on common intents.

## 4. Non-functional requirements
- Privacy: opt-in per session.
- Local model preferred where feasible.

## 5. UI surfaces
- Command bar.

## 6. Permissions
- Microphone: OS permission required.

## 7. Telemetry
- `voice_command.used`

## 8. Failure modes
- Mic denied: "Microphone access required."
- Transcription fails: text fallback.

## 9. Dependencies
- Web Speech API or Whisper local.

## 10. Out of scope
- Continuous listening.
- Wake-word detection.

## 11. Acceptance criteria summary
- [ ] Opt-in.
- [ ] <500ms transcription.

## 12. Open questions
- Q: Local vs. cloud transcription trade-off?

## 13. Change log
| Date | Change | Author |
|------|--------|--------|
| 2026-06-30 | Initial spec — deferred to H2 | Frontend AI |

---

*End NX-FEAT-1207.*