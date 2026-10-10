# Vizantu Documentação — Instruções para a IA

## O que é este projeto

Este é o repositório central de documentação da Vizantu e a base de conhecimento da empresa para todos os projetos. Aqui fica registrado tudo sobre a empresa: clientes, estratégias, processos, decisões e aprendizados. Quando estiver consolidado, este conteúdo será levado para o Vizantu Tarefas.

**Nunca salvar documentação aqui proveniente de outros projetos técnicos como vizantu-os.**

---

## Estrutura

```
clientes/
  README.md              ← índice único dos clientes (status e projeto no Vizantu Tarefas)
  [slug]/
    context-[slug].md    ← contexto completo do cliente (SEMPRE ler antes de agir)
    [data]-*.html|md     ← relatórios e entregas

operacao/
  01-contexto-atual.md   ← estado atual da operação Vizantu
  02-descobertas-da-conversa.md
  03-decisoes-aprovadas.md
  04-pops.md
  05-automacoes.md
  06-backlog-de-otimizacao.md
  07-app-controle-operacional-vizantu.md
  fluxos/                ← diagramas dos fluxos (SVG de origem + PNG exportado)

brand/                   ← ativos oficiais da marca Vizantu
skills/                  ← skills da Vizantu para agentes
```

---

## Clientes

A lista de clientes, o status de cada contexto e o projeto correspondente no Vizantu Tarefas ficam em `clientes/README.md`. Não manter outra lista de clientes em nenhum outro arquivo.

Todo `context-[slug].md` começa com um cabeçalho padrão (`slug`, `nome`, `segmento`, `cidade`, `status_doc`, `projeto_tarefas`, `atualizado_em`), descrito em `clientes/README.md`.

---

## Regras

1. **Sempre ler o context-[slug].md antes de gerar qualquer conteúdo, estratégia ou análise para um cliente.**
2. Qualquer aprendizado novo revelado na conversa → atualizar o context imediatamente, junto com o `atualizado_em` do cabeçalho.
3. Decisões aprovadas → registrar em `operacao/03-decisoes-aprovadas.md`.
4. Novos clientes → criar pasta `clientes/[slug]/` com `context-[slug].md` (com o cabeçalho padrão) e adicionar a linha em `clientes/README.md`.
5. Nada solto na raiz: documento de operação vai em `operacao/`, de cliente em `clientes/[slug]/`.
