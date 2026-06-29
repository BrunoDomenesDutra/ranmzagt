## 13. Complete reference — all tabs

This section describes **every tab and every option** in the settings window, in the order they appear in the sidebar. Use as reference — for day-to-day use, the previous sections are enough.

### General

Where the program operates.

- **Capture Backend** — how the program reads screen pixels:
  - *Auto (recommended)* — chooses itself: WGC on Windows 11, DXGI on Windows 10.
  - *WGC (Windows 11)* — Windows Graphics Capture; captures without yellow border on Win11.
  - *DXGI (Windows 10)* — Desktop Duplication; exists so Windows 10 doesn't draw a yellow/golden border around the captured monitor. The change applies immediately, no restart needed.
- **Monitor → Active screen** — which monitor the program captures, translates and displays on. *Automatic* uses Windows' primary monitor. Switching monitors **clears the saved capture area** and **requires a restart** ("Restart now" button appears below).
- **Floating toolbar → Show floating toolbar** — enables the always-visible button window, draggable between monitors (see section 3). Can also be opened/closed via the **Show/hide floating toolbar** hotkey (default `NumpadSubtract`), and it **remembers the last position** you left it at.
- **Configuration → Reset to defaults** — restores all options to factory values. **Keeps** the monitor, selected areas, API keys, and prompts (System Prompt and Game Information).
- **Interface language** — changes the language of the settings window itself (Portuguese/English). Auto-detects Windows language on first run (defaults to English if not Portuguese); can be manually changed anytime here.

### Language

The source language field **adapts to the OCR engine** selected in the OCR tab.

- **Original text language**:
  - *WinOCR* — a BCP-47 tag (ex.: `en`, `ja`, `ko`, `zh-Hans`, `pt`). If the language package isn't installed in Windows, a red warning appears with an **Install language package** button (opens Windows language settings directly).
  - *OneOCR* — **automatic detection**; no source language to configure.
- **Target language** — which language to translate to (ex.: `en`, `es`, `fr`, `de`, `it`, `zh`).

### Capture

Appearance of manual translation and image preprocessing.

- **Text**
  - *Font* — "System default (Segoe UI)" or any font from the `fonts/` folder.
  - *Font size* — 8 to 72 pt.
  - *Line height* — 0.80 to 2.00 (spacing between lines).
  - *Auto-fit* — progressively shrinks the font so text fits the block without cutting off.
- **Background and Outline** (they're alternatives — enabling one disables the other)
  - *Show background* + *Background opacity* (10–100%) — dark box behind text.
  - *Show outline* + *Thickness* (2–5 px) — black outline around each letter.
- **Display → Overlay duration** — Never clear / 15 s / 30 s / **1 minute (default)** / 2 / 5 / 10 minutes.
- **OCR Preprocessing** — filters applied to the image before recognition:
  - *Enable preprocessing* (unlocks the section)
  - *Grayscale* · *Invert colors*
  - *Contrast* (1.0–3.0×) · *Upscale* (1.0–4.0×) · *Sharpen* (0–2.0×)
  - *Advanced* (only applied when enabled): *Threshold* (0–255), *Blur* (0–5.0×), *Dilation* (0–10 px), *Erosion* (0–10 px).

### Caption

Has its own appearance and preprocessing, independent from the Capture tab.

- **Capture**
  - *Interval* — how often the area is re-read (50 ms to 5 s).
  - *Visible lines* — how many caption lines to keep on screen (1 to 8).
  - *Clear after silence* — clears caption if no new text appears for X seconds (1 to 5 s).
- **Overlay Appearance**
  - *Font size* (10–48 pt)
  - *Show background* + *Opacity* (10–100%)
  - *Show outline* + *Outline thickness* (1–5 px)
- **OCR Preprocessing** — same controls as the Capture tab, but independent.

### Shortcuts

Ten global hotkeys (work with game in focus; disabled when the settings window is in the foreground). Each has **Ctrl / Alt / Shift** modifiers and a main key (Numpad groups, Function F1–F12, and Letters): Select area · Translate · Translate with AI Vision · Clear overlay · Toggle Caption Mode · Select caption area · Show/hide areas · Toggle Real-time Mode · Select Real-time area · Show/hide floating toolbar.

> Letters as main key **require** a modifier (Ctrl, Alt, or Shift) to not conflict with the game. Numpad and F-keys work without modifier.

### Translators

- **Translation Provider → Active provider**:
  - *Google Translate* — free, no key needed. **Doesn't support Vision Mode.**
  - *DeepL* — requires a key (has a free tier; keys ending in `:fx` use the free server automatically). High-quality dedicated translator; **doesn't support Vision Mode**. No model selection, but has **Formality** (Default / More formal / More informal) — affects supported languages including English. DeepL also leverages the **Game Information** field (AI tab) and, in Caption Mode, previous lines, as context for better translation (no extra cost). With DeepL selected, a **DeepL usage** card appears showing **characters** translated in this session + **account quota** via "Update" button; "Reset session" restarts the count. It's the only engine with this tracking — AI engines don't expose spending.
  - *OpenAI*, *Anthropic (Claude)*, *Gemini* — require an API key.
- **Authentication** (appears for providers with a key; credentials are **saved per engine independently**, so switching and coming back doesn't erase anything):
  - *API Key* — your key (`sk-...`, `sk-ant-...`, `AIza...`).
  - *Model*:
    - OpenAI: GPT-4o mini (economical) · GPT-4o (superior quality).
    - Claude: Haiku 4.5 (fast/economical) · Sonnet 4.6 (superior quality).
    - Gemini: 1.5 Flash · 2.0 Flash · 1.5 Pro.
  - *Test connection* — makes a test call to the provider with your current key and model and shows immediately if it works (✓, with example translation) or the returned error (✗), instead of discovering the problem only when translating. Also available for Google (checks connectivity).

### AI

The first three sections only appear with an AI provider selected (not Google).

- **Model Parameters**
  - *Temperature* (0–2) — 0.0 literal · 0.3 recommended · 1.0+ creative.
  - *Max tokens* (256–4096) — response size; 1024 is enough for translation.
- **Conversation Context → Previous lines** (0–20) — in Caption Mode, sends the last lines (original + translation) as context to keep consistency of terms and tone. 0 = disabled; recommended 3–5.
- **System Prompt** — translator role and general rules (**Save** and **Restore defaults** buttons, which recovers factory text just for this field).
- **Game Information** — theme, characters and glossary; change per game (**Save** and **Restore defaults** buttons). The general reset (General tab) **doesn't** erase this field or the System Prompt.

### OCR

- **OCR Engine → Active engine**:
  - *WinOCR* (default) — native to Windows, ~30 ms, offline; depends on Windows language packages. Can fail on very stylized fonts.
  - *OneOCR* (experimental, Windows 11) — engine from Screenshot Tool (Snipping Tool), ~50–150 ms, auto-multilingual. Uses an unofficial Microsoft API; you copy 3 files from Windows itself (`oneocr.dll`, `oneocr.onemodel`, `onnxruntime.dll`) and point to the folder (Browse / Verify buttons — folder configures automatically if valid).
- **Block Grouping** — how detected lines are combined before translating:
  - *Paragraph Mode* — groups vertically close lines (dialogs, flowing text). Shows *Grouping sensitivity* (0–3.0; default 1): lower separates more, higher groups more.
  - *Line Mode* — each line becomes an independent block (menus, HUD).

### Web

Streams translations to browsers on the local network (and to OBS).

- **Web Server**
  - *Server active* — starts the local HTTP server.
  - *Show translation on screen* — displays the overlay even with the server running; turn off to send **only** to browser/OBS.
  - *Port* (1024–65535) — also shows how many clients are connected.
- **Addresses** — `/captura` (with history and Clear button) and `/captura/obs` (transparent background, for Browser Source on OBS), with Copy button.
- **Appearance** — *Theme* (Dark / Light / Dracula) · *Font size* (12–48 px) · *Bold* · *Detected text* (shows original) · *Time and service* · *Custom colors* (unlocks 6 color pickers: translated text, original text, time, service/badge, card background, card border).
- **History → Entries kept in buffer** (10–200).

### History

Lists translations from the **current session** (time, service, translation and, below, the original text), newest to oldest, up to the limit set in the Web tab. **Clear history** button.

### Lab

Laboratory to test preprocessing without affecting the game.

- **Test Image** — chooses an image from the `images/lab_images/` folder (next to the executable).
- **Preprocessing Parameters** — the same controls as the Capture tab, with **live preview** (original image × processed).
- **Apply to Capture** and **Apply to Caption** buttons — copy the tested configuration to the corresponding tab.

### Monitor

- **Monitoring → Active** — logs the time of each pipeline step for every translation (kept when navigating tabs).
- **Execution History** — table of the last 10 captures: Time, Capture, Preproc, OCR, Translation, Total, Blocks, Cache (hits without API) and API (calls made).
- **Statistics** — min / average / max of each step (from 2 executions onward).

### Debug

- **Debug Mode → Enabled** — saves diagnostic images for each capture in the output folder.
- **Images to save** — Original capture (`frame.png`), capture after preprocessing (`frame_proc.png`), OCR lines (`ocr_lines.png`), grouped paragraphs (`ocr_paragraphs.png`), inpainting mask preview (`mask.png`).
- **Output folder** — path to files + button to open the folder.

### Logs

Real-time session log.

- **Log captured texts and translations** — privacy toggle; **disabled by default**. Keep off when sharing logs for support, to not expose game content.
- **Filter lines** · **Auto-scroll** · **Update** — view controls (errors in red, warnings in yellow, etc.).

### Experimental

> Everything in this tab is **under development** — behavior may change, bugs are expected, and features may be removed.

- **AI-reconstructed background (MI-GAN)** — instead of a black box, erases the original text from the capture and reconstructs the background using an inpainting model (MI-GAN) running inside the program; the translation is drawn on top, as if native to the game. Works on **manual translations** (Translate and Vision); Caption Mode doesn't use it. Costs ~50–200 ms per translation and ~200 MB RAM while active. Requires downloading `migan_pipeline_v2.onnx` (28 MB) and `onnxruntime.dll`, placing them in the same folder and pointing to it (Browse / Verify). Tip: enable **Outline** in the Capture tab, since reconstructed background may be light.
- **Real-time Mode** — continuous translation drawn **in the original text's place**, over its own area. Has its own interval, font, background, outline, and auto-off options, stability adjustments (*Position stability* and *Hold on OCR failure*, against shaking/flickering with animated backgrounds) and exclusive image preprocessing. Hotkeys `Numpad3` (toggle) and `Numpad6` (select area). See **section 9**.
- **Typewriter (typewriter effect)** — waits for text to stop changing before translating, avoiding translating sentences still being "typed" on screen. Works for Caption Mode and Real-time Mode. Adjust how stable text needs to be and maximum wait time before translating anyway.
- **Hide overlay from screen capture** — prevents the drawn translation from being re-captured by OCR (feedback loop), useful mainly in continuous modes. Works for the main overlay and caption overlay. Side effect: the overlay also **disappears from recordings and streams** (OBS, Game Bar, screen sharing) — in those cases use the **web server** (section 10) to show the translation.
