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
head = head.replace('href="/assets', 'href="/assets') # No change since it's absolute now

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

def assemble_page(content_html, title_meta, desc_meta):
    page_head = head.replace('<title>Terapeuta TRG Online | Valéria Godoy</title>', f'<title>{title_meta}</title>')
    page_head = page_head.replace('<meta name="description" content="Conheça Valéria Godoy, terapeuta emocional com atendimento em Terapia TRG online. Saiba como funciona e agende uma conversa.">', f'<meta name="description" content="{desc_meta}">')
    
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

# --- Base Service template ---
servico_match = re.search(r'(<div class="pagina[^"]*" id="p-servico">.*?</div>\s*<!-- =+)', html, re.DOTALL)
if not servico_match:
    servico_match = re.search(r'(<div class="pagina[^"]*" id="p-servico">.*)</div>', html, re.DOTALL)
s_base = servico_match.group(1) if servico_match else ''
s_base = s_base.replace('class="pagina"', 'class="pagina ativa" style="display:block;"')
s_base = s_base.replace('href="#home"', 'href="/"')
s_base = s_base.replace('href="#contato"', 'href="/contato"')
s_base = s_base.replace('data-ir="home"', '')
s_base = s_base.replace('data-ir="contato"', '')
s_base = s_base.replace('https://wa.me/5519999999999', 'https://wa.me/5519920009231')
s_base = s_base.replace('Medo de dirigir', 'Serviços')

# Custom content area (between buttons and FAQ)
def build_servico(title_short, title, abertura, content_html, faq_html, file_path):
    s_html = s_base
    s_html = s_html.replace('Amaxofobia', title_short)
    s_html = s_html.replace('Tratamento para medo de dirigir', title)
    s_html = s_html.replace('Para quem tem CNH válida e mesmo assim não sai da garagem — e para quem dirige, mas só na rua de casa, só de dia, só sem passageiro.', abertura)
    
    # Replace content between buttons and FAQ
    content_area = re.search(r'</a>\s*</div>\s*<h2 style="margin-top:var\(--e7\)">Como isso costuma aparecer</h2>(.*?)<div class="faq" style="margin-top:var\(--e7\)">', s_html, re.DOTALL)
    if content_area:
        s_html = s_html.replace(content_area.group(1), f"\n{content_html}\n")
    
    # Replace FAQ
    faq_area = re.search(r'<div class="faq" style="margin-top:var\(--e7\)">\s*<h2>Perguntas sobre esse atendimento</h2>(.*?)</div>\s*</div>\s*<aside class="grudado">', s_html, re.DOTALL)
    if faq_area:
        s_html = s_html.replace(faq_area.group(1), f"\n{faq_html}\n")
        
    s_html = s_html.replace('<h2 style="margin-top:var(--e7)">Como isso costuma aparecer</h2>', '')
    
    final_html = assemble_page(s_html, f'{title} | Valéria Godoy', abertura)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_html)

s1_content = """
<h2 style="margin-top:var(--e7)">O que é o reprocessamento de traumas e fobias?</h2>
<p>O reprocessamento busca trabalhar questões emocionais ligadas a experiências dolorosas. A abordagem utiliza um protocolo organizado em etapas. Não exige necessariamente que o cliente conte todos os detalhes, e o processo respeita seu conforto.</p>
<h2 style="margin-top:var(--e7)">Como funciona o atendimento?</h2>
<ol class="etapas" style="margin-top:var(--e5)">
    <li><h4>Conversa inicial</h4><p>Compreensão do seu momento e do que levou você a procurar apoio.</p></li>
    <li><h4>Conhecimento</h4><p>Explicações sobre a metodologia TRG.</p></li>
    <li><h4>Trabalho terapêutico</h4><p>Sessões estruturadas, com atenção à carga emocional no seu ritmo.</p></li>
</ol>
"""
s1_faq = """
<details open><summary>Preciso contar todos os detalhes do trauma?<span class="sinal" aria-hidden="true"></span></summary><div class="faq__corpo"><p>Não. A metodologia não exige que você reviva todos os detalhes no discurso.</p></div></details>
<details><summary>Pode ajudar em casos de fobia?<span class="sinal" aria-hidden="true"></span></summary><div class="faq__corpo"><p>Sim. Trabalhamos os medos persistentes a partir de uma abordagem estruturada.</p></div></details>
"""
build_servico("Traumas e Fobias", "Reprocessamento de Traumas", "Um espaço para trabalhar experiências que ainda despertam sofrimento.", s1_content, s1_faq, "build/servicos/reprocessamento-de-traumas-e-fobias.html")

s2_content = """
<h2 style="margin-top:var(--e7)">O que é esse atendimento?</h2>
<p>A Terapia TRG utiliza um protocolo estruturado para trabalhar questões e padrões emocionais. No atendimento voltado à ansiedade, o foco é compreender o que a pessoa vivencia.</p>
<h2 style="margin-top:var(--e7)">Para quem pode ser indicado?</h2>
<ul>
    <li>Vivenciam preocupação excessiva</li>
    <li>Enfrentam episódios de medo intenso ou pânico</li>
    <li>Sentem que questões emocionais interferem na rotina</li>
</ul>
"""
s2_faq = """
<details open><summary>A Terapia TRG é indicada para ansiedade?<span class="sinal" aria-hidden="true"></span></summary><div class="faq__corpo"><p>Sim, ajuda na regulação emocional e no reprocessamento dos gatilhos da ansiedade.</p></div></details>
<details><summary>Preciso parar meu tratamento médico?<span class="sinal" aria-hidden="true"></span></summary><div class="faq__corpo"><p>De forma alguma. Atua como complementar. Nunca interrompa medicação sem orientação.</p></div></details>
"""
build_servico("Ansiedade", "Terapia para Ansiedade e Síndrome do Pânico", "Acolhimento para quem enfrenta ansiedade e crises de pânico.", s2_content, s2_faq, "build/servicos/terapia-para-ansiedade-e-sindrome-do-panico.html")

s3_content = """
<h2 style="margin-top:var(--e7)">O que é o atendimento para depressão e vazio existencial?</h2>
<p>O atendimento pode ser procurado por pessoas que vivenciam sofrimento relacionado a perdas, lutos ou sentimentos de vazio. A Terapia TRG não deve substituir acompanhamento psiquiátrico quando necessário.</p>
"""
s3_faq = """
<details open><summary>A terapia pode ajudar com o vazio existencial?<span class="sinal" aria-hidden="true"></span></summary><div class="faq__corpo"><p>Sim. Oferecemos um espaço de escuta para ajudar a reencontrar um equilíbrio.</p></div></details>
<details><summary>Preciso de diagnóstico para buscar atendimento?<span class="sinal" aria-hidden="true"></span></summary><div class="faq__corpo"><p>Não é necessário. Você pode iniciar as sessões e se for indicado faremos encaminhamentos.</p></div></details>
"""
build_servico("Depressão", "Terapia para Depressão e Vazio Existencial", "Um espaço de acolhimento para momentos de sofrimento e falta de sentido.", s3_content, s3_faq, "build/servicos/terapia-para-depressao-e-vazio-existencial.html")


# --- BLOG SUBPAGES (Using p-sobre as a template since blog single is not provided) ---
sobre_match = re.search(r'(<div class="pagina[^"]*" id="p-sobre">.*?</div>\s*<!-- =+)', html, re.DOTALL)
if not sobre_match:
    sobre_match = re.search(r'(<div class="pagina[^"]*" id="p-sobre">.*)</div>', html, re.DOTALL)
b_base = sobre_match.group(1) if sobre_match else ''
b_base = b_base.replace('class="pagina"', 'class="pagina ativa" style="display:block;"')
b_base = b_base.replace('href="#home"', 'href="/"')
b_base = b_base.replace('href="#contato"', 'href="/contato"')
b_base = b_base.replace('href="#blog"', 'href="/blog"')
b_base = b_base.replace('data-ir="home"', '')
b_base = b_base.replace('data-ir="contato"', '')
b_base = b_base.replace('data-ir="blog"', '')
b_base = b_base.replace('https://wa.me/5519999999999', 'https://wa.me/5519920009231')

def build_blog(title, content, date, file_path, img):
    b_html = b_base
    b_html = b_html.replace('Sobre', 'Blog')
    b_html = b_html.replace('Sobre mim', date)
    b_html = b_html.replace('Renata Salvetti', title)
    b_html = b_html.replace('Terapeuta TRG há dez anos, em Santa Bárbara d\'Oeste. Atendo adultos que já tentaram resolver no entendimento e continuam travando na hora.', '')
    
    # Replace content between abertura and aside
    content_area = re.search(r'(<p class="abertura".*?)</div>\s*<aside class="grudado">', b_html, re.DOTALL)
    if content_area:
        b_html = b_html.replace(content_area.group(1), f"{content}\n      </div>\n")
        
    b_html = b_html.replace('<div class="hero__retrato" style="aspect-ratio:3/4"><span>Retrato profissional — 900×1200px</span></div>', f'<div class="hero__retrato" style="aspect-ratio:3/4"><img src="{img}?v=4" style="width:100%; height:100%; object-fit:cover;"></div>')
    
    final_html = assemble_page(b_html, f'{title} | Valéria Godoy', 'Artigo do blog')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_html)

b1 = """
<p class="abertura" style="font-size:var(--t-lg)">A Terapia de Reprocessamento Generativo (TRG) é uma metodologia terapêutica projetada para resolver questões emocionais profundas, como traumas, fobias, compulsões, depressão e ansiedade.</p>

<p>Reconhecida pelo MEC e amplamente apoiada pelo CITRG – Conselho Internacional de Terapia de Reprocessamento Generativo, com seu Código de Ética e Disciplina Profissional.</p>

<h2 style="margin-top:var(--e7)">Como a TRG atua?</h2>
<p>A TRG, ao contrário das terapias tradicionais, não depende exclusivamente de discussões verbais, mas trabalha diretamente com o inconsciente para acessar e reprocessar memórias emocionais armazenadas. Esse método permite transformar experiências negativas em lições positivas, melhorando o bem-estar psicológico e emocional dos clientes.</p>

<h2 style="margin-top:var(--e7)">As 5 etapas da TRG</h2>
<p>O método funciona através de cinco passos estruturados e eficazes para libertar amarras emocionais:</p>
<ul style="list-style: none; padding: 0; margin-top: 1.5rem; display: flex; flex-direction: column; gap: 1rem;">
    <li><b style="color: #f76b59;">1. Cronológico:</b> Explora a linha do tempo da sua vida, identificando eventos e traumas passados que influenciam o presente.</li>
    <li><b style="color: #8c2844;">2. Somático:</b> Trabalha as sensações e tensões físicas do corpo relacionadas às emoções não processadas.</li>
    <li><b style="color: #f19a38;">3. Temático:</b> Reprocessa temas recorrentes e padrões de comportamento indesejados em diferentes áreas da vida.</li>
    <li><b style="color: #63a8e1;">4. Futuro:</b> Libera ansiedades e preocupações sobre o futuro, construindo novas perspectivas positivas.</li>
    <li><b style="color: #8cd6a5;">5. Potencialização:</b> Ativa e fortalece os seus recursos internos, habilidades e o seu máximo potencial.</li>
</ul>

<h2 style="margin-top:var(--e7)">Para quem é indicada e quais as suas vantagens?</h2>
<p>Por ser uma terapia breve, a TRG foca em resolver o problema de forma efetiva. É indicada para todas as faixas etárias e trata com sucesso síndromes de pânico, ansiedade severa, fobias, traumas emocionais profundos, luto não resolvido e casos de depressão.</p>

<h2 style="margin-top:var(--e7)">Cuidados ao escolher um atendimento</h2>
<p>É vital certificar-se de que o profissional é registrado no conselho internacional de TRG (CITRG). Vale lembrar que, embora extremamente poderosa no trabalho das dores emocionais, em casos de emergência psiquiátrica ou necessidades clínicas, a terapia não substitui o acompanhamento de médicos ou psiquiatras, mas funciona maravilhosamente bem de maneira complementar.</p>
"""
build_blog("O que é Terapia TRG?", b1, "15 Set 2026", "build/blog/o-que-e-terapia-trg.html", "/assets/img/blog-1.jpg")

b2 = """
<p class="abertura" style="font-size:var(--t-lg)">A ansiedade pode estar relacionada a diferentes experiências e situações. Quando o sofrimento interfere na vida cotidiana, buscar informações e apoio profissional pode ajudar a compreender as possibilidades de cuidado.</p>

<h2 style="margin-top:var(--e7)">O que é ansiedade e quando ela interfere na rotina?</h2>
<p>A ansiedade é uma reação natural do corpo ao perigo ou ao estresse. No entanto, ela se torna disfuncional quando paralisa suas ações, rouba seu sono ou gera medos constantes de situações corriqueiras. Se a preocupação dita as regras do seu dia a dia, é o momento de buscar ajuda.</p>

<h2 style="margin-top:var(--e7)">Como a Terapia TRG trabalha questões emocionais?</h2>
<p>Na TRG, não focamos apenas em entender racionalmente a ansiedade, mas em ir à origem do registro traumático que deixa o cérebro em "estado de alerta" constante. Reprocessamos as memórias associadas para que a carga emocional perca a força.</p>

<h2 style="margin-top:var(--e7)">Como funciona uma sessão online para ansiedade?</h2>
<p>A sessão online para ansiedade segue as mesmas regras do presencial: é um espaço de escuta ativa. O terapeuta guiará você por um protocolo mental seguro. Se a crise apertar, há espaço para pausas. Você controla o ritmo enquanto avançamos nas raízes do problema.</p>

<h2 style="margin-top:var(--e7)">A importância da avaliação médica e psicológica</h2>
<p>Embora a TRG tenha foco rápido e traga muito alívio para dores emocionais, sintomas físicos e neurológicos severos da ansiedade (como o pânico extremo) muitas vezes precisam de regulação química inicial. Procurar suporte psiquiátrico paralelo à TRG acelera a retomada do bem-estar.</p>
"""
build_blog("Terapia TRG para ansiedade", b2, "10 Set 2026", "build/blog/terapia-trg-para-ansiedade.html", "/assets/img/blog-2.jpg")

b3 = """
<p class="abertura" style="font-size:var(--t-lg)">A depressão é uma condição que exige atenção e avaliação adequada. Antes de buscar qualquer modalidade de terapia, é importante compreender as possibilidades de cuidado e a importância de um acompanhamento compatível com as necessidades de cada pessoa.</p>

<h2 style="margin-top:var(--e7)">O que é depressão e como o sofrimento se manifesta?</h2>
<p>A depressão é mais do que tristeza passageira; é uma ausência prolongada de energia, perda de sentido e, muitas vezes, um cansaço inexplicável frente à vida. Ela pode se manifestar em dores físicas, insônia, excesso de sono, ou como uma sensação crônica de apatia e vazio existencial.</p>

<h2 style="margin-top:var(--e7)">Por que a avaliação adequada é importante?</h2>
<p>Porque o sofrimento emocional severo afeta a química do cérebro. Para tratar as feridas mais profundas da mente, o corpo também precisa de atenção. Por isso, a avaliação médica correta é o primeiro e mais importante passo, garantindo que o cérebro tenha estrutura para reagir ao tratamento terapêutico.</p>

<h2 style="margin-top:var(--e7)">Como a TRG atua nas questões emocionais?</h2>
<p>A Terapia de Reprocessamento Generativo busca encontrar onde a energia vital foi "congelada" por traumas do passado. Ajudamos a limpar o arquivo emocional acumulado na infância e nas experiências dolorosas, reduzindo a bagagem de dor que pesa na sua rotina hoje.</p>

<h2 style="margin-top:var(--e7)">A importância do acompanhamento em conjunto</h2>
<p>Se você está enfrentando a depressão, não faça isso sozinho e não dispense a medicina tradicional. A TRG trabalha nas emoções estagnadas, mas não substitui psicólogos ou psiquiatras. O melhor resultado sempre nasce do cuidado integrado.</p>
"""
build_blog("Terapia TRG para depressão", b3, "05 Set 2026", "build/blog/terapia-trg-para-depressao.html", "/assets/img/blog-3.jpg")

print("Serviços e Blog Subpages reconstruídos com fidelidade perfeita.")
