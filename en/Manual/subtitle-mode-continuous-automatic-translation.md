# 9. Subtitle Mode — continuous automatic translation

For scenes with continuous dialogue (cutscenes, visual novel auto mode, subtitled videos), Subtitle Mode translates **by itself**, without you pressing anything for each line.

## How to set up

1. Press **Select subtitle area** (default `Numpad1`) and draw a rectangle over where the subtitle shows up in the game. This area is separate from the screen capture area.
2. Press **Toggle subtitles** (default `Numpad0`) to turn it on. An alert on screen confirms it.

The program always opens with subtitles off. The options are in **Overlay › Subtitles**, and the defaults already work well for most cases.

<p align="center"><img src="media/en/overlay-legenda-captura.png" alt="Overlay › Subtitles tab — Capture and alphabet" width="820"></p>

From then on, the program watches that area several times per second and translates each new text as soon as it shows up and repeats in a second reading. This avoids translating a line that is still being written on screen. If the area stays the same, the program does not even read the text again.

By default, the translation shows up **above** the selected area and disappears by itself a few seconds after the subtitle leaves the game. You can switch that to the translation on top of the original subtitle — that is the next topic.

<div style="position:relative;padding-top:56.25%;max-width:820px;margin:0 auto">
  <iframe src="https://player.vimeo.com/video/1217784520"
          style="position:absolute;top:0;left:0;width:100%;height:100%;border:0"
          allow="fullscreen; picture-in-picture" allowfullscreen
          title="Subtitle Mode translating by itself"></iframe>
</div>

<p align="center"><i>Subtitle Mode translating by itself, with the translation above the selected area.</i></p>

## Ignore text away from the center of the area

The **Ignore text away from the center of the area** option, in the **Capture** card, comes on. With it, the program ignores text near the edges of the area, like signs and other game text that shows up beside the subtitle.

- The tighter the area is around the subtitle, the better it works. Mark only the strip where the subtitle appears.
- In games with left-aligned dialogue, like some RPGs and visual novels, keep this option off.

## Stick to the detected text

In **Overlay › Subtitles**, the first card (*Translation position*) has the **Stick to the detected text** option. When on, the translation no longer shows above the area and is drawn **on top of the original line**, with the same line breaks, covering the game subtitle — as if the game were subtitled in your language.

- In this mode the program shows **one line at a time**, and *Lines on screen* stays at 1.
- The translation **is not shrunk to fit**: a larger font spills over the area, on purpose. That is how you can make the subtitle bigger than the game's.
- The selected area is still what the program reads. It must fit the whole game subtitle.

> In this mode the subtitle is **hidden from screen captures**. That is what stops the OCR from reading its own translation in the next cycle. It only works with programs running **ON THIS PC** (OBS, Game Bar, NVIDIA ShadowPlay, etc). Recording with a capture card, the translation shows anyway.

<div style="position:relative;padding-top:56.25%;max-width:820px;margin:0 auto">
  <iframe src="https://player.vimeo.com/video/1218094053"
          style="position:absolute;top:0;left:0;width:100%;height:100%;border:0"
          allow="fullscreen; picture-in-picture" allowfullscreen
          title="Translation covering the original subtitle"></iframe>
</div>

<p align="center"><i>The translation drawn over the original subtitle. The video was recorded with a phone because, in this mode, the subtitle is hidden from screen captures — a regular recording would not show the feature working.</i></p>

## More than one line on screen

With *Stick to the detected text* off, **Lines on screen** (1 to 8, default 1) sets how many lines stay visible at once. With more than one, each line sits on its own row, starting with a dash, in the middle of the monitor. A line too long for the width shrinks the font of the block instead of wrapping.

## Letting the AI "remember" previous lines

With an AI (OpenAI, Anthropic, Gemini, Groq or OpenAI-compatible), **Translation › AI** has the **Previous lines** control (5 to 10, default 5). The AI receives the last lines already translated as reference before translating the next one — this helps keep the same names, terms and tone throughout a conversation. Each extra line costs tokens on every translation.

> **DeepL** receives only the original text of those lines, as context, and does not charge for it. The other dedicated translators (Google Translate, Google Cloud and Azure) translate each line on its own.

## Separate appearance

Overlay › Subtitles has its own font, color, background and outline options — independent from screen capture — so you can keep the continuous subtitle smaller and more discreet and the screen capture translation larger, for example.

## Turning it off

Press **`Numpad0`** again, or the toggle subtitles button on the floating toolbar. The subtitle on screen is cleared immediately.

The mode also **turns itself off** after a while with no text in the area, so it does not keep running for nothing when you leave the cutscene and forget to turn it off. The time is chosen in *Overlay › Subtitles → Turn off subtitles with no text in the area*: Never, 1, 2, 5 or 10 minutes (default 1 minute). A subtitle standing still on screen counts as text. Note that this **turns the mode off**, it does not just hide the subtitle — to turn it back on, press `Numpad0`.

---
