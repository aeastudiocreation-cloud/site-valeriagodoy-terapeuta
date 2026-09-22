import bs4
import os

filepath = 'build/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    soup = bs4.BeautifulSoup(f, 'lxml')

cta_html = '<div style="margin-top:var(--e6); text-align: center; width: 100%;"><a class="btn btn--zap" href="https://wa.me/5519920009231" rel="noopener" target="_blank">Agendar Avaliação</a></div>'

# 1. Por que escolher
h2_escolher = soup.find(lambda tag: tag.name == 'h2' and 'Por que escolher' in tag.text)
if h2_escolher:
    sec = h2_escolher.find_parent('section')
    if sec:
        sec.append(bs4.BeautifulSoup(cta_html, 'html.parser').div)

# 2. Como funciona
h2_funciona = soup.find(lambda tag: tag.name == 'h2' and 'Como funciona' in tag.text)
if h2_funciona:
    sec = h2_funciona.find_parent('section')
    if sec:
        wrap = sec.find('div', class_='wrap')
        cta_contato_html = '<div style="margin-top:var(--e6); text-align: center; width: 100%;"><a class="btn btn--zap" href="https://wa.me/5519920009231" rel="noopener" target="_blank">Entrar em Contato</a></div>'
        (wrap if wrap else sec).append(bs4.BeautifulSoup(cta_contato_html, 'html.parser').div)

# 3. Depoimentos
h2_depo = soup.find(lambda tag: tag.name == 'h2' and 'O que dizem' in tag.text)
if h2_depo:
    sec = h2_depo.find_parent('section')
    if sec:
        wrap = sec.find('div', class_='wrap')
        (wrap if wrap else sec).append(bs4.BeautifulSoup(cta_html, 'html.parser').div)

# 4. FAQ
div_faq = soup.find('div', class_='faq')
if div_faq:
    # Append after the faq div, inside the grudado wrap
    wrap = div_faq.find_parent('div', class_='wrap')
    if wrap:
        wrap.append(bs4.BeautifulSoup(cta_html, 'html.parser').div)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(str(soup))
