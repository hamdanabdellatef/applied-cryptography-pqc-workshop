"""Execute Lab 1 (default) or a session companion in a fresh local kernel.

Pass session-03-hashes-passwords-kdfs or session-04-classical-public-key.

Creates verification artifacts locally; never writes executed outputs into
student notebooks. This is local kernel verification, not a live Colab test.
"""
import json
import os
from pathlib import Path
import sys

import nbformat
from build_day2 import DAY2_NAMES
from build_day3 import DAY3_NAMES
from nbclient import NotebookClient
from jupyter_client import KernelManager
from jupyter_client.kernelspec import KernelSpecManager

ROOT = Path(__file__).resolve().parents[1]


def main():
    work = ROOT / '.verification'
    kernel_dir = work / 'kernels' / 'workshop'
    kernel_dir.mkdir(parents=True, exist_ok=True)
    (kernel_dir / 'kernel.json').write_text(json.dumps({
        'argv': [sys.executable, '-m', 'ipykernel_launcher', '-f', '{connection_file}'],
        'display_name': 'Workshop verification', 'language': 'python',
    }), encoding='utf-8')
    os.environ['JUPYTER_RUNTIME_DIR'] = str(work / 'runtime')
    os.environ['IPYTHONDIR'] = str(work / 'ipython')
    os.environ['MPLCONFIGDIR'] = str(work / 'matplotlib')
    os.environ['MPLBACKEND'] = 'module://matplotlib_inline.backend_inline'
    spec = KernelSpecManager(kernel_dirs=[str(work / 'kernels')])
    km = KernelManager(kernel_name='workshop', kernel_spec_manager=spec)
    name = sys.argv[1] if len(sys.argv) > 1 else 'lab-01-aead'
    assert name in set(DAY2_NAMES + DAY3_NAMES) | {'lab-01-aead', 'session-03-hashes-passwords-kdfs',
                    'session-04-classical-public-key', 'session-05-digital-signatures'}
    notebook = nbformat.read(ROOT / 'notebooks' / (name + '.ipynb'), as_version=4)
    nbformat.validate(notebook)
    client = NotebookClient(notebook, km=km, timeout=180, resources={'metadata': {'path': str(work)}})
    client.execute()
    nbformat.write(notebook, work / (name + '.executed.ipynb'))
    outputs = '\n'.join(output.get('text', '') for cell in notebook.cells
                        for output in cell.get('outputs', []) if output.output_type == 'stream')
    if name in DAY2_NAMES + DAY3_NAMES:
        assert f'PASS: completed {name}' in outputs
        if name.startswith('lab-'):
            assert 'NOT ATTEMPTED:' in outputs
            assert 'reference checks' in outputs
        if name in {'session-08-quantum-threat', 'session-11-ml-dsa', 'session-16-pqc-migration'}:
            assert any('image/png' in output.get('data', {}) for cell in notebook.cells
                       for output in cell.get('outputs', [])), 'Expected rendered graph'
        print(outputs)
        print(f'PASS: fresh local kernel verified {name}')
        return
    if name.startswith('session-'):
        assert outputs.count('PASS:') == 7, 'Expected all seven experiment success messages'
        print(outputs)
        print(f'PASS: {name} executed in a fresh local kernel; student outputs remain clean.')
        return
    assert 'NOT ATTEMPTED' in outputs, 'Untouched learner exercise must not be reported as passing'
    assert 'supplied reference solution passed acceptance checks' in outputs
    assert 'amount=00000999' in outputs, 'Nonce-reuse recovery did not execute'
    assert any('image/png' in output.get('data', {}) for cell in notebook.cells
               for output in cell.get('outputs', [])), 'Notebook graph was not rendered'
    print(outputs)
    print('PASS: complete notebook executed in a fresh local kernel; student outputs remain clean.')


if __name__ == '__main__':
    main()
