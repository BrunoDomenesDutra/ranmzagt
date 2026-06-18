## 9. Modo Tempo Real — tradução contínua no lugar (experimental)

> Recurso **experimental** — ligado e configurado pela aba **Experimental**. O comportamento
> ainda pode mudar e bugs são esperados.

O Modo Tempo Real junta o melhor dos outros dois modos: é **contínuo e automático** como o
Modo Legenda (não precisa apertar nada a cada fala), mas desenha a tradução **no lugar do texto
original**, sobre cada linha detectada, como o modo Traduzir — em vez de empilhar tudo numa
caixa fora da área. Ele trabalha sobre uma **área própria**, normalmente maior que a da legenda
(cobre a caixa de diálogo inteira, o nome do personagem, várias linhas de uma vez).

É indicado para conversas com NPCs em que aparecem **nome + várias linhas de fala** ao mesmo
tempo, e você quer tudo traduzido ao vivo, na posição original, sem clicar.

### Como usar

1. Na aba **Experimental**, ajuste as opções do Tempo Real (intervalo, fonte, fundo, contorno,
   desligamento automático) — os padrões já funcionam.
2. Aperte **Selecionar área do Tempo Real** (padrão `Numpad6`) e desenhe o retângulo sobre a
   região onde o texto aparece.
3. Aperte **Ligar/desligar Modo Tempo Real** (padrão `Numpad3`) para ativar. A tradução passa a
   aparecer sobreposta, atualizando sozinha conforme o texto muda.
4. Aperte `Numpad3` de novo para desligar.

> Por ser contínuo e desenhar várias áreas ao vivo, o Tempo Real é mais pesado que os outros
> modos. Se notar travadas, aumente o **intervalo** na aba Experimental.

### Estabilidade com fundo animado

Em cenas com fundo em movimento (animações de jogos de RPG, vídeos), o reconhecimento de texto
pode oscilar de um quadro para outro, fazendo a tradução **tremer** ou **piscar**. Dois ajustes
na aba Experimental controlam isso:

- **Estabilidade da posição** — quantos pixels o texto precisa andar para a tradução ser
  reposicionada. Maior = tradução mais "parada" (ignora o tremor); menor = acompanha o texto
  mais de perto. (Padrão: 12px.)
- **Segurar em falha de OCR** — por quantos ciclos uma tradução continua na tela quando o
  reconhecimento falha por um instante, evitando a piscada. Maior = segura mais tempo; menor =
  some mais rápido. (Padrão: 6.)

Regra prática: se ainda **tremer**, aumente a *Estabilidade da posição*; se ainda **piscar**,
aumente o *Segurar em falha de OCR*.

### Efeito máquina de escrever (typewriter)

Muitos jogos revelam o texto **letra por letra**. Para não traduzir frases pela metade, ligue
**Máquina de escrever** na aba Experimental: o programa espera o texto "assentar" (parar de
mudar) antes de traduzir. Vale tanto para o Modo Tempo Real quanto para o Modo Legenda. Dá para
ajustar quão estável o texto precisa ficar e o tempo máximo de espera antes de traduzir mesmo
assim.

---
