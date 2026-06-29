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
