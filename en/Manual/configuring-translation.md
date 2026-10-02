# 6. Configuring translation

## Text type: dialog or menu?

The grouping mode **is not chosen in a tab** — it is decided at capture time, by the shortcut you press:

- **`Numpad8` — Paragraph Mode** — joins nearby lines into a single translation block. Use it for **dialogues, character lines, running text** (visual novels, JRPGs).
- **`Numpad9` — Line Mode** — each line becomes a separate translation. Use it for **menus, inventory, stats, HUD** — where each line is independent information and must not be mixed with the one above or below.

The same goes for Vision: `Numpad5` is paragraph and `Numpad6` is line.

If Paragraph mode is joining lines that should be separate (or splitting a line that should stay together), adjust the **Grouping sensitivity** in **Overlay › Capture**:

- Text **split too much**? Raise the value (up to 3.0).
- Text **joined too much**? Lower the value (down to 0.5).

This setting only affects Paragraph mode — Line mode ignores it.

<p align="center"><img src="media/ocr-sensibilidade.png" alt="Grouping sensitivity, in Overlay › Capture" width="820"></p>

<p align="center"><i>The setting is in the <b>Overlay › Capture</b> tab, in the <b>Paragraph Mode Fine-Tuning</b> card.</i></p>

## Switching OCR engine — and why OneOCR is recommended

OCR is the text reader: it turns what shows up in the marked area into text to be translated. It is used in screen capture and in Subtitle Mode, and the better it reads, the better the translation. In **General › OCR** you choose between two:

- **WinOCR** (native to Windows) — ready out of the box, nothing to install, and the default. It reads text on a plain background well, but gets lost easily when the background behind the text has details, colors or movement, and only reads languages whose pack is installed in Windows.
- **OneOCR** (recommended) — the text reader of the Windows 11 Snipping Tool. It is the one you should use.

<p align="center"><img src="media/geral-ocr.png" alt="General › OCR tab with WinOCR" width="820"></p>

**Why OneOCR is far better:**

- **It reads much more accurately.** Stylized fonts, text with outline, shadow or effects on top, small text, text over busy backgrounds — situations where WinOCR returns swapped letters or missing words and OneOCR reads correctly.
- **All languages at once, with no setup.** It is a single multilingual model (Latin, Japanese, Chinese, Korean, Cyrillic…) with automatic detection: there is no "text language" to choose and no Windows language pack to install. A game that mixes English and Japanese on the same screen is read the same way.
- **Fewer things to go wrong day to day.** No missing language pack and no switching languages for every game.

**Is it worth the trouble of getting the files?** Yes, by far. It is three files copied once — after that the quality of the whole translation goes up, because everything that comes after (grouping, translation, subtitles) depends on the text being read correctly.

**What it needs:** the files `oneocr.dll`, `oneocr.onemodel` and `onnxruntime.dll`. The program **never goes after them by itself**: you copy them, with one click.

**On Windows 11 it is one click.** Choose *OneOCR* in **General › OCR** (or in the OCR step of the guide) and use the **Detect and copy** button: the program finds the installed Snipping Tool, copies the 3 files to its folder and sets everything up. If the Snipping Tool is not installed, or is a version without the files, it tells you instead of failing silently. Until the files are copied, the card shows *"Did not load"* and the OCR stays stopped.

<p align="center"><img src="media/geral-ocr-oneocr.png" alt="OneOCR card, in General › OCR" width="820"></p>

<p align="center"><i>With <b>OneOCR</b> selected, the card has the <b>Detect and copy</b> button, the folder field and, below, the step by step for Windows 10.</i></p>

**On Windows 10 it is manual**, because **the files only come with the Windows 11 Snipping Tool** (OneOCR itself runs on both). Copy the three from a Windows 11 machine and point to the folder with **Browse...** — the step by step inside the card has the PowerShell command that shows where they are.

Since it uses an unofficial Microsoft API, a Snipping Tool update can break the integration; in that case, click **Detect and copy** again.

## Subtitle alphabet filter

In Subtitle Mode, the program can consider only the letters of one alphabet and ignore the rest: Latin, Japanese/Chinese, Korean or Cyrillic. Useful when names, signs or symbols in another alphabet show up near the subtitle. It is in **Overlay › Subtitles**, in the **Original subtitle alphabet** card:

- With **OneOCR**, you choose the alphabet in the list (default: *Any alphabet*).
- With **WinOCR**, the filter follows the language chosen in **General › Language** by itself.

Example: in the scene below, the English subtitle sits on top of a Japanese news headline. With *Any alphabet*, the program reads both together and sends the Japanese to the translation in the middle of the line. With *Latin*, it ignores the Japanese characters and translates only the subtitle.

<p align="center"><img src="media/legenda-alfabeto-exemplo.png" alt="English subtitle on top of a Japanese headline" width="820"></p>

It only applies to Subtitle Mode; screen capture reads all the text in the area.

## OpenAI fast queue

With OpenAI selected, the model card has the **OpenAI fast queue** option. When on, OpenAI serves your requests first, at twice the price per token. It helps when OpenAI is slow. It comes **off**: the key is yours, so the doubled bill only happens if you turn it on.

## AI on your PC or another service

Many AI programs and services accept the same request format as OpenAI: LM Studio, Ollama, llama.cpp, OpenRouter and others. The **OpenAI-compatible** translator talks to any of them. You enter the address and the model name, and the program sends the game text there.

**Setting it up.** In **Translation › Translators**, pick *OpenAI-compatible* and fill in:

- **Base URL** — the server address, as the AI program shows it. It can be with or without `/chat/completions` at the end. A server on your own PC is usually something like `http://localhost:1234/v1` (LM Studio) or `http://localhost:11434/v1` (Ollama).
- **Model** — the exact model name, as the server shows it. There is no list to pick from: each server has its own.
- **The model accepts images** — only turn it on if the model reads images. It is what enables [Vision Mode](/en/Manual/vision-mode-when-ocr-fails.md) for this translator.
- **API Keys** — only if the service asks for one. A server on your PC usually does not, and the field stays empty.

<p align="center"><img src="media/tradutores-openai-compat.png" alt="Translators with OpenAI-compatible: Base URL, Model, The model accepts images and Test connection" width="820"></p>

Then click **Test connection**. It translates one word through the server and shows whether it worked or which error came back. The button only unlocks with the URL and the model filled in.

**Good practices**

- **Use a model that follows instructions.** Very small models sometimes answer with comments instead of the translation, and that answer is discarded.
- **A server on the same PC shares the graphics card with the game.** Both the game and the translation can get slower. Subtitles wait for the answer, so a slow model delays the subtitle.
- **The first translation can take a while.** Many servers only load the model on the first call. The program waits up to 90 seconds for an answer with this translator.
- **Reasoning models:** the `<think>` block some models write before the answer is discarded.
- With the server off, the *"API compatível: server not responding"* alert shows up. Without a URL or a model, *"API compatível: fill in URL and model"*.

---
