# Blueprint do plano — seção por seção

**Nome do documento (obrigatório):** `PLANO DE [MÊS] | [PROJETO]`, em caixa alta — no `<title>`, na topbar (`mini-brand`) e no rodapé. Ex.: `PLANO DE JULHO | TERRANET`. O eyebrow do hero pode repetir em versão amigável ("Plano de julho · TerraNet").

**Papel do documento:** além de apresentar a estratégia, o plano é o **instrumento de aprovação do cliente** — ele recebe o link, lê e avalia cada conteúdo na própria página (ver componente de aprovação na seção de roteiros). Escreva pensando nesse leitor: alguém que decide, não alguém que executa.

O plano é uma narrativa em bandas horizontais que alternam fundo claro (`.band`), fundo suave da marca (`.band.alt`) e fundo escuro (`.band.deep`). Cada seção tem um `section-head` com número + rótulo (`01 · OBJETIVO`) e um `h2` editorial que resume a tese da seção em uma frase com personalidade — nunca um rótulo burocrático ("Objetivo da campanha" é fraco; "Fazer o público perceber o risco, entender o caminho e reconhecer quem pode orientar." é o padrão).

**Respiro:** as seções precisam de separação generosa para o leitor sentir que mudou de assunto — o template já traz `padding` de 128px nas bands e 72px abaixo dos cabeçalhos; não comprima. Na dúvida, mais espaço, não menos.

A ordem abaixo é a do plano de campanha completo. Adapte por tipo de serviço (ver final do arquivo).

## 0. Topbar (sticky)

`header.topbar` com: `mini-brand` (ponto colorido + nome curto do plano), nav de âncoras para as seções, botão `Imprimir / PDF` (`onclick="window.print()"`). A nav some no mobile e no print.

## 1. Hero (`section.hero`)

Fundo escuro da marca, borda inferior grossa na cor de destaque. Grid 1.3fr/.7fr:

- **Esquerda**: logo do cliente (base64, versão para fundo escuro), eyebrow (`Plano de campanha · NOME`), `h1` grande com um trecho em `<strong>` na cor de destaque — o h1 resume a jornada da campanha em uma linha (ex.: "Do reconhecimento à **conversa no WhatsApp.**"), parágrafo `hero-intro` (o que é a campanha em 2 linhas), `hero-note` com a tagline/assinatura da marca e o tom da comunicação.
- **Direita**: `hero-stats` — 4 números-chave empilhados: dias de campanha, quantidade de conteúdos, frequência semanal, data da primeira gravação (ou os 4 números mais relevantes do projeto).

## 2. Objetivo (`band`, id="objetivo")

`objective-grid`: à esquerda um parágrafo grande (`objective-main`, 26px) com o objetivo comercial e o posicionamento, com trecho-chave em `<strong>`; à direita a lista `principles` ("O que precisa acontecer") com 4–6 itens curtos e concretos extraídos do briefing.

## 3. Estratégia (`band alt`, id="estrategia")

`strategy-grid` com 4 passos do funil (`strategy-step`): cada um tem rótulo numerado (`01 · Reconhecer`), um `h3` escrito na voz do público ("Isso acontece dentro da minha empresa.") e um parágrafo do que os conteúdos fazem nessa etapa. Feche com `audience-note` (bloco colorido em grid 180px/1fr): recorte de público prioritário + amplitude da mensagem.

## 4. Como o público vai ver (`band`, id="visual")

Atenção ao enquadramento: esta seção **não** é um manual de regras visuais ("use verde nos títulos") — o cliente não é designer e não quer instrução interna. Ela responde à pergunta dele: *"como o meu público, que é muito visual, vai ver esse projeto na tela?"*. Tudo se escreve do ponto de vista do seguidor/espectador:

- `swatches`: as cores que vão dominar o feed — mesmas 5 amostras com hex, mas apresentadas como "o que o público reconhece de longe".
- `type-sample`: uma frase grande do jeito que aparecerá nos cards/letterings — o cliente vê um pedaço real da experiência, não uma especificação de fonte. Se houver substituição de fonte (ex.: Gotham → Montserrat), registre em uma linha discreta.
- `ds-rules` → 3 cartões de experiência: **O que o público vê** (formatos, rostos, cenários), **O que ele sente** (tom, proximidade, humor ou sobriedade), **O que ele reconhece** (as marcas visuais que identificam o cliente antes de ler o nome).

O h2 e o lead descrevem a cena na tela do público, citando a personalidade do manual sem virar aula de branding.

## 5. Cronograma (`band alt`, id="cronograma")

Duas formas, conforme o serviço:

- **Campanha pontual**: `timeline` em colunas `week` (uma por semana), cada uma com rótulo temático e os posts como `post-date`. As semanas contam a progressão do funil.
- **Gestão de marca / plano mensal**: prefira um **calendário visual do mês** — grade de 7 colunas (domingo→sábado), um `cal-day` por dia com o número da data e os conteúdos como **chips clicáveis** (`<a href="#roteiro-N">`) coloridos por formato. Datas comemorativas travadas (badge no dia). No mobile, a grade vira agenda vertical (cada dia um card; dias vazios somem). É o formato que deixa a sazonalidade óbvia e ajuda o cliente a decidir o melhor dia de cada conteúdo. Calcule os dias da semana com precisão (ex.: `datetime.date(ano,mes,1).weekday()`), acerte as datas comemorativas e marque a captação (ver abaixo).

### Captação (regra da Vizantu)

- **A diária de captação de um mês grava o conteúdo do mês SEGUINTE** (ex.: a captação que aparece em agosto está gravando setembro; o material de agosto já foi captado em julho). **Sempre marque a captação no mês**, deixando explícito no rótulo/nota que é a gravação do próximo mês. Vale para todos os clientes de gestão de marca.
- **Horários** — muda por cliente:
  - **Casa Caramelo**: sábado, 14h, no **2º e 3º sábados** do mês.
  - **Wainny**: sexta, 14h — o dia exato fica **a definir com ela**.
  - **Demais clientes**: dia e hora **a definir**.
- Se quiser detalhar o que gravar, use o bloco `recording` (escuro, duas colunas: data/hora + lista de takes/b-roll/cenas). Em plano mensal com calendário, um `cal-note` curto abaixo do calendário costuma bastar.

## 6. Estrutura de tráfego (`band deep`, id="trafego")

Só quando há mídia paga (se o usuário não definiu, recomende uma estrutura e sinalize que é recomendação):

- `traffic-map`: fluxo horizontal `flow-node → flow-node.accent → flow-node` (entrada → topo → fundo), com setas `flow-arrow`. Cada nó: eyebrow, h3, parágrafo, lista de 3 itens.
- `campaigns`: um `campaign-card` por campanha com `dl` (Criativos / Público / Otimização / Saída).
- `traffic-table`: tabela etapa × função × materiais × CTA × indicador.

## 7. Roteiros aprovados (`band alt`, id="roteiros")

O coração do documento — e onde vale a regra do verbatim.

- `script-index`: grade de cards-âncora, um por material (número + formato, título, etapa · data).
- Um `article.script` por material, com:
  - `script-header`: eyebrow (`Material 01`), `h3` com o título, e as `tags`: status de aprovação (`tag approved`), formato (`tag format`), etapa do funil, campanha de tráfego (`tag traffic`), data (`tag date`).
  - `script-copy` com `approved-block`s: **Direcionamento** (parágrafos), **Roteiro / Conteúdo** (tabela CENA×FALA×LETTERING para vídeo; SLIDE×VISUAL×TEXTO para carrossel; Headline/Texto de apoio/Fechamento em parágrafos com `<strong>` para estático), **Referências** (quando o material aprovado citar fontes — ver abaixo) e **Legenda** (`caption-block`, borda esquerda colorida).
  - `aside.ig-mockup` (sticky no desktop): simulação do post no Instagram. Ver regras abaixo.

### Aprovação: NÃO inclua caixas manuais

A plataforma **Vizantu Planos** (onde o HTML é hospedado) **injeta automaticamente a interface de aprovação em cada conteúdo no momento do upload** — ela detecta cada bloco aprovável (`article.script[id]`, `section.band`, `section.slide`) e adiciona ali os botões de aprovar / pedir ajuste. Por isso:

- **Não** adicione `div.approval`, `approval-bar`, botões `btn-ok`/`btn-adjust`, `textarea` de comentário nem o `<script>` de `localStorage`. Eram do modelo antigo e hoje duplicam/atrapalham a injeção automática.
- Garanta só que cada conteúdo seja um bloco detectável com título claro: `article.script` com `id` único e um `script-header` contendo `eyebrow` (ex.: `Material 01`) + `h3` (título). É desse header que a plataforma tira o nome do item na aprovação.
- O documento continua sendo o instrumento de aprovação — só que a camada de aprovação vem da plataforma, não do HTML. Ao abrir o arquivo solto (fora da plataforma), não haverá botões, e tudo bem.

### Links e referências clicáveis (obrigatório)

Todo URL que aparecer no documento **precisa ser um link clicável** — `<a href="…" target="_blank" rel="noopener">`. O cliente precisa conseguir abrir cada referência que embasa o conteúdo.

- Quando o material aprovado citar fontes (dados de saúde, estatísticas, datas comemorativas), renderize um `approved-block` **Referências** com uma `<ul class="refs">` de links clicáveis (rótulo legível + `href`).
- URLs soltos no meio do texto (ex.: link de trend de referência no direcionamento) também devem virar `<a>` — nunca deixe URL como texto puro.
- Estilo mínimo: links em `--primary`/`--accent` com sublinhado e `overflow-wrap:break-word` para não estourar a largura.

### Regras do mockup de Instagram

O mockup é o que faz o cliente "ver" o post antes de existir — capriche:

- `ig-top`: avatar com iniciais do cliente, handle real do Instagram, cidade.
- `ig-visual`: `reel` (4:5, fundo escuro, `play-mark` ▶) para vídeo; `square` (1:1, fundo claro) para estático; `square` + `carousel-stack` para carrossel.
- Dentro do visual: `ig-kicker` (categoria · etapa), o `<strong>` com a headline ou primeira fala **real** do material, e `ig-signature` com a tagline da marca.
- Os pseudo-elementos `::before`/`::after` do `.ig-visual` são o acento gráfico da marca — redesenhe-os conforme o manual (barra, círculo, forma orgânica, ângulo…), não copie o da referência.
- `ig-caption`: a legenda **real e completa** do material, com o handle em negrito na frente.

## 8. Resultados esperados (`band`, id="resultados")

- `results-grid`: 4 cards numerados (`result`) com os resultados qualitativos esperados.
- `measurement`: duas colunas — lista de indicadores acompanhados + `kpi-note` com o critério de sucesso. Nunca invente metas numéricas: se investimento/histórico não foram informados, diga explicitamente que as projeções dependem desses dados (como na referência).

## 9. Rodapé (`footer.footer`)

Logo do cliente (base64) + texto à direita: nome do plano e período, "Documento consolidado a partir dos N materiais aprovados", e a linha de integridade `Fonte dos roteiros: SHA-256 <hash>`.

## 10. Template verbatim (invisível)

`<template id="approved-source-verbatim">` com o markdown-fonte dos materiais aprovados, na íntegra. Não renderiza, mas garante que o documento carrega a fonte da verdade.

---

# Variações por tipo de serviço

A arquitetura (topbar, hero, seções numeradas, mockups, rodapé com hash) permanece; o miolo se adapta:

- **Campanha pontual** (padrão): a sequência completa acima.
- **Gestão de marca / plano mensal**: troque "Estratégia de funil" por **linhas editoriais** (mesma `strategy-grid`, cada passo vira uma editoria com propósito); o cronograma vira calendário do mês; a seção de tráfego só entra se houver mídia paga (senão, substitua por uma seção de rotina/fluxo de aprovação usando os mesmos componentes).
- **Lançamento**: acrescente fases (aquecimento → abertura → fechamento) na timeline e use o `recording`/blocos de data para os marcos do lançamento.
- **Campanha política/institucional**: mesma lógica, mas cheque conformidade (período eleitoral, disclaimers exigidos) e troque "venda/WhatsApp" pela conversão real (cadastro de apoiadores, presença em evento etc.).

Se o serviço não se encaixa em nenhum desses, mantenha o esqueleto e pergunte-se: qual é a jornada que o cliente precisa enxergar? Cada seção existe para responder uma pergunta dele (o que vamos alcançar? como? quando? com que cara? o que será publicado? como saberemos que funcionou?). Monte as seções que respondem essas perguntas.
