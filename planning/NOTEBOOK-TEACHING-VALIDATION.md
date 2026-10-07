# Interactive teaching and notebook diagrams validation

Validated 7 October 2026.

Sessions 7–16 now include common Next step, Run all steps, Reset experiment and Print revealed objects controls, with scenario selection, explicit disposable-secret reveal and plain-function equivalents. Quantum risk and migration planning expose numeric assumption sliders. Instructor pages give prediction and debrief prompts for each experiment.

All implemented notebook generators replace Mermaid fences with embedded PNG display cells. Images are produced locally by a pinned Mermaid CLI, cached by source hash and retained in notebook code so no online rendering service is needed at execution time. Original Mermaid is in diagram-cell metadata. Run all cells, including the collapsed Display teaching diagram cells, to display images.

## Results

- All 18 implemented notebooks executed in separate fresh local kernels.
- All 51 diagram cells across 17 of those notebooks emitted `image/png`; the remaining implemented notebook has no Mermaid fences. No Markdown Mermaid fences remain in notebook cells.
- All 20 unit tests passed, including the complete Sessions 7–16 scenario matrix, key-display opt-in, dropdown/reset controls, grant restoration, historical backup exposure, planning sensitivity and retirement gates.
- All six notebook generation entry points passed `--check`.
- Course inventory validation and strict website build passed.
- Representative PKI, TLS, HNDL, KEM, key-lifecycle and migration diagram images visually inspected.

## Limits

Local widget callbacks and notebook outputs were verified; a live Colab runtime was not executed in this update. Learners must reopen the GitHub notebook to obtain the new version; saved personal copies do not update automatically. Policy/planning models remain labelled and are not production validators or protocol implementations. TLS is a real whole-handshake operation, not a packet-by-packet trace. KEM/hybrid teaching key schedules are not standardized deployed profiles. Source notebooks retain no executed secret outputs.
