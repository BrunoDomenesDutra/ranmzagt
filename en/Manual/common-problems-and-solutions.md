# 13. Common problems and solutions

#### "Error opening program: VCRUNTIME140.dll not found" (or MSVCP140.dll)
→ Your Windows is missing **Microsoft Visual C++ Redistributable** — a free Microsoft component some freshly-formatted PCs don't have. Download and install the **x64** package from this official link: <https://aka.ms/vs/17/release/vc_redist.x64.exe> — then reopen Ranmza GT, it should open normally.

#### "Recognition detects nothing" / red warning about language
→ Go to **General › Language** and click the warning to install the necessary Windows language package.

#### "I pressed the hotkey and nothing happened"
→ Check if the settings window isn't in the foreground (hotkeys only work with the game in focus). If still nothing, enable the **floating toolbar** (**General › Config**) and use its buttons.

#### "Hotkeys don't work in some games (even with game in focus)"
→ Some games run with elevated privileges (Administrator) and therefore **block Ranmza GT's global hotkey registration**. In that case, **run Ranmza GT as Administrator** (right-click the `.exe` → *Run as administrator*) — then it can activate hotkeys over the game. To avoid repeating every time, check *Run this program as an administrator* in **Properties → Compatibility** of the executable. (Alternative: use the **floating toolbar**, which fires actions by mouse click and doesn't depend on keyboard hotkeys.)

#### "Translation doesn't appear, or it's slow"
→ Check the **History** and **Debug › Monitor** tabs to see if translation is being done. Transient failures (rate limit, server briefly down, connection drop) are **automatically retried** once before falling back to Google Translate. If you have **more than one key** registered for the engine, it still tries the other keys in the list before the fallback. If a yellow "fallback to Google Translate" warning appears — and in History the translation is marked "Google Translate (fallback)" —, the configured service (DeepL, Azure or an AI engine) failed on **every** key; check your API keys and credits in Translation › Translators.

#### "Rate limit reached" using Google Translate
→ Google Translate here is the **free service, with no API key** — and a free service limits how many translations it accepts in a short window. When you hit that limit, the yellow warning appears and that capture isn't translated.

What makes you hit the limit sooner than you'd expect: the program sends **one request per text block** in the capture, all at the same time. A screen with many separate lines of dialogue becomes many requests at once. And the continuous modes (**Subtitle** and **Real-time**) repeat that on every cycle.

The program already retries once on its own, after a moment — the warning only appears when the second attempt fails too. And there's a difference worth knowing: when an engine with a key (DeepL, Azure, AI) fails, the program falls back to Google Translate. **Google has nothing to fall back to** — it is already the last resort.

##### Why your limit looks smaller than your neighbour's: CGNAT

The limit isn't per program or per account: it's counted **per IP address** — the number that identifies your connection on the internet. Everything that leaves your house reaches Google with that same number, and that's what Google uses to count how many translations you asked for.

The catch is that a lot of people today **share the same IP with strangers**. There aren't enough public IPs to go around, so many ISPs (budget fibre, fixed wireless and above all mobile 4G/5G) use a technique called **CGNAT**: hundreds of customers reach the internet through a single public IP. It's like a large building with only one street number — every letter arrives at the front desk and someone hands them out inside. Seen from outside, you and your neighbours look like one person.

So as far as Google is concerned, that IP's quota is spent by everyone together. If someone sharing your IP has been using Google services, part of the quota is gone before you even open the game — and the warning shows up far sooner than it would for someone with a **public IP of their own**. It isn't a fault in the program or in your computer, and no setting inside it can fix that.

**How to tell whether you're behind CGNAT:** compare the IP shown on your router's status page (the WAN IP) with the one a "what is my IP" site reports. If the two differ, it's CGNAT — and the router's one usually starts somewhere between **100.64** and **100.127**, a range reserved for exactly this. Some ISPs will give you a public IP on request, sometimes for an extra fee.

What fixes it, from simplest to most permanent:

- **Wait a few minutes.** The limit is temporary and clears on its own.
- **Use paragraph mode** (`Numpad8`) instead of line mode (`Numpad9`). Paragraph joins the lines of the same speech into a single block — fewer blocks, fewer requests, same screen translated.
- **In the continuous modes, raise the capture interval** in **Overlay › Subtitles**. Translating every half second costs far more than translating every two.
- **Switch engines** in **Translation › Translators**. **DeepL** and **Azure Translator** have free tiers: they require creating an API key, but in exchange you get your own, far more generous limit, and better translation quality. If you're behind CGNAT, this is the fix that actually works: the limit is then counted against **your key**, not against the IP, so what your ISP's other customers do stops affecting you.

#### "A red error warning appeared"
→ Usually means invalid API key, exhausted credits, or the service temporarily down. Check **Translation › Translators**. If the warning says the response was **cut off at the token limit**, increase **Max tokens** in **Translation › AI** (happens only with very large text blocks).

#### "On Azure the test says the key is invalid — but the key is right"
→ Check the **Resource region** in **Translation › Translators**. Azure returns the **same error** for an invalid key and for a wrong or missing region, so a mistyped region looks like a key problem. Copy the region from your resource's *Keys and Endpoint* page in the Azure portal — you can paste it exactly as shown there ("Brazil South"), the program strips the space and the capitals by itself. While the field is empty, the *Test connection* button stays disabled.

#### "Recognized text is wrong/incomplete"
→ Try enabling preprocessing (**Overlay › Capture**) with upscale and contrast adjustments, or use **Translate with AI Vision** (`Numpad5` paragraph, `Numpad6` line) to let the AI "see" the image and correct it.

#### "Translation is cut off or doesn't fit in the box"
→ For manual translation (`Numpad8`/`Numpad9`), enable **Auto-fit** in **Overlay › Capture** — the program will automatically shrink the font until it fits.
→ In **Subtitle Mode** with *Replace the original subtitle in place* on there is no auto-fit: the translation has to fit the area you marked. Lower the *Font size* in **Overlay › Subtitles**, or redo the area selection a bit taller than the game's subtitle.

#### "Translations of different lines are mixing into one block (or the opposite)"
→ First check you pressed the right hotkey: `Numpad8` merges lines (paragraph) and `Numpad9` keeps them apart (line). If the mode is right and it still gets it wrong, adjust **Grouping sensitivity** in **Overlay › Capture** — it only affects Paragraph Mode.

#### "I switched monitors and capture isn't working right anymore"
→ Restart the program via the button in **General › Config** — it's necessary after switching monitors.

#### "I want to share my logs for support, but don't want to show game content"
→ Check **Debug › Logs** if the option "Log captured texts and translations" is **disabled** (it's the default) — this way logs don't show text/translation content.

---
