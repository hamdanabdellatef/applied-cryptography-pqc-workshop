# Architecture review

Use this worksheet with [Session 14](../day-3/14-secure-architecture.md) and the [CedarArchive capstone](../capstone/index.md). For each row record **pass, fail, unknown or not applicable**, an owner, evidence and a next action. Unknown is a discovery task; it is not a passing result.

**System / reviewer / date:** …  
**Data classification and secrecy lifetime:** …  
**Adversary capabilities and exclusions:** …

| Area | Review question or action | Required evidence |
| --- | --- | --- |
| Requirements | Specify confidentiality lifetime, server processing, tenant isolation and recovery objectives. | Signed requirement and explicit conflicts |
| Data flow | Trace documents, metadata, indexes, queues, logs, caches and backups. | Diagram marking plaintext and derived sensitive data |
| Trust boundaries | Identify who can read, decrypt, sign, modify policy or deploy code. | Role-to-operation map |
| Adversary cases | Evaluate stolen storage, compromised worker, administrator and recovery authority separately. | Exposure table for each compromise |
| Protocol composition | Validate peer identity, context, freshness and authorized use; use reviewed protocols. | Wrong-peer, replay and malformed-input tests |
| Recovery and availability | Consider KMS outage, credential loss and failed restore without bypassing checks. | Failure-mode rehearsal |
| Claims | State residual risks and assumptions, including endpoint compromise. | Bounded claim paired with supporting evidence |

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

