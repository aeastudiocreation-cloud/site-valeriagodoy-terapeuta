import glob
import os
from bs4 import BeautifulSoup
from datetime import datetime

DOMINIO = "https://valeriagodoyterapeuta.com"
KEYWORD = "Terapeuta TRG em Santa Bárbara d'Oeste"

def get_canonical_path(filepath):
    # build\index.html -> /
    # build\sobre.html -> /sobre
    # build\blog\post.html -> /blog/post
    rel_path = os.path.relpath(filepath, "build").replace('\\', '/')
    if rel_path == "index.html":
        return "/"
    elif rel_path.endswith(".html"):
        return "/" + rel_path[:-5]
    return "/" + rel_path

urls_for_sitemap = []

for filepath in glob.glob('build/**/*.html', recursive=True):
    # Skip test files or drafts if any (404 is fine)
    if "test" in filepath.lower():
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'lxml')
        
    # 1. <html> lang
    if soup.html:
        soup.html['lang'] = 'pt-BR'
        
    # 2. Canonical
    canonical_path = get_canonical_path(filepath)
    canonical_url = DOMINIO + canonical_path
    
    # Store for sitemap
    urls_for_sitemap.append(canonical_url)
    
    if not soup.head:
        continue # Should not happen
        
    # Remove existing canonical if any
    for link in soup.head.find_all('link', rel='canonical'):
        link.decompose()
        
    canon = soup.new_tag('link', rel='canonical', href=canonical_url)
    soup.head.append(canon)
    
    # 3. Title (max 60)
    page_name = ""
    if soup.h1:
        page_name = soup.h1.get_text(strip=True)[:30]
    else:
        page_name = os.path.basename(filepath).replace(".html", "").replace("-", " ").title()
        
    if page_name.lower() == "index" or page_name.lower() == "você não precisa enfrentar suas questões emocionais sem acolhimento.":
        title_text = f"Valéria Godoy | {KEYWORD}"
    else:
        title_text = f"{page_name} | {KEYWORD}"
        
    if len(title_text) > 60:
        title_text = title_text[:57] + "..."
        
    if soup.title:
        soup.title.string = title_text
    else:
        title_tag = soup.new_tag('title')
        title_tag.string = title_text
        soup.head.append(title_tag)
        
    # 4. Meta Description (max 155)
    desc_text = f"Valéria Godoy, {KEYWORD.lower()}. Atendimento para ansiedade, depressão e reprocessamento de traumas online e presencial."
    
    existing_desc = soup.head.find('meta', attrs={'name': 'description'})
    if existing_desc:
        existing_desc['content'] = desc_text
    else:
        meta_desc = soup.new_tag('meta', attrs={'name': 'description', 'content': desc_text})
        soup.head.append(meta_desc)
        
    # 5. Open Graph & Twitter Cards
    # Remove old ones first to avoid duplicates
    for meta in soup.head.find_all('meta', property=lambda x: x and x.startswith('og:')):
        meta.decompose()
    for meta in soup.head.find_all('meta', attrs={'name': lambda x: x and x.startswith('twitter:')}):
        meta.decompose()
        
    og_tags = [
        ('og:title', title_text),
        ('og:description', desc_text),
        ('og:url', canonical_url),
        ('og:image', f"{DOMINIO}/assets/img/logo.png"),
        ('og:type', 'website'),
        ('og:site_name', 'Valéria Godoy Terapeuta')
    ]
    for prop, content in og_tags:
        tag = soup.new_tag('meta', property=prop, content=content)
        soup.head.append(tag)
        
    tw_tags = [
        ('twitter:card', 'summary_large_image'),
        ('twitter:title', title_text),
        ('twitter:description', desc_text),
        ('twitter:image', f"{DOMINIO}/assets/img/logo.png")
    ]
    for name, content in tw_tags:
        tag = soup.new_tag('meta', attrs={'name': name, 'content': content})
        soup.head.append(tag)
        
    # 6. H1 / H2 Hierarchy
    h1s = soup.find_all('h1')
    if len(h1s) > 1:
        # Keep the first one, change the rest to H2 with inline styling to preserve layout
        for i in range(1, len(h1s)):
            h1s[i].name = 'h2'
            # h1 default style in CSS: font-size:var(--h2);line-height:1.15;letter-spacing:-.01em
            # So changing to h2 might be perfectly fine visually, but just to be sure:
            existing_style = h1s[i].get('style', '')
            h1s[i]['style'] = existing_style + "; font-size:var(--h2);line-height:1.15;letter-spacing:-.01em;"
            
    # 7. Alt text in images
    for img in soup.find_all('img'):
        if not img.get('alt') or img.get('alt').strip() == "":
            img['alt'] = "Valéria Godoy Terapeuta TRG"
            
    # 8. Anchor texts generic
    for a in soup.find_all('a'):
        text = a.get_text(strip=True).lower()
        if text in ["clique aqui", "saiba mais", "leia mais", "veja mais"]:
            a.string = "Conheça nossos serviços de Terapia Emocional"
            
    # Optional: Fix any internal links (just making sure they exist, but the layout generation handles this usually)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))

# 9. Generate Sitemap
sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap_xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
today = datetime.now().strftime("%Y-%m-%d")
for url in sorted(set(urls_for_sitemap)):
    sitemap_xml += f"  <url>\n    <loc>{url}</loc>\n    <lastmod>{today}</lastmod>\n  </url>\n"
sitemap_xml += '</urlset>'

with open('build/sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_xml)
    
# 10. Generate robots.txt
robots_txt = f"""User-agent: *
Allow: /
Sitemap: {DOMINIO}/sitemap.xml

# Permitir crawlers de IA (importante para visibilidade em buscas com IA em 2026)
User-agent: GPTBot
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: PerplexityBot
Allow: /
"""
with open('build/robots.txt', 'w', encoding='utf-8') as f:
    f.write(robots_txt)
    
print("SEO optimization applied globally!")
