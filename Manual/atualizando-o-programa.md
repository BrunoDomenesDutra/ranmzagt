# 15. Atualizando o programa

Ao abrir o programa, se existir uma versão mais nova publicada, aparece um aviso com a versão
que você tem e a que saiu. O botão **Baixar** abre a página da versão nova no seu navegador —
é lá que estão as novidades daquela versão e o arquivo `.zip`.

**O programa não baixa e não instala nada sozinho.** Ele só avisa; o download e a troca dos
arquivos são feitos por você, do mesmo jeito que na primeira instalação. Isso é de propósito:
um programa que substitui o próprio executável é exatamente o comportamento que o Windows
Defender bloqueia, e não vale o risco de o programa inteiro parar de abrir.

**Como atualizar**, depois de baixar o `.zip`: feche o Ranmza-GT, extraia o conteúdo por cima
da pasta atual e confirme a substituição dos arquivos. Suas configurações (`config.json`),
as chaves de API, as fontes que você colocou em `fonts/` e os arquivos de `models/` (OneOCR e
MI-GAN) **não estão no `.zip`** e continuam onde estão.

Para desligar o aviso, marque **Não avisar sobre novas versões** no próprio aviso, ou desligue
em **Geral › Config → Atualizações**. É por esse toggle que ele volta a aparecer.

Mesmo com o aviso desligado, o botão **Verificar agora**, no mesmo card, consulta na hora se
saiu versão nova — é o jeito de olhar de vez em quando sem ficar sendo avisado toda vez.

> O programa consulta a página de versões no máximo uma vez a cada 6 horas, mesmo que você
> abra e feche várias vezes no dia — o aviso continua aparecendo em toda abertura, porque ele
> usa a última resposta guardada. O botão *Verificar agora* ignora esse intervalo. Se você
> estiver sem internet, nada acontece: nenhum erro aparece e o programa abre normalmente.
