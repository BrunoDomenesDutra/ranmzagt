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

---
