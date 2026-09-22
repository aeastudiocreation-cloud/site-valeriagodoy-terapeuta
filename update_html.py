import os, glob, re

replacements = {
    'quem-somos.jpg?v=3': 'hero.webp',
    'quem-somos.jpg': 'hero.webp',
    'valeria-godoy.jpg?v=3': 'valeria-godoy.webp',
    'valeria-godoy.jpg': 'valeria-godoy.webp',
    'valeria-godoy-small.jpg': 'valeria-godoy-small.webp',
    'ansiedade.jpg': 'blog-1.webp',
    'homem-na-cortina.jpg': 'blog-2.webp',
    'logo-valeria.jpeg': 'logo-valeria.webp',
    'favicon.svg': 'favicon.png',
    'type="image/svg+xml"': 'type="image/png"'
}

files = glob.glob('build/**/*.html', recursive=True)
files += glob.glob('04-referencia-visual/**/*.html', recursive=True)
files += glob.glob('*.py')

def add_missing_attributes(html_content):
    # Regex to find all img tags
    # We will ensure they have alt and loading="lazy"
    
    def replacer(match):
        img_tag = match.group(0)
        if 'alt=' not in img_tag:
            img_tag = img_tag.replace('<img', '<img alt=""')
        if 'loading=' not in img_tag:
            img_tag = img_tag.replace('<img', '<img loading="lazy"')
        return img_tag

    return re.sub(r'<img[^>]+>', replacer, html_content)

for filepath in files:
    if filepath == os.path.basename(__file__) or filepath == 'process_images.py':
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    for old, new in replacements.items():
        new_content = new_content.replace(old, new)
    
    if filepath.endswith('.html'):
        new_content = add_missing_attributes(new_content)
        
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
