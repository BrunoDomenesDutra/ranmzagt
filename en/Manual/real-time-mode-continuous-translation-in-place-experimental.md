# 9. Real-time Mode — continuous translation in place (experimental)

> **Experimental feature** — configured via the **Experimental** tab. Behavior may still change and bugs are expected.

Real-time Mode combines the best of the other two modes: it's **continuous and automatic** like Subtitle Mode (no need to press anything for each line), but draws the translation **in the original text's place**, over each detected line, like Translate mode — instead of stacking everything in a box outside the area. It works over its **own area**, usually bigger than the subtitle area (covers the entire dialog box, character name, multiple lines at once).

It's ideal for conversations with NPCs where **name + multiple lines of speech** appear at the same time, and you want everything translated live, in the original position, without clicking.

## How to use

Everything about Real-time Mode lives in the **Experimental** tab, inside the *Real-time Mode (live overlay)* card — including the shortcuts, which come with **no key assigned**. That's deliberate: while the feature is experimental, it doesn't claim a key on your keyboard without you asking.

1. Open the **Experimental** tab and expand the **Real-time Mode** card.
2. Turn on **Allow Real-time Mode**. That switch only **unlocks** the hotkey — it doesn't start translating anything by itself. With it off, the hotkey does absolutely nothing.
3. Set the two keys right there: **Toggle Real-time** and **Select Real-time area**. Pick free Numpad keys (`Numpad3` and `Numpad4` are unused in the factory defaults) or any other combination.
4. Adjust the options if you like (interval, font, background, outline, auto-clear) — the defaults work fine.
5. Press your **select area** key and draw the rectangle over the region where text appears.
6. Press your **toggle** key. Translation starts appearing overlaid, updating automatically as text changes. Press it again to turn it off.

> **Turn on "Hide overlay from screen capture" first**, the top card of the Experimental tab. Without it, the translation the program draws on top ends up recaptured by its own OCR on the next cycle — the text feeds back on itself and turns to mush. The Real-time card reminds you of this.

> Because it's continuous and draws multiple areas live, Real-time Mode is heavier than other modes. If you notice stuttering, increase the **interval** in the card.

## Stability with animated backgrounds

In scenes with moving backgrounds (RPG game animations, videos), text recognition may vary from frame to frame, making the translation **shake** or **flicker**. Two adjustments in the Real-time card control this:

- **Position stability** — how many pixels text must move for the translation to reposition. Higher = translation more "still" (ignores shaking); lower = follows text more closely. (Default: 12px.)
- **Hold on OCR failure** — how many cycles a translation stays on screen when recognition fails for a moment, avoiding flicker. Higher = holds longer; lower = disappears faster. (Default: 6.)

Quick rule: still **shaking**? Increase *Position stability*; still **flickering**? Increase *Hold on OCR failure*.

## Typewriter effect (typewriter)

Many games reveal text **letter by letter**. To avoid translating incomplete sentences, turn on **Wait for the text to settle**, in the *Wait for complete text (typewriter effect)* card of the Experimental tab: the program waits for the line to stop changing before translating. Works for both Real-time Mode and Subtitle Mode.

Three controls fine-tune it: how many consecutive reads must match (*Required stable captures*), how alike they must be to count as identical (*'Same text' threshold*), and the longest it will wait before translating whatever it has (*Wait cap*).

---
