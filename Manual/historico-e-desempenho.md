# 11. Histórico e desempenho

- **Aba Historico**: mostra as traduções feitas durante a sessão atual (texto original,
  tradução, horário e serviço usado), da mais recente para a mais antiga. Clique numa entrada
  para copiar a tradução; há também um botão para limpar tudo.
- **Debug › Monitor**: liga um registro das últimas 10 traduções com o tempo que cada etapa
  levou (captura, pré-processamento, reconhecimento, tradução, total) — útil para perceber se
  alguma configuração está deixando o programa lento (por exemplo, pré-processamento muito
  pesado). A coluna **Cache** mostra quantos blocos foram resolvidos sem chamar a API, e a
  **API**, quantas chamadas foram feitas de fato.
- **Uso do DeepL** (**Traducao › Tradutores**, com o DeepL selecionado): mostra quantos
  **caracteres** o DeepL traduziu nesta sessão e a **cota da conta** (caracteres usados/limite do
  período de cobrança) — clique em "Atualizar" para consultar. É exclusivo do DeepL; os motores
  de IA não expõem o gasto pela chave.

---
