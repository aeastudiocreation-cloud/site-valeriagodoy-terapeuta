import os
import glob

search_text = '<div style="display: flex; flex-direction: column; gap: 0.25rem;">
<span>© 2026 Valéria Godoy · Terapeuta TRG</span>
<span style="font-size: 0.85em; opacity: 0.8;">Site desenvolvido por <a href="https://aeawebstudio.com/" target="_blank" rel="noopener" style="text-decoration: underline;">A&Ä Studio</a></span>
</div>'
replace_text = '''<div style="display: flex; flex-direction: column; gap: 0.25rem;">
<div style="display: flex; flex-direction: column; gap: 0.25rem;">
<span>© 2026 Valéria Godoy · Terapeuta TRG</span>
<span style="font-size: 0.85em; opacity: 0.8;">Site desenvolvido por <a href="https://aeawebstudio.com/" target="_blank" rel="noopener" style="text-decoration: underline;">A&Ä Studio</a></span>
</div>
<span style="font-size: 0.85em; opacity: 0.8;">Site desenvolvido por <a href="https://aeawebstudio.com/" target="_blank" rel="noopener" style="text-decoration: underline;">A&Ä Studio</a></span>
</div>'''

files = glob.glob('build/**/*.html', recursive=True)
files += glob.glob('04-referencia-visual/**/*.html', recursive=True)
files += glob.glob('*.py')

count = 0
for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if search_text in content:
        new_content = content.replace(search_text, replace_text)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f'Updated {filepath}')

print(f'Total files updated: {count}')
