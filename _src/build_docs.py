# -*- coding: utf-8 -*-
# Passo 2: _raw.md -> site Docsify na raiz do repo.
# Limpa o markdown, divide em uma pagina por secao "## " e gera README/_sidebar.
import re, os, shutil, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "_raw.md")
MEDIA_SRC = os.path.join(HERE, "media")
OUT = os.path.dirname(HERE)            # raiz do repo (uma acima de _src/)
KEEP = {".git", "_src", ".gitignore"}  # nunca apagar na limpeza

raw = open(SRC, encoding="utf-8").read()

# 1. remove ancoras do Google Docs, se houver (<a id="_heading=..."></a>)
raw = re.sub(r'<a id="[^"]*"></a>', '', raw)
# 2. desfaz escapes seguros (pontuacao que nunca e markdown inline; "_" nao
#    vira italico intra-palavra no GFM/Docsify)
for ch in ['.', ',', ';', ':', '!', '?', '(', ')', '"', '-', '/', '_']:
    raw = raw.replace('\\' + ch, ch)
# 3. remove cabecalhos vazios e colapsa linhas em branco
raw = '\n'.join(l for l in raw.split('\n') if not re.match(r'^#{1,6}\s*$', l.strip()))
raw = re.sub(r'\n{3,}', '\n\n', raw).strip() + '\n'

lines = raw.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('## ')]
topmatter = lines[:idx[0]]

sections = []
for k, start in enumerate(idx):
    end = idx[k + 1] if k + 1 < len(idx) else len(lines)
    sections.append((lines[start][3:].strip(), '\n'.join(lines[start:end]).strip()))

def slug(s):
    s = re.sub(r'^\d+[.)]?\s*', '', s)
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-zA-Z0-9]+', '-', s).strip('-').lower() or 'secao'

img = re.search(r'!\[\]\((media/[^)]+)\)', '\n'.join(topmatter))
img_src = img.group(1) if img else None

# limpa a saida antiga (preserva .git e _src)
for n in os.listdir(OUT):
    if n in KEEP:
        continue
    p = os.path.join(OUT, n)
    shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)

if os.path.isdir(MEDIA_SRC):
    shutil.copytree(MEDIA_SRC, os.path.join(OUT, 'media'))

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

tagline = "Traduz qualquer jogo, vídeo ou texto na tela — por cima, em tempo real."
desc = ("O **Ranmza GT** captura uma área da tela, reconhece o texto com OCR, traduz e "
        "desenha a tradução **sobreposta ao jogo**, na mesma posição do texto original — "
        "como uma legenda flutuante. Funciona com qualquer jogo, vídeo ou programa que "
        "mostre texto na tela.")

home = '<h1 align="center">Ranmza Game Translator</h1>\n\n'
if img_src:
    home += f'<p align="center"><img src="{img_src}" alt="Ranmza GT" width="200"></p>\n\n'
home += f'<p align="center"><i>{tagline}</i></p>\n\n'
home += '<p align="center">\n'
home += f'  <a href="{RELEASES_URL}"><img src="{b_release}" alt="Release"></a>\n'
home += f'  <a href="{RELEASES_URL}"><img src="{b_downloads}" alt="Downloads"></a>\n'
home += f'  <a href="{REPO_URL}/stargazers"><img src="{b_stars}" alt="Stars"></a>\n'
home += f'  <img src="{b_platform}" alt="Plataforma">\n'
home += '</p>\n\n---\n\n'
home += desc + '\n\n'
home += (f"\U0001F4D6 **[Manual completo]({PAGES_URL})** &nbsp;&middot;&nbsp; "
         f"⬇️ **[Baixar (Releases)]({RELEASES_URL})**\n")
write('README.md', home)

write('index.html', '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ranmza GT - Manual do Usuario</title>
  <meta name="description" content="Manual do usuario do Ranmza Game Translator">
  <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify@4/lib/themes/vue.css">
</head>
<body>
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
  </script>
  <script src="//cdn.jsdelivr.net/npm/docsify@4"></script>
  <script src="//cdn.jsdelivr.net/npm/docsify@4/lib/plugins/search.min.js"></script>
</body>
</html>
''')

print("OK ->", OUT, "| paginas:", len(sidebar))
