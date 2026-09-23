"""Execute all Day 3 notebooks in separate fresh local kernels."""
import subprocess
import sys
from build_day3 import DAY3_NAMES, ROOT

for name in DAY3_NAMES:
    subprocess.run([sys.executable, str(ROOT / 'scripts/verify_aead_notebook.py'), name], check=True)
print('PASS: all five Day 3 notebooks verified locally; live Colab not tested')
