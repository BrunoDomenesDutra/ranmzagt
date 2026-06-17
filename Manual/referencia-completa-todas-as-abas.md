## 12. Referência completa — todas as abas

Esta seção descreve **cada aba e cada opção** da janela de configuração, na ordem em que aparecem na barra lateral. Use como consulta — para o dia a dia, as seções anteriores já bastam.

### Geral

Onde o programa opera.

- **Backend de captura** — como o programa lê os pixels da tela:
- *Auto (recomendado)* — escolhe sozinho: WGC no Windows 11, DXGI no Windows 10.
- *WGC (Windows 11)* — Windows Graphics Capture; no Win11 captura sem a borda amarela.
- *DXGI (Windows 10)* — Desktop Duplication; existe para o Windows 10 não desenhar a borda amarela/dourada ao redor do monitor capturado. A troca é aplicada na hora, sem reiniciar.
- **Monitor → Tela ativa** — em qual monitor o programa captura, traduz e exibe. *Automático* usa o monitor principal do Windows. Trocar de monitor **limpa a área de captura** salva e **exige reiniciar** (botão "Reiniciar agora" aparece logo abaixo).
- **Barra flutuante → Mostrar barra flutuante** — liga a janelinha de botões sempre visível, arrastável entre monitores (veja a seção 3).

### Idioma

O campo do idioma de origem **se adapta ao motor de OCR** selecionado na aba OCR.

- **Idioma do texto original**:
- *WinOCR* — uma tag BCP-47 (ex.: en, ja, ko, zh-Hans, pt). Se o pacote do idioma não estiver instalado no Windows, aparece um aviso vermelho com o botão **Instalar pacote de idioma** (abre direto a tela de idiomas do Windows).
- *OneOCR* — **detecção automática**; não há idioma de origem para configurar.
- **Idioma destino** — para qual idioma traduzir (ex.: pt, es, fr, de, it, zh).

### Captura

Aparência da tradução manual e pré-processamento da imagem.

**Texto**

- *Fonte* — "Padrão do sistema (Segoe UI)" ou qualquer fonte da pasta fonts/.
- *Tamanho da fonte* — 8 a 72 pt.
- *Altura da linha* — 0,80 a 2,00 (espaçamento entre linhas).
- *Auto-fit* — reduz a fonte progressivamente para o texto caber no bloco sem cortar.

**Fundo e Contorno** (são alternativos — ligar um desliga o outro)

- *Mostrar fundo* + *Opacidade do fundo* (10–100%) — caixa escura atrás do texto.
- *Mostrar contorno* + *Espessura* (2–5 px) — contorno preto ao redor de cada letra.

**Exibição → Duração do overlay** — Nunca limpar / 15 s / 30 s / **1 minuto (padrão)** / 2 / 5 / 10 minutos.

**Pré-processamento OCR** — filtros aplicados à imagem antes do reconhecimento:

- *Ativar pré-processamento* (liga a seção)
- *Escala de cinza* · *Inverter cores*
- *Contraste* (1,0–3,0×) · *Upscale* (1,0–4,0×) · *Sharpen* (0–2,0×)
- *Avançado* (só é aplicado quando ligado): *Threshold* (0–255), *Blur* (0–5,0×), *Dilatação* (0–10 px), *Erosão* (0–10 px).

### Legenda

Tem aparência e pré-processamento **próprios**, independentes da aba Captura.

**Captura**

- *Intervalo* — de cada quanto tempo a área é relida (50 ms a 5 s).
- *Linhas visíveis* — quantas linhas de legenda manter na tela (1 a 8).
- *Limpar após silêncio* — limpa a legenda se nenhum texto novo aparecer por X segundos (1 a 5 s).
- Desligamento automático — desliga o modo legenda após X minutos configuráveis

**Aparência do Overlay**

- *Tamanho da fonte* (10–48 pt)
- *Mostrar fundo* + *Opacidade* (10–100%)
- *Mostrar contorno* + *Espessura do contorno* (1–5 px)

**Pré-processamento OCR** — mesmos controles da aba Captura, mas independentes.

### Atalhos

Sete atalhos globais (funcionam com o jogo em foco; desativados quando a janela de config está em primeiro plano). Cada um tem os modificadores **Ctrl / Alt / Shift** e a tecla principal (grupos Numpad, Função F1–F12 e Letras): Selecionar área · Traduzir · Traduzir com IA Vision · Limpar overlay · Ligar/desligar legenda · Selecionar área da legenda · Mostrar/ocultar áreas.

***Letras como tecla principal exigem um modificador (Ctrl, Alt ou Shift) para não conflitar com o jogo. Numpad e F-keys funcionam sem modificador.***

### Tradutores

**Provedor de Tradução → Provedor ativo**:

*Google Translate* — gratuito, sem chave. **Não suporta o Modo Vision.**

*OpenAI*, *Anthropic (Claude)*, *Gemini* — exigem chave de API.

- **Autenticação** (aparece para os provedores com chave; as credenciais são **salvas por motor independentemente**, então trocar e voltar não apaga nada):
- *API Key* — sua chave (sk-..., sk-ant-..., AIza...).

*Modelo*:

- OpenAI: GPT-4o mini (econômico) · GPT-4o (qualidade superior).
- Claude: Haiku 4.5 (rápido/econômico) · Sonnet 4.6 (qualidade superior).
- Gemini: 1.5 Flash · 2.0 Flash · 1.5 Pro.

### IA

As três primeiras seções só aparecem com um provedor de IA selecionado (não no Google).

**Parâmetros do Modelo**

- *Temperature* (0–2) — 0,0 literal · 0,3 recomendado · 1,0+ criativo.
- *Max tokens* (256–4096) — tamanho da resposta; 1024 é suficiente para tradução.

**Contexto de Conversa → Falas anteriores** (0–20) — no Modo Legenda, envia as últimas falas (original + tradução) como contexto para manter consistência de termos e tom. 0 = desativado; recomendado 3–5.

**System Prompt** — papel do tradutor e regras gerais (botão **Salvar**).

**Informações do Jogo** — tema, personagens e glossário; mude por jogo (botão **Salvar**).

### OCR

**Engine de OCR → Engine ativo**:

- *WinOCR* (padrão) — nativo do Windows, ~30 ms, offline; depende dos pacotes de idioma instalados. Pode errar em fontes muito estilizadas.
- *OneOCR* (experimental, Windows 11) — motor do Snipping Tool, ~50–150 ms, multilíngue automático. Usa API não oficial da Microsoft; você copia 3 arquivos do próprio Windows (oneocr.dll, oneocr.onemodel, onnxruntime.dll) e aponta a pasta (botões Procurar / Verificar — a pasta é configurada automaticamente se válida).

**Agrupamento de Blocos** — como as linhas detectadas são combinadas antes de traduzir:

- *Modo Parágrafo* — agrupa linhas verticalmente próximas (diálogos, texto corrido). Mostra *Sensibilidade do agrupamento* (0–3,0; padrão 1): menor separa mais, maior junta mais.
- *Modo Linha* — cada linha vira um bloco independente (menus, HUD).

### Web

Transmite as traduções para navegadores na rede local (e para o OBS).

**Servidor Web**

- *Servidor ativo* — inicia o servidor HTTP local.
- *Mostrar tradução na tela* — exibe o overlay mesmo com o servidor ligado; desligue para enviar **só** ao navegador/OBS.
- *Porta* (1024–65535) — mostra também quantos clientes estão conectados.

**Endereços** — /captura (com histórico e botão Limpar) e /captura/obs (fundo transparente, para Browser Source no OBS), com botão Copiar.

**Aparência** — *Tema* (Dark / Light / Dracula) · *Tamanho da fonte* (12–48 px) · *Negrito* · *Texto detectado* (mostra o original) · *Horário e serviço* · *Cores personalizadas* (libera 6 seletores de cor: texto traduzido, texto original, horário, serviço/badge, fundo do card, borda do card).

**Histórico → Entradas mantidas no buffer** (10–200).

### Histórico

Lista as traduções da **sessão atual** (horário, serviço, tradução e, abaixo, o texto original), da mais recente para a mais antiga, até o limite definido na aba Web. Botão **Limpar histórico**.

### Lab

Laboratório para testar o pré-processamento sem afetar o jogo.

- **Imagem de Teste** — escolhe uma imagem da pasta images/lab_images/ (ao lado do executável).
- **Parâmetros de Pré-processamento** — os mesmos controles da aba Captura, com **preview ao vivo** (imagem original × processada).
- Botões **Aplicar em Captura** e **Aplicar em Legenda** — copiam a configuração testada para a aba correspondente.

### Monitor

- **Monitoramento → Ativo** — registra o tempo de cada etapa do pipeline a cada tradução (mantido ao navegar entre abas).
- **Histórico de Execuções** — tabela das últimas 10 capturas: Hora, Captura, Preproc, OCR, Tradução, Total, Blocos, Cache (acertos sem API) e API (chamadas feitas).
- **Estatísticas** — mín / média / máx de cada etapa (a partir de 2 execuções).

### Debug

- **Modo Debug → Ativado** — salva imagens de diagnóstico a cada captura na pasta de output.
- **Imagens a salvar** — Captura original (frame.png), Captura pós pré-processamento (frame_proc.png), Linhas do OCR (ocr_lines.png), Parágrafos agrupados (ocr_paragraphs.png), Preview da máscara de inpainting (mask.png).
- **Pasta de output** — caminho dos arquivos + botão para abrir a pasta.

### Logs

Log da sessão em tempo real.

- **Logar textos capturados e traduções** — toggle de privacidade; **desativado por padrão**. Mantenha desligado ao compartilhar logs para suporte, para não expor o conteúdo do jogo.
- **Filtrar linhas** · **Auto-scroll** · **Atualizar** — controles da visualização (erros em vermelho, avisos em amarelo, etc.).

### Experimental

***Tudo nesta aba está em desenvolvimento — o comportamento pode mudar, bugs são esperados e recursos podem ser removidos.***

- **Fundo reconstruído por IA (MI-GAN)** — em vez da caixa preta, apaga o texto original da captura e reconstrói o fundo com um modelo de inpainting (MI-GAN) rodando dentro do programa; a tradução é desenhada por cima, como se fosse nativa do jogo. Funciona nas **traduções manuais** (Traduzir e Vision); o Modo Legenda não usa. Custa ~50–200 ms por tradução e ~200 MB de RAM enquanto ativo. Requer baixar migan_pipeline_v2.onnx (28 MB) e onnxruntime.dll, colocá-los na mesma pasta e apontar (Procurar / Verificar). Dica: ative o **Contorno** na aba Captura, pois o fundo reconstruído pode ficar claro.
