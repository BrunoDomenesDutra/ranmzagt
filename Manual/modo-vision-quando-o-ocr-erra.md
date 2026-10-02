# 8. Modo Vision — quando o OCR erra

Às vezes o reconhecimento de texto comum (OCR) erra letras, perde pedaços do texto ou se perde
totalmente em fontes muito estilizadas, com símbolos ou ícones no meio do texto.

Para esses casos, use o **Traduzir com I.A Vision**. Junto com o texto reconhecido, o programa
**envia a imagem da área para a IA**, que "olha" a imagem, corrige o que o OCR leu errado e
traduz. Símbolo ou ícone no meio da frase vira `[...]` na tradução.

Assim como no Traduzir normal, o Vision tem os dois modos, e você escolhe pelo atalho:

- **`Numpad5`** — Vision no **modo parágrafo** (diálogos).
- **`Numpad6`** — Vision no **modo linha** (menus e listas).

**Importante:**
- Só funciona com **OpenAI, Anthropic (Claude) ou Gemini**. Com Google Translate, Google Cloud,
  DeepL, Azure ou Groq, o atalho traduz só o texto do OCR e mostra o alerta *"Vision só com IA"*.
- Usa o mesmo modelo escolhido em **Tradução › Tradutores**.
- É um pouco mais lento e **sempre faz uma chamada nova** à IA: não usa as traduções guardadas,
  porque a resposta depende da imagem.
- A posição da tradução na tela ainda depende de onde o reconhecimento de texto encontrou algo.

**Quando usar**: fontes desenhadas à mão, créditos estilizados, textos com ícones/símbolos
misturados (ex: "pressione [ícone de botão] para continuar"), ou sempre que o atalho normal
("Traduzir") devolver um texto sem sentido.

---
