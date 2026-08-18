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
- Texto sendo **juntado demais**? Diminua o valor (até 0).

Esse ajuste só afeta o modo Parágrafo — no modo Linha ele é ignorado.

<p align="center"><img src="media/ocr-sensibilidade.png" alt="Sensibilidade do agrupamento, em Overlay › Captura" width="820"></p>

<p align="center"><i>O ajuste fica na aba <b>Overlay › Captura</b>, no card <b>Ajuste Fino do Modo Parágrafo</b>.</i></p>

## Melhorando o reconhecimento de texto difícil

Antes de mexer em filtro nenhum: se você ainda está no **WinOCR**, o ajuste que mais resolve é
trocar o motor de OCR para o **OneOCR** — veja *Trocando o motor de OCR*, logo abaixo. Com ele,
boa parte dos casos desta lista simplesmente deixa de existir.

Se o programa continua não detectando o texto direito (fontes pequenas, estilizadas, com
efeitos), vá em **Overlay › Captura** e ative o **Pré-processamento**. Algumas dicas rápidas:

- **Texto pequeno**: aumente o **Upscale** (2x ou 3x costuma resolver).
- **Fonte com contorno grosso**: aumente um pouco o **Sharpen**.
- **Texto com pouco contraste contra o fundo**: aumente o **Contraste**.
- **Texto claro sobre fundo escuro** (ou vice-versa, se estiver dando errado): tente
  **Inverter cores**.

<p align="center"><img src="media/captura-preprocessamento.png" alt="Card Pré-processamento OCR, em Overlay › Captura" width="820"></p>

<p align="center"><i>O card <b>Pré-processamento OCR</b>, em <b>Overlay › Captura</b>. Os filtros extras
(Threshold, Blur, Dilatação, Erosão) só entram com o <b>Avançado</b> ligado.</i></p>

Não sabe por onde começar? Use **Ferramentas › Lab** — lá dá para testar todas essas opções em
imagens de exemplo, ver o resultado em tempo real, e depois aplicar a configuração que funcionou
melhor direto na Captura ou na Legenda.

## Trocando o motor de OCR — e por que o OneOCR é o recomendado

Em **Geral › OCR** você escolhe qual "motor" lê o texto da tela. São dois:

- **WinOCR** (nativo do Windows) — já vem pronto, não precisa instalar nada. É a opção que
  funciona no primeiro minuto de uso, mas tropeça em fontes estilizadas de jogo e só lê os
  idiomas cujo pacote está instalado no Windows.
- **OneOCR** (recomendado) — o motor de OCR da Ferramenta de Captura (Snipping Tool) do
  Windows 11. É o que você deve usar.

**Por que o OneOCR é bem superior:**

- **Qualidade de reconhecimento muito acima do WinOCR.** Fontes estilizadas, texto com
  contorno, sombra ou efeito por cima, texto pequeno, texto sobre fundo movimentado — situações
  em que o WinOCR entrega letra trocada ou palavra faltando e o OneOCR lê certo.
- **Todos os idiomas de uma vez, sem configurar nada.** É um modelo único multilíngue (latim,
  japonês, chinês, coreano, cirílico…) com detecção automática: não existe "idioma do texto"
  para escolher, nem pacote de idioma do Windows para instalar, nem aviso amarelo. Um jogo que
  mistura inglês e japonês na mesma tela é lido do mesmo jeito.
- **Você para de brigar com o pré-processamento.** Com o WinOCR, texto difícil vira uma sessão
  de ajuste de Upscale, Contraste, Sharpen e afins até acertar. O OneOCR costuma ler bem a
  imagem crua, então na maioria dos jogos dá para deixar o pré-processamento desligado e nunca
  mais mexer nele.
- **Menos coisa para dar errado no dia a dia.** Sem pacote de idioma faltando, sem reajustar
  filtro quando o jogo troca de fonte ou de cena.

**Vale a pena o trabalho de pegar os arquivos?** Vale, e com folga. São três arquivos copiados
uma única vez — depois disso a qualidade da tradução inteira sobe junto, porque tudo o que vem
depois (agrupamento, tradução, legenda) depende do texto ter sido lido corretamente. Nenhum
outro ajuste do programa muda tanta coisa de uma vez.

**O que ele exige:** os arquivos `oneocr.dll`, `oneocr.onemodel` e `onnxruntime.dll`.

**No Windows 11 é um clique.** Escolha *OneOCR* em **Geral › OCR** e use o botão **Detectar e
Copiar Automaticamente**: o programa acha o Snipping Tool instalado, copia os 3 arquivos para a
pasta dele e já deixa tudo configurado. Se o Snipping Tool não estiver instalado, ou for uma
versão sem os arquivos, ele avisa em vez de falhar em silêncio.

<p align="center"><img src="media/geral-ocr-oneocr.png" alt="Card de configuração do OneOCR, em Geral › OCR" width="820"></p>

<p align="center"><i>Com o <b>OneOCR</b> selecionado, o card traz o botão automático e, abaixo,
o passo a passo manual — que dá para recolher depois de instalar.</i></p>

**No Windows 10 é manual**, porque **os arquivos são exclusivos das versões do app do Windows
11** (o OneOCR em si roda nos dois). Copie os três de uma máquina com Windows 11 e aponte a
pasta — o passo a passo dentro do card traz o comando do PowerShell que mostra onde eles estão.

Por usar uma API não oficial da Microsoft, uma atualização do Snipping Tool pode quebrar a
integração; nesse caso, rode a detecção de novo (ou reextraia os arquivos).

---
