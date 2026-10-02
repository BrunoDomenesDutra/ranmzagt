# 13. Referência completa — todas as abas

Esta seção descreve **cada aba e cada opção** da janela de configuração, na ordem em que
aparecem no menu da esquerda. É material de consulta — para o dia a dia, as seções anteriores
já bastam.

O menu tem cinco grupos com sub-itens (**Geral**, **Overlay**, **Tradução**, **Ferramentas**,
**Debug**) e dois itens soltos embaixo (**Histórico** e **Sobre**).

## Geral › Config

<p align="center"><img src="media/geral-config.png" alt="Aba Geral › Config" width="820"></p>

- **Idioma do programa → Idioma da interface** — troca o idioma da própria janela de
  configuração (Português / Inglês) e dos alertas. Não afeta os idiomas de OCR e tradução. Na
  primeira execução ele segue o idioma do Windows (cai para Inglês se não for Português).
- **Aparência** — cores desta tela e da barra flutuante:
  - *Tema* — Escuro ou Claro.
  - *Daltônico* — paleta de cores acessível para daltonismo.
  - *Escala de cinza* — para acromatopsia.
- **Atualizações → Avisar sobre novas versões** — liga o aviso que aparece ao abrir o programa
  quando existe versão mais nova publicada (veja a seção 14).
- **Atualizações → Verificar agora** — consulta na hora se existe versão nova, mesmo com o
  aviso desligado.

<p align="center"><img src="media/geral-config-monitor.png" alt="Aba Geral › Config — reset, backend, monitor e alertas" width="820"></p>

<p align="center"><i>Rolando a mesma aba: <b>Configuração</b>, <b>Backend de captura</b>,
<b>Monitor</b> e <b>Alertas na tela</b>.</i></p>

- **Configuração → Resetar para o padrão** — restaura todas as opções aos valores de fábrica.
  **Mantém** o idioma e o tema da tela, o monitor, as áreas selecionadas, as chaves de API, as
  Informações do Jogo e a preferência de aviso de atualização.
- **Backend de captura → Backend** — como o programa lê os pixels da tela:
  - *Auto (recomendado)* — escolhe sozinho: WGC no Windows 11, DXGI no Windows 10, sem a borda
    amarela. A troca vale na hora, sem reiniciar.
  - *WGC (Windows 11)* — Windows Graphics Capture.
  - *DXGI (Windows 10)* — Desktop Duplication; existe para o Windows 10 não desenhar a borda
    amarela ao redor do monitor capturado.
- **Monitor → Tela ativa** — em qual monitor abrem a seleção das áreas, os alertas, a prévia das
  áreas e a barra flutuante. *Automático* usa o monitor principal do Windows. Vale na hora, sem
  reiniciar; cada monitor guarda as próprias áreas, e cada perfil guarda o próprio monitor.
- **Alertas na tela → Mostrar alertas** — avisos curtos no canto inferior direito, só em situação
  grave (limite de uso, chave, sem internet, OCR ou captura que falhou, atalho apertado com esta
  tela em foco) e ao ligar e desligar a legenda.

## Geral › Perfis

Um conjunto de configurações por jogo. O conceito e o passo a passo estão na
[seção 4](/Manual/perfis-um-conjunto-de-ajustes-por-jogo.md); aqui ficam só os controles.

<p align="center"><img src="media/geral-perfis.png" alt="Aba Geral › Perfis" width="820"></p>

- **Novo perfil → Nome do jogo** — o nome do perfil que vai ser criado.
  - **Duplicar o atual** — cria a partir de tudo que está valendo agora, **inclusive as áreas
    selecionadas**.
  - **Começar do zero** — cria com os valores de fábrica, no monitor atual, e abre o Guia de
    configuração.
  - Em ambos os casos o perfil criado **já fica ativo**, e daí em diante tudo que você mexer
    nas outras abas é gravado nele sozinho.
- **Seus perfis** — a lista, num card retrátil. O perfil ativo aparece destacado e marcado como
  *ativo*; clique em qualquer outro para ativá-lo na hora.
  - **Renomear** — troca o nome. O **Padrão** não tem este botão.
  - **Apagar** — pede confirmação (*Apagar mesmo*). O **Padrão** não pode ser apagado. Se o
    perfil apagado era o que estava em uso, o Padrão assume na hora.
- **O que muda ao trocar de perfil** — o resumo de quais opções acompanham o perfil e quais
  valem para todos.

## Geral › Idioma

O campo do idioma de origem **se adapta ao motor de OCR** escolhido em Geral › OCR.

<p align="center"><img src="media/geral-idioma.png" alt="Aba Geral › Idioma" width="820"></p>

- **Idioma do texto original**
  - Com *WinOCR* — lista dos idiomas com pacote de leitura de texto instalado no Windows, sem
    opção padrão: escolha o idioma do jogo. Sem escolha, aparece um aviso. Se o idioma salvo não
    estiver mais instalado, aparece o botão **Instalar pacote de idioma**, que abre a tela de
    idiomas do Windows.
  - Com *OneOCR* — **detecção automática**; não há idioma de origem para configurar.
- **Idioma destino** — para qual idioma traduzir: Português (Brasil), Português (Portugal),
  Español, English, Français, Deutsch, Italiano, 日本語, 한국어, 中文（简体）e Русский.

## Geral › OCR

Qual motor reconhece o texto na tela.

<p align="center"><img src="media/geral-ocr.png" alt="Aba Geral › OCR" width="820"></p>

- **Engine de OCR → Engine ativo**
  - *WinOCR (nativo do Windows)* — o padrão. Embutido no Windows, sem nada para instalar. Lê o
    idioma escolhido em Geral › Idioma; se perde em fundo com detalhes e em fonte muito
    estilizada.
  - *OneOCR (Ferramenta de Captura do Windows 11 — recomendado)* — modelo multilíngue com
    detecção automática de idioma, bem superior ao WinOCR em fontes de jogo (o porquê está na
    [seção 6](/Manual/configurando-a-traducao.md), em *Trocando o motor de OCR*). **Roda no
    Windows 10 e no 11**; o que é exclusivo do Windows 11 são os arquivos `oneocr.dll`,
    `oneocr.onemodel` e `onnxruntime.dll`. Usa uma API não oficial da Microsoft — uma
    atualização da Ferramenta de Captura pode quebrar a integração.
- **OneOCR** (aparece com o OneOCR selecionado)
  - *Estado* — mostra a pasta de onde o OneOCR carregou, ou *"Não carregou"* quando faltam os
    arquivos.
  - *Pasta dos arquivos* — vazia, usa a pasta onde o **Detectar e copiar** coloca os arquivos.
    **Procurar...** escolhe outra pasta e confere se os 3 arquivos estão nela.
  - *Detectar e copiar* — acha a Ferramenta de Captura instalada, copia os 3 arquivos e configura
    a pasta. Avisa quando o app não está instalado ou quando é uma versão sem os arquivos (o caso
    do Windows 10). **É o único jeito de o programa copiar os arquivos**: ele nunca vai atrás
    deles sozinho.
  - *Windows 10: copiar de um PC com Windows 11* — bloco recolhível com o passo a passo da cópia à
    mão.

## Geral › Atalhos

<p align="center"><img src="media/geral-atalhos.png" alt="Aba Geral › Atalhos — barra flutuante e atalhos globais" width="820"></p>

- **Barra flutuante → Mostrar barra flutuante** — liga a janelinha de botões sempre visível
  (veja o passo 2.8). Também abre e fecha pelo atalho `NumpadSubtract`, e ela **lembra a última
  posição** e o tamanho em que você a deixou.

Onze atalhos globais — funcionam com o jogo em foco e ficam pausados enquanto a janela de
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
| Retraduzir sem cache | `Numpad4` |
| Limpar overlay | `NumpadDecimal` |
| Ligar/desligar legenda | `Numpad0` |
| Selecionar área da legenda | `Numpad1` |
| Mostrar/ocultar áreas | `Numpad2` |
| Mostrar/esconder barra flutuante | `NumpadSubtract` |

> **Letras e números** como tecla principal **exigem** um modificador (Ctrl, Alt ou Shift) para
> não conflitar com o jogo, que usa WASD e os slots 0–9 o tempo todo. Numpad, F-keys e teclas de
> navegação funcionam sem modificador. Os grupos Números e Navegação salvam quem está em
> notebook sem teclado numérico.

O programa avisa se você repetir a mesma combinação em dois atalhos — um dos dois não seria
registrado. A troca de tecla vale na hora, sem reiniciar.

## Overlay › Captura

Aparência da tradução da captura de tela.

<p align="center"><img src="media/overlay-captura.png" alt="Aba Overlay › Captura" width="820"></p>

- **Exibição**
  - *Duração do overlay* — **1 minuto (padrão)**, 2, 5 ou 10 minutos.
  - *Esconder a tradução de gravações e transmissões* — a tradução continua visível na sua tela,
    mas some das capturas. Funciona só com programas rodando neste PC (OBS, Game Bar, NVIDIA
    ShadowPlay, etc); gravando por placa de captura, ela aparece assim mesmo.
- **Texto**
  - *Fonte* — "Padrão do sistema (Arial)", as fontes da pasta `fonts/` ou as do Windows, com
    prévia logo abaixo.
  - *Cor do texto* — seletor de cor (padrão branco).
  - *Tamanho da fonte* — 8 a 100 px.
  - *Altura da linha* — 1,00 a 2,00 vezes o tamanho da fonte.
  - *Auto-fit* — reduz a fonte até o texto caber no lugar do original.
- **Fundo e Contorno** — podem ser ligados juntos ou separados.
  - *Mostrar fundo* + *Opacidade do fundo* (10–100%) — caixa escura atrás do texto.
  - *Mostrar contorno* + *Espessura* (0,5–5 px) + *Cor do contorno* — contorno ao redor de cada
    letra.
- **Ajuste Fino do Modo Parágrafo → Sensibilidade do agrupamento** (0,5–3,0) — valores menores
  separam parágrafos com mais facilidade; maiores juntam linhas mais distantes num bloco só. O
  modo em si (parágrafo ou linha) **não se escolhe aqui**: é decidido na hora de capturar, pelo
  atalho — `Numpad8` (parágrafo) ou `Numpad9` (linha).

## Overlay › Legenda

O Modo Legenda tem aparência **própria**, independente de Overlay › Captura.

<p align="center"><img src="media/overlay-legenda.png" alt="Aba Overlay › Legenda" width="820"></p>

- **Posição da tradução → Colar no texto detectado** — desenha a tradução em cima da fala
  original, com as mesmas quebras de linha, em vez de acima da área. Mostra uma fala por vez, e
  fonte maior transborda a área. Nesse modo a legenda some das capturas feitas neste PC — é o que
  impede o OCR de reler a própria tradução. Ver a seção 9.
- **Texto** — *Fonte*, *Cor do texto* e *Tamanho da fonte* (10–48 px).
- **Fundo e Contorno** — *Mostrar fundo* + *Opacidade* (10–100%) e *Mostrar contorno* +
  *Espessura do contorno* (0,5–5 px) + *Cor do contorno*.

<p align="center"><img src="media/overlay-legenda-captura.png" alt="Aba Overlay › Legenda — Captura e alfabeto" width="820"></p>

- **Captura**
  - *Ignorar texto fora do centro da área* — ligada por padrão. Pula placas e letreiros perto das
    bordas da área; desligue em diálogo alinhado à esquerda.
  - *Falas na tela* — quantas falas ficam visíveis (1 a 8). Fica em 1 com *Colar no texto
    detectado* ligado.
  - *Tradução fica depois que a legenda some* — 1 a 3 s (padrão 2 s).
  - *Desligar a legenda sem texto na área* — **desliga o modo** depois desse tempo sem texto:
    Nunca / 1 / 2 / 5 / 10 minutos (padrão 1 minuto).
- **Alfabeto da legenda original** — só caracteres desse alfabeto são considerados na legenda;
  o resto é ignorado. Com o OneOCR, escolha *Qualquer alfabeto*, latino, japonês/chinês, coreano
  ou cirílico. Com o WinOCR, segue o idioma de Geral › Idioma, com o botão **Mudar idioma**.

## Overlay › Web

Transmite as traduções da captura de tela para navegadores na rede local — e para o OBS.

<p align="center"><img src="media/overlay-web.png" alt="Aba Overlay › Web" width="820"></p>

- **Servidor Web**
  - *Servidor ativo* — sobe um servidor HTTP local, acessível por qualquer aparelho na mesma
    rede.
  - *Mostrar tradução na tela* — mantém o overlay mesmo com o servidor ligado; desligue para
    mandar **só** para o navegador/OBS.
  - *Porta* — padrão 7474. Mostra também quantos clientes estão conectados.
- **Endereços** — `/captura` (com histórico e botão Limpar) e `/captura/obs` (fundo
  transparente, para usar como Browser Source no OBS), cada um com botão **Copiar**.

<p align="center"><img src="media/overlay-web-aparencia.png" alt="Aba Overlay › Web — aparência da página e histórico" width="820"></p>

<p align="center"><i>Rolando a mesma aba: <b>Aparência</b> da página web e o buffer do <b>Histórico</b>.</i></p>

- **Aparência** — *Tema* (Dark, Light ou Dracula) · *Tamanho da fonte* · *Negrito* · *Texto
  detectado* (mostra o original abaixo da tradução) · *Horário e serviço* · *Cores
  personalizadas*, que libera os seletores de cor da página.
- **Histórico → Entradas mantidas no buffer** — quantas traduções a página guarda para quem
  abre depois.

## Tradução › Tradutores

Qual serviço traduz e com quais chaves.

<p align="center"><img src="media/tradutores-google-cloud.png" alt="Aba Tradução › Tradutores com Google Cloud Translation" width="820"></p>

- **Provedor de Tradução → Provedor ativo**
  - *Google Translate — gratuito* — API não oficial, nada para configurar. É o mesmo endereço que
    a página do Google Tradutor usa internamente; como não é publicada nem documentada, o Google
    pode alterá-la ou desativá-la a qualquer momento. **Não suporta o Modo Vision.** Por ser
    gratuito, tem **limite de requisições**, contado por endereço de IP — o que fazer está na
    [seção 12](/Manual/problemas-comuns-e-solucoes.md).
  - *Google Cloud Translation* — a API oficial do Google, com chave criada no Google Cloud
    Console (*APIs e serviços › Credenciais*). **Não suporta o Modo Vision.**
  - *DeepL* — tradutor dedicado. A chave do plano gratuito termina em `:fx`, e o programa escolhe
    o servidor certo sozinho. **Não suporta o Modo Vision.**
  - *Azure Translator* — o tradutor da Microsoft; exige chave e **região** do recurso. **Não
    suporta o Modo Vision.**
  - *OpenAI*, *Anthropic (Claude)*, *Gemini* — IAs, com chave de API e Modo Vision.
  - *Groq* — IA com plano gratuito, com chave de API. **Não suporta o Modo Vision.**
- **Autenticação** — aparece nas IAs e no Azure.
  - *Modelo* (IAs) — cada uma traz uma lista curta. A primeira é o padrão.
    - OpenAI: GPT-5.4 mini (mais rápido, recomendado) · GPT-4.1 mini · GPT-4.1
    - Anthropic: Haiku 4.5 · Sonnet 5 · Opus 5
    - Gemini: 3.5 Flash-Lite · 3.6 Flash · 3.7 Flash
    - Groq: gpt-oss-20b · gpt-oss-120b
    - *Personalizado…* — última opção da lista: abre um campo livre onde você digita **qualquer
      ID de modelo** aceito pelo serviço, para usar um modelo mais novo sem esperar uma
      atualização do programa.
    - *Ver a lista completa de modelos do provedor* — abre no navegador a página oficial do
      serviço, com todos os modelos e os IDs exatos, para copiar para o *Personalizado…*.
  - *Fila rápida da OpenAI* — aparece abaixo do modelo, só com a OpenAI. **Vem desligada.**
    Ligada, a OpenAI atende antes, pelo dobro do preço por token.
  - *Região do recurso* (só no Azure) — **obrigatória**. Aceita a grafia do portal ("Brazil
    South"): maiúsculas e espaços são ajustados sozinhos. O link *Ver a lista oficial de regiões
    do Azure* abre a tabela da Microsoft no navegador. Chave e região saem da mesma página:
    <https://portal.azure.com> → o seu recurso de Translator → *Keys and Endpoint*.
- **Chaves de API** — card recolhível onde entra a chave do serviço selecionado. Ele **abre
  sozinho** enquanto nenhuma chave estiver preenchida. As chaves ficam guardadas criptografadas e
  só abrem neste PC, na sua conta do Windows.
  - *+ Adicionar chave* / *Apagar* — dá para cadastrar **quantas chaves quiser** no mesmo serviço.
    Quando a chave em uso é recusada, fica sem crédito ou bate no limite de requisições, a
    próxima da lista assume na hora; esgotadas todas, cai no Google Translate.
  - *Testar* — traduz uma palavra só com aquela chave, usando o modelo e a região escolhidos. O
    botão fica **verde** quando a chave funciona e **vermelho** quando falha. Passe o mouse em cima
    para ver o motivo, como "chave inválida", "sem crédito" ou "Sem internet". Editar a chave
    apaga o resultado.
  - *Testar todas* — testa as chaves da lista uma por vez e pinta o botão de cada uma.

<p align="center"><img src="media/tradutores-testar-chave.png" alt="Botões Testar: chave funcionando em verde e chave com problema em vermelho" width="820"></p>

<p align="center"><img src="media/tradutores-openai.png" alt="Tradutores com OpenAI selecionado" width="820"></p>

## Tradução › I.A

Contexto enviado às IAs.

<p align="center"><img src="media/ia.png" alt="Aba Tradução › I.A" width="820"></p>

- **Contexto de Conversa → Falas anteriores** (5–10, padrão 5) — no Modo Legenda, envia as
  últimas falas (original + tradução) como contexto, para a IA manter consistência de termos e
  tom. Cada fala a mais custa tokens em toda tradução.
- **System Prompt** — regras gerais do tradutor, para todos os jogos. Vem **em branco**, com um
  exemplo em cinza dentro do campo; nada é enviado à IA enquanto você não escrever o seu. Botões
  **Salvar** e **Restaurar padrão** (que esvazia o campo de novo). O idioma de destino não precisa
  estar aqui: o programa já manda para a IA o idioma escolhido na aba **Idioma**, e um pedido de
  outro idioma neste campo é ignorado. Regras concretas (glossário, manter nomes, não suavizar
  palavrões) funcionam em todos os modelos.
- **Informações do Jogo** — tema, personagens e glossário; mude a cada jogo. Também vem em
  branco, com exemplo em cinza. Mesmos botões.

> Com um tradutor que não é IA ativo, os cards ficam marcados em vermelho: eles só valem para
> OpenAI, Anthropic, Gemini e Groq.

O reset geral (Geral › Config) **não** apaga as Informações do Jogo.

## Ferramentas › Inpaint

Reconstrução de fundo por IA (MI-GAN).

<p align="center"><img src="media/ferramentas-inpaint.png" alt="Aba Ferramentas › Inpaint" width="820"></p>

Em vez da caixa escura atrás da tradução, apaga o texto original da captura de tela e reconstrói o
fundo com um modelo de inpainting rodando dentro do programa — a tradução fica parecendo nativa do
jogo. Vale para a **captura de tela** (Traduzir e Vision); o Modo Legenda não usa.

<div style="position:relative;padding-top:56.25%;max-width:820px;margin:0 auto">
  <iframe src="https://player.vimeo.com/video/1217778049"
          style="position:absolute;top:0;left:0;width:100%;height:100%;border:0"
          allow="fullscreen; picture-in-picture" allowfullscreen
          title="Fundo reconstruído por IA"></iframe>
</div>

<p align="center"><i>O fundo reconstruído no lugar da caixa escura atrás da tradução.</i></p>

- **Ativar fundo reconstruído** — só pode ser ligado depois de baixar o modelo, no card abaixo.
- **Ajuste fino da máscara** — valem **por captura**, sem reiniciar.
  - *Dilatação da máscara* (0–12 px; padrão 3) — se depois de apagar o texto ainda sobra um
    resíduo de borda (o halo da fonte), aumente para o MI-GAN reconstruir um pouco além das
    letras.
  - *Limiar de detecção* (1,05–1,50; padrão 1,30) — limiar menor deixa a máscara mais sensível
    (pega mais halo, mas pode confundir fundo texturizado com texto).
  - *Contorno* (0–16 px; padrão 8) — até onde o contorno da letra é apagado. Suba se sobrar
    mancha escura com texto de contorno grosso; 0 apaga só a letra, bom para texto sem contorno.
  - *Fundo* (0–150%; padrão 25%) — grão devolvido ao fundo gerado, para ele não ficar liso perto
    do cenário. Abaixe se o fundo ficar granulado demais.

### Baixar automaticamente

<p align="center"><img src="media/ferramentas-inpaint-baixar.png" alt="Card Baixar automaticamente, em Ferramentas › Inpaint" width="820"></p>

O recurso precisa do modelo do MI-GAN (27 MB), que não vem no `.zip` do programa. O card
**Baixar automaticamente** baixa e confere o modelo:

- *Pasta do modelo* — vazia, usa a pasta `models\inpaint`, ao lado do executável. **Procurar...**
  escolhe outra.
- *Baixar* — a barra mostra o andamento e o botão vira **Cancelar**. Cancelado ou interrompido, o
  download recomeça do zero na próxima vez.

O programa confere o **sha256** do arquivo antes de aceitá-lo. Arquivo que chega corrompido ou
diferente do esperado é apagado e o download falha com aviso — nunca fica um arquivo pela metade
se passando por bom.

> Dica: ative o **Contorno** na aba Overlay › Captura, porque o fundo reconstruído pode ficar
> claro demais para texto branco.

## Debug › Monitor

Tempo de cada etapa da captura de tela.

<p align="center"><img src="media/debug-monitor.png" alt="Aba Debug › Monitor" width="820"></p>

- **Monitoramento → Ativo** — registra os tempos de cada etapa a cada tecla da captura de tela.
  O histórico é mantido ao navegar entre abas.
- **Histórico de Execuções** — tabela das últimas 10 capturas: Hora, Captura, OCR, Tradução,
  Total, Blocos, Cache (acertos sem chamar a API) e API (chamadas feitas).
- **Estatísticas** — mínimo, média e máximo de cada etapa.

## Debug › Logs

Log desta execução, em tempo real.

<p align="center"><img src="media/debug-logs.png" alt="Aba Debug › Logs" width="820"></p>

- **Logar textos capturados e traduções** — chave de privacidade, **desligada por padrão**.
  Deixe desligada ao mandar log para suporte, para não expor o conteúdo do jogo. As chaves de API
  nunca vão para o log.
- **Filtrar linhas** · **Auto-scroll** · **Atualizar** — controles da visualização; erros saem
  em vermelho, avisos em amarelo.

Cada execução grava um arquivo em `logs\`, ao lado do executável, e o programa guarda os 20 mais
recentes. É esse arquivo que o suporte vai pedir.

## Histórico

<p align="center"><img src="media/historico.png" alt="Aba Histórico" width="820"></p>

Lista as traduções da captura de tela na **sessão atual** — horário, serviço, tradução e, abaixo,
o texto original. Clique numa entrada para copiar a tradução. Botão **Limpar histórico**.

## Sobre

Informações do programa: ícone, nome e **versão** instalada, o autor, os links do projeto e de
apoio, e a **Licença de Uso** completa — o que é permitido (uso pessoal gratuito, distribuir
cópias não modificadas, criar conteúdo como vídeos e streams) e o que é proibido (modificar ou
fazer engenharia reversa, vender, redistribuir versões modificadas, uso comercial sem
autorização, remover créditos), além do aviso de garantia.

---
