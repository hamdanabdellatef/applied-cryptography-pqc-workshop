# Session 4 validation

Completed 22 September 2026. Python 3.11 and cryptography 50.0.1.

- Seven experiments passed as a standalone script and in a fresh local notebook kernel: RSA-OAEP round trip/randomization/size rejection, X25519 agreement, unusable-input rejection, directional HKDF/AEAD, simulated key substitution, trusted-signature rejection cases, and fresh exchanges versus retained RSA key transport.
- Strict MkDocs build and course inventory checks passed. Generated notebook/download/demo synchronization checked; Session 3 generation remains unchanged.
- Browser verified all seven lesson and three instructor Mermaid diagrams render without diagram errors. Inspected the attack sequence, table borders and wrapping, and expandable worked answers.
- Session 4 headings use letter-leading anchors to avoid the theme's numeric-selector navigation issue.
- Canonical notebooks have no execution counts or outputs. Executed verification artifacts remain in the ignored `.verification` directory.

Live Google Colab execution has not been tested. Notebook setup is self-contained, with a pinned dependency and no repository checkout requirement. Examples model communication in memory and do not implement a production protocol or prove forward secrecy. Lab 2 remains a scaffold.

See README for generation and verification commands.
