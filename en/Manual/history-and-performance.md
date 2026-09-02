# 12. History and performance

- **History tab**: shows translations made during the current session (original text, translation, time and service used), most recent first. Click an entry to copy the translation; there's also a button to clear everything.
- **Debug › Monitor**: turns on a log of the last 10 translations with the time each step took (capture, preprocessing, recognition, translation, total) — useful to notice if any configuration is slowing the program down (for example, heavy preprocessing).
- **DeepL usage** (**Translation › Translators**, with DeepL selected): shows how many **characters** DeepL translated in this session and your **account quota** (characters used/billing period limit) — click "Update" to check. Exclusive to DeepL: the AI engines don't expose spend through the key, and Azure has no equivalent quota endpoint (you track it in the Azure portal).

<p align="center"><img src="media/historico.png" alt="History tab" width="820"></p>

<p align="center"><img src="media/debug-monitor.png" alt="Debug › Monitor tab" width="820"></p>

---
