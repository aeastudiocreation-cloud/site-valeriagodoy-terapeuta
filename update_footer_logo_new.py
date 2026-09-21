import os
from bs4 import BeautifulSoup

build_dir = 'build'
html_files = []

for root, _, files in os.walk(build_dir):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'lxml')
    
    # Encontrar a imagem da logo no rodapé
    footer = soup.find('footer')
    if footer:
        img = footer.find('img', class_='footer-logo')
        if img:
            img['src'] = '/assets/img/logo-nova-rodape.jpg'
            # Manter a proporcao correta e garantir legibilidade se for escura/clara, mas aqui e uma imagem.
            img['style'] = "max-height: 120px; width: auto; mix-blend-mode: multiply;" 
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"Updated {filepath}")
