"""Check the course inventory and notebook scaffold using the standard library."""

import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    course = json.loads((ROOT / 'course.json').read_text(encoding='utf-8'))
    assert len(course['lessons']) == 16, 'Expected 16 lessons'
    assert len(course['labs']) == 6, 'Expected six labs'
    for group in ('lessons', 'labs'):
        entries = course[group]
        assert len({entry['id'] for entry in entries}) == len(entries)
        for entry in entries:
            assert (ROOT / entry['page']).is_file(), entry['page']
            for field in ('instructor_page', 'worksheet', 'demo'):
                if field in entry:
                    assert (ROOT / entry[field]).is_file(), entry[field]
    for lab in course['labs'] + [lesson for lesson in course['lessons'] if 'notebook' in lesson]:
        if 'starter' in lab:
            ast.parse((ROOT / lab['starter']).read_text(encoding='utf-8'))
        notebook = json.loads((ROOT / lab['notebook']).read_text(encoding='utf-8'))
        assert notebook['nbformat'] == 4
        assert notebook['metadata']['kernelspec']['language'] == 'python'
        ids = [cell['id'] for cell in notebook['cells']]
        assert len(ids) == len(set(ids))
        for cell in notebook['cells']:
            if cell['cell_type'] == 'code':
                assert cell['execution_count'] is None
                assert cell['outputs'] == []
                ast.parse(''.join(cell['source']))
    print('PASS: course pages, instructor resources, Python starters, and all registered clean notebooks.')


if __name__ == '__main__':
    main()
