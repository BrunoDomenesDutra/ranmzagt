# -*- coding: utf-8 -*-
# Gera o site Docsify bilíngue (PT raiz + EN em /en/) a partir de dois mestres.
# Divide cada markdown em uma pagina por secao "## " e escreve README/_sidebar/etc.
#
# Multi-idioma e feito do jeito canonico do Docsify: UM unico index.html roteia
#   PT  -> #/            (README.md, _sidebar.md, Manual/*.md na raiz)
#   EN  -> #/en/         (en/README.md, en/_sidebar.md, en/Manual/*.md)
# O index.html (mantido a mao) tem o alias do _sidebar de /en/ e o botao de idioma.
#
# Fonte: mestre PT vive em game-translator/planos/MANUAL_DO_USUARIO.md e e copiado
# para _src/manual.md; manual_en.md (EN) e a traducao mantida aqui em _src/.
import re, os, shutil, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)            # raiz do repo (uma acima de _src/)
KEEP = {".git", "_src", ".gitignore", "LICENSE", "index.html"}  # nunca apagar na limpeza

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
    path = os.path.join(OUT, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8', newline='\n').write(text)

RELEASES_URL = "https://github.com/BrunoDomenesDutra/ranmzagt/releases"
REPO_URL = "https://github.com/BrunoDomenesDutra/ranmzagt"
PAGES_URL = "https://brunodomenesdutra.github.io/ranmzagt/"

b_release = "https://img.shields.io/github/v/release/BrunoDomenesDutra/ranmzagt?label=release&color=blue"
b_downloads = "https://img.shields.io/github/downloads/BrunoDomenesDutra/ranmzagt/total?label=downloads&color=brightgreen"
b_stars = "https://img.shields.io/github/stars/BrunoDomenesDutra/ranmzagt?label=stars&color=yellow"
b_platform = "https://img.shields.io/badge/plataforma-Windows-0078D6"
b_license = "https://img.shields.io/badge/licen%C3%A7a-Freeware-orange"
LICENSE_URL = f"{REPO_URL}/blob/main/LICENSE"

def build_lang(sections, *, out_prefix, sidebar_home_label, home_md,
               skip_slug, manual_label):
    """Gera Manual/*.md + _sidebar.md de um idioma. out_prefix='' (PT) ou 'en' (EN).

    Os links do sidebar sao ABSOLUTOS com o prefixo do idioma (`/...` ou `/en/...`):
    com relativePath desligado (padrao do Docsify), link de sidebar resolve a partir
    da raiz — logo o sidebar EN precisa do prefixo /en/ para nao cair no conteudo PT.
    """
    manual_dir = os.path.join(OUT, out_prefix, 'Manual')
    os.makedirs(manual_dir, exist_ok=True)

    route = f"/{out_prefix}/" if out_prefix else "/"   # /  ou  /en/
    sidebar = [f"- [{sidebar_home_label}]({route})"]
    for title, body in sections:
        if slug(title) == skip_slug:
            continue
        fname = f"{slug(title)}.md"
        open(os.path.join(manual_dir, fname), 'w', encoding='utf-8', newline='\n').write(body + '\n')
        sidebar.append(f"- [{title}]({route}Manual/{fname})")

    write(os.path.join(out_prefix, '_sidebar.md'), '\n'.join(sidebar) + '\n')
    write(os.path.join(out_prefix, 'README.md'), home_md)
    return len(sidebar)

# ---------- Home (README.md) de cada idioma ----------
# Links de idioma usam rotas de hash do Docsify: '/' = PT, '/en/' = EN.

def badges(platform_alt, license_alt):
    s  = '<p align="center">\n'
    s += f'  <a href="{RELEASES_URL}"><img src="{b_release}" alt="Release"></a>\n'
    s += f'  <a href="{RELEASES_URL}"><img src="{b_downloads}" alt="Downloads"></a>\n'
    s += f'  <a href="{REPO_URL}/stargazers"><img src="{b_stars}" alt="Stars"></a>\n'
    s += f'  <img src="{b_platform}" alt="{platform_alt}">\n'
    s += f'  <a href="{LICENSE_URL}"><img src="{b_license}" alt="{license_alt}">\n'
    s += '</a></p>\n\n'
    return s

# --- PT ---
tagline_pt = "Traduz qualquer jogo, vídeo ou texto na tela — por cima, em tempo real."
desc_pt = ("O **Ranmza GT** captura uma área da tela, reconhece o texto com OCR, traduz e "
           "desenha a tradução **sobreposta ao jogo**, na mesma posição do texto original — "
           "como uma legenda flutuante. Funciona com qualquer jogo, visual novel, mangá "
           "digital, vídeo ou programa que mostre texto na tela.")
how_pt = ("1. **Captura** — ao apertar o atalho, fotografa a área da tela escolhida.\n"
          "2. **OCR** — reconhece o texto na imagem (Windows OCR nativo ou OneOCR, à sua escolha).\n"
          "3. **Tradução** — envia o texto para o motor escolhido (Google, OpenAI, Claude ou "
          "Gemini) e recebe a tradução.\n"
          "4. **Overlay** — desenha a tradução por cima do jogo, na mesma posição do texto "
          "original, sem capturar foco nem travar a janela.")
rust_pt = ("Desenvolvido em **Rust** 🦀 — nativo para Windows, sem runtime pesado, com baixo "
           "consumo de CPU/memória mesmo rodando junto de um jogo.")

home_pt = '<h1 align="center">Ranmza Game Translator</h1>\n\n'
if img_src:
    home_pt += f'<p align="center"><img src="{img_src}" alt="Ranmza GT" width="200"></p>\n\n'
home_pt += f'<p align="center"><i>{tagline_pt}</i></p>\n\n'
home_pt += badges("Plataforma", "Licenca")
home_pt += '<p align="center"><strong>🇧🇷 Português</strong> &nbsp;·&nbsp; <a href="#/en/">🇬🇧 English</a></p>\n\n---\n\n'
home_pt += desc_pt + '\n\n'
home_pt += '### Como funciona\n\n' + how_pt + '\n\n'
home_pt += rust_pt + '\n\n'
home_pt += (f"📖 **[Abrir o manual completo]({PAGES_URL})** &nbsp;·&nbsp; "
            f"⬇️ **[Baixar (Releases)]({RELEASES_URL})**\n")

# --- EN ---
tagline_en = "Translate any game, video or on-screen text — overlaid, in real time."
desc_en = ("**Ranmza GT** captures an area of the screen, recognizes the text with OCR, "
           "translates it and draws the translation **overlaid on the game**, in the same "
           "position as the original text — like a floating subtitle. Works with any game, "
           "visual novel, digital manga, video or program that shows text on screen.")
how_en = ("1. **Capture** — when you press the hotkey, it grabs the chosen area of the screen.\n"
          "2. **OCR** — recognizes the text in the image (native Windows OCR or OneOCR, your choice).\n"
          "3. **Translation** — sends the text to the chosen engine (Google, OpenAI, Claude or "
          "Gemini) and gets the translation back.\n"
          "4. **Overlay** — draws the translation over the game, in the same position as the "
          "original text, without stealing focus or freezing the window.")
rust_en = ("Built in **Rust** 🦀 — native for Windows, no heavy runtime, low CPU/memory "
           "footprint even while running alongside a game.")

home_en = '<h1 align="center">Ranmza Game Translator</h1>\n\n'
if img_src:
    home_en += f'<p align="center"><img src="{img_src}" alt="Ranmza GT" width="200"></p>\n\n'
home_en += f'<p align="center"><i>{tagline_en}</i></p>\n\n'
home_en += badges("Platform", "License")
home_en += '<p align="center"><a href="#/">🇧🇷 Português</a> &nbsp;·&nbsp; <strong>🇬🇧 English</strong></p>\n\n---\n\n'
home_en += desc_en + '\n\n'
home_en += '### How it works\n\n' + how_en + '\n\n'
home_en += rust_en + '\n\n'
home_en += (f"📖 **[Open the full manual]({PAGES_URL}#/en/)** &nbsp;·&nbsp; "
            f"⬇️ **[Download (Releases)]({RELEASES_URL})**\n")

# ---------- Gera ----------
n_pt = build_lang(read_and_split(SRC_PT), out_prefix='',   sidebar_home_label='Início',
                  home_md=home_pt, skip_slug='sumario',           manual_label='Manual')
n_en = build_lang(read_and_split(SRC_EN), out_prefix='en', sidebar_home_label='Home',
                  home_md=home_en, skip_slug='table-of-contents', manual_label='Manual')

write('.nojekyll', '')

print(f"OK -> {OUT} | PT: {n_pt} itens | EN: {n_en} itens")
