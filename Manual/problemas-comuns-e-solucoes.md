## 12. Problemas comuns e soluções

**"Erro ao abrir o programa: VCRUNTIME140.dll não foi encontrado" (ou MSVCP140.dll)**
→ Falta o **Microsoft Visual C++ Redistributable** no seu Windows — um componente gratuito da
Microsoft que alguns PCs recém-formatados ainda não têm. Baixe e instale o pacote **x64** por este
link oficial: <https://aka.ms/vs/17/release/vc_redist.x64.exe> — depois reabra o Ranmza GT, que ele
abre normalmente.

**"O reconhecimento não detecta nada" / aviso vermelho sobre idioma**
→ Vá na aba Idioma e clique no aviso para instalar o pacote de idioma do Windows necessário.

**"Apertei o atalho e nada acontece"**
→ Confira se a janela de configuração não está em primeiro plano (os atalhos só funcionam com
o jogo em foco). Se mesmo assim não funcionar, ative a **barra flutuante** (aba Geral) e use os
botões dela.

**"Os atalhos não funcionam em alguns jogos (mesmo com o jogo em foco)"**
→ Alguns jogos rodam com privilégios elevados (Administrador) e, por isso, **bloqueiam o registro
dos atalhos globais** do Ranmza GT. Nesse caso, **execute o Ranmza GT como Administrador** (clique
com o botão direito no `.exe` → *Executar como administrador*) — assim ele consegue ativar os
atalhos por cima do jogo. Para não precisar repetir toda vez, marque *Executar este programa como
administrador* em **Propriedades → Compatibilidade** do executável. (Alternativa: use a **barra
flutuante**, que dispara as ações por clique do mouse e não depende dos atalhos do teclado.)

**"A tradução não aparece, ou demora muito"**
→ Confira a aba Histórico/Monitor para ver se a tradução está sendo feita. Se aparecer um aviso
amarelo de "fallback para Google Translate", quer dizer que o serviço configurado (OpenAI,
Claude, Gemini) falhou — confira sua chave de API e créditos na aba Tradutores.

**"Apareceu um aviso vermelho de erro"**
→ Geralmente indica chave de API inválida, créditos esgotados, ou o serviço fora do ar
temporariamente. Confira a aba Tradutores.

**"O texto reconhecido está errado/incompleto"**
→ Tente ativar o pré-processamento (aba Captura) com upscale e ajuste de contraste, ou use o
atalho **Traduzir com IA Vision** (`Numpad4`) para deixar a IA "ver" a imagem e corrigir.

**"A tradução fica cortada ou não cabe na caixa"**
→ Ative **Auto-fit** na aba Captura — o programa vai diminuir a fonte automaticamente até
caber.

**"As traduções de falas diferentes estão se misturando num bloco só" (ou o contrário)**
→ Ajuste a **Sensibilidade do agrupamento** na aba OCR (Modo Parágrafo).

**"Troquei de monitor e a captura não funciona mais direito"**
→ Reinicie o programa pelo botão da aba Geral — é necessário após trocar de monitor.

**"Quero compartilhar meus logs para suporte, mas não quero mostrar o conteúdo do jogo"**
→ Confira na aba Logs/Debug se a opção "Logar textos capturados e traduções" está
**desativada** (é o padrão) — assim os logs não mostram o conteúdo dos textos/traduções.

---
