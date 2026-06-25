## 7. Modo Vision — quando o OCR erra

Às vezes o reconhecimento de texto comum (OCR) erra letras, perde pedaços do texto ou se perde
totalmente em fontes muito estilizadas/artísticas, com símbolos ou ícones no meio do texto.

Para esses casos, use o atalho **Traduzir com IA Vision** (padrão `Numpad4`). Em vez de confiar
só no texto reconhecido, o programa **envia a imagem da tela para a Inteligência Artificial**,
que "olha" a imagem e entende melhor o que está escrito, mesmo que o reconhecimento de texto
tenha errado.

**Importante:**
- Só funciona com **OpenAI, Claude ou Gemini** (Google Translate e DeepL não suportam esse modo).
- É um pouco mais lento e **sempre faz uma chamada nova** à IA (não usa o histórico de
  traduções já feitas).
- A posição da tradução na tela ainda depende de onde o reconhecimento de texto encontrou algo
  — então, em casos raros, a tradução pode ficar maior que a área detectada.

**Quando usar**: fontes desenhadas à mão, créditos estilizados, textos com ícones/símbolos
misturados (ex: "pressione [ícone de botão] para continuar"), ou sempre que o atalho normal
("Traduzir") devolver um texto sem sentido.

---
