# 11. Using with OBS / streaming

If you stream or record the game and want **the translation to also appear in the video/stream** (or only in the video, without appearing in the game itself), use the **Web** tab:

1. Turn on **Server active**.
2. Copy the **Capture — OBS** address (`/captura/obs`) shown in the tab, with the *Copy* button.
3. In OBS, add a source of type **"Browser Source"** and paste that address. This version of the page has a transparent background, ready to overlay the game capture.
4. (Optional) **Turn off** the **"Show translation on screen"** switch to drop the overlay from the game and let the translation appear **only** on the browser page/OBS — useful if OBS's capture already includes the overlay window and you don't want to see the translation twice. Leave it **on** if you want the translation in both places.

<p align="center"><img src="media/overlay-web.png" alt="Overlay › Web tab" width="820"></p>

You can also customize theme (light/dark/dracula), colors, font size, and whether you want to show the original text together with the translation, time, and which service was used.

<p align="center"><img src="media/overlay-web-aparencia.png" alt="Overlay › Web tab — page appearance" width="820"></p>

The page can also be opened in any browser on the local network (phone, second monitor, etc.) using the **Capture** address (`/captura`) shown in the tab — that version comes with history and a clear button.

> If the translation disappears from your recordings and streams, there are three possible causes. Two are automatic, in the modes that draw **over** the original text: Real-time Mode (always) and Subtitle Mode with *"Replace the original subtitle in place"* on — in both the overlay has to be invisible to captures, otherwise the OCR would re-read its own translation. The third is your own choice: *"Hide the translation from recordings and streams"*, in the **Display** card of Overlay › Capture. That is exactly the case the Web server solves.

---
