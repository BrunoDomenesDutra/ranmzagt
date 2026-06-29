## 8. Caption Mode — continuous automatic translation

For scenes with ongoing dialog (cutscenes, visual novel auto mode, videos with subtitles), Caption Mode translates **on its own, repeatedly**, without you needing to press anything.

### How to set up

1. In the **Caption** tab, adjust capture options (interval, how many lines to show, etc.) — defaults work well for most cases.
2. Press **Select caption area** (default `Numpad1`) and draw a rectangle over where the game's caption/dialog appears.
3. Press **Toggle Caption Mode** (default `Numpad0`) to activate.

From then on, the program watches that area, automatically translating whenever new text appears and stays "still" for a moment (this avoids translating letters appearing one by one in "typewriter" effects).

Translations appear **above** the selected area, in order (most recent at bottom), and disappear on their own if no new text appears for a few seconds.

### Letting the AI "remember" previous lines

If you're using OpenAI, Claude, or Gemini, the **AI** tab has a **"Previous lines"** control (0 to 20, default 5). When enabled, the AI gets the last already-translated lines as reference before translating the next one — this helps keep the same character names, terms, and tone throughout a conversation. If you notice the AI is changing a character's name or translation tone from one line to another, increase this value; if you prefer each line translated without depending on previous ones, leave it at 0.

> **DeepL** also benefits from previous lines as context, **at no extra cost** — it gets the last lines as reference (following the same **"Previous lines"** control) to keep character names and terms consistent. Even though it's not a conversational AI, this makes continuous translation more cohesive. **Google Translate** doesn't use this context.

### Separate appearance

The Caption tab has its own font, background, and outline options — separate from manual translation — so you can keep continuous caption smaller/more discreet and manual translation (`Numpad9`) bigger, for example.

### Turning it off

Press **Numpad0** again (or the corresponding button, if you created one on the floating toolbar). The caption on screen clears immediately.

---
