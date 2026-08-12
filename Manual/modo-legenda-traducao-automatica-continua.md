# 8. Modo Legenda — tradução automática contínua

Para cenas com diálogo contínuo (cutscenes, modo automático de visual novels, vídeos com
legenda), o Modo Legenda traduz **sozinho, repetidamente**, sem você precisar apertar nada.

## Como configurar

1. Em **Overlay › Legenda**, ajuste as opções de captura (intervalo, quantas linhas mostrar,
   etc.) — os padrões já funcionam bem para a maioria dos casos.
2. Aperte **Selecionar área da legenda** (padrão `Numpad1`) e desenhe um retângulo sobre onde a
   legenda/diálogo aparece no jogo.
3. Aperte **Ligar/desligar legenda** (padrão `Numpad0`) para ativar.

A partir daí, o programa fica de olho naquela área, traduzindo automaticamente sempre que um
texto novo aparecer e ficar "parado" por um instante (isso evita traduzir letras aparecendo uma
por uma em efeitos de "máquina de escrever").

Por padrão, as traduções aparecem **acima** da área selecionada, em ordem (mais recente
embaixo), e somem sozinhas se nenhum texto novo aparecer por alguns segundos. Dá para trocar
isso pela sobreposição no lugar da legenda original — é o tópico a seguir.

## Substituindo a legenda original no lugar

Em **Overlay › Legenda**, o primeiro card (*Posição da tradução*) tem a opção **"Substituir a
legenda original no lugar"**. Ligada, a tradução deixa de aparecer acima da área e passa a ser
desenhada **em cima** dela, cobrindo a legenda original do jogo — como se o jogo estivesse
legendado no seu idioma.

Nesse modo o programa mostra **uma fala por vez**, e o controle *Linhas visíveis* fica travado
em 1. O motivo é simples: a área que você selecionou tem o tamanho de **uma** legenda do jogo,
então empilhar duas ou três falas traduzidas ali dentro não caberia — o texto sairia cortado na
borda. Sua escolha de linhas fica guardada e volta a valer assim que você desligar a opção.

> Se mesmo com uma fala a tradução não couber (o português costuma ser mais longo que o inglês
> ou o japonês), diminua o *Tamanho da fonte* no card **Texto**, ou refaça a seleção da área um
> pouco mais alta que a legenda do jogo.

> Nesse modo a legenda fica **escondida das capturas de tela**. Não é um defeito: é justamente
> isso que impede o OCR de reler a própria tradução no ciclo seguinte e se retroalimentar.
> Funciona só com programas rodando **NESTE PC** (OBS, Game Bar, NVIDIA ShadowPlay, etc).
> Gravando por placa de captura, a tradução aparece assim mesmo.

A opção vale só para o Modo Legenda — a tradução manual (`Numpad8`/`Numpad9`) e o Modo Tempo
Real não são afetados.

## Deixando a IA "lembrar" das falas anteriores

Se você está usando OpenAI, Claude ou Gemini, **Traducao › I.A** tem um controle **"Falas
anteriores"** (0 a 20, padrão 5). Com ele ligado, a IA recebe as últimas falas já traduzidas
como referência antes de traduzir a próxima — isso ajuda a manter os mesmos nomes, termos e
tom ao longo de uma conversa. Se notar que a IA está mudando o nome de um personagem ou o tom
da tradução de uma fala para outra, aumente esse valor; se preferir que cada fala seja
traduzida sem depender das anteriores, deixe em 0.

> O **DeepL** também aproveita as falas anteriores como contexto, **sem custo extra** — ele
> recebe as últimas falas como referência (seguindo o mesmo controle **"Falas anteriores"**)
> para manter a consistência de nomes e termos. Mesmo não sendo uma IA conversacional, isso
> deixa a tradução contínua mais coesa. **Google Translate** não usa esse contexto.

## Aparência separada

Overlay › Legenda tem suas próprias opções de fonte, cor, fundo e contorno — independentes da
tradução manual — então você pode deixar a legenda contínua menor/mais discreta e a tradução
manual (`Numpad8`/`Numpad9`) maior, por exemplo. O pré-processamento de imagem também é
independente.

## Desligando

Aperte **`Numpad0`** novamente, ou o botão verde de balão na barra flutuante. A legenda na tela
é limpa imediatamente.

O modo também **se desliga sozinho** depois de um tempo sem detectar texto na região, para não
ficar rodando à toa quando você sai da cutscene e esquece de desligar. O tempo é escolhido em
*Overlay › Legenda → Desligar Modo Legenda após inatividade*: Nunca, 1, 2, 3, 5 ou 10 minutos
(padrão 1 minuto). Repare que isso **desliga o modo**, não só esconde a legenda — para religar,
aperte `Numpad0`.

---
