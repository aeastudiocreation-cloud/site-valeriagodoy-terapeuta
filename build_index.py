import os

content = """
<!-- ======================= HOME ======================= -->
<div class="pagina ativa" id="p-home">
  <!-- 1.1 Hero Section -->
  <section class="wrap bloco hero" id="home">
    <div class="hero__texto">
      <div class="trilho"><span>Terapeuta TRG em Santa Bárbara d'Oeste</span></div>
      <h1>Você não precisa enfrentar suas questões emocionais sem acolhimento</h1>
      <p class="abertura">A Terapia de Reprocessamento Generativo (TRG) é uma abordagem estruturada para trabalhar experiências dolorosas, padrões emocionais e situações que continuam afetando sua vida. Com Valéria Godoy, você encontra um espaço de escuta, respeito e acompanhamento individualizado, atendimento online, de onde estiver.</p>
      
      <div class="hero__acoes">
        <a class="btn btn--zap" href="https://wa.me/5519920009231" target="_blank">Falar no WhatsApp</a>
        <a class="btn btn--secundario" href="#como-funciona">Conheça a Terapia TRG</a>
      </div>
      <p class="text-sm mt-4 text-[#3E5163]/80">Dê o primeiro passo para compreender melhor o que você está vivendo e conhecer uma abordagem terapêutica que pode fazer sentido para o seu momento.</p>
    </div>
    
    <div class="hero__imagem">
      <!-- Imagem Placeholder -->
      <div class="hero__retrato" style="background-image: url('/assets/img/hero.jpg'); background-color: #EAF3FB; background-size: cover;">
        <span class="sr-only">Retrato Valéria Godoy — 900×1200px</span>
      </div>
      <div class="hero__selo text-center">
        <strong class="block text-navy font-fraunces text-xl">Atendimento online</strong>
        <span class="text-sm">Para qualquer lugar do mundo</span>
      </div>
    </div>
  </section>

  <!-- 1.3 Barra de credibilidade -->
  <section class="wrap border-y border-[#EAF3FB] py-8 my-12" aria-label="Credenciais">
    <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
      <div>
        <svg class="mx-auto mb-2 text-secondary" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        <b class="block text-navy font-fraunces text-lg">Atendimento individualizado</b>
        <span class="text-sm text-gray-600">Um espaço de acolhimento e respeito.</span>
      </div>
      <div>
        <svg class="mx-auto mb-2 text-secondary" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
        <b class="block text-navy font-fraunces text-lg">Metodologia estruturada</b>
        <span class="text-sm text-gray-600">Protocolo em cinco etapas.</span>
      </div>
      <div>
        <svg class="mx-auto mb-2 text-secondary" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9"/></svg>
        <b class="block text-navy font-fraunces text-lg">Atendimento online</b>
        <span class="text-sm text-gray-600">Sessões à distância.</span>
      </div>
      <div>
        <svg class="mx-auto mb-2 text-[#C9A227]" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
        <b class="block text-navy font-fraunces text-lg">Avaliação no Google</b>
        <span class="text-sm text-gray-600">Nota 5,0 (1 avaliação).</span>
      </div>
    </div>
  </section>


  <!-- 1.5 Serviços -->
  <section class="bg-[#F9FAFD] py-20" id="servicos">
    <div class="wrap text-center max-w-2xl mx-auto mb-12">
      <div class="trilho justify-center"><span>Serviços</span></div>
      <h2>Como a Terapia TRG pode fazer parte do seu processo emocional</h2>
      <p>Conheça as áreas de atendimento e veja qual delas se aproxima das questões que você deseja compreender e trabalhar.</p>
    </div>
    
    <div class="wrap grade grade--3">
      <!-- Card 1 -->
      <article class="card card--destaque">
        <div class="card__topo">
          <span class="card__icone" aria-hidden="true"><svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></span>
          <h3>Traumas e Fobias</h3>
        </div>
        <p>A abordagem trabalha a carga emocional associada a experiências dolorosas do passado, traumas, medos e fobias, respeitando a história e os limites de cada pessoa.</p>
        <a class="card__link" href="/servicos/reprocessamento-de-traumas-e-fobias">Conhecer o atendimento</a>
      </article>

      <!-- Card 2 -->
      <article class="card">
        <div class="card__topo">
          <span class="card__icone" aria-hidden="true"><svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg></span>
          <h3>Ansiedade e Pânico</h3>
        </div>
        <p>Atendimento direcionado a adultos que enfrentam ansiedade e crises de pânico, com foco no trabalho emocional e na busca por maior estabilidade.</p>
        <a class="card__link" href="/servicos/terapia-para-ansiedade-e-sindrome-do-panico">Conhecer o atendimento</a>
      </article>

      <!-- Card 3 -->
      <article class="card">
        <div class="card__topo">
          <span class="card__icone" aria-hidden="true"><svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82zM7 7h.01"/></svg></span>
          <h3>Depressão e Luto</h3>
        </div>
        <p>Um espaço de acolhimento para trabalhar sofrimento emocional, perdas, lutos não resolvidos e sentimentos de falta de sentido na vida.</p>
        <a class="card__link" href="/servicos/terapia-para-depressao-e-vazio-existencial">Conhecer o atendimento</a>
      </article>
    </div>
    
    <div class="wrap text-center mt-12">
      <a href="/servicos" class="btn btn--primario">Quero conhecer todos os serviços</a>
    </div>
  </section>

  <!-- 1.6 Benefícios -->
  <section class="wrap py-20">
    <div class="trilho"><span>Por que escolher Valéria Godoy</span></div>
    <h2 class="mb-12">Um processo direcionado às suas questões emocionais</h2>
    
    <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
      <div>
        <h3 class="text-xl font-fraunces text-navy mb-3">Foco na resolução</h3>
        <p>A proposta da Terapia TRG é trabalhar as questões emocionais que estão sendo vivenciadas, em vez de se limitar ao aprendizado de como conviver com elas. O percurso é conduzido de acordo com a abordagem e as necessidades individuais.</p>
      </div>
      <div>
        <h3 class="text-xl font-fraunces text-navy mb-3">Metodologia estruturada</h3>
        <p>A TRG utiliza um protocolo organizado em cinco etapas. Essa estrutura oferece um direcionamento ao processo, sem transformar o tempo ou o resultado do atendimento em uma promessa.</p>
      </div>
      <div>
        <h3 class="text-xl font-fraunces text-navy mb-3">Acolhimento individualizado</h3>
        <p>Cada pessoa tem uma história, um ritmo e uma maneira própria de expressar o que sente. O atendimento valoriza a escuta, o respeito e os limites individuais.</p>
      </div>
      <div>
        <h3 class="text-xl font-fraunces text-navy mb-3">Atendimento online integral</h3>
        <p>Você pode realizar suas sessões sem precisar se deslocar até um consultório. O atendimento online permite o acompanhamento à distância, desde que existam condições adequadas de privacidade e conexão.</p>
      </div>
    </div>
  </section>

  <!-- 1.4 Quem somos -->
  <section class="wrap my-16 text-center max-w-3xl mx-auto">
    <div class="trilho justify-center"><span>Terapia emocional com acolhimento e direcionamento</span></div>
    <h2 class="mb-6">Um olhar com mais atenção para suas questões emocionais</h2>
    <p class="mb-4">A Valéria Godoy Terapeuta Emocional oferece atendimento em Terapia de Reprocessamento Generativo (TRG) para adultos que desejam olhar com mais atenção para suas questões emocionais. O trabalho parte da compreensão da história e das necessidades individuais de cada pessoa.</p>
    <p class="mb-8">A proposta é oferecer um processo terapêutico estruturado, com escuta respeitosa e foco nas questões que o cliente deseja trabalhar. Cada atendimento considera o ritmo, os limites e o contexto de quem busca apoio, com atendimento online para pessoas de qualquer lugar do mundo.</p>
    <a href="/sobre" class="btn btn--secundario">Conheça Valéria Godoy</a>
  </section>

  <!-- 1.7 Como Funciona -->
  <section class="bg-[#EAF3FB] py-20" id="como-funciona">
    <div class="wrap">
      <div class="trilho"><span>Passo a passo</span></div>
      <h2 class="mb-6">Como funciona a Terapia de Reprocessamento Generativo?</h2>
      <p class="max-w-2xl mb-12">O processo segue uma metodologia estruturada, com condução individualizada. As etapas abaixo explicam o caminho geral de chegada e acompanhamento, sem representar uma promessa de duração ou resultado.</p>
      
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
          <span class="text-[#C9A227] font-fraunces text-3xl block mb-4">1</span>
          <h4 class="font-fraunces text-navy text-lg mb-2">Entre em contato</h4>
          <p class="text-sm">Fale com Valéria Godoy pelo WhatsApp para conhecer o atendimento e tirar suas primeiras dúvidas.</p>
        </div>
        <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
          <span class="text-[#C9A227] font-fraunces text-3xl block mb-4">2</span>
          <h4 class="font-fraunces text-navy text-lg mb-2">Converse sobre seu momento</h4>
          <p class="text-sm">Compartilhe, dentro dos seus limites, o que está levando você a buscar apoio e quais questões deseja trabalhar.</p>
        </div>
        <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
          <span class="text-[#C9A227] font-fraunces text-3xl block mb-4">3</span>
          <h4 class="font-fraunces text-navy text-lg mb-2">Conheça a abordagem</h4>
          <p class="text-sm">A terapeuta explica como funciona a TRG e avalia a adequação do atendimento às suas necessidades.</p>
        </div>
        <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
          <span class="text-[#C9A227] font-fraunces text-3xl block mb-4">4</span>
          <h4 class="font-fraunces text-navy text-lg mb-2">Inicie o processo</h4>
          <p class="text-sm">Se houver concordância, as sessões são conduzidas conforme a metodologia e o ritmo individual.</p>
        </div>
        <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
          <span class="text-[#C9A227] font-fraunces text-3xl block mb-4">5</span>
          <h4 class="font-fraunces text-navy text-lg mb-2">Acompanhe seu percurso</h4>
          <p class="text-sm">O processo é desenvolvido com atenção às questões trabalhadas, aos limites pessoais e à necessidade de encaminhamentos.</p>
        </div>
      </div>
    </div>
  </section>


  <!-- 1.8 Prova Social -->
  <section class="wrap py-20 bg-white">
    <div class="trilho justify-center text-center"><span>Depoimentos Reais</span></div>
    <h2 class="text-center mb-12">O que dizem os clientes sobre o atendimento?</h2>
    
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto">
      <div class="bg-[#F9FAFD] p-8 rounded-2xl">
        <div class="flex text-[#C9A227] mb-4">
          <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
          <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
          <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
          <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
          <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
        </div>
        <p class="italic text-gray-700 mb-4">"A Valéria me ajudou a enfrentar questões que eu nem imaginava que ainda me afetavam tanto. O processo foi muito acolhedor."</p>
        <strong class="text-sm font-fraunces text-navy">— Cliente Autorizado</strong>
      </div>
      <div class="bg-[#F9FAFD] p-8 rounded-2xl flex flex-col justify-center items-center text-center border border-gray-100">
        <span class="text-4xl font-fraunces text-navy mb-2">5,0</span>
        <div class="flex text-[#C9A227] mb-4">
          <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
          <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
          <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
          <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
          <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
        </div>
        <span class="text-sm text-gray-600">Avaliação no Google</span>
      </div>
    </div>
  </section>

  <!-- 1.9 Local & Mapa -->
  <section class="wrap bloco py-20 border-t border-[#EAF3FB]">
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
      <div>
        <div class="trilho"><span>Terapia TRG em Santa Bárbara d'Oeste e online</span></div>
        <h2 class="mb-6">Local de atendimento</h2>
        <p class="mb-8">A Valéria Godoy Terapeuta Emocional está localizada em Santa Bárbara d'Oeste (SP). O atendimento também é oferecido online para pessoas de qualquer lugar do mundo.</p>
        
        <div class="mb-6">
          <h4 class="font-fraunces text-navy text-lg">Endereço presencial</h4>
          <p class="text-gray-700">Rua Romeu Fornazzari, 120, Bloco F, Apto 303<br>Bairro Dona Regina, Santa Bárbara d'Oeste – SP</p>
        </div>
        <div class="mb-6">
          <h4 class="font-fraunces text-navy text-lg">Atendimento Online</h4>
          <p class="text-gray-700">Sessões por vídeo para qualquer lugar do mundo.</p>
        </div>
        <div>
          <h4 class="font-fraunces text-navy text-lg">Horário</h4>
          <p class="text-gray-700">Consulte a disponibilidade diretamente pelo WhatsApp.</p>
        </div>
      </div>
      <div class="h-96 w-full rounded-2xl overflow-hidden shadow-sm">
        <iframe title="Mapa do consultório" class="w-full h-full border-0" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d14705.517316684725!2d-47.3669841!3d-22.7365533!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94c89b88cf5ac189%3A0x107a3109315dfdc7!2sJardim%20Dona%20Regina%2C%20Santa%20B%C3%A1rbara%20d'Oeste%20-%20SP!5e0!3m2!1spt-BR!2sbr!4v1715000000000!5m2!1spt-BR!2sbr" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
      </div>
    </div>
  </section>

  <!-- 1.10 FAQ (Accordion Alpine) -->
  <section class="wrap py-20" id="faq">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-12">
      <div class="md:col-span-1">
        <div class="trilho"><span>Dúvidas comuns</span></div>
        <h2 class="mb-4">Perguntas frequentes sobre Terapia TRG</h2>
        <p class="text-sm text-gray-600 mb-6">Dúvidas sobre o método, atendimento online e agendamento.</p>
      </div>
      
      <div class="md:col-span-2 flex flex-col gap-4">
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
            <span>Como funciona a Terapia TRG online?</span>
            <span x-text="open ? '−' : '+'" class="text-[#C9A227] text-2xl"></span>
          </button>
          <div x-show="open" x-collapse class="mt-4 text-gray-700">
            O atendimento é realizado por meio de uma plataforma de comunicação à distância, permitindo sessões sem deslocamento até o consultório. É necessário ter privacidade, conexão estável e um ambiente adequado para o atendimento.
          </div>
        </div>
        <div class="pt-4 text-center">
          <a href="/faq" class="btn btn--fantasma">Ver todas as perguntas</a>
        </div>
      </div>
    </div>
  </section>

  <!-- 1.11 CTA Final -->
  <section class="wrap py-12">
    <div class="cta-final text-center md:text-left bg-navy text-white rounded-3xl p-10 lg:p-16 flex flex-col md:flex-row items-center justify-between gap-8 relative overflow-hidden">
      <div class="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-[#B8860B] via-[#F3E0A1] to-[#9C7416]"></div>
      <div class="max-w-2xl">
        <h2 class="text-white text-3xl font-fraunces mb-4">Vamos conversar sobre o seu momento emocional?</h2>
        <p class="text-white/80">Buscar apoio é uma decisão pessoal. Se você deseja conhecer a Terapia TRG, entender como funciona o atendimento ou tirar dúvidas sobre as sessões, Valéria Godoy está disponível para conversar com você.</p>
      </div>
      <div class="flex flex-col gap-4 min-w-[240px]">
        <a class="btn btn--zap w-full text-center" href="https://wa.me/5519920009231" target="_blank">Falar com a Valéria Godoy</a>
        <span class="text-xs text-white/60 text-center">Consulte horários e condições de atendimento.</span>
      </div>
    </div>
  </section>
</div>
"""

with open('scaffold.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace the base content for index.html using replace or write directly
import re
with open('build/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<!-- HOME CONTENT HERE -->', content)

with open('build/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html updated successfully.")
