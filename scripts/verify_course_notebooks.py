"""Execute every implemented notebook; save detailed output only under .verification."""
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
course=json.loads((ROOT/'course.json').read_text(encoding='utf-8'))
names=[Path(item['notebook']).stem for item in course['lessons']+course['labs']
       if item.get('status')=='implemented' and 'notebook' in item]
for name in names:
    result=subprocess.run([sys.executable,'-X','utf8',str(ROOT/'scripts/verify_aead_notebook.py'),name],
                          cwd=ROOT,capture_output=True,text=True,encoding='utf-8')
    (ROOT/'.verification'/f'{name}.log').write_text(result.stdout+'\n'+result.stderr,encoding='utf-8')
    if result.returncode:
        raise SystemExit(f'FAIL: {name}; inspect .verification/{name}.log')
    print('PASS:',name,flush=True)
print(f'PASS: all {len(names)} implemented notebooks, including embedded diagram outputs')
