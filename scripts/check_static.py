#!/usr/bin/env python3
"""Static-site integrity checks for the ICMC prototype."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = sorted([p for p in ROOT.glob('*.html') if p.name != '404.html'])
REF_RE = re.compile(r'(?:href|src)=["\']([^"\']+)["\']', re.IGNORECASE)
IGNORE_PREFIXES = ('http://', 'https://', 'mailto:', 'tel:', '#', 'data:', 'javascript:')

required_files = [
    ROOT / 'index.html',
    ROOT / 'site.css',
    ROOT / 'site.js',
    ROOT / 'services.html',
    ROOT / 'docs/wp-content/uploads/2022/01/ICMC-Logo_Small.png',
    ROOT / 'docs/services/marriage/index.html',
    ROOT / 'docs/services/funeral/index.html',
    ROOT / 'docs/services/shahada/index.html',
]

errors: list[str] = []

for req in required_files:
    if not req.exists():
        errors.append(f'Missing required file: {req.relative_to(ROOT)}')

for html_path in HTML_FILES:
    text = html_path.read_text(encoding='utf-8')

    if '<nav ' not in text:
        errors.append(f'{html_path.name}: missing <nav> block')
    if '<footer' not in text:
        errors.append(f'{html_path.name}: missing <footer> block')

    for ref in REF_RE.findall(text):
        if ref.startswith(IGNORE_PREFIXES):
            continue
        base_ref = ref.split('#', 1)[0]
        if not base_ref:
            continue

        target = (ROOT / base_ref).resolve()
        if base_ref.startswith('./'):
            target = (html_path.parent / base_ref[2:]).resolve()
        elif not base_ref.startswith('/'):
            target = (html_path.parent / base_ref).resolve()

        if base_ref.endswith('/') and target.is_dir():
            target = target / 'index.html'

        try:
            target.relative_to(ROOT)
        except ValueError:
            errors.append(f'{html_path.name}: reference escapes repo root: {ref}')
            continue

        if not target.exists():
            rel = target.relative_to(ROOT)
            errors.append(f'{html_path.name}: broken local reference "{ref}" -> {rel}')

if errors:
    print('Static integrity check failed:')
    for err in errors:
        print(f'- {err}')
    sys.exit(1)

print(f'OK: {len(HTML_FILES)} pages scanned, required assets present, local references resolved.')
