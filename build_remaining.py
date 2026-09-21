import re

servicos_list_content = """
<!-- ======================= SERVIÇOS (LISTA) ======================= -->
<div class="pagina ativa" id="p-servicos">
  <section class="wrap bloco pt-16">
    <p class="text-sm text-gray-500 mb-8"><a href="/" class="hover:text-secondary">Início</a> › Serviços</p>
    
    <div class="text-center max-w-2xl mx-auto mb-16">
      <div class="trilho justify-center"><span>Terapia TRG: Serviços de Atendimento Emocional</span></div>
      <h1 class="mb-6">Encontre um atendimento alinhado ao seu momento</h1>
      <p class="text-lg text-gray-600 mb-6">A Terapia de Reprocessamento Generativo (TRG) é uma abordagem estruturada para trabalhar questões emocionais, experiências dolorosas e padrões que podem continuar influenciando a vida cotidiana.</p>
      <p>Conheça os serviços oferecidos por Valéria Godoy e encontre informações sobre cada área de atendimento. A indicação e a adequação da abordagem são avaliadas individualmente.</p>
    </div>

    <h2 class="font-fraunces text-navy text-2xl mb-8 text-center">Nossos serviços</h2>

    <div class="grade grade--3 mb-16">
      <article class="card bg-[#F9FAFD] border border-gray-100">
        <div class="card__topo mb-4">
          <span class="text-secondary block mb-3"><svg width="28" height="28" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></span>
          <h3 class="font-fraunces text-navy text-xl">Traumas, Fobias e Ansiedade</h3>
        </div>
        <p class="text-gray-700 mb-6 flex-grow">Trabalho terapêutico com a carga emocional associada a experiências dolorosas do passado, traumas, medos e fobias.</p>
        <a class="btn btn--secundario w-full text-center" href="/servicos/reprocessamento-de-traumas-e-fobias">Saiba mais sobre traumas e fobias</a>
      </article>

      <article class="card bg-[#F9FAFD] border border-gray-100">
        <div class="card__topo mb-4">
          <span class="text-secondary block mb-3"><svg width="28" height="28" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg></span>
          <h3 class="font-fraunces text-navy text-xl">Ansiedade e Síndrome do Pânico</h3>
        </div>
        <p class="text-gray-700 mb-6 flex-grow">Atendimento direcionado a adultos que enfrentam ansiedade e crises de pânico, com foco no trabalho emocional e na busca por maior estabilidade.</p>
        <a class="btn btn--secundario w-full text-center" href="/servicos/terapia-para-ansiedade-e-sindrome-do-panico">Conheça o atendimento</a>
      </article>

      <article class="card bg-[#F9FAFD] border border-gray-100">
        <div class="card__topo mb-4">
          <span class="text-secondary block mb-3"><svg width="28" height="28" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82zM7 7h.01"/></svg></span>
          <h3 class="font-fraunces text-navy text-xl">Depressão e Vazio Existencial</h3>
        </div>
        <p class="text-gray-700 mb-6 flex-grow">Acolhimento e trabalho terapêutico com sofrimento emocional, perdas, lutos não resolvidos e sentimentos de falta de sentido.</p>
        <a class="btn btn--secundario w-full text-center" href="/servicos/terapia-para-depressao-e-vazio-existencial">Conheça o atendimento</a>
      </article>
    </div>

    <div class="bg-[#EAF3FB] p-10 rounded-3xl text-center max-w-4xl mx-auto border border-white">
      <h3 class="font-fraunces text-navy text-2xl mb-4">Como escolher o serviço adequado?</h3>
      <p class="text-gray-700 mb-8 max-w-2xl mx-auto">Você não precisa definir sozinho qual atendimento é o mais indicado. Entre em contato para explicar o que está vivendo e conhecer a abordagem, os limites do atendimento e as possibilidades de acompanhamento.</p>
      
      <p class="mb-6">Valéria Godoy atende presencialmente e online para pessoas de qualquer lugar do mundo.</p>
      <a class="btn btn--zap inline-block" href="https://wa.me/5519920009231" target="_blank">Falar no WhatsApp</a>
    </div>
  </section>
</div>
"""

blog_list_content = """
<!-- ======================= BLOG ======================= -->
<div class="pagina ativa" id="p-blog">
  <section class="wrap bloco pt-16">
    <p class="text-sm text-gray-500 mb-8"><a href="/" class="hover:text-secondary">Início</a> › Blog</p>
    
    <div class="trilho"><span>Blog de Terapia Emocional e Reprocessamento</span></div>
    <h1 class="mb-6">Informação para compreender melhor suas questões emocionais</h1>
    <p class="text-lg text-gray-600 mb-4 max-w-3xl">O blog da Valéria Godoy Terapeuta Emocional reúne conteúdos sobre Terapia de Reprocessamento Generativo, questões emocionais e possibilidades de atendimento.</p>
    <p class="max-w-3xl mb-8">Aqui, você encontrará artigos explicativos sobre traumas, fobias, ansiedade, síndrome do pânico, depressão, luto, vazio existencial e terapia online. O objetivo é oferecer informação clara para quem deseja conhecer melhor esses temas e compreender quando pode ser importante buscar apoio profissional.</p>
    
    <div class="bg-yellow-50 text-yellow-800 p-4 rounded-xl text-sm mb-12 max-w-3xl border border-yellow-200">
      <strong>Aviso editorial:</strong> Os conteúdos do blog têm finalidade informativa e não substituem avaliação ou tratamento realizado por profissionais habilitados.
    </div>

    <h2 class="font-fraunces text-navy text-2xl mb-8">Conheça nossos artigos</h2>
    
    <div class="grade grade--3 mb-16">
      <article class="card border border-gray-100 flex flex-col hover:shadow-lg transition-shadow">
        <div class="w-full h-48 bg-[#EAF3FB] -mt-6 -mx-6 mb-6 rounded-t-[19px] overflow-hidden" style="background-image: url('/assets/img/blog-1.jpg'); background-size: cover; border-bottom: 2px solid #C9A227;"></div>
        <p class="text-xs text-gray-500 mb-2">15 Set 2026 · 6 min de leitura</p>
        <h3 class="font-fraunces text-navy text-lg mb-3">O que é Terapia TRG e como funciona o Reprocessamento Generativo?</h3>
        <p class="text-sm text-gray-600 mb-6 flex-grow">Entenda o conceito da TRG, sua proposta e como o processo estruturado é apresentado.</p>
        <a class="text-secondary font-semibold text-sm hover:underline" href="/blog/o-que-e-terapia-trg">Ler o artigo →</a>
      </article>

      <article class="card border border-gray-100 flex flex-col hover:shadow-lg transition-shadow">
        <div class="w-full h-48 bg-[#EAF3FB] -mt-6 -mx-6 mb-6 rounded-t-[19px] overflow-hidden" style="background-image: url('/assets/img/blog-2.jpg'); background-size: cover; border-bottom: 2px solid #C9A227;"></div>
        <p class="text-xs text-gray-500 mb-2">10 Set 2026 · 5 min de leitura</p>
        <h3 class="font-fraunces text-navy text-lg mb-3">Terapia TRG para ansiedade: como funciona o atendimento?</h3>
        <p class="text-sm text-gray-600 mb-6 flex-grow">Informações sobre ansiedade e o atendimento emocional com TRG.</p>
        <a class="text-secondary font-semibold text-sm hover:underline" href="/blog/terapia-trg-para-ansiedade">Ler o artigo →</a>
      </article>

      <article class="card border border-gray-100 flex flex-col hover:shadow-lg transition-shadow">
        <div class="w-full h-48 bg-[#EAF3FB] -mt-6 -mx-6 mb-6 rounded-t-[19px] overflow-hidden" style="background-image: url('/assets/img/blog-3.jpg'); background-size: cover; border-bottom: 2px solid #C9A227;"></div>
        <p class="text-xs text-gray-500 mb-2">05 Set 2026 · 7 min de leitura</p>
        <h3 class="font-fraunces text-navy text-lg mb-3">Terapia TRG para depressão: o que saber antes de buscar atendimento?</h3>
        <p class="text-sm text-gray-600 mb-6 flex-grow">Informações sobre sofrimento emocional, depressão e a importância da avaliação adequada.</p>
        <a class="text-secondary font-semibold text-sm hover:underline" href="/blog/terapia-trg-para-depressao">Ler o artigo →</a>
      </article>
    </div>
    
  </section>
</div>
"""

faq_content = """
<!-- ======================= FAQ ======================= -->
<div class="pagina ativa" id="p-faq">
  <section class="wrap bloco pt-16">
    <p class="text-sm text-gray-500 mb-8"><a href="/" class="hover:text-secondary">Início</a> › Dúvidas Frequentes</p>
    <div class="max-w-3xl mx-auto">
      <div class="trilho"><span>Dúvidas Frequentes</span></div>
      <h1 class="mb-12">Perguntas sobre a Terapia TRG e os atendimentos</h1>

      <div class="flex flex-col gap-4">
        <!-- FAQ Item -->
        <div x-data="{ open: false }" class="border-b border-gray-200 pb-4">
          <button @click="open = !open" class="flex justify-between w-full text-left font-fraunces text-navy text-lg">
            <span>O que é a Terapia TRG?</span>
            <span x-text="open ? '−' : '+'" class="text-[#C9A227] text-2xl"></span>
          </button>
          <div x-show="open" x-collapse class="mt-4 text-gray-700">
            A Terapia TRG, ou Terapia de Reprocessamento Generativo, é uma abordagem que trabalha questões emocionais por meio de um protocolo estruturado em etapas. O processo busca auxiliar o cliente no enfrentamento e no reprocessamento de experiências e padrões emocionais.
          </div>
        </div>
        <div x-data="{ open: false }" class="border-b border-gray-200 pb-4">
          <button @click="open = !open" class="flex justify-between w-full text-left font-fraunces text-navy text-lg">
            <span>Como funciona uma sessão de Terapia TRG?</span>
            <span x-text="open ? '−' : '+'" class="text-[#C9A227] text-2xl"></span>
          </button>
          <div x-show="open" x-collapse class="mt-4 text-gray-700">
            As sessões seguem uma metodologia estruturada, considerando o histórico e as necessidades individuais do cliente. A terapeuta orienta o processo de acordo com a abordagem TRG, com acolhimento e respeito ao ritmo de cada pessoa.
          </div>
        </div>
        <div x-data="{ open: false }" class="border-b border-gray-200 pb-4">
          <button @click="open = !open" class="flex justify-between w-full text-left font-fraunces text-navy text-lg">
            <span>A Terapia TRG é indicada para quem tem traumas e fobias?</span>
            <span x-text="open ? '−' : '+'" class="text-[#C9A227] text-2xl"></span>
          </button>
          <div x-show="open" x-collapse class="mt-4 text-gray-700">
            A TRG pode ser procurada por adultos que desejam trabalhar experiências traumáticas, medos e fobias. A avaliação inicial ajuda a compreender as necessidades do cliente e a adequação do atendimento.
          </div>
        </div>
        <div x-data="{ open: false }" class="border-b border-gray-200 pb-4">
          <button @click="open = !open" class="flex justify-between w-full text-left font-fraunces text-navy text-lg">
            <span>A Terapia TRG pode ajudar em casos de ansiedade e síndrome do pânico?</span>
            <span x-text="open ? '−' : '+'" class="text-[#C9A227] text-2xl"></span>
          </button>
          <div x-show="open" x-collapse class="mt-4 text-gray-700">
            A abordagem é procurada por pessoas que enfrentam ansiedade e crises de pânico. A indicação e os limites do atendimento devem ser avaliados individualmente, e casos de maior gravidade podem exigir acompanhamento de profissionais habilitados em saúde mental.
          </div>
        </div>
        <div x-data="{ open: false }" class="border-b border-gray-200 pb-4">
          <button @click="open = !open" class="flex justify-between w-full text-left font-fraunces text-navy text-lg">
            <span>A Terapia TRG funciona para depressão e vazio existencial?</span>
            <span x-text="open ? '−' : '+'" class="text-[#C9A227] text-2xl"></span>
          </button>
          <div x-show="open" x-collapse class="mt-4 text-gray-700">
            A TRG pode ser buscada por pessoas que vivenciam sofrimento emocional, perdas e sentimentos de falta de sentido. Depressão exige avaliação adequada, e a terapia não deve substituir acompanhamento médico ou psicológico quando necessário.
          </div>
        </div>
        <div x-data="{ open: false }" class="border-b border-gray-200 pb-4">
          <button @click="open = !open" class="flex justify-between w-full text-left font-fraunces text-navy text-lg">
            <span>Como funciona a Terapia TRG online?</span>
            <span x-text="open ? '−' : '+'" class="text-[#C9A227] text-2xl"></span>
          </button>
          <div x-show="open" x-collapse class="mt-4 text-gray-700">
            O atendimento é realizado por meio de uma plataforma de comunicação à distância, permitindo sessões sem deslocamento até o consultório. É necessário ter privacidade, conexão estável e um ambiente adequado para o atendimento.
          </div>
        </div>
        <div x-data="{ open: false }" class="border-b border-gray-200 pb-4">
          <button @click="open = !open" class="flex justify-between w-full text-left font-fraunces text-navy text-lg">
            <span>Preciso reviver ou contar todos os detalhes de um trauma durante a sessão?</span>
            <span x-text="open ? '−' : '+'" class="text-[#C9A227] text-2xl"></span>
          </button>
          <div x-show="open" x-collapse class="mt-4 text-gray-700">
            A metodologia TRG possui um protocolo estruturado e não depende necessariamente de longos relatos detalhados de todas as experiências. A forma de condução deve respeitar os limites, o conforto e as necessidades individuais do cliente.
          </div>
        </div>
        <div x-data="{ open: false }" class="border-b border-gray-200 pb-4">
          <button @click="open = !open" class="flex justify-between w-full text-left font-fraunces text-navy text-lg">
            <span>Como agendar uma sessão com Valéria Godoy?</span>
            <span x-text="open ? '−' : '+'" class="text-[#C9A227] text-2xl"></span>
          </button>
          <div x-show="open" x-collapse class="mt-4 text-gray-700">
            O agendamento é realizado pelo WhatsApp. Basta clicar no botão de atendimento do site para entrar em contato com Valéria Godoy e consultar as informações sobre as sessões.
          </div>
        </div>
      </div>
      
      <div class="mt-12 text-center">
        <a class="btn btn--zap" href="https://wa.me/5519920009231" target="_blank">Agendar pelo WhatsApp</a>
      </div>
    </div>
  </section>
</div>
"""

privacidade_content = """
<!-- ======================= PRIVACIDADE ======================= -->
<div class="pagina ativa" id="p-privacidade">
  <section class="wrap bloco pt-16">
    <div class="max-w-3xl mx-auto">
      <h1 class="mb-8">Política de Privacidade</h1>
      <p class="mb-4">Este documento descreve como os seus dados pessoais são coletados, utilizados e protegidos durante o uso do site e o contato com a Valéria Godoy Terapeuta Emocional, em conformidade com a Lei Geral de Proteção de Dados Pessoais (LGPD – Lei nº 13.709/2018).</p>

      <h2 class="font-fraunces text-navy text-xl mt-8 mb-4">1. Quem é o controlador dos dados pessoais?</h2>
      <p class="mb-4">A responsável (controladora) pelas decisões referentes ao tratamento dos seus dados pessoais é Valéria Godoy. O contato para tratar sobre privacidade e dados pessoais pode ser feito através do e-mail ou WhatsApp informados no site.</p>

      <h2 class="font-fraunces text-navy text-xl mt-8 mb-4">2. Quais dados pessoais podem ser tratados?</h2>
      <p class="mb-4">O tratamento de dados ocorre conforme a sua interação com os serviços oferecidos. Podem ser coletados:</p>
      <ul class="list-disc pl-5 mb-4">
        <li><strong>Dados de Contato:</strong> Nome, telefone (WhatsApp) e e-mail, quando você inicia uma conversa para agendamento, informações ou dúvidas.</li>
        <li><strong>Dados Sensíveis:</strong> Informações sobre a saúde, estado emocional ou histórico pessoal que você decida compartilhar durante o contato inicial ou nas sessões terapêuticas.</li>
        <li><strong>Dados de Navegação (Cookies):</strong> Endereço IP, tipo de navegador, tempo de visita e páginas acessadas, coletados automaticamente por ferramentas analíticas para entender o uso do site.</li>
      </ul>

      <h2 class="font-fraunces text-navy text-xl mt-8 mb-4">3. Para quais finalidades os dados são utilizados?</h2>
      <p class="mb-4">Seus dados são tratados com base nas finalidades abaixo e nas bases legais previstas pela LGPD (como consentimento, tutela da saúde e execução de contrato):</p>
      <ul class="list-disc pl-5 mb-4">
        <li>Responder a mensagens, fornecer informações sobre o atendimento, agendar avaliações ou sessões.</li>
        <li>Conduzir o processo terapêutico (Terapia TRG) de forma adequada e individualizada, garantindo sigilo e respeito.</li>
        <li>Melhorar a experiência de navegação no site por meio de cookies analíticos e de funcionamento básico.</li>
      </ul>

      <h2 class="font-fraunces text-navy text-xl mt-8 mb-4">4. Como seus dados são protegidos?</h2>
      <p class="mb-4">As informações coletadas são tratadas com sigilo ético e medidas de segurança compatíveis com o padrão do atendimento terapêutico. Os dados não são vendidos, alugados ou compartilhados com terceiros para fins de marketing. O compartilhamento só ocorrerá se houver obrigação legal, determinação judicial ou necessidade vital para a sua segurança, conforme previsão ética.</p>

      <h2 class="font-fraunces text-navy text-xl mt-8 mb-4">5. Uso de Cookies e Google Consent Mode</h2>
      <p class="mb-4">O site utiliza cookies para entender como os visitantes interagem com as páginas. Atendendo às exigências de transparência, implementamos ferramentas de controle (Consent Mode) que permitem a você aceitar ou recusar o uso de cookies analíticos por meio do banner apresentado no rodapé do site.</p>
    </div>
  </section>
</div>
"""

def update_file(filepath, content, placeholder):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    html = html.replace(placeholder, content)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

update_file('build/servicos.html', servicos_list_content, '<!-- SERVICOS CONTENT HERE -->')
update_file('build/blog.html', blog_list_content, '<!-- BLOG CONTENT HERE -->')
update_file('build/faq.html', faq_content, '<!-- FAQ CONTENT HERE -->')
update_file('build/privacidade.html', privacidade_content, '<!-- PRIVACIDADE CONTENT HERE -->')

print("servicos.html, blog.html, faq.html, privacidade.html updated successfully.")
