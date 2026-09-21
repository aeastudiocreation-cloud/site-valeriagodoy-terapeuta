# Blueprint Visual e Estrutural

Este documento descreve detalhadamente a estrutura de páginas, elementos e estilos visuais extraídos dos arquivos de referência (`home.html`, `sobre.jpeg` e `paleta site valeria.jpg`).

## Estilos Globais

**Cores**
*   **Pastel Sky Blue (`#A9D6F2`)** e variações claras (como Azure-claro `#EAF3FB`): Utilizados em blocos de fundo, superfícies secundárias, traços decorativos e ícones.
*   **Azure Blue (`#3175B9`)**: Utilizado para interações principais, como botões primários, ícones de destaque e links da marca (CTA secundários, botões WhatsApp, links interativos). Variação mais escura (`#2A6BA0`) para foco/hover e texto menor.
*   **Metallic Gold (Gradiente dourado) / Ouro chapado (`#C9A227`)**: Usados para detalhes nobres: fios divisórios finos (2 a 3px), sublinhados, aros, estrelas de avaliação, botões secundários específicos e contornos sutis de destaque.
*   **Soft Beige / Champagne (`#E0BE8C`)** e variações claras (`#F5E6CC`): Utilizados para blocos de fundos alternados, gradientes misturados ao azul nas imagens e preenchimento de áreas como avisos.
*   **Tinta / Navy (`#1F5482`)**: Cor base para títulos, CTAs finais e fundo do rodapé.
*   **Grafite (`#3E5163`)**: Cor de alto contraste utilizada no corpo de texto regular e textos descritivos.
*   **Pure Bright White (`#FFFFFF`)**: Fundo geral principal do site e de cards internos para garantir leitura limpa.

**Fontes**
*   **Títulos e Destaques (H1, H2, H3, H4):** `Fraunces` (serifada, transmitindo profissionalismo e solidez).
*   **Corpo do Texto e Elementos UI (Botões, navegação):** `Karla` (sans-serif, com visualização clara e legibilidade moderna).

**Tamanhos e Layout**
*   **Design Responsivo Mobile-First:** Grid que avança de 1 coluna (mobile) para grade de 2, 3 e até 4 colunas (desktop).
*   **Largura Máxima:** Contêiner delimitado a `1160px`.
*   **Formatos:** Forte uso de "Pílulas" (bordas totalmente arredondadas, `border-radius: 999px`) em botões, selos e tags/chips de categorias. Uso de cantos arredondados normais (`6px` a `20px`) em blocos de imagem, iframes de mapas e cards.

---

## Estrutura do Header e Footer

### HEADER
**Comportamento:** Fixo no topo (sticky) com efeito translúcido (blur).
**Elementos e Ordem:**
1.  **Logo / Marca:** Sigla quadrada com fundo navy e texto dourado, acompanhado pelo Nome da Terapeuta e cargo/região abaixo.
2.  **Navegação Principal (Desktop):** Links horizontais indicando a página ativa com um sublinhado dourado sutil ("Início, Medo de dirigir, Sobre, Blog, Contato, Guia de estilo").
3.  **Ações:** 
    *   Botão "WhatsApp" secundário.
    *   Ícone de Hambúrguer (Mobile) que abre uma gaveta (drawer) abrigando o menu completo e um botão extra de CTA ("Agendar avaliação").

### FOOTER
**Apresentação:** Fundo escuro (Navy) com texto em tom de azul claro e branco.
**Elementos e Ordem:**
1.  **Grade de 4 Colunas:**
    *   *Coluna 1:* Repetição da Logo + texto de resumo do serviço oferecido (Fobias, ansiedade, localização).
    *   *Coluna 2 (Atendimentos):* Lista de links para as especialidades / páginas de serviço.
    *   *Coluna 3 (Navegar):* Lista de links de navegação para as páginas do site.
    *   *Coluna 4 (Consultório):* Endereço físico completo, WhatsApp, E-mail, e Horário de funcionamento por extenso.
2.  **Barra Base Inferior:**
    *   Texto de Copyright e data.
    *   Aviso de isenção de responsabilidade médica ("A TRG é abordagem complementar...").
    *   Link para Política de Privacidade.
3.  **Barra Fixa (Somente Mobile):** Uma barra inferior fixada com um botão largo do WhatsApp, presente em todas as páginas para rápida conversão na versão mobile.

---

## Páginas e Estruturas de Seções

### 1) Home (Início)
1.  **Hero Section:** H1 principal, pequeno parágrafo de introdução, botões duplos de ação (WhatsApp + Como Funciona), texto de localização, imagem/retrato com fundo arredondado e um "Selo flutuante" sobreposto na foto de descrição, seguido por uma nuvem de chips (tags em pílula) de sintomas/dores clicáveis.
2.  **Faixa de Credibilidade:** Bloco horizontal com 4 colunas de ícones pequenos acompanhados de métricas/chancelas em negrito e texto (ex: Formação, Sessões, Local).
3.  **Cards de Serviços (O que traz até aqui):** Título de seção, descrição, grade com 6 cards em formato bloco (ícone, título, resumo, lista de 3 marcadores, link de saída). Um dos cards ganha destaque com borda azul e sombra.
4.  **Depoimentos:** Título, aviso de privacidade/autoria e 3 blocos retangulares exibindo estrelas douradas, citações e assinatura dos clientes.
5.  **Seção de Livros (Produtos alternativos):** Título, breve explicação, bloco contendo a foto grande da terapeuta à esquerda e dois cards de livros à direita (com imagem de capa, selo da edição, título, resumo, preço, formato e botão de compra).
6.  **Localização:** Coluna textual (título, descrição, blocos descritivos de endereço, estacionamento, linhas de ônibus e botão pro Google Maps) ao lado de um Iframe grande contendo o Mapa com marcação.
7.  **FAQ (Dúvidas Gerais):** Bloco dividido em dois: Coluna fixa (título lateral) e um Accordion do lado (várias perguntas expansíveis que abrem as respostas ao clicar, exibindo ícone de + que vira um x).
8.  **CTA Final (Call to Action):** Bloco retangular escuro (Navy) com gradiente dourado na borda superior contendo um Título forte, breve texto de reforço, e os 2 botões principais (WhatsApp / Formulário).

### 2) Página de Serviço Interna (ex: Medo de Dirigir)
1.  **Conteúdo e Corpo (Estrutura 2 colunas no Desktop):**
    *   **Coluna Principal (Esquerda):** Migalhas de pão (Breadcrumb), H1 da fobia tratada, texto descritivo. Lista de marcadores detalhando "Como costuma aparecer". Lista enumerada vertical das 4 Etapas do Tratamento (Avaliação, Reprocessamento, Instalação, Teste Real). Sessão com detalhes "O que a TRG não é". Accordion de FAQ focado 100% naquela fobia específica.
    *   **Coluna Lateral (Direita - Fixa/Sticky):** Card de "Resumo Prático" com duração da sessão, valor, pacote, e formato. Botão pro WhatsApp, e um aviso extra ("Nota importante" preenchido com tom amarelo champanhe) sobre tratamento médico paralelo.
2.  **CTA Final:** Bloco retangular padrão (Navy com fio dourado), idêntico ao estilo geral que convida à marcação de avaliação com botões de WhatsApp e Redirecionamento de Contato.

### 3) Sobre Mim
1.  **Conteúdo Principal (Estrutura 2 colunas no Desktop):**
    *   **Coluna Principal (Esquerda):** Breadcrumbs, Título H1 "Renata Salvetti", parágrafo de introdução sobre a especialidade, a narrativa cronológica da profissão (textos fluídos). Seção secundária: "Como é estar no consultório comigo", "Onde eu não atuo" e encaminhamentos psiquiátricos.
    *   **Coluna Lateral (Direita - Fixa/Sticky):** Retrato vertical de formato retangular. Card secundário chamativo para "Vamos Conversar" incitando o paciente a perguntar se houver dúvidas, finalizando com um CTA de agendamento.
2.  **CTA Final:** Mesmo formato padronizado visualmente ao fim da Home e Serviços, encorajando conversas prévias sem compromisso de 10 minutos.

### 4) Contato
1.  **Formulário e Contatos (Estrutura 2 colunas):**
    *   **Coluna Principal (Formulário):** Breadcrumbs, Título principal (H1) "Agendar avaliação". Um longo formulário de preenchimento (inputs e selects com labels bem marcados, e pequenas frases de orientação), incluindo: Nome, WhatsApp, E-mail, Assunto (Dropdown), Formato preferido (Dropdown) e Caixa de Mensagem longa. Alerta amarelo para não utilizar em casos de emergência vital e botão largo "Enviar Pedido".
    *   **Coluna Secundária:** Dois blocos de Cards verticais. Card 1: Canais Diretos (WhatsApp, Telefone fixo, E-mail, Instagram) com Botão WhatsApp no final. Card 2: Endereço resumido e blocos informativos separados listando o horário de funcionamento dia a dia.
2.  **Mapa de Fundo:** Um Iframe largo ocupando todo o bloco curto horizontal demonstrando o local fixo da clínica.

### 5) Blog
1.  **Cabeçalho do Blog:** Breadcrumbs, Título H1. Lista horizontal de Filtros de navegação na página no formato chips ("Todos", "Fobias", "Ansiedade", "Trauma", "Como Funciona").
2.  **Cards de Posts:** Grade responsiva composta por imagens de capa abstratas retangulares com fio dourado abaixo, seguidas pela Data e tempo de leitura, Título clicável do post, texto de excerto (resumo curto), e link de leitura para "Ler o artigo". (Acompanhado ao final da grade de dois botões para paginação: "Página Anterior" e "Página 2").
3.  **CTA Final:** Retângulo de ação azul escuro encorajando quem se identificou com as leituras a entrar em contato com os dois botões clássicos (WhatsApp + Agendar Avaliação).
