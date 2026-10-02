# 8. Vision Mode — when OCR fails

Sometimes regular text recognition (OCR) misreads letters, loses pieces of the text or gets completely lost with very stylized fonts, with symbols or icons in the middle of the text.

For those cases, use **Translate with AI Vision**. Along with the recognized text, the program **sends the image of the area to the AI**, which "looks" at the image, fixes what the OCR misread and translates. A symbol or icon in the middle of a sentence becomes `[...]` in the translation.

Just like regular Translate, Vision has both modes, and you pick by shortcut:

- **`Numpad5`** — Vision in **paragraph mode** (dialogues).
- **`Numpad6`** — Vision in **line mode** (menus and lists).

**Important:**
- It only works with **OpenAI, Anthropic (Claude), Gemini** or **OpenAI-compatible** with *The model accepts images* on. With Google Translate, Google Cloud, DeepL, Azure or Groq, the shortcut translates only the OCR text and shows the *"Vision needs an AI provider"* alert.
- It uses the same model chosen in **Translation › Translators**.
- It is a bit slower and **always makes a new call** to the AI: it does not use saved translations, because the answer depends on the image.
- The position of the translation on screen still depends on where text recognition found something.

**When to use it**: hand-drawn fonts, stylized credits, text mixed with icons/symbols (e.g. "press [button icon] to continue"), or whenever the regular shortcut ("Translate") returns nonsense.

---
