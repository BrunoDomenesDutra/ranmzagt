# 2. Configuração rápida

São **cinco ajustes**. Depois deles você já está traduzindo; todo o resto deste manual é
refinamento, e você lê quando (e se) precisar.

| Passo | O que fazer | Onde |
|---|---|---|
| 1 | Escolher o monitor | aba **Geral › Config** |
| 2 | Escolher os idiomas | aba **Geral › Idioma** |
| 3 | Escolher o tradutor | aba **Traducao › Tradutores** |
| 4 | Marcar a área do texto | atalho `Numpad7`, com o jogo aberto |
| 5 | Traduzir | atalho `Numpad9` (linha) ou `Numpad8` (parágrafo) |

> **Antes de tudo: o jogo em modo Janela.** Em *Tela cheia exclusiva* nenhum programa consegue
> desenhar por cima — a tradução simplesmente não aparece. Troque o jogo para **Janela sem
> borda** nas opções de vídeo dele. Explicação completa na
> [seção 1](/Manual/o-que-o-programa-faz.md).

> **O programa nem abriu, com erro *"VCRUNTIME140.dll não foi encontrado"*?** Falta o
> **Microsoft Visual C++ Redistributable (x64)**, um componente gratuito da Microsoft que a
> maioria dos PCs já tem (vem junto com muitos jogos). Instale por este link oficial e abra o
> programa de novo:
> <https://aka.ms/vs/17/release/vc_redist.x64.exe>

## 2.1 Primeiro olhar: como a janela é organizada

<p align="center"><img src="media/geral-config.png" alt="Aba Geral › Config" width="820"></p>

O menu da esquerda agrupa as opções por assunto. Nesta configuração rápida você só encosta em
**Geral** e **Traducao** — o resto existe para quando você quiser afinar alguma coisa.

| Menu | O que tem dentro |
|---|---|
| **Geral** | Config (monitor, tema, barra flutuante), Perfis, Idioma, OCR e Atalhos |
| **Overlay** | Aparência da tradução na tela: Captura, Legenda e Web |
| **Traducao** | Tradutores (motor e chaves de API) e I.A (prompts e parâmetros) |
| **Ferramentas** | Inpaint (apagar o texto original) e Lab (testar pré-processamento) |
| **Debug** | Monitor de desempenho, imagens de diagnóstico e Logs |
| **Historico** | As traduções da sessão atual |
| **Experimental** | Recursos em desenvolvimento, como o Modo Tempo Real |
| **Sobre** | Versão do programa e links |

> **Idioma da interface** (em *Geral › Config*) muda só o idioma **do programa** — os menus e
> textos que você está vendo. Não tem nada a ver com o idioma que vai ser traduzido; esse é o
> passo 2.3.

## 2.2 Escolha o monitor

Ainda em **Geral › Config**, no card **Monitor**, escolha em **Tela ativa** onde o programa vai
trabalhar. Com um monitor só, deixe em *Automatico* e siga em frente.

Trocar de monitor **exige reiniciar o programa** — aparece um aviso com o botão **Reiniciar
agora** no rodapé da aba. Só depois do reinício a captura, o seletor de área e a tradução na
tela passam a valer para a outra tela. A área que você já tinha selecionado é apagada na troca.

O **Backend de captura** logo acima pode ficar em *Auto (recomendado)*: ele usa o método certo
para a sua versão do Windows sozinho e troca na hora, sem reiniciar.

## 2.3 Escolha os idiomas

Abra **Geral › Idioma**.

<p align="center"><img src="media/geral-idioma.png" alt="Aba Geral › Idioma" width="820"></p>

- **Idioma do texto** — o idioma que está escrito no jogo. Digite a sigla do idioma
  (`en` para inglês, `ja` para japonês, `ko` para coreano, `zh` para chinês…).
- **Idioma destino** — o idioma no qual você quer ler. `pt` para português.

> **Aviso amarelo sobre pacote de idioma?** O Windows OCR só reconhece idiomas cujo pacote está
> instalado no Windows. Instale em *Configurações → Hora e Idioma → Idioma e região*. Sem o
> pacote, o programa não consegue ler o texto naquele idioma.

> **Usando OneOCR?** Aí não existe idioma de origem para escolher: ele é um modelo único
> multilíngue (latim, CJK, cirílico…) que detecta o idioma sozinho, e o campo **Idioma do
> texto** nem aparece enquanto ele estiver selecionado — nem o aviso de pacote do Windows, que
> não se aplica. O **Idioma destino** continua valendo normalmente. O OneOCR é o motor
> **recomendado** e se escolhe em *Geral › OCR*; para começar dá para seguir com o WinOCR, mas
> vale trocar assim que puder — veja *Trocando o motor de OCR* na
> [seção 6](/Manual/configurando-a-traducao.md).

## 2.4 Escolha o tradutor

Abra **Traducao › Tradutores**.

<p align="center"><img src="media/tradutores-google.png" alt="Aba Traducao › Tradutores com Google Translate" width="820"></p>

O padrão é o **Google Translate — gratuito, sem chave**: não precisa configurar nada, já está
pronto para uso. É com ele que você deve fazer o primeiro teste.

> **Gratuito, mas com limite.** O Google Translate sem chave aceita só um punhado de traduções
> num intervalo curto. Passou disso, aparece o aviso *"Limite de requisições atingido"* e aquela
> captura fica sem tradução. Para traduzir uma fala aqui e ali ele dá conta; em sessão longa e nos
> modos contínuos (Legenda e Tempo Real) o limite chega rápido. E o limite é contado **por
> endereço de IP** — quem usa internet móvel ou provedor com **CGNAT** divide esse limite com
> outros clientes e bate nele bem mais cedo. A explicação e o que fazer estão na
> [seção 13](/Manual/problemas-comuns-e-solucoes.md).
>
> Some a isso que ela **não é uma API oficial**: é o mesmo endereço que a página do Google
> Tradutor usa por baixo dos panos, sem chave e sem conta. O Google pode mudá-la ou tirá-la do ar
> quando quiser, sem aviso. Os motores com chave não correm esse risco.

Quando quiser mais qualidade, troque em **Provedor ativo**:

- **DeepL** — tradutor dedicado, muito natural, com opção de formalidade. Precisa de chave de
  API, mas tem **plano gratuito** (as chaves terminam em `:fx`, e o programa reconhece sozinho
  qual servidor usar).
- **Azure Translator** — o tradutor da Microsoft, também dedicado. Além da chave de API, exige a
  **região** do recurso (as duas coisas ficam na mesma página do portal do Azure). Detecta o idioma
  de origem **bloco a bloco**, o que ajuda quando a captura mistura idiomas.
- **OpenAI**, **Anthropic (Claude)** ou **Gemini** — motores de IA. Precisam de chave de API
  com créditos, e em troca entregam traduções bem mais naturais e consistentes, principalmente
  em diálogos longos. Escolha o modelo em *Autenticação* e cole a chave em *Chaves de API*.

Cada motor guarda as suas próprias credenciais, então trocar de um para outro e voltar não
apaga nada. Use o botão **Testar conexao** para confirmar que a chave está válida antes de
entrar no jogo.

> **Várias chaves com rotação automática.** Todo motor com chave aceita **mais de uma**: clique
> em *+ Adicionar chave*. Se a chave em uso ficar sem crédito ou bater no limite de requisições,
> o programa passa sozinho para a próxima da lista; esgotadas todas, ele cai no Google
> Translate. Ajuda bastante em sessões longas de Modo Legenda.

> Só os motores de IA (OpenAI, Claude, Gemini) suportam o **Modo Vision** — o Google Translate, o
> DeepL e o Azure Translator não. Veja a [seção 8](/Manual/modo-vision-quando-o-ocr-erra.md).

## 2.5 Marque a área do texto

Com o jogo aberto e em foco, aperte **`Numpad7`**. A tela escurece e você arrasta o mouse para
desenhar um retângulo sobre a região onde o texto aparece — normalmente a caixa de diálogo.
Solte o botão para confirmar, ou aperte `ESC` para cancelar.

A área fica salva. Você só precisa marcar de novo se o jogo mudar a posição da caixa de texto
ou se você trocar a resolução.

> Não marcou nenhuma área? O programa captura a **tela inteira** — funciona, mas fica mais lento
> e erra mais. Vale marcar.

<div style="position:relative;padding-top:56.25%;max-width:820px;margin:0 auto">
  <iframe src="https://player.vimeo.com/video/1218016540"
          style="position:absolute;top:0;left:0;width:100%;height:100%;border:0"
          allow="fullscreen; picture-in-picture" allowfullscreen
          title="Marcando a área do texto"></iframe>
</div>

<p align="center"><i>Marcando a área do texto com o `Numpad7`.</i></p>

## 2.6 Traduza

Com o texto na tela, aperte um dos dois atalhos de tradução — a diferença é só **como as linhas
são agrupadas** antes de traduzir:

| Atalho | Modo | Use quando |
|---|---|---|
| **`Numpad9`** | **Linha** | Menus, listas, itens, botões — cada linha é uma coisa separada |
| **`Numpad8`** | **Parágrafo** | Diálogos e textos corridos — junta as linhas próximas num bloco só |

Na dúvida, comece pelo `Numpad8` em jogos de história e pelo `Numpad9` em menus.

A tradução aparece por cima do jogo, na posição do texto original, e some sozinha depois de um
tempo. Para tirá-la na hora, aperte **`NumpadDecimal`** (a vírgula do teclado numérico).

<div style="position:relative;padding-top:56.25%;max-width:820px;margin:0 auto">
  <iframe src="https://player.vimeo.com/video/1217778050"
          style="position:absolute;top:0;left:0;width:100%;height:100%;border:0"
          allow="fullscreen; picture-in-picture" allowfullscreen
          title="Selecionando a área e traduzindo"></iframe>
</div>

<p align="center"><i>Selecionando a área e traduzindo — nos modos linha e parágrafo.</i></p>

> **Os atalhos só funcionam com o jogo em foco.** Com a janela de configuração do Ranmza GT em
> primeiro plano eles ficam desativados de propósito — assim você digita nos campos sem
> disparar comandos sem querer. Clique de volta no jogo antes de testar.

## 2.7 Plano B: a barra flutuante

Alguns jogos "engolem" as teclas do Numpad, e às vezes o NumLock atrapalha. Para esses casos,
ative **Mostrar barra flutuante** em *Geral › Config*: uma janelinha com os mesmos comandos em
botões, disparados por clique do mouse.

<p align="center"><img src="media/barra-flutuante.png" alt="Barra flutuante do Ranmza GT" width="560"></p>

Ela fica **sempre por cima de tudo** — inclusive de jogo em janela sem borda — e você a arrasta
pelo canhoto de pontinhos da esquerda para qualquer canto de qualquer monitor. O atalho
`NumpadSubtract` (o menos do teclado numérico) mostra e esconde a barra.

Os botões, da esquerda para a direita (passe o mouse sobre um para ver o nome):

| Ícone | O que faz |
|---|---|
| Colchetes (ciano) | Selecionar área de captura |
| Três linhas (roxo) | Traduzir (Parágrafo) |
| Traço (roxo) | Traduzir (Linha) |
| Três linhas (rosa) | Traduzir com I.A Vision (Parágrafo) |
| Traço (rosa) | Traduzir com I.A Vision (Linha) |
| X (vermelho) | Limpar overlay |
| Balão (verde) | Modo Legenda — ligar/desligar |
| Retângulo (verde) | Selecionar área da legenda |
| Quatro pontos (laranja) | Mostrar/ocultar áreas |

## 2.8 Trocando os atalhos

Se as teclas padrão não te servem — teclado sem numérico, conflito com os controles do jogo —
troque em **Geral › Atalhos**.

<p align="center"><img src="media/geral-atalhos.png" alt="Aba Geral › Atalhos" width="820"></p>

Cada ação tem uma tecla principal, escolhida na lista à direita, e três botões de modificador
(Ctrl, Alt e Shift) que você liga se quiser combinar.

> **Letra ou número como tecla principal exige um modificador** (Ctrl, Alt ou Shift), senão você
> dispararia o programa toda vez que digitasse no jogo. Teclas do Numpad, F1–F12 e as de
> navegação funcionam sozinhas.

As teclas do **Modo Tempo Real** não ficam aqui: por ser experimental, elas moram na aba
**Experimental**, e vêm sem tecla definida. Veja a
[seção 10](/Manual/modo-tempo-real-traducao-continua-no-lugar-experimental.md).

## Deu certo? E se não deu

Se a tradução apareceu sobre o jogo, está tudo pronto — siga para a
[seção 3](/Manual/uso-basico-no-dia-a-dia.md).

- **Nada aconteceu ao apertar o atalho** → a janela de configuração estava em foco, ou o jogo
  está "engolindo" as teclas do Numpad. Use a **barra flutuante** (passo 2.7) ou troque a tecla
  (passo 2.8).
- **A tradução aparece na aba Historico, mas não sobre o jogo** → o jogo está em *Tela cheia
  exclusiva*. Troque para *Janela sem borda*.
- **Saiu tradução errada ou embaralhada** → o OCR leu mal. Comece trocando o modo de
  agrupamento (`Numpad9` ↔ `Numpad8`) e veja a
  [seção 6](/Manual/configurando-a-traducao.md).

Outros problemas estão na [seção 13](/Manual/problemas-comuns-e-solucoes.md).

---
