# Re-applies phone layout CSS if a sync strips it. Run by .github/workflows/mobile-guard.yml
import json, os
base = json.load(open('.jm/base.json')); mob = open('.jm/mobile.html').read()
changed = []
for f, d in base.items():
    if not os.path.exists(f): continue
    s = open(f).read(); o = s
    if d['base'] and '.wrap {' not in s and '<style id="jm-apple-system">' in s:
        s = s.replace('<style id="jm-apple-system">', d['base'] + '\n<style id="jm-apple-system">', 1)
    if 'id="jm-mobile"' not in s and '</head>' in s:
        i = s.index('</head>'); s = s[:i] + mob + s[i:]
    if s != o: open(f, 'w').write(s); changed.append(f)
print('repaired:', changed or 'nothing')
