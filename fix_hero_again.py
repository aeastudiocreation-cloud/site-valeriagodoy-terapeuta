import os
import re

build_dir = r'c:\Users\aline\OneDrive\Desktop\Site-terapeuta-valeriagodoy\build'
path = os.path.join(build_dir, 'index.html')

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

old_p = '<p style="font-size:var(--t-sm);color:#000;font-weight:500;margin:0;margin-inline:auto;">Dê o primeiro passo'
new_p = '<p class="esconde-mobile" style="font-size:var(--t-sm);color:#000;font-weight:500;margin:0;margin-inline:auto;">Dê o primeiro passo'

if old_p in content:
    content = content.replace(old_p, new_p)
    content = re.sub(r'style-v2\.css\?v=\d+', 'style-v2.css?v=23', content)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('HTML updated.')
else:
    print('String not found in HTML.')

# Also update CSS
css_path = os.path.join(build_dir, 'assets', 'css', 'style-v2.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the previous block we added
old_css_hero = '''/* MOBILE HERO TEXT FIX */
@media (max-width: 768px) {
  .hero p.abertura {
    font-size: 15px !important;
    font-weight: 500 !important;
    line-height: 1.4 !important;
    margin-bottom: 1.25rem !important;
  }
}'''

new_css_hero = '''/* MOBILE HERO TEXT FIX V2 */
@media (max-width: 768px) {
  .hero p.abertura {
    font-size: 16.5px !important;
    font-weight: 500 !important;
    line-height: 1.45 !important;
    margin-bottom: 1.5rem !important;
  }
  .esconde-mobile {
    display: none !important;
  }
}'''

if old_css_hero in css:
    css = css.replace(old_css_hero, new_css_hero)
else:
    css += '\n' + new_css_hero

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print('CSS updated.')
