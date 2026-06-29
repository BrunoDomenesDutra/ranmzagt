## 5. Configuring translation

### Text type: dialog or menu?

In the **OCR** tab, under "Block Grouping", choose:

- **Paragraph Mode** (default) — groups nearby lines into a single translation block. Use for **dialogs, character speech, flowing text** (visual novels, JRPGs).
- **Line Mode** — each line becomes a separate translation. Use for **menus, inventory, status, HUD** — where each line is independent info and shouldn't be mixed with the one above or below.

If the program is grouping lines that should be separate (or separating a speech that should stay together), adjust the **"Grouping sensitivity"** control that appears in Paragraph Mode:
- Text being **separated too much**? Increase the value (up to 3.0).
- Text being **grouped too much**? Decrease the value (down to 0).

### Improving difficult text recognition

If the program isn't detecting text correctly (small fonts, stylized, with effects), go to the **Capture** tab and enable **Preprocessing**. A few quick tips:

- **Small text**: increase **Upscale** (2x or 3x usually fixes it).
- **Font with thick outline**: increase **Sharpen** a bit.
- **Text with low contrast against background**: increase **Contrast**.
- **Light text on dark background** (or vice versa, if it's giving wrong results): try **Invert colors**.

Don't know where to start? Use the **Lab** tab — you can test all these options on sample images, see the result in real time, and then apply the best-working configuration directly to Capture or Caption.

### Switching OCR engine (advanced)

If preprocessing still doesn't fix recognition, the **OCR** tab lets you switch the text recognition "engine":

- **WinOCR** (default) — fast, comes ready, but can fail on very stylized fonts.
- **OneOCR** (experimental, Windows 11) — the OCR engine from Windows Screenshot Tool (Snipping Tool), much better than WinOCR on stylized fonts and auto-detects language (no need to configure source language). You copy 3 files from Windows itself to a folder of yours — the OCR tab shows step-by-step. Because it uses an unofficial Microsoft API, a Snipping Tool update might break it; if so, just re-extract the files.

---
