"""Render course Mermaid diagrams locally using pinned mermaid-cli.

Install scripts/diagram-renderer dependencies first. Supply --node and optionally
--browser for a locally installed Chromium/Edge executable. No external rendering service.
"""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
from notebook_diagrams import ROOT, PATTERN, diagram_id

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--node', default='node')
parser.add_argument('--browser')
args = parser.parse_args()
sources = list((ROOT / 'docs').glob('day-*/*.md')) + list((ROOT / 'docs/labs').glob('*.md')) + list((ROOT / 'notebooks/source').glob('*.md'))
diagrams = {}
for path in sources:
    for match in PATTERN.finditer(path.read_text(encoding='utf-8')):
        diagrams[diagram_id(match.group(1))] = match.group(1)
out = ROOT / 'notebooks/diagrams'
out.mkdir(exist_ok=True)
pending = {k:v for k,v in diagrams.items() if not (out / (k+'.png')).exists()}
if pending:
    work = ROOT / '.verification/mermaid'
    work.mkdir(parents=True, exist_ok=True)
    (work / 'manifest.json').write_text(json.dumps(pending), encoding='utf-8')
    command = [args.node, str(ROOT / 'scripts/diagram-renderer/render.mjs'), str(work/'manifest.json'),str(out)]
    if args.browser: command.append(args.browser)
    subprocess.run(command, check=True)
print(f'PASS: {len(diagrams)} unique Mermaid PNG assets ready')
