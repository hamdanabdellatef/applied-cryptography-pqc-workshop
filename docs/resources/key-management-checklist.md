# Key-management review

Use this worksheet with [Session 12](../day-3/12-key-management.md) and the [CedarArchive capstone](../capstone/index.md). For each row record **pass, fail, unknown or not applicable**, an owner, evidence and a next action. Unknown is a discovery task; it is not a passing result.

**System / reviewer / date:** …  
**Data classification and secrecy lifetime:** …  
**Adversary capabilities and exclusions:** …

| Area | Review question or action | Required evidence |
| --- | --- | --- |
| Inventory | Identify key ID, purpose, algorithm, owner, tenant scope and every raw or wrapped copy. | Key registry and data-to-key map |
| Generation and provisioning | Use approved randomness and authenticated provisioning; distinguish export from operation rights. | Configuration and negative access test |
| Use | Restrict operation, workload and tenant; bind expected object context. | Wrong-tenant and wrong-operation rejection |
| Rotation | Define new-write switch, old-read path and whether DEKs change or only wrappers change. | Migration counts and historical-copy analysis |
| Recovery | Record RTO/RPO, independent recovery authority and retained backup dependencies. | Timed clean-environment restore |
| Compromise | Contain credentials and key-use permissions; assess collected ciphertext and old wrapped keys. | Scoped incident rehearsal |
| Destruction | Resolve retention and all key-copy dependencies before removal. | Owner approval and deletion evidence with stated limits |

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

