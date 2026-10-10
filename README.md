# Documentação Vizantu

Base de conhecimento da Vizantu: clientes, operação, marca e skills. É a fonte de contexto para todos os projetos da empresa e será levada para o Vizantu Tarefas quando estiver consolidada.

## Mapa

| Pasta | O que tem |
|---|---|
| [`clientes/`](clientes/README.md) | Um contexto por cliente (`context-[slug].md`) e as entregas datadas. O índice com status fica em `clientes/README.md`. |
| [`operacao/`](operacao/) | Como a Vizantu funciona: contexto atual, descobertas, decisões aprovadas, POPs, automações, backlog e a proposta do app de controle operacional. Diagramas em `operacao/fluxos/`. |
| [`brand/`](brand/README.md) | Ativos oficiais da marca Vizantu. |
| [`skills/`](skills/README.md) | Skills da Vizantu para agentes. |

`CLAUDE.md` (com `AGENTS.md` apontando para ele) e `SKILL.md` são as instruções para os agentes de IA que trabalham neste repositório.

## Arquivos de operação

- `operacao/01-contexto-atual.md`: estado atual da operação e entendimento consolidado;
- `operacao/02-descobertas-da-conversa.md`: anotações incrementais do que for sendo aprendido;
- `operacao/03-decisoes-aprovadas.md`: decisões validadas;
- `operacao/04-pops.md`: procedimentos operacionais padrão;
- `operacao/05-automacoes.md`: ideias, requisitos e automações aprovadas;
- `operacao/06-backlog-de-otimizacao.md`: oportunidades, problemas e priorização;
- `operacao/07-app-controle-operacional-vizantu.md`: proposta do app de controle operacional.

## Regra de manutenção

- tudo que for relevante sobre a Vizantu deve ser registrado;
- tudo que for aprovado entra em `operacao/03-decisoes-aprovadas.md`;
- POPs aprovados ou em definição entram em `operacao/04-pops.md`;
- automações discutidas entram em `operacao/05-automacoes.md`;
- mudou o contexto de um cliente, atualiza o cabeçalho do context e a linha dele em `clientes/README.md`.
