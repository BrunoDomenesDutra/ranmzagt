# 13. Problemas comuns e soluções

**"Erro ao abrir o programa: VCRUNTIME140.dll não foi encontrado" (ou MSVCP140.dll)**
→ Falta o **Microsoft Visual C++ Redistributable** no seu Windows — um componente gratuito da
Microsoft que alguns PCs recém-formatados ainda não têm. Baixe e instale o pacote **x64** por este
link oficial: <https://aka.ms/vs/17/release/vc_redist.x64.exe> — depois reabra o Ranmza GT, que ele
abre normalmente.

**"O reconhecimento não detecta nada" / aviso vermelho sobre idioma**
→ Vá em **Geral › Idioma** e clique no aviso para instalar o pacote de idioma do Windows necessário.

**"Apertei o atalho e nada acontece"**
→ Confira se a janela de configuração não está em primeiro plano (os atalhos só funcionam com
o jogo em foco). Se mesmo assim não funcionar, ative a **barra flutuante** (**Geral › Config**) e use
os botões dela.

**"Os atalhos não funcionam em alguns jogos (mesmo com o jogo em foco)"**
→ Alguns jogos rodam com privilégios elevados (Administrador) e, por isso, **bloqueiam o registro
dos atalhos globais** do Ranmza GT. Nesse caso, **execute o Ranmza GT como Administrador** (clique
com o botão direito no `.exe` → *Executar como administrador*) — assim ele consegue ativar os
atalhos por cima do jogo. Para não precisar repetir toda vez, marque *Executar este programa como
administrador* em **Propriedades → Compatibilidade** do executável. (Alternativa: use a **barra
flutuante**, que dispara as ações por clique do mouse e não depende dos atalhos do teclado.)

**"A tradução não aparece, ou demora muito"**
→ Confira as abas **Historico** e **Debug › Monitor** para ver se a tradução está sendo feita. Falhas passageiras
(limite de requisições, servidor fora do ar por um instante, queda de conexão) são **tentadas de
novo automaticamente** uma vez antes de recorrer ao Google Translate. Se você tiver **mais de uma
chave** cadastrada para o motor, ele ainda tenta as demais chaves da lista antes do fallback. Se
aparecer um aviso amarelo de "fallback para Google Translate" — e no Histórico a tradução vier
marcada como "Google Translate (fallback)" —, quer dizer que o serviço configurado (OpenAI, Claude,
Gemini) falhou em **todas** as chaves; confira suas chaves de API e créditos em Traducao › Tradutores.

**"Apareceu um aviso vermelho de erro"**
→ Geralmente indica chave de API inválida, créditos esgotados, ou o serviço fora do ar
temporariamente. Confira **Traducao › Tradutores**. Se o aviso disser que a resposta foi **cortada no
limite de tokens**, aumente o **Max tokens** em **Traducao › I.A** (acontece só em blocos de texto muito
grandes).

**"O texto reconhecido está errado/incompleto"**
→ Tente ativar o pré-processamento (**Overlay › Captura**) com upscale e ajuste de contraste,
ou use o **Traduzir com I.A Vision** (`Numpad5` parágrafo, `Numpad6` linha) para deixar a IA
"ver" a imagem e corrigir.

**"A tradução fica cortada ou não cabe na caixa"**
→ Na tradução manual (`Numpad8`/`Numpad9`), ative **Auto-fit** em **Overlay › Captura** — o programa
vai diminuir a fonte automaticamente até caber.
→ No **Modo Legenda** com *Substituir a legenda original no lugar* ligado não há auto-fit: a
tradução tem que caber na área que você marcou. Diminua o *Tamanho da fonte* em **Overlay ›
Legenda**, ou refaça a seleção da área um pouco mais alta que a legenda do jogo.

**"As traduções de falas diferentes estão se misturando num bloco só" (ou o contrário)**
→ Primeiro confira se você apertou o atalho certo: `Numpad8` junta as linhas (parágrafo) e
`Numpad9` separa (linha). Se o modo está certo e ainda erra, ajuste a **Sensibilidade do
agrupamento** em **Geral › OCR** — ela só afeta o modo Parágrafo.

**"Troquei de monitor e a captura não funciona mais direito"**
→ Reinicie o programa pelo botão em **Geral › Config** — é necessário após trocar de monitor.

**"Quero compartilhar meus logs para suporte, mas não quero mostrar o conteúdo do jogo"**
→ Confira em **Debug › Logs** se a opção "Logar textos capturados e traduções" está
**desativada** (é o padrão) — assim os logs não mostram o conteúdo dos textos/traduções.

---
