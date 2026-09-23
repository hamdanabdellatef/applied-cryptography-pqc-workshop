# Crypto-agility review

Use this worksheet with [Session 15](../day-3/15-crypto-agility.md) and the [CedarArchive capstone](../capstone/index.md). For each row record **pass, fail, unknown or not applicable**, an owner, evidence and a next action. Unknown is a discovery task; it is not a passing result.

**System / reviewer / date:** …  
**Data classification and secrecy lifetime:** …  
**Adversary capabilities and exclusions:** …

| Area | Review question or action | Required evidence |
| --- | --- | --- |
| Inventory | Locate algorithms in formats, protocols, libraries, trust stores and recovery tools. | Dependency map with owners |
| Profiles | Register approved complete profiles and their security floor. | Versioned reviewed registry |
| Acceptance | Separate permitted new writes from historical reads; reject unknown identifiers. | Negative routing and downgrade tests |
| Context | Authenticate negotiated choices and meaningful metadata in the real protocol. | Protocol review and tamper cases |
| Rollout | Upgrade readers and trust before writers; monitor compatibility. | Canary results and measured fallback behavior |
| Rollback | Define a safe operational rollback that preserves minimum policy. | Rehearsed rollback with prohibited-profile tests |
| Retirement | Account for old clients, backup retention and clean-environment recovery. | Restore record and owner sign-off |

## Decision record

| Finding | Status | Owner | Evidence location | Next action and due date |
| --- | --- | --- | --- | --- |
| Example: retained backup depends on old KEK | Unknown | Recovery lead | Backup catalog; restore test pending | Identify oldest retained copy and rehearse recovery |
| Your finding | … | … | … | … |

A completed checklist documents reasoning, not certification. Validate assumptions by testing an allowed path and a prohibited path. Record the actual configuration and version used so that results can be reproduced.

## Adversarial review

Assume the attacker first obtains a storage snapshot, then a tenant workload identity, and finally a policy-administrator account in separate scenarios. For each, identify newly exposed data, useful containment and historical exposure that cannot be undone. Do not combine these scenarios silently.

## Review outcome

Write a bounded claim: “Under assumptions ___, control ___ protects ___ against ___, supported by ___.” Then list unresolved risks, the person who accepts each risk, and the trigger for reviewing it again. Use the [capstone rubric](../capstone/rubric.md) to assess the quality of the explanation.

