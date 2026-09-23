"""Build Session 4's clean notebook and demo from its Markdown lesson."""
import argparse
from build_session03 import ROOT, render


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    notebook, demo = render(session=4)
    name = 'session-04-classical-public-key'
    for relative, expected in [(f'notebooks/{name}.ipynb', notebook),
                               (f'docs/downloads/{name}.ipynb', notebook),
                               ('examples/session-04/demo.py', demo)]:
        path = ROOT / relative
        if args.check:
            assert path.exists() and path.read_text(encoding='utf-8') == expected, f'Stale: {relative}'
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(expected, encoding='utf-8')
    print('PASS: Session 4 notebook, download, and demo synchronized.')


if __name__ == '__main__':
    main()
