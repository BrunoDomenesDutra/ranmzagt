# 2. Quick setup

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

## 2.1 The Setup guide

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

## 2.2 First look: how the window is organized

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

## 2.3 Pick your monitor

In **General › Config**, in the **Monitor** card, choose under **Active display** where the game is. With a single monitor, leave it on *Automatic* and move on.

The chosen monitor is where area selection, alerts, the area preview and the floating toolbar open, until you drag the toolbar elsewhere. The translation shows up on the monitor where the area was marked.

- **The change applies right away**, no restart.
- **Each monitor keeps its own areas.** When you switch monitors, the areas of the previous monitor are kept; when you switch back, they come back. The first time you use a monitor, mark the areas on it.
- **Each profile keeps its own monitor.** With one profile per game, each game comes back on its monitor.
- If the chosen monitor is disconnected, the program uses the Windows primary one.

The **Capture backend** just above can stay on *Auto (recommended)*: it picks the right method for your Windows version by itself and switches right away, no restart.

## 2.4 Pick your languages

Open **General › Language**.

<p align="center"><img src="media/geral-idioma.png" alt="General › Language tab" width="820"></p>

- **Text language** — the language the game is in. With WinOCR, the list only shows the languages that already have the text recognition pack installed in Windows. On a new install the field comes empty, with a warning: pick one from the list.
- **Target language** — the language you want to read.

> **The game language is not on the list?** WinOCR only reads languages whose pack is installed in Windows. Install it in *Settings → Time & Language → Language & region* and open the program again. If Windows has no pack with text recognition at all, the warning has an **Install language pack** button that opens that screen.

> **Using OneOCR?** Then there is no source language to choose: it is a single multilingual model (Latin, Japanese, Chinese, Korean, Cyrillic…) that detects the language by itself, and the **Text language** field does not even show while it is selected. The **Target language** still applies normally. OneOCR is the **recommended** engine and is chosen in *General › OCR* — see *Switching OCR engine* in [section 6](/en/Manual/configuring-translation.md).

## 2.5 Pick your translator

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

## 2.6 Mark the text area

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

## 2.7 Translate

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

## 2.8 Plan B: the floating bar

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

## 2.9 Changing the hotkeys

If the default keys do not suit you — keyboard without a numpad, conflict with the game controls — change them in **General › Shortcuts**.

<p align="center"><img src="media/geral-atalhos.png" alt="General › Shortcuts tab" width="820"></p>

Each action has a main key, chosen in the list on the right, and three modifier buttons (Ctrl, Alt and Shift) you turn on if you want to combine them. The change applies right away, no restart.

> **A letter or number as the main key requires a modifier** (Ctrl, Alt or Shift), otherwise you would trigger the program every time you type in the game. Numpad keys, F1–F12 and the navigation keys work on their own.

## Did it work? And if it didn't

If the translation showed up over the game, everything is ready — go on to [section 3](/en/Manual/basic-day-to-day-usage.md).

- **Nothing happened when pressing the shortcut** → the settings window was in focus, or the game is "swallowing" the Numpad keys. Use the **floating toolbar** (step 2.8) or change the key (step 2.9).
- **The translation shows up in the History tab, but not over the game** → the game is in *Exclusive Fullscreen*. Switch to *Borderless Window*.
- **The translation came out wrong or scrambled** → the OCR misread. Start by switching the grouping mode (`Numpad9` ↔ `Numpad8`) and see [section 6](/en/Manual/configuring-translation.md).

Other problems are in [section 12](/en/Manual/common-problems-and-solutions.md).

---
