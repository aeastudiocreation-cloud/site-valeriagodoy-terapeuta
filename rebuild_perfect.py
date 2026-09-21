import os
import re

# Read reference HTML
with open('04-referencia-visual/home.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract sections using regex
head_match = re.search(r'(<head>.*?</head>)', html, re.DOTALL)
head = head_match.group(1) if head_match else ''
head = head.replace('<title>Renata Salvetti · Terapeuta TRG em Santa Bárbara d\'Oeste</title>', '<title>Terapeuta TRG Online | Valéria Godoy</title>')
head = head.replace('<meta name="description" content="Atendimento em Terapia de Reprocessamento Generativo (TRG) em Santa Bárbara d\'Oeste – SP. Fobias, ansiedade, pânico, trauma e luto. Presencial no Centro e online.">', '<meta name="description" content="Conheça Valéria Godoy, terapeuta emocional com atendimento em Terapia TRG online. Saiba como funciona e agende uma conversa.">')

consent_mode = """
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('consent', 'default', {
  'ad_storage': 'denied',
  'ad_user_data': 'denied',
  'ad_personalization': 'denied',
  'analytics_storage': 'denied'
});
</script>
<link rel="stylesheet" href="/assets/css/style-v2.css?v=8">
"""
head = head.replace('</title>', '</title>\n' + consent_mode)
head = re.sub(r'<style>.*?</style>', '', head, flags=re.DOTALL)

# Header
header_match = re.search(r'(<header class="header">.*?</header>)', html, re.DOTALL)
header = header_match.group(1) if header_match else ''
header = header.replace('Renata Salvetti', 'Valéria Godoy')
header = header.replace('RS', 'VG')
header = header.replace('Terapeuta TRG · Santa Bárbara d\'Oeste', 'Terapeuta Emocional')
header = header.replace('https://wa.me/5519999999999', 'https://wa.me/5519920009231')
header = header.replace('Medo de dirigir', 'Serviços')
header = header.replace('#servico', '/servicos')
header = header.replace('#sobre', '/sobre')
header = header.replace('#blog', '/blog')
header = header.replace('#contato', '/contato')
header = header.replace('#home', '/')
header = header.replace('data-ir="home"', '')
header = header.replace('data-ir="servico"', '')
header = header.replace('data-ir="sobre"', '')
header = header.replace('data-ir="blog"', '')
header = header.replace('data-ir="contato"', '')
header = re.sub(r'<a href="#guia".*?Guia de estilo</a>', '', header)
header = header.replace('#guia', '')

logo_html = '<a class="marca" href="/" style="display:flex; align-items:center;"><img src="/assets/img/logo.png" alt="Valéria Godoy Logo" style="max-height: 80px; width: auto;"></a>'
header = re.sub(r'<a class="marca".*?</a>', logo_html, header, flags=re.DOTALL)

# Footer
footer_match = re.search(r'(<footer class="footer">.*?</footer>)', html, re.DOTALL)
footer = footer_match.group(1) if footer_match else ''
footer = footer.replace('Renata Salvetti', 'Valéria Godoy')
footer = footer.replace('RS', 'VG')
footer = footer.replace('https://wa.me/5519999999999', 'https://wa.me/5519920009231')
footer = footer.replace('(19) 99999-9999', '(19) 92000-9231')
footer = footer.replace('contato@renatasalvetti.com.br', 'contato@valeriagodoy.com.br')
footer = footer.replace('Rua do Comércio, 482 · sala 12', 'Rua Romeu Fornazzari, 120, Bloco F, Apto 303')
footer = footer.replace('Centro · Santa Bárbara d\'Oeste – SP', 'Bairro Dona Regina, Santa Bárbara d\'Oeste - SP')
footer = footer.replace('© 2026 Renata Salvetti', '© 2026 Valéria Godoy')
footer = footer.replace('#servico', '/servicos')
footer = footer.replace('#sobre', '/sobre')
footer = footer.replace('#blog', '/blog')
footer = footer.replace('#contato', '/contato')
footer = footer.replace('#home', '/')
footer = footer.replace('data-ir="home"', '')
footer = footer.replace('data-ir="servico"', '')
footer = footer.replace('data-ir="sobre"', '')
footer = footer.replace('data-ir="blog"', '')
footer = footer.replace('data-ir="contato"', '')
footer = re.sub(r'<li><a href="#guia".*?Guia de estilo</a></li>', '', footer)
footer = footer.replace("Atendimento presencial no Centro de Santa Bárbara d'Oeste e online para todo o Brasil.", "Atendimento online para todo o Brasil e exterior.")

footer = re.sub(r'<a class="marca".*?</a>', logo_html, footer, flags=re.DOTALL)

# Scripts
clean_scripts = """
<script src="/assets/js/script.js"></script>
<script>
  var btn = document.getElementById("menuBtn");
  var gaveta = document.getElementById("gaveta");
  function fecharGaveta(){
    gaveta.classList.remove("aberta");
    btn.setAttribute("aria-expanded","false");
  }
  btn.addEventListener("click", function(){
    var aberto = gaveta.classList.toggle("aberta");
    btn.setAttribute("aria-expanded", String(aberto));
  });
</script>
"""

lgpd_banner = """
<div id="lgpd-banner" style="display:none; position:fixed; bottom:0; left:0; right:0; background:#fff; border-top:1px solid #E7E1D8; padding:1.5rem; box-shadow:0 -6px 20px -14px rgba(15,36,48,.5); z-index:9999; flex-wrap:wrap; gap:1rem; align-items:center; justify-content:space-between;">
  <p style="margin:0; font-size:14px; max-width:800px; color:#3E5163;">Este site utiliza cookies para melhorar sua experiência. Ao continuar, você concorda com nossa Política de Privacidade.</p>
  <div style="display:flex; gap:0.5rem; flex-wrap:wrap;">
    <button id="btn-reject-cookies" class="btn btn--secundario btn--pequeno">Recusar</button>
    <button id="btn-accept-cookies" class="btn btn--primario btn--pequeno">Aceitar</button>
  </div>
</div>
"""

def build_page(page_id, title_meta, desc_meta, custom_replacements, base_folder='build'):
    page_match = re.search(rf'(<div class="pagina[^"]*" id="{page_id}">.*?</div>\s*<!-- =+)', html, re.DOTALL)
    if not page_match:
        page_match = re.search(rf'(<div class="pagina[^"]*" id="{page_id}">.*)</div>', html, re.DOTALL)
    
    page_content = page_match.group(1) if page_match else ''
    page_content = page_content.replace('class="pagina"', 'class="pagina ativa" style="display:block;"')
    page_content = page_content.replace('class="pagina ativa"', 'class="pagina ativa" style="display:block;"')
    
    page_content = page_content.replace('href="#servico"', 'href="/servicos"')
    page_content = page_content.replace('href="#sobre"', 'href="/sobre"')
    page_content = page_content.replace('href="#contato"', 'href="/contato"')
    page_content = page_content.replace('href="#blog"', 'href="/blog"')
    page_content = page_content.replace('href="#home"', 'href="/"')
    page_content = page_content.replace('data-ir="servico"', '')
    page_content = page_content.replace('data-ir="sobre"', '')
    page_content = page_content.replace('data-ir="contato"', '')
    page_content = page_content.replace('data-ir="blog"', '')
    page_content = page_content.replace('data-ir="home"', '')
    page_content = page_content.replace('https://wa.me/5519999999999', 'https://wa.me/5519920009231')

    for old, new in custom_replacements:
        page_content = page_content.replace(old, new)

    page_head = head.replace('<title>Terapeuta TRG Online | Valéria Godoy</title>', f'<title>{title_meta}</title>')
    page_head = page_head.replace('<meta name="description" content="Conheça Valéria Godoy, terapeuta emocional com atendimento em Terapia TRG online. Saiba como funciona e agende uma conversa.">', f'<meta name="description" content="{desc_meta}">')
    
    # adjust paths if building in subfolders
    if base_folder != 'build':
        page_head = page_head.replace('href="/assets', 'href="/assets')

    final_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
{page_head}
<body>
<a class="pular" href="#conteudo">Ir para o conteúdo</a>
{header}
<main id="conteudo">
{page_content}
</main>
{footer}
{lgpd_banner}
<div class="barra-zap">
  <a class="btn btn--zap btn--bloco" href="https://wa.me/5519920009231" target="_blank" rel="noopener">Falar no WhatsApp</a>
</div>
{clean_scripts}
</body>
</html>"""
    return final_html

# ---------------- HOME ----------------
home_replacements = []

home_html = build_page('p-home', 'Terapeuta TRG Online | Valéria Godoy', 'Conheça Valéria Godoy.', home_replacements)

# Swap Localização and Dúvidas
loc_match = re.search(r'(<section class="wrap bloco">\s*<div class="duas-colunas">\s*<div>\s*<div class="trilho"><span>Onde fica</span></div>.*?</section>)', home_html, re.DOTALL)
faq_match = re.search(r'(<section class="bloco bloco--curto bloco--bege">\s*<div class="wrap duas-colunas--esq duas-colunas">\s*<div class="grudado">\s*<div class="trilho"><span>Dúvidas</span></div>.*?</section>)', home_html, re.DOTALL)

if loc_match and faq_match:
    loc_html = loc_match.group(1)
    faq_html = faq_match.group(1)
    
    # Substituir no HTML
    home_html = home_html.replace(loc_html, '<!-- LOC_PLACEHOLDER -->')
    home_html = home_html.replace(faq_html, '<!-- FAQ_PLACEHOLDER -->')
    
    # Inverter
    home_html = home_html.replace('<!-- LOC_PLACEHOLDER -->', faq_html)
    home_html = home_html.replace('<!-- FAQ_PLACEHOLDER -->', loc_html)

with open('build/index.html', 'w', encoding='utf-8') as f:
    f.write(home_html)


# ---------------- SOBRE ----------------
sobre_replacements = []
sobre_html = build_page('p-sobre', 'Sobre Valéria Godoy', 'Saiba mais.', sobre_replacements)
with open('build/sobre.html', 'w', encoding='utf-8') as f:
    f.write(sobre_html)


# ---------------- CONTATO ----------------
contato_replacements = []
contato_html = build_page('p-contato', 'Contato e Agendamento', 'Entre em contato.', contato_replacements)

with open('build/contato.html', 'w', encoding='utf-8') as f:
    f.write(contato_html)


# ---------------- SERVICOS.HTML (Extracting from HOME) ----------------
servicos_section = re.search(r'(<section class="wrap bloco">\s*<div class="trilho"><span>Serviços</span></div>.*?</section>)', html, re.DOTALL)
if servicos_section:
    s_html = servicos_section.group(1)
    s_html = s_html.replace('href="/servicos"', 'href="/servicos"')
    
    s_html = f"""<div class="pagina ativa" style="display:block; padding-top:var(--e5)">
<p class="migalha wrap"><a href="/">Início</a> › Serviços</p>
{s_html}
</div>"""
    
    final_servicos = f"""<!DOCTYPE html>
<html lang="pt-BR">
{head.replace('<title>Terapeuta TRG Online | Valéria Godoy</title>', '<title>Serviços | Valéria Godoy</title>')}
<body>
<a class="pular" href="#conteudo">Ir para o conteúdo</a>
{header}
<main id="conteudo">
{s_html}
</main>
{footer}
{lgpd_banner}
<div class="barra-zap">
  <a class="btn btn--zap btn--bloco" href="https://wa.me/5519920009231" target="_blank" rel="noopener">Falar no WhatsApp</a>
</div>
{clean_scripts}
</body>
</html>"""
    with open('build/servicos.html', 'w', encoding='utf-8') as f:
        f.write(final_servicos)

print("Gerou home, sobre, contato e servicos. Continuar com FAQ e subpáginas no próximo.")
