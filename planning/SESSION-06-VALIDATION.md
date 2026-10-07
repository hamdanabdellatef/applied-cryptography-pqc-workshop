# Session 6 interactive notebook update

Verified locally on 7 October 2026.

## Changes

Certificate/key inspector for all four roles, PEM printing with explicit disposable private-key disclosure, decoded field/extension tables, and explanations of PEM, DER, TBSCertificate, SAN, KU/EKU and key identifiers.

Interactive server/client validation with next-step, reveal-all and reset controls. Cases include trust, chain delivery, altered signed bytes, time, purpose, identity, missing client, revocation evidence and separate authorization. Failure stops subsequent decisions, which are marked SKIP.

Real signed direct CRLs illustrate leaf serial revocation, signature checks, freshness and unavailable evidence. CRL PEM, issuer, timestamps, serials and reasons can be printed. Widget-free function calls expose the same operations. The instructor page includes facilitation prompts.

## Verification

- All 16 unit tests passed, including every modeled failure stage for server/client, wrong-key CRL signatures, stale/future CRLs, serial-specific revocation, explicit private printing and widget next/reset/dropdown callbacks.
- Session 6 executed end to end in a fresh local notebook kernel (`python -X utf8 scripts/verify_aead_notebook.py session-06-pki-certificates`). Use UTF-8 on Windows consoles for the explanatory arrows.
- Source/download notebooks remain clean and synchronized; generated local demo includes the same helper.
- Course structure validation and strict MkDocs build passed.

## Limits

The interactive sequence is a fixed-chain explanatory model, not a production validator or an internal OpenSSL trace. It does not implement arbitrary path construction, general name/policy constraints, unknown extension handling, wildcard/IP rules, intermediate revocation, indirect/delta CRLs or online OCSP/CRL fetching. The separate real TLS/mTLS examples keep verification enabled but do not perform revocation checks. All printed private keys are generated disposable teaching material. No executed private-key output is committed. Live Colab frontend interaction still requires a delivery rehearsal; local Python widget callbacks were tested.
