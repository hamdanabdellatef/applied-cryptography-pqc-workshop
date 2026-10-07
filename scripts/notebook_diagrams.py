"""Embed locally rendered Mermaid PNGs in executable, collapsed notebook cells."""
import base64
import hashlib
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PATTERN = re.compile(r'^```mermaid\n(.*?)\n```[ \t]*$', re.M | re.S)


def diagram_id(source):
    return hashlib.sha256(source.strip().encode()).hexdigest()[:20]


def embed_diagrams(cells):
    result = []
    for cell in cells:
        if cell['cell_type'] != 'markdown':
            result.append(cell)
            continue
        source = ''.join(cell['source'])
        cursor = 0
        for match in PATTERN.finditer(source):
            before = source[cursor:match.start()].strip()
            if before:
                result.append(dict(cell_type='markdown', metadata={}, source=[before + '\n']))
            key = diagram_id(match.group(1))
            png = ROOT / 'notebooks/diagrams' / (key + '.png')
            if not png.exists():
                raise FileNotFoundError(f'Render Mermaid asset {key} with scripts/render_notebook_diagrams.py first')
            payload = base64.b64encode(png.read_bytes()).decode()
            code = ('#@title Display teaching diagram\n'
                    'from IPython.display import display as _diagram_display, Image as _DiagramImage\n'
                    'import base64 as _diagram_base64\n'
                    f'_diagram_display(_DiagramImage(data=_diagram_base64.b64decode({payload!r})))\n')
            result.append(dict(cell_type='code', metadata={'cellView':'form', 'jupyter':{'source_hidden':True},
                               'workshop_mermaid':match.group(1), 'diagram_id':key},
                               source=code.splitlines(keepends=True), execution_count=None, outputs=[]))
            cursor = match.end()
        if cursor:
            if source[cursor:].strip():
                result.append(dict(cell_type='markdown', metadata={}, source=[source[cursor:].strip() + '\n']))
        else:
            result.append(cell)
    for i, cell in enumerate(result):
        cell['id'] = f'course-{i:03d}'
    return result
