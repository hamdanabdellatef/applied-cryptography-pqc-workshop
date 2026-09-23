# Lab verification

`test_aead.py` verifies Lab 1's reference API: round trips, field mutations, expected context, truncation, empty/Unicode/binary messages, nonce allocation calls, and the documented replay limitation. Run `python -m unittest discover -s tests -v` in the workshop environment.

Learner acceptance checks live in `labs/lab-01-aead/check_exercise.py`; they intentionally fail until the starter is implemented. `scripts/verify_aead_notebook.py` executes the complete notebook in a fresh kernel and requires both the reference checks and graph output.

These checks verify teaching behavior, not the cryptographic library's implementation or a production protocol. Future modules need their own success and failure checks.
