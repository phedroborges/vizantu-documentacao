# Clientes

Índice único dos clientes documentados. Cada pasta `clientes/[slug]/` tem um `context-[slug].md` (contexto completo) e, quando houver, as entregas datadas (`[data]-*.md|html`).

Conferido com o Vizantu Tarefas em 2026-10-10.

| Slug | Cliente | Segmento | Cidade | Documentação | Projeto no Vizantu Tarefas | Arquivo |
|------|---------|----------|--------|--------------|----------------------------|---------|
| `casa-caramelo` | Casa Caramelo | Pet shop e clínica veterinária | Mineiros/GO | 🟡 Parcial | Casa Caramelo | [context](casa-caramelo/context-casa-caramelo.md) |
| `cctam` | CCTAM | Clube de tiro esportivo | Mineiros/GO | ✅ Completo | — | [context](cctam/context-cctam.md) |
| `dr-lourival` | Dr. Lourival Lobo | Política — candidato a Deputado Estadual GO 2026 | Mineiros/GO | ✅ Completo | Campanha do Dr Lourival | [context](dr-lourival/context-dr-lourival.md) |
| `ecomodular` | Eco Modular | Fabricante de tijolos ecológicos | Mineiros/GO | ✅ Completo | — | [context](ecomodular/context-ecomodular.md) |
| `ecoville` | Ecoville Confresa | Franquia de produtos de limpeza | Confresa/MT | ✅ Completo | — | [context](ecoville/context-ecoville.md) |
| `ena` | ENA | Educação — escola particular | Mineiros/GO | ✅ Completo | — | [context](ena/context-ena.md) |
| `laura-rayane` | Laura Rayane | Política — vereadora | Mineiros/GO | ✅ Completo | Campanha Laura Rayane | [context](laura-rayane/context-laura-rayane.md) |
| `mundo-criativo` | Mundo Criativo | — | — | ⚠️ Template vazio | Mundo Criativo | [context](mundo-criativo/context-mundo-criativo.md) |
| `ohbra` | Ohbra Engenharia | Construtora com foco em financiamento habitacional | Mineiros/GO | ✅ Completo | — | [context](ohbra/context-ohbra.md) |
| `parceria-ambiental` | Parceria Ambiental | Consultoria ambiental | Mineiros/GO | ✅ Completo | Parceria Ambiental | [context](parceria-ambiental/context-parceria-ambiental.md) |
| `sangue-bom` | Projeto Sangue Bom | Projeto de extensão da UNIFIMES — banco de sangue canino | Mineiros/GO | ✅ Completo | — | [context](sangue-bom/context-sangue-bom.md) |
| `terranet` | TerraNet | Provedor de internet rural | Sudoeste de Goiás | ✅ Completo | Terranet | [context](terranet/context-terranet.md) |
| `wainny` | Dra. Wainny | Saúde feminina — ultrassom e morfológico | Mineiros/GO | ✅ Completo | Dra Wainny | [context](wainny/context-wainny.md) |

## Projetos do Vizantu Tarefas ainda sem pasta aqui

Global Energia, House Flipping, LAF, Sanfér Produções, Target Informações, Tawper, VINT3 e Vizantu.

## Cabeçalho padrão do context

Todo `context-[slug].md` começa com este bloco, que é o que o Vizantu Tarefas usa para saber de qual projeto é o documento:

```yaml
---
slug: ohbra
nome: "Ohbra Engenharia"
segmento: "Construtora com foco em financiamento habitacional"
cidade: "Mineiros/GO"
status_doc: completo        # completo | parcial | template
projeto_tarefas: null       # nome exato do projeto no Vizantu Tarefas, ou null se não existir lá
atualizado_em: 2026-05-28
---
```

Ao mudar o contexto de um cliente, atualizar `atualizado_em` e, se for o caso, `status_doc` e a linha dele na tabela acima.
