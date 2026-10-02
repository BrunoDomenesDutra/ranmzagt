# 14. Updating the program

When opening the program, if a newer version is published, a warning shows the version you have and the one that came out. The **Download** button opens the new version's page in your browser — that is where the news of that version and the `.zip` file are.

**The program does not download or install anything by itself.** It only warns you; downloading and replacing the files are done by you, the same way as the first install. This is on purpose: a program that replaces its own executable is exactly the behavior Windows Defender blocks, and it is not worth the risk of the whole program not opening anymore.

**How to update**, after downloading the `.zip`: close Ranmza GT, extract the contents over the current folder and confirm replacing the files. Your settings (`config.json`), the profiles (`profiles\`), the API keys, the fonts you put in `fonts/` and the files in `models/` (OneOCR and MI-GAN) **are not in the `.zip`** and stay where they are.

> API keys are encrypted for this PC and this Windows account. If you copy the settings to another PC, type the keys again there.

To turn off the warning, check **Don't notify me about new versions** in the warning itself, or turn it off in **General › Config → Updates**. That switch is how it comes back.

Even with the warning off, the **Check now** button, in the same card, checks right away whether a new version came out — it is the way to take a look now and then without being warned every time.

> The program checks the releases page at most once every 6 hours, even if you open and close it several times a day — the warning keeps showing on every opening, because it uses the last saved answer. The *Check now* button ignores that interval. If you are offline, nothing happens: no error shows and the program opens normally.
