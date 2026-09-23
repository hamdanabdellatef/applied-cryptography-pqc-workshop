# Day 3 setup

Day 3 has five self-contained notebook companions. Each embeds its lesson text, Python examples and dependency installation cell. Download a notebook from its lesson, open [Google Colab](https://colab.research.google.com/), choose **Upload**, then run the cells in order. No repository checkout, cloud account credentials, KMS subscription or hardware security module is needed.

Use a Python 3 CPU runtime and synthetic data. If an older library was imported before setup, restart the runtime and run all cells again. Mermaid diagrams are provided as source in the notebooks and rendered on the course website.

## Local execution

From the workshop directory, install the pinned dependencies in your virtual environment:

```powershell
.venv\Scripts\python -m pip install -r requirements-day3.txt
.venv\Scripts\python examples/session-12/demo.py
```

Change the session number to run Sessions 13–16. Session 16 displays a planning chart; close the chart window to finish a local script. The notebooks show the chart inline.

## What each experiment demonstrates

| Session | Experiment | Boundary of the claim |
| --- | --- | --- |
| 12 | AES-GCM envelope encryption and AES key wrapping | Real primitives, local keys; no remote KMS or production envelope format |
| 13 | Operation and tenant authorization | Policy simulation; no real authentication or hardware isolation |
| 14 | Plaintext exposure after selected compromises | Explicit set model; no automatic attack-path discovery |
| 15 | Profile acceptance and retirement gates | Policy model; no wire protocol or authenticated negotiation |
| 16 | Dependency ordering and schedule chart | Invented durations; no forecast of quantum-computer arrival |

Predict outcomes, run the examples, then change one input at a time. A failed assertion after an intentional edit is useful feedback: explain why the original claim no longer holds. Restore the original cell before continuing dependent cells.

## Verification and delivery

Repository checks execute each notebook in a fresh local kernel and keep student copies free of outputs. Live Colab installation remains a separate delivery check. Before teaching, rehearse upload and execution in the actual classroom environment. The [Day 3 overview](../day-3/index.md) gives the study order.
