# Day 2 setup and delivery

Day 2 has six self-study lessons, six instructor guides and three guided labs. Each has a downloadable notebook. Upload an `.ipynb` using **File → Upload notebook** in [Google Colab](https://colab.research.google.com/), then run cells from the top. Use only disposable teaching data.

The notebooks install `cryptography==50.0.1`, `matplotlib==3.10.6` and `ipywidgets==8.1.7`. They embed [shared helper code](../downloads/day2_helpers.py) and require no repository checkout. If a different version was already imported, restart the runtime after installation. A supported official binary wheel and backend are required for ML-KEM/ML-DSA. An unsupported-backend error must stop the experiment; never substitute a dummy secret or classical algorithm.

For local use, run from the repository root:

```powershell
.\.venv\Scripts\python -m pip install -r requirements-day2.txt
.\.venv\Scripts\python scripts/build_day2.py
.\.venv\Scripts\python examples/session-06/demo.py
.\.venv\Scripts\python labs/lab-04-mini-pki/starter.py
```

Use `.venv/bin/python` on macOS/Linux. Session examples live in `examples/session-06` through `session-11`; Labs 4–6 retain their named folders. The lesson and lab Markdown files are authoritative. `scripts/build_day2.py --check` checks generated notebooks, downloadable helper source, and local demos/starters.

PKI/TLS exercises create fresh keys and a temporary certificate directory. The handshake uses real TLS 1.3 through memory buffers, without network listeners, external hosts, or changes to the operating-system trust store. They do not implement online certificate revocation. Temporary-file removal does not promise secure erasure.

The PQ examples use real ML-KEM-768 and ML-DSA-65. They are primitive demonstrations, not a standardized PQ TLS implementation. The hybrid example is explicitly a teaching combiner. SLH-DSA is covered conceptually only.

## If an experiment fails

| Symptom | Check |
| --- | --- |
| Import or unsupported-algorithm error | Pinned version, supported Python/wheel, clean runtime and backend; do not silently downgrade |
| TLS hostname error | Expected service identity and certificate SAN; do not disable checking |
| Unknown issuer | Correct local anchor and supplied intermediate chain |
| Certificate expired | Runtime clock and newly generated teaching certificates |
| Widget not visible | Use the documented direct function call; widgets are optional controls |
| Learner checks say NOT ATTEMPTED | Implement the learner function; reference checks do not count as your completion |
| Mermaid appears as source in notebook | View diagrams on the website; explanations and source are still available |

Local verification and live Colab verification are distinct. See `planning/DAY-02-VALIDATION.md` for completed checks and remaining delivery limitations. No upload to a Google account is performed automatically.
