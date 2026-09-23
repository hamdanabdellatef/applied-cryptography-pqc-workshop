# Day 3 validation

Verified locally on 23 September 2026.

## Delivered

- Sessions 12–16: self-study lessons, separate timed instructor guides, five self-contained notebooks and five generated local Python demos.
- Key-management, architecture, agility and migration review worksheets.
- CedarArchive capstone: brief, editable worksheet and CSV inventory, six incident scenarios, rubric, worked architecture and facilitation guide.
- Runtime setup, navigation, course inventory and reproducible notebook generation.

## Checks completed

- `scripts/build_day3.py --check`: notebook, demo and download copies match Markdown sources.
- `scripts/build_day2.py --check`: previous-day companions remain synchronized after the Day 3 transition link update.
- `scripts/verify_day3.py`: all five notebooks executed in separate fresh local kernels. Encryption/context rejection, historical rewrap exposure, authorization scope, exposure modeling, profile rejection, retirement gates and cycle detection passed. Session 16 produced an inline PNG chart.
- `scripts/validate_structure.py`: registered pages and clean notebook sources validated.
- `python -m unittest discover -s tests -v`: all 11 existing regression tests passed.
- `python -m mkdocs build --strict`: successful without warnings.
- Browser: 21 Mermaid diagrams rendered without error across the overview, five lessons, five instructor guides, capstone brief, worksheet and worked architecture. Overview and worked architecture visually inspected. Table cells retain borders, normal wrapping and overflow wrapping.

## Scope and remaining delivery checks

Local execution is not a live Google Colab test. Rehearse notebook upload and package installation before teaching. Mermaid uses the existing CDN renderer and is shown as source in notebook Markdown.

Session 12 uses real AES-GCM and AES Key Wrap with disposable local keys. Sessions 13–16 use explicit policy, exposure and dependency models; they do not provision a real KMS/HSM, authenticate workloads, discover escalation paths or prove a production design. The migration chart uses invented durations. Capstone systems, incidents and constraints are fictional.

All sixteen lesson pages now contain learning material. Labs 2–3 remain scaffolds. The original design source and prior dated validation reports are preserved as historical records.
