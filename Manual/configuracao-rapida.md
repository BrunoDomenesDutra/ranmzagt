# 2. Configuração rápida

Na primeira vez que você abre o programa, o **Guia de configuração** aparece sozinho e passa por
tudo o que precisa ser escolhido. Siga o guia e você já sai traduzindo; o resto desta seção
explica cada passo com mais calma, para quem pulou o guia ou quer entender o que escolheu.

| Passo | O que fazer | Onde |
|---|---|---|
| 1 | Escolher o monitor | guia ou aba **Geral › Config** |
| 2 | Escolher o leitor de texto (OCR) | guia ou aba **Geral › OCR** |
| 3 | Escolher os idiomas | guia ou aba **Geral › Idioma** |
| 4 | Escolher o tradutor | guia ou aba **Tradução › Tradutores** |
| 5 | Marcar a área do texto | atalho `Numpad7`, com o jogo aberto |
| 6 | Traduzir | atalho `Numpad9` (linha) ou `Numpad8` (parágrafo) |

> **Antes de tudo: o jogo em modo Janela.** Em *Tela cheia exclusiva* nenhum programa consegue
> desenhar por cima — a tradução simplesmente não aparece. Troque o jogo para **Janela sem
> borda** nas opções de vídeo dele. Explicação completa na
> [seção 1](/Manual/o-que-o-programa-faz.md).

> **O programa nem abriu, com erro *"VCRUNTIME140.dll não foi encontrado"*?** Falta o
> **Microsoft Visual C++ Redistributable (x64)**, um componente gratuito da Microsoft que a
> maioria dos PCs já tem (vem junto com muitos jogos). Instale por este link oficial e abra o
> programa de novo:
> <https://aka.ms/vs/17/release/vc_redist.x64.exe>

## 2.1 O Guia de configuração

O guia é uma janela por cima da tela de configurações, com oito passos:

| Passo | O que você escolhe |
|---|---|
| **Início** | Nada: explica como o programa funciona e os dois jeitos de traduzir |
| **Monitor** | Em qual monitor o jogo fica, e o que essa escolha muda |
| **OCR** | WinOCR ou OneOCR, com os prós e contras de cada um. Com o OneOCR, o botão para copiar os arquivos dele |
| **Idiomas** | O idioma do texto do jogo e o idioma em que você quer ler |
| **Tradução** | O serviço de tradução e a chave dele, se precisar, com uma lista de qual escolher |
| **Captura** | Quanto tempo a tradução da captura de tela fica na tela, fonte, cor e Auto-fit |
| **Legenda** | Fonte, cor e o filtro de alfabeto do Modo Legenda |
| **Pronto** | Um resumo do que você escolheu e as teclas para começar |

Tudo o que você muda no guia vale na hora, igual nas abas. Os passos no topo são clicáveis, para
voltar ou pular para outro. Com o **WinOCR**, o guia não passa do passo Idiomas sem um idioma
escolhido, porque sem ele o WinOCR não sabe o que ler.

- **Concluir**, no último passo, ou **Pular**, a qualquer momento, fecham o guia. Ele não volta
  sozinho depois disso.
- Fechar o programa no meio do guia faz ele aparecer de novo na próxima vez.
- Para ver o guia de novo, use o botão **Guia** no topo da tela.
- Criar um perfil com **Começar do zero** também abre o guia, para configurar o jogo novo.

## 2.2 Como a janela é organizada

<p align="center"><img src="media/geral-config.png" alt="Aba Geral › Config" width="820"></p>

O menu da esquerda agrupa as opções por assunto. Na configuração rápida você só encosta em
**Geral** e **Tradução** — o resto existe para quando você quiser afinar alguma coisa.

| Menu | O que tem dentro |
|---|---|
| **Geral** | Config (idioma da tela, aparência, atualizações, monitor, alertas), Perfis, Idioma, OCR e Atalhos (barra flutuante) |
| **Overlay** | Aparência da tradução na tela: Captura, Legenda e Web |
| **Tradução** | Tradutores (serviço e chaves de API) e I.A (prompts e contexto) |
| **Ferramentas** | Inpaint (apagar o texto original) |
| **Debug** | Monitor de desempenho e Logs |
| **Histórico** | As traduções da captura de tela na sessão atual |
| **Sobre** | Versão do programa, licença e links |

No topo da janela ficam o seletor de **Perfil**, o botão **Guia** e os botões **A−** e **A+**,
que diminuem e aumentam o texto da tela de configurações.

> **Idioma da interface** (em *Geral › Config*) muda só o idioma **do programa** — os menus e
> textos que você está vendo. Não tem nada a ver com o idioma que vai ser traduzido; esse é o
> passo 2.4.

## 2.3 Escolha o monitor

Em **Geral › Config**, no card **Monitor**, escolha em **Tela ativa** onde o jogo fica. Com um
monitor só, deixe em *Automático* e siga em frente.

O monitor escolhido é onde abrem a seleção das áreas, os alertas, a prévia das áreas e a barra
flutuante, até você arrastá-la. A tradução aparece no monitor onde a área foi marcada.

- **A troca vale na hora**, sem reiniciar.
- **Cada monitor guarda as próprias áreas.** Ao trocar de monitor, as áreas do monitor anterior
  ficam guardadas; ao voltar para ele, elas voltam. No primeiro uso de um monitor, marque as
  áreas nele.
- **Cada perfil guarda o próprio monitor.** Com um perfil por jogo, cada jogo volta no monitor
  dele.
- Se o monitor escolhido for desconectado, o programa usa o principal do Windows.

O **Backend de captura** logo acima pode ficar em *Auto (recomendado)*: ele usa o método certo
para a sua versão do Windows sozinho e troca na hora, sem reiniciar.

## 2.4 Escolha os idiomas

Abra **Geral › Idioma**.

<p align="center"><img src="media/geral-idioma.png" alt="Aba Geral › Idioma" width="820"></p>

- **Idioma do texto** — o idioma em que o jogo está. Com o WinOCR, a lista mostra só os idiomas
  que já têm o pacote de leitura de texto instalado no Windows. Numa instalação nova o campo vem
  vazio, com um aviso: escolha um da lista.
- **Idioma destino** — o idioma em que você quer ler. Português (Brasil) é o padrão.

> **O idioma do jogo não está na lista?** O WinOCR só lê idiomas cujo pacote está instalado no
> Windows. Instale em *Configurações → Hora e Idioma → Idioma e região* e abra o programa de novo.
> Se o Windows não tiver nenhum pacote com leitura de texto, o aviso traz o botão **Instalar
> pacote de idioma**, que abre essa tela.

> **Usando OneOCR?** Aí não existe idioma de origem para escolher: ele é um modelo único
> multilíngue (latim, japonês, chinês, coreano, cirílico…) que detecta o idioma sozinho, e o
> campo **Idioma do texto** nem aparece enquanto ele estiver selecionado. O **Idioma destino**
> continua valendo normalmente. O OneOCR é o motor **recomendado** e se escolhe em
> *Geral › OCR* — veja *Trocando o motor de OCR* na [seção 6](/Manual/configurando-a-traducao.md).

## 2.5 Escolha o tradutor

Abra **Tradução › Tradutores**.

<p align="center"><img src="media/tradutores-google.png" alt="Aba Tradução › Tradutores com Google Translate" width="820"></p>

O padrão é o **Google Translate — gratuito**: não precisa de chave nem de configuração, já está
pronto para uso. É com ele que você deve fazer o primeiro teste.

> **Gratuito, mas com limite.** O Google Translate sem chave aceita só um punhado de traduções
> num intervalo curto. Passou disso, aparece o alerta *"Google: limite de uso (429)"* e aquela
> captura fica sem tradução. Para traduzir uma fala aqui e ali ele dá conta; em sessão longa e no
> Modo Legenda o limite chega rápido. E o limite é contado **por endereço de IP** — quem usa
> internet móvel ou provedor com **CGNAT** divide esse limite com outros clientes e bate nele bem
> mais cedo. A explicação e o que fazer estão na [seção 12](/Manual/problemas-comuns-e-solucoes.md).

?> **Atenção: a API do Google usada aqui não é oficial.** É o mesmo endereço que a página do
Google Tradutor usa por baixo dos panos, sem chave e sem conta. Ela não é publicada nem
documentada, então o Google pode mudá-la ou tirá-la do ar quando quiser, sem aviso — e nesse dia
só voltam a traduzir os serviços com chave. Se você depende do programa para jogar, vale ter uma
chave de outro serviço já configurada.

Quando quiser mais qualidade, troque em **Provedor ativo**:

- **Google Cloud Translation**, **DeepL** e **Azure Translator** — tradutores dedicados. Precisam
  de chave de API e têm plano gratuito com limite por mês. No DeepL, as chaves do plano gratuito
  terminam em `:fx`, e o programa reconhece sozinho qual servidor usar. O DeepL também recebe as
  Informações do Jogo e as falas anteriores como contexto, sem custo extra. O Azure, além da chave,
  exige a **região** do recurso (as duas coisas ficam na mesma página do portal do Azure).
- **OpenAI**, **Anthropic (Claude)**, **Gemini** e **Groq** — IAs. Precisam de chave de API, e
  em troca entregam traduções mais naturais e consistentes, porque traduzem levando em conta as
  falas anteriores e as Informações do Jogo. OpenAI e Anthropic cobram por uso; Gemini e Groq têm
  plano gratuito. Escolha o modelo no card de autenticação e cole a chave em *Chaves de API*.
- **Compatível com OpenAI** — para usar uma IA que roda no seu PC (LM Studio, Ollama) ou outro
  serviço que não está na lista. Você informa o endereço e o nome do modelo. Veja
  [IA no seu PC ou outro serviço](/Manual/configurando-a-traducao.md) na seção 6.

<p align="center"><img src="media/tradutores-openai.png" alt="Aba Tradução › Tradutores com OpenAI" width="820"></p>

Cada serviço guarda as suas próprias chaves, então trocar de um para outro e voltar não apaga
nada. As chaves ficam guardadas **criptografadas** e só abrem neste PC, na sua conta do Windows.

> **Várias chaves com rotação automática.** Todo serviço com chave aceita **mais de uma**:
> clique em *+ Adicionar chave*. Se a chave em uso for recusada, ficar sem crédito ou bater no
> limite de requisições, o programa passa na hora para a próxima da lista; esgotadas todas, ele
> cai no Google Translate e mostra o alerta *"<serviço> falhou, usando Google"*. Ajuda bastante em sessões longas de Modo Legenda.

> Só a OpenAI, a Anthropic, o Gemini e o Compatível com OpenAI (quando o modelo aceita imagem)
> suportam o **Modo Vision** — o Google Translate, o Google Cloud, o DeepL, o Azure e a Groq não.
> Veja a [seção 8](/Manual/modo-vision-quando-o-ocr-erra.md).

## 2.6 Marque a área do texto

Com o jogo aberto e em foco, aperte **`Numpad7`**. A tela escurece e você arrasta o mouse para
desenhar um retângulo sobre a região onde o texto aparece — normalmente a caixa de diálogo.
Solte o botão para confirmar, ou aperte `ESC` para cancelar.

A área fica salva. Você só precisa marcar de novo se o jogo mudar a posição da caixa de texto
ou se você trocar a resolução.

> Sem área marcada, os atalhos de tradução não traduzem nada: aparece o alerta *"Captura sem
> área"*. Marque a área primeiro.

<div style="position:relative;padding-top:56.25%;max-width:820px;margin:0 auto">
  <iframe src="https://player.vimeo.com/video/1218016540"
          style="position:absolute;top:0;left:0;width:100%;height:100%;border:0"
          allow="fullscreen; picture-in-picture" allowfullscreen
          title="Marcando a área do texto"></iframe>
</div>

<p align="center"><i>Marcando a área do texto com o `Numpad7`.</i></p>

## 2.7 Traduza

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
> disparar comandos sem querer. Se você apertar um atalho com a configuração em foco, um alerta
> avisa. Clique de volta no jogo antes de testar.

## 2.8 Plano B: a barra flutuante

Alguns jogos "engolem" as teclas do Numpad, e às vezes o NumLock atrapalha. Para esses casos,
ative **Mostrar barra flutuante** em *Geral › Atalhos*: uma janelinha com os mesmos comandos em
botões, disparados por clique do mouse.

<p align="center"><img src="media/barra-flutuante.png" alt="Barra flutuante do Ranmza GT" width="560"></p>

Ela fica **sempre por cima de tudo** — inclusive de jogo em janela sem borda — e você a arrasta
pela alça de pontinhos da esquerda para qualquer canto de qualquer monitor. O atalho
`NumpadSubtract` (o menos do teclado numérico) mostra e esconde a barra.

Os botões, da esquerda para a direita (passe o mouse sobre um para ver o nome), em três grupos:

| Grupo | Botões |
|---|---|
| Captura de tela | Selecionar área · Traduzir (parágrafo) · Traduzir (linha) · Vision (parágrafo) · Vision (linha) · Limpar |
| Modo Legenda | Selecionar área da legenda · Ligar/desligar legenda |
| Prévia | Mostrar/ocultar áreas |

No canto direito, dois botões **+ / −** ajustam o tamanho da barra inteira na tela — útil em
monitores 4K ou muito pequenos. As cores dos botões seguem o tema da tela de configurações.

## 2.9 Trocando os atalhos

Se as teclas padrão não te servem — teclado sem numérico, conflito com os controles do jogo —
troque em **Geral › Atalhos**.

<p align="center"><img src="media/geral-atalhos.png" alt="Aba Geral › Atalhos" width="820"></p>

Cada ação tem uma tecla principal, escolhida na lista à direita, e três botões de modificador
(Ctrl, Alt e Shift) que você liga se quiser combinar. A troca vale na hora, sem reiniciar.

> **Letra ou número como tecla principal exige um modificador** (Ctrl, Alt ou Shift), senão você
> dispararia o programa toda vez que digitasse no jogo. Teclas do Numpad, F1–F12 e as de
> navegação funcionam sozinhas.

## Deu certo? E se não deu

Se a tradução apareceu sobre o jogo, está tudo pronto — siga para a
[seção 3](/Manual/uso-basico-no-dia-a-dia.md).

- **Nada aconteceu ao apertar o atalho** → a janela de configuração estava em foco, ou o jogo
  está "engolindo" as teclas do Numpad. Use a **barra flutuante** (passo 2.8) ou troque a tecla
  (passo 2.9).
- **A tradução aparece na aba Histórico, mas não sobre o jogo** → o jogo está em *Tela cheia
  exclusiva*. Troque para *Janela sem borda*.
- **Saiu tradução errada ou embaralhada** → o OCR leu mal. Comece trocando o modo de
  agrupamento (`Numpad9` ↔ `Numpad8`) e veja a [seção 6](/Manual/configurando-a-traducao.md).

Outros problemas estão na [seção 12](/Manual/problemas-comuns-e-solucoes.md).

---
