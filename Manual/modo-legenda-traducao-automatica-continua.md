# 9. Modo Legenda — tradução automática contínua

Para cenas com diálogo contínuo (cutscenes, modo automático de visual novels, vídeos com
legenda), o Modo Legenda traduz **sozinho**, sem você precisar apertar nada a cada fala.

## Como configurar

1. Aperte **Selecionar área da legenda** (padrão `Numpad1`) e desenhe um retângulo sobre onde a
   legenda aparece no jogo. Essa área é separada da área da captura de tela.
2. Aperte **Ligar/desligar legenda** (padrão `Numpad0`) para ligar. Um alerta na tela confirma.

O programa sempre abre com a legenda desligada. As opções ficam em **Overlay › Legenda**, e os
padrões já funcionam bem para a maioria dos casos.

<p align="center"><img src="media/overlay-legenda-captura.png" alt="Aba Overlay › Legenda — Captura e alfabeto" width="820"></p>

A partir daí, o programa fica de olho naquela área várias vezes por segundo e traduz cada texto
novo assim que ele aparece e se repete numa segunda leitura. Isso evita traduzir uma fala ainda
sendo escrita na tela. Se a área ficar igual, o programa nem relê o texto.

Por padrão, a tradução aparece **acima** da área selecionada e some sozinha alguns segundos
depois de a legenda sumir do jogo. Dá para trocar isso pela tradução em cima da legenda original
— é o tópico a seguir.

<div style="position:relative;padding-top:56.25%;max-width:820px;margin:0 auto">
  <iframe src="https://player.vimeo.com/video/1217784520"
          style="position:absolute;top:0;left:0;width:100%;height:100%;border:0"
          allow="fullscreen; picture-in-picture" allowfullscreen
          title="Modo Legenda traduzindo sozinho"></iframe>
</div>

<p align="center"><i>Modo Legenda traduzindo sozinho, com a tradução acima da área selecionada.</i></p>

## Ignorar texto fora do centro da área

A opção **Ignorar texto fora do centro da área**, no card **Captura**, vem ligada. Com ela, o
programa ignora o texto perto das bordas da área, como placas, letreiros e textos do jogo que
aparecem ao lado da legenda.

- Quanto mais justa a área estiver em volta da legenda, melhor funciona. Marque só a faixa onde
  a legenda aparece.
- Em jogos com diálogo alinhado à esquerda, como alguns RPGs e visual novels, deixe essa opção
  desligada.

## Colar no texto detectado

Em **Overlay › Legenda**, o primeiro card (*Posição da tradução*) tem a opção **Colar no texto
detectado**. Ligada, a tradução deixa de aparecer acima da área e passa a ser desenhada **em
cima da fala original**, com as mesmas quebras de linha, cobrindo a legenda do jogo — como se o
jogo estivesse legendado no seu idioma.

- Nesse modo o programa mostra **uma fala por vez**, e *Falas na tela* fica em 1.
- A tradução **não é encolhida para caber**: fonte maior transborda a área, de propósito. É assim
  que dá para deixar a legenda maior que a do jogo.
- A área selecionada continua sendo o que o programa lê. Ela precisa caber a legenda inteira do
  jogo.

> Nesse modo a legenda fica **escondida das capturas de tela**. É isso que impede o OCR de reler
> a própria tradução no ciclo seguinte. Funciona só com programas rodando **NESTE PC** (OBS, Game
> Bar, NVIDIA ShadowPlay, etc). Gravando por placa de captura, a tradução aparece assim mesmo.

<div style="position:relative;padding-top:56.25%;max-width:820px;margin:0 auto">
  <iframe src="https://player.vimeo.com/video/1218094053"
          style="position:absolute;top:0;left:0;width:100%;height:100%;border:0"
          allow="fullscreen; picture-in-picture" allowfullscreen
          title="Tradução cobrindo a legenda original"></iframe>
</div>

<p align="center"><i>A tradução desenhada por cima da legenda original. O vídeo foi gravado com
celular porque, nesse modo, a legenda fica escondida das capturas de tela — uma gravação normal
não mostraria a função funcionando.</i></p>

## Mais de uma fala na tela

Com *Colar no texto detectado* desligado, **Falas na tela** (1 a 8, padrão 1) define quantas
falas ficam visíveis ao mesmo tempo. Com mais de uma, cada fala fica numa linha, começando com um
traço, no meio do monitor. Fala comprida demais para a largura diminui a fonte do bloco, em vez de
quebrar a linha.

## Deixando a IA "lembrar" das falas anteriores

Com uma IA (OpenAI, Anthropic, Gemini ou Groq), **Tradução › I.A** tem o controle **Falas
anteriores** (5 a 10, padrão 5). A IA recebe as últimas falas já traduzidas como referência antes
de traduzir a próxima — isso ajuda a manter os mesmos nomes, termos e tom ao longo de uma
conversa. Cada fala a mais custa tokens em toda tradução.

> O **DeepL** recebe só o texto original dessas falas, como contexto, e não cobra por ele. Os
> outros tradutores dedicados (Google Translate, Google Cloud e Azure) traduzem cada fala sozinha.

## Aparência separada

Overlay › Legenda tem suas próprias opções de fonte, cor, fundo e contorno — independentes da
captura de tela — então você pode deixar a legenda contínua menor e mais discreta e a tradução da
captura de tela maior, por exemplo.

## Desligando

Aperte **`Numpad0`** novamente, ou o botão de ligar/desligar a legenda na barra flutuante. A
legenda na tela é limpa imediatamente.

O modo também **se desliga sozinho** depois de um tempo sem texto na área, para não ficar rodando
à toa quando você sai da cutscene e esquece de desligar. O tempo é escolhido em
*Overlay › Legenda → Desligar a legenda sem texto na área*: Nunca, 1, 2, 5 ou 10 minutos (padrão
1 minuto). Legenda parada na tela conta como texto. Repare que isso **desliga o modo**, não só
esconde a legenda — para religar, aperte `Numpad0`.

---
