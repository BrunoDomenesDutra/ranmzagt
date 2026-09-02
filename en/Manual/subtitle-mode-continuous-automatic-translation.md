# 9. Subtitle Mode — continuous automatic translation

For scenes with ongoing dialog (cutscenes, visual novel auto mode, videos with subtitles), Subtitle Mode translates **on its own, repeatedly**, without you needing to press anything.

## How to set up

1. In **Overlay › Subtitles**, adjust capture options (interval, how many lines to show, etc.) — defaults work well for most cases.
2. Press **Select subtitle area** (default `Numpad1`) and draw a rectangle over where the game's subtitle/dialogue appears.
3. Press **Toggle subtitles** (default `Numpad0`) to activate.

<p align="center"><img src="media/overlay-legenda-captura.png" alt="Overlay › Subtitles tab — Capture" width="820"></p>

From then on, the program watches that area, automatically translating whenever new text appears and stays "still" for a moment (this avoids translating letters appearing one by one in "typewriter" effects).

By default, translations appear **above** the selected area, in order (most recent at bottom), and disappear on their own if no new text appears for a few seconds. You can swap that for drawing over the original subtitle instead — that's the next topic.

<div style="position:relative;padding-top:56.25%;max-width:820px;margin:0 auto">
  <iframe src="https://player.vimeo.com/video/1217784520"
          style="position:absolute;top:0;left:0;width:100%;height:100%;border:0"
          allow="fullscreen; picture-in-picture" allowfullscreen
          title="Subtitle Mode translating on its own"></iframe>
</div>

<p align="center"><i>Subtitle Mode translating on its own, with the translations above the selected area.</i></p>

## Replacing the original subtitle in place

In **Overlay › Subtitles**, the first card (*Translation position*) has the **"Replace the original subtitle in place"** option. When on, the translation stops appearing above the area and is drawn **over** it, covering the game's original subtitle — as if the game were subtitled in your language.

In this mode the program shows **one line at a time**, and the *Visible lines* control is locked at 1. The reason is simple: the area you selected is the size of **one** game subtitle, so stacking two or three translated lines in there wouldn't fit — the text would end up cut off at the edge. Your line choice is kept and comes back as soon as you turn the option off.

> If the translation doesn't fit even with a single line (English or Japanese is often shorter than other languages), lower the *Font size* in the **Text** card, or redo the area selection a bit taller than the game's subtitle.

> In this mode the subtitle is **hidden from screen capture**. It's not a defect: that's exactly what keeps the OCR from re-reading its own translation on the next cycle and feeding back on itself. Only works with programs running **ON THIS PC** (OBS, Game Bar, NVIDIA ShadowPlay, etc). If you record with a capture card, the translation still shows up.

The option applies to Subtitle Mode only — manual translation (`Numpad8`/`Numpad9`) and Real-time Mode are not affected.

<div style="position:relative;padding-top:56.25%;max-width:820px;margin:0 auto">
  <iframe src="https://player.vimeo.com/video/1218094053"
          style="position:absolute;top:0;left:0;width:100%;height:100%;border:0"
          allow="fullscreen; picture-in-picture" allowfullscreen
          title="Translation covering the original subtitle"></iframe>
</div>

<p align="center"><i>The translation drawn over the game's original subtitle. The video was recorded with a phone because, in this mode, the subtitle is hidden from screen capture — a normal screen recording wouldn't show the feature working.</i></p>

## Letting the AI "remember" previous lines

If you're using OpenAI, Claude, or Gemini, **Translation › AI** has a **"Previous lines"** control (0 to 20, default 5). When enabled, the AI gets the last already-translated lines as reference before translating the next one — this helps keep the same character names, terms, and tone throughout a conversation. If you notice the AI is changing a character's name or translation tone from one line to another, increase this value; if you prefer each line translated without depending on previous ones, leave it at 0.

> **DeepL** also benefits from previous lines as context, **at no extra cost** — it gets the last lines as reference (following the same **"Previous lines"** control) to keep character names and terms consistent. Even though it's not a conversational AI, this makes continuous translation more cohesive. **Google Translate** and **Azure Translator** don't use this context — the Azure translation API has no context parameter.

## Separate appearance

Overlay › Subtitles has its own font, color, background and outline options — separate from manual translation — so you can keep the continuous subtitle smaller/more discreet and the manual translation (`Numpad8`/`Numpad9`) bigger, for example. The image preprocessing is independent too.

## Turning it off

Press **`Numpad0`** again, or the green bubble button on the floating toolbar. The subtitle on screen clears immediately.

The mode also **turns itself off** after a while with no text detected in the region, so it doesn't keep running for nothing when you leave the cutscene and forget to switch it off. The timeout is set in *Overlay › Subtitles → Turn off Subtitle Mode after inactivity*: Never, 1, 2, 3, 5 or 10 minutes (default 1 minute). Note this **turns the mode off**, not just hides the subtitle — press `Numpad0` to switch it back on.

---
