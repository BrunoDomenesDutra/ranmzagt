# -*- coding: utf-8 -*-
# Passo 1: MANUAL_DO_USUARIO.docx -> _raw.md
# docx -> HTML (mammoth, preserva tabelas) -> markdown (markdownify, tabelas GFM)
# Requisitos: pip install mammoth markdownify
import os, mammoth
from markdownify import markdownify as md

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "MANUAL_DO_USUARIO.docx")
MEDIA = os.path.join(HERE, "media")
os.makedirs(MEDIA, exist_ok=True)

count = [0]
def handle_image(image):
    count[0] += 1
    ext = (image.content_type or "image/png").split("/")[-1]
    name = f"img{count[0]}.{ext}"
    with image.open() as f, open(os.path.join(MEDIA, name), "wb") as out:
        out.write(f.read())
    return {"src": f"media/{name}"}

with open(SRC, "rb") as f:
    html = mammoth.convert_to_html(
        f, convert_image=mammoth.images.img_element(handle_image)
    ).value

text = md(html, heading_style="ATX", bullets="-", strong_em_symbol="*")
open(os.path.join(HERE, "_raw.md"), "w", encoding="utf-8", newline="\n").write(text)
print("imagens:", count[0], "| chars:", len(text))
