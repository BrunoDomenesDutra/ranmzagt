# 10. Modo Tempo Real — tradução contínua no lugar (experimental)

> Recurso **experimental** — ligado e configurado pela aba **Experimental**. O comportamento
> ainda pode mudar e bugs são esperados.

O Modo Tempo Real junta o melhor dos outros dois modos: é **contínuo e automático** como o
Modo Legenda (não precisa apertar nada a cada fala), mas desenha a tradução **no lugar do texto
original**, sobre cada linha detectada, como o modo Traduzir — em vez de empilhar tudo numa
caixa fora da área. Ele trabalha sobre uma **área própria**, normalmente maior que a da legenda
(cobre a caixa de diálogo inteira, o nome do personagem, várias linhas de uma vez).

É indicado para conversas com NPCs em que aparecem **nome + várias linhas de fala** ao mesmo
tempo, e você quer tudo traduzido ao vivo, na posição original, sem clicar.

## Como usar

Tudo do Tempo Real fica na aba **Experimental**, dentro do card *Modo Tempo Real (sobreposição
ao vivo)* — inclusive os atalhos, que **não vêm com tecla definida**. É de propósito: enquanto
o recurso é experimental, ele não ocupa uma tecla do seu teclado sem você pedir.

1. Abra a aba **Experimental** e expanda o card **Modo Tempo Real**.
2. Ligue **Permitir Modo Tempo Real**. Essa chave só **destrava** a hotkey — não começa a
   traduzir nada por si só. Com ela desligada, o atalho não faz absolutamente nada.
3. Defina as duas teclas ali mesmo: **Ligar/desligar Tempo Real** e **Selecionar área do Tempo
   Real**. Escolha teclas livres do Numpad (`Numpad3` e `Numpad4` estão sobrando nos padrões de
   fábrica) ou qualquer outra combinação.
4. Ajuste as opções, se quiser (intervalo, fonte, fundo, contorno, limpeza automática) — os
   padrões já funcionam.
5. Aperte a tecla de **selecionar área** e desenhe o retângulo sobre a região onde o texto
   aparece.
6. Aperte a tecla de **ligar/desligar**. A tradução passa a aparecer sobreposta, atualizando
   sozinha conforme o texto muda. Aperte de novo para desligar.

> O overlay do Tempo Real é **sempre** escondido das capturas de tela — não há nada para
> ligar. Sem isso, a tradução que o programa desenha por cima seria recapturada pelo próprio
> OCR no ciclo seguinte, se retroalimentando até virar uma bagunça. Funciona só com programas
> rodando **NESTE PC** (OBS, Game Bar, NVIDIA ShadowPlay, etc). Gravando por placa de captura,
> a tradução aparece assim mesmo.

> Por ser contínuo e desenhar várias áreas ao vivo, o Tempo Real é mais pesado que os outros
> modos. Se notar travadas, aumente o **intervalo** no card.

## Estabilidade com fundo animado

Em cenas com fundo em movimento (animações de jogos de RPG, vídeos), o reconhecimento de texto
pode oscilar de um quadro para outro, fazendo a tradução **tremer** ou **piscar**. Dois ajustes
no card do Tempo Real controlam isso:

- **Estabilidade da posição** — quantos pixels o texto precisa andar para a tradução ser
  reposicionada. Maior = tradução mais "parada" (ignora o tremor); menor = acompanha o texto
  mais de perto. (Padrão: 12px.)
- **Segurar em falha de OCR** — por quantos ciclos uma tradução continua na tela quando o
  reconhecimento falha por um instante, evitando a piscada. Maior = segura mais tempo; menor =
  some mais rápido. (Padrão: 6.)

Regra prática: se ainda **tremer**, aumente a *Estabilidade da posição*; se ainda **piscar**,
aumente o *Segurar em falha de OCR*.

## Efeito máquina de escrever (typewriter)

Muitos jogos revelam o texto **letra por letra**. Para não traduzir frases pela metade, ligue
**Esperar o texto assentar**, no card *Esperar texto completo (efeito máquina de escrever)* da
aba Experimental: o programa aguarda a fala parar de mudar antes de traduzir. Vale tanto para o
Modo Tempo Real quanto para o Modo Legenda.

Três controles afinam o comportamento: quantas leituras seguidas precisam bater (*Capturas
estáveis exigidas*), o quanto elas precisam se parecer para contarem como iguais (*Limiar de
"mesmo texto"*) e quanto tempo no máximo esperar antes de traduzir do jeito que está (*Teto de
espera*).

---
