# Vizantu Documentação — Instruções para a IA

## O que é este projeto

Este é o repositório central de documentação da Vizantu. Aqui fica registrado tudo sobre a empresa: clientes, estratégias, processos, decisões e aprendizados. Está em construção e será transformado em algo maior.

**Nunca salvar documentação aqui proveniente de outros projetos técnicos como vizantu-os.**

---

## Estrutura

```
clientes/
  [slug]/
    context-[slug].md    ← contexto completo do cliente (SEMPRE ler antes de agir)
    [data]-*.html|md     ← relatórios e entregas

01-contexto-atual.md     ← estado atual da operação Vizantu
02-descobertas-da-conversa.md
03-decisoes-aprovadas.md
04-pops.md
05-automacoes.md
06-backlog-de-otimizacao.md
```

---

## Clientes com contexto documentado

| Slug | Cliente | Arquivo | Status |
|------|---------|---------|--------|
| `ecoville` | Ecoville Confresa — franquia produtos de limpeza, Confresa/MT | `clientes/ecoville/context-ecoville.md` | ✅ Completo |
| `cctam` | CCTAM — clube de tiro, Mineiros/GO | `clientes/cctam/context-cctam.md` | ✅ Completo |
| `ecomodular` | Eco Modular — tijolos ecológicos | `clientes/ecomodular/context-ecomodular.md` | ✅ Completo |
| `ohbra` | Ohbra Engenharia — financiamento habitacional | `clientes/ohbra/context-ohbra.md` | ✅ Completo |
| `dr-lourival` | Dr. Lourival Lobo — Deputado Estadual GO 2026 | `clientes/dr-lourival/context-dr-lourival.md` | ✅ Completo |
| `laura-rayane` | Laura Rayane — vereadora, Mineiros/GO | `clientes/laura-rayane/context-laura-rayane.md` | ✅ Completo |
| `wainny` | Dra. Wainny — saúde feminina e ultrassom | `clientes/wainny/context-wainny.md` | ✅ Completo |
| `casa-caramelo` | Casa Caramelo — pet shop e clínica veterinária | `clientes/casa-caramelo/context-casa-caramelo.md` | ⚠️ Template vazio |
| `terranet` | TerraNet — provedor de internet rural | `clientes/terranet/context-terranet.md` | ⚠️ Template vazio |
| `mundo-criativo` | Mundo Criativo | `clientes/mundo-criativo/context-mundo-criativo.md` | ⚠️ Template vazio |
| `ena` | ENA | `clientes/ena/context-ena.md` | ⚠️ Template vazio |

---

## Regras

1. **Sempre ler o context-[slug].md antes de gerar qualquer conteúdo, estratégia ou análise para um cliente.**
2. Qualquer aprendizado novo revelado na conversa → atualizar o context imediatamente.
3. Decisões aprovadas → registrar em `03-decisoes-aprovadas.md`.
4. Novos clientes → criar pasta `clientes/[slug]/` com `context-[slug].md`.
