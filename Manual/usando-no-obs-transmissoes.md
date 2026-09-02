# 11. Usando no OBS / transmissões

Se você transmite ou grava o jogo e quer que **a tradução apareça também no vídeo/stream**
(ou só no vídeo, sem aparecer no jogo em si), use **Overlay › Web**:

1. Ative o **Servidor ativo**.
2. Copie o endereço **Captura — OBS** (`/captura/obs`) mostrado na aba, no botão *Copiar*.
3. No OBS, adicione uma fonte do tipo **"Navegador" (Browser Source)** e cole esse endereço.
   Essa versão da página tem fundo transparente, pronta para sobrepor à captura do jogo.
4. (Opcional) **Desative** a chave **"Mostrar tradução na tela"** para tirar o overlay do jogo e
   deixar a tradução aparecer **só** na página do navegador/OBS — útil se a captura do OBS já
   inclui a janela do overlay e você não quer ver a tradução duplicada. Deixe **ligada** se
   quiser a tradução nos dois lugares.

<p align="center"><img src="media/overlay-web.png" alt="Aba Overlay › Web" width="820"></p>

Você também pode personalizar tema (claro/escuro/dracula), cores, tamanho da fonte, e se quer
mostrar o texto original junto com a tradução, horário e qual serviço foi usado.

<p align="center"><img src="media/overlay-web-aparencia.png" alt="Aba Overlay › Web — aparência da página" width="820"></p>

A página também pode ser aberta em qualquer navegador da rede local (celular, segundo monitor,
etc.) usando o endereço **Captura** (`/captura`) mostrado na aba — essa versão vem com histórico
e botão de limpar.

> Se a tradução some das suas gravações e transmissões, há três causas possíveis. Duas são
> automáticas, nos modos que desenham **por cima** do texto original: o Modo Tempo Real (sempre)
> e o Modo Legenda com *"Substituir a legenda original no lugar"* ligado — nos dois o overlay
> precisa ficar invisível para capturas, senão o OCR releria a própria tradução. A terceira é
> uma escolha sua: *"Esconder a tradução de gravações e transmissões"*, no card **Exibição** de
> Overlay › Captura. É justamente nesses casos que o servidor Web resolve.

---
