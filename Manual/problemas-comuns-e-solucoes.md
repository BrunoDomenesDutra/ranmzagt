# 13. Problemas comuns e soluções

#### "Erro ao abrir o programa: VCRUNTIME140.dll não foi encontrado" (ou MSVCP140.dll)
→ Falta o **Microsoft Visual C++ Redistributable** no seu Windows — um componente gratuito da
Microsoft que alguns PCs recém-formatados ainda não têm. Baixe e instale o pacote **x64** por este
link oficial: <https://aka.ms/vs/17/release/vc_redist.x64.exe> — depois reabra o Ranmza GT, que ele
abre normalmente.

#### "O reconhecimento não detecta nada" / aviso vermelho sobre idioma
→ Vá em **Geral › Idioma** e clique no aviso para instalar o pacote de idioma do Windows necessário.
Esse aviso é coisa do **WinOCR**: o **OneOCR** não usa pacotes de idioma do Windows e lê qualquer
idioma sem instalar nada — outro motivo para trocar de motor em **Geral › OCR**.

#### "Apertei o atalho e nada acontece"
→ Confira se a janela de configuração não está em primeiro plano (os atalhos só funcionam com
o jogo em foco). Se mesmo assim não funcionar, ative a **barra flutuante** (**Geral › Atalhos**) e use
os botões dela.

#### "Os atalhos não funcionam em alguns jogos (mesmo com o jogo em foco)"
→ Alguns jogos rodam com privilégios elevados (Administrador) e, por isso, **bloqueiam o registro
dos atalhos globais** do Ranmza GT. Nesse caso, **execute o Ranmza GT como Administrador** (clique
com o botão direito no `.exe` → *Executar como administrador*) — assim ele consegue ativar os
atalhos por cima do jogo. Para não precisar repetir toda vez, marque *Executar este programa como
administrador* em **Propriedades → Compatibilidade** do executável. (Alternativa: use a **barra
flutuante**, que dispara as ações por clique do mouse e não depende dos atalhos do teclado.)

#### "A tradução não aparece, ou demora muito"
→ Confira as abas **Historico** e **Debug › Monitor** para ver se a tradução está sendo feita. Falhas passageiras
(limite de requisições, servidor fora do ar por um instante, queda de conexão) são **tentadas de
novo automaticamente** uma vez antes de recorrer ao Google Translate. Se você tiver **mais de uma
chave** cadastrada para o motor, ele ainda tenta as demais chaves da lista antes do fallback. Se
aparecer um aviso amarelo de "fallback para Google Translate" — e no Histórico a tradução vier
marcada como "Google Translate (fallback)" —, quer dizer que o serviço configurado (DeepL, Azure ou
um motor de IA) falhou em **todas** as chaves; confira suas chaves de API e créditos em
Traducao › Tradutores.

#### "Limite de requisições atingido" usando o Google Translate
→ O Google Translate aqui é o **serviço gratuito, sem chave de API** — e serviço gratuito tem
limite de quantas traduções aceita num intervalo curto. Quando você bate nesse limite, aparece o
aviso amarelo e a tradução daquela captura não sai.

O que faz você bater no limite mais rápido do que parece: o programa envia **uma requisição para
cada bloco de texto** da captura, todas ao mesmo tempo. Uma tela com muitas falas separadas vira
muitas requisições de uma vez só. E os modos contínuos (**Legenda** e **Tempo Real**) repetem isso
a cada ciclo.

O programa já tenta de novo sozinho, uma vez, depois de um instante — o aviso só aparece quando a
segunda tentativa também falha. E aqui vale saber de uma diferença: quando um motor com chave
(DeepL, Azure, IA) falha, o programa cai no Google Translate. **O Google não tem para onde cair** —
ele já é o último recurso.

##### Por que o seu limite parece menor que o do vizinho: CGNAT

O limite não é por programa nem por conta: ele é contado **por endereço de IP** — o número que
identifica a sua conexão na internet. Tudo o que sai da sua casa chega ao Google com esse mesmo
número, e é ele que o Google usa para contar quantas traduções você pediu.

O problema é que muita gente hoje **divide o mesmo IP com estranhos**. Não existe IP público
sobrando para todo mundo, então boa parte dos provedores (fibra popular, rádio e principalmente
internet móvel 4G/5G) usa uma técnica chamada **CGNAT**: centenas de clientes saem para a internet
por um único IP público. É como um prédio grande que tem só um número na rua — as cartas chegam
todas na portaria e alguém distribui lá dentro. Visto de fora, você e os vizinhos parecem uma
pessoa só.

Para o Google, então, o limite daquele IP é gasto por todos juntos. Se alguém que divide o IP com
você já andou usando serviços do Google, parte da cota foi embora antes de você abrir o jogo — e o
aviso aparece bem mais cedo do que apareceria para quem tem um **IP público só seu**. Não é defeito
do programa nem do seu computador, e não existe ajuste interno que resolva.

**Como saber se você está atrás de CGNAT:** compare o IP que aparece na tela de status do seu
roteador (o IP da WAN) com o que um site de "qual é o meu IP" mostra. Se os dois forem diferentes,
é CGNAT — e o do roteador normalmente começa com algo entre **100.64** e **100.127**, faixa
reservada justamente para isso. Alguns provedores fornecem IP público a pedido, às vezes cobrando
à parte.

O que resolve, do mais simples ao mais definitivo:

- **Espere alguns minutos.** O limite é temporário e se solta sozinho.
- **Use o modo Parágrafo** (`Numpad8`) em vez do modo Linha (`Numpad9`). O Parágrafo junta as
  linhas de uma mesma fala num bloco só — menos blocos, menos requisições, mesma tela traduzida.
- **Nos modos contínuos, aumente o intervalo de captura** em **Overlay › Legenda**. Traduzir a cada
  meio segundo gasta muito mais do que traduzir a cada dois.
- **Troque de motor** em **Traducao › Tradutores**. **DeepL** e **Azure Translator** têm plano
  gratuito: exigem criar uma chave de API, mas em troca você ganha um limite próprio, muito mais
  folgado, e tradução de qualidade melhor. Se você está atrás de CGNAT, é a solução que realmente
  funciona: o limite passa a ser contado pela **sua chave**, e não pelo IP, então o que os outros
  clientes do seu provedor fazem deixa de te atrapalhar.

#### "Apareceu um aviso vermelho de erro"
→ Geralmente indica chave de API inválida, créditos esgotados, ou o serviço fora do ar
temporariamente. Confira **Traducao › Tradutores**. Se o aviso disser que a resposta foi **cortada no
limite de tokens**, aumente o **Max tokens** em **Traducao › I.A** (acontece só em blocos de texto muito
grandes).

#### "No Azure, o teste diz que a chave é inválida — mas a chave está certa"
→ Confira a **Região do recurso** em **Traducao › Tradutores**. O Azure responde o **mesmo erro**
para chave inválida e para região errada ou ausente, então uma região trocada parece problema de
chave. Copie a região da página *Keys and Endpoint* do seu recurso, no portal do Azure — pode colar
como aparece lá ("Brazil South"), que o programa ajusta o espaço e as maiúsculas sozinho. Enquanto o
campo estiver vazio, o botão *Testar conexão* fica bloqueado.

#### "O texto reconhecido está errado/incompleto"
→ A solução que mais resolve é trocar o motor de OCR para o **OneOCR** em **Geral › OCR** — ele
lê fontes de jogo muito melhor que o WinOCR e dispensa quase todo ajuste de imagem (o passo a
passo e o porquê estão na [seção 6](/Manual/configurando-a-traducao.md), em *Trocando o motor de
OCR*). Se preferir seguir no WinOCR, ative o pré-processamento (**Overlay › Captura**) com
upscale e ajuste de contraste. Em último caso, use o **Traduzir com I.A Vision** (`Numpad5`
parágrafo, `Numpad6` linha) para deixar a IA "ver" a imagem e corrigir.

#### "A tradução fica cortada ou não cabe na caixa"
→ Na tradução manual (`Numpad8`/`Numpad9`), ative **Auto-fit** em **Overlay › Captura** — o programa
vai diminuir a fonte automaticamente até caber.
→ No **Modo Legenda** com *Substituir a legenda original no lugar* ligado não há auto-fit: a
tradução tem que caber na área que você marcou. Diminua o *Tamanho da fonte* em **Overlay ›
Legenda**, ou refaça a seleção da área um pouco mais alta que a legenda do jogo.

#### "As traduções de falas diferentes estão se misturando num bloco só" (ou o contrário)
→ Primeiro confira se você apertou o atalho certo: `Numpad8` junta as linhas (parágrafo) e
`Numpad9` separa (linha). Se o modo está certo e ainda erra, ajuste a **Sensibilidade do
agrupamento** em **Overlay › Captura** — ela só afeta o modo Parágrafo.

#### "Troquei de monitor e a captura não funciona mais direito"
→ Reinicie o programa pelo botão em **Geral › Config** — é necessário após trocar de monitor.

#### "Quero compartilhar meus logs para suporte, mas não quero mostrar o conteúdo do jogo"
→ Confira em **Debug › Logs** se a opção "Logar textos capturados e traduções" está
**desativada** (é o padrão) — assim os logs não mostram o conteúdo dos textos/traduções.

---
