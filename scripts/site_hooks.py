"""Add GitHub-backed Colab links to implemented notebook downloads."""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def on_page_markdown(markdown, page, config, files):
    course = json.loads((ROOT / 'course.json').read_text(encoding='utf-8'))
    implemented = {Path(entry['notebook']).name for entry in course['lessons'] + course['labs']
                   if entry.get('status') == 'implemented' and 'notebook' in entry}
    repository = config['repo_url'].removeprefix('https://github.com/').rstrip('/')

    def add_colab(match):
        name = match.group(1)
        if name not in implemented:
            return match.group(0)
        url = f'https://colab.research.google.com/github/{repository}/blob/main/notebooks/{name}'
        return match.group(0) + f' · [Open in Colab]({url})'

    return re.sub(r'\[[^\]]+\]\([^)]*downloads/([^/()]+\.ipynb)\)', add_colab, markdown)
