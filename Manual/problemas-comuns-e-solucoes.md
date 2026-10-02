# 12. Problemas comuns e soluções

#### "Erro ao abrir o programa: VCRUNTIME140.dll não foi encontrado" (ou MSVCP140.dll)
→ Falta o **Microsoft Visual C++ Redistributable** no seu Windows — um componente gratuito da
Microsoft que alguns PCs recém-formatados ainda não têm. Baixe e instale o pacote **x64** por este
link oficial: <https://aka.ms/vs/17/release/vc_redist.x64.exe> — depois reabra o Ranmza GT, que ele
abre normalmente.

#### "O Ranmza GT já está aberto."
→ O programa abre uma vez só, para os atalhos não brigarem. Feche a outra janela do Ranmza GT —
inclusive uma versão antiga, se estiver aberta — e abra de novo.

#### "O reconhecimento não detecta nada" / aviso sobre idioma
→ Com o **WinOCR**, vá em **Geral › Idioma** e confira se um idioma está escolhido e se o pacote
dele está instalado no Windows. O **OneOCR** não usa pacotes de idioma do Windows e lê qualquer
idioma sem instalar nada — outro motivo para trocar de motor em **Geral › OCR**.

#### "Escolhi o OneOCR e o card diz *Não carregou*"
→ Também aparece o alerta *"OCR não carregou"*. Os arquivos do OneOCR ainda não foram copiados. Clique em **Detectar e copiar**, no card do
OneOCR em **Geral › OCR**. No Windows 10, siga o passo a passo do mesmo card. Enquanto o OneOCR
não carrega, o OCR fica parado.

#### "O guia não me deixa passar do passo Idiomas"
→ Com o WinOCR, o idioma do texto é obrigatório: escolha um na lista. Se a lista estiver vazia, o
Windows não tem nenhum pacote de idioma com leitura de texto; instale o pacote do idioma do jogo,
ou volte ao passo OCR e escolha o OneOCR.

#### "Apertei o atalho e nada acontece"
→ Confira se a janela de configuração não está em primeiro plano (os atalhos só funcionam com
o jogo em foco). Se aparecer o alerta *"Captura sem área"* ou *"Legenda sem área"*, marque a área
primeiro (`Numpad7` ou `Numpad1`). Se mesmo assim não funcionar, ative a **barra flutuante**
(**Geral › Atalhos**) e use os botões dela.

#### "Os atalhos não funcionam em alguns jogos (mesmo com o jogo em foco)"
→ Alguns jogos rodam com privilégios elevados (Administrador) e, por isso, **bloqueiam o registro
dos atalhos globais** do Ranmza GT. Nesse caso, **execute o Ranmza GT como Administrador** (clique
com o botão direito no `.exe` → *Executar como administrador*) — assim ele consegue ativar os
atalhos por cima do jogo. Para não precisar repetir toda vez, marque *Executar este programa como
administrador* em **Propriedades → Compatibilidade** do executável. (Alternativa: use a **barra
flutuante**, que dispara as ações por clique do mouse e não depende dos atalhos do teclado.)

#### "A tradução não aparece, ou demora muito"
→ Confira as abas **Histórico** e **Debug › Monitor** para ver se a tradução está sendo feita.
Falhas passageiras (servidor fora do ar por um instante, queda de conexão) são **tentadas de novo
automaticamente** antes de recorrer ao Google Translate. Se você tiver **mais de uma chave**
cadastrada para o serviço e o problema for da chave (recusada, sem crédito ou no limite de
requisições), ele passa na hora para a próxima chave da lista. Se aparecer o alerta
*"<serviço> falhou, usando Google"* — e no Histórico a tradução vier marcada como
*Google (fallback)* —, quer dizer que o serviço configurado falhou em **todas** as chaves;
confira suas chaves de API e créditos em Tradução › Tradutores. O serviço da configuração não
muda: a próxima tradução tenta ele de novo.

#### "Google: limite de uso (429)"
→ O Google Translate aqui é o **serviço gratuito, sem chave de API** — e serviço gratuito tem
limite de quantas traduções aceita num intervalo curto. Quando você bate nesse limite, aparece o
alerta e a tradução daquela captura não sai.

O que faz você bater no limite mais rápido do que parece: o **Modo Legenda** manda uma tradução a
cada fala nova, e uma captura de tela com muitos blocos separados vira muitos textos de uma vez.

E aqui vale saber de uma diferença: quando um serviço com chave falha, o programa cai no Google
Translate. **O Google não tem para onde cair** — ele já é o último recurso.

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
  linhas de uma mesma fala num bloco só — menos blocos, mesma tela traduzida.
- **Troque de serviço** em **Tradução › Tradutores**. **Google Cloud**, **DeepL**, **Azure**,
  **Gemini** e **Groq** têm plano gratuito: exigem criar uma chave de API, mas em troca você ganha
  um limite próprio, muito mais folgado. Se você está atrás de CGNAT, é a solução que realmente
  funciona: o limite passa a ser contado pela **sua chave**, e não pelo IP.

#### "Apareceu um alerta vermelho de erro"
→ Geralmente indica chave de API inválida, créditos esgotados, ou o serviço fora do ar
temporariamente. Confira **Tradução › Tradutores** e a aba **Debug › Logs**.

#### "No Azure, a chave parece inválida — mas a chave está certa"
→ Confira a **Região do recurso** em **Tradução › Tradutores**. O Azure responde o **mesmo erro**
para chave inválida e para região errada ou ausente, então uma região trocada parece problema de
chave. Copie a região da página *Keys and Endpoint* do seu recurso, no portal do Azure — pode colar
como aparece lá ("Brazil South"), que o programa ajusta o espaço e as maiúsculas sozinho.

#### "A IA traduziu errado, e a mesma tradução errada volta sempre"
→ O programa guarda cada tradução e reaproveita quando o mesmo texto aparece de novo. Com o texto
na tela, aperte **`Numpad4` (Retraduzir sem cache)**: ele traduz de novo sem olhar o que está
guardado e troca a tradução antiga pela nova. Se a tradução nova também sair ruim, tente o
**Vision** (`Numpad5` ou `Numpad6`), que manda a imagem para a IA.

#### "O texto reconhecido está errado/incompleto"
→ A solução que mais resolve é trocar o motor de OCR para o **OneOCR** em **Geral › OCR** — ele
lê fontes de jogo muito melhor que o WinOCR (o passo a passo e o porquê estão na
[seção 6](/Manual/configurando-a-traducao.md), em *Trocando o motor de OCR*). No Modo Legenda,
confira também se a área está justa em volta da legenda e o **filtro de alfabeto**. Na captura de
tela, use o **Traduzir com I.A Vision** (`Numpad5` parágrafo, `Numpad6` linha) para deixar a IA
"ver" a imagem e corrigir.

#### "A tradução não cabe no lugar do texto original"
→ Na captura de tela, ligue o **Auto-fit** em **Overlay › Captura** — o programa diminui a fonte
até caber.
→ No **Modo Legenda** com *Colar no texto detectado* ligado, a tradução transborda a área de
propósito. Diminua o *Tamanho da fonte* em **Overlay › Legenda** se ela cobrir o que não deve.

#### "As traduções de falas diferentes estão se misturando num bloco só" (ou o contrário)
→ Primeiro confira se você apertou o atalho certo: `Numpad8` junta as linhas (parágrafo) e
`Numpad9` separa (linha). Se o modo está certo e ainda erra, ajuste a **Sensibilidade do
agrupamento** em **Overlay › Captura** — ela só afeta o modo Parágrafo.

#### "Troquei de monitor e as áreas sumiram"
→ Cada monitor guarda as próprias áreas. Na primeira vez que você usa um monitor, ele não tem área
nenhuma: marque de novo (`Numpad7` e `Numpad1`). Ao voltar para o monitor anterior, as áreas dele
voltam sozinhas.

#### "Quero compartilhar meus logs para suporte, mas não quero mostrar o conteúdo do jogo"
→ Confira em **Debug › Logs** se a opção "Logar textos capturados e traduções" está
**desativada** (é o padrão) — assim os logs não mostram o conteúdo dos textos e traduções, e as
chaves de API nunca aparecem neles.

---
