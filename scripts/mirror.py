"""Capture public ICMC pages for a static redesign sandbox."""
import json
from pathlib import Path
import subprocess
import shutil
from bs4 import BeautifulSoup

capture = Path('capture')
result = subprocess.run([
    'wget', '-e', 'robots=off', '--recursive', '--level=3', '--page-requisites',
    '--convert-links', '--adjust-extension', '--no-parent',
    '--domains=icmclean.org', '--timeout=20', '--tries=2',
    '--wait=0.2', '--quota=200m', '--max-redirect=5',
    '--reject-regex=wp-admin|wp-login|wp-json|replytocom|/feed/|[?]s=',
    '--directory-prefix=capture', '--output-file=mirror.log',
    'https://icmclean.org/'
], timeout=900)
source = capture / 'icmclean.org'
pages = list(source.rglob('*.html'))
if not (source / 'index.html').exists() or len(pages) < 2:
    raise RuntimeError('Capture did not produce a multipage site; inspect mirror.log')
for path in pages:
    soup = BeautifulSoup(path.read_bytes(), 'html.parser')
    if soup.head:
        for old in soup.select('meta[name="robots"], link[rel="canonical"]'):
            old.decompose()
        soup.head.append(soup.new_tag('meta', attrs={'name': 'robots', 'content': 'noindex,nofollow'}))
    for form in soup.find_all('form'):
        form['action'] = '#'
        form['onsubmit'] = 'return false'
        for control in form.select('input,textarea,select,button'):
            control['disabled'] = 'disabled'
    if soup.body:
        banner = soup.new_tag('div', attrs={'style': 'background:#fff3cd;color:#493600;padding:9px;text-align:center;font:14px sans-serif;position:relative;z-index:99999'})
        banner.string = 'ICMC website prototype — forms are disabled for testing.'
        soup.body.insert(0, banner)
    path.write_text(str(soup), encoding='utf-8')
if Path('docs').exists():
    shutil.rmtree('docs')
shutil.copytree(source, 'docs')
Path('docs/.nojekyll').touch()
Path('docs/robots.txt').write_text('User-agent: *\nDisallow: /\n')
Path('index.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex,nofollow"><meta http-equiv="refresh" content="0;url=docs/"><title>ICMC prototype</title></head><body><a href="docs/">Open the ICMC prototype</a></body></html>')
report = {'wget_exit_code': result.returncode, 'pages': [str(p.relative_to(source)) for p in pages], 'files': sum(1 for p in source.rglob('*') if p.is_file()), 'limitations': ['WordPress backend is not included.', 'Forms are disabled.', 'External embeds and services remain external.', 'Browser visual QA and custom-domain setup remain pending.']}
Path('mirror-report.json').write_text(json.dumps(report, indent=2))
print(json.dumps(report, indent=2))
