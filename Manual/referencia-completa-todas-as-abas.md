# 13. Referência completa — todas as abas

Esta seção descreve **cada aba e cada opção** da janela de configuração, na ordem em que
aparecem no menu da esquerda. É material de consulta — para o dia a dia, as seções anteriores
já bastam.

O menu tem cinco grupos com sub-itens (**Geral**, **Overlay**, **Traducao**, **Ferramentas**,
**Debug**) e três itens soltos embaixo (**Historico**, **Experimental**, **Sobre**).

## Geral › Config

Onde o programa opera.

<p align="center"><img src="media/geral-config.png" alt="Aba Geral › Config" width="820"></p>

- **Idioma do programa → Idioma da interface** — troca o idioma da própria janela de
  configuração (Português / Inglês). Não afeta os idiomas de OCR e tradução. Na primeira
  execução ele detecta o idioma do Windows (cai para Inglês se não for Português).
- **Configuração → Resetar para o padrão** — restaura todas as opções aos valores de fábrica.
  **Mantém** o monitor, as áreas selecionadas, as chaves de API e os prompts (System Prompt e
  Informações do Jogo).
- **Backend de captura → Backend** — como o programa lê os pixels da tela:
  - *Auto (recomendado)* — escolhe sozinho: WGC no Windows 11, DXGI no Windows 10, sem a borda
    amarela. A troca vale na hora, sem reiniciar.
  - *WGC (Windows 11)* — Windows Graphics Capture.
  - *DXGI (Windows 10)* — Desktop Duplication; existe para o Windows 10 não desenhar a borda
    amarela ao redor do monitor capturado.
- **Monitor → Tela ativa** — em qual monitor o programa captura, traduz e exibe. *Automático*
  usa o monitor principal do Windows. Trocar de monitor **limpa a área de captura** salva e
  **exige reiniciar** (botão "Reiniciar agora" aparece no rodapé da aba).
- **Barra flutuante → Mostrar barra flutuante** — liga a janelinha de botões sempre visível
  (veja o passo 2.7). Também abre e fecha pelo atalho `NumpadSubtract`, e ela **lembra a última
  posição** em que você a deixou.

## Geral › Idioma

O campo do idioma de origem **se adapta ao motor de OCR** escolhido na aba OCR.

<p align="center"><img src="media/geral-idioma.png" alt="Aba Geral › Idioma" width="820"></p>

- **Idioma do texto original**
  - Com *WinOCR* — o campo **Idioma do texto** recebe uma tag BCP-47 (`en`, `ja`, `ko`,
    `zh-Hans`, `pt`…). Se o pacote do idioma não estiver instalado no Windows, aparece um aviso
    com o botão **Instalar pacote de idioma**, que abre direto a tela de idiomas do Windows.
  - Com *OneOCR* — **detecção automática**; não há idioma de origem para configurar e o campo
    não aparece.
- **Idioma destino** — para qual idioma traduzir (`pt`, `es`, `fr`, `de`, `it`, `zh`…).

## Geral › OCR

Qual motor reconhece o texto e como ele agrupa as linhas.

<p align="center"><img src="media/geral-ocr.png" alt="Aba Geral › OCR" width="820"></p>

- **Engine de OCR → Engine ativo**
  - *WinOCR (padrão — nativo, ~30 ms)* — motor embutido no Windows: rápido, offline e sem
    dependência externa. O reconhecimento depende dos pacotes de idioma instalados no sistema.
    É o mais rápido, mas pode errar em fontes muito estilizadas de jogos.
  - *OneOCR (Snipping Tool — experimental, ~50–150 ms)* — modelo multilíngue com detecção
    automática de idioma. **Roda no Windows 10 e no 11**; o que é exclusivo do Windows 11 são os
    arquivos: `oneocr.dll`, `oneocr.onemodel` e `onnxruntime.dll` só vêm com o Snipping Tool do
    Windows 11. Você os copia de uma máquina com Win11 e aponta a pasta (o card traz o passo a
    passo, inclusive o comando do PowerShell para achar a pasta do Snipping Tool). Usa uma API
    não oficial da Microsoft — uma atualização do Snipping Tool pode quebrar a integração, e aí
    é só reextrair os arquivos.
  - O card de configuração do motor é **recolhível**: fica aberto enquanto a pasta não estiver
    configurada, e depois você pode fechá-lo.
- **Ajuste Fino do Modo Parágrafo → Sensibilidade do agrupamento** (0–3,0; padrão 1) —
  multiplicador sobre o espaçamento vertical típico entre linhas, usado para decidir se duas
  linhas pertencem ao mesmo parágrafo. Valores menores separam parágrafos com mais facilidade;
  maiores juntam linhas mais distantes num bloco só.

> **O modo não se escolhe aqui.** Parágrafo ou linha é decidido **na hora de capturar**, pelo
> atalho que você aperta: `Numpad8` (parágrafo) ou `Numpad9` (linha). Esta aba só afina como o
> modo Parágrafo agrupa.

## Geral › Atalhos

<p align="center"><img src="media/geral-atalhos.png" alt="Aba Geral › Atalhos" width="820"></p>

Dez atalhos globais — funcionam com o jogo em foco e ficam desativados enquanto a janela de
configuração está em primeiro plano. Cada um tem os modificadores **Ctrl / Alt / Shift** e uma
tecla principal, escolhida entre os grupos **Numpad**, **Função** (F1–F12), **Navegação**
(setas, Insert, Delete, Home, End, PageUp, PageDown), **Números** e **Letras**.

| Ação | Padrão |
|---|---|
| Selecionar área | `Numpad7` |
| Traduzir (modo linha) | `Numpad9` |
| Traduzir (modo parágrafo) | `Numpad8` |
| Traduzir com I.A Vision (modo parágrafo) | `Numpad5` |
| Traduzir com I.A Vision (modo linha) | `Numpad6` |
| Limpar overlay | `NumpadDecimal` |
| Ligar/desligar legenda | `Numpad0` |
| Selecionar área da legenda | `Numpad1` |
| Mostrar/ocultar áreas (preview) | `Numpad2` |
| Mostrar/esconder barra flutuante | `NumpadSubtract` |

> **Letras e números** como tecla principal **exigem** um modificador (Ctrl, Alt ou Shift) para
> não conflitar com o jogo, que usa WASD e os slots 0–9 o tempo todo. Numpad, F-keys e teclas de
> navegação funcionam sem modificador. Os grupos Números e Navegação salvam quem está em
> notebook sem teclado numérico.

O programa avisa se você repetir a mesma combinação em dois atalhos — um dos dois não seria
registrado.

Os atalhos do **Modo Tempo Real** não estão aqui: por ser experimental, eles ficam na aba
Experimental e vêm **sem tecla definida**.

## Overlay › Captura

Aparência da tradução manual e pré-processamento da imagem.

<p align="center"><img src="media/overlay-captura.png" alt="Aba Overlay › Captura" width="820"></p>

- **Texto**
  - *Fonte* — "Padrão do sistema (Arial)" ou qualquer fonte da pasta `fonts/`, com prévia ao
    lado.
  - *Cor do texto* — seletor de cor (padrão branco).
  - *Tamanho da fonte* — 8 a 72 pt.
  - *Altura da linha* — 0,80 a 2,00.
  - *Auto-fit* — reduz a fonte progressivamente para o texto caber no bloco sem cortar.
- **Fundo e Contorno** — são alternativos, ligar um desliga o outro.
  - *Mostrar fundo* + *Opacidade do fundo* (10–100%) — caixa escura atrás do texto.
  - *Mostrar contorno* + *Espessura* (2–5 px) — contorno preto ao redor de cada letra.
- **Exibição → Duração do overlay** — Nunca limpar automaticamente / 15 s / 30 s /
  **1 minuto (padrão)** / 2 / 5 / 10 minutos.
- **Pré-processamento OCR** — filtros aplicados à imagem antes do reconhecimento:
  - *Ativar pré-processamento* liga o bloco.
  - *Escala de cinza* · *Inverter cores*
  - *Contraste* (1,0–3,0×) · *Upscale* (1,0–4,0×) · *Sharpen* (0–2,0×)
  - *Avançado* — só é aplicado quando ligado: *Threshold* (0–255), *Blur* (0–5,0×),
    *Dilatação* (0–10 px), *Erosão* (0–10 px).

## Overlay › Legenda

O Modo Legenda tem aparência e pré-processamento **próprios**, independentes da aba Captura.

<p align="center"><img src="media/overlay-legenda.png" alt="Aba Overlay › Legenda" width="820"></p>

- **Texto** — *Fonte*, *Cor do texto* e *Tamanho da fonte* (10–48 pt). Não tem altura de linha
  nem auto-fit.
- **Fundo e Contorno** — *Mostrar fundo* + *Opacidade* (10–100%) ou *Mostrar contorno* +
  *Espessura do contorno* (1–5 px).
- **Captura**
  - *Intervalo* — de quanto em quanto tempo a área é relida (25 ms a 5 s).
  - *Linhas visíveis* — quantas linhas de legenda manter na tela (1 a 8).
  - *Limpar após silêncio* — apaga a legenda se nenhum texto novo aparecer por X segundos
    (1 a 5 s).
  - *Desligar Modo Legenda após inatividade* — **desliga o modo**, não só esconde, depois desse
    tempo sem detectar texto na região: Nunca / 1 / 2 / 3 / 5 / 10 minutos.
- **Pré-processamento OCR** — os mesmos controles da aba Captura, porém independentes dela.

## Overlay › Web

Transmite as traduções para navegadores na rede local — e para o OBS.

<p align="center"><img src="media/overlay-web.png" alt="Aba Overlay › Web" width="820"></p>

- **Servidor Web**
  - *Servidor ativo* — sobe um servidor HTTP local, acessível por qualquer aparelho na mesma
    rede.
  - *Mostrar tradução na tela* — mantém o overlay mesmo com o servidor ligado; desligue para
    mandar **só** para o navegador/OBS.
  - *Porta* (1024–65535) — mostra também quantos clientes estão conectados.
- **Endereços** — `/captura` (com histórico e botão Limpar) e `/captura/obs` (fundo
  transparente, para usar como Browser Source no OBS), cada um com botão **Copiar**.
- **Aparência** — *Tema* · *Tamanho da fonte* (12–48 px) · *Negrito* · *Texto detectado* (mostra
  o original abaixo da tradução) · *Horário e serviço* · *Cores personalizadas*, que libera seis
  seletores: texto traduzido, texto original, horário, serviço (badge), fundo do card e borda do
  card.
- **Histórico → Entradas mantidas no buffer** (10–200).

## Traducao › Tradutores

Qual serviço traduz e com quais credenciais.

<p align="center"><img src="media/tradutores-deepl.png" alt="Aba Traducao › Tradutores com DeepL" width="820"></p>

- **Provedor de Tradução → Provedor ativo**
  - *Google Translate — gratuito, sem chave* — API não oficial, nada para configurar.
    **Não suporta o Modo Vision.**
  - *DeepL (requer chave de API)* — tradutor dedicado de alta qualidade; **não suporta o Modo
    Vision**. Não tem seleção de modelo, mas tem **Formalidade** (Padrão / Mais formal / Mais
    informal), que só afeta os idiomas-destino com suporte — PT-BR incluso — e é ignorada nos
    demais. Aproveita o campo **Informações do Jogo** (aba I.A) e, no Modo Legenda, as falas
    anteriores como contexto, sem custo extra.
  - *OpenAI*, *Anthropic (Claude)*, *Gemini* — motores de IA, exigem chave de API.
- **Autenticação** — aparece nos provedores com chave. As credenciais são **salvas por motor**,
  então trocar de serviço e voltar não apaga nada.
  - *Modelo* (motores de IA) — cada motor traz três faixas: rápida/econômica, melhor equilíbrio
    e qualidade superior.
    - OpenAI: GPT-4.1 nano · GPT-4.1 mini · GPT-4.1
    - Claude: Haiku 4.5 · Sonnet 5 · Opus 4.8
    - Gemini: 2.0 Flash · 2.5 Flash · 2.5 Pro
    - *Personalizado…* — última opção da lista: abre um campo livre onde você digita **qualquer
      ID de modelo** aceito pelo provedor, para usar um modelo mais novo sem esperar uma
      atualização do programa.
  - *Testar conexão* — faz uma chamada de teste com a chave e o modelo atuais e mostra na hora
    se está tudo certo ou qual erro voltou, em vez de você descobrir o problema no meio do jogo.
    Também existe no Google, para checar a conectividade.
- **Chaves de API** — card recolhível onde entra a credencial do motor selecionado (`sk-…`,
  `sk-ant-…`, `AIza…`, ou a chave DeepL `:fx` do plano gratuito). Ele **abre sozinho** enquanto
  nenhuma chave estiver preenchida.
  - *+ Adicionar chave* / *✕* — dá para cadastrar **quantas chaves quiser** no mesmo motor.
    Quando a chave em uso fica sem crédito ou bate no limite de requisições, a próxima da lista
    assume automaticamente; esgotadas todas, cai no Google Translate.
- **Uso do DeepL** — só com o DeepL selecionado: chamadas e caracteres traduzidos na sessão, mais
  a **cota da conta** (botão *Atualizar*); *Zerar sessão* reinicia a contagem. É o único motor
  com esse acompanhamento — os de IA não expõem o gasto pela chave.

<p align="center"><img src="media/tradutores-claude.png" alt="Tradutores com Anthropic (Claude) selecionado" width="820"></p>

## Traducao › I.A

Parâmetros do modelo e prompts.

<p align="center"><img src="media/ia.png" alt="Aba Traducao › I.A" width="820"></p>

- **Parâmetros do Modelo**
  - *Temperature* (0–2) — 0,0 literal · 0,3 recomendado · 1,0+ criativo.
  - *Max tokens* (256–4096) — tamanho da resposta; 1024 basta para tradução.
- **Contexto de Conversa → Falas anteriores** (0–20) — no Modo Legenda, envia as últimas falas
  (original + tradução) como contexto, para a IA manter consistência de termos e tom.
  0 desativa; recomendado 3–5.
- **System Prompt** — papel do tradutor e regras gerais, com botões **Salvar** e **Restaurar
  padrão** (que recupera o texto de fábrica só deste campo).
- **Informações do Jogo** — tema, personagens e glossário; mude a cada jogo. Mesmos botões.

> Com o Google Translate ativo, os cards que não se aplicam ficam marcados em vermelho
> ("Só vale pros motores de IA…" e "O Google Translate não usa isso."). O **Contexto de
> Conversa** e as **Informações do Jogo** também valem para o DeepL.

<p align="center"><img src="media/ia-avisos.png" alt="Aba I.A com o Google Translate ativo, mostrando os avisos vermelhos" width="820"></p>

O reset geral (Geral › Config) **não** apaga o System Prompt nem as Informações do Jogo.

## Ferramentas › Inpaint

Reconstrução de fundo por IA (MI-GAN) — em desenvolvimento.

<p align="center"><img src="media/ferramentas-inpaint.png" alt="Aba Ferramentas › Inpaint" width="820"></p>

Em vez da caixa preta atrás da tradução, apaga o texto original da captura e reconstrói o fundo
com um modelo de inpainting rodando dentro do programa — a tradução fica parecendo nativa do
jogo. Vale para as **traduções manuais** (Traduzir e Vision); o Modo Legenda não usa. Custa
~50–200 ms por tradução e ~200 MB de RAM enquanto ativo.

- **Ativar fundo reconstruído** — só tem efeito com os arquivos configurados abaixo.
- **Ajuste fino da máscara**
  - *Dilatação da máscara* (0–12 px; padrão 3) — se depois de apagar o texto ainda sobra um
    resíduo de borda (o halo da fonte), aumente para o MI-GAN reconstruir um pouco além das
    letras.
  - *Limiar de detecção* (1,05–1,60; padrão 1,30) — limiar menor deixa a máscara mais sensível
    (pega mais halo, mas pode confundir fundo texturizado com texto).
  - Os dois valem **por captura**, sem reiniciar.
- **Instalação** — baixe `migan_pipeline_v2.onnx` (28 MB) e o `onnxruntime.dll` (de dentro do
  `onnxruntime-win-x64-1.26.0.zip`), coloque os dois na mesma pasta e aponte aqui
  (**Procurar** / **Verificar**). Trocar a pasta da `onnxruntime.dll` exige reiniciar o
  programa.

> Dica: ative o **Contorno** na aba Overlay › Captura, porque o fundo reconstruído pode ficar
> claro demais para texto branco.

## Ferramentas › Lab

Laboratório para testar o pré-processamento sem mexer no jogo.

<p align="center"><img src="media/ferramentas-lab-preprocessamento.png" alt="Aba Ferramentas › Lab" width="820"></p>

- **Imagem de Teste** — escolhe uma imagem PNG/JPG da pasta `images/lab_images/`, ao lado do
  executável.
- **Parâmetros de Pré-processamento** — os mesmos controles da aba Captura, com **prévia ao
  vivo**: a imagem original e a processada aparecem embaixo, lado a lado.
- **Aplicar em Captura** / **Aplicar em Legenda** — copiam a configuração que você acabou de
  testar para a aba correspondente.

Ligar *Avançado* revela Threshold, Blur, Dilatação e Erosão, para os casos difíceis:

<p align="center"><img src="media/ferramentas-lab-avancado.png" alt="Lab com os filtros avançados ligados" width="820"></p>

## Debug › Monitor

Latência de cada etapa do pipeline.

<p align="center"><img src="media/debug-monitor.png" alt="Aba Debug › Monitor" width="820"></p>

- **Monitoramento → Ativo** — registra os tempos de cada etapa a cada tradução. O histórico é
  mantido ao navegar entre abas.
- **Histórico de Execuções** — tabela das últimas 10 capturas: Hora, Captura, Preproc, OCR,
  Tradução, Total, Blocos, Cache (acertos sem chamar a API) e API (chamadas feitas).
- **Estatísticas** — mínimo, média e máximo de cada etapa.

## Debug › Imagem

Imagens de diagnóstico.

<p align="center"><img src="media/debug-imagem.png" alt="Aba Debug › Imagem" width="820"></p>

- **Modo Debug → Ativado** — salva imagens de diagnóstico a cada captura.
- **Imagens a salvar** — Captura original antes do pré-processamento (`frame.png`), Captura pós
  pré-processamento (`frame_proc.png`), Linhas do OCR (`ocr_lines.png`), Parágrafos agrupados
  (`ocr_paragraphs.png`) e Preview da máscara de inpainting (`mask.png`).
- **Pasta de output** — o caminho (padrão `images\ocr_debug_images`) e um botão para abrir a
  pasta.

## Debug › Logs

Log da sessão atual, em tempo real.

<p align="center"><img src="media/debug-logs.png" alt="Aba Debug › Logs" width="820"></p>

- **Logar textos capturados e traduções** — chave de privacidade, **desligada por padrão**.
  Deixe desligada ao mandar log para suporte, para não expor o conteúdo do jogo.
- **Filtrar linhas** · **Auto-scroll** · **Atualizar** — controles da visualização; erros saem
  em vermelho, avisos em amarelo.

## Historico

<p align="center"><img src="media/historico.png" alt="Aba Historico" width="820"></p>

Lista as traduções da **sessão atual** — horário, serviço, tradução e, abaixo, o texto original
— da mais recente para a mais antiga, até o limite definido em Overlay › Web. Clique numa
entrada para copiar a tradução. Botão **Limpar histórico**.

## Experimental

> Tudo nesta aba está **em desenvolvimento**: o comportamento pode mudar, bugs são esperados e
> recursos podem ser removidos.

<p align="center"><img src="media/experimental.png" alt="Aba Experimental" width="820"></p>

São três cards recolhíveis.

**Esconder overlay da captura de tela** — impede que a tradução desenhada por cima seja
recapturada pelo OCR (realimentação), o que atrapalha principalmente os modos contínuos. No Modo
Legenda, a tradução passa a substituir a legenda original no lugar. Efeito colateral: o overlay
também **some de gravações e transmissões** (OBS, Game Bar, compartilhamento de tela) — para
mostrar na live, use o servidor Web como Browser Source (seção 10).

**Modo Tempo Real (sobreposição ao vivo)** — tradução contínua desenhada no lugar do texto
original, sobre uma área própria.

<p align="center"><img src="media/experimental-tempo-real.png" alt="Card do Modo Tempo Real" width="820"></p>

- *Permitir Modo Tempo Real* — destrava a hotkey abaixo, que é quem liga e desliga a captura de
  fato. Com isso desligado, a hotkey não faz nada.
- Os dois atalhos — *Ligar/desligar Tempo Real* e *Selecionar área do Tempo Real* — moram aqui e
  vêm **sem tecla definida**; escolha as suas.
- *Intervalo* (25 ms–2 s) · *Tamanho da fonte* (10–48 pt) · *Mostrar fundo* + *Opacidade*
  (10–100%) · *Mostrar contorno* · *Limpar após silêncio* (0–10 s).
- *Estabilidade da posição* (0–60 px) e *Segurar em falha de OCR* (0–30 ticks) — contra tremor e
  piscada quando o fundo é animado.
- Tem ainda um pré-processamento de imagem exclusivo. Veja a **seção 9**.

> O card recomenda ligar **Esconder overlay da captura** antes de usar o Tempo Real.

**Esperar texto completo (efeito máquina de escrever)** — só traduz depois que a fala termina de
aparecer, evitando traduzir frases ainda "sendo digitadas" na tela. Vale para o Modo Legenda e o
Modo Tempo Real.

<p align="center"><img src="media/experimental-typewriter.png" alt="Card do efeito máquina de escrever" width="820"></p>

- *Capturas estáveis exigidas* (2–8 frames) — quantas leituras seguidas precisam bater.
- *Limiar de "mesmo texto"* (80–99%) — o quanto duas leituras precisam se parecer para contarem
  como iguais.
- *Teto de espera* (0–4 s) — tempo máximo de espera antes de traduzir do jeito que está.

## Sobre

Informações do programa: ícone, nome e **versão** instalada, a lista de funcionalidades, o autor
e a **Licença de Uso** completa — o que é permitido (uso pessoal gratuito, distribuir cópias não
modificadas, criar conteúdo como vídeos e streams) e o que é proibido (modificar ou fazer
engenharia reversa, vender, redistribuir versões modificadas, uso comercial sem autorização,
remover créditos), além do aviso de garantia.
