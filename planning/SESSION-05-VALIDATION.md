# Session 5 validation

Completed 22 September 2026 with Python 3.11 and cryptography 50.0.1.

- Seven experiments executed successfully in a fresh local notebook kernel. The standalone demo also ran successfully before the additional manifest edge-case assertions, which were then verified in the notebook.
- Checks cover original signatures, altered message/signature/key, truncation, equivalent JSON with different bytes, untrusted supplied keys, artifact digest mismatch, wrong product, rollback policy, impostor signatures, bad schema, Boolean version, wrong purpose, duplicate fields, and ECDSA/RSA-PSS altered-message rejection.
- Strict MkDocs build and curriculum/clean-notebook validation passed. Session 3 generation remains unchanged; Session 4 was regenerated solely for its updated next-session link/status text.
- Browser checked six lesson and three instructor Mermaid diagrams: all rendered without diagram errors. Inspected firmware flowchart layout, section navigation, table borders/wrapping, and expandable worked answers.
- Notebook and website download are generated from Markdown and have no saved outputs. Executed artifacts stay in the ignored `.verification` directory.

Live Colab execution has not been tested. The notebook installs its pinned dependency without requiring a repository checkout. No firmware is installed, and the acceptance function is a teaching policy rather than a production updater. Labs 2–3 remain scaffolds.

Reproduction commands are in README.
