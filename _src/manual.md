# Manual do Usuário — Ranmza GT

Guia prático de uso do **Ranmza GT**, o tradutor de jogos, visual novels, vídeos e qualquer
conteúdo em tela. Este manual explica **como usar** cada parte do programa, sem entrar em
detalhes técnicos.

---

## Sumário

1. [O que o programa faz](#1-o-que-o-programa-faz)
2. [Configuração rápida](#2-configuração-rápida)
3. [Uso básico no dia a dia](#3-uso-básico-no-dia-a-dia)
4. [Atalhos de teclado](#4-atalhos-de-teclado)
5. [Configurando a tradução](#5-configurando-a-tradução)
6. [Deixando a tradução com a "cara" do jogo](#6-deixando-a-tradução-com-a-cara-do-jogo)
7. [Modo Vision — quando o OCR erra](#7-modo-vision--quando-o-ocr-erra)
8. [Modo Legenda — tradução automática contínua](#8-modo-legenda--tradução-automática-contínua)
9. [Modo Tempo Real — tradução contínua no lugar (experimental)](#9-modo-tempo-real--tradução-contínua-no-lugar-experimental)
10. [Usando no OBS / transmissões](#10-usando-no-obs--transmissões)
11. [Histórico e desempenho](#11-histórico-e-desempenho)
12. [Problemas comuns e soluções](#12-problemas-comuns-e-soluções)
13. [Referência completa — todas as abas](#13-referência-completa--todas-as-abas)

---

## 1. O que o programa faz

O Ranmza GT tira um "print" de uma área da tela, reconhece o texto que está nela, traduz e
mostra a tradução **por cima do jogo**, na mesma posição do texto original — como se fosse uma
legenda flutuante.

Funciona com qualquer jogo, visual novel, vídeo ou programa que mostre texto na
tela.

> **⚠️ Requisito essencial: o jogo precisa estar em modo Janela ou Janela sem borda.** O Ranmza
> GT desenha a tradução **por cima** da janela do jogo — então rode o jogo em **modo Janela**
> (*Windowed*) ou, de preferência, **Janela sem borda** (*Borderless* / *Fullscreen sem borda*),
> que ocupa a tela inteira e ainda deixa a tradução aparecer por cima. Em **Tela cheia exclusiva**
> (*Exclusive Fullscreen*) o Windows entrega a tela só para o jogo e nenhum programa consegue
> desenhar sobre ela — a tradução não vai aparecer. Sintoma típico: você aperta Traduzir, a
> tradução até surge na aba **Histórico**, mas nada aparece sobre o jogo. Solução: troque o jogo
> para **Janela sem borda** nas opções de vídeo dele.

O fluxo básico é sempre:

1. Você escolhe **onde** está o texto (uma área da tela).
2. Aperta um atalho para **traduzir**.
3. A tradução aparece sobreposta ao jogo.
4. Aperta outro atalho para **limpar** quando quiser, ou ela some sozinha depois de um tempo.

---

## 2. Configuração rápida

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

### 2.1 Primeiro olhar: como a janela é organizada

<p align="center"><img src="media/geral-config.png" alt="Aba Geral › Config" width="820"></p>

O menu da esquerda agrupa as opções por assunto. Nesta configuração rápida você só encosta em
**Geral** e **Traducao** — o resto existe para quando você quiser afinar alguma coisa.

| Menu | O que tem dentro |
|---|---|
| **Geral** | Config (monitor, tema, barra flutuante), Idioma, OCR e Atalhos |
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

### 2.2 Escolha o monitor

Ainda em **Geral › Config**, no card **Monitor**, escolha em **Tela ativa** onde o programa vai
trabalhar. Com um monitor só, deixe em *Automatico* e siga em frente.

Trocar de monitor **exige reiniciar o programa** — aparece um aviso com o botão **Reiniciar
agora** no rodapé da aba. Só depois do reinício a captura, o seletor de área e a tradução na
tela passam a valer para a outra tela. A área que você já tinha selecionado é apagada na troca.

O **Backend de captura** logo acima pode ficar em *Auto (recomendado)*: ele usa o método certo
para a sua versão do Windows sozinho e troca na hora, sem reiniciar.

### 2.3 Escolha os idiomas

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
> não se aplica. O **Idioma destino** continua valendo normalmente. O motor de OCR se troca em
> *Geral › OCR*, mas para começar deixe no padrão.

### 2.4 Escolha o tradutor

Abra **Traducao › Tradutores**.

<p align="center"><img src="media/tradutores-google.png" alt="Aba Traducao › Tradutores com Google Translate" width="820"></p>

O padrão é o **Google Translate — gratuito, sem chave**: não precisa configurar nada, já está
pronto para uso. É com ele que você deve fazer o primeiro teste.

Quando quiser mais qualidade, troque em **Provedor ativo**:

- **DeepL** — tradutor dedicado, muito natural, com opção de formalidade. Precisa de chave de
  API, mas tem **plano gratuito** (as chaves terminam em `:fx`, e o programa reconhece sozinho
  qual servidor usar).
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

> Só os motores de IA (OpenAI, Claude, Gemini) suportam o **Modo Vision** — o Google Translate e
> o DeepL não. Veja a [seção 7](/Manual/modo-vision-quando-o-ocr-erra.md).

### 2.5 Marque a área do texto

Com o jogo aberto e em foco, aperte **`Numpad7`**. A tela escurece e você arrasta o mouse para
desenhar um retângulo sobre a região onde o texto aparece — normalmente a caixa de diálogo.
Solte o botão para confirmar, ou aperte `ESC` para cancelar.

A área fica salva. Você só precisa marcar de novo se o jogo mudar a posição da caixa de texto
ou se você trocar a resolução.

> Não marcou nenhuma área? O programa captura a **tela inteira** — funciona, mas fica mais lento
> e erra mais. Vale marcar.

### 2.6 Traduza

Com o texto na tela, aperte um dos dois atalhos de tradução — a diferença é só **como as linhas
são agrupadas** antes de traduzir:

| Atalho | Modo | Use quando |
|---|---|---|
| **`Numpad9`** | **Linha** | Menus, listas, itens, botões — cada linha é uma coisa separada |
| **`Numpad8`** | **Parágrafo** | Diálogos e textos corridos — junta as linhas próximas num bloco só |

Na dúvida, comece pelo `Numpad8` em jogos de história e pelo `Numpad9` em menus.

A tradução aparece por cima do jogo, na posição do texto original, e some sozinha depois de um
tempo. Para tirá-la na hora, aperte **`NumpadDecimal`** (a vírgula do teclado numérico).

> **Os atalhos só funcionam com o jogo em foco.** Com a janela de configuração do Ranmza GT em
> primeiro plano eles ficam desativados de propósito — assim você digita nos campos sem
> disparar comandos sem querer. Clique de volta no jogo antes de testar.

### 2.7 Plano B: a barra flutuante

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

### 2.8 Trocando os atalhos

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
[seção 9](/Manual/modo-tempo-real-traducao-continua-no-lugar-experimental.md).

### Deu certo? E se não deu

Se a tradução apareceu sobre o jogo, está tudo pronto — siga para a
[seção 3](/Manual/uso-basico-no-dia-a-dia.md).

- **Nada aconteceu ao apertar o atalho** → a janela de configuração estava em foco, ou o jogo
  está "engolindo" as teclas do Numpad. Use a **barra flutuante** (passo 2.7) ou troque a tecla
  (passo 2.8).
- **A tradução aparece na aba Historico, mas não sobre o jogo** → o jogo está em *Tela cheia
  exclusiva*. Troque para *Janela sem borda*.
- **Saiu tradução errada ou embaralhada** → o OCR leu mal. Comece trocando o modo de
  agrupamento (`Numpad9` ↔ `Numpad8`) e veja a
  [seção 5](/Manual/configurando-a-traducao.md).

Outros problemas estão na [seção 12](/Manual/problemas-comuns-e-solucoes.md).

---

## 3. Uso básico no dia a dia

> **Importante**: os atalhos de teclado só funcionam com a **janela do jogo em foco**. Se a
> janela de configuração do Ranmza GT estiver aberta e selecionada (em primeiro plano), os
> atalhos ficam desativados — clique de volta no jogo (ou minimize a configuração) antes de
> usar `Numpad9`, `Numpad7`, etc.

1. Jogue normalmente.
2. Quando aparecer um texto que você quer traduzir, aperte **Traduzir** (padrão `Numpad9`).
3. A tradução aparece na tela, na posição do texto original.
4. Ela some sozinha depois de um tempo (configurável), ou aperte **Limpar overlay** (padrão
   `NumpadDecimal`) para tirá-la na hora.
5. Se o texto do jogo mudar antes da tradução sumir, é só apertar **Traduzir** de novo — a
   tradução antiga é limpa automaticamente antes da nova captura.

### Não confia nos atalhos do teclado?

Ative a **barra flutuante** na aba **Geral**. É uma janelinha compacta que fica **sempre por
cima de qualquer janela** — inclusive jogos em tela cheia (sem borda) — com os 7 comandos
principais à mão: selecionar área, traduzir, traduzir com Vision, limpar, ligar/desligar Modo
Legenda, selecionar área da legenda e mostrar/ocultar áreas (passe o mouse sobre um botão para
ver o nome).

Os três trunfos dela:

- **Fica sempre visível, acima de tudo** — não some atrás do jogo nem precisa de Alt+Tab.
- **Move livremente entre monitores** — arraste para qualquer canto da tela, em qualquer monitor.
- **Funciona quando o teclado não funciona** — alguns jogos "engolem" ou bloqueiam as teclas do
  Numpad (ou o NumLock atrapalha). Como a barra dispara as ações por clique do mouse, ela
  contorna isso completamente: é o plano B garantido para quando os atalhos não respondem.

### Conferindo se as áreas estão certas

Aperte **Mostrar/ocultar áreas** (padrão `Numpad2`) para desenhar retângulos coloridos
mostrando onde o programa vai capturar (e, se o Modo Legenda estiver configurado, onde a
legenda aparece). Aperte de novo para esconder. Não traduz nada, é só um guia visual.

---

## 4. Atalhos de teclado

| Atalho | Padrão | O que faz |
|---|---|---|
| Selecionar área | `Numpad7` | Abre o seletor para escolher onde está o texto |
| Traduzir | `Numpad9` | Captura, traduz e mostra na tela |
| Traduzir com IA Vision | `Numpad4` | Igual ao "Traduzir", mas usando IA mais inteligente (veja seção 7) |
| Limpar tradução | `NumpadDecimal` (vírgula do Numpad) | Esconde a tradução exibida |
| Ligar/desligar Modo Legenda | `Numpad0` | Ativa a tradução automática contínua (veja seção 8) |
| Selecionar área da legenda | `Numpad1` | Escolhe onde está a legenda do jogo |
| Mostrar/ocultar áreas | `Numpad2` | Mostra os retângulos das áreas configuradas |
| Ligar/desligar Modo Tempo Real | `Numpad3` | Tradução contínua no lugar, experimental (veja seção 9) |
| Selecionar área do Tempo Real | `Numpad6` | Escolhe a área que o Modo Tempo Real vai traduzir |
| Mostrar/ocultar barra flutuante | `NumpadSubtract` (menos do Numpad) | Abre ou fecha a barra flutuante de botões (veja seção 3) |

Todos podem ser trocados na aba **Atalhos** — escolha outra tecla e, se quiser, combine com
Ctrl/Alt/Shift. Se escolher uma **letra** como atalho, é **obrigatório** usar pelo menos um
modificador (Ctrl, Alt ou Shift), para não atrapalhar os controles normais do jogo.

> Os atalhos só funcionam quando a janela do jogo está em foco (ou seja, quando a janela de
> configuração do Ranmza GT não está em primeiro plano). Assim você pode digitar normalmente
> nos campos da configuração sem disparar comandos sem querer.

---

## 5. Configurando a tradução

### Tipo de texto: diálogo ou menu?

Na aba **OCR**, em "Agrupamento de Blocos", escolha:

- **Modo Parágrafo** (padrão) — junta linhas próximas em um único bloco de tradução. Use para
  **diálogos, falas de personagens, textos corridos** (visual novels, JRPGs).
- **Modo Linha** — cada linha vira uma tradução separada. Use para **menus, inventário, status,
  HUD** — onde cada linha é uma informação independente e não deve ser misturada com a de cima
  ou de baixo.

Se o programa estiver juntando falas que deveriam ser separadas (ou separando uma fala que
deveria ficar junta), ajuste o controle **"Sensibilidade do agrupamento"** que aparece no Modo
Parágrafo:
- Texto sendo **separado demais**? Aumente o valor (até 3.0).
- Texto sendo **juntado demais**? Diminua o valor (até 0).

### Melhorando o reconhecimento de texto difícil

Se o programa não está detectando o texto direito (fontes pequenas, estilizadas, com efeitos),
vá na aba **Captura** e ative o **Pré-processamento**. Algumas dicas rápidas:

- **Texto pequeno**: aumente o **Upscale** (2x ou 3x costuma resolver).
- **Fonte com contorno grosso**: aumente um pouco o **Sharpen**.
- **Texto com pouco contraste contra o fundo**: aumente o **Contraste**.
- **Texto claro sobre fundo escuro** (ou vice-versa, se estiver dando errado): tente
  **Inverter cores**.

Não sabe por onde começar? Use a aba **Lab** — lá dá para testar todas essas opções em imagens
de exemplo, ver o resultado em tempo real, e depois aplicar a configuração que funcionou
melhor direto na Captura ou na Legenda.

### Trocando o motor de OCR (avançado)

Se mesmo com pré-processamento o reconhecimento continuar ruim, a aba **OCR** permite trocar
o "motor" de reconhecimento de texto:

- **WinOCR** (padrão) — rápido, já vem pronto, mas pode errar em fontes muito estilizadas.
- **OneOCR** (experimental, Windows 11) — o motor de OCR da Ferramenta de Captura (Snipping
  Tool), muito melhor que o WinOCR em fontes estilizadas e multilíngue automático (não precisa
  configurar idioma de origem). Você copia 3 arquivos do próprio Windows para uma pasta sua —
  o card na aba OCR mostra o passo a passo. Por usar uma API não oficial da Microsoft, uma
  atualização do Snipping Tool pode parar de funcionar; nesse caso, basta reextrair os arquivos.

---

## 6. Deixando a tradução com a "cara" do jogo

Na aba **Captura**, seção de aparência:

- **Fonte**: escolha entre as fontes incluídas na pasta `fonts/` ou use a fonte padrão do
  Windows.
- **Tamanho da fonte** e **Altura da linha**: ajuste para o texto ficar legível e bem
  espaçado.
- **Auto-fit**: deixe ativado para o programa **diminuir a fonte automaticamente** até a
  tradução inteira caber no espaço do texto original — assim o texto nunca é cortado. Dica: com
  o Auto-fit ligado, deixe o **Tamanho da fonte** no máximo — o programa encontra sozinho o
  maior tamanho que exibe a tradução completa preenchendo bem a área, e subir mais o controle
  não muda mais nada.
- **Fundo**: desenha uma caixa escura atrás do texto (com opacidade ajustável), para garantir
  legibilidade sobre qualquer cenário.
- **Contorno**: alternativa ao fundo — desenha uma borda preta nas letras, sem caixa visível,
  para um visual mais discreto/integrado.

> Fundo e contorno são opções alternativas — ativar uma desativa a outra automaticamente.

### Quanto tempo a tradução fica na tela

Em "Exibição", escolha por quanto tempo a tradução permanece visível depois de aparecer: 15s,
30s, 1 minuto (padrão), 2, 5 ou 10 minutos — ou "Nunca" (a tradução só some quando você apertar
o atalho de limpar ou traduzir de novo).

---

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

## 8. Modo Legenda — tradução automática contínua

Para cenas com diálogo contínuo (cutscenes, modo automático de visual novels, vídeos com
legenda), o Modo Legenda traduz **sozinho, repetidamente**, sem você precisar apertar nada.

### Como configurar

1. Na aba **Legenda**, ajuste as opções de captura (intervalo, quantas linhas mostrar, etc.) —
   os padrões já funcionam bem para a maioria dos casos.
2. Aperte **Selecionar área da legenda** (padrão `Numpad1`) e desenhe um retângulo sobre onde a
   legenda/diálogo aparece no jogo.
3. Aperte **Ligar/desligar Modo Legenda** (padrão `Numpad0`) para ativar.

A partir daí, o programa fica de olho naquela área, traduzindo automaticamente sempre que um
texto novo aparecer e ficar "parado" por um instante (isso evita traduzir letras aparecendo uma
por uma em efeitos de "máquina de escrever").

As traduções aparecem **acima** da área selecionada, em ordem (mais recente embaixo), e somem
sozinhas se nenhum texto novo aparecer por alguns segundos.

### Deixando a IA "lembrar" das falas anteriores

Se você está usando OpenAI, Claude ou Gemini, a aba **IA** tem um controle **"Falas
anteriores"** (0 a 20, padrão 5). Com ele ligado, a IA recebe as últimas falas já traduzidas
como referência antes de traduzir a próxima — isso ajuda a manter os mesmos nomes, termos e
tom ao longo de uma conversa. Se notar que a IA está mudando o nome de um personagem ou o tom
da tradução de uma fala para outra, aumente esse valor; se preferir que cada fala seja
traduzida sem depender das anteriores, deixe em 0.

> O **DeepL** também aproveita as falas anteriores como contexto, **sem custo extra** — ele
> recebe as últimas falas como referência (seguindo o mesmo controle **"Falas anteriores"**)
> para manter a consistência de nomes e termos. Mesmo não sendo uma IA conversacional, isso
> deixa a tradução contínua mais coesa. **Google Translate** não usa esse contexto.

### Aparência separada

A aba Legenda tem suas próprias opções de fonte, fundo e contorno — independentes da tradução
manual — então você pode deixar a legenda contínua menor/mais discreta e a tradução manual
(`Numpad9`) maior, por exemplo.

### Desligando

Aperte **Numpad0** novamente (ou o botão correspondente, se você tiver criado um na barra
flutuante). A legenda na tela é limpa imediatamente.

---

## 9. Modo Tempo Real — tradução contínua no lugar (experimental)

> Recurso **experimental** — ligado e configurado pela aba **Experimental**. O comportamento
> ainda pode mudar e bugs são esperados.

O Modo Tempo Real junta o melhor dos outros dois modos: é **contínuo e automático** como o
Modo Legenda (não precisa apertar nada a cada fala), mas desenha a tradução **no lugar do texto
original**, sobre cada linha detectada, como o modo Traduzir — em vez de empilhar tudo numa
caixa fora da área. Ele trabalha sobre uma **área própria**, normalmente maior que a da legenda
(cobre a caixa de diálogo inteira, o nome do personagem, várias linhas de uma vez).

É indicado para conversas com NPCs em que aparecem **nome + várias linhas de fala** ao mesmo
tempo, e você quer tudo traduzido ao vivo, na posição original, sem clicar.

### Como usar

1. Na aba **Experimental**, ajuste as opções do Tempo Real (intervalo, fonte, fundo, contorno,
   desligamento automático) — os padrões já funcionam.
2. Aperte **Selecionar área do Tempo Real** (padrão `Numpad6`) e desenhe o retângulo sobre a
   região onde o texto aparece.
3. Aperte **Ligar/desligar Modo Tempo Real** (padrão `Numpad3`) para ativar. A tradução passa a
   aparecer sobreposta, atualizando sozinha conforme o texto muda.
4. Aperte `Numpad3` de novo para desligar.

> Por ser contínuo e desenhar várias áreas ao vivo, o Tempo Real é mais pesado que os outros
> modos. Se notar travadas, aumente o **intervalo** na aba Experimental.

### Estabilidade com fundo animado

Em cenas com fundo em movimento (animações de jogos de RPG, vídeos), o reconhecimento de texto
pode oscilar de um quadro para outro, fazendo a tradução **tremer** ou **piscar**. Dois ajustes
na aba Experimental controlam isso:

- **Estabilidade da posição** — quantos pixels o texto precisa andar para a tradução ser
  reposicionada. Maior = tradução mais "parada" (ignora o tremor); menor = acompanha o texto
  mais de perto. (Padrão: 12px.)
- **Segurar em falha de OCR** — por quantos ciclos uma tradução continua na tela quando o
  reconhecimento falha por um instante, evitando a piscada. Maior = segura mais tempo; menor =
  some mais rápido. (Padrão: 6.)

Regra prática: se ainda **tremer**, aumente a *Estabilidade da posição*; se ainda **piscar**,
aumente o *Segurar em falha de OCR*.

### Efeito máquina de escrever (typewriter)

Muitos jogos revelam o texto **letra por letra**. Para não traduzir frases pela metade, ligue
**Máquina de escrever** na aba Experimental: o programa espera o texto "assentar" (parar de
mudar) antes de traduzir. Vale tanto para o Modo Tempo Real quanto para o Modo Legenda. Dá para
ajustar quão estável o texto precisa ficar e o tempo máximo de espera antes de traduzir mesmo
assim.

---

## 10. Usando no OBS / transmissões

Se você transmite ou grava o jogo e quer que **a tradução apareça também no vídeo/stream**
(ou só no vídeo, sem aparecer no jogo em si), use a aba **Web**:

1. Ative o **servidor**.
2. Copie o endereço `/captura/obs` mostrado na aba.
3. No OBS, adicione uma fonte do tipo **"Navegador" (Browser Source)** e cole esse endereço.
   Essa versão da página tem fundo transparente, pronta para sobrepor à captura do jogo.
4. (Opcional) Ative **"Mostrar tradução na tela"** para **desligar o overlay normal** e deixar
   a tradução aparecer **só** na página do navegador/OBS — útil se a captura do OBS já inclui a
   janela do overlay e você não quer ver a tradução duplicada.

Você também pode personalizar tema (claro/escuro/dracula), cores, tamanho da fonte, e se quer
mostrar o texto original junto com a tradução, horário e qual serviço foi usado.

A página também pode ser aberta em qualquer navegador da rede local (celular, segundo monitor,
etc.) usando o endereço `/captura` mostrado na aba.

---

## 11. Histórico e desempenho

- **Aba Histórico**: mostra as traduções feitas durante a sessão atual (texto original,
  tradução, horário e serviço usado). Tem um botão para limpar.
- **Aba Monitor**: liga um registro das últimas traduções com o tempo que cada etapa levou
  (captura, reconhecimento, tradução, total) — útil para perceber se alguma configuração está
  deixando o programa lento (por exemplo, pré-processamento muito pesado).
- **Uso do DeepL** (aba **Tradutores**, com o DeepL selecionado): mostra quantos **caracteres** o
  DeepL traduziu nesta sessão e a **cota da conta** (caracteres usados/limite do período de
  cobrança) — clique em "Atualizar" para consultar. É exclusivo do DeepL.

---

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
→ Confira a aba Histórico/Monitor para ver se a tradução está sendo feita. Falhas passageiras
(limite de requisições, servidor fora do ar por um instante, queda de conexão) são **tentadas de
novo automaticamente** uma vez antes de recorrer ao Google Translate. Se você tiver **mais de uma
chave** cadastrada para o motor, ele ainda tenta as demais chaves da lista antes do fallback. Se
aparecer um aviso amarelo de "fallback para Google Translate" — e no Histórico a tradução vier
marcada como "Google Translate (fallback)" —, quer dizer que o serviço configurado (OpenAI, Claude,
Gemini) falhou em **todas** as chaves; confira suas chaves de API e créditos na aba Tradutores.

**"Apareceu um aviso vermelho de erro"**
→ Geralmente indica chave de API inválida, créditos esgotados, ou o serviço fora do ar
temporariamente. Confira a aba Tradutores. Se o aviso disser que a resposta foi **cortada no
limite de tokens**, aumente o **Max Tokens** na aba I.A (acontece só em blocos de texto muito
grandes).

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

## 13. Referência completa — todas as abas

Esta seção descreve **cada aba e cada opção** da janela de configuração, na ordem em que
aparecem na barra lateral. Use como consulta — para o dia a dia, as seções anteriores já
bastam.

### Geral

Onde o programa opera.

- **Backend de captura** — como o programa lê os pixels da tela:
  - *Auto (recomendado)* — escolhe sozinho: WGC no Windows 11, DXGI no Windows 10.
  - *WGC (Windows 11)* — Windows Graphics Capture; no Win11 captura sem a borda amarela.
  - *DXGI (Windows 10)* — Desktop Duplication; existe para o Windows 10 não desenhar a borda
    amarela/dourada ao redor do monitor capturado. A troca é aplicada na hora, sem reiniciar.
- **Monitor → Tela ativa** — em qual monitor o programa captura, traduz e exibe. *Automático*
  usa o monitor principal do Windows. Trocar de monitor **limpa a área de captura** salva e
  **exige reiniciar** (botão "Reiniciar agora" aparece logo abaixo).
- **Barra flutuante → Mostrar barra flutuante** — liga a janelinha de botões sempre visível,
  arrastável entre monitores (veja a seção 3). Também pode ser aberta/fechada pelo atalho
  **Mostrar/ocultar barra flutuante** (padrão `NumpadSubtract`), e ela **lembra a última posição**
  em que você a deixou.
- **Configuração → Resetar para o padrão** — restaura todas as opções aos valores de fábrica.
  **Mantém** o monitor, as áreas selecionadas, as chaves de API e os prompts (System Prompt e
  Informações do Jogo).
- **Idioma da interface** — troca o idioma da própria tela de configuração (Português/Inglês).
  Detecta automaticamente o idioma do Windows na primeira vez (cai para Inglês se não for
  Português); pode ser trocado manualmente aqui a qualquer momento.

### Idioma

O campo do idioma de origem **se adapta ao motor de OCR** selecionado na aba OCR.

- **Idioma do texto original**:
  - *WinOCR* — uma tag BCP-47 (ex.: `en`, `ja`, `ko`, `zh-Hans`, `pt`). Se o pacote do idioma
    não estiver instalado no Windows, aparece um aviso vermelho com o botão **Instalar pacote
    de idioma** (abre direto a tela de idiomas do Windows).
  - *OneOCR* — **detecção automática**; não há idioma de origem para configurar.
- **Idioma destino** — para qual idioma traduzir (ex.: `pt`, `es`, `fr`, `de`, `it`, `zh`).

### Captura

Aparência da tradução manual e pré-processamento da imagem.

- **Texto**
  - *Fonte* — "Padrão do sistema (Segoe UI)" ou qualquer fonte da pasta `fonts/`.
  - *Tamanho da fonte* — 8 a 72 pt.
  - *Altura da linha* — 0,80 a 2,00 (espaçamento entre linhas).
  - *Auto-fit* — reduz a fonte progressivamente para o texto caber no bloco sem cortar.
- **Fundo e Contorno** (são alternativos — ligar um desliga o outro)
  - *Mostrar fundo* + *Opacidade do fundo* (10–100%) — caixa escura atrás do texto.
  - *Mostrar contorno* + *Espessura* (2–5 px) — contorno preto ao redor de cada letra.
- **Exibição → Duração do overlay** — Nunca limpar / 15 s / 30 s / **1 minuto (padrão)** /
  2 / 5 / 10 minutos.
- **Pré-processamento OCR** — filtros aplicados à imagem antes do reconhecimento:
  - *Ativar pré-processamento* (liga a seção)
  - *Escala de cinza* · *Inverter cores*
  - *Contraste* (1,0–3,0×) · *Upscale* (1,0–4,0×) · *Sharpen* (0–2,0×)
  - *Avançado* (só é aplicado quando ligado): *Threshold* (0–255), *Blur* (0–5,0×),
    *Dilatação* (0–10 px), *Erosão* (0–10 px).

### Legenda

Tem aparência e pré-processamento **próprios**, independentes da aba Captura.

- **Captura**
  - *Intervalo* — de cada quanto tempo a área é relida (50 ms a 5 s).
  - *Linhas visíveis* — quantas linhas de legenda manter na tela (1 a 8).
  - *Limpar após silêncio* — limpa a legenda se nenhum texto novo aparecer por X segundos (1 a 5 s).
- **Aparência do Overlay**
  - *Tamanho da fonte* (10–48 pt)
  - *Mostrar fundo* + *Opacidade* (10–100%)
  - *Mostrar contorno* + *Espessura do contorno* (1–5 px)
- **Pré-processamento OCR** — mesmos controles da aba Captura, mas independentes.

### Atalhos

Dez atalhos globais (funcionam com o jogo em foco; desativados quando a janela de config está
em primeiro plano). Cada um tem os modificadores **Ctrl / Alt / Shift** e a tecla principal,
escolhida entre os grupos **Numpad**, **Função** (F1–F12), **Navegação** (setas, Insert, Delete,
Home, End, PageUp, PageDown), **Números** (0–9 da fileira superior) e **Letras**: Selecionar
área · Traduzir · Traduzir com IA Vision · Limpar overlay · Ligar/desligar legenda · Selecionar
área da legenda · Mostrar/ocultar áreas · Ligar/desligar Tempo Real · Selecionar área do Tempo
Real · Mostrar/ocultar barra flutuante.

> **Letras e números** como tecla principal **exigem** um modificador (Ctrl, Alt ou Shift) para
> não conflitar com o jogo (jogos usam WASD e os slots 0–9 o tempo todo). Numpad, F-keys e as
> teclas de navegação funcionam sem modificador. Os grupos Números e Navegação são úteis em
> notebooks sem teclado numérico.

### Tradutores

- **Provedor de Tradução → Provedor ativo**:
  - *Google Translate* — gratuito, sem chave. **Não suporta o Modo Vision.**
  - *DeepL* — exige chave (com plano gratuito; chaves `:fx` usam o servidor gratuito
    automaticamente). Tradutor dedicado de alta qualidade; **não suporta o Modo Vision**. Sem
    seleção de modelo, mas com **Formalidade** (Padrão / Mais formal / Mais informal) — afeta os
    idiomas com suporte, incluindo PT-BR. O DeepL também aproveita o campo **Informações do Jogo**
    (aba IA) e, no Modo Legenda, as falas anteriores, como contexto para traduzir melhor (sem
    custo extra). Com o DeepL selecionado, aparece ainda o card **Uso do DeepL** (caracteres
    traduzidos na sessão + **Cota da conta** via botão "Atualizar"; "Zerar sessão" reinicia a
    contagem). É o único motor com esse acompanhamento — os de IA não expõem o gasto pela chave.
  - *OpenAI*, *Anthropic (Claude)*, *Gemini* — exigem chave de API.
- **Autenticação** (aparece para os provedores com chave; as configurações são **salvas por motor
  independentemente**, então trocar e voltar não apaga nada):
  - *Formalidade* (só DeepL) — mais formal / mais informal / padrão.
  - *Modelo* (motores de IA) — cada motor oferece três faixas: uma **rápida/econômica**, uma de
    **equilíbrio** e uma **top** (qualidade superior).
    - OpenAI: GPT-4.1 nano · GPT-4.1 mini · GPT-4.1.
    - Claude: Haiku 4.5 · Sonnet 5 · Opus 4.8.
    - Gemini: 2.0 Flash · 2.5 Flash · 2.5 Pro.
    - *Personalizado…* — última opção do seletor: abre um campo de texto livre para você
      digitar **qualquer ID de modelo** aceito pelo provedor. Serve para usar um modelo mais
      novo que ainda não está na lista, sem esperar uma atualização do programa (o backend
      ajusta os parâmetros sozinho, inclusive para os modelos de raciocínio da OpenAI).
  - *Testar conexão* — faz uma chamada de teste ao provedor com a(s) chave(s) e o modelo atuais e
    mostra na hora se está tudo certo (✓, com a tradução de exemplo) ou o erro retornado (✗),
    em vez de você só descobrir o problema ao traduzir. Também disponível no Google (verifica a
    conectividade).
- **Chaves de API** (card recolhível, o **último** da aba; no DeepL fica logo antes do card *Uso
  do DeepL*): onde você cadastra a credencial do motor selecionado (`sk-...`, `sk-ant-...`,
  `AIza...`, ou a chave DeepL `:fx` do plano gratuito). As chaves são **salvas por motor**, então
  trocar de serviço e voltar não apaga nada.
  - *Adicionar chave* / *✕* — você pode cadastrar **quantas chaves quiser** para o mesmo motor.
    Quando a chave em uso **fica sem crédito** ou bate no limite de requisições, a tradução tenta a
    **próxima chave da lista** automaticamente e passa a usá-la; esgotadas todas, cai no fallback do
    Google Translate. Útil em sessões longas, que estouram a cota de uma só chave.
  - O card **abre sozinho** enquanto nenhuma chave estiver preenchida e pode ser **recolhido**
    depois de configurado.

### IA

As três primeiras seções só aparecem com um provedor de IA selecionado (não no Google).

- **Parâmetros do Modelo**
  - *Temperature* (0–2) — 0,0 literal · 0,3 recomendado · 1,0+ criativo.
  - *Max tokens* (256–4096) — tamanho da resposta; 1024 é suficiente para tradução.
- **Contexto de Conversa → Falas anteriores** (0–20) — no Modo Legenda, envia as últimas falas
  (original + tradução) como contexto para manter consistência de termos e tom. 0 = desativado;
  recomendado 3–5.
- **System Prompt** — papel do tradutor e regras gerais (botões **Salvar** e **Restaurar
  padrão**, que recupera o texto de fábrica só deste campo).
- **Informações do Jogo** — tema, personagens e glossário; mude por jogo (botões **Salvar** e
  **Restaurar padrão**). O reset geral (aba Geral) **não** apaga este campo nem o System Prompt.

### OCR

- **Engine de OCR → Engine ativo**:
  - *WinOCR* (padrão) — nativo do Windows, ~30 ms, offline; depende dos pacotes de idioma
    instalados. Pode errar em fontes muito estilizadas.
  - *OneOCR* (experimental, Windows 11) — motor do Snipping Tool, ~50–150 ms, multilíngue
    automático. Usa API não oficial da Microsoft; você copia 3 arquivos do próprio Windows
    (`oneocr.dll`, `oneocr.onemodel`, `onnxruntime.dll`) e aponta a pasta (botões Procurar /
    Verificar — a pasta é configurada automaticamente se válida). O card com o passo a passo é
    **recolhível**: enquanto a pasta não estiver configurada ele fica sempre aberto (para o
    tutorial ficar visível); depois de configurado, você pode recolhê-lo e ele **lembra** essa
    escolha entre sessões.
- **Agrupamento de Blocos** — como as linhas detectadas são combinadas antes de traduzir:
  - *Modo Parágrafo* — agrupa linhas verticalmente próximas (diálogos, texto corrido). Mostra
    *Sensibilidade do agrupamento* (0–3,0; padrão 1): menor separa mais, maior junta mais.
  - *Modo Linha* — cada linha vira um bloco independente (menus, HUD).

### Web

Transmite as traduções para navegadores na rede local (e para o OBS).

- **Servidor Web**
  - *Servidor ativo* — inicia o servidor HTTP local.
  - *Mostrar tradução na tela* — exibe o overlay mesmo com o servidor ligado; desligue para
    enviar **só** ao navegador/OBS.
  - *Porta* (1024–65535) — mostra também quantos clientes estão conectados.
- **Endereços** — `/captura` (com histórico e botão Limpar) e `/captura/obs` (fundo
  transparente, para Browser Source no OBS), com botão Copiar.
- **Aparência** — *Tema* (Dark / Light / Dracula) · *Tamanho da fonte* (12–48 px) · *Negrito* ·
  *Texto detectado* (mostra o original) · *Horário e serviço* · *Cores personalizadas* (libera
  6 seletores de cor: texto traduzido, texto original, horário, serviço/badge, fundo do card,
  borda do card).
- **Histórico → Entradas mantidas no buffer** (10–200).

### Histórico

Lista as traduções da **sessão atual** (horário, serviço, tradução e, abaixo, o texto
original), da mais recente para a mais antiga, até o limite definido na aba Web. Botão **Limpar
histórico**.

### Lab

Laboratório para testar o pré-processamento sem afetar o jogo.

- **Imagem de Teste** — escolhe uma imagem da pasta `images/lab_images/` (ao lado do executável).
- **Parâmetros de Pré-processamento** — os mesmos controles da aba Captura, com **preview ao
  vivo** (imagem original × processada).
- Botões **Aplicar em Captura** e **Aplicar em Legenda** — copiam a configuração testada para a
  aba correspondente.

### Monitor

- **Monitoramento → Ativo** — registra o tempo de cada etapa do pipeline a cada tradução
  (mantido ao navegar entre abas).
- **Histórico de Execuções** — tabela das últimas 10 capturas: Hora, Captura, Preproc, OCR,
  Tradução, Total, Blocos, Cache (acertos sem API) e API (chamadas feitas).
- **Estatísticas** — mín / média / máx de cada etapa (a partir de 2 execuções).

### Debug

- **Modo Debug → Ativado** — salva imagens de diagnóstico a cada captura na pasta de output.
- **Imagens a salvar** — Captura original (`frame.png`), Captura pós pré-processamento
  (`frame_proc.png`), Linhas do OCR (`ocr_lines.png`), Parágrafos agrupados
  (`ocr_paragraphs.png`), Preview da máscara de inpainting (`mask.png`).
- **Pasta de output** — caminho dos arquivos + botão para abrir a pasta.

### Logs

Log da sessão em tempo real.

- **Logar textos capturados e traduções** — toggle de privacidade; **desativado por padrão**.
  Mantenha desligado ao compartilhar logs para suporte, para não expor o conteúdo do jogo.
- **Filtrar linhas** · **Auto-scroll** · **Atualizar** — controles da visualização (erros em
  vermelho, avisos em amarelo, etc.).

### Experimental

> Tudo nesta aba está **em desenvolvimento** — o comportamento pode mudar, bugs são esperados e
> recursos podem ser removidos.

- **Fundo reconstruído por IA (MI-GAN)** — em vez da caixa preta, apaga o texto original da
  captura e reconstrói o fundo com um modelo de inpainting (MI-GAN) rodando dentro do programa;
  a tradução é desenhada por cima, como se fosse nativa do jogo. Funciona nas **traduções
  manuais** (Traduzir e Vision); o Modo Legenda não usa. Custa ~50–200 ms por tradução e
  ~200 MB de RAM enquanto ativo. Requer baixar `migan_pipeline_v2.onnx` (28 MB) e
  `onnxruntime.dll`, colocá-los na mesma pasta e apontar (Procurar / Verificar). Dica: ative o
  **Contorno** na aba Captura, pois o fundo reconstruído pode ficar claro.
- **Modo Tempo Real** — tradução contínua desenhada **no lugar** do texto original, sobre uma
  área própria. Tem suas próprias opções de intervalo, fonte, fundo, contorno e desligamento
  automático, ajustes de estabilidade (*Estabilidade da posição* e *Segurar em falha de OCR*,
  contra tremor/piscada com fundo animado) e um pré-processamento de imagem exclusivo. Atalhos
  `Numpad3` (liga/desliga) e `Numpad6` (selecionar área). Veja a **seção 9**.
- **Máquina de escrever (efeito typewriter)** — espera o texto parar de mudar antes de traduzir,
  evitando traduzir frases que ainda estão "sendo digitadas" na tela. Vale para o Modo Legenda e
  o Modo Tempo Real. Ajuste quão estável o texto precisa ficar e o tempo máximo de espera.
- **Esconder overlay da captura de tela** — impede que a tradução desenhada por cima seja
  recapturada pelo OCR (realimentação), útil principalmente nos modos contínuos. Vale para o
  overlay principal e o da legenda. Efeito colateral: o overlay também **some de gravações e
  transmissões** (OBS, Game Bar, compartilhamento de tela) — nesses casos use o **servidor web**
  (seção 10) para mostrar a tradução.
