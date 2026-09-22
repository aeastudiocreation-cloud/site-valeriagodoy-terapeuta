import re
import os

servico_template = """
<!-- ======================= SERVIÇO ======================= -->
<div class="pagina ativa">
  <section class="wrap bloco pt-16">
    <p class="text-sm text-gray-500 mb-8"><a href="/" class="hover:text-secondary">Início</a> › <a href="/servicos" class="hover:text-secondary">Serviços</a> › {title_short}</p>
    
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-16">
      <div class="lg:col-span-2">
        <div class="trilho"><span>{title_short}</span></div>
        <h1 class="mb-6">{title}</h1>
        <p class="abertura mb-8">{description}</p>

        {content_html}

        <h2 class="mt-12 mb-6 font-fraunces text-navy text-2xl">Perguntas frequentes</h2>
        <div class="flex flex-col gap-4 mb-8">
          {faq_html}
        </div>
      </div>

      <aside class="lg:col-span-1">
        <div class="sticky top-24">
          <div class="card bg-[#F9FAFD] border border-gray-100 shadow-sm p-6 rounded-2xl mb-8">
            <h3 class="font-fraunces text-navy text-xl" style="margin-bottom: 1.5rem;">Resumo prático</h3>
            <ul class="space-y-3 text-sm text-gray-700 mb-6">
              <li class="flex justify-between border-b border-gray-200 pb-2"><b>Formato:</b> <span>Online ou Presencial</span></li>
              <li class="flex justify-between border-b border-gray-200 pb-2"><b>Duração:</b> <span>Aprox. 60 min</span></li>
              <li class="flex justify-between border-b border-gray-200 pb-2"><b>Avaliação:</b> <span>Contato inicial via WhatsApp</span></li>
            </ul>
            <a class="btn btn--zap w-full text-center" href="https://wa.me/5519920009231" target="_blank">Tirar dúvida no WhatsApp</a>
            <p class="text-xs text-center text-gray-500 mt-3">Resposta em horário comercial</p>
          </div>
          
          <div class="bg-yellow-50 text-yellow-800 p-4 rounded-xl text-sm border border-yellow-200">
            <strong>Nota importante.</strong> A TRG é uma abordagem complementar. Se você já faz tratamento médico ou psiquiátrico, mantenha — meu trabalho soma, não substitui.
          </div>
        </div>
      </aside>
    </div>
  </section>

  <!-- CTA final -->
  <section class="wrap py-12">
    <div class="cta-final text-center md:text-left bg-navy text-white rounded-3xl p-10 flex flex-col md:flex-row items-center justify-between gap-8 relative overflow-hidden">
      <div class="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-[#B8860B] via-[#F3E0A1] to-[#9C7416]"></div>
      <div class="max-w-xl">
        <h2 class="text-white text-2xl font-fraunces mb-2">Vamos conversar?</h2>
        <p class="text-white/80 text-sm">Se você deseja conhecer o atendimento para {title_short}, fale com Valéria Godoy.</p>
      </div>
      <a class="btn btn--zap" href="https://wa.me/5519920009231" target="_blank">Falar com Valéria Godoy</a>
    </div>
  </section>
</div>
"""

blog_post_template = """
<!-- ======================= BLOG POST ======================= -->
<div class="pagina ativa">
  <section class="wrap bloco pt-16">
    <p class="text-sm text-gray-500 mb-8"><a href="/" class="hover:text-secondary">Início</a> › <a href="/blog" class="hover:text-secondary">Blog</a> › {title}</p>
    
    <div class="max-w-3xl mx-auto">
      <div class="text-sm text-gray-500 mb-4">{date}</div>
      <h1 class="mb-8">{title}</h1>
      
      <div class="w-full h-64 md:h-96 bg-[#EAF3FB] rounded-2xl overflow-hidden mb-12" style="background-image: url('{img_url}'); background-size: cover;"></div>

      <div class="bg-[#F9FAFD] p-6 rounded-2xl mb-12 border border-gray-100">
        <h3 class="font-fraunces text-navy text-lg mb-3">Índice</h3>
        <ul class="list-disc pl-5 text-sm text-secondary space-y-2">
          {toc_html}
        </ul>
      </div>

      <div class="prose max-w-none text-gray-700 space-y-6">
        {content_html}
      </div>

      <h2 class="mt-16 mb-6 font-fraunces text-navy text-2xl">Perguntas frequentes</h2>
      <div class="flex flex-col gap-4 mb-16">
        {faq_html}
      </div>

      <!-- Author Box -->
      <div class="bg-[#F9FAFD] border border-gray-100 rounded-2xl p-6 flex flex-col sm:flex-row gap-6 items-center sm:items-start mb-16">
        <div class="w-24 h-24 rounded-full bg-gray-200 overflow-hidden shrink-0" style="background-image: url('/assets/img/valeria-godoy-small.jpg'); background-size: cover;"></div>
        <div>
          <h3 class="font-fraunces text-navy text-xl">Valéria Godoy</h3>
          <p class="text-sm text-secondary mb-2">Terapeuta Emocional TRG</p>
          <p class="text-sm text-gray-600">Atua com atendimento em Terapia de Reprocessamento Generativo (TRG), oferecendo um espaço de acolhimento e acompanhamento individualizado para adultos que desejam trabalhar questões emocionais.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA final -->
  <section class="wrap pb-16">
    <div class="cta-final text-center bg-navy text-white rounded-3xl p-10 relative overflow-hidden max-w-3xl mx-auto">
      <div class="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-[#B8860B] via-[#F3E0A1] to-[#9C7416]"></div>
      <h2 class="text-white text-2xl font-fraunces mb-4">Deseja iniciar seu reprocessamento emocional?</h2>
      <p class="text-white/80 text-sm mb-8">O primeiro passo é uma conversa para entender o seu momento.</p>
      <a class="btn btn--zap inline-flex" href="https://wa.me/5519920009231" target="_blank">Falar com Valéria Godoy no WhatsApp</a>
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

# SERVICO 1: Traumas
s1 = servico_template.format(
    title_short="Traumas e Fobias",
    title="Reprocessamento de Traumas e Fobias com Terapia TRG",
    description="Um espaço para trabalhar experiências que ainda despertam sofrimento. Experiências dolorosas podem continuar influenciando a maneira como uma pessoa se sente, pensa e reage em determinadas situações.",
    content_html="""<h2 class="font-fraunces text-navy text-xl mt-8 mb-4">O que é o reprocessamento de traumas e fobias?</h2>
        <p class="mb-4">O reprocessamento de traumas e fobias, dentro da proposta de atendimento TRG, busca trabalhar questões emocionais relacionadas a experiências dolorosas, medos e fobias.</p>
        <p class="mb-4">A abordagem utiliza um protocolo organizado em etapas. A condução não exige necessariamente que o cliente conte todos os detalhes de uma experiência, e o processo deve respeitar seu conforto e seus limites.</p>
        <h2 class="font-fraunces text-navy text-xl mt-8 mb-4">Como funciona o atendimento?</h2>
        <ol class="list-decimal pl-5 space-y-4 text-gray-700">
          <li><strong>Conversa inicial:</strong> Você entra em contato e conhece as informações.</li>
          <li><strong>Compreensão do seu momento:</strong> A terapeuta busca entender quais questões estão levando você a procurar apoio.</li>
          <li><strong>Conhecimento da abordagem TRG:</strong> Você recebe explicações sobre a metodologia.</li>
          <li><strong>Trabalho terapêutico:</strong> As sessões seguem a abordagem TRG, com atenção à carga emocional e ao seu ritmo individual.</li>
        </ol>""",
    faq_html="""
        <div x-data="{ open: false }" class="border-b border-gray-200 pb-4">
          <button @click="open = !open" class="flex justify-between w-full text-left font-fraunces text-navy text-lg"><span>Preciso contar todos os detalhes do trauma?</span><span x-text="open ? '−' : '+'" class="text-[#C9A227] text-2xl"></span></button>
          <div x-show="open" x-collapse class="mt-4 text-gray-700">A metodologia TRG não exige que você reviva todos os detalhes no discurso. O foco é no reprocessamento da carga emocional no seu ritmo.</div>
        </div>
        <div x-data="{ open: false }" class="border-b border-gray-200 pb-4">
          <button @click="open = !open" class="flex justify-between w-full text-left font-fraunces text-navy text-lg"><span>A Terapia TRG pode ajudar em casos de fobia?</span><span x-text="open ? '−' : '+'" class="text-[#C9A227] text-2xl"></span></button>
          <div x-show="open" x-collapse class="mt-4 text-gray-700">Sim. Trabalhamos os medos persistentes a partir de uma abordagem estruturada para reprocessar a origem da fobia.</div>
        </div>
    """
)
update_file('build/servicos/reprocessamento-de-traumas-e-fobias.html', s1, '<!-- SERVICO CONTENT HERE -->')

# SERVICO 2: Ansiedade
s2 = servico_template.format(
    title_short="Ansiedade e Síndrome do Pânico",
    title="Terapia TRG para Ansiedade e Síndrome do Pânico",
    description="Acolhimento para quem enfrenta ansiedade e crises de pânico. A ansiedade pode fazer parte de diferentes momentos da vida. Quando o sofrimento emocional se torna intenso ou interfere na rotina, buscar apoio pode ser um passo importante.",
    content_html="""<h2 class="font-fraunces text-navy text-xl mt-8 mb-4">O que é esse atendimento?</h2>
        <p class="mb-4">A Terapia TRG utiliza um protocolo estruturado para trabalhar questões e padrões emocionais. No atendimento voltado à ansiedade e ao pânico, o foco é compreender o que a pessoa vivencia e avaliar como a abordagem pode fazer parte do seu processo.</p>
        <p class="mb-4">A terapia não substitui avaliação médica ou psicológica quando necessária. Sintomas intensos, recorrentes ou que geram risco devem ser avaliados por profissionais habilitados.</p>
        <h2 class="font-fraunces text-navy text-xl mt-8 mb-4">Para quem pode ser indicado?</h2>
        <ul class="list-disc pl-5 space-y-2 text-gray-700">
          <li>Vivenciam preocupação excessiva ou sofrimento relacionado à ansiedade.</li>
          <li>Enfrentam episódios de medo intenso ou crises de pânico.</li>
          <li>Sentem que questões emocionais interferem na rotina.</li>
        </ul>""",
    faq_html="""
        <div x-data="{ open: false }" class="border-b border-gray-200 pb-4">
          <button @click="open = !open" class="flex justify-between w-full text-left font-fraunces text-navy text-lg"><span>A Terapia TRG é indicada para ansiedade?</span><span x-text="open ? '−' : '+'" class="text-[#C9A227] text-2xl"></span></button>
          <div x-show="open" x-collapse class="mt-4 text-gray-700">Sim, a TRG tem protocolos voltados para ajudar na regulação emocional e no reprocessamento dos gatilhos da ansiedade.</div>
        </div>
        <div x-data="{ open: false }" class="border-b border-gray-200 pb-4">
          <button @click="open = !open" class="flex justify-between w-full text-left font-fraunces text-navy text-lg"><span>Preciso parar meu tratamento médico para fazer TRG?</span><span x-text="open ? '−' : '+'" class="text-[#C9A227] text-2xl"></span></button>
          <div x-show="open" x-collapse class="mt-4 text-gray-700">De forma alguma. A Terapia TRG atua como abordagem complementar. Nunca interrompa acompanhamento psiquiátrico ou medicação sem orientação médica.</div>
        </div>
    """
)
update_file('build/servicos/terapia-para-ansiedade-e-sindrome-do-panico.html', s2, '<!-- SERVICO CONTENT HERE -->')

# SERVICO 3: Depressão
s3 = servico_template.format(
    title_short="Depressão e Vazio Existencial",
    title="Terapia TRG para Depressão e Vazio Existencial",
    description="Um espaço de acolhimento para momentos de sofrimento emocional. Sentimentos de vazio, perdas, lutos e falta de sentido podem tornar o cotidiano mais difícil.",
    content_html="""<h2 class="font-fraunces text-navy text-xl mt-8 mb-4">O que é o atendimento para depressão e vazio existencial?</h2>
        <p class="mb-4">A abordagem TRG utiliza um protocolo estruturado para trabalhar questões emocionais. O atendimento pode ser procurado por pessoas que vivenciam sofrimento relacionado a perdas, lutos, sentimentos de vazio ou experiências dolorosas.</p>
        <p class="mb-4">Depressão exige avaliação adequada. A Terapia TRG não deve substituir acompanhamento médico ou psicológico quando necessário, nem ser apresentada como garantia de tratamento ou cura.</p>""",
    faq_html="""
        <div x-data="{ open: false }" class="border-b border-gray-200 pb-4">
          <button @click="open = !open" class="flex justify-between w-full text-left font-fraunces text-navy text-lg"><span>A terapia pode ajudar com o vazio existencial?</span><span x-text="open ? '−' : '+'" class="text-[#C9A227] text-2xl"></span></button>
          <div x-show="open" x-collapse class="mt-4 text-gray-700">Sim. Oferecemos um espaço de escuta e processamento emocional para ajudar a reencontrar um equilíbrio e compreender os sentimentos.</div>
        </div>
        <div x-data="{ open: false }" class="border-b border-gray-200 pb-4">
          <button @click="open = !open" class="flex justify-between w-full text-left font-fraunces text-navy text-lg"><span>Preciso já ter um diagnóstico para buscar atendimento?</span><span x-text="open ? '−' : '+'" class="text-[#C9A227] text-2xl"></span></button>
          <div x-show="open" x-collapse class="mt-4 text-gray-700">Não é necessário. Você pode iniciar as sessões para trabalhar suas dores emocionais de forma independente, e se for indicado, faremos os encaminhamentos necessários.</div>
        </div>
    """
)
update_file('build/servicos/terapia-para-depressao-e-vazio-existencial.html', s3, '<!-- SERVICO CONTENT HERE -->')

# BLOG 1
b1 = blog_post_template.format(
    title="O que é Terapia TRG e como funciona o Reprocessamento Generativo?",
    date="15 de Setembro de 2026",
    img_url="/assets/img/blog-1.jpg",
    toc_html="<li>O que é a TRG?</li><li>Como funciona o protocolo estruturado?</li><li>Como é uma sessão de TRG?</li>",
    content_html="""<p>A Terapia de Reprocessamento Generativo (TRG) é uma metodologia terapêutica projetada para resolver questões emocionais profundas, como traumas, fobias, compulsões, depressão e ansiedade.</p>
    <p>Reconhecida pelo MEC e amplamente apoiada pelo CITRG – Conselho Internacional de Terapia de Reprocessamento Generativo, com seu Código de Ética e Disciplina Profissional.</p>
    <h2 class="font-fraunces text-navy text-xl mt-8 mb-4">O que é a TRG?</h2>
    <p>A TRG, ao contrário das terapias tradicionais, não depende exclusivamente de discussões verbais, mas trabalha diretamente com o inconsciente para acessar e reprocessar memórias emocionais armazenadas. Esse método permite transformar experiências negativas em lições positivas, melhorando o bem-estar psicológico e emocional dos clientes.</p>
    <h2 class="font-fraunces text-navy text-xl mt-8 mb-4">Como funciona o protocolo estruturado em cinco etapas?</h2>
    <ul style="list-style: none; padding: 0; margin-top: 1.5rem; display: flex; flex-direction: column; gap: 1rem;">
        <li><b style="color: #f76b59;">1. Cronológico:</b> Explora a linha do tempo da sua vida, identificando eventos e traumas passados que influenciam o presente.</li>
        <li><b style="color: #8c2844;">2. Somático:</b> Trabalha as sensações e tensões físicas do corpo relacionadas às emoções não processadas.</li>
        <li><b style="color: #f19a38;">3. Temático:</b> Reprocessa temas recorrentes e padrões de comportamento indesejados em diferentes áreas da vida.</li>
        <li><b style="color: #63a8e1;">4. Futuro:</b> Libera ansiedades e preocupações sobre o futuro, construindo novas perspectivas positivas.</li>
        <li><b style="color: #8cd6a5;">5. Potencialização:</b> Ativa e fortalece os seus recursos internos, habilidades e o seu máximo potencial.</li>
    </ul>""",
    faq_html="""
        <div x-data="{ open: false }" class="border-b border-gray-200 pb-4">
          <button @click="open = !open" class="flex justify-between w-full text-left font-fraunces text-navy text-lg"><span>Como é uma sessão de TRG?</span><span x-text="open ? '−' : '+'" class="text-[#C9A227] text-2xl"></span></button>
          <div x-show="open" x-collapse class="mt-4 text-gray-700">A sessão é conduzida num ambiente seguro, guiada pelo terapeuta em busca de reprocessar os sentimentos mais incômodos sem a obrigação da fala extensiva de detalhes.</div>
        </div>
    """
)
update_file('build/blog/o-que-e-terapia-trg.html', b1, '<!-- BLOG POST CONTENT HERE -->')

# BLOG 2
b2 = blog_post_template.format(
    title="Terapia TRG para ansiedade: como funciona o atendimento?",
    date="10 de Setembro de 2026",
    img_url="/assets/img/blog-2.jpg",
    toc_html="<li>O que causa a ansiedade desproporcional?</li><li>Como a TRG ajuda?</li><li>Terapia online funciona?</li>",
    content_html="""<p>Informações sobre ansiedade e o atendimento emocional com TRG. A ansiedade faz parte da vida, mas quando desproporcional, exige suporte.</p>
    <h2 class="font-fraunces text-navy text-xl mt-8 mb-4">Como a TRG ajuda?</h2>
    <p>Ela reprocessa memórias e sensações corporais atreladas às crises e gatilhos da ansiedade generalizada, ajudando a estabilizar a resposta emocional.</p>""",
    faq_html="""
        <div x-data="{ open: false }" class="border-b border-gray-200 pb-4">
          <button @click="open = !open" class="flex justify-between w-full text-left font-fraunces text-navy text-lg"><span>Ansiedade tem cura?</span><span x-text="open ? '−' : '+'" class="text-[#C9A227] text-2xl"></span></button>
          <div x-show="open" x-collapse class="mt-4 text-gray-700">Não se fala em cura definitiva, mas em estabilização, compreensão e regulação dos níveis de ansiedade para recuperar a qualidade de vida.</div>
        </div>
    """
)
update_file('build/blog/terapia-trg-para-ansiedade.html', b2, '<!-- BLOG POST CONTENT HERE -->')

# BLOG 3
b3 = blog_post_template.format(
    title="Terapia TRG para depressão: o que saber antes de buscar atendimento?",
    date="05 de Setembro de 2026",
    img_url="/assets/img/blog-3.jpg",
    toc_html="<li>O poder do reprocessamento emocional</li><li>O acolhimento da dor</li><li>Os limites da terapia</li>",
    content_html="""<p>Informações sobre sofrimento emocional, depressão e o poder do reprocessamento.</p>
    <h2 class="font-fraunces text-navy text-xl mt-8 mb-4">O poder do reprocessamento emocional</h2>
    <p>A TRG atua diretamente nas dores da alma e nas raízes emocionais dos estados depressivos. Ao focar no reprocessamento do seu histórico emocional, buscamos fortalecer a sua base para que você recupere a alegria de viver.</p>""",
    faq_html="""
        <div x-data="{ open: false }" class="border-b border-gray-200 pb-4">
          <button @click="open = !open" class="flex justify-between w-full text-left font-fraunces text-navy text-lg"><span>A TRG pode ajudar na depressão?</span><span x-text="open ? '−' : '+'" class="text-[#C9A227] text-2xl"></span></button>
          <div x-show="open" x-collapse class="mt-4 text-gray-700">Sim, a TRG trabalha no reprocessamento dos traumas e bloqueios emocionais que frequentemente estão na base dos estados depressivos, oferecendo uma forma profunda de aliviar esse peso.</div>
        </div>
    """
)
update_file('build/blog/terapia-trg-para-depressao.html', b3, '<!-- BLOG POST CONTENT HERE -->')

print("Subpages updated.")
