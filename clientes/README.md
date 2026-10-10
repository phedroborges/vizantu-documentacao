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
| `tawper` | Tawper | Importação e distribuição de mangueiras e conexões hidráulicas premium | Monte Aprazível/SP | 🟡 Parcial | Tawper | [context](tawper/context-tawper.md) |
| `terranet` | TerraNet | Provedor de internet rural | Sudoeste de Goiás | ✅ Completo | Terranet | [context](terranet/context-terranet.md) |
| `vizantu` | Vizantu | Gestão de marcas | Mineiros/GO | 🟡 Parcial | Vizantu | [context](vizantu/context-vizantu.md) |
| `wainny` | Dra. Wainny | Saúde feminina — ultrassom e morfológico | Mineiros/GO | ✅ Completo | Dra Wainny | [context](wainny/context-wainny.md) |

## Projetos do Vizantu Tarefas sem pasta aqui

| Projeto | Situação |
|---------|----------|
| Global Energia | Fica sem contexto (decisão do Phedro em 2026-10-10) |
| House Flipping | Fica sem contexto (decisão do Phedro em 2026-10-10) |
| VINT3 | Fica sem contexto por enquanto (decisão do Phedro em 2026-10-10) |
| Sanfér Produções | Phedro está alinhando a história com o cliente; criar quando ele enviar |
| LAF | A criar a partir do guia e das fontes do Vizantu Tarefas |
| Target Informações | A criar a partir do guia e das fontes do Vizantu Tarefas |

Mundo Criativo tem pasta, mas o contexto ainda é o modelo vazio: aguardando material do Phedro.

## Padrão de documentação do cliente

Todo `context-[slug].md` segue o modelo [`_modelo-context.md`](_modelo-context.md): o cabeçalho abaixo e sempre as mesmas dez seções, na mesma ordem e com o mesmo nome.

| # | Seção | O que entra | Bloco do guia no Vizantu Tarefas |
|---|-------|-------------|----------------------------------|
| 1 | Ficha do cliente | Cadastro, contatos, ClickUp, time | — |
| 2 | Quem é e o que faz | Negócio, história, produtos, mercado, concorrentes | Quem é |
| 3 | O que o cliente quer | Objetivos, metas, momento atual | O que ele quer |
| 4 | Público | Perfis, dores, objeções | Como o trabalho é feito |
| 5 | Marca e tom de voz | Posicionamento, valores, identidade verbal e visual | Como o trabalho é feito |
| 6 | Estratégia e conteúdo | Estratégia, pilares, formatos, cadência, calendário | Como o trabalho é feito |
| 7 | Como lidar com o cliente | Pessoas do cliente, quem aprova, pontos de atenção | Como lidar |
| 8 | Operação | Regras operacionais, fluxo no ClickUp, contrato | Como o trabalho é feito |
| 9 | Histórico e entregas | Fases, entregas aprovadas, status | — |
| 10 | Referências e fontes | Referências de mercado e origem das informações | Como o trabalho é feito |

Regras:

- As dez seções existem em todo contexto. Seção sem informação fica com `> A documentar.`, nunca é apagada.
- O conteúdo específico de cada cliente entra como subseção (`###`) dentro da seção certa. Não criar seção nova de nível `##`.
- Informação nova que não parece caber em nenhuma seção vai para a mais próxima, como subseção.

### Cabeçalho

Este bloco abre o arquivo e é o que o Vizantu Tarefas usa para saber de qual projeto é o documento:


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
