"""Build Session 5's notebook and Python demo from its Markdown lesson."""
import argparse
from build_session03 import ROOT, render


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    notebook, demo = render(session=5)
    name = 'session-05-digital-signatures'
    for relative, expected in [(f'notebooks/{name}.ipynb', notebook),
                               (f'docs/downloads/{name}.ipynb', notebook),
                               ('examples/session-05/demo.py', demo)]:
        path = ROOT / relative
        if args.check:
            assert path.exists() and path.read_text(encoding='utf-8') == expected, f'Stale: {relative}'
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(expected, encoding='utf-8')
    print('PASS: Session 5 notebook, download, and demo synchronized.')


if __name__ == '__main__':
    main()
