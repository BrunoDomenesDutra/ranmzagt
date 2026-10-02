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

It only applies to Subtitle Mode; screen capture reads all the text in the area.

## OpenAI fast queue

With OpenAI selected, the model card has the **OpenAI fast queue** option. When on, OpenAI serves your requests first, at twice the price per token. It helps when OpenAI is slow. It comes **off**: the key is yours, so the doubled bill only happens if you turn it on.

---
