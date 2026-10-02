# 4. Profiles — one set of settings per game

Each game needs different settings: the dialogue box sits in a corner of the screen, the language is another, the font that reads well in one does not in another, and the glossary of names is useless anywhere else. A **profile** keeps all of that together, and you switch games in one click.

The selector is at the **top of the window**, next to the **Guide** button, and shows up in every tab — because the active profile is the context of everything they show.

<p align="center"><img src="media/geral-perfis.png" alt="General › Profiles tab" width="820"></p>

## The Default profile

It always exists, comes active and **cannot be deleted or renamed**. If you never create another profile, everything you adjust stays in it.

Anyone who already used Ranmza GT loses nothing in the update — the previous settings become the Default profile automatically.

## Creating a profile

Go to **General › Profiles**, write the game name and choose:

- **Duplicate current** — copies everything in effect right now, including the monitor and the selected areas. It is the usual path: you set the program up right for a game and want to keep it under a name.
- **Start from scratch** — uses the factory values, on the current monitor, and opens the **Setup guide** for you to set up the new game. Good for a game that has nothing to do with the previous one.

The new profile becomes active right away. From then on, just adjust the program normally, in the usual tabs: **everything you change is saved in it by itself**, with no save button.

## Switching profiles

Click the selector at the top and pick another one (or click its row in *General › Profiles*). The switch applies right away — monitor, areas, languages, appearance and glossary change together, no restart. An alert on screen confirms which profile came in, useful when you switch with the game in the foreground.

If **Subtitle Mode** is on, it stays on and starts capturing the new profile's area.

## Renaming and deleting

In **General › Profiles**, each profile (except Default) has **Rename** and **Delete**. Deleting asks for confirmation; if you delete the profile in use, Default takes over right away.

## What does NOT change when you switch profiles

Not everything is "per game" — what is yours stays the same in every profile:

| Follows the profile | Applies to all profiles |
|---|---|
| Monitor and the saved areas of each monitor | API keys |
| Screen capture area and subtitle area | Keyboard shortcuts and floating toolbar |
| Text language, alphabet filter and target language | Capture backend |
| Screen capture and subtitle appearance | OCR engine, OneOCR folder and Paragraph mode grouping |
| Translation service, model and Azure region | Inpaint |
| Previous lines, System Prompt and Game Info | Web server and alerts |
| Subtitle Mode options | Language, theme and zoom of the settings screen |

The API key is the case that matters most: you type it **once** and it applies to every profile, including the ones you create later.

---
