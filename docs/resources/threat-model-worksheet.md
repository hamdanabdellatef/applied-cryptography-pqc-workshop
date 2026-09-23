# Session 1: Threat-model worksheet

[Self-study lesson](../day-1/01-security-requirements.md) · [Instructor guide](../teach/01-security-requirements.md)

Copy this worksheet into your notes or a Markdown file. Model the invoice submission/retrieval flow, then change one assumption. No code or account setup is required.

## 1. Scope and assumptions

- **Flow being modeled:**
- **Business harm we want to prevent:**
- **Outside this exercise's scope:**
- **Assumptions that our claim depends on:**
- **Model owner and review date:**

Keep exclusions explicit. “Out of scope” is not the same as “safe.”

## 2. Assets and actors

| Asset | Why it matters | Where it exists, including copies |
| --- | --- | --- |
| Asset 1 | | |
| Asset 2 | | |
| Asset 3 | | |

| Actor | What they can do | What they cannot do under this scenario |
| --- | --- | --- |
| Actor 1 | | |
| Actor 2 | | |

## 3. Trust boundaries and data flows

Draw the client, application, storage, and relevant key service. Label the data on the arrows and the permission or trust change at each boundary. Include logs and backups where they affect your claim.

| Boundary crossing | Data or operation | Identity/validation needed |
| --- | --- | --- |
| Client → API | | |
| Application → storage | | |
| Application → key service | | |

## 4. Threat records

Use the following two-column record for each threat. Complete two in the taught exercise and three during independent study.

| Field | Your answer |
| --- | --- |
| Threat ID and actor capability | |
| Action and resulting harm | |
| Testable security requirement | |
| Proposed control | |
| Verification action and expected outcome | |
| Priority and reason | |
| Owner | |
| Assumption or residual risk | |

## 5. Change the assumption

**Incident:** the application server is fully compromised; the key service is not.

- Which assets or operations can the attacker now reach?
- Can the attacker ask for decryption without extracting a raw key?
- Which earlier claim must be narrowed or withdrawn?
- Which control still helps, and what limit remains?
- Who should own the next design decision?

## 6. Highly confidential data and a state actor

Assume the documents must remain confidential for 20 years and a well-funded adversary persistently targets the organization. Record capabilities explicitly; do not assume unlimited access or automatic cryptographic breaks.

| Question | Your answer |
| --- | --- |
| What makes disclosure harmful, and for how long? | |
| Which specific adversary capability changes the original model? | |
| What route could expose plaintext today? | |
| What material could be collected now for future analysis? | |
| What remains protected if one workload or endpoint is compromised? | |
| Which control, owner, and verification action address each route? | |
| What residual risk must be acknowledged? | |

## 7. Completion check

Your model is ready for discussion when each threat identifies an actor's capability, a harm, a response, and a way to check that response. Another learner should be able to explain what is and is not covered without asking you to supply missing assumptions.

The [lesson exercise](../day-1/01-security-requirements.md#7-your-exercise-change-one-assumption) contains a worked example and incident answer. Compare reasoning rather than copying its wording.
