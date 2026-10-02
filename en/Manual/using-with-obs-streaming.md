# 10. Using with OBS / streaming

If you stream or record the game and want **the screen capture translation to show up in the video/stream too** (or only in the video, without showing in the game itself), use **Overlay › Web**:

1. Turn on **Server active**.
2. Copy the **Capture — OBS** address (`/captura/obs`) shown in the tab, with the *Copy* button.
3. In OBS, add a **"Browser" (Browser Source)** source and paste that address. This version of the page has a transparent background, ready to overlay the game capture.
4. (Optional) **Turn off** the **"Show translation on screen"** switch to remove the overlay from the game and have the translation show **only** in the browser/OBS page — useful if the OBS capture already includes the overlay window and you do not want to see the translation twice. Keep it **on** if you want the translation in both places.

<p align="center"><img src="media/en/overlay-web.png" alt="Overlay › Web tab" width="820"></p>

You can also customize the theme (light/dark/dracula), colors, font size, and whether to show the original text along with the translation, the time and which service was used. Open pages change right away.

<p align="center"><img src="media/en/overlay-web-aparencia.png" alt="Overlay › Web tab — page appearance" width="820"></p>

The page can also be opened in any browser on the local network (phone, second monitor, etc.) using the **Capture** address (`/captura`) shown in the tab — that version comes with history and a clear button.

> If the translation disappears from your recordings and streams, there are two possible causes. One is automatic: Subtitle Mode with *Stick to the detected text* on draws **over** the original text, and then the overlay must be invisible to captures, otherwise the OCR would read its own translation. The other is your choice: *"Hide the translation from recordings and streams"*, in the **Display** card of Overlay › Capture. For screen capture, those are exactly the cases the Web server solves.

---
