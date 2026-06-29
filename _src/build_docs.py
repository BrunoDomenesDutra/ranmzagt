# -*- coding: utf-8 -*-
# Gera o site Docsify bilíngue (PT + EN) a partir de dois markdown-mestres.
# Divide cada markdown em uma pagina por secao "## " e escreve README/_sidebar/etc.
#
# Fonte: mestres vivem em game-translator/planos/MANUAL_DO_USUARIO.md (PT) e
# são copiados para _src/manual.md; manual_en.md (EN) é a tradução.
import re, os, shutil, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)            # raiz do repo (uma acima de _src/)
KEEP = {".git", "_src", ".gitignore", "LICENSE", "index.html", "index_en.html"}  # nunca apagar na limpeza

# Tenta sincronizar o mestre PT do game-translator
MASTER = os.path.normpath(os.path.join(
    HERE, "..", "..", "game-translator", "planos", "MANUAL_DO_USUARIO.md"))
SRC_PT = os.path.join(HERE, "manual.md")
SRC_EN = os.path.join(HERE, "manual_en.md")

if os.path.isfile(MASTER):
    shutil.copyfile(MASTER, SRC_PT)
    print("manual.md sincronizado do mestre")

LOGO = os.path.join(HERE, "logo.png")  # asset fixo da marca

def read_and_split(filepath):
    """Le um markdown e o divide em secoes (## title)."""
    raw = open(filepath, encoding="utf-8").read()

    # Limpeza leve
    raw = re.sub(r'<a id="[^"]*"></a>', '', raw)
    raw = '\n'.join(l for l in raw.split('\n') if not re.match(r'^#{1,6}\s*$', l.strip()))
    raw = re.sub(r'\n{3,}', '\n\n', raw).strip() + '\n'

    lines = raw.split('\n')
    idx = [i for i, l in enumerate(lines) if l.startswith('## ')]

    sections = []
    for k, start in enumerate(idx):
        end = idx[k + 1] if k + 1 < len(idx) else len(lines)
        sections.append((lines[start][3:].strip(), '\n'.join(lines[start:end]).strip()))

    return sections

def slug(s):
    s = re.sub(r'^\d+[.)]?\s*', '', s)
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-zA-Z0-9]+', '-', s).strip('-').lower() or 'secao'

# limpa a saida antiga (preserva KEEP)
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

# ---- Processa PT e EN ----
sections_pt = read_and_split(SRC_PT)
sections_en = read_and_split(SRC_EN)

RELEASES_URL = "https://github.com/BrunoDomenesDutra/ranmzagt/releases"

# PT
MANUAL_DIR_PT = os.path.join(OUT, 'Manual')
os.makedirs(MANUAL_DIR_PT, exist_ok=True)

sidebar_pt = ["- [Inicio](README.md)"]
first_page_pt = None
for title, body in sections_pt:
    if slug(title) == 'sumario':
        continue
    fname = f"{slug(title)}.md"
    if first_page_pt is None:
        first_page_pt = fname
    open(os.path.join(MANUAL_DIR_PT, fname), 'w', encoding='utf-8', newline='\n').write(body + '\n')
    sidebar_pt.append(f"- [{title}](Manual/{fname})")
write('_sidebar.md', '\n'.join(sidebar_pt) + '\n')

# EN
MANUAL_DIR_EN = os.path.join(OUT, 'Manual_EN')
os.makedirs(MANUAL_DIR_EN, exist_ok=True)

sidebar_en = ["- [Home](README_EN.md)"]
first_page_en = None
for title, body in sections_en:
    if slug(title) == 'table-of-contents':
        continue
    fname = f"{slug(title)}.md"
    if first_page_en is None:
        first_page_en = fname
    open(os.path.join(MANUAL_DIR_EN, fname), 'w', encoding='utf-8', newline='\n').write(body + '\n')
    sidebar_en.append(f"- [{title}](Manual_EN/{fname})")
write('_sidebar_en.md', '\n'.join(sidebar_en) + '\n')

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

# README.md (PT com link pra EN)
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
home += '</p>\n\n'
home += '<p align="center">\n'
home += '  <strong><a href="/">🇧🇷 Português</a></strong> &nbsp;·&nbsp; '
home += '  <strong><a href="/index_en.html">🇬🇧 English</a></strong>\n'
home += '</p>\n\n---\n\n'

home += '## Português\n\n'
home += desc_pt + '\n\n'
home += '**Como funciona:**\n\n' + how_pt + '\n\n'
home += rust_pt + '\n\n'
home += (f"📖 **[Manual completo]({PAGES_URL})** &nbsp;·&nbsp; "
         f"⬇️ **[Baixar (Releases)]({RELEASES_URL})**\n\n---\n\n")

home += '## English\n\n'
home += desc_en + '\n\n'
home += '**How it works:**\n\n' + how_en + '\n\n'
home += rust_en + '\n\n'
home += (f"📖 **[Full manual]({PAGES_URL}index_en.html)** &nbsp;·&nbsp; "
         f"⬇️ **[Download (Releases)]({RELEASES_URL})**\n")
write('README.md', home)

# README_EN.md (EN com link pra PT)
home_en = '<h1 align="center">Ranmza Game Translator</h1>\n\n'
if img_src:
    home_en += f'<p align="center"><img src="{img_src}" alt="Ranmza GT" width="200"></p>\n\n'
home_en += f'<p align="center"><i>{tagline_en}</i></p>\n\n'
home_en += '<p align="center">\n'
home_en += f'  <a href="{RELEASES_URL}"><img src="{b_release}" alt="Release"></a>\n'
home_en += f'  <a href="{RELEASES_URL}"><img src="{b_downloads}" alt="Downloads"></a>\n'
home_en += f'  <a href="{REPO_URL}/stargazers"><img src="{b_stars}" alt="Stars"></a>\n'
home_en += f'  <img src="{b_platform}" alt="Platform">\n'
home_en += f'  <a href="{LICENSE_URL}"><img src="{b_license}" alt="License"></a>\n'
home_en += '</p>\n\n'
home_en += '<p align="center">\n'
home_en += '  <strong><a href="/">🇧🇷 Português</a></strong> &nbsp;·&nbsp; '
home_en += '  <strong><a href="/index_en.html">🇬🇧 English</a></strong>\n'
home_en += '</p>\n\n---\n\n'

home_en += desc_en + '\n\n'
home_en += '**How it works:**\n\n' + how_en + '\n\n'
home_en += rust_en + '\n\n'
home_en += (f"📖 **[Full manual]({PAGES_URL}index_en.html)** &nbsp;·&nbsp; "
            f"⬇️ **[Download (Releases)]({RELEASES_URL})**\n")
write('README_EN.md', home_en)

# index_en.html e index.html nao sao regenerados (mantidos a mao, blindados em KEEP)
# Se index_en.html nao existir ainda, cria como cópia de index.html mas apontando a _sidebar_en
# (na prática, o usuario vai customizar o index_en.html se necessário)

print(f"OK -> {OUT} | PT: {len(sidebar_pt)} paginas | EN: {len(sidebar_en)} paginas")
