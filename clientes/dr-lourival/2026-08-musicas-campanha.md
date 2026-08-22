# Músicas de Campanha — Dr. Lourival Lobo
**Fase 3 — Campanha Oficial | Agosto de 2026 | Versão 3**
Vizantu | 5 faixas com objetivo definido + prompt de Suno

**Número: 20777** — cantado "vinte, sete sete sete"

---

## O que mudou na v3

**1. A fonética estava errada e foi refeita do zero.**
Escrever "doto" no lugar de "doutor" matou as músicas. O jeito certo é o do jingle da praça: **português normal, trocando só a palavra específica que o Suno erra** — "praça" vira "prassa" e mais nada. Todas as letras abaixo estão em português correto.

Provável causa do reggaeton na faixa 1: `"Eli naum é dji gabinetchi"` não parece português para o modelo, parece sopa de língua latina. A fonética exagerada empurrou o Suno para o espanhol. Escrever certo já resolve metade.

**2. Cada faixa agora tem objetivo declarado.**

| # | Faixa | Objetivo |
|---|---|---|
| 1 | O Doutor Tá no Baile | Animação total |
| 2 | O Bebê Pegou a BR | Animar + bater na oposição |
| 3 | Quebra o Vaso | Esperança |
| 4 | Ô Trem Bão | Animação total |
| 5 | Esperança | Animação |

**3. Entrou graça, sarcasmo e chamada de galera em todas.**
Sempre no alvo certo: a obra, a placa, a fita cortada, a live. **Nunca uma pessoa, nunca um nome** — é a mesma regra que o jingle da praça respeita.

**4. Faixa 1 refeita como funk carioca de verdade.** Era reggaeton porque o prompt dizia só "brazilian funk". Agora pede tamborzão, surdo, timbal, apito, e exclui dembow explicitamente.

**5. Faixa 2 reescrita inteira.** "Chega aflita, sai tranquila" era fraco e não falava de pediatria. Agora é o bebê que pega a BR porque não tem UTI, com humor e pediatria concreta — bronquiolite, pneumonia, madrugada.

**6. Faixa 4 recalibrada pela análise do áudio de referência.**

---

## Análise do "Olha o Trem" — Jirayauai

Rodei a faixa no librosa. **Nada aqui é cópia** — são as características técnicas do gênero, que não são protegidas por direito autoral. Nenhuma melodia, letra ou levada específica foi reaproveitada.

| Medida | Valor | O que significa |
|---|---|---|
| **BPM** | **129** | Eu tinha posto 145. Estava errado |
| **Tom** | **Mi menor** | |
| **Sub 20–80 Hz** | **76,0%** | O sub-grave **é** a música |
| Bass 80–250 Hz | 16,6% | |
| **Mid 250 Hz–2 kHz** | **5,9%** | Praticamente vazio |
| High 2–8 kHz | 1,5% | Só vocal picotado e chimbal |
| Onsets | 2,47/s | Groove contínuo de colcheia, sem espaço |
| Salto no drop | **18x** | Sub vai de 6,5 para 117 em 5 segundos |
| Breaks | Silêncio quase total | Zera antes de cada drop |

**A conclusão que muda o prompt:** eletrofunk goiano não é "grave pesado". É um **mix oco** — o sub-grave carrega a melodia inteira e não existe nada no meio. Sem instrumento harmônico, sem pad, sem guitarra, sem teclado. Só sub, kick, voz gritada e vocal picotado no agudo.

Estrutura observada: build longo e quieto (35s) → drop violento → break → drop → **silêncio quase total (15s)** → drop final longo. O silêncio antes do drop é o que faz o drop bater.

---

## Fonética — a regra certa, e ela é curta

O Suno canta português brasileiro bem. **Não fonetize.** Só existe uma família de palavra que ele erra de verdade:

| Escreva assim | No lugar de | Por quê |
|---|---|---|
| **prassa** | praça | `ç` antes de a/o/u sai como "k" |
| **licensa** | licença | idem |
| **criansa** | criança | idem |
| **forsa** | força | idem |
| **comessa** | começa | idem |
| **vinte, sete sete sete** | 20777 | dígito o Suno não canta |

**O que NÃO trocar:** `ção` fica normal — medicação, plantão, coração, inauguração. O jingle da praça prova isso: só "prassa" foi trocada, todo o resto ficou em português correto.

Nas letras abaixo, as trocas já estão feitas.

---

## Configuração do Suno

- **Custom Mode** ligado, **Instrumental** desligado
- Modelo mais recente disponível
- **Weirdness** 15–25% · **Style Influence** 80–90%
- Gerar 4 versões de cada faixa
- Se sair em espanhol ou com sotaque errado, adicione `brazilian portuguese vocals` no style e `spanish, english, latin` no exclude

---

# FAIXA 1 — "O Doutor Tá no Baile"

**Objetivo: animação total.** É a faixa de energia pura — chant, baile, mão pro alto. Sem sermão.

**Gênero:** Funk carioca (tamborzão, beat 150)
**BPM:** 150 · **Tom:** Mi menor · **Duração:** 1'50"

> **Por que a v2 saiu reggaeton:** o prompt dizia só "brazilian funk", que o Suno resolve com dembow. Agora o style nomeia a percussão do tamborzão (surdo, timbal, atabaque) e o exclude derruba dembow, reggaeton e latin explicitamente.

## Letra

```
[Intro]
Alô Mineiros!
Tá tocando aonde?     (Em Mineiros!)
E é o doutor de quem?  (Das mães!)
Então vai!

[Refrão]
Ô, ô, ô, ô
Vinte, sete sete sete!
Ô, ô, ô, ô
É o doutor que resolve!
Ô, ô, ô, ô
Vinte, sete sete sete!
Levanta a mão, Mineiros
Que o pediatra tá no baile!

[Verso 1]
Ele não é de foto, ele é de plantão
Não corta fita, ele corta a inflamação
Não faz promessa em cima de caminhão
Ele faz diagnóstico e faz na mão

Toda mãe de Mineiros já sentou naquela sala
Entrou desesperada, saiu de alma lavada
Ele olha pro bebê e já sabe o que é
E a mãe que entrou no choro sai de pé

[Refrão]

[Verso 2]
UTI Neonatal, ó, cadê? Não tem!
Bebê pega estrada que nem caminhoneiro, ein
Transporte pro pré-natal, ó, cadê? Não tem!
Mãe vai a pé duas hora e não aparece ninguém

Mas eu não vim aqui só pra reclamar, não
Eu vim trazer quem resolve — bota a mão no chão!

[Ponte]
Ah, mas se ele ganhar ele para de atender?
Para nada, meu amor, ele vai é crescer
Consultório de manhã, Assembleia depois
Mesmo homem, mesma mão, agora fazendo por nóis

[Drop]
VINTE! SETE SETE SETE!
VINTE! SETE SETE SETE!
Grita, Mineiros!
VINTE! SETE SETE SETE!

[Refrão final]
```

## Prompt Suno

**Style of Music:**
```
Funk carioca, baile funk from Rio de Janeiro, tamborzão beat, 150 BPM, E minor,
syncopated surdo and timbal percussion, atabaque samples, whistle and air horn,
male MC shouting with crowd call and response, brazilian portuguese vocals,
party sound system energy, punchy clean sub bass
```

**Exclude Styles:**
```
reggaeton, dembow, latin pop, spanish, moombahton, afrobeats, amapiano, trap,
melodic singing, english vocals, slow
```

**Lyrics:** a letra acima, copiada como está.

**Se sair errado:** ainda em reggaeton → troque o style por `tamborzão, funk carioca 150 bpm, brazilian favela funk, NO dembow rhythm`. Se vier melódico demais, adicione `shouted vocals, no melody, chant only`.

---

# FAIXA 2 — "O Bebê Pegou a BR"

**Objetivo: animar e bater na oposição.** Arrasta-pé com graça, sarcasmo e pediatria de verdade.

**Gênero:** Pisadinha / piseiro
**BPM:** 138 · **Tom:** Sol maior · **Duração:** 3'00"

> **Por que joguei fora a v2:** "chega aflita, sai tranquila" era bonito no briefing e fraco na música — não tinha piada, não tinha alvo, e não falava de pediatria em nenhum momento. Essa aqui fala de bronquiolite, pneumonia, madrugada e ambulância. E tem alvo.
>
> **O alvo, como no jingle da praça:** a fita cortada, a placa de obra, a live. Nunca uma pessoa, nunca um nome.

## Letra

```
[Intro - falado, dois compadres]
Ô compadre, cadê a UTI?
Foi inaugurada?
Foi não. Inauguraram a placa.
Ah bom, então tá resolvido.

[Verso 1]
Meu bebê tem três dias
E já rodou de montão
Conhece mais a estrada
Que motorista de caminhão

Nasceu aqui em Mineiros
Mas não pôde aqui ficar
Foi de ambulância e sirene
Pra outra cidade internar

[Pré-refrão]
Não é filme, não é lenda
Não é caso de exceção
É a conta que não fecha
De cidade sem UTI e sem plantão

[Refrão]
Cortaram fita bonita
Tem placa em todo lugar
Mas cortar fita de obra
Não corta cordão umbilical

Mineiros pede UTI
Mineiros pede plantão
Criansa não se cura
Com placa de inauguração

[Verso 2]
Se propaganda curasse
Ninguém mais adoecia
Se live curasse febre
A gente vivia de alegria

Mas quando o bebê arria
E o relógio não perdoa
Não adianta ter cartaz
O que salva é UTI boa

[Refrão]

[Falado - break, os dois compadres]
Ô compadre
Tem UTI Neonatal em Mineiros?
Tem não
E tem obra?
Tem de montão
E o bebê, vai pra onde?
Vai pra estrada, compadre. Vai pra estrada.

[Verso 3]
Faz mais de vinte ano
Que ele atende essa cidade
Já viu febre, já viu chiado
Já viu susto de verdade

Já tratou bronquiolite
Já tratou pneumonia
Já segurou mão de mãe
Que chorava e não dormia

[Verso 4]
Ele não fala de fora
Ele fala do plantão
Não aprendeu na cartilha
Aprendeu no coração

Seis meses de licença
UTI e condução
Vinte, sete sete sete
É pediatra na Assembleia, cidadão

[Refrão final - dobrado, coro]

[Outro - falado]
Placa é bonita, compadre
Mas UTI é que salva
```

## Prompt Suno

**Style of Music:**
```
Piseiro, pisadinha, brazilian forró eletrônico, 138 BPM, G major, bright Yamaha PSR
keyboard lead riff, electronic zabumba and triangle, marked walking bass, accordion
on the chorus, male lead with female backing on the chorus, warm northeastern
brazilian accent, cordel storytelling delivery, festive danceable groove,
spoken comedic dialogue breaks
```

**Exclude Styles:**
```
sertanejo universitário, rock, trap, english vocals, spanish, reggaeton, sad ballad,
orchestral, slow tempo
```

**Lyrics:** a letra acima. Note que **"criansa"** está trocada de propósito.

**Se sair errado:** sem riff de teclado → adicione `strong PSR keyboard riff intro`. Se o Suno cantar os trechos falados em vez de falar, marque como `[Spoken - two men talking, no singing]`. Os dois breaks falados são o coração da graça — se ficarem ruins, grave com duas pessoas de verdade e cole na edição, sai melhor.

---

# FAIXA 3 — "Quebra o Vaso"

**Objetivo: esperança.** É a única faixa que não pede nada.

**Gênero:** Louvor — balada de adoração congregacional
**BPM:** 72 · **Tom:** Ré maior · **Duração:** 5'00"
**Base:** Juízes 6–7 · 2 Coríntios 4.7 · Gideões Internacionais

## Por que não há espada

O texto bíblico traz *"a espada do Senhor e de Gideão"* (Juízes 7.20). Removi — o briefing não admite arma em nenhum material, nem como metáfora.

Ficou a imagem melhor: **os trezentos carregavam tochas escondidas dentro de vasos de barro, e a vitória começou quando quebraram os vasos e a luz apareceu.** Amarra em 2 Coríntios 4.7, amarra na cruz vazada da identidade visual, e amarra nos Gideões Internacionais — a Bíblia esquecida numa gaveta, coisa pequena e sem força aparente, que muda uma vida quando alguém abre.

**Sem número, sem nome, sem pedido de voto.** Se entrar campanha, ela morre.

## Letra

```
[Intro - piano solo]

[Verso 1]
Eu era o menor da casa do meu pai
Escondido no lagar
Batendo o meu trigo em silêncio
Com medo de levantar

E Tu me chamaste valente
Antes de eu ser
Antes de eu crer
Antes de eu vencer

[Verso 2]
Eu contei trinta e dois mil ao meu lado
E Tu me disseste: são gente demais
Porque se a forsa for minha
Eu esqueço de Quem me traz a paz

[Pré-refrão]
Então desceu pra dez mil
E Tu disseste: inda tem
Até sobrar só trezentos
E aí Tu disseste: amém

[Refrão]
Trezentos bastam
Se Tu vais na frente
Trezentos bastam
Se o Senhor tá presente

Quebra o vaso
Acende a luz
Que o mundo veja
Não a minha forsa
Mas o Deus que me conduz

[Verso 3]
Uma tocha escondida dentro de um vaso de barro
Uma trombeta na mão de quem não era ninguém
Tu não pediste um exército
Tu pediste coragem de um povo que crê e diz amém

[Verso 4]
E ainda hoje Tu fazes assim
Uma Bíblia esquecida na gaveta de um quarto
Num hospital, numa escola, na mão
De alguém que chorava sozinho no escuro

Ninguém viu quem deixou
Ninguém soube o nome
Mas alguém abriu, alguém leu
E a vida inteira mudou

[Refrão - com bateria]

[Ponte - repete 3x crescendo]
Somos poucos
Mas contigo somos muitos
Somos barro
Mas trazemos Tua luz
Se Tu sopras
A trombeta vai soar
Se Tu queres
O impossível vai passar

[Clímax - só voz e piano, depois coral]
Quebra o vaso em mim, Senhor
Quebra o vaso em mim
Que se apague a minha glória
E que a Tua brilhe enfim

Quebra o vaso em mim, Senhor
Quebra o vaso em mim
Se for preciso eu me quebrar
Pra Tua luz chegar
Quebra o vaso em mim

[Outro - coral pianíssimo]
Trezentos bastam
Trezentos bastam
Se Tu vais na frente
```

## Prompt Suno

**Style of Music:**
```
Brazilian worship ballad, portuguese gospel, 72 BPM, D major, intimate grand piano
intro, steel string acoustic guitar, string quartet swelling on the chorus, drums
entering only on the second chorus, congregational choir on the finale, emotive
male lead vocal in brazilian portuguese, cinematic dynamic build, reverent and warm
```

**Exclude Styles:**
```
EDM, electronic drums, american gospel choir, distortion, rap, upbeat, march tempo,
drums from the start, orchestral bombast, english vocals
```

**Lyrics:** a letra acima. Só **"forsa"** está trocada.

**Se sair errado:** o Suno entra com bateria cedo demais em balada. Gere em duas partes — versos 1 a 3 com `[soft, piano and guitar only, no drums]` e o resto separado — e monte na edição. O clímax é a **queda**, não o pico: depois da ponte no volume máximo tudo cai para voz e piano. Gerar versão instrumental também.

---

# FAIXA 4 — "Ô Trem Bão"

**Objetivo: animação total.** Orgulho goiano, som de carro, grito de galera.

**Gênero:** Eletrofunk goiano
**BPM:** 129 · **Tom:** Mi menor · **Duração:** 2'30"

> Os parâmetros abaixo vêm da análise do áudio de referência, não de palpite. **O sub-grave é o instrumento principal e o meio do espectro é vazio** — é isso que separa eletrofunk goiano de eletrofunk genérico. Se o Suno entregar com teclado, pad ou guitarra no meio, está errado por definição.

## Letra

```
[Intro tag - voz grave processada]
Uai...
Ô trem bão
Sudoeste de Goiás
Segura

[Build - tensão subindo, 16 compassos]
Vem, vem, vem
Vem, vem, vem
Levanta a poeira
E grita:

[Drop]
Ô TREM BÃO!   (uai)
Ô TREM BÃO!   (uai)
Vinte, sete sete sete
Ô TREM BÃO!   (uai)
Ô TREM BÃO!   (uai)
O doutor do Sudoeste

[Verso - rápido, gritado]
Sol rachando o cerrado, poeira no retrovisor
Da BR pra cidade, quem cuida é o doutor
Mineiros, Portelândia, Chapadão do Céu
Santa Rita, Serranópolis, o Sudoeste é meu

Não é palanque, é plantão
Não é promessa, é prontuário
Ele não fala de longe, não
Ele fala do consultório diário

Cê já viu político andar duas hora a pé?
Pois esse aqui andou pra ver como é que é
Chegar no hospital sem carro e sem ninguém
Quem sentiu na canela é quem resolve também

[Silêncio total - 2 compassos]

[Build 2]
UTI pra criansa respirar
Transporte pra mãe poder chegar
Seis meses de licensa
Que quatro não dá, não dá, não dá

[Drop 2 - cheio]
Ô TREM BÃO!   (uai)
Vinte, sete sete sete, Lourival
Ô TREM BÃO!   (uai)
Pediatra do povo, é do interior
Ô TREM BÃO!   (uai)
Goiás inteiro no comando
UAI!

[Outro tag]
Ô trem bão
Doutor Lourival
Uai
```

## Prompt Suno

**Style of Music:**
```
Eletrofunk goiano from Goiás Brazil, 129 BPM, E minor, MASSIVE dominant sine sub
bass carrying the entire melody, hollow empty midrange with no harmonic instruments,
sparse punchy kick, continuous eighth note groove, fast chopped vocal stabs in the
high end, long tense quiet build then violent drop, dead silence before each drop,
shouted male vocals in brazilian portuguese, deep pitched-down DJ tag,
car sound system mix
```

**Exclude Styles:**
```
reggaeton, dembow, trap, melodic instruments, guitar, piano, synth pads, strings,
warm midrange, english vocals, spanish, EDM festival, house, slow tempo, singing
```

**Lyrics:** a letra acima. **"criansa"** e **"licensa"** trocadas.

**Se sair errado:** o erro mais provável é o Suno colocar teclado ou pad no meio. Reforce com `no midrange instruments, sub bass only, hollow mix`. Se o drop não bater, é porque não teve silêncio antes — force com `[Silence - 2 bars]` antes do drop. O `Ô TREM BÃO` é a assinatura: se não ficar destacado, gere isolado e replique na edição.

**Sobre as cidades:** citar Portelândia, Chapadão do Céu, Santa Rita e Serranópolis não é enfeite. O diagnóstico aponta capilaridade territorial como a fragilidade número 1 do Dr. — a base é concentrada em Mineiros. Cantar o nome das cidades vizinhas é a forma mais barata que existe de plantar presença fora dela.

---

# FAIXA 5 — "Esperança"

**Objetivo: animação.** Anthem de festival com coro de galera — não é a balada contemplativa da v2.

**Gênero:** Brazilian bass / progressive house
**BPM:** 124 · **Tom:** Lá menor · **Duração:** 3'20"

## Letra

```
[Intro]
Goiás!
Levanta a mão
Quem tem esperança levanta a mão!

[Build 1]
Não solta a minha mão
Que a noite vai passar
Não solta a minha mão
Que o sol vai voltar

Dias melhores virão!
Dias melhores virão!

[Drop 1 - vocal picotado + coro de galera]
Ô-ô-ô-ô
Es-pe-ran-sa
Ô-ô-ô-ô
Es-pe-ran-sa

[Verso]
Sol nascendo no cerrado
Mãe com o filho no colo
Sem ter carro, sem ter hora, sem ter fim

Ela anda porque ama
E o amor não pede estrada
O amor abre caminho pra ela e pra mim

[Build 2]
Se cair, eu levanto
Se doer, eu não desisto
Se demorar, eu espero

É só tentando
É só tentando
É só tentando que a gente consegue!

[Drop 2 - cheio, coro grande]
Ô-ô-ô-ô
Es-pe-ran-sa
Ô-ô-ô-ô
Es-pe-ran-sa

Dias melhores virão!
Dias melhores virão!

[Breakdown - cai tudo]
Esperansa é o que sobra
Quando tudo mais acaba
E é o que basta pra recomeçar

[Drop final - tudo]
Ô-ô-ô-ô
Es-pe-ran-sa
Dias melhores virão!

[Outro]
Goiás, levanta a mão
Vinte, sete sete sete
```

> **A última linha é opcional.** Sem ela, essa faixa é a marca e sobrevive à eleição — funciona em 2027 igual funciona hoje. Com ela, vira campanha e vence em outubro. Recomendo **gerar as duas versões** e usar cada uma no seu lugar.

## Prompt Suno

**Style of Music:**
```
Brazilian bass, progressive house festival anthem, 124 BPM, A minor, atmospheric pad
intro, ethereal female vocal with long reverb, chopped vocal lead on the drop, deep
rolling bassline, plucked synth lead, tribal percussion, big crowd chant vocals,
euphoric festival build, brazilian portuguese vocals, uplifting
```

**Exclude Styles:**
```
hardstyle, dubstep, aggressive, rap, distorted, dark techno, trap, english vocals,
spanish, sad, slow
```

**Lyrics:** a letra acima. **"Es-pe-ran-sa"** e **"esperansa"** trocadas.

**Se sair errado:** se o Suno cantar "Esperança" inteira em vez de picotar, escreva `Es. Pe. Ran. Sa.` com pontos. Gerar **versão instrumental obrigatória** para trilha de narração do Dr.

---

# Checklist

## Antes de gerar
- [x] Número **20777** aplicado nas faixas 1, 2, 4 e (opcional) 5
- [x] Fonética corrigida — só `ç` antes de a/o/u e o número por extenso
- [ ] Gerar 4 versões de cada faixa
- [ ] Gerar instrumental das faixas 3 e 5
- [ ] Gerar as duas versões da faixa 5 (com e sem o número no fim)

## Antes de publicar
- [ ] Aprovação do Dr. nas letras
- [ ] Validar a faixa 3 com o pastor Christofer Cruz — é a de maior risco reputacional se soar oportunista
- [ ] Gravar os dois breaks falados da faixa 2 com duas pessoas de verdade. Sai melhor que o Suno e é onde está a graça
- [ ] Conferir que o **20777** está audível e correto em todas as faixas que o citam

## Sobre bater na oposição — a linha que não pode ser cruzada
- [ ] Nenhuma letra cita nome de pessoa, cargo ou partido. **Manter assim.** O briefing proíbe ataque nominal, e o jingle da praça respeita isso: o alvo é a obra, a placa, a fita, a live — nunca quem cortou
- [ ] Toda faixa que levanta problema apresenta resolução. Nenhuma termina em reclamação
- [ ] Se alguma linha for lida como direcionada a uma pessoa específica, trocar antes de publicar. Não vale o risco de representação no TRE

## Direitos autorais
- [ ] **Composições originais apenas.** A análise do "Olha o Trem" extraiu só parâmetros técnicos (BPM, tom, balanço espectral) — nenhuma melodia, letra ou levada foi reaproveitada. Parâmetro técnico não é obra protegida, mas **nenhum trecho da faixa de referência pode entrar na produção**
- [ ] Verificar os **termos de uso do Suno** quanto a titularidade e uso comercial/eleitoral do áudio gerado, e se o plano contratado permite. Resolver antes de veicular
- [ ] Contrato de cessão com quem finalizar, mixar e masterizar
- [ ] Registro na Biblioteca Nacional / ECAD antes da veiculação

## Veiculação — Lei 9.504/97
- [ ] Propaganda liberada desde 16/08/2026 — as faixas 1, 2, 4 e 5 podem pedir voto
- [ ] Carro de som: das 8h às 22h, e proibido a menos de 200 m de hospitais, escolas em funcionamento, bibliotecas, igrejas, teatros e sedes dos Poderes
- [ ] Showmício é proibido
- [ ] Validar com a assessoria jurídica eleitoral antes de veicular em rádio

## Ordem de produção
Restam cerca de 6 semanas até 04/10/2026.

1. **Faixa 2** — maior alcance por real investido, é a que ganha Mineiros
2. **Faixa 4** — resolve a capilaridade territorial citando as cidades vizinhas
3. **Faixa 1** — alcance jovem, potencial de trend
4. **Faixa 5** — ativo de longo prazo
5. **Faixa 3** — a mais difícil de acertar. Se não sair com qualidade real, não usar

---

*Vizantu · Agosto de 2026 · Versão 3*
