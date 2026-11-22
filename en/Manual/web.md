# 10. Web

The **Overlay › Web** tab turns on a server on your local network that shows the translations on a browser page. Use it to follow the translations on your phone or a second monitor, and to bring the translation into OBS when it does not show up in the recording.

> **You do not need the Web server for the translation to show up in OBS.** With OBS capturing the monitor (*Display Capture*), the translation goes into the recording like any window. It is left out in three cases:
> - OBS uses *Game Capture*, which records only the game image, without the windows on top;
> - Subtitle Mode has *Stick to the detected text* on, which hides the subtitle from recordings so the OCR does not read its own translation;
> - *Hide the translation from recordings and streams* is on in Overlay › Capture.
>
> In those cases, use the OBS addresses of this tab.

?> **Hiding from recordings only applies to programs that record or stream on this same PC**, such as OBS, Game Bar, Discord and NVIDIA ShadowPlay. **When recording with a capture card**, on another PC, the card receives the same image that goes to your monitor: the translation, the subtitle stuck to the detected text, the toolbar and the alerts show up normally in the recording, even with the hide options on. In that case you do not need the OBS addresses.

<p align="center"><img src="media/en/overlay-web.png" alt="Overlay › Web tab" width="820"></p>

## Web Server

- **Server active** — turns the server on. With it off, none of the addresses below work. The first time, Windows Firewall asks whether to allow the program on the network.
- **Show translation on screen** — applies to screen capture. Off, the translation shows only on the pages, not on top of the game. It can only be changed with the server on.
- **Port** — default 7474. Next to it you see how many pages are connected.

## Addresses

Each address has a **Copy** button.

- **Capture** (`/captura`) — list of the screen capture translations, with history and a Clear button. Open it in the browser of any device on the same network, such as your phone.
- **Capture — OBS** (`/captura/obs`) — the same list, with a transparent background and no button, for use in OBS.
- **Subtitles — OBS** (`/legenda/obs`) — the Subtitle Mode subtitle with *Stick to the detected text* on, in the same place as the original subtitle.

The two capture pages only receive screen capture translations (`Numpad8`, `Numpad9` and Vision). The subtitle goes only to the **Subtitles — OBS** address.

## Adding it to OBS

**Screen capture translation:**

1. Turn on **Server active** and copy the **Capture — OBS** address.
2. In OBS, add a **"Browser" (Browser Source)** source with that address.
3. If the translation also shows up in the monitor capture and appears twice, turn off **Show translation on screen**.

**Subtitle stuck to the detected text:**

1. Turn on **Server active** and copy the **Subtitles — OBS** address.
2. In OBS, add a **"Browser" (Browser Source)** source with that address and your monitor resolution. Keep the source above the game, the same size and in the same position as the game image.
3. In **Overlay › Subtitles**, keep *Stick to the detected text* on.

The subtitle shows in OBS in the same place as the original, with the font, colors and background of the Subtitles tab, and it disappears together with the one on screen. If the game image is cropped or windowed in the scene, the subtitle is out of place. In OBS, the *Glass effect* becomes the dark background, because the page does not receive the game image.

## Appearance

Applies to the **Capture** and **Capture — OBS** pages. The subtitle page uses the appearance of the Subtitles tab. Open pages change right away.

<p align="center"><img src="media/en/overlay-web-aparencia.png" alt="Overlay › Web tab — page appearance" width="820"></p>

- **Theme** — Dark, Light or Dracula.
- **Font size** — 12 to 48 px.
- **Bold** — translation in bold.
- **Detected text** — shows the original text read by the OCR below the translation.
- **Time and service** — shows the time of the translation and the service that translated it.
- **Custom colors** — replaces the theme colors with yours: translated text, original text, time, service, card background and card border.

## History

- **Entries kept in the buffer** — how many translations the server keeps for whoever opens the page later, from 10 to 200. The Clear button on the page and the one in the History tab erase the list.

## Toolbar, alerts and preview in recordings

The floating toolbar, the alerts and the area preview also show up in recordings. To remove the toolbar and the alerts, turn on *Hide the toolbar from recordings and streams* (General › Shortcuts) and *Hide alerts from recordings and streams* (General › Config). The preview has no such option: turn it off with `Numpad2` before recording.

---
