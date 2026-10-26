from pathlib import Path
import hashlib,json
from urllib.parse import quote
root=Path('docs')
mapping={}
# Restore prior names before a repeat normalization pass.
report=Path('filename-fixes.json')
if report.exists():
    prior=json.loads(report.read_text())
    for p in list(root.rglob('*')):
        if not p.is_file(): continue
        for old,new in prior.items():
            if p.name==new: p.rename(p.with_name(old)); break
    for p in root.rglob('*'):
        if not p.is_file(): continue
        try: text=p.read_text()
        except (UnicodeDecodeError,OSError): continue
        original=text
        for old,new in prior.items(): text=text.replace(new,quote(old,safe=''))
        if text!=original: p.write_text(text)

for p in list(root.rglob('*')):
    if p.is_file() and '?' in p.name:
        stem=p.name.split('?')[0]
        suffix=Path(stem).suffix
        if p.name.endswith('.html'): suffix='.html'
        if suffix and stem.endswith(suffix): stem=stem[:-len(suffix)]
        new=stem+'-'+hashlib.sha256(p.name.encode()).hexdigest()[:10]+suffix
        mapping[p.name]=new
        p.rename(p.with_name(new))
for p in root.rglob('*'):
    if not p.is_file(): continue
    try: text=p.read_text()
    except (UnicodeDecodeError,OSError): continue
    original=text
    for old,new in sorted(mapping.items(),key=lambda x:-len(x[0])):
        text=text.replace(quote(old,safe=''),new).replace(old.replace('&','&amp;'),new).replace(old,new)
    if text!=original: p.write_text(text)
Path('filename-fixes.json').write_text(json.dumps(mapping,indent=2))
print('Normalized',len(mapping),'query-string filenames.')
