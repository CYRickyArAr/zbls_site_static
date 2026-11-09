"""Read the local database and refresh the publishable snapshot."""
import gzip
import hashlib
import json
import re
import sys
sys.dont_write_bytecode = True
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'database'))
from store import ROOT, data_script, write, export_theme_images


def export_image_library():
    images = {}
    for path in sorted((ROOT / 'static' / 'images').rglob('C*.svg')):
        if re.fullmatch(r'C\d+(?:-\d+)?\.svg', path.name) and path.parent.name in ('images', 'light'):
            images[path.relative_to(ROOT / 'static').as_posix()] = ['image/svg+xml', path.read_text(encoding='utf-8')]
    raw = json.dumps({'version': 1, 'images': images}, ensure_ascii=False, separators=(',', ':')).encode('utf-8')
    packed = gzip.compress(raw, mtime=0)
    write(ROOT / 'static' / 'images' / 'image-library.json', raw)
    write(ROOT / 'static' / 'images' / 'image-library.json.gz', packed)
    print('ZBLS image library:', len(images), 'images,', len(packed), 'gzip bytes')
    return hashlib.sha256(raw).hexdigest()[:16]


def main():
    export_theme_images()
    image_version = export_image_library()
    script = data_script()
    write(ROOT / 'static' / 'data.js', script)
    path = ROOT / 'static' / 'index.html'
    text = path.read_text(encoding='utf-8')
    version = hashlib.sha256(script.encode('utf-8')).hexdigest()[:12]
    text = re.sub(r'data\.js\?v=[\w]+', 'data.js?v=' + version, text)
    text = re.sub(r'(images/image-library\.json(?:\.gz)?\?v=)[\w]+', lambda m: m[1] + image_version, text)
    write(path, text)
    print('ZBLS static data exported:', version)


if __name__ == '__main__':
    main()
