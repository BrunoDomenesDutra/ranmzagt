# 6. Configuring translation

## Text type: dialog or menu?

The grouping mode **isn't picked in a tab** — it's decided at capture time, by which hotkey you press:

- **`Numpad8` — Paragraph Mode** — groups nearby lines into a single translation block. Use for **dialogs, character speech, flowing text** (visual novels, JRPGs).
- **`Numpad9` — Line Mode** — each line becomes a separate translation. Use for **menus, inventory, status, HUD** — where each line is independent info and shouldn't be mixed with the one above or below.

The same goes for Vision: `Numpad5` is paragraph and `Numpad6` is line.

If Paragraph Mode is grouping lines that should be separate (or separating a speech that should stay together), adjust the **Grouping sensitivity**, in **Overlay › Capture**:
- Text being **separated too much**? Increase the value (up to 3.0).
- Text being **grouped too much**? Decrease the value (down to 0).

This adjustment only affects Paragraph Mode — in Line Mode it is ignored.

<p align="center"><img src="media/ocr-sensibilidade.png" alt="Grouping sensitivity, in Overlay › Capture" width="820"></p>

<p align="center"><i>The setting sits in the <b>Overlay › Capture</b> tab, in the <b>Paragraph Mode Fine-Tuning</b> card.</i></p>

## Improving difficult text recognition

If the program isn't detecting text correctly (small fonts, stylized, with effects), go to **Overlay › Capture** and enable **Preprocessing**. A few quick tips:

- **Small text**: increase **Upscale** (2x or 3x usually fixes it).
- **Font with thick outline**: increase **Sharpen** a bit.
- **Text with low contrast against background**: increase **Contrast**.
- **Light text on dark background** (or vice versa, if it's giving wrong results): try **Invert colors**.

<p align="center"><img src="media/captura-preprocessamento.png" alt="OCR Preprocessing card, in Overlay › Capture" width="820"></p>

<p align="center"><i>The <b>OCR Preprocessing</b> card, in <b>Overlay › Capture</b>. The extra filters (Threshold, Blur, Dilation, Erosion) only kick in with <b>Advanced</b> turned on.</i></p>

Don't know where to start? Use **Tools › Lab** — you can test all these options on sample images, see the result in real time, and then apply the best-working configuration directly to Capture or Subtitles.

## Switching OCR engine (advanced)

If preprocessing still doesn't fix recognition, **General › OCR** lets you switch the text recognition "engine":

- **WinOCR** (default) — fast (~30 ms), comes ready, but can fail on very stylized fonts.
- **OneOCR** (experimental) — the OCR engine from the Snipping Tool, much better than WinOCR on stylized fonts and auto-detects language (no need to configure source language). You copy 3 files from Windows itself to a folder of yours — the OCR tab shows step-by-step. Because it uses an unofficial Microsoft API, a Snipping Tool update might break it; if so, just re-extract the files.

## OpenAI-compatible service

Many AI services and programs accept the same request format as the OpenAI API. The **OpenAI-compatible** engine talks to any of them: you enter the address and the model name, and the program sends the text on screen there.

**Setting it up.** In **Translation › Translators**, pick *OpenAI-compatible* and fill in:

- **Base URL** — the service address, as its documentation shows it. With or without `/chat/completions` at the end. A server running on your own PC is usually something like `http://localhost:1234/v1`.
- **Model** — the exact model name, as the service shows it. There's no list to pick from: each service has its own.
- **API key** — only if the service asks for one. A local server usually doesn't, and then the field stays empty.
- **The model accepts images** — turn it on only if the model reads images. It enables [Vision Mode](/en/Manual/vision-mode-when-ocr-fails.md) on this engine. With it off, Vision Mode warns that the engine doesn't support it.

<p align="center"><img src="media/tradutores-openai-compat.png" alt="Translators with OpenAI-compatible selected, showing Base URL, Model and the image option" width="820"></p>

Then use **Test connection**. It translates one word through the real path and shows how long the response took.

**What the service must accept.** The program sends `POST <Base URL>/chat/completions` with `model`, `messages`, `temperature` and `max_tokens`, plus the key (when there is one) in the `Authorization: Bearer` header. The translation is read from `choices[0].message.content`. The prompt, Game Info and Subtitle Mode's Conversation Context are sent the same way as with OpenAI.

**Good practices**

- **Use a model that follows instructions.** The response has to come in a fixed format, with a number for each block. Small models get that format wrong more often, and when that happens the screen is translated by Google Translate.
- **A server on the same PC shares the graphics card with the game.** Both the game and the translation can get slower.
- **The first translation can take a while.** Many local servers only load the model on the first call. The program waits up to 90 seconds for a response on this engine.
- **Reasoning models spend tokens thinking.** If you get the warning about a response cut off at the token limit, raise *Max Tokens* in **Translation › AI** or switch models. The `<think>` block some models write before the answer is discarded.
- **The whole screen goes in a single request.** With the OpenAI, Claude and Gemini engines, screens with many blocks are split into parallel requests. Not here, because a local server usually handles one request at a time.

---
