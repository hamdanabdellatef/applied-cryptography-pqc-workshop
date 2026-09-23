# Post-quantum migration worksheet

Use this worksheet with [Session 16](../day-3/16-pqc-migration.md) and the [CedarArchive capstone](../capstone/index.md). For each row record **pass, fail, unknown or not applicable**, an owner, evidence and a next action. Unknown is a discovery task; it is not a passing result.

**System / reviewer / date:** …  
**Data classification and secrecy lifetime:** …  
**Adversary capabilities and exclusions:** …

| Area | Review question or action | Required evidence |
| --- | --- | --- |
| Discover | List each cryptographic use, protocol, algorithm, library, peer and accountable owner. | Inventory with unknowns and discovery method |
| Prioritize | Record secrecy lifetime, collection exposure, migration lead time and impact. | Ranked rationale, not an invented quantum deadline |
| Dependencies | Map verifier, trust-distribution, format, device and vendor dependencies. | Directed dependency graph without cycles |
| Select | Choose a reviewed interoperable profile and validated implementation as required. | Profile version and interoperability results |
| Pilot | Test sizes, latency, failure handling, peer authentication and policy. | Representative traffic and negative tests |
| Transition | Define old/new acceptance, rollout gates and safe rollback. | Approved staged transition plan |
| Retire | Include retained backups, offline clients, signing trust and disaster recovery. | Owner approval backed by recovery tests |

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

