## 2. Quick setup — ready to use in 5 minutes

**Five settings.** After them you're already translating; everything else in this manual is fine-tuning, to be read when (and if) you need it.

| Step | What to do | Where |
|---|---|---|
| 1 | Pick your monitor | **Geral › Config** tab |
| 2 | Pick your languages | **Geral › Idioma** tab |
| 3 | Pick your translator | **Traducao › Tradutores** tab |
| 4 | Mark the text area | `Numpad7` hotkey, with the game open |
| 5 | Translate | `Numpad9` (line) or `Numpad8` (paragraph) hotkey |

> **Before anything else: run the game in Windowed mode.** In *Exclusive Fullscreen* no program can draw on top — the translation simply won't appear. Switch the game to **Borderless Fullscreen** in its video options. Full explanation in [section 1](/en/Manual/what-the-program-does.md).

> **Program won't even open, with the error *"VCRUNTIME140.dll not found"*?** The **Microsoft Visual C++ Redistributable (x64)** is missing — a free component from Microsoft that most PCs already have (it ships with many games), but is often absent on a freshly formatted Windows. Install it from this official link and open the program again: <https://aka.ms/vs/17/release/vc_redist.x64.exe>

### 2.1 First look: how the window is organized

<p align="center"><img src="media/geral-config.png" alt="Geral › Config tab" width="820"></p>

The left-hand menu groups options by subject. For this quick setup you only touch **Geral** and **Traducao** — the rest is there for when you want to fine-tune something.

| Menu | What's inside |
|---|---|
| **Geral** | Config (monitor, theme, floating bar), Idioma, OCR and Atalhos |
| **Overlay** | How the translation looks on screen: Captura, Legenda and Web |
| **Traducao** | Tradutores (engine and API keys) and I.A (prompts and parameters) |
| **Ferramentas** | Inpaint (erase the original text) and Lab (test preprocessing) |
| **Debug** | Performance monitor, diagnostic images and Logs |
| **Historico** | Translations from the current session |
| **Experimental** | Features under development, such as Real-time Mode |
| **Sobre** | Program version and links |

> **Interface language** (in *Geral › Config*) only changes the language **of the program** — the menus and labels you're looking at. It has nothing to do with the language being translated; that's step 2.3.

### 2.2 Pick your monitor

Still in **Geral › Config**, in the **Monitor** card, choose in **Tela ativa** which screen the program should work on. With a single monitor, leave it on *Automatico* and move on.

Switching monitors **requires restarting the program** — a notice with a **Reiniciar agora** button appears at the bottom of the tab. Only after the restart do capture, the area selector and the on-screen translation move to the other screen. Any area you had already selected is cleared by the switch.

The **Backend de captura** just above can stay on *Auto (recomendado)*: it picks the right method for your Windows version by itself, and switches on the fly with no restart.

### 2.3 Pick your languages

Open **Geral › Idioma**.

<p align="center"><img src="media/geral-idioma.png" alt="Geral › Idioma tab" width="820"></p>

- **Idioma do texto** — the language written in the game. Type the language code (`en` for English, `ja` for Japanese, `ko` for Korean, `zh` for Chinese…).
- **Idioma destino** — the language you want to read in. `en` for English.

> **Yellow warning about a language pack?** Windows OCR only recognizes languages whose pack is installed in Windows. Install it under *Settings → Time & Language → Language & region*. Without the pack, the program can't read text in that language.

> **Using OneOCR?** Then there's no source language to pick: it's a single multilingual model (Latin, CJK, Cyrillic…) that detects the language on its own, and the **Idioma do texto** field doesn't even show while it's selected — nor does the Windows pack warning, which doesn't apply. **Idioma destino** works normally. The OCR engine is switched in *Geral › OCR*, but leave it on the default to get started.

### 2.4 Pick your translator

Open **Traducao › Tradutores**.

<p align="center"><img src="media/tradutores-google.png" alt="Traducao › Tradutores tab with Google Translate" width="820"></p>

The default is **Google Translate — free, no key**: nothing to configure, it's ready to use. Do your first test with it.

When you want better quality, switch in **Provedor ativo**:

- **DeepL** — a dedicated translator, very natural, with a formality option. Requires an API key, but has a **free plan** (those keys end in `:fx`, and the program figures out which server to use by itself).
- **OpenAI**, **Anthropic (Claude)** or **Gemini** — AI engines. They need an API key with credits, and in return deliver far more natural and consistent translations, especially in long dialogue. Pick the model under *Autenticação* and paste the key under *Chaves de API*.

Each engine stores its own credentials, so switching away and back doesn't erase anything. Use the **Testar conexao** button to confirm the key is valid before jumping into the game.

> **Multiple keys with automatic rotation.** Every engine with a key accepts **more than one**: click *+ Adicionar chave*. If the key in use runs out of credit or hits the request limit, the program moves to the next one in the list by itself; once all are exhausted, it falls back to Google Translate. Very handy in long Caption Mode sessions.

> Only the AI engines (OpenAI, Claude, Gemini) support **Vision Mode** — Google Translate and DeepL don't. See [section 7](/en/Manual/vision-mode-when-ocr-fails.md).

### 2.5 Mark the text area

With the game open and focused, press **`Numpad7`**. The screen dims and you drag the mouse to draw a rectangle over the region where the text appears — usually the dialogue box. Release the button to confirm, or press `ESC` to cancel.

The area is saved. You only need to mark it again if the game moves its text box or if you change resolution.

> Didn't mark any area? The program captures the **whole screen** — it works, but it's slower and less accurate. Marking is worth it.

### 2.6 Translate

With text on screen, press one of the two translation hotkeys — the only difference is **how lines are grouped** before translating:

| Hotkey | Mode | Use it for |
|---|---|---|
| **`Numpad9`** | **Line** | Menus, lists, items, buttons — each line is its own thing |
| **`Numpad8`** | **Paragraph** | Dialogue and running text — merges nearby lines into a single block |

When in doubt, start with `Numpad8` in story games and `Numpad9` in menus.

The translation appears over the game, in the position of the original text, and disappears on its own after a while. To clear it right away, press **`NumpadDecimal`** (the numpad's decimal point).

> **Hotkeys only work with the game focused.** With the Ranmza GT settings window in the foreground they're disabled on purpose — that way you can type into fields without firing off commands. Click back into the game before testing.

### Did it work? And if it didn't

If the translation showed up over the game, you're all set — move on to [section 3](/en/Manual/basic-day-to-day-usage.md).

- **Nothing happened when you pressed the hotkey** → the settings window was focused, or the game is swallowing the numpad keys. Enable the **floating bar** in *Geral › Config* and use the buttons with your mouse (see [section 3](/en/Manual/basic-day-to-day-usage.md)).
- **The translation shows in the Historico tab, but not over the game** → the game is in *Exclusive Fullscreen*. Switch it to *Borderless Fullscreen*.
- **The translation came out wrong or scrambled** → the OCR misread it. Start by switching the grouping mode (`Numpad9` ↔ `Numpad8`) and see [section 5](/en/Manual/configuring-translation.md).

Other problems are covered in [section 12](/en/Manual/common-problems-and-solutions.md).

---
