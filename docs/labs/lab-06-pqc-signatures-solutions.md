# Lab 6: worked solution

[Manual](lab-06-pqc-signatures.md) · [Notebook](../downloads/lab-06-pqc-signatures.ipynb)

Attempt the learner task first. This public walkthrough is instructional; copying it is not evidence of independent completion.

## Reference function

The notebook supplies the helper and imports before this function. Run the reference with the manual's acceptance checker.

```python
def reference_verify(public, message, signature, context):
    try:
        public.verify(signature, message, context)
    except InvalidSignature:
        return False
    return True
```

## Why it works

Verification binds exact message bytes and context to a trusted public key. It does not establish that the key supplied in an untrusted bundle belongs to the release authority. An intact replay or wrong-product release still requires application checks.

## Expected evidence

Require explicit Boolean success only after verification, with rejection of changed bytes/context/key and truncation. A function returning True unconditionally must fail. Unexpected exceptions must not be counted as signature success.

ML-DSA-65 produces a 3309-byte signature and 1952-byte raw public key here. Ordinary signature validity does not grant installation permission. Provision new verification trust authentically before relying on PQ-signed updates, and explicitly define any dual-signature acceptance policy.

## What remains outside the result

The lab uses generated test keys and a narrow teaching policy. Cryptographic success is not authorization, endpoint integrity, secure key custody or full protocol assurance. Explain the missing protections listed in the manual before marking the task complete.

