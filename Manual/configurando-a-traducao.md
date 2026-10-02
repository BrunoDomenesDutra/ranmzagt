# 6. Configurando a tradução

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
deveria ficar junta), ajuste a **Sensibilidade do agrupamento**, em **Overlay › Captura**:

- Texto sendo **separado demais**? Aumente o valor (até 3,0).
- Texto sendo **juntado demais**? Diminua o valor (até 0,5).

Esse ajuste só afeta o modo Parágrafo — no modo Linha ele é ignorado.

<p align="center"><img src="media/ocr-sensibilidade.png" alt="Sensibilidade do agrupamento, em Overlay › Captura" width="820"></p>

<p align="center"><i>O ajuste fica na aba <b>Overlay › Captura</b>, no card <b>Ajuste Fino do Modo Parágrafo</b>.</i></p>

## Trocando o motor de OCR — e por que o OneOCR é o recomendado

O OCR é o leitor de texto: ele transforma em texto o que aparece na área marcada, para ser
traduzido. Ele é usado na captura de tela e no Modo Legenda, e quanto melhor ele lê, melhor a
tradução. Em **Geral › OCR** você escolhe entre dois:

- **WinOCR** (nativo do Windows) — já vem pronto, não precisa instalar nada, e é o padrão. Lê bem
  texto sobre fundo liso, mas se perde fácil quando o fundo atrás do texto tem detalhes, cores ou
  movimento, e só lê os idiomas cujo pacote está instalado no Windows.
- **OneOCR** (recomendado) — o leitor de texto da Ferramenta de Captura (Snipping Tool) do
  Windows 11. É o que você deve usar.

<p align="center"><img src="media/geral-ocr.png" alt="Aba Geral › OCR com o WinOCR" width="820"></p>

**Por que o OneOCR é bem superior:**

- **Lê com muito mais precisão.** Fontes estilizadas, texto com contorno, sombra ou efeito por
  cima, texto pequeno, texto sobre fundo cheio de detalhes — situações em que o WinOCR entrega
  letra trocada ou palavra faltando e o OneOCR lê certo.
- **Todos os idiomas de uma vez, sem configurar nada.** É um modelo único multilíngue (latim,
  japonês, chinês, coreano, cirílico…) com detecção automática: não existe "idioma do texto"
  para escolher, nem pacote de idioma do Windows para instalar. Um jogo que mistura inglês e
  japonês na mesma tela é lido do mesmo jeito.
- **Menos coisa para dar errado no dia a dia.** Sem pacote de idioma faltando e sem ter que
  trocar de idioma a cada jogo.

**Vale a pena o trabalho de pegar os arquivos?** Vale, e com folga. São três arquivos copiados
uma única vez — depois disso a qualidade da tradução inteira sobe junto, porque tudo o que vem
depois (agrupamento, tradução, legenda) depende do texto ter sido lido corretamente.

**O que ele exige:** os arquivos `oneocr.dll`, `oneocr.onemodel` e `onnxruntime.dll`. O programa
**não vai atrás deles sozinho**: quem copia é você, com um clique.

**No Windows 11 é um clique.** Escolha *OneOCR* em **Geral › OCR** (ou no passo OCR do guia) e use
o botão **Detectar e copiar**: o programa acha a Ferramenta de Captura instalada, copia os 3
arquivos para a pasta dele e já deixa tudo configurado. Se a Ferramenta de Captura não estiver
instalada, ou for uma versão sem os arquivos, ele avisa em vez de falhar em silêncio. Enquanto os
arquivos não forem copiados, o card mostra *"Não carregou"* e o OCR fica parado.

<p align="center"><img src="media/geral-ocr-oneocr.png" alt="Card do OneOCR, em Geral › OCR" width="820"></p>

<p align="center"><i>Com o <b>OneOCR</b> selecionado, o card traz o botão <b>Detectar e copiar</b>,
o campo da pasta e, abaixo, o passo a passo para o Windows 10.</i></p>

**No Windows 10 é manual**, porque **os arquivos só vêm na Ferramenta de Captura do Windows 11**
(o OneOCR em si roda nos dois). Copie os três de uma máquina com Windows 11 e aponte a pasta com
**Procurar...** — o passo a passo dentro do card traz o comando do PowerShell que mostra onde eles
estão.

Por usar uma API não oficial da Microsoft, uma atualização da Ferramenta de Captura pode quebrar a
integração; nesse caso, clique em **Detectar e copiar** de novo.

## Filtro de alfabeto da legenda

No Modo Legenda, o programa pode considerar só as letras de um alfabeto e ignorar o resto:
latino, japonês/chinês, coreano ou cirílico. Útil quando aparecem nomes, placas ou símbolos em
outro alfabeto perto da legenda. Fica em **Overlay › Legenda**, no card **Alfabeto da legenda
original**:

- Com o **OneOCR**, você escolhe o alfabeto na lista (padrão: *Qualquer alfabeto*).
- Com o **WinOCR**, o filtro segue sozinho o idioma escolhido em **Geral › Idioma**.

Exemplo: na cena abaixo, a legenda em inglês fica por cima de uma manchete de jornal em japonês.
Com *Qualquer alfabeto*, o programa lê as duas juntas e manda o japonês para a tradução no meio da
fala. Com *Latino*, ele ignora os caracteres japoneses e traduz só a legenda.

<p align="center"><img src="media/legenda-alfabeto-exemplo.png" alt="Legenda em inglês por cima de uma manchete em japonês" width="820"></p>

Vale só para o Modo Legenda; a captura de tela lê todo o texto da área.

## Fila rápida da OpenAI

Com a OpenAI escolhida, o card do modelo tem a opção **Fila rápida da OpenAI**. Ligada, a OpenAI
atende os seus pedidos antes, pelo dobro do preço por token. Ajuda quando a OpenAI está lenta. Vem
**desligada**: a chave é sua, então a conta dobrada só acontece se você ligar.

## IA no seu PC ou outro serviço

Muitos programas e serviços de IA aceitam o mesmo formato de pedido da OpenAI: LM Studio, Ollama,
llama.cpp, OpenRouter e outros. O tradutor **Compatível com OpenAI** conversa com qualquer um
deles. Você informa o endereço e o nome do modelo, e o programa manda o texto do jogo para lá.

**Configurando.** Em **Tradução › Tradutores**, escolha *Compatível com OpenAI* e preencha:

- **URL base** — o endereço do servidor, do jeito que o programa de IA mostra. Pode ser com ou
  sem `/chat/completions` no fim. Servidor no seu próprio PC costuma ser algo como
  `http://localhost:1234/v1` (LM Studio) ou `http://localhost:11434/v1` (Ollama).
- **Modelo** — o nome exato do modelo, como o servidor mostra. Não existe lista para escolher:
  cada servidor tem os seus.
- **O modelo aceita imagem** — ligue só se o modelo lê imagens. É o que libera o
  [Modo Vision](/Manual/modo-vision-quando-o-ocr-erra.md) nesse tradutor.
- **Chaves de API** — só se o serviço pedir. Servidor no seu PC geralmente não pede, e aí o
  campo fica vazio.

<p align="center"><img src="media/tradutores-openai-compat.png" alt="Tradutores com Compatível com OpenAI: URL base, Modelo, O modelo aceita imagem e Testar conexão" width="820"></p>

Depois clique em **Testar conexão**. Ele traduz uma palavra pelo servidor e mostra se deu certo
ou qual erro voltou. O botão só libera com a URL e o modelo preenchidos.

**Boas práticas**

- **Use um modelo que siga instruções.** Modelos muito pequenos às vezes respondem com
  comentários em vez da tradução, e essa resposta é descartada.
- **Servidor no mesmo PC divide a placa de vídeo com o jogo.** O jogo e a tradução podem ficar
  mais lentos. A legenda espera a resposta, então um modelo lento atrasa a legenda.
- **A primeira tradução pode demorar.** Muitos servidores só carregam o modelo na primeira
  chamada. O programa espera até 90 segundos por resposta neste tradutor.
- **Modelo de raciocínio:** o bloco `<think>` que alguns modelos escrevem antes da resposta é
  descartado.
- Com o servidor desligado aparece o alerta *"API compatível: servidor não responde"*. Sem URL
  ou sem modelo, *"API compatível: preencha URL e modelo"*.

---
