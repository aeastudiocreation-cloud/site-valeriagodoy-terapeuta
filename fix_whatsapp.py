import os
import re

build_dir = r'c:\Users\aline\OneDrive\Desktop\Site-terapeuta-valeriagodoy\build'

old_btn = '''<a class="btn btn--zap btn--pequeno" href="https://wa.me/5519920009231" rel="noopener" target="_blank">
<svg aria-hidden="true" fill="currentColor" height="17" viewbox="0 0 24 24" width="17"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .1-1.7-.1a11 11 0 0 1-5.9-5.1c-.4-.7-.7-1.5-.7-2.2 0-.7.4-1.4.7-1.7.3-.3.6-.3.8-.3h.6c.2 0 .4 0 .6.5l.8 1.9c.1.2 0 .4-.1.5l-.4.5c-.1.2-.3.3-.1.6a8 8 0 0 0 3.6 3.1c.3.2.5.1.6 0l.7-.8c.2-.2.4-.2.6-.1l1.8.9c.2.1.4.2.4.3.1.2.1.5 0 .8Z"></path></svg>
        WhatsApp
      </a>'''

new_btn = '''<a class="btn btn--zap btn--pequeno header-zap" href="https://wa.me/5519920009231" rel="noopener" target="_blank" aria-label="WhatsApp">
<svg aria-hidden="true" fill="currentColor" viewBox="0 0 24 24" width="20" height="20"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .1-1.7-.1a11 11 0 0 1-5.9-5.1c-.4-.7-.7-1.5-.7-2.2 0-.7.4-1.4.7-1.7.3-.3.6-.3.8-.3h.6c.2 0 .4 0 .6.5l.8 1.9c.1.2 0 .4-.1.5l-.4.5c-.1.2-.3.3-.1.6a8 8 0 0 0 3.6 3.1c.3.2.5.1.6 0l.7-.8c.2-.2.4-.2.6-.1l1.8.9c.2.1.4.2.4.3.1.2.1.5 0 .8Z"></path></svg>
<span class="zap-texto" style="margin-left: 6px;">WhatsApp</span>
</a>'''

# Actually, the SVG might just be easier to target via Regex in case whitespace is slightly different
regex_pattern = r'<a class="btn btn--zap btn--pequeno" href="https://wa\.me/5519920009231" rel="noopener" target="_blank">\s*<svg[^>]+>.*?</svg>\s*WhatsApp\s*</a>'

count = 0
for root, _, files in os.walk(build_dir):
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = re.sub(regex_pattern, new_btn, content, flags=re.DOTALL)
            if new_content != content:
                new_content = re.sub(r'style-v2\.css\?v=\d+', 'style-v2.css?v=19', new_content)
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
print(f'Replaced in {count} files.')

css_path = os.path.join(build_dir, 'assets', 'css', 'style-v2.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Fix CSS to match the new class structure
old_css = '''.header__acoes .btn--zap {
    font-size: 0 !important;
    padding: 0 !important;
    width: 44px !important;
    height: 44px !important;
    min-width: 44px !important;
    min-height: 44px !important;
    border-radius: 50% !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
  }
  .header__acoes .btn--zap svg {
    margin: 0 !important;
    width: 22px !important;
    height: 22px !important;
  }'''

new_css = '''.header__acoes .header-zap .zap-texto { display: none !important; }
  .header__acoes .header-zap {
    padding: 0 !important;
    width: 44px !important;
    height: 44px !important;
    min-width: 44px !important;
    min-height: 44px !important;
    border-radius: 50% !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
  }
  .header__acoes .header-zap svg {
    margin: 0 !important;
    width: 24px !important;
    height: 24px !important;
  }'''

if old_css in css_content:
    css_content = css_content.replace(old_css, new_css)
else:
    # Just append it if old wasn't found (should be found)
    pass

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("CSS updated.")
