import os
import re

# Read reference HTML
with open('04-referencia-visual/home.html', 'r', encoding='utf-8') as f:
    html = f.read()

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

footer = re.sub(r'<a class="marca".*?</a>', logo_html, footer, flags=re.DOTALL)

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

def assemble_page(content_html, title_meta, desc_meta, base_folder='build'):
    page_head = head.replace('<title>Terapeuta TRG Online | Valéria Godoy</title>', f'<title>{title_meta}</title>')
    page_head = page_head.replace('<meta name="description" content="Conheça Valéria Godoy, terapeuta emocional com atendimento em Terapia TRG online. Saiba como funciona e agende uma conversa.">', f'<meta name="description" content="{desc_meta}">')
    
    if base_folder != 'build':
        page_head = page_head.replace('href="/assets', 'href="/assets')

    final_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
{page_head}
<body>
<a class="pular" href="#conteudo">Ir para o conteúdo</a>
{header}
<main id="conteudo">
{content_html}
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

# ---------------- FAQ.HTML (Extracting from HOME) ----------------
faq_section = re.search(r'(<section class="bloco bloco--curto bloco--bege">.*?)</section>', html, re.DOTALL)
if faq_section:
    f_html = faq_section.group(1) + "</section>"
    f_html = f"""<div class="pagina ativa" style="display:block; padding-top:var(--e5)">
<p class="migalha wrap"><a href="/">Início</a> › Dúvidas</p>
{f_html}
</div>"""
    f_html = f_html.replace('href="#contato"', 'href="/contato"')
    final_faq = assemble_page(f_html, 'Dúvidas Frequentes | Valéria Godoy', 'Tire suas dúvidas sobre o atendimento de Terapia TRG com Valéria Godoy.')
    with open('build/faq.html', 'w', encoding='utf-8') as f:
        f.write(final_faq)

# ---------------- BLOG.HTML ----------------
blog_match = re.search(r'(<div class="pagina[^"]*" id="p-blog">.*?</div>\s*<!-- =+)', html, re.DOTALL)
if not blog_match:
    blog_match = re.search(r'(<div class="pagina[^"]*" id="p-blog">.*)</div>', html, re.DOTALL)
b_html = blog_match.group(1) if blog_match else ''
b_html = b_html.replace('class="pagina"', 'class="pagina ativa" style="display:block;"')
b_html = b_html.replace('href="#home"', 'href="/"')
b_html = b_html.replace('href="#contato"', 'href="/contato"')
b_html = b_html.replace('data-ir="home"', '')
b_html = b_html.replace('data-ir="contato"', '')
b_html = b_html.replace('https://wa.me/5519999999999', 'https://wa.me/5519920009231')

b_html = b_html.replace('href="#blog"', 'href="/blog/o-que-e-terapia-trg"', 1)
b_html = b_html.replace('href="#blog"', 'href="/blog/terapia-trg-para-ansiedade"', 1)
b_html = b_html.replace('href="#blog"', 'href="/blog/terapia-trg-para-depressao"', 1)

final_blog = assemble_page(b_html, 'Blog | Valéria Godoy', 'Textos sobre ansiedade, medos e Terapia TRG.')
with open('build/blog.html', 'w', encoding='utf-8') as f:
    f.write(final_blog)

print("FAQ e Blog gerados.")
