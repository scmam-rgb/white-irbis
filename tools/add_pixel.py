"""Inserts <script src="/pixel.js"> into every public page (idempotent).
Run after any build_*.py:  python3 tools/add_pixel.py"""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parent.parent
TAG = '<script src="/pixel.js" defer></script>'
pages = [p for p in ROOT.rglob('*.html')
         if '.git' not in p.parts and 'tools' not in p.parts and p.parent.name != 'promo']
for p in pages:
    s = p.read_text(encoding='utf-8')
    if 'src="/pixel.js"' in s:
        continue
    s2, n = re.subn(r'(<meta charset="?utf-8"?\s*/?>)', r'\1' + TAG, s, count=1, flags=re.I)
    if n:
        p.write_text(s2, encoding='utf-8')
        print('added', p.relative_to(ROOT))
    else:
        print('SKIP (no charset meta)', p.relative_to(ROOT))
