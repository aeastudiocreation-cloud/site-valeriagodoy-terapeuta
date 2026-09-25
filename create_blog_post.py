import json
import re
from datetime import datetime

template_path = r'c:\Users\aline\OneDrive\Desktop\Site-terapeuta-valeriagodoy\build\blog\o-que-e-terapia-trg.html'
with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

# Replace Metadata
template = re.sub(r'<title>.*?</title>', '<title>Terapia TRG para traumas: reprocessamento | Valéria Godoy</title>', template)
template = re.sub(r'<meta content="Valéria Godoy, terapeuta trg.*?" name="description"/>', '<meta content="Descubra como a Terapia de Reprocessamento Generativo (TRG) auxilia no tratamento de traumas e fobias de forma estruturada." name="description"/>', template)
template = re.sub(r'<link href="https://valeriagodoyterapeuta.com/blog/o-que-e-terapia-trg" rel="canonical"/>', '<link href="https://valeriagodoyterapeuta.com/blog/terapia-trg-para-traumas" rel="canonical"/>', template)

# Replace OG / Twitter
template = re.sub(r'content="https://valeriagodoyterapeuta.com/blog/o-que-e-terapia-trg" property="og:url"', 'content="https://valeriagodoyterapeuta.com/blog/terapia-trg-para-traumas" property="og:url"', template)

# Replace Breadcrumb
template = re.sub(r'› O que é Terapia TRG e como funciona o Reprocessamento Generativo\?</p>', '› Terapia TRG para traumas: como funciona o processo terapêutico?</p>', template)

# Replace Title and Date
template = re.sub(r'15 de Setembro de 2026', '22 de Setembro de 2026', template)
template = re.sub(r'<h1 class="mb-8">.*?</h1>', '<h1 class="mb-8">Terapia TRG para traumas: como funciona o processo terapêutico?</h1>', template)

# Create Content
new_content = """<div class="prose max-w-none text-gray-700 space-y-6">
<p>Os traumas psicológicos são como feridas invisíveis que, quando não tratadas, continuam a causar dor e a limitar a nossa qualidade de vida. Muitas pessoas convivem anos com os reflexos de experiências difíceis, acreditando que o tempo, por si só, curará tudo. No entanto, memórias mal processadas podem continuar enviando sinais de alerta ao cérebro, desencadeando respostas de medo, fuga ou ansiedade crônica. É exatamente nesse ponto que a <strong>Terapia de Reprocessamento Generativo (TRG)</strong> atua, oferecendo um caminho seguro e estruturado para o reprocessamento emocional.</p>
<p>Diferente de algumas abordagens que exigem anos de sessões para chegar à raiz do problema, a TRG foca diretamente no inconsciente, localizando e reprocessando os eventos que causaram o bloqueio inicial. Se você está em busca de entender como essa metodologia pode ajudar no tratamento de traumas profundos, este artigo detalha o passo a passo de como o processo terapêutico funciona na prática.</p>

<h2 id="o-que-e-trauma" class="font-fraunces text-navy text-xl mt-8 mb-4">1. O que é um trauma do ponto de vista emocional?</h2>
<p>Antes de entender o tratamento, é fundamental compreender o que define um trauma. Um trauma não é necessariamente o evento em si (como um acidente, uma perda irreparável ou uma situação de abuso), mas sim <em>como o cérebro processou e arquivou essa experiência</em>.</p>
<p>Quando vivemos uma situação de alto impacto emocional, o nosso cérebro pode falhar na hora de "arquivar" corretamente a memória. A lembrança fica congelada, ativa e latente. Sempre que algo no presente — um cheiro, um tom de voz, uma situação semelhante — serve como gatilho, a pessoa revive o sofrimento emocional como se estivesse acontecendo de novo. É isso que gera as fobias intensas, as crises de pânico e os bloqueios invisíveis.</p>

<div class="bg-blue-50 border-l-4 border-blue-500 p-6 my-8 rounded-r-xl">
<h3 class="font-bold text-navy mb-2">Você precisa de ajuda com seus traumas?</h3>
<p class="text-sm text-gray-700 mb-4">O primeiro passo é reconhecer que não precisa lidar com esse peso sozinho. Clique no botão abaixo para conversar comigo e entender como a TRG pode te ajudar.</p>
<a class="btn btn--zap inline-flex" href="https://wa.me/5519920009231" target="_blank">Conversar pelo WhatsApp</a>
</div>

<h2 id="como-a-trg-atua" class="font-fraunces text-navy text-xl mt-8 mb-4">2. Como a TRG atua no cérebro traumatizado?</h2>
<p>O objetivo principal da Terapia de Reprocessamento Generativo (TRG) não é apagar a sua memória. É impossível e não seria saudável esquecer o que vivemos. O objetivo da TRG é <strong>tirar a carga emocional negativa</strong> que está grudada nessa memória.</p>
<p>Na prática, a TRG acessa o inconsciente do cliente de forma leve e guiada. Sem a necessidade de falar compulsivamente sobre os detalhes traumáticos, o terapeuta ajuda o cliente a acessar a sensação do trauma, processá-la e reestruturá-la. Após o reprocessamento, o cliente ainda lembrará do que aconteceu, mas a lembrança não trará mais o peso, a dor ou o medo paralisante de antes. Ela vira apenas um fato do passado, não mais uma ameaça do presente.</p>

<h2 id="etapas-do-processo" class="font-fraunces text-navy text-xl mt-8 mb-4">3. As etapas do processo terapêutico para traumas</h2>
<p>A TRG é uma terapia breve e extremamente metódica. Para tratar traumas de maneira segura e evitar revitimizações, o terapeuta segue cinco etapas rigorosas:</p>
<ul class="list-disc pl-5 space-y-2 mt-4 mb-4">
<li><strong>O Método Cronológico:</strong> O terapeuta guia o cliente por toda a sua linha da vida, desde as primeiras lembranças da infância até o dia atual, limpando eventos estressores que ficaram pendentes.</li>
<li><strong>O Método Somático:</strong> Muitos traumas ficam arquivados no corpo, na forma de dores inexplicáveis, tensões ou doenças psicossomáticas. Esta etapa foca na leitura corporal e liberação dessas memórias físicas.</li>
<li><strong>O Método Temático:</strong> É aqui que as fobias específicas, medos paralisantes (como o medo de dirigir, medo do abandono, etc.) ou compulsões são tratados de forma isolada, se ainda restarem após a limpeza cronológica.</li>
<li><strong>O Método Futuro:</strong> Traumas passados geram ansiedade em relação ao que está por vir. O terapeuta ajuda o cliente a olhar para o futuro sem os filtros do medo.</li>
<li><strong>Potencialização:</strong> Ao retirar as barreiras traumáticas, o cliente é estimulado a fortalecer sua identidade e capacidades.</li>
</ul>

<h2 id="porque-escolher-a-trg" class="font-fraunces text-navy text-xl mt-8 mb-4">4. Por que a TRG é tão eficaz e respeitosa?</h2>
<p>Uma das grandes vantagens da TRG no tratamento de traumas é que o paciente não precisa ficar dissecando sua dor repetidas vezes. O reprocessamento não exige um foco exaustivo na narrativa. Para pessoas que viveram traumas severos, relatar a história pode ser doloroso demais. A TRG trabalha com a emoção arquivada, e uma vez que essa emoção é liberada no reprocessamento, o processo de cura acontece de forma progressiva e muitas vezes rápida, respeitando integralmente a história do cliente.</p>
</div>
"""

# Replace the specific TOC and prose content
# I will use regex to find everything from <div class="bg-[#F9FAFD] p-6 to </div> before Perguntas frequentes
start_idx = template.find('<div class="bg-[#F9FAFD] p-6')
end_idx = template.find('<h2 class="mt-16 mb-6 font-fraunces text-navy text-2xl">Perguntas frequentes</h2>')

new_toc = """<div class="bg-[#F9FAFD] p-6 rounded-2xl mb-12 border border-gray-100">
<h3 class="font-fraunces text-navy text-lg mb-3">Índice</h3>
<ul class="list-disc pl-5 text-sm text-secondary space-y-2">
<li><a href="#o-que-e-trauma" class="hover:underline">O que é um trauma emocional?</a></li>
<li><a href="#como-a-trg-atua" class="hover:underline">Como a TRG atua no cérebro?</a></li>
<li><a href="#etapas-do-processo" class="hover:underline">As etapas do reprocessamento</a></li>
<li><a href="#porque-escolher-a-trg" class="hover:underline">Por que escolher a TRG?</a></li>
</ul>
</div>
"""

template = template[:start_idx] + new_toc + new_content + template[end_idx:]

# Replace FAQs
start_faq = template.find('<details class="faq">')
end_faq = template.find('<!-- Author Box -->')

new_faqs = """<details class="faq">
<summary>A TRG apaga a memória do trauma?</summary>
<div><p>Não. Nenhuma terapia apaga memórias. O que a TRG faz é retirar a carga emocional negativa ligada ao trauma, permitindo que você lembre do evento sem sentir dor, medo ou angústia.</p></div>
</details>
<details class="faq">
<summary>Vou ter que contar detalhes do que sofri?</summary>
<div><p>Não obrigatoriamente. A TRG não exige que você relate exaustivamente o que aconteceu. Trabalhamos na camada emocional e no reprocessamento da sensação, o que torna a técnica muito mais leve e evita que você reviva a dor ativamente.</p></div>
</details>
<details class="faq">
<summary>A TRG funciona de forma online?</summary>
<div><p>Sim! O atendimento online tem a exata mesma eficácia do presencial. É necessário apenas que você tenha um local privado, conexão com internet e um fone de ouvido para realizarmos a sessão.</p></div>
</details>
<details class="faq">
<summary>Quantas sessões são necessárias para tratar um trauma?</summary>
<div><p>Como a TRG é um tratamento personalizado, a duração varia de acordo com a idade, a complexidade da história e a resposta emocional de cada um. Porém, por ser uma terapia breve, os resultados costumam ser notados rapidamente ao longo do processo.</p></div>
</details>
<details class="faq">
<summary>Posso fazer TRG se já faço tratamento psiquiátrico?</summary>
<div><p>Sim. A TRG atua de forma integrativa e complementar. Se você faz uso de medicação psiquiátrica, deve continuar seu tratamento médico normalmente. A TRG cuidará das raízes emocionais dos sintomas.</p></div>
</details>
</div>
"""

template = template[:start_faq] + new_faqs + template[end_faq:]

# Schema Update (Simplistic regex replacement for the script tag)
schema_start = template.find('<script type="application/ld+json">')
schema_end = template.find('</script>', schema_start) + 9

new_schema = """<script type="application/ld+json">{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://valeriagodoyterapeuta.com/blog/terapia-trg-para-traumas",
      "url": "https://valeriagodoyterapeuta.com/blog/terapia-trg-para-traumas",
      "name": "Terapia TRG para traumas: como funciona o processo terapêutico?",
      "description": "Descubra como a Terapia de Reprocessamento Generativo (TRG) auxilia no tratamento de traumas e fobias de forma estruturada.",
      "inLanguage": "pt-BR"
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://valeriagodoyterapeuta.com/" },
        { "@type": "ListItem", "position": 2, "name": "Blog", "item": "https://valeriagodoyterapeuta.com/blog" },
        { "@type": "ListItem", "position": 3, "name": "Terapia TRG Para Traumas", "item": "https://valeriagodoyterapeuta.com/blog/terapia-trg-para-traumas" }
      ]
    },
    {
      "@type": "BlogPosting",
      "@id": "https://valeriagodoyterapeuta.com/blog/terapia-trg-para-traumas#blogposting",
      "headline": "Terapia TRG para traumas: como funciona o processo terapêutico?",
      "datePublished": "2026-09-22T08:00:00-03:00",
      "author": { "@type": "Person", "name": "Valéria Godoy" }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        { "@type": "Question", "name": "A TRG apaga a memória do trauma?", "acceptedAnswer": { "@type": "Answer", "text": "Não. Nenhuma terapia apaga memórias. O que a TRG faz é retirar a carga emocional negativa ligada ao trauma." } },
        { "@type": "Question", "name": "Vou ter que contar detalhes do que sofri?", "acceptedAnswer": { "@type": "Answer", "text": "Não obrigatoriamente. A TRG não exige que você relate exaustivamente o que aconteceu." } },
        { "@type": "Question", "name": "A TRG funciona de forma online?", "acceptedAnswer": { "@type": "Answer", "text": "Sim! O atendimento online tem a exata mesma eficácia do presencial." } },
        { "@type": "Question", "name": "Quantas sessões são necessárias para tratar um trauma?", "acceptedAnswer": { "@type": "Answer", "text": "Como a TRG é um tratamento personalizado, a duração varia de acordo com a história. É uma terapia breve." } },
        { "@type": "Question", "name": "Posso fazer TRG se já faço tratamento psiquiátrico?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A TRG atua de forma integrativa e complementar." } }
      ]
    }
  ]
}</script>"""

template = template[:schema_start] + new_schema + template[schema_end:]

# Save
new_path = r'c:\Users\aline\OneDrive\Desktop\Site-terapeuta-valeriagodoy\build\blog\terapia-trg-para-traumas.html'
with open(new_path, 'w', encoding='utf-8') as f:
    f.write(template)

print(f"Created {new_path}")
