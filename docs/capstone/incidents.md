# Capstone incident injects

[Brief](index.md) · [Worksheet](worksheet.md) · [Instructor](../teach/capstone.md)

Reveal injects at the specified checkpoints. Evidence below is fictional and intentionally incomplete. Learners may request missing facts; record assumptions instead of inventing reassuring answers. Facilitators should evaluate reasoning using the prompts, not require one vendor solution.

## Inject A: storage copy stolen — minute 70

Evidence: an attacker copied the database and object store. They have record identifiers, timestamps, object lengths, ciphertexts and wrapped DEKs. There is no evidence yet of key-service access. Some search-index fields are plaintext by design.

Ask: which contents remain protected, which metadata/index data is exposed, and what must be checked before claiming no document disclosure? Does AEAD prevent the attacker deleting or replaying stored records?

Expected reasoning: confidentiality is conditional on key separation and no useful credentials/keys in the dump. Plaintext fields and metadata are already disclosed. AEAD does not guarantee completeness or freshness. Inspect exports, caches and key identifiers; do not announce “encrypted, therefore no impact.”

## Inject B: authorized worker compromised — minute 82

Evidence: a worker serving tenant Acme is controlled by the adversary for two hours. It can invoke every key operation permitted to its identity. Its token was not exported from hardware, but it remained usable by the process. The gateway and identity service are not known to be compromised.

Ask: does non-exportable key storage prevent disclosure? Which other tenants and historical records can this worker reach? How do you contain use without destroying evidence or breaking every tenant?

Expected reasoning: authorized decrypt/sign operations may be abused without extraction. Scope, tenant enforcement and permitted history determine blast radius. Isolate the host, revoke/restrict identities and key use, preserve evidence, evaluate plaintext exposure and recover onto clean systems. Rewrapping alone cannot repair stolen DEKs or plaintext.

## Inject C: old backups and later key loss — minute 95

Evidence: five years of backups were copied last year. A KEK used three years ago is now suspected exposed. Current production DEKs were rewrapped six months ago, but the backups retain old wrapped DEKs.

Ask: does current rotation protect the copied history? Can old keys be destroyed today while meeting the restore requirement? Which retained copies need migration and which attacker copies cannot be recalled?

Expected reasoning: old KEK plus old wrapped DEKs may recover unchanged DEKs. New wrapping does not erase adversary knowledge. Separate containment of future data, recovery of retained authorized data and assessment of past exposure. Do not destroy the only recovery path without an approved retention decision.

## Inject D: insider changes key policy — optional replacement for B

Evidence: a privileged administrator cannot decrypt directly but can edit the key-service policy and deploy application code without independent approval. An audit trail exists only on the administered host.

Ask: is separation of duties meaningful? What evidence source remains trustworthy? Which administrative paths need independent authorization?

Expected reasoning: indirect ability to grant access defeats a naive “admin cannot decrypt” claim. Independent policy controls, release approval and audit custody are needed; an HSM label does not resolve this authority path.

## Inject E: long-lived data and legacy reader — minute 108

Evidence: a new collection requires 20 years of secrecy. Network recordings are plausible. The offline reader takes 18 months to replace and cannot process the proposed new key/signature formats. A gateway upgrade is ready now.

Ask: which exposure does the gateway upgrade reduce, what remains, and how will new-format archives be restored? Is it truthful to label the archive fully migrated?

Expected reasoning: treat transport, stored key protection, reader and trust-update mechanisms separately. Preserve a safe recoverable rollout, prioritize the long-lived path, and name the residual risk owner. No quantum arrival date is needed to identify the dependency. Upgrading today cannot recall past recordings.

## Inject F: emergency retirement — minute 118 or review

Evidence: an implementation used by an approved profile must be retired due to a serious flaw. A rollback button reinstates the old binary and configuration. One backup reader needs that profile. No exploit is confirmed yet.

Ask: what does safe rollback mean now? Who can authorize temporary constrained recovery? Which tests prevent silent fallback into the retired configuration?

Expected reasoning: distinguish code rollback, profile policy and emergency historical access. Pause affected operations if necessary, stage a verified replacement, enforce a security floor and document any restricted exception. “No confirmed exploit” is not evidence the vulnerable path is safe indefinitely.

## Response standard

For every inject, provide an exposed/surviving/unknown table, containment owner, recovery step, verification test and residual-risk statement. During independent study, answer before reading each expected-reasoning paragraph. During teaching, the instructor may present only the evidence first.
