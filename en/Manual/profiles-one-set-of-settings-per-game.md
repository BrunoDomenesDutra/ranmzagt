# 4. Profiles — one set of settings per game

Every game asks for different settings: the dialogue box sits in a different corner of the screen, the language is another one, the font that reads well in one doesn't in the other, and the glossary of names is useless anywhere else. A **profile** keeps all of that together, and you switch games in one click.

The selector lives in the **top-right corner of the window**, next to the theme button, and shows up on every tab — because the active profile is the context for everything they display.

<p align="center"><img src="media/geral-perfis.png" alt="General › Profiles tab" width="820"></p>

## The Default profile

It always exists, comes active and **cannot be deleted or renamed**. If you never create another profile, the program works exactly as before: everything you adjust stays in it.

Nobody already using Ranmza GT loses anything on the update — your current configuration becomes the Default profile automatically.

## Creating a profile

Go to **General › Profiles**, type the game's name and choose:

- **Duplicate current** — copies everything in effect right now, selected areas included. This is the usual path: you got the program right for a game and want to save that under a name.
- **Start from scratch** — uses the factory values. Good for a game that has nothing to do with the previous one.

The new profile becomes active right away. From there you just set the program up as usual, in the same tabs: **everything you change is saved into it by itself**, with no save button.

## Switching profiles

Click the selector in the header and pick another one (or click its row in *General › Profiles*). The switch takes effect immediately — areas, languages, appearance and glossary all change together, with no restart. An on-screen notification confirms which profile took over, handy when you switch with the game in the foreground.

If **Subtitle Mode** or **Real-time Mode** are running, they stay running and start capturing the new profile's area.

## Renaming and deleting

In **General › Profiles**, every profile (except Default) has **Rename** and **Delete**. Deleting asks for confirmation; if you delete the profile in use, Default takes over immediately.

## What does NOT change when you switch profiles

Not everything is "per game" — what is yours keeps applying across all profiles:

| Follows the profile | Applies to every profile |
|---|---|
| Source and translation languages | API keys |
| Capture area and subtitle area | Keyboard shortcuts |
| Translation appearance (font, color, background, duration) | Monitor and floating toolbar |
| Image preprocessing | OCR engine and OneOCR folder (*General › OCR* tab) |
| Translation engine and model | Inpaint |
| System Prompt and Game Information | Web server |
| Subtitle Mode and Real-time Mode | Interface language and the diagnostic options |

The API key is the one that matters most: you type it **once** and it applies to every profile, including the ones you create later.

---
