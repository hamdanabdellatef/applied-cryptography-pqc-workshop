"""Execute every Day 2 notebook in its own fresh local kernel, sequentially."""
import subprocess
import sys
from build_day2 import DAY2_NAMES, ROOT

for name in DAY2_NAMES:
    subprocess.run([sys.executable, str(ROOT / 'scripts/verify_aead_notebook.py'), name], check=True)
print('PASS: all nine Day 2 notebooks verified locally; live Colab not tested')
