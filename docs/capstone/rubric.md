# Capstone assessment rubric

[Brief](index.md) · [Worksheet](worksheet.md) · [Worked architecture](worked-architecture.md)

Score only the submitted capstone evidence, not earlier lab success. The capstone subtotal is 100 points. If using the source workshop's overall weighting, multiply this subtotal by 0.30; the other components are knowledge/decision questions 20%, vulnerable-code analysis 30%, and hands-on implementation 20%. Unfinished Labs 2–3 are not silently assigned marks.

| Criterion | Weight | Observable evidence for full credit |
| --- | --- | --- |
| Requirements and adversary | 15 | Lifetimes, state-actor capabilities, assumptions and confidentiality/integrity/availability objectives are explicit |
| Trust and plaintext boundaries | 20 | Diagram covers termination, search, storage, queues, logs and recovery; every decrypt authority is named |
| Key lifecycle and recovery | 20 | DEK/KEK and signing/identity roles separated; rotation limits, old data, backups, restore test and destruction dependencies addressed |
| Mechanisms and validation | 15 | Correct AEAD/context, identity validation and authorized use; no claim that encryption alone stops replay or endpoint compromise |
| PQ migration and agility | 15 | Vulnerable roles inventoried, dependencies ordered, profiles distinguished from primitives, acceptance and downgrade/rollback policy defined |
| Incident reasoning and feasibility | 15 | Evidence-based exposed/surviving/unknown distinctions, operational owners, measurable tests and honest residual risk |

## Scoring levels

Apply one level per criterion and multiply its weight by the factor. Half-levels are unnecessary; document evidence behind disagreements.

| Level | Factor | Meaning |
| --- | --- | --- |
| Missing or contradictory | 0 | No relevant evidence, or the design contradicts the claimed protection |
| Named only | 0.25 | Labels products/algorithms but does not explain boundaries, dependencies or tests |
| Partially reasoned | 0.50 | Some correct decisions; material assumptions, failures or operational details unresolved |
| Coherent | 0.75 | Main paths and controls are justified with tests; remaining gaps explicitly owned |
| Defensible and evidenced | 1.00 | Requirements trace to mechanisms and verified/planned evidence, including failure and recovery paths |

Example: a coherent key-lifecycle design earns `20 × 0.75 = 15` points. It does not earn full credit merely by mentioning a KMS.

## Critical corrections before design acceptance

Regardless of subtotal, mark **revision required** if the design disables certificate verification, treats unauthenticated keys as trusted, silently downgrades required protection, claims endpoint compromise is solved by storage encryption, or destroys the only required recovery key without an approved retention decision. Explain the specific unsupported claim and ask for correction; this is a design-review gate, not an additional hidden point deduction.

For solo study, score once before reading the worked architecture and once after revising. Record what evidence changed your judgment. The worked architecture is one defensible direction, not a universal answer or production security approval.
