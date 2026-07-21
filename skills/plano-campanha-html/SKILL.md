---
name: plano-campanha-html
description: >-
  Cria planos de campanha e apresentações de estratégia completos em HTML (arquivo único,
  autocontido, pronto para enviar ao cliente e imprimir em PDF) no padrão visual premium da
  Vizantu. Use esta skill SEMPRE que o usuário pedir um "plano de campanha", "plano mensal",
  "apresentação de estratégia", "documento de entrega", "plano de gestão de marca" ou enviar
  materiais de um cliente (manual de marca, logo, roteiros aprovados, copies, cronograma,
  estratégia) pedindo para consolidar tudo em um documento — mesmo que não mencione HTML
  explicitamente. Também use quando o usuário citar clientes da Vizantu e pedir "monta o plano",
  "faz a entrega", "consolida os roteiros" ou algo parecido.
---

# Plano de Campanha em HTML

Esta skill produz um **plano de campanha completo em um único arquivo HTML autocontido** — fontes e imagens embutidas em base64, zero dependências externas — que funciona como documento de entrega premium para o cliente: navegável no browser, responsivo no celular e imprimível em PDF (A4) pelo botão da própria página.

O plano não é só apresentação: é o **instrumento de aprovação**. O fluxo real da Vizantu é subir o HTML na plataforma **Vizantu Planos**, enviar o link ao cliente, e o cliente avaliar cada conteúdo ali mesmo — aprovando ou pedindo ajuste. **A interface de aprovação é injetada automaticamente pela plataforma no upload** (ela detecta cada conteúdo pelos blocos `article.script[id]` / `section.band`). Portanto **não** coloque caixas de aprovação, barra fixa nem script de aprovação no HTML — só estruture cada conteúdo como um bloco detectável com título claro (detalhes em `references/estrutura.md`).

Regras fixas de apresentação:

- **Nome do documento:** `PLANO DE [MÊS] | [PROJETO]` em caixa alta — no `<title>`, na topbar e no rodapé.
- **Respiro:** seções bem separadas (o template já traz os espaçamentos); o leitor precisa perceber cada mudança de assunto sem esforço.
- A seção visual mostra **como o público vai ver o projeto**, não regras internas de design.

O padrão de qualidade é o plano PGRS da Parceria Ambiental. A lógica dele deve ser preservada; a pele visual deve ser reconstruída para cada cliente.

## Papéis que você assume

Estrategista de marketing, diretor de criação, especialista em mídia paga e designer digital sênior — ao mesmo tempo. Isso significa: as seções estratégicas (objetivo, funil, tráfego, resultados) precisam ter substância real derivada do briefing, não texto genérico; e o design precisa parecer feito sob medida para a marca, não um template preenchido.

## Insumos esperados

O usuário normalmente envia:

1. **Marca do cliente** — manual de marca/brand book, logo, site, redes sociais.
2. **Roteiros/copies aprovados** — o conteúdo que será publicado.
3. **Datas** — período da campanha, data da primeira gravação, frequência.
4. **Estratégia** — briefing, objetivo comercial, público, região, destino de conversão.
5. **Tipo de serviço** — campanha pontual, gestão de marca mensal, lançamento etc.

Se faltar algo essencial (paleta de cores, datas, destino da conversão), pergunte antes de gerar — um plano com dados inventados quebra a confiança do cliente. Se houver divergência entre o site e o manual de marca, **o manual de marca tem prioridade**: o site pode estar desatualizado.

## Regra central: conteúdo aprovado é intocável

Os roteiros, copies, legendas, headlines, CTAs, letterings, textos de slides, falas, cenas, direcionamentos e observações de produção aprovados entram no HTML **integralmente e sem reescrita**. Não resuma, não corrija, não reorganize, não "melhore" e não elimine nenhuma linha. O motivo: esse material já passou pelo cliente; qualquer alteração silenciosa vira retrabalho, quebra de confiança ou conteúdo publicado errado.

Mecanismo de integridade (copie do padrão da referência):

1. Inclua ao final do `<body>` um `<template id="approved-source-verbatim">` com o texto-fonte aprovado, verbatim, em markdown.
2. Calcule o SHA-256 do arquivo-fonte dos roteiros (`python -c "import hashlib,sys;print(hashlib.sha256(open(sys.argv[1],'rb').read()).hexdigest())" arquivo.md`) e registre no rodapé: `Fonte dos roteiros: SHA-256 <hash>`.
3. Marque cada material com a tag `Status: aprovado pelo usuário` (ou o status real informado).

O que você **pode** criar livremente: títulos das seções, leads, textos estratégicos, organização visual, mockups — tudo que não é material aprovado.

## Processo

### 1. Ler e mapear os materiais

Leia tudo que foi enviado. Extraia: paleta (hex exatos do manual), tipografia da marca, tom de voz, tagline/assinatura, handle do Instagram, cidade/região, nome de quem atende, e a lista completa de materiais aprovados com formato (vídeo/estático/carrossel), etapa do funil e data.

### 2. Construir o design system do cliente

Leia [references/design-system.md](references/design-system.md) e traduza a marca para os tokens semânticos do template. Não reproduza a paleta da Parceria Ambiental — ela é do cliente dela.

### 3. Montar o HTML

Parta de [assets/template-base.html](assets/template-base.html) — ele carrega toda a arquitetura CSS testada (grid, responsivo 980/680px, print A4, mockups de Instagram). Leia [references/estrutura.md](references/estrutura.md) para o blueprint seção por seção e as variações por tipo de serviço.

### 4. Embutir os assets

O arquivo final não pode depender de internet nem de arquivos externos:

- **Fonte**: a fonte padrão da Vizantu é **Poppins** — use em todos os planos, salvo pedido explícito em contrário. `python scripts/embed_font.py --family "Poppins" --weights 400,500,600,700 -o fonts.css` gera os blocos `@font-face` em base64 (Google Fonts). Cole no lugar do marcador `/* {{FONT_FACES}} */` e use `'Poppins'` no `font-family`. Só troque de fonte se o usuário pedir; se a fonte pedida não estiver no Google Fonts e o usuário não fornecer os arquivos, use a alternativa mais próxima e avise.
- **Logo e imagens**: `python scripts/embed_image.py caminho/logo.png` imprime o data URI para usar no `src`.

### 5. Controle de qualidade antes de entregar

Abra o arquivo no browser (preview) e verifique:

- [ ] Todos os roteiros aprovados presentes, verbatim — confira por amostragem contra a fonte.
- [ ] Cada mockup de Instagram reflete o material correto (headline/primeira fala no visual, legenda real na caption, formato certo: reel 4:5 / quadrado 1:1 / carrossel).
- [ ] Números do hero batem com o plano (dias, quantidade de conteúdos, frequência, data de gravação).
- [ ] Datas do cronograma batem com as tags de data dos roteiros e com o índice.
- [ ] Âncoras da navegação funcionam; nada da paleta antiga sobrou; contraste legível em todos os blocos.
- [ ] **Nenhuma caixa de aprovação manual** no HTML (sem `.approval`, `approval-bar`, `btn-ok/btn-adjust`, `textarea` ou script de `localStorage`) — a plataforma Vizantu Planos injeta a aprovação por conteúdo no upload. Cada material é um `article.script` com `id` único e header com título.
- [ ] **Todos os URLs são links clicáveis** (`<a href target="_blank">`): links de referência/trend no direcionamento e o bloco **Referências** quando o material cita fontes.
- [ ] Teste responsivo (mobile) e o botão Imprimir/PDF.
- [ ] Rodapé com período, hash SHA-256 e logo.

Salve o arquivo como `plano-<campanha>-<cliente>.html` na pasta de saída que o usuário indicar (ou junto aos materiais do cliente).

## Arquivos desta skill

| Arquivo | Quando ler |
|---|---|
| `references/estrutura.md` | Sempre — blueprint das seções, componentes e variações por serviço |
| `references/design-system.md` | Sempre — como traduzir a marca do cliente para os tokens |
| `assets/template-base.html` | Sempre — esqueleto HTML/CSS de partida |
| `scripts/embed_font.py` | Para embutir a fonte da marca |
| `scripts/embed_image.py` | Para embutir logo/fotos |
