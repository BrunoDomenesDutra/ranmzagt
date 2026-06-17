## 8. Modo Legenda — tradução automática contínua

Para cenas com diálogo contínuo (cutscenes, modo automático de visual novels, vídeos com legenda), o Modo Legenda traduz **sozinho, repetidamente**, sem você precisar apertar nada.

### Como configurar

- Na aba **Legenda**, ajuste as opções de captura (intervalo, quantas linhas mostrar, etc.) — os padrões já funcionam bem para a maioria dos casos.
- Aperte **Selecionar área da legenda** (padrão Numpad1) e desenhe um retângulo sobre onde a legenda/diálogo aparece no jogo.
- Aperte **Ligar/desligar Modo Legenda** (padrão Numpad0) para ativar.

A partir daí, o programa fica de olho naquela área, traduzindo automaticamente sempre que um texto novo aparecer e ficar "parado" por um instante (isso evita traduzir letras aparecendo uma por uma em efeitos de "máquina de escrever").

As traduções aparecem **acima** da área selecionada, em ordem (mais recente embaixo), e somem sozinhas se nenhum texto novo aparecer por alguns segundos.

### Deixando a IA "lembrar" das falas anteriores

Se você está usando OpenAI, Claude ou Gemini, a aba **IA** tem um controle **"Falas anteriores"** (0 a 20, padrão 5). Com ele ligado, a IA recebe as últimas falas já traduzidas como referência antes de traduzir a próxima — isso ajuda a manter os mesmos nomes, termos e tom ao longo de uma conversa. Se notar que a IA está mudando o nome de um personagem ou o tom da tradução de uma fala para outra, aumente esse valor; se preferir que cada fala seja traduzida sem depender das anteriores, deixe em 0.

### Aparência separada

A aba Legenda tem suas próprias opções de fonte, fundo e contorno — independentes da tradução manual — então você pode deixar a legenda contínua menor/mais discreta e a tradução manual (Numpad9) maior, por exemplo.

### Desligando

Aperte **Numpad0** novamente (ou o botão correspondente, se você tiver criado um na barra flutuante). A legenda na tela é limpa imediatamente.

### Desligamento Automático

Esqueceu de desligar o modo legenda? Não tem problema, por padrão o modo é desligado após 1 minuto de inatividade, sendo que este tempo pode ser estendido até 10 minutos, só configurar de acordo com seu gosto.
