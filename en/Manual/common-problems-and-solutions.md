# 13. Common problems and solutions

**"Error opening program: VCRUNTIME140.dll not found" (or MSVCP140.dll)**
→ Your Windows is missing **Microsoft Visual C++ Redistributable** — a free Microsoft component some freshly-formatted PCs don't have. Download and install the **x64** package from this official link: <https://aka.ms/vs/17/release/vc_redist.x64.exe> — then reopen Ranmza GT, it should open normally.

**"Recognition detects nothing" / red warning about language**
→ Go to **General › Language** and click the warning to install the necessary Windows language package.

**"I pressed the hotkey and nothing happened"**
→ Check if the settings window isn't in the foreground (hotkeys only work with the game in focus). If still nothing, enable the **floating toolbar** (**General › Config**) and use its buttons.

**"Hotkeys don't work in some games (even with game in focus)"**
→ Some games run with elevated privileges (Administrator) and therefore **block Ranmza GT's global hotkey registration**. In that case, **run Ranmza GT as Administrator** (right-click the `.exe` → *Run as administrator*) — then it can activate hotkeys over the game. To avoid repeating every time, check *Run this program as an administrator* in **Properties → Compatibility** of the executable. (Alternative: use the **floating toolbar**, which fires actions by mouse click and doesn't depend on keyboard hotkeys.)

**"Translation doesn't appear, or it's slow"**
→ Check the **History** and **Debug › Monitor** tabs to see if translation is being done. Transient failures (rate limit, server briefly down, connection drop) are **automatically retried** once before falling back to Google Translate. If you have **more than one key** registered for the engine, it still tries the other keys in the list before the fallback. If a yellow "fallback to Google Translate" warning appears — and in History the translation is marked "Google Translate (fallback)" —, the configured service (OpenAI, Claude, Gemini) failed on **every** key; check your API keys and credits in Translation › Translators.

**"A red error warning appeared"**
→ Usually means invalid API key, exhausted credits, or the service temporarily down. Check **Translation › Translators**. If the warning says the response was **cut off at the token limit**, increase **Max tokens** in **Translation › AI** (happens only with very large text blocks).

**"Recognized text is wrong/incomplete"**
→ Try enabling preprocessing (**Overlay › Capture**) with upscale and contrast adjustments, or use **Translate with AI Vision** (`Numpad5` paragraph, `Numpad6` line) to let the AI "see" the image and correct it.

**"Translation is cut off or doesn't fit in the box"**
→ For manual translation (`Numpad8`/`Numpad9`), enable **Auto-fit** in **Overlay › Capture** — the program will automatically shrink the font until it fits.
→ In **Subtitle Mode** with *Replace the original subtitle in place* on there is no auto-fit: the translation has to fit the area you marked. Lower the *Font size* in **Overlay › Subtitles**, or redo the area selection a bit taller than the game's subtitle.

**"Translations of different lines are mixing into one block (or the opposite)"**
→ First check you pressed the right hotkey: `Numpad8` merges lines (paragraph) and `Numpad9` keeps them apart (line). If the mode is right and it still gets it wrong, adjust **Grouping sensitivity** in **General › OCR** — it only affects Paragraph Mode.

**"I switched monitors and capture isn't working right anymore"**
→ Restart the program via the button in **General › Config** — it's necessary after switching monitors.

**"I want to share my logs for support, but don't want to show game content"**
→ Check **Debug › Logs** if the option "Log captured texts and translations" is **disabled** (it's the default) — this way logs don't show text/translation content.

---
