# 10. Web

A aba **Overlay › Web** liga um servidor na sua rede local que mostra as traduções numa página de
navegador. Serve para acompanhar as traduções no celular ou num segundo monitor e para levar a
tradução ao OBS quando ela não entra na gravação.

> **Você não precisa do servidor Web para a tradução aparecer no OBS.** Com o OBS capturando o
> monitor (*Captura de tela*), a tradução entra na gravação como qualquer janela. Ela fica de fora
> em três casos:
> - o OBS usa *Captura de jogo*, que grava só a imagem do jogo, sem as janelas por cima;
> - o Modo Legenda está com *Colar no texto detectado* ligado, que esconde a legenda das
>   gravações para o OCR não ler a própria tradução;
> - *Esconder a tradução de gravações e transmissões* está ligado em Overlay › Captura.
>
> Nesses casos, use os endereços do OBS desta aba.

<p align="center"><img src="media/overlay-web.png" alt="Aba Overlay › Web" width="820"></p>

## Servidor Web

- **Servidor ativo** — liga o servidor. Com ele desligado, nenhum endereço abaixo funciona. Na
  primeira vez, o Firewall do Windows pergunta se libera o programa na rede.
- **Mostrar tradução na tela** — vale para a captura de tela. Desligado, a tradução aparece só
  nas páginas, e não por cima do jogo. Só dá para mudar com o servidor ligado.
- **Porta** — padrão 7474. Ao lado aparece quantas páginas estão conectadas.

## Endereços

Cada endereço tem o botão **Copiar**.

- **Captura** (`/captura`) — lista das traduções da captura de tela, com histórico e botão
  Limpar. Abra no navegador de qualquer aparelho na mesma rede, como o celular.
- **Captura — OBS** (`/captura/obs`) — a mesma lista, com fundo transparente e sem o botão, para
  usar no OBS.
- **Legenda — OBS** (`/legenda/obs`) — a legenda do Modo Legenda com *Colar no texto detectado*
  ligado, no mesmo lugar da legenda original.

As duas páginas de captura recebem só as traduções da captura de tela (`Numpad8`, `Numpad9` e o
Vision). A legenda vai só para o endereço **Legenda — OBS**.

## Colocando no OBS

**Tradução da captura de tela:**

1. Ligue o **Servidor ativo** e copie o endereço **Captura — OBS**.
2. No OBS, adicione uma fonte **"Navegador" (Browser Source)** com esse endereço.
3. Se a tradução também aparecer na captura do monitor e ficar duplicada, desligue **Mostrar
   tradução na tela**.

**Legenda colada no texto:**

1. Ligue o **Servidor ativo** e copie o endereço **Legenda — OBS**.
2. No OBS, adicione uma fonte **"Navegador" (Browser Source)** com esse endereço e a resolução do
   seu monitor. Deixe a fonte acima do jogo, do mesmo tamanho e na mesma posição da imagem dele.
3. Em **Overlay › Legenda**, deixe *Colar no texto detectado* ligado.

A legenda aparece no OBS no mesmo lugar da original, com a fonte, as cores e o fundo da aba
Legenda, e some junto com a da tela. Se a imagem do jogo estiver cortada ou em janela na cena, a
legenda sai do lugar. No OBS, o *Efeito de vidro* vira o fundo escuro, porque a página não
recebe a imagem do jogo.

## Aparência

Vale para as páginas **Captura** e **Captura — OBS**. A página da legenda usa a aparência da aba
Legenda. As páginas abertas mudam na hora.

<p align="center"><img src="media/overlay-web-aparencia.png" alt="Aba Overlay › Web — aparência da página" width="820"></p>

- **Tema** — Dark, Light ou Dracula.
- **Tamanho da fonte** — 12 a 48 px.
- **Negrito** — tradução em negrito.
- **Texto detectado** — mostra o texto original lido pelo OCR abaixo da tradução.
- **Horário e serviço** — mostra a hora da tradução e o serviço que traduziu.
- **Cores personalizadas** — troca as cores do tema pelas suas: texto traduzido, texto original,
  horário, serviço, fundo e borda do card.

## Histórico

- **Entradas mantidas no buffer** — quantas traduções o servidor guarda para quem abre a página
  depois, de 10 a 200. O botão Limpar da página e o da aba Histórico apagam a lista.

## Barra, alertas e prévia na gravação

A barra flutuante, os alertas e a prévia das áreas também aparecem na gravação. Para tirar a
barra e os alertas, ligue *Esconder a barra de gravações e transmissões* (Geral › Atalhos) e
*Esconder os alertas de gravações e transmissões* (Geral › Config). A prévia não tem essa opção:
desligue com o `Numpad2` antes de gravar.

---
