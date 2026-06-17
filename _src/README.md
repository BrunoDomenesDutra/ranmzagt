# Fonte do manual (gerador do site)

O site publicado (raiz do repo) e gerado a partir de um unico markdown.

**Fonte (mestre):** `game-translator/planos/MANUAL_DO_USUARIO.md` (no repo de codigo).
`_src/manual.md` e uma copia dele, usada pelo build — sincronizada automaticamente
quando este repo esta clonado ao lado do `game-translator`.

## Atualizar o manual

1. Edite `game-translator/planos/MANUAL_DO_USUARIO.md`.
2. Rode (a partir desta pasta):

   ```
   python build_docs.py
   ```

   Ele copia o mestre para `manual.md`, divide em uma pagina por secao `## ` e
   escreve `README.md`, `_sidebar.md`, `index.html` e `media/` na raiz do repo.
3. Faca commit e push (deste repo). O GitHub Pages republica sozinho.

> Se editar direto o `_src/manual.md` (sem o repo de codigo ao lado), o build usa
> essa copia — mas lembre de refletir a mudanca no mestre depois.

`logo.png` e o asset fixo da marca (vai para `media/logo.png` no build); nao vem
do texto do manual.
