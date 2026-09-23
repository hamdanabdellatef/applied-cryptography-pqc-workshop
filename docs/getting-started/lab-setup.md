# Lab setup

Labs 1 and 4–6 are implemented. Labs 2–3 remain scaffolds. The local validation runtime is Python 3.11. Use a fresh Colab CPU runtime or local Python 3.11 environment. For PKI, TLS and PQC use the [Day 2 setup](day-2-setup.md).

## Colab route

Download the [Lab 1 notebook](../downloads/lab-01-aead.ipynb), open [Colab](https://colab.research.google.com/), and use **File → Upload notebook**. Save your own copy. GitHub-backed launch links will follow repository publication.

Lab 1 installs `cryptography==50.0.1`, `ipywidgets==8.1.7`, and `matplotlib==3.10.6` when necessary. Run its setup before the experiments. If you already imported a package that setup replaces, restart the runtime and rerun from the top. All data and keys are generated in memory; no external services or credentials are required.

The notebook's plain-function experiments work even if your viewer does not display widgets. It is executed locally for verification; live Colab installation and widget behavior still need a delivery check.

The mini-PKI lab uses real TLS through in-memory buffers, without exposing a public server. Full network inspection can be a local extension.

## Local route

From the repository root in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements-labs.txt
.\.venv\Scripts\python labs/lab-01-aead/demo.py
```

If `.venv` already exists, skip its creation. On macOS/Linux use `.venv/bin/python`.

For notebook authoring and verification, install `requirements-dev.txt`. Open `notebooks/lab-01-aead.ipynb` in your preferred Jupyter-compatible editor and select this virtual environment. The development requirements provide the Python kernel; they do not install the full JupyterLab application.

To preview the teaching website, install `requirements-site.txt`, then run `python -m mkdocs serve` using the environment's Python. Mermaid diagrams load a pinned renderer from a CDN; their source and nearby explanatory text remain available when offline.

## Reproducibility

Reset and run all cells before delivery. Do not use production credentials or data. Clear outputs before publishing notebooks. Colab sessions and installed packages are temporary.
