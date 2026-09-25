import re

raw_text = r"""
1: <!DOCTYPE html>
2: <html lang="pt-BR">
3: <head>
4: <meta charset="utf-8">
5: <meta name="viewport" content="width=device-width, initial-scale=1">
6: <title>Terapeuta TRG Online | Valéria Godoy</title>
7: 
8: <script>
9: window.dataLayer = window.dataLayer || [];
10: function gtag(){dataLayer.push(arguments);}
11: gtag('consent', 'default', {
12:   'ad_storage': 'denied',
13:   'ad_user_data': 'denied',
14:   'ad_personalization': 'denied',
15:   'analytics_storage': 'denied'
16: });
17: </script>
18: <link rel="stylesheet" href="/assets/css/style-v2.css?v=9">
19: 
20: <meta name="description" content="Conheça Valéria Godoy.">
21: <link rel="preconnect" href="https://fonts.googleapis.com">
22: <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
23: <link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
24: 
25: </head>
26: <body>
27: <a class="pular" href="#conteudo">Ir para o conteúdo</a>
28: <header class="header">
29:   <div class="wrap header__in">
30:     <a class="marca" href="/" style="display:flex; align-items:center;"><img src="/assets/img/logo.png" alt="Valéria Godoy Logo" style="max-height: 80px; width: auto;"></a>
31: 
32:     <nav class="nav" aria-label="Principal">
33:       <a href="/" >Início</a>
34:       <a href="/servicos" >Serviços</a>
35:       <a href="/sobre" >Sobre</a>
36:       <a href="/blog" >Blog</a>
37:       <a href="/contato" >Contato</a>
38:       
39:     </nav>
40: 
41:     <div class="header__acoes">
42:       <a class="btn btn--zap btn--pequeno" href="https://wa.me/5519920009231" target="_blank" rel="noopener">
43:         <svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .1-1.7-.1a11 11 0 0 1-5.9-5.1c-.4-.7-.7-1.5-.7-2.2 0-.7.4-1.4.7-1.7.3-.3.6-.3.8-.3h.6c.2 0 .4 0 .6.5l.8 1.9c.1.2 0 .4-.1.5l-.4.5c-.1.2-.3.3-.1.6a8 8 0 0 0 3.6 3.1c.3.2.5.1.6 0l.7-.8c.2-.2.4-.2.6-.1l1.8.9c.2.1.4.2.4.3.1.2.1.5 0 .8Z"/></svg>
44:         WhatsApp
45:       </a>
46:       <button class="menu-btn" id="menuBtn" aria-expanded="false" aria-controls="gaveta" aria-label="Abrir menu">
47:         <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
48:       </button>
49:     </div>
50:   </div>
51: 
52:   <div class="gaveta" id="gaveta">
53:     <div class="wrap">
54:       <a href="/" >Início</a>
55:       <a href="/servicos" >Serviços</a>
56:       <a href="/sobre" >Sobre</a>
57:       <a href="/blog" >Blog</a>
58:       <a href="/contato" >Contato</a>
59:       
60:       <a class="btn btn--primario btn--bloco" href="/contato" >Agendar avaliação</a>
61:     </div>
62:   </div>
63: </header>
64: <main id="conteudo">
65: <div class="pagina ativa" style="display:block;" id="p-home">
66: 
67:   <section class="hero" style="background: url('/assets/img/hero.webp') center/cover no-repeat; position: relative; padding-top: 8rem; padding-bottom: 12rem;">
68:     <div style="position: absolute; inset: 0; background: rgba(0, 0, 0, 0.2);"></div>
69:     <div class="wrap" style="position: relative; z-index: 1;">
70:       <div style="background: rgba(255, 255, 255, 0.2); backdrop-filter: blur(12px); padding: var(--e5) var(--e7); border-radius: var(--r-lg); max-width: 1100px; margin-inline: auto; text-align: center; box-shadow: var(--sombra-2);">
71:         <div class="trilho" style="justify-content: center;"><span>Master Terapeuta TRG</span></div>
72:         <h1 style="color: #000; text-shadow: none; margin-inline: auto;">Você não precisa enfrentar suas questões emocionais sem acolhimento.</h1>
73:         <p class="abertura" style="color: #000; text-shadow: none; margin-inline: auto;">A Terapia de Reprocessamento Generativo (TRG) é uma abordagem estruturada para trabalhar experiências dolorosas, padrões emocionais e situações que continuam afetando sua vida. Com Valéria Godoy, você encontra um espaço de escuta, respeito e acompanhamento individualizado, atendimento online, de onde estiver.</p>
74:         <div class="hero__acoes" style="justify-content: center;">
75:           <a class="btn btn--zap" href="https://wa.me/5519920009231" target="_blank" rel="noopener">Falar no WhatsApp</a>
76:           <a class="btn" style="background: var(--champanhe); color: #000; border: none; font-weight: 600;" href="https://valeriagodoyterapeuta.com/blog/o-que-e-terapia-trg">Conheça a Terapia TRG</a>
77:         </div>
78:         <p style="font-size:var(--t-sm);color:#000;font-weight:500;margin:0;margin-inline:auto;">Dê o primeiro passo para compreender melhor o que você está vivendo e conhecer uma abordagem terapêutica que pode fazer sentido para o seu momento.</p>
79:       </div>
80:     </div>
81:   </section>
82: 
83:   <section class="wrap bloco">
84:     <div class="faixa">
85:       <div>
86:         <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 3 4 7v5c0 4.4 3.4 8.4 8 9 4.6-.6 8-4.6 8-9V7l-8-4Z"/></svg>
87:         <span><b>Atendimento individualizado</b>Um espaço de acolhimento e respeito à sua história.</span>
88:       </div>
89:       <div>
90:         <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>
91:         <span><b>Metodologia estruturada</b>Protocolo organizado em cinco etapas.</span>
92:       </div>
93:       <div>
94:         <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="2.6"/></svg>
95:         <span><b>Atendimento online</b>Sessões à distância de onde você estiver.</span>
96:       </div>
97:       <div>
98:         <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 5h16v11H7l-3 3V5Z"/></svg>
99:         <span><b>Avaliação no Google</b>Nota 5,0 por quem já conheceu.</span>
100:       </div>
101:     </div>
102:   </section>
103: 
104:   <section class="wrap bloco">
105:     <div class="trilho"><span>Serviços</span></div>
106:     <h2>Como a Terapia TRG pode fazer parte do seu processo emocional</h2>
107:     <p class="limite">Conheça as áreas de atendimento e veja qual delas se aproxima das questões que você deseja compreender e trabalhar.</p>
108: 
109:     <div class="grade grade--3" style="margin-top:var(--e6)">
110: 
111:       <article class="card card--bege">
112:         <div class="card__topo">
113:           <span class="card__icone" aria-hidden="true">
114:             <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M5 16 6.6 9.8A2 2 0 0 1 8.5 8.3h7a2 2 0 0 1 1.9 1.5L19 16"/><path d="M3 16h18v3h-3v-3M6 19H3v-3"/><circle cx="7.5" cy="16" r="0"/></svg>
115:           </span>
116:           <h3>Reprocessamento de Traumas e Fobias</h3>
117:         </div>
118:         <p>A abordagem trabalha a carga emocional associada a experiências dolorosas do passado, traumas, medos e fobias, respeitando a história e os limites de cada pessoa.</p>
119:         <a class="card__link" href="/servicos/reprocessamento-de-traumas-e-fobias">Conhecer o atendimento</a>
120:       </article>
121: 
122:       <article class="card card--bege">
123:         <div class="card__topo">
124:           <span class="card__icone" aria-hidden="true">
125:             <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 12h3l2-5 3 10 2.5-7 1.8 4H21"/></svg>
126:           </span>
127:           <h3>Ansiedade e Síndrome do Pânico</h3>
128:         </div>
129:         <p>Atendimento direcionado a adultos que enfrentam ansiedade e crises de pânico, com foco no trabalho emocional e na busca por maior estabilidade.</p>
130:         <a class="card__link" href="/servicos/terapia-para-ansiedade-e-sindrome-do-panico">Conhecer o atendimento</a>
131:       </article>
132: 
133:       <article class="card card--bege">
134:         <div class="card__topo">
135:           <span class="card__icone" aria-hidden="true">
136:             <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 21s-7-4.4-7-9.6A4 4 0 0 1 12 8a4 4 0 0 1 7 3.4C19 16.6 12 21 12 21Z"/></svg>
137:           </span>
138:           <h3>Depressão e Vazio Existencial</h3>
139:         </div>
140:         <p>Um espaço de acolhimento para trabalhar sofrimento emocional, perdas, lutos não resolvidos e sentimentos de falta de sentido na vida.</p>
141:         <a class="card__link" href="/servicos/terapia-para-depressao-e-vazio-existencial">Conhecer o atendimento</a>
142:       </article>
143: 
144:     </div>
145:     
146:     <div style="margin-top: var(--e6); text-align: center;">
147:       <a class="btn btn--secundario" href="/servicos">Quero conhecer todos os serviços</a>
148:     </div>
149:   </section>
150: 
151:   <section class="wrap bloco">
152:     <div class="trilho"><span>Benefícios e diferenciais</span></div>
153:     <h2>Por que escolher Valéria Godoy como sua terapeuta TRG?</h2>
154: 
155:     <div class="grade grade--2" style="margin-top:var(--e6)">
156:       <div class="card card--bege">
157:         <h3>Um processo direcionado às suas questões emocionais</h3>
158:         <p>A proposta da Terapia TRG é trabalhar as questões emocionais que estão sendo vivenciadas, em vez de se limitar ao aprendizado de como conviver com elas. O percurso é conduzido de acordo com a abordagem e as necessidades individuais.</p>
159:       </div>
160:       <div class="card card--bege">
161:         <h3>Metodologia estruturada</h3>
162:         <p>A TRG utiliza um protocolo organizado em cinco etapas. Essa estrutura oferece um direcionamento ao processo, sem transformar o tempo ou o resultado do atendimento em uma promessa.</p>
163:       </div>
164:       <div class="card card--bege">
165:         <h3>Acolhimento individualizado</h3>
166:         <p>Cada pessoa tem uma história, um ritmo e uma maneira própria de expressar o que sente. O atendimento valoriza a escuta, o respeito e os limites individuais.</p>
167:       </div>
168:       <div class="card card--bege">
169:         <h3>Atendimento online</h3>
170:         <p>Você pode realizar suas sessões sem precisar se deslocar até um consultório. O atendimento online permite o acompanhamento à distância, desde que existam condições adequadas de privacidade e conexão.</p>
171:       </div>
172:       <div class="card card--bege">
173:         <h3>Olhar integral para o ser humano</h3>
174:         <p>O processo considera as experiências, os padrões emocionais e o contexto de vida de cada pessoa, buscando compreender suas questões de maneira ampla.</p>
175:       </div>
176:       <div class="card card--bege">
177:         <h3>Sigilo e privacidade</h3>
178:         <p>As sessões são conduzidas em um ambiente seguro e confidencial. Você terá liberdade para falar sobre suas questões com a certeza de que tudo será mantido em rigoroso sigilo e respeito.</p>
179:       </div>
180:     </div>
181:   </section>
182: 
183:   <section class="wrap bloco bloco--escuro" style="background: sienna; padding-inline: var(--e4); max-width: 100%; padding-block: var(--e8);">
184:     <div class="wrap hero__in">
185:       <div>
186:         <div class="trilho"><span>Quem somos</span></div>
187:         <h2 style="margin-top:var(--e3)">Terapia emocional com acolhimento e direcionamento</h2>
188:         <p>Valéria Godoy oferece atendimento em Terapia de Reprocessamento Generativo (TRG) para adultos que desejam olhar com mais atenção para suas questões emocionais. O trabalho parte da compreensão da história e das necessidades individuais de cada pessoa.</p>
        <p>Valéria Godoy é Master Terapeuta especialista em Transtornos Graves, com excelentes resultados no tratamento de diversas condições, como depressão, ansiedade, bruxismo e fibromialgia.</p>
189:         <p>A proposta é oferecer um processo terapêutico estruturado, com escuta respeitosa e foco nas questões que o cliente deseja trabalhar. Cada atendimento considera o ritmo, os limites e o contexto de quem busca apoio.</p>
190:         <p>O atendimento é online para pessoas de qualquer lugar do mundo.</p>
191:         <div style="margin-top:var(--e5)">
192:           <a class="btn btn--primario" href="/sobre">Conheça Valéria Godoy</a>
193:         </div>
194:       </div>
195:       <div>
196:       <div style="position: relative; z-index: 1;">
197:         <div style="position: absolute; inset: 0; background: var(--ouro-grad); transform: translate(12px, 12px); border-radius: var(--r-lg); z-index: 0; opacity: 0.8; box-shadow: var(--sombra-1);"></div>
198:         <div class="hero__retrato" style="position: relative; z-index: 1; border: 6px solid #fff; box-shadow: var(--sombra-2);"><img src="/assets/img/valeria-godoy.webp" alt="Consultório Valéria Godoy" style="width:100%; height:100%; object-fit:cover;"></div>
199:       </div>
200:       <div class="hero__selo" style="position: relative; z-index: 2;">
201:           <b>Valéria Godoy</b>
202:           <p style="margin:var(--e2) 0 0;font-size:var(--t-sm);color:#333;text-align:center;">Master Terapeuta TRG</p>
203:           <p style="margin:var(--e1) 0 0;font-size:var(--t-xs);color:var(--cinza);">CITRG 06.936</p>
204:         </div>
205:       </div>
206:     </div>
207:   </section>

  <section class="wrap bloco" style="text-align: center;">
    <div class="trilho" style="justify-content: center;"><span>Impacto e Resultados</span></div>
    <h2 style="margin-top: var(--e2); margin-bottom: var(--e5);">Uma trajetória de transformação</h2>
    <div class="grade grade--2" style="max-width: 800px; margin: 0 auto; gap: 2rem;">
      <div class="card" style="background: #fff; padding: 2.5rem; text-align: center; border: 1px solid rgba(0,0,0,0.05); box-shadow: var(--sombra-1);">
        <h3 style="font-size: 3.5rem; color: #B8860B; margin-bottom: 0.5rem; font-weight: 700; line-height: 1;">+<span class="num-cont" data-alvo="3000">0</span></h3>
        <p style="font-size: 1.1rem; font-weight: 600; color: #333; margin: 0;">Sessões Realizadas</p>
      </div>
      <div class="card" style="background: #fff; padding: 2.5rem; text-align: center; border: 1px solid rgba(0,0,0,0.05); box-shadow: var(--sombra-1);">
        <h3 style="font-size: 3.5rem; color: #B8860B; margin-bottom: 0.5rem; font-weight: 700; line-height: 1;">+<span class="num-cont" data-alvo="500">0</span></h3>
        <p style="font-size: 1.1rem; font-weight: 600; color: #333; margin: 0;">Vidas Transformadas</p>
      </div>
    </div>
  </section>
  <script>
  document.addEventListener("DOMContentLoaded", function() {
    const contadores = document.querySelectorAll('.num-cont');
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const span = entry.target;
          const target = +span.getAttribute('data-alvo');
          let count = 0;
          const duration = 2000;
          const increment = Math.ceil(target / (duration / 30));
          const updateCount = () => {
            if (count < target) {
              count += increment;
              if(count > target) count = target;
              span.innerText = count.toLocaleString('pt-BR');
              setTimeout(updateCount, 30);
            } else {
              span.innerText = target.toLocaleString('pt-BR');
            }
          };
          updateCount();
          obs.unobserve(span);
        }
      });
    }, { threshold: 0.5 });
    contadores.forEach(contador => observer.observe(contador));
  });
  </script>
208: 
209:   <section class="bloco bloco--nevoa">
210:     <div class="wrap">
211:       <div class="trilho"><span>Como funciona</span></div>
212:       <h2>Como funciona a Terapia de Reprocessamento Generativo?</h2>
213:       <p class="limite">O processo segue uma metodologia estruturada, com condução individualizada. As etapas abaixo explicam o caminho geral de chegada e acompanhamento, sem representar uma promessa de duração ou resultado.</p>
214:       
215:       <ol class="etapas" style="margin-top:var(--e6); max-width: 800px;">
216:         <li>
217:           <h4>Entre em contato</h4>
218:           <p>Fale com Valéria Godoy pelo WhatsApp para conhecer o atendimento e tirar suas primeiras dúvidas.</p>
219:         </li>
220:         <li>
221:           <h4>Converse sobre o seu momento</h4>
222:           <p>Compartilhe, dentro dos seus limites, o que está levando você a buscar apoio e quais questões deseja trabalhar.</p>
223:         </li>
224:         <li>
225:           <h4>Conheça a abordagem TRG</h4>
226:           <p>A terapeuta explica como funciona a Terapia de Reprocessamento Generativo e avalia a adequação do atendimento às suas necessidades.</p>
227:         </li>
228:         <li>
229:           <h4>Inicie o processo terapêutico</h4>
230:           <p>Se houver concordância e condições adequadas para o atendimento, as sessões são conduzidas conforme a metodologia e o ritmo individual.</p>
231:         </li>
232:         <li>
233:           <h4>Acompanhe seu percurso</h4>
234:           <p>O processo é desenvolvido com atenção às questões trabalhadas, aos limites pessoais e à necessidade de outros encaminhamentos quando apropriado.</p>
235:         </li>
236:       </ol>
237:     </div>
238:   </section>
239: 
240: 
241:   <section class="wrap bloco">
242:     <div class="trilho"><span>Prova social</span></div>
243:     <h2>O que dizem os clientes sobre o atendimento?</h2>
244:     <p class="limite">A experiência de cada pessoa com o processo terapêutico é individual.</p>
245:     
246:     <div style="margin-top:var(--e5)">
247:       <div class="faixa" style="max-width: 400px; padding-block: var(--e4); border-bottom: none;">
248:         <div>
249:           <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 5h16v11H7l-3 3V5Z"/></svg>
250:           <span><b>Avaliação no Google</b>5,0 (1 avaliação)</span>
251:         </div>
252:       </div>
253:     </div>
254:   </section>
255: 
256:   <section class="bloco bloco--bege">
257:     <div class="wrap duas-colunas--esq duas-colunas">
258:       <div class="grudado">
259:         <div class="trilho"><span>Dúvidas</span></div>
260:         <h2>Antes de marcar</h2>
261:         <p style="font-size:var(--t-sm)">Não achou a sua pergunta? Entre em contato pelo WhatsApp para tirar suas dúvidas.</p>
262:       </div>
263:       <div class="faq">
264:         <details open>
265:           <summary>O que é a Terapia TRG?<span class="sinal" aria-hidden="true"></span></summary>
266:           <div class="faq__corpo">
267:             <p>A Terapia TRG, ou Terapia de Reprocessamento Generativo, é uma abordagem que trabalha questões emocionais por meio de um protocolo estruturado em etapas. O processo busca auxiliar o cliente no enfrentamento e no reprocessamento de experiências e padrões emocionais.</p>
268:           </div>
269:         </details>
270:         <details>
271:           <summary>Como funciona uma sessão de Terapia TRG?<span class="sinal" aria-hidden="true"></span></summary>
272:           <div class="faq__corpo">
273:             <p>As sessões seguem uma metodologia estruturada, considerando o histórico e as necessidades individuais do cliente. A terapeuta orienta o processo de acordo com a abordagem TRG, com acolhimento e respeito ao ritmo de cada pessoa.</p>
274:           </div>
275:         </details>
276:         <details>
277:           <summary>A Terapia TRG é indicada para quem tem traumas e fobias?<span class="sinal" aria-hidden="true"></span></summary>
278:           <div class="faq__corpo">
279:             <p>A TRG pode ser procurada por adultos que desejam trabalhar experiências traumáticas, medos e fobias. A avaliação inicial ajuda a compreender as necessidades do cliente e a adequação do atendimento.</p>
280:           </div>
281:         </details>
282:         <details>
283:           <summary>A Terapia TRG pode ajudar em casos de ansiedade e síndrome do pânico?<span class="sinal" aria-hidden="true"></span></summary>
284:           <div class="faq__corpo">
285:             <p>A abordagem é procurada por pessoas que enfrentam ansiedade e crises de pânico. A indicação e os limites do atendimento devem ser avaliados individualmente, e casos de maior gravidade podem exigir acompanhamento de profissionais habilitados em saúde mental.</p>
286:           </div>
287:         </details>
288:         <details>
289:           <summary>A Terapia TRG funciona para depressão e vazio existencial?<span class="sinal" aria-hidden="true"></span></summary>
290:           <div class="faq__corpo">
291:             <p>A TRG pode ser buscada por pessoas que vivenciam sofrimento emocional, perdas e sentimentos de falta de sentido. Depressão exige avaliação adequada, e a terapia não deve substituir acompanhamento médico ou psicológico quando necessário.</p>
292:           </div>
293:         </details>
294:         <details>
295:           <summary>Como funciona a Terapia TRG online?<span class="sinal" aria-hidden="true"></span></summary>
296:           <div class="faq__corpo">
297:             <p>O atendimento é realizado por meio de uma plataforma de comunicação à distância, permitindo sessões sem deslocamento até o consultório. É necessário ter privacidade, conexão estável e um ambiente adequado para o atendimento.</p>
298:           </div>
299:         </details>
300:         <details>
301:           <summary>Preciso reviver ou contar todos os detalhes de um trauma durante a sessão?<span class="sinal" aria-hidden="true"></span></summary>
302:           <div class="faq__corpo">
303:             <p>A metodologia TRG possui um protocolo estruturado e não depende necessariamente de longos relatos detalhados de todas as experiências. A forma de condução deve respeitar os limites, o conforto e as necessidades individuais do cliente.</p>
304:           </div>
305:         </details>
306:         <details>
307:           <summary>Como agendar uma sessão com Valéria Godoy?<span class="sinal" aria-hidden="true"></span></summary>
308:           <div class="faq__corpo">
309:             <p>O agendamento é realizado pelo WhatsApp. Basta entrar em contato com Valéria Godoy e consultar as informações sobre as sessões. No primeiro contato, você pode explicar o que está buscando, tirar dúvidas e verificar a disponibilidade.</p>
310:           </div>
311:         </details>
312:       </div>
313:     </div>
314:   </section>
315: 
316:   <section class="wrap bloco">
317:     <div class="duas-colunas">
318:       <div>
319:         <div class="trilho"><span>Onde fica</span></div>
320:         <h2>Terapia TRG em Santa Bárbara d'Oeste e online</h2>
321:         <p>A Valéria Godoy Terapeuta Emocional está localizada em Santa Bárbara d'Oeste, no estado de São Paulo. O atendimento é oferecido online para pessoas de qualquer lugar do mundo.</p>
322:         <ul class="dados">
323:           <li><b>Endereço</b><span>Rua Romeu Fornazzari, 120, Bloco F, Apartamento 303<br>Bairro Dona Regina, Santa Bárbara d'Oeste – SP</span></li>
324:           <li><b>Área de atendimento</b><span>Atendimento online para pessoas de qualquer lugar do mundo.</span></li>
325:           <li><b>Horário</b><span>Consulte a disponibilidade diretamente pelo WhatsApp.</span></li>
326:         </ul>
327:         <a class="btn btn--secundario" href="https://www.google.com/maps?q=Rua+Romeu+Fornazzari,+120,+Dona+Regina,+Santa+Bárbara+d'Oeste" target="_blank" rel="noopener">Abrir rota no Google Maps</a>
328:       </div>
329:       <div class="mapa">
330:         <iframe title="Mapa do consultório em Santa Bárbara d'Oeste"
331:           src="https://www.google.com/maps?q=Rua+Romeu+Fornazzari,+120,+Dona+Regina,+Santa+Bárbara+d'Oeste&output=embed"
332:           loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
333:       </div>
334:     </div>
335:   </section>
336: 
337:   <section class="wrap bloco--curto">
338:     <div class="cta-final">
339:       <div>
340:         <h2>Vamos conversar sobre o seu momento emocional?</h2>
341:         <p>Buscar apoio é uma decisão pessoal. Se você deseja conhecer a Terapia TRG, entender como funciona o atendimento ou tirar dúvidas sobre as sessões, Valéria Godoy está disponível para conversar com você.</p>
342:       </div>
343:       <div class="acoes">
344:         <a class="btn btn--zap" href="https://wa.me/5519920009231" target="_blank" rel="noopener">Falar com a Valéria Godoy</a>
345:       </div>
346:       <p style="font-size:var(--t-sm);color:var(--cinza);margin-top:var(--e3)">Entre em contato para consultar horários, condições de atendimento e os próximos passos.</p>
347:     </div>
348:   </section>
349: </div>
350: 
351: <!-- =======================
352: </main>
353: <footer class="footer">
354:   <div class="wrap">
355:     <div class="footer__grade">
356:       <div>
357:         <a class="marca" href="/" style="display:flex; align-items:center;"><img src="/assets/img/logo.png" alt="Valéria Godoy Logo" style="max-height: 80px; width: auto;"></a>
358:         <p style="font-size:var(--t-sm)">Terapia de Reprocessamento Generativo para fobias, ansiedade, trauma e luto. Atendimento online para todo o Brasil e exterior.</p>
359:       </div>
360: 
361:       <div>
362:         <h4>Atendimentos</h4>
363:         <ul class="footer__lista">
364:           <li><a href="/servicos" >Medo de dirigir</a></li>
365:           <li><a href="/servicos" >Ansiedade e pânico</a></li>
366:           <li><a href="/servicos" >Trauma</a></li>
367:           <li><a href="/servicos" >Luto e términos</a></li>
368:           <li><a href="/servicos" >Atendimento online</a></li>
369:         </ul>
370:       </div>
371: 
372:       <div>
373:         <h4>Navegar</h4>
374:         <ul class="footer__lista">
375:           <li><a href="/" >Início</a></li>
376:           <li><a href="/sobre" >Sobre</a></li>
377:           <li><a href="/blog" >Blog</a></li>
378:           <li><a href="/contato" >Contato</a></li>
379:           
380:         </ul>
381:       </div>
382: 
383:       </div>
384:     </div>
385: 
386:     <div class="footer__base">
387:       <div style="display: flex; flex-direction: column; gap: 0.25rem;">
<span>© 2026 Valéria Godoy · Terapeuta TRG · Atendimento Online</span>
<span style="font-size: 0.85em; opacity: 0.8;">Site desenvolvido por <a href="https://aeawebstudio.com/" target="_blank" rel="noopener" style="text-decoration: underline;">A&Ä Studio</a></span>
</div>
388:       <span>A TRG é abordagem complementar e não substitui tratamento médico ou psicológico.</span>
389:       <span><a href="/contato" >Política de privacidade</a></span>
390:     </div>
391:   </div>
392: </footer>
393: 
394: <div id="lgpd-banner" style="display:none; position:fixed; bottom:0; left:0; right:0; background:#fff; border-top:1px solid #E7E1D8; padding:1.5rem; box-shadow:0 -6px 20px -14px rgba(15,36,48,.5); z-index:9999; flex-wrap:wrap; gap:1rem; align-items:center; justify-content:space-between;">
395:   <p style="margin:0; font-size:14px; max-width:800px; color:#3E5163;">Este site utiliza cookies para melhorar sua experiência. Ao continuar, você concorda com nossa Política de Privacidade.</p>
396:   <div style="display:flex; gap:0.5rem; flex-wrap:wrap;">
397:     <button id="btn-reject-cookies" class="btn btn--secundario btn--pequeno">Recusar</button>
398:     <button id="btn-accept-cookies" class="btn btn--primario btn--pequeno">Aceitar</button>
399:   </div>
400: </div>
401: 
402: <div class="barra-zap">
403:   <a class="btn btn--zap btn--bloco" href="https://wa.me/5519920009231" target="_blank" rel="noopener">Falar no WhatsApp</a>
404: </div>
405: 
406: <script src="/assets/js/script.js"></script>
407: <script>
408:   var btn = document.getElementById("menuBtn");
409:   var gaveta = document.getElementById("gaveta");
410:   function fecharGaveta(){
411:     gaveta.classList.remove("aberta");
412:     btn.setAttribute("aria-expanded","false");
413:   }
414:   btn.addEventListener("click", function(){
415:     var aberto = gaveta.classList.toggle("aberta");
416:     btn.setAttribute("aria-expanded", String(aberto));
417:   });
418: </script>
419: 
420: </body>
421: </html>
"""

lines = raw_text.strip().split('\n')
clean_lines = []
for l in lines:
    idx = l.find(': ')
    if idx != -1 and l[:idx].isdigit():
        clean_lines.append(l[idx+2:])
    else:
        clean_lines.append(l)

content = '\n'.join(clean_lines)

# THE FIX THE USER REQUESTED: Apply the beige card class which uses the Sienna color
content = content.replace('card--azul-claro', 'card--bege')

with open(r'c:\Users\aline\OneDrive\Desktop\Site-terapeuta-valeriagodoy\build\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open(r'c:\Users\aline\OneDrive\Desktop\Site-terapeuta-valeriagodoy\04-referencia-visual\home.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Files restored successfully!")
