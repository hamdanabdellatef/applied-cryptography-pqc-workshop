# Course authoring pattern

The AEAD unit establishes the pattern for future modules. Each unit has distinct public pages for independent learning and instructor explanation, with shared exercises and reference code.

## Required artifacts per unit

| Artifact | Purpose | AEAD example |
| --- | --- | --- |
| Self-study lesson | Full explanation, worked examples, predictions, answers, limitations, sources | `docs/day-1/02-symmetric-aead.md` |
| Instructor lesson | Timed explanation sequence, diagrams, questions, expected answers, misconceptions | `docs/teach/02-aead.md` |
| Student lab manual | Setup, tasks, outcomes, hints, deliverables, troubleshooting | `docs/labs/lab-01-aead.md` |
| Instructor lab page | Facilitation, timing, diagnostic hints, formative assessment | `docs/teach/lab-01-aead.md` |
| Public walkthrough | Reference implementation and reasoning for independent learners | `docs/labs/lab-01-aead-solutions.md` |
| Notebook Markdown | Portable narrative and Python experiments | `notebooks/source/lab-01-aead.md` |
| Shared Python | Reviewed implementation for reuse and tests | `src/crypto_workshop/aead.py` |
| Local exercise | Deliberately incomplete task and acceptance checks | `labs/lab-01-aead/` |

## Visual explanations

Use Mermaid for relationships, trust boundaries, message sequences, decisions, and small explanatory graphs. Every important diagram needs nearby prose explaining how to read it. Avoid decorative diagrams that duplicate a simple list. Label quantitative axes, units, approximations, and toy parameters. Use evenly spaced sample values when a line chart uses categorical labels.

Fenced `mermaid` blocks render via `docs/assets/javascripts/mermaid-init.js`. The pinned renderer is loaded from a CDN; source and explanatory text remain available without it. Browser-check diagram syntax and visual readability after editing. Do not embed secrets in diagram source.

## Notebook workflow

Write notebook content in Markdown. `scripts/build_notebooks.py` turns top-level fenced Python blocks into code cells and embeds the shared reference module at the explicit reference marker. The result is self-contained, with no unpublished GitHub URLs or external data dependencies. It also generates the website's downloadable copy.

Keep learner work distinct from supplied solutions. The untouched exercise must say NOT ATTEMPTED, not pass. Incorrect implemented exercises must fail visibly. Provide staged hints and a reference implementation later in the notebook; keep reference function names separate from the learner function.

Interactive controls need a direct function-call fallback. Keep dependency installation at the start, pin course versions, and use ephemeral synthetic data. The published notebook must have no execution counts or outputs.

## Verification before marking locally complete

1. Run `scripts/build_notebooks.py --check`.
2. Run meaningful success/failure and context-boundary tests.
3. Execute the entire notebook in a fresh kernel and confirm graph output.
4. Run the strict site build and check links, downloads, diagrams, and answer disclosures in a browser.
5. Record what was actually tested, and distinguish local execution from a live Colab delivery check.

Update `course.json`, the website navigation, module status, and the roadmap. Before teaching, validate installation and widget behavior in the actual Colab/runtime environment and rehearse timing. Keep private assessment material outside public website and repository content.
