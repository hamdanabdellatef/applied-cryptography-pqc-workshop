# Facilitate the architecture capstone

**135 minutes plus 45-minute review.** [Brief](../capstone/index.md) · [Worksheet](../capstone/worksheet.md) · [Incidents](../capstone/incidents.md) · [Rubric](../capstone/rubric.md) · [Worked reasoning](../capstone/worked-architecture.md)

## Prepare

Assign groups of two to four, or let an independent learner take each role in sequence: data owner, service architect, key/recovery operator and adversarial reviewer. Provide the fixed fictional constraints. Ask learners to keep unknowns visible rather than assume an ideal KMS or flawless administrator.

The solutions and incident reasoning are public teaching resources. For an unaided exercise, display only the brief and evidence at first; do not use public content as a private exam. No live systems or production secrets are needed.

## Facilitation sequence

| Time | Instructor action | Evidence to request |
| --- | --- | --- |
| 0–15 | Elicit objectives and assumptions | Secrecy lifetime, recovery objectives, actor capabilities and trust owners |
| 15–45 | Challenge diagrams at every termination | Plaintext at gateway, worker, search, logs and recovery |
| 45–70 | Ask how yesterday's backup restores | DEK/KEK lifecycle, identity and signing roles, actual restore evidence needed |
| 70–82 | Reveal incident A | Conditional confidentiality claim plus exposed metadata |
| 82–95 | Reveal B or D | Authorized-use exposure and administrative escape paths |
| 95–108 | Reveal C | Old wrapped-key dependency and limits of rewrap |
| 108–120 | Reveal E, optionally F | Legacy-reader dependency and security floor during migration |
| 120–135 | Require revised deliverables | Diagram, inventory, migration gates, owners and residual-risk statement |

Do not let product names substitute for decisions. Ask “Which identity can request this operation?”, “Where is the plaintext?”, “Who can change that permission?”, and “Which old copy still needs this key?”

## Review period

Use 30 minutes for presentations or a solo comparison against the worked architecture. For many groups, use parallel peer reviews with the same rubric. Reserve 15 minutes for scoring, corrections and concrete next actions. Each reviewer must cite evidence in the submission for the selected rubric level.

Do not double-count earlier implementation marks. Apply the capstone's 100-point scale, then its 30% workshop weight only if the complete overall assessment is being used. Labs 2–3 are still unfinished and should not receive invented completion marks.

## Critical teaching corrections

Pause a proposal that disables verification, treats arbitrary public keys as trusted, uses silent downgrade, claims storage encryption defeats authorized host compromise, or deletes the sole recovery key without a retention decision. Explain the failed requirement, let the group revise, and record the correction separately from scoring.

Encourage alternatives when their tradeoffs are explicit. Client-side encryption may suit the restricted tier but cannot preserve every server-search and recovery feature unchanged. Hardware key custody is useful but does not authorize the correct operation by itself. PQ migration changes vulnerable dependencies; it does not repair all operational weaknesses.

## Completion and independent study

Ask each participant to state one protection achieved, one trust assumption, one unhandled incident and one measurable next test. Solo learners should preserve an initial answer, score it, compare with the worked reasoning, then write the revised claim. The goal is defensible reasoning, not copying a single diagram.
