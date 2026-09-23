# Session 3 validation

Validated locally on 21 September 2026 using Python 3.11, cryptography 50.0.1, and argon2-cffi 25.1.0.

- Generated the notebook and Python demo from the self-study Markdown. Website download and repository notebook are identical and contain no saved outputs.
- Executed all eight lesson code blocks as a standalone demo and in a fresh notebook kernel. Assertions cover exact hash inputs, HMAC rejection for modified input/key/tag, synthetic offline guessing, salted password verification and mismatch rejection, HKDF context separation, and AEAD rejection with the wrong directional key.
- Strict MkDocs build passed. Course inventory and notebook syntax/clean-output checks passed.
- Browser checked seven self-study Mermaid diagrams and three instructor diagrams: all rendered, with no diagram errors. Visually checked bordered tables and wrapped text on the lesson page.
- Notebook supports upload to Colab with pinned dependency setup. A live Google Colab runtime has not been tested. Mermaid rendering is provided on the website; notebook viewers retain the diagram source.

Reproduce using the Session 3 commands in the repository README. Executed notebooks are written only to the ignored `.verification` directory.
