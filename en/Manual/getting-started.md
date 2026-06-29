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
