"""Read the local database and refresh the publishable snapshot."""
import hashlib
import re
import sys
sys.dont_write_bytecode = True
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'database'))
from store import ROOT, data_script, write


def main():
    script = data_script()
    write(ROOT / 'static' / 'data.js', script)
    path = ROOT / 'static' / 'index.html'
    text = path.read_text(encoding='utf-8')
    version = hashlib.sha256(script.encode('utf-8')).hexdigest()[:12]
    text = re.sub(r'data\.js\?v=[\w]+', 'data.js?v=' + version, text)
    write(path, text)
    print('ZBLS static data exported:', version)


if __name__ == '__main__':
    main()
