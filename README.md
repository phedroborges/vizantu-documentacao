# Documentacao Vizantu

Este diretorio concentra a documentacao viva da operacao da Vizantu.

Objetivos:
- registrar o funcionamento atual da operacao;
- consolidar tudo o que for aprendido nesta conversa;
- documentar decisoes aprovadas;
- estruturar POPs;
- mapear e detalhar automacoes;
- manter historico de evolucao operacional.

Estrutura de clientes:
- `clientes/[slug]/context-[slug].md`: contexto completo do cliente (histórico, marca, estratégia, tom de voz, regras operacionais)
- `clientes/[slug]/[data]-relatorio-*.html`: relatórios de fechamento em HTML
- `clientes/[slug]/[data]-relatorio-*.md`: versões em markdown dos relatórios

Clientes ativos:
- `clientes/cctam/` — CCTAM (clube de tiro esportivo, Mineiros/GO)
- `clientes/ecomodular/` — Eco Modular (fabricante de tijolos ecológicos, Mineiros/GO)
- `clientes/ohbra/` — Ohbra Engenharia (construtora com foco em financiamento habitacional, Mineiros/GO)

Arquivos base:
- `01-contexto-atual.md`: estado atual da operacao e entendimento consolidado;
- `02-descobertas-da-conversa.md`: anotacoes incrementais do que for sendo aprendido;
- `03-decisoes-aprovadas.md`: decisoes validadas durante a conversa;
- `04-pops.md`: procedimentos operacionais padrao;
- `05-automacoes.md`: ideias, requisitos e automacoes aprovadas;
- `06-backlog-de-otimizacao.md`: oportunidades, problemas e priorizacao.

Regra de manutencao:
- tudo que for relevante sobre a Vizantu deve ser registrado;
- tudo que for aprovado deve entrar explicitamente em `03-decisoes-aprovadas.md`;
- POPs aprovados ou em definicao devem ser registrados em `04-pops.md`;
- automacoes discutidas devem ser registradas em `05-automacoes.md`.
