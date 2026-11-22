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

The floating toolbar, the alerts and the area preview also show up in recordings. To remove the toolbar and the alerts, turn on *Hide the toolbar from recordings and streams* (General › Shortcuts) and *Hide alerts from recordings and streams* (General › Config). The preview has no such option: turn it off with `Numpad2` before recording.

> If the translation disappears from your recordings and streams, there are two possible causes. One is automatic: Subtitle Mode with *Stick to the detected text* on draws **over** the original text, and then the overlay must be invisible to captures, otherwise the OCR would read its own translation. The other is your choice: *"Hide the translation from recordings and streams"*, in the **Display** card of Overlay › Capture. The Web server solves both cases: the **Capture — OBS** address for screen capture and the **Subtitles — OBS** address for the subtitle stuck to the detected text.

## Subtitle stuck to the detected text in OBS

With *Stick to the detected text* on, the subtitle disappears from recordings, so the OCR does not read its own translation. To show it in OBS:

1. In **Overlay › Web**, turn on **Server active**.
2. Copy the **Subtitles — OBS** address (`/legenda/obs`).
3. In OBS, add a **"Browser" (Browser Source)** source with that address and your monitor resolution. Keep the source above the game, the same size and in the same position as the game image.
4. In **Overlay › Subtitles**, keep *Stick to the detected text* on.

The subtitle shows in OBS in the same place as the original, with the font, colors and background of the Subtitles tab, and it disappears together with the one on screen. If the game image is cropped or windowed in the scene, the subtitle is out of place. In OBS, the *Glass effect* becomes the dark background, because the page does not receive the game image.

---
