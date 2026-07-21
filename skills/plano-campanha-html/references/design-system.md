# Design system — traduzindo a marca do cliente para o template

O template usa tokens semânticos em `:root`. Sua tarefa é mapear a paleta do manual de marca para esses papéis — não é buscar cores "parecidas" com a referência, é entender a função de cada token:

| Token | Papel | Na referência (Parceria Ambiental) |
|---|---|---|
| `--accent` | Cor de destaque/ação: strongs do h1, bordas, pontos, números, CTA visual | verde-folha #AAD241 |
| `--soft` | Fundo suave da marca: bands alternadas, blocos de citação | creme #FAFED9 |
| `--primary` | Cor institucional: eyebrows, números de seção, títulos de tabela secundários | verde #2D6A4F |
| `--deep` | Fundo escuro: hero, bands deep, headers de tabela, blocos de gravação | verde-profundo #1B2B1F |
| `--paper` | Fundo dos cards e da página | branco / #F5F7F1 |
| `--ink` | Texto principal | #173226 |
| `--muted` | Texto secundário | #5E6E64 |
| `--line` | Bordas e divisórias | #DDE7D7 |

## Como mapear

1. **`--deep`** é a cor mais escura e "séria" da paleta do cliente. Se o manual não tem uma cor escura, derive uma versão bem escura da cor institucional (ex.: HSL com luminosidade ~12–18%). O hero precisa de peso.
2. **`--accent`** é a cor mais viva — a que a marca usa para chamar atenção. Precisa ter contraste legível sobre `--deep` E funcionar como fundo com texto `--deep` por cima (o bloco `recording-date` e o `flow-node.accent` dependem disso).
3. **`--soft`** é um tom quase-branco derivado da paleta (creme, off-white, tom pastel da marca). Se não existir, gere um tint bem claro (~96% luminosidade) da cor institucional.
4. **`--ink` e `--muted`** ficam melhores levemente tingidos com o hue da marca do que preto/cinza puros — é isso que faz a página inteira "cheirar" à marca.
5. Derive `--line` como um tom dessaturado e claro do hue da marca.

Confira contraste dos pares críticos: texto claro sobre `--deep`; `--accent` sobre `--deep`; `--deep` sobre `--accent`; `--muted` sobre `--paper`. Se algum par falhar na leitura, ajuste luminosidade do token, não abandone a estrutura.

## Tipografia

- **Fonte padrão da Vizantu: Poppins.** Use Poppins em todos os planos, salvo pedido explícito em contrário do usuário. Embuta via `python scripts/embed_font.py --family "Poppins" --weights 400,500,600,700 -o fonts.css` (Google Fonts) e use `--font-family: 'Poppins'` no template. O template já usa os quatro pesos.
- Só troque a fonte se o usuário pedir outra explicitamente. Nesse caso: se estiver no Google Fonts, embuta pelo mesmo script; se não estiver, peça os arquivos ao usuário ou use a alternativa mais próxima e registre a substituição no texto de entrega.
- Mantenha a hierarquia do template: títulos em peso 500 (o tamanho grande já dá o peso), ênfases e números em 600–700.

## Logo: obedeça a página de "aplicação sobre fundos"

Antes de colocar o logo no hero e no rodapé (fundos escuros), procure no manual a página de aplicação sobre fundos e use **a versão que o manual designa para fundo escuro**. Muitos manuais proíbem versões em negativo (preto) ou em positivo (branco) quando a versão colorida tem contraste suficiente — nesse caso, o logo colorido vai direto sobre o fundo escuro. **Nunca fabrique uma versão branca/negativa recolorindo o logo**: além de frequentemente violar o manual, a silhueta branca funde as letras e destrói a legibilidade de wordmarks bold. Se o manual exigir versão monocromática e ela não estiver disponível em boa qualidade, peça o arquivo ao usuário.

Ao extrair o logo de um PDF, prefira as imagens embutidas (resolução nativa) às páginas renderizadas, remova o fundo por chroma-key com cuidado e suavize o canal alfa (blur ~0.5px) para eliminar serrilhado do recorte.

## Personalidade além da cor

Re-skinnar não é só trocar hex. Ajuste os detalhes que carregam personalidade:

- **Acentos gráficos dos mockups** (`.ig-visual::before/::after`): a referência usa barra lateral + círculo orgânico porque a marca é "orgânica e sólida". Uma marca geométrica pede ângulos; uma marca elegante pede linhas finas; uma campanha política pede a estrela/símbolo do partido estilizado. Redesenhe.
- **Raio de borda**: a referência é quase reta (4–7px) — sóbria. Marca jovem/leve tolera raios maiores; marca jurídica/médica pede retas.
- **Emojis e assinatura**: use a assinatura/tagline real do cliente no `hero-note` e no `ig-signature`; os emojis das legendas vêm do material aprovado (não adicione nem remova).
- **Tom dos textos estratégicos**: escreva os leads e h2 no tom de voz do manual (próximo? técnico? provocador?). O h1 do hero deve soar como a marca falaria.

## O que não mudar

A engenharia do template está testada — preserve: os breakpoints (980px, 680px), o CSS de print (A4, quebras por roteiro, mockup centralizado), o sticky do mockup no desktop, o `scroll-margin-top` das seções, o `table-scroll` para tabelas largas e o comportamento da topbar. Mudanças aqui quebram a experiência em celular ou o PDF.
