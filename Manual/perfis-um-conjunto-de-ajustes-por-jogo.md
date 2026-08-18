# 4. Perfis — um conjunto de ajustes por jogo

Cada jogo pede um ajuste diferente: a caixa de diálogo fica num canto da tela, o idioma é
outro, a fonte que lê bem num não lê no outro, e o glossário de nomes não serve para mais
nada fora dali. Um **perfil** guarda tudo isso junto, e você troca de jogo em um clique.

O seletor fica no **canto superior direito da janela**, ao lado do botão de tema, e aparece
em todas as abas — porque o perfil ativo é o contexto de tudo que elas mostram.

<p align="center"><img src="media/geral-perfis.png" alt="Aba Geral › Perfis" width="820"></p>

## O perfil Padrão

Existe sempre, já vem ativo e **não pode ser apagado nem renomeado**. Se você nunca criar
outro perfil, o programa funciona exatamente como antes: tudo que você ajustar fica nele.

Quem já usava o Ranmza GT não perde nada na atualização — a configuração de hoje vira o
perfil Padrão automaticamente.

## Criando um perfil

Vá em **Geral › Perfis**, escreva o nome do jogo e escolha:

- **Duplicar o atual** — copia tudo que está valendo agora, inclusive as áreas já
  selecionadas. É o caminho normal: você deixou o programa do jeito certo para um jogo e quer
  guardar aquilo com um nome.
- **Começar do zero** — usa os valores de fábrica. Serve para um jogo que não tem nada a ver
  com o anterior.

O perfil criado já fica ativo. A partir daí é só ajustar o programa normalmente, nas abas de
sempre: **tudo que você mexer é gravado nele sozinho**, sem botão de salvar.

## Trocando de perfil

Clique no seletor do cabeçalho e escolha outro (ou clique na linha dele em *Geral › Perfis*).
A troca vale na hora — áreas, idiomas, aparência e glossário mudam juntos, sem reiniciar. Uma
notificação na tela confirma qual perfil entrou, útil quando você troca com o jogo em
primeiro plano.

Se o **Modo Legenda** ou o **Tempo Real** estiverem ligados, eles continuam ligados e passam
a capturar a área do perfil novo.

## Renomear e apagar

Em **Geral › Perfis**, cada perfil (menos o Padrão) tem **Renomear** e **Apagar**. Apagar pede
confirmação; se você apagar o perfil que está em uso, o Padrão assume na hora.

## O que NÃO muda ao trocar de perfil

Nem tudo é "por jogo" — o que é seu continua valendo em todos os perfis:

| Acompanha o perfil | Vale para todos os perfis |
|---|---|
| Idioma do texto e da tradução | Chaves de API |
| Área de captura e área da legenda | Atalhos de teclado |
| Aparência da tradução (fonte, cor, fundo, duração) | Monitor e barra flutuante |
| Pré-processamento de imagem | Motor de OCR e pasta do OneOCR (aba *Geral › OCR*) |
| | Sensibilidade do agrupamento (em *Overlay › Captura*) |
| Motor de tradução e modelo | Inpaint |
| System Prompt e Informações do Jogo | Servidor web |
| Modo Legenda e Modo Tempo Real | Idioma da interface e as opções de diagnóstico |

A chave de API é o caso que mais importa: você digita **uma vez** e ela vale em todos os
perfis, inclusive nos que criar depois.

---
