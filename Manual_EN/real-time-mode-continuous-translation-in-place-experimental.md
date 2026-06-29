## 9. Real-time Mode — continuous translation in place (experimental)

> **Experimental feature** — configured via the **Experimental** tab. Behavior may still change and bugs are expected.

Real-time Mode combines the best of the other two modes: it's **continuous and automatic** like Caption Mode (no need to press anything for each line), but draws the translation **in the original text's place**, over each detected line, like Translate mode — instead of stacking everything in a box outside the area. It works over its **own area**, usually bigger than the caption area (covers the entire dialog box, character name, multiple lines at once).

It's ideal for conversations with NPCs where **name + multiple lines of speech** appear at the same time, and you want everything translated live, in the original position, without clicking.

### How to use

1. In the **Experimental** tab, adjust Real-time options (interval, font, background, outline, auto-off) — defaults work fine.
2. Press **Select Real-time area** (default `Numpad6`) and draw the rectangle over the region where text appears.
3. Press **Toggle Real-time Mode** (default `Numpad3`) to activate. Translation starts appearing overlaid, updating automatically as text changes.
4. Press `Numpad3` again to turn it off.

> Because it's continuous and draws multiple areas live, Real-time Mode is heavier than other modes. If you notice stuttering, increase the **interval** in the Experimental tab.

### Stability with animated backgrounds

In scenes with moving backgrounds (RPG game animations, videos), text recognition may vary from frame to frame, making the translation **shake** or **flicker**. Two adjustments in the Experimental tab control this:

- **Position stability** — how many pixels text must move for the translation to reposition. Higher = translation more "still" (ignores shaking); lower = follows text more closely. (Default: 12px.)
- **Hold on OCR failure** — how many cycles a translation stays on screen when recognition fails for a moment, avoiding flicker. Higher = holds longer; lower = disappears faster. (Default: 6.)

Quick rule: still **shaking**? Increase *Position stability*; still **flickering**? Increase *Hold on OCR failure*.

### Typewriter effect (typewriter)

Many games reveal text **letter by letter**. To avoid translating incomplete sentences, turn on **Typewriter** in the Experimental tab: the program waits for text to "settle" (stop changing) before translating. Works for both Real-time Mode and Caption Mode. You can adjust how stable text needs to be and the maximum wait time before translating anyway.

---
