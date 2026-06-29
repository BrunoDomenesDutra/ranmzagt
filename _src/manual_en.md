# User Manual — Ranmza GT

Practical guide to using **Ranmza GT**, the translator for games, visual novels, manga, and any on-screen content. This manual explains **how to use** each part of the program, without going into technical details.

---

## Table of Contents

1. [What the program does](#1-what-the-program-does)
2. [Getting started](#2-getting-started)
3. [Basic day-to-day usage](#3-basic-day-to-day-usage)
4. [Keyboard shortcuts](#4-keyboard-shortcuts)
5. [Configuring translation](#5-configuring-translation)
6. [Making translation look like the game](#6-making-translation-look-like-the-game)
7. [Vision Mode — when OCR fails](#7-vision-mode--when-ocr-fails)
8. [Caption Mode — continuous automatic translation](#8-caption-mode--continuous-automatic-translation)
9. [Real-time Mode — continuous translation in place (experimental)](#9-real-time-mode--continuous-translation-in-place-experimental)
10. [Using with OBS / streaming](#10-using-with-obs--streaming)
11. [History and performance](#11-history-and-performance)
12. [Common problems and solutions](#12-common-problems-and-solutions)
13. [Complete reference — all tabs](#13-complete-reference--all-tabs)

---

## 1. What the program does

Ranmza GT takes a screenshot of an area on your screen, recognizes the text in it, translates it, and displays the translation **on top of the game**, in the same position as the original text — like a floating subtitle.

Works with any game, visual novel, digital manga, video, or program that shows text on screen.

> **⚠️ Essential requirement: the game must be running in Windowed or Borderless Fullscreen mode.** Ranmza GT draws the translation **on top** of the game window — so run your game in **Windowed mode** (*Windowed*) or, preferably, **Borderless Fullscreen** (*Borderless* / *Fullscreen borderless*), which takes up the full screen and still lets the translation appear on top. In **Exclusive Fullscreen**, Windows gives the screen only to the game and no program can draw over it — the translation won't appear. Typical symptom: you press Translate, the translation even shows up in the **History** tab, but nothing appears over the game. Solution: change the game to **Borderless Fullscreen** in its video options.

The basic workflow is always:

1. You choose **where** the text is (an area of the screen).
2. Press a hotkey to **translate**.
3. The translation appears overlaid on the game.
4. Press another hotkey to **clear** it when you want, or it disappears on its own after a while.

---

## 2. Getting started

> **Before you start — Windows requirement:** Ranmza GT needs the **Microsoft Visual C++ Redistributable (x64)**, a free component from Microsoft. Most PCs already have it (it comes with many games and programs), but on a **freshly formatted Windows** it might be missing — then the program won't open, showing the error *"VCRUNTIME140.dll not found"*. If that happens, download and install the **x64** package from this official link:
> <https://aka.ms/vs/17/release/vc_redist.x64.exe>

### 2.1 Choose your monitor (if you have more than one)

In the **General** tab, choose which monitor the program should work on. If you always game on the same screen, leave it on "Automatic". If you switch monitors, the program asks you to restart (button "Restart now" in the tab itself) — this is necessary for everything (capture, selected area, overlay) to work on the correct screen.

> **Windows 10**: by default (Auto backend, which uses DXGI on Windows 10), **no yellow/golden border** appears around the captured screen anymore. It only shows if you manually change the **Capture Backend** (General tab) to *WGC* on Windows 10 — in that case, switch back to *Automatic* (or *DXGI*) to remove it. On Windows 11 this border never appears.

### 2.2 Choose your languages

In the **Language** tab:

- **Original text language**: the language of the game you want to translate (Japanese, English, Korean, etc.).
- **Target language**: which language you want to read (English, for example).

> If a red warning appears saying the language isn't installed, click the warning button — it opens Windows language settings directly so you can install the necessary package. Without it, text recognition won't work for that language.

### 2.3 Choose how to translate

In the **Translators** tab, choose the translation service:

- **Google Translate** — works "out of the box" with no setup needed. Good option to start.
- **DeepL** — high-quality translation, the gold standard for naturalness. Requires an API key, but DeepL offers a **free tier** (keys ending in `:fx`); paste the key and the program picks the right server automatically (free or paid). Not a conversational AI — it's a dedicated translator, fast and cheap, with **formality** options (see Translators tab).
- **OpenAI**, **Claude** or **Gemini** — require you to have an API key (paid account or with credits on the respective service). In return, they deliver much more natural and consistent translations, especially for long dialogues. Paste your key in the "Authentication" field and choose your desired model.

You can switch services anytime — each service's keys are stored separately, so switching back doesn't erase anything.

### 2.4 Select the text area

Press the **Select area** hotkey (default `Numpad7`). The screen gets a "curtain" and you drag the mouse to draw a rectangle over the region where game text appears (for example, the dialog box). Release the button to confirm, or press `ESC` to cancel.

This area is saved — you only need to select again if the game changes the text box position, resolution, etc.

> Haven't selected an area? The program captures the **entire screen**.

---

## 3. Basic day-to-day usage

> **Important**: keyboard shortcuts only work with the **game window in focus**. If Ranmza GT's settings window is open and selected (in the foreground), the shortcuts are disabled — click back on the game (or minimize the settings) before using `Numpad9`, `Numpad7`, etc.

1. Play normally.
2. When text you want to translate appears, press **Translate** (default `Numpad9`).
3. The translation appears on screen, in the position of the original text.
4. It disappears on its own after a while (configurable), or press **Clear overlay** (default `NumpadDecimal`) to remove it right away.
5. If game text changes before the translation disappears, just press **Translate** again — the old translation is automatically cleared before the new capture.

### Don't trust keyboard shortcuts?

Enable the **floating toolbar** in the **General** tab. It's a compact window that stays **always on top of any window** — even fullscreen games (borderless) — with the main commands at hand: select area, translate, translate with Vision, clear, toggle Caption Mode, select caption area, and show/hide areas (hover over a button to see its name).

Three advantages:

- **Always visible, on top of everything** — doesn't disappear behind the game or need Alt+Tab.
- **Moves freely between monitors** — drag it to any corner of the screen, on any monitor.
- **Works when the keyboard doesn't** — some games swallow or block Numpad keys (or NumLock interferes). Since the toolbar fires actions by mouse click, it completely works around this: it's a guaranteed plan B for when hotkeys don't respond.

### Checking if your areas are correct

Press **Show/hide areas** (default `Numpad2`) to draw colored rectangles showing where the program will capture (and, if Caption Mode is configured, where the caption appears). Press again to hide them. It doesn't translate anything, just a visual guide.

---

## 4. Keyboard shortcuts

| Shortcut | Default | What it does |
|---|---|---|
| Select area | `Numpad7` | Opens the selector to choose where text is |
| Translate | `Numpad9` | Captures, translates and displays on screen |
| Translate with AI Vision | `Numpad4` | Same as "Translate", but using smarter AI (see section 7) |
| Clear translation | `NumpadDecimal` (Numpad period) | Hides the displayed translation |
| Toggle Caption Mode | `Numpad0` | Activates continuous automatic translation (see section 8) |
| Select caption area | `Numpad1` | Choose where the game's caption appears |
| Show/hide areas | `Numpad2` | Shows rectangles of configured areas |
| Toggle Real-time Mode | `Numpad3` | Continuous translation in place, experimental (see section 9) |
| Select Real-time area | `Numpad6` | Choose the area Real-time Mode will translate |
| Show/hide floating toolbar | `NumpadSubtract` (Numpad minus) | Opens or closes the floating toolbar of buttons (see section 3) |

All can be changed in the **Shortcuts** tab — choose another key and, if you want, combine with Ctrl/Alt/Shift. If you choose a **letter** as a hotkey, it's **mandatory** to use at least one modifier (Ctrl, Alt, or Shift) to not interfere with normal game controls.

> Shortcuts only work when the game window is in focus (i.e., when Ranmza GT's settings window isn't in the foreground). This way you can type normally in settings fields without triggering commands accidentally.

---

## 5. Configuring translation

### Text type: dialog or menu?

In the **OCR** tab, under "Block Grouping", choose:

- **Paragraph Mode** (default) — groups nearby lines into a single translation block. Use for **dialogs, character speech, flowing text** (visual novels, JRPGs).
- **Line Mode** — each line becomes a separate translation. Use for **menus, inventory, status, HUD** — where each line is independent info and shouldn't be mixed with the one above or below.

If the program is grouping lines that should be separate (or separating a speech that should stay together), adjust the **"Grouping sensitivity"** control that appears in Paragraph Mode:
- Text being **separated too much**? Increase the value (up to 3.0).
- Text being **grouped too much**? Decrease the value (down to 0).

### Improving difficult text recognition

If the program isn't detecting text correctly (small fonts, stylized, with effects), go to the **Capture** tab and enable **Preprocessing**. A few quick tips:

- **Small text**: increase **Upscale** (2x or 3x usually fixes it).
- **Font with thick outline**: increase **Sharpen** a bit.
- **Text with low contrast against background**: increase **Contrast**.
- **Light text on dark background** (or vice versa, if it's giving wrong results): try **Invert colors**.

Don't know where to start? Use the **Lab** tab — you can test all these options on sample images, see the result in real time, and then apply the best-working configuration directly to Capture or Caption.

### Switching OCR engine (advanced)

If preprocessing still doesn't fix recognition, the **OCR** tab lets you switch the text recognition "engine":

- **WinOCR** (default) — fast, comes ready, but can fail on very stylized fonts.
- **OneOCR** (experimental, Windows 11) — the OCR engine from Windows Screenshot Tool (Snipping Tool), much better than WinOCR on stylized fonts and auto-detects language (no need to configure source language). You copy 3 files from Windows itself to a folder of yours — the OCR tab shows step-by-step. Because it uses an unofficial Microsoft API, a Snipping Tool update might break it; if so, just re-extract the files.

---

## 6. Making translation look like the game

In the **Capture** tab, appearance section:

- **Font**: choose from fonts in the `fonts/` folder or use Windows' default font.
- **Font size** and **Line height**: adjust so text is readable and well-spaced.
- **Auto-fit**: leave enabled so the program **automatically shrinks the font** if the translation is bigger than the original text's space — this way text is never cut off.
- **Background**: draws a dark box behind the text (with adjustable opacity) to guarantee readability over any scenery.
- **Outline**: alternative to background — draws a black border around letters, no visible box, for a more discrete/integrated look.

> Background and outline are alternatives — enabling one disables the other automatically.

### How long translation stays on screen

Under "Display", choose how long the translation stays visible after appearing: 15s, 30s, 1 minute (default), 2, 5, or 10 minutes — or "Never" (translation only disappears when you press clear or translate again).

---

## 7. Vision Mode — when OCR fails

Sometimes normal text recognition (OCR) misses letters, loses parts of text, or gets completely lost on very stylized/artistic fonts, with symbols or icons mixed in the text.

For those cases, use the **Translate with AI Vision** hotkey (default `Numpad4`). Instead of relying only on recognized text, the program **sends the screen image to Artificial Intelligence**, which "looks" at the image and understands better what's written, even if text recognition got it wrong.

**Important:**
- Only works with **OpenAI, Claude, or Gemini** (Google Translate and DeepL don't support this mode).
- It's a bit slower and **always makes a new call** to the AI (doesn't use translation history).
- The translation's position on screen still depends on where text recognition found something — so in rare cases, the translation might be larger than the detected area.

**When to use**: hand-drawn fonts, stylized credits, text with icons/symbols mixed in (ex: "press [button icon] to continue"), or whenever the normal hotkey ("Translate") returns nonsensical text.

---

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

## 10. Using with OBS / streaming

If you stream or record the game and want **the translation to also appear in the video/stream** (or only in the video, without appearing in the game itself), use the **Web** tab:

1. Enable the **server**.
2. Copy the `/captura/obs` address shown in the tab.
3. In OBS, add a source of type **"Browser Source"** and paste that address. This version of the page has a transparent background, ready to overlay the game capture.
4. (Optional) Enable **"Show translation on screen"** to **turn off the normal overlay** and let the translation appear **only** on the browser page/OBS — useful if OBS's capture already includes the overlay window and you don't want to see the translation twice.

You can also customize theme (light/dark/dracula), colors, font size, and whether you want to show the original text together with the translation, time, and which service was used.

The page can also be opened in any browser on the local network (phone, second monitor, etc.) using the `/captura` address shown in the tab.

---

## 11. History and performance

- **History tab**: shows translations made during the current session (original text, translation, time and service used). Has a button to clear.
- **Monitor tab**: turns on a log of the latest translations with the time each step took (capture, recognition, translation, total) — useful to notice if any configuration is slowing the program down (for example, heavy preprocessing).
- **DeepL usage** (Translators tab, with DeepL selected): shows how many **characters** DeepL translated in this session and your **account quota** (characters used/billing period limit) — click "Update" to check. Exclusive to DeepL.

---

## 12. Common problems and solutions

**"Error opening program: VCRUNTIME140.dll not found" (or MSVCP140.dll)**
→ Your Windows is missing **Microsoft Visual C++ Redistributable** — a free Microsoft component some freshly-formatted PCs don't have. Download and install the **x64** package from this official link: <https://aka.ms/vs/17/release/vc_redist.x64.exe> — then reopen Ranmza GT, it should open normally.

**"Recognition detects nothing" / red warning about language**
→ Go to the Language tab and click the warning to install the necessary Windows language package.

**"I pressed the hotkey and nothing happened"**
→ Check if the settings window isn't in the foreground (hotkeys only work with the game in focus). If still nothing, enable the **floating toolbar** (General tab) and use its buttons.

**"Hotkeys don't work in some games (even with game in focus)"**
→ Some games run with elevated privileges (Administrator) and therefore **block Ranmza GT's global hotkey registration**. In that case, **run Ranmza GT as Administrator** (right-click the `.exe` → *Run as administrator*) — then it can activate hotkeys over the game. To avoid repeating every time, check *Run this program as an administrator* in **Properties → Compatibility** of the executable. (Alternative: use the **floating toolbar**, which fires actions by mouse click and doesn't depend on keyboard hotkeys.)

**"Translation doesn't appear, or it's slow"**
→ Check the History/Monitor tab to see if translation is being done. If a yellow "fallback to Google Translate" warning appears, the configured service (OpenAI, Claude, Gemini) failed — check your API key and credits in the Translators tab.

**"A red error warning appeared"**
→ Usually means invalid API key, exhausted credits, or the service temporarily down. Check the Translators tab.

**"Recognized text is wrong/incomplete"**
→ Try enabling preprocessing (Capture tab) with upscale and contrast adjustments, or use the **Translate with AI Vision** hotkey (`Numpad4`) to let the AI "see" the image and correct it.

**"Translation is cut off or doesn't fit in the box"**
→ Enable **Auto-fit** in the Capture tab — the program will automatically shrink the font until it fits.

**"Translations of different lines are mixing into one block (or the opposite)"**
→ Adjust **Grouping sensitivity** in the OCR tab (Paragraph Mode).

**"I switched monitors and capture isn't working right anymore"**
→ Restart the program via the General tab button — it's necessary after switching monitors.

**"I want to share my logs for support, but don't want to show game content"**
→ Check the Logs/Debug tab if the option "Log captured texts and translations" is **disabled** (it's the default) — this way logs don't show text/translation content.

---

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
