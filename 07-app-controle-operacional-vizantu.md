# App de Controle Operacional da Vizantu

Status: proposta em construção
Atualizado em: 2026-06-15

## Objetivo do documento

Este documento descreve o app interno que a Vizantu precisa desenvolver para controlar melhor entregas, reuniões, planejamentos, captações, demandas do ClickUp, problemas de WhatsApp e satisfação dos clientes.

O app não substitui o ClickUp. Ele funciona como uma camada de leitura, acompanhamento e inteligência operacional por cliente.

## O que é o app

O app é um painel interno de gestão da Vizantu para responder, de forma simples, uma pergunta central:

**A Vizantu está cuidando bem de cada cliente e cumprindo os compromissos principais?**

Hoje o ClickUp controla demandas e tarefas de produção. Isso continua sendo necessário, mas ele não resolve sozinho a visão macro de relacionamento, cadência e entrega estratégica.

O app entra para organizar:

- planejamento entregue ou não entregue;
- captação realizada ou não realizada;
- reunião de alinhamento realizada ou não realizada;
- demandas do planejamento em andamento no ClickUp;
- problemas percebidos no WhatsApp;
- tempo de resposta nos grupos;
- resolução de problemas;
- transcrições de reuniões;
- satisfação e NPS do cliente;
- histórico e memória operacional de cada cliente.

## Princípio central

O app deve ser simples.

O controle principal das entregas não deve usar vários status. A lógica principal é:

- havia uma entrega prevista;
- havia uma data prevista;
- foi entregue ou não foi entregue;
- se foi entregue, quando foi entregue;
- se não foi entregue, o painel precisa mostrar isso com clareza.

O app não deve virar uma segunda ferramenta de tarefas. A esteira detalhada de produção continua no ClickUp.

## O que o app não é

O app não é:

- substituto do ClickUp;
- calendário editorial;
- ferramenta de criação de conteúdo;
- ferramenta de aprovação criativa;
- chat interno;
- CRM comercial completo;
- local para duplicar todas as tarefas.

O app é uma visão de controle, compromisso, histórico e saúde do cliente.

## Como o app se encaixa com o ClickUp

O ClickUp continua responsável pela execução das demandas.

No ClickUp ficam:

- tarefas de conteúdo;
- tarefas de design;
- tarefas de vídeo;
- demandas de campanha;
- demandas em revisão;
- aprovações do cliente;
- prazos internos de produção;
- responsáveis pela execução;
- status da esteira de produção.

No app ficam:

- visão por cliente;
- checks de entregas principais;
- datas previstas e datas reais;
- leitura consolidada das demandas do ClickUp;
- conexão entre planejamento e execução;
- alertas de atraso;
- histórico de reuniões;
- problemas de relacionamento e atendimento;
- satisfação do cliente.

## Integração com o ClickUp por tags

As demandas que fazem parte do planejamento podem continuar sendo criadas no ClickUp.

Para que o app reconheça essas demandas, o ClickUp deve usar tags padronizadas.

Tags sugeridas:

- `planejamento`
- `captacao`
- `reuniao-alinhamento`
- `conteudo-planejado`
- `campanha`
- `problema-cliente`
- `aprovacao-cliente`
- `nps`
- `prioridade-gestao`
- `relatorio`

O app deve puxar as tarefas do ClickUp e organizar por:

- cliente;
- tag;
- data de entrega;
- responsável;
- status atual no ClickUp;
- tarefa atrasada ou não;
- tarefa em aprovação do cliente;
- tarefa aguardando material;
- tarefa em problema externo/interno.

Importante: o app pode mostrar o status vindo do ClickUp, mas não deve transformar isso em um novo fluxo de status dentro do próprio app.

## Entregas principais controladas pelo app

O app deve controlar os marcos mais importantes da operação da Vizantu.

### Planejamento

Controle simples:

- cliente;
- mês ou ciclo;
- data prevista;
- entregue ou não entregue;
- data real de entrega;
- link do planejamento, se existir;
- demandas do ClickUp vinculadas por tag.

Objetivo:

- saber se o cliente recebeu planejamento no período certo;
- entender quais demandas nasceram daquele planejamento;
- enxergar se o planejamento está virando execução real.

### Captação

Controle simples:

- cliente;
- data prevista;
- captação realizada ou não realizada;
- data real;
- local, quando necessário;
- observação curta;
- demandas do ClickUp vinculadas.

Objetivo:

- saber quais clientes tiveram captação recente;
- evitar cliente sem material;
- conectar captação com produção de conteúdo.

### Reunião de alinhamento

Controle simples:

- cliente;
- data prevista;
- reunião realizada ou não realizada;
- data real;
- link do Meet;
- link da transcrição no Google Docs/Drive;
- resumo;
- decisões;
- pendências;
- próximos passos.

Objetivo:

- saber se a reunião aconteceu;
- transformar a transcrição em memória útil;
- evitar que decisões fiquem perdidas no Google Drive ou na conversa.

### Relatório ou revisão mensal

Controle simples:

- cliente;
- período analisado;
- data prevista;
- entregue ou não entregue;
- data real;
- link do relatório;
- principais aprendizados.

Objetivo:

- manter rotina de revisão;
- registrar aprendizados;
- conectar resultado com próximos planejamentos.

### NPS e satisfação

Controle simples:

- cliente;
- data de envio;
- resposta recebida ou não;
- nota;
- comentário;
- classificação;
- sinal de risco, quando houver.

Objetivo:

- acompanhar satisfação real;
- cruzar NPS com reuniões e WhatsApp;
- identificar risco antes de virar problema maior.

## Integração com Google Meet, Docs e Drive

As reuniões com clientes acontecem no Google Meet e geram transcrição automaticamente.

Essas transcrições vão para o Google Docs/Drive. O app deve usar esses arquivos como fonte de inteligência.

O fluxo ideal:

1. Reunião acontece no Google Meet.
2. A transcrição é salva no Google Docs/Drive.
3. O app identifica o arquivo.
4. O app vincula a transcrição ao cliente correto.
5. O app gera um resumo operacional.
6. O app extrai decisões, pendências e próximos passos.
7. O app sugere demandas que podem virar tarefa no ClickUp.

Dados extraídos da reunião:

- resumo da reunião;
- assuntos discutidos;
- decisões tomadas;
- dúvidas do cliente;
- cobranças do cliente;
- pendências da Vizantu;
- pendências do cliente;
- próximos passos;
- possíveis demandas;
- sinais de satisfação ou insatisfação.

## Integração com WhatsApp

O WhatsApp é uma fonte importante para entender atendimento, urgência, problemas e satisfação.

No primeiro momento, o controle pode ser manual ou semiautomático.

O app deve registrar:

- cliente;
- problema identificado;
- origem do problema;
- data em que apareceu;
- responsável interno;
- se foi resolvido ou não;
- data de resolução;
- resumo do que aconteceu;
- link, print ou referência, se existir.

Com automação futura, o app pode:

- ler mensagens dos grupos;
- identificar mensagens sem resposta;
- detectar reclamações;
- detectar cobranças;
- detectar elogios;
- medir tempo médio de resposta;
- sugerir problemas a registrar;
- sinalizar risco de insatisfação.

O cuidado principal é não transformar qualquer conversa em problema. O app deve diferenciar:

- dúvida comum;
- pedido simples;
- solicitação de material;
- cobrança;
- reclamação;
- problema real;
- risco de relacionamento.

## Tela 1: Dashboard geral

Esta é a tela inicial do sistema.

Objetivo:

Mostrar, em poucos segundos, quais clientes precisam de atenção.

Conteúdo da tela:

- lista de clientes ativos;
- planejamento do período: entregue ou não;
- captação: realizada ou não;
- reunião de alinhamento: realizada ou não;
- NPS mais recente;
- problemas de WhatsApp em aberto;
- demandas importantes do ClickUp;
- atrasos principais;
- alertas de risco.

Formato visual recomendado:

- tabela clara;
- filtros por período;
- checks visuais;
- datas visíveis;
- alertas discretos;
- clique no cliente para abrir a visão detalhada.

Exemplo de colunas:

| Cliente | Planejamento | Captação | Reunião | ClickUp | WhatsApp | NPS | Atenção |
|---|---|---|---|---|---|---|---|
| Ecoville | Entregue em 05/06 | Feita em 10/06 | Feita em 12/06 | 12 demandas | 1 problema | 9 | Baixa |
| CCTAM | Não entregue | Feita em 11/06 | Não feita | 7 demandas | OK | 8 | Alta |

O dashboard deve evitar excesso de números. O foco é clareza.

## Tela 2: Cliente

Esta é a tela mais importante do sistema.

Objetivo:

Concentrar tudo que a Vizantu precisa saber sobre um cliente.

Conteúdo da tela:

- dados básicos do cliente;
- responsáveis internos;
- entregas do mês;
- planejamento;
- captação;
- reuniões;
- demandas do ClickUp;
- problemas de WhatsApp;
- NPS;
- histórico recente;
- próximos compromissos;
- memória do cliente.

Blocos recomendados:

### Resumo do cliente

- nome;
- segmento;
- responsáveis;
- canais principais;
- frequência de entrega;
- último planejamento;
- última reunião;
- última captação;
- NPS mais recente.

### Checks do período

- planejamento entregue;
- captação feita;
- reunião feita;
- relatório entregue;
- NPS enviado;
- problemas resolvidos.

### Demandas do ClickUp

- tarefas com tag de planejamento;
- tarefas em aprovação do cliente;
- tarefas atrasadas;
- tarefas em problema externo/interno;
- tarefas aguardando material.

### Reuniões recentes

- data;
- resumo;
- decisões;
- pendências;
- link da transcrição.

### Problemas recentes

- problema;
- origem;
- data;
- resolvido ou não;
- responsável.

### Histórico

Linha do tempo com:

- reuniões;
- planejamentos;
- captações;
- NPS;
- problemas;
- entregas relevantes;
- decisões importantes.

## Tela 3: Entregas

Objetivo:

Controlar as entregas principais por data e check.

Essa tela deve ser simples e rápida de atualizar.

Campos:

- cliente;
- tipo de entrega;
- período;
- data prevista;
- entregue ou não entregue;
- data real;
- link;
- observação.

Tipos de entrega:

- planejamento;
- captação;
- reunião de alinhamento;
- relatório;
- NPS;
- revisão estratégica;
- entrega extraordinária.

Visões úteis:

- entregas da semana;
- entregas do mês;
- entregas atrasadas;
- entregas por cliente;
- entregas não realizadas.

Regra:

Não criar status intermediários. O check é o controle principal.

## Tela 4: ClickUp

Objetivo:

Mostrar o que está acontecendo no ClickUp sem tirar a execução de lá.

Conteúdo:

- tarefas por cliente;
- tarefas por tag;
- tarefas do planejamento;
- tarefas atrasadas;
- tarefas em aprovação do cliente;
- tarefas aguardando material;
- tarefas em problema;
- responsáveis;
- datas de entrega.

Ações possíveis:

- abrir tarefa no ClickUp;
- vincular tarefa a uma entrega do app;
- identificar tarefas sem tag;
- identificar demandas do planejamento;
- filtrar por cliente e período.

O app não precisa editar todo o ClickUp. A prioridade é leitura, organização e vínculo.

## Tela 5: Reuniões

Objetivo:

Centralizar as reuniões com clientes e transformar transcrições em memória operacional.

Conteúdo:

- lista de reuniões;
- cliente;
- data;
- participantes;
- link do Meet;
- link da transcrição;
- resumo;
- decisões;
- pendências;
- próximos passos;
- demandas sugeridas.

Ações possíveis:

- abrir transcrição original;
- vincular reunião ao cliente;
- confirmar resumo;
- transformar pendência em entrega;
- criar demanda no ClickUp;
- vincular demanda existente do ClickUp;
- marcar reunião como realizada no checklist.

Essa tela é uma das fontes mais importantes para o app, porque a reunião contém contexto que não aparece no ClickUp.

## Tela 6: WhatsApp e problemas

Objetivo:

Acompanhar problemas reais que aparecem nos grupos dos clientes.

Conteúdo:

- problemas abertos;
- problemas resolvidos;
- cliente;
- origem;
- data;
- responsável;
- tempo de resolução;
- resumo;
- impacto;
- relação com alguma demanda do ClickUp.

Classificações úteis:

- dúvida;
- pedido;
- cobrança;
- reclamação;
- problema operacional;
- problema de entrega;
- risco de satisfação.

Ações possíveis:

- registrar problema;
- marcar como resolvido;
- vincular a uma tarefa do ClickUp;
- vincular a uma reunião;
- registrar observação;
- gerar alerta para gestão.

## Tela 7: NPS e satisfação

Objetivo:

Acompanhar a satisfação dos clientes de forma quantitativa e qualitativa.

Conteúdo:

- pesquisas enviadas;
- respostas recebidas;
- nota;
- comentário;
- evolução do cliente;
- clientes sem resposta;
- clientes com risco;
- relação com problemas recentes.

O app deve cruzar NPS com:

- reclamações no WhatsApp;
- pendências de reunião;
- atrasos de entrega;
- problemas no ClickUp;
- ausência de captação ou planejamento.

Exemplo de leitura útil:

Um cliente pode dar nota 8, mas ter cobrado atraso em três reuniões seguidas. O app precisa ajudar a enxergar esse tipo de risco.

## Tela 8: Calendário operacional

Objetivo:

Mostrar os compromissos operacionais da Vizantu.

Não é calendário editorial.

Mostra:

- reuniões com clientes;
- datas previstas de planejamento;
- datas de captação;
- envio de relatório;
- envio de NPS;
- revisão mensal;
- compromissos internos ligados a clientes.

Visões:

- semana;
- mês;
- cliente;
- tipo de entrega;
- atrasados.

O calendário operacional responde:

**O que a Vizantu precisa cumprir esta semana para manter os clientes bem atendidos?**

## Tela 9: Memória do cliente

Objetivo:

Permitir consulta rápida ao histórico e contexto do cliente.

Essa tela pode funcionar como busca inteligente.

Fontes:

- reuniões;
- transcrições;
- ClickUp;
- entregas;
- WhatsApp;
- NPS;
- relatórios;
- planejamentos.

Perguntas que o sistema deve responder:

- O que foi combinado na última reunião?
- Quais pendências ainda estão abertas?
- Quais cobranças o cliente fez recentemente?
- Quais planejamentos já foram entregues?
- Quais problemas aconteceram nos últimos meses?
- O que foi prometido e ainda não virou demanda?
- Qual foi o último NPS?
- Quais são os sinais de insatisfação?

Essa tela transforma o app em uma memória operacional da Vizantu.

## Tela 10: Configurações

Objetivo:

Configurar integrações, clientes, tags e regras do app.

Conteúdo:

- clientes ativos;
- usuários internos;
- responsáveis por cliente;
- tipos de entrega;
- cadência esperada por cliente;
- tags do ClickUp reconhecidas;
- conexão com ClickUp;
- conexão com Google Drive/Docs;
- conexão com ferramenta de NPS;
- regras de alerta;
- permissões.

Configurações importantes:

- quais clientes aparecem no dashboard;
- qual cadência cada cliente precisa cumprir;
- quais tags do ClickUp entram no painel;
- onde ficam as transcrições no Drive;
- como identificar o cliente pelo nome do arquivo;
- quais eventos geram alerta.

## Fluxo operacional semanal

O uso ideal do app na rotina semanal:

1. Gestão abre o dashboard geral.
2. Verifica clientes com entregas não realizadas.
3. Confere planejamentos, captações e reuniões da semana.
4. Abre clientes que exigem atenção.
5. Confere demandas do ClickUp por tag.
6. Confere reuniões recentes e pendências.
7. Verifica problemas de WhatsApp.
8. Atualiza checks quando algo foi entregue.
9. Cria ou vincula demandas no ClickUp quando necessário.

## Fluxo após uma reunião com cliente

1. Reunião acontece no Google Meet.
2. Transcrição vai para o Google Docs/Drive.
3. O app importa ou identifica a transcrição.
4. O app vincula a reunião ao cliente.
5. O app gera resumo, decisões e pendências.
6. Gestão revisa o resumo.
7. Pendências viram checks, entregas ou tarefas no ClickUp.
8. A reunião entra no histórico do cliente.

## Fluxo de planejamento

1. Planejamento é previsto para um cliente em uma data.
2. O app mostra esse compromisso no dashboard e no calendário operacional.
3. Quando o planejamento é entregue, alguém marca o check.
4. O app registra data real e link.
5. As demandas do planejamento são criadas no ClickUp.
6. Essas demandas recebem tags padronizadas.
7. O app lê as tarefas pelo ClickUp e conecta com o planejamento.
8. Gestão acompanha se o planejamento virou execução.

## Fluxo de captação

1. Captação é prevista no app.
2. O dashboard mostra a data.
3. Quando a captação acontece, alguém marca como entregue.
4. O app registra data real.
5. As demandas geradas pela captação são acompanhadas no ClickUp.
6. O cliente deixa de aparecer como sem material recente.

## Fluxo de problema no WhatsApp

1. Problema aparece no grupo.
2. Alguém registra manualmente no app ou o app sugere automaticamente no futuro.
3. Problema recebe cliente, data, resumo e responsável.
4. Se exigir produção, é vinculado ou transformado em tarefa no ClickUp.
5. Quando resolvido, é marcado como resolvido.
6. O app registra tempo de resolução.
7. O histórico do cliente recebe esse evento.

## Indicadores do app

Indicadores úteis:

- planejamentos previstos;
- planejamentos entregues;
- planejamentos não entregues;
- captações previstas;
- captações realizadas;
- reuniões previstas;
- reuniões realizadas;
- problemas abertos;
- problemas resolvidos;
- tempo médio de resposta no WhatsApp;
- tempo médio de resolução de problemas;
- NPS por cliente;
- clientes sem NPS recente;
- demandas do planejamento no ClickUp;
- tarefas atrasadas no ClickUp com tag relevante;
- tarefas em aprovação do cliente há muito tempo;
- tarefas aguardando material.

## Alertas

O app deve gerar alertas simples e úteis.

Alertas possíveis:

- planejamento não entregue na data prevista;
- captação não realizada na data prevista;
- reunião não realizada;
- cliente sem reunião recente;
- cliente sem captação recente;
- problema de WhatsApp aberto há muitos dias;
- NPS baixo;
- cliente sem resposta de NPS;
- tarefa do planejamento atrasada no ClickUp;
- muitas tarefas em aprovação do cliente;
- pendência de reunião sem ação.

## Modelo de dados inicial

Entidades principais:

### Cliente

- id;
- nome;
- slug;
- status ativo/inativo;
- responsáveis internos;
- cadência de planejamento;
- cadência de reunião;
- cadência de captação;
- link da pasta no Drive;
- lista ou espaço correspondente no ClickUp.

### Entrega

- id;
- cliente;
- tipo;
- período;
- data prevista;
- entregue;
- data real;
- link;
- observação.

### Tarefa do ClickUp

- id no ClickUp;
- nome;
- cliente;
- tags;
- status no ClickUp;
- responsável;
- due date;
- link;
- entrega vinculada.

### Reunião

- id;
- cliente;
- data;
- participantes;
- link do Meet;
- link da transcrição;
- resumo;
- decisões;
- pendências;
- próximos passos;
- demandas sugeridas.

### Problema

- id;
- cliente;
- origem;
- data de abertura;
- resumo;
- responsável;
- resolvido;
- data de resolução;
- tarefa do ClickUp vinculada;
- impacto.

### NPS

- id;
- cliente;
- data de envio;
- respondido;
- nota;
- comentário;
- classificação;
- alerta de risco.

## MVP recomendado

O MVP deve começar pequeno para evitar complexidade desnecessária.

### Fase 1

Telas essenciais:

1. Dashboard geral.
2. Tela do cliente.
3. Entregas.
4. ClickUp.
5. Reuniões.

Funcionalidades:

- cadastro de clientes;
- criação de entregas com data e check;
- dashboard com checks por cliente;
- leitura básica do ClickUp por tags;
- cadastro/importação inicial de reuniões;
- link manual para transcrições do Drive;
- histórico básico por cliente.

### Fase 2

Adicionar:

- Google Drive/Docs automático;
- resumo automático de reuniões;
- extração de decisões e pendências;
- criação ou sugestão de tarefas no ClickUp;
- calendário operacional;
- módulo de problemas do WhatsApp;
- NPS.

### Fase 3

Adicionar:

- leitura automatizada de WhatsApp, se tecnicamente viável;
- análise de sentimento;
- memória inteligente do cliente;
- perguntas sobre histórico;
- alertas preditivos;
- relatórios executivos.

## Critérios de sucesso

O app será útil se a gestão conseguir responder rapidamente:

- quais clientes estão em dia;
- quais clientes estão sem planejamento entregue;
- quais clientes estão sem captação recente;
- quais clientes não tiveram reunião;
- quais clientes têm problema aberto;
- quais clientes estão com risco de insatisfação;
- quais demandas do planejamento estão no ClickUp;
- quais pendências surgiram nas últimas reuniões;
- o que foi prometido e ainda não virou tarefa;
- onde a Vizantu precisa agir nesta semana.

## Decisão de produto

A decisão mais importante é manter o app simples.

O ClickUp organiza a produção.

O app organiza a visão de gestão, relacionamento e compromisso com o cliente.

Sempre que surgir uma dúvida sobre adicionar uma funcionalidade, a pergunta deve ser:

**Isso ajuda a gestão a entender se o cliente está sendo bem cuidado e se a Vizantu está cumprindo o que precisa cumprir?**

Se a resposta for sim, pode entrar no app.

Se a resposta for apenas "isso ajuda a controlar mais uma tarefa", provavelmente deve continuar no ClickUp.
