# User Manual — Ranmza GT

Practical guide to using **Ranmza GT**, the translator for games, visual novels, videos, and any on-screen content. This manual explains **how to use** each part of the program, without going into technical details.

---

## Table of Contents

1. [What the program does](#1-what-the-program-does)
2. [Quick setup](#2-quick-setup)
3. [Basic day-to-day usage](#3-basic-day-to-day-usage)
4. [Profiles — one set of settings per game](#4-profiles--one-set-of-settings-per-game)
5. [Keyboard shortcuts](#5-keyboard-shortcuts)
6. [Configuring translation](#6-configuring-translation)
7. [Making translation look like the game](#7-making-translation-look-like-the-game)
8. [Vision Mode — when OCR fails](#8-vision-mode--when-ocr-fails)
9. [Subtitle Mode — continuous automatic translation](#9-subtitle-mode--continuous-automatic-translation)
10. [Using with OBS / streaming](#10-using-with-obs--streaming)
11. [History and performance](#11-history-and-performance)
12. [Common problems and solutions](#12-common-problems-and-solutions)
13. [Complete reference — all tabs](#13-complete-reference--all-tabs)
14. [Updating the program](#14-updating-the-program)

---

## 1. What the program does

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

## 2. Quick setup

The first time you open the program, the **Setup guide** shows up by itself and walks through everything you need to choose. Follow the guide and you are ready to translate; the rest of this section explains each step more calmly, for those who skipped the guide or want to understand what they chose.

| Step | What to do | Where |
|---|---|---|
| 1 | Pick the monitor | guide or **General › Config** tab |
| 2 | Pick the text reader (OCR) | guide or **General › OCR** tab |
| 3 | Pick the languages | guide or **General › Language** tab |
| 4 | Pick the translator | guide or **Translation › Translators** tab |
| 5 | Mark the text area | `Numpad7` shortcut, with the game open |
| 6 | Translate | `Numpad9` (line) or `Numpad8` (paragraph) shortcut |

> **First of all: the game in Windowed mode.** In *Exclusive Fullscreen* no program can draw on top — the translation simply does not show. Switch the game to **Borderless Window** in its video options. Full explanation in [section 1](/en/Manual/what-the-program-does.md).

> **The program did not even open, with the error *"VCRUNTIME140.dll was not found"*?** The **Microsoft Visual C++ Redistributable (x64)** is missing — a free Microsoft component most PCs already have (it ships with many games). Install it from this official link and open the program again: <https://aka.ms/vs/17/release/vc_redist.x64.exe>

### 2.1 The Setup guide

The guide is a window over the settings screen, with eight steps:

| Step | What you choose |
|---|---|
| **Start** | Nothing: it explains how the program works and the two ways to translate |
| **Monitor** | Which monitor the game is on, and what that choice changes |
| **OCR** | WinOCR or OneOCR, with the pros and cons of each. With OneOCR, the button to copy its files |
| **Languages** | The language of the game text and the language you want to read |
| **Translation** | The translation service and its key, if needed, with a list of which one to choose |
| **Capture** | How long the screen capture translation stays on screen, font, color and Auto-fit |
| **Subtitle** | Font, color and the alphabet filter of Subtitle Mode |
| **Done** | A summary of what you chose and the keys to get started |

Everything you change in the guide applies right away, just like in the tabs. The steps at the top are clickable, to go back or jump to another one. With **WinOCR**, the guide does not go past the Languages step without a chosen language, because without it WinOCR does not know what to read.

- **Finish**, on the last step, or **Skip**, at any time, close the guide. It does not come back by itself after that.
- Closing the program in the middle of the guide makes it show up again next time.
- To see the guide again, use the **Guide** button at the top of the screen.
- Creating a profile with **Start from scratch** also opens the guide, to set up the new game.

### 2.2 First look: how the window is organized

<p align="center"><img src="media/geral-config.png" alt="General › Config tab" width="820"></p>

The left menu groups the options by subject. In the quick setup you only touch **General** and **Translation** — the rest is there for when you want to fine-tune something.

| Menu | What is inside |
|---|---|
| **General** | Config (screen language, appearance, updates, monitor, alerts), Profiles, Language, OCR and Shortcuts (floating toolbar) |
| **Overlay** | How the translation looks on screen: Capture, Subtitles and Web |
| **Translation** | Translators (service and API keys) and AI (prompts and context) |
| **Tools** | Inpaint (erase the original text) |
| **Debug** | Performance monitor and Logs |
| **History** | Screen capture translations from the current session |
| **About** | Program version, license and links |

At the top of the window are the **Profile** selector, the **Guide** button and the **A−** and **A+** buttons, which shrink and enlarge the text of the settings screen.

> **Interface language** (in *General › Config*) changes only the language **of the program** — the menus and texts you are looking at. It has nothing to do with the language being translated; that is step 2.4.

### 2.3 Pick your monitor

In **General › Config**, in the **Monitor** card, choose under **Active display** where the game is. With a single monitor, leave it on *Automatic* and move on.

The chosen monitor is where area selection, alerts, the area preview and the floating toolbar open, until you drag the toolbar elsewhere. The translation shows up on the monitor where the area was marked.

- **The change applies right away**, no restart.
- **Each monitor keeps its own areas.** When you switch monitors, the areas of the previous monitor are kept; when you switch back, they come back. The first time you use a monitor, mark the areas on it.
- **Each profile keeps its own monitor.** With one profile per game, each game comes back on its monitor.
- If the chosen monitor is disconnected, the program uses the Windows primary one.

The **Capture backend** just above can stay on *Auto (recommended)*: it picks the right method for your Windows version by itself and switches right away, no restart.

### 2.4 Pick your languages

Open **General › Language**.

<p align="center"><img src="media/geral-idioma.png" alt="General › Language tab" width="820"></p>

- **Text language** — the language the game is in. With WinOCR, the list only shows the languages that already have the text recognition pack installed in Windows. On a new install the field comes empty, with a warning: pick one from the list.
- **Target language** — the language you want to read.

> **The game language is not on the list?** WinOCR only reads languages whose pack is installed in Windows. Install it in *Settings → Time & Language → Language & region* and open the program again. If Windows has no pack with text recognition at all, the warning has an **Install language pack** button that opens that screen.

> **Using OneOCR?** Then there is no source language to choose: it is a single multilingual model (Latin, Japanese, Chinese, Korean, Cyrillic…) that detects the language by itself, and the **Text language** field does not even show while it is selected. The **Target language** still applies normally. OneOCR is the **recommended** engine and is chosen in *General › OCR* — see *Switching OCR engine* in [section 6](/en/Manual/configuring-translation.md).

### 2.5 Pick your translator

Open **Translation › Translators**.

<p align="center"><img src="media/tradutores-google.png" alt="Translation › Translators tab with Google Translate" width="820"></p>

The default is **Google Translate — free**: no key and no setup, ready to use. Do your first test with it.

> **Free, but limited.** Keyless Google Translate only accepts a handful of translations in a short window. Past that, the *"Google: rate limited (429)"* alert shows and that capture stays untranslated. For a line here and there it works; in a long session and in Subtitle Mode the limit comes fast. And the limit is counted **per IP address** — people on mobile internet or a provider with **CGNAT** share that limit with other customers and hit it much sooner. The explanation and what to do are in [section 12](/en/Manual/common-problems-and-solutions.md).

?> **Heads up: the Google API used here is not official.** It is the same address the Google Translate web page uses behind the scenes, without a key or account. It is not published or documented, so Google can change it or take it down whenever it wants, without notice — and on that day only the services with a key will keep translating. If you depend on the program to play, it is worth having a key for another service already set up.

When you want more quality, switch in **Active provider**:

- **Google Cloud Translation**, **DeepL** and **Azure Translator** — dedicated translators. They need an API key and have a free plan with a monthly limit. On DeepL, free plan keys end in `:fx`, and the program figures out which server to use. DeepL also receives the Game Info and the previous lines as context, at no extra cost. Azure, besides the key, requires the resource **region** (both are on the same page of the Azure portal).
- **OpenAI**, **Anthropic (Claude)**, **Gemini** and **Groq** — AIs. They need an API key and, in return, deliver more natural and consistent translations, because they take the previous lines and the Game Info into account. OpenAI and Anthropic charge per use; Gemini and Groq have a free plan. Pick the model in the authentication card and paste the key under *API Keys*.

<p align="center"><img src="media/tradutores-openai.png" alt="Translation › Translators tab with OpenAI" width="820"></p>

Each service keeps its own keys, so switching from one to another and back does not erase anything. Keys are stored **encrypted** and only open on this PC, in your Windows account.

> **Multiple keys with automatic rotation.** Every service with a key accepts **more than one**: click *+ Add key*. If the key in use is rejected, runs out of credit or hits the request limit, the program switches right away to the next one in the list; when all are used up, it falls back to Google Translate and shows the *"<service> failed, using Google"* alert. This helps a lot in long Subtitle Mode sessions.

> Only OpenAI, Anthropic and Gemini support **Vision Mode** — Google Translate, Google Cloud, DeepL, Azure and Groq do not. See [section 8](/en/Manual/vision-mode-when-ocr-fails.md).

### 2.6 Mark the text area

With the game open and in focus, press **`Numpad7`**. The screen darkens and you drag the mouse to draw a rectangle over the region where the text appears — usually the dialogue box. Release the button to confirm, or press `ESC` to cancel.

The area is saved. You only need to mark it again if the game moves the text box or you change the resolution.

> With no area marked, the translation shortcuts do not translate anything: the *"Capture: no area"* alert shows up. Mark the area first.

<div style="position:relative;padding-top:56.25%;max-width:820px;margin:0 auto">
  <iframe src="https://player.vimeo.com/video/1218016540"
          style="position:absolute;top:0;left:0;width:100%;height:100%;border:0"
          allow="fullscreen; picture-in-picture" allowfullscreen
          title="Marking the text area"></iframe>
</div>

<p align="center"><i>Marking the text area with `Numpad7`.</i></p>

### 2.7 Translate

With the text on screen, press one of the two translation shortcuts — the only difference is **how lines are grouped** before translating:

| Shortcut | Mode | Use when |
|---|---|---|
| **`Numpad9`** | **Line** | Menus, lists, items, buttons — each line is a separate thing |
| **`Numpad8`** | **Paragraph** | Dialogues and running text — joins nearby lines into one block |

When in doubt, start with `Numpad8` in story games and `Numpad9` in menus.

The translation shows up over the game, where the original text was, and disappears by itself after a while. To remove it right away, press **`NumpadDecimal`** (the numpad decimal key).

<div style="position:relative;padding-top:56.25%;max-width:820px;margin:0 auto">
  <iframe src="https://player.vimeo.com/video/1217778050"
          style="position:absolute;top:0;left:0;width:100%;height:100%;border:0"
          allow="fullscreen; picture-in-picture" allowfullscreen
          title="Selecting the area and translating"></iframe>
</div>

<p align="center"><i>Selecting the area and translating — in line and paragraph modes.</i></p>

> **Shortcuts only work with the game in focus.** With the Ranmza GT settings window in the foreground they are disabled on purpose — so you can type in the fields without triggering commands by accident. If you press a shortcut with the settings in focus, an alert tells you. Click back into the game before testing.

### 2.8 Plan B: the floating bar

Some games "swallow" the Numpad keys, and sometimes NumLock gets in the way. For those cases, turn on **Show floating toolbar** in *General › Shortcuts*: a small window with the same commands as buttons, triggered by mouse click.

<p align="center"><img src="media/barra-flutuante.png" alt="Ranmza GT floating toolbar" width="560"></p>

It stays **always on top of everything** — including a borderless window game — and you drag it by the dotted handle on the left to any corner of any monitor. The `NumpadSubtract` shortcut (the numpad minus) shows and hides the toolbar.

The buttons, from left to right (hover over one to see its name), in three groups:

| Group | Buttons |
|---|---|
| Screen capture | Select area · Translate (paragraph) · Translate (line) · Vision (paragraph) · Vision (line) · Clear |
| Subtitle Mode | Select subtitle area · Toggle subtitles |
| Preview | Show/hide areas |

On the right end, two **+ / −** buttons resize the whole toolbar on screen — useful on 4K or very small monitors. The button colors follow the theme of the settings screen.

### 2.9 Changing the hotkeys

If the default keys do not suit you — keyboard without a numpad, conflict with the game controls — change them in **General › Shortcuts**.

<p align="center"><img src="media/geral-atalhos.png" alt="General › Shortcuts tab" width="820"></p>

Each action has a main key, chosen in the list on the right, and three modifier buttons (Ctrl, Alt and Shift) you turn on if you want to combine them. The change applies right away, no restart.

> **A letter or number as the main key requires a modifier** (Ctrl, Alt or Shift), otherwise you would trigger the program every time you type in the game. Numpad keys, F1–F12 and the navigation keys work on their own.

### Did it work? And if it didn't

If the translation showed up over the game, everything is ready — go on to [section 3](/en/Manual/basic-day-to-day-usage.md).

- **Nothing happened when pressing the shortcut** → the settings window was in focus, or the game is "swallowing" the Numpad keys. Use the **floating toolbar** (step 2.8) or change the key (step 2.9).
- **The translation shows up in the History tab, but not over the game** → the game is in *Exclusive Fullscreen*. Switch to *Borderless Window*.
- **The translation came out wrong or scrambled** → the OCR misread. Start by switching the grouping mode (`Numpad9` ↔ `Numpad8`) and see [section 6](/en/Manual/configuring-translation.md).

Other problems are in [section 12](/en/Manual/common-problems-and-solutions.md).

---

## 3. Basic day-to-day usage

> **Important**: keyboard shortcuts only work with the **game window in focus**. If the Ranmza GT settings window is open and selected (in the foreground), shortcuts are disabled — click back into the game (or minimize the settings) before using `Numpad9`, `Numpad7`, etc.

1. Play normally.
2. When a text you want translated shows up, press **Translate**: `Numpad8` for dialogues (paragraph mode) or `Numpad9` for menus (line mode).
3. The translation shows up on screen, where the original text was.
4. It disappears by itself after a while (configurable), or press **Clear overlay** (default `NumpadDecimal`) to remove it right away.
5. If the game text changes before the translation disappears, just press **Translate** again — the old translation is cleared automatically before the new capture.

For dialogues that play on their own, like cutscenes, use **Subtitle Mode** ([section 9](/en/Manual/subtitle-mode-continuous-automatic-translation.md)): you turn it on once and it translates each line without you pressing anything.

### Paragraph or line: get the hang of it

Choosing between `Numpad8` and `Numpad9` is the setting that changes the result the most day to day, and you do it on the spot, without opening any settings:

- **`Numpad8` (paragraph)** joins nearby lines into one block. That is what you want in a dialogue box, where the line continues from one row to the next.
- **`Numpad9` (line)** translates each line on its own. That is what you want in an inventory or menu, where "Potion" and "Long sword" have nothing to do with each other.

Wrong mode? Press the other shortcut right after — the previous translation is cleared by itself.

### Don't trust keyboard shortcuts?

Turn on the **floating toolbar** in **General › Shortcuts** and trigger everything with the mouse. It stays above any window, moves freely between monitors and is plan B for when the game "swallows" the Numpad keys. The nine buttons are explained in [step 2.8](/en/Manual/quick-setup.md).

### Checking if your areas are correct

Press **Show/hide the selected areas** (default `Numpad2`) to draw on the chosen monitor the outline and name of each area: the screen capture area, the subtitle area and the strip where the subtitle translation appears. Press it again to hide them. It does not translate anything, it is only a visual guide, and it follows a new area or a settings change right away.

---

## 4. Profiles — one set of settings per game

Each game needs different settings: the dialogue box sits in a corner of the screen, the language is another, the font that reads well in one does not in another, and the glossary of names is useless anywhere else. A **profile** keeps all of that together, and you switch games in one click.

The selector is at the **top of the window**, next to the **Guide** button, and shows up in every tab — because the active profile is the context of everything they show.

<p align="center"><img src="media/geral-perfis.png" alt="General › Profiles tab" width="820"></p>

### The Default profile

It always exists, comes active and **cannot be deleted or renamed**. If you never create another profile, everything you adjust stays in it.

Anyone who already used Ranmza GT loses nothing in the update — the previous settings become the Default profile automatically.

### Creating a profile

Go to **General › Profiles**, write the game name and choose:

- **Duplicate current** — copies everything in effect right now, including the monitor and the selected areas. It is the usual path: you set the program up right for a game and want to keep it under a name.
- **Start from scratch** — uses the factory values, on the current monitor, and opens the **Setup guide** for you to set up the new game. Good for a game that has nothing to do with the previous one.

The new profile becomes active right away. From then on, just adjust the program normally, in the usual tabs: **everything you change is saved in it by itself**, with no save button.

### Switching profiles

Click the selector at the top and pick another one (or click its row in *General › Profiles*). The switch applies right away — monitor, areas, languages, appearance and glossary change together, no restart. An alert on screen confirms which profile came in, useful when you switch with the game in the foreground.

If **Subtitle Mode** is on, it stays on and starts capturing the new profile's area.

### Renaming and deleting

In **General › Profiles**, each profile (except Default) has **Rename** and **Delete**. Deleting asks for confirmation; if you delete the profile in use, Default takes over right away.

### What does NOT change when you switch profiles

Not everything is "per game" — what is yours stays the same in every profile:

| Follows the profile | Applies to all profiles |
|---|---|
| Monitor and the saved areas of each monitor | API keys |
| Screen capture area and subtitle area | Keyboard shortcuts and floating toolbar |
| Text language, alphabet filter and target language | Capture backend |
| Screen capture and subtitle appearance | OCR engine, OneOCR folder and Paragraph mode grouping |
| Translation service, model and Azure region | Inpaint |
| Previous lines, System Prompt and Game Info | Web server and alerts |
| Subtitle Mode options | Language, theme and zoom of the settings screen |

The API key is the case that matters most: you type it **once** and it applies to every profile, including the ones you create later.

---

## 5. Keyboard shortcuts

| Shortcut | Default | What it does |
|---|---|---|
| Select area | `Numpad7` | Opens the selector to choose where the screen capture text is |
| Translate (paragraph mode) | `Numpad8` | Captures and translates joining nearby lines into a block — dialogues |
| Translate (line mode) | `Numpad9` | Captures and translates each line on its own — menus and lists |
| Translate with AI Vision (paragraph mode) | `Numpad5` | Same as `Numpad8`, but sending the image to the AI (see section 8) |
| Translate with AI Vision (line mode) | `Numpad6` | Same as `Numpad9`, but sending the image to the AI (see section 8) |
| Retranslate (no cache) | `Numpad4` | Repeats the last translation without using saved translations (see below) |
| Clear overlay | `NumpadDecimal` (numpad decimal) | Hides the screen capture translation |
| Toggle subtitles | `Numpad0` | Turns on continuous automatic translation (see section 9) |
| Select subtitle area | `Numpad1` | Chooses where the game subtitle is |
| Show/hide the selected areas | `Numpad2` | Shows the outline of the configured areas |
| Show/hide floating toolbar | `NumpadSubtract` (numpad minus) | Opens or closes the floating button toolbar (see section 3) |

> **Retranslate (`Numpad4`).** Every translation is saved in the profile, and the same text does not go to the API again: it comes out instantly and at no cost. The downside is that, if the AI translated something wrong, the mistake comes back every time the text shows up. `Numpad4` repeats the last translation, in the same mode (paragraph, line or Vision), without looking at what is saved, and the new translation replaces the old one. It works on screen capture translations, by shortcut or by the floating toolbar; Subtitle Mode is not included.

All of them can be changed in **General › Shortcuts** — pick another key and, if you want, combine it with Ctrl/Alt/Shift. If you choose a **letter or a number** from the top row, you **must** use at least one modifier (Ctrl, Alt or Shift), so it does not get in the way of the game's normal controls (which use WASD and slots 0–9 all the time). Numpad, F1–F12 and the navigation keys work on their own — the **Digits** and **Navigation** groups help people on laptops without a numpad.

<p align="center"><img src="media/geral-atalhos.png" alt="General › Shortcuts tab" width="820"></p>

> Shortcuts only work when the game window is in focus (that is, when the Ranmza GT settings window is not in the foreground). This way you can type normally in the settings fields without triggering commands by accident.

---

## 6. Configuring translation

### Text type: dialog or menu?

The grouping mode **is not chosen in a tab** — it is decided at capture time, by the shortcut you press:

- **`Numpad8` — Paragraph Mode** — joins nearby lines into a single translation block. Use it for **dialogues, character lines, running text** (visual novels, JRPGs).
- **`Numpad9` — Line Mode** — each line becomes a separate translation. Use it for **menus, inventory, stats, HUD** — where each line is independent information and must not be mixed with the one above or below.

The same goes for Vision: `Numpad5` is paragraph and `Numpad6` is line.

If Paragraph mode is joining lines that should be separate (or splitting a line that should stay together), adjust the **Grouping sensitivity** in **Overlay › Capture**:

- Text **split too much**? Raise the value (up to 3.0).
- Text **joined too much**? Lower the value (down to 0.5).

This setting only affects Paragraph mode — Line mode ignores it.

<p align="center"><img src="media/ocr-sensibilidade.png" alt="Grouping sensitivity, in Overlay › Capture" width="820"></p>

<p align="center"><i>The setting is in the <b>Overlay › Capture</b> tab, in the <b>Paragraph Mode Fine-Tuning</b> card.</i></p>

### Switching OCR engine — and why OneOCR is recommended

OCR is the text reader: it turns what shows up in the marked area into text to be translated. It is used in screen capture and in Subtitle Mode, and the better it reads, the better the translation. In **General › OCR** you choose between two:

- **WinOCR** (native to Windows) — ready out of the box, nothing to install, and the default. It reads text on a plain background well, but gets lost easily when the background behind the text has details, colors or movement, and only reads languages whose pack is installed in Windows.
- **OneOCR** (recommended) — the text reader of the Windows 11 Snipping Tool. It is the one you should use.

<p align="center"><img src="media/geral-ocr.png" alt="General › OCR tab with WinOCR" width="820"></p>

**Why OneOCR is far better:**

- **It reads much more accurately.** Stylized fonts, text with outline, shadow or effects on top, small text, text over busy backgrounds — situations where WinOCR returns swapped letters or missing words and OneOCR reads correctly.
- **All languages at once, with no setup.** It is a single multilingual model (Latin, Japanese, Chinese, Korean, Cyrillic…) with automatic detection: there is no "text language" to choose and no Windows language pack to install. A game that mixes English and Japanese on the same screen is read the same way.
- **Fewer things to go wrong day to day.** No missing language pack and no switching languages for every game.

**Is it worth the trouble of getting the files?** Yes, by far. It is three files copied once — after that the quality of the whole translation goes up, because everything that comes after (grouping, translation, subtitles) depends on the text being read correctly.

**What it needs:** the files `oneocr.dll`, `oneocr.onemodel` and `onnxruntime.dll`. The program **never goes after them by itself**: you copy them, with one click.

**On Windows 11 it is one click.** Choose *OneOCR* in **General › OCR** (or in the OCR step of the guide) and use the **Detect and copy** button: the program finds the installed Snipping Tool, copies the 3 files to its folder and sets everything up. If the Snipping Tool is not installed, or is a version without the files, it tells you instead of failing silently. Until the files are copied, the card shows *"Did not load"* and the OCR stays stopped.

<p align="center"><img src="media/geral-ocr-oneocr.png" alt="OneOCR card, in General › OCR" width="820"></p>

<p align="center"><i>With <b>OneOCR</b> selected, the card has the <b>Detect and copy</b> button, the folder field and, below, the step by step for Windows 10.</i></p>

**On Windows 10 it is manual**, because **the files only come with the Windows 11 Snipping Tool** (OneOCR itself runs on both). Copy the three from a Windows 11 machine and point to the folder with **Browse...** — the step by step inside the card has the PowerShell command that shows where they are.

Since it uses an unofficial Microsoft API, a Snipping Tool update can break the integration; in that case, click **Detect and copy** again.

### Subtitle alphabet filter

In Subtitle Mode, the program can consider only the letters of one alphabet and ignore the rest: Latin, Japanese/Chinese, Korean or Cyrillic. Useful when names, signs or symbols in another alphabet show up near the subtitle. It is in **Overlay › Subtitles**, in the **Original subtitle alphabet** card:

- With **OneOCR**, you choose the alphabet in the list (default: *Any alphabet*).
- With **WinOCR**, the filter follows the language chosen in **General › Language** by itself.

It only applies to Subtitle Mode; screen capture reads all the text in the area.

### OpenAI fast queue

With OpenAI selected, the model card has the **OpenAI fast queue** option. When on, OpenAI serves your requests first, at twice the price per token. It helps when OpenAI is slow. It comes **off**: the key is yours, so the doubled bill only happens if you turn it on.

---

## 7. Making translation look like the game

In **Overlay › Capture**, in the **Text** card:

<p align="center"><img src="media/captura-texto.png" alt="Text card, in Overlay › Capture" width="720"></p>

- **Font**: choose among the fonts in the `fonts/` folder, next to the program, the Windows fonts or the system default (Arial). The preview just below shows how it looks.
- **Text color**: white by default; change it to match the game palette.
- **Font size** and **Line height**: adjust so the text is readable and well spaced.
- **Auto-fit** (on by default): shrinks the font until the translation fits where the original text was. When off, a translation longer than the original spills past that spot and may cover nearby text. Tip: with Auto-fit on, keep the **Font size** high — the program finds the largest size that fits by itself.

In the **Background and Outline** card:

<p align="center"><img src="media/captura-fundo.png" alt="Background and Outline card, in Overlay › Capture" width="720"></p>

- **Background**: draws a dark box behind the text (with adjustable opacity), to keep it readable over any scenery.
- **Outline**: draws a border around the letters, with adjustable thickness and color — it can be used on its own or together with the background.

### How long translation stays on screen

In **Display**, choose how long the screen capture translation stays visible after it shows up: 1 minute (default), 2, 5, 10 minutes or *Never*, which keeps the translation on screen until you clear it or translate again. To remove it sooner, press the clear shortcut or translate again.

The same card has **"Hide the translation from recordings and streams"**: when on, the translation stays on your screen normally, but does not show up for capture programs. Useful for recording the game without the translation on top. It only applies to screen capture.

<p align="center"><img src="media/captura-exibicao-duracao.png" alt="Display card, in Overlay › Capture" width="820"></p>

> It only works with programs running **ON THIS PC** (OBS, Game Bar, NVIDIA ShadowPlay, etc). Recording with a capture card, the translation shows anyway — Windows is the one hiding the window, and what goes out through the video cable is the whole screen.

---

## 8. Vision Mode — when OCR fails

Sometimes regular text recognition (OCR) misreads letters, loses pieces of the text or gets completely lost with very stylized fonts, with symbols or icons in the middle of the text.

For those cases, use **Translate with AI Vision**. Along with the recognized text, the program **sends the image of the area to the AI**, which "looks" at the image, fixes what the OCR misread and translates. A symbol or icon in the middle of a sentence becomes `[...]` in the translation.

Just like regular Translate, Vision has both modes, and you pick by shortcut:

- **`Numpad5`** — Vision in **paragraph mode** (dialogues).
- **`Numpad6`** — Vision in **line mode** (menus and lists).

**Important:**
- It only works with **OpenAI, Anthropic (Claude) or Gemini**. With Google Translate, Google Cloud, DeepL, Azure or Groq, the shortcut translates only the OCR text and shows the *"Vision needs an AI provider"* alert.
- It uses the same model chosen in **Translation › Translators**.
- It is a bit slower and **always makes a new call** to the AI: it does not use saved translations, because the answer depends on the image.
- The position of the translation on screen still depends on where text recognition found something.

**When to use it**: hand-drawn fonts, stylized credits, text mixed with icons/symbols (e.g. "press [button icon] to continue"), or whenever the regular shortcut ("Translate") returns nonsense.

---

## 9. Subtitle Mode — continuous automatic translation

For scenes with continuous dialogue (cutscenes, visual novel auto mode, subtitled videos), Subtitle Mode translates **by itself**, without you pressing anything for each line.

### How to set up

1. Press **Select subtitle area** (default `Numpad1`) and draw a rectangle over where the subtitle shows up in the game. This area is separate from the screen capture area.
2. Press **Toggle subtitles** (default `Numpad0`) to turn it on. An alert on screen confirms it.

The program always opens with subtitles off. The options are in **Overlay › Subtitles**, and the defaults already work well for most cases.

<p align="center"><img src="media/overlay-legenda-captura.png" alt="Overlay › Subtitles tab — Capture and alphabet" width="820"></p>

From then on, the program watches that area several times per second and translates each new text as soon as it shows up and repeats in a second reading. This avoids translating a line that is still being written on screen. If the area stays the same, the program does not even read the text again.

By default, the translation shows up **above** the selected area and disappears by itself a few seconds after the subtitle leaves the game. You can switch that to the translation on top of the original subtitle — that is the next topic.

<div style="position:relative;padding-top:56.25%;max-width:820px;margin:0 auto">
  <iframe src="https://player.vimeo.com/video/1217784520"
          style="position:absolute;top:0;left:0;width:100%;height:100%;border:0"
          allow="fullscreen; picture-in-picture" allowfullscreen
          title="Subtitle Mode translating by itself"></iframe>
</div>

<p align="center"><i>Subtitle Mode translating by itself, with the translation above the selected area.</i></p>

### Ignore text away from the center of the area

The **Ignore text away from the center of the area** option, in the **Capture** card, comes on. With it, the program ignores text near the edges of the area, like signs and other game text that shows up beside the subtitle.

- The tighter the area is around the subtitle, the better it works. Mark only the strip where the subtitle appears.
- In games with left-aligned dialogue, like some RPGs and visual novels, keep this option off.

### Stick to the detected text

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

### More than one line on screen

With *Stick to the detected text* off, **Lines on screen** (1 to 8, default 1) sets how many lines stay visible at once. With more than one, each line sits on its own row, starting with a dash, in the middle of the monitor. A line too long for the width shrinks the font of the block instead of wrapping.

### Letting the AI "remember" previous lines

With an AI (OpenAI, Anthropic, Gemini or Groq), **Translation › AI** has the **Previous lines** control (5 to 10, default 5). The AI receives the last lines already translated as reference before translating the next one — this helps keep the same names, terms and tone throughout a conversation. Each extra line costs tokens on every translation.

> **DeepL** receives only the original text of those lines, as context, and does not charge for it. The other dedicated translators (Google Translate, Google Cloud and Azure) translate each line on its own.

### Separate appearance

Overlay › Subtitles has its own font, color, background and outline options — independent from screen capture — so you can keep the continuous subtitle smaller and more discreet and the screen capture translation larger, for example.

### Turning it off

Press **`Numpad0`** again, or the toggle subtitles button on the floating toolbar. The subtitle on screen is cleared immediately.

The mode also **turns itself off** after a while with no text in the area, so it does not keep running for nothing when you leave the cutscene and forget to turn it off. The time is chosen in *Overlay › Subtitles → Turn off subtitles with no text in the area*: Never, 1, 2, 5 or 10 minutes (default 1 minute). A subtitle standing still on screen counts as text. Note that this **turns the mode off**, it does not just hide the subtitle — to turn it back on, press `Numpad0`.

---

## 10. Using with OBS / streaming

If you stream or record the game and want **the screen capture translation to show up in the video/stream too** (or only in the video, without showing in the game itself), use **Overlay › Web**:

1. Turn on **Server active**.
2. Copy the **Capture — OBS** address (`/captura/obs`) shown in the tab, with the *Copy* button.
3. In OBS, add a **"Browser" (Browser Source)** source and paste that address. This version of the page has a transparent background, ready to overlay the game capture.
4. (Optional) **Turn off** the **"Show translation on screen"** switch to remove the overlay from the game and have the translation show **only** in the browser/OBS page — useful if the OBS capture already includes the overlay window and you do not want to see the translation twice. Keep it **on** if you want the translation in both places.

<p align="center"><img src="media/overlay-web.png" alt="Overlay › Web tab" width="820"></p>

You can also customize the theme (light/dark/dracula), colors, font size, and whether to show the original text along with the translation, the time and which service was used. Open pages change right away.

<p align="center"><img src="media/overlay-web-aparencia.png" alt="Overlay › Web tab — page appearance" width="820"></p>

The page can also be opened in any browser on the local network (phone, second monitor, etc.) using the **Capture** address (`/captura`) shown in the tab — that version comes with history and a clear button.

> If the translation disappears from your recordings and streams, there are two possible causes. One is automatic: Subtitle Mode with *Stick to the detected text* on draws **over** the original text, and then the overlay must be invisible to captures, otherwise the OCR would read its own translation. The other is your choice: *"Hide the translation from recordings and streams"*, in the **Display** card of Overlay › Capture. For screen capture, those are exactly the cases the Web server solves.

---

## 11. History and performance

- **History tab**: shows the screen capture translations made in the current session (original text, translation, time and service used). Click an entry to copy the translation; there is also a button to clear everything. Closing the program clears the history.
- **Debug › Monitor**: turns on a log of the last 10 screen captures with how long each step took (capture, recognition, translation, total) — useful to see what is making translation slow. The **Cache** column shows how many blocks were resolved without calling the API, and **API**, how many calls were actually made.

<p align="center"><img src="media/historico.png" alt="History tab" width="820"></p>

<p align="center"><img src="media/debug-monitor.png" alt="Debug › Monitor tab" width="820"></p>

---

## 12. Common problems and solutions

##### "Error opening the program: VCRUNTIME140.dll was not found" (or MSVCP140.dll)
→ Your Windows is missing the **Microsoft Visual C++ Redistributable** — a free Microsoft component some freshly formatted PCs do not have yet. Download and install the **x64** package from this official link: <https://aka.ms/vs/17/release/vc_redist.x64.exe> — then reopen Ranmza GT, and it opens normally.

##### "Ranmza GT is already running."
→ The program opens only once, so the shortcuts do not clash. Close the other Ranmza GT window — including an old version, if it is open — and open it again.

##### "Recognition does not detect anything" / language warning
→ With **WinOCR**, go to **General › Language** and check that a language is chosen and that its pack is installed in Windows. **OneOCR** does not use Windows language packs and reads any language without installing anything — another reason to switch engines in **General › OCR**.

##### "I chose OneOCR and the card says *Did not load*"
→ The *"OCR failed to load"* alert also shows. The OneOCR files have not been copied yet. Click **Detect and copy**, in the OneOCR card in **General › OCR**. On Windows 10, follow the step by step in the same card. While OneOCR does not load, the OCR stays stopped.

##### "The guide does not let me past the Languages step"
→ With WinOCR, the text language is required: pick one from the list. If the list is empty, Windows has no language pack with text recognition; install the pack for the game language, or go back to the OCR step and pick OneOCR.

##### "I pressed the shortcut and nothing happens"
→ Check that the settings window is not in the foreground (shortcuts only work with the game in focus). If the *"Capture: no area"* or *"Subtitles: no area"* alert shows up, mark the area first (`Numpad7` or `Numpad1`). If it still does not work, turn on the **floating toolbar** (**General › Shortcuts**) and use its buttons.

##### "Shortcuts don't work in some games (even with the game in focus)"
→ Some games run with elevated privileges (Administrator) and therefore **block the registration of Ranmza GT's global shortcuts**. In that case, **run Ranmza GT as Administrator** (right-click the `.exe` → *Run as administrator*) — that way it can enable the shortcuts over the game. To avoid repeating it every time, check *Run this program as an administrator* in the executable's **Properties → Compatibility**. (Alternative: use the **floating toolbar**, which triggers actions by mouse click and does not depend on keyboard shortcuts.)

##### "The translation does not show up, or takes too long"
→ Check the **History** and **Debug › Monitor** tabs to see if the translation is being made. Temporary failures (server down for a moment, connection drop) are **retried automatically** before falling back to Google Translate. If you have **more than one key** registered for the service and the problem is with the key (rejected, out of credit or at the request limit), it switches right away to the next key in the list. If the *"<service> failed, using Google"* alert shows — and the History marks the translation as *Google (fallback)* —, the configured service failed on **all** keys; check your API keys and credits in Translation › Translators. The service in the settings does not change: the next translation tries it again.

##### "Google: rate limited (429)"
→ Google Translate here is the **free service, without an API key** — and a free service limits how many translations it accepts in a short window. When you hit that limit, the warning shows and the translation of that capture does not come out.

What makes you hit the limit faster than it seems: **Subtitle Mode** sends a translation for every new line, and a screen capture with many separate blocks turns into many texts at once.

And here there is a difference worth knowing: when a service with a key fails, the program falls back to Google Translate. **Google has nowhere to fall back to** — it already is the last resort.

###### Why your limit seems smaller than your neighbor's: CGNAT

The limit is not per program or per account: it is counted **per IP address** — the number that identifies your connection on the internet. Everything that leaves your home reaches Google with that same number, and that is what Google uses to count how many translations you asked for.

The problem is that many people today **share the same IP with strangers**. There are not enough public IPs for everyone, so many providers (budget fiber, radio and especially 4G/5G mobile internet) use a technique called **CGNAT**: hundreds of customers go out to the internet through a single public IP. It is like a big building with only one street number — all the letters arrive at the front desk and someone distributes them inside. Seen from outside, you and your neighbors look like one person.

For Google, then, that IP's limit is spent by everyone together. If someone sharing your IP has been using Google services, part of the quota was gone before you opened the game — and the warning shows up much sooner than it would for someone with a **public IP of their own**. It is not a defect of the program or your computer, and there is no internal setting that fixes it.

**How to know if you are behind CGNAT:** compare the IP shown on your router's status page (the WAN IP) with what a "what is my IP" site shows. If they are different, it is CGNAT — and the router's usually starts with something between **100.64** and **100.127**, a range reserved precisely for this. Some providers give a public IP on request, sometimes for an extra fee.

What fixes it, from simplest to most definitive:

- **Wait a few minutes.** The limit is temporary and lifts by itself.
- **Use Paragraph mode** (`Numpad8`) instead of Line mode (`Numpad9`). Paragraph joins the lines of the same speech into one block — fewer blocks, same screen translated.
- **Switch services** in **Translation › Translators**. **Google Cloud**, **DeepL**, **Azure**, **Gemini** and **Groq** have a free plan: they require creating an API key, but in return you get your own, much roomier limit. If you are behind CGNAT, it is the fix that really works: the limit is counted by **your key**, not by the IP.

##### "A red error alert showed up"
→ It usually means an invalid API key, credits used up, or the service temporarily down. Check **Translation › Translators** and the **Debug › Logs** tab.

##### "On Azure, the key looks invalid — but the key is correct"
→ Check the **Resource region** in **Translation › Translators**. Azure answers the **same error** for an invalid key and for a wrong or missing region, so a wrong region looks like a key problem. Copy the region from the *Keys and Endpoint* page of your resource in the Azure portal — you can paste it as it appears there ("Brazil South"), and the program fixes spaces and capitals by itself.

##### "The AI translated something wrong, and the same wrong translation always comes back"
→ The program saves every translation and reuses it when the same text shows up again. With the text on screen, press **`Numpad4` (Retranslate)**: it translates again without looking at what is saved and replaces the old translation with the new one. If the new translation is also bad, try **Vision** (`Numpad5` or `Numpad6`), which sends the image to the AI.

##### "The recognized text is wrong/incomplete"
→ The fix that helps the most is switching the OCR engine to **OneOCR** in **General › OCR** — it reads game fonts much better than WinOCR (the step by step and the why are in [section 6](/en/Manual/configuring-translation.md), in *Switching OCR engine*). In Subtitle Mode, also check that the area is tight around the subtitle and the **alphabet filter**. In screen capture, use **Translate with AI Vision** (`Numpad5` paragraph, `Numpad6` line) to let the AI "see" the image and fix it.

##### "The translation does not fit where the original text was"
→ In screen capture, check that **Auto-fit** is on in **Overlay › Capture** — the program shrinks the font until it fits.
→ In **Subtitle Mode** with *Stick to the detected text* on, the translation spills over the area on purpose. Lower the *Font size* in **Overlay › Subtitles** if it covers what it should not.

##### "Translations of different lines are getting mixed into one block" (or the opposite)
→ First check that you pressed the right shortcut: `Numpad8` joins the lines (paragraph) and `Numpad9` splits them (line). If the mode is right and it still gets it wrong, adjust the **Grouping sensitivity** in **Overlay › Capture** — it only affects Paragraph mode.

##### "I switched monitors and the areas disappeared"
→ Each monitor keeps its own areas. The first time you use a monitor, it has no area at all: mark them again (`Numpad7` and `Numpad1`). When you go back to the previous monitor, its areas come back by themselves.

##### "I want to share my logs with support, but I don't want to show the game content"
→ Check in **Debug › Logs** that the "Log captured text and translations" option is **off** (the default) — that way the logs do not show the content of texts and translations, and API keys never show up in them.

---

## 13. Complete reference — all tabs

This section describes **every tab and every option** of the settings window, in the order they appear in the left menu. It is reference material — for day-to-day use, the previous sections are enough.

The menu has five groups with sub-items (**General**, **Overlay**, **Translation**, **Tools**, **Debug**) and two standalone items at the bottom (**History** and **About**).

### General › Config

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

### General › Profiles

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

### General › Language

The source language field **adapts to the OCR engine** chosen in General › OCR.

<p align="center"><img src="media/geral-idioma.png" alt="General › Language tab" width="820"></p>

- **Source text language**
  - With *WinOCR* — list of the languages with a text recognition pack installed in Windows, with no default option: pick the game language. With no choice, a warning shows up. If the saved language is no longer installed, the **Install language pack** button shows up and opens the Windows language screen.
  - With *OneOCR* — **automatic detection**; there is no source language to set.
- **Target language** — which language to translate into: Português (Brasil), Português (Portugal), Español, English, Français, Deutsch, Italiano, 日本語, 한국어, 中文（简体）and Русский.

### General › OCR

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

### General › Shortcuts

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

### Overlay › Capture

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
  - *Auto-fit* — shrinks the font until the text fits where the original was. **On by default.**
- **Background and Outline** — can be on together or separately.
  - *Show background* + *Background opacity* (10–100%) — dark box behind the text.
  - *Show outline* + *Thickness* (0.5–5 px) + *Outline color* — outline around each letter.
- **Paragraph Mode Fine-Tuning → Grouping sensitivity** (0.5–3.0) — lower values separate paragraphs more easily; higher values join more distant lines into one block. The mode itself (paragraph or line) **is not chosen here**: it is decided at capture time, by the shortcut — `Numpad8` (paragraph) or `Numpad9` (line).

### Overlay › Subtitles

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

### Overlay › Web

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

### Translation › Translators

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

### Translation › AI

Context sent to the AIs.

<p align="center"><img src="media/ia.png" alt="Translation › AI tab" width="820"></p>

- **Conversation Context → Previous lines** (5–10, default 5) — in Subtitle Mode, sends the last lines (original + translation) as context, so the AI keeps terms and tone consistent. Each extra line costs tokens on every translation. With DeepL, only the originals go, at no cost.
- **System Prompt** — general translator rules, for every game. It comes **blank**, with a gray example inside the field; nothing is sent to the AI until you write your own. **Save** and **Restore default** buttons (which empties the field again). The target language does not need to be here: the program already sends the AI the language chosen in the **Language** tab, and asking for another language in this field is ignored. Concrete rules (glossary, keep names, do not soften swearing) work on every model.
- **Game Info** — theme, characters and glossary; change it for each game. It also comes blank, with a gray example. Same buttons. With DeepL, the text goes as context: it helps with tone and terms, but requests written here are not followed.

> With Google Translate, Google Cloud or Azure active, the cards are marked in red, because they do not apply to them. With DeepL, only the System Prompt is marked.

The general reset (General › Config) does **not** erase the Game Info.

### Tools › Inpaint

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

#### Automatic download

<p align="center"><img src="media/ferramentas-inpaint-baixar.png" alt="Automatic download card, in Tools › Inpaint" width="820"></p>

The feature needs the MI-GAN model (27 MB), which does not come in the program `.zip`. The **Download automatically** card downloads and checks the model:

- *Model folder* — empty, it uses the `models\inpaint` folder, next to the executable. **Browse...** picks another one.
- *Download* — the bar shows the progress and the button turns into **Cancel**. Canceled or interrupted, the download starts over next time.

The program checks the file's **sha256** before accepting it. A file that arrives corrupted or different from the expected one is deleted and the download fails with a warning — a half file never passes as a good one.

> Tip: turn on the **Outline** in the Overlay › Capture tab, because the reconstructed background may be too light for white text.

### Debug › Monitor

Time of each screen capture step.

<p align="center"><img src="media/debug-monitor.png" alt="Debug › Monitor tab" width="820"></p>

- **Monitoring → Active** — records the time of each step on every screen capture key press. The history is kept when navigating between tabs.
- **Run History** — table of the last 10 captures: Time, Capture, OCR, Translation, Total, Blocks, Cache (hits without calling the API) and API (calls actually made).
- **Statistics** — minimum, average and maximum of each step.

### Debug › Logs

Log of this run, in real time.

<p align="center"><img src="media/debug-logs.png" alt="Debug › Logs tab" width="820"></p>

- **Log captured text and translations** — privacy switch, **off by default**. Keep it off when sending a log to support, so you do not expose the game content. API keys never go to the log.
- **Filter lines** · **Auto-scroll** · **Refresh** — viewing controls; errors come out in red, warnings in yellow.

Each run writes a file in `logs\`, next to the executable, and the program keeps the 20 most recent. That is the file support will ask for.

### History

<p align="center"><img src="media/historico.png" alt="History tab" width="820"></p>

Lists the screen capture translations of the **current session** — time, service, translation and, below, the original text. Click an entry to copy the translation. **Clear history** button.

### About

Program information: icon, name and installed **version**, the author, the project and support links, and the full **Terms of Use** — what is allowed (free personal use, distributing unmodified copies, creating content like videos and streams) and what is forbidden (modifying or reverse engineering, selling, redistributing modified versions, commercial use without permission, removing credits), plus the warranty disclaimer.

---

## 14. Updating the program

When opening the program, if a newer version is published, a warning shows the version you have and the one that came out. The **Download** button opens the new version's page in your browser — that is where the news of that version and the `.zip` file are.

**The program does not download or install anything by itself.** It only warns you; downloading and replacing the files are done by you, the same way as the first install. This is on purpose: a program that replaces its own executable is exactly the behavior Windows Defender blocks, and it is not worth the risk of the whole program not opening anymore.

**How to update**, after downloading the `.zip`: close Ranmza GT, extract the contents over the current folder and confirm replacing the files. Your settings (`config.json`), the profiles (`profiles\`), the API keys, the fonts you put in `fonts/` and the files in `models/` (OneOCR and MI-GAN) **are not in the `.zip`** and stay where they are.

> API keys are encrypted for this PC and this Windows account. If you copy the settings to another PC, type the keys again there.

To turn off the warning, check **Don't notify me about new versions** in the warning itself, or turn it off in **General › Config → Updates**. That switch is how it comes back.

Even with the warning off, the **Check now** button, in the same card, checks right away whether a new version came out — it is the way to take a look now and then without being warned every time.

> The program checks the releases page at most once every 6 hours, even if you open and close it several times a day — the warning keeps showing on every opening, because it uses the last saved answer. The *Check now* button ignores that interval. If you are offline, nothing happens: no error shows and the program opens normally.
