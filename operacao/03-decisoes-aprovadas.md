# Decisoes Aprovadas

Status: ativo
Atualizado em: 2026-06-15

## Decisoes

### 2026-05-07

- Toda a conversa sobre a Vizantu deve ser documentada em arquivos `.md` na pasta `Documents`.
- A estrutura inicial de documentacao foi criada em `/Users/phedroborges/Documents/vizantu-documentacao`.
- A documentacao deve registrar:
  - o que for aprendido sobre a Vizantu;
  - o que for aprovado durante a conversa;
  - POPs;
  - automacoes;
  - oportunidades de otimizacao.

### 2026-05-18

- POP-001 (Criação de tarefa no ClickUp) aprovado e documentado em `04-pops.md`.
- Regras validadas por Phedro:
  - LEGENDA(ORG) e LEGENDA(ADS): obrigatórias antes de mover para "aprovação da copy" (a legenda é parte da copy).
  - LINK DO ARQUIVO: obrigatório assim que a pasta for criada — seja pelo recebimento de material do cliente ou pela criação pelo diretor de arte ao iniciar a demanda.
  - Responsável: pode ser múltiplos — todos os envolvidos na demanda devem estar adicionados.
  - Prioridade: usar apenas com urgência real de prazo, não como hábito.

### 2026-06-09

- A legenda deixa de existir como custom field separado (`LEGENDA(ORG)` e `LEGENDA(ADS)` deixam de ser usados).
- A legenda passa a ficar dentro da `Descrição` da tarefa, como a terceira seção obrigatória depois de `Direcionamento` e `Roteiro`.
- A estrutura obrigatória da descrição passa a ser:
  - `### Direcionamento:`
  - `### Roteiro:`
  - `### Legenda:`
  - checklist final de qualidade.
- O ClickUp passa a ser usado com foco em tarefas e entregas, nao como calendario editorial principal.
- O calendario de conteudo sera externo e ficara sob responsabilidade da social media.
- A social media tambem assume papel de CS operacional: conduz a aprovacao dos materiais com o cliente, cobra retornos e acompanha materiais pendentes.
- Os status aprovados para a esteira do ClickUp sao:
  - ideia
  - aprovação de copy
  - aguardando material
  - ajuste
  - pronto para criação
  - revisão
  - aprovação(cliente)
  - aprovado(status de fechamento)
  - problema externo/interno

### 2026-06-13

- Demandas em pacote devem ficar juntas quando representam a mesma entrega operacional, como captação de videos, leva de carrosseis, rodada de posts estaticos ou pacote editorial planejado.
- A tarefa de pacote so deve ser considerada entregue quando todos os materiais do pacote estiverem aprovados.
- Pendencias variaveis, cobranças, confirmações e atualizações de andamento devem ficar nos comentarios da tarefa, nao na descrição.
- A descrição da tarefa deve usar `#` para títulos principais da demanda e dos materiais, e `###` para blocos internos. Não usar `##`.
- Todo título principal `#` da descrição deve ser seguido por `---` como divisor padrão.
- O checklist de qualidade continua obrigatorio como criterio interno de revisão, mas nao precisa aparecer na descrição da tarefa.
- Links de referencia devem permanecer dentro do material correspondente para nao se perderem na reorganização da demanda.
- A regra de Markdown vale para toda descrição da tarefa no ClickUp: títulos principais em `#`, blocos internos em `###` e texto simples dentro dos blocos.
- O Direcionamento deixa de ser narrativo longo por padrão. Deve ser um briefing objetivo, proporcional à complexidade da demanda, com apenas o contexto necessário para o criativo executar sem dúvida.
- A esteira criativa passa a priorizar 8 formatos recorrentes no POP-003: video, carrossel, post estatico, story, impresso, capa, apresentação e website.
- Campanha comercial, relatório, planejamento, identidade visual e branding passam a ser tratados como planejamentos ou projetos maiores, nao como formatos criativos recorrentes dentro do POP-003.
- O time criativo deve receber conjuntos de criativos em uma demanda unica e entregar o conjunto completo ate a data estipulada.
- O POP-003 passa a cobrir todo tipo de material em três grupos: formatos criativos recorrentes, formatos criativos complementares e projetos/planejamentos maiores.
- Formatos criativos complementares mapeados: destaque de Instagram, copy, figurinha de WhatsApp e assinatura de e-mail.
- Projetos e planejamentos maiores mapeados: campanha comercial, relatório/planejamento e logo/identidade visual/branding/template.
- Links, anexos e referencias passam a ser parte obrigatoria do briefing. Nenhuma IA, MCP ou pessoa pode remover, resumir, trocar, ocultar ou deixar de migrar links existentes ao criar, reescrever ou reorganizar uma demanda.
- Se a IA nao conseguir abrir, interpretar ou acessar um link, deve avisar explicitamente o usuário ou registrar em comentário operacional, mas o link deve ser preservado na descrição.
- Antes de finalizar atualização de descrição no ClickUp, a quantidade de links da versão nova deve bater com a quantidade de links da versão original.
- A hierarquia visual das descrições no ClickUp passa a usar `#` para títulos principais da demanda e dos materiais, e `###` para blocos internos como Direcionamento, Roteiro / Conteúdo e Legenda.
- Demandas de vídeo devem nomear cada material no padrão `VÍDEO N | TÍTULO DO VÍDEO`, sempre em maiúsculo. Não usar `#` dentro do título porque o ClickUp pode corromper a formatação.
- Divisores `---` devem ficar logo abaixo dos títulos principais, sem linha em branco extra entre o divisor e o conteúdo seguinte.
- Legendas devem ser prontas para rede social, com uso moderado de emojis ou marcadores visuais quando fizer sentido, evitando que fiquem apenas como bloco de texto limpo.

### 2026-06-15

- A primeira linha da legenda (gancho) nunca deve ser uma instrução genérica como "leia a legenda", "salva esse post" ou "faça isso antes de ler". O gancho deve ser conteúdo de verdade — uma cena, dado ou provocação que gere identificação e puxe a leitura naturalmente.
- Para ler tarefas longas no ClickUp (demandas em pacote, com vários materiais numa só tarefa), usar SEMPRE o navegador para ler a descrição completa antes de editar. O `clickup_get_task` (MCP) trunca descrições muito longas e pode esconder materiais/legendas/links — o que causaria perda de conteúdo ao reescrever a descrição inteira.
- A escrita/atualização da tarefa continua sendo feita pelo MCP do ClickUp (`clickup_update_task`). O navegador é usado apenas para a leitura completa e segura.
- Numeração de demandas-pacote recorrentes: demandas que se repetem ao longo do tempo para o mesmo cliente (ex.: "VÍDEOS ORGÂNICOS", "CARROSSÉIS") seguem numeração sequencial no título. A primeira leva fica sem número (é a #1 implícita); as próximas recebem "#2", "#3" etc., sempre antes do sufixo " | CLIENTE". Ex.: "VÍDEOS ORGÂNICOS | ENA" (1ª) → "VÍDEOS ORGÂNICOS #2 | ENA" (2ª). Antes de criar uma nova leva, conferir na lista do cliente qual foi o último número usado naquele tipo e incrementar.
- TerraNet (reunião com Ianka, Wesley e Bruno em 02/06): retomada da campanha B2C em Perolândia e Estância, em resposta ao avanço do concorrente TBM nessas cidades (vendedor local, instalação na hora, chip a R$9,90). Pacote de resposta aprovado:
  - Preço promocional de R$ 79,90 nos 3 primeiros meses (R$10 abaixo da referência do concorrente).
  - Programa de indicação: cliente indica, e quando o indicado se torna cliente, quem indicou ganha uma mensalidade inteira de internet (benefício pontual, sem caráter de renda recorrente — evitar qualquer associação com pirâmide).
  - Ação ligada à Copa: camisa do Brasil + marcação da TerraNet no Instagram (story) = desconto na mensalidade a cada gol do Brasil, em todos os jogos (não só o primeiro). Referência: campanha da Petoria (a cada gol, chopp grátis).
  - Tráfego pago: 24 dias, 5 dias por semana, ~R$100/dia, focado em Perolândia e Estância.
  - Task `86aj0kfca` reestruturada: vídeos 1 e 2 (Copa institucional) + vídeos 3-5 (campanha B2C Perolândia/Estância — promoção R$79,90, indique e ganhe, 50% por gol do Brasil).
- Peças que vão circular tanto como orgânico quanto como anúncio (caso da TerraNet) passam a ter, na descrição da tarefa, duas versões de legenda por material: `### Legenda` (pronta para post orgânico) e `### Legenda (Anúncio)` (estruturada em Texto principal / Título / Descrição, para Meta Ads). As duas convivem no mesmo material — não substituem uma à outra.
