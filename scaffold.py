import os

base_html = '''<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- Google Consent Mode v2 -->
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('consent', 'default', {{
      'ad_storage': 'denied',
      'ad_user_data': 'denied',
      'ad_personalization': 'denied',
      'analytics_storage': 'denied'
    }});
  </script>
  <!-- Global site tag (gtag.js) - Google Analytics -->
  <!-- <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-XXXXXXXXXX');
  </script> -->

  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Karla:wght@400;500;700&display=swap" rel="stylesheet">

  <!-- CSS Custom & Tailwind -->
  <link rel="stylesheet" href="/assets/css/style-v2.css?v=8">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            primary: '#A9D6F2',
            secondary: '#3175B9',
            gold: '#C9A227',
            navy: '#1F5482'
          }},
          fontFamily: {{
            fraunces: ['Fraunces', 'serif'],
            karla: ['Karla', 'sans-serif']
          }}
        }}
      }}
    }}
  </script>
  <!-- Alpine.js -->
  <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
</head>
<body class="bg-white text-[#3E5163] font-karla" x-data="{{ menuOpen: false }}">

  <!-- Header -->
  <header class="fixo bg-white/90 backdrop-blur border-b border-[#EAF3FB] z-50">
    <div class="wrap nav">
      <a class="marca" href="/">
        <span class="marca__sigla bg-navy text-[#C9A227]" aria-hidden="true">VG</span>
        <span>
          <span class="marca__nome text-navy">Valéria Godoy</span>
          <span class="marca__papel">Terapeuta TRG · Santa Bárbara d'Oeste</span>
        </span>
      </a>
      
      <!-- Desktop Nav -->
      <nav class="hidden md:flex gap-6 items-center">
        <a href="/" class="text-sm font-medium hover:text-[#2A6BA0]">Início</a>
        <a href="/servicos" class="text-sm font-medium hover:text-[#2A6BA0]">Serviços</a>
        <a href="/sobre" class="text-sm font-medium hover:text-[#2A6BA0]">Sobre</a>
        <a href="/blog" class="text-sm font-medium hover:text-[#2A6BA0]">Blog</a>
        <a href="/contato" class="text-sm font-medium hover:text-[#2A6BA0]">Contato</a>
      </nav>

      <a class="btn btn--secundario hidden md:inline-flex" href="https://wa.me/5519920009231" target="_blank">WhatsApp</a>
      
      <!-- Mobile Toggle -->
      <button @click="menuOpen = true" class="md:hidden p-2" aria-label="Abrir menu">
        <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>
    </div>
  </header>

  <!-- Gaveta Mobile -->
  <div x-show="menuOpen" style="display: none;" class="fixed inset-0 z-[100] bg-white flex flex-col p-6" x-transition>
    <div class="flex justify-between items-center mb-8">
      <span class="font-fraunces text-navy text-xl">Menu</span>
      <button @click="menuOpen = false" class="p-2"><svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6L6 18M6 6l12 12"/></svg></button>
    </div>
    <nav class="flex flex-col gap-6 text-lg">
      <a href="/">Início</a>
      <a href="/servicos">Serviços</a>
      <a href="/sobre">Sobre</a>
      <a href="/blog">Blog</a>
      <a href="/contato">Contato</a>
      <a href="https://wa.me/5519920009231" class="btn btn--primario text-center mt-4">Agendar avaliação</a>
    </nav>
  </div>

  <main class="pt-[72px]">
    {content}
  </main>

  <!-- Footer -->
  <footer class="footer bg-navy mt-16">
    <div class="wrap py-12">
      <div class="footer__grade">
        <div>
          <a class="marca mb-4 inline-flex" href="/">
            <span class="marca__sigla bg-white text-navy" aria-hidden="true">VG</span>
            <span>
              <span class="marca__nome text-white">Valéria Godoy</span>
              <span class="marca__papel text-white/80">Terapeuta TRG</span>
            </span>
          </a>
          <p class="text-sm text-white/80">Terapia de Reprocessamento Generativo para fobias, ansiedade, trauma e luto. Atendimento presencial no Centro de Santa Bárbara d'Oeste e online para todo o Brasil.</p>
        </div>
        <div>
          <h4 class="text-white">Atendimentos</h4>
          <ul class="footer__lista">
            <li><a href="/servicos/reprocessamento-de-traumas-e-fobias">Traumas e fobias</a></li>
            <li><a href="/servicos/terapia-para-ansiedade-e-sindrome-do-panico">Ansiedade e pânico</a></li>
            <li><a href="/servicos/terapia-para-depressao-e-vazio-existencial">Depressão e luto</a></li>
          </ul>
        </div>
        <div>
          <h4 class="text-white">Navegar</h4>
          <ul class="footer__lista">
            <li><a href="/">Início</a></li>
            <li><a href="/sobre">Sobre</a></li>
            <li><a href="/servicos">Serviços</a></li>
            <li><a href="/blog">Blog</a></li>
            <li><a href="/contato">Contato</a></li>
          </ul>
        </div>
        <div>
          <h4 class="text-white">Consultório</h4>
          <ul class="footer__lista text-white/80">
            <li>Rua Romeu Fornazzari, 120, Bloco F</li>
            <li>Dona Regina · Santa Bárbara d'Oeste – SP</li>
            <li><a href="https://wa.me/5519920009231" target="_blank">WhatsApp (19) 99200-0923</a></li>
            <li>Atendimento com horário agendado</li>
          </ul>
        </div>
      </div>
      <div class="footer__base border-t border-white/20 mt-12 pt-6 flex flex-col md:flex-row gap-4 justify-between text-sm text-white/60">
        <div style="display: flex; flex-direction: column; gap: 0.25rem;">
<span>© 2026 Valéria Godoy · Terapeuta TRG</span>
<span style="font-size: 0.85em; opacity: 0.8;">Site desenvolvido por <a href="https://aeawebstudio.com/" target="_blank" rel="noopener" style="text-decoration: underline;">A&Ä Studio</a></span>
</div>
        <span>A TRG é abordagem complementar e não substitui tratamento médico.</span>
        <span><a href="/privacidade">Política de privacidade</a></span>
      </div>
    </div>
  </footer>

  <!-- Barra Fixa Mobile (WhatsApp) -->
  <div class="md:hidden fixed bottom-0 left-0 w-full p-4 bg-white/90 backdrop-blur border-t border-[#EAF3FB] z-40">
    <a class="btn btn--zap btn--bloco" href="https://wa.me/5519920009231" target="_blank">
      Falar no WhatsApp agora
    </a>
  </div>

  <!-- LGPD Consent Banner -->
  <div id="lgpd-banner" class="fixed bottom-4 md:bottom-8 left-4 right-4 md:left-auto md:right-8 md:w-[400px] bg-white shadow-2xl rounded-lg p-5 z-[999] border border-gray-100 flex-col gap-4" style="display: none;">
    <p class="text-sm text-gray-600">Utilizamos cookies para melhorar sua experiência, analisar o tráfego e personalizar conteúdo. Ao continuar, você concorda com nossa <a href="/privacidade" class="text-secondary underline">Política de Privacidade</a>.</p>
    <div class="flex gap-3 mt-3">
      <button id="btn-accept-cookies" class="btn btn--primario flex-1 text-sm">Aceitar</button>
      <button id="btn-reject-cookies" class="btn btn--secundario flex-1 text-sm">Recusar</button>
    </div>
  </div>

  <script src="/assets/js/script.js"></script>
</body>
</html>
'''

pages = {
    'index.html': {'title': 'Terapeuta TRG Online | Valéria Godoy', 'description': 'Conheça Valéria Godoy, terapeuta emocional com atendimento em Terapia TRG online.', 'content': '<!-- HOME CONTENT HERE -->'},
    'sobre.html': {'title': 'Valéria Godoy: Terapeuta Emocional e Terapeuta TRG', 'description': 'Conheça Valéria Godoy e a Terapia TRG.', 'content': '<!-- SOBRE CONTENT HERE -->'},
    'servicos.html': {'title': 'Terapia TRG: Serviços de Atendimento Emocional', 'description': 'Veja os serviços de Terapia TRG.', 'content': '<!-- SERVICOS CONTENT HERE -->'},
    'contato.html': {'title': 'Fale com Valéria Godoy, Terapeuta TRG', 'description': 'Entre em contato e agende sua avaliação.', 'content': '<!-- CONTATO CONTENT HERE -->'},
    'blog.html': {'title': 'Blog de Terapia Emocional e Reprocessamento', 'description': 'Artigos sobre saúde emocional, TRG e bem-estar.', 'content': '<!-- BLOG CONTENT HERE -->'},
    'faq.html': {'title': 'Dúvidas Frequentes - Valéria Godoy', 'description': 'Principais dúvidas sobre a TRG e atendimentos.', 'content': '<!-- FAQ CONTENT HERE -->'},
    'privacidade.html': {'title': 'Política de Privacidade', 'description': 'Termos e políticas de privacidade.', 'content': '<!-- PRIVACIDADE CONTENT HERE -->'},
    '404.html': {'title': 'Página não encontrada', 'description': 'Erro 404', 'content': '<div class="wrap text-center py-20"><h1>404 - Página não encontrada</h1><a href="/" class="btn btn--primario mt-4">Voltar ao início</a></div>'}
}

# Subpages structure
subpages_servicos = [
    'reprocessamento-de-traumas-e-fobias.html',
    'terapia-para-ansiedade-e-sindrome-do-panico.html',
    'terapia-para-depressao-e-vazio-existencial.html'
]
subpages_blog = [
    'o-que-e-terapia-trg.html',
    'terapia-trg-para-ansiedade.html',
    'terapia-trg-para-depressao.html'
]

for filename, data in pages.items():
    html = base_html.format(**data)
    with open(f'build/{filename}', 'w', encoding='utf-8') as f:
        f.write(html)

for slug in subpages_servicos:
    html = base_html.format(title='Serviço | Valéria Godoy', description='Serviço TRG', content='<!-- SERVICO CONTENT HERE -->')
    with open(f'build/servicos/{slug}', 'w', encoding='utf-8') as f:
        f.write(html)

for slug in subpages_blog:
    html = base_html.format(title='Blog | Valéria Godoy', description='Artigo TRG', content='<!-- BLOG POST CONTENT HERE -->')
    with open(f'build/blog/{slug}', 'w', encoding='utf-8') as f:
        f.write(html)

print('All base HTML files generated successfully.')
