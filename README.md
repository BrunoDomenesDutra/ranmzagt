<h1 align="center">Ranmza Game Translator</h1>

<p align="center"><img src="media/logo.png" alt="Ranmza GT" width="200"></p>

<p align="center"><i>Traduz qualquer jogo, vídeo ou texto na tela — por cima, em tempo real.</i></p>

<p align="center">
  <a href="https://github.com/BrunoDomenesDutra/ranmzagt/releases"><img src="https://img.shields.io/github/v/release/BrunoDomenesDutra/ranmzagt?label=release&color=blue" alt="Release"></a>
  <a href="https://github.com/BrunoDomenesDutra/ranmzagt/releases"><img src="https://img.shields.io/github/downloads/BrunoDomenesDutra/ranmzagt/total?label=downloads&color=brightgreen" alt="Downloads"></a>
  <a href="https://github.com/BrunoDomenesDutra/ranmzagt/stargazers"><img src="https://img.shields.io/github/stars/BrunoDomenesDutra/ranmzagt?label=stars&color=yellow" alt="Stars"></a>
  <img src="https://img.shields.io/badge/plataforma-Windows-0078D6" alt="Plataforma">
  <a href="https://github.com/BrunoDomenesDutra/ranmzagt/blob/main/LICENSE"><img src="https://img.shields.io/badge/licen%C3%A7a-Freeware-orange" alt="Licenca"></a>
</p>

---

## Português

O **Ranmza GT** captura uma área da tela, reconhece o texto com OCR, traduz e desenha a tradução **sobreposta ao jogo**, na mesma posição do texto original — como uma legenda flutuante. Funciona com qualquer jogo, visual novel, mangá digital, vídeo ou programa que mostre texto na tela.

**Como funciona:**

1. **Captura** — fotografa uma área da tela (ou a tela inteira) várias vezes por segundo.
2. **OCR** — reconhece o texto na imagem (Windows OCR nativo, OneOCR ou Tesseract, à sua escolha).
3. **Tradução** — envia o texto para o motor escolhido (Google, OpenAI, Claude ou Gemini) e recebe a tradução.
4. **Overlay** — desenha a tradução por cima do jogo, na mesma posição do texto original, sem capturar foco nem travar a janela.

Desenvolvido em **Rust** 🦀 — nativo para Windows, sem runtime pesado, com baixo consumo de CPU/memória mesmo rodando junto de um jogo.

📖 **[Manual completo](https://brunodomenesdutra.github.io/ranmzagt/)** &nbsp;&middot;&nbsp; ⬇️ **[Baixar (Releases)](https://github.com/BrunoDomenesDutra/ranmzagt/releases)**

---

## English

**Ranmza GT** captures an area of the screen, recognizes the text with OCR, translates it and draws the translation **overlaid on the game**, in the same position as the original text — like a floating subtitle. Works with any game, visual novel, digital manga, video or program that shows text on screen.

**How it works:**

1. **Capture** — grabs an area of the screen (or the whole screen) several times per second.
2. **OCR** — recognizes the text in the image (native Windows OCR, OneOCR or Tesseract, your choice).
3. **Translation** — sends the text to the chosen engine (Google, OpenAI, Claude or Gemini) and gets the translation back.
4. **Overlay** — draws the translation over the game, in the same position as the original text, without stealing focus or freezing the window.

Built in **Rust** 🦀 — native for Windows, no heavy runtime, low CPU/memory footprint even while running alongside a game.

📖 **[Full manual](https://brunodomenesdutra.github.io/ranmzagt/)** &nbsp;&middot;&nbsp; ⬇️ **[Download (Releases)](https://github.com/BrunoDomenesDutra/ranmzagt/releases)**
