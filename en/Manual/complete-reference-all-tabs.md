# 13. Complete reference — all tabs

This section describes **every tab and every option** of the settings window, in the order they appear in the left menu. It is reference material — for day-to-day use, the previous sections are enough.

The menu has five groups with sub-items (**General**, **Overlay**, **Translation**, **Tools**, **Debug**) and two standalone items at the bottom (**History** and **About**).

## General › Config

<p align="center"><img src="media/geral-config.png" alt="General › Config tab" width="820"></p>

- **Program language → Interface language** — switches the language of the settings window itself (Portuguese / English) and of the alerts. It does not affect the OCR and translation languages. On first run it follows the Windows language (falls back to English if it is not Portuguese).
- **Appearance** — colors of this screen and of the floating toolbar:
  - *Theme* — Dark or Light.
  - *Colorblind* — accessible color palette for color blindness.
  - *Grayscale* — for achromatopsia.
- **Updates → Notify me about new versions** — turns on the warning shown when opening the program when a newer version is published (see section 14).
- **Updates → Check now** — checks right away whether there is a new version, even with the warning off.

<p align="center"><img src="media/geral-config-monitor.png" alt="General › Config tab — reset, backend, monitor and alerts" width="820"></p>

<p align="center"><i>Scrolling the same tab: <b>Configuration</b>, <b>Capture backend</b>, <b>Monitor</b> and <b>On-screen alerts</b>.</i></p>

- **Configuration → Reset to default** — restores every option to factory values. It **keeps** the language and theme of the screen, the monitor, the selected areas, the API keys, the Game Info and the update warning preference.
- **Capture backend → Backend** — how the program reads the screen pixels:
  - *Auto (recommended)* — picks by itself: WGC on Windows 11, DXGI on Windows 10, without the yellow border. The switch applies right away, no restart.
  - *WGC (Windows 11)* — Windows Graphics Capture.
  - *DXGI (Windows 10)* — Desktop Duplication; it exists so Windows 10 does not draw the yellow border around the captured monitor.
- **Monitor → Active display** — which monitor area selection, alerts, the area preview and the floating toolbar open on. *Automatic* uses the Windows primary monitor. It applies right away, no restart; each monitor keeps its own areas, and each profile keeps its own monitor.
- **On-screen alerts → Show alerts** — short warnings in the bottom-right corner, only in serious situations (usage limit, key, no internet, OCR or capture that failed, shortcut pressed with this screen in focus) and when turning subtitles on and off.

## General › Profiles

A set of settings per game. The concept and the step by step are in [section 4](/en/Manual/profiles-one-set-of-settings-per-game.md); here are only the controls.

<p align="center"><img src="media/geral-perfis.png" alt="General › Profiles tab" width="820"></p>

- **New profile → Game name** — the name of the profile to be created.
  - **Duplicate current** — creates it from everything in effect right now, **including the selected areas**.
  - **Start from scratch** — creates it with factory values, on the current monitor, and opens the Setup guide.
  - In both cases the new profile **becomes active right away**, and from then on everything you change in the other tabs is saved in it by itself.
- **Your profiles** — the list, in a collapsible card. The active profile is highlighted and marked as *active*; click any other to activate it right away.
  - **Rename** — changes the name. **Default** does not have this button.
  - **Delete** — asks for confirmation (*Delete it*). **Default** cannot be deleted. If the deleted profile was the one in use, Default takes over right away.
- **What changes when you switch profiles** — the summary of which options follow the profile and which apply to all.

## General › Language

The source language field **adapts to the OCR engine** chosen in General › OCR.

<p align="center"><img src="media/geral-idioma.png" alt="General › Language tab" width="820"></p>

- **Source text language**
  - With *WinOCR* — list of the languages with a text recognition pack installed in Windows, with no default option: pick the game language. With no choice, a warning shows up. If the saved language is no longer installed, the **Install language pack** button shows up and opens the Windows language screen.
  - With *OneOCR* — **automatic detection**; there is no source language to set.
- **Target language** — which language to translate into: Português (Brasil), Português (Portugal), Español, English, Français, Deutsch, Italiano, 日本語, 한국어, 中文（简体）and Русский.

## General › OCR

Which engine recognizes the text on screen.

<p align="center"><img src="media/geral-ocr.png" alt="General › OCR tab" width="820"></p>

- **OCR Engine → Active engine**
  - *WinOCR (native to Windows)* — the default. Built into Windows, nothing to install. It reads the language chosen in General › Language; it gets lost with busy backgrounds and very stylized fonts.
  - *OneOCR (Windows 11 Snipping Tool — recommended)* — multilingual model with automatic language detection, far better than WinOCR with game fonts (the why is in [section 6](/en/Manual/configuring-translation.md), in *Switching OCR engine*). **It runs on Windows 10 and 11**; what is exclusive to Windows 11 are the files `oneocr.dll`, `oneocr.onemodel` and `onnxruntime.dll`. It uses an unofficial Microsoft API — a Snipping Tool update can break the integration.
- **OneOCR** (shows up with OneOCR selected)
  - *Status* — shows the folder OneOCR loaded from, or *"Did not load"* when the files are missing.
  - *Files folder* — empty, it uses the folder where **Detect and copy** puts the files. **Browse...** picks another folder and checks that the 3 files are in it.
  - *Detect and copy* — finds the installed Snipping Tool, copies the 3 files and sets the folder. It warns when the app is not installed or when it is a version without the files (the Windows 10 case). **It is the only way the program copies the files**: it never goes after them by itself.
  - *Windows 10: copy from a Windows 11 PC* — collapsible block with the step by step for copying by hand.

## General › Shortcuts

<p align="center"><img src="media/geral-atalhos.png" alt="General › Shortcuts tab — floating toolbar and global shortcuts" width="820"></p>

- **Floating toolbar → Show floating toolbar** — turns on the always-visible button window (see step 2.8). It also opens and closes with the `NumpadSubtract` shortcut, and it **remembers the last position** and size you left it at.

Eleven global shortcuts — they work with the game in focus and are paused while the settings window is in the foreground. Each has the **Ctrl / Alt / Shift** modifiers and a main key, chosen among the **Numpad**, **Function** (F1–F12), **Navigation** (arrows, Insert, Delete, Home, End, PageUp, PageDown), **Digits** and **Letters** groups.

| Action | Default |
|---|---|
| Select area | `Numpad7` |
| Translate (line mode) | `Numpad9` |
| Translate (paragraph mode) | `Numpad8` |
| Translate with AI Vision (paragraph mode) | `Numpad5` |
| Translate with AI Vision (line mode) | `Numpad6` |
| Retranslate (no cache) | `Numpad4` |
| Clear overlay | `NumpadDecimal` |
| Toggle subtitles | `Numpad0` |
| Select subtitle area | `Numpad1` |
| Show/hide the selected areas | `Numpad2` |
| Show/hide floating toolbar | `NumpadSubtract` |

> **Letters and digits** as the main key **require** a modifier (Ctrl, Alt or Shift) so they do not conflict with the game, which uses WASD and slots 0–9 all the time. Numpad, F-keys and navigation keys work without a modifier. The Digits and Navigation groups help people on laptops without a numpad.

The program warns you if you repeat the same combination in two shortcuts — one of them would not be registered. A key change applies right away, no restart.

## Overlay › Capture

How the screen capture translation looks.

<p align="center"><img src="media/overlay-captura.png" alt="Overlay › Capture tab" width="820"></p>

- **Display**
  - *Overlay duration* — **1 minute (default)**, 2, 5, 10 minutes or *Never* (stays until the clear shortcut or the next capture).
  - *Hide the translation from recordings and streams* — the translation stays visible on your screen, but disappears from captures. It only works with programs running on this PC (OBS, Game Bar, NVIDIA ShadowPlay, etc); recording with a capture card, it shows anyway.
- **Text**
  - *Font* — "System default (Arial)", the fonts in the `fonts/` folder or the Windows fonts, with a preview just below.
  - *Text color* — color picker (white by default).
  - *Font size* — 8 to 100 px.
  - *Line height* — 1.00 to 2.00 times the font size.
  - *Auto-fit* — shrinks the font until the text fits where the original was.
- **Background and Outline** — can be on together or separately.
  - *Show background* + *Background opacity* (10–100%) — dark box behind the text.
  - *Show outline* + *Thickness* (0.5–5 px) + *Outline color* — outline around each letter.
- **Paragraph Mode Fine-Tuning → Grouping sensitivity** (0.5–3.0) — lower values separate paragraphs more easily; higher values join more distant lines into one block. The mode itself (paragraph or line) **is not chosen here**: it is decided at capture time, by the shortcut — `Numpad8` (paragraph) or `Numpad9` (line).

## Overlay › Subtitles

Subtitle Mode has its **own** appearance, independent from Overlay › Capture.

<p align="center"><img src="media/overlay-legenda.png" alt="Overlay › Subtitles tab" width="820"></p>

- **Translation position → Stick to the detected text** — draws the translation on top of the original line, with the same line breaks, instead of above the area. It shows one line at a time, and a larger font spills over the area. In this mode the subtitle disappears from captures made on this PC — that is what stops the OCR from reading its own translation. See section 9.
- **Text** — *Font*, *Text color* and *Font size* (10–48 px).
- **Background and Outline** — *Show background* + *Opacity* (10–100%) and *Show outline* + *Outline thickness* (0.5–5 px) + *Outline color*.

<p align="center"><img src="media/overlay-legenda-captura.png" alt="Overlay › Subtitles tab — Capture and alphabet" width="820"></p>

- **Capture**
  - *Ignore text away from the center of the area* — on by default. Skips signs near the edges of the area; turn it off for left-aligned dialogue.
  - *Lines on screen* — how many lines stay visible (1 to 8). It stays at 1 with *Stick to the detected text* on.
  - *Translation stays after the subtitle goes away* — 1 to 3 s (default 2 s).
  - *Turn off subtitles with no text in the area* — **turns the mode off** after that long with no text: Never / 1 / 2 / 5 / 10 minutes (default 1 minute).
- **Original subtitle alphabet** — only characters of that alphabet are considered in the subtitle; the rest is ignored. With OneOCR, choose *Any alphabet*, Latin, Japanese/Chinese, Korean or Cyrillic. With WinOCR, it follows the language in General › Language, with the **Change language** button.

## Overlay › Web

Streams screen capture translations to browsers on the local network — and to OBS.

<p align="center"><img src="media/overlay-web.png" alt="Overlay › Web tab" width="820"></p>

- **Web Server**
  - *Server active* — starts a local HTTP server, reachable from any device on the same network.
  - *Show translation on screen* — keeps the overlay even with the server on; turn it off to send **only** to the browser/OBS.
  - *Port* — 7474 by default. It also shows how many clients are connected.
- **Addresses** — `/captura` (with history and a Clear button) and `/captura/obs` (transparent background, to use as a Browser Source in OBS), each with a **Copy** button.

<p align="center"><img src="media/overlay-web-aparencia.png" alt="Overlay › Web tab — page appearance and history" width="820"></p>

<p align="center"><i>Scrolling the same tab: the web page <b>Appearance</b> and the <b>History</b> buffer.</i></p>

- **Appearance** — *Theme* (Dark, Light or Dracula) · *Font size* · *Bold* · *Detected text* (shows the original below the translation) · *Time and service* · *Custom colors*, which unlocks the page color pickers.
- **History → Entries kept in the buffer** — how many translations the page keeps for whoever opens it later.

## Translation › Translators

Which service translates and with which keys.

<p align="center"><img src="media/tradutores-google-cloud.png" alt="Translation › Translators tab with Google Cloud Translation" width="820"></p>

- **Translation Provider → Active provider**
  - *Google Translate — free* — unofficial API, nothing to set up. It is the same address the Google Translate web page uses internally; since it is not published or documented, Google can change or disable it at any time. **Does not support Vision Mode.** Being free, it has a **request limit**, counted per IP address — what to do is in [section 12](/en/Manual/common-problems-and-solutions.md).
  - *Google Cloud Translation* — Google's official API, with a key created in the Google Cloud Console (*APIs & Services › Credentials*). **Does not support Vision Mode.**
  - *DeepL* — dedicated translator. The free plan key ends in `:fx`, and the program picks the right server by itself. It receives the Game Info and the previous lines as context, at no cost. **Does not support Vision Mode.**
    - *Formality* — shows up below the provider, only with DeepL: *Default*, *More formal* or *More informal*. It changes how people are addressed (tu/vous, du/Sie). It is ignored in languages where DeepL has no formality. It is saved in the profile.
  - *Azure Translator* — Microsoft's translator; requires a key and the resource **region**. **Does not support Vision Mode.**
  - *OpenAI*, *Anthropic (Claude)*, *Gemini* — AIs, with an API key and Vision Mode.
  - *Groq* — AI with a free plan, with an API key. **Does not support Vision Mode.**
- **Authentication** — shows up for the AIs and for Azure.
  - *Model* (AIs) — each one has a short list. The first one is the default.
    - OpenAI: GPT-5.4 mini (fastest, recommended) · GPT-4.1 mini · GPT-4.1
    - Anthropic: Haiku 4.5 · Sonnet 5 · Opus 5
    - Gemini: 3.5 Flash-Lite · 3.6 Flash · 3.7 Flash
    - Groq: gpt-oss-20b · gpt-oss-120b
    - *Custom…* — last option in the list: opens a free field where you type **any model ID** the service accepts, to use a newer model without waiting for a program update.
    - *See the provider's full model list* — opens the service's official page in the browser, with every model and the exact IDs, to copy into *Custom…*.
  - *OpenAI fast queue* — shows up below the model, only with OpenAI. **It comes off.** When on, OpenAI serves you first, at twice the price per token.
  - *Resource region* (Azure only) — **required**. It accepts the portal spelling ("Brazil South"): capitals and spaces are fixed by themselves. The *See Azure's official region list* link opens Microsoft's table in the browser. Key and region come from the same page: <https://portal.azure.com> → your Translator resource → *Keys and Endpoint*.
- **API Keys** — collapsible card where the key of the selected service goes. It **opens by itself** while no key is filled in. Keys are stored encrypted and only open on this PC, in your Windows account.
  - *+ Add key* / *Delete* — you can register **as many keys as you want** for the same service. When the key in use is rejected, runs out of credit or hits the request limit, the next one in the list takes over right away; when all are used up, it falls back to Google Translate.
  - *Test* — translates one word using only that key, with the chosen model and region. The button turns **green** when the key works and **red** when it fails. Hover over it to see why, such as "invalid key", "out of credit" or "No internet". Editing the key clears the result.
  - *Test all* — tests the keys in the list one at a time and colors each one's button.
  - With **DeepL**, a working key shows below it how much of the monthly quota has been used (*"Monthly quota: 4,359 of 500,000 characters"*).

<p align="center"><img src="media/tradutores-deepl.png" alt="Translators with DeepL: formality and monthly quota below the tested key" width="820"></p>

<p align="center"><img src="media/tradutores-testar-chave.png" alt="Test buttons: working key in green and failing key in red" width="820"></p>

<p align="center"><img src="media/tradutores-openai.png" alt="Translators with OpenAI selected" width="820"></p>

## Translation › AI

Context sent to the AIs.

<p align="center"><img src="media/ia.png" alt="Translation › AI tab" width="820"></p>

- **Conversation Context → Previous lines** (5–10, default 5) — in Subtitle Mode, sends the last lines (original + translation) as context, so the AI keeps terms and tone consistent. Each extra line costs tokens on every translation. With DeepL, only the originals go, at no cost.
- **System Prompt** — general translator rules, for every game. It comes **blank**, with a gray example inside the field; nothing is sent to the AI until you write your own. **Save** and **Restore default** buttons (which empties the field again). The target language does not need to be here: the program already sends the AI the language chosen in the **Language** tab, and asking for another language in this field is ignored. Concrete rules (glossary, keep names, do not soften swearing) work on every model.
- **Game Info** — theme, characters and glossary; change it for each game. It also comes blank, with a gray example. Same buttons. With DeepL, the text goes as context: it helps with tone and terms, but requests written here are not followed.

> With Google Translate, Google Cloud or Azure active, the cards are marked in red, because they do not apply to them. With DeepL, only the System Prompt is marked.

The general reset (General › Config) does **not** erase the Game Info.

## Tools › Inpaint

AI background reconstruction (MI-GAN).

<p align="center"><img src="media/ferramentas-inpaint.png" alt="Tools › Inpaint tab" width="820"></p>

Instead of the dark box behind the translation, it erases the original text from the screen capture and rebuilds the background with an inpainting model running inside the program — the translation looks native to the game. It applies to **screen capture** (Translate and Vision); Subtitle Mode does not use it.

<div style="position:relative;padding-top:56.25%;max-width:820px;margin:0 auto">
  <iframe src="https://player.vimeo.com/video/1217778049"
          style="position:absolute;top:0;left:0;width:100%;height:100%;border:0"
          allow="fullscreen; picture-in-picture" allowfullscreen
          title="AI-reconstructed background"></iframe>
</div>

<p align="center"><i>The reconstructed background instead of the dark box behind the translation.</i></p>

- **Enable reconstructed background** — can only be turned on after downloading the model, in the card below.
- **Mask fine-tuning** — applies **per capture**, no restart.
  - *Mask dilation* (0–12 px; default 3) — if a border residue (the font halo) is left after erasing the text, raise it so MI-GAN rebuilds a bit beyond the letters.
  - *Detection threshold* (1.05–1.50; default 1.30) — a lower threshold makes the mask more sensitive (catches more halo, but may mistake textured background for text).
  - *Outline* (0–16 px; default 8) — how far the letter outline is erased. Raise it if a dark stain is left with thick-outlined text; 0 erases only the letter, good for text without an outline.
  - *Background* (0–150%; default 25%) — grain given back to the generated background, so it does not look flat next to the scenery. Lower it if the background gets too grainy.

### Automatic download

<p align="center"><img src="media/ferramentas-inpaint-baixar.png" alt="Automatic download card, in Tools › Inpaint" width="820"></p>

The feature needs the MI-GAN model (27 MB), which does not come in the program `.zip`. The **Download automatically** card downloads and checks the model:

- *Model folder* — empty, it uses the `models\inpaint` folder, next to the executable. **Browse...** picks another one.
- *Download* — the bar shows the progress and the button turns into **Cancel**. Canceled or interrupted, the download starts over next time.

The program checks the file's **sha256** before accepting it. A file that arrives corrupted or different from the expected one is deleted and the download fails with a warning — a half file never passes as a good one.

> Tip: turn on the **Outline** in the Overlay › Capture tab, because the reconstructed background may be too light for white text.

## Debug › Monitor

Time of each screen capture step.

<p align="center"><img src="media/debug-monitor.png" alt="Debug › Monitor tab" width="820"></p>

- **Monitoring → Active** — records the time of each step on every screen capture key press. The history is kept when navigating between tabs.
- **Run History** — table of the last 10 captures: Time, Capture, OCR, Translation, Total, Blocks, Cache (hits without calling the API) and API (calls actually made).
- **Statistics** — minimum, average and maximum of each step.

## Debug › Logs

Log of this run, in real time.

<p align="center"><img src="media/debug-logs.png" alt="Debug › Logs tab" width="820"></p>

- **Log captured text and translations** — privacy switch, **off by default**. Keep it off when sending a log to support, so you do not expose the game content. API keys never go to the log.
- **Filter lines** · **Auto-scroll** · **Refresh** — viewing controls; errors come out in red, warnings in yellow.

Each run writes a file in `logs\`, next to the executable, and the program keeps the 20 most recent. That is the file support will ask for.

## History

<p align="center"><img src="media/historico.png" alt="History tab" width="820"></p>

Lists the screen capture translations of the **current session** — time, service, translation and, below, the original text. Click an entry to copy the translation. **Clear history** button.

## About

Program information: icon, name and installed **version**, the author, the project and support links, and the full **Terms of Use** — what is allowed (free personal use, distributing unmodified copies, creating content like videos and streams) and what is forbidden (modifying or reverse engineering, selling, redistributing modified versions, commercial use without permission, removing credits), plus the warranty disclaimer.

---
