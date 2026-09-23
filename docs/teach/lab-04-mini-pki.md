# Facilitate Lab 4: Build and Use a Mini-PKI

**60 minutes.** [Learner manual](../labs/lab-04-mini-pki.md) · [Solutions](../labs/lab-04-mini-pki-solutions.md)

## Prepare

Run the downloaded notebook in a fresh runtime. Setup and helper code are embedded. Untouched learner functions deliberately report NOT ATTEMPTED; supplied reference tests are labelled separately. No production credentials, certificates or artifacts belong in this exercise. Widget controls have direct-call fallbacks.

## Facilitation sequence

15 minutes: inspect generated hierarchy; 15 minutes: predict TLS failures; 20 minutes: implement the wrapper; 10 minutes: explain boundaries.

Have learners predict each outcome, execute it, then explain the protection responsible. Ask pairs to compare failure classifications rather than only PASS counts.

## Acceptance and diagnostic guidance

Require a trusted-root success plus rejection of wrong SAN, unknown root, expiry, missing intermediate, absent required client certificate and wrong client purpose. The wrapper must preserve verification and propagate errors. Do not accept disabling certificate checks as a repair.

Root trust is local policy. The intermediate signs leaf certificates; the server sends its chain to help the client build a path. The client still needs a trust anchor. Client-certificate validity authenticates an identity under the selected policy, not its application permissions.

Do not fill in the learner function before they try. First point to the relevant API, then give the parameter hint in the manual, then review the public reference. If a backend is unsupported, resolve the pinned environment; never replace the PQ primitive with mock output.

## Debrief and submission

Collect code, observed failures and the manual's written boundary statement. Wrong SAN requires correct service identity or reissuance, not check_hostname=False. Missing intermediate is a chain-delivery problem in this clean client. Unknown root is a trust-policy problem. Expiration needs renewal or clock diagnosis. Missing or wrong-purpose client credentials must not downgrade required mTLS.

A local successful kernel run does not establish live Colab delivery, production security or learner completion. Rehearse the actual teaching runtime and ask learners to identify an omitted control. Keep Lab 4 revocation and application authorization, Lab 5 identity/replay/forward-secrecy assumptions, and Lab 6 release policy explicit.

