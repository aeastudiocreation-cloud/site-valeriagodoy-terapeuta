import sys

files = [
    r'c:\Users\aline\OneDrive\Desktop\Site-terapeuta-valeriagodoy\build\index.html',
    r'c:\Users\aline\OneDrive\Desktop\Site-terapeuta-valeriagodoy\04-referencia-visual\home.html'
]

for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    start_str = '<div class="trilho"><span>Depoimentos</span></div>'
    s_start = content.find(start_str)
    if s_start == -1:
        continue
    
    section_start = content.rfind('<section class="wrap bloco">', 0, s_start)
    section_end = content.find('</section>', s_start) + len('</section>')

    new_section = """  <section class="wrap bloco">
    <div class="trilho"><span>Depoimentos</span></div>
    <h2>O que dizem os clientes sobre o atendimento?</h2>
    <p class="limite">A experiência de cada pessoa com o processo terapêutico é individual.</p>
    
    <div class="grade grade--3" style="margin-top: var(--e5); align-items: stretch;">
      
      <!-- Depoimento 1 -->
      <div class="card card--bege" style="padding: var(--e5); height: 100%; display: flex; flex-direction: column;">
        <svg width="40" height="40" viewBox="0 0 24 24" fill="var(--ouro)" opacity="0.3" style="margin-bottom: 1rem;"><path d="M3 21c3 0 7-1 7-8V5c0-1.25-.756-2.017-2-2H4c-1.25 0-2 .75-2 1.972V11c0 1.25.75 2 2 2 1 0 1 0 1 1v1c0 1-1 2-2 2s-1 .008-1 1.031V20c0 1 0 1 1 1zm14 0c3 0 7-1 7-8V5c0-1.25-.756-2.017-2-2h-4c-1.25 0-2 .75-2 1.972V11c0 1.25.75 2 2 2 1 0 1 0 1 1v1c0 1-1 2-2 2s-1 .008-1 1.031V20c0 1 0 1 1 1z"/></svg>
        <div style="font-style: italic; font-size: 1.05rem; line-height: 1.6; color: var(--tinta); flex-grow: 1;">
          <span style="font-weight: 600; display: block; margin-bottom: 1rem;">"Hoje, a transformação é real. Consigo respirar com mais leveza. Sinto que finalmente aprendi a viver comigo mesma de um jeito mais gentil."</span>
          <details style="border: none;">
            <summary style="padding: 0; font-size: 0.95rem; color: var(--tinta); font-weight: 600; text-decoration: underline; list-style: none;">Ler depoimento completo</summary>
            <div style="margin-top: 1rem; font-weight: 400; font-size: 0.95rem;">
              "A Terapia de Reprocessamento Generativo tem sido um marco na minha vida. Antes dela, eu vivia tomada pela ansiedade. Sofria por antecipação, carregava um peso enorme nas costas e me cobrava o tempo todo, especialmente no trabalho, onde tudo parecia urgente, crítico e impossível de dar conta. Eu me sentia exausta por dentro.<br><br>
              Essa mudança não ficou apenas no emocional — ela tocou meu corpo também. Minha pressão alta, que sempre refletiu meu estado interno, começou a se estabilizar de um jeito tão impressionante que meu cardiologista suspendeu minha medicação. Ele queria ver se era mesmo a TRG… e, para minha surpresa, meu corpo respondeu com equilíbrio.<br><br>
              No próximo ano, farei novos exames, confiante e esperançosa de que essa estabilidade continuará. Hoje, eu me olho e reconheço: eu estou me reconstruindo, e isso tem sido libertador.<br><br>
              Sou grata a minha anja Valeria que conduz as sessões com excelente profissionalismo e carinho."
            </div>
          </details>
        </div>
        <div style="margin-top: var(--e4); border-top: 1px solid rgba(0,0,0,0.1); padding-top: var(--e3);">
          <b style="display: block; font-size: 1.1rem;">Ana Lucia Marcondes</b>
          <span style="font-size: var(--t-sm); color: var(--cinza);">53 anos, Professora e Terapeuta TRG</span>
        </div>
      </div>

      <!-- Depoimento 2 -->
      <div class="card card--azul-claro" style="padding: var(--e5); height: 100%; display: flex; flex-direction: column;">
        <svg width="40" height="40" viewBox="0 0 24 24" fill="var(--ouro)" opacity="0.3" style="margin-bottom: 1rem;"><path d="M3 21c3 0 7-1 7-8V5c0-1.25-.756-2.017-2-2H4c-1.25 0-2 .75-2 1.972V11c0 1.25.75 2 2 2 1 0 1 0 1 1v1c0 1-1 2-2 2s-1 .008-1 1.031V20c0 1 0 1 1 1zm14 0c3 0 7-1 7-8V5c0-1.25-.756-2.017-2-2h-4c-1.25 0-2 .75-2 1.972V11c0 1.25.75 2 2 2 1 0 1 0 1 1v1c0 1-1 2-2 2s-1 .008-1 1.031V20c0 1 0 1 1 1z"/></svg>
        <div style="font-style: italic; font-size: 1.05rem; line-height: 1.6; color: var(--tinta); flex-grow: 1;">
          <span style="font-weight: 600; display: block; margin-bottom: 1rem;">"Sessão após sessão venho me curando das dores, dos traumas, dos bloqueios. As dores físicas já não existem e minha vida vem sendo transformada dia após dia."</span>
          <details style="border: none;">
            <summary style="padding: 0; font-size: 0.95rem; color: var(--tinta); font-weight: 600; text-decoration: underline; list-style: none;">Ler depoimento completo</summary>
            <div style="margin-top: 1rem; font-weight: 400; font-size: 0.95rem;">
              "Durante muitos anos da minha vida, carreguei muita insegurança e muito medo. As vezes era invadida por uma tristeza profunda e tinha crises intensas de choro. As dores emocionais eram muitas e confesso, algumas eu nem sabia que existiam: era normal escolher o último lugar, a roupa que mais me 'apagava', assumir a culpa e a responsabilidade de outras pessoas, falar sim mesmo sem poder, não me encaixar em nenhum lugar, me calar querendo/precisando falar...<br><br>
              E é óbvio que tive que lidar com as consequências: dores físicas, perda da visão, depressão, relacionamentos tóxicos e fibromialgia.<br><br>
              Mas.... encontrei a Valéria Godoy, terapeuta da TRG, fui acolhida sem julgamento, sem a necessidade de me mostrar forte, sem precisar sorrir querendo chorar, e como eu chorei.... o mais incrível é o quanto a terapia me faz viver na prática a Palavra de Deus. Tenho vivido desde o arrancar das raízes de amargura (HB12.15) até o viver pela fé crendo que assim como eu creio me será feito (Mt8.13).<br><br>Gratidão a Deus, a Valéria e a TRG."
            </div>
          </details>
        </div>
        <div style="margin-top: var(--e4); border-top: 1px solid rgba(0,0,0,0.1); padding-top: var(--e3);">
          <b style="display: block; font-size: 1.1rem;">Marta</b>
          <span style="font-size: var(--t-sm); color: var(--cinza);">Cliente de TRG</span>
        </div>
      </div>

      <!-- Depoimento 3 -->
      <div class="card card--bege" style="padding: var(--e5); height: 100%; display: flex; flex-direction: column;">
        <svg width="40" height="40" viewBox="0 0 24 24" fill="var(--ouro)" opacity="0.3" style="margin-bottom: 1rem;"><path d="M3 21c3 0 7-1 7-8V5c0-1.25-.756-2.017-2-2H4c-1.25 0-2 .75-2 1.972V11c0 1.25.75 2 2 2 1 0 1 0 1 1v1c0 1-1 2-2 2s-1 .008-1 1.031V20c0 1 0 1 1 1zm14 0c3 0 7-1 7-8V5c0-1.25-.756-2.017-2-2h-4c-1.25 0-2 .75-2 1.972V11c0 1.25.75 2 2 2 1 0 1 0 1 1v1c0 1-1 2-2 2s-1 .008-1 1.031V20c0 1 0 1 1 1z"/></svg>
        <div style="font-style: italic; font-size: 1.05rem; line-height: 1.6; color: var(--tinta); flex-grow: 1;">
          <span style="font-weight: 600; display: block; margin-bottom: 1rem;">"A ansiedade sumiu, a depressão também, minha autoestima se elevou... fiquei uma mulher alegre e feliz com sentido de vida. Meu passado foi restaurado."</span>
          <details style="border: none;">
            <summary style="padding: 0; font-size: 0.95rem; color: var(--tinta); font-weight: 600; text-decoration: underline; list-style: none;">Ler depoimento completo</summary>
            <div style="margin-top: 1rem; font-weight: 400; font-size: 0.95rem;">
              "Sempre tive depressão desde pequena mas não sabia. Com o tempo foi agravando, a ansiedade piorou e depressão também, além da fobia social me paralisava, não conseguia trabalhar fora de casa por conta da depressão, tinha muita timidez e vergonha, baixa estima e um sentimento de morte terrível. Fiz anos de terapia com psicólogos, mas passava um tempo voltava tudo de novo.<br><br>
              Foi então que alguém me indicou a TRG e comecei a fazer essa terapia, achei fantástico. Em poucas sessões já conseguia resolver algumas dificuldades que tinha, como medo. Depois com os meses fui vendo a transformação em minha vida, comecei a falar em público que era impossível.<br><br>
              Agradeço à terapeuta Valéria por contribuir com essa obra em minha vida, que teve paciência, zelo e profissionalismo comigo.<br><br>
              Hoje não tenho sentimentos de morte, graças a Deus e à TRG. Hoje sinto vontade de viver intensamente a vida, feliz e sem culpa. Hoje é só gratidão."
            </div>
          </details>
        </div>
        <div style="margin-top: var(--e4); border-top: 1px solid rgba(0,0,0,0.1); padding-top: var(--e3);">
          <b style="display: block; font-size: 1.1rem;">Katilce Xavier</b>
          <span style="font-size: var(--t-sm); color: var(--cinza);">Cliente de TRG</span>
        </div>
      </div>

    </div>
  </section>"""

    new_content = content[:section_start] + new_section + content[section_end:]

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Testimonial accordion added successfully")
