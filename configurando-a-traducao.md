## 5. Configurando a tradução

### Tipo de texto: diálogo ou menu?

Na aba **OCR**, em "Agrupamento de Blocos", escolha:

- **Modo Parágrafo** (padrão) — junta linhas próximas em um único bloco de tradução. Use para **diálogos, falas de personagens, textos corridos** (visual novels, JRPGs).
- **Modo Linha** — cada linha vira uma tradução separada. Use para **menus, inventário, status, HUD** — onde cada linha é uma informação independente e não deve ser misturada com a de cima ou de baixo.

Se o programa estiver juntando falas que deveriam ser separadas (ou separando uma fala que deveria ficar junta), ajuste o controle **"Sensibilidade do agrupamento"** que aparece no Modo Parágrafo:

- Texto sendo **separado demais**? Aumente o valor (até 3.0).
- Texto sendo **juntado demais**? Diminua o valor (até 0).

### Melhorando o reconhecimento de texto difícil

Se o programa não está detectando o texto direito (fontes pequenas, estilizadas, com efeitos), vá na aba **Captura** e ative o **Pré-processamento**. Algumas dicas rápidas:

- **Texto pequeno**: aumente o **Upscale** (2x ou 3x costuma resolver).
- **Fonte com contorno grosso**: aumente um pouco o **Sharpen**.
- **Texto com pouco contraste contra o fundo**: aumente o **Contraste**.
- **Texto claro sobre fundo escuro** (ou vice-versa, se estiver dando errado): tente **Inverter cores**.

Não sabe por onde começar? Use a aba **Lab** — lá dá para testar todas essas opções em imagens de exemplo, ver o resultado em tempo real, e depois aplicar a configuração que funcionou melhor direto na Captura ou na Legenda.

### Trocando o motor de OCR (avançado)

Se mesmo com pré-processamento o reconhecimento continuar ruim, a aba **OCR** permite trocar o "motor" de reconhecimento de texto:

- **WinOCR** (padrão) — rápido, já vem pronto, mas pode errar em fontes muito estilizadas.
- **OneOCR** (experimental) — o motor de OCR da Ferramenta de Captura (Snipping Tool), muito melhor que o WinOCR em fontes estilizadas e multilíngue automático (não precisa configurar idioma de origem). Você copia 3 arquivos do próprio Windows 11 para uma pasta sua. Por usar uma API não oficial da Microsoft, uma atualização do Snipping Tool pode parar de funcionar; nesse caso, basta re-extrair os arquivos.

***O OneOCR funciona tanto em Windows 10 quanto em Windows 11, mas você só consegue achar os arquivos necessários dentro do Windows 11.***
