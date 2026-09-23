# Facilitate Lab 6: ML-DSA Signatures

**30 minutes.** [Learner manual](../labs/lab-06-pqc-signatures.md) · [Solutions](../labs/lab-06-pqc-signatures-solutions.md)

## Prepare

Run the downloaded notebook in a fresh runtime. Setup and helper code are embedded. Untouched learner functions deliberately report NOT ATTEMPTED; supplied reference tests are labelled separately. No production credentials, certificates or artifacts belong in this exercise. Widget controls have direct-call fallbacks.

## Facilitation sequence

5 minutes: sign and measure; 15 minutes: implement verifier; 10 minutes: context failures and debrief.

Have learners predict each outcome, execute it, then explain the protection responsible. Ask pairs to compare failure classifications rather than only PASS counts.

## Acceptance and diagnostic guidance

Require explicit Boolean success only after verification, with rejection of changed bytes/context/key and truncation. A function returning True unconditionally must fail. Unexpected exceptions must not be counted as signature success.

Verification binds exact message bytes and context to a trusted public key. It does not establish that the key supplied in an untrusted bundle belongs to the release authority. An intact replay or wrong-product release still requires application checks.

Do not fill in the learner function before they try. First point to the relevant API, then give the parameter hint in the manual, then review the public reference. If a backend is unsupported, resolve the pinned environment; never replace the PQ primitive with mock output.

## Debrief and submission

Collect code, observed failures and the manual's written boundary statement. ML-DSA-65 produces a 3309-byte signature and 1952-byte raw public key here. Ordinary signature validity does not grant installation permission. Provision new verification trust authentically before relying on PQ-signed updates, and explicitly define any dual-signature acceptance policy.

A local successful kernel run does not establish live Colab delivery, production security or learner completion. Rehearse the actual teaching runtime and ask learners to identify an omitted control. Keep Lab 4 revocation and application authorization, Lab 5 identity/replay/forward-secrecy assumptions, and Lab 6 release policy explicit.

