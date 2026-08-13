# 6. Making translation look like the game

In **Overlay › Capture**, in the **Text** card:

- **Font**: choose from fonts in the `fonts/` folder or use the system default (Arial). The preview right below shows how it looks.
- **Text color**: white by default; change it to match the game's palette.
- **Font size** and **Line height**: adjust so text is readable and well-spaced.
- **Auto-fit**: leave enabled so the program **automatically shrinks the font** until the whole translation fits the original text's space — this way text is never cut off. Tip: with Auto-fit on, set **Font size** to the maximum — the program finds the largest size that shows the complete translation filling the area nicely, and raising the control further changes nothing.
- **Background**: draws a dark box behind the text (with adjustable opacity) to guarantee readability over any scenery.
- **Outline**: alternative to background — draws a black border around letters, no visible box, for a more discrete/integrated look.

> Background and outline are alternatives — enabling one disables the other automatically.

<p align="center"><img src="media/captura-texto-fundo.png" alt="Text and Background & Outline cards, in Overlay › Capture" width="720"></p>

<p align="center"><i>The <b>Text</b> and <b>Background &amp; Outline</b> cards, in <b>Overlay › Capture</b>. The preview under the font shows the result before you try it in the game.</i></p>

## How long translation stays on screen

Under "Display", choose how long the translation stays visible after appearing: 15s, 30s, 1 minute (default), 2, 5, or 10 minutes — or "Never" (translation only disappears when you press clear or translate again).

The same card holds **"Hide the translation from recordings and streams"**: when on, the translation stays on your screen as usual but doesn't show up for capture programs. Handy for recording the game without the translation on top. It only affects manual translation; Subtitle Mode has the equivalent option in its own tab.

<p align="center"><img src="media/captura-exibicao-duracao.png" alt="Display card, in Overlay › Capture" width="820"></p>

<p align="center"><i>The <b>Display</b> card, in <b>Overlay › Capture</b>.</i></p>

> Only works with programs running **ON THIS PC** (OBS, Game Bar, NVIDIA ShadowPlay, etc). If you record with a capture card, the translation still shows up — it's Windows that hides the window, and what goes out the video cable is the whole screen.

---
