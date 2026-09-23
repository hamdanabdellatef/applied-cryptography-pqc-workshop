# Lab 4: worked solution

[Manual](lab-04-mini-pki.md) · [Notebook](../downloads/lab-04-mini-pki.ipynb)

Attempt the learner task first. This public walkthrough is instructional; copying it is not evidence of independent completion.

## Reference function

The notebook supplies the helper and imports before this function. Run the reference with the manual's acceptance checker.

```python
def reference_connect(hostname, require_client, client_present):
    return tls_trial(hostname=hostname, mtls=require_client, send_client=client_present)
```

## Why it works

Root trust is local policy. The intermediate signs leaf certificates; the server sends its chain to help the client build a path. The client still needs a trust anchor. Client-certificate validity authenticates an identity under the selected policy, not its application permissions.

## Expected evidence

Require a trusted-root success plus rejection of wrong SAN, unknown root, expiry, missing intermediate, absent required client certificate and wrong client purpose. The wrapper must preserve verification and propagate errors. Do not accept disabling certificate checks as a repair.

Wrong SAN requires correct service identity or reissuance, not check_hostname=False. Missing intermediate is a chain-delivery problem in this clean client. Unknown root is a trust-policy problem. Expiration needs renewal or clock diagnosis. Missing or wrong-purpose client credentials must not downgrade required mTLS.

## What remains outside the result

The lab uses generated test keys and a narrow teaching policy. Cryptographic success is not authorization, endpoint integrity, secure key custody or full protocol assurance. Explain the missing protections listed in the manual before marking the task complete.

