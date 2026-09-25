import os
import re
from datetime import datetime

build_dir = r'c:\Users\aline\OneDrive\Desktop\Site-terapeuta-valeriagodoy\build'
today = datetime.now().strftime('%Y-%m-%d')
today_iso = datetime.now().strftime('%Y-%m-%dT08:00:00-03:00')
today_pt = "22 de Setembro de 2026"

new_card = f"""
<article class="post" data-cat="traumas">
<div aria-hidden="true" class="post__capa" style="background: #fff url('/assets/img/blog-1.webp') center/cover no-repeat; color:transparent;">Terapia TRG para traumas</div>
<div class="post__corpo">
<p class="post__meta">{today_pt}</p>
<h3><a href="/blog/terapia-trg-para-traumas">Terapia TRG para traumas: como funciona o processo terapêutico?</a></h3>
<p>Descubra como a Terapia de Reprocessamento Generativo (TRG) auxilia no tratamento de traumas e fobias de forma estruturada.</p>
<a class="card__link" href="/blog/terapia-trg-para-traumas">Ler o artigo</a>
</div>
</article>"""

# Update blog/index.html
blog_index = os.path.join(build_dir, 'blog', 'index.html')
with open(blog_index, 'r', encoding='utf-8') as f:
    content = f.read()

anchor = '<div class="grade grade--3" id="listaPosts" style="margin-top:var(--e5)">'
if anchor in content and 'terapia-trg-para-traumas' not in content:
    content = content.replace(anchor, anchor + new_card)
    with open(blog_index, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated blog index.")

# Update sitemap.xml
sitemap_path = os.path.join(build_dir, 'sitemap.xml')
if os.path.exists(sitemap_path):
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        sitemap = f.read()
    
    if '/blog/terapia-trg-para-traumas' not in sitemap:
        new_sitemap_entry = f"""
  <url>
    <loc>https://valeriagodoyterapeuta.com/blog/terapia-trg-para-traumas</loc>
    <lastmod>{today}</lastmod>
    <priority>0.7</priority>
  </url>"""
        sitemap = sitemap.replace('</urlset>', new_sitemap_entry + '\n</urlset>')
        with open(sitemap_path, 'w', encoding='utf-8') as f:
            f.write(sitemap)
        print("Updated sitemap.xml.")

# Create feed.xml
feed_path = os.path.join(build_dir, 'feed.xml')
feed_content = f"""<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>Blog - Valéria Godoy Terapeuta TRG</title>
  <subtitle>Artigos sobre Terapia Emocional, TRG, Ansiedade e Depressão</subtitle>
  <link href="https://valeriagodoyterapeuta.com/feed.xml" rel="self"/>
  <link href="https://valeriagodoyterapeuta.com/blog"/>
  <updated>{today_iso}</updated>
  <id>https://valeriagodoyterapeuta.com/blog</id>
  <author>
    <name>Valéria Godoy</name>
  </author>
  
  <entry>
    <title>Terapia TRG para traumas: como funciona o processo terapêutico?</title>
    <link href="https://valeriagodoyterapeuta.com/blog/terapia-trg-para-traumas"/>
    <id>https://valeriagodoyterapeuta.com/blog/terapia-trg-para-traumas</id>
    <updated>{today_iso}</updated>
    <summary>Descubra como a Terapia de Reprocessamento Generativo (TRG) auxilia no tratamento de traumas e fobias de forma estruturada.</summary>
  </entry>
</feed>
"""
# Assuming we overwrite or create a simple one for now
with open(feed_path, 'w', encoding='utf-8') as f:
    f.write(feed_content)
print("Created feed.xml.")
