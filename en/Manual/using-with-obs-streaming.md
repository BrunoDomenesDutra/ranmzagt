# 10. Using with OBS / streaming

If you stream or record the game and want **the translation to also appear in the video/stream** (or only in the video, without appearing in the game itself), use the **Web** tab:

1. Turn on **Server active**.
2. Copy the **Capture — OBS** address (`/captura/obs`) shown in the tab, with the *Copy* button.
3. In OBS, add a source of type **"Browser Source"** and paste that address. This version of the page has a transparent background, ready to overlay the game capture.
4. (Optional) **Turn off** the **"Show translation on screen"** switch to drop the overlay from the game and let the translation appear **only** on the browser page/OBS — useful if OBS's capture already includes the overlay window and you don't want to see the translation twice. Leave it **on** if you want the translation in both places.

You can also customize theme (light/dark/dracula), colors, font size, and whether you want to show the original text together with the translation, time, and which service was used.

The page can also be opened in any browser on the local network (phone, second monitor, etc.) using the **Capture** address (`/captura`) shown in the tab — that version comes with history and a clear button.

> If the translation disappears from your recordings and streams without you touching any of this, the culprit is **Hide overlay from screen capture** (Experimental tab): it makes the overlay invisible to any screen capture, OBS included. That is exactly the case the Web server solves.

---
