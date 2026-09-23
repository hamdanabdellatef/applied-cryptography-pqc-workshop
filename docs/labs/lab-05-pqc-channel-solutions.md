# Lab 5: worked solution

[Manual](lab-05-pqc-channel.md) · [Notebook](../downloads/lab-05-pqc-channel.ipynb)

Attempt the learner task first. This public walkthrough is instructional; copying it is not evidence of independent completion.

## Reference function

The notebook supplies the helper and imports before this function. Run the reference with the manual's acceptance checker.

```python
def reference_key(secret, transcript, direction):
    return derive_day2(secret, transcript, direction)
```

## Why it works

The public key and KEM ciphertext are public exchange material. The shared secret stays local and enters HKDF. Transcript context and direction separate key uses but do not authenticate a public key. Identity and replay policy remain outside the lab.

## Expected evidence

Require the expected KDF schedule, matching peer keys, directional separation, transcript sensitivity and AEAD rejection. Explain same-length KEM implicit rejection versus wrong-length failure. Ensure learners distinguish the KEM ciphertext from the AEAD record.

Raw ML-KEM-768 contribution sizes total 2272 bytes; the two raw X25519 contributions total 64 bytes. These exclude credentials and framing. A modified correctly sized KEM ciphertext returns a different secret, so record authentication fails. A recorded valid packet can replay because no sequence state is implemented.

## What remains outside the result

The lab uses generated test keys and a narrow teaching policy. Cryptographic success is not authorization, endpoint integrity, secure key custody or full protocol assurance. Explain the missing protections listed in the manual before marking the task complete.

