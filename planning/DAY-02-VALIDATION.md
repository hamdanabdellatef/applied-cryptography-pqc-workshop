# Day 2 validation

Completed locally on 22 September 2026, Python 3.11, cryptography 50.0.1, matplotlib 3.10.6, ipywidgets 8.1.7.

## Delivered

- Sessions 6–11: self-study Markdown, instructor pages, Mermaid diagrams, clean downloadable notebooks, generated local Python demonstrations.
- Labs 4–6: manuals, learner functions and acceptance checks, optional widget controls with direct-call fallbacks, public references/solutions, facilitation guides, standalone notebooks and local starters.
- Shared PKI/TLS helpers, Day 2 setup, curriculum inventory/navigation/status updates and reproducible build/verification scripts.

## Executed evidence

- All nine notebooks executed in separate fresh local kernels with no cell errors. Canonical student notebooks remain output-free. Both matplotlib graphs produced image output.
- Native ML-KEM-768 round trip, wrong-length rejection, same-length corruption, wrong-recipient secret mismatch and downstream AEAD rejection passed.
- ML-DSA-65 verified correct messages and rejected altered message/context/key and truncation. Measured public-key/signature lengths matched assertions.
- Real TLS 1.3 over MemoryBIO passed server-auth and mTLS handshakes and application-byte delivery. Wrong SAN, unknown root, expired leaf, missing intermediate, missing required client certificate and wrong client purpose all failed.
- Lab learners remain NOT ATTEMPTED until implemented. Supplied reference checks pass separately. Three mutation tests reject a TLS bypass, constant KDF and always-accept signature verifier. All eleven repository unit tests passed, including eight existing AEAD tests.
- Strict MkDocs build and course inventory/notebook syntax checks passed. Generated artifact synchronization checked.
- Browser verified all 24 new Mermaid diagrams/charts across six lessons, six instructor pages and three lab manuals without diagram errors. Reviewed lab hints, section navigation and layout.

## Limits

Live Google Colab installation/widget rendering has not been tested. Local notebook widgets and direct calls execute, but this does not substitute for delivery rehearsal. No external uploads or services were used.

TLS examples do not check online revocation or application authorization. PQ primitives are real, but neither the TLS demo nor teaching hybrid combiner claims a standardized PQ TLS profile. SLH-DSA is conceptual only. Algorithm standardization is not runtime FIPS validation. Labs 2–3 and Day 3 remain unfinished.

Reproduce with `scripts/build_day2.py --check`, `scripts/verify_day2.py`, `scripts/validate_structure.py`, `python -m unittest discover -s tests -v`, and `python -m mkdocs build --strict` in the pinned development environment.
