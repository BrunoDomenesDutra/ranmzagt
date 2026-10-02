# 12. Common problems and solutions

#### "Error opening the program: VCRUNTIME140.dll was not found" (or MSVCP140.dll)
→ Your Windows is missing the **Microsoft Visual C++ Redistributable** — a free Microsoft component some freshly formatted PCs do not have yet. Download and install the **x64** package from this official link: <https://aka.ms/vs/17/release/vc_redist.x64.exe> — then reopen Ranmza GT, and it opens normally.

#### "Ranmza GT is already running."
→ The program opens only once, so the shortcuts do not clash. Close the other Ranmza GT window — including an old version, if it is open — and open it again.

#### "Recognition does not detect anything" / language warning
→ With **WinOCR**, go to **General › Language** and check that a language is chosen and that its pack is installed in Windows. **OneOCR** does not use Windows language packs and reads any language without installing anything — another reason to switch engines in **General › OCR**.

#### "I chose OneOCR and the card says *Did not load*"
→ The *"OCR failed to load"* alert also shows. The OneOCR files have not been copied yet. Click **Detect and copy**, in the OneOCR card in **General › OCR**. On Windows 10, follow the step by step in the same card. While OneOCR does not load, the OCR stays stopped.

#### "The guide does not let me past the Languages step"
→ With WinOCR, the text language is required: pick one from the list. If the list is empty, Windows has no language pack with text recognition; install the pack for the game language, or go back to the OCR step and pick OneOCR.

#### "I pressed the shortcut and nothing happens"
→ Check that the settings window is not in the foreground (shortcuts only work with the game in focus). If the *"Capture: no area"* or *"Subtitles: no area"* alert shows up, mark the area first (`Numpad7` or `Numpad1`). If it still does not work, turn on the **floating toolbar** (**General › Shortcuts**) and use its buttons.

#### "Shortcuts don't work in some games (even with the game in focus)"
→ Some games run with elevated privileges (Administrator) and therefore **block the registration of Ranmza GT's global shortcuts**. In that case, **run Ranmza GT as Administrator** (right-click the `.exe` → *Run as administrator*) — that way it can enable the shortcuts over the game. To avoid repeating it every time, check *Run this program as an administrator* in the executable's **Properties → Compatibility**. (Alternative: use the **floating toolbar**, which triggers actions by mouse click and does not depend on keyboard shortcuts.)

#### "The translation does not show up, or takes too long"
→ Check the **History** and **Debug › Monitor** tabs to see if the translation is being made. Temporary failures (server down for a moment, connection drop) are **retried automatically** before falling back to Google Translate. If you have **more than one key** registered for the service and the problem is with the key (rejected, out of credit or at the request limit), it switches right away to the next key in the list. If the *"<service> failed, using Google"* alert shows — and the History marks the translation as *Google (fallback)* —, the configured service failed on **all** keys; check your API keys and credits in Translation › Translators. The service in the settings does not change: the next translation tries it again.

#### "Google: rate limited (429)"
→ Google Translate here is the **free service, without an API key** — and a free service limits how many translations it accepts in a short window. When you hit that limit, the warning shows and the translation of that capture does not come out.

What makes you hit the limit faster than it seems: **Subtitle Mode** sends a translation for every new line, and a screen capture with many separate blocks turns into many texts at once.

And here there is a difference worth knowing: when a service with a key fails, the program falls back to Google Translate. **Google has nowhere to fall back to** — it already is the last resort.

##### Why your limit seems smaller than your neighbor's: CGNAT

The limit is not per program or per account: it is counted **per IP address** — the number that identifies your connection on the internet. Everything that leaves your home reaches Google with that same number, and that is what Google uses to count how many translations you asked for.

The problem is that many people today **share the same IP with strangers**. There are not enough public IPs for everyone, so many providers (budget fiber, radio and especially 4G/5G mobile internet) use a technique called **CGNAT**: hundreds of customers go out to the internet through a single public IP. It is like a big building with only one street number — all the letters arrive at the front desk and someone distributes them inside. Seen from outside, you and your neighbors look like one person.

For Google, then, that IP's limit is spent by everyone together. If someone sharing your IP has been using Google services, part of the quota was gone before you opened the game — and the warning shows up much sooner than it would for someone with a **public IP of their own**. It is not a defect of the program or your computer, and there is no internal setting that fixes it.

**How to know if you are behind CGNAT:** compare the IP shown on your router's status page (the WAN IP) with what a "what is my IP" site shows. If they are different, it is CGNAT — and the router's usually starts with something between **100.64** and **100.127**, a range reserved precisely for this. Some providers give a public IP on request, sometimes for an extra fee.

What fixes it, from simplest to most definitive:

- **Wait a few minutes.** The limit is temporary and lifts by itself.
- **Use Paragraph mode** (`Numpad8`) instead of Line mode (`Numpad9`). Paragraph joins the lines of the same speech into one block — fewer blocks, same screen translated.
- **Switch services** in **Translation › Translators**. **Google Cloud**, **DeepL**, **Azure**, **Gemini** and **Groq** have a free plan: they require creating an API key, but in return you get your own, much roomier limit. If you are behind CGNAT, it is the fix that really works: the limit is counted by **your key**, not by the IP.

#### "A red error alert showed up"
→ It usually means an invalid API key, credits used up, or the service temporarily down. Check **Translation › Translators** and the **Debug › Logs** tab.

#### "On Azure, the key looks invalid — but the key is correct"
→ Check the **Resource region** in **Translation › Translators**. Azure answers the **same error** for an invalid key and for a wrong or missing region, so a wrong region looks like a key problem. Copy the region from the *Keys and Endpoint* page of your resource in the Azure portal — you can paste it as it appears there ("Brazil South"), and the program fixes spaces and capitals by itself.

#### "The AI translated something wrong, and the same wrong translation always comes back"
→ The program saves every translation and reuses it when the same text shows up again. With the text on screen, press **`Numpad4` (Retranslate)**: it translates again without looking at what is saved and replaces the old translation with the new one. If the new translation is also bad, try **Vision** (`Numpad5` or `Numpad6`), which sends the image to the AI.

#### "The recognized text is wrong/incomplete"
→ The fix that helps the most is switching the OCR engine to **OneOCR** in **General › OCR** — it reads game fonts much better than WinOCR (the step by step and the why are in [section 6](/en/Manual/configuring-translation.md), in *Switching OCR engine*). In Subtitle Mode, also check that the area is tight around the subtitle and the **alphabet filter**. In screen capture, use **Translate with AI Vision** (`Numpad5` paragraph, `Numpad6` line) to let the AI "see" the image and fix it.

#### "The translation does not fit where the original text was"
→ In screen capture, turn on **Auto-fit** in **Overlay › Capture** — the program shrinks the font until it fits.
→ In **Subtitle Mode** with *Stick to the detected text* on, the translation spills over the area on purpose. Lower the *Font size* in **Overlay › Subtitles** if it covers what it should not.

#### "Translations of different lines are getting mixed into one block" (or the opposite)
→ First check that you pressed the right shortcut: `Numpad8` joins the lines (paragraph) and `Numpad9` splits them (line). If the mode is right and it still gets it wrong, adjust the **Grouping sensitivity** in **Overlay › Capture** — it only affects Paragraph mode.

#### "I switched monitors and the areas disappeared"
→ Each monitor keeps its own areas. The first time you use a monitor, it has no area at all: mark them again (`Numpad7` and `Numpad1`). When you go back to the previous monitor, its areas come back by themselves.

#### "I want to share my logs with support, but I don't want to show the game content"
→ Check in **Debug › Logs** that the "Log captured text and translations" option is **off** (the default) — that way the logs do not show the content of texts and translations, and API keys never show up in them.

---
