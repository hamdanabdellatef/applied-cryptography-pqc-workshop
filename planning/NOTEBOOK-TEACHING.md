# Interactive notebook authoring

Sessions 7–16 use a common predict → step → inspect → explain pattern. Their lesson Markdown contains the panel launch and widget-free alternative. Instructor pages supply scenario prompts. `src/crypto_workshop/teaching_panels.py` implements lazy experiment generators and the common widget shell; only the next requested operation executes. Each session distinguishes real cryptographic operations from architectural/policy models.

## Mermaid rendering

Notebook builders replace Mermaid fences with collapsed executable diagram cells. Each cell embeds a PNG and displays it through IPython when run. It needs no external diagram service or JavaScript permission. The original Mermaid is preserved in cell metadata (`workshop_mermaid`); website Markdown remains unchanged. Student code outputs stay empty in Git. Run all cells to display the diagrams in Colab/Jupyter.

The image assets are checked in under `notebooks/diagrams/`. Rebuilds reuse the asset whose filename hashes the source. If Mermaid source changes, generate its new image before rebuilding notebooks:

```powershell
$env:PUPPETEER_SKIP_DOWNLOAD='true'
npm.cmd ci --prefix scripts/diagram-renderer --ignore-scripts
.venv\Scripts\python scripts/render_notebook_diagrams.py --browser 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'
```

On other platforms supply an installed Chromium-compatible executable, or install Puppeteer's managed browser and omit `--browser`. The local renderer uses the pinned package lock. It renders sequentially to keep memory use bounded. The images are build artifacts from authored course content, not external images.

Regenerate with `build_notebooks.py`, `build_session03.py`, `build_session04.py`, `build_session05.py`, `build_day2.py` and `build_day3.py`. Each supports `--check`. Then run `scripts/verify_course_notebooks.py`, structure validation and the unit tests. The verifier requires a PNG output from every diagram cell separately, so a lesson's unrelated plotting output cannot mask a missing diagram.

## Teaching controls

Use Next step or Run all steps, then Print revealed objects. Public bytes print as length, SHA-256 and full hex. Disposable secrets require an explicit reveal setting. Reset and scenario changes clear prior rows and inspection output. Sessions 8 and 16 also expose a numeric assumption slider. Plain-function alternatives return the same rows and artifacts for examination without widgets.

Never substitute production keys. Clear execution outputs before distributing a saved notebook. Local callback tests and fresh-kernel execution do not establish that every Colab frontend configuration works; rehearse the actual teaching runtime.
