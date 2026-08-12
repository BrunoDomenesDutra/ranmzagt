# 14. Updating the program

When you open the program, if a newer version has been published, a notice appears showing the version you have and the one that came out. The **Download** button opens the new version's page in your browser — that's where the release notes and the `.zip` file are.

**The program does not download and does not install anything by itself.** It only tells you; downloading and replacing the files is up to you, the same way you did the first install. This is on purpose: a program that replaces its own executable is exactly the behaviour Windows Defender blocks, and it isn't worth the risk of the whole program failing to start.

**How to update**, once you have the `.zip`: close Ranmza-GT, extract its contents over your current folder and confirm replacing the files. Your settings (`config.json`), the API keys, the fonts you dropped in `fonts/` and the files in `models/` (OneOCR and MI-GAN) are **not in the `.zip`** and stay where they are.

To turn the notice off, tick **Do not notify me about new versions** on the notice itself, or turn it off in **General › Config → Updates**. That toggle is how it comes back.

Even with the notice off, the **Check now** button in the same card checks right away whether a new version is out — that's how to look every once in a while without being told every time.

> The program queries the releases page at most once every 6 hours, no matter how many times you open and close it during the day — the notice still appears on every launch, because it uses the last stored answer. The *Check now* button ignores that interval. If you have no internet, nothing happens: no error shows up and the program opens normally.
