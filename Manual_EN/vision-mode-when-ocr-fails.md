## 7. Vision Mode — when OCR fails

Sometimes normal text recognition (OCR) misses letters, loses parts of text, or gets completely lost on very stylized/artistic fonts, with symbols or icons mixed in the text.

For those cases, use the **Translate with AI Vision** hotkey (default `Numpad4`). Instead of relying only on recognized text, the program **sends the screen image to Artificial Intelligence**, which "looks" at the image and understands better what's written, even if text recognition got it wrong.

**Important:**
- Only works with **OpenAI, Claude, or Gemini** (Google Translate and DeepL don't support this mode).
- It's a bit slower and **always makes a new call** to the AI (doesn't use translation history).
- The translation's position on screen still depends on where text recognition found something — so in rare cases, the translation might be larger than the detected area.

**When to use**: hand-drawn fonts, stylized credits, text with icons/symbols mixed in (ex: "press [button icon] to continue"), or whenever the normal hotkey ("Translate") returns nonsensical text.

---
