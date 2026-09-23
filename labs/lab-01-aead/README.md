# Lab 1: Authenticated Encryption

Implemented learning unit with a deliberately incomplete learner exercise.

- `starter.py`: implement `decrypt_verified` here.
- `check_exercise.py`: acceptance checks; intentionally fail on the untouched starter.
- `demo.py`: runnable reference scenario using the shared library.
- Student notebook: `notebooks/lab-01-aead.ipynb` at the repository root.
- Lab manual: `docs/labs/lab-01-aead.md` at the repository root.

AES-GCM, tampering, AAD, and nonce management.

Shared implementations live in `src/crypto_workshop/aead.py`. The notebook is built from `notebooks/source/lab-01-aead.md`; the build script embeds the shared solution so that the notebook runs without a repository checkout.

From the repository root, install `requirements-labs.txt` in `.venv`, then run `.venv/Scripts/python labs/lab-01-aead/demo.py`. Run `.venv/Scripts/python -m unittest discover -s tests -v` to check the reference implementation. On macOS/Linux replace `.venv/Scripts/python` with `.venv/bin/python`.
