"""Build the self-contained Lab 1 notebook from Markdown and shared Python.

Only top-level fenced python blocks become executable cells. Other text remains
Markdown. Use --check to detect stale committed notebooks/downloads.
"""
import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def render():
    source = (ROOT / 'notebooks/source/lab-01-aead.md').read_text(encoding='utf-8')
    reference = (ROOT / 'src/crypto_workshop/aead.py').read_text(encoding='utf-8').rstrip()
    source = source.replace('<!-- workshop:reference-aead -->', f'```python\n{reference}\n```')
    cells = []

    def add(kind, text):
        if not text.strip():
            return
        cell = {'cell_type': kind, 'id': f'aead-{len(cells):03d}', 'metadata': {},
                'source': (text.strip() + '\n').splitlines(keepends=True)}
        if kind == 'code':
            cell.update(execution_count=None, outputs=[])
        cells.append(cell)

    cursor = 0
    for match in re.finditer(r'^```python\n(.*?)\n```\s*$', source, re.M | re.S):
        add('markdown', source[cursor:match.start()])
        add('code', match.group(1))
        cursor = match.end()
    add('markdown', source[cursor:])
    notebook = {'cells': cells, 'metadata': {
        'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'},
        'language_info': {'name': 'python'},
        'colab': {'name': 'lab-01-aead.ipynb', 'provenance': []},
    }, 'nbformat': 4, 'nbformat_minor': 5}
    return json.dumps(notebook, ensure_ascii=False, indent=2) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    expected = render()
    for path in ['notebooks/lab-01-aead.ipynb', 'docs/downloads/lab-01-aead.ipynb']:
        target = ROOT / path
        if args.check:
            if not target.exists() or target.read_text(encoding='utf-8') != expected:
                raise SystemExit(f'Stale notebook: {path}; run python scripts/build_notebooks.py')
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(expected, encoding='utf-8')
    print('PASS: Lab 1 notebook and website download are synchronized.')


if __name__ == '__main__':
    main()
