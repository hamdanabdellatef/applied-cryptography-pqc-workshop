# Facilitate Lab 5: ML-KEM Secure Channel

**60 minutes.** [Learner manual](../labs/lab-05-pqc-channel.md) · [Solutions](../labs/lab-05-pqc-channel-solutions.md)

## Prepare

Run the downloaded notebook in a fresh runtime. Setup and helper code are embedded. Untouched learner functions deliberately report NOT ATTEMPTED; supplied reference tests are labelled separately. No production credentials, certificates or artifacts belong in this exercise. Widget controls have direct-call fallbacks.

## Facilitation sequence

15 minutes: compare classical and KEM establishment; 20 minutes: implement KDF; 15 minutes: tamper; 10 minutes: debrief.

Have learners predict each outcome, execute it, then explain the protection responsible. Ask pairs to compare failure classifications rather than only PASS counts.

## Acceptance and diagnostic guidance

Require the expected KDF schedule, matching peer keys, directional separation, transcript sensitivity and AEAD rejection. Explain same-length KEM implicit rejection versus wrong-length failure. Ensure learners distinguish the KEM ciphertext from the AEAD record.

The public key and KEM ciphertext are public exchange material. The shared secret stays local and enters HKDF. Transcript context and direction separate key uses but do not authenticate a public key. Identity and replay policy remain outside the lab.

Do not fill in the learner function before they try. First point to the relevant API, then give the parameter hint in the manual, then review the public reference. If a backend is unsupported, resolve the pinned environment; never replace the PQ primitive with mock output.

## Debrief and submission

Collect code, observed failures and the manual's written boundary statement. Raw ML-KEM-768 contribution sizes total 2272 bytes; the two raw X25519 contributions total 64 bytes. These exclude credentials and framing. A modified correctly sized KEM ciphertext returns a different secret, so record authentication fails. A recorded valid packet can replay because no sequence state is implemented.

A local successful kernel run does not establish live Colab delivery, production security or learner completion. Rehearse the actual teaching runtime and ask learners to identify an omitted control. Keep Lab 4 revocation and application authorization, Lab 5 identity/replay/forward-secrecy assumptions, and Lab 6 release policy explicit.

