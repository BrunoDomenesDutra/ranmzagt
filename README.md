<h1 align="center">Ranmza Game Translator</h1>

<p align="center"><img src="media/logo.png" alt="Ranmza GT" width="200"></p>

<p align="center"><i>Traduz qualquer jogo, vídeo ou texto na tela — por cima, em tempo real.</i></p>

<p align="center">
  <a href="https://github.com/BrunoDomenesDutra/ranmzagt/releases"><img src="https://img.shields.io/github/v/release/BrunoDomenesDutra/ranmzagt?label=release&color=blue" alt="Release"></a>
  <a href="https://github.com/BrunoDomenesDutra/ranmzagt/releases"><img src="https://img.shields.io/github/downloads/BrunoDomenesDutra/ranmzagt/total?label=downloads&color=brightgreen" alt="Downloads"></a>
  <a href="https://github.com/BrunoDomenesDutra/ranmzagt/stargazers"><img src="https://img.shields.io/github/stars/BrunoDomenesDutra/ranmzagt?label=stars&color=yellow" alt="Stars"></a>
  <img src="https://img.shields.io/badge/plataforma-Windows-0078D6" alt="Plataforma">
  <a href="https://github.com/BrunoDomenesDutra/ranmzagt/blob/main/LICENSE"><img src="https://img.shields.io/badge/licen%C3%A7a-Freeware-orange" alt="Licenca">
</a></p>

<p align="center"><strong>🇧🇷 Português</strong> &nbsp;·&nbsp; <a href="#/en/">🇬🇧 English</a></p>

---

O **Ranmza GT** captura uma área da tela, reconhece o texto com OCR, traduz e desenha a tradução **sobreposta ao jogo**, na mesma posição do texto original — como uma legenda flutuante. Funciona com qualquer jogo, visual novel, vídeo ou programa que mostre texto na tela.

### Como funciona

1. **Captura** — ao apertar o atalho, fotografa a área da tela escolhida; no Modo Legenda, lê a área da legenda sozinho, fala por fala.
2. **OCR** — reconhece o texto na imagem (Windows OCR nativo ou OneOCR, à sua escolha).
3. **Tradução** — envia o texto para o serviço escolhido (Google, Google Cloud, DeepL, Azure, OpenAI, Claude, Gemini ou Groq) e recebe a tradução.
4. **Overlay** — desenha a tradução por cima do jogo, na mesma posição do texto original, sem capturar foco nem travar a janela.

Desenvolvido em **Rust** 🦀 — nativo para Windows, sem runtime pesado, com baixo consumo de CPU/memória mesmo rodando junto de um jogo.

📖 **[Abrir o manual completo](https://brunodomenesdutra.github.io/ranmzagt/)** &nbsp;·&nbsp; ⬇️ **[Baixar (Releases)](https://github.com/BrunoDomenesDutra/ranmzagt/releases)**

### Apoie o projeto

O Ranmza GT é gratuito. Se ele te ajudou, considere apoiar o desenvolvimento:

<p align="center">
  <a href="https://livepix.gg/ranmza"><img src="https://img.shields.io/badge/LivePix-doar%20via%20Pix-32BCAD?logo=pix&logoColor=white" alt="LivePix"></a>
  <a href="https://ko-fi.com/ranmza"><img src="https://img.shields.io/badge/Ko--fi-apoiar-FF5E5B?logo=kofi&logoColor=white" alt="Ko-fi"></a>
</p>

💚 **[LivePix](https://livepix.gg/ranmza)** (Pix, nacional) &nbsp;·&nbsp; ☕ **[Ko-fi](https://ko-fi.com/ranmza)** (cartão/PayPal, internacional)

### Privacidade

O Ranmza GT não coleta nenhum dado seu. Não tem analytics, telemetria, rastreamento nem conta de usuário, e nada é enviado para nós.

Tudo o que o programa guarda fica no seu computador, na pasta dele: configurações, perfis, chaves de API (criptografadas pelo Windows), cache de traduções e logs.

O programa só se conecta à internet nestes casos, e nenhum deles passa por nós:

- **Tradução:** o texto lido na tela vai direto do seu PC para o serviço de tradução que você escolheu (Google, DeepL, OpenAI, Claude…), com a sua chave. No modo Vision, a imagem da área também vai junto. O que o serviço faz com isso segue a política de privacidade dele.
- **Aviso de versão nova:** ao abrir, o programa consulta o GitHub para saber se existe versão mais nova. Vai só o número da versão instalada. Dá para desligar em **Geral › Config → Atualizações**.
- **Modelo do Inpaint:** é baixado do Hugging Face só quando você clica em **Baixar**.
- **Servidor Web:** funciona só na sua rede local e vem desligado.

Os logs ficam só no seu PC. Por padrão, eles não gravam o texto do jogo nem as traduções, e as chaves de API nunca aparecem neles. A única forma de um log chegar até nós é você mesmo enviá-lo.

Do nosso lado, vemos só o número de downloads que o GitHub mostra na página de versões.

---

## English

**Ranmza GT** captures an area of the screen, recognizes the text with OCR, translates it and draws the translation **overlaid on the game**, in the same position as the original text — like a floating subtitle. Works with any game, visual novel, video or program that shows text on screen.

### How it works

1. **Capture** — when you press the hotkey, it grabs the chosen area of the screen; in Subtitle Mode, it reads the subtitle area by itself, line by line.
2. **OCR** — recognizes the text in the image (native Windows OCR or OneOCR, your choice).
3. **Translation** — sends the text to the chosen service (Google, Google Cloud, DeepL, Azure, OpenAI, Claude, Gemini or Groq) and gets the translation back.
4. **Overlay** — draws the translation over the game, in the same position as the original text, without stealing focus or freezing the window.

Built in **Rust** 🦀 — native for Windows, no heavy runtime, low CPU/memory footprint even while running alongside a game.

📖 **[Open the full manual](https://brunodomenesdutra.github.io/ranmzagt/#/en/)** &nbsp;·&nbsp; ⬇️ **[Download (Releases)](https://github.com/BrunoDomenesDutra/ranmzagt/releases)**

### Support the project

Ranmza GT is free. If it helped you, consider supporting the development:

<p align="center">
  <a href="https://ko-fi.com/ranmza"><img src="https://img.shields.io/badge/Ko--fi-support-FF5E5B?logo=kofi&logoColor=white" alt="Ko-fi"></a>
  <a href="https://livepix.gg/ranmza"><img src="https://img.shields.io/badge/LivePix-donate%20with%20Pix-32BCAD?logo=pix&logoColor=white" alt="LivePix"></a>
</p>

☕ **[Ko-fi](https://ko-fi.com/ranmza)** (card/PayPal, worldwide) &nbsp;·&nbsp; 💚 **[LivePix](https://livepix.gg/ranmza)** (Pix, Brazil only)

### Privacy

Ranmza GT does not collect any of your data. There is no analytics, telemetry, tracking or user account, and nothing is sent to us.

Everything the program stores stays on your computer, in its own folder: settings, profiles, API keys (encrypted by Windows), translation cache and logs.

The program only connects to the internet in these cases, and none of them goes through us:

- **Translation:** the text read on screen goes straight from your PC to the translation service you picked (Google, DeepL, OpenAI, Claude…), with your key. In Vision mode, the image of the area goes too. What the service does with it follows its own privacy policy.
- **New version notice:** on startup, the program asks GitHub whether a newer version exists. Only the installed version number is sent. You can turn it off in **General › Config → Updates**.
- **Inpaint model:** it is downloaded from Hugging Face only when you click **Download**.
- **Web server:** it only works on your local network and comes off by default.

Logs stay on your PC only. By default, they do not record game text or translations, and API keys never show up in them. The only way a log reaches us is if you send it yourself.

On our side, we only see the download count that GitHub shows on the releases page.
