# Fonte do manual (gerador do site)

O site publicado (raiz do repo) e gerado a partir do `MANUAL_DO_USUARIO.docx`.
Para atualizar o manual:

1. Edite `MANUAL_DO_USUARIO.docx` (no Word).
2. Instale as dependencias (uma vez): `pip install mammoth markdownify`
3. Rode os dois passos a partir desta pasta:

   ```
   python convert.py      # docx -> _raw.md (+ media/)
   python build_docs.py   # _raw.md -> site na raiz do repo
   ```

4. Faca commit e push. O GitHub Pages republica sozinho.

`convert.py` usa o mammoth (docx->HTML, preserva tabelas) + markdownify
(HTML->markdown GFM). `build_docs.py` limpa o markdown, divide em uma pagina
por secao `## ` e escreve `README.md`, `_sidebar.md`, `index.html` e `media/`
na raiz. Arquivos intermediarios (`_raw.md`, `media/`) ficam nesta pasta.
