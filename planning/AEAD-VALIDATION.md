# AEAD module validation

Validated locally on 19 September 2026 with Python 3.11.5 on Windows.

## Completed

- Eight reference API tests, including rejected mutations and wrong context, empty/binary/Unicode messages, nonce allocation, and accepted replay as a documented limit.
- Four learner acceptance test methods run against the reference implementation. The untouched learner starter remains intentionally incomplete.
- Self-study lesson Python examples executed in sequence.
- Entire self-contained notebook executed in a fresh local Jupyter kernel, including the tampering matrix, reference exercise checks, context checks, replay, collision plot output, nonce-reuse recovery, and ChaCha20-Poly1305 extension.
- Untouched notebook exercise explicitly reports NOT ATTEMPTED; the reference solution has a separate result.
- Published notebook files have no execution counts or outputs; notebook source and website download match.
- Strict MkDocs build passed; dependency compatibility check passed.
- All 16 Mermaid diagrams/graphs rendered in the browser: seven self-study, five instructor-lesson, one instructor-lab, two student-lab, and one solution diagram. The collision graph was visually checked and its line contrast improved.
- Self-study answer disclosure was opened and verified in the browser.

## Communication-context addition — 21 September 2026

Added Alice/Bob sender–receiver explanations, two self-study Mermaid diagrams, and one instructor diagram. Key establishment and key management are explicitly deferred to later modules. The strict website build passed, and browser verification found nine rendered self-study diagrams and six instructor-lesson diagrams with no diagram errors. The module now contains 19 Mermaid diagrams in total.

## Delivery checks still required

- Fresh live Google Colab installation and widget interaction; local kernel execution does not establish this.
- Rehearse learner timing and instructor pacing with the intended audience.
- Recheck dependency versions and references before the course release.

The website is local and has not been published. Mermaid currently loads a pinned renderer from a CDN. Public instructor pages and solutions are intentionally part of the site.
