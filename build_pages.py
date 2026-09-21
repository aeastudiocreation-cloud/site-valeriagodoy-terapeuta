import re

sobre_content = """
<!-- ======================= SOBRE ======================= -->
<div class="pagina ativa" id="p-sobre">
  <section class="wrap bloco pt-16">
    <p class="text-sm text-gray-500 mb-8"><a href="/" class="hover:text-secondary">Início</a> › Sobre</p>
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-16">
      
      <div class="lg:col-span-2">
        <div class="trilho"><span>Valéria Godoy: Terapeuta Emocional e Terapeuta TRG</span></div>
        <h1 class="mb-6">Um espaço para acolher sua história</h1>
        <p class="abertura mb-8">A Valéria Godoy Terapeuta Emocional oferece atendimento em Terapia de Reprocessamento Generativo (TRG) para adultos que desejam trabalhar questões emocionais, experiências dolorosas e padrões que afetam sua vida.</p>

        <p class="mb-6">O atendimento é baseado em uma metodologia estruturada e em uma condução individualizada. A proposta é respeitar o momento de cada pessoa, oferecendo um espaço de escuta e acompanhamento.</p>

        <h2 class="mt-12 mb-6">Minha história profissional</h2>
        <p class="mb-4">Minha trajetória na área do cuidado emocional nasceu do desejo de compreender melhor as experiências que influenciam a vida das pessoas. Ao conhecer a Terapia de Reprocessamento Generativo, encontrei uma abordagem estruturada que se tornou parte do meu trabalho como terapeuta emocional.</p>
        <p class="mb-8">Hoje, ofereço um espaço de acolhimento e respeito, no qual cada pessoa pode conhecer a abordagem TRG e compreender se ela é adequada ao seu momento.</p>

        <h2 class="mt-12 mb-6">Missão e Valores</h2>
        <h3 class="font-fraunces text-navy text-xl mb-3">Missão</h3>
        <p class="mb-6">Oferecer um atendimento emocional acolhedor, ético e individualizado, com uma metodologia estruturada e atenção às necessidades de cada pessoa.</p>
        <h3 class="font-fraunces text-navy text-xl mb-3">Valores</h3>
        <ul class="list-disc pl-5 mb-8 space-y-2 text-gray-700">
          <li>Acolhimento e respeito à individualidade.</li>
          <li>Escuta sem julgamentos.</li>
          <li>Clareza sobre o processo terapêutico.</li>
          <li>Respeito aos limites e ao ritmo de cada cliente.</li>
          <li>Responsabilidade na condução do atendimento.</li>
          <li>Reconhecimento da importância de encaminhamentos profissionais quando necessários.</li>
        </ul>

        <h2 class="mt-12 mb-6">Formação e certificações</h2>
        <ul class="space-y-2 text-gray-700">
          <li><strong>Formação profissional:</strong> Terapeuta TRG</li>
          <li><strong>Instituição de formação:</strong> IBTF</li>
          <li><strong>Registro profissional:</strong> CITRG 06.936</li>
        </ul>
      </div>

      <aside class="lg:col-span-1">
        <div class="sticky top-24">
          <div class="w-full aspect-[3/4] bg-[#EAF3FB] rounded-2xl overflow-hidden mb-8" style="background-image: url('/assets/img/valeria-godoy.jpg'); background-size: cover;">
            <span class="sr-only">Valéria Godoy, terapeuta emocional TRG.</span>
          </div>
          <div class="card bg-[#F9FAFD] border border-gray-100 shadow-sm p-6 rounded-2xl">
            <h3 class="font-fraunces text-navy text-xl mb-3">Conheça a abordagem</h3>
            <p class="text-sm text-gray-700 mb-6">O trabalho terapêutico é desenvolvido a partir da metodologia TRG, com atenção à história individual e às questões emocionais apresentadas. O atendimento pode ocorrer presencialmente em Santa Bárbara d'Oeste ou online.</p>
            <a class="btn btn--primario w-full text-center" href="/servicos">Conheça os serviços</a>
            <a class="btn btn--fantasma w-full text-center mt-2" href="https://wa.me/5519920009231" target="_blank">Fale com Valéria Godoy</a>
          </div>
        </div>
      </aside>
    </div>
  </section>

  <!-- CTA final -->
  <section class="wrap py-12">
    <div class="cta-final text-center md:text-left bg-navy text-white rounded-3xl p-10 lg:p-16 flex flex-col md:flex-row items-center justify-between gap-8 relative overflow-hidden">
      <div class="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-[#B8860B] via-[#F3E0A1] to-[#9C7416]"></div>
      <div class="max-w-2xl">
        <h2 class="text-white text-3xl font-fraunces mb-4">Vamos conversar sobre o seu momento emocional?</h2>
        <p class="text-white/80">Buscar apoio é uma decisão pessoal. Se você deseja conhecer a Terapia TRG, entender como funciona o atendimento ou tirar dúvidas sobre as sessões, Valéria Godoy está disponível para conversar com você.</p>
      </div>
      <div class="flex flex-col gap-4 min-w-[240px]">
        <a class="btn btn--zap w-full text-center" href="https://wa.me/5519920009231" target="_blank">Falar com Valéria Godoy</a>
      </div>
    </div>
  </section>
</div>
"""

contato_content = """
<!-- ======================= CONTATO ======================= -->
<div class="pagina ativa" id="p-contato">
  <section class="wrap bloco pt-16">
    <p class="text-sm text-gray-500 mb-8"><a href="/" class="hover:text-secondary">Início</a> › Contato</p>
    
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-16">
      <div>
        <div class="trilho"><span>Contato</span></div>
        <h1 class="mb-6">Fale com Valéria Godoy, Terapeuta TRG</h1>
        <p class="text-lg text-gray-600 mb-8">O primeiro passo começa com uma conversa. Se você deseja conhecer a Terapia de Reprocessamento Generativo, esclarecer dúvidas ou consultar informações sobre o atendimento, entre em contato pelo WhatsApp.</p>
        <p class="mb-12">Você pode falar sobre o que está buscando e conhecer as possibilidades de acompanhamento, sem compromisso de iniciar o processo.</p>

        <div class="bg-[#F9FAFD] border-l-4 border-secondary p-8 rounded-r-2xl mb-12 shadow-sm">
          <h2 class="font-fraunces text-navy text-2xl mb-4">Fale pelo WhatsApp</h2>
          <p class="text-gray-700 mb-6">Envie uma mensagem para consultar disponibilidade, modalidade de atendimento, valores e informações sobre o agendamento.</p>
          <a class="btn btn--zap w-full md:w-auto text-center" href="https://wa.me/5519920009231" target="_blank">Iniciar conversa no WhatsApp</a>
        </div>

        <h3 class="font-fraunces text-navy text-xl mb-3 mt-12">Atendimento online</h3>
        <p class="text-gray-700 mb-4">A Terapia TRG é oferecida online para pessoas de qualquer lugar do mundo. Para participar, é importante ter:</p>
        <ul class="list-disc pl-5 mb-8 space-y-2 text-gray-700">
          <li>Um ambiente privado e adequado para a sessão.</li>
          <li>Conexão estável com a internet.</li>
          <li>Dispositivo com câmera e áudio.</li>
          <li>Disponibilidade para realizar o atendimento sem interrupções.</li>
        </ul>
      </div>

      <aside>
        <div class="card bg-[#F9FAFD] border border-gray-100 shadow-sm p-8 rounded-2xl mb-8">
          <h3 class="font-fraunces text-navy text-xl mb-6">Consultório Presencial</h3>
          <p class="text-gray-700 mb-6">Rua Romeu Fornazzari, 120, Bloco F, Apto 303<br>Bairro Dona Regina, Santa Bárbara d'Oeste – SP</p>
          
          <h4 class="font-fraunces text-navy text-lg mb-2">Horários de atendimento</h4>
          <p class="text-sm text-gray-600 mb-6">Consulte os dias e horários disponíveis diretamente com Valéria Godoy pelo WhatsApp.</p>

          <h4 class="font-fraunces text-navy text-lg mb-2">Redes Sociais</h4>
          <ul class="space-y-2 text-sm text-gray-600">
            <li><strong>Instagram:</strong> <a href="https://www.instagram.com/valeriagodoyterapeuta/" target="_blank" class="text-secondary hover:underline">@valeriagodoyterapeuta</a></li>
            <li><strong>Facebook:</strong> <a href="https://www.facebook.com/valeriagodoy.terapeuta/" target="_blank" class="text-secondary hover:underline">Valéria Godoy Terapeuta</a></li>
            <li><strong>Threads:</strong> <a href="https://www.threads.com/@valeriagodoyterapeuta" target="_blank" class="text-secondary hover:underline">@valeriagodoyterapeuta</a></li>
          </ul>
        </div>
      </aside>
    </div>
  </section>

  <!-- Mapa -->
  <section class="wrap py-12">
    <div class="h-[400px] w-full rounded-2xl overflow-hidden shadow-sm">
      <iframe title="Localização do consultório em Santa Bárbara d'Oeste" class="w-full h-full border-0" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d14705.517316684725!2d-47.3669841!3d-22.7365533!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94c89b88cf5ac189%3A0x107a3109315dfdc7!2sJardim%20Dona%20Regina%2C%20Santa%20B%C3%A1rbara%20d'Oeste%20-%20SP!5e0!3m2!1spt-BR!2sbr!4v1715000000000!5m2!1spt-BR!2sbr" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
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

update_file('build/sobre.html', sobre_content, '<!-- SOBRE CONTENT HERE -->')
update_file('build/contato.html', contato_content, '<!-- CONTATO CONTENT HERE -->')

print("sobre.html and contato.html updated successfully.")
