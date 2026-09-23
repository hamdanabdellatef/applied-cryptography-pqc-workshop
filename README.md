# Applied Cryptography & Post-Quantum Security Workshop

[Course website](https://hamdanabdellatef.github.io/applied-cryptography-pqc-workshop/) · [GitHub repository](https://github.com/hamdanabdellatef/applied-cryptography-pqc-workshop)

**Status: Sessions 1–16, the capstone, and Labs 1 and 4–6 implemented; Labs 2–3 remain scaffolds.** A Markdown-first website with separate self-study and instructor pages, Python exercises, and Colab notebooks.

Begin with [Session 1: security requirements and threat models](docs/day-1/01-security-requirements.md), its [instructor page](docs/teach/01-security-requirements.md), and [worksheet](docs/resources/threat-model-worksheet.md). The lesson includes protecting highly confidential data against a well-funded state actor.

Start with the [self-study AEAD lesson](docs/day-1/02-symmetric-aead.md), [instructor lesson page](docs/teach/02-aead.md), or [Lab 1 manual](docs/labs/lab-01-aead.md). The lab has a public [solution walkthrough](docs/labs/lab-01-aead-solutions.md) and [facilitation guide](docs/teach/lab-01-aead.md).

## Repository layout

```text
docs/                  Website source: Markdown lessons and lab manuals
  getting-started/     Overview, prerequisites, setup, schedule
  day-1/               Sessions 01–05: applied cryptography
  day-2/               Sessions 06–11: PKI, TLS, and PQC
  day-3/               Sessions 12–16: architecture and migration
  labs/                Six lab instruction pages
  capstone/            Brief, worksheet, incidents, rubric
  resources/           Checklists, cheat sheets, and references
  advanced/            Optional extension outline
  teach/               Instructor explanations and facilitation pages
  assets/              Mermaid rendering and course styles
  downloads/           Generated notebook downloads
notebooks/             Labs 1, 4–6 and Sessions 3–16; Labs 2–3 scaffolds
  source/              Markdown authoring source for completed notebooks
labs/                  Python starter workspaces for the same six labs
src/crypto_workshop/   Shared Python reference helpers
tests/                 Implementation and authentication-failure checks
instructor/            Facilitation notes and future solutions
slides/                Optional Markdown slide materials
planning/              Design comments, roadmap, source, and templates
scripts/               Structure validation
course.json            Lesson/lab inventory
mkdocs.yml             Website navigation and build configuration
requirements-site.txt  Website build dependency baseline
requirements-labs.txt  Pinned Lab 1 and Session 3 runtime dependencies
requirements-dev.txt   Build, notebook, and verification dependencies
```

## Preview the website locally

Run from this directory using Python 3.11 or a compatible Python version:

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements-site.txt
.\.venv\Scripts\python -m mkdocs serve
```

Open the local URL printed by MkDocs. Build static HTML with:

```powershell
.\.venv\Scripts\python -m mkdocs build --strict
```

On macOS/Linux use `.venv/bin/python` instead. Generated output goes to `site/`. GitHub Actions builds and publishes updates to GitHub Pages when changes are pushed to `main`. See [publishing instructions](planning/PUBLISHING.md).

## Colab notebooks

Lab 1 is self-contained, with package setup, experiments, interactive tampering controls, a collision graph, staged hints, learner checks, and a separate reference solution. Upload `notebooks/lab-01-aead.ipynb` to Colab. Day 2's nine notebooks are also self-contained and downloadable from their pages. The website includes Open in Colab links next to implemented notebook downloads. Labs 2–3 remain scaffolds.

Edit `notebooks/source/lab-01-aead.md` and the shared Python module, then run `python scripts/build_notebooks.py`. Do not hand-edit the generated notebook or its website copy. Learners should work in their own notebook copies. Mermaid diagrams on the website require access to the pinned CDN renderer; descriptions and source remain readable offline.

## Verify the AEAD module

```powershell
.\.venv\Scripts\python -m pip install -r requirements-dev.txt
.\.venv\Scripts\python scripts/build_notebooks.py --check
.\.venv\Scripts\python -m unittest discover -s tests -v
.\.venv\Scripts\python scripts/verify_aead_notebook.py
.\.venv\Scripts\python -m mkdocs build --strict
```

The local starter intentionally requires learner implementation. Its separate checks fail until it is completed. Reference tests and notebook execution do not count as learner completion. Live Colab delivery validation is still required before class.

## Review and next steps

Day 3 includes five self-study lessons, five instructor guides, five notebook companions and a complete architecture capstone with incidents, rubric, worked design and editable downloads. Edit `docs/day-3/` Markdown, then run `scripts/build_day3.py`, `scripts/build_day3.py --check` and `scripts/verify_day3.py` with the virtual-environment Python. Runtime dependencies are in `requirements-day3.txt`; see `planning/DAY-03-VALIDATION.md` for verification and limitations.

Day 2 includes Sessions 6–11 and Labs 4–6, with nine self-contained notebooks, nine instructor/facilitation pages, and public lab solutions. Author the lesson/lab Markdown and `src/crypto_workshop/day2.py`, then run:

```powershell
.\.venv\Scripts\python -m pip install -r requirements-dev.txt
.\.venv\Scripts\python scripts/build_day2.py
.\.venv\Scripts\python scripts/build_day2.py --check
.\.venv\Scripts\python scripts/verify_day2.py
.\.venv\Scripts\python scripts/validate_structure.py
.\.venv\Scripts\python -m mkdocs build --strict
```

For execution only, install `requirements-day2.txt`. See `docs/getting-started/day-2-setup.md` and `planning/DAY-02-VALIDATION.md`. The PKI lab uses real TLS over MemoryBIO; PQ examples use native ML-KEM/ML-DSA in the pinned cryptography wheel. They do not implement PQ TLS or a standardized hybrid profile. Live Colab execution is not yet verified.

Session 5 has a self-study lesson, 45-minute instructor guide, and notebook at `notebooks/session-05-digital-signatures.ipynb`. Edit `docs/day-1/05-digital-signatures.md`, then regenerate and verify:

```powershell
.\.venv\Scripts\python scripts/build_session05.py
.\.venv\Scripts\python scripts/build_session05.py --check
.\.venv\Scripts\python examples/session-05/demo.py
.\.venv\Scripts\python scripts/verify_aead_notebook.py session-05-digital-signatures
```

Install `requirements-session05.txt` for the demo or `requirements-dev.txt` for notebook verification. Examples cover exact-byte signatures, untrusted keys, signed release manifests, and acceptance policy. No firmware is installed. Live Colab execution remains a delivery check before class.

Session 4 has a complete self-study lesson, 60-minute instructor guide, and notebook companion. Its source is `docs/day-1/04-classical-public-key.md`. Regenerate and verify with:

```powershell
.\.venv\Scripts\python scripts/build_session04.py
.\.venv\Scripts\python scripts/build_session04.py --check
.\.venv\Scripts\python examples/session-04/demo.py
.\.venv\Scripts\python scripts/verify_aead_notebook.py session-04-classical-public-key
```

Install `requirements-session04.txt` for the demo, or `requirements-dev.txt` for verification. The notebook is `notebooks/session-04-classical-public-key.ipynb`. It simulates communication in memory, including an unauthenticated exchange attack and signature checks; it is not a production protocol. Lab 2 remains a scaffold.

Session 3 now includes a self-study lesson, a 60-minute instructor guide, and an executable notebook companion. Its authoritative source is `docs/day-1/03-hashes-passwords-kdfs.md`; Python blocks generate both the notebook and local demo. Rebuild after editing:

```powershell
.\.venv\Scripts\python scripts/build_session03.py
.\.venv\Scripts\python scripts/build_session03.py --check
.\.venv\Scripts\python examples/session-03/demo.py
.\.venv\Scripts\python scripts/verify_aead_notebook.py session-03-hashes-passwords-kdfs
```

Install `requirements-session03.txt` for the standalone demo, or `requirements-dev.txt` for notebook verification. Upload `notebooks/session-03-hashes-passwords-kdfs.ipynb` to Colab; this companion does not change the six-lab curriculum. Local execution is verified; live Colab delivery remains to be checked.

Read [design comments](planning/DESIGN-NOTES.md) and the [development roadmap](planning/ROADMAP.md). The unchanged [source design](planning/source/workshop-design.md) is retained for traceability.

Run `python scripts/validate_structure.py` to check the curriculum inventory and clean notebook files. Use the commands above for Lab 1 implementation verification.
