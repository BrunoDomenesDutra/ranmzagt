# 5. Configurando a tradução

## Tipo de texto: diálogo ou menu?

O modo de agrupamento **não se escolhe numa aba** — é decidido na hora da captura, pelo atalho
que você aperta:

- **`Numpad8` — Modo Parágrafo** — junta linhas próximas em um único bloco de tradução. Use para
  **diálogos, falas de personagens, textos corridos** (visual novels, JRPGs).
- **`Numpad9` — Modo Linha** — cada linha vira uma tradução separada. Use para **menus,
  inventário, status, HUD** — onde cada linha é uma informação independente e não deve ser
  misturada com a de cima ou de baixo.

O mesmo vale para o Vision: `Numpad5` é parágrafo e `Numpad6` é linha.

Se o modo Parágrafo estiver juntando falas que deveriam ser separadas (ou separando uma fala que
deveria ficar junta), ajuste a **Sensibilidade do agrupamento**, em **Geral › OCR**:

- Texto sendo **separado demais**? Aumente o valor (até 3,0).
- Texto sendo **juntado demais**? Diminua o valor (até 0).

Esse ajuste só afeta o modo Parágrafo — no modo Linha ele é ignorado.

## Melhorando o reconhecimento de texto difícil

Se o programa não está detectando o texto direito (fontes pequenas, estilizadas, com efeitos),
vá em **Overlay › Captura** e ative o **Pré-processamento**. Algumas dicas rápidas:

- **Texto pequeno**: aumente o **Upscale** (2x ou 3x costuma resolver).
- **Fonte com contorno grosso**: aumente um pouco o **Sharpen**.
- **Texto com pouco contraste contra o fundo**: aumente o **Contraste**.
- **Texto claro sobre fundo escuro** (ou vice-versa, se estiver dando errado): tente
  **Inverter cores**.

Não sabe por onde começar? Use **Ferramentas › Lab** — lá dá para testar todas essas opções em
imagens de exemplo, ver o resultado em tempo real, e depois aplicar a configuração que funcionou
melhor direto na Captura ou na Legenda.

## Trocando o motor de OCR (avançado)

Se mesmo com pré-processamento o reconhecimento continuar ruim, **Geral › OCR** permite trocar
o "motor" de reconhecimento de texto:

- **WinOCR** (padrão) — rápido (~30 ms), já vem pronto, mas pode errar em fontes muito
  estilizadas.
- **OneOCR** (experimental) — o motor de OCR da Ferramenta de Captura (Snipping Tool), muito
  melhor que o WinOCR em fontes estilizadas e multilíngue automático (não precisa configurar
  idioma de origem). **Roda no Windows 10 e no 11**; o que é exclusivo do Windows 11 são os
  3 arquivos que ele usa — eles só vêm com o Snipping Tool do Win11, então você os copia de uma
  máquina com Windows 11 e aponta a pasta. O card em Geral › OCR mostra o passo a passo. Por
  usar uma API não oficial da Microsoft, uma atualização do Snipping Tool pode parar de
  funcionar; nesse caso, basta reextrair os arquivos.

---
