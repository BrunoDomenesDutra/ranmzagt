# 1. What the program does

Ranmza GT takes a "screenshot" of an area of the screen, recognizes the text in it, translates it and shows the translation **over the game**. It works with any game, visual novel, video or program that shows text on screen: subtitles, dialogues, menus, letters, items.

There are two ways to translate:

- **Screen capture** — you press a key and the program translates the marked area once, with the translation drawn over each piece of the original text. Good for menus, inventory, letters, still dialogues and screens full of text.
- **Subtitle Mode** — you turn it on once and the program keeps reading the subtitle area by itself, translating each new line as it appears. Good for cutscenes, videos and dialogues that play on their own.

> **⚠️ Essential requirement: the game must be in Windowed or Borderless Window mode.** Ranmza GT draws the translation **over** the game window — so run the game in **Windowed** mode or, preferably, **Borderless Window** (*Borderless* / *Borderless Fullscreen*), which fills the whole screen and still lets the translation show on top. In **Exclusive Fullscreen**, Windows hands the screen to the game alone and no program can draw over it — the translation will not show. Typical symptom: you press Translate, the translation even shows up in the **History** tab, but nothing appears over the game. Fix: switch the game to **Borderless Window** in its video options.

The basic screen capture flow is always:

1. You choose **where** the text is (an area of the screen).
2. You press a shortcut to **translate**.
3. The translation shows up over the game.
4. You press another shortcut to **clear** it when you want, or it disappears by itself after a while.

Subtitle Mode has its own area and its own on/off shortcut — see [section 9](/en/Manual/subtitle-mode-continuous-automatic-translation.md).

---
