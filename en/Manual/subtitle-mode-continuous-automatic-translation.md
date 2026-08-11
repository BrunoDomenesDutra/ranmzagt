# 8. Subtitle Mode — continuous automatic translation

For scenes with ongoing dialog (cutscenes, visual novel auto mode, videos with subtitles), Subtitle Mode translates **on its own, repeatedly**, without you needing to press anything.

## How to set up

1. In **Overlay › Subtitles**, adjust capture options (interval, how many lines to show, etc.) — defaults work well for most cases.
2. Press **Select subtitle area** (default `Numpad1`) and draw a rectangle over where the game's subtitle/dialogue appears.
3. Press **Toggle subtitles** (default `Numpad0`) to activate.

From then on, the program watches that area, automatically translating whenever new text appears and stays "still" for a moment (this avoids translating letters appearing one by one in "typewriter" effects).

Translations appear **above** the selected area, in order (most recent at bottom), and disappear on their own if no new text appears for a few seconds.

## Letting the AI "remember" previous lines

If you're using OpenAI, Claude, or Gemini, **Translation › AI** has a **"Previous lines"** control (0 to 20, default 5). When enabled, the AI gets the last already-translated lines as reference before translating the next one — this helps keep the same character names, terms, and tone throughout a conversation. If you notice the AI is changing a character's name or translation tone from one line to another, increase this value; if you prefer each line translated without depending on previous ones, leave it at 0.

> **DeepL** also benefits from previous lines as context, **at no extra cost** — it gets the last lines as reference (following the same **"Previous lines"** control) to keep character names and terms consistent. Even though it's not a conversational AI, this makes continuous translation more cohesive. **Google Translate** doesn't use this context.

## Separate appearance

Overlay › Subtitles has its own font, color, background and outline options — separate from manual translation — so you can keep the continuous subtitle smaller/more discreet and the manual translation (`Numpad8`/`Numpad9`) bigger, for example. The image preprocessing is independent too.

## Turning it off

Press **`Numpad0`** again, or the green bubble button on the floating toolbar. The subtitle on screen clears immediately.

The mode also **turns itself off** after a while with no text detected in the region, so it doesn't keep running for nothing when you leave the cutscene and forget to switch it off. The timeout is set in *Overlay › Subtitles → Turn off Subtitle Mode after inactivity*: Never, 1, 2, 3, 5 or 10 minutes (default 1 minute). Note this **turns the mode off**, not just hides the subtitle — press `Numpad0` to switch it back on.

---
