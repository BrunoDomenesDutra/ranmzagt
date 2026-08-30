# 14. Complete reference — all tabs

This section describes **every tab and every option** in the settings window, in the order they appear in the left-hand menu. It's reference material — for day-to-day use, the earlier sections are enough.

The menu has five groups with sub-items (**General**, **Overlay**, **Translation**, **Tools**, **Debug**) and three standalone items below them (**History**, **Experimental**, **About**).

> The screenshots show the interface in Portuguese; the labels quoted in the text are the English ones you'll see with **Interface language** set to English.

## General › Config

Where the program runs.

<p align="center"><img src="media/geral-config.png" alt="General › Config tab" width="820"></p>

- **App language → Interface language** — switches the language of the settings window itself (Portuguese / English). It does not affect the OCR and translation languages. On first run it detects the Windows language (falling back to English if it isn't Portuguese).
- **Updates → Notify me about new versions** — turns on the notice that shows up when you open the program and a newer version has been published (see section 15). Turn it off here, or from the notice itself, and turn it back on with this toggle.
- **Updates → Check now** — checks right away whether a new version is out, even with the notice turned off. The answer appears next to the button: *"You are on the latest version"*, the version found (with a **Download** button that opens the page in your browser), or a warning that the check failed.
- **Configuration → Reset to default** — restores every option to factory values. It **keeps** the monitor, the selected areas, the API keys, the prompts (System Prompt and Game Info) and the update-notice preference.
- **Capture backend → Backend** — how the program reads screen pixels:
  - *Auto (recommended)* — decides on its own: WGC on Windows 11, DXGI on Windows 10, with no yellow border. Switches instantly, no restart.
  - *WGC (Windows 11)* — Windows Graphics Capture.
  - *DXGI (Windows 10)* — Desktop Duplication; it exists so Windows 10 doesn't draw the yellow border around the captured monitor.
- **Monitor → Active display** — which monitor the program captures, translates and displays on. *Automatic* uses the Windows primary monitor. Switching monitors **clears the saved capture area** and **requires a restart** (a "Restart now" button appears at the bottom of the tab).
- **Floating toolbar → Show floating toolbar** — turns on the always-visible button window (see step 2.7). It also opens and closes with the `NumpadSubtract` hotkey, and it **remembers the last position** you left it in.

## General › Profiles

One set of settings per game. The concept and the walkthrough are in [section 4](/en/Manual/profiles-one-set-of-settings-per-game.md); this is just the controls.

<p align="center"><img src="media/geral-perfis.png" alt="General › Profiles tab" width="820"></p>

- **New profile → Game name** — the name of the profile to be created.
  - **Duplicate current** — creates it from everything in effect right now, **selected areas included**.
  - **Start from scratch** — creates it with the factory values.
  - Either way the new profile **becomes active**, and from then on everything you change in the other tabs is saved into it by itself.
- **Your profiles** — the list, in a collapsible card: click the header to fold it away once it grows. The active profile is highlighted and marked *active*; click any other one to activate it right away.
  - **Rename** — changes the name. **Default** doesn't have this button: its name follows the interface language.
  - **Delete** — asks for confirmation (*Delete it*). **Default** cannot be deleted. If the deleted profile was the one in use, Default takes over immediately.
- **What changes when you switch profiles** — the summary of which options follow the profile and which apply to all of them (API keys, shortcuts, monitor, OCR tab, Inpaint and web server).

## General › Language

The source-language field **adapts to the OCR engine** picked in General › OCR.

<p align="center"><img src="media/geral-idioma.png" alt="General › Language tab" width="820"></p>

- **Source text language**
  - With *WinOCR* — the **Text language** field takes a BCP-47 tag (`en`, `ja`, `ko`, `zh-Hans`, `pt`…). If the language pack isn't installed in Windows, a warning appears with an **Install language pack** button that opens the Windows language screen directly.
  - With *OneOCR* — **automatic detection**; there's no source language to configure and the field doesn't show.
- **Target language** — what to translate into (`pt`, `es`, `fr`, `de`, `it`, `zh`…).

## General › OCR

Which engine recognizes the text, and how it groups lines.

<p align="center"><img src="media/geral-ocr.png" alt="General › OCR tab" width="820"></p>

- **OCR Engine → Active engine**
  - *WinOCR (default — native, ~30 ms)* — the engine built into Windows: fast, offline, no external dependency. Recognition depends on the language packs installed on the system. It's the fastest, but can trip on heavily stylized game fonts.
  - *OneOCR (Snipping Tool — experimental, ~50–150 ms)* — a multilingual model with automatic language detection. It **runs on Windows 10 and 11**; what's exclusive to Windows 11 are the files: `oneocr.dll`, `oneocr.onemodel` and `onnxruntime.dll` only ship with the Windows 11 Snipping Tool. You copy them from a Win11 machine and point to the folder (the card walks you through it, including the PowerShell command to find the Snipping Tool folder). It uses an unofficial Microsoft API — a Snipping Tool update can break the integration, in which case you just re-extract the files.
  - The engine's configuration card is **collapsible**: it stays open while the folder isn't configured, and you can fold it away afterwards.
- **Paragraph Mode Fine-Tuning → Grouping sensitivity** (0–3.0; default 1) — a multiplier over the typical vertical spacing between lines, used to decide whether two lines belong to the same paragraph. Lower values split paragraphs more readily; higher ones merge more distant lines into a single block.

> **The mode isn't chosen here.** Paragraph or line is decided **at capture time**, by which hotkey you press: `Numpad8` (paragraph) or `Numpad9` (line). This tab only fine-tunes how Paragraph mode groups.

## General › Shortcuts

<p align="center"><img src="media/geral-atalhos.png" alt="General › Shortcuts tab" width="820"></p>

Ten global shortcuts — they work with the game focused, and are disabled while the settings window is in the foreground. Each has the **Ctrl / Alt / Shift** modifiers plus a main key, picked from the **Numpad**, **Function** (F1–F12), **Navigation** (arrows, Insert, Delete, Home, End, PageUp, PageDown), **Numbers** and **Letters** groups.

| Action | Default |
|---|---|
| Select area | `Numpad7` |
| Translate (line mode) | `Numpad9` |
| Translate (paragraph mode) | `Numpad8` |
| Translate with AI Vision (paragraph mode) | `Numpad5` |
| Translate with AI Vision (line mode) | `Numpad6` |
| Clear overlay | `NumpadDecimal` |
| Toggle subtitles | `Numpad0` |
| Select subtitle area | `Numpad1` |
| Show/hide areas (preview) | `Numpad2` |
| Show/hide floating toolbar | `NumpadSubtract` |

> **Letters and numbers** as the main key **require** a modifier (Ctrl, Alt or Shift) so they don't clash with the game, which uses WASD and slots 0–9 constantly. Numpad, F-keys and navigation keys work without one. The Numbers and Navigation groups are what save you on a laptop with no numpad.

The program warns you if you assign the same combination to two shortcuts — one of them wouldn't be registered.

The **Real-time Mode** shortcuts aren't here: being experimental, they live in the Experimental tab and come with **no key assigned**.

## Overlay › Capture

Appearance of manual translations, and image preprocessing.

<p align="center"><img src="media/overlay-captura.png" alt="Overlay › Capture tab" width="820"></p>

- **Text**
  - *Font* — "System default (Arial)" or any font in the `fonts/` folder, with a preview beside it.
  - *Text color* — color picker (white by default).
  - *Font size* — 8 to 72 pt.
  - *Line height* — 0.80 to 2.00.
  - *Auto-fit* — gradually shrinks the font so the text fits the block without clipping.
- **Background and Outline** — mutually exclusive; turning one on turns the other off.
  - *Show background* + *Background opacity* (10–100%) — a dark box behind the text.
  - *Show outline* + *Thickness* (2–5 px) — a black outline around each letter.

<p align="center"><img src="media/overlay-captura-exibicao.png" alt="Overlay › Capture tab — Display and preprocessing" width="820"></p>

- **Display**
  - *Overlay duration* — Never clear automatically / 15 s / 30 s / **1 minute (default)** / 2 / 5 / 10 minutes.
  - *Hide the translation from recordings and streams* — the translation stays visible on your own
    screen but disappears from captures. Only works with programs running on this PC (OBS, Game Bar,
    NVIDIA ShadowPlay, etc); with a capture card it still shows up. Affects manual translation only.
- **OCR Preprocessing** — filters applied to the image before recognition:
  - *Enable preprocessing* turns the block on.
  - *Grayscale* · *Invert colors*
  - *Contrast* (1.0–3.0×) · *Upscale* (1.0–4.0×) · *Sharpen* (0–2.0×)
  - *Advanced* — only applied when enabled: *Threshold* (0–255), *Blur* (0–5.0×), *Dilation* (0–10 px), *Erosion* (0–10 px).

## Overlay › Subtitles

Subtitle Mode has its **own** appearance and preprocessing, independent of Overlay › Capture.

<p align="center"><img src="media/overlay-legenda.png" alt="Overlay › Subtitles tab" width="820"></p>

- **Translation position** — *Replace the original subtitle in place*: draws the translation over the
  captured area, covering the original subtitle, instead of showing it above the area. Shows one line
  at a time (see *Visible lines* below). In this mode the subtitle disappears from captures made on
  this PC — that's what keeps the OCR from re-reading its own translation. See section 9.
- **Text** — *Font*, *Text color* and *Font size* (10–48 pt). No line height and no auto-fit.
- **Background and Outline** — *Show background* + *opacity* (10–100%), or *Show outline* + *Outline thickness* (1–5 px).

<p align="center"><img src="media/overlay-legenda-captura.png" alt="Overlay › Subtitles tab — Capture and preprocessing" width="820"></p>

- **Capture**
  - *Interval* — how often the area is re-read (25 ms to 5 s).
  - *Visible lines* — how many subtitle lines to keep on screen (1 to 8). **Locked at 1** when
    *Replace the original subtitle in place* is on; the value you picked is kept for when the option
    is turned off.
  - *Clear after silence* — wipes the subtitle if no new text shows up for X seconds (1 to 5 s).
  - *Turn off Subtitle Mode after inactivity* — **turns the mode off**, not just hides it, after that long without detecting text in the region: Never / 1 / 2 / 3 / 5 / 10 minutes.
- **OCR Preprocessing** — the same controls as Overlay › Capture, but independent of it.

## Overlay › Web

Streams translations to browsers on the local network — and to OBS.

<p align="center"><img src="media/overlay-web.png" alt="Overlay › Web tab" width="820"></p>

- **Web Server**
  - *Server active* — starts a local HTTP server, reachable from any device on the same network.
  - *Show translation on screen* — keeps the overlay even with the server running; turn it off to send **only** to the browser/OBS.
  - *Port* (1024–65535) — also shows how many clients are connected.
- **Addresses** — `/captura` (with history and a Clear button) and `/captura/obs` (transparent background, for use as a Browser Source in OBS), each with a **Copy** button.
- **Appearance** — *Theme* · *Font size* (12–48 px) · *Bold* · *Detected text* (shows the original below the translation) · *Time and service* · *Custom colors*, which unlocks six pickers: translated text, original text, time, service (badge), card background and card border.
- **History → Entries kept in the buffer** (10–200).

## Translation › Translators

Which service translates, and with which credentials.

<p align="center"><img src="media/tradutores-deepl.png" alt="Translation › Translators tab with DeepL" width="820"></p>

- **Translation Provider → Active provider**
  - *Google Translate — free, no key* — unofficial API, nothing to configure. **Doesn't support Vision Mode.** Being free, it has a **request limit**: on captures with many blocks or in continuous use, a *"Rate limit reached"* warning may appear — what to do about it is in [section 13](/en/Manual/common-problems-and-solutions.md).
  - *DeepL (requires API key)* — a high-quality dedicated translator; **doesn't support Vision Mode**. It has no model selection, but it does have **Formality** (Default / More formal / More informal), which only affects target languages that support it — PT-BR included — and is ignored on the rest. It makes use of the **Game Info** field (Translation › AI) and, in Subtitle Mode, the previous lines as context, at no extra cost.
  - *Azure Translator (requires API key and region)* — Microsoft's translator; **doesn't support Vision Mode**. It has no model selection and no formality, and it **doesn't use** Conversation Context or Game Info — its translation API takes no context. In exchange, it detects the source language **block by block**: in a capture where part of the text is in another language, each block is translated from the right one.
  - *OpenAI*, *Anthropic (Claude)*, *Gemini* — AI engines, requiring an API key.
- **Authentication** — shown for providers with a key. Credentials are **saved per engine**, so switching services and back erases nothing.
  - *Model* (AI engines) — each engine offers three tiers: fast/cheap, best balance, and top quality.
    - OpenAI: GPT-4.1 nano · GPT-4.1 mini · GPT-4.1
    - Claude: Haiku 4.5 · Sonnet 5 · Opus 5
    - Gemini: 3.5 Flash-Lite · 3.6 Flash · 3.7 Flash
    - *Custom…* — the last option in the list: opens a free-text field where you type **any model ID** the provider accepts, so you can use a newer model without waiting for a program update.
    - *See the provider's full model list* — opens the selected engine's official page in your browser, with every model and its exact ID. Useful in two situations: when a model newer than the built-in list comes out, and when you have an older key that still reaches models the provider has closed off to new accounts — that's the case with the Gemini 2.0 and 2.5 families, which answer for older keys but return an error on freshly created ones. Either way, copy the ID from there into the *Custom…* field.
  - *Resource region* (Azure only) — **required**, and it sits where DeepL shows Formality. It accepts the portal spelling ("Brazil South"): capitals and spaces are normalized for you. The *See Azure's official region list* link opens Microsoft's table in your browser. Key and region come from the same page: <https://portal.azure.com> → your Translator resource → *Keys and Endpoint*.
  - *Test connection* — makes a test call with the current key and model and tells you right away whether everything is fine or which error came back, instead of you finding out mid-game. It also exists for Google, to check connectivity. On Azure it only unlocks once the region is filled in, because without it the error that comes back is indistinguishable from an invalid key.
- **API Keys** — a collapsible card where the selected engine's credential goes (`sk-…`, `sk-ant-…`, `AIza…`, or the free-plan DeepL `:fx` key). It **opens by itself** while no key is filled in.
  - *+ Add key* / *✕* — you can register **as many keys as you like** for the same engine. When the key in use runs out of credit or hits the request limit, the next one in the list takes over automatically; once all are exhausted, it falls back to Google Translate.
- **DeepL usage** — only with DeepL selected: calls and characters translated this session, plus the **account quota** (*Refresh* button); *Reset session* restarts the count. It's the only engine with this tracking — the AI ones don't expose spend through the key, and Azure has no equivalent quota endpoint.

<p align="center"><img src="media/tradutores-claude.png" alt="Translators with Anthropic (Claude) selected" width="820"></p>

<p align="center"><img src="media/tradutores-azure.png" alt="Translators with Azure Translator selected, showing the Resource region field" width="820"></p>

## Translation › AI

Model parameters and prompts.

<p align="center"><img src="media/ia.png" alt="Translation › AI tab" width="820"></p>

- **Model Parameters**
  - *Temperature* (0–2) — 0.0 literal · 0.3 recommended · 1.0+ creative.
  - *Max tokens* (256–4096) — response size; 1024 is plenty for translation.
- **Conversation Context → Previous lines** (0–20) — in Subtitle Mode, sends the last lines (original + translation) as context, so the AI keeps terminology and tone consistent. 0 disables it; 3–5 recommended.
- **System Prompt** — translator role and general rules, with **Save** and **Restore default** buttons (the latter recovers the factory text for this field only).
- **Game Info** — theme, characters and glossary; change it per game. Same buttons.

> With a non-AI engine active, the cards that don't apply are flagged in red ("Only applies to AI engines…" and "The current translation engine doesn't use this."). **Conversation Context** and **Game Info** also apply to **DeepL**; **Google Translate** and **Azure Translator** ignore both.

<p align="center"><img src="media/ia-avisos.png" alt="AI tab with Google Translate active, showing the red warnings" width="820"></p>

The global reset (General › Config) does **not** wipe the System Prompt or the Game Info.

## Tools › Inpaint

AI-reconstructed background (MI-GAN) — under development.

<p align="center"><img src="media/ferramentas-inpaint.png" alt="Tools › Inpaint tab" width="820"></p>

Instead of a black box behind the translation, it erases the original text from the capture and reconstructs the background with an inpainting model running inside the program — the translation ends up looking native to the game. It applies to **manual translations** (Translate and Vision); Subtitle Mode doesn't use it. It costs ~50–200 ms per translation and ~200 MB of RAM while active.

<div style="position:relative;padding-top:56.25%;max-width:820px;margin:0 auto">
  <iframe src="https://player.vimeo.com/video/1217778049"
          style="position:absolute;top:0;left:0;width:100%;height:100%;border:0"
          allow="fullscreen; picture-in-picture" allowfullscreen
          title="AI-reconstructed background"></iframe>
</div>

<p align="center"><i>The reconstructed background in place of the black box behind the translation.</i></p>

- **Enable reconstructed background** — only takes effect with the files configured below.
- **Mask fine-tuning**
  - *Mask dilation* (0–12 px; default 3) — if an edge residue remains after erasing the text (the font halo), raise it so MI-GAN reconstructs a bit beyond the letters.
  - *Detection threshold* (1.05–1.60; default 1.30) — a lower threshold makes the mask more sensitive (catches more halo, but may mistake textured background for text).
  - Both apply **per capture**, with no restart.
### Download automatically

The feature needs two files that don't ship inside the program's `.zip`: the MI-GAN model (27 MB) and `onnxruntime.dll` (72 MB). The **Download automatically** card fetches both for you.

Click **Download** on each one. The bar shows progress and the button turns into **Cancel** — cancelling doesn't throw away what already came down: resuming picks up where it stopped.

<p align="center"><img src="media/ferramentas-inpaint-baixando.png" alt="MI-GAN download in progress" width="820"></p>

Once finished, both read **Ready, files verified** with a green check, and **the folder is configured on its own** — you don't have to copy any path.

<p align="center"><img src="media/ferramentas-inpaint-pronto.png" alt="Both files downloaded and verified" width="820"></p>

The program checks each file's **sha256** before accepting it. A file that arrives corrupted or different from what was expected is deleted and the download fails with a message — a half-written file never gets to pass for a good one. Both land in `models\inpaint`, next to the executable.

#### Alternate address

If the default download doesn't work on your network (some corporate networks and some ISPs block HuggingFace and GitHub), open **Alternate address** and paste another link.

<p align="center"><img src="media/ferramentas-inpaint-endereco.png" alt="Alternate address field open" width="820"></p>

Hash verification **still applies** to the alternate address. It changes where the file comes from, never which file is accepted: a link that serves something else is rejected.

### Manual installation

If you'd rather do it by hand — or if the gaming machine has no internet — open **Manual installation**. It has the links for both files and the folder field, with **Browse** and **Verify**.

<p align="center"><img src="media/ferramentas-inpaint-manual.png" alt="Manual installation block open" width="820"></p>

Download `migan_pipeline_v2.onnx` and `onnxruntime.dll` (from inside `onnxruntime-win-x64-1.26.0.zip`), put both in the same folder and point here. Once it finds both, the folder is configured right away.

> Moving the `onnxruntime.dll` to another folder requires restarting the program.

> Tip: turn on **Outline** in Overlay › Capture, because the reconstructed background can come out too light for white text.

## Tools › Lab

A lab for testing preprocessing without touching the game.

<p align="center"><img src="media/ferramentas-lab-preprocessamento.png" alt="Tools › Lab tab" width="820"></p>

- **Test Image** — pick a PNG/JPG from the `images/lab_images/` folder, next to the executable.
- **Preprocessing Parameters** — the same controls as Overlay › Capture, with a **live preview**: the original and processed images appear below, side by side.
- **Apply to Capture** / **Apply to Subtitles** — copy the setup you just tested into the matching tab.

Turning on *Advanced* reveals Threshold, Blur, Dilation and Erosion, for the hard cases:

<p align="center"><img src="media/ferramentas-lab-avancado.png" alt="Lab with the advanced filters enabled" width="820"></p>

## Debug › Monitor

Latency of each pipeline stage.

<p align="center"><img src="media/debug-monitor.png" alt="Debug › Monitor tab" width="820"></p>

- **Monitoring → Active** — records the timing of each stage on every translation. The history survives navigating between tabs.
- **Run History** — a table of the last 10 captures: Time, Capture, Preproc, OCR, Translation, Total, Blocks, Cache (hits that skipped the API) and API (calls made).
- **Statistics** — min, average and max for each stage.

## Debug › Image

Diagnostic images.

<p align="center"><img src="media/debug-imagem.png" alt="Debug › Image tab" width="820"></p>

- **Debug Mode → Enabled** — saves diagnostic images on every capture.
- **Images to save** — Original capture before preprocessing (`frame.png`), Capture after preprocessing (`frame_proc.png`), OCR lines (`ocr_lines.png`), Grouped paragraphs (`ocr_paragraphs.png`) and the inpainting mask preview (`mask.png`).
- **Output folder** — the path (default `images\ocr_debug_images`) and a button to open the folder.

## Debug › Logs

The current session's log, in real time.

<p align="center"><img src="media/debug-logs.png" alt="Debug › Logs tab" width="820"></p>

- **Log captured text and translations** — a privacy switch, **off by default**. Leave it off when sending a log to support, so you don't expose the game's content.
- **Filter lines** · **Auto-scroll** · **Refresh** — view controls; errors come out in red, warnings in yellow.

## History

<p align="center"><img src="media/historico.png" alt="History tab" width="820"></p>

Lists the **current session's** translations — time, service, translation and, below it, the original text — most recent first, up to the limit set in Overlay › Web. Click an entry to copy the translation. **Clear history** button.

## Experimental

> Everything in this tab is **under development**: behavior can change, bugs are expected, and features can be removed.

<p align="center"><img src="media/experimental.png" alt="Experimental tab" width="820"></p>

Two collapsible cards.

**Real-time Mode (live overlay)** — continuous translation drawn in place of the original text, over its own area.

<p align="center"><img src="media/experimental-tempo-real.png" alt="Real-time Mode card" width="820"></p>

- *Allow Real-time Mode* — unlocks the hotkey below, which is what actually starts and stops the capture. With this off, the hotkey does nothing.
- Both shortcuts — *Toggle Real-time* and *Select Real-time area* — live here and come with **no key assigned**; pick your own.
- *Interval* (25 ms–2 s) · *Font size* (10–48 pt) · *Show background* + *opacity* (10–100%) · *Show outline* · *Clear after silence* (0–10 s).
- *Position stability* (0–60 px) and *Hold on OCR failure* (0–30 ticks) — against shaking and flicker when the background is animated.
- It also has its own dedicated image preprocessing. See **section 10**.

> The Real-time overlay is always hidden from screen capture (OBS included) — see section 10.

**Wait for complete text (typewriter effect)** — only translates once the line has finished appearing, so you don't translate sentences still "being typed" on screen. Applies to Subtitle Mode and Real-time Mode.

<p align="center"><img src="media/experimental-typewriter.png" alt="Typewriter effect card" width="820"></p>

- *Required stable captures* (2–8 frames) — how many consecutive reads must match.
- *'Same text' threshold* (80–99%) — how alike two reads must be to count as identical.
- *Wait cap* (0–4 s) — the longest it will wait before translating whatever it has.

## About

Program information: icon, name and installed **version**, the feature list, the author, and the full **License** — what's allowed (free personal use, distributing unmodified copies, creating content such as videos and streams) and what's prohibited (modifying or reverse-engineering, selling, redistributing modified versions, commercial use without authorization, removing credits), plus the warranty disclaimer.

---
