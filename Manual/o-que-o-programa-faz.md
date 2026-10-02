# 1. O que o programa faz

O Ranmza GT tira um "print" de uma área da tela, reconhece o texto que está nela, traduz e
mostra a tradução **por cima do jogo**. Funciona com qualquer jogo, visual novel, vídeo ou
programa que mostre texto na tela: legendas, diálogos, menus, cartas, itens.

São dois jeitos de traduzir:

- **Captura de tela** — você aperta uma tecla e o programa traduz a área marcada uma vez, com a
  tradução desenhada por cima de cada trecho do texto original. Serve para menus, inventário,
  cartas, diálogos parados e telas cheias de texto.
- **Modo Legenda** — você liga uma vez e o programa fica lendo a área da legenda sozinho,
  traduzindo cada fala nova enquanto ela aparece. Serve para cutscenes, vídeos e diálogos que
  passam sozinhos.

> **⚠️ Requisito essencial: o jogo precisa estar em modo Janela ou Janela sem borda.** O Ranmza
> GT desenha a tradução **por cima** da janela do jogo — então rode o jogo em **modo Janela**
> (*Windowed*) ou, de preferência, **Janela sem borda** (*Borderless* / *Fullscreen sem borda*),
> que ocupa a tela inteira e ainda deixa a tradução aparecer por cima. Em **Tela cheia exclusiva**
> (*Exclusive Fullscreen*) o Windows entrega a tela só para o jogo e nenhum programa consegue
> desenhar sobre ela — a tradução não vai aparecer. Sintoma típico: você aperta Traduzir, a
> tradução até surge na aba **Histórico**, mas nada aparece sobre o jogo. Solução: troque o jogo
> para **Janela sem borda** nas opções de vídeo dele.

O fluxo básico da captura de tela é sempre:

1. Você escolhe **onde** está o texto (uma área da tela).
2. Aperta um atalho para **traduzir**.
3. A tradução aparece sobreposta ao jogo.
4. Aperta outro atalho para **limpar** quando quiser, ou ela some sozinha depois de um tempo.

O Modo Legenda tem a própria área e o próprio atalho de ligar e desligar — está na
[seção 9](/Manual/modo-legenda-traducao-automatica-continua.md).

---
