# -*- coding: utf-8 -*-
# Gera o site Docsify (raiz do repo) a partir do markdown-mestre do manual.
# Divide o markdown em uma pagina por secao "## " e escreve README/_sidebar/etc.
#
# Fonte: o mestre vive em game-translator/planos/MANUAL_DO_USUARIO.md. Se este
# clone estiver ao lado do repo de codigo, o mestre e copiado para _src/manual.md
# automaticamente; senao, usa a copia ja presente em _src/manual.md.
import re, os, shutil, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)            # raiz do repo (uma acima de _src/)
KEEP = {".git", "_src", ".gitignore", "LICENSE"}  # nunca apagar na limpeza

SRC = os.path.join(HERE, "manual.md")
MASTER = os.path.normpath(os.path.join(
    HERE, "..", "..", "game-translator", "planos", "MANUAL_DO_USUARIO.md"))
if os.path.isfile(MASTER):
    shutil.copyfile(MASTER, SRC)
    print("manual.md sincronizado do mestre")

LOGO = os.path.join(HERE, "logo.png")  # asset fixo da marca (nao vem do manual)

raw = open(SRC, encoding="utf-8").read()

# Limpeza leve (o mestre ja e markdown limpo; passos idempotentes):
# remove ancoras herdadas, cabecalhos vazios e colapsa linhas em branco.
raw = re.sub(r'<a id="[^"]*"></a>', '', raw)
raw = '\n'.join(l for l in raw.split('\n') if not re.match(r'^#{1,6}\s*$', l.strip()))
raw = re.sub(r'\n{3,}', '\n\n', raw).strip() + '\n'

lines = raw.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('## ')]

sections = []
for k, start in enumerate(idx):
    end = idx[k + 1] if k + 1 < len(idx) else len(lines)
    sections.append((lines[start][3:].strip(), '\n'.join(lines[start:end]).strip()))

def slug(s):
    s = re.sub(r'^\d+[.)]?\s*', '', s)
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-zA-Z0-9]+', '-', s).strip('-').lower() or 'secao'

# limpa a saida antiga (preserva o que esta em KEEP)
for n in os.listdir(OUT):
    if n in KEEP:
        continue
    p = os.path.join(OUT, n)
    shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)

# logo (asset fixo) -> media/logo.png
os.makedirs(os.path.join(OUT, 'media'), exist_ok=True)
img_src = None
if os.path.isfile(LOGO):
    shutil.copyfile(LOGO, os.path.join(OUT, 'media', 'logo.png'))
    img_src = 'media/logo.png'

def write(name, text):
    open(os.path.join(OUT, name), 'w', encoding='utf-8', newline='\n').write(text)

# paginas do manual vao para a subpasta Manual/
MANUAL_DIR = os.path.join(OUT, 'Manual')
os.makedirs(MANUAL_DIR, exist_ok=True)
RELEASES_URL = "https://github.com/BrunoDomenesDutra/ranmzagt/releases"

sidebar = ["- [Inicio](README.md)"]
first_page = None
for title, body in sections:
    if slug(title) == 'sumario':
        continue
    fname = f"{slug(title)}.md"
    if first_page is None:
        first_page = fname
    open(os.path.join(MANUAL_DIR, fname), 'w', encoding='utf-8', newline='\n').write(body + '\n')
    sidebar.append(f"- [{title}](Manual/{fname})")
write('_sidebar.md', '\n'.join(sidebar) + '\n')
write('.nojekyll', '')

REPO_URL = "https://github.com/BrunoDomenesDutra/ranmzagt"
PAGES_URL = "https://brunodomenesdutra.github.io/ranmzagt/"

b_release = "https://img.shields.io/github/v/release/BrunoDomenesDutra/ranmzagt?label=release&color=blue"
b_downloads = "https://img.shields.io/github/downloads/BrunoDomenesDutra/ranmzagt/total?label=downloads&color=brightgreen"
b_stars = "https://img.shields.io/github/stars/BrunoDomenesDutra/ranmzagt?label=stars&color=yellow"
b_platform = "https://img.shields.io/badge/plataforma-Windows-0078D6"
b_license = "https://img.shields.io/badge/licen%C3%A7a-Freeware-orange"
LICENSE_URL = f"{REPO_URL}/blob/main/LICENSE"

tagline_pt = "Traduz qualquer jogo, vídeo ou texto na tela — por cima, em tempo real."
desc_pt = ("O **Ranmza GT** captura uma área da tela, reconhece o texto com OCR, traduz e "
           "desenha a tradução **sobreposta ao jogo**, na mesma posição do texto original — "
           "como uma legenda flutuante. Funciona com qualquer jogo, visual novel, mangá "
           "digital, vídeo ou programa que mostre texto na tela.")
how_pt = ("1. **Captura** — ao apertar o atalho, fotografa a área da tela escolhida.\n"
          "2. **OCR** — reconhece o texto na imagem (Windows OCR nativo ou OneOCR, "
          "à sua escolha).\n"
          "3. **Tradução** — envia o texto para o motor escolhido (Google, OpenAI, Claude ou "
          "Gemini) e recebe a tradução.\n"
          "4. **Overlay** — desenha a tradução por cima do jogo, na mesma posição do texto "
          "original, sem capturar foco nem travar a janela.")
rust_pt = ("Desenvolvido em **Rust** 🦀 — nativo para Windows, sem runtime pesado, com baixo "
           "consumo de CPU/memória mesmo rodando junto de um jogo.")

tagline_en = "Translate any game, video or on-screen text — overlaid, in real time."
desc_en = ("**Ranmza GT** captures an area of the screen, recognizes the text with OCR, "
           "translates it and draws the translation **overlaid on the game**, in the same "
           "position as the original text — like a floating subtitle. Works with any game, "
           "visual novel, digital manga, video or program that shows text on screen.")
how_en = ("1. **Capture** — when you press the hotkey, it grabs the chosen area of the "
          "screen.\n"
          "2. **OCR** — recognizes the text in the image (native Windows OCR or OneOCR, "
          "your choice).\n"
          "3. **Translation** — sends the text to the chosen engine (Google, OpenAI, Claude "
          "or Gemini) and gets the translation back.\n"
          "4. **Overlay** — draws the translation over the game, in the same position as the "
          "original text, without stealing focus or freezing the window.")
rust_en = ("Built in **Rust** 🦀 — native for Windows, no heavy runtime, low CPU/memory "
           "footprint even while running alongside a game.")

home = '<h1 align="center">Ranmza Game Translator</h1>\n\n'
if img_src:
    home += f'<p align="center"><img src="{img_src}" alt="Ranmza GT" width="200"></p>\n\n'
home += f'<p align="center"><i>{tagline_pt}</i></p>\n\n'
home += '<p align="center">\n'
home += f'  <a href="{RELEASES_URL}"><img src="{b_release}" alt="Release"></a>\n'
home += f'  <a href="{RELEASES_URL}"><img src="{b_downloads}" alt="Downloads"></a>\n'
home += f'  <a href="{REPO_URL}/stargazers"><img src="{b_stars}" alt="Stars"></a>\n'
home += f'  <img src="{b_platform}" alt="Plataforma">\n'
home += f'  <a href="{LICENSE_URL}"><img src="{b_license}" alt="Licenca"></a>\n'
home += '</p>\n\n---\n\n'

home += '## Português\n\n'
home += desc_pt + '\n\n'
home += '**Como funciona:**\n\n' + how_pt + '\n\n'
home += rust_pt + '\n\n'
home += (f"\U0001F4D6 **[Manual completo]({PAGES_URL})** &nbsp;&middot;&nbsp; "
          f"⬇️ **[Baixar (Releases)]({RELEASES_URL})**\n\n---\n\n")

home += '## English\n\n'
home += desc_en + '\n\n'
home += '**How it works:**\n\n' + how_en + '\n\n'
home += rust_en + '\n\n'
home += (f"\U0001F4D6 **[Full manual]({PAGES_URL})** &nbsp;&middot;&nbsp; "
          f"⬇️ **[Download (Releases)]({RELEASES_URL})**\n")
write('README.md', home)

write('index.html', '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ranmza GT - Manual do Usuario</title>
  <meta name="description" content="Manual do usuario do Ranmza Game Translator">
  <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify@4/lib/themes/vue.css">
  <style>
    /* ── Paleta Dracula oficial (https://draculatheme.com) ──
       Light = Alucard Classic · Dark = Dracula Classic.
       Sobrescreve as cores do tema vue do docsify via variaveis. */
    :root{
      /* Light = Alucard Classic */
      --bg:#FFFBEB; --text:#1F1F1F; --muted:#6C664B;
      --border:#CFCFDE; --soft:#CFCFDE; --code-text:#A3144D;
      --accent:#644AC9; --theme-color:#644AC9;
      --c-purple:#644AC9; --c-pink:#A3144D; --c-cyan:#036A96;
      --c-green:#14710A; --c-orange:#A34D14; --c-yellow:#846E15;
    }
    html[data-theme="dark"]{
      /* Dark = Dracula Classic */
      --bg:#282A36; --text:#F8F8F2; --muted:#6272A4;
      --border:#44475A; --soft:#44475A; --code-text:#FF79C6;
      --accent:#BD93F9; --theme-color:#BD93F9;
      --c-purple:#BD93F9; --c-pink:#FF79C6; --c-cyan:#8BE9FD;
      --c-green:#50FA7B; --c-orange:#FFB86C; --c-yellow:#F1FA8C;
    }
    body{ background:var(--bg); color:var(--text); }
    #app{ color:var(--text); }
    .sidebar{ background:var(--bg); color:var(--text); border-right:1px solid var(--border); }
    .sidebar .app-name-link{ color:var(--accent); }
    .sidebar ul li a{ color:var(--text); }
    .sidebar ul li a:hover{ color:var(--accent); }
    .sidebar ul li.active > a{ color:var(--accent); border-right:2px solid var(--accent); }
    .markdown-section a{ color:var(--accent); }
    /* Titulos por nivel, cada um com uma cor da paleta (texto vive no .anchor span). */
    .markdown-section h1,.markdown-section h1 a,.markdown-section h1 .anchor span{ color:var(--c-purple) !important; }
    .markdown-section h2,.markdown-section h2 a,.markdown-section h2 .anchor span{ color:var(--c-pink) !important; }
    .markdown-section h3,.markdown-section h3 a,.markdown-section h3 .anchor span{ color:var(--c-cyan) !important; }
    .markdown-section h4,.markdown-section h4 a,.markdown-section h4 .anchor span{ color:var(--c-green) !important; }
    .markdown-section h5,.markdown-section h5 a,.markdown-section h5 .anchor span{ color:var(--c-orange) !important; }
    .markdown-section h6,.markdown-section h6 a,.markdown-section h6 .anchor span{ color:var(--c-yellow) !important; }
    .markdown-section strong{ color:var(--text); }
    .markdown-section p,.markdown-section li,.markdown-section td{ color:var(--text); }
    /* Callouts: texto em contraste cheio (antes usava a cor "Comment", ilegivel). */
    .markdown-section blockquote{ border-left:4px solid var(--accent); background:var(--soft); color:var(--text); }
    .markdown-section blockquote p,.markdown-section blockquote li{ color:var(--text); }
    .markdown-section code{ background:var(--bg); border:1px solid var(--border); color:var(--code-text); }
    .markdown-section pre{ background:var(--soft); }
    .markdown-section pre > code{ background:transparent; border:0; color:var(--text); }
    .markdown-section tr{ border-top:1px solid var(--border); background:var(--bg); }
    .markdown-section tr:nth-child(2n){ background:var(--soft); }
    .markdown-section th,.markdown-section td{ border:1px solid var(--border); }
    .markdown-section hr{ border-bottom:1px solid var(--border); }
    /* plugin de busca */
    .search input{ background:var(--bg); color:var(--text); border:1px solid var(--border); }
    .search .results-panel{ background:var(--bg); color:var(--text); }
    .search .matching-post{ border-bottom:1px solid var(--border); }
    .search p{ color:var(--muted); }
    .search .search-keyword{ color:var(--accent); }
    .search h2,.search .matching-post h2{ color:var(--text); }
    /* botao de alternar tema */
    #theme-toggle{
      position:fixed; top:14px; right:16px; z-index:100;
      width:40px; height:40px; border-radius:10px;
      border:1px solid var(--border); background:var(--bg); color:var(--text);
      cursor:pointer; font-size:18px; line-height:1;
      display:flex; align-items:center; justify-content:center;
      box-shadow:0 2px 6px rgba(0,0,0,.18); transition:border-color .15s,color .15s;
    }
    #theme-toggle:hover{ border-color:var(--accent); color:var(--accent); }
  </style>
  <script>
    /* Define o tema ANTES da pintura (evita flash): escolha salva -> preferencia do SO -> dark. */
    (function(){
      var k='ranmza-doc-theme', s=null;
      try{ s=localStorage.getItem(k); }catch(e){}
      if(!s) s=(window.matchMedia && matchMedia('(prefers-color-scheme: dark)').matches) ? 'dark' : 'light';
      document.documentElement.setAttribute('data-theme', s);
    })();
  </script>
</head>
<body>
  <button id="theme-toggle" onclick="RToggleTheme()" aria-label="Alternar tema claro/escuro" title="Alternar tema">&#127769;</button>
  <div id="app">Carregando o manual...</div>
  <script>
    window.$docsify = {
      name: 'Ranmza GT',
      repo: 'https://github.com/BrunoDomenesDutra/ranmzagt',
      loadSidebar: true,
      alias: { '/.*/_sidebar.md': '/_sidebar.md' },
      subMaxLevel: 3,
      auto2top: true,
      search: { placeholder: 'Buscar no manual...', noData: 'Nada encontrado.' }
    };
    function RSyncThemeBtn(){
      var dark = document.documentElement.getAttribute('data-theme') === 'dark';
      var b = document.getElementById('theme-toggle');
      if(b) b.innerHTML = dark ? '&#9728;&#65039;' : '&#127769;';
    }
    function RToggleTheme(){
      var k='ranmza-doc-theme';
      var next = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      try{ localStorage.setItem(k, next); }catch(e){}
      document.documentElement.setAttribute('data-theme', next);
      RSyncThemeBtn();
    }
    RSyncThemeBtn();
  </script>
  <script src="//cdn.jsdelivr.net/npm/docsify@4"></script>
  <script src="//cdn.jsdelivr.net/npm/docsify@4/lib/plugins/search.min.js"></script>
</body>
</html>
''')

print("OK ->", OUT, "| paginas:", len(sidebar))
