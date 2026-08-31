# 2. Quick setup

**Five settings.** After them you're already translating; everything else in this manual is fine-tuning, to be read when (and if) you need it.

| Step | What to do | Where |
|---|---|---|
| 1 | Pick your monitor | **General › Config** tab |
| 2 | Pick your languages | **General › Language** tab |
| 3 | Pick your translator | **Translation › Translators** tab |
| 4 | Mark the text area | `Numpad7` hotkey, with the game open |
| 5 | Translate | `Numpad9` (line) or `Numpad8` (paragraph) hotkey |

> **Before anything else: run the game in Windowed mode.** In *Exclusive Fullscreen* no program can draw on top — the translation simply won't appear. Switch the game to **Borderless Fullscreen** in its video options. Full explanation in [section 1](/en/Manual/what-the-program-does.md).

> **Program won't even open, with the error *"VCRUNTIME140.dll not found"*?** The **Microsoft Visual C++ Redistributable (x64)** is missing — a free component from Microsoft that most PCs already have (it ships with many games). Install it from this official link and open the program again: <https://aka.ms/vs/17/release/vc_redist.x64.exe>

## 2.1 First look: how the window is organized

<p align="center"><img src="media/geral-config.png" alt="General › Config tab" width="820"></p>

The left-hand menu groups options by subject. For this quick setup you only touch **General** and **Translation** — the rest is there for when you want to fine-tune something.

| Menu | What's inside |
|---|---|
| **General** | Config (monitor, theme, floating toolbar), Profiles, Language, OCR and Shortcuts |
| **Overlay** | How the translation looks on screen: Capture, Subtitles and Web |
| **Translation** | Translators (engine and API keys) and AI (prompts and parameters) |
| **Tools** | Inpaint (erase the original text) and Lab (test preprocessing) |
| **Debug** | Performance monitor, diagnostic images and Logs |
| **History** | Translations from the current session |
| **Experimental** | Features under development, such as Real-time Mode |
| **About** | Program version and links |

> **Interface language** (in *General › Config*) only changes the language **of the program** — the menus and labels you're looking at. It has nothing to do with the language being translated; that's step 2.3.

## 2.2 Pick your monitor

Still in **General › Config**, in the **Monitor** card, choose in **Active display** which screen the program should work on. With a single monitor, leave it on *Automatic* and move on.

Switching monitors **requires restarting the program** — a notice with a **Restart now** button appears at the bottom of the tab. Only after the restart do capture, the area selector and the on-screen translation move to the other screen. Any area you had already selected is cleared by the switch.

The **Capture backend** just above can stay on *Auto (recommended)*: it picks the right method for your Windows version by itself, and switches on the fly with no restart.

## 2.3 Pick your languages

Open **General › Language**.

<p align="center"><img src="media/geral-idioma.png" alt="General › Language tab" width="820"></p>

- **Text language** — the language written in the game. Type the language code (`en` for English, `ja` for Japanese, `ko` for Korean, `zh` for Chinese…).
- **Target language** — the language you want to read in. `en` for English.

> **Yellow warning about a language pack?** Windows OCR only recognizes languages whose pack is installed in Windows. Install it under *Settings → Time & Language → Language & region*. Without the pack, the program can't read text in that language.

> **Using OneOCR?** Then there's no source language to pick: it's a single multilingual model (Latin, CJK, Cyrillic…) that detects the language on its own, and the **Text language** field doesn't even show while it's selected — nor does the Windows pack warning, which doesn't apply. **Target language** works normally. The OCR engine is switched in *General › OCR*, but leave it on the default to get started.

## 2.4 Pick your translator

Open **Translation › Translators**.

<p align="center"><img src="media/tradutores-google.png" alt="Translation › Translators tab with Google Translate" width="820"></p>

The default is **Google Translate — free, no key**: nothing to configure, it's ready to use. Do your first test with it.

> **Free, but capped.** Google Translate with no key only accepts a handful of translations in a short window. Go past that and a *"Rate limit reached"* warning appears, leaving that capture untranslated. For the odd line here and there it's fine; in a long session or in the continuous modes (Subtitle and Real-time) you reach the cap quickly. And the cap is counted **per IP address** — if you're on mobile internet or an ISP that uses **CGNAT**, you share that cap with other customers and hit it much sooner. The explanation and what to do about it are in [section 13](/en/Manual/common-problems-and-solutions.md).
>
> On top of that, it **isn't an official API**: it's the same address the Google Translate web page uses under the hood, with no key and no account. Google can change it or take it down whenever it likes, without notice. Engines with a key don't carry that risk.

When you want better quality, switch in **Active provider**:

- **DeepL** — a dedicated translator, very natural, with a formality option. Requires an API key, but has a **free plan** (those keys end in `:fx`, and the program figures out which server to use by itself).
- **Azure Translator** — Microsoft's translator, dedicated as well. On top of the API key it requires the resource **region** (both live on the same page of the Azure portal). It detects the source language **block by block**, which helps when a capture mixes languages.
- **OpenAI**, **Anthropic (Claude)** or **Gemini** — AI engines. They need an API key with credits, and in return deliver far more natural and consistent translations, especially in long dialogue. Pick the model under *Authentication* and paste the key under *API Keys*.

Each engine stores its own credentials, so switching away and back doesn't erase anything. Use the **Test connection** button to confirm the key is valid before jumping into the game.

> **Multiple keys with automatic rotation.** Every engine with a key accepts **more than one**: click *+ Add key*. If the key in use runs out of credit or hits the request limit, the program moves to the next one in the list by itself; once all are exhausted, it falls back to Google Translate. Very handy in long Subtitle Mode sessions.

> Only the AI engines (OpenAI, Claude, Gemini) support **Vision Mode** — Google Translate, DeepL and Azure Translator don't. See [section 8](/en/Manual/vision-mode-when-ocr-fails.md).

## 2.5 Mark the text area

With the game open and focused, press **`Numpad7`**. The screen dims and you drag the mouse to draw a rectangle over the region where the text appears — usually the dialogue box. Release the button to confirm, or press `ESC` to cancel.

The area is saved. You only need to mark it again if the game moves its text box or if you change resolution.

> Didn't mark any area? The program captures the **whole screen** — it works, but it's slower and less accurate. Marking is worth it.

<div style="position:relative;padding-top:56.25%;max-width:820px;margin:0 auto">
  <iframe src="https://player.vimeo.com/video/1218016540"
          style="position:absolute;top:0;left:0;width:100%;height:100%;border:0"
          allow="fullscreen; picture-in-picture" allowfullscreen
          title="Marking the text area"></iframe>
</div>

<p align="center"><i>Marking the text area with `Numpad7`.</i></p>

## 2.6 Translate

With text on screen, press one of the two translation hotkeys — the only difference is **how lines are grouped** before translating:

| Hotkey | Mode | Use it for |
|---|---|---|
| **`Numpad9`** | **Line** | Menus, lists, items, buttons — each line is its own thing |
| **`Numpad8`** | **Paragraph** | Dialogue and running text — merges nearby lines into a single block |

When in doubt, start with `Numpad8` in story games and `Numpad9` in menus.

The translation appears over the game, in the position of the original text, and disappears on its own after a while. To clear it right away, press **`NumpadDecimal`** (the numpad's decimal point).

<div style="position:relative;padding-top:56.25%;max-width:820px;margin:0 auto">
  <iframe src="https://player.vimeo.com/video/1217778050"
          style="position:absolute;top:0;left:0;width:100%;height:100%;border:0"
          allow="fullscreen; picture-in-picture" allowfullscreen
          title="Selecting the area and translating"></iframe>
</div>

<p align="center"><i>Selecting the area and translating — in line and paragraph modes.</i></p>

> **Hotkeys only work with the game focused.** With the Ranmza GT settings window in the foreground they're disabled on purpose — that way you can type into fields without firing off commands. Click back into the game before testing.

## 2.7 Plan B: the floating bar

Some games swallow the numpad keys, and NumLock sometimes gets in the way. For those cases, turn on **Show floating toolbar** in *General › Config*: a small window with the same commands as buttons, fired with the mouse.

<p align="center"><img src="media/barra-flutuante.png" alt="Ranmza GT floating bar" width="560"></p>

It stays **on top of everything** — including a game in borderless fullscreen — and you drag it by the dotted handle on the left to any corner of any monitor. The `NumpadSubtract` hotkey (the numpad's minus) shows and hides the bar.

The buttons, left to right (hover over one to see its name):

| Icon | What it does |
|---|---|
| Brackets (cyan) | Select capture area |
| Three lines (purple) | Translate (Paragraph) |
| Dash (purple) | Translate (Line) |
| Three lines (pink) | Translate with AI Vision (Paragraph) |
| Dash (pink) | Translate with AI Vision (Line) |
| X (red) | Clear overlay |
| Bubble (green) | Subtitle Mode — on/off |
| Rectangle (green) | Select subtitle area |
| Four dots (orange) | Show/hide areas |

## 2.8 Changing the hotkeys

If the default keys don't suit you — a keyboard with no numpad, a clash with the game's controls — change them in **General › Shortcuts**.

<p align="center"><img src="media/geral-atalhos.png" alt="General › Shortcuts tab" width="820"></p>

Each action has a main key, picked from the list on the right, plus three modifier buttons (Ctrl, Alt and Shift) you toggle if you want a combination.

> **A letter or number as the main key requires a modifier** (Ctrl, Alt or Shift) — otherwise you'd fire the program every time you typed in the game. Numpad keys, F1–F12 and the navigation keys work on their own.

The **Real-time Mode** keys aren't here: being experimental, they live in the **Experimental** tab, and come with no key assigned. See [section 10](/en/Manual/real-time-mode-continuous-translation-in-place-experimental.md).

## Did it work? And if it didn't

If the translation showed up over the game, you're all set — move on to [section 3](/en/Manual/basic-day-to-day-usage.md).

- **Nothing happened when you pressed the hotkey** → the settings window was focused, or the game is swallowing the numpad keys. Use the **floating bar** (step 2.7) or change the key (step 2.8).
- **The translation shows in the History tab, but not over the game** → the game is in *Exclusive Fullscreen*. Switch it to *Borderless Fullscreen*.
- **The translation came out wrong or scrambled** → the OCR misread it. Start by switching the grouping mode (`Numpad9` ↔ `Numpad8`) and see [section 6](/en/Manual/configuring-translation.md).

Other problems are covered in [section 13](/en/Manual/common-problems-and-solutions.md).

---
